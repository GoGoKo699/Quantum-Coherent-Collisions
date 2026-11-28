# Quantum Coherent Collisions

## Coherent amplitude powers from unknown copies

How many copies of an unknown quantum state are needed to square, cube, or otherwise raise its amplitudes to a fixed integer power while preserving the multiplied relative phases?

For an arbitrary unknown pure state in a known basis,

```math
|\alpha\rangle=\sum_{i=1}^{N}\alpha_i|i\rangle,
```

the target is

```math
|\alpha^{[r]}\rangle
=\frac{\sum_i\alpha_i^r|i\rangle}{\sqrt{S_r}},
\qquad
S_r=\sum_i|\alpha_i|^{2r},
\qquad r\ge2.
```

A collective collision extractor produces this state exactly on heralded success in the ideal gate model. Its adaptive algorithm consumes

```math
O_r(S_r^{-1/r})
```

copies in expectation, including calibration and failed trials. No knowledge of the collision moment is required.

The optimal worst-case scale is

```math
\boxed{\Theta_r(N^{1-1/r}).}
```

A finite schedule attains this order with a hard copy budget and constant success. The lower bound already holds for flat magnitudes with arbitrary continuous phases and permits arbitrary collective processing and approximate output. For example, it applies to success at least $`1/2`$ and conditional target fidelity at least $`3/4`$ on every input, with fidelity defined as the population of the target pure state.

| Operation | Independent equality-postselection trials | Optimal collective copies |
|---|---:|---:|
| Square the amplitudes | $`\Theta(N)`$ | $`\Theta(\sqrt N)`$ |
| Cube the amplitudes | $`\Theta(N^2)`$ | $`\Theta(N^{2/3})`$ |

These are worst-case scalings for fixed power. The model supplies independent copies and allows known operations on the held registers.

## How the construction works

1. **Calibrate the batch.** Measure independent copies in the specified basis until a label has occurred `r` times. If the pilot took `tau` copies, take a fresh batch of `t = r + floor(tau / (96 r!))` unmeasured copies. [Pilot and retry rules](science/unknown_moment.md#algorithm)
2. **Test the batch coherently.** Reversibly sort its labels and mark whether exactly one run has length from `r` to `2r − 1`, with every other run shorter than `r`. Undo the counting and sorting, then measure the eligibility flag. If it passes, apply inverse symmetrization to get a clean sorted occupation list. [Eligibility and compression](science/implementation.md#2-measure-only-a-boolean-eligibility-flag)
3. **Extract and herald.** Locate the unique run coherently and route `r` of its entries to the tail by controlled swaps. Copy the tail label to the output register and clear the tail. Use the specified rotation to give the success qubit’s `1` branch its run-length-dependent amplitude, then uncompute the position and run length from the output label and residual list. Measure the success qubit. On `1`, keep the output register and discard the residual, which factors from the exact powered state. On either failure, restart with fresh pilot and batch copies. [Extraction and cleanup](science/implementation.md#4-sparse-extraction-and-cleanup)

Only the pilot copies and the two flags are measured. The resource counts include pilot copies, rejected batches, the sort and compression circuits, and the workspace for the realized batch size. Exactness holds in the ideal rotation model. [Charged resources and synthesis](science/implementation.md#6-gate-memory-and-depth-accounting)

## Mixed-state powers and source access

The ordered collision filter prepares the normalized entrywise power of an unknown density matrix from independent copies. For $`p_i=\rho_{ii}`$, its successful output is $`\rho^{\circ r}/S_r`$, where $`S_r=\sum_i p_i^r`$. Off-diagonal entries undergo the same power as the diagonal. The expected and worst-case copy laws above apply to this task as well. [Mixed-state proof](science/mixed_states.md)

For the ordered filter, prepare a uniform rank register with Hadamards and mark the ranks of `r` equal-label positions whose removal leaves every residual multiplicity below `r`. Measure only the mark. On success, route the common label, chosen positions and ordered residual into separate registers, recompute and erase the rank, and discard the positions and residual. The label register is the output. The same separate pilot and fresh-batch retries apply. [Ordered routing and rank erasure](science/mixed_states.md#exact-mixed-copy-extraction)

[Quantum Hadamard Powers](https://github.com/GoGoKo699/Quantum-Hadamard-Powers) uses the same ordered filter with reversible purification access and analyzes what changes when [controlled reflections](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/reflection_budget.md) or [ordinary forward queries](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/forward_only.md) are supplied.

## Read the scientific account

- [Model and exact guarantees](science/model.md): inputs, success, fidelity, copy budgets and scope.
- [Exact collective extraction](science/coherent_extraction.md): the instrument, residual factorization and success formula.
- [Mixed-state powers](science/mixed_states.md) gives the ordered-rank construction and its full-rank lower bound.
- [Unknown-moment adaptation](science/unknown_moment.md): calibration, exact integer batch selection and full retry cost.
- [Converse](science/converse.md): hard and expected budgets, success-weighted accuracy and exact profile-minimax bounds.
- [Implementation](science/implementation.md): charged symmetrization, reversible extraction, workspace and finite precision.
- [Interpretation](science/interpretation.md): effective support, coherent output and the limits of the result.
- [Related work and bibliography](references/RELATED_WORK.md): inherited constructions and precise access-model comparisons.

The [science entrypoint](science/README.md) connects these pages into a proof route. The profile-dependent optimality statement is exact and minimax over arbitrary phases at a fixed nontrivial amplitude profile. The robust approximate-output optimality statement is worst-case.

## Learn the project

The educational anchor is Ronald de Wolf’s [*Quantum Computing: Lecture Notes*, version 6](https://arxiv.org/abs/1907.09415v6). The [learning bridge](learning/DE_WOLF_BRIDGE.md) connects its foundations to heralded extraction, mixed-state powers and the role of source access.

The [30-milestone map](learning/MILESTONES.md) provides a common route through the complete contribution. Its **11 background/preliminaries milestones** establish the operational and probabilistic framework. Its **19 narrative/innovation milestones** connect exact pure and mixed extraction, unknown-moment adaptation, the robust converse and the charged implementation. Each milestone identifies its question, understanding target, earlier dependencies, conceptual connection and scientific references.

Use the bridge alongside the milestones for self-directed study. [The LLM reading guide](llms.txt) maps scientific questions and study topics to their authoritative files. The direct proof route above remains available independently of the learning sequence.

## Reproduce the finite checks

Python 3.10 or later is sufficient; the verification program uses only the standard library.

~~~bash
python3 verification/check_science.py
~~~

The finite checks cover pure-input factorization, ordered mixed-state extraction and rank erasure, reversible list maps, charge-block inequalities, pilot laws and the distinction between weighted and unweighted fidelity. See [verification](verification/README.md) for commands, expected results and limits.

## Scope and attribution

The power is fixed and the input copies are independent and identically prepared in a specified basis. The resource accounts charge the realized batch size, connectivity and coherent workspace. The occupation circuit uses ideal known rotations with a quantified synthesis error. The ordered circuit uses a uniform rank register and reversible routing.

Exact nonlinear powers and several collision, covariance and filtering methods are established prior work. A Fourier-support promise can already make some supplied-copy products easy. The result here is the universal arbitrary-amplitude construction and its optimal worst-case copy law. It does not assert optimality for every specially promised family or a generic application-level quantum speedup.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
