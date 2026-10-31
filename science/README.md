# Coherent powers from supplied copies

The question is how many copies of an unknown pure state are needed to prepare a normalized coordinatewise power of its amplitudes while preserving the multiplied relative phases.

For every fixed integer $r\ge2$, a collective heralded construction produces the exact power with expected $O_r(S_r^{-1/r})$ consumed copies, including calibration and retries. The robust worst-case copy law is $\Theta_r(N^{1-1/r})$. The explicit construction, adaptive schedule, converse and charged implementation form one connected account.

## Reading route

| Page | Question answered |
|---|---|
| [Model and principal results](model.md) | What is supplied, what output is required, and which resources and accuracy conventions are charged? |
| [Exact coherent extraction](coherent_extraction.md) | How do multiplicity-corrected Kraus operators leave the desired state independent of the residual? |
| [Unknown-moment calibration](unknown_moment.md) | How can the algorithm select a useful batch without knowing the collision moment? |
| [Copy lower bounds](converse.md) | Why do arbitrary collective and adaptive operations still need the birthday scale in the worst case? |
| [Circuit and finite precision](implementation.md) | How are occupation compression, extraction, cleanup, gates and memory implemented and charged? |
| [Interpretation and limits](interpretation.md) | What does the result say about coherent processing, effective support and structured promises? |

For attribution and comparisons, see [related work](../references/RELATED_WORK.md). For independent finite checks and their scope, see [verification](../verification/README.md).

## Proof dependencies

The occupation expansion and validity of the Kraus instrument give the exact factorization and success identity. An occupancy union bound converts that identity into a constant-success batch at the collision scale. A first-collision pilot and renewal argument remove knowledge of the moment. A separate phase-covariant lower bound establishes the worst-case obstruction. The circuit realizes the constructive instrument using a credited coherent symmetrizer and explicit reversible cleanup.

Finite computations check the stated formulas and small circuit mappings. The asymptotic claims rest on the analytical proofs, not on numerical extrapolation.
