# From de Wolf to coherent collision powers

The common learning source for Quantum Coherent Collisions and [Quantum Hadamard Powers](https://github.com/GoGoKo699/Quantum-Hadamard-Powers) is Ronald de Wolf’s [*Quantum Computing: Lecture Notes*, version 6](https://arxiv.org/abs/1907.09415v6). Use this bridge alongside the [30 milestones](MILESTONES.md). The notes supply the circuit and state framework. The linked project chapters derive the collision filter, the adaptive copy law and the phase converse.

## 1. State, basis and resource

Read §§1.2–1.4 and Appendix A.6. Fix the basis before defining a power. On a pure state, the operation changes relative phases as well as label probabilities. On a mixed state, read §15.1 and write the target explicitly in that same basis:

```math
F_r(\rho)=\frac{\rho^{\circ r}}{S_r},\qquad
(\rho^{\circ r})_{ij}=(\rho_{ij})^r,\qquad
S_r=\sum_i\rho_{ii}^r.
```

The power is applied to entries, so the chosen basis is part of the problem. The source supplies independent copies, represented jointly by $`\rho^{\otimes t}`$. A preparation unitary is a different resource because it can act on inputs other than the reset state. [Model](../science/model.md) · [Mixed states](../science/mixed_states.md)

## 2. A successful map and its residual

Use §§1.2.2–1.2.3, §15.1 and §18.3. For a measurement with a success flag, keep the accepted operator $`\sigma`$ before normalization. Its trace is the success probability. The conditional state is $`\sigma/\operatorname{Tr}(\sigma)`$ on trials with positive success probability.

In the occupation instrument, an accepted residual factors from the pure powered state. In the ordered instrument, two basis tuples with the same residual and selected positions can contribute to an off-diagonal entry of the mixed output. The rank may differ between those two tuples. Recomputing and clearing it restores the shared environment needed for their off-diagonal entry to survive the partial trace. [Pure-state factorization](../science/coherent_extraction.md#lemma-2-every-accepted-residual-gives-the-same-exact-target) · [Ordered mixed extraction](../science/mixed_states.md#exact-mixed-copy-extraction)

## 3. Collision probability and the adaptive batch

Use Appendix B.2 for probability conventions, then follow the local occupancy argument. For $`p_i=\rho_{ii}`$, a particular $`r`$-subset of independent measured labels agrees with probability $`S_r`$. A collective trial processes many subsets of one physical batch. The exact filter weights those subsets so that the normalized output is independent of the residual. The first-collision pilot estimates a useful scale without revealing labels in the fresh coherent batch. Charge the pilot copies and all rejected trials. [Exact success identity](../science/coherent_extraction.md#exact-success-probability) · [Adaptive proof](../science/unknown_moment.md)

## 4. Accuracy and the converse

Read §15.1 for measurement on a density matrix and Appendix A.5 for singular values. The project uses the conventions

```math
D(\sigma,\tau)=\tfrac12\|\sigma-\tau\|_1,\qquad
F_{\beta}(\sigma)=\langle\beta|\sigma|\beta\rangle
```

for normalized states and a pure target $`|\beta\rangle`$. To apply an overlap bound to a successful map, multiply the conditional overlap by the success probability before averaging over source phases. The occupation expansion and phase covariance argument are explained in the local proof. They track which input sectors can supply the required output coherences. [Accuracy and hard budgets](../science/converse.md#3-hard-budget-consequences-and-accuracy-quantifiers) · [Full-rank lower bound](../science/mixed_states.md#full-rank-lower-bound-when-the-tolerance-resolves-coherence)

## 5. Circuits and the sister results

Use §§1.4 and 2.1–2.2 for known gates, controlled actions and uncomputation. The copy circuit charges its realized batch and workspace. The occupation implementation uses multiplicity rotations and credits its inherited symmetrizer. The ordered circuit uses a uniform rank register and reversible basis routing. [Implementation](../science/implementation.md) · [Verification](../verification/README.md)

Sections 4.6 and 7.3 and Chapters 8–9 supply the phase-estimation, amplification, walk and block-encoding background for the sister’s spectral filter. Compare the state copies and the executable operations as separate inputs when reading the [reflection budget](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/reflection_budget.md) and [forward-only query law](https://github.com/GoGoKo699/Quantum-Hadamard-Powers/blob/main/science/forward_only.md).
