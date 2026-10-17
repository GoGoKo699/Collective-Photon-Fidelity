<a id="sec-phases"></a>

# Controls that cannot improve modal fidelity

Within a single coherent output, symmetric diagonal phases and common deterministic rate shaping cannot overcome the native modal-fidelity ceiling. The restrictions below apply to complete photon states and their normalized reduced states.

**Reading route:** [Model and conventions](model.md) · [Native emission](native_emission.md) · [Uniform attenuation](attenuation.md) · [Independent local loss](local_loss.md)

Label the symmetric ladder by the emitted count $`m=0,\ldots,N`$.
Consider a single coherent output and a diagonal Hamiltonian,

<a id="eq-ladder"></a>

```math
L(t)=\sum_{m=0}^{N-1}\sqrt{r_m(t)}e^{i\theta_m(t)}
 |m+1\rangle\langle m|,\qquad
 H(t)=\sum_{m=0}^{N}E_m(t)|m\rangle\langle m|.
```

We set $`\hbar=1`$. Every Hamiltonian that preserves both excitation
number and the fully symmetric spin sector has this diagonal
form, because each excitation sector of that spin representation
is one-dimensional. This statement does not cover Hamiltonians
that mix spin sectors or introduce a cavity, memory, or other
ancilla.

## Proposition: Phase removal and scalar rate shaping

At fixed rates $`r_m(t)`$, removing the Hamiltonian and jump phases
cannot decrease the optimized full-photon fidelity or the optimized
fidelity of any normalized $`k`$-particle reduced state.
For native rates $`r_m(t)=\kappa(t)(m+1)(N-m)`$, common deterministic
shaping with $`\int_0^\infty\kappa(t)\,\mathrm{d} t=\infty`$ leaves those
optimized fidelities unchanged.

**Proof.**

Let $`\psi_0\ge0`$ be the phase-free amplitude. The
[coherent ladder](control_restrictions.md#eq-ladder) changes it only to
$`\psi_H(\boldsymbol t)=\psi_0(\boldsymbol t)e^{i\Phi(\boldsymbol t)}`$.
For retained variables $`\boldsymbol t`$ and traced variables
$`\boldsymbol z`$,

<a id="eq-phaserm"></a>

```math
\begin{aligned}
F_k(H;f)
 &=\int\,\mathrm{d}\boldsymbol z\,
 \left|\int\psi_H(\boldsymbol t,\boldsymbol z)
                \prod_{i=1}^k f(t_i)^*\,\mathrm{d}\boldsymbol t\right|^2\\
 &\le\int\,\mathrm{d}\boldsymbol z\,
 \left[\int\psi_0(\boldsymbol t,\boldsymbol z)
                \prod_{i=1}^k |f(t_i)|\,\mathrm{d}\boldsymbol t\right]^2
 =F_k(0;|f|).
\end{aligned}
```

For $`k=N`$ there are no traced variables. Optimization proves
the phase claim, including after uniform attenuation.

Let $`\tau(t)=\int_0^t\kappa(s)\,\mathrm{d} s`$. The map

<a id="eq-isometry"></a>

```math
(U_\kappa f)(t)=\sqrt{\kappa(t)}\,f(\tau(t))
```

is a one-photon isometry, and acts identically on every emitted
coordinate. The transformed field and all its reduced states lie
in its range, so optimization over all physical modes gives the
same fidelity as before the transformation. Partial tracing
commutes with this common isometry. This proves the rate claim.

∎

Arbitrary functions of $`J_z`$, including nonlinear collective
phases within this ladder, are covered by the [phase-removal inequality](control_restrictions.md#eq-phaserm).
Combining them with common rate shaping cannot remove
the [native fidelity law](model.md#eq-main) or the [surviving-photon ceiling](attenuation.md#eq-survivor). The same invariance
holds for any common lossless one-photon unitary. Independent
local loss at a fixed physical rate changes the problem, as the
[independent-local-loss account](local_loss.md#sec-local) explains.

## Ideal all-photon mode filtering

For an ideal filter retaining one normalized temporal mode $`f`$
and rejecting its orthogonal complement, the probability that
all $`N`$ photons are retained is
$`|\langle N_f|\Psi_N\rangle|^2`$. On that event the retained
state is $`\lvert N_{f}\rangle`$. Optimization gives
$`F_N^\star=\Theta(N^{-1/2})`$ for the fully inverted source.
This equality follows by projecting onto occupation $`n_f=N`$.
It gives an all-photon extraction probability, distinct from a
deterministic source guarantee. A usable herald must identify
success without consuming the desired retained photons; the
projection probability alone does not supply such an apparatus.

## Connections

Continue with [prefix detection](prefix_detection.md), which changes the retained photon-number resource, or [exact Fock control](exact_fock_control.md), which changes the coherent transition ladder.
