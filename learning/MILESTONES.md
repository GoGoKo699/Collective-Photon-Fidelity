# Thirty milestones for collective photon fidelity

This is the shared understanding map for humans and LLMs working with this project. It organizes the scientific dependencies and the explanation each topic needs. Learner attempts and progress belong in the teaching session. The [tutoring protocol](../AGENTS.md#learning-map-and-tutoring) governs requested lessons; the questions below identify the subject of each milestone.

The canonical reference is [Single-mode fidelity of collective photon emission](../theory/collective_photon_fidelity.pdf), with [LaTeX source](../theory/collective_photon_fidelity.tex). The educational anchor is Alexander Holm Kiilerich and Klaus Mølmer, [*Quantum interactions with pulses of radiation*, Physical Review A **102**, 023717 (2020)](https://arxiv.org/abs/2003.04573), DOI [10.1103/PhysRevA.102.023717](https://doi.org/10.1103/PhysRevA.102.023717). Read its Sections II A–C and III along the route below; the [bridge guide](BRIDGE.md) connects its notation and pulse formalism to this project.

## Structure and use

**Phase I, background/preliminaries, contains M01–M14.** It moves from the source and one temporal mode through input–output dynamics, several modes, emission trajectories, and the probability tools needed to formulate the global fidelity problem. Fourteen milestones leave room to distinguish the different states and observables before using them in a proof.

**Phase II, narrative/innovation, contains M15–M30.** Its sixteen milestones follow the constructive lower bound and uniform upper bound into excitation regimes, optical and atomic loss, prefix resources, and the boundary between exact and approximate control. Here “innovation” identifies the project's argument and consequences; attribution follows the canonical reference's discussion of prior work. The additional space is needed because these conclusions depend on different physical assumptions and cannot be folded into one generic robustness claim.

Each phase ends with a synthesis. All milestone dependencies point to earlier milestones. A source pointer may introduce the canonical location where a background concept is later used; that is a reading reference, not an additional prerequisite. Anchor pointers appear where the paper supplies relevant foundations, while the project's theorems are sourced to the canonical reference.

**Teaching intensity** specifies one, two, or three learning rounds as a planning guide: one for a focused distinction, two for a derivation and its interpretation, and three for several linked arguments or a synthesis. Pacing follows the linked tutoring protocol. The map specifies no personal completion status.

| Milestones | Reading destination |
|---|---|
| [M01–M08](#m01) | Source assumptions, temporal modes, observables, and the anchor's input-output framework. |
| [M09–M14](#m09) | Collective trajectories, probability tools, and the background synthesis. |
| [M15–M17](#m15) | Constructive and uniform bounds, the native exponent, and the exact two-photon example. |
| [M18–M22](#m18) | Excitation regimes, optical attenuation, and local-loss conditioning. |
| [M23–M24](#m23) | Prefix preparation, photon costs, detection, and switching delay. |
| [M25–M30](#m25) | Restricted controls, exact and approximate Fock emission, and the final synthesis. |

## Phase I — Background/preliminaries

<a id="m01"></a>
### M01 — Source and field assumptions

- **Central question:** Which physical source and output field does the fidelity question describe?
- **Understanding target:** Identify a fully inverted ensemble, vacuum input, the collective jump $L=\sqrt{\Gamma}J_-$, and the ideal single output channel. Separate an emitter state from the emitted field state. A single spatial output channel still admits many temporal modes. Keep independent atomic loss and additional controls outside the native model until their assumptions are introduced.
- **Dependencies and story role:** Entry milestone. It fixes the physical system before defining its target state.
- **Sources:** [Theory Section 1, “Model, observables, and main result”](../theory/collective_photon_fidelity.tex), `sec:model`. Anchor: Section II, opening model and input–output assumptions.
- **Teaching intensity:** 1 round.

<a id="m02"></a>
### M02 — A normalized temporal-mode Fock state

- **Central question:** What does it mean for all $n$ photons to occupy one temporal mode?
- **Understanding target:** Use a normalized complex envelope $f$ with $\int_0^\infty |f(t)|^2dt=1$ to define $a_f^\dagger=\int f(t)b^\dagger(t)dt$ and $|n_f\rangle=(a_f^\dagger)^n|0\rangle/\sqrt{n!}$. Connect the continuum commutator to $[a_f,a_f^\dagger]=1$. Recognize that an overall phase of $f$ changes only the global phase of this fixed-number target.
- **Dependencies and story role:** [M01](#m01). Defines the one-mode target used throughout both phases.
- **Sources:** [Theory Section 1](../theory/collective_photon_fidelity.tex), `eq:fidelitydef`. Anchor: Section II A, normalized pulse and its quantum state.
- **Teaching intensity:** 2 rounds.

<a id="m03"></a>
### M03 — Which fidelity and which probability?

- **Central question:** Which observable answers the all-photons-in-one-mode question?
- **Understanding target:** Distinguish squared target overlap $\langle n_f|\rho_n|n_f\rangle$ from overlap amplitude, density-matrix purity, and mean mode occupation. For a normalized fixed-number sector $\rho_n$, keep its probability $p_n$, conditional fidelity $F_{\mathrm{cond}}$, and unconditional target yield $Y=p_nF_{\mathrm{cond}}$ separate. Optimization over $f$ changes the selected mode, not the normalization of the sector.
- **Dependencies and story role:** [M02](#m02). Establishes the quantities that later loss and conditioning results must report.
- **Sources:** [Theory Section 1](../theory/collective_photon_fidelity.tex), `sec:model` and `eq:fidelitydef`. Anchor: Sections II B–C supply the later comparison between mode occupation and the mode's full quantum state.
- **Teaching intensity:** 2 rounds.

<a id="m04"></a>
### M04 — Markov input–output dynamics

- **Central question:** How does an open-system jump operator specify radiation entering an output channel?
- **Understanding target:** Connect the Lindblad description, the continuum input–output relation, and the channel-labelled jump operators. Keep a Hamiltonian term, a dissipative channel, and a measurement record conceptually distinct. Understand why combining amplitudes into one coherent output jump differs from treating the same transitions as separately resolved reservoirs.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). Supplies the dynamical language for the virtual source and for the collective emission ladder.
- **Sources:** [Theory Section 1](../theory/collective_photon_fidelity.tex), `sec:model`; [Section 9](../theory/collective_photon_fidelity.tex), `eq:ladder`, for the later general ladder. Anchor: Section II, Eqs. (2)–(3), and Section II A, cascaded dynamics.
- **Teaching intensity:** 2 rounds.

<a id="m05"></a>
### M05 — A virtual source for a prescribed pulse

- **Central question:** How can one oscillator represent an incoming quantum pulse with a chosen envelope?
- **Understanding target:** Follow the anchor's virtual-source construction and the relation between the emitted envelope and the oscillator's time-dependent coupling. Track the complex conjugation and the remaining-pulse normalization in that relation. Interpret the construction as a representation of a prescribed quantum input; whether a particular physical emitter generates that pulse is a separate source-dynamics question.
- **Dependencies and story role:** [M02](#m02), [M04](#m04). Introduces pulse synthesis and the survival-hazard idea reused in the exact-control criterion.
- **Sources:** Anchor: Section II A, especially Eqs. (6)–(9). Project application: [Theory Section 11](../theory/collective_photon_fidelity.tex), `eq:exactcriterion` and `eq:linearjump`.
- **Teaching intensity:** 2 rounds.

<a id="m06"></a>
### M06 — Correlations and mode occupations

- **Central question:** What can first-order field correlations reveal about the emitted pulse?
- **Understanding target:** Interpret the first-order correlation kernel and its mode decomposition: eigenfunctions identify orthogonal temporal modes and eigenvalues give their mean occupations. Relate the largest occupation to an experimentally useful one-body statistic while preserving the distinction from an Fock overlap for $n$ photons. A large fraction in one mode does not by itself certify the probability that every photon occupies that mode.
- **Dependencies and story role:** [M03](#m03), [M04](#m04). Explains why the project asks for more than a dominant-mode calculation.
- **Sources:** Anchor: Section II B, especially Eq. (15). [Theory Section 1](../theory/collective_photon_fidelity.tex), `sec:model`, and [Section 14](../theory/collective_photon_fidelity.tex), `sec:discussion`.
- **Teaching intensity:** 2 rounds.

<a id="m07"></a>
### M07 — A virtual receiver and the selected-mode state

- **Central question:** How can a calculation access the complete quantum state in one output pulse?
- **Understanding target:** Follow the downstream virtual receiver for a chosen mode and distinguish its accumulated-pulse normalization from the source's remaining-pulse normalization. Identify the receiver state with the one-mode reduced state after tracing over orthogonal output modes. With a fixed total of $n$ photons, its probability for $n$ photons equals the full single-mode target overlap.
- **Dependencies and story role:** [M05](#m05), [M06](#m06). Connects a specified temporal envelope to an operationally meaningful quantum-state observable.
- **Sources:** Anchor: Section II C, especially Eqs. (17)–(19). Project connection: [Theory Section 9.1, “Ideal all-photon mode filtering”](../theory/collective_photon_fidelity.tex), under `sec:phases`; target definition `eq:fidelitydef` in [Section 1](../theory/collective_photon_fidelity.tex).
- **Teaching intensity:** 2 rounds.

<a id="m08"></a>
### M08 — Multimode states and two distinct reductions

- **Central question:** Which degrees of freedom are being traced out in a reduced description?
- **Understanding target:** Distinguish a one-mode reduced state, obtained by tracing out other field modes, from a normalized reduced density matrix for $k$ particles of a bosonic state with fixed total photon number $N$. The former has a distribution of photon numbers; the latter describes exactly $k$ particles. Keep both reductions separate from tracing out a residual emitter or a loss reservoir. Mode correlations can survive even when first-order observables look simple.
- **Dependencies and story role:** [M07](#m07). Prepares the reduced-state language needed for uniform attenuation.
- **Sources:** Anchor: Sections III A–B, joint states of several pulse modes. Project definition: [Theory Section 7](../theory/collective_photon_fidelity.tex), `sec:attenuation` and the paragraph following `eq:binomialloss`.
- **Teaching intensity:** 2 rounds.

<a id="m09"></a>
### M09 — The symmetric Dicke emission ladder

- **Central question:** Why does the next collective emission rate depend on how many photons have already left?
- **Understanding target:** Derive the jump amplitudes within the fully symmetric Dicke manifold. After $m$ emissions from full inversion, the physical rate is $\Gamma(m+1)(N-m)$. For a symmetric state of $M$ emitters with $n$ excitations, it is $\Gamma(n-m)(a+m)$ with $a=M-n+1$. Preparing an arbitrary subset of excited emitters does not supply this symmetric initial state.
- **Dependencies and story role:** [M01](#m01), [M04](#m04). Establishes the rate structure whose startup and middle portions later control the fidelity bounds.
- **Sources:** [Theory Section 2](../theory/collective_photon_fidelity.tex), `sec:wave`; [Section 5](../theory/collective_photon_fidelity.tex), `sec:partial`, opening ladder and `eq:affine`.
- **Teaching intensity:** 2 rounds.

<a id="m10"></a>
### M10 — From jump records to a normalized wavefunction

- **Central question:** How do ordered emission times become a symmetric many-photon field amplitude?
- **Understanding target:** Combine no-jump survival amplitudes and jump factors on an ordered time simplex, then recover the symmetric wavefunction. Track the distinction between $\int|\psi_N|^2=1$ on the full time domain and the ordered joint density $N!|\psi_N|^2$. Keep physical time separate from the dimensionless time used in the native proof. Explain why positivity of the native amplitude allows nonnegative trial modes in the optimization.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M09](#m09). Converts emitter dynamics into the normalized field object to which probability arguments apply.
- **Sources:** [Theory Section 2, “Exact emitted wavefunction”](../theory/collective_photon_fidelity.tex), `sec:wave` and `eq:wave`.
- **Teaching intensity:** 3 rounds.

<a id="m11"></a>
### M11 — Temporal counts and the product-state benchmark

- **Central question:** What does a single-mode Fock state predict for the number of early photons?
- **Understanding target:** Relate the factorized coordinate amplitude of $|N_f\rangle$ to independent arrival times with density $|f|^2$, while preserving bosonic symmetrization. An early/late cut then gives a binomial count distribution. Understand how a count measurement bounds quantum fidelity by the squared classical affinity between the two count distributions, without requiring access to every field observable.
- **Dependencies and story role:** [M03](#m03), [M10](#m10). Introduces the experimentally interpretable statistic behind the global upper bound.
- **Sources:** [Theory Section 4.1, “Every trial pulse supplies its own median cut”](../theory/collective_photon_fidelity.tex), `eq:countfidelity`; [Section 7](../theory/collective_photon_fidelity.tex), `eq:measurement`.
- **Teaching intensity:** 2 rounds.

<a id="m12"></a>
### M12 — Affinity and relative entropy

- **Central question:** How can a positive many-photon amplitude produce a constructive fidelity bound?
- **Understanding target:** With $P_N=|\psi_N|^2$ and $Q_p=p^{\otimes N}$, identify the overlap amplitude with the classical affinity $\int\sqrt{P_NQ_p}$. Apply Jensen's inequality to obtain the squared-overlap bound $F_N[\sqrt p]\ge e^{-D(Q_p\Vert P_N)}$. Preserve the direction $Q_p\Vert P_N$ and distinguish optimizing this entropy bound from optimizing the original fidelity functional.
- **Dependencies and story role:** [M03](#m03), [M10](#m10). Supplies the second proof tool, complementary to the count measurement.
- **Sources:** [Theory Section 3.1, “A classical affinity identity”](../theory/collective_photon_fidelity.tex), `eq:kl`; variational scope in [Section 3.3](../theory/collective_photon_fidelity.tex), under `sec:lower`.
- **Teaching intensity:** 2 rounds.

<a id="m13"></a>
### M13 — Asymptotic statements and numerical evidence

- **Central question:** What does each kind of calculation actually establish?
- **Understanding target:** Read finite-size inequalities, $O$ and $\Theta$ statements, fixed-ratio limits, and liminf/limsup bounds with their quantifiers intact. Distinguish an achievable trial overlap from the optimized fidelity. Understand the role of normalization checks, independent quadrature, and explicit truncation errors in testing formulas; those checks do not replace uniform estimates or establish an asymptotic prefactor.
- **Dependencies and story role:** [M10](#m10), [M11](#m11), [M12](#m12). Sets the evidential standard for interpreting every result in Phase II.
- **Sources:** [Theory Section 1, “Fully inverted source” theorem](../theory/collective_photon_fidelity.tex), `eq:main`; [Section 13](../theory/collective_photon_fidelity.tex), `sec:numerics` and `eq:recursion`. Reproducible implementation: [verification/check_fidelity.py](../verification/check_fidelity.py) and [verification/fidelity.py](../verification/fidelity.py).
- **Teaching intensity:** 2 rounds.

<a id="m14"></a>
### M14 — Synthesis: from source to a testable field question

- **Central question:** How do the physical model, pulse formalism, and probability tools fit into one fidelity question?
- **Understanding target:** Connect the chain from source preparation through channel-labelled dynamics and the normalized emitted wavefunction to a selected temporal-mode target. Explain which information comes from first-order correlations, a one-mode state, a particle reduction, and a temporal-count measurement. Place the count upper bound and the entropy lower bound around the same squared Fock overlap, with a common normalization convention.
- **Dependencies and story role:** [M01](#m01)–[M13](#m13). Ends the background phase by assembling its local definitions into the global research problem.
- **Sources:** [Theory Sections 1–4](../theory/collective_photon_fidelity.tex), `sec:model`, `sec:wave`, `sec:lower`, `sec:upper`; [Section 7](../theory/collective_photon_fidelity.tex), `sec:attenuation`. Anchor synthesis: Sections II A–C and III; see [BRIDGE.md](BRIDGE.md).
- **Teaching intensity:** 3 rounds.

## Phase II — Narrative/innovation

<a id="m15"></a>
### M15 — A constructive pulse and its variational scope

- **Central question:** Which explicit temporal mode proves an achievable native fidelity of order $N^{-1/2}$?
- **Understanding target:** Follow the normalized pulse, its exact moments, the product relative entropy, and the lower bound at finite $N$. Understand why the quantile formulation makes the entropy minimization pointwise and convex, including the role of the support offset. Separate the rigorously optimal product density for this relative-entropy principle from the still distinct problem of finding the exact fidelity-maximizing mode.
- **Dependencies and story role:** [M12](#m12), [M13](#m13), [M14](#m14). Begins the result narrative with a concrete achievable state and its precise variational claim.
- **Sources:** [Theory Sections 3.2–3.3](../theory/collective_photon_fidelity.tex), `eq:pulse`, `eq:lower`, and “Optimality within the relative-entropy variational principle,” under `sec:lower`.
- **Teaching intensity:** 3 rounds.

<a id="m16"></a>
### M16 — A uniform upper bound from temporal counts

- **Central question:** How can one rule out high fidelity for every possible native trial pulse?
- **Understanding target:** Follow the trial pulse's own median cut, the arrival-density/dwell-time bound on native count probabilities, and the central binomial affinity estimate. Understand why uniformity over the cut makes the bound uniform over $f$. In the improved constant, take $N\to\infty$ with the auxiliary arrival count $K$ fixed before taking $K\to\infty$; do not exchange these limits without a new estimate.
- **Dependencies and story role:** [M09](#m09), [M11](#m11), [M13](#m13), [M14](#m14). Supplies the obstruction that matches the constructive exponent.
- **Sources:** [Theory Sections 4.1–4.3](../theory/collective_photon_fidelity.tex), `sec:upper`, `eq:countfidelity`, and `eq:dwell`.
- **Teaching intensity:** 3 rounds.

<a id="m17"></a>
### M17 — The native fidelity law and its exact two-photon check

- **Central question:** What is now proved about the native source, and what remains undetermined?
- **Understanding target:** Combine the two bounds to obtain $F_N^\star=\Theta(N^{-1/2})$. Interpret $\sqrt{2\pi}$ and $4\sqrt{2\pi}/e$ as lower and upper asymptotic bounding constants, not an identified exact prefactor or bounds at finite $N$. Relate the count mismatch to uncertain startup followed by rapid collective emission. Use the exactly solvable two-photon integral operator and its Bessel-zero result to distinguish the true optimum from a trial value.
- **Dependencies and story role:** [M15](#m15), [M16](#m16). States the central native result before changing the source or adding resources.
- **Sources:** [Theory Section 1, “Fully inverted source” theorem](../theory/collective_photon_fidelity.tex), `eq:main`; [Section 4.4](../theory/collective_photon_fidelity.tex); [Section 6](../theory/collective_photon_fidelity.tex), `sec:two`; [Section 13](../theory/collective_photon_fidelity.tex), `sec:numerics`.
- **Teaching intensity:** 3 rounds.

<a id="m18"></a>
### M18 — The partially excited source and real-parameter family

- **Central question:** Which part of the proof survives when the symmetric ensemble is not fully inverted?
- **Understanding target:** Introduce $M$ emitters, $n$ initial excitations, and $a=M-n+1$. Follow the exact positive kernel, normalized trial density, and product relative entropy. Understand the mathematical extension to real $a\ge1$ with $M=n+a-1$: it is a normalized kernel family, not a source with a fractional number of emitters. This extension later identifies the conditional local-loss state without inventing a new physical preparation.
- **Dependencies and story role:** [M09](#m09), [M15](#m15), [M17](#m17). Makes initial excitation a controlled parameter and prepares the reuse of the proof.
- **Sources:** [Theory Section 5 and Section 5.1](../theory/collective_photon_fidelity.tex), `sec:partial`, `eq:affine`, `eq:trial`, and `eq:D`.
- **Teaching intensity:** 2 rounds.

<a id="m19"></a>
### M19 — The excitation-regime map

- **Central question:** How does the amount of initial inversion change the asymptotic conclusion?
- **Understanding target:** Distinguish the dilute limit $n/M\to0$, a fixed fraction $n/M\to\rho\in(0,1)$, and near inversion $a=o(M)$. Trace the uniform dilute estimate to the convex-order/curvature bound and the uniform near-inversion upper estimate to the Fourier bound on arrival densities. The conclusions are respectively fidelity tending to one, a positive achievable lower bound, and $\Theta(\sqrt{a/M})$. Trial prefactors at fixed $a$ do not identify the exact optimized prefactor.
- **Dependencies and story role:** [M13](#m13), [M16](#m16), [M18](#m18). Organizes the source family into regimes rather than extrapolating the fully inverted law everywhere.
- **Sources:** [Theory Sections 5.2–5.3](../theory/collective_photon_fidelity.tex), `eq:dilutebound`, `eq:dilutefidelity`, `eq:fraction`, theorem `thm:partial`, `eq:realascaling`, `eq:fourierbound`, and `eq:fixedalower`.
- **Teaching intensity:** 3 rounds.

<a id="m20"></a>
### M20 — Uniform attenuation and survivor fidelity

- **Central question:** Does randomly losing photons remove the native modal obstruction?
- **Understanding target:** For mode-independent optical attenuation, derive the binomial sector probability and identify the state conditioned on exactly $k$ surviving photons as the normalized particle reduction of order $k$. Follow the hypergeometric early-count law and its bound. Retain the uniform $O(k^{-1/2})$ ceiling for all $N\ge k\to\infty$, the matching fixed-retained-fraction scaling, and the optimized unconditional number-and-mode yield $\Theta(N^{-1})$ at fixed transmission $\eta\in(0,1)$. This reduction law assumes uniform attenuation.
- **Dependencies and story role:** [M03](#m03), [M08](#m08), [M16](#m16), [M17](#m17). First robustness result, with the channel and sector probability made explicit.
- **Sources:** [Theory Section 7](../theory/collective_photon_fidelity.tex), “Uniform survivor bound” theorem and “Optimize both output photon number and mode” corollary; `eq:binomialloss`, `eq:hypergeom`, `eq:thinningbound`, `eq:survivor`, `eq:rdmlower`, and `eq:anynumber`.
- **Teaching intensity:** 3 rounds.

<a id="m21"></a>
### M21 — Independent local loss and all-photon yield

- **Central question:** What changes when excitations decay locally before contributing to the desired output?
- **Understanding target:** For local jumps $\sqrt{\gamma}\sigma_i^-$ and $\epsilon=\gamma/\Gamma$, identify the sector containing all $N$ desired photons as the sector with no local jumps. Derive its competing-rate product probability and the extra amplitude factor $e^{-\gamma\sum_i t_i/2}$. Map the normalized conditional kernel to $a=1+\epsilon$, $M=N+\epsilon$. At fixed $\epsilon$, distinguish conditional $\Theta(N^{-1/2})$ fidelity from unconditional yield $\Theta(N^{-\epsilon-1/2})$. The product treatment has prior attribution; its modal-fidelity use is the focus here.
- **Dependencies and story role:** [M03](#m03), [M10](#m10), [M18](#m18), [M19](#m19), [M20](#m20). Introduces a physically different loss mechanism and reuses the real-parameter theorem.
- **Sources:** [Theory Section 8](../theory/collective_photon_fidelity.tex), “Exact all-photon sector” proposition and “Conditional scaling and fixed-loss target yield” corollary; `eq:localprob`, `eq:localkernel`, `eq:localconditionalscaling`, `eq:fixedlossyield`, and the Paulisch attribution following the proposition.
- **Teaching intensity:** 3 rounds.

<a id="m22"></a>
### M22 — Strong conditioning and its probability cost

- **Central question:** Can higher conditional single-mode fidelity make local loss a useful unconditional preparation resource?
- **Understanding target:** Track both quantities when $\epsilon$ grows with $N$. For $\epsilon=cN$ with fixed $c>0$, the positive conditional-fidelity lower bound accompanies exponentially small all-photon probability; for $\epsilon/N\to\infty$, conditional fidelity tends to one. A nonvanishing asymptotic conditional fidelity requires $\epsilon=\Omega(N)$ in the native model. The unconditional all-photon target yield is nonincreasing with local loss, while monotonicity of the normalized conditional fidelity is not asserted. A usable herald requires appropriate monitoring or a nondestructive flag.
- **Dependencies and story role:** [M19](#m19), [M21](#m21). Makes the normalization and operational costs of conditioning part of the conclusion.
- **Sources:** [Theory Section 8](../theory/collective_photon_fidelity.tex), “Strong conditioning has an exponential cost” corollary, `eq:strongF` and `eq:strongP`; sector and heralding qualifications in `sec:local`.
- **Teaching intensity:** 2 rounds.

<a id="m23"></a>
### M23 — Consuming a prefix to change the source

- **Central question:** What state remains after a recorded prefix of the native emission is deliberately consumed?
- **Understanding target:** With perfect detection and immediate switching, for $1\le r\lt N$, click number $r$ leaves the symmetric source with $M=N$, $n=N-r$, and $a=r+1$. Align the retained pulse to that recorded click time and obtain the exact partial-source fidelity identity. For $r=0$, use the preparation time. Read $r=o(N)$ as a $\Theta(\sqrt{(r+1)/N})$ resource law and $r/N\to\alpha\in(0,1)$ as permitting a positive achievable fidelity. Count the consumed photons and the timing record as resources; the identity uses every ideal record, without selecting favorable click times.
- **Dependencies and story role:** [M09](#m09), [M18](#m18), [M19](#m19). Converts the partial-source theorem into a specific causal protocol.
- **Sources:** [Theory Section 10, “Prefix identity” proposition](../theory/collective_photon_fidelity.tex), `eq:prefixidentity`, `eq:prefixlaw`, and `eq:prefixfraction`.
- **Teaching intensity:** 2 rounds.

<a id="m24"></a>
### M24 — Detector inefficiency and switching delay

- **Central question:** What is the exact nominal-target penalty for the stated imperfect prefix protocol?
- **Understanding target:** For the ideal native source, take $1\le r\lt N$, detector efficiency $0\lt d\le1$, and delay $\Delta\ge0$. Let registered click number $r$ trigger diversion. Follow the negative-binomial emission-count law truncated by the finite source and the no-emission survival while native emission continues during the fixed delay $\Delta$. Refer the retained pulse to the actual switch time. The nominal $n=N-r$ target has unconditional yield $d^r e^{-\Gamma(N-r)(r+1)\Delta}F^\star_{N,N-r}$; conditioning on a trigger divides by its trigger probability. The $\Gamma N^2\Delta$ scaling requires both consumed and retained fractions to be macroscopic. Keep the exact rate otherwise, and preserve the assumptions of independent detector efficiency, the simple stopping rule, and no added atomic-loss trajectories.
- **Dependencies and story role:** [M03](#m03), [M23](#m23). Adds measurable imperfections to that protocol, without claiming optimality over all record inference or adaptive schemes.
- **Sources:** [Theory Section 10, “Exact nominal-target detection and latency cost” proposition](../theory/collective_photon_fidelity.tex), `eq:prefixcost` and its scope paragraph.
- **Teaching intensity:** 2 rounds.

<a id="m25"></a>
### M25 — Phase controls, common rate shaping, and mode filtering

- **Central question:** Which transformations leave the modal obstruction intact under their stated assumptions?
- **Understanding target:** Use positivity and the triangle inequality to remove diagonal phases, including after fixed-particle tracing. Treat deterministic common rate shaping with complete emission as a one-particle time isometry; optimization is also invariant under lossless one-particle unitaries. Keep the symmetric-ladder restriction visible. Shaping the collective rate with a fixed physical local-loss rate changes the problem. An ideal one-mode filter's all-photon success probability is the overlap it selects, with usable heralding a separate operational requirement.
- **Dependencies and story role:** [M07](#m07), [M10](#m10), [M20](#m20), [M21](#m21). Defines the restricted control class before considering controls that alter rung-dependent amplitudes.
- **Sources:** [Theory Section 9](../theory/collective_photon_fidelity.tex), “Phase removal and scalar rate shaping” proposition, `eq:phaserm` and `eq:isometry`; [Section 9.1](../theory/collective_photon_fidelity.tex), ideal mode filtering.
- **Teaching intensity:** 2 rounds.

<a id="m26"></a>
### M26 — Exact Fock emission from a coherent ladder

- **Central question:** What must a Markov emission ladder satisfy to produce an exact prescribed Fock pulse?
- **Understanding target:** Identify the one-photon hazard $h(t)=|f(t)|^2/[1-\int_0^t|f(s)|^2ds]$ and the required rates $r_m(t)=(N-m)h(t)$. Include the compatible rung phases after diagonal Hamiltonian evolution. Rate equality holds almost everywhere at all reachable times, including pulse gaps; the phase condition applies where $f\ne0$. Recognize the bosonic release construction and its prior foundations. All rungs must couple coherently to the same output channel.
- **Dependencies and story role:** [M05](#m05), [M09](#m09), [M11](#m11), [M25](#m25). Gives a precise constructive escape within a specified control model.
- **Sources:** [Theory Section 11, “Exact Fock criterion within a Markov ladder” theorem](../theory/collective_photon_fidelity.tex), `eq:exactcriterion`, `eq:phase`, and `eq:linearjump`; prior attribution in [Section 14](../theory/collective_photon_fidelity.tex), `sec:discussion`. Anchor connection: Section II A, virtual bosonic pulse source, and Section III A, coherent cascaded modes.
- **Teaching intensity:** 3 rounds.

<a id="m27"></a>
### M27 — The exact-factorization cost under a native-rate cap

- **Central question:** What cost follows if an exactly Fock-factorized lossless release can only attenuate native transition rates?
- **Understanding target:** Under $r_m(t)\le\Gamma(m+1)(N-m)$, use the still-reachable initial rung to infer $h(t)\le\Gamma$. Derive the exact-release mean-time lower bound $H_N/\Gamma$, compared with the native $2H_N/[\Gamma(N+1)]$, where $H_N$ is the harmonic number. With added fixed local loss, this same class of exact lossless-release controls has all-photon probability at most $(1+\epsilon)^{-N}$. The proposition concerns exact factorization; it does not establish a uniform penalty for fidelities approaching one.
- **Dependencies and story role:** [M21](#m21), [M26](#m26). Locates a sharp exact-control restriction whose scope must survive the next milestone.
- **Sources:** [Theory Section 11, “Exact-purity penalty under a native-rate cap” proposition](../theory/collective_photon_fidelity.tex), `eq:ratecap`, `eq:exactslow`, and `eq:nativetime`.
- **Teaching intensity:** 2 rounds.

<a id="m28"></a>
### M28 — Fast emission with asymptotically unit fidelity

- **Central question:** How can fidelity tend to one rapidly under the same rate cap that penalizes exact Fock factorization?
- **Understanding target:** Follow the seed interval, the target's logistic cumulative distribution, and the clipped rung rates. On the good event, target and controlled path amplitudes coincide; its quantifier is $v\in[K/N,1]$. Use the probability estimate at finite $K$ to obtain $F\ge(1-\delta_K)^2$. Choose the smallest even $K\ge24\ln N$. For sufficiently large $N$, this has $K\lt N$ and $K=O(\ln N)$, and yields $F\ge1-O(N^{-3})$ with mean release time $O(\ln N/(\Gamma N))$. Account for both the target tail and the controlled process's residual waiting time.
- **Dependencies and story role:** [M13](#m13), [M16](#m16), [M26](#m26), [M27](#m27). Shows why the exact-factorization penalty cannot be promoted to a uniform restriction on approximate Fock emission.
- **Sources:** [Theory Section 12](../theory/collective_photon_fidelity.tex), “Finite-K fidelity and release-time guarantee” theorem; `eq:cappedcdf`, `eq:cappedrates`, `eq:good`, `eq:deltak`, `eq:cappedtime`, and `eq:cappedasymptotic`.
- **Teaching intensity:** 3 rounds.

<a id="m29"></a>
### M29 — Loss robustness and accepted completion times

- **Central question:** What remains achievable when the capped construction also experiences fixed local loss?
- **Understanding target:** Tilt the target mode by $e^{-\gamma t/2}$, retaining its phase and normalizing with $q(\gamma)=\int e^{-\gamma t}|f(t)|^2dt$. Follow the acceptance bounds, the conditional fidelity bound $(1-\delta_K)^2$, and the inverse-polynomial acceptance guarantee for fixed $\epsilon$ with $K=O(\ln N)$. Use the positive association of independent exponential clock variables to show accepted completion times are stochastically earlier than the lossless controlled times. Keep the all-photon sector's operational heralding requirement distinct from its mathematical conditioning.
- **Dependencies and story role:** [M21](#m21), [M22](#m22), [M28](#m28). Completes the approximate-control result with loss and timing; it proves an achievable guarantee, not an optimal control frontier.
- **Sources:** [Theory Section 12.1](../theory/collective_photon_fidelity.tex), “Loss robustness of the capped construction” theorem and “Accepted completion times are stochastically earlier” lemma; `eq:tiltedmode`, `eq:accbounds`, `eq:lossF`, `eq:polysuccess`, and `eq:acceptedtime`.
- **Teaching intensity:** 3 rounds.

<a id="m30"></a>
### M30 — Synthesis: claims, resources, and implementation scope

- **Central question:** What is the complete scientific story once its source, loss, and control assumptions are stated together?
- **Understanding target:** Explain the native exponent, its excitation dependence, uniform attenuation, native local-loss conditioning, prefix consumption, and restricted phase/rate controls using the same observable conventions. Bring the exact-cap penalty together with the fast approximate construction so neither is overstated. For each preparation claim, name the sector yield, retained photon number, timing reference, and control resource. Distinguish an abstract coherent excitation-dependent jump from measured feedback or independently resolved transition rates; the reference supplies no hardware implementation. Attribute established ingredients and keep numerical trial values within their verified role.
- **Dependencies and story role:** [M14](#m14) and [M15](#m15)–[M29](#m29). Ends the result phase with one coherent account of what the proofs establish and under which physical assumptions.
- **Sources:** [Theory Section 14, “Relation to prior work and physical scope”](../theory/collective_photon_fidelity.tex), `sec:discussion`; [Section 1](../theory/collective_photon_fidelity.tex), `eq:main`; [Sections 5–12](../theory/collective_photon_fidelity.tex), `thm:partial`, `sec:attenuation`, `sec:local`, `sec:phases`, `sec:prefix`, `sec:exact`, and `sec:capped`; [Section 13](../theory/collective_photon_fidelity.tex), `sec:numerics`. Anchor synthesis: Sections II A–C and III, with [BRIDGE.md](BRIDGE.md).
- **Teaching intensity:** 3 rounds.
