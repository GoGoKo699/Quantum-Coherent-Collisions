# Quantum Coherent Collisions

## Coherent amplitude powers from unknown copies

How many copies of an unknown quantum state are needed to square, cube, or otherwise raise its amplitudes to a fixed integer power while preserving the multiplied relative phases?

For an arbitrary unknown pure state in a known basis,

$$
|\alpha\rangle=\sum_{i=1}^{N}\alpha_i|i\rangle,
$$

the target is

$$
|\alpha^{[r]}\rangle
=\frac{\sum_i\alpha_i^r|i\rangle}{\sqrt{S_r}},
\qquad
S_r=\sum_i|\alpha_i|^{2r},
\qquad r\ge2.
$$

A collective collision extractor produces this state exactly on heralded success in the ideal gate model. Its adaptive algorithm consumes

$$
O_r(S_r^{-1/r})
$$

copies in expectation, including calibration and failed trials. No knowledge of the collision moment is required.

The optimal worst-case scale is

$$
\boxed{\Theta_r(N^{1-1/r}).}
$$

The lower bound already holds for flat magnitudes with arbitrary continuous phases and allows arbitrary collective processing, constant success, and constant-quality approximate output.

| Operation | Independent equality-postselection trials | Optimal collective copies |
|---|---:|---:|
| Square the amplitudes | $\Theta(N)$ | $\Theta(\sqrt N)$ |
| Cube the amplitudes | $\Theta(N^2)$ | $\Theta(N^{2/3})$ |

These are worst-case scalings for fixed power. The input consists of supplied copies; preparation unitaries, their inverses, source reflections, amplitude oracles, and QRAM are not supplied.

## How the construction works

The algorithm processes a batch coherently in the symmetric occupation basis. It accepts occupations with one sufficiently repeated label and applies a multiplicity correction. That correction makes the powered output factor exactly from the remaining registers. The repeated label is never measured, and the circuit clears the position and run-length records that would reveal it.

A classical first-collision pilot selects the scale of a fresh coherent batch. A separate phase-covariant argument proves that operations without enough collision weight cannot carry the required multiplied phases with nontrivial uniform accuracy.

## Read the scientific account

- [Model and exact guarantees](science/model.md): inputs, success, fidelity, copy budgets and scope.
- [Exact collective extraction](science/coherent_extraction.md): the instrument, residual factorization and success formula.
- [Unknown-moment adaptation](science/unknown_moment.md): calibration, exact integer batch selection and full retry cost.
- [Converse](science/converse.md): hard and expected budgets, success-weighted accuracy and exact profile-minimax bounds.
- [Implementation](science/implementation.md): charged symmetrization, reversible extraction, workspace and finite precision.
- [Interpretation](science/interpretation.md): effective support, coherent output and the limits of the result.
- [Related work and bibliography](references/RELATED_WORK.md): inherited constructions and precise access-model comparisons.

The [science entrypoint](science/README.md) connects these pages into a proof route.

## Reproduce the finite checks

Python 3.10 or later is sufficient; the verification program uses only the standard library.

~~~bash
python3 verification/check_science.py
~~~

The checks cover Kraus validity and exact factorization for finite complex inputs, independent ordered-sample success probabilities, reversible list extraction and cleanup, charge-block inequalities, pilot stopping distributions, and a counterexample distinguishing weighted and unweighted conditional fidelity. See [verification](verification/README.md) for commands, expected results and limits.

## Scope and attribution

The power is fixed, the inputs are identical pure states, and the circuit assumes the stated connectivity and explicit collective storage. Exactness concerns ideal known rotations; finite universal gate synthesis has a quantified conditional output error. The gate analysis specifies a circuit construction and credits the inherited symmetrizer; the verification suite is not an end-to-end gate compiler or hardware experiment.

Exact nonlinear powers and several collision, covariance and filtering methods are established prior work. A Fourier-support promise can already make some supplied-copy products easy. The result here is the universal arbitrary-amplitude construction and its optimal worst-case copy law. It does not assert optimality for every specially promised family or a generic application-level quantum speedup.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
