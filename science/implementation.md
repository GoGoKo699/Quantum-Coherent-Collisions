# Implementation and resource accounting

The collision extractor can be implemented with source-independent circuits on the supplied copies. Its ideal successful output is exact. A finite universal gate set gives an arbitrarily accurate heralded implementation with an explicitly controlled conditional error.

The construction uses coherent symmetrization as an inherited subroutine, followed by reversible processing of a sparse sorted list. All copies, data registers, ancillary registers, and gates are charged. The circuit does not use a quantum RAM or an oracle for preparing, reversing, or reflecting about the unknown source state. See [RELATED_WORK.md](../references/RELATED_WORK.md) for attribution and comparisons.

## 1. Instrument to implement

Let

$$
|\alpha\rangle=\sum_{i=1}^{N}\alpha_i|i\rangle,\qquad
p_i=|\alpha_i|^2,\qquad
S_r=\sum_i p_i^r,\qquad R=S_r^{-1/r},
$$

with fixed integer $r\ge2$. For a block of $t\ge r$ copies, write $L=t-r$ and

$$
C_r=\frac{(2r-1)!}{(r-1)!}.
$$

The successful Kraus operators are

$$
K_z=\sum_i
\sqrt{\frac{(z_i+r)!}{z_i!\,C_r}}\,
|i\rangle\langle z+r e_i|_{\rm sym},
\qquad |z|=L,\quad 0\le z_i<r.
$$

An accepted occupation vector therefore has exactly one label with multiplicity $k\in\{r,\ldots,2r-1\}$, and every other label has multiplicity below $r$. The implementation preserves coherence between all such occupations and all possible distinguished labels.

This section describes the circuit on the promised symmetric input $|\alpha\rangle^{\otimes t}$. A sorted list contains $t$ binary labels, rather than an array of $N$ occupation counters.

## 2. Measure only a Boolean eligibility flag

An initial projection onto the accepted occupation sector makes the needed symmetrization subroutine particularly simple. Define

$$
E(n)=1
\quad\Longleftrightarrow\quad
\#\{i:n_i\ge r\}=1
\quad\text{and}\quad
\max_i n_i<2r.
$$

The projection is implemented before occupation compression:

1. Reversibly sort the $t$ label registers, retaining every comparison record.
2. On the sorted list, compute the number of runs of length at least $r$ and the number of runs of length at least $2r$. Copy the predicate “the first count is one and the second count is zero” into a single flag.
3. Reverse the counting computation and then reverse the sorting circuit. This clears all counters, comparison records, and temporary label data.
4. Measure only the flag. Reject the whole block if it is zero.

For example, a run beginning at position $j$ has length at least $r$ precisely when it is a run start and $x_j=x_{j+r-1}$, with the obvious boundary convention. Fixed-position comparisons and reversible counters implement the scan; no indexed quantum memory access is required.

Every permutation of an occupation vector has the same predicate. Thus the successful measurement acts as

$$
\sum_n c_n|n\rangle_{\rm sym}
\longmapsto
\frac{\sum_{n:E(n)=1}c_n|n\rangle_{\rm sym}}
{\sqrt{\sum_{n:E(n)=1}|c_n|^2}}.
$$

It retains the relative amplitudes and phases of the accepted occupations. In particular, neither the distinguished label nor its multiplicity is measured. All $t$ input copies are counted even when this preliminary measurement rejects the block.

Because $K_z$ vanishes outside this sector, inserting the projection leaves the overall successful map and its success probability unchanged.

## 3. Charged coherent occupation compression

[Liu, Childs, and Gottesman, *Low-Depth Quantum Symmetrization*, Physical Review X **16**, 031056 (2026)](https://journals.aps.org/prx/pdf/10.1103/9qhy-ms2y) give a unitary symmetrizer for coherent superpositions of sorted lists with repetitions. Its inverse maps normalized symmetric occupation states to sorted lists with clean auxiliary registers. The relevant result is their superposed-input construction in Section IV, rather than a sorting circuit with its comparison record discarded. Their asymptotic construction assumes unrestricted connectivity; their paper also explains how to substitute explicit bitonic sorting networks for AKS networks.

We use the unitary on the accepted bounded-multiplicity subspace. This avoids treating preparation of a uniform state over a quantum-specified interval as a free operation.

### The two permutation resources

The symmetrization construction separates a global permutation resource from the stabilizer of a repeated list.

**Global permutations.** The strictly increasing-list subroutine prepares the uniform permutation resource using lower exceeding sequences. Its elementary uniform states have ranges $1,\ldots,j$, where $j$ is known when the circuit is compiled. Each such state has a binary preparation using a polynomial in $\log t$ gates and known rotations. The range endpoints are classical circuit constants.

**Permutations within equal-label runs.** After the eligibility projection, each run has length at most $2r-1$. For every possible start position $j$ and length $k\le2r-1$, compute coherently whether a run of exactly that length begins there. Conditional on that predicate, prepare the uniform permutation of the distinct position labels

$$
j,j+1,\ldots,j+k-1
$$

in the permutation-work register, and uncompute the predicate.

For fixed $r$, the normalized permutation state for each $k$ has constant dimension. It can be prepared by a fixed circuit of known rotations and reversible gates. Subtracting and restoring the known offset $j$ costs a polynomial in $\log t$. Although the loop considers all possible run starts, the enabled blocks on any input branch are disjoint. This constructs the stabilizer resource coherently with $O_r(t\,\mathrm{polylog}(tN))$ gates.

The stabilizer circuit has a definite positive-amplitude convention. Its inverse removes the run-dependent permutation information. No occupation-dependent phase or unmeasured permutation record is discarded.

### Normalization and reversibility

If an occupation has stabilizer size

$$
h_n=\prod_i n_i!,
$$

the global permutation resource decomposes into distinct permutations of the list and a *normalized* uniform stabilizer state. Erasing the latter leaves amplitude

$$
\sqrt{\frac{h_n}{t!}}
$$

on each of the $t!/h_n$ distinct strings. The resulting state is exactly the normalized $|n\rangle_{\rm sym}$. Consequently, the inverse compression preserves the occupation coefficient $c_n$; it does not introduce a multiplicity-dependent normalization.

This bounded-multiplicity implementation need only agree with the full symmetrizer on the accepted subspace. Every constituent gate remains a valid unitary on the full register space. The preliminary projection ensures that the input to its inverse lies in the subspace on which the clean compression identity is required.

## 4. Sparse extraction and cleanup

After inverse symmetrization, let $x_1\le\cdots\le x_t$ be the coherent sorted list. There is one run of length $k\in\{r,\ldots,2r-1\}$, beginning at position $b$, whose label will become the output.

### Find the run without measuring it

Compute $b$ and $k$ reversibly, leaving all scan workspace clean. At each fixed position $j$, form the predicate that a run begins there and its first $r$ entries agree. Exactly one such predicate is true. Controlled on it, XOR the known position $j$ and the run length obtained from the next at most $2r-1$ fixed positions into the output records; then uncompute the temporary comparisons. Position $b$ occupies $O(\log t)$ bits. This realizes the scan without a coherently indexed lookup.

### Remove the repeated entries

For $j=1,\ldots,t-r$ in increasing order, apply

$$
\operatorname{SWAP}(x_j,x_{j+r})
\quad\text{controlled on }b\le j.
$$

On the accepted domain, the first $r$ entries of the affected suffix are equal. The first $L=t-r$ registers after these swaps are therefore the sorted residual list, and the final $r$ registers all contain the distinguished label $i$.

Copy one tail label into an initially zero output register using computational-basis CNOTs. XOR that output label into each of the $r$ tail registers, clearing all of them. This operation is coherent: copying a computational label inside this reversible basis map does not measure that label.

### Apply the multiplicity filter

On a fresh success qubit, implement the controlled rotation

$$
|0\rangle_F\longmapsto
\sqrt{1-a_k^2}\,|0\rangle_F+a_k|1\rangle_F,
\qquad
a_k=\sqrt{\frac{k!}{(k-r)!\,C_r}}.
$$

There are only $r$ nonzero rotation values for fixed $r$, and $0<a_k\le1$. Their successful amplitudes are positive real numbers.

### Erase position and multiplicity information

The records $b$ and $k$ must be cleared before discarding any workspace. They can be recomputed from the output label and the residual list:

$$
b=1+\#\{j\le L:z_j^{\rm list}<i\},\qquad
k=r+\#\{j\le L:z_j^{\rm list}=i\}.
$$

Compute these counts in fresh work registers, XOR them into the original records, and reverse the new counting computation. This clears $b$, $k$, and the temporary counters. The procedure uses comparisons against each explicitly held residual register.

Finally measure the success qubit. On success, the only nontrivial quantum registers are the output label and the residual list. All comparison, position, run-length, tail, and symmetrization-work registers are clean.

## 5. Why the residual can be discarded

For

$$
|\alpha\rangle^{\otimes t}
=\sum_{|n|=t}
\sqrt{\frac{t!}{\prod_j n_j!}}\,
\prod_j\alpha_j^{n_j}|n\rangle_{\rm sym},
$$

the successful circuit amplitude at output label $i$ and residual $z$ is

$$
\sqrt{\frac{t!}{C_r\prod_j z_j!}}\,
\left(\prod_j\alpha_j^{z_j}\right)\alpha_i^r.
$$

The filter cancels the input multinomial factor exactly. Thus the successful joint state factors as

$$
\left(\sum_i\alpha_i^r|i\rangle\right)
\otimes
\left(
\sum_{\substack{|z|=L\\z_j<r}}
\sqrt{\frac{t!}{C_r\prod_j z_j!}}\,
\prod_j\alpha_j^{z_j}|z\rangle_{\rm list}
\right).
$$

Tracing out the residual leaves the exact normalized Hadamard power. Zero amplitudes cause no difficulty, with the convention $\alpha_i^0=1$.

The full block success probability, including the Boolean prefilter, remains

$$
P_{\rm succ}(t,\alpha)
=\frac{(t)_rS_r}{C_r}\,
\Pr_{\operatorname{Mult}(t-r,p)}
[\max_i z_i<r].
$$

## 6. Gate, memory, and depth accounting

Let

$$
q=\lceil\log_2\max\{N,2\}\rceil,\qquad
\ell=\lceil\log_2(t+1)\rceil.
$$

The ideal elementary gate model permits known one-qubit rotations and bounded-arity reversible gates. Toffoli and controlled-SWAP gates have constant-size decompositions into bounded-arity gates. Arbitrary connectivity is assumed.

| Component | Charged resources |
|---|---|
| Supplied coherent block | $t$ source copies in $tq$ data qubits |
| Boolean prefilter | Two reversible sorts, a run scan, and one flag measurement |
| Bitonic sorting records | $O(t\ell^2)$ auxiliary bits, cleared before disposal |
| Coherent compression | Inverse inherited symmetrization, including permutation-resource preparation and erasure |
| Bounded-run stabilizer cleanup | $O_r(t\,\mathrm{polylog}(tN))$ gates |
| Sparse extraction and record cleanup | $O_r(t(q+\ell))$ gates using a sequential scan |
| Output | One $q$-qubit state and a success flag |

A conservative bound obtained with bitonic networks and elementary reversible arithmetic is

$$
G_0(t,N)
=O_r\!\left(
t(q+\ell^2)\ell^4\log(q+\ell+2)
\right),
$$

with peak coherent width

$$
W_0(t,N)=O_r\!\left(t(q+\ell^2)\right).
$$

These are convenient upper bounds, not optimized gate counts. The key property is linear dependence on the number of explicitly held registers, up to logarithms. The known-range uniform preparations and the bounded-run conditional preparations are included.

The sequential extractor has depth $O_r(t(q+\ell))$. One may use the inherited parallel schedules for the remaining operations, or simply use the conservative total bound $D_0\le G_0$. The complete algorithm is not claimed to have polylogarithmic depth.

### Unknown-moment calibration

The [unknown-moment procedure](unknown_moment.md) measures separate source copies until the first classical $r$-fold collision, at sample count $\tau$, then chooses

$$
t=r+\left\lfloor\frac{\tau}{96r!}\right\rfloor.
$$

Thus $\kappa_r=1/(96r!)$ is rational and the block size is computed by exact integer division. $R$ is used only in the resource analysis. The coherent block consists of fresh copies.

The classical occupancy dictionary stores measured labels and counts. Its ordinary classical lookup cost is charged; it is not a quantum RAM. A balanced dictionary gives polynomial logarithmic processing overhead per sample.

For fixed $r$, calibration and independent heralded retries use $O_r(R)$ source copies in expectation. Moreover,

$$
\tau\le(r-1)N+1
$$

deterministically. This bound, together with $\mathbb E\tau=O_r(R)$, gives expected total ideal quantum gate cost $O_r(R\,\mathrm{polylog}(N))$, including rejected blocks. Classical calibration also fits this asymptotic bound in elementary bit operations.

The width bound above applies to the realized block size $t$. Without prior knowledge of $S_r$, the statement is an expected resource guarantee; it does not assert a deterministic peak width of $O_r(R\log N)$.

## 7. Finite universal synthesis and heralding error

Exactness refers to the ideal known-rotation model. A finite universal gate implementation generally gives an approximate successful state. The success flag alone does not certify zero synthesis error.

Let $p_*(r)>0$ be the proved lower bound on the success probability of one complete trial, including calibration. For each realized $t$, approximate the coherent circuit to operator-norm error at most $\delta$. It suffices to approximate each of its at most $G_0(t,N)$ nontrivial gates to error $O(\delta/G_0(t,N))$.

Use operator-norm approximation after decomposing controlled gates, with their relative phases fixed. An uncontrolled gate approximation only specified up to an arbitrary phase is insufficient when that phase can become a branch-dependent phase in a controlled operation.

The [Solovay–Kitaev synthesis algorithm of Dawson and Nielsen](https://arxiv.org/abs/quant-ph/0505030) supplies a conservative finite-set bound

$$
G_{\rm fin}(t,N,\varepsilon)
=O_r\!\left[
G_0(t,N)\,
\log^4\!\left(
2+\frac{G_0(t,N)}{p_*(r)\varepsilon}
\right)
\right],
$$

when $\delta=O(p_*(r)\varepsilon)$. More specialized synthesis can reduce this logarithmic overhead. No exact finite-gate synthesis assertion is needed.

### Condition on the aggregate trial, not each pilot outcome

Some pilot transcripts produce block sizes with very small ideal success probability. Conditioning separately on each such transcript would give an uncontrolled error amplification.

Instead, average over the classical pilot before normalizing the successful output. Let $A$ and $\widetilde A$ denote the ideal and synthesized subnormalized successful output states for a complete trial. Uniform circuit error $\delta$ implies

$$
\|A-\widetilde A\|_1\le2\delta,\qquad
|\operatorname{Tr}A-\operatorname{Tr}\widetilde A|
\le2\delta.
$$

Writing $p=\operatorname{Tr}A\ge p_*(r)$ and
$\widetilde p=\operatorname{Tr}\widetilde A$, the conditional trace distance is bounded by

$$
D\!\left(\frac{\widetilde A}{\widetilde p},
|\alpha^{[r]}\rangle\langle\alpha^{[r]}|\right)
\le\frac{2\delta}{p_*(r)-2\delta}.
$$

For $0<\varepsilon\le1$, taking $\delta\le p_*(r)\varepsilon/8$ therefore guarantees conditional trace distance at most $\varepsilon$ and success probability at least $p_*(r)/2$.

Independent complete trials have the same synthesized successful-output distribution. Repeating until the first success returns $\widetilde A/\widetilde p$; the conditional error does not accumulate with the random number of rejected trials. Expected copies remain $O_r(R)$, and expected finite-gate cost is

$$
O_r\!\left(R\,\mathrm{polylog}(N/\varepsilon)\right).
$$

These bounds address synthesis error in otherwise ideal gates, measurements, and supplied copies. They do not constitute a noise-tolerance theorem for imperfect source states or hardware.

## 8. Scope

The resource statements keep $r$ fixed. The constants in the filter, calibration, and bounded-run circuits may grow rapidly with $r$. The construction provides no uncharged classical data loading and no efficient claim for degree growing with $N$. Exact residual decoupling, Boolean prefiltering, and cleanup are necessary to the stated coherent output guarantee.
