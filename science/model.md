# Model and principal results

[Scientific route](README.md) · [Exact construction](coherent_extraction.md) · [Adaptive copies](unknown_moment.md) · [Converse](converse.md) · [Implementation](implementation.md)

## The quantum output

Fix a known orthonormal basis of an $N$-dimensional system with $N\ge2$ and an integer $r\ge 2$. The source supplies independent, identical copies of the unknown pure state

$$
|\alpha\rangle=\sum_{i=1}^{N}\alpha_i|i\rangle,\qquad
p_i=|\alpha_i|^2,\qquad \sum_i p_i=1.
$$

Define

$$
S_r=\sum_{i=1}^{N}p_i^r,\qquad
R=S_r^{-1/r},\qquad
|\alpha^{[r]}\rangle=\frac{\sum_i\alpha_i^r|i\rangle}{\sqrt{S_r}}.
$$

The task is to produce this normalized quantum state, together with a classical success flag. The operation depends on the specified basis. A different global phase of the input changes the output only by a global phase, so the target is well defined as a pure-state density operator.

On success, computational-basis measurement gives $q_i=p_i^r/S_r$, while the relative phases are multiplied by $r$. The output specification includes both features. A procedure that merely samples $q$ does not establish the coherent-output claim.

The state is unknown to the algorithm. No classical amplitude description, preparation unitary, inverse preparation, reflection about the source, amplitude oracle or QRAM is part of the input. Known operations on the supplied registers and source-independent ancillas are allowed. The dimension and power are known. Zeros in the amplitudes are allowed.

## Charged resources and correctness

Every consumed source copy is counted: measured calibration copies, coherent working copies and copies used in failed attempts. Classical randomization, intermediate measurements, adaptive control, ancillas and joint processing are allowed in the lower bounds. A hard budget $t$ counts all copies supplied before termination, including copies that are later discarded. A random-cost algorithm has a copy count $C$, including failed trials and any calibration.

On the success branch, let $\sigma_\alpha$ be the unnormalized output state and let

$$
p_{\mathrm{succ}}(\alpha)=\operatorname{tr}\sigma_\alpha,\qquad
F_\alpha=\frac{\langle\alpha^{[r]}|\sigma_\alpha|\alpha^{[r]}\rangle}
{p_{\mathrm{succ}}(\alpha)}
$$

when the success probability is nonzero. This $F_\alpha$ is the squared overlap convention for fidelity with a pure target. Exact heralded correctness means

$$
\sigma_\alpha=p_{\mathrm{succ}}(\alpha)
|\alpha^{[r]}\rangle\langle\alpha^{[r]}|.
$$

Exactness is a mathematical instrument statement in an ideal gate model. [Implementation](implementation.md) separates that statement from approximation over a finite universal gate set. Gate cost, explicit retained-copy storage, classical calibration memory and connectivity are accounted for there.

All asymptotic notation with a subscript $r$ permits constants depending on the fixed power. The constants provided by the proofs are conservative; the results do not claim a uniform favorable bound when $r$ grows with $N$.

## The result package

**Universal exact upper bound.** There is a source-independent heralded algorithm for every pure input with expected total copy consumption

$$
\mathbb{E}_\alpha C=O_r(R)=O_r(S_r^{-1/r}).
$$

It does not need to know $S_r$. Every successful output is exactly the required pure state in the ideal model, and the repeated algorithm terminates almost surely. The classical calibration and all retries are included. See [unknown-moment calibration](unknown_moment.md).

**Worst-case copy law.** Since $S_r\ge N^{1-r}$, the worst-case expected cost is $O_r(N^{1-1/r})$. A separate finite geometric schedule gives the same hard-budget order with constant success. Conversely, any algorithm that succeeds with a fixed positive probability and fixed sufficiently high conditional fidelity on every unknown input needs

$$
t=\Omega_r(N^{1-1/r})
$$

in the worst case. The obstruction already occurs for flat amplitudes with independent continuous phases. The lower bound also extends to expected copy consumption under the precise success-weighted accuracy condition in [the converse](converse.md). Therefore

$$
\boxed{\text{worst-case copy complexity}=\Theta_r(N^{1-1/r}).}
$$

For example, success at least $1/2$ and conditional fidelity at least $3/4$ suffice for a dimension-independent lower-bound constant when $N\ge2$. The exact upper bound is stronger than this approximate-output specification.

**Implementation.** For a coherent batch of $t$ copies, a charged circuit uses $O_r(t\,\operatorname{polylog}(Nt))$ ideal elementary gates and explicit storage for the batch, with the detailed workspace and finite-synthesis dependence stated in [implementation](implementation.md). This uses the existing repeated-list symmetrization of Liu, Childs and Gottesman as an attributed primitive. No low-depth claim for the complete new extraction circuit is needed.

**Exact profile-minimax consequence.** If an amplitude profile $p$ is fixed and known but its relative phases are arbitrary, exact constant-success synthesis requires $\Omega_r(S_r^{-1/r})$ copies whenever the target has at least two nonzero coordinates. Together with the upper bound this gives an exact phase-minimax law. The qualifier is essential: an approximate target concentrated on a known basis state can be easy, and a specially promised phase or Fourier family need not contain the hard phase ensemble.

## Baseline and scope

Elementary equality postselection on exactly $r$ copies has success probability $S_r$. Independent repetition costs $r/S_r$ copies in expectation. Its worst-case cost is $\Theta_r(N^{r-1})$. The collective construction changes this to $\Theta_r(N^{1-1/r})$.

| Fixed power | Independent equality trials, worst case | Optimal collective scale |
|---|---:|---:|
| $r=2$ | $\Theta(N)$ | $\Theta(N^{1/2})$ |
| $r=3$ | $\Theta(N^2)$ | $\Theta(N^{2/3})$ |
| General fixed $r$ | $\Theta_r(N^{r-1})$ | $\Theta_r(N^{1-1/r})$ |

This comparison concerns copy consumption for the specified coherent output. It does not establish an application-level speedup over classical computation or an improvement over a stronger oracle-query model. Nonlinear products/powers, covariance methods and several collision mechanisms are prior work; [related work](../references/RELATED_WORK.md) identifies the inherited results and the consequential distinction.

The analysis assumes identical pure-state copies. It makes no noisy-source or arbitrary mixed-state claim, no growing-power guarantee, and no corresponding general theorem for products of two unrelated arbitrary-amplitude sources. Those tasks require separate analysis.
