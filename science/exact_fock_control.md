<a id="sec-exact"></a>

# Exact Fock factorization and the native-rate cap

A coherent Markov ladder emits an exact single-mode Fock state precisely when its hazards and phases have the form below. Under a cap set by the native Dicke rates, this exact factorization imposes a completion-time and local-loss penalty.

**Reading route:** [Model and conventions](model.md) · [Coherent ladder and restricted controls](control_restrictions.md) · [Independent local loss](local_loss.md)

We return to the [coherent ladder](control_restrictions.md#eq-ladder), with locally
integrable rates, vacuum input, and complete emission. No extra
environment records its excitation-dependent control.
For a normalized target pulse $`p(t)=|f(t)|^2`$, define its
survival $`S(t)=1-\int_0^t p(s)\,\mathrm{d} s`$ and hazard
$`h(t)=p(t)/S(t)`$ where $`S(t)>0`$.

## Theorem: Exact Fock criterion within a Markov ladder

The output is exactly $`\lvert N_{f}\rangle`$, up to a global phase, if and
only if on reachable times and levels

<a id="eq-exactcriterion"></a>

```math
r_m(t)=(N-m)h(t),\qquad
 \phi_m(t)=\arg f(t)+c_m\pmod{2\pi},
```

where $`c_m`$ are constants and

<a id="eq-phase"></a>

```math
\phi_m(t)=\theta_m(t)
 -\int_0^t[E_m(s)-E_{m+1}(s)]\,\mathrm{d} s .
```

The rate equality holds almost everywhere at every reachable time,
including pulse gaps where $`h=0`$. The phase equality is required
only where $`f\ne0`$.
When its cumulative probability is strictly between zero and one,
every level is reachable and the rate equality applies to every
$`m=0,\ldots,N-1`$.

**Proof.**

In an $`N`$-photon Fock mode the detection times are independent
draws from $`p`$. Given $`m`$ arrivals by time $`t`$, the hazard of
the next is $`(N-m)h(t)`$. The physical ladder hazard is $`r_m(t)`$.
Equality of the joint density therefore forces the first condition.
All levels have positive binomial probability when the cumulative
probability lies in $`(0,1)`$. Conversely, those hazards generate
the independent order-statistic law, so the positive amplitude
equals the target amplitude.

For ordered times $`0<t_1<\cdots<t_N`$, the product of jump phases
and diagonal propagators has phase
$`\sum_{j=1}^N\phi_{j-1}(t_j)`$, up to a global final-state phase.
To equal the target, its difference from
$`\sum_j\arg f(t_j)`$ must be constant on the ordered support.
Varying one ordered coordinate at a time implies the second
condition almost everywhere; the constants are consistent across
overlapping ordered neighborhoods. The condition is sufficient
by multiplication. Support gaps and times after release impose
only the corresponding reachable-state requirements.

∎

For stationary positive rates and phases removed, the criterion
reduces to $`r_m=\kappa(N-m)`$, with
$`f(t)=\sqrt{\kappa}e^{-\kappa t/2}`$. A formal realization is

<a id="eq-linearjump"></a>

```math
L_{\mathrm{lin}}(t)
 =\sqrt{h(t)}\,J_-[N-\hat n+1]^{-1/2},
```

where $`\hat n`$ is the current excitation number and the right
factor acts first. Its matrix element is $`\sqrt{h(t)n}`$.
This is a truncated bosonic annihilation ladder. Bosonic
Fock-state release and pulse synthesis are established prior
constructions [Gough–Zhang](../references/RELATED_WORK.md#gough), [Brown et al.](../references/RELATED_WORK.md#brown), [Pfaff et al.](../references/RELATED_WORK.md#pfaff); the [linearized jump coupling](exact_fock_control.md#eq-linearjump)
identifies the coupling required inside this spin ladder.
Measuring the count and updating a scalar rate is not automatically
equivalent: an extra history record can destroy temporal coherence.

For reference, a stationary positive ladder has the following
exact overlap with the exponential comparison mode:

<a id="eq-stationaryoverlap"></a>

```math
F_{\exp}(\kappa)=
 \prod_{m=0}^{N-1}
 \left[\frac{2\sqrt{r_m\kappa(N-m)}}{r_m+\kappa(N-m)}\right]^2.
```

It follows by integrating the square root of each pair of
exponential waiting densities. Writing
$`r_m=\kappa(N-m)e^{\xi_m}`$ gives
$`F_{\exp}=\prod_m\operatorname{sech}^2(\xi_m/2)`$. Thus small independent
relative mismatches accumulate quadratically. This is a
comparison-mode formula, not a necessary error budget for the
fully optimized fidelity.

## Proposition: Exact-factorization penalty under a native-rate cap

Assume the control can only attenuate native rates:

<a id="eq-ratecap"></a>

```math
0\le r_m(t)\le\Gamma(m+1)(N-m).
```

If its lossless output is an exact single-mode Fock state, then
$`h(t)\le\Gamma`$ and

<a id="eq-exactslow"></a>

```math
\mathbb{E} T_{\mathrm{last}}\ge\frac{\mathsf{H}_N}{\Gamma},
 \qquad \mathsf{H}_N=\sum_{j=1}^N\frac1j.
```

Constant $`h=\Gamma`$ attains this bound. Native emission has

<a id="eq-nativetime"></a>

```math
\mathbb{E} T_{\mathrm{last}}^{\mathrm{native}}
 =\frac{2\mathsf{H}_N}{\Gamma(N+1)}.
```

If independent local loss $`\gamma`$ is added to these same
lossless-exact controls, their all-desired sector remains
single-mode, but its probability is at most
$`(1+\gamma/\Gamma)^{-N}`$.

**Proof.**

The $`m=0`$ constraint in the [native-rate cap](exact_fock_control.md#eq-ratecap), together with
the [exact Fock criterion](exact_fock_control.md#eq-exactcriterion), gives $`h\le\Gamma`$.
The zero-count state remains reachable whenever $`S(t)>0`$, so
it cannot be removed from this argument by appealing to typical
counts. The cumulative hazard obeys
$`\int_0^t h\le\Gamma t`$. Coupling each of the $`N`$ independent
target arrival times to a unit-rate exponential shows that it is
no earlier than an exponential of rate $`\Gamma`$. The expected
maximum of the latter is $`\mathsf{H}_N/\Gamma`$, proving
the [exact-factorization completion-time bound](exact_fock_control.md#eq-exactslow). Summing the native waiting means
$`\{\Gamma j(N-j+1)\}^{-1}`$ proves the [native completion-time formula](exact_fock_control.md#eq-nativetime).

With local loss, the unnormalized one-photon mode is

```math
v_\gamma(t)=e^{i\arg f(t)}\sqrt{h(t)}
 e^{-\frac12\int_0^t h(s)\,\mathrm{d} s-\gamma t/2},\qquad
 q=\left\lVert v_\gamma\right\rVert_2^2.
```

The all-desired field is
$`q^{N/2}\lvert N_{v_\gamma/\sqrt q}\rangle`$, with probability $`q^N`$.
Since its lossless arrival time is stochastically no earlier than
$`\operatorname{Exp}(\Gamma)`$,
$`q=\mathbb{E} e^{-\gamma t}\le\Gamma/(\Gamma+\gamma)`$.
Equality holds for constant $`h=\Gamma`$.

∎

The exact lossless Fock-factorization constraint therefore incurs at least
a factor $`(N+1)/2`$ in mean completion time under the cap.
This statement does not classify controls designed only to purify
a lossy postselected sector, whose conditioning changes transition
hazards. It also does not extend to fidelity approaching one. The next
construction shows why that distinction is essential.

## Connections

The [capped coherent construction](capped_control.md) uses the same native-rate cap while allowing fidelity to approach one. Its rare clipped histories explain why the exact-factorization penalty does not extend to that limit.
