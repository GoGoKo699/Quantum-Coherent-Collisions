# Related work

## Scope of the contribution

For a fixed integer $`r\ge2`$, the task is to consume supplied copies of an unknown pure state
```math
|\alpha\rangle=\sum_{i=1}^{N}\alpha_i|i\rangle
```
and herald the normalized state proportional to $`\sum_i\alpha_i^r|i\rangle`$. The input model supplies no state-preparation circuit, inverse, reflection, or amplitude oracle. With $`S_r=\sum_i|\alpha_i|^{2r}`$, coherent collision powers gives an exact heralded collective transformation, expected copy cost $`O_r(S_r^{-1/r})`$ without knowing $`S_r`$, and worst-case copy complexity $`\Theta_r(N^{1-1/r})`$. The worst-case lower bound permits approximate outputs and arbitrary quantum channels.

The relevant distinction is the collective resource law for arbitrary amplitudes. Exact nonlinear state products, postselection, covariant conversion, and occupation representations all have substantial antecedents. Moreover, structured promises can permit much cheaper transformations than the general bound. In particular, the Fourier construction below is already a supplied-copy algorithm under its support promise.

## An exact Fourier-support predecessor

Huang, Nishi, Zushi, and Matsushita study Hadamard products of function-encoded states [HNZM26]. Their formal Problem 1 gives preparation oracles, but **the unamplified circuit in Figure 2 also works on supplied copies**: replace its two initial preparation calls by the two states, then retain the inverse Fourier transforms, modular addition, Fourier transform, known shift, Hadamard gates, and final postselection. No source inverse occurs in this remaining circuit. The relevant source locations are §2.2, Figure 2 and Steps 1–7, pp.4–6; the formal exact-support result is Corollary 1, p.3.

Here is the resulting transfer in explicit copy-access notation. Let $`N=2^n`$, $`M=2^m`$ with $`1\le m\le n`$, and let
```math
W=\{-M/2,\ldots,M/2-1\}\pmod N,\qquad
|\phi_W\rangle=F\Pi_WF^\dagger|\phi\rangle,
```
where $`F`$ is the quantum Fourier transform. Directly evaluating their circuit gives the unnormalized success vector
```math
\sqrt{\frac NM}\sum_i\psi_i(\phi_W)_i|i\rangle.
```
Consequently, if the Fourier support of $`\phi`$ is contained in the chosen window, its accepted output is the **exact** Hadamard product and
```math
P_{\rm Fourier}=\frac NM\sum_i|\psi_i\phi_i|^2.
```
For a square, $`\psi=\phi=\alpha`$, this is $`NS_2/M\ge1/M`$. A known bounded-width Fourier window therefore gives a dimension-independent exact copy cost for squares. This is a genuine special-case improvement over elementary two-copy postselection.

The window is information used by the algorithm. Figure 2 specifies $`M`$ in advance and centers the window at zero; a known translated window is implemented by changing the known shift. Section 2.3, pp.8–9, proposes choosing $`M`$ from a histogram using additional preparation pairs. These pilot copies must be charged in a supplied-copy interpretation. A finite histogram with a tolerance does not certify that an arbitrarily small tail is exactly zero.

Without exact support, the accepted vector contains $`\phi_W`$, not $`\phi`$. Independently of the paper's regularity estimates, if
```math
v=\psi\circ\phi,\qquad \widetilde v=\psi\circ\phi_W,
```
then
```math
\left\|\frac{v}{\|v\|}-\frac{\widetilde v}{\|\widetilde v\|}\right\|
\le \frac{2\|\psi\|_\infty\|\phi-\phi_W\|}{\|v\|},
```
whenever the normalized vectors are defined. Approximation thus requires controlling both the tail and the product normalization.

For unrestricted phases, exact Fourier support can fill all $`N`$ frequencies, so this shortcut can require $`M=N`$. The general coherent collision result operates without a Fourier promise. Its $`S_r`$-dependent upper bound is not a claim of optimality for every promised family or every individual state. The matching lower bound uses the full arbitrary-phase family, rather than a known Fourier subspace.

## Comparator map

| Work | Operational task and access | Established ingredient | Relationship to coherent collision powers |
| --- | --- | --- | --- |
| Holmes et al. [HCSS23] | Copies of input states; postselected nonlinear transformations | Arbitrary pure-state products and repeated powers | Establishes the task and elementary filter; a single $`r`$-copy attempt succeeds with $`S_r`$. Collective pooling is the additional resource improvement. |
| Huang et al. [HNZM26] | Function/Fourier promises; a fixed two-copy circuit survives from the oracle formulation | Fourier convolution and support-window postselection | Gives an exact, sometimes constant-copy restricted-family predecessor, as detailed above. |
| Rossi–Sarkar [RS26] | Unitary block-encoding access; controlled access for general polynomials | Efficient element-wise matrix powers and transforms | A block encoding is an executable operator, and its output normalization remains charged. It is not supplied-state access. |
| Guo–Mitarai–Fujii [GMF24]; Rattew–Rebentrost [RR23] | State-preparation unitaries, controlled uses and adjoints | Nonlinear amplitudes through block encodings and QSVT | Direct amplitude-transform ancestors in a stronger access model. |
| Bhateja–Esmaili–Mantri [BEM26] | Source preparations and reflections; separate supplied-copy lower bounds | Coherent collision/index erasure and birthday-sector converses | Closest collision ancestor; its upper bound is approximate and flat-magnitude, with a different charged resource. |
| Marvian–Spekkens [MS13]; Herasymenko et al. [HLVG26] | Covariant pure-state conversion; phase-state cloning from copies | Characteristic functions, occupation shifts and Choi block constraints | The representation and optimization methods are inherited; the target and the solved resource law differ. |
| Jiang–Zhang–Sun [JZS18]; Hoch et al. [HGCSS26] | Unknown qubit inputs; rational quantum-to-quantum transformations | Exact nonlinear copy filters and surplus-copy success analysis | Close finite-dimensional predecessors; no dimension-growing arbitrary-state collision threshold is supplied by those constructions. |
| Liu–Childs–Gottesman [LCG26] | Known coherent circuits on superposed repeated lists | Deterministic coherent symmetrization | An explicit implementation dependency used in reverse for occupation compression. |

## Matrix transforms and source-unitary amplitude transforms

The current version of *Quantum element-wise transforms* is arXiv:2606.06456v2, dated 30 September 2026 [RS26]. Theorem II.2, p.18, constructs a block encoding of $`A^{\circ d}`$ using $`d`$ calls to a block-encoding unitary. Theorem II.3, p.21, treats polynomial transforms using controlled calls. The amplification variants in §III charge additional access, including adjoints; their constant-success near-identity case has an additional operator promise. “Copies” of a unitary in these statements means uses of that unitary, not copies of its output state.

A useful specialization test is to set $`A=|\alpha\rangle\langle0|`$. Its element-wise power is the rank-one operator with column $`(\alpha_i^r)_i`$. Even granting the required block encoding, its successful action on $`|0\rangle`$ has squared norm $`S_r`$. Constructing the block encoding does not itself establish constant-success production of the normalized state, nor furnish the oracle from unknown copies. This distinguishes both the access and success conventions.

Two references directly connected to the amplitude task deserve separate credit. Guo–Mitarai–Fujii define their input to include a state-preparation oracle, its adjoint, and controlled versions; see Definition 1 and Theorems 4–5 [GMF24]. Rattew–Rebentrost use diagonal amplitude block encodings and importance sampling; their Theorem 3, p.9, explicitly counts controlled preparation and adjoint calls [RR23]. Their conclusion, p.19, identifies sample-based state exponentiation as a different direction. These papers provide general nonlinear-amplitude machinery, but their stated circuits do not instantiate the present copy-only instrument.

## Collision and covariance antecedents

Bhateja–Esmaili–Mantri §8.1, Theorem 8.1, gives an approximate flat-magnitude Hadamard product in $`O(N^{1/3})`$ preparation/reflection queries [BEM26]. Its mechanism already preserves product phases through a coherent collision and index removal. Section 8.2, Proposition 8.2, gives a Haar-square query lower bound, rather than an arbitrary-amplitude upper bound. Appendix A.3, Proposition A.2, bounds classical heavy-output generation from supplied Haar copies using square-free versus repeated occupation sectors. Both the coherent collision idea and a supplied-copy birthday converse therefore precede this work.

The comparison concerns consumed copies, exact output, arbitrary amplitudes and the matching copy model. The oracle-query exponent is a separate resource statement.

Marvian–Spekkens Theorem 26 and Corollary 27, §IX, p.22 of arXiv:1104.0018v2, characterize stochastic exact pure-state covariant conversion through positive-definite characteristic functions [MS13]. Substitution of the torus representations for $`t`$ copies and the phase-power target yields an occupation-packing formulation. This feasibility framework is established prior work.

Herasymenko et al. provide a particularly explicit recent comparison [HLVG26]. Section X.B, pp.34–36, derives phase-covariant Choi blocks labelled by occupation shifts and their diagonal trace constraints. Theorem X.1, p.33, optimizes $`t\to t+K`$ phase-state cloning; Theorem X.6 and Corollary X.7, p.42, analyze its fidelity scaling. Their target is many copies carrying the original phases. Here the output representation has characters $`e^{ir\theta_i}`$ on a single $`N`$-dimensional register. Substituting that target changes the optimization problem; their cloning optimum cannot be transferred unchanged.

The contribution uses this established representation language to prove a task-specific, success-weighted approximate-output bound. A successful-output fidelity must be combined with its probability of success when averaging phase-dependent instruments.

## Nonlinear filters, qubits and implementation

Holmes et al. §II.C, Figures 2–3 and Equations (7)–(12), implement Hadamard products and iterated powers through postselection [HCSS23]. Repeating disjoint $`r`$-copy attempts costs $`O_r(S_r^{-1})`$. The collective extractor replaces this baseline with $`O_r(S_r^{-1/r})`$ expected copies. Its crucial constructive property is that the multiplicity correction makes the desired output factor from every accepted residual occupation.

Quantum-to-quantum Bernoulli factories provide a second nonlinear-copy lineage. Jiang–Zhang–Sun characterize exact qubit transformations [JZS18]. Hoch et al. §III.C and Figure 2 study surplus-copy success for rational qubit transforms, including squared amplitudes; §§IV–V extend their input/function variants [HGCSS26]. These results establish nonlinear copy filters and the usefulness of surplus inputs. The dimension-growing arbitrary-$`N`$ resource law requires a different analysis.

For implementation, Liu–Childs–Gottesman **Result 2 and §IV** supply deterministic coherent symmetrization for arbitrary superpositions of lists with repetitions [LCG26]. Its inverse is the compression step. Repeated-list support and clean ancillary registers matter to the coherent extractor. The circuit accounting includes that inverse, reversible extraction, the multiplicity rotation and cleanup; the symmetrizer is credited as an imported algorithm. Finite universal gate compilation uses the standard Solovay–Kitaev construction described by Dawson and Nielsen [DN05], with the heralding probability included in the conditional error budget.

## Educational anchor

The project's single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018) [W18]**. The author's [book page](https://jhwatrous.github.io/books-and-courses.html) and [complete manuscript](https://jhwatrous.github.io/TQI.pdf) provide §2.2.2 for Choi/Kraus/Stinespring representations, §2.3 for measurements, §3.2 for fidelity, and §7.1.1 for the symmetric subspace. The [Watrous bridge](../learning/WATROUS_BRIDGE.md) translates these foundations into the project's notation and identifies the additional derivations and research dependencies. The [30-milestone map](../learning/MILESTONES.md) organizes the complete scientific route.

Watrous supplies foundations for the instrument and converse. The primary papers below supply the attributed research ingredients; they are not additional assigned educational anchors.

## Primary references and precise versions

Full bibliographic records are in [references.bib](references.bib).

- **[HCSS23]** Zoë Holmes, Nolan J. Coble, Andrew T. Sornborger, and Yiğit Subaşı. *Nonlinear transformations in quantum computation*. Physical Review Research **5**, 013105 (2023). [DOI](https://doi.org/10.1103/PhysRevResearch.5.013105); [arXiv:2112.12307v2](https://arxiv.org/pdf/2112.12307v2).
- **[HNZM26]** Xinchi Huang, Hirofumi Nishi, Tomofumi Zushi, and Yu-ichiro Matsushita. *An efficient quantum Hadamard product algorithm for functions*. [arXiv:2606.03612v1](https://arxiv.org/pdf/2606.03612v1), 2 June 2026.
- **[RS26]** Zane M. Rossi and Rahul Sarkar. *Quantum element-wise transforms*. [arXiv:2606.06456v2](https://arxiv.org/pdf/2606.06456v2), 30 September 2026.
- **[GMF24]** Naixu Guo, Kosuke Mitarai, and Keisuke Fujii. *Nonlinear transformation of complex amplitudes via quantum singular value transformation*. Physical Review Research **6**, 043227 (2024). [DOI](https://doi.org/10.1103/PhysRevResearch.6.043227); inspected [arXiv:2107.10764v2](https://arxiv.org/pdf/2107.10764v2).
- **[RR23]** Arthur G. Rattew and Patrick Rebentrost. *Non-Linear Transformations of Quantum Amplitudes: Exponential Improvement, Generalization, and Applications*. [arXiv:2309.09839v1](https://arxiv.org/pdf/2309.09839v1), 18 September 2023.
- **[BEM26]** Keshav Bhateja, Mehdi Esmaili, and Atul Mantri. *Tight Query Lower Bounds for Quantum Sampling, with an Application to Certified Randomness*. [arXiv:2610.06721v1](https://arxiv.org/pdf/2610.06721v1), 5 October 2026.
- **[MS13]** Iman Marvian and Robert W. Spekkens. *The theory of manipulations of pure state asymmetry: basic tools and equivalence classes of states under symmetric operations*. New Journal of Physics **15**, 033001 (2013). [DOI](https://doi.org/10.1088/1367-2630/15/3/033001); [arXiv:1104.0018v2](https://arxiv.org/pdf/1104.0018v2). The arXiv PDF uses the variant title ending “I: basic tools, equivalence classes, and single copy transformations.”
- **[HLVG26]** Yaroslav Herasymenko, Junqiao Lin, Philip Verduyn Lunel, and Dmitry Grinko. *Approximate cloning of structured pure states*. [arXiv:2610.06723v1](https://arxiv.org/pdf/2610.06723v1), 5 October 2026.
- **[JZS18]** Jiaqing Jiang, Jialin Zhang, and Xiaoming Sun. *Quantum-to-Quantum Bernoulli Factory*. Physical Review A **97**, 032303 (2018). [DOI](https://doi.org/10.1103/PhysRevA.97.032303); [arXiv:1712.09817v2](https://arxiv.org/pdf/1712.09817v2).
- **[HGCSS26]** Francesco Hoch, Taira Giordani, Gonzalo Carvacho, Nicolò Spagnolo, and Fabio Sciarrino. *Complexity and multifunctional variants of the quantum-to-quantum Bernoulli factories*. Physical Review Research **8**, 033003 (2026). [DOI](https://doi.org/10.1103/k8kd-58h8); [arXiv:2512.10810v1](https://arxiv.org/pdf/2512.10810v1).
- **[LCG26]** Zhenning Liu, Andrew M. Childs, and Daniel Gottesman. *Low-Depth Quantum Symmetrization*. Physical Review X **16**, 031056 (2026). [DOI](https://doi.org/10.1103/9qhy-ms2y); [journal PDF](https://journals.aps.org/prx/pdf/10.1103/9qhy-ms2y); [arXiv:2411.04019v2](https://arxiv.org/pdf/2411.04019v2).
- **[DN05]** Christopher M. Dawson and Michael A. Nielsen. *The Solovay-Kitaev algorithm*. [arXiv:quant-ph/0505030v2](https://arxiv.org/abs/quant-ph/0505030v2), 23 August 2005.
