# Numerical and exact consistency checks

The checks evaluate squared overlaps for explicitly specified, normalized trial pulses and compare independent formulas for finite ingredients of the analysis. The overlap calculations use floating-point quadrature and ordinary differential equations. The hypergeometric identities use exact rational arithmetic. The [scientific numerical account](../science/numerical_checks.md) gives the cascade equations, pulse conventions, and representative values.

## Run from a fresh checkout

From the repository root, create and activate a Python virtual environment and install the dependencies in [requirements.txt](../requirements.txt):

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make check
```

The check target runs [check_fidelity.py](check_fidelity.py). The same checks can be invoked directly, and their complete output can be requested as JSON:

```bash
python verification/check_fidelity.py
python verification/check_fidelity.py --json
```

A successful run exits with status zero and reports that all checks passed. A failed numerical or exact comparison exits nonzero. The checks use explicit runtime conditions and remain active when Python optimization is enabled. The JSON writer rejects nonfinite values.

The default native sizes are $`N=1,2,5,10,20,50,100`$. To select native sizes within the documented integration range, use, for example:

```bash
python verification/check_fidelity.py --native-n 10 50 100 --json
```

The CLI accepts native photon numbers from 1 through 100. Selecting these sizes changes only the native rows; the partial-excitation, conditional-loss, exact-mode, and combinatorial checks still run. The separate native $`N=1000`$ check evaluates closed bounds and does not integrate a large cascade.

## What is checked

The implementation is in [fidelity.py](fidelity.py), and the independent comparisons are in [check_fidelity.py](check_fidelity.py).

| Benchmark | Independent comparison and scope | Scientific account |
|---|---|---|
| Native and symmetric partial excitation | Infinite-mode normalization by quadrature; the closed relative entropy against a one-dimensional quantile integral; trial overlaps under two ODE tolerance settings and two cutoffs; comparison with analytic lower and finite count upper bounds | [Native emission](../science/native_emission.md), [partial excitation](../science/partial_excitation.md#eq-d), and [cascade recursion](../science/numerical_checks.md#eq-recursion) |
| Exact one-photon modes | Unit fidelity for the native case, noninteger $`a=9.5`$, and the largest finite floating-point $`a`$; the last case checks that finite scaled coefficients do not overflow | [Exact Fock criterion](../science/exact_fock_control.md#eq-exactcriterion) |
| Exact two-photon mode | Independent Bessel-mode normalization and the recursion overlap against the analytic optimum $`32/j_{0,1}^{4}`$, where $`j_{0,1}`$ is the first positive zero of $`J_0`$ | [Two-photon optimum](../science/native_emission.md#sec-two) |
| Noninteger-parameter exponential mode | At $`n=5,a=1.25`$, the cascade overlap is compared with a product of elementary exponential waiting-time integrals | [Stationary exponential overlap](../science/exact_fock_control.md#eq-stationaryoverlap) |
| Independent local loss | The beta-function evaluation of the all-desired probability is compared with exact `Fraction` branching products, including zero loss and $`\epsilon=10^{16}`$. At the largest finite loss ratio, one photon has a representable subnormal probability while the two-photon probability rounds to zero | [All-desired probability](../science/local_loss.md#eq-localprob) |
| Uniform attenuation | Exact `Fraction` equalities for the unweighted and weighted hypergeometric sums, including endpoint cases, plus normalization of the survivor-count distribution | [Hypergeometric thinning](../science/attenuation.md#eq-hypergeom) and [thinned count bound](../science/attenuation.md#eq-thinningbound) |
| Small relative entropy and finite count bounds | The small-ratio KL series is constrained by independent curvature bounds at $`n=10,a=10^3,10^8`$; native $`n=1000`$ has a nontrivial consistent lower/upper pair; the largest finite $`a`$ gives the exact trivial upper bound one without invalid or overflowing intermediates | [Dilute-regime bounds](../science/partial_excitation.md#eq-dilutebound) and [temporal-count bound](../science/native_emission.md#sec-upper) |

The default partial-source pairs $`(M,n)`$ are $`(10,2),(20,10),(100,10),(100,90)`$. The local-loss example has $`n=5,\epsilon=0.25`$, hence effective $`a=1.25`$ and $`M=5.25`$. This effective parameter is not a physical emitter count. Its output records the sector probability, conditional trial fidelity, and their product as the unconditional trial yield.

## Numerical and exact pass criteria

| Comparison | Criterion implemented by the runner |
|---|---|
| Infinite-mode normalization | Absolute residual below $`10^{-10}`$ |
| Closed KL expression versus independent quadrature | Absolute difference below $`10^{-9}`$; computed KL at least $`-10^{-12}`$ |
| Two-tolerance and two-cutoff differences | Each below $`2\times10^{-8}`$ |
| Lower-bound consistency | Infinite-trial KL lower bound no larger than the final truncated-mode estimate plus its analytic cutoff budget and $`2\times10^{-8}`$ |
| Upper-bound consistency | Nonnegative final estimate, at most the finite count upper bound plus $`2\times10^{-8}`$ |
| Exact one-photon, Bessel, and exponential overlaps | Absolute residual below $`10^{-9}`$ |
| Local-loss probability versus rational branching product | Relative residual below $`10^{-11}`$ when the exact value is representable; zero loss gives exactly one; the extreme underflow case gives zero while its exact rational product remains positive |
| Hypergeometric identities and normalization | Exact rational equality, with no floating-point tolerance |
| Small-divergence curvature bounds | Bounds respected with relative slack $`10^{-12}`$ |

These numerical thresholds are implementation consistency criteria, not certified error intervals. The ODE uses `DOP853`: the loose run has `rtol=2e-11, atol=1e-50`, and the tight run has `rtol=2e-12, atol=1e-80`. Both use tail parameter 30 before the tight calculation is repeated with tail parameter 35. Small absolute tolerances matter because the positive cascade can be strongly nonnormal. Quadrature error estimates and observed agreement are recorded separately.

The loss benchmarks construct their reference branching products exactly with `fractions.Fraction`; the comparison to the special-function implementation is nevertheless a floating-point comparison. The hypergeometric identities themselves are evaluated and compared entirely as rational numbers. Raw numerical estimates can differ slightly from physical endpoints through roundoff: for example, an exact one-photon fidelity of one may be reported as `1.0000000000000766` within the stated tolerance.

## Analytic cutoff budget and observed cutoff differences

The final trial pulse is truncated at scaled time $`X=\ln(M/a)+35`$ and then exactly renormalized. Its removed one-photon norm is

```math
q=\frac{M e^{-X}}{a+(n-1)e^{-X}}.
```

The infinite and truncated $`n`$-photon targets have squared overlap $`(1-q)^n`$. Consequently their projection probabilities against any source differ by at most

```math
\sqrt{1-(1-q)^n}.
```

This is an analytic bound on changing the target pulse. It does not include ODE integration error. The JSON field `analytic_cutoff_projection_probability_budget` records this bound, while `two_cutoff_difference` records the observed change between the two computed cutoffs. A small observed difference does not replace the analytic budget, and the budget need not be close to the observed difference. In the reference run the largest budget among the default trial rows is approximately $`2.511\times10^{-7}`$, while the largest observed cutoff difference is approximately $`6.46\times10^{-12}`$.

## Complete reference output

[expected/check_fidelity.json](expected/check_fidelity.json) contains the complete output of one successful default `--json` run in this environment:

| Component | Version or platform |
|---|---|
| Python | 3.12.14 |
| NumPy | 2.3.5 |
| SciPy | 1.17.0 |
| Operating system | Linux, x86-64, glibc 2.39 |

Both `make check` and the JSON run completed successfully. The reference JSON parses strictly and contains no NaN or infinite numerical values. Selected results are:

| Quantity | Reference value |
|---|---:|
| Exact two-photon optimum | 0.956787875131927 |
| Two-photon Bessel recursion residual | $`1.9063\times10^{-13}`$ |
| Native $`N=100`$ trial fidelity | 0.2928377760766531 |
| Largest two-tolerance difference over the default trial rows | $`2.6514\times10^{-12}`$ |
| Largest two-cutoff difference over the default trial rows | $`6.4593\times10^{-12}`$ |
| Largest mode-normalization residual over those rows | $`2.2204\times10^{-16}`$ |
| Largest independent KL quadrature difference over those rows | $`5.6843\times10^{-14}`$ |
| Local-loss example: sector probability | 0.5883789413201178 |
| Local-loss example: conditional trial fidelity | 0.8693225960756151 |
| Local-loss example: unconditional trial yield | 0.5114911087446268 |

The committed JSON is a reference run, not a bitwise cross-platform golden-test gate. Last digits, quadrature estimates, and ODE evaluation counts can vary with the numerical environment. The runner recomputes the independent comparisons and applies its explicit tolerances; it does not compare output bytes with this file. The dependency file declares package lower bounds rather than pinning this one environment.

## Connection to the proofs

The finite calculations support the implemented pulse overlaps, local-loss probability, and combinatorial ingredients. The optimized native exponent, uniform survivor bounds, exact-control converse, and capped-control guarantees follow from their written arguments in the [science route](../science/model.md). Numerical pulse overlaps are attainable values for the specified mode, and do not establish global mode optimality or uniform asymptotic laws. The [related-work account](../references/RELATED_WORK.md) identifies the imported scientific ingredients.
