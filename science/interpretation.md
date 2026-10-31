# Meaning and limits of the copy law

[Scientific route](README.md) · [Principal results](model.md) · [Related work](../references/RELATED_WORK.md)

## From repeated samples to a coherent state

For an ordinary classical sample stream, repetitions become likely once enough potential $`r`$-tuples have accumulated. The relevant collision moment is $`S_r=\sum_i p_i^r`$, so the generalized birthday scale is $`S_r^{-1/r}`$.

A repeated classical label by itself does not solve the quantum problem. The desired state carries the unknown phases $`r\arg(\alpha_i)`$ in coherent superposition. Measuring the winning label replaces that superposition by a basis-state mixture. The exact extraction instead keeps the winning label coherent, corrects its occupation multiplicity, and removes every record that would distinguish it from the residual.

This explains both the upper and lower bounds. The algorithm turns a suitable collision sector into an exact pure target. The phase-covariant converse shows that sectors without a collision cannot supply the required coherent phase multiplication with nontrivial uniform accuracy.

## A two-level example

Let

```math
|\alpha\rangle=\sqrt{p}\,|0\rangle+
e^{i\theta}\sqrt{1-p}\,|1\rangle.
```

Squaring gives

```math
|\alpha^{[2]}\rangle
=\frac{p\,|0\rangle+e^{2i\theta}(1-p)\,|1\rangle}
{\sqrt{p^2+(1-p)^2}}.
```

The probability distribution sharpens and the relative phase doubles. In particular, measuring classical collision samples can reproduce information about $`p`$ without producing the phase $`e^{2i\theta}`$. Conversely, for a known restricted phase family the synthesis can be easier than for arbitrary continuous phases. The lower bound explicitly includes all independent continuous phases; replacing them by binary phases would change the task for even powers.

## Dimension and effective support

For a state uniform in magnitude on $`M`$ basis states,

```math
S_r=M^{1-r},\qquad
R=M^{1-1/r}.
```

The universal algorithm adapts to this effective support through the collision pilot, even if its location is unknown. In the ambient worst case, $`M=N`$, yielding the stated dimension exponent. For $`r=2`$, $`S_2`$ is the classical collision probability of the basis measurement distribution, so the scale is the square root of its inverse participation ratio.

If a nearly concentrated target can be approximated by a known basis state, a constant-error instance can be much easier. Accordingly, the robust optimality theorem is worst-case; the profile-dependent optimality statement requires exact output and minimax uncertainty over all phases. Structured Fourier promises can also make individual families easy, as explained in [the literature comparison](../references/RELATED_WORK.md).

## A resource tradeoff, not a free source

The gain in copy consumption uses collective quantum storage and processing of a batch. The quantum registers are explicitly present. The circuit does not access a bank of classical amplitudes for free and does not assume an unknown preparation inverse or source reflection.

There is no contradiction with linear quantum mechanics: the unnormalized success map is completely positive and linear on the joint input density operator. The normalized output is nonlinear in the single-copy amplitudes because the input contains several copies and the protocol conditions on a heralded event.

Likewise, this is not a direct comparison with the query complexity of algorithms supplied with stronger coherent preparation/reflection or block-encoding access. Those models expose operations that a finite collection of unknown copies does not supply for free.

## Boundaries that affect use

- **Basis choice:** the transformation is coordinatewise in a specified basis. Changing the basis changes the task and can change $`S_r`$.
- **Purity and identical copies:** exact factorization uses the tensor power of one pure state. An arbitrary mixed or drifting source is not covered.
- **Fixed degree:** constants include factorial and calibration factors depending on $`r`$. The proof does not promise favorable scaling for increasing degree.
- **Success and accuracy:** ideal heralded outputs are exact. Finite synthesis gives approximate outputs with a quantified conditional error and still-counted failure probability.
- **Memory and connectivity:** the circuit retains a realized batch and assumes the connectivity stated in the implementation. It is not a geometry-optimized architecture.
- **Application output:** the resource law concerns a prepared quantum state. Any later observable estimation, readout, source preparation or application-level comparison requires its own analysis.

These qualifications delimit a complete contribution. They are not evidence for extensions to mixed inputs, general two-source products or an unrestricted computational advantage.
