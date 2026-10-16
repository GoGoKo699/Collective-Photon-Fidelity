"""Reusable calculations for the positive Dicke photon wavefunction.

Time is dimensionless, tau = Gamma * physical_time.  For n photons and
a >= 1, put M = n + a - 1.  The normalized symmetric photon density is

    P(tau) = Gamma_E(M+1) / Gamma_E(a)
             * exp[-a sum(tau_i) - sum_{i<j} abs(tau_i-tau_j)].

Here Gamma_E denotes Euler's gamma function.  Native full inversion has
a=1.  A symmetric n-excitation state of M physical emitters has a=M-n+1.
For n initially excited emitters conditioned on no independent local decay,
a=1+gamma/Gamma; M is then an effective parameter, not an emitter count.

The wavefunction is sqrt(P), and fidelity is the SQUARED overlap with a
normalized single-mode n-photon Fock state.  We evaluate a specified positive
trial mode, not a global mode optimization.  In scaled time x=M*tau it is

    phi(x) = sqrt(a*M) exp(-x/2) / [a+(n-1)exp(-x)],
    f(tau) = sqrt(M) phi(M*tau).

The positive ordered-amplitude cascade costs O(n) per right-hand-side
evaluation.  It can be strongly nonnormal: successful integration with a
loose componentwise absolute tolerance is insufficient.  The check script
compares small absolute tolerances and finite cutoffs.  All numerical results
are floating-point estimates, not interval certificates.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from numbers import Integral
from typing import Callable

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import gammaln


@dataclass(frozen=True)
class DickeFamily:
    """n is an integer photon number; real a >= 1 selects the density above."""

    n: int
    a: float = 1.0

    def __post_init__(self) -> None:
        if isinstance(self.n, bool) or not isinstance(self.n, Integral) or self.n < 1:
            raise ValueError("n must be a positive integer")
        if not math.isfinite(self.a) or self.a < 1:
            raise ValueError("a must be finite and at least one")

    @property
    def M(self) -> float:
        return self.n + self.a - 1

    def trial_phi(self, x: float) -> float:
        """Exactly normalized infinite-support mode in x=M*tau, for x>=0."""
        return math.sqrt(self.a * self.M) * math.exp(-x / 2) / (
            self.a + (self.n - 1) * math.exp(-x)
        )

    def mode_tail(self, xmax: float) -> float:
        """Exact integral of phi(x)^2 over x>xmax."""
        z = math.exp(-xmax)
        return self.M * z / (self.a + (self.n - 1) * z)

    def kl_divergence(self) -> float:
        """D(product |f|^2 || P); exp(-D) bounds the infinite trial fidelity.

        An algebraic rearrangement avoids subtracting large gamma functions.
        For small (n-1)/a, a series starts after the exactly cancelling linear
        term, avoiding loss of the small positive divergence.
        """
        if self.n == 1:
            return 0.0
        b = self.n - 1
        ratio = b / self.a
        if ratio < 0.02:
            return math.fsum(
                (-1) ** (k + 1) * ratio**k / k
                * (self.n / (k + 1) - math.fsum((j / b) ** k for j in range(self.n)))
                for k in range(2, 18)
            )
        integral = (1 + 1 / ratio) * math.log1p(ratio) - 1
        return self.n * integral - math.fsum(
            math.log1p(j / self.a) for j in range(self.n)
        )

    def quantile_kl(self) -> tuple[float, float]:
        """Independent 1D quadrature of D, returning value and error estimate.

        The exact quantile is t(v)=[log(1+(n-1)v/a)-log(1-v)]/M.
        Also p(t(v))=(a+(n-1)v)(1-v).  Integrating the pair interaction
        against iid quantiles gives (n-1)(2v-1)t(v) per photon.
        """
        b = self.n - 1

        def integrand(v: float) -> float:
            t = (math.log1p(b * v / self.a) - math.log1p(-v)) / self.M
            logp = math.log(self.a + b * v) + math.log1p(-v)
            return logp + (self.a + b * (2 * v - 1)) * t

        value, error = quad(integrand, 0, 1, epsabs=2e-12, epsrel=2e-12, limit=200)
        normalizer = math.fsum(math.log(self.a + j) for j in range(self.n))
        return self.n * value - normalizer, self.n * error

    def finite_count_upper(self) -> float:
        """Finite upper bound on the optimized fidelity, not a fitted asymptote.

        At the target mode's median, target photon counts are Binomial(n,1/2).
        The first waiting-time density gives P(count=m) <= n*a/r_m, where
        r_m=(n-m)(a+m).  The classical count affinity bounds the quantum
        fidelity.  Endpoint caps are one; the result can be uninformative.
        """
        m = np.arange(self.n + 1, dtype=float)
        log_binomial = (
            gammaln(self.n + 1) - gammaln(m + 1)
            - gammaln(self.n - m + 1) - self.n * math.log(2)
        )
        caps = np.ones(self.n + 1)
        middle = m[1:-1]
        caps[1:-1] = np.minimum(
            1, self.n * self.a / ((self.n - middle) * (self.a + middle))
        )
        return min(1.0, float(np.sum(np.sqrt(caps) * np.exp(log_binomial / 2)) ** 2))


def ordered_amplitude(
    family: DickeFamily,
    phi: Callable[[float], float],
    xmax: float,
    *,
    rtol: float = 2e-12,
    atol: float = 1e-80,
) -> tuple[float, int]:
    """Return the unnormalized cutoff amplitude and number of RHS evaluations.

    phi must be real and nonnegative with integral_0^xmax phi^2 <= 1.
    Starting at c_0(0)=1, the bosonic ordered integral obeys

      c_j' = -(n-j)(a+j)/(2M) c_j
             + sqrt[j(n-j+1)(a+j-1)/M] phi c_(j-1).

    Thus c_n(xmax) is the overlap for phi supported on [0,xmax], before
    renormalizing that mode.  The j=0 equation contains just its decay term.
    """
    if not math.isfinite(xmax) or xmax <= 0:
        raise ValueError("xmax must be finite and positive")
    n, a, M = family.n, family.a, family.M
    j = np.arange(n + 1, dtype=float)
    decay = (n - j) * (a + j) / (2 * M)
    coupling = np.sqrt(j * (n - j + 1) * (a + j - 1) / M)

    def rhs(x: float, state: np.ndarray) -> np.ndarray:
        out = -decay * state
        out[1:] += coupling[1:] * phi(x) * state[:-1]
        return out

    initial = np.zeros(n + 1)
    initial[0] = 1
    solution = solve_ivp(
        rhs, (0, xmax), initial, method="DOP853", rtol=rtol, atol=atol
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    amplitude = float(solution.y[n, -1])
    if not math.isfinite(amplitude) or not -1e-10 <= amplitude <= 1 + 1e-8:
        raise RuntimeError(f"Unphysical amplitude {amplitude}; integration failed")
    return amplitude, int(solution.nfev)


@dataclass(frozen=True)
class TrialEstimate:
    """Estimate for an exactly normalized mode with a stated finite cutoff."""

    fidelity: float
    cutoff: float
    removed_mode_norm: float
    rhs_evaluations: int


def trial_fidelity(
    family: DickeFamily, *, tail: float = 35, rtol: float = 2e-12, atol: float = 1e-80
) -> TrialEstimate:
    """Evaluate and exactly normalize the trial mode truncated at x=X.

    X=log(M/a)+tail, so the removed one-photon norm is approximately
    exp(-tail).  The analytic KL bound concerns the infinite mode.  For any
    source state the two target projection probabilities differ by at most
    sqrt[1-(1-q)^n], with q the removed norm.  This is a conservative analytic
    cutoff budget, separate from the measured two-cutoff numerical difference.
    """
    xmax = math.log(family.M / family.a) + tail
    raw, evaluations = ordered_amplitude(
        family, family.trial_phi, xmax, rtol=rtol, atol=atol
    )
    removed = family.mode_tail(xmax)
    fidelity = raw**2 * math.exp(-family.n * math.log1p(-removed))
    return TrialEstimate(fidelity, xmax, removed, evaluations)


def no_local_loss_probability(n: int, epsilon: float) -> float:
    """Probability of all n desired photons from n inverted emitters.

    Desired jump sqrt(Gamma) J_- and independent local jumps
    sqrt(gamma) sigma_i^- have epsilon=gamma/Gamma.  This is the probability
    product_{j=1}^n j/(j+epsilon), not a conditional fidelity or a herald.
    """
    if not math.isfinite(epsilon) or epsilon < 0:
        raise ValueError("epsilon must be finite and nonnegative")
    DickeFamily(n, 1 + epsilon)
    return float(math.exp(gammaln(n + 1) + gammaln(1 + epsilon) - gammaln(n + 1 + epsilon)))


def hypergeometric_weight(N: int, m: int, k: int, j: int) -> Fraction:
    """Exact rational survivor-count weight HG(N,m,k,j).

    Conditional on k photons surviving uniform, mode-independent attenuation,
    select k among N photons, of which m preceded a time cut.  Invalid j has
    weight zero.  Exact rational arithmetic supports the thinning identities.
    """
    if not 0 <= m <= N or not 0 <= k <= N:
        raise ValueError("Require 0 <= m,k <= N")
    if j < 0 or j > m or k - j < 0 or k - j > N - m:
        return Fraction(0)
    return Fraction(math.comb(m, j) * math.comb(N - m, k - j), math.comb(N, k))
