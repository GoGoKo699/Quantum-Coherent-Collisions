# Verification

[Scientific account](../science/README.md) · [Exact construction](../science/coherent_extraction.md) · [Converse](../science/converse.md) · [Circuit](../science/implementation.md)

The analytical proofs establish the asymptotic statements. The program here provides independent finite checks designed to catch normalization, multiplicity, phase, indexing and accuracy-convention errors.

## Run

Requirements: Python 3.10 or later, standard library only. No quantum simulator, NumPy, external solver or network access is needed.

From the repository root:

~~~bash
python3 verification/check_science.py
~~~

To retain the complete numerical report outside the source tree:

~~~bash
python3 verification/check_science.py --json /tmp/coherent-collision-checks.json
~~~

The program exits nonzero on a failed condition. Assertions are implemented as explicit runtime checks and remain active under optimized Python. The seed is fixed for reproducibility. Floating-point comparisons use a tolerance of $`3\times10^{-11}`$; the proof statements themselves are exact mathematical statements.

## What is checked

| Check | Independent comparison | Scope |
|---|---|---|
| Kraus instrument | Construct accepted branches in the symmetric basis and accumulate their effects | 39 cases with $`N=2,\ldots,4`$, $`r=2,\ldots,4`$, several batch sizes and complex, uniform, concentrated and zero-amplitude inputs |
| Exact output | Compare every branch and the accepted density operator with the factored powered target | Includes branches with zero norm and batches with zero success |
| Success formula | Compare the quantum calculation, multinomial identity and an ordered-label-string enumeration | Checks factorial normalization and residual occupancy |
| Reversible extraction | Execute the stated controlled suffix swaps, tail XORs and reconstruction of run records | 1,085 accepted occupation/list cases |
| Covariant converse | Build random trace-nonincreasing charge maps, verify the single-label negative-charge property and compare the overlap bound | 189 finite maps, including zero-copy and below-threshold inputs |
| Calibration | Enumerate the finite stopping-time Markov chain and compare its mean with a separate backward recurrence | 21 pilot laws, including deterministic and zero-probability labels |
| Accuracy convention | Numerically integrate the explicit one-copy qubit counterexample | Distinguishes success-weighted fidelity from unweighted conditional fidelity |

A reference run yields status **pass** with the counts above. The largest ordered-sample discrepancy is below $`4\times10^{-15}`$, and the branch-factorization discrepancy is below $`10^{-15}`$. Exact floating-point values may vary slightly by platform while remaining far below the stated tolerance.

The fidelity counterexample gives weighted fidelity $`1/2`$, unweighted conditional fidelity $`1/2+1/(3\sqrt3)\approx0.69245`$, and minimum success approximately $`0.07180`$.

## What the checks do not establish

Finite cases do not prove the large-dimension complexity law, exhaustive optimality, or novelty. Those claims depend on the proofs and literature comparisons.

The list-map test checks the new reversible extraction and cleanup on basis states. It does not execute the complete inherited Liu–Childs–Gottesman symmetrizer at elementary-gate level. That component is justified by its published construction and the charged bounded-multiplicity implementation in the scientific account. No physical-noise or hardware-performance conclusion is drawn.

Source checks and numerical tests also do not establish hosted mathematical rendering. A hosted review must inspect the actual pages at their pinned revision separately.
