<a id="sec-discussion"></a>
# Related work and physical scope

The collective rate ladder, multiphoton wavefunction, and multimode character of Dicke emission are established background. This account identifies the imported ingredients, distinguishes the observables and physical models used in nearby work, and states the scope of the [project's fidelity results](../science/model.md). Citation keys in square brackets match the structured [bibliography](references.bib).

The central quantity is the optimized probability that the complete emitted field occupies a single temporal-mode Fock state. A dominant one-photon occupation, a conditional state's fidelity, and the unconditional probability of preparing that target answer different questions. The [model and observable definitions](../science/model.md#eq-fidelitydef) keep these quantities separate.

## Collective emission and the full propagating state

<a id="paulisch"></a>
### Collective waveguide emission and loss

**V. Paulisch, M. Perarnau-Llobet, A. González-Tudela, and J. I. Cirac, “Quantum metrology with one-dimensional superradiant photonic states,” Physical Review A 99, 043807 (2019)** [paulisch]. [Primary preprint](https://arxiv.org/abs/1805.00712).

Paulisch and collaborators analyze superradiant photonic states and their metrological usefulness. The collective ladder, trajectory construction, and competing collective/local-decay rates are established ingredients. Their [main Eq. (7)](https://arxiv.org/html/1805.00712v2) gives the weak-loss product approximation, while the supplemental competing-rate dynamics (SM25–SM35) yield the exact no-local-loss branching product used here. The [local-loss account](../science/local_loss.md#eq-localprob) uses that sector probability together with a separate analysis of its normalized modal fidelity.

<a id="perarnau"></a>
### Multimode multiphoton Fock states

**M. Perarnau-Llobet, A. González-Tudela, and J. I. Cirac, “Multimode Fock states with large photon number: effective descriptions and applications in quantum metrology,” Quantum Science and Technology 5, 025003 (2020)** [perarnau]. [Primary preprint](https://arxiv.org/abs/1910.03323), especially Section IV D and Appendix I E.

This work develops efficient observables and explicit few-mode Fock decompositions of collective photonic states. Complete multiphoton structure and Fock-state overlaps therefore already have a literature; the present contribution is the set of quantitative bounds and resource laws proved for the stated source, loss, and control models.

<a id="tziperman"></a>
### Finite-size Fock fidelities of collective emission

**O. Tziperman et al., “Nonlinear quantum light generation in collective spontaneous emission,” ACS Nano 19, 21260–21270 (2025)** [tziperman]. [Publisher](https://doi.org/10.1021/acsnano.4c15257), [primary preprint, under its earlier title](https://arxiv.org/abs/2306.11348).

Tziperman and collaborators study complete propagating quantum states and finite-size single-mode Fock fidelities, including direct collective decay. This is prior work on the full target-state observable. The [native theorem](../science/model.md#eq-main) provides a uniform asymptotic conclusion and explicit bounding constants; the [numerical checks](../science/numerical_checks.md) evaluate specified modes within that analytical framework.

<a id="lemberger"></a>
### One-photon temporal-mode occupations

**B. Lemberger and K. Mølmer, “Radiation eigenmodes of Dicke superradiance,” Physical Review A 103, 033713 (2021)** [lemberger]. [Primary preprint](https://arxiv.org/abs/2009.11687).

This work studies the one-photon temporal modes and finds a dominant occupation above 90 percent. That occupation fraction does not determine the optimized probability that all photons share one mode. The [educational bridge](../learning/BRIDGE.md#4-a-populated-mode-and-a-fock-state-are-different-claims) gives an explicit example of states with the same first-order correlations and different overlaps with a chosen Fock target.

<a id="malz"></a>
### Large-ensemble population dynamics

**D. Malz, R. Trivedi, and J. I. Cirac, “Large-$`N`$ limit of Dicke superradiance,” Physical Review A 106, 013716 (2022)** [malz]. [Primary preprint](https://arxiv.org/abs/2202.05197).

Malz, Trivedi, and Cirac establish the large-$`N`$ Dicke population dynamics. The [temporal-count proof](../science/native_emission.md#sec-upper) starts from the same collective rate model and proves a uniform arrival-density bound suitable for bounding fidelity over every trial pulse.

## Distinct state-preparation regimes and mode objectives

<a id="liu"></a>
### Weakly excited superradiant sources

**Q. Liu and J.-T. Shen, “Photonic Fock state generation using superradiance,” Optics Letters 47, 4576–4579 (2022)** [liu]. [Publisher](https://doi.org/10.1364/OL.468481).

Liu and Shen's weak-excitation Fock-generation regime is consistent with the [dilute symmetric-source bounds](../science/partial_excitation.md#eq-dilutefidelity). Excitation density is an essential part of the comparison: a weakly excited symmetric ensemble and a fully inverted ensemble occupy different limits of the collective ladder.

<a id="yadav"></a>
### A discrete radiation oscillator

**A. Yadav and D. D. Yavuz, “Quantum statistics of single-mode radiation emitted by superradiant Dicke states,” arXiv:2508.09962 (2025)** [yadav]. [Primary preprint](https://arxiv.org/abs/2508.09962).

This work uses the discrete cavity-mode Tavis–Cummings setting. Its single radiation oscillator defines a different output problem from a propagating Markov channel with a continuum of temporal modes. A single spatial channel in the [native model](../science/model.md#sec-model) does not restrict that continuum to one temporal mode.

<a id="belliardo"></a>
### Temporal modes for information extraction

**F. Belliardo, A. Chu, M. Koppenhöfer, and A. A. Clerk, “Extracting information from a superradiant burst using simple measurements,” arXiv:2603.13130v2 (31 March 2026)** [belliardo]. [Primary preprint, version 2](https://arxiv.org/abs/2603.13130v2).

Belliardo and collaborators optimize temporal modes for extracting information from a superradiant burst. An information-optimal mode can contain a vanishing fraction of the photons. A task-optimal mode therefore need not be the most occupied one-photon mode, and neither objective is the complete Fock-target probability studied here.

<a id="holdaway"></a>
### Center-of-mass uncertainty and a many-body overlap

**D. I. H. Holdaway, C. Weiss, and S. A. Gardiner, “Quantum theory of bright matter-wave solitons in harmonic confinement,” Physical Review A 85, 053618 (2012)** [holdaway]. [Primary preprint](https://arxiv.org/abs/1203.6006), especially Section V C.

Quantum-soliton analyses describe how center-of-mass delocalization can suppress a many-body Hartree overlap even when its $`N`$th root stays close to one. That root is distinct from a one-photon occupation or a reduced-state fidelity. The pair-distance factor in the [native photon wavefunction](../science/native_emission.md#eq-wave) makes this comparison relevant, while the source dynamics and the observables must retain their own definitions.

## Established preparation and release mechanisms

<a id="gough"></a>
### Shaped bosonic input synthesis

**J. E. Gough and G. Zhang, “Generating nonclassical quantum input field states with modulating filters,” EPJ Quantum Technology 2, 15 (2015)** [gough]. [Publisher](https://doi.org/10.1140/epjqt/s40507-015-0027-z).

Shaped bosonic input synthesis, including the release of a prescribed Fock pulse, is an established construction. The [exact coherent-ladder criterion](../science/exact_fock_control.md#eq-exactcriterion) states the compatible rates and phases explicitly and makes the role of the native Dicke matrix elements and their rate cap visible.

<a id="brown"></a>
### Deterministic optical Fock-state preparation

**K. R. Brown, K. M. Dani, D. M. Stamper-Kurn, and K. B. Whaley, “Deterministic optical Fock-state generation,” Physical Review A 67, 043818 (2003)** [brown]. [Publisher](https://doi.org/10.1103/PhysRevA.67.043818), [primary preprint](https://arxiv.org/abs/quant-ph/0211134).

Deterministic optical Fock preparation and coherent cavity loading are prior state-preparation mechanisms. Their availability emphasizes that restrictions on native collective emission are statements about a specified source and allowed operations.

<a id="pfaff"></a>
### Controlled release from a cavity memory

**W. Pfaff et al., “Controlled release of multiphoton quantum states from a microwave cavity memory,” Nature Physics 13, 882–887 (2017)** [pfaff]. [Publisher](https://doi.org/10.1038/nphys4143).

Controlled release from a bosonic memory is an established route to travelling multiphoton states. The memory and its controllable release coupling are physical resources that differ from the native emitter-only ladder.

<a id="gorshkov"></a>
### Dissipative Rydberg filtering

**A. V. Gorshkov, R. Nath, and T. Pohl, “Dissipative Many-Body Quantum Optics in Rydberg Media,” Physical Review Letters 110, 153601 (2013)** [gorshkov]. [Publisher](https://doi.org/10.1103/PhysRevLett.110.153601), [primary preprint](https://arxiv.org/abs/1211.7060).

Dissipative Rydberg filtering supplies a different state-preparation mechanism and motivates careful treatment of timing records and photon purity. Such filtering has its own output-state and conditioning analysis; it does not establish the uniform-attenuation particle-reduction identity or the native collective fidelity bound.

<a id="pasharavesh"></a>
### Photon subtraction and temporal switching

**A. Pasharavesh and M. Bajcsy, “Multi-Photon Fock State Generation via Selective Single Photon Subtraction in a Cascaded Waveguide QED System,” Advanced Quantum Technologies 8, 2400616 (2025)** [pasharavesh]. [Publisher](https://doi.org/10.1002/qute.202400616).

Photon subtraction and temporal heralding or switching are established preparation mechanisms. The [prefix-detection result](../science/prefix_detection.md) specifies a particular native-source stopping rule, the consumed photons and timing reference, and the exact nominal-target penalties for its detector efficiency and switching delay.

<a id="abudayyeh"></a>
### Temporal heralding of quantum-dot emission

**H. Abudayyeh, B. Lubotzky, S. Majumder, J. A. Hollingsworth, and R. Rapaport, “Purification of single photons by temporal heralding of quantum dot sources,” ACS Photonics 6(2), 446–452 (2019)** [abudayyeh]. [Publisher](https://doi.org/10.1021/acsphotonics.8b01396), [primary preprint](https://arxiv.org/abs/1805.00201).

Temporal heralding can be used to purify emitted photons in a different source setting. Together with the preparation mechanisms above, it motivates reporting deterministic emission, conditional fidelity, and unconditional target yield separately. A mathematical photon-number sector becomes a usable herald only when the success flag leaves the desired photons available.

## Coherent transition control and implementation scope

<a id="higgins"></a>
### Engineering rates along a collective ladder

**K. D. B. Higgins, S. C. Benjamin, T. M. Stace, G. J. Milburn, B. W. Lovett, and E. M. Gauger, “Superabsorption of light via quantum engineering,” Nature Communications 5, 4705 (2014)** [higgins]. [Publisher](https://doi.org/10.1038/ncomms5705).

Transition-rate engineering along collective ladders is used in the superabsorption proposal. Resolving transition frequencies and engineering their rates does not alone implement the coherent single jump

```math
L(t)=\sum_m\sqrt{r_m(t)}\,|m+1\rangle\langle m|
```

required by the [capped construction](../science/capped_control.md#eq-cappedrates). Distinct output channels can retain rung information. That construction specifies a coherent excitation-dependent coupling to the same output, with no additional environmental history record. It is an abstract control model; the rate prescription alone supplies neither an experimental architecture nor a finite-bandwidth implementation.

The restrictions proved in this project depend on the allowed operations. [Uniform attenuation](../science/attenuation.md), symmetric diagonal phases, and [deterministic common rate shaping](../science/control_restrictions.md) retain the modal ceiling in their stated senses. [Prefix detection](../science/prefix_detection.md) changes the photon-number resource and uses its recorded time origin. Excitation-dependent coherent coupling changes the transition ladder.

[Exact Fock factorization under a native-rate cap](../science/exact_fock_control.md#eq-exactslow) is slow, while the [controlled approximation](../science/capped_control.md#eq-cappedasymptotic) retains fast release with fidelity tending to one. The distinction between exact factorization and approximate fidelity is part of the result.

These are restrictions and constructions for the stated symmetric Markov models. Their conclusions are not a classification of all excitation-preserving dynamics, other spin sectors, ancillary memories, adaptive measurements, or non-Markov sources. Emitter disorder, additional channels, and unobserved local-loss histories change the output-state problem. In particular, [independent atomic decay](../science/local_loss.md) is not uniform optical attenuation, and separately resolved rung rates or measured feedback do not by themselves preserve the coherent output amplitudes required by the controlled construction.

## Selected educational anchor

<a id="kiilerich2020"></a>
### Quantum interactions with pulses of radiation

**Alexander Holm Kiilerich and Klaus Mølmer, “Quantum interactions with pulses of radiation,” Physical Review A 102, 023717 (2020)** [kiilerich2020]. [Publisher](https://doi.org/10.1103/PhysRevA.102.023717), [primary preprint](https://arxiv.org/abs/2003.04573).

This is the single educational anchor for the [30-milestone route](../learning/MILESTONES.md), especially Sections II A–C and III. Its virtual pulse sources and receivers, mode occupations, complete mode states, and cascaded dynamics provide the foundations translated in the [source-to-project bridge](../learning/BRIDGE.md). The research references above retain their attribution roles; the project's bounds and resource theorems are developed in the connected [scientific account](../science/model.md).
