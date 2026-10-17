# Uniform attenuation and the surviving-photon ceiling

Uniform optical loss samples particles from the emitted state without selecting a temporal mode. The conditional state is therefore a reduced density operator, and its temporal count statistics retain a uniform fidelity ceiling. The underlying model and fidelity convention are fixed in [Model and central question](model.md).

## Uniform attenuation: surviving photons retain a modal ceiling

<a id="sec-attenuation"></a>

Let $`\mathcal L_\eta`$ be uniform, mode-independent attenuation of the
ideal output, with vacuum in the unused port and $`0<\eta<1`$.
The number $`K_{\mathrm{out}}`$ of transmitted photons is binomial:

<a id="eq-binomialloss"></a>

```math
\mathbb{P}(K_{\mathrm{out}}=k)=B_{N,\eta}(k)
 =\binom Nk\eta^k(1-\eta)^{N-k}.
```

Conditioned on $`k`$, the temporal state is the normalized
$`k`$-particle reduced density operator $`\rho_N^{(k)}`$. This follows
by applying the same beam splitter to each particle coordinate:
choosing the transmitted labels gives the binomial coefficient, and
tracing the other port traces the remaining coordinates. Write
$`F_{N\to k}^\star=F^\star(\rho_N^{(k)})`$.

**Theorem (Uniform survivor bound).**

There is a universal $`C<\infty`$ such that
$`F_{N\to k}^\star\le C/\sqrt{k}`$ for all $`N\ge k\ge1`$.
More precisely, along every sequence $`N\ge k\to\infty`$,

<a id="eq-survivor"></a>

```math
\limsup \sqrt{k}\,F_{N\to k}^\star
 \le\frac{4\sqrt{2\pi}}e.
```

For a fixed retained fraction $`k/N\to\eta_0\in(0,1]`$,
$`F_{N\to k}^\star=\Theta(N^{-1/2})`$.

**Proof.**

Let $`p_m(T)`$ be the probability of $`m`$ original photons before
a dimensionless cut $`T`$. The [uniform count argument](native_emission.md#sec-upper) already establishes
the arrival-density and dwell estimate

<a id="eq-entrydwell"></a>

```math
p_m(T)\le\frac{N}{(m+1)(N-m)}
 \le\frac{N}{m(N-m)},\qquad 1\le m<N.
```

The retained early count has the hypergeometric mixture

<a id="eq-hypergeom"></a>

```math
q_j(T)=\sum_{m=0}^N p_m(T)
 \underbrace{\frac{\binom mj\binom{N-m}{k-j}}{\binom Nk}}
 _{\operatorname{HG}(N,m,k,j)}.
```

For $`1\le j<k`$, the kernel vanishes at $`m=0,N`$. The identities
$`\binom mj/m=\binom{m-1}{j-1}/j`$ and its complementary version,
followed by Vandermonde convolution, give

<a id="eq-thinningbound"></a>

```math
\begin{aligned}
\sum_{m=1}^{N-1}\frac{\operatorname{HG}(N,m,k,j)}{m(N-m)}
 &=\frac{\binom{N-1}{k-1}}
 {j(k-j)\binom Nk}
 =\frac{k}{N j(k-j)},\\
 q_j(T)&\le\frac{k}{j(k-j)}.
\end{aligned}
```

This estimate is uniform in $`T,N,k`$.

For any proposed mode choose a median time $`T`$ of $`|f|^2`$.
The target $`\lvert k_{f}\rangle`$ has cut-count law
$`b_j=\binom kj2^{-k}`$. Monotonicity of fidelity under this
measurement implies

<a id="eq-measurement"></a>

```math
\langle k_f|\rho_N^{(k)}|k_f\rangle
 \le\left(\sum_{j=0}^k\sqrt{q_j(T)b_j}\right)^2.
```

On $`|j-k/2|\le k^{2/3}`$, the [thinned count bound](#eq-thinningbound) is at most
$`(4+o(1))/k`$. Stirling's formula gives
$`\sum_j\sqrt{b_j}\sim(2\pi k)^{1/4}`$. Outside this window, the
affinity contribution is at most the square root of the binomial
tail probability, by Cauchy–Schwarz, and is exponentially small in
$`k^{1/3}`$. This proves a universal $`O(k^{-1/2})`$ bound.

For the stated prefactor, the [uniform count argument](native_emission.md#sec-upper) proves that
the density supremum of the first fixed $`J\ge2`$ arrivals is
$`N[c_J+o_N(1)]`$, where $`c_J=(1-1/J)^{J-1}`$.
Thus the numerator $`N`$ in the [native entry-and-dwell estimate](#eq-entrydwell) can be replaced by
$`N[c_J+o_N(1)]`$ whenever $`m\ge J`$. For central retained
$`j\ge J`$, every contributing $`m`$ is at least $`J`$, so the same
Vandermonde identity applies. The [measured-fidelity inequality](#eq-measurement) yields
$`\limsup\sqrt{k}F_{N\to k}^\star\le4c_J\sqrt{2\pi}`$.
Since $`N\ge k\to\infty`$, the error is uniform along every stated
sequence. Taking $`J\to\infty`$ gives the [uniform survivor ceiling](#eq-survivor).

For the lower bound, the falling-factorial occupation identity is

<a id="eq-rdmlower"></a>

```math
\langle k_f|\rho_N^{(k)}|k_f\rangle
 =\left\langle\frac{(\hat n_f)_k}{(N)_k}\right\rangle
 \ge\langle N_f|\rho_N|N_f\rangle.
```

The contribution from occupation $`n_f=N`$ is one and all other
terms are nonnegative. Optimize and apply the [native fidelity theorem](model.md#eq-main).
For $`k`$ proportional to $`N`$, the two orders match.

∎

**Corollary (Optimize both output photon number and mode).**

At fixed $`0<\eta<1`$,

<a id="eq-anynumber"></a>

```math
\max_{0\le k\le N}\sup_f
 \langle k_f|\mathcal L_\eta(\rho_N)|k_f\rangle
 =\Theta(N^{-1}).
```

If all $`N`$ photons are required instead, the yield is
$`\eta^NF_N^\star=\Theta(\eta^N/\sqrt N)`$.

**Proof.**

In a fixed bulk interval around $`\eta N`$, the binomial point
probability is $`O(N^{-1/2})`$ and the conditional fidelity is
$`O(N^{-1/2})`$. Outside that interval the point probability is
exponentially small. For the reverse inequality choose a modal
binomial count, whose probability is $`\Theta(N^{-1/2})`$, and use
the [falling-factorial lower bound](#eq-rdmlower) with the full-source trial mode.

∎

A parasitic *collective* channel $`\sqrt{\kappa}J_-`$ is equivalent
to this beam-splitter loss after a clock rescaling, with
$`\eta=\Gamma/(\Gamma+\kappa)`$. A time- or frequency-selective
filter is not uniform attenuation and is not covered by this theorem.

## Continue reading

[Independent local atomic decay](local_loss.md) produces a different conditional kernel and different photon-number statistics. The distinction determines which loss theorem can be used.
