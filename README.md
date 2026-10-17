# Collective Photon Fidelity

**How well can a collectively emitting atomic ensemble prepare many photons in one temporal mode?** For ideal Dicke emission from $`N`$ fully excited emitters, the best squared overlap with any single-mode $`N`$-photon Fock state obeys

```math
F_N^\star=\Theta(N^{-1/2}).
```

A bright superradiant pulse can have a large dominant-mode occupation while its complete many-photon state has decreasing Fock fidelity. An explicit normalized pulse supplies the lower bound; a photon-count argument gives an upper bound uniform over every candidate temporal mode. The [model and exact statement](science/model.md) and [native-emission proof](science/native_emission.md) fix the assumptions and bounding constants.

The multimode character of collective emission and finite-size Fock-state overlaps have an established literature. The [related-work account](references/RELATED_WORK.md) identifies those ingredients and explains the quantities compared here.

## Photon, loss, and control resources

The native source has vacuum input, one Markov output channel $`L_{\mathrm{out}}=\sqrt{\Gamma}J_-`$, and identical emitters in the symmetric spin sector. Its emission rates are $`r_m=\Gamma(m+1)(N-m)`$, with $`\Gamma>0`$, and emission completes. Each extension below specifies its additional operation.

For a normalized $`n`$-photon sector $`\rho_n`$, the target fidelity is $`F^\star(\rho_n)=\sup_{\lVert f\rVert_2=1}\langle n_f|\rho_n|n_f\rangle`$. If that sector occurs with probability $`p_n`$, its unconditional target yield is $`Y_n^\star=p_nF^\star(\rho_n)`$. Mean mode occupation and density-matrix purity are different observables.

| Preparation or operation | Quantitative conclusion | Exact account |
|---|---|---|
| Symmetric $`n`$-excitation Dicke state in $`M`$ emitters | With $`a=M-n+1=o(M)`$, $`F_{M,n}^\star=\Theta(\sqrt{a/M})`$; in the dilute regime $`n/M\to0`$, fidelity tends to one. | [Partial excitation](science/partial_excitation.md) |
| Uniform optical attenuation | Conditional survivor fidelity is at most $`C/\sqrt{k}`$ for $`1\le k\le N`$. At fixed $`0\lt\eta\lt1`$, optimizing both photon number and mode gives unconditional yield $`\Theta(N^{-1})`$. | [Attenuation](science/attenuation.md) |
| Detect and consume a prefix of $`r`$ photons | With the recorded final click as the new origin, $`F_{\mathrm{prefix}}(N,r)=F_{N,N-r}^\star`$. A sublinear prefix leaves vanishing fidelity. | [Prefix detection](science/prefix_detection.md) |
| Independent local atomic decay | At fixed $`\epsilon=\gamma/\Gamma`$, the all-desired-photon yield is $`\Theta(N^{-\epsilon-1/2})`$. Its sector probability and conditional fidelity have separate laws. | [Local loss](science/local_loss.md) |
| Exact Fock emission under the native rate cap | The mean final-emission time is at least $`H_N/\Gamma`$, with $`H_N=\sum_{j=1}^N1/j`$. | [Exact Fock control](science/exact_fock_control.md) |
| Abstract coherent excitation-dependent coupling under the same cap | In the lossless model, an explicit construction achieves $`F_N[f]\ge1-O(N^{-3})`$ at mean time $`O(\log N/(\Gamma N))`$. At fixed local-loss ratio, it has an inverse-polynomial acceptance guarantee and conditional fidelity approaching one. | [Capped coherent control](science/capped_control.md) |

For the ideal prefix protocol, consuming half the photons gives the asymptotic lower bound

```math
\liminf_{N\to\infty}F_{\mathrm{prefix}}(N,\lfloor N/2\rfloor)
\ge \frac{e}{2\sqrt{2}}\approx0.9611.
```

This is an achievable lower bound, not an exact optimum or finite-size equality. Every ideal timing record is accepted, and the remaining pulse is defined relative to that record.

For the predetermined retained photon number $`N-r`$, detection efficiency $`d`$ and switching delay $`\Delta`$ impose the exact yield factor

```math
Y_{N-r}^{\mathrm{nom}}(d,\Delta)
=d^r e^{-\Gamma(N-r)(r+1)\Delta}F_{N,N-r}^\star.
```

The [detection and latency law](science/prefix_detection.md#eq-prefixcost) states the stopping rule, trigger conditioning, and required assumptions. It makes the consumed photons, detection efficiency, and switching time explicit resources.

## Read the science

Start with the [model and observables](science/model.md). Follow the [emitted wavefunction and matching native bounds](science/native_emission.md), then the [excitation regimes](science/partial_excitation.md). The two loss models and the prefix protocol show how changing the preparation affects the conditional state and its yield. The control pages explain why some operations preserve the limitation and how a coherent change of ladder can overcome it. The [physical interpretation](science/interpretation.md) connects the results.

| To inspect | Read |
|---|---|
| State conventions, fidelity, and the principal theorem | [Model](science/model.md) |
| Explicit pulse, relative entropy, uniform count bound, and the exact two-photon optimum | [Native emission](science/native_emission.md) |
| Dilute, fixed-fraction, and near-inversion limits, including real effective parameters | [Partial excitation](science/partial_excitation.md) |
| Surviving photons after a mode-independent attenuator | [Attenuation](science/attenuation.md) |
| No-local-loss kernel, acceptance probability, and strong-conditioning cost | [Local loss](science/local_loss.md) |
| Diagonal phases, common rate shaping, and ideal mode filtering | [Control restrictions](science/control_restrictions.md) |
| Prefix preparation, consumed photons, detector efficiency, and delay | [Prefix detection](science/prefix_detection.md) |
| Necessary and sufficient Fock criterion and its exact-emission time penalty | [Exact Fock control](science/exact_fock_control.md) |
| Finite-parameter control guarantees, loss robustness, and accepted completion times | [Capped coherent control](science/capped_control.md) |
| Ordered-amplitude recursion, numerical tables, and cutoff budgets | [Numerical methods](science/numerical_checks.md) |
| Physical meaning and resource boundaries | [Interpretation](science/interpretation.md) |
| Source attribution and bibliographic identities | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

## Learn the project

The single educational anchor is **A. H. Kiilerich and K. Mølmer, “Quantum interactions with pulses of radiation,” Physical Review A 102, 023717 (2020)**. [Publisher](https://doi.org/10.1103/PhysRevA.102.023717) · [Open version](https://arxiv.org/abs/2003.04573).

The [anchor bridge](learning/BRIDGE.md) selects Sections II A–C and III, translates the notation, and connects the input–output and selected-mode framework to this project's proofs. The [30-milestone map](learning/MILESTONES.md) gives a common understanding route: **14 background/preliminaries milestones** establish the field, states, and probability tools; **16 narrative/innovation milestones** join the bounds and resource laws into the complete story.

Use the bridge alongside the milestones for self-directed study. Every milestone has a central question, an understanding target, earlier dependencies, a conceptual connection, and scientific source pointers. The [LLM reading guide](llms.txt) maps reader intentions to the authoritative files.

## Reproduce the calculations

From the repository root, install the dependencies and run:

```bash
python3 -m pip install -r requirements.txt
make check
```

The [verification guide](verification/README.md) provides an isolated-environment setup, the reference output, and the scope of each check. Use `--json` for machine-readable residuals and cutoff budgets:

```bash
python3 verification/check_fidelity.py --json
```

The calculations evaluate specified trial modes and check independent exact identities, normalization, and convergence. The proofs establish the uniform optimization bounds and asymptotic laws.

## Scope

The partial-excitation source is a symmetric Dicke state; exciting an arbitrary subset prepares a different state. Uniform attenuation and independent local atomic decay produce different conditional states. A photon-number sector is not automatically an operational herald, and its probability must be included in unconditional yield.

The control restrictions apply to the specified symmetric ladder and output channel. The fast high-fidelity construction assumes one coherent excitation-dependent output jump; separate rate equations do not establish its implementation. Exact Fock factorization and fidelity approaching one have different time constraints. Each scientific page states the finite-parameter conditions before its asymptotic consequences.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository is distributed under the [MIT License](LICENSE).
