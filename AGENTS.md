# Working with this research repository

## Scientific purpose

This repository studies the optimized overlap of collectively emitted light
with a single temporal-mode Fock state. The central objects are the complete
photon wavefunction, its reduced states, and preparation protocols with
explicit photon and control resources.

The canonical mathematical reference is
theory/collective_photon_fidelity.tex and its compiled PDF. Read the relevant
definitions and proof before changing a claim. The README is the entry point;
verification/ contains reproducible consistency checks.

## Conventions and claims

- Fidelity means squared overlap with a pure Fock target. Distinguish it from
  amplitude, density-matrix purity, and the fraction of photons occupying a
  dominant one-photon mode.
- Distinguish the probability of a photon-number sector, its normalized
  conditional fidelity, and its unconditional target-state yield.
- Keep physical time and dimensionless time separate. The collective decay
  rate and Euler's gamma function are different quantities.
- State whether the initial source is fully inverted or a symmetric Dicke
  state with partial excitation. Exciting an arbitrary subset is a different
  preparation.
- Uniform optical attenuation and independent local atomic decay are
  different channels. The reduced-state survivor theorem applies to uniform
  attenuation, not to arbitrary local-loss trajectories.
- Keep all asymptotic regimes explicit, including which ratios are fixed.
  The native theorem determines an exponent and two bounding constants;
  neither constant is an established exact asymptotic prefactor.
- The prefix protocol consumes detected photons and uses the recorded time
  origin. Its nominal-target detector and latency formula assumes the stated
  stopping rule. A switching rate of order Gamma times N squared requires both
  the consumed and retained photon numbers to be macroscopic.
- The phase and common-rate restrictions concern the symmetric ladder and
  the specified output model. Shaping the collective rate while a local
  physical loss rate stays fixed changes that problem.
- Exact Fock factorization under the native rate cap has a time penalty.
  The capped coherent construction shows that this penalty does not extend
  to every sequence of fidelities tending to one.
- Coherent excitation-dependent coupling must preserve the one-output
  quantum amplitude. Separate rate equations or measured feedback do not by
  themselves establish an implementation.
- An all-photon sector is not automatically a usable herald. State the
  measurement or monitoring assumptions when discussing an operational source.

## Mathematical and numerical work

Prefer analytic arguments and explicit finite-size inequalities. When adding
a result, state its assumptions, quantity, and quantifiers before the proof.
Use primary literature for attribution and distinguish established ingredients
from results proved in this repository.

Numerical pulse overlaps are achievable values for the specified mode, not
certificates of the optimized fidelity. Numerical checks support algebra and
implementation; they do not establish uniform or asymptotic theorems.
Preserve normalization conventions and control numerical tails explicitly.
Add checks when they address a concrete failure mode or a new mathematical
claim, rather than copying an implementation into a second formula.

## Documentation and review

Keep the reader-facing material focused on the science, its assumptions,
proofs, and reproducibility. Present a complete reference without exploration
diaries, progress bars, journal predictions, or lists of unrelated work not
undertaken. Preserve the README's Purpose and contact statement.

Use GitHub-native dollar-delimited mathematics in Markdown. Put display
equations on their own lines with blank lines around them; keep equations out
of headings. Check links and rendering when changing the README.

Before merging scientific changes, run the verification command documented in
the README. Rebuild the PDF when its source changes, inspect compilation
warnings, and render the changed pages to check formulas, tables, and page
breaks. Keep the compiled PDF synchronized with its source. Exclude temporary
LaTeX products, caches, and local environments from version control.

Keep changes scoped to this repository and the user's current task.
