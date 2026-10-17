<a id="sec-capped"></a>

# Capped coherent control with fidelity tending to one

An excitation-dependent coupling to one coherent output can respect every native rate cap and still approach a single-mode Fock state at the native order of completion time. The construction below also gives an explicit acceptance bound under fixed independent local loss.

**Reading route:** [Model and conventions](model.md) · [Exact Fock criterion and rate-cap penalty](exact_fock_control.md) · [Independent local loss](local_loss.md)

Choose an even integer $`4\le K<N`$ and set
$`T_0=-\Gamma^{-1}\ln(1-K/N)`$. Define a target cumulative
distribution and its hazard by

<a id="eq-cappedcdf"></a>

<a id="eq-cappedhazard"></a>

```math
\begin{aligned}
u(t)&=
 \begin{cases}
  1-e^{-\Gamma t},&0\le t\le T_0,\\[2pt]
  \displaystyle\left[1+\frac{N-K}{K}
  e^{-\Gamma N(t-T_0)/2}\right]^{-1},&t\ge T_0,
 \end{cases} \\
 h(t)&=\frac{u'(t)}{1-u(t)}
 =\begin{cases}\Gamma,&t<T_0,\\
 \Gamma Nu(t)/2,&t>T_0.
 \end{cases}
\end{aligned}
```

The target mode is $`f=\sqrt{u'}`$. Its ideal Fock ladder would
have rates $`s_m=(N-m)h`$. Instead implement the single coherent
jump with zero phases and rates

<a id="eq-cappedrates"></a>

```math
r_m^C(t)=(N-m)\min\{h(t),\Gamma(m+1)\}.
```

They obey

<a id="eq-cappedbounds"></a>

```math
\Gamma(N-m)\le r_m^C(t)\le\Gamma(m+1)(N-m).
```

Every rung is attenuated from its native value by the amplitude
factor $`\min\{1,\sqrt{h(t)/[\Gamma(m+1)]}\}`$. This is coherent,
excitation-dependent coupling to one output, not feedback based
on a measured photon record. The piecewise regular model permits
the hazard jump at $`T_0`$.

## Theorem: Finite-K fidelity and release-time guarantee

Let

<a id="eq-deltak"></a>

```math
\delta_K=\min\left\{1,\frac{e^{-K/8}}{1-e^{-1/4}}\right\}.
```

The lossless source with the [capped rates](capped_control.md#eq-cappedrates) satisfies

<a id="eq-cappedfidelity"></a>

```math
F_N^C[f]\ge(1-\delta_K)^2.
```

For $`0<\delta_{\mathrm{tail}}<1`$, define

<a id="eq-t1"></a>

```math
T_1=T_0+\frac2{\Gamma N}
 \ln\frac{N(N-K)}{K\delta_{\mathrm{tail}}}.
```

Then

<a id="eq-cappedtime"></a>

```math
\mathbb{E}_C T_{\mathrm{last}}
 \le T_1+(\delta_K+\delta_{\mathrm{tail}})\frac{\mathsf{H}_N}{\Gamma}.
```

For the smallest even $`K\ge24\ln N`$ and
$`\delta_{\mathrm{tail}}=N^{-3}`$, at sufficiently large $`N`$,

<a id="eq-cappedasymptotic"></a>

```math
F_N^C[f]\ge1-O(N^{-3}),\qquad
 \mathbb{E}_C T_{\mathrm{last}}
 =O\!\left(\frac{\ln N}{\Gamma N}\right).
```

**Proof.**

Under the target Fock density, $`U_i=u(t_i)`$ are independent
uniform variables. Write $`M(v)=\#\{i:U_i\le v\}`$ and define

<a id="eq-good"></a>

```math
G=\{M(v)+1\ge Nv/2\text{ for every }v\in[K/N,1]\}.
```

On $`G`$, actual and target rates agree at every time along the
entire history, including all no-jump intervals. Before $`T_0`$
they agree without restriction. Their positive amplitudes and
probability densities therefore coincide pointwise on $`G`$.

If $`G`$ fails at $`v`$, let $`j=M(v)+1<Nv/2`$.
When $`j\le K/2`$, it follows that
$`M(K/N)<K/2`$; the binomial lower-tail bound is $`e^{-K/8}`$.
For $`j>K/2`$, the $`j`$th order statistic satisfies
$`U_{(j)}>2j/N`$, so a binomial with mean $`2j`$ is at most
$`j-1`$, of probability at most $`e^{-j/4}`$.
Only $`j<N/2`$ can violate the inequality, but extending the sum
to infinity increases the bound. Hence

```math
\mathbb{P}_f(G^c)
 \le e^{-K/8}+\sum_{j>K/2}e^{-j/4}
 =\frac{e^{-K/8}}{1-e^{-1/4}}\le\delta_K
```

when the displayed untruncated bound is at most one; otherwise
the trivial probability bound supplies $`\delta_K=1`$.
The normalized actual and target densities agree on $`G`$, so
$`\mathbb{P}_C(G^c)=\mathbb{P}_f(G^c)\le\delta_K`$.
Their affinity is at least their common probability on $`G`$.
Squaring proves the [finite-K fidelity bound](capped_control.md#eq-cappedfidelity).

The [cutoff time](capped_control.md#eq-t1) gives
$`1-u(T_1)=\delta_{\mathrm{tail}}/(N+\delta_{\mathrm{tail}})`$.
Thus the target probability of a late photon is
$`1-u(T_1)^N\le N[1-u(T_1)]\le\delta_{\mathrm{tail}}`$.
Equality of the good-history densities implies
$`\mathbb{P}_C(T_{\mathrm{last}}>T_1)\le\delta_K+\delta_{\mathrm{tail}}`$.
From any state and time, the lower half of the
[two-sided rate bound](capped_control.md#eq-cappedbounds) limits the mean remaining release time
by $`\mathsf{H}_N/\Gamma`$. Splitting the mean completion time at
$`T_1`$ proves the [mean completion-time bound](capped_control.md#eq-cappedtime). Finally the stated choice
of $`K`$ gives $`\delta_K=O(N^{-3})`$, while
$`T_0=O(\ln N/(\Gamma N))`$ and the second term in
the [cutoff time](capped_control.md#eq-t1) has the same order.

∎

The initial part of the target pulse contains mean count $`K`$.
The later hazard rises with its deterministic cumulative
probability. Only strongly delayed count histories would need
a rate enhancement; clipping changes these rare histories.
Thus the exact-factorization slowdown in [Exact Fock factorization and the native-rate cap](exact_fock_control.md#sec-exact) is not
a bound on fidelities tending to one. The
[capped rates](capped_control.md#eq-cappedrates) and their [asymptotic fidelity and time guarantee](capped_control.md#eq-cappedasymptotic) give a
constructive counterexample under the very same native-rate cap.

## Fixed local loss: polynomial acceptance and high conditional fidelity

Add independent local decay at rate $`\gamma`$ per excitation.
Let $`\psi_C`$ be the normalized lossless capped-source amplitude.
The all-desired amplitude is
$`e^{-\gamma\sum_i t_i/2}\psi_C`$, by the same integrated-excitation
identity used in [Independent local loss](local_loss.md#sec-local). Define

<a id="eq-tiltedmode"></a>

```math
q(\gamma)=\int_0^\infty e^{-\gamma t}|f(t)|^2\,\mathrm{d} t,\qquad
 g_\gamma(t)=q(\gamma)^{-1/2}e^{-\gamma t/2}f(t).
```

## Theorem: Loss robustness of the capped construction

Let $`P_{\mathrm{acc}}`$ be the probability that all $`N`$ photons
enter the desired output, and $`Y_N[g_\gamma]`$ its unconditional
overlap with $`\lvert N_{g_\gamma}\rangle`$. Then

<a id="eq-accbounds"></a>

<a id="eq-lossf"></a>

```math
\begin{aligned}
(1-\delta_K)q(\gamma)^N
 &\le P_{\mathrm{acc}}\le q(\gamma)^N, \\
 Y_N[g_\gamma]&\ge q(\gamma)^N(1-\delta_K)^2,\\
 F_{N\mid\mathrm{all\ desired}}[g_\gamma]
 &\ge(1-\delta_K)^2.
\end{aligned}
```

Moreover, with $`\epsilon=\gamma/\Gamma`$,

<a id="eq-polysuccess"></a>

```math
q(\gamma)^N
 \ge\exp\{-\epsilon[K+2\ln(N/K)]\}.
```

For fixed $`\epsilon`$ and the $`K=O(\ln N)`$ choice above,
acceptance has a polynomial lower bound in $`N`$, while conditional
fidelity tends to one.

**Proof.**

Exponential tilting by $`e^{-\gamma t}`$ makes the distribution
$`|g_\gamma|^2`$ stochastically earlier than $`|f|^2`$. One may
see this by noting that an increasing indicator of a late time
has nonpositive covariance with the decreasing weight.
The event $`G`$ is preserved by moving any arrival earlier.
An independent quantile coupling therefore gives
$`\mathbb{P}_{g_\gamma}(G)\ge1-\delta_K`$.

On $`G`$, $`\psi_C=\prod_i f(t_i)`$. Integrating its locally
attenuated squared modulus over $`G`$ gives
$`P_{\mathrm{acc}}\ge q^N\mathbb{P}_{g_\gamma}(G)`$.
Likewise, restricting the positive overlap with
$`\prod_i g_\gamma(t_i)`$ to $`G`$ gives amplitude at least
$`q^{N/2}\mathbb{P}_{g_\gamma}(G)`$, proving the yield bound.

For the upper bound on acceptance, $`r_m^C(t)\le s_m(t)`$ at
every common state and time. Couple the two pure-birth processes
so that whenever their counts agree all actual jumps can be
shared with target jumps, with extra jumps allowed for the
target. When the counts differ, unit jumps cannot reverse their
order. This gives every actual arrival time no earlier than
its coupled target arrival. Hence

```math
P_{\mathrm{acc}}=\mathbb{E}_C e^{-\gamma\sum_i t_i}
 \le\mathbb{E}_f e^{-\gamma\sum_i t_i}=q^N .
```

Dividing the yield lower bound by this upper bound proves
the [conditional-fidelity bound](capped_control.md#eq-lossf).

Integrating the survival function in the [target cumulative distribution](capped_control.md#eq-cappedcdf) gives
the exact first moment

<a id="eq-firstmoment"></a>

```math
N\mathbb{E}_f t
 =N\int_0^\infty[1-u(t)]\,\mathrm{d} t
 =\frac{K+2\ln(N/K)}{\Gamma}.
```

Jensen's inequality,
$`\mathbb{E}_f e^{-\gamma t}\ge e^{-\gamma\mathbb{E}_f t}`$,
proves the [polynomial acceptance bound](capped_control.md#eq-polysuccess).

∎

The polynomial exponent in the [polynomial acceptance bound](capped_control.md#eq-polysuccess) is a guarantee,
not an optimized loss frontier. It may be worse than the native
success exponent in the [native fixed-loss yield law](local_loss.md#eq-fixedlossyield). The result concerns
the all-desired sector; operational use of its conditioning has
the heralding qualification stated in [Independent local loss](local_loss.md#sec-local).

## Lemma: Accepted completion times are stochastically earlier

For any such time-dependent pure-birth ladder with positive
cumulative rates and complete release, conditioning on no
independent local loss makes the completion time stochastically
no later than its lossless completion time. In particular,

<a id="eq-acceptedtime"></a>

```math
\mathbb{E}[T_{\mathrm{last}}\mid\mathrm{all\ desired}]
 \le\mathbb{E}_C T_{\mathrm{last}}.
```

**Proof.**

Let $`R_m(t)=\int_0^t r_m(s)\,\mathrm{d} s`$. Using independent
unit-rate exponentials $`E_m`$, construct successive arrivals by

```math
T_{m+1}=R_m^{-1}\bigl(R_m(T_m)+E_m\bigr),\qquad T_0=0.
```

Here $`R_m^{-1}(x)=\inf\{t\ge0:R_m(t)\ge x\}`$ is the
generalized inverse, allowing intervals with zero rate.
Each $`T_j`$ is coordinatewise increasing in all the $`E_m`$.
Independent product measures are associated: two increasing
functions have nonnegative covariance. This follows by the
one-variable Chebyshev covariance identity and induction over
independent coordinates. Therefore any increasing function of
the arrivals has nonpositive covariance with
$`W=e^{-\gamma\sum_jT_j}`$, a decreasing function of those
coordinates. The no-local-loss conditional measure weights
histories by $`W/\mathbb{E} W`$. Applying the covariance inequality to
$`\mathbf{1}_{\{T_N>t\}}`$ proves stochastic domination; integrating
the tail inequality proves the [accepted completion-time bound](capped_control.md#eq-acceptedtime).

∎

The argument uses monotonic cumulative rates and their inverses,
not monotonic instantaneous rates in time. Consequently accepted
runs of the capped construction also finish in mean time
$`O(\ln N/(\Gamma N))`$.

## Connections

The [physical interpretation](interpretation.md) connects this construction to the native, loss, and prefix results. The [verification guide](../verification/README.md) distinguishes finite consistency checks from the analytic guarantees proved here.
