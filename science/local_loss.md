# Independent local decay and conditional photon fidelity

Local atomic decay records which emitter lost an excitation. The all-desired-photon sector remains tractable through a no-jump identity, while sectors with fewer desired photons need not remain symmetric. The [partial-source kernel](partial_excitation.md) gives the exact conditional fidelity problem.

## Independent local decay and the cost of strong conditioning

<a id="sec-local"></a>

Now add independent channels
$`L_i=\sqrt{\gamma}\,\sigma_i^-`$, one for each emitter, with constant
$`\gamma\ge0`$, and define $`\epsilon=\gamma/\Gamma`$.
With no pumping, observing all $`N`$ desired photons means that no
local jump occurred. The $`N`$-photon sector is pure: its local
environment is vacuum and the emitters end in their ground state.
It can be identified retrospectively by destructive total counting.
A usable herald that leaves the photons available requires an
additional nondestructive success flag or suitable monitoring of the
undesired environment.

**Proposition (Exact all-photon sector).**

Put $`a=1+\epsilon`$ and $`M=N+a-1`$. The sector probability is

<a id="eq-localprob"></a>

```math
p_0=\prod_{j=1}^N\frac{j}{j+\epsilon}
 =\frac{\Gamma_{\!E}(N+1)\Gamma_{\!E}(1+\epsilon)}{\Gamma_{\!E}(N+1+\epsilon)}.
```

Its unnormalized symmetric amplitude and normalized density are

<a id="eq-localkernel"></a>

```math
\begin{aligned}
\psi_{\mathrm{un}}(\boldsymbol\tau)
 &=\sqrt{N!}\,
   e^{-a\sum_i\tau_i/2-\sum_{i<j}|\tau_i-\tau_j|/2},\\
 P_{\mathrm{cond}}(\boldsymbol\tau)
 &=\frac{\Gamma_{\!E}(N+a)}{\Gamma_{\!E}(a)}
   e^{-a\sum_i\tau_i-\sum_{i<j}|\tau_i-\tau_j|}.
\end{aligned}
```

The physical-time amplitude additionally has the Jacobian factor
$`\Gamma^{N/2}`$.

**Proof.**

Before desired jump $`j`$, there are $`q=N-j+1`$ excitations.
The desired rate is $`\Gamma jq`$, and the sum of the local rates is
$`\gamma q`$. The next jump is desired with probability
$`j/(j+\epsilon)`$; its waiting time, independent of that jump
identity, has rate $`\Gamma q(j+\epsilon)`$. Multiplying these
probabilities proves the [all-photon sector probability](#eq-localprob). Along a history with no
local jump, the integrated excitation number is $`\sum_i t_i`$.
The no-local-jump propagator consequently multiplies the ideal
amplitude by $`e^{-\gamma\sum_i t_i/2}`$, proving the first line.
Dividing its squared modulus by the [all-photon sector probability](#eq-localprob) gives the
second line. Equivalently the normalized ordered waits have
dimensionless rates $`(N-j+1)(a+j-1)`$.

∎

The competing-rate, no-jump-product treatment of local decay is
used by [Paulisch et al.](../references/RELATED_WORK.md#paulisch). Its exact gamma
quotient supplies the success probability and normalization for
the optimized temporal-mode fidelity analyzed here.

**Corollary (Conditional scaling and fixed-loss target yield).**

For every sequence $`a=1+\epsilon\ge1`$ with $`a=o(N)`$,

<a id="eq-localconditionalscaling"></a>

```math
F_{\mathrm{cond}}^\star
 =\Theta\!\left(\sqrt{\frac aN}\right),
```

with uniform implicit constants. At fixed $`\epsilon\ge0`$,

<a id="eq-fixedlossyield"></a>

```math
p_0\sim\Gamma_{\!E}(1+\epsilon)N^{-\epsilon},\qquad
 Y_N^\star=p_0F_{\mathrm{cond}}^\star
 =\Theta(N^{-\epsilon-1/2}).
```

**Proof.**

The [local-loss conditional kernel](#eq-localkernel) is precisely the
[affine-kernel density](partial_excitation.md#eq-affine) with $`n=N`$, $`a=1+\epsilon`$, and
$`M=N+a-1`$. The real-$`a`$ [near-inversion theorem](partial_excitation.md#thm-partial)
therefore gives the conditional scaling, with
$`M/N\to1`$ in this regime. The fixed-$`\epsilon`$ gamma-ratio
asymptotic in the [all-photon sector probability](#eq-localprob) gives the sector probability,
and multiplying proves the target-yield law.

∎

The unconditional optimized yield is nonincreasing in $`\epsilon`$.
Indeed an optimal mode for the nonnegative kernel can be chosen
nonnegative, and increasing $`\epsilon`$ decreases every such
unnormalized overlap pointwise. No corresponding monotonicity of
the normalized conditional fidelity is assumed.

**Corollary (Strong conditioning has an exponential cost).**

If $`\epsilon=cN`$, with fixed $`c>0`$, then

<a id="eq-strongf"></a>

<a id="eq-strongp"></a>

```math
\begin{aligned}
\liminf F_{\mathrm{cond}}^\star
 &\ge e\left(\frac c{1+c}\right)^{c+1/2}, \\
 p_0&\sim\sqrt{\frac{2\pi Nc}{1+c}}
 \left[\frac{c^c}{(1+c)^{1+c}}\right]^N.
\end{aligned}
```

More generally, keeping this native source's conditional fidelity
bounded below by a positive constant requires
$`\epsilon=\Omega(N)`$, and hence exponentially small acceptance.
If $`\epsilon/N\to\infty`$, the conditional fidelity tends to one.

**Proof.**

For $`\epsilon=cN`$, the [Stirling-remainder identity](partial_excitation.md#eq-stirlingd) tends to
$`(c+\tfrac12)\ln[(1+c)/c]-1`$; exponentiating proves
the [strong-conditioning fidelity bound](#eq-strongf). Stirling's formula in the [all-photon sector probability](#eq-localprob)
gives the [strong-conditioning acceptance asymptotic](#eq-strongp). If $`\epsilon`$ were not $`\Omega(N)`$,
a subsequence would have $`a/N\to0`$, contradicting
the [uniform near-inversion law](partial_excitation.md#eq-realascaling). When $`\epsilon\ge cN`$, monotonicity of
$`p_0`$ gives an exponential upper bound using the [strong-conditioning acceptance asymptotic](#eq-strongp).
Finally $`a/N\to\infty`$ makes the lower bound
[real-parameter lower bound](partial_excitation.md#eq-realalower) tend to one.

∎

At $`\epsilon=N`$, these statements read
$`p_0=\binom{2N}{N}^{-1}\sim\sqrt{\pi N}\,4^{-N}`$ and
$`\liminf F_{\mathrm{cond}}^\star\ge e/(2\sqrt2) =0.961057757\ldots`$.
For size-dependent $`\epsilon`$, the exact gamma quotient must be
used outside the stated asymptotic regimes.

Local atomic loss is not uniform optical attenuation. After a local
jump the emitter state can leave the symmetric sector, and the
environment carries atom-specific information. For example, at
$`N=2`$ the desired photon-number probabilities are

```math
\mathbb{P}(K_{\mathrm{out}}=2)=\frac2{(1+\epsilon)(2+\epsilon)},\quad
 \mathbb{P}(K_{\mathrm{out}}=1)=\frac{2\epsilon}{(1+\epsilon)(2+\epsilon)},
 \quad
 \mathbb{P}(K_{\mathrm{out}}=0)=\frac{\epsilon}{2+\epsilon}.
```

To obtain them, after a first local jump decompose the remaining
one-excitation mixture equally into its symmetric bright and
antisymmetric dark states; only the bright part can emit into
$`J_-`$. At $`\epsilon=1`$ all three probabilities are $`1/3`$,
which is not a two-photon binomial law. The
[uniform survivor theorem](attenuation.md#eq-survivor) therefore does not apply to the
fewer-than-$`N`$ sectors of local atomic loss.

The gamma-quotient formulas also extend to
$`\gamma(t)=\epsilon\Gamma(t)`$ with constant ratio and complete
emission, by using $`\tau=\int_0^t\Gamma(s)\,\mathrm{d} s`$. If
$`\Gamma(t)`$ is shaped while physical $`\gamma`$ stays fixed,
the factor $`e^{-\gamma\sum_i t_i/2}`$ remains in physical time;
the constant-ratio formulas cannot be substituted without a new
calculation.

## Continue reading

The [phase and common-rate restrictions](control_restrictions.md) delimit controls that preserve the ideal modal ceiling. The [exact-Fock criterion](exact_fock_control.md) and [capped coherent construction](capped_control.md) then distinguish exact factorization from fidelity tending to one.
