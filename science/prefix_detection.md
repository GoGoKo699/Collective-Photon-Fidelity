<a id="sec-prefix"></a>

# Prefix detection: photon resources and imperfections

Detecting and consuming an initial photon prefix prepares a less excited symmetric source for the remaining emission. The record-aligned state gives an exact fidelity identity, and the same stopping rule gives an exact cost for imperfect detection and delayed routing.

**Reading route:** [Model and conventions](model.md) · [Partial excitation](partial_excitation.md) · [Restrictions on controls](control_restrictions.md)

Start with the lossless native source. Detect and consume its first
$`r`$ photons, $`0\le r<N`$, and immediately route all later photons
to the retained output. Use the $`r`$th-click time as the new time
origin; for $`r=0`$, use the preparation time.

## Proposition: Prefix identity

With perfect detection, time resolution, and switching, the
record-aligned retained field has exactly the partial-source state
with $`M=N`$, $`n=N-r`$, $`a=r+1`$. Hence

<a id="eq-prefixidentity"></a>

```math
F_{\mathrm{prefix}}(N,r)=F_{N,N-r}^\star.
```

In particular, for $`r=o(N)`$,

<a id="eq-prefixlaw"></a>

```math
F_{\mathrm{prefix}}(N,r)
 =\Theta\!\left(\sqrt{\frac{r+1}{N}}\right).
```

If $`r/N\to\alpha\in(0,1)`$, then

<a id="eq-prefixfraction"></a>

```math
\liminf F_{\mathrm{prefix}}(N,r)
 \ge e\,\alpha^{(1+\alpha)/[2(1-\alpha)]}.
```

**Proof.**

Between clicks the symmetric ladder state acquires a scalar
no-jump factor; each click applies $`J_-`$. After $`r`$ desired
jumps the normalized state is the symmetric Dicke state with
$`N-r`$ excitations, independent of all earlier waiting times.
The Markov property and stationary coupling make the future field
relative to that click precisely the partial-source output.
The remaining assertions follow from [Partial excitation](partial_excitation.md#sec-partial). No favorable timing record is selected: in the ideal
model the $`r`$th click eventually occurs with probability one.

∎

A sublinear consumed prefix cannot keep the fidelity bounded away
from zero. A macroscopic prefix permits a nonzero limiting
fidelity while retaining a macroscopic photon number.
For $`\alpha=1/2`$, the explicit lower bound is
$`e/(2\sqrt2)=0.961057757\ldots`$, not the exact optimal fidelity.
If $`N-r=o(N)`$, the dilute-source bound implies fidelity tending
to one. At finite size with $`N-r>1`$, one may use
$`e^{-D_{N,N-r}}`$. For one retained photon the fidelity is exactly
one. A simpler sufficient bound, valid also in that case, is

```math
F_{\mathrm{prefix}}(N,r)\ge
 \exp\!\left[-\frac{(N-r)(N-r-1)}{12(r+1)^2}\right].
```

Ignoring the recorded origin produces a mixture of temporal
translations, a different target problem. This protocol consumes
the prefix; it is not a nondestructive measurement on the original
$`N`$-photon state, nor an optimality theorem for all adaptive controls.

## Proposition: Exact nominal-target detection and latency cost

Let $`r\ge1`$, detector efficiency $`0<d\le1`$, and a deterministic
delay $`\Delta\ge0`$ between the $`r`$th detected click and routing.
Each prefix photon is independently detected, no other source
loss is present, and native emission continues during the delay.
For the predetermined target photon number $`n=N-r`$, the optimized
record-aligned yield per initial trial is exactly

<a id="eq-prefixcost"></a>

```math
Y_{N-r}^{\mathrm{nom}}(d,\Delta)
 =d^r e^{-\Gamma(N-r)(r+1)\Delta}F_{N,N-r}^\star.
```

Conditioning the ensemble on a trigger divides this by
$`\mathbb{P}[\operatorname{Bin}(N,d)\ge r]`$.

**Proof.**

If $`S`$ photons have actually been emitted at the $`r`$th detected
click, then

```math
\mathbb{P}(S=s,\mathrm{trigger})
 =\binom{s-1}{r-1}d^r(1-d)^{s-r},\qquad r\le s\le N.
```

Summing gives the stated trigger probability. Only $`S=r`$ can
leave the nominal $`N-r`$ photons, and that event has probability
$`d^r`$. From this post-click level, the next waiting rate is
$`\Gamma(N-r)(r+1)`$. Keeping the same nominal number during the
delay requires no additional emission, with probability equal to
the exponential factor in the [nominal-target yield formula](prefix_detection.md#eq-prefixcost). Conditioned on no
such jump, the normalized spin state is unchanged. Its future
field, referred to the switch time, is the same partial source.
Every other branch is orthogonal to the nominal photon-number
target, so multiplication gives the exact result.

∎

For $`r=\Theta(N)`$, fixed $`d<1`$ gives an exponential
nominal-yield penalty. To keep the detection factor nonvanishing
requires $`r[-\ln d]=O(1)`$, equivalently $`r(1-d)=O(1)`$ near
unit efficiency. When both $`r`$ and $`N-r`$ are proportional to
$`N`$, the delay factor requires
$`\Gamma N^2\Delta=O(1)`$; in general the exact condition is
$`\Gamma(N-r)(r+1)\Delta=O(1)`$. The corresponding $`o(1)`$ conditions
make the penalties tend to one. These statements apply to this
stopping rule and predetermined target. Extra number information,
accepting several output counts, buffering, or stopping emission
during the delay changes the protocol and its resource accounting.

## Connections

For coherent changes to the source ladder, continue with the [exact Fock criterion and rate-cap penalty](exact_fock_control.md), followed by the [capped construction with fidelity tending to one](capped_control.md).
