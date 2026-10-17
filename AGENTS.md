# Working with this research repository

## Scientific purpose and sources

This repository studies the optimized squared overlap of collectively emitted
light with a single temporal-mode Fock state, and the photon, loss, and control
resources that change that overlap.

The authoritative scientific account is organized by topic under [science](science/).
Begin with [model.md](science/model.md), use the result-specific proof pages, and
connect their conclusions through [interpretation.md](science/interpretation.md).
[README.md](README.md) is the reader entrypoint. [llms.txt](llms.txt) maps questions
to sources, [references](references/RELATED_WORK.md) records attribution, and
[verification](verification/README.md) documents reproducible checks.

## Conventions and claims

- Fidelity means squared overlap with a pure Fock target. Distinguish it from
  amplitude, density-matrix purity, and dominant one-photon mode occupation.
- Keep photon-number sector probability, normalized conditional fidelity,
  and unconditional target yield separate.
- Distinguish physical time from the dimensionless collective clock, and the
  collective decay rate from Euler's gamma function.
- State whether the initial source is fully inverted or a symmetric Dicke
  state with partial excitation. Exciting an arbitrary subset is a different
  preparation.
- Uniform optical attenuation and independent local atomic decay are
  different channels. The reduced-state survivor theorem applies to uniform
  attenuation, not to arbitrary local-loss trajectories.
- Keep all asymptotic regimes explicit, including which ratios are fixed.
  The native theorem determines an exponent and bounding constants; neither
  constant is an established exact asymptotic prefactor.
- The prefix protocol consumes detected photons and uses the recorded time
  origin. Its nominal-target detector and latency formula requires the stated
  stopping rule. The Gamma-times-N-squared switching scale requires both the
  consumed and retained photon numbers to be macroscopic.
- Phase and common-rate restrictions concern the symmetric ladder and the
  specified output. Shaping the collective rate while a physical local-loss
  rate stays fixed changes the conditional-state problem.
- Exact Fock factorization under the native rate cap has a time penalty.
  The capped coherent construction shows that this penalty does not extend
  to every sequence of fidelities tending to one.
- A coherent excitation-dependent coupling must preserve the one-output
  quantum amplitude. Separate transition rates or measured feedback do not
  by themselves establish an implementation.
- A selected photon-number sector is not automatically a usable herald.
  State the monitoring or success-flag assumptions for an operational source.

## Mathematical and numerical work

Prefer analytical arguments and explicit finite-size inequalities. State the
assumptions, quantity, and quantifiers before each result. Give each proof one
authoritative home and preserve its dependencies when reorganizing material.
Attribute imported ingredients through the primary-source account and
structured bibliography.

Numerical pulse overlaps are achievable values for specified modes. The
written proofs establish the uniform optimization bounds and asymptotic laws.
Preserve normalization conventions and the distinction between an analytical
cutoff budget and an observed convergence difference. Add checks only for a
concrete mathematical or implementation risk.

## Documentation and verification

Keep the scientific question, reasoning, interpretation, source attribution,
and reproduction routes easy to find. Preserve the README's Purpose and
contact wording, repository license, and the exact scope of the claims.

The common learning route is [learning/MILESTONES.md](learning/MILESTONES.md):
exactly M01–M30, with 14 background/preliminaries and 16 narrative/innovation
milestones. Its central questions, understanding targets, dependencies,
conceptual connections, and sources follow the science. The single educational
anchor is Kiilerich and Mølmer, *Quantum interactions with pulses of radiation*,
Physical Review A 102, 023717 (2020); [learning/BRIDGE.md](learning/BRIDGE.md)
connects its relevant sections to the project. Research attribution remains
in the full bibliography.

Use GitHub-native inline mathematics and fenced math displays. Expand custom
macros in each expression, keep mathematics out of headings, and put blank
lines around displays. Preserve explicit equation anchors and repair incoming
links after moving an argument. Check substantial mathematical changes in the
actual hosted renderer, including bra–ket notation, inequalities, piecewise
expressions, and table layout; source checks alone do not establish readability.

Run the documented `make check` command before merging scientific or numerical
changes. For a structural migration, verify preservation of all mathematical
statements and proofs, source links, milestone dependencies, and reproduction
instructions. Keep caches, temporary outputs, and local environments out of
version control. The committed numerical reference output illustrates a
verified run; the program's independent checks and tolerances define success.

Keep changes scoped to this repository and the user's current task.
