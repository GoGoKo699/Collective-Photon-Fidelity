#!/usr/bin/env python3
"""Run compact reproducible checks of the Dicke fidelity calculations.

Run from the repository root: python3 verification/check_fidelity.py
Use --json for machine-readable results; --native-n selects native sizes
within 1..100.  Partial-excitation, noninteger local-loss, exact-mode and
combinatorial checks always run.  The default needs only NumPy and SciPy.

The reported pulse values are floating-point estimates for a specified,
normalized, truncated trial mode, never optimized fidelities.  Numerical
agreement supports implementation consistency, not asymptotic theorems or
rigorous interval bounds.  Analytic finite bounds and the N=1,2 benchmarks
provide separate comparisons.  Any violated check exits nonzero, including
when Python is run with optimization enabled.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
import sys

import numpy as np
from scipy.integrate import quad
from scipy.special import j1, jn_zeros

from fidelity import (
    DickeFamily, hypergeometric_weight, no_local_loss_probability,
    ordered_amplitude, trial_fidelity,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def check_trial(family: DickeFamily) -> dict:
    """Compare tolerances, cutoffs, normalization, KL quadrature and bounds."""
    loose = trial_fidelity(family, tail=30, rtol=2e-11, atol=1e-50)
    tight = trial_fidelity(family, tail=30)
    final = trial_fidelity(family)
    norm, _ = quad(lambda x: family.trial_phi(x)**2,
                   0, np.inf, epsabs=2e-12, epsrel=2e-12)
    kl = family.kl_divergence()
    integrated_kl, quadrature_error = family.quantile_kl()
    lower, upper = math.exp(-kl), family.finite_count_upper()
    tolerance_difference = abs(loose.fidelity - tight.fidelity)
    cutoff_difference = abs(tight.fidelity - final.fidelity)
    cutoff_budget = math.sqrt(-math.expm1(family.n * math.log1p(-final.removed_mode_norm)))
    label = f"n={family.n}, a={family.a:g}"
    numerical_budget = 2e-8
    require(abs(norm - 1) < 1e-10, f"Mode normalization failed: {label}")
    require(abs(kl - integrated_kl) < 1e-9, f"Independent KL quadrature failed: {label}")
    require(kl >= -1e-12, f"Negative KL divergence: {label}")
    require(max(tolerance_difference, cutoff_difference) < numerical_budget,
            f"Tolerance/cutoff convergence failed: {label}")
    require(lower <= final.fidelity + cutoff_budget + numerical_budget,
            f"KL lower-bound consistency failed: {label}")
    require(0 <= final.fidelity <= upper + numerical_budget,
            f"Finite count upper-bound consistency failed: {label}")
    if family.n == 1:
        require(abs(final.fidelity - 1) < 1e-9, f"Exact one-photon case failed: {label}")
    return {
        "n": family.n, "a": family.a, "M_effective": family.M,
        "trial_fidelity_estimate": final.fidelity,
        "analytic_infinite_trial_KL_lower": lower,
        "analytic_optimized_fidelity_count_upper": upper,
        "KL_divergence": kl,
        "independent_KL_quadrature_difference": abs(kl - integrated_kl),
        "KL_quadrature_error_estimate": quadrature_error,
        "mode_normalization_residual": abs(norm - 1),
        "two_tolerance_difference": tolerance_difference,
        "two_cutoff_difference": cutoff_difference,
        "final_scaled_time_cutoff": final.cutoff,
        "removed_one_photon_norm": final.removed_mode_norm,
        "analytic_cutoff_projection_probability_budget": cutoff_budget,
        "rhs_evaluations_total": sum(x.rhs_evaluations for x in (loose, tight, final)),
    }


def check_exact_modes() -> dict:
    """Check the cascade against independent one-, two- and exponential modes."""
    zero = float(jn_zeros(0, 1)[0])
    denominator = math.sqrt(2) * float(j1(zero))

    def bessel_phi(x: float) -> float:
        z = math.exp(-x / 4)
        return z * float(j1(zero * z)) / denominator

    norm, _ = quad(lambda x: bessel_phi(x)**2, 0, np.inf, epsabs=2e-12, epsrel=2e-12)
    value, _ = ordered_amplitude(DickeFamily(2), bessel_phi, 38)
    exact = 32 / zero**4
    bessel_fidelity = value**2
    residual = abs(bessel_fidelity - exact)
    require(abs(norm - 1) < 1e-10, "The exact two-photon Bessel mode is not normalized")
    require(residual < 1e-9, "The exact two-photon Bessel benchmark failed")

    # General real-a factors can be tested without a variational pulse:
    # exponential targets permit a product of elementary dwell integrals.
    family = DickeFamily(5, 1.25)
    kappa = family.M / 2
    phi = lambda x: math.sqrt(kappa / family.M) * math.exp(-kappa * x / (2 * family.M))
    value, _ = ordered_amplitude(family, phi, 45 * family.M / kappa)
    exact_exponential = math.prod(
        4 * (family.a + m) * kappa / (family.a + m + kappa)**2
        for m in range(family.n)
    )
    exponential_residual = abs(value**2 - exact_exponential)
    require(exponential_residual < 1e-9, "The noninteger-a exponential benchmark failed")

    # n=1 is an exponential for every a, not just a=1.
    one = check_trial(DickeFamily(1, 9.5))
    return {
        "exact_global_F_2_star": exact,
        "Bessel_mode_recursion_fidelity": bessel_fidelity,
        "Bessel_mode_absolute_residual": residual,
        "Bessel_mode_normalization_residual": abs(norm - 1),
        "noninteger_a_exponential_exact_fidelity": exact_exponential,
        "noninteger_a_exponential_recursion_residual": exponential_residual,
        "noninteger_a_one_photon_fidelity": one["trial_fidelity_estimate"],
    }


def check_exact_loss_and_thinning() -> dict:
    """Use exact rational combinatorics, independent of the wavefunction ODE."""
    products = []
    for n, epsilon in [(2, Fraction(1)), (5, Fraction(1, 4)), (10, Fraction(1)),
                       (20, Fraction(2)), (50, Fraction(1, 2))]:
        product = math.prod(Fraction(j) / (j + epsilon) for j in range(1, n + 1))
        gamma_value = no_local_loss_probability(n, float(epsilon))
        relative_residual = abs(gamma_value / float(product) - 1)
        require(relative_residual < 1e-11, f"Gamma/product loss identity failed: n={n}")
        products.append({"n": n, "epsilon": str(epsilon), "probability": gamma_value,
                         "relative_residual": relative_residual})

    # Include endpoints in the unweighted identity, and nontrivial interior
    # values in the weighted identity needed for uniform survivor bounds.
    identities = []
    for N, k, j in [(5, 2, 1), (10, 7, 2), (20, 10, 5), (100, 23, 9), (100, 99, 50)]:
        for endpoint in {0, j, k}:
            total = sum(hypergeometric_weight(N, m, k, endpoint) for m in range(N + 1))
            require(total == Fraction(N + 1, k + 1),
                    f"Unweighted Vandermonde identity failed: {N,k,endpoint}")
        weighted = sum(
            hypergeometric_weight(N, m, k, j) / (m * (N - m)) for m in range(1, N)
        )
        require(weighted == Fraction(k, N * j * (k - j)),
                f"Weighted Vandermonde identity failed: {N,k,j}")
        for m in {0, N // 2, N}:
            total = sum(hypergeometric_weight(N, m, k, v) for v in range(k + 1))
            require(total == 1, f"Hypergeometric normalization failed: {N,m,k}")
        identities.append({"N": N, "k": k, "j": j, "status": "exact rational equality"})
    return {"local_loss_gamma_products": products, "thinning_identities": identities}


def check_analytic_bounds() -> dict:
    """Exercise small-divergence stability and a nontrivial finite count bound.

    These evaluations use only closed formulas, not a large-photon ODE.
    Curvature bounds independently constrain the small-ratio KL series.
    The elementary count bound is clipped at one for native n<=100; at
    n=1000 it is nontrivial and must still exceed the constructive lower bound.
    """
    small_divergences = []
    for a in (1000.0, 1e8):
        family = DickeFamily(10, a)
        value = family.kl_divergence()
        lower = family.n * (family.n - 1) / (12 * family.M**2)
        upper = family.n * (family.n - 1) / (12 * family.a**2)
        require(lower * (1 - 1e-12) <= value <= upper * (1 + 1e-12),
                f"Small-divergence curvature bounds failed: a={a}")
        small_divergences.append({"n": family.n, "a": a, "KL_divergence": value,
                                  "curvature_lower": lower, "curvature_upper": upper})
    family = DickeFamily(1000)
    lower = math.exp(-family.kl_divergence())
    upper = family.finite_count_upper()
    require(0 < lower <= upper < 1, "Nontrivial finite lower/upper bounds are inconsistent")
    return {"small_divergence_cases": small_divergences,
            "native_n1000_closed_bounds_only": {"KL_lower": lower, "count_upper": upper}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print complete machine-readable results")
    parser.add_argument("--native-n", nargs="+", type=int,
                        help="Native photon numbers to check, each from 1 through 100")
    args = parser.parse_args()
    sizes = sorted(set(args.native_n if args.native_n is not None else [1, 2, 5, 10, 20, 50, 100]))
    if any(n < 1 or n > 100 for n in sizes):
        parser.error("The CLI's integration settings are scoped to 1 <= n <= 100")
    try:
        exact = check_exact_modes()
        native = [check_trial(DickeFamily(n)) for n in sizes]
        partial = [check_trial(DickeFamily(n, M - n + 1))
                   for M, n in [(10, 2), (20, 10), (100, 10), (100, 90)]]
        local = check_trial(DickeFamily(5, 1.25))
        local["epsilon"] = 0.25
        local["all_photon_probability"] = no_local_loss_probability(5, 0.25)
        local["unconditional_trial_yield"] = local["all_photon_probability"] * local["trial_fidelity_estimate"]
        identities = check_exact_loss_and_thinning()
        analytic_bounds = check_analytic_bounds()
    except (RuntimeError, ValueError, OverflowError) as error:
        print(f"CHECK FAILED: {error}", file=sys.stderr)
        return 1
    record = {
        "status": "All checks passed; floating-point trial estimates, not optimized fidelities or interval certificates",
        "scope": "Native and symmetric partial Dicke emission, no-local-loss sector, uniform attenuation identities",
        "exact_mode_benchmarks": exact,
        "native_trial_results": native,
        "partial_trial_results": partial,
        "conditional_local_loss_trial_result": local,
        "analytic_bound_checks": analytic_bounds,
        **identities,
    }
    if args.json:
        print(json.dumps(record, indent=2, allow_nan=False))
        return 0
    print("Specified trial-pulse squared overlaps; these are not global mode optimizations.")
    print("Floating-point consistency checks, not rigorous numerical certificates.")
    print(f"Exact optimum F_2* = {exact['exact_global_F_2_star']:.12f}; Bessel recursion residual = {exact['Bessel_mode_absolute_residual']:.2g}")
    print("\nNative full inversion")
    print("  N       trial F       KL lower    finite upper    tolerance diff   cutoff diff")
    for row in native:
        print(f"{row['n']:3d}  {row['trial_fidelity_estimate']:.10f}  {row['analytic_infinite_trial_KL_lower']:.10f}"
              f"  {row['analytic_optimized_fidelity_count_upper']:.10f}"
              f"  {row['two_tolerance_difference']:14.2g}  {row['two_cutoff_difference']:12.2g}")
    print("\nSymmetric partial excitation")
    print("  M    n       trial F       KL lower")
    for row in partial:
        print(f"{row['M_effective']:3.0f}  {row['n']:3d}  {row['trial_fidelity_estimate']:.10f}"
              f"  {row['analytic_infinite_trial_KL_lower']:.10f}")
    print("\nIndependent local loss: N=5, epsilon=0.25")
    print(f"All-photon probability = {local['all_photon_probability']:.10f}; conditional trial F = {local['trial_fidelity_estimate']:.10f}")
    print(f"Unconditional trial yield = {local['unconditional_trial_yield']:.10f}")
    all_rows = native + partial + [local]
    print(f"\nMaximum trial normalization residual: {max(r['mode_normalization_residual'] for r in all_rows):.2g}")
    print(f"Maximum independent KL quadrature difference: {max(r['independent_KL_quadrature_difference'] for r in all_rows):.2g}")
    print("Exact rational thinning identities and local-loss gamma products passed.")
    print("Small-divergence KL and nontrivial finite count-bound checks passed (closed formulas only).")
    print("All checks passed. Use --json for all residuals and explicit cutoff budgets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
