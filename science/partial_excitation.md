# Partial excitation and the uniform fidelity crossover

Changing the number of symmetric excitations changes the relative importance of the initial waiting-time uncertainty. The same positive kernel connects the dilute regime, fixed excitation fractions, and near complete inversion. Its extension to a real parameter also supplies the conditional state for [independent local decay](local_loss.md).

## Dependence on the initial excitation

<a id="sec-partial"></a>

Let $`M`$ be the total number of emitters and $`n`$ the excitation
number of an initially symmetric Dicke state. Put $`a=M-n+1`$.
Exciting an arbitrary subset of $`n`$ emitters in a larger array
does not in general prepare this state or preserve the symmetric
sector. In the lossless symmetric problem the emitted-count rates
are $`r_j=(n-j)(a+j)`$, $`j=0,\ldots,n-1`$. Their product is
$`n!\Gamma_{\!E}(M+1)/\Gamma_{\!E}(a)`$, so the same ordered-coordinate normalization
as in the [exact emitted wavefunction](native_emission.md#sec-wave) gives

<a id="eq-affine"></a>

```math
P_{M,n}(\boldsymbol t)=\frac{\Gamma_{\!E}(M+1)}{\Gamma_{\!E}(a)}
 \exp\!\left[-a\sum_i t_i-\sum_{i\lt j}|t_i-t_j|\right].
```

Its positive square root is the normalized emitted amplitude.

### An exact product relative-entropy bound

The quantile argument of the [constructive lower bound](native_emission.md#sec-lower) now has
$`A(u)=(1-u)[a+(n-1)u]`$, and its initial-offset term is $`a x_0`$.
The pointwise minimizing derivative is again $`X'(u)=1/A(u)`$.
For $`n>1`$,

<a id="eq-trial"></a>

```math
\begin{aligned}
X_{M,n}(u)&=\frac1M
 \ln\frac{a+(n-1)u}{a(1-u)},\\
 p_{M,n}(t)&=\frac{aM^2e^{Mt}}{[ae^{Mt}+n-1]^2}.
\end{aligned}
```

The cumulative distribution of this pulse is
$`a(e^{Mt}-1)/(ae^{Mt}+n-1)`$. Thus normalization is exact.
Its product relative entropy with respect to the [affine-kernel density](#eq-affine) is

<a id="eq-d"></a>

```math
\boxed{
 D_{M,n}=n\left[\frac{M\ln M-a\ln a}{n-1}-1\right]
 -\ln\Gamma_{\!E}(M+1)+\ln\Gamma_{\!E}(a),\qquad
 F_{M,n}^\star\ge e^{-D_{M,n}}.}
```

The formula follows by substituting the quantile into the same
strictly convex functional used for the fully inverted source.
It is the global minimum of the product relative entropy, not
necessarily the pulse maximizing the actual fidelity. For $`n=1`$,
the density is $`p(t)=M e^{-Mt}`$, and fidelity one is exact.

The [affine-kernel density](#eq-affine), its normalization, and the variational
calculation also hold for integer $`n`$ and any real $`a\ge1`$,
with $`M=n+a-1`$. In that extension $`M`$ is a distribution parameter,
not a fractional emitter number. This will be needed for local-loss
conditioning in the [local-decay analysis](local_loss.md#sec-local).

### Uniform control in the dilute regime

Set $`b=n-1`$. The [optimized product relative entropy](#eq-d) is equivalently

<a id="eq-gridentropy"></a>

```math
D_{M,n}
 =n\left[\frac1b\int_a^M\ln x\,\mathrm{d} x
 -\frac1{b+1}\sum_{j=0}^b\ln(a+j)\right].
```

The equally weighted, endpoint-inclusive grid dominates the uniform
interval in convex order. To see this, a convex function's integral
average is at most its composite trapezoidal average. If its grid
values are $`g_0,\ldots,g_b`$, the grid average minus the trapezoidal
average is

```math
\frac{(b-1)(g_0+g_b)/2-\sum_{j=1}^{b-1}g_j}{b(b+1)}\ge0,
```

where the inequality follows by bounding the internal values by
the endpoint chord. For $`x^2/2`$, the grid average minus the
continuous average is $`b/12`$. Comparing the curvature of
$`\ln x`$ with $`-M^{-2}`$ and $`-a^{-2}`$, or applying convex
order to $`\ln x+x^2/(2a^2)`$ and concave order to
$`\ln x+x^2/(2M^2)`$, therefore gives

<a id="eq-dilutebound"></a>

```math
\boxed{\frac{n(n-1)}{12M^2}\le D_{M,n}\le
 \frac{n(n-1)}{12a^2}.}
```

Consequently,

<a id="eq-dilutefidelity"></a>

```math
F_{M,n}^\star\ge
 \exp\!\left[-\frac{n(n-1)}{12(M-n+1)^2}\right],
 \qquad n/M\to0\ \Longrightarrow\ F_{M,n}^\star\to1.
```

This remains uniform when $`n\to\infty`$. The qualitative
weak-excitation route to Fock emission is established in
[Liu and Shen](../references/RELATED_WORK.md#liu); the [dilute-source fidelity bound](#eq-dilutefidelity) quantifies the present
optimized-pulse problem.

### Fixed excitation fraction and uniform near-inversion scaling

Write the Stirling remainder as

```math
\ln\Gamma_{\!E}(x)=(x-\tfrac12)\ln x-x+\tfrac12\ln(2\pi)+R(x),
 \qquad 0\lt R(x)\lt \frac1{12x},\quad x\ge1.
```

Using $`\Gamma_{\!E}(M+1)=M\Gamma_{\!E}(M)`$, the [optimized product relative entropy](#eq-d) rearranges exactly to

<a id="eq-stirlingd"></a>

```math
D_{M,n}=\frac12\ln\frac Ma-1+
 \frac a{n-1}\ln\frac Ma+R(a)-R(M).
```

In particular, $`\ln(1+z)/z\le1`$ gives the real-$`a`$ bound

<a id="eq-realalower"></a>

```math
F_{M,n}^\star\ge e^{-D_{M,n}}
 \ge e^{-1/(12a)}\sqrt{\frac aM}.
```

If $`n/M\to\rho\in(0,1)`$, the [Stirling-remainder identity](#eq-stirlingd) gives

<a id="eq-fraction"></a>

```math
\liminf F_{M,n}^\star\ge
 e(1-\rho)^{(2-\rho)/(2\rho)}>0.
```

This is a lower bound, not the exact limiting fidelity. At
$`\rho=1/2`$ it is $`e/(2\sqrt2)=0.961057757\ldots`$.

**Theorem (Near complete inversion, including real $`a`$).**

<a id="thm-partial"></a>

For integer $`n`$, real $`a\ge1`$, and $`M=n+a-1`$, along every
sequence $`M\to\infty`$ with $`a=o(M)`$,

<a id="eq-realascaling"></a>

```math
\boxed{F_{M,n}^\star=\Theta\!\left(\sqrt{\frac aM}\right).}
```

The implicit constants may be chosen uniformly along these
sequences. For physical integer $`M,n`$, this is the symmetric
partial-source fidelity.

**Proof.**

The lower estimate is uniform by the [real-parameter lower bound](#eq-realalower).
For the upper estimate take $`J=\max(2,\lceil a\rceil)`$, which is
$`o(n)`$. Each of the first $`J`$ waiting rates is at most $`2na`$.
The sum $`T_J`$ of those waits therefore has characteristic function
bounded by

```math
|\widehat h_J(\omega)|
 \le[1+(\omega/(2na))^2]^{-J/2}.
```

Fourier inversion gives

<a id="eq-fourierbound"></a>

```math
\begin{aligned}
\left\lVert h_J\right\rVert_\infty
 &\le\frac{na}{\sqrt\pi}
 \frac{\Gamma_{\!E}((J-1)/2)}{\Gamma_{\!E}(J/2)}
 \le\frac{na}{\sqrt{J-1}}
 \le\sqrt2\,n\sqrt a.
\end{aligned}
```

The middle inequality is the beta-integral bound
$`\int_{\mathbb R}(1+x^2)^{-J/2}\,\mathrm{d} x\le\pi/\sqrt{J-1}`$;
it follows from the Wallis gamma-ratio inequality and is equality
at $`J=2`$. Convolution with later waits does not increase the
density supremum. The [arrival-density and dwell bound](native_emission.md#eq-dwell) now yields

```math
p_m(T)\le
 \frac{\sqrt2\,n\sqrt a}{(n-m)(a+m)},\qquad J\le m\lt n.
```

For $`n/4\le m\le3n/4`$ this is $`O(\sqrt a/n)`$.
At the median of an arbitrary trial pulse, the target count is
$`\mathrm{Bin}(n,1/2)`$. Its square-root probabilities sum to
$`O(n^{1/4})`$; the contribution outside the stated central
interval is exponentially small by Cauchy–Schwarz and the
binomial tail bound. The [count-affinity inequality](native_emission.md#eq-countfidelity) therefore
gives $`F_{M,n}^\star=O(\sqrt{a/n})`$.
Since $`n/M\to1`$, this proves the [uniform near-inversion law](#eq-realascaling).

∎

The trial lower bound has more explicit constants. If
$`a\to\infty`$ while $`a=o(M)`$, the [Stirling-remainder identity](#eq-stirlingd) gives
$`e^{-D_{M,n}}=[e+o(1)]\sqrt{a/M}`$. If $`a`$ is fixed,

<a id="eq-fixedalower"></a>

```math
\sqrt M\,e^{-D_{M,n}}\longrightarrow
 \sqrt{2\pi}\frac{a^a e^{1-a}}{\Gamma_{\!E}(a)}.
```

These are asymptotics of the analytic lower bound, not asserted
optimal-fidelity prefactors. They include the fully inverted
case $`a=1`$. At the opposite extreme $`n/a\to0`$,
the [real-parameter lower bound](#eq-realalower) also implies fidelity tending to one.

## Continue reading

Compare this preparation change with [uniform attenuation](attenuation.md), which traces out photons after emission. The real-parameter result is used in [local-loss conditioning](local_loss.md), and the integer case supplies the exact [prefix-detection identity](prefix_detection.md).
