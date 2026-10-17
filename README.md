# Collective Photon Fidelity

How well can a collectively emitting atomic ensemble prepare many photons in one temporal mode?

This repository studies that question for ideal Dicke emission and for specified loss, measurement, and control operations. A superradiant pulse can put a large fraction of its photons in a dominant temporal mode while its overlap with a single-mode many-photon Fock state decreases with photon number. For $N$ fully excited emitters, the optimized **squared fidelity** obeys

$$
F_N^\star=\Theta(N^{-1/2}).
$$

Uniform attenuation preserves a vanishing fidelity when a macroscopic number of photons survives. Detecting a prefix of the burst and using its last click to set the remaining pulse's time origin changes the preparation problem: consuming a fixed fraction can leave a macroscopic pulse with high conditional fidelity. The results quantify that photon cost and the penalties from imperfect detection and switching delay.

**Full mathematical reference:** [Theory note (PDF)](theory/collective_photon_fidelity.pdf) · [LaTeX source](theory/collective_photon_fidelity.tex)

**Learning route:** [30-milestone map](learning/MILESTONES.md) · [Bridge from the educational anchor](learning/BRIDGE.md) · [LLM reading guide](llms.txt)

## Physical model

The native source consists of $N$ identical two-level emitters, initially fully excited, coupled to one Markov output channel:

$$
L_{\mathrm{out}}=\sqrt{\Gamma}J_-,
\qquad
J_-=\sum_{i=1}^{N}\sigma_i^-,
\qquad
\Gamma>0.
$$

The input field is vacuum. The emitters remain in the fully symmetric spin sector, and emission completes. Unless a result explicitly adds another process, there is no drive, dephasing, local decay, or feedback.

After $m$ photons have been emitted, the next emission rate is

$$
r_m=\Gamma(m+1)(N-m),
\qquad 0\le m\lt N.
$$

The increasing collective factor near the beginning of the cascade produces the superradiant burst. The emitted photons also have correlated arrival times. Those correlations matter when asking whether the *whole pulse* occupies a single temporal mode.

For partial excitation, the source is a **symmetric Dicke state** with $n$ excitations in $M$ emitters. Preparing an arbitrary subset of $n$ excited emitters is a different initial state.

## What fidelity measures

Let $b^\dagger(t)$ create an output photon at physical time $t$, with $[b(t),b^\dagger(s)]=\delta(t-s)$. A normalized, possibly complex temporal mode $f$ defines

$$
\int_0^\infty |f(t)|^2dt=1,
\qquad
a_f^\dagger=\int_0^\infty f(t)b^\dagger(t)dt,
\qquad
|n_f\rangle=\frac{(a_f^\dagger)^n}{\sqrt{n!}}|0\rangle.
$$

For a trace-one state $\rho_n$ in the sector containing $n$ photons, the quantity studied here is

$$
F^\star(\rho_n)
=\sup_{\Vert f\Vert_2=1}\langle n_f|\rho_n|n_f\rangle.
$$

For a pure state this is the squared overlap. The optimization includes every normalized temporal mode; it is not restricted to the most populated eigenmode of a first-order correlation function.

Three quantities need separate names:

| Quantity | Meaning |
|---|---|
| $p_n$ | Probability that the output contains exactly $n$ photons. |
| $F^\star(\rho_n)$ | Best single-mode Fock fidelity of the normalized state in that sector. |
| $Y_n^\star=p_nF^\star(\rho_n)$ | Unconditional overlap with the best single-mode target containing $n$ photons, per preparation attempt. |

The mean occupation fraction $\langle a_f^\dagger a_f\rangle/n$, the density-matrix purity $\mathrm{Tr}(\rho_n^2)$, and the fidelity defined above answer different questions.

All asymptotic statements concern growing system size under the stated assumptions. The notation $\Theta(g_N)$ means that positive, size-independent constants bound the quantity above and below by multiples of $g_N$ for sufficiently large size. It does not determine an exact prefactor.

## Main results

### 1. Native emission and partial excitation

For the pure output $\rho_N=|\Psi_N\rangle\langle\Psi_N|$ of the fully inverted native source,

$$
F_N^\star
=\sup_{\Vert f\Vert_2=1}|\langle N_f|\Psi_N\rangle|^2
=\Theta(N^{-1/2}).
$$

The theorem supplies bounds on the leading coefficient:

$$
\sqrt{2\pi}
\le \liminf_{N\to\infty}\sqrt{N}F_N^\star
\le \limsup_{N\to\infty}\sqrt{N}F_N^\star
\le \frac{4\sqrt{2\pi}}{e}.
$$

Neither endpoint is asserted to be the exact asymptotic prefactor.

For $n$ symmetric excitations in $M$ emitters, write $F_{M,n}^\star$ for the corresponding optimum and set $a=M-n+1$. The preparation regimes are:

| Regime | Fidelity statement |
|---|---|
| Near full inversion: $a=o(M)$ | $F_{M,n}^\star=\Theta(\sqrt{a/M})$. |
| Dilute excitation: $n/M\to0$ | $F_{M,n}^\star\to1$. |
| Fixed fraction: $n/M\to\rho\in(0,1)$ | A positive asymptotic lower bound is available, as given below. |

At a fixed excitation fraction,

$$
\liminf F_{M,n}^\star
\ge e(1-\rho)^{(2-\rho)/(2\rho)}.
$$

The theory note gives an explicit normalized trial pulse and finite-size lower bounds. Numerically evaluating that pulse gives an achievable fidelity, not a certificate of the optimized value.

### 2. Uniform attenuation and surviving photons

Apply a uniform attenuator with transmission $0\lt \eta\lt 1$ to the ideal field of $N$ photons, with vacuum in the unused port. The attenuation acts identically on every temporal mode.

Conditioned on exactly $k$ transmitted photons, the normalized output is the reduced density operator $\rho_N^{(k)}$ for $k$ particles of the ideal field. Its optimized fidelity satisfies a universal bound

$$
F_{N\to k}^\star
:=\sup_{\Vert f\Vert_2=1}\langle k_f|\rho_N^{(k)}|k_f\rangle
\le \frac{C}{\sqrt{k}},
\qquad 1\le k\le N.
$$

For a fixed retained fraction $k/N\to c\in(0,1]$, the matching order is

$$
F_{N\to k}^\star=\Theta(N^{-1/2}).
$$

The transmitted photon number is binomial:

$$
p_k=\binom Nk\eta^k(1-\eta)^{N-k}.
$$

Even when the target photon number and temporal mode may both be chosen, the unconditional optimum at fixed $\eta$ obeys

$$
\max_{0\le k\le N}\sup_{\Vert f\Vert_2=1}
\langle k_f|\mathcal L_\eta(\rho_N)|k_f\rangle
=\Theta(N^{-1}).
$$

Requiring all $N$ photons instead gives the exact yield $\eta^N F_N^\star$.

These statements concern mode-independent attenuation. A mode-selective filter with conditioning is a different operation. Independent local atomic decay also requires a separate treatment, given below.

### 3. Detecting a prefix prepares a different source

Start with the lossless native source. Detect and consume its first $r$ photons, immediately route the remaining field to the output, and use the time of click number $r$ as the new time origin. For $r=0$, use the initial preparation time.

With perfect detection, timing, and switching, the remaining emitters are exactly in the symmetric Dicke state with $N-r$ excitations. The record-aligned field therefore has

$$
F_{\mathrm{prefix}}(N,r)=F_{N,N-r}^\star.
$$

Every timing record is accepted in this ideal protocol. The recorded origin defines the target pulse for each run; averaging over unrecorded time translations defines a different output state.

For a sublinear consumed prefix,

$$
r=o(N)
\quad\Longrightarrow\quad
F_{\mathrm{prefix}}(N,r)
=\Theta\left(\sqrt{\frac{r+1}{N}}\right).
$$

Thus a sublinear prefix cannot maintain a nonzero limiting fidelity. Consuming a fixed fraction $r/N\to\alpha\in(0,1)$ permits

$$
\liminf F_{\mathrm{prefix}}(N,r)
\ge e\alpha^{(1+\alpha)/[2(1-\alpha)]}.
$$

For example, consuming half the photons gives the **asymptotic lower bound**

$$
\liminf_{N\to\infty}
F_{\mathrm{prefix}}(N,\lfloor N/2\rfloor)
\ge \frac{e}{2\sqrt{2}}
\approx 0.9611.
$$

This value is a lower bound, not an exact optimum or a finite-size equality. If the retained fraction tends to zero, $(N-r)/N\to0$, the fidelity tends to one; the retained photon number may still grow.

This resource law applies to the specified prefix protocol. It does not classify every possible adaptive measurement or purification operation.

#### Detection and switching costs

Let $1\le r\lt N$. Suppose each diverted photon independently registers with efficiency $0\lt d\le1$, and routing begins a fixed delay $\Delta\ge0$ after the detector registers click number $r$. Assume otherwise ideal timestamps, no dark counts or other source loss, and continued native emission during the delay.

For the predetermined target photon number $n=N-r$, the optimized yield per initial attempt, with the pulse referred to the actual switch time, is exactly

$$
Y_{N-r}^{\mathrm{nom}}(d,\Delta)
=d^r
e^{-\Gamma(N-r)(r+1)\Delta}
F_{N,N-r}^\star.
$$

Only branches with no missed prefix photon and no extra emission during the delay contain the nominal number of retained photons. Conditioning only on obtaining a trigger divides this yield by $\Pr[\mathrm{Bin}(N,d)\ge r]$.

For $r$ proportional to $N$, keeping the detection factor nonvanishing requires $r[-\ln d]=O(1)$, or $r(1-d)=O(1)$ near unit efficiency. When both the consumed and retained photon numbers are proportional to $N$, the delay factor requires $\Gamma N^2\Delta=O(1)$. The exact general condition is $\Gamma(N-r)(r+1)\Delta=O(1)$.

These costs belong to this stopping rule and predetermined photon count. Buffering, pausing emission, or using additional number information changes the protocol and its resource accounting.

### 4. Independent local atomic decay

Add separate undesired channels

$$
L_i=\sqrt{\gamma}\sigma_i^-,
\qquad
\epsilon=\frac{\gamma}{\Gamma},
$$

with constant rates and no pumping. The desired output contains all $N$ photons precisely in the sector with no local decay. Its probability is

$$
p_0
=\prod_{j=1}^{N}\frac{j}{j+\epsilon}
=\frac{\Gamma_{\mathrm E}(N+1)\Gamma_{\mathrm E}(1+\epsilon)}
{\Gamma_{\mathrm E}(N+1+\epsilon)}.
$$

Here $\Gamma_{\mathrm E}$ denotes Euler's gamma function, while $\Gamma$ is the physical collective decay rate. The branching-rate calculation is an established ingredient of collective-emission theory; see [Paulisch et al.](https://arxiv.org/abs/1805.00712).

The normalized temporal state in this sector is described by the same positive density family as the partial-excitation problem, with $a=1+\epsilon$ and effective parameter $M=N+\epsilon$. This is an identity between distributions; it does not represent a fractional number of physical emitters.

For fixed $\epsilon\ge0$,

$$
p_0\sim\Gamma_{\mathrm E}(1+\epsilon)N^{-\epsilon},
\qquad
F_{\mathrm{cond}}^\star=\Theta(N^{-1/2}),
\qquad
Y_N^\star=p_0F_{\mathrm{cond}}^\star
=\Theta(N^{-\epsilon-1/2}).
$$

Stronger conditioning can select a higher-fidelity state, with a correspondingly smaller sector probability. In this native-source model, keeping the conditional fidelity bounded away from zero requires $\epsilon=\Omega(N)$, and the acceptance probability is bounded above by an exponentially decreasing function of $N$. At the illustrative point $\epsilon=N$,

$$
p_0=\binom{2N}{N}^{-1},
\qquad
\liminf F_{\mathrm{cond}}^\star\ge\frac{e}{2\sqrt{2}}.
$$

The all-photon sector is a conditional state, not automatically a usable heralded source. Operational heralding requires suitable monitoring or another success flag; counting and consuming all desired photons only certifies the event retrospectively.

After an actual local jump, the emitters can leave the symmetric sector. Desired outputs with fewer than $N$ photons are therefore not generally reduced states of the ideal field, and the uniform-attenuation survivor theorem does not apply to them.

The constant-ratio formulas also apply when $\gamma(t)=\epsilon\Gamma(t)$ and emission completes. Shaping $\Gamma(t)$ while a physical local-loss rate $\gamma$ remains fixed changes the conditional temporal state.

### 5. Control restrictions and a coherent escape

In the ideal lossless model, a lossless unitary change of temporal modes preserves the optimized fidelity. A common deterministic envelope $\Gamma(t)$ also preserves it when $\int_0^\infty\Gamma(t)dt=\infty$: it reparametrizes the clock through $\tau(t)=\int_0^t\Gamma(s)ds$.

At fixed jump amplitudes, arbitrary diagonal Hamiltonians and transition phases cannot increase the optimum above the positive, phase-free output. The same inequality holds for every normalized reduced state of $k$ particles. This includes emitter-only Hamiltonians that conserve excitation and preserve the symmetric spin sector, where each excitation subspace is one-dimensional.

For a general single-output Markov ladder, exact single-mode Fock emission requires a bosonic rate ladder and compatible phases:

$$
r_m(t)=(N-m)h(t),
\qquad
h(t)=\frac{|f(t)|^2}{\int_t^\infty |f(s)|^2ds}.
$$

Shaped Fock emission from a bosonic oscillator is an established construction; see [Gough and Zhang](https://doi.org/10.1140/epjqt/s40507-015-0027-z). Here the criterion makes the role of the native Dicke matrix elements explicit.

If coherent amplitude controls obey the pointwise native cap

$$
0\le r_m(t)\le\Gamma(m+1)(N-m),
$$

then **exact single-mode Fock emission** forces $h(t)\le\Gamma$. With $H_N=\sum_{j=1}^{N}1/j$, the mean last-emission times satisfy

$$
\mathbb E T_{\mathrm{last}}^{\mathrm{exact\ Fock}}
\ge\frac{H_N}{\Gamma},
\qquad
\mathbb E T_{\mathrm{last}}^{\mathrm{native}}
=\frac{2H_N}{\Gamma(N+1)}.
$$

For controls whose lossless output is an exact single-mode Fock state, adding independent local decay also bounds the survival of all $N$ photons by $(1+\epsilon)^{-N}$.

The distinction between exact Fock factorization and fidelity approaching one is essential. An explicit **abstract coherent excitation-dependent coupling** respects the same rate cap and achieves

$$
F_N[f]\ge1-O(N^{-3}),
\qquad
\mathbb E T_{\mathrm{last}}
=O\left(\frac{\ln N}{\Gamma N}\right).
$$

It therefore retains the native asymptotic time order while approaching unit fidelity. With a fixed local-loss ratio, the construction also has an inverse-polynomial lower bound on all-photon acceptance and conditional fidelity tending to one.

This construction assumes a single coherent output jump whose amplitudes depend on excitation number and time. Separate transition-rate equations or measured classical feedback do not establish such an implementation: coherence between emission histories must be preserved. Cavity memories, auxiliary levels, and couplings that mix spin sectors introduce additional degrees of freedom and have their own preparation and release problems.

## Why the analytical bounds work

In a single-mode Fock state, photon detection times are independent draws from $|f(t)|^2$. The number arriving before the mode's median time is therefore binomial. For Dicke emission, each central count probability is at most of order $1/N$, uniformly in the cut time. Comparing these count distributions gives an upper bound on quantum fidelity that is valid for every candidate mode.

The lower bound uses the positive collective-emission wavefunction, an explicit normalized product pulse, and a relative-entropy inequality. The matching size dependence establishes the exponent without a numerical search over all pulse shapes.

Uniform attenuation thins the cut counts through a hypergeometric distribution. An exact combinatorial identity carries the upper bound to the surviving photons. Prefix detection instead prepares a definite partial-excitation Dicke state at a recorded time, allowing the partial-source bounds to be applied directly.

## Reading order

### Learning route

Start with the [30-milestone map](learning/MILESTONES.md). Its 14 background/preliminary milestones establish the field, source, and proof tools; its 16 narrative/innovation milestones develop the bounds and resource laws. Each phase builds from individual ingredients to an integrated understanding. Every milestone states a conceptual target, its dependencies, and the relevant source material.

The single educational anchor is **A. H. Kiilerich and K. Mølmer, “Quantum interactions with pulses of radiation,” Physical Review A 102, 023717 (2020)**. [Publisher](https://doi.org/10.1103/PhysRevA.102.023717) · [Open preprint](https://arxiv.org/abs/2003.04573). The [bridge guide](learning/BRIDGE.md) selects the relevant parts of Sections II–III, translates notation, and connects the output-mode framework to the collective-emission results proved here. Read those parts alongside the corresponding milestones; the scientific bibliography below remains the route for research attribution.

The [LLM reading guide](llms.txt) maps questions to the canonical definitions, proofs, and numerical checks. The shared milestone map is separate from a learner's session progress; the [repository guidance](AGENTS.md#learning-map-and-tutoring) specifies how to teach a milestone when a lesson is requested.

### Proof and verification route

1. Read the model and fidelity definitions above to fix the source, target state, and conditioning convention.
2. Open the [theory note](theory/collective_photon_fidelity.pdf) for the native-source proof, explicit trial pulse, and partial-excitation bounds.
3. Continue through uniform attenuation, local atomic decay, and prefix detection to compare photon-number probability with modal fidelity and preparation yield.
4. Read the control sections for the exact-factorization criterion and the capped coherent construction.
5. Run the [verification program](verification/check_fidelity.py) alongside the finite-size formulas.

The [LaTeX source](theory/collective_photon_fidelity.tex) is the canonical mathematical reference. The [repository guidance](AGENTS.md) records the conventions used when modifying scientific claims.

## Reproduce the calculations

Run these commands from the repository root. Python dependencies are recorded in [requirements.txt](requirements.txt):

```bash
python3 -m pip install -r requirements.txt
python3 verification/check_fidelity.py
```

The equivalent Make target is:

```bash
make check
```

The numerical program checks finite-size formulas and evaluates overlaps for specified trial modes. Such overlaps are achievable values. The analytic proofs in the theory note establish optimization bounds and asymptotic statements.

To rebuild the PDF:

```bash
make pdf
```

This requires a LaTeX distribution with pdflatex and the packages geometry, fontenc, lmodern, microtype, amsmath, amssymb, amsthm, mathtools, booktabs, array, graphicx, xcolor, hyperref, and fancyhdr. The [Makefile](Makefile) compiles twice to resolve references and writes the result to [theory/collective_photon_fidelity.pdf](theory/collective_photon_fidelity.pdf). Temporary compilation files are placed in the build directory.

## Relation to primary literature

The collective source, its multimode character, dominant one-photon modes, and finite-size Fock-state fidelities have an established literature. Temporal heralding and bosonic pulse synthesis are also established techniques. The theory note develops the quantitative bounds under the assumptions stated above and provides the full bibliography.

- **Collective waveguide emission and loss:** V. Paulisch, M. Perarnau-Llobet, A. González-Tudela, and J. I. Cirac, “Quantum metrology with one-dimensional superradiant photonic states,” *Physical Review A* **99**, 043807 (2019). [Primary preprint](https://arxiv.org/abs/1805.00712). The collective/no-local-loss trajectory rates underlying the survival product appear in its supplemental analysis.
- **Multimode multiphoton states:** M. Perarnau-Llobet, A. González-Tudela, and J. I. Cirac, “Multimode Fock states with large photon number: effective descriptions and applications in quantum metrology,” *Quantum Science and Technology* **5**, 025003 (2020). [Primary preprint](https://arxiv.org/abs/1910.03323).
- **Temporal-mode occupations:** B. Lemberger and K. Mølmer, “Radiation eigenmodes of Dicke superradiance,” *Physical Review A* **103**, 033713 (2021). [Primary preprint](https://arxiv.org/abs/2009.11687).
- **Partially excited sources:** Q. Liu and J.-T. Shen, “Photonic Fock state generation using superradiance,” *Optics Letters* **47**, 4576–4579 (2022). [Publisher](https://doi.org/10.1364/OL.468481).
- **Finite-size quantum states of collective emission:** O. Tziperman et al., “Nonlinear Quantum Light Generation in Collective Spontaneous Emission,” *ACS Nano* **19**, 21260–21270 (2025). [Publisher](https://doi.org/10.1021/acsnano.4c15257) · [Preprint, under its earlier title](https://arxiv.org/abs/2306.11348).
- **Timing records and photon purity:** A. V. Gorshkov, R. Nath, and T. Pohl, “Dissipative Many-Body Quantum Optics in Rydberg Media,” *Physical Review Letters* **110**, 153601 (2013). [Primary preprint](https://arxiv.org/abs/1211.7060).
- **Temporal heralding and switching for Fock pulses:** A. Pasharavesh and M. Bajcsy, “Multi-Photon Fock State Generation via Selective Single Photon Subtraction in a Cascaded Waveguide QED System,” *Advanced Quantum Technologies* **8**, 2400616 (2025). [Full text](https://doi.org/10.1002/qute.202400616).
- **Shaped bosonic Fock emission:** J. E. Gough and G. Zhang, “Generating nonclassical quantum input field states with modulating filters,” *EPJ Quantum Technology* **2**, 15 (2015). [Full text](https://doi.org/10.1140/epjqt/s40507-015-0027-z).
- **Coherent cavity loading:** K. R. Brown, K. M. Dani, D. M. Stamper-Kurn, and K. B. Whaley, “Deterministic optical Fock-state generation,” *Physical Review A* **67**, 043818 (2003). [Primary preprint](https://arxiv.org/abs/quant-ph/0211134).
- **Controlled release from a memory:** W. Pfaff et al., “Controlled release of multiphoton quantum states from a microwave cavity memory,” *Nature Physics* **13**, 882–887 (2017). [Publisher](https://doi.org/10.1038/nphys4143).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository is distributed under the [MIT License](LICENSE).
