# Model and central question

How closely can all photons emitted by a collective source occupy one temporal mode, and which preparation or control resources change that fidelity? The account follows this question from the native emission law to photon loss, prefix detection, and coherent control.

## Scientific overview

For ideal Dicke emission from $`N`$ initially excited emitters, the
maximum squared overlap with any single-temporal-mode $`N`$-photon
Fock state is $`\Theta(N^{-1/2})`$. An explicit normalized pulse and
a relative-entropy inequality give the lower bound; temporal photon
counts give an upper bound uniform over all pulse shapes. The argument
extends to $`n`$ symmetric excitations in $`M`$ emitters: near full
inversion the fidelity is $`\Theta(\sqrt{(M-n+1)/M})`$, whereas it
tends to one when $`n/M\to0`$. Uniform attenuation retains a
conditional ceiling of order $`k^{-1/2}`$ for $`k`$ surviving photons,
and at fixed transmission $`0\lt\eta\lt1`$ the best unconditional
photon-number and mode target has yield $`\Theta(N^{-1})`$. Independent local decay
instead produces a different exact conditional kernel and a
polynomial all-photon yield at fixed loss ratio. Diagonal collective
phases and common rate shaping cannot improve the ideal modal
fidelity. Detecting and consuming a prefix gives an exact resource
law, with explicit detection-efficiency and switching-delay costs.
Exact Fock emission from a coherent Markov ladder requires bosonic
rates and separable phases; under a native-rate cap exact Fock
factorization is slow. This exactness restriction is singular: a capped,
excitation-dependent coherent coupling achieves fidelity tending to
one at the native order of completion time, with polynomial
all-photon acceptance at fixed local-loss ratio. The control construction
specifies a mathematical coupling model rather than an experimental
implementation.

## Model, observables, and main result

<a id="sec-model"></a>

We consider identical two-level emitters in their fully symmetric spin
sector, vacuum input, one desired Markov output, and complete eventual
emission. The native coupling is $`L_{\mathrm{out}}=\sqrt{\Gamma}J_-`$,
with $`\Gamma>0`$. Unless a section explicitly introduces loss or
control, there is no pumping, dephasing, feedback, or other output
channel. These are the ideal collective-emission assumptions used in
the waveguide descriptions of Refs. [Paulisch et al.](../references/RELATED_WORK.md#paulisch), [Perarnau-Llobet et al.](../references/RELATED_WORK.md#perarnau).

Let $`b^\dagger(t)`$ create an output photon, with
$`[b(t),b^\dagger(s)]=\delta(t-s)`$. For a normalized temporal mode,

<a id="eq-fidelitydef"></a>

```math
a_f^\dagger=\int_0^\infty f(t)b^\dagger(t)\,\mathrm{d} t,\qquad
 \lvert n_{f}\rangle=\frac{(a_f^\dagger)^n}{\sqrt{n!}}|0\rangle,\qquad
 F^\star(\rho_n)=\sup_{\left\lVert f\right\rVert_2=1}\langle n_f|\rho_n|n_f\rangle.
```

Here $`\rho_n`$ has trace one in the $`n`$-photon sector. All
fidelities are squared overlaps, or their mixed-state extension
against a pure target. The optimization includes arbitrary complex
pulse shapes and is not restricted to the most populated one-photon
mode. If the sector occurs with probability $`p_n`$, its unconditional
target-state yield is $`Y_n^\star=p_nF^\star(\rho_n)`$. Sector
probability, conditional mode fidelity, and yield are separate
quantities.

For the lossless [native-source calculations](native_emission.md) and
[partial-source calculations](partial_excitation.md), time is measured in units
$`\Gamma^{-1}`$, and $`t`$ denotes the dimensionless coordinate.
Rescaling a physical mode by
$`\widetilde f(\tau)=\Gamma^{-1/2}f(\tau/\Gamma)`$ preserves its norm
and all overlaps. Later loss and control sections use physical
$`t`$, with dimensionless $`\tau=\Gamma t`$ stated when needed.
Euler's gamma function is denoted $`\Gamma_{\!E}`$, to distinguish it from
the emission rate.

**Theorem (Fully inverted source).**

For the ideal output $`\rho_N=|\Psi_N\rangle\langle\Psi_N|`$ of $`N`$ fully excited emitters, write $`F_N^\star=F^\star(\rho_N)`$. Then

<a id="eq-main"></a>

```math
\boxed{
 \sqrt{2\pi}\le\liminf_{N\to\infty}\sqrt N F_N^\star
 \le\limsup_{N\to\infty}\sqrt N F_N^\star
 \le\frac{4\sqrt{2\pi}}{e}.}
```

Consequently $`F_N^\star=\Theta(N^{-1/2})`$. The two endpoint constants are approximately $`2.506628`$ and $`3.688548`$.

The [native fidelity theorem](#eq-main) determines the power, not the existence or value of a limiting prefactor. The displayed asymptotic constants are not finite-$`N`$ upper and lower inequalities without their limiting qualifications.

The [constructive lower bound](native_emission.md#sec-lower) and
[uniform count argument](native_emission.md#sec-upper) prove the two sides
of this theorem.

## Continue reading

Continue with the [exact waveform and native fidelity bounds](native_emission.md). The [partial-excitation analysis](partial_excitation.md) introduces the common family used by the loss and prefix protocols.
