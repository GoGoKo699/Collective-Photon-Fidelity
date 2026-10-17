# Collective emission, conditional preparation, and control

The central question concerns the complete emitted state: can one temporal mode contain the entire many-photon pulse as a Fock state? The [model](model.md) defines that overlap, the [native-emission argument](native_emission.md) proves its size dependence, and the remaining pages identify which physical resources change the answer.

## A dominant mode and a complete Fock pulse

A first-order correlation kernel determines the mean occupations of orthogonal temporal modes. A large occupation in one mode is a useful one-body statement. The Fock fidelity instead asks for the overlap of the full state with a target in which every photon occupies that same mode. The [primary literature](../references/RELATED_WORK.md#lemberger) distinguishes these observables, and earlier work already treats [multimode Fock-state overlaps](../references/RELATED_WORK.md#perarnau).

For the native fully inverted source, the emitted wavefunction is positive in symmetric photon-time coordinates but contains correlations between those coordinates. A normalized single-mode Fock target has independent photon times drawn from the same density. Optimizing its envelope cannot remove the correlations of the source.

The two parts of the proof quantify this distinction. The [relative-entropy construction](native_emission.md#sec-lower) supplies an explicit product pulse with squared overlap of order $`N^{-1/2}`$. For the converse, every candidate pulse defines its own median time. The target's count before that time is binomial, whereas each central native-source count probability is bounded by order $`1/N`$, uniformly in the chosen cut. The [count-fidelity argument](native_emission.md#sec-upper), including its tail control, then bounds every candidate mode by the same order.

The result determines an exponent and bounds the possible leading coefficient. It does not identify an exact asymptotic prefactor or the optimal envelope for every photon number. The [two-photon solution](native_emission.md#sec-two) provides a finite case with a certified optimum; numerical trial overlaps have a different role.

## What changes when the source is less inverted

A symmetric $`n`$-excitation Dicke state in $`M`$ emitters has the parameter $`a=M-n+1`$. The same positive density family connects three distinct limits:

| Initial excitation regime | Consequence |
|---|---|
| Near inversion, $`a=o(M)`$ | Optimized fidelity has order $`\sqrt{a/M}`$. |
| Fixed $`n/M\to\rho\in(0,1)`$ | An explicit positive limiting lower bound is available. |
| Dilute excitation, $`n/M\to0`$ | Fidelity tends to one. |

These are statements about a symmetric initial state. The [partial-excitation account](partial_excitation.md) gives the finite formulas, uniform estimates, and real-parameter extension. That extension also describes a conditional local-loss kernel; a real effective emitter parameter is a distributional identity rather than a fractional physical ensemble.

## Loss and a recorded prefix prepare different conditional states

For a photon-number sector with probability $`p_n`$ and normalized state $`\rho_n`$, retain all three quantities:

```math
p_n,\qquad
F^\star(\rho_n)=\sup_{\lVert f\rVert_2=1}\langle n_f|\rho_n|n_f\rangle,
\qquad
Y_n^\star=p_nF^\star(\rho_n).
```

Conditioning changes the state being evaluated; multiplying by the sector probability accounts for its yield per initial preparation.

| Operation | Conditional state and record | Resource consequence |
|---|---|---|
| Uniform attenuation | The normalized $`k`$-photon sector is a reduced state of the ideal field. No record of the discarded photon times is used. | The survivor fidelity retains a $`C/\sqrt{k}`$ ceiling. At fixed $`0\lt\eta\lt1`$, photon-number fluctuations contribute to the optimized unconditional $`\Theta(N^{-1})`$ yield. |
| Independent local atomic decay, conditioned on all desired photons | The accepted histories contain no local jump, and their temporal density differs from the lossless one. | Native-source conditioning at fixed loss ratio retains vanishing fidelity. Making that fidelity bounded away from zero requires a loss ratio at least of order $`N`$, with exponentially small acceptance. |
| Detect and consume a prefix | The final detected time defines a new origin, and the remaining source is a definite symmetric Dicke state. | The protocol trades consumed photons and timing information for higher fidelity of the retained pulse. Its detector and switching costs depend on the stated stopping rule. |

The [attenuation theorem](attenuation.md), [local-loss analysis](local_loss.md), and [prefix law](prefix_detection.md) establish these statements separately. An actual local atomic jump can take the emitters outside the symmetric sector; its fewer-photon output is not generally the reduced ideal state appearing in the attenuation proof.

In the ideal prefix protocol, every timing record is accepted. The target mode is referred to that record. Averaging over unrecorded translations produces a different state, so retaining the time origin is part of the preparation. Similarly, selecting an all-desired-photon sector does not itself supply a nondestructive success flag. A usable herald requires the monitoring or additional information stated for that implementation.

## Why exact and approximate Fock emission have different time costs

Changing a common deterministic clock or adding symmetric diagonal phases does not supply arbitrary control over the amplitudes of the ladder. The [control-restriction result](control_restrictions.md) states the corresponding invariance and phase-removal inequalities, including their reduced-state versions.

For a single coherent Markov output ladder, exact Fock factorization requires

```math
r_m(t)=(N-m)h_f(t),
```

on reachable levels and times, together with compatible trajectory phases. Each remaining excitation then carries the same one-photon hazard. Under the native cap $`r_m(t)\le\Gamma(m+1)(N-m)`$, the [exact criterion and time bound](exact_fock_control.md) force $`h_f(t)\le\Gamma`$ and

```math
\mathbb E T_{\mathrm{last}}^{\mathrm{exact\ Fock}}
\ge\frac{H_N}{\Gamma},
\qquad
\mathbb E T_{\mathrm{last}}^{\mathrm{native}}
=\frac{2H_N}{\Gamma(N+1)}.
```

Here $`H_N=\sum_{j=1}^N1/j`$. The lower bound concerns exact factorization. The [capped coherent construction](capped_control.md) instead matches a fast bosonic reference on complete high-probability histories. It obeys the same instantaneous rate cap while its fidelity approaches one at the native asymptotic time order. The finite-parameter theorem controls the exceptional histories and completion time explicitly.

This construction assumes a coherent excitation-dependent coupling to one output, preserving amplitudes across different emission histories. Engineering separately resolved transition rates is not sufficient: an environmental record of the rung changes the quantum state. The [related-work and physical-scope account](../references/RELATED_WORK.md#higgins) keeps that requirement distinct from established rate engineering and bosonic state-release methods.

At fixed local-loss ratio $`\epsilon=\gamma/\Gamma`$, the stated logarithmic-$`K`$ construction has an inverse-polynomial acceptance guarantee and conditional fidelity approaching one. Its accepted completion-time comparison concerns the duration within an accepted run. Retry throughput and the time needed to obtain a usable herald require the corresponding operational protocol.

## Reading the analytical and numerical evidence together

The full-state optimization bounds follow from explicit inequalities and proofs over their stated domains. The [numerical account](numerical_checks.md) reduces chosen-mode overlaps to an ordered-amplitude recursion, supplies independent benchmarks, and reports a separate analytical truncation budget. The [verification guide](../verification/README.md) gives the commands and actual reference output.

Use a trial overlap as an achievable value for that normalized mode, an exact finite example within its specified case, and a theorem within its stated quantifiers. This keeps the photon-number probability, timing record, mode fidelity, and allowed control resources visible throughout the scientific story.
