# Native collective emission and its single-mode fidelity

The fully inverted source emits a pure multiphoton state with correlated arrival times. This page gives its exact wavefunction, an explicit trial pulse, the matching uniform fidelity exponent, and the exact two-photon benchmark. The [model](model.md) fixes the target quantity and physical assumptions.

## Exact emitted wavefunction

<a id="sec-wave"></a>

Use the normalized symmetric-coordinate convention

```math
|\Psi_N\rangle=\frac1{\sqrt{N!}}\int_{[0,\infty)^N}
 \psi_N(\boldsymbol t)\prod_{i=1}^N b^\dagger(t_i)\,d^N t,
 \qquad\int|\psi_N|^2\,d^Nt=1.
```

The successive waiting times between emissions are independent exponentials with rates

```math
\lambda_j=j(N-j+1),\qquad j=1,\ldots,N.
```

For ordered times $`0=t_0\lt t_1\lt \cdots\lt t_N`$,

```math
\begin{aligned}
\sum_{j=1}^N\lambda_j(t_j-t_{j-1})
 &=\sum_{j=1}^N(2j-N)t_j\\
 &=\sum_i t_i+\sum_{i\lt j}|t_i-t_j|.
\end{aligned}
```

Since $`\prod_j\lambda_j=(N!)^2`$, the standard cascade amplitude [Perarnau-Llobet et al.](../references/RELATED_WORK.md#perarnau) becomes

<a id="eq-wave"></a>

```math
\boxed{
 \psi_N(\boldsymbol t)=\sqrt{N!}\exp\!\left[-\frac12\sum_i t_i-
 \frac12\sum_{i\lt j}|t_i-t_j|\right].}
```

Indeed the ordered-domain density is $`N!|\psi_N|^2=(N!)^2\exp[-\sum_j\lambda_j(t_j-t_{j-1})]`$, which integrates to one over that domain. The symmetric density $`P_N=|\psi_N|^2`$ therefore integrates to one over the full orthant. Positivity permits replacing $`f`$ by $`|f|`$ without decreasing the overlap.

## Constructive lower bound

<a id="sec-lower"></a>

### A classical affinity identity

For a probability density $`p`$ on the half-line, put $`f=\sqrt p`$ and $`Q_p(\boldsymbol t)=\prod_i p(t_i)`$. The amplitude is exactly the classical Hellinger affinity,

```math
\langle N_f|\Psi_N\rangle=\int\sqrt{P_NQ_p}\,d^Nt
 =\mathbb{E}_{Q_p}\exp\!\left[\tfrac12\log(P_N/Q_p)\right].
```

Jensen's inequality, followed by squaring, gives

```math
\boxed{F_N^\star\ge F_N[f]\ge\exp[-D(Q_p\Vert P_N)].}
```

From the [native wavefunction](#eq-wave),

<a id="eq-kl"></a>

```math
D(Q_p\Vert P_N)=N\int p\log p+N\mathbb{E}_p t+
 \frac{N(N-1)}2\mathbb{E}_p|t-s|-\log N!.
```

No approximation or independence assumption about the actual output is used: only the trial density $`Q_p`$ is a product.

### An explicit normalized pulse

Choose

<a id="eq-pulse"></a>

```math
\boxed{
 p_N(t)=\frac{N^2e^{Nt}}{(e^{Nt}+N-1)^2},\qquad
 f_N(t)=\frac{Ne^{Nt/2}}{e^{Nt}+N-1},\qquad t\ge0.}
```

Its cumulative distribution is $`(e^{Nt}-1)/(e^{Nt}+N-1)`$, so normalization is exact. For $`N>1`$,

```math
\begin{aligned}
\mathbb{E} t&=\frac{\log N}{N-1},&
 \mathbb{E}|t-s|&=\frac{2[(N-1)-\log N]}{(N-1)^2},\\
 \int p_N\log p_N&=\frac{N\log N}{N-1}-2.
\end{aligned}
```

Substitution yields

```math
D(Q_{p_N}\Vert P_N)=\frac{N^2\log N}{N-1}-N-\log N!,
```

and the exact finite-$`N`$ lower bound

<a id="eq-lower"></a>

```math
\boxed{
 F_N^\star\ge L_N:=\frac{e^N N!}{N^{N^2/(N-1)}}\quad(N\ge2).}
```

For $`N=1`$, the [normalized native trial pulse](#eq-pulse) reduces to $`p_1(t)=e^{-t}`$ and $`F_1^\star=1`$. Stirling's expansion gives

```math
L_N=\sqrt{\frac{2\pi}{N}}\exp\!\left[-\frac{\log N}{N-1}
 +\frac1{12N}+O(N^{-3})\right],
```

which proves the lower half of the [native fidelity theorem](model.md#eq-main).

### Optimality within the relative-entropy variational principle

The [normalized native trial pulse](#eq-pulse) globally minimizes the [relative-entropy functional](#eq-kl), although it need not maximize the true fidelity. Let $`X(u)`$ be the quantile of $`p`$, $`v(u)=X'(u)>0`$, and $`x_0=X(0)\ge0`$. For an absolutely continuous quantile with finite objective,

```math
\frac{D(Q_p\Vert P_N)+\log N!}{N}
 =x_0+\int_0^1[A_N(u)v(u)-\log v(u)]\,du,
```

where $`A_N(u)=(1-u)[1+(N-1)u]`$. The integrand is strictly convex in $`v`$ and minimized pointwise at $`v=1/A_N`$; $`x_0`$ is minimized at zero. Integration gives

```math
X_N(u)=\frac1N\log\frac{1+(N-1)u}{1-u},
```

equivalent to the [normalized native trial pulse](#eq-pulse). Quantile jumps and singular increments add the nonnegative Stieltjes term $`\int A_N\,dX_{\mathrm{singular}}`$ and cannot improve the infimum. This establishes the same minimum for density-derived generalized quantiles with finite objective.

## Uniform upper bound from temporal photon counts

<a id="sec-upper"></a>

### Every trial pulse supplies its own median cut

Fix any normalized mode $`f`$. There is a time $`T`$ with $`\int_0^T|f(t)|^2dt=1/2`$. The number $`m`$ of photons before $`T`$ in $`|N_f\rangle`$ has distribution

```math
b_N(m)=2^{-N}\binom Nm.
```

Let $`p_m(T)`$ be the corresponding Dicke-output count distribution. Projection onto the orthogonal count sectors, followed by Cauchy–Schwarz within each sector, implies

<a id="eq-countfidelity"></a>

```math
|\langle N_f|\Psi_N\rangle|
 \le\sum_{m=0}^N\sqrt{p_m(T)b_N(m)}.
```

The cut may depend on $`f`$ because the following estimates are uniform in $`T`$. This is an analysis device, not an assumption of feedback during emission.

### Arrival times bound count probabilities

The emitted count is a pure-birth process with rates $`r_m=(m+1)(N-m)`$ from $`m`$ to $`m+1`$. This reduction is standard Dicke dynamics [Malz et al.](../references/RELATED_WORK.md#malz). Write $`T_m`$ for the $`m`$th arrival and $`h_m`$ for its density. For $`1\le m\le N-1`$,

<a id="eq-dwell"></a>

```math
p_m(T)=\int_0^T h_m(s)e^{-r_m(T-s)}\,ds
 \le\frac{\left\lVert h_m\right\rVert_\infty}{r_m}.
```

$`T_m`$ contains the independent first waiting time $`\mathrm{Exp}(N)`$, so convolution gives $`\left\lVert h_m\right\rVert_\infty\le N`$. Already,

```math
p_m(T)\le\min\!\left\{1,\frac{N}{(m+1)(N-m)}\right\}.
```

Together with the [count-affinity inequality](#eq-countfidelity), this gives an explicit finite-$`N`$ upper bound by inserting the displayed expression for $`1\le m\lt N`$ and the bound one for $`m=0,N`$, and clipping the resulting squared sum at one.

To improve the asymptotic constant, fix $`K\ge2`$ independently of $`N`$. For $`m\ge K`$, convolution contraction gives $`\left\lVert h_m\right\rVert_\infty\le\left\lVert h_K\right\rVert_\infty`$. The density of $`NT_K`$ converges uniformly to that of $`Y_K=\sum_{j=1}^K\mathrm{Exp}(j)`$. This follows from convergence of each fixed-rate exponential density in both $`L^1`$ and $`L^\infty`$, followed by convolution. $`Y_K`$ has the distribution of the maximum of $`K`$ independent unit-rate exponentials, hence

```math
h_{Y_K}(s)=Ke^{-s}(1-e^{-s})^{K-1},\qquad
 \left\lVert h_{Y_K}\right\rVert_\infty=c_K=(1-1/K)^{K-1}.
```

Therefore $`\left\lVert h_K\right\rVert_\infty=N[c_K+o_N(1)]`$. Uniformly over $`T`$ and $`|m-N/2|\le N^{2/3}`$,

```math
p_m(T)\le\frac{4c_K+o_N(1)}{N}.
```

### The binomial width determines the exponent

A binomial Chernoff bound and Cauchy–Schwarz give

```math
\sum_{|m-N/2|>N^{2/3}}\sqrt{p_m(T)b_N(m)}
 \le\sqrt2\,e^{-N^{1/3}}.
```

Stirling's formula with Gaussian tail control gives

```math
\sum_{m=0}^N\sqrt{b_N(m)}=(2\pi N)^{1/4}[1+o(1)].
```

Combining the central and tail estimates in the [count-affinity inequality](#eq-countfidelity), uniformly over every $`f`$,

```math
F_N^\star\le\frac{4c_K\sqrt{2\pi}+o_N(1)}{\sqrt N}.
```

First take $`N\to\infty`$ at each fixed $`K`$, then $`K\to\infty`$. Since $`c_K\to e^{-1}`$, the upper half of the [native fidelity theorem](model.md#eq-main) follows. No exchange of a growing-$`K`$ limit is needed.

### Physical origin of the count bound

The source starts at rate $`N`$ and accelerates to rates of order
$`N^2`$. The early waiting-time uncertainty is not erased by that
acceleration. At a trial mode's median cut, a Fock pulse has a
binomial count width of order $`\sqrt N`$; Dicke emission has central
count probabilities at most of order $`1/N`$. This mismatch bounds the
affinity even after pulse optimization. The arrival-density divided
by dwell-rate argument also applies to other radiative cascades,
although it alone does not supply a matching lower exponent for
another source.

## Exact optimal fidelity for two photons

<a id="sec-two"></a>

For $`N=2`$, $`\psi_2(t,s)=\sqrt2e^{-\max(t,s)}`$ is a positive symmetric integral kernel. Its eigenvalue equation differentiates to

```math
f''+f'+\frac{\sqrt2}{\lambda}e^{-t}f=0,\qquad f'(0)=0.
```

Decay at infinity selects the Bessel solution. If $`j_{0,1}`$ is the first positive zero of $`J_0`$,

```math
\boxed{
 F_2^\star=\frac{32}{j_{0,1}^4}=0.956787875131927\ldots,\qquad
 f_2^\star(t)=\frac{e^{-t/2}J_1(j_{0,1}e^{-t/2})}{J_1(j_{0,1})}.}
```

The pulse is exactly normalized. The first zero gives the largest kernel eigenvalue $`4\sqrt2/j_{0,1}^2`$.

## Continue reading

The [partial-excitation analysis](partial_excitation.md) extends the same kernel and variational principle. The [attenuation theorem](attenuation.md) applies the count argument after photons are lost, and the [numerical checks](numerical_checks.md) evaluate specified trial pulses.
