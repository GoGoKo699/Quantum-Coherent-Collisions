# Coherent powers from supplied copies

The question is how many copies of an unknown state are needed to prepare a normalized coordinatewise power in a specified basis. On pure states this raises the amplitudes to a power and multiplies their relative phases. On mixed states it raises the density-matrix entries to that power.

For every fixed integer $`r\ge2`$, a collective heralded construction produces the exact power with expected $`O_r(S_r^{-1/r})`$ consumed copies, including calibration and retries. The robust worst-case copy law is $`\Theta_r(N^{1-1/r})`$. The explicit construction, adaptive schedule, converse and charged implementation form one connected account.

## Reading route

| Page | Question answered |
|---|---|
| [Model and principal results](model.md) | What is supplied, what output is required, and which resources and accuracy conventions are charged? |
| [Exact coherent extraction](coherent_extraction.md) | How do multiplicity-corrected Kraus operators leave the desired state independent of the residual? |
| [Exact mixed-state powers](mixed_states.md) | How does the ordered-rank circuit preserve the entrywise powers of a full tensor-product density operator? |
| [Unknown-moment calibration](unknown_moment.md) | How can the algorithm select a useful batch without knowing the collision moment? |
| [Copy lower bounds](converse.md) | Why do arbitrary collective and adaptive operations still need the birthday scale in the worst case? |
| [Circuit and finite precision](implementation.md) | How are occupation compression, extraction, cleanup, gates and memory implemented and charged? |
| [Interpretation and limits](interpretation.md) | What does the result say about coherent processing, effective support and structured promises? |

For attribution and comparisons, see [related work](../references/RELATED_WORK.md). For independent finite checks and their scope, see [verification](../verification/README.md).

## Proof dependencies

On pure inputs the occupation expansion and validity of the Kraus instrument give the exact factorization and success identity. The ordered-rank circuit proves the corresponding identity on mixed inputs by tracing out the residual and position registers after erasing the rank. An occupancy union bound converts that identity into a constant-success batch at the collision scale. A first-collision pilot and renewal argument remove knowledge of the moment. A separate phase-covariant lower bound establishes the worst-case obstruction. The occupation circuit uses a credited coherent symmetrizer and explicit reversible cleanup. The ordered circuit uses the same collision criterion with coherent rank selection.

[Quantum Hadamard Powers](https://github.com/GoGoKo699/Quantum-Hadamard-Powers) studies the same ordered filter with reversible purification access and gives the [reflection-budget](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/reflection_budget.md) and [forward-only](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/forward_only.md) proofs.

Finite computations check the stated formulas and small circuit mappings. The asymptotic claims rest on the analytical proofs, not on numerical extrapolation.
