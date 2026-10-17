# Thirty milestones for collective photon fidelity

This is the common scientific understanding map for readers and LLMs working with this project. Each milestone identifies a central question, an understanding target, its dependencies, a conceptual connection, and the relevant scientific sources.

The connected scientific account begins with the [model and principal result](../science/model.md). The educational anchor is Alexander Holm Kiilerich and Klaus Mølmer, [*Quantum interactions with pulses of radiation*, Physical Review A **102**, 023717 (2020)](../references/RELATED_WORK.md#kiilerich2020), DOI [10.1103/PhysRevA.102.023717](https://doi.org/10.1103/PhysRevA.102.023717). Read its Sections II A–C and III along the route below; the [bridge guide](BRIDGE.md) connects its notation and pulse formalism to this project.

## Structure and use

**Phase I, background/preliminaries, contains M01–M14.** It moves from the source and one temporal mode through input–output dynamics, several modes, emission trajectories, and the probability tools needed to formulate the global fidelity problem. Fourteen milestones leave room to distinguish the different states and observables before using them in a proof.

**Phase II, narrative/innovation, contains M15–M30.** Its sixteen milestones follow the constructive lower bound and uniform upper bound into excitation regimes, optical and atomic loss, prefix resources, and the boundary between exact and approximate control. Here “innovation” identifies the project's argument and consequences; attribution follows [Related work and physical scope](../references/RELATED_WORK.md#sec-discussion). The additional space is needed because these conclusions depend on different physical assumptions and cannot be folded into one generic robustness claim.

Each phase ends with a synthesis. All milestone dependencies point to earlier milestones. A source pointer may introduce the canonical location where a background concept is later used; that is a reading reference, not an additional prerequisite. Anchor pointers appear where the paper supplies relevant foundations, while the project's theorems link to their authoritative topic pages.

Each conceptual connection explains how the milestone joins prerequisite ideas to the scientific account. The map provides global understanding of the project; detailed proofs and specialist calculations remain in the linked sources.

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
- **Conceptual connection:** One spatial channel fixes where the light propagates; its continuum of emission times still supports a many-mode quantum state. This separates the source geometry from the modal-fidelity question.
- **Sources:** [Model and observables](../science/model.md#sec-model). Anchor: Section II, opening model and input–output assumptions.

<a id="m02"></a>
### M02 — A normalized temporal-mode Fock state

- **Central question:** What does it mean for all $n$ photons to occupy one temporal mode?
- **Understanding target:** Use a normalized complex envelope $f$ with $\int_0^\infty |f(t)|^2dt=1$ to define $a_f^\dagger=\int f(t)b^\dagger(t)dt$ and $|n_f\rangle=(a_f^\dagger)^n|0\rangle/\sqrt{n!}$. Connect the continuum commutator to $[a_f,a_f^\dagger]=1$. Recognize that an overall phase of $f$ changes only the global phase of this fixed-number target.
- **Dependencies and story role:** [M01](#m01). Defines the one-mode target used throughout both phases.
- **Conceptual connection:** Bosonic mode normalization turns a classical envelope into a precise many-photon target and links its product coordinate wavefunction to independent arrival-time statistics.
- **Sources:** [Fock-fidelity definition](../science/model.md#eq-fidelitydef). Anchor: Section II A, normalized pulse and its quantum state.

<a id="m03"></a>
### M03 — Which fidelity and which probability?

- **Central question:** Which observable answers the all-photons-in-one-mode question?
- **Understanding target:** Distinguish squared target overlap $\langle n_f|\rho_n|n_f\rangle$ from overlap amplitude, density-matrix purity, and mean mode occupation. For a normalized fixed-number sector $\rho_n$, keep its probability $p_n$, conditional fidelity $F_{\mathrm{cond}}$, and unconditional target yield $Y=p_nF_{\mathrm{cond}}$ separate. Optimization over $f$ changes the selected mode, not the normalization of the sector.
- **Dependencies and story role:** [M02](#m02). Establishes the quantities that later loss and conditioning results must report.
- **Conceptual connection:** The same prepared field has distinct one-body statistics, fixed-number target overlaps, and preparation probabilities. Their separation gives a common language for every later resource comparison.
- **Sources:** [Model and observables](../science/model.md#sec-model); [Fock-fidelity definition](../science/model.md#eq-fidelitydef). Anchor: Sections II B–C connect mode occupation to the mode's full quantum state.

<a id="m04"></a>
### M04 — Markov input–output dynamics

- **Central question:** How does an open-system jump operator specify radiation entering an output channel?
- **Understanding target:** Connect the Lindblad description, the continuum input–output relation, and the channel-labelled jump operators. Keep a Hamiltonian term, a dissipative channel, and a measurement record conceptually distinct. Understand why combining amplitudes into one coherent output jump differs from treating the same transitions as separately resolved reservoirs.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). Supplies the dynamical language for the virtual source and for the collective emission ladder.
- **Conceptual connection:** The input–output model connects emitter dynamics to field amplitudes. Its channel structure decides which transition alternatives interfere and which leave a distinguishable environmental record.
- **Sources:** [Model and observables](../science/model.md#sec-model); [General coherent ladder](../science/control_restrictions.md#eq-ladder). Anchor: Section II, Eqs. (2)–(3), and Section II A, cascaded dynamics.

<a id="m05"></a>
### M05 — A virtual source for a prescribed pulse

- **Central question:** How can one oscillator represent an incoming quantum pulse with a chosen envelope?
- **Understanding target:** Follow the anchor's virtual-source construction and the relation between the emitted envelope and the oscillator's time-dependent coupling. Track the complex conjugation and the remaining-pulse normalization in that relation. Interpret the construction as a representation of a prescribed quantum input; whether a particular physical emitter generates that pulse is a separate source-dynamics question.
- **Dependencies and story role:** [M02](#m02), [M04](#m04). Introduces pulse synthesis and the survival-hazard idea reused in the exact-control criterion.
- **Conceptual connection:** The prescribed pulse's survival function becomes an instantaneous hazard. The oscillator's linear occupation factor then anticipates the rate criterion for exact Fock emission.
- **Sources:** Anchor: Section II A, especially Eqs. (6)–(9). Project application: [Exact Fock criterion](../science/exact_fock_control.md#eq-exactcriterion); [Bosonic release jump](../science/exact_fock_control.md#eq-linearjump).

<a id="m06"></a>
### M06 — Correlations and mode occupations

- **Central question:** What can first-order field correlations reveal about the emitted pulse?
- **Understanding target:** Interpret the first-order correlation kernel and its mode decomposition: eigenfunctions identify orthogonal temporal modes and eigenvalues give their mean occupations. Relate the largest occupation to an experimentally useful one-body statistic while preserving the distinction from a Fock overlap for $n$ photons. A large fraction in one mode does not by itself certify the probability that every photon occupies that mode.
- **Dependencies and story role:** [M03](#m03), [M04](#m04). Explains why the project asks for more than a dominant-mode calculation.
- **Conceptual connection:** A one-photon correlation operator is a marginal of the full field state. Its most populated eigenmode need not carry a large probability for the complete many-photon target.
- **Sources:** Anchor: Section II B, especially Eq. (15). Project account: [Model and observables](../science/model.md#sec-model); [Related work and physical scope](../references/RELATED_WORK.md#sec-discussion).

<a id="m07"></a>
### M07 — A virtual receiver and the selected-mode state

- **Central question:** How can a calculation access the complete quantum state in one output pulse?
- **Understanding target:** Follow the downstream virtual receiver for a chosen mode and distinguish its accumulated-pulse normalization from the source's remaining-pulse normalization. Identify the receiver state with the one-mode reduced state after tracing over orthogonal output modes. With a fixed total of $n$ photons, its probability for $n$ photons equals the full single-mode target overlap.
- **Dependencies and story role:** [M05](#m05), [M06](#m06). Connects a specified temporal envelope to an operationally meaningful quantum-state observable.
- **Conceptual connection:** The receiver translates a travelling-mode question into an oscillator-state question. Fixed total photon number makes its top number-sector probability equal to the global Fock overlap.
- **Sources:** Anchor: Section II C, especially Eqs. (17)–(19). Project connection: [Control restrictions, including ideal all-photon mode filtering](../science/control_restrictions.md#sec-phases); [Fock-fidelity definition](../science/model.md#eq-fidelitydef).

<a id="m08"></a>
### M08 — Multimode states and two distinct reductions

- **Central question:** Which degrees of freedom are being traced out in a reduced description?
- **Understanding target:** Distinguish a one-mode reduced state, obtained by tracing out other field modes, from a normalized reduced density matrix for $k$ particles of a bosonic state with fixed total photon number $N$. The former has a distribution of photon numbers; the latter describes exactly $k$ particles. Keep both reductions separate from tracing out a residual emitter or a loss reservoir. Mode correlations can survive even when first-order observables look simple.
- **Dependencies and story role:** [M07](#m07). Prepares the reduced-state language needed for uniform attenuation.
- **Conceptual connection:** Tracing modes and tracing particle coordinates preserve different information. This distinction identifies the conditional state produced by uniform attenuation and prevents transferring that identity to unrelated loss channels.
- **Sources:** Anchor: Sections III A–B, joint states of several pulse modes. Project definition: [Uniform attenuation](../science/attenuation.md#sec-attenuation); [Survivor-sector probability](../science/attenuation.md#eq-binomialloss), including the particle-reduction identity following the sector probability.

<a id="m09"></a>
### M09 — The symmetric Dicke emission ladder

- **Central question:** Why does the next collective emission rate depend on how many photons have already left?
- **Understanding target:** Derive the jump amplitudes within the fully symmetric Dicke manifold. After $m$ emissions from full inversion, the physical rate is $\Gamma(m+1)(N-m)$. For a symmetric state of $M$ emitters with $n$ excitations, it is $\Gamma(n-m)(a+m)$ with $a=M-n+1$. Preparing an arbitrary subset of excited emitters does not supply this symmetric initial state.
- **Dependencies and story role:** [M01](#m01), [M04](#m04). Establishes the rate structure whose startup and middle portions later control the fidelity bounds.
- **Conceptual connection:** The two Dicke rate factors connect remaining excitation to collective enhancement. Their variation along the ladder provides the mechanism behind both the startup uncertainty and excitation-dependent fidelity.
- **Sources:** [Exact emitted wavefunction](../science/native_emission.md#sec-wave); [Partial excitation](../science/partial_excitation.md#sec-partial); [Partial-source wavefunction](../science/partial_excitation.md#eq-affine).

<a id="m10"></a>
### M10 — From jump records to a normalized wavefunction

- **Central question:** How do ordered emission times become a symmetric many-photon field amplitude?
- **Understanding target:** Combine no-jump survival amplitudes and jump factors on an ordered time simplex, then recover the symmetric wavefunction. Track the distinction between $\int|\psi_N|^2=1$ on the full time domain and the ordered joint density $N!|\psi_N|^2$. Keep physical time separate from the dimensionless time used in the native proof. Explain why positivity of the native amplitude allows nonnegative trial modes in the optimization.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M09](#m09). Converts emitter dynamics into the normalized field object to which probability arguments apply.
- **Conceptual connection:** Quantum trajectories supply a positive amplitude as well as a classical detection density. Their normalization and symmetrization make probability inequalities applicable to a bosonic overlap.
- **Sources:** [Exact emitted wavefunction](../science/native_emission.md#sec-wave); [Normalized native wavefunction](../science/native_emission.md#eq-wave).

<a id="m11"></a>
### M11 — Temporal counts and the product-state benchmark

- **Central question:** What does a single-mode Fock state predict for the number of early photons?
- **Understanding target:** Relate the factorized coordinate amplitude of $|N_f\rangle$ to independent arrival times with density $|f|^2$, while preserving bosonic symmetrization. An early/late cut then gives a binomial count distribution. Understand how a count measurement bounds quantum fidelity by the squared classical affinity between the two count distributions, without requiring access to every field observable.
- **Dependencies and story role:** [M03](#m03), [M10](#m10). Introduces the experimentally interpretable statistic behind the global upper bound.
- **Conceptual connection:** Product-mode factorization imposes binomial temporal-count fluctuations. Comparing those fluctuations with the collective count process gives a mode-independent obstruction through a simple measurement.
- **Sources:** [Temporal-count fidelity bound](../science/native_emission.md#eq-countfidelity); [Fidelity after count measurement](../science/attenuation.md#eq-measurement).

<a id="m12"></a>
### M12 — Affinity and relative entropy

- **Central question:** How can a positive many-photon amplitude produce a constructive fidelity bound?
- **Understanding target:** With $P_N=|\psi_N|^2$ and $Q_p=p^{\otimes N}$, identify the overlap amplitude with the classical affinity $\int\sqrt{P_NQ_p}$. Apply Jensen's inequality to obtain the squared-overlap bound $F_N[\sqrt p]\ge e^{-D(Q_p\Vert P_N)}$. Preserve the direction $Q_p\Vert P_N$ and distinguish optimizing this entropy bound from optimizing the original fidelity functional.
- **Dependencies and story role:** [M03](#m03), [M10](#m10). Supplies the second proof tool, complementary to the count measurement.
- **Conceptual connection:** Positivity converts the quantum overlap into classical affinity, and relative entropy supplies a computable lower bound for a chosen pulse without solving the original optimization problem.
- **Sources:** [Affinity and relative entropy](../science/native_emission.md#eq-kl); variational scope in [Constructive lower bound](../science/native_emission.md#sec-lower).

<a id="m13"></a>
### M13 — Asymptotic statements and numerical evidence

- **Central question:** What does each kind of calculation actually establish?
- **Understanding target:** Read finite-size inequalities, $O$ and $\Theta$ statements, fixed-ratio limits, and liminf/limsup bounds with their quantifiers intact. Distinguish an achievable trial overlap from the optimized fidelity. Understand the role of normalization checks, independent quadrature, and explicit truncation errors in testing formulas; those checks do not replace uniform estimates or establish an asymptotic prefactor.
- **Dependencies and story role:** [M10](#m10), [M11](#m11), [M12](#m12). Sets the evidential standard for interpreting every result in Phase II.
- **Conceptual connection:** An achievable pulse, a finite bound, and a uniform asymptotic law answer different questions. Explicit quantifiers connect numerical consistency to the claims that require analytical proof.
- **Sources:** [Native fidelity theorem](../science/model.md#eq-main); [Numerical consistency checks](../science/numerical_checks.md#sec-numerics); [Ordered-integral recursion](../science/numerical_checks.md#eq-recursion). Reproducible implementation: [verification/check_fidelity.py](../verification/check_fidelity.py) and [verification/fidelity.py](../verification/fidelity.py).

<a id="m14"></a>
### M14 — Synthesis: from source to a testable field question

- **Central question:** How do the physical model, pulse formalism, and probability tools fit into one fidelity question?
- **Understanding target:** Connect the chain from source preparation through channel-labelled dynamics and the normalized emitted wavefunction to a selected temporal-mode target. Explain which information comes from first-order correlations, a one-mode state, a particle reduction, and a temporal-count measurement. Place the count upper bound and the entropy lower bound around the same squared Fock overlap, with a common normalization convention.
- **Dependencies and story role:** [M01](#m01)–[M13](#m13). Ends the background phase by assembling its local definitions into the global research problem.
- **Conceptual connection:** The field conventions, source dynamics, and two probability tools now address one normalized target quantity. This common framework is what lets later changes in excitation, loss, and control be compared.
- **Sources:** [Model and observables](../science/model.md#sec-model); [Exact emitted wavefunction](../science/native_emission.md#sec-wave); [Constructive lower bound](../science/native_emission.md#sec-lower); [Uniform count upper bound](../science/native_emission.md#sec-upper); [Uniform attenuation](../science/attenuation.md#sec-attenuation). Anchor synthesis: Sections II A–C and III; see [BRIDGE.md](BRIDGE.md).

## Phase II — Narrative/innovation

<a id="m15"></a>
### M15 — A constructive pulse and its variational scope

- **Central question:** Which explicit temporal mode proves an achievable native fidelity of order $N^{-1/2}$?
- **Understanding target:** Follow the normalized pulse, its exact moments, the product relative entropy, and the lower bound at finite $N$. Understand why the quantile formulation makes the entropy minimization pointwise and convex, including the role of the support offset. Separate the rigorously optimal product density for this relative-entropy principle from the still distinct problem of finding the exact fidelity-maximizing mode.
- **Dependencies and story role:** [M12](#m12), [M13](#m13), [M14](#m14). Begins the result narrative with a concrete achievable state and its precise variational claim.
- **Conceptual connection:** The explicit pulse connects a tractable entropy variational problem to a guaranteed many-photon overlap. The distinction between these objectives explains both the strength and the limit of the construction.
- **Sources:** [Native trial pulse](../science/native_emission.md#eq-pulse); [Finite native lower bound](../science/native_emission.md#eq-lower); product relative-entropy optimality in [Constructive lower bound](../science/native_emission.md#sec-lower).

<a id="m16"></a>
### M16 — A uniform upper bound from temporal counts

- **Central question:** How can one rule out high fidelity for every possible native trial pulse?
- **Understanding target:** Follow the trial pulse's own median cut, the arrival-density/dwell-time bound on native count probabilities, and the central binomial affinity estimate. Understand why uniformity over the cut makes the bound uniform over $f$. In the improved constant, take $N\to\infty$ with the auxiliary arrival count $K$ fixed before taking $K\to\infty$; do not exchange these limits without a new estimate.
- **Dependencies and story role:** [M09](#m09), [M11](#m11), [M13](#m13), [M14](#m14). Supplies the obstruction that matches the constructive exponent.
- **Conceptual connection:** The collective waiting-time model bounds count probabilities uniformly in time. Choosing each target's own median transfers that uniformity to optimization over every temporal mode.
- **Sources:** [Uniform count upper bound](../science/native_emission.md#sec-upper); [Temporal-count fidelity bound](../science/native_emission.md#eq-countfidelity); [Arrival-density and dwell-time bound](../science/native_emission.md#eq-dwell).

<a id="m17"></a>
### M17 — The native fidelity law and its exact two-photon check

- **Central question:** What is now proved about the native source, and what remains undetermined?
- **Understanding target:** Combine the two bounds to obtain $F_N^\star=\Theta(N^{-1/2})$. Interpret $\sqrt{2\pi}$ and $4\sqrt{2\pi}/e$ as lower and upper asymptotic bounding constants, not an identified exact prefactor or bounds at finite $N$. Relate the count mismatch to uncertain startup followed by rapid collective emission. Use the exactly solvable two-photon integral operator and its Bessel-zero result to distinguish the true optimum from a trial value.
- **Dependencies and story role:** [M15](#m15), [M16](#m16). States the central native result before changing the source or adding resources.
- **Conceptual connection:** Matching constructive and obstructive exponents turns the source's timing correlations into a precise fidelity law. The exact two-photon example illustrates why a good trial pulse need not be the optimizer.
- **Sources:** [Native fidelity theorem](../science/model.md#eq-main); [Uniform count upper bound](../science/native_emission.md#sec-upper); [Exact two-photon optimum](../science/native_emission.md#sec-two); [Numerical consistency checks](../science/numerical_checks.md#sec-numerics).

<a id="m18"></a>
### M18 — The partially excited source and real-parameter family

- **Central question:** Which part of the proof survives when the symmetric ensemble is not fully inverted?
- **Understanding target:** Introduce $M$ emitters, $n$ initial excitations, and $a=M-n+1$. Follow the exact positive kernel, normalized trial density, and product relative entropy. Understand the mathematical extension to real $a\ge1$ with $M=n+a-1$: it is a normalized kernel family, not a source with a fractional number of emitters. This extension later identifies the conditional local-loss state without inventing a new physical preparation.
- **Dependencies and story role:** [M09](#m09), [M15](#m15), [M17](#m17). Makes initial excitation a controlled parameter and prepares the reuse of the proof.
- **Conceptual connection:** The same positive-kernel family describes partial excitation and normalized no-local-loss histories. Extending its parameter continuously joins these physical questions without changing the actual emitter count.
- **Sources:** [Partial excitation](../science/partial_excitation.md#sec-partial); [Partial-source wavefunction](../science/partial_excitation.md#eq-affine); [Partial-source trial mode](../science/partial_excitation.md#eq-trial); [Product relative entropy](../science/partial_excitation.md#eq-d).

<a id="m19"></a>
### M19 — The excitation-regime map

- **Central question:** How does the amount of initial inversion change the asymptotic conclusion?
- **Understanding target:** Distinguish the dilute limit $n/M\to0$, a fixed fraction $n/M\to\rho\in(0,1)$, and near inversion $a=o(M)$. Trace the uniform dilute estimate to the convex-order/curvature bound and the uniform near-inversion upper estimate to the Fourier bound on arrival densities. The conclusions are respectively fidelity tending to one, a positive achievable lower bound, and $\Theta(\sqrt{a/M})$. Trial prefactors at fixed $a$ do not identify the exact optimized prefactor.
- **Dependencies and story role:** [M13](#m13), [M16](#m16), [M18](#m18). Organizes the source family into regimes rather than extrapolating the fully inverted law everywhere.
- **Conceptual connection:** The initial excitation deficit changes the startup part of the ladder and the resulting count concentration. Keeping each limit explicit explains how dilute emission, fixed fractions, and near inversion fit together.
- **Sources:** [Uniform dilute entropy bound](../science/partial_excitation.md#eq-dilutebound); [Dilute-source fidelity](../science/partial_excitation.md#eq-dilutefidelity); [Fixed-fraction lower bound](../science/partial_excitation.md#eq-fraction); [Real-parameter fidelity theorem](../science/partial_excitation.md#thm-partial); [Near-inversion scaling](../science/partial_excitation.md#eq-realascaling); [Uniform arrival-density estimate](../science/partial_excitation.md#eq-fourierbound); [Fixed-parameter achievable asymptotic](../science/partial_excitation.md#eq-fixedalower).

<a id="m20"></a>
### M20 — Uniform attenuation and survivor fidelity

- **Central question:** Does randomly losing photons remove the native modal obstruction?
- **Understanding target:** For mode-independent optical attenuation, derive the binomial sector probability and identify the state conditioned on exactly $k$ surviving photons as the normalized particle reduction of order $k$. Follow the hypergeometric early-count law and its bound. Retain the uniform $O(k^{-1/2})$ ceiling for all $N\ge k\to\infty$, the matching fixed-retained-fraction scaling, and the optimized unconditional number-and-mode yield $\Theta(N^{-1})$ at fixed transmission $\eta\in(0,1)$. This reduction law assumes uniform attenuation.
- **Dependencies and story role:** [M03](#m03), [M08](#m08), [M16](#m16), [M17](#m17). First robustness result, with the channel and sector probability made explicit.
- **Conceptual connection:** Unobserved photon removal acts on particle coordinates rather than on the prepared source or its recorded time origin. The survivor bound therefore separates attenuation from deliberate prefix consumption.
- **Sources:** [Uniform attenuation](../science/attenuation.md#sec-attenuation); [Survivor-sector probability](../science/attenuation.md#eq-binomialloss); [Hypergeometric temporal counts](../science/attenuation.md#eq-hypergeom); [Uniform thinned-count bound](../science/attenuation.md#eq-thinningbound); [Uniform survivor theorem](../science/attenuation.md#eq-survivor); [Reduced-state lower bound](../science/attenuation.md#eq-rdmlower); [Optimized number-and-mode yield](../science/attenuation.md#eq-anynumber).

<a id="m21"></a>
### M21 — Independent local loss and all-photon yield

- **Central question:** What changes when excitations decay locally before contributing to the desired output?
- **Understanding target:** For local jumps $\sqrt{\gamma}\sigma_i^-$ and $\epsilon=\gamma/\Gamma$, identify the sector containing all $N$ desired photons as the sector with no local jumps. Derive its competing-rate product probability and the extra amplitude factor $e^{-\gamma\sum_i t_i/2}$. Map the normalized conditional kernel to $a=1+\epsilon$, $M=N+\epsilon$. At fixed $\epsilon$, distinguish conditional $\Theta(N^{-1/2})$ fidelity from unconditional yield $\Theta(N^{-\epsilon-1/2})$. The product treatment has prior attribution; its modal-fidelity use is the focus here.
- **Dependencies and story role:** [M03](#m03), [M10](#m10), [M18](#m18), [M19](#m19), [M20](#m20). Introduces a physically different loss mechanism and reuses the real-parameter theorem.
- **Conceptual connection:** A no-local-jump history reweights the full temporal amplitude while the competing jump rates determine its occurrence probability. Their combination yields conditional quality and unconditional success separately.
- **Sources:** [Independent local loss](../science/local_loss.md#sec-local); [No-local-loss probability](../science/local_loss.md#eq-localprob); [Conditional local-loss kernel](../science/local_loss.md#eq-localkernel); [Conditional scaling](../science/local_loss.md#eq-localconditionalscaling); [Fixed-loss target yield](../science/local_loss.md#eq-fixedlossyield); [Paulisch attribution](../references/RELATED_WORK.md#paulisch).

<a id="m22"></a>
### M22 — Strong conditioning and its probability cost

- **Central question:** Can higher conditional single-mode fidelity make local loss a useful unconditional preparation resource?
- **Understanding target:** Track both quantities when $\epsilon$ grows with $N$. For $\epsilon=cN$ with fixed $c>0$, the positive conditional-fidelity lower bound accompanies exponentially small all-photon probability; for $\epsilon/N\to\infty$, conditional fidelity tends to one. A nonvanishing asymptotic conditional fidelity requires $\epsilon=\Omega(N)$ in the native model. The unconditional all-photon target yield is nonincreasing with local loss, while monotonicity of the normalized conditional fidelity is not asserted. A usable herald requires appropriate monitoring or a nondestructive flag.
- **Dependencies and story role:** [M19](#m19), [M21](#m21). Makes the normalization and operational costs of conditioning part of the conclusion.
- **Conceptual connection:** Normalization can amplify the fidelity of a rare sector. Keeping its probability alongside its state exposes the preparation cost and the distinction between conditional improvement and useful yield.
- **Sources:** [Strong-conditioning fidelity](../science/local_loss.md#eq-strongf); [Strong-conditioning probability](../science/local_loss.md#eq-strongp); sector, monotonicity, and heralding qualifications in [Independent local loss](../science/local_loss.md#sec-local).

<a id="m23"></a>
### M23 — Consuming a prefix to change the source

- **Central question:** What state remains after a recorded prefix of the native emission is deliberately consumed?
- **Understanding target:** With perfect detection and immediate switching, for $1\le r\lt N$, click number $r$ leaves the symmetric source with $M=N$, $n=N-r$, and $a=r+1$. Align the retained pulse to that recorded click time and obtain the exact partial-source fidelity identity. For $r=0$, use the preparation time. Read $r=o(N)$ as a $\Theta(\sqrt{(r+1)/N})$ resource law and $r/N\to\alpha\in(0,1)$ as permitting a positive achievable fidelity. Count the consumed photons and the timing record as resources; the identity uses every ideal record, without selecting favorable click times.
- **Dependencies and story role:** [M09](#m09), [M18](#m18), [M19](#m19). Converts the partial-source theorem into a specific causal protocol.
- **Conceptual connection:** A detected prefix changes the remaining Dicke rung and supplies a causal timing reference. Those two resources explain the exact connection to a partially excited source.
- **Sources:** [Prefix identity](../science/prefix_detection.md#eq-prefixidentity); [Sublinear-prefix resource law](../science/prefix_detection.md#eq-prefixlaw); [Fractional-prefix lower bound](../science/prefix_detection.md#eq-prefixfraction).

<a id="m24"></a>
### M24 — Detector inefficiency and switching delay

- **Central question:** What is the exact nominal-target penalty for the stated imperfect prefix protocol?
- **Understanding target:** For the ideal native source, take $1\le r\lt N$, detector efficiency $0\lt d\le1$, and delay $\Delta\ge0$. Let registered click number $r$ trigger diversion. Follow the negative-binomial emission-count law truncated by the finite source and the no-emission survival while native emission continues during the fixed delay $\Delta$. Refer the retained pulse to the actual switch time. The nominal $n=N-r$ target has unconditional yield $d^r e^{-\Gamma(N-r)(r+1)\Delta}F^\star_{N,N-r}$; conditioning on a trigger divides by its trigger probability. The $\Gamma N^2\Delta$ scaling requires both consumed and retained fractions to be macroscopic. Keep the exact rate otherwise, and preserve the assumptions of independent detector efficiency, the simple stopping rule, and no added atomic-loss trajectories.
- **Dependencies and story role:** [M03](#m03), [M23](#m23). Adds measurable imperfections to that protocol, without claiming optimality over all record inference or adaptive schemes.
- **Conceptual connection:** Missed detections and emissions during switching can move an attempt out of the nominal target-number sector. Their probabilities give the stated penalty without changing the conditional modal calculation.
- **Sources:** [Nominal-target detection and latency cost](../science/prefix_detection.md#eq-prefixcost) and the protocol scope in [Prefix detection](../science/prefix_detection.md#sec-prefix).

<a id="m25"></a>
### M25 — Phase controls, common rate shaping, and mode filtering

- **Central question:** Which transformations leave the modal obstruction intact under their stated assumptions?
- **Understanding target:** Use positivity and the triangle inequality to remove diagonal phases, including after fixed-particle tracing. Treat deterministic common rate shaping with complete emission as a one-particle time isometry; optimization is also invariant under lossless one-particle unitaries. Keep the symmetric-ladder restriction visible. Shaping the collective rate with a fixed physical local-loss rate changes the problem. An ideal one-mode filter's all-photon success probability is the overlap it selects, with usable heralding a separate operational requirement.
- **Dependencies and story role:** [M07](#m07), [M10](#m10), [M20](#m20), [M21](#m21). Defines the restricted control class before considering controls that alter rung-dependent amplitudes.
- **Conceptual connection:** Phase changes, clock changes, and lossless mode transformations act within a restricted class of field descriptions. Excitation-dependent changes to jump magnitudes alter the ladder itself and require a different analysis.
- **Sources:** [Control restrictions](../science/control_restrictions.md#sec-phases); [Phase-removal inequality](../science/control_restrictions.md#eq-phaserm); [Common-rate time isometry](../science/control_restrictions.md#eq-isometry), including ideal all-photon mode filtering.

<a id="m26"></a>
### M26 — Exact Fock emission from a coherent ladder

- **Central question:** What must a Markov emission ladder satisfy to produce an exact prescribed Fock pulse?
- **Understanding target:** Identify the one-photon hazard $h(t)=|f(t)|^2/[1-\int_0^t|f(s)|^2ds]$ and the required rates $r_m(t)=(N-m)h(t)$. Include the compatible rung phases after diagonal Hamiltonian evolution. Rate equality holds almost everywhere at all reachable times, including pulse gaps; the phase condition applies where $f\ne0$. Recognize the bosonic release construction and its prior foundations. All rungs must couple coherently to the same output channel.
- **Dependencies and story role:** [M05](#m05), [M09](#m09), [M11](#m11), [M25](#m25). Gives a precise constructive escape within a specified control model.
- **Conceptual connection:** Independent target arrival times force a rate proportional to the number of remaining photons. This connects the virtual oscillator, order statistics, and the coherent-ladder criterion.
- **Sources:** [Exact Fock criterion](../science/exact_fock_control.md#eq-exactcriterion); [Compatible ladder phases](../science/exact_fock_control.md#eq-phase); [Bosonic release jump](../science/exact_fock_control.md#eq-linearjump); [Related work and physical scope](../references/RELATED_WORK.md#sec-discussion). Anchor connection: Section II A, virtual bosonic pulse source, and Section III A, coherent cascaded modes.

<a id="m27"></a>
### M27 — The exact-factorization cost under a native-rate cap

- **Central question:** What cost follows if an exactly Fock-factorized lossless release can only attenuate native transition rates?
- **Understanding target:** Under $r_m(t)\le\Gamma(m+1)(N-m)$, use the still-reachable initial rung to infer $h(t)\le\Gamma$. Derive the exact-release mean-time lower bound $H_N/\Gamma$, compared with the native $2H_N/[\Gamma(N+1)]$, where $H_N$ is the harmonic number. With added fixed local loss, this same class of exact lossless-release controls has all-photon probability at most $(1+\epsilon)^{-N}$. The proposition concerns exact factorization; it does not establish a uniform penalty for fidelities approaching one.
- **Dependencies and story role:** [M21](#m21), [M26](#m26). Locates a sharp exact-control restriction whose scope must survive the next milestone.
- **Conceptual connection:** Exact factorization constrains every reachable rung, including the initial bottleneck. That global requirement turns the native cap into both a release-time cost and a local-loss survival cost.
- **Sources:** [Native-rate cap](../science/exact_fock_control.md#eq-ratecap); [Exact-factorization time and loss costs](../science/exact_fock_control.md#eq-exactslow); [Native mean release time](../science/exact_fock_control.md#eq-nativetime).

<a id="m28"></a>
### M28 — Fast emission with asymptotically unit fidelity

- **Central question:** How can fidelity tend to one rapidly under the same rate cap that penalizes exact Fock factorization?
- **Understanding target:** Follow the seed interval, the target's logistic cumulative distribution, and the clipped rung rates. On the good event, target and controlled path amplitudes coincide; its quantifier is $v\in[K/N,1]$. Use the probability estimate at finite $K$ to obtain $F\ge(1-\delta_K)^2$. Choose the smallest even $K\ge24\ln N$. For sufficiently large $N$, this has $K\lt N$ and $K=O(\ln N)$, and yields $F\ge1-O(N^{-3})$ with mean release time $O(\ln N/(\Gamma N))$. Account for both the target tail and the controlled process's residual waiting time.
- **Dependencies and story role:** [M13](#m13), [M16](#m16), [M26](#m26), [M27](#m27). Shows why the exact-factorization penalty cannot be promoted to a uniform restriction on approximate Fock emission.
- **Conceptual connection:** High fidelity permits a controlled mismatch on a low-probability set of trajectories. The good-event argument joins the rate cap to rapid collective release without imposing exact factorization everywhere.
- **Sources:** [Capped coherent control](../science/capped_control.md#sec-capped); [Target cumulative distribution](../science/capped_control.md#eq-cappedcdf); [Clipped coherent rates](../science/capped_control.md#eq-cappedrates); [Good-event definition](../science/capped_control.md#eq-good); [Finite-K error bound](../science/capped_control.md#eq-deltak); [Mean release-time bound](../science/capped_control.md#eq-cappedtime); [Fast asymptotically unit fidelity](../science/capped_control.md#eq-cappedasymptotic).

<a id="m29"></a>
### M29 — Loss robustness and accepted completion times

- **Central question:** What remains achievable when the capped construction also experiences fixed local loss?
- **Understanding target:** Tilt the target mode by $e^{-\gamma t/2}$, retaining its phase and normalizing with $q(\gamma)=\int e^{-\gamma t}|f(t)|^2dt$. Follow the acceptance bounds, the conditional fidelity bound $(1-\delta_K)^2$, and the inverse-polynomial acceptance guarantee for fixed $\epsilon$ with $K=O(\ln N)$. Use the positive association of independent exponential clock variables to show accepted completion times are stochastically earlier than the lossless controlled times. Keep the all-photon sector's operational heralding requirement distinct from its mathematical conditioning.
- **Dependencies and story role:** [M21](#m21), [M22](#m22), [M28](#m28). Completes the approximate-control result with loss and timing; it proves an achievable guarantee, not an optimal control frontier.
- **Conceptual connection:** Loss tilts the target's time distribution and suppresses long histories. Positive association of the independent clock variables connects that weighting to both acceptance bounds and earlier accepted completion times.
- **Sources:** [Loss-tilted mode](../science/capped_control.md#eq-tiltedmode); [Acceptance bounds](../science/capped_control.md#eq-accbounds); [Conditional fidelity bound](../science/capped_control.md#eq-lossf); [Polynomial acceptance guarantee](../science/capped_control.md#eq-polysuccess); [Accepted completion times](../science/capped_control.md#eq-acceptedtime), with the loss-robustness theorem and accepted-time proof in [Capped coherent control](../science/capped_control.md#sec-capped).

<a id="m30"></a>
### M30 — Synthesis: claims, resources, and implementation scope

- **Central question:** What is the complete scientific story once its source, loss, and control assumptions are stated together?
- **Understanding target:** Explain the native exponent, its excitation dependence, uniform attenuation, native local-loss conditioning, prefix consumption, and restricted phase/rate controls using the same observable conventions. Bring the exact-cap penalty together with the fast approximate construction so neither is overstated. For each preparation claim, name the sector yield, retained photon number, timing reference, and control resource. Distinguish an abstract coherent excitation-dependent jump from measured feedback or independently resolved transition rates; the reference supplies no hardware implementation. Attribute established ingredients and keep numerical trial values within their verified role.
- **Dependencies and story role:** [M14](#m14) and [M15](#m15)–[M29](#m29). Ends the result phase with one coherent account of what the proofs establish and under which physical assumptions.
- **Conceptual connection:** A source protocol is specified by its state, accepted sector, photon cost, timing information, and coherent control. Combining those specifications produces the complete comparison while preserving each theorem's domain.
- **Sources:** [Related work and physical scope](../references/RELATED_WORK.md#sec-discussion); [Native fidelity theorem](../science/model.md#eq-main); [Real-parameter fidelity theorem](../science/partial_excitation.md#thm-partial); [Uniform attenuation](../science/attenuation.md#sec-attenuation); [Independent local loss](../science/local_loss.md#sec-local); [Control restrictions](../science/control_restrictions.md#sec-phases); [Prefix detection](../science/prefix_detection.md#sec-prefix); [Exact Fock control](../science/exact_fock_control.md#sec-exact); [Capped coherent control](../science/capped_control.md#sec-capped); [Numerical consistency checks](../science/numerical_checks.md#sec-numerics). Anchor synthesis: Sections II A–C and III, with [BRIDGE.md](BRIDGE.md).
