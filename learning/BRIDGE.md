# From quantum pulses to collective photon fidelity

This bridge connects the description of a travelling quantum pulse to the full-field fidelity studied in this repository. Its central question is: **what would it mean for all emitted photons to occupy one temporal mode, and how can that claim be tested?**

The educational anchor is Alexander Holm Kiilerich and Klaus Mølmer, *Quantum interactions with pulses of radiation*, **Physical Review A 102, 023717 (2020)**: [primary preprint](https://arxiv.org/abs/2003.04573), [primary PDF](https://arxiv.org/pdf/2003.04573). The collective-emission results are in the project's [theory note](../theory/collective_photon_fidelity.pdf) and [canonical LaTeX source](../theory/collective_photon_fidelity.tex).

Use the [30-milestone map](MILESTONES.md) for the learning sequence. This page supplies notation, derivations, and connections to consult along that route. References such as `sec:wave` and `eq:fidelitydef` are stable labels in the canonical LaTeX source; the accompanying section titles identify the same material in the PDF.

## 1. Read the anchor with a specific destination

Equation numbers in this table refer to the linked primary preprint.

| Reading | Equations | Purpose |
|---|---|---|
| Section II, opening | (2), (3) | Lindblad evolution and the input-output relation. |
| Section II A | (4)–(10) | A virtual source for an incident pulse. |
| Section II B | (13)–(15) | Intensity, correlations, and occupied temporal modes. |
| Section II C | (17)–(19) | A virtual receiver for a selected outgoing mode. |
| Section III A | (23), (24) | Several input and output modes. |
| Section III B | (25) | Correlations between an emitter and outgoing modes. |

The translation below fixes its own operator conventions explicitly. It then replaces the local quantum system by the collective Dicke ladder. The native asymptotic law, count bound, relative-entropy bound, and resource theorems belong to the project theory.

**Map connection:** [M04](MILESTONES.md#m04)–[M08](MILESTONES.md#m08).

## 2. Fix the field convention before choosing a pulse

In physical time, let the outgoing continuum satisfy

$$
[b(t),b^\dagger(s)]=\delta(t-s).
$$

A temporal mode is a function with unit norm. Define

$$
\int_0^\infty \lvert f(t)\rvert^2dt=1,
\qquad
a_f^\dagger=\int_0^\infty f(t)b^\dagger(t)dt,
\qquad
a_f=\int_0^\infty f(t)^*b(t)dt.
$$

The conjugation in the annihilation operator follows by taking the adjoint. These definitions give

$$
[a_f,a_g^\dagger]
=\int_0^\infty f(t)^*g(t)dt,
\qquad
[a_f,a_f^\dagger]=1.
$$

Consequently,

$$
\lvert n_f\rangle
=\frac{(a_f^\dagger)^n}{\sqrt{n!}}\lvert0\rangle
$$

is a normalized state with exactly $n$ photons in mode $f$ and vacuum in its orthogonal complement. Within the chosen spatial channel, $f$ specifies temporal shape and phase; a number state specifies how that mode is populated.

### Notation and convention map

| Anchor notation or object | Convention used here and in the project |
|---|---|
| Incident envelope $u(t)$; selected outgoing envelope $v(t)$ | Use $f(t)$ for the mode currently under discussion. |
| Pulse creation operator in Eq. (6) | $a_f^\dagger$ has the envelope $f$, with no conjugation. |
| Local-system operator $\hat c$ | For native collective emission, use $J_-$. |
| Desired-channel rate $\gamma$ | Use $\Gamma$ for collective emission; the project's $\gamma$ denotes separate local atomic loss. |
| Virtual oscillators $\hat a_u,\hat a_v$ | Use $a_{\mathrm{src}},a_{\mathrm{rec}}$; these are auxiliary oscillator operators. |
| Coupling symbols $g_u,g_v$ | Define a separate coefficient $\lambda$ explicitly through $L_{\mathrm{cav}}=\lambda a$. |
| Autocorrelation $g^{(1)}(t,s)$ in Section II B | Use $G^{(1)}(t,s)=\langle b^\dagger(t)b(s)\rangle$; it is not normalized to one. |
| Physical time | Use $t$ here; write $\tau=\Gamma t$ when entering the dimensionless native calculation. |

The physical field and envelope have units of inverse square root of time. The rescaling

$$
\widetilde f(\tau)=\Gamma^{-1/2}f(\tau/\Gamma),
\qquad
\widetilde b(\tau)=\Gamma^{-1/2}b(\tau/\Gamma)
$$

preserves the continuum commutator, mode norm, and creation operator. It therefore preserves all Fock overlaps. In the first native sections of the theory note, the variable called $t$ is already dimensionless; the distinction matters when returning to detector delays and physical loss rates.

**Canonical reference:** “Model, observables, and main result,” `sec:model`, `eq:fidelitydef`. **Map connection:** [M01](MILESTONES.md#m01)–[M04](MILESTONES.md#m04).

## 3. Virtual source and receiver in one consistent convention

The reduced state of the emitter at a given time does not retain all outgoing-field information. The full channel-labelled Markov model, including its input state and coupling operators, determines that information. An auxiliary oscillator provides a way to retain the state of a chosen pulse without storing the entire continuum.

For the derivations here, declare

$$
L_{\mathrm{cav}}(t)=\lambda(t)a,
\qquad
b_{\mathrm{out}}(t)=b_{\mathrm{in}}(t)+\lambda(t)a(t).
$$

With no oscillator Hamiltonian, the corresponding Langevin equation is

$$
\frac{da}{dt}
=-\frac{\lvert\lambda(t)\rvert^2}{2}a(t)
-\lambda(t)^*b_{\mathrm{in}}(t).
$$

The coefficient of the input noise is the complex conjugate of the coefficient of $a$ in the jump. This is the convention used throughout the following derivation.

### Emitting a prescribed mode

Define the cumulative probability and survival of the mode by

$$
C_f(t)=\int_0^t\lvert f(s)\rvert^2ds,
\qquad
S_f(t)=1-C_f(t).
$$

For vacuum incident on the source oscillator, the coefficient of $a_{\mathrm{src}}(0)$ in the outgoing annihilation field is

$$
\lambda_{\mathrm{src}}(t)
\exp\left[-\frac12\int_0^t
\lvert\lambda_{\mathrm{src}}(s)\rvert^2ds\right].
$$

To make this coefficient equal to $f(t)$, choose

$$
\lambda_{\mathrm{src}}(t)=\frac{f(t)}{\sqrt{S_f(t)}},
\qquad
\lvert\lambda_{\mathrm{src}}(t)\rvert^2
=\frac{\lvert f(t)\rvert^2}{S_f(t)}
=h_f(t).
$$

Indeed, $dS_f/dt=-h_fS_f$, so the exponential is $\sqrt{S_f(t)}$. The pulse intensity determines the instantaneous decay rate through its **hazard** $h_f$: emission probability per unit time, conditional on the excitation not yet having left.

A passive linear oscillator transfers its initial creation operator into $a_f^\dagger$ when release is complete. Starting it in $\lvert n\rangle$ therefore prepares $\lvert n_f\rangle$. This supplies a useful comparison source: its matrix element at oscillator occupation $q$ is $\sqrt{q}\lambda_{\mathrm{src}}$, so its emission rate is $q h_f$.

### Capturing a prescribed mode

Start a receiver oscillator in vacuum and place it downstream. Its final input-dependent operator follows from the same Langevin equation:

$$
a_{\mathrm{rec}}(\infty)
=-\int_0^\infty
\lambda_{\mathrm{rec}}(t)^*
\exp\left[-\frac12\int_t^\infty
\lvert\lambda_{\mathrm{rec}}(s)\rvert^2ds\right]
b_{\mathrm{in}}(t)dt.
$$

The homogeneous initial-oscillator contribution vanishes in the ideal capture limit. Choose

$$
\lambda_{\mathrm{rec}}(t)=-\frac{f(t)}{\sqrt{C_f(t)}}.
$$

Now $\lvert\lambda_{\mathrm{rec}}\rvert^2=C_f'/C_f$, and the exponential in the integral equals $\sqrt{C_f(t)}$. Thus

$$
a_{\mathrm{rec}}(\infty)
=\int_0^\infty f(t)^*b_{\mathrm{in}}(t)dt
=a_f.
$$

The receiver stores the selected mode's complete oscillator state. Orthogonal outgoing modes remain outside it. These are ideal transfer identities: a zero denominator requires the appropriate support limit, and a bounded physical coupling requires its own approximation analysis.

**Conjugation when reading the anchor.** Its Eqs. (7) and (17) display $g_u=u^{\ast}/\sqrt{S_u}$ and $g_v=-v^{\ast}/\sqrt{C_v}$. The formulas above are derived for the explicitly defined jump coefficient $\lambda$. Translate each operator equation using that definition; do not identify every printed coupling symbol by an unchecked global substitution.

For a simple phase check, take $0\lt\kappa$ and real $\omega$. The normalized modes $f(t)=\sqrt{\kappa}e^{-\kappa t/2}e^{-i\omega t}$ and $f(t)^*$ have identical intensities, but

$$
\lvert\langle n_f\mid n_{f^*}\rangle\rvert^2
=\left(\frac{\kappa^2}{\kappa^2+4\omega^2}\right)^n.
$$

Conjugating the intended envelope can therefore change the target state substantially even when every intensity plot is unchanged.

### Preserve the direction of the cascade

For an upstream component $A$ and downstream component $B$, use their declared jumps to form

$$
L_{\mathrm{tot}}=L_A+L_B,
\qquad
H_{\mathrm{cas}}=\frac{i}{2}
\left(L_A^\dagger L_B-L_B^\dagger L_A\right).
$$

The joint master equation contains both the Hamiltonian $H_A+H_B+H_{\mathrm{cas}}$ and the dissipator $\mathcal D[L_{\mathrm{tot}}]$, where

$$
\mathcal D[L]\rho
=L\rho L^\dagger
-\frac12\left(L^\dagger L\rho+\rho L^\dagger L\right).
$$

The cross terms cancel the influence of $B$ on $A$ while retaining the influence of $A$ on $B$. A shared dissipator alone would not implement this directionality. For native Dicke emission, the physical upstream component is the initially excited emitter ensemble; no virtual incident source is needed.

For several receivers, the anchor's Section III and Appendix account for how an upstream receiver reshapes the field seen downstream. Independently inserting the original orthogonal envelopes into the single-receiver formula does not generally perform that construction.

**Map connection:** [M05](MILESTONES.md#m05), [M07](MILESTONES.md#m07), [M08](MILESTONES.md#m08), and later [M26](MILESTONES.md#m26).

## 4. A populated mode and a Fock state are different claims

The first-order correlation determines the mean occupation of any mode:

$$
G^{(1)}(t,s)=\langle b^\dagger(t)b(s)\rangle,
\qquad
\langle a_f^\dagger a_f\rangle
=\int_0^\infty\int_0^\infty
f(t)f(s)^*G^{(1)}(t,s)dt ds.
$$

Diagonalizing this quadratic form identifies the most populated one-photon modes. Maximizing it answers an occupation question. The project asks for the probability of the complete Fock target:

$$
F^\star(\rho_n)
=\sup_{\Vert f\Vert_2=1}
\langle n_f\lvert\rho_n\rvert n_f\rangle.
$$

Here $\rho_n$ is normalized within the sector containing exactly $n$ photons. The fidelity is squared overlap for a pure state.

### What a selected receiver measures

If the complete field has exactly $N$ photons, the selected oscillator's reduced state is diagonal in photon number:

$$
\rho_f=\sum_{j=0}^N P_f(j)\lvert j\rangle\langle j\rvert.
$$

Different oscillator occupations require different photon numbers in the complement, so tracing that complement removes their coherences. In this fixed-total-number setting,

$$
\langle N_f\lvert\rho_N\rvert N_f\rangle=P_f(N),
\qquad
\frac{\langle a_f^\dagger a_f\rangle}{N}
=\frac1N\sum_{j=0}^N jP_f(j).
$$

The first identity holds because occupation $N$ in the receiver leaves no photons elsewhere. It does not follow from the mean occupation alone.

For an explicit example, let $f$ and $g$ be orthogonal and $N\ge2$. Compare

$$
\rho_A=\lvert(N-1)_f,1_g\rangle\langle(N-1)_f,1_g\rvert
$$

with

$$
\rho_B=\frac{N-1}{N}\lvert N_f\rangle\langle N_f\rvert
+\frac1N\lvert N_g\rangle\langle N_g\rvert.
$$

Both have the same first-order correlation: mean occupations $N-1$ and $1$ in the two modes, with no first-order cross coherence. Yet their fidelities to the chosen target $\lvert N_f\rangle$ are respectively zero and $(N-1)/N$. These are fixed-mode comparisons, not claims about their optimized fidelities.

Three distinctions will recur:

- For **variable total photon number**, the receiver probability $P_f(n)$ can include extra photons in other modes. The global target yield requires both occupation $n$ in $f$ and vacuum in the complement.
- A **reduced state for $k$ particles**, $\rho_N^{(k)}$, traces particle coordinates from a fixed-number field. It differs from the oscillator state $\rho_f$, which traces orthogonal modes and includes several number sectors.
- If the desired sector occurs with probability $p_n$, its unconditional target yield is $Y_n^\star=p_nF^\star(\rho_n)$. Conditional fidelity, acceptance, and their product are separate quantities.

**Canonical references:** `eq:fidelitydef` in `sec:model`; the reduced-state identity `eq:rdmlower` in “Uniform attenuation,” `sec:attenuation`. **Map connection:** [M03](MILESTONES.md#m03), [M06](MILESTONES.md#m06), [M08](MILESTONES.md#m08).

## 5. Replace the oscillator by the Dicke ladder

The native model has vacuum input, one desired Markov output, complete emission, and $N$ fully excited identical two-level emitters in the symmetric spin sector:

$$
L_{\mathrm{out}}=\sqrt{\Gamma}J_-.
$$

After $m$ photons have been emitted,

$$
r_m=\Gamma(m+1)(N-m),
\qquad
0\le m\lt N.
$$

The factor $N-m$ counts remaining excitations. The additional collective factor $m+1$ makes this different from the oscillator rate $(N-m)h_f(t)$. It also creates the acceleration of the burst.

With zero Hamiltonian, every interval on a fixed ladder level contributes a no-jump amplitude $e^{-r_m\Delta t/2}$, and the next desired jump contributes $\sqrt{r_m}$. For ordered detection times $0=t_0\lt t_1\lt\cdots\lt t_N$,

$$
A_{\mathrm{ord}}(t_1,\ldots,t_N)
=\prod_{j=1}^N
\sqrt{r_{j-1}}
\exp\left[-\frac{r_{j-1}}2(t_j-t_{j-1})\right].
$$

Its squared modulus is a normalized density on the ordered domain. The symmetric-coordinate wavefunction is $A_{\mathrm{ord}}/\sqrt{N!}$, extended to every ordering. This factorial is essential: the full orthant contains $N!$ equivalent orderings.

In dimensionless coordinates $\tau_i=\Gamma t_i$, the canonical result is

$$
\psi_N(\boldsymbol\tau)
=\sqrt{N!}
\exp\left[
-\frac12\sum_i\tau_i
-\frac12\sum_{i\lt j}\lvert\tau_i-\tau_j\rvert
\right],
\qquad
\int\lvert\psi_N\rvert^2d^N\tau=1.
$$

The physical-time wavefunction has the additional factor $\Gamma^{N/2}$. In this convention the Fock target has wavefunction $\prod_i\widetilde f(\tau_i)$, and

$$
F_N[\widetilde f]
=\left\lvert
\int\psi_N(\boldsymbol\tau)
\prod_i\widetilde f(\tau_i)^*d^N\tau
\right\rvert^2.
$$

The native amplitude is positive. The triangle inequality therefore permits replacing a trial mode by its absolute value when maximizing this overlap. No assumption that the actual photon times are independent has been made.

**Canonical reference:** “Exact emitted wavefunction,” `sec:wave`, `eq:wave`. **Map connection:** [M09](MILESTONES.md#m09), [M10](MILESTONES.md#m10).

## 6. Two probability arguments determine the native exponent

### A product trial gives a lower bound

Set $P_N=\lvert\psi_N\rvert^2$, choose a one-photon probability density $p$, and put $Q_p(\boldsymbol\tau)=\prod_i p(\tau_i)$. For the trial mode $\sqrt p$, the amplitude is a classical affinity:

$$
\langle N_{\sqrt p}\mid\Psi_N\rangle
=\int\sqrt{P_NQ_p}d^N\tau.
$$

Writing the integrand as an expectation under $Q_p$ and applying Jensen's inequality gives

$$
F_N^\star\ge F_N[\sqrt p]
\ge e^{-D(Q_p\Vert P_N)}.
$$

The direction of the relative entropy matters: the expectation is under the product trial $Q_p$. For the exactly normalized choice

$$
p_N(\tau)=\frac{N^2e^{N\tau}}{(e^{N\tau}+N-1)^2},
$$

the theory evaluates that relative entropy explicitly and obtains

$$
F_N^\star\ge
\frac{e^NN!}{N^{N^2/(N-1)}}
\sim\sqrt{\frac{2\pi}{N}},
\qquad N\ge2.
$$

This pulse minimizes the product relative-entropy objective. That does not establish that it maximizes the true overlap, because Jensen's inequality need not be an equality.

**Canonical reference:** “Constructive lower bound,” `sec:lower`, `eq:kl`, `eq:pulse`, `eq:lower`. **Map connection:** [M12](MILESTONES.md#m12), [M15](MILESTONES.md#m15).

### Every trial mode supplies an upper-bound measurement

Choose a median time $T$ of the proposed mode's intensity. A Fock target has independent arrival coordinates with that density, so its number of photons before $T$ has probabilities

$$
b_N(m)=2^{-N}\binom Nm.
$$

Let $p_m(T)$ denote the native source's count probabilities. Projecting both states onto the same temporal count sectors gives

$$
\lvert\langle N_f\mid\Psi_N\rangle\rvert
\le\sum_{m=0}^N\sqrt{p_m(T)b_N(m)}.
$$

The source's count process retains the early waiting-time uncertainty even while later rates accelerate. An arrival-density divided by dwell-rate estimate bounds its central count probabilities by order $1/N$, uniformly in $T$. The target's binomial distribution occupies a width of order $\sqrt N$. Combining these facts bounds the affinity amplitude by order $N^{-1/4}$, hence the squared fidelity by order $N^{-1/2}$. The full proof controls the tails and constants uniformly over the proposed mode.

Together, the two arguments establish

$$
\sqrt{2\pi}
\le\liminf_{N\to\infty}\sqrt N F_N^\star
\le\limsup_{N\to\infty}\sqrt N F_N^\star
\le\frac{4\sqrt{2\pi}}e.
$$

The result is $F_N^\star=\Theta(N^{-1/2})$. Neither bounding constant is an established exact prefactor, and an overlap computed for one mode is an achievable value rather than an optimization certificate.

**Canonical references:** “Uniform upper bound from temporal photon counts,” `sec:upper`, `eq:countfidelity`, `eq:dwell`; main theorem `eq:main`. **Map connection:** [M11](MILESTONES.md#m11), [M13](MILESTONES.md#m13), [M16](MILESTONES.md#m16), [M17](MILESTONES.md#m17).

## 7. Read each resource change as a change of quantum state

### Partial excitation and a recorded prefix

For $M$ emitters initially in a symmetric Dicke state with $n$ excitations, define $a=M-n+1$. The rates are

$$
r_m=\Gamma(n-m)(a+m).
$$

The partial-source family makes the excitation resource explicit. Near full inversion, $a=o(M)$ gives $F_{M,n}^\star=\Theta(\sqrt{a/M})$; in the dilute regime $n/M\to0$, the fidelity tends to one. An arbitrary subset of excited atoms is not the assumed symmetric preparation.

With perfect detection, time resolution, and immediate switching, detecting and consuming the first $r$ photons of a fully inverted source prepares this family with $M=N$, $n=N-r$, and $a=r+1$. Here $0\le r\lt N$. Referring the retained pulse to the recorded time of click number $r$ removes the random translation accumulated before that event; for $r=0$, use the preparation time. Thus

$$
F_{\mathrm{prefix}}(N,r)=F_{N,N-r}^\star.
$$

A sublinear prefix has fidelity $\Theta(\sqrt{(r+1)/N})$ and cannot maintain a positive limiting fidelity. A fixed fractional prefix can: consuming half the photons gives the **asymptotic lower bound** $e/(2\sqrt2)\approx0.9611$. This is neither an exact optimum nor a finite-size equality. Discarding early light without retaining and using the timing record defines a different state.

Detector efficiency and switching latency affect the yield for a predetermined retained photon number. The stopping rule routes the field a fixed delay $\Delta\ge0$ after the detector registers click number $r$, with $1\le r\lt N$ and efficiency $0\lt d\le1$. Assume independent prefix detection, no other source loss, and continued native emission during the delay. For the target containing $N-r$ photons, aligned to the actual switch time, the exact yield factor in `eq:prefixcost` is $d^r e^{-\Gamma(N-r)(r+1)\Delta}$ per initial attempt. A latency scale involving $\Gamma N^2$ requires both the consumed and retained photon numbers to be macroscopic.

**Canonical references:** “Dependence on the initial excitation,” `sec:partial`, `eq:affine`, `eq:realascaling`, `eq:dilutefidelity`; “Detect a prefix,” `sec:prefix`, `eq:prefixidentity`, `eq:prefixfraction`, `eq:prefixcost`. **Map connection:** [M18](MILESTONES.md#m18), [M19](MILESTONES.md#m19), [M23](MILESTONES.md#m23), [M24](MILESTONES.md#m24).

### Uniform attenuation

Uniform optical attenuation traces photons without selecting a temporal mode or retaining a useful emission-time record. Apply it to the ideal native field with vacuum in the unused port and fixed transmission $0\lt\eta\lt1$. Conditioning on $k$ survivors gives the normalized particle reduction $\rho_N^{(k)}$. Its optimized fidelity obeys a universal bound $F_{N\to k}^\star\le C/\sqrt{k}$ for $1\le k\le N$. For $k/N$ tending to a positive fraction, it remains $\Theta(N^{-1/2})$.

The probability of the sector is binomial. Combining its probability with conditional mode fidelity gives an unconditional optimum of order $N^{-1}$ when both the target number and mode may be selected. This distinction explains why fewer photons after unobserved loss do not automatically reproduce the prefix protocol.

**Canonical reference:** “Uniform attenuation,” `sec:attenuation`, `eq:binomialloss`, `eq:survivor`, `eq:anynumber`. **Map connection:** [M20](MILESTONES.md#m20).

### Independent local atomic decay

Local channels $L_i=\sqrt{\gamma}\sigma_i^-$ change the trajectory model itself. Requiring all $N$ desired photons selects histories with no local jump. For constant rates, set $\epsilon=\gamma/\Gamma$. Their probability is

$$
p_0=\prod_{j=1}^N\frac{j}{j+\epsilon}.
$$

The no-local-jump amplitude acquires the factor $e^{-\gamma\sum_i t_i/2}$. After normalization, it belongs to the partial-source distribution family with real parameter $a=1+\epsilon$; the associated $M=N+\epsilon$ is a distribution parameter, not a fractional emitter count.

At fixed $\epsilon$, the conditional fidelity still scales as $\Theta(N^{-1/2})$, while the unconditional target yield is $\Theta(N^{-\epsilon-1/2})$. Conditioning strongly enough to maintain nonvanishing native-source fidelity requires $\epsilon=\Omega(N)$ and entails at least exponential suppression of acceptance.

A number sector is a mathematical conditioning event. Destructively counting all desired photons identifies that event retrospectively; a usable herald must leave the desired photons available and provide an appropriate success flag. Sectors containing fewer photons after local atomic decay are not automatically the uniform-attenuation particle reductions.

**Canonical reference:** “Independent local decay,” `sec:local`, `eq:localprob`, `eq:localkernel`, `eq:fixedlossyield`, `eq:strongF`, `eq:strongP`. **Map connection:** [M21](MILESTONES.md#m21), [M22](MILESTONES.md#m22).

## 8. Return to the oscillator to understand the control boundary

The virtual source supplied a precise benchmark: each remaining oscillator excitation contributes the same hazard. For a single coherent Markov ladder with vacuum input and complete emission to emit exactly $\lvert N_f\rangle$, the project proves the necessary and sufficient rate condition on reachable levels and times, almost everywhere,

$$
r_m(t)=(N-m)h_f(t),
$$

together with compatible trajectory phases. The rate condition also follows directly from order statistics: after $m$ arrivals, the earliest of the $N-m$ remaining independent photon times has hazard $(N-m)h_f$.

This explains three different control statements.

First, in the lossless symmetric model, a common deterministic collective-rate envelope merely changes the clock of the native wavefunction, provided emission completes. A common lossless temporal-mode transformation similarly changes the basis in which the optimum is sought. Neither improves the optimized fidelity. At fixed jump amplitudes, diagonal Hamiltonians and jump phases cannot improve the optimum over the positive, phase-free amplitude. This restriction covers excitation-preserving emitter Hamiltonians within the symmetric spin sector; adding a cavity, ancillary levels, or other spin sectors changes the model. If physical local loss stays fixed while $\Gamma(t)$ is shaped, the no-local-jump weighting changes; the constant ratio case $\gamma(t)=\epsilon\Gamma(t)$ is a different stated model.

Second, if rates are constrained by the native cap

$$
0\le r_m(t)\le\Gamma(m+1)(N-m),
$$

exact Fock factorization forces $h_f(t)\le\Gamma$. The mean final emission time is then at least $H_N/\Gamma$, where $H_N=\sum_{j=1}^N1/j$. Native emission instead takes $2H_N/[\Gamma(N+1)]$ on average.

Third, that exact-purity penalty cannot be extended to every sequence approaching unit fidelity. The canonical capped construction uses an **abstract coherent excitation-dependent coupling** and attains

$$
F_N[f]\ge1-O(N^{-3}),
\qquad
\mathbb E T_{\mathrm{last}}
=O\left(\frac{\ln N}{\Gamma N}\right).
$$

Its finite-size construction, fixed-local-loss acceptance bounds, and accepted-time analysis have explicit assumptions in `sec:capped`. A classical controller that measures the emitted count and updates a rate is not automatically the same quantum channel: its additional history record can remove the temporal coherence that the coherent construction preserves.

The virtual receiver is an analysis device, and the formal ladder coupling is a specified quantum model. Neither alone supplies a physical implementation or a nondestructive herald.

**Canonical references:** “Controls that cannot improve the modal fidelity,” `sec:phases`, `eq:phaserm`, `eq:isometry`; “Exact single-mode ladders,” `sec:exact`, `eq:exactcriterion`, `eq:exactslow`, `eq:nativetime`; “A capped coherent control,” `sec:capped`, `eq:cappedrates`, `eq:cappedasymptotic`, `eq:accbounds`, `eq:acceptedtime`. **Map connection:** [M25](MILESTONES.md#m25)–[M29](MILESTONES.md#m29).

## 9. Use the bridge along the learning route

Read Sections 2–4 while working through the field and pulse foundations in [M01–M08](MILESTONES.md#m01). Then use Sections 5–6 to connect the ladder, trajectories, probability arguments, and asymptotic conventions in [M09–M14](MILESTONES.md#m09).

In the second phase, follow the canonical lower and upper proofs for [M15–M17](MILESTONES.md#m15). Use Section 7 to compare the source and conditioning resources in [M18–M24](MILESTONES.md#m18), then Section 8 for the control boundary in [M25–M29](MILESTONES.md#m25). The final synthesis, [M30](MILESTONES.md#m30), connects each state and protocol to its fidelity, acceptance, timing information, and allowed control.

For reproducibility, the [verification script](../verification/check_fidelity.py) checks finite formulas and specified trial overlaps:

```bash
python3 verification/check_fidelity.py
```

Run it from the repository root. Its results support the stated algebra and implementation; the uniform optimization and asymptotic claims rest on the canonical proofs. The [README](../README.md) gives the complete project overview and research bibliography.
