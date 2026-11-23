# Exact Hadamard powers of mixed states

[Scientific route](README.md) · [Pure-state model](model.md) · [Verification](../verification/README.md)

The ordered-rank extractor from [Quantum Hadamard Powers](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/4faee71dbdc348f6a06a55c3f231afe2d2ba1a8d/science/extraction.md) extends the [exact supplied-copy guarantee](model.md) from pure states to independent copies of an arbitrary density matrix.

Fix a basis, dimension $`N\geq 2`$, and integer $`r\geq 2`$. For a density operator $`\rho`$, let $`p_i=\rho_{ii}`$, $`S_r=\sum_i p_i^r`$, and

```math
F_r(\rho)=\frac{\rho^{\circ r}}{S_r},
\qquad
(\rho^{\circ r})_{ij}=(\rho_{ij})^r.
```

The Schur product theorem makes $`\rho^{\circ r}`$ positive semidefinite. Its trace is $`S_r`$. On a pure input $`\rho=|\psi\rangle\langle\psi|`$, this is the projector onto the normalized vector with amplitudes proportional to $`\psi_i^r`$. For mixed inputs, the relative coherence $`\rho_{ij}/\sqrt{p_i p_j}`$ is raised to power $`r`$ whenever $`p_i p_j>0`$.

## Exact mixed-copy extraction

Let $`t\geq r`$, and choose a power of two $`B_r\geq\binom{2r-1}{r}`$. Append a coherent uniform rank register $`B_r^{-1/2}\sum_{k=0}^{B_r-1}|k\rangle`$ to $`\rho^{\otimes t}`$. For each basis tuple $`x`$, order lexicographically the sets $`J`$ of $`r`$ positions such that their labels all agree and the residual ordered tuple $`z=x_{[t]\setminus J}`$ has every multiplicity below $`r`$. The projective mark accepts exactly the ranks of these sets. An accepted tuple has one repeated label of multiplicity between $`r`$ and $`2r-1`$, hence at most $`\binom{2r-1}{r}`$ ranks.

The marked-pair map $`(x,k)\mapsto(y,J,z)`$ is injective, where $`y`$ is the common label and $`J`$ has rank $`k`$ in $`x`$. Conversely, every $`y`$, every $`r`$-subset $`J`$, and every admissible $`z`$ specify a valid pair by reinserting $`y`$ into the positions in $`J`$. Implement this basis isometry coherently by the reversible ordered routing, erase $`k`$ by recomputing it from the decoded data, and trace out $`J,z`$. The surviving $`(y,y')`$ element sums over equal $`J,z`$ in the bra and ket. For each pair the original tuple entry is

```math
(\rho_{yy'})^r\prod_{\ell=1}^{t-r}p_{z_\ell}.
```

The rank density-matrix entry is $`1/B_r`$, even if the ranks of $`J`$ differ in the two tuples. Define $`Q_r(L,p)`$ as the probability that every multiplicity in $`L`$ independent draws from $`p`$ is below $`r`$. The successful subnormalized output is exactly

```math
\frac{\binom tr}{B_r}Q_r(t-r,p)\,\rho^{\circ r}.
```

Its trace is $`\binom tr S_r Q_r(t-r,p)/B_r`$. Every successful output equals $`F_r(\rho)`$. The derivation uses $`\rho^{\otimes t}`$. A correlated or drifting source requires a different analysis.

The rank erasure matters because rank can reveal the output label. The symmetric-occupation Kraus map in Coherent Collisions needs its original pure-input assumption. For instance, its symmetric projection and multiplicity correction at $`r=2,t=3`$, on $`\rho=\mathrm{diag}(4/5,1/5)`$, give unnormalized diagonal $`(208/375,7/375)`$, whereas $`F_2(\rho)=\mathrm{diag}(16/17,1/17)`$. The ordered-rank circuit operates on the full tensor-product space and also gives an exact noiseless implementation for the original pure-input task. The rank register uses Hadamard gates. Reversible sorting, routing, rank erasure and uncomputation act by known basis permutations and use $`O_r(t\,\mathrm{polylog}(Nt))`$ gates per attempt. A non-dyadic batch can use tagged inactive slots in the sorting network. Only the supplied slots enter the mark.

## Copy and query consequences

The mark's success probability equals the occupation extractor's success formula for the same diagonal times the fixed factor $`C_r/(r!B_r)`$, where $`C_r=(2r-1)!/(r-1)!`$. The [first-collision pilot](unknown_moment.md) and geometric hard-budget arguments therefore transfer. Basis measurement of independent mixed inputs yields independent $`p`$-draws for the same pilot. In particular, setting $`R=S_r^{-1/r}`$, the first $`r`$-collision has mean $`O_r(R)`$ and lies in an $`r`$-dependent constant interval about $`R`$ with constant probability. A fresh batch of residual size a small fixed fraction of the pilot length then satisfies $`t=O_r(R)`$ and has constant success on that event, by $`Q_r(L,p)\geq 1-\binom Lr S_r`$. Independent retries give expected total cost $`O_r(S_r^{-1/r})`$, including pilot copies and failures, and the geometric hard-budget schedule gives $`O_r(N^{1-1/r})`$ at constant success. The existing phase-ensemble lower bound on the pure subclass supplies matching worst-case copy order at fixed sufficiently small conditional trace error.

In the reversible model, suppose $`U|0\rangle`$ is an arbitrary purification of $`\rho`$, written $`\sum_i\sqrt{p_i}|i\rangle|g_i\rangle`$ on the positive-probability labels. Keep the whole purification slot in each local state-projector test. The [existing algorithm](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/4faee71dbdc348f6a06a55c3f231afe2d2ba1a8d/science/model.md#sources-with-additional-registers) approximates the joint vector $`S_r^{-1/2}\sum_i p_i^{r/2}|i\rangle|g_i\rangle^{\otimes r}`$. Tracing the selected auxiliary registers gives $`F_r(\rho)`$ because $`\rho_{ij}=\sqrt{p_i p_j}\langle g_j|g_i\rangle`$. Trace-distance contractivity preserves the error. The same expected $`O_r(S_r^{-1/(r+1)}\log^2(1/\epsilon))`$ and hard $`O_r(N^{(r-1)/(r+1)}\log^2(1/\epsilon))`$ reversible-query guarantees follow, with conditional trace error $`\epsilon`$ and success probability at least $`1-\epsilon`$. The pure subclass again suffices for the known matching worst-case lower exponent $`1/3`$ at $`r=2`$. This algorithm requires both directions of the purification circuit and access to its auxiliary output registers.

The sister repository also analyzes the separate [controlled-reflection budget](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/reflection_budget.md) and [ordinary forward-only query model](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/forward_only.md).

## Full-rank lower bound when the tolerance resolves coherence

For flat-magnitude phase states $`|\psi_\theta\rangle=N^{-1/2}\sum_i e^{i\theta_i}|i\rangle`$, fix $`0<\eta<1`$ and let $`\rho_{\eta,\theta}=(1-\eta)|\psi_\theta\rangle\langle\psi_\theta|+\eta I/N`$. These states have full rank. Their Schur powers are $`F_r(\rho_{\eta,\theta})=a|\psi_{r\theta}\rangle\langle\psi_{r\theta}|+(1-a)I/N`$, where $`a=(1-\eta)^r`$.

Given copies of $`|\psi_\theta\rangle`$, a fixed depolarizing channel can supply copies of $`\rho_{\eta,\theta}`$. A mixed-copy protocol of hard budget $`t`$, success at least $`s_0`$, and conditional trace error $`\epsilon`$ against $`F_r(\rho_{\eta,\theta})`$ therefore has conditional population at least $`1/N+a(1-1/N)-\epsilon`$ in the pure target on this simulated input. Substitution in [converse Theorem 1](converse.md#1-definitions-and-the-hard-budget-theorem) bounds the collision probability from below by $`s_0[a-\epsilon/(1-1/N)]`$ whenever the bracket is positive. The union bound over $`r`$-subsets then yields

```math
t\geq \bigl(r!s_0[a-\epsilon/(1-1/N)]\bigr)^{1/r}N^{1-1/r}.
```

For fixed $`0\lt\epsilon\lt a`$, the order holds at sufficiently large $`N`$. For $`\epsilon\geq a(1-1/N)`$, the fixed output $`I/N`$ already meets the tolerance for every phase in this family. This distinguishes the effect of retained coherence from the density operator's rank.

The entrywise operation and the baseline $`r`$-copy equality postselection are prior work. See [Bechmann-Pasquinucci, Huttner and Gisin, 1998](https://arxiv.org/abs/quant-ph/9708040) and [Holmes et al., 2023, §II C](https://doi.org/10.1103/PhysRevResearch.5.013105). The joint result is the exact collective mixed-copy law and its comparison with reversible purification access for the same output.
