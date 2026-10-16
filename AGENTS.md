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
of headings. Check links and inspect substantial mathematics in the actual
hosted README or tutorial before declaring its presentation ready. Parser
checks alone do not establish correct rendering. Look for rejected macros,
unrendered inline expressions, lost inequalities, stray spacing punctuation,
and collisions in tables. Treat any syntax correction as specific to that
renderer; preserve the canonical LaTeX notation and mathematical meaning.

Before merging scientific changes, run the verification command documented in
the README. Rebuild the PDF when its source changes, inspect compilation
warnings, and render the changed pages to check formulas, tables, and page
breaks. Keep the compiled PDF synchronized with its source. Exclude temporary
LaTeX products, caches, and local environments from version control.

Keep changes scoped to this repository and the user's current task.

## Learning map and tutoring

The common understanding route is [learning/MILESTONES.md](learning/MILESTONES.md),
with the notation and argument bridge in [learning/BRIDGE.md](learning/BRIDGE.md).
[llms.txt](llms.txt) routes scientific questions to canonical sources. The
educational anchor is Kiilerich and Mølmer, *Quantum interactions with pulses
of radiation*, Physical Review A 102, 023717 (2020), especially Sections
II A–C and III. Use that one anchor for teaching foundations and the project
theory for its results; preserve the research bibliography for attribution.

Maintain exactly 30 milestones, M01–M30, in the two phases
background/preliminaries and narrative/innovation. Their targets and
allocation follow the science. Explain changes to the map when the science
changes, review the dependencies and both phase syntheses, and settle the
revised map before teaching from it. Adjust explanations and practice to a
learner while keeping the shared map stable. Keep learner attempts and
progress in the teaching session rather than in the public map.

Begin interactive teaching when the user requests a lesson. Repository
maintenance or a request for an explanation does not itself start a quiz.
For a requested milestone tutorial, use this protocol:

- Give every round a Revise, Learn, Test sequence. Revision recalls the
  relevant definitions, assumptions, and earlier results. Learning explains
  the idea or addresses a specific misconception before the test.
- Each milestone has one challenge with as many attempts as needed. Start
  with a compact revision and explanation followed by two questions. Each
  question has four options and exactly one correct answer. All answers in
  the same attempt must be correct to pass.
- Present challenge questions one at a time and give correctness feedback
  after the complete set. Finish the set even if an earlier answer was wrong.
  Use conceptual inferences, physical interpretation, limiting cases, and
  resource accounting; require only minimal mental calculation. Prefer
  clickable answer controls when available.
- Supply the prerequisites without copying the test answer into the
  explanation. Use plausible distractors and fresh applications on retries.
  Replace ambiguous or unreadable questions without counting a presentation
  defect as a conceptual error. If clickable selection is unavailable, state
  that briefly and accept a minimal option selection.
- After a failed challenge, give one to three targeted learning rounds.
  Each has its own revision, explanation, and one-question test. Correct
  and explain every learning-test answer immediately, including the last
  answer in the learning block. These answers guide teaching without
  changing the next challenge's length or passing the milestone.
- Count completed failed challenges within the current milestone. The next
  challenge has `min(2 + failed_challenges, 6)` fresh questions. At six,
  further failures still lead to a learning block and a fresh six-question
  attempt. Keep the all-correct passing rule and do not pool correct answers
  across failed attempts. Use the milestone's intensity as guidance for
  choosing one to three learning rounds, rather than extending a block
  indefinitely.
- A pass advances to the next milestone, which starts with two questions.
  Preserve enough session state to resume an interrupted attempt: milestone,
  round type, completed failed challenges, questions asked, and answers.
  An unfinished challenge is not a failure; a continuation request is not
  evidence of an answer or a pass.
- Completion means all 30 milestones have been passed under this protocol.
  State that scoped completion without adding a further examination or
  claiming mastery of every technical detail or neighboring subject. Preserve
  completed milestones rather than resetting them to prolong the course.

Keep the scientific qualifications visible in the teaching material, and
check substantial hosted mathematics when updating the map or bridge.
