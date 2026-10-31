# Converse: copy requirements for coherent Hadamard powers

This page proves lower bounds for producing a **coherent quantum output** from independent copies of an unknown pure state. The bounds allow arbitrary collective operations, ancillary systems independent of the unknown state, measurements, classical feedforward, and heralded failure. They do not assume that the processor itself is phase covariant.

For every fixed integer $`r\ge 2`$, a processor that works on all $`N`$-dimensional pure states needs $`\Omega_r(N^{1-1/r})`$ copies in the worst case, even with constant output error and constant success probability. The same exponent holds for expected copy budgets. For exact output, a stronger statement holds on each nontrivial fixed amplitude profile: the required scale is $`R=S_r^{-1/r}`$, where $`S_r=\sum_i|\alpha_i|^{2r}`$.

See [the model](model.md) for the supplied-copy access convention and [coherent extraction](coherent_extraction.md) for the matching construction. The covariance machinery used below is inherited; the final section gives primary sources and links to [related work](../references/RELATED_WORK.md).

## 1. Definitions and the hard-budget theorem

Fix integers $`N\ge 2`$, $`r\ge 2`$, and $`t\ge 0`$. On the flat phase family, write

```math
|\alpha_\theta\rangle
=\frac{1}{\sqrt N}\sum_{i=1}^N e^{i\theta_i}|i\rangle,
\qquad
|\beta_\theta\rangle
=\frac{1}{\sqrt N}\sum_{i=1}^N e^{ir\theta_i}|i\rangle,
\qquad
\theta\in[0,2\pi)^N.
```

Let $`\mu`$ be normalized Haar measure on this torus. The desired output is $`|\beta_\theta\rangle`$, the normalized $`r`$th Hadamard power of $`|\alpha_\theta\rangle`$.

A protocol with a hard budget of $`t`$ copies has a successful completely positive, trace-nonincreasing map

```math
\mathcal S:\mathcal L(\mathrm{Sym}^t\mathbb C^N)
\longrightarrow\mathcal L(\mathbb C^N).
```

Define its subnormalized successful output, success probability, and target overlap by

```math
\sigma_\theta
=\mathcal S\!\left((|\alpha_\theta\rangle\langle\alpha_\theta|)^{\otimes t}\right),
\qquad
s_\theta=\mathrm{Tr}\sigma_\theta,
\qquad
w_\theta=\langle\beta_\theta|\sigma_\theta|\beta_\theta\rangle.
```

When $`s_\theta\gt 0`$, conditional fidelity means the pure-target population

```math
F_\theta=\frac{w_\theta}{s_\theta}.
```

This is the squared fidelity convention. No conditional state or fidelity needs to be defined when $`s_\theta=0`$. Bars denote averages with respect to $`\mu`$.

Let $`P_{\mathrm{col}}^{(r)}(t;N)`$ be the probability that $`t`$ independent uniform labels from $`[N]`$ contain a label at least $`r`$ times. We use $`\binom tr=0`$ for $`t\lt r`$.

**Theorem 1 — success–fidelity bound.** Every such successful map satisfies

```math
\boxed{
\overline w\le\frac{\overline s}{N}
+\left(1-\frac1N\right)P_{\mathrm{col}}^{(r)}(t;N).
}
\qquad\text{(1)}
```

Moreover,

```math
P_{\mathrm{col}}^{(r)}(t;N)
\le \min\!\left\{1,\binom tr N^{1-r}\right\}.
\qquad\text{(2)}
```

The map may include all accepted classical records, any record-dependent correction to the output, and a partial trace over all remaining systems. A protocol requesting at most $`t`$ copies adaptively can be supplied all $`t`$ at the beginning and discard unused registers. Thus its successful action has precisely the form above. This argument concerns ordinary supplied copies, not coherent oracle access to an unknown preparation procedure.

## 2. Proof of Theorem 1

### 2.1 Twirl the unnormalized successful map

Let $`D_\theta=\mathrm{diag}(e^{i\theta_1},\ldots,e^{i\theta_N})`$. On the symmetric input space set $`U_\theta=D_\theta^{\otimes t}`$, and on the output set $`V_\theta=D_{r\theta}`$. Define

```math
\widetilde{\mathcal S}(X)
=\int V_\theta^\dagger
\mathcal S(U_\theta XU_\theta^\dagger)
V_\theta\,d\mu(\theta).
\qquad\text{(3)}
```

Integration preserves complete positivity and trace nonincrease. Translation invariance of Haar measure gives

```math
\widetilde{\mathcal S}(U_\phi XU_\phi^\dagger)
=V_\phi\widetilde{\mathcal S}(X)V_\phi^\dagger.
\qquad\text{(4)}
```

On the zero-phase input, the trace and target overlap of $`\widetilde{\mathcal S}`$ are exactly $`\overline s`$ and $`\overline w`$. It is essential that the **subnormalized map** is twirled: its conditional fidelity is $`\overline w/\overline s`$, not the unweighted average of $`F_\theta`$.

### 2.2 An explicit charge decomposition

Let

```math
\mathcal A_t=\{n\in\mathbb Z_{\ge0}^N:\textstyle\sum_i n_i=t\}.
```

In the normalized symmetric occupation basis,

```math
U_\theta|n\rangle_{\mathrm{sym}}
=e^{in\cdot\theta}|n\rangle_{\mathrm{sym}}.
```

Use the output-first convention for the unnormalized Choi operator,

```math
J=\sum_{n,m\in\mathcal A_t}
\widetilde{\mathcal S}(|n\rangle\langle m|)
\otimes|n\rangle\langle m|.
```

Equation (4) says that $`J`$ commutes with $`V_\theta\otimes\overline{U_\theta}`$. The basis vector $`|i\rangle\otimes|n\rangle_{\mathrm{sym}}`$ has character

```math
e^{i(re_i-n)\cdot\theta}.
```

Orthogonality of torus characters therefore makes $`J`$ block diagonal in the integer charge

```math
z=n-re_i,\qquad \sum_i z_i=t-r.
```

Each block is positive semidefinite. Diagonalize each block and reshape its eigenvectors into Kraus operators. This gives a Kraus representation

```math
K_{z,\ell}
=\sum_{i:\,z+re_i\in\mathcal A_t}
k_{z,\ell,i}|i\rangle\langle z+re_i|_{\mathrm{sym}},
\qquad
\sum_{z,\ell}K_{z,\ell}^\dagger K_{z,\ell}\le I.
\qquad\text{(5)}
```

No covariance property was assumed for individual Kraus operators of the original protocol. Equation (5) is obtained from the positive Choi blocks of its twirl.

### 2.3 Negative charges have a single output label

Suppose $`z_j\lt 0`$. For $`z+re_i`$ to be an occupation vector, one must have $`i=j`$; otherwise its $`j`$th coordinate remains negative. Consequently, a charge with a negative entry has at most one admissible output label. A charge with two negative entries has no admissible label.

Every nonzero negative-charge Kraus operator thus has range contained in $`\mathrm{span}\{|j\rangle\}`$ for one $`j`$. Since the flat target has

```math
|\langle\beta_0|j\rangle|^2=\frac1N,
```

that operator contributes exactly $`1/N`$ times its successful trace to the target overlap.

### 2.4 Nonnegative charges require an input collision

Let $`\Pi_{\mathrm{col}}`$ project onto occupation vectors with $`\max_i n_i\ge r`$. If $`z\ge0`$, each input occupation coupled by $`K_{z,\ell}`$ is $`z+re_i`$, so

```math
K_{z,\ell}=K_{z,\ell}\Pi_{\mathrm{col}}.
```

The combined effect of all these Kraus operators obeys

```math
0\le M_+:=\sum_{z\ge0,\ell}K_{z,\ell}^\dagger K_{z,\ell}
\le\Pi_{\mathrm{col}}.
\qquad\text{(6)}
```

Indeed, trace nonincrease gives $`M_+\le I`$, while its support lies within $`\Pi_{\mathrm{col}}`$. Let $`s_+`$ and $`s_-`$ be the successful traces on the zero-phase input from the nonnegative and negative charge sectors. Then

```math
s_+\le
\langle\alpha_0|^{\otimes t}\Pi_{\mathrm{col}}|\alpha_0\rangle^{\otimes t},
\qquad
s_++s_-=\overline s.
```

The occupation expansion is

```math
|\alpha_0\rangle^{\otimes t}
=\sum_{n\in\mathcal A_t}
\sqrt{\frac{t!}{N^t\prod_i n_i!}}\,|n\rangle_{\mathrm{sym}}.
```

Its occupation probabilities are exactly the multinomial probabilities of $`t`$ uniform classical labels. Hence $`s_+\le P_{\mathrm{col}}^{(r)}(t;N)`$. The positive-charge overlap is at most $`s_+`$, and the negative-charge overlap is exactly $`s_-/N`$. Therefore

```math
\overline w\le s_++\frac{s_-}{N}
=\frac{\overline s}{N}+\left(1-\frac1N\right)s_+,
```

which proves (1). For (2), take a union bound over the $`\binom tr`$ choices of $`r`$ sample positions. All labels in a fixed choice agree with probability $`N^{1-r}`$. $`\square`$

The common global phase causes no additional identification of charge blocks: all charges already have the same coordinate sum $`t-r`$. Equivalently, one may fix one phase to zero; the remaining phases distinguish the same blocks.

## 3. Hard-budget consequences and accuracy quantifiers

Suppose

```math
\overline s\ge s_0\gt 0,
\qquad
\overline w\ge(1-\varepsilon)\overline s,
\qquad
\varepsilon\lt 1-\frac1N.
\qquad\text{(7)}
```

These assumptions hold, in particular, if every input has success probability at least $`s_0`$ and every normalized successful output has fidelity at least $`1-\varepsilon`$. More generally, (7) is an average-success and **success-weighted** average-fidelity condition.

Set

```math
\kappa_0
=\frac{s_0(1-\varepsilon-1/N)}{1-1/N}\gt 0.
```

Theorem 1 implies

```math
P_{\mathrm{col}}^{(r)}(t;N)\ge\kappa_0,
\qquad
t\ge (r!\kappa_0)^{1/r}N^{1-1/r}.
\qquad\text{(8)}
```

For fixed $`r,s_0\gt 0`$ and fixed $`\varepsilon\lt 1`$, this is $`\Omega_r(N^{1-1/r})`$ for sufficiently large $`N`$, with constants also depending on $`s_0`$ and $`\varepsilon`$. The claim is about a constant error bounded away from one, not uniform constants as the fidelity advantage approaches zero.

If the successful output is exact, (1) simplifies to

```math
\overline s\le P_{\mathrm{col}}^{(r)}(t;N).
\qquad\text{(9)}
```

For a deterministic processor, $`s_\theta=1`$, and

```math
\overline F\le \frac1N+\left(1-\frac1N\right)P_{\mathrm{col}}^{(r)}(t;N).
```

Trace distance is $`D(\rho,\tau)=\tfrac12\|\rho-\tau\|_1`$. For a pure target, measuring its projector gives

```math
1-\langle\beta|\rho|\beta\rangle
\le D(\rho,|\beta\rangle\langle\beta|).
```

Thus a conditional trace-distance guarantee $`D\le\delta`$ implies (7) with $`\varepsilon=\delta`$. The same implication holds for a success-weighted average trace-distance guarantee.

### Why an unweighted conditional average is insufficient

This distinction is necessary even when success is bounded below everywhere. Take $`N=2`$, $`r=2`$, and one input copy

```math
|\alpha_\phi\rangle=(|0\rangle+e^{i\phi}|1\rangle)/\sqrt2.
```

Let the successful Kraus operator be

```math
K=\frac{I-bX}{1+b},\qquad b=\frac1{\sqrt3}.
```

It is a contraction, so it defines a valid successful operation. Direct calculation gives

```math
\min_\phi s_\phi
=\left(\frac{1-b}{1+b}\right)^2\gt 0,
\qquad
\frac{\overline w}{\overline s}=\frac12,
\qquad
\int F_\phi\,\frac{d\phi}{2\pi}
=\frac12+\frac{b(1-b^2)}2
=\frac12+\frac1{3\sqrt3}.
```

The unweighted conditional average is approximately $`0.69245`$, although one copy cannot contain a two-fold collision. Replacing the weighted condition in (7) by that unweighted average would therefore give a false conclusion.

## 4. Expected copy budgets, including approximate output

Let a protocol request a random number $`L`$ of copies. Count every requested copy, including copies consumed on unsuccessful runs. The protocol's eventual successful output defines $`s_\theta`$ and $`w_\theta`$ as before. Assume the averaged expected cost is finite:

```math
\overline T=\int\mathbb E_\theta[L]\,d\mu(\theta)\lt \infty.
```

This is weaker than assuming a uniform expected-cost bound for every phase. The latter immediately bounds $`\overline T`$ from above.

**Theorem 2 — expected-budget converse.** For every integer $`t\ge0`$,

```math
\overline w-\frac{\overline s}{N}
\le\left(1-\frac1N\right)
\left(P_{\mathrm{col}}^{(r)}(t;N)+\frac{\overline T}{t+1}\right).
\qquad\text{(10)}
```

Consequently, if

```math
\kappa=\frac{\overline w-\overline s/N}{1-1/N}\gt 0,
```

then

```math
\boxed{
\overline T\ge
\frac\kappa2\left(\frac{r!\kappa}{2}\right)^{1/r}N^{1-1/r}.
}
\qquad\text{(11)}
```

Under (7), one may replace $`\kappa`$ on the right by $`\kappa_0`$. In particular, constant success and constant conditional fidelity above the baseline require the same worst-case dimension exponent for expected budgets.

**Proof.** Abort immediately before the protocol requests copy $`t+1`$, treating this abort as failure. The retained successful branches define a hard-budget map $`\mathcal S_{\le t}`$, so Theorem 1 bounds their averaged score $`w-s/N`$ by $`(1-1/N)P_{\mathrm{col}}^{(r)}(t;N)`$.

The removed successful outputs form a positive semidefinite subnormalized state $`\sigma_{\gt t,\theta}`$. For every positive semidefinite $`A`$,

```math
\langle\beta_\theta|A|\beta_\theta\rangle-\frac{\mathrm{Tr}A}{N}
\le\left(1-\frac1N\right)\mathrm{Tr}A.
```

Moreover,

```math
\mathrm{Tr}\sigma_{\gt t,\theta}
\le\Pr_\theta[L\gt t]
\le\frac{\mathbb E_\theta[L]}{t+1},
```

because $`L`$ is integer valued. Adding retained and removed scores and averaging proves (10).

For (11), choose

```math
x=\left(\frac{r!\kappa}{2}\right)^{1/r}N^{1-1/r},
\qquad t=\lfloor x\rfloor.
```

Equation (2) gives $`P_{\mathrm{col}}^{(r)}(t;N)\le\kappa/2`$. Equation (10) therefore gives $`\overline T\ge(t+1)\kappa/2\ge x\kappa/2`$, as required. $`\square`$

This proof never assumes that conditioning on a copy cutoff preserves conditional fidelity. Such conditioning can select less accurate branches. The centered **unnormalized** score in (10) accounts for that possibility directly. The constants in (11) are sufficient for the fixed-success, fixed-error theorem; no optimal dependence on vanishing success probability or error gap is claimed.

## 5. Exact profile-minimax lower bound

Fix a probability vector $`p=(p_1,\ldots,p_N)`$ with at least two positive entries. Permit the processor to know $`p`$, but keep the phases unknown. Consider

```math
|\alpha_\theta\rangle=\sum_i\sqrt{p_i}\,e^{i\theta_i}|i\rangle,
\qquad
|\beta_\theta\rangle
=\frac{1}{\sqrt{S_r}}\sum_i p_i^{r/2}e^{ir\theta_i}|i\rangle,
\qquad
S_r=\sum_i p_i^r,
\qquad R=S_r^{-1/r}.
```

Let $`P_{\mathrm{col}}^{(r)}(t;p)`$ be the probability of an $`r`$-fold collision among $`t`$ independent labels from $`p`$. In the notation of the construction, it is $`1-Q_r(t;p)`$.

**Corollary 3 — exact fixed-profile converse.** If every successful output is exactly the target, then a hard-budget protocol satisfies

```math
\boxed{
\overline s\le P_{\mathrm{col}}^{(r)}(t;p)
\le\binom tr S_r.
}
\qquad\text{(12)}
```

Thus average success at least $`s_0\gt 0`$ requires

```math
t\ge(r!s_0)^{1/r}R.
\qquad\text{(13)}
```

For an exact protocol with averaged expected cost $`\overline T`$, one has, for every $`t\ge0`$,

```math
\overline s\le P_{\mathrm{col}}^{(r)}(t;p)+\frac{\overline T}{t+1},
```

and hence, if $`\overline s\gt 0`$,

```math
\overline T\ge
\frac{\overline s}{2}
\left(\frac{r!\overline s}{2}\right)^{1/r}R.
\qquad\text{(14)}
```

These bounds hold even when only the average success or average expected cost over the phase family is specified. They imply the corresponding worst-case phase bounds.

**Proof.** Keep the full $`N`$-torus, including coordinates where $`p_i=0`$. The twirling and charge decomposition in Section 2 do not require nonzero input occupation coefficients, so they apply without modification. Exactness gives

```math
\widetilde{\mathcal S}\!\left((|\alpha_0\rangle\langle\alpha_0|)^{\otimes t}\right)
=\overline s\,|\beta_0\rangle\langle\beta_0|.
```

A sum of positive semidefinite operators supported on one ray can only have summands supported on that ray. Every negative-charge summand, however, is supported on a computational-basis ray. Since $`|\beta_0\rangle`$ has at least two nonzero components, these rays differ. Every negative-charge summand must therefore vanish on this input.

All successful weight consequently comes from nonnegative charges. Equation (6) bounds it by the input collision weight. The occupation probabilities are now

```math
\frac{t!}{\prod_i n_i!}\prod_i p_i^{n_i},
```

the multinomial distribution with parameter $`p`$. This proves the first inequality in (12). For each chosen $`r`$-subset of sample positions, the probability that all labels agree is $`\sum_i p_i^r=S_r`$; the union bound gives the second inequality.

For an expected-budget exact protocol, every retained subset of successful branches remains exact: it is a positive semidefinite summand of the rank-one successful output. Apply (12) to the cutoff protocol and bound removed success by $`\overline T/(t+1)`$. Choosing $`t=\lfloor(r!\overline s/(2S_r))^{1/r}\rfloor`$ proves (14). $`\square`$

For each fixed nontrivial $`p`$, these lower bounds match the $`O_r(R)`$ exact construction at constant success, and its expected-copy version when the moment is unknown. If $`p`$ has support one, phase multiplication is vacuous: the target is a single basis state. A processor told that profile can prepare it with zero copies, so this degenerate case is excluded from the exact profile-minimax assertion.

## 6. Boundaries of the claims

The robust dimension lower bound uses flat phases and requires a coherent output close to the entire target state. It does not lower-bound the cost of merely sampling the target in the computational basis: for the flat family that distribution is uniform and can be generated without input copies.

The exact profile result must not be advertised as a constant-error instance-optimality theorem for every $`p`$. At a general profile, the same charge argument gives only

```math
\overline w
\le q_{\max}\overline s+(1-q_{\max})P_{\mathrm{col}}^{(r)}(t;p),
\qquad
q_{\max}=\max_i\frac{p_i^r}{S_r}.
```

When the target is concentrated on a known basis label, approximate output may be much easier. For example, take $`r=2`$, $`p_1=N^{-1/3}`$, and $`p_i=(1-p_1)/(N-1)`$ for $`i\gt 1`$. Then $`R=\Theta(N^{1/3})`$, but outputting $`|1\rangle`$ with no copies has fidelity $`p_1^2/S_2\to1`$ uniformly over phases. Exact phase-sensitive output still obeys Corollary 3.

The proofs require the arbitrary continuous-phase family. They cannot be transferred unchanged to a small finite phase alphabet: if every phase is an $`r`$th root of unity, the flat target is a known state. They also assume that all initial side information and ancillary states are independent of the unknown phases. Extra source-dependent quantum programs or preparation oracles are different access models.

## 7. Inherited methods and primary sources

Group twirling and covariant stochastic pure-state conversion are established tools. Marvian and Spekkens give a general characteristic-function criterion in Section IX, Theorem 26 and Corollary 27 of [*The theory of manipulations of pure state asymmetry I*](https://arxiv.org/abs/1104.0018). The proof here is self-contained and specializes the Choi representation directly to the supplied-copy Hadamard-power target.

Herasymenko, Lin, Verduyn Lunel, and Grinko derive torus twirling, occupation-shift Choi blocks, and their positive-semidefinite and trace constraints in Section X.B of [*Approximate cloning of structured pure states*](https://arxiv.org/abs/2610.06723). Their phase-state target is a larger tensor power of the original state. The one-register phase-multiplied target considered here has the additional single-label property for negative charges used in Section 2.3.

Bhateja, Esmaili, and Mantri use repeated-occupation versus collision-free sectors for a supplied-copy lower bound on classical heavy outputs in Appendix A.3, Proposition A.2 of [*Tight Query Lower Bounds for Quantum Sampling, with an Application to Certified Randomness*](https://arxiv.org/abs/2610.06721). That collision-sector method is also prior art. The present statements concern coherent Hadamard powers, accepted subnormalized fidelity, and the explicit budget and accuracy guarantees above. See [related work](../references/RELATED_WORK.md) for the broader comparison.
