# Adapting to an unknown collision moment

[Model](model.md) · [Exact filter](coherent_extraction.md) · [Lower bounds](converse.md) · [Gate accounting](implementation.md)

The exact filter needs a batch on the scale $`R=S_r^{-1/r}`$ to have uniformly bounded success. A larger batch is not always better: several repeated labels can cause rejection. This page shows how a classical collision pilot selects a useful scale without estimating the entire distribution or learning its phases.

## Algorithm

In each independent trial:

1. Measure fresh source copies in the known basis until some label has appeared $`r`$ times. Let $`\tau`$ be the number of pilot copies consumed.
2. Request a fresh coherent batch of
   $`t=r+\lfloor\kappa_r\tau\rfloor`$ copies, with $`\kappa_r=1/(96r!)`$ as justified below. This is an exact integer division.
3. Apply the exact instrument from [coherent extraction](coherent_extraction.md). If it succeeds, return its output. Otherwise restart the complete trial with fresh copies.

Pilot labels are stored in an ordinary classical dictionary. The coherent batch is independent of all measured pilot copies. Classical measurements therefore do not erase its relative phases. No query in superposition to the dictionary is used.

The proof counts both stages and every retry.

## The first-collision scale

Let

```math
A_r=6r!,
\qquad R=S_r^{-1/r}.
```

### Lemma: the pilot has the right mean and a useful central interval

For every distribution $`p`$,

```math
\mathbb{E}\tau\le A_rR,
\qquad
\Pr[R/2\le\tau\le8A_rR]\ge3/4.
```

**Proof of the mean bound.** Embed the iid sample stream in a rate-one Poisson process, whose waiting times are independent of its labels. During any time interval of length $`R`$, the count of label $`i`$ is an independent Poisson variable with mean $`\lambda_i=Rp_i`$. Since $`p_i^r\le S_r`$, every $`\lambda_i\le1`$. Therefore

```math
\Pr[\mathrm{Pois}(\lambda_i)\ge r]
\ge e^{-1}\frac{\lambda_i^r}{r!}.
```

The probability that no label reaches $`r`$ within that interval is at most

```math
\prod_i\left(1-\frac{\lambda_i^r}{e\,r!}\right)
\le
\exp\left[-\frac{\sum_i\lambda_i^r}{e\,r!}\right]
=
\exp\left[-\frac{1}{e\,r!}\right].
```

Counts in disjoint intervals are independent. The first interval containing an internal $`r`$-collision has mean index at most $`(1-\exp[-1/(e\,r!)])^{-1}`$. For $`0\lt x\le1`$, the inequality $`1-e^{-x}\ge x/2`$ gives

```math
\left(1-\exp\left[-\frac{1}{e\,r!}\right]\right)^{-1}
\le 2e\,r!\lt 6r!=A_r.
```

A collision accumulated across intervals can only happen earlier. The expected continuous stopping time is thus at most $`A_rR`$.

Conditional on the label-determined stopping index $`\tau`$, the sum of the independent rate-one exponential waiting times has mean $`\tau`$. Hence the expected continuous stopping time equals $`\mathbb{E}\tau`$, establishing the claimed bound.

**Proof of the interval bound.** A union bound over sample subsets gives

```math
\Pr[\tau\lt R/2]\le\frac{1}{2^r r!}\le\frac18.
```

The integer endpoint causes no problem: there are fewer than $`R/2`$ draws on this event. Markov's inequality gives

```math
\Pr[\tau\gt 8A_rR]\le\frac18.
```

The complement of these two tails has probability at least $`3/4`$.

These deliberately loose bounds suffice for the resource exponent; no asymptotic birthday approximation is used. The integer constant $`A_r`$ will also make the implemented batch-size decision exact rational arithmetic.

## A constant chance of an exact coherent output

Choose

```math
\kappa_r=\frac{1}{16A_r}=\frac{1}{96r!},\qquad
q_r=1-\frac{1}{2^r r!},\qquad
b_r=\frac{(\kappa_r/2)^r q_r}{C_r}.
```

On the central calibration event, the residual size $`L=\lfloor\kappa_r\tau\rfloor`$ obeys

```math
L\le R/2,\qquad L+1\gt \kappa_r\tau\ge\kappa_rR/2.
```

Using the exact success identity,

```math
P_r(r+L,p)
=\frac{(r+L)_r S_r}{C_r}Q_r(L,p)
\ge b_r.
```

Thus one entire pilot-plus-coherent trial succeeds with probability at least

```math
p_\star=\frac34 b_r\gt 0.
```

This is an unconditional trial probability, averaged over the pilot. Individual atypical pilot outcomes need not have this lower bound. That distinction also matters in finite gate-synthesis error accounting.

Every successful quantum output is the same exact target, regardless of the pilot value. Averaging over accepted pilot histories therefore preserves the target state.

## Expected total consumption, including retries

The expected consumption in one complete trial satisfies

```math
\mathbb{E}[\tau+t]
\le(1+\kappa_r)A_rR+r
\le D_rR,\qquad
D_r=(1+\kappa_r)A_r+r.
```

Independent fresh trials have the same joint law of cost and success. Their cost and success may be correlated within a trial; independence within a trial is unnecessary. A renewal equation, or summation over independent preceding failures, gives

```math
\mathbb{E}C=
\frac{\mathbb{E}[\text{cost of one trial}]}
{\Pr[\text{one trial succeeds}]}
\le\frac{D_r}{p_\star}R
=O_r(S_r^{-1/r}).
```

Termination is almost sure because the per-trial success probability is uniformly positive. This is a Las Vegas guarantee: the ideal successful state is exact, while the total number of consumed copies is random.

The hard worst-case budget from [the geometric schedule](coherent_extraction.md#a-hard-budget-without-knowing-the-moment) is a separate guarantee. Expected instance cost should not be mislabeled as a deterministic $`O_r(R)`$ copy cap.

## Memory, gates and stopping bounds

The pigeonhole principle gives

```math
\tau\le(r-1)N+1
```

deterministically. The classical pilot dictionary has at most $`\min(N,\tau)`$ entries, each storing a label and a count below $`r`$. Its operations can be performed using ordinary balanced-tree lookup with logarithmic overhead.

The realized coherent batch has $`t=r+\lfloor\kappa_r\tau\rfloor`$ registers. Its quantum workspace is stated as a function of this realized $`t`$ in [implementation](implementation.md). The expectation of the retained batch size is $`O_r(R)`$, but this does not give a deterministic workspace cap proportional to the unknown instance scale. The deterministic bound is $`O_r(N)`$ registers.

Because every trial's $`t`$ is at most $`O_r(N)`$, logarithmic gate factors can be bounded uniformly by logarithms in $`N`$ and the target synthesis accuracy. Combined with the renewal argument, the compiled expected gate cost is near-linear in $`R`$ up to those factors, with constants depending on fixed $`r`$.

## What the calibration establishes

The pilot discovers a collision scale without tomography, coherent source access or prior knowledge of $`S_r`$. It does not estimate every amplitude, certify a Fourier promise, or identify a universal best algorithm for every structured family. The lower bound matches this scale for exact phase-minimax synthesis and in the robust worst case. [Related work](../references/RELATED_WORK.md) discusses promised families with other useful algorithms.
