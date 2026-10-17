# Numerical consistency checks and exact benchmarks

The analytic statements are proved in the scientific pages. The calculations here provide finite-size checks of their formulas and evaluate attainable overlaps for explicitly specified pulses. [Verification instructions](../verification/README.md) give the commands and explain the output.

## Reproducible numerical consistency checks

<a id="sec-numerics"></a>

The executable [verification/check_fidelity.py](../verification/check_fidelity.py) evaluates
specified trial modes, verifies exact identities, and reports
ordinary floating-point convergence checks. Numerical overlaps
are achievable values for those modes, not certificates of
global optimality. The analytic uniform and asymptotic theorems
do not depend on fitting the numerical results.

For these numerical calculations set $`\Gamma=1`$. For the native
source, use scaled time $`x=Nt`$ and write
$`f(t)=\sqrt N\,\phi(x)`$. Set $`c_0(0)=1`$ and $`c_j(0)=0`$
for $`j>0`$. The positive ordered-amplitude recursion is

<a id="eq-recursion"></a>

```math
c_j'=-\frac{(j+1)(N-j)}{2N}c_j+
 j\sqrt{\frac{N-j+1}{N}}\,\phi(x)c_{j-1},
 \qquad j=0,\ldots,N,
```

with the second term absent at $`j=0`$. Then
$`c_N(\infty)`$ is the exact trial amplitude. Thus an ordered
$`N`$-dimensional integral reduces to $`N+1`$ ordinary differential
equations. The same construction with the general cascade rates
evaluates the partial-source and local-loss conditional kernels.
The reported values use the trial mode truncated at
$`x=X=\ln(M/a)+35`$ and then exactly renormalized. If $`q`$ is
the removed one-photon norm, then

```math
q=\frac{M e^{-X}}{a+(n-1)e^{-X}}.
```

The infinite and truncated $`n`$-photon target states have squared
overlap $`(1-q)^n`$. Their projection probabilities against any
source therefore differ by at most
$`\sqrt{1-(1-q)^n}`$, their pure-state trace distance. The code
reports this conservative analytic cutoff budget separately from
the measured change between two numerical cutoffs.

For the [explicit fully inverted pulse](native_emission.md#eq-pulse),
representative values are

| $`N`$ | Trial fidelity | $`\sqrt N`$ times trial fidelity | Infinite-pulse lower bound |
| ---: | ---: | ---: | ---: |
| 1 | 1.000000000 | 1.000000 | 1.000000000 |
| 2 | 0.955818490 | 1.351731 | 0.923632012 |
| 5 | 0.833841887 | 1.864527 | 0.762238935 |
| 10 | 0.704689065 | 2.228422 | 0.618866167 |
| 20 | 0.565254318 | 2.527894 | 0.480738698 |
| 50 | 0.396241902 | 2.801853 | 0.327835432 |
| 100 | 0.292837776 | 2.928378 | 0.239469289 |

The infinite one-photon pulse has fidelity one exactly. The exact
[two-photon optimum](native_emission.md#sec-two) is larger than the
trial value, as required.

For the [partial-source trial pulse](partial_excitation.md#eq-trial), the check
also evaluates the relative entropy by an independent
one-dimensional quantile integral:

| $`M`$ | $`n`$ | $`e^{-D_{M,n}}`$ | Trial fidelity |
| ---: | ---: | ---: | ---: |
| 10 | 2 | 0.998151912 | 0.999058744 |
| 20 | 10 | 0.967523540 | 0.981861157 |
| 100 | 10 | 0.999176823 | 0.999581755 |
| 100 | 90 | 0.681685371 | 0.763737854 |

A noninteger-parameter example is native emission with
$`N=5`$, $`\epsilon=0.25`$. The [all-photon sector probability](local_loss.md#eq-localprob) gives
$`p_0=0.5883789413`$; the conditional trial fidelity is
$`0.8693225961`$, and the unconditional trial yield is
$`0.5114911087`$.

Across these default rows, the largest change between the two
tolerance settings is $`2.7\times10^{-12}`$, and the largest
change between tail parameters 30 and 35 is
$`6.5\times10^{-12}`$. The largest mode-normalization residual is
$`2.2\times10^{-16}`$, and the independent quantile-integral
discrepancy is $`5.7\times10^{-14}`$. Evaluating the exact
two-photon Bessel mode with the cascade recursion gives a
squared-fidelity residual of $`1.9\times10^{-13}`$.

The verification also compares the direct product and gamma
quotient for $`p_0`$, the unweighted hypergeometric identity
$`\sum_m\operatorname{HG}(N,m,k,j)=(N+1)/(k+1)`$, and the weighted identity
used in the [thinned count bound](attenuation.md#eq-thinningbound). The hypergeometric comparisons
use exact rational arithmetic. The program's machine-readable
output records the residuals, tolerance comparisons, and cutoff
budgets. These checks support implementation consistency; the
analytic proofs establish the uniform and asymptotic results.

## Continue reading

Run the documented commands in [verification/README.md](../verification/README.md). For the origin and scope of the analytic ingredients, see [Related work](../references/RELATED_WORK.md).
