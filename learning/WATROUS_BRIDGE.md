# From Watrous to coherent collision powers

A source supplies identical copies of an unknown pure quantum state. The task is to combine those copies into a new state whose amplitudes are the original amplitudes raised to a fixed integer power. The output must retain the corresponding relative phases. Its computational-basis distribution alone is insufficient.

The selected educational anchor is **John Watrous, _The Theory of Quantum Information_ (2018)**. Section and theorem numbers below refer to the author's [complete 2018 prepublication manuscript](https://jhwatrous.github.io/TQI.pdf), with front matter dated January 2018; the [author's book page](https://jhwatrous.github.io/books-and-courses.html) identifies the published book. The manuscript is linked, not reproduced here.

Watrous supplies the language of states, physical maps, measurements, fidelity, and symmetric subspaces. This bridge develops the connections to the particular extraction, stopping rule, circuit, and converse in this project. The [30-milestone map](MILESTONES.md) has **11 background milestones and 19 narrative milestones**. Its background joins local objects into the operational model; its narrative joins the extraction, resource analysis, and converse into the complete result. These are understanding targets for the science, independent of any reader's prior assessment.

The [model](../science/model.md) owns the exact promises and theorem statements. The [related-work account](../references/RELATED_WORK.md) distinguishes the contribution from its research antecedents.

## 1. Focused readings from the single anchor

The relevant sections are lookups within one source. They support the scientific route without requiring the entire book as a prerequisite.

| Project connection | Watrous sections and precise landmarks | Role in the bridge |
|---|---|---|
| M01–M02: basis, states, and independently supplied copies | §§1.1.1–1.1.2 and 2.1.1–2.1.2 | Vectors, operators, tensor products, and density operators. The restricted source access is specified by this project. |
| M03–M05: admissible maps, success branches, and discarded records | §§2.1.3, 2.2.1–2.2.2, and 2.3.1–2.3.2; Theorems 2.22 and 2.26; equations (2.226)–(2.228) | Kraus and Choi representations, partial traces, measurement probabilities, and normalization after a heralded outcome. |
| M06: accuracy conventions | §3.2, especially Definition 3.11, Proposition 3.13, and Theorem 3.33 | Watrous uses root fidelity. The project uses its square for a pure target. |
| M07: occupations and their multiplicities | §7.1.1; Propositions 7.1–7.2 and Example 7.4 | The normalized symmetric occupation basis and the number of distinct strings in one occupation. |
| M08: collision probabilities and expected cost | §1.2.2; union bound (1.246), expectation (1.247)–(1.251), and Markov's inequality, Theorem 1.13 | Basic probability tools. The collision pilot, Poisson argument, and renewal calculation are supplied locally. |
| M09: phase averaging and the Choi framework | §2.2.2, especially (2.65), Proposition 2.20, and Theorem 2.22 | Positive Choi matrices and their conversion to Kraus operators. The specific torus decomposition is a research ingredient developed below. |
| M10: coherent circuits and approximation | §§2.1.3 and 2.2.2; §3.3.2, Corollary 3.40 and Proposition 3.41 | Dilation, record disposal, and error control under processing. Efficient repeated-list compression and gate synthesis require the separately attributed algorithms. |
| M11 and M28–M30: the complete resource statement | The preceding foundations, [model](../science/model.md), and [interpretation](../science/interpretation.md) | Combine access, exactness, success, copy cost, gates, memory, and theorem boundaries. |

The narrative milestones M12–M27 use these foundations in the connected derivations below. The book does not claim the coherent collision algorithm, its unknown-moment calibration, or its resource lower bound.

## 2. Translate the objects before the claims

Write the input and target as

```math
|\alpha\rangle=\sum_{i=1}^{N}\alpha_i|i\rangle,\qquad
p_i=|\alpha_i|^2,\qquad
S_r=\sum_i p_i^r,\qquad
R=S_r^{-1/r},
```

```math
|\alpha^{[r]}\rangle
=\frac{\sum_i\alpha_i^r|i\rangle}{\sqrt{S_r}},
\qquad r\ge2,\quad N\ge2.
```

The basis is specified and $`r`$ is fixed. The source gives copies of $`|\alpha\rangle`$, not a unitary that prepares it. No preparation inverse, source reflection, amplitude description, or QRAM is supplied. Every measured pilot copy, coherent working copy, and failed attempt is counted.

| Watrous object or notation | Project notation | Translation |
|---|---|---|
| A vector $`u`$, its adjoint $`u^*`$, and $`uu^*`$ | $`\lvert\alpha\rangle`$, $`\langle\alpha\rvert`$, and $`\lvert\alpha\rangle\langle\alpha\rvert`$ | Vector, bra, and pure-state density operator. |
| $`\mathrm{L}(\mathcal X)`$, $`\mathrm{Pos}(\mathcal X)`$, $`\mathrm{D}(\mathcal X)`$ | Operators, positive operators, and density operators on the input space | A successful branch is positive but usually has trace below one. |
| CP Kraus terms $`A_a X A_a^*`$ | $`K_z\rho K_z^\dagger`$ | The adjoint symbols agree. The index labels a branch or an environment basis vector. |
| A bag $`\varphi\in\mathrm{Bag}(t,\Sigma)`$ and its normalized vector $`u_\varphi`$ | An occupation vector $`n`$ and $`\lvert n\rangle_{\mathrm{sym}}`$ | The multiplicity of label $`i`$ is $`n_i=\varphi(i)`$. |
| An ensemble element $`\eta(a)`$ in §2.3.2 | A successful output $`\sigma_\alpha`$ | Its trace is the branch probability; division by that trace gives the conditional state. |
| $`J(\Phi)\in\mathrm{L}(\mathcal Y\otimes\mathcal X)`$ | The output-first Choi matrix in the converse | The same unnormalized convention is used; there is no division by the input dimension. |
| $`F(\rho,\tau)`$ in Watrous | $`F_{\mathrm W}(\rho,\tau)`$ here | Root fidelity, distinguished below from the project's squared overlap. |

### Fidelity and successful weight

Let $`\beta=|\alpha^{[r]}\rangle\langle\alpha^{[r]}|`$. Watrous Definition 3.11 and Proposition 3.13 give

```math
F_{\mathrm W}(\rho,\tau)=\|\sqrt{\rho}\sqrt{\tau}\|_1,
\qquad
F_{\mathrm W}(\rho,\beta)^2
=\langle\alpha^{[r]}|\rho|\alpha^{[r]}\rangle.
```

For an unnormalized successful output $`\sigma_\alpha`$, define

```math
s_\alpha=\mathrm{Tr}\sigma_\alpha,\qquad
w_\alpha=\langle\alpha^{[r]}|\sigma_\alpha|\alpha^{[r]}\rangle.
```

When $`s_\alpha\gt0`$, the fidelity denoted $`F_\alpha`$ in the science files is

```math
F_\alpha=\frac{w_\alpha}{s_\alpha}
=F_{\mathrm W}(\sigma_\alpha/s_\alpha,\beta)^2.
```

Thus $`w_\alpha=s_\alpha F_\alpha`$, while Watrous fidelity of the subnormalized operator satisfies $`F_{\mathrm W}(\sigma_\alpha,\beta)=\sqrt{w_\alpha}`$. These quantities must not be interchanged.

The project uses trace distance $`D(\rho,\tau)=\tfrac12\|\rho-\tau\|_1`$. Theorem 3.33 translates to

```math
1-\sqrt{F_\alpha}
\le D(\sigma_\alpha/s_\alpha,\beta)
\le\sqrt{1-F_\alpha}.
```

For a pure target there is also the useful sharper lower bound $`1-F_\alpha\le D`$: measuring the target projector gives outcome probabilities $`F_\alpha`$ and one. Consequently, conditional trace distance at most $`\varepsilon`$ implies the squared-fidelity guarantee $`F_\alpha\ge1-\varepsilon`$ used in the converse.

## 3. A heralded transformation is a linear physical map

The target depends nonlinearly on the single-copy amplitudes. Physical admissibility is checked on the joint input density operator, on which the successful map is linear:

```math
\mathcal E_{\mathrm{succ}}(\rho)
=\sum_zK_z\rho K_z^\dagger.
```

By Watrous Theorem 2.22, this is completely positive. Define its effect

```math
M=\sum_zK_z^\dagger K_z.
```

For every positive input,

```math
\mathrm{Tr}\mathcal E_{\mathrm{succ}}(\rho)
=\mathrm{Tr}(M\rho).
```

It is therefore trace-nonincreasing exactly when $`M\le I`$. The equality case is the trace-preserving condition in Theorem 2.26; the inequality follows from the same trace pairing. A failure branch into a separate output sector, with operator $`\sqrt{I-M}`$, completes the physical instrument.

The normalized conditional output divides by $`\mathrm{Tr}(M\rho)`$. That normalization is where conditioning enters. There is no assertion of a deterministic nonlinear single-copy channel.

This distinction also separates existence from efficiency. A Kraus proof establishes an admissible operation. An efficient implementation still needs a circuit and a charged resource analysis.

### Why a discarded record can remove the phase

Watrous §2.1.3 supplies the partial trace. Apply it to

```math
|\Psi\rangle=\sum_i c_i|i\rangle|g_i\rangle.
```

The reduced output is

```math
\mathrm{Tr}_{G}|\Psi\rangle\langle\Psi|
=\sum_{i,j}c_i\overline{c_j}
\langle g_j|g_i\rangle\,|i\rangle\langle j|.
```

If the record states are orthogonal for different labels, the off-diagonal terms vanish. If the joint vector factors into one output vector and one common residual vector, the residual may be discarded safely. The extraction proof establishes precisely this factorization. Simply finding a collision and measuring its label does not establish it.

These foundations connect M03–M05 to the construction in M13–M14 and to the record cleanup in M19–M21.

## 4. Symmetric occupations explain the factorials

For $`n=(n_1,\ldots,n_N)`$ with nonnegative integer entries and $`\sum_i n_i=t`$, there are

```math
M_n=\frac{t!}{\prod_i n_i!}
```

distinct basis strings with those multiplicities. Watrous Proposition 7.2 normalizes their uniform sum by $`M_n^{-1/2}`$. In the project's notation,

```math
|n\rangle_{\mathrm{sym}}
=\frac1{\sqrt{M_n}}
\sum_{\substack{x\in[N]^t\\\mathrm{occ}(x)=n}}|x\rangle.
```

Every string in this sum has input amplitude $`\prod_i\alpha_i^{n_i}`$. Their equal amplitudes combine into

```math
|\alpha\rangle^{\otimes t}
=\sum_{\sum_i n_i=t}
\sqrt{\frac{t!}{\prod_i n_i!}}
\left(\prod_i\alpha_i^{n_i}\right)|n\rangle_{\mathrm{sym}}.
```

The occupations retain the complex phases. They are a coherent basis representation, not measured classical counts.

### The multiplicity-corrected instrument

Set

```math
C_r=\frac{(2r-1)!}{(r-1)!}.
```

For each residual occupation $`z`$ with $`\sum_i z_i=t-r`$ and $`0\le z_i\lt r`$, use

```math
K_z=\sum_i
\sqrt{\frac{(z_i+r)!}{z_i!\,C_r}}\,
|i\rangle\langle z+r e_i|_{\mathrm{sym}}.
```

An accepted occupation has exactly one label with multiplicity $`k\in\{r,\ldots,2r-1\}`$. The other labels occur fewer than $`r`$ times. Each accepted occupation consequently determines one distinguished label and one residual. Within each Kraus operator, different distinguished labels also have orthogonal outputs. The success effect is diagonal in the occupation basis, with eigenvalues

```math
\frac{k!}{(k-r)!\,C_r}\le1.
```

This proves trace nonincrease on the symmetric subspace. Defining the successful operators to vanish on its orthogonal complement proves it on the whole input space.

The square-root coefficient has a second role beyond admissibility. On applying the operator to the tensor-power expansion,

```math
\sqrt{\frac{(z_i+r)!}{z_i!\,C_r}}\,
\sqrt{\frac{t!}{(z_i+r)!\prod_{j\ne i}z_j!}}
=\sqrt{\frac{t!}{C_r\prod_jz_j!}}.
```

The right side is independent of the output label $`i`$. At the same time,

```math
\prod_j\alpha_j^{z_j+r\delta_{ij}}
=\left(\prod_j\alpha_j^{z_j}\right)\alpha_i^r.
```

Therefore

```math
K_z|\alpha\rangle^{\otimes t}
=\sqrt{\frac{t!}{C_r\prod_jz_j!}}
\left(\prod_j\alpha_j^{z_j}\right)
\sum_i\alpha_i^r|i\rangle.
```

Every nonzero successful branch has the same normalized target. With a coherent residual register, summing these branches gives a tensor product. Zero amplitudes cause no exception: positive powers vanish and the polynomial convention is $`\alpha_i^0=1`$.

This is the connection from the standard occupation basis in M07 to the locally proved extraction in M13–M14. [Coherent extraction](../science/coherent_extraction.md) gives the full instrument proof.

## 5. Complete example: three copies of a qubit

Use basis labels zero and one in this example. Let

```math
|\alpha\rangle=a|0\rangle+b|1\rangle,\qquad
|a|^2+|b|^2=1,
```

and take $`r=2`$, $`t=3`$, so $`C_2=6`$. Watrous Example 7.4 supplies the four normalized symmetric basis vectors. In occupation notation,

```math
|\alpha\rangle^{\otimes3}
=a^3|3,0\rangle
+\sqrt3\,a^2b|2,1\rangle
+\sqrt3\,ab^2|1,2\rangle
+b^3|0,3\rangle.
```

All four occupations pass the Boolean eligibility test. The two residuals are $`(1,0)`$ and $`(0,1)`$, and the successful operators are

```math
K_{(1,0)}
=|0\rangle\langle3,0|
+\frac1{\sqrt3}|1\rangle\langle1,2|,
```

```math
K_{(0,1)}
=\frac1{\sqrt3}|0\rangle\langle2,1|
+|1\rangle\langle0,3|.
```

Their combined effect, in the displayed occupation order, is $`\mathrm{diag}(1,1/3,1/3,1)`$. It is bounded by the identity; the complementary effect gives a valid failure outcome.

Applying the operators gives

```math
K_{(1,0)}|\alpha\rangle^{\otimes3}
=a\bigl(a^2|0\rangle+b^2|1\rangle\bigr),
```

```math
K_{(0,1)}|\alpha\rangle^{\otimes3}
=b\bigl(a^2|0\rangle+b^2|1\rangle\bigr).
```

The successful joint vector, before discarding the residual, is exactly

```math
\bigl(a^2|0\rangle+b^2|1\rangle\bigr)
\otimes
\bigl(a|1,0\rangle_Z+b|0,1\rangle_Z\bigr).
```

The residual factor has norm one, so the total success probability is

```math
P_{\mathrm{succ}}=|a|^4+|b|^4=S_2.
```

The two residual branch probabilities are $`|a|^2S_2`$ and $`|b|^2S_2`$. The failure probability is $`2|a|^2|b|^2=1-S_2`$. All probabilities therefore sum to one.

For $`a=1/\sqrt2`$ and $`b=e^{i\theta}/\sqrt2`$, success has probability one half and the normalized output is

```math
\frac{|0\rangle+e^{2i\theta}|1\rangle}{\sqrt2}.
```

The residual retains a phase $`e^{i\theta}`$, but it factors from the output, so tracing it out preserves the doubled phase. Measuring the output label instead would leave only a classical zero-or-one result.

This small example isolates the exact factorization. It is not a claim of copy savings at these parameters: elementary two-copy equality postselection also succeeds with probability $`S_2`$. The collective gain appears in the dimension-dependent batch scaling.

## 6. From exact branch amplitudes to a collision scale

For $`L=t-r`$, let $`Q_r(L,p)`$ be the probability that $`L`$ ordinary independent samples from $`p`$ contain no label repeated $`r`$ times. Summing the branch probabilities above gives

```math
P_r(t,p)
=\frac{(t)_rS_r}{C_r}\,Q_r(t-r,p),
\qquad
(t)_r=t(t-1)\cdots(t-r+1).
```

To see the classical probability inside this quantum expression, the residual sum is

```math
\sum_{\substack{\sum_i z_i=L\\z_i\lt r}}
\frac{L!}{\prod_i z_i!}\prod_i p_i^{z_i}
=Q_r(L,p).
```

These are exactly multinomial probabilities. No measurement of the coherent residual is needed to use the identity in the analysis.

Any fixed set of $`r`$ sample positions has all labels equal with probability $`S_r`$. The union bound from Watrous §1.2.2 therefore gives

```math
Q_r(L,p)\ge1-\binom Lr S_r.
```

The scale $`R=S_r^{-1/r}`$ makes the expected number of such collisions constant. For the analysis-only choice $`L=\lfloor R/2\rfloor`$,

```math
Q_r(L,p)\ge q_r:=1-\frac1{2^r r!},
\qquad
(r+L)_r S_r\ge2^{-r}.
```

One batch then succeeds with probability at least $`q_r/(2^rC_r)`$ and consumes $`O_r(R)`$ copies. An excessively large batch can fail the eligibility restriction, so this success probability is not assumed to increase with batch size.

The elementary equality filter uses exactly $`r`$ copies, accepts only the all-equal strings, and succeeds with probability $`S_r`$. Independent equality attempts consume $`r/S_r`$ copies on average. Pooling copies coherently changes the relevant exponent of the collision moment.

Convexity gives $`N^{1-r}\le S_r\le1`$, hence $`1\le R\le N^{1-1/r}`$. A finite schedule of fresh residual sizes zero and powers of two covers the unknown scale with a hard worst-case budget $`O_r(N^{1-1/r})`$. Its inclusion condition is the exact integer comparison $`(2L)^r\le N^{r-1}`$. The [geometric-schedule proof](../science/coherent_extraction.md#a-hard-budget-without-knowing-the-moment) supplies the constant-success bound.

This connects M12 and M15–M16: the known elementary primitive, the exact new success identity, and a finite hard-budget algorithm have distinct roles.

## 7. An unknown moment can be handled by a measured pilot

The instance-sensitive algorithm in M17–M18 must work without knowing $`S_r`$ or $`R`$. Its classical pilot measures fresh copies until some basis label has appeared $`r`$ times. Let $`\tau`$ be this first-collision sample count. Then it requests a separate coherent batch of size

```math
t=r+\left\lfloor\frac{\tau}{96r!}\right\rfloor.
```

This choice uses exact integer division. The pilot consumes copies and retains classical labels; the fresh coherent batch retains the source phases. No query in superposition to the pilot dictionary is required.

The probability foundation in Watrous §1.2.2 supplies expectations, independence, the union bound, and Markov's inequality. The following scale argument is local to the project.

Set $`A_r=6r!`$. Embed the sample labels in a rate-one Poisson arrival process. During an interval of length $`R`$, the count of label $`i`$ has Poisson mean $`\lambda_i=Rp_i`$. The identities

```math
\lambda_i\le1,\qquad \sum_i\lambda_i^r=1
```

imply that the probability of an internal collision during this interval is at least

```math
\Delta_r=1-\exp[-1/(e\,r!)].
```

Indeed, each label reaches count $`r`$ with probability at least $`e^{-1}\lambda_i^r/r!`$, and the different label counts are independent. Multiplying their no-collision probabilities proves the bound. Independent time intervals then give a geometric upper bound on the continuous stopping time. The arrival waiting times are independent of the label-determined stopping index, so its mean equals $`\mathbb E\tau`$. Since $`\Delta_r^{-1}\le2er!\lt A_r`$,

```math
\mathbb E\tau\le A_rR.
```

The early-collision union bound and the late-tail Markov bound give

```math
\Pr[\tau\lt R/2]\le\frac1{2^r r!}\le\frac18,
\qquad
\Pr[\tau\gt8A_rR]\le\frac18.
```

With probability at least three quarters, the chosen residual size lies below $`R/2`$ and is sufficiently large on the scale of $`R`$. More precisely, with $`\kappa_r=1/(96r!)`$ and $`L=\lfloor\kappa_r\tau\rfloor`$,

```math
L\le R/2,\qquad L+1\ge\kappa_rR/2
```

on that event. The success identity consequently gives the unconditional whole-trial lower bound

```math
\Pr[\text{pilot and coherent trial succeed}]
\ge p_\star
:=
\frac{3q_r}{4C_r}\left(\frac{\kappa_r}{2}\right)^r
\gt0.
```

This is an average over pilot histories. It is not a lower bound for every possible pilot value.

The expected cost of one complete trial is $`O_r(R)`$. On failure, the algorithm repeats the complete trial with fresh copies. If $`c`$ is the mean trial cost and $`s`$ its success probability, the mean total cost $`T`$ satisfies

```math
T=c+(1-s)T,
\qquad T=c/s=O_r(R).
```

Cost and success can be correlated within a trial. The equation only uses fresh independence of the next trial. Since every successful history has the same ideal target, accepting the first success does not change that target.

This is an expected-cost guarantee with almost-sure termination. The pilot itself obeys $`\tau\le(r-1)N+1`$, but the full number of trials is random. A deterministic instance-wise copy or workspace cap of order $`R`$ does not follow. [Unknown-moment calibration](../science/unknown_moment.md) gives the complete constants and resource accounting.

## 8. The admissible instrument needs a charged coherent circuit

Watrous's representation theorems establish physical realizability. They do not automatically give a short circuit. The implementation in M19–M22 therefore makes the following operations explicit.

**Boolean eligibility.** Reversible sorting and counting compute whether an occupation has exactly one run of length at least $`r`$ and no run of length at least $`2r`$. The circuit copies only this Boolean predicate to a flag, then reverses the counters and sorting records before measuring the flag. Accepted occupation amplitudes remain coherent. Every rejected block still consumes all its copies.

**Clean occupation compression.** The inverse of the repeated-list symmetrizer of [Liu, Childs, and Gottesman, Result 2 and §IV](https://journals.aps.org/prx/pdf/10.1103/9qhy-ms2y) converts a normalized occupation state to its sorted list with clean ancillary registers. This is an imported algorithm. Sorting and discarding comparison bits would not provide the same operation.

The bounded-multiplicity prefilter is also useful for implementation: each equal-label run has length at most $`2r-1`$. The within-run permutation resources can therefore be prepared by fixed, $`r`$-dependent circuits with known rotations. The global permutation resources use ranges known at circuit-compilation time. Neither step assumes that a state over an arbitrary quantum-specified range can be prepared for free. The stabilizer normalization $`\prod_i n_i!`$ is included; compression introduces no extra occupation weight.

**Extraction and cleanup.** On the sorted list, fixed-position comparisons find the unique long run coherently. A reversible sequence removes $`r`$ equal entries, puts their label into the output, and clears the copied tail. A rotation controlled by the original run length $`k`$ applies the success amplitude

```math
a_k=\sqrt{\frac{k!}{(k-r)!\,C_r}}.
```

The run position and length can be recomputed from the output label and the remaining sorted list. Computing them again, XORing the records, and reversing the new computation clears those records. Only the output, residual list, and success flag remain. The proven factorization then permits disposal of the residual.

**Resource meaning.** For a realized batch $`t`$, the implementation gives $`O_r(t\,\mathrm{polylog}(Nt))`$ ideal gates and explicit batch storage, with conservative width $`O_r(t(\log N+\log^2(t+1)))`$. The source-independent rotations are known exactly in the ideal model. The circuit assumes unrestricted connectivity and makes no polylogarithmic-depth claim for the full extractor. The [implementation account](../science/implementation.md) states the detailed gate, width, and depth bounds.

### Finite synthesis must respect the success probability

A finite universal gate set generally approximates the ideal rotations. Let $`A`$ and $`\widetilde A`$ be the ideal and compiled **subnormalized** successful output states, averaged over the pilot. Suppose each realized batch circuit is approximated uniformly well enough that

```math
\|A-\widetilde A\|_1\le2\delta.
```

Writing $`s=\mathrm{Tr}A\ge p_\star`$ and $`\widetilde s=\mathrm{Tr}\widetilde A`$, trace-norm contraction and normalization give

```math
D\!\left(\frac{\widetilde A}{\widetilde s},
|\alpha^{[r]}\rangle\langle\alpha^{[r]}|\right)
\le\frac{2\delta}{p_\star-2\delta}.
```

For $`0\lt\varepsilon\le1`$, choosing $`\delta\le p_\star\varepsilon/8`$ ensures conditional trace distance at most $`\varepsilon`$ and success at least $`p_\star/2`$. Conditioning separately on each pilot value would be unsound because some values have very small ideal success.

The [Dawson–Nielsen Solovay–Kitaev construction](https://arxiv.org/abs/quant-ph/0505030) is the attributed finite-synthesis ingredient. It supplies a conservative logarithmic gate overhead; it does not make an arbitrary ideal rotation exact. Controlled operations must retain the specified relative phases. Independent repetitions return the same normalized successful mixture, so their number does not accumulate conditional synthesis error.

The compiled expected copy cost remains $`O_r(R)`$, and expected gate cost is $`O_r(R\,\mathrm{polylog}(N/\varepsilon))`$. The success flag heralds the accepted branch; it does not certify zero synthesis error. Imperfect source copies and hardware noise require separate analysis.

## 9. Why arbitrary processing cannot avoid the collision scale

M23–M27 connect the channel foundations to a universal converse. Consider the flat-amplitude phase family

```math
|\alpha_\theta\rangle
=\frac1{\sqrt N}\sum_i e^{i\theta_i}|i\rangle,
\qquad
|\beta_\theta\rangle
=\frac1{\sqrt N}\sum_i e^{ir\theta_i}|i\rangle.
```

The phases vary independently and continuously. A processor using at most $`t`$ supplied copies, including adaptive measurements and discarded systems, has a successful completely positive trace-nonincreasing map $`\mathcal S`$. All accepted records and their corrections can be included before taking its output partial trace.

### Average the subnormalized map

Let $`U_\theta=D_\theta^{\otimes t}`$ on the symmetric input and $`V_\theta=D_{r\theta}`$ on the output. Average

```math
\widetilde{\mathcal S}(X)
=\int V_\theta^\dagger
\mathcal S(U_\theta XU_\theta^\dagger)
V_\theta\,d\mu(\theta),
```

where $`\mu`$ is the uniform probability measure on the phase torus. This preserves complete positivity and trace nonincrease. The original processor need not be covariant.

For $`s_\theta=\mathrm{Tr}\sigma_\theta`$ and $`w_\theta=\langle\beta_\theta|\sigma_\theta|\beta_\theta\rangle`$, the averaged conditional squared fidelity is

```math
\frac{\overline w}{\overline s}
=\frac{\int s_\theta F_\theta\,d\mu(\theta)}
{\int s_\theta\,d\mu(\theta)}.
```

It is weighted by success. The unweighted average of separately normalized outputs is a different quantity. In particular, normalizing a branch before averaging would discard information used by the converse.

### Choi blocks become occupation shifts

Watrous §2.2.2 gives the output-first Choi matrix

```math
J=\sum_{n,m}
\widetilde{\mathcal S}(|n\rangle\langle m|)
\otimes|n\rangle\langle m|.
```

It is positive semidefinite, with output partial trace bounded by the input identity. Phase covariance makes it commute with $`V_\theta\otimes\overline{U_\theta}`$. The vector $`|i\rangle\otimes|n\rangle_{\mathrm{sym}}`$ carries the phase character $`e^{i(re_i-n)\cdot\theta}`$. Integrating distinct characters gives zero, so the matrix splits into positive blocks labelled by

```math
z=n-r e_i.
```

Diagonalizing each positive block and reshaping its vectors, as in Theorem 2.22, gives Kraus operators with terms

```math
|i\rangle\langle z+r e_i|_{\mathrm{sym}}.
```

The next distinction uses the specific one-register phase-power target.

If a coordinate $`z_j`$ is negative, an admissible input occupation requires $`i=j`$. Such a block can output only one basis label and therefore has target squared overlap exactly $`1/N`$ per unit successful trace. If $`z\ge0`$, every contributing input occupation contains at least $`r`$ copies of its output label. Its input support lies in the collision sector.

Let $`s_+`$ and $`s_-`$ be the successful weights from these two sectors. Trace nonincrease bounds the first weight by the input probability of a collision:

```math
s_+\le P_{\mathrm{col}}^{(r)}(t;N),
\qquad
s_++s_-=\overline s.
```

The occupation probabilities of the flat input are the multinomial probabilities of $`t`$ uniform classical samples. Hence

```math
\overline w
\le s_++\frac{s_-}{N}
\le\frac{\overline s}{N}
+\left(1-\frac1N\right)P_{\mathrm{col}}^{(r)}(t;N),
```

```math
P_{\mathrm{col}}^{(r)}(t;N)
\le\binom tr N^{1-r}.
```

Constant success and a fixed fidelity advantage above the one-label baseline therefore require $`t=\Omega_r(N^{1-1/r})`$. The [converse](../science/converse.md) states the exact accuracy and averaging quantifiers.

The twirling framework and occupation-shift Choi methods have research antecedents, including [Marvian–Spekkens](https://arxiv.org/abs/1104.0018) and [Herasymenko et al.](https://arxiv.org/abs/2610.06723). The collision-sector comparison also has predecessors. The [related-work account](../references/RELATED_WORK.md#collision-and-covariance-antecedents) identifies what is inherited and what the present success-weighted specialization proves.

### Random cost and exact profile claims need their own qualifications

For a random copy count, cutting the algorithm off after $`t`$ copies can change the accuracy of its accepted subset. The proof therefore cuts off the unnormalized centered score $`w-s/N`$. If the phase-averaged expected consumption is $`\overline T`$, the removed successful weight is at most $`\overline T/(t+1)`$, giving

```math
\overline w-\frac{\overline s}{N}
\le\left(1-\frac1N\right)
\left(P_{\mathrm{col}}^{(r)}(t;N)
+\frac{\overline T}{t+1}\right).
```

A suitable cutoff yields the same dimension exponent for expected cost. This argument does not assume that conditioning on early termination preserves conditional fidelity.

For a known nontrivial amplitude profile and arbitrary unknown phases, exact output with a fixed positive success probability gives the stronger profile-minimax lower bound $`\Omega_r(S_r^{-1/r})`$. Exactness forces every successful positive summand onto the target ray, eliminating all single-label negative-charge contributions. This reasoning fails as a uniform approximate profile-optimality claim: a target almost concentrated on a known basis state can be approximated without discovering its phases. Profiles with support one are excluded from the exact fixed-profile lower bound.

## 10. Join the three strands

The constructive strand starts with normalized occupations and chooses a multiplicity filter that cancels their factorial imbalance. The accepted quantum output then factors from its residual, including all complex phases.

The resource strand turns that exact identity into constant success at the collision scale and uses a measured pilot to find a useful scale without knowing the moment. The circuit charges the coherent compression, record cleanup, storage, rejected copies, and finite synthesis.

The converse strand represents every allowed successful processor as a trace-nonincreasing map. Phase averaging separates sectors that can preserve the required phase coherence from sectors that only output one label. The successful coherent weight is limited by the input collision weight.

Together these establish expected exact copy cost $`O_r(S_r^{-1/r})`$ in the ideal model and the robust worst-case copy law $`\Theta_r(N^{1-1/r})`$. The exact profile-minimax law has the additional phase-family and nontrivial-support qualifications above. The construction assumes identical pure copies, a specified basis, and fixed degree. It does not by itself establish mixed-state robustness, a general two-source product algorithm, or an application-level computational speedup.

| Ingredient | Source of the ingredient | Where the full account lives |
|---|---|---|
| States, partial traces, CP/Kraus/Choi maps, measurements, fidelity, symmetric occupations | Watrous, the single educational anchor | The precise sections in the reading table |
| Nonlinear target and elementary equality postselection | Prior nonlinear-transform and quantum Bernoulli-factory work | [Related work](../references/RELATED_WORK.md#nonlinear-filters-qubits-and-implementation) |
| Multiplicity-corrected extraction and exact residual decoupling | The construction proved in this project | [Coherent extraction](../science/coherent_extraction.md) |
| Unknown-moment pilot and charged expected consumption | The calibration argument proved in this project | [Unknown moment](../science/unknown_moment.md) |
| Repeated-list symmetrization and finite gate synthesis | Liu–Childs–Gottesman and Dawson–Nielsen, used as research dependencies | [Implementation](../science/implementation.md) |
| Covariance and occupation-shift machinery; task-specific success-weighted bound | Inherited representation methods, specialized and proved for this output task | [Converse](../science/converse.md) and [related work](../references/RELATED_WORK.md) |

The source separation is part of the scientific account: standard foundations explain why the objects make sense, imported algorithms supply particular operations, and the local proofs establish the stated resource law.
