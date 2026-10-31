# Exact coherent collision extraction

[Model](model.md) · [Unknown-moment algorithm](unknown_moment.md) · [Circuit](implementation.md)

## Occupations retain the phases

For an occupation vector $`n\in\mathbb{Z}_{\ge0}^{N}`$ with $`|n|=\sum_i n_i=t`$, let $`|n\rangle_{\mathrm{sym}}`$ be the normalized uniform superposition of all length-$`t`$ basis strings having those occupations. The identical-copy input lies in the symmetric subspace:

```math
|\alpha\rangle^{\otimes t}
=\sum_{|n|=t}
\sqrt{\frac{t!}{\prod_i n_i!}}
\left(\prod_i\alpha_i^{n_i}\right)
|n\rangle_{\mathrm{sym}}.
```

An $`r`$-fold repetition of label $`i`$ contains the phase factor $`\alpha_i^r`$. Extracting that factor coherently requires the residual registers to become independent of the surviving label. Simply finding and measuring the repeated label would not meet the quantum-output specification.

The following instrument accomplishes the extraction with a correction for the occupation multiplicities.

## A universal instrument

Take $`t\ge r`$ and define

```math
C_r=\frac{(2r-1)!}{(r-1)!}.
```

For each residual occupation vector $`z`$ satisfying

```math
|z|=t-r,\qquad 0\le z_i\lt r\ \text{for every }i,
```

define the successful Kraus operator

```math
K_z=\sum_{i=1}^{N}
\sqrt{\frac{(z_i+r)!}{z_i!\,C_r}}\,
|i\rangle\langle z+r e_i|_{\mathrm{sym}}.
```

The operator is zero outside the symmetric subspace. Here $`e_i`$ is the $`i`$th coordinate unit vector. The complete success map is

```math
\mathcal{E}_{\mathrm{succ}}(\rho)=\sum_z K_z\rho K_z^\dagger.
```

### Lemma 1: the success map is physically admissible

The accepted occupation vectors have exactly one coordinate of size at least $`r`$. That coordinate has size $`k\in\{r,\ldots,2r-1\}`$; every other coordinate is below $`r`$.

For a given accepted $`n`$, the exceptional coordinate $`i`$ is unique, and its residual is uniquely $`z=n-r e_i`$. Thus no accepted input occupation belongs to two distinct residual terms. Within a fixed $`K_z`$, distinct $`i`$ have orthogonal output labels. Consequently

```math
\sum_z K_z^\dagger K_z
=\sum_{\substack{n\ \mathrm{accepted}\\ i\ \mathrm{exceptional}}}
\frac{n_i!}{(n_i-r)!\,C_r}
|n\rangle_{\mathrm{sym}}\langle n|.
```

The falling factorial $`k!/(k-r)!`$ increases with $`k`$ and is at most $`C_r`$ on the accepted range. Every eigenvalue is therefore in $`[0,1]`$. The sum is bounded above by the symmetric-subspace projector and hence by the identity on the full input space. A failure operator given by the positive square root of the complementary effect completes the instrument.

This argument is independent of the unknown state and includes zero amplitudes.

### Lemma 2: every accepted residual gives the same exact target

Substitute the occupation expansion into $`K_z`$. For each output coordinate $`i`$, the two factorial factors cancel:

```math
\sqrt{\frac{(z_i+r)!}{z_i!\,C_r}}\,
\sqrt{\frac{t!}{(z_i+r)!\prod_{j\ne i}z_j!}}
=\sqrt{\frac{t!}{C_r\prod_j z_j!}}.
```

The amplitude factor separates in the same way:

```math
\prod_j\alpha_j^{z_j+r\delta_{ij}}
=\left(\prod_j\alpha_j^{z_j}\right)\alpha_i^r.
```

Therefore

```math
K_z|\alpha\rangle^{\otimes t}
=
\sqrt{\frac{t!}{C_r\prod_jz_j!}}
\left(\prod_j\alpha_j^{z_j}\right)
\sum_i\alpha_i^r|i\rangle.
```

Every nonzero accepted branch is proportional to the desired state. With a coherent residual register, the entire success vector is a tensor product of the powered state and one residual vector. Discarding that residual is legitimate because of this factorization. It is not legitimate to measure the collision label or retain unremoved label-dependent sorting records.

The factorization is exact for arbitrary complex amplitudes. Use $`\alpha_i^0=1`$ in the usual polynomial convention; branches containing a positive power of a zero amplitude simply vanish.

## Exact success probability

For $`L\ge0`$, define the ordinary occupancy probability

```math
Q_r(L,p)=
\Pr_{X_1,\ldots,X_L\ \mathrm{iid}\ p}
[\text{every label appears fewer than }r\text{ times}].
```

Let $`(t)_r=t(t-1)\cdots(t-r+1)`$. Summing the squared branch norms yields

```math
P_r(t,p)=
\frac{(t)_rS_r}{C_r}\,Q_r(t-r,p).
```

Indeed, the sum over residual occupations is

```math
\sum_{\substack{|z|=L\\ z_i\lt r}}
\frac{L!}{\prod_i z_i!}\prod_i p_i^{z_i}
=Q_r(L,p),
```

and $`t!/L!=(t)_r`$. This is an exact identity, not a Poisson or large-dimension approximation.

For any particular $`r`$-subset of the $`L`$ samples, the probability that its labels all agree is $`S_r`$. A union bound over those subsets gives

```math
Q_r(L,p)\ge 1-\binom{L}{r}S_r,
```

with $`\binom{L}{r}=0`$ when $`L\lt r`$. Although the displayed right side can become negative for a very large batch, its use below is confined to the regime where it is a positive constant. Oversized batches can have low or zero success; monotonicity in batch size is not assumed.

## Constant success at the collision scale

Write $`R=S_r^{-1/r}\ge1`$, and first suppose this quantity is known. Set

```math
L=\lfloor R/2\rfloor,\qquad t=r+L.
```

Then

```math
Q_r(L,p)\ge q_r,\qquad
q_r=1-\frac{1}{2^r r!}\gt 0,
```

and

```math
(t)_r S_r
=\frac{(L+1)(L+2)\cdots(L+r)}{R^r}
\ge \frac{(L+1)^r}{R^r}
\ge 2^{-r}.
```

Thus

```math
P_r(t,p)\ge \frac{q_r}{2^r C_r}\gt 0.
```

The batch uses $`O_r(R)`$ copies, and a fixed number of independent repetitions gives any chosen constant success probability. This includes concentrated inputs with $`R`$ close to one; no large-support assumption is required.

The constants are not asserted to be optimal. In particular, at $`t=r`$ the present conservative filter succeeds with $`r!S_r/C_r`$, whereas the elementary equality filter succeeds with $`S_r`$. The purpose of the construction is its collective scaling and exact factorization.

## A hard budget without knowing the moment

The expected instance-sensitive algorithm is proved in [unknown_moment.md](unknown_moment.md). A simpler deterministic schedule establishes a worst-case hard copy budget.

Let $`R_{\max}=N^{1-1/r}`$, which is known. Run fresh coherent batches with residual sizes $`L=0`$ and then $`L=1,2,4,\ldots`$, stopping the schedule before the residual size exceeds $`R_{\max}/2`$. The inclusion test is the exact integer comparison $`(2L)^r\le N^{r-1}`$, so no real-number oracle is needed. Halt on a success flag.

If $`R\lt 2`$, the $`L=0`$ batch has success at least $`r!/(2^rC_r)`$. If $`R\ge2`$, the schedule contains a power of two satisfying

```math
R/4\lt L\le R/2.
```

At that batch, $`Q_r(L,p)\ge q_r`$ and $`(t)_r S_r\ge4^{-r}`$, so its success probability is at least $`q_r/(4^rC_r)`$. Fresh batches ensure this conditional probability remains valid if earlier trials failed. Hence the whole schedule has a fixed positive success probability depending only on $`r`$.

The sum of the power-of-two sizes is $`O(R_{\max})`$, and the $`r`$-copy overhead per batch is $`O_r(1+\log R_{\max})=O_r(R_{\max})`$. Repeating the complete schedule a fixed $`r`$-dependent number of times yields, for example, success at least $`1/2`$ with hard budget $`O_r(N^{1-1/r})`$.

## Connection to implementation and prior work

This page specifies the mathematical instrument. [Implementation](implementation.md) realizes it using an eligibility flag, clean occupation compression, reversible removal of $`r`$ equal labels, a bounded-multiplicity rotation and uncomputation.

The nonlinear target and elementary equality postselection are established ingredients. Symmetric occupations and covariance are also standard. The construction here is the universal multiplicity-corrected extraction whose target factors from every accepted residual, enabling the collective copy law. The full model-level comparison is in [related work](../references/RELATED_WORK.md).
