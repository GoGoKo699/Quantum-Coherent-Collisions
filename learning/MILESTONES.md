# Project understanding map: 30 milestones

This map organizes coherent Hadamard powers from supplied quantum copies into exactly **30 milestones**. It describes the project's understanding targets for any reader, including an LLM. Its allocation and dependencies are determined by the science rather than by an individual's prior knowledge.

The allocation is **11 background/preliminaries milestones** and **19 narrative/innovation milestones**. The background develops one connected framework: states and registers, physical successful maps, probability, symmetry, and charged implementation. The narrative needs more space because exact coherent extraction, adaptation to an unknown moment, and a robust converse are separate arguments that must be joined. Circuit realization, finite precision, and promise-sensitive attribution are part of that joined account.

Both phases proceed from local objects and mechanisms toward global understanding. M11 assembles the operational question from the prerequisites. M28–M30 assemble the construction, converse, physical resources, and scope into the scientific contribution. The map does not attempt to reproduce every lemma or cover every neighboring subject; the scientific pages remain authoritative for complete statements and proofs.

The **single educational anchor** is John Watrous, *The Theory of Quantum Information* (2018). Section numbers below refer to the author's [complete manuscript](https://jhwatrous.github.io/TQI.pdf), whose version and notation are recorded in the [Watrous bridge](WATROUS_BRIDGE.md). The bridge distinguishes textbook foundations from local derivations and imported research algorithms. Research references attached to the science provide attribution, not additional educational anchors.

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M05 | States, supplied copies, successful operations, and residual records |
| Background/preliminaries | M06–M10 | Accuracy, occupations, probability, symmetry, and physical resources |
| Background/preliminaries | M11 | The complete operational question and its distinct guarantees |
| Narrative/innovation | M12–M15 | Elementary postselection becomes an exact collective instrument |
| Narrative/innovation | M16–M18 | Collision-scale success becomes hard-budget and adaptive expected-cost algorithms |
| Narrative/innovation | M19–M22 | The mathematical instrument becomes a charged circuit with controlled synthesis error |
| Narrative/innovation | M23–M27 | Phase covariance becomes robust and exact copy lower bounds with precise quantifiers |
| Narrative/innovation | M28–M30 | Matching bounds, attribution, promises, and resources become one scientific account |

## Phase I: background/preliminaries

### M01 Amplitudes in a specified basis

**Central question.** What information must the powered quantum state retain?

**Understanding target.** Interpret $`\alpha_i`$ as a complex amplitude and $`p_i=|\alpha_i|^2`$ as a measurement probability. Distinguish relative phase from a physically irrelevant global phase. Understand why coordinatewise powering depends on the specified basis and changes both the probability distribution and the relative phases.

**Dependencies and story role.** None within this map. This supplies the local state description on which the entire task depends.

**Conceptual connection.** A classical distribution does not determine a pure quantum state. Producing samples from the powered distribution therefore does not establish production of the coherent powered state.

**Sources.** Watrous §§1.1.1 and 2.1.2; [the quantum output](../science/model.md#the-quantum-output); [two-level example](../science/interpretation.md#a-two-level-example).

### M02 Independent copies and the access model

**Central question.** What does the source supply, and which operations does it leave unavailable?

**Understanding target.** Interpret $`|\alpha\rangle^{\otimes t}`$ as independent preparations of the same unknown pure state. Separate register dimension from copy count. Distinguish possessed state registers from executable preparation, inverse-preparation, reflection, or amplitude oracles.

**Dependencies and story role.** M01. The local state becomes a precisely specified computational input.

**Conceptual connection.** An operation may be easy with a preparation circuit while remaining costly with supplied copies. Initial information independent of the unknown source is different from an extra source-dependent quantum program.

**Sources.** Watrous §§1.1.2 and 2.1.1–2.1.2; [input and resource conventions](../science/model.md); [a resource tradeoff](../science/interpretation.md#a-resource-tradeoff-not-a-free-source).

### M03 Positive maps and Kraus admissibility

**Central question.** When does a proposed amplitude transformation define a physical successful operation?

**Understanding target.** Relate complete positivity to Kraus representations and positive Choi operators. Interpret $`\sum_z K_z^\dagger K_z\le I`$ as a trace-nonincreasing successful map that can be completed by a failure branch. A useful formula on selected input vectors must still define an admissible operation on its full input space.

**Dependencies and story role.** M01–M02. This introduces the physical validity criterion used by both construction and converse.

**Conceptual connection.** Linearity applies to the joint input density operator. Normalizing a heralded output can produce a nonlinear function of the single-copy amplitudes without modifying quantum mechanics.

**Sources.** Watrous §§1.1.3 and 2.2.1–2.2.2; [admissibility of the success map](../science/coherent_extraction.md#lemma-1-the-success-map-is-physically-admissible); [interpretation of postselection](../science/interpretation.md#a-resource-tradeoff-not-a-free-source).

### M04 Heralds and subnormalized outputs

**Central question.** How should output quality and the chance of obtaining that output be recorded together?

**Understanding target.** Read a successful output $`\sigma`$ as carrying both probability $`s=\mathrm{Tr}\,\sigma`$ and conditional state $`\sigma/s`$ when $`s\gt0`$. Absorb accepted measurement records, their corrections, and discarded systems into one successful map. Keep normalized and unnormalized quantities distinct.

**Dependencies and story role.** M03. The physical map is connected to its observable success flag and output specification.

**Conceptual connection.** A rare accurate branch is not a high-success algorithm. Combining classical branches requires adding their subnormalized states before normalizing the accepted ensemble.

**Sources.** Watrous §§2.3.1–2.3.2; [correctness conventions](../science/model.md#charged-resources-and-correctness); [successful-map definitions](../science/converse.md#1-definitions-and-the-hard-budget-theorem).

### M05 Residual systems and coherent cleanup

**Central question.** When can auxiliary quantum information be discarded without damaging the output?

**Understanding target.** Use partial trace to distinguish a tensor-separated output from one correlated with a residual system. Understand why a record that distinguishes output labels can remove their coherence even if that record is never read. Relate reversible computation and uncomputation to the physical output state.

**Dependencies and story role.** M02–M04. This identifies the principal constructive hazard: obtaining the correct label amplitudes while leaving information about those labels elsewhere.

**Conceptual connection.** Erasing a computational record coherently is different from ignoring it. The final factorization proof, rather than the apparent classical irrelevance of the record, licenses disposal.

**Sources.** Watrous §§2.1.3 and 2.3.2; [exact target factorization](../science/coherent_extraction.md#lemma-2-every-accepted-residual-gives-the-same-exact-target); [why the residual can be discarded](../science/implementation.md#5-why-the-residual-can-be-discarded).

### M06 Fidelity distance and conventions

**Central question.** What does it mean for a heralded quantum output to be accurate?

**Understanding target.** Distinguish half-trace distance from pure-target overlap. Watrous uses root fidelity, whereas the project uses its square for a pure target: $`F_{\mathrm W}(\rho,|\beta\rangle\langle\beta|)^2=\langle\beta|\rho|\beta\rangle`$. Interpret successful overlap as probability times this conditional overlap, and understand why normalization can amplify a small unnormalized error.

**Dependencies and story role.** M04–M05. Accuracy becomes compatible with the successful-map convention needed later.

**Conceptual connection.** A statement about an aggregate accepted output, an individual branch, and a success-weighted average are different statements. The root-versus-square convention must be translated before comparing formulas.

**Sources.** Watrous §3.2, especially §§3.2.1 and 3.2.3, and §3.1.1; [accuracy quantifiers](../science/converse.md#3-hard-budget-consequences-and-accuracy-quantifiers); [finite heralding error](../science/implementation.md#7-finite-universal-synthesis-and-heralding-error).

### M07 Symmetric occupations and multiplicities

**Central question.** How can identical copies be organized without measuring their labels?

**Understanding target.** Interpret a normalized symmetric occupation state $`|n\rangle_{\mathrm{sym}}`$ and the number $`t!/\prod_i n_i!`$ of distinct strings in its orbit. Connect these multiplicities to the tensor-power expansion. Distinguish a symmetric superposition from a classical mixture of its strings.

**Dependencies and story role.** M02, M05. This provides the representation in which a collision can be removed while its phase remains coherent.

**Conceptual connection.** Equal amplitudes within an occupation class do not justify sorting and discarding permutation information. Normalized orbit states and clean auxiliary registers must both be preserved.

**Sources.** Watrous §7.1.1 and §1.1.2; [occupations retain the phases](../science/coherent_extraction.md#occupations-retain-the-phases); [compression normalization](../science/implementation.md#normalization-and-reversibility).

### M08 Collision probabilities and random budgets

**Central question.** What elementary probability statements connect repeated labels to resource cost?

**Understanding target.** Interpret $`S_r=\sum_i p_i^r`$ as the probability that a specified group of $`r`$ independent labels agrees. Distinguish that event from an occurrence anywhere in a longer stream. Connect union bounds, expectations, Markov's inequality, and independent repetitions to collision probabilities and random total costs.

**Dependencies and story role.** M01–M02. This adds the probability language needed to turn an admissible instrument into an algorithm with a charged budget.

**Conceptual connection.** A hard cap, an expected cost, and a stopping-time distribution are separate resources. The Poisson embedding and renewal argument needed here are supplied in the project, rather than presumed from the textbook section.

**Sources.** Watrous §1.2.2; [occupancy success identity](../science/coherent_extraction.md#exact-success-probability); [first-collision scale](../science/unknown_moment.md#the-first-collision-scale); [expected total consumption](../science/unknown_moment.md#expected-total-consumption-including-retries).

### M09 Choi representations and symmetry averaging

**Central question.** How can symmetry simplify a completely unrestricted physical processor?

**Understanding target.** Relate a map to its Choi operator, recognize averaging over known unitary conjugations as a physical operation, and understand the role of invariant measures. Distinguish covariance imposed on the input model from covariance obtained by averaging an arbitrary candidate map.

**Dependencies and story role.** M03–M04, M07. This assembles the representation framework required for a universal converse.

**Conceptual connection.** Averaging can preserve an appropriately chosen performance functional without making an implementability assumption about the original algorithm. The particular torus characters and charge blocks are derived locally in the project.

**Sources.** Watrous §§2.2.2 and 7.2.1; [twirling reduction](../science/converse.md#21-twirl-the-unnormalized-successful-map); [charge decomposition](../science/converse.md#22-an-explicit-charge-decomposition).

### M10 Known circuits and charged resources

**Central question.** What separates existence of a successful map from an efficiently implemented processor?

**Understanding target.** Separate consumed copies, data qubits, work registers, classical memory, gates, connectivity, and synthesis precision. Interpret a known unitary dilation as a starting point for a circuit, not a free implementation. Distinguish ideal known rotations from their approximation over a finite universal gate set.

**Dependencies and story role.** M02–M06. This places physical implementation and accuracy within the same resource account.

**Conceptual connection.** A sparse list of held labels avoids an uncharged table of amplitudes, while coherent addressing and cleanup still require actual gates. Watrous supplies the operator framework; the reversible circuit and synthesis accounting are project-specific developments and attributed imports.

**Sources.** Watrous §§2.2.2, 1.1.3, and 3.3.2–3.3.3; [gate, memory, and depth accounting](../science/implementation.md#6-gate-memory-and-depth-accounting); [finite synthesis](../science/implementation.md#7-finite-universal-synthesis-and-heralding-error).

### M11 The complete operational question

**Central question.** Which unknown-input task and which resource law does the project actually solve?

**Understanding target.** Assemble supplied identical pure-state copies, a fixed coordinate basis, exact heralded quantum output, arbitrary source-independent processing, and charged failures into one model. Distinguish the universal upper bound, the robust worst-case lower bound, and the exact fixed-profile phase-minimax statement.

**Dependencies and story role.** M06–M10, with M01–M05 supplying their foundations. This is the global synthesis of the background phase.

**Conceptual connection.** Identify what changes when a preparation oracle, a Fourier promise, noise, a variable degree, or a classical-only output is supplied. The desired nonlinear output is compatible with a linear physical map on several copies.

**Sources.** Watrous §§2.1–2.3 as the operational framework and §3.2 for accuracy; [model and principal results](../science/model.md); [meaning and limits](../science/interpretation.md).

## Phase II: narrative/innovation

### M12 The elementary equality baseline

**Central question.** Why does applying the familiar power filter independently waste copies in the worst case?

**Understanding target.** Follow equality postselection on exactly $`r`$ copies, whose accepted amplitudes are proportional to $`\alpha_i^r`$ and whose success probability is $`S_r`$. Relate disjoint repetition to expected cost $`r/S_r`$. Identify the additional opportunity in a larger coherent block: many possible collision locations share the same input copies.

**Dependencies and story role.** M04, M07–M08, M11. The narrative begins with a local known mechanism and the specific resource limitation to be overcome.

**Conceptual connection.** Collective pooling changes the use of available copies; it does not introduce the nonlinear task or postselection for the first time.

**Sources.** Watrous §2.3.2; [baseline and scope](../science/model.md#baseline-and-scope); [nonlinear-filter antecedents](../references/RELATED_WORK.md#nonlinear-filters-qubits-and-implementation).

### M13 A physically admissible collision instrument

**Central question.** Which collision occupations can be processed coherently with a bounded correction?

**Understanding target.** Recognize the accepted sector: one coordinate has multiplicity between $`r`$ and $`2r-1`$, and every other coordinate has multiplicity below $`r`$. Removing $`r`$ entries leaves a unique residual $`z`$. Explain how orthogonal output labels and the bound $`(z_i+r)!/z_i!\le C_r`$ make the sum of Kraus effects at most the identity.

**Dependencies and story role.** M03, M07, M12. A candidate collision rule becomes one valid universal quantum instrument.

**Conceptual connection.** Completeness must hold simultaneously for all accepted occupations, not merely after averaging the intended source. Unique residual assignment prevents distinct success branches from overusing an input basis vector.

**Sources.** Watrous §§2.2.2 and 1.1.3; [the universal instrument](../science/coherent_extraction.md#a-universal-instrument); [admissibility proof](../science/coherent_extraction.md#lemma-1-the-success-map-is-physically-admissible).

### M14 Factorial cancellation and exact decoupling

**Central question.** Why does every accepted residual leave the same powered pure state?

**Understanding target.** Connect the multinomial input coefficient to the square-root factorial ratio in $`K_z`$. Follow the cancellation that leaves one scalar depending on $`z`$ times $`\sum_i\alpha_i^r|i\rangle`$. Understand the resulting tensor factorization, including arbitrary complex amplitudes and zero amplitudes.

**Dependencies and story role.** M05, M07, M13. Physical admissibility is joined to exact quantum correctness.

**Conceptual connection.** The correction compensates for differing permutation multiplicities. Its purpose is to decouple the output from the residual, not simply to increase the probability of finding any repeated label.

**Sources.** Watrous §§2.1.3 and 7.1.1; [factorial cancellation](../science/coherent_extraction.md#lemma-2-every-accepted-residual-gives-the-same-exact-target); [circuit factorization](../science/implementation.md#5-why-the-residual-can-be-discarded).

### M15 The exact success identity and collision scale

**Central question.** How does exact factorization produce a useful copy bound for arbitrary amplitudes?

**Understanding target.** Interpret each factor in the identity

```math
P_r(t,p)=\frac{(t)_rS_r}{C_r}\,Q_r(t-r,p).
```

Relate the residual sum to a classical multinomial probability. Use the union bound with $`t=r+\lfloor R/2\rfloor`$ to obtain constant success for $`R=S_r^{-1/r}`$, including concentrated inputs and integer endpoints.

**Dependencies and story role.** M08, M14. The exact quantum mechanism becomes an instance-dependent quantitative upper bound.

**Conceptual connection.** Larger batches are not automatically better: additional collision labels can reduce eligibility. The useful scale balances a growing falling factorial against the no-residual-collision probability.

**Sources.** Watrous §1.2.2 and §7.1.1; [exact success probability](../science/coherent_extraction.md#exact-success-probability); [constant success at the collision scale](../science/coherent_extraction.md#constant-success-at-the-collision-scale).

### M16 A finite geometric schedule

**Central question.** How can a worst-case hard budget avoid knowing the input's collision moment?

**Understanding target.** Follow fresh batches with residual sizes zero and successive powers of two up to the known dimension cutoff. Separate the $`R\lt2`$ case from the scale-containing batch when $`R\ge2`$. Explain why one batch has constant success and why the sum of all charged batches is $`O_r(N^{1-1/r})`$.

**Dependencies and story role.** M08, M15. A moment-dependent batch becomes a universal algorithm with a deterministic copy cap and constant success.

**Conceptual connection.** The schedule does not need success to improve monotonically with batch size. Fresh inputs preserve the useful batch's conditional success probability after earlier failures.

**Sources.** Watrous §1.2.2; [hard budget without knowing the moment](../science/coherent_extraction.md#a-hard-budget-without-knowing-the-moment); [worst-case result](../science/model.md#the-result-package).

### M17 The first collision as a pilot

**Central question.** How can measured copies reveal a useful scale without learning the state?

**Understanding target.** Interpret the first classical $`r`$-collision time $`\tau`$. Follow the Poisson embedding that gives $`\mathbb E\tau=O_r(R)`$, and the lower-tail and Markov bounds giving a constant-probability interval around $`R`$. Use the rational batch rule $`t=r+\lfloor\tau/(96r!)\rfloor`$ to obtain a useful fresh coherent block.

**Dependencies and story role.** M08, M15. The upper-bound analysis gains an implementable instance-sensitive scale selection.

**Conceptual connection.** The pilot measures independent copies and leaves the fresh coherent block intact. A collision scale is sufficient; neither a phase estimate nor a complete distribution estimate is supplied.

**Sources.** Watrous §1.2.2 for probability foundations; [pilot algorithm](../science/unknown_moment.md#algorithm); [first-collision proof](../science/unknown_moment.md#the-first-collision-scale); [constant trial success](../science/unknown_moment.md#a-constant-chance-of-an-exact-coherent-output). The Poisson argument is locally derived.

### M18 Renewal without knowing the moment

**Central question.** Why do calibration, failures, and repetitions together still cost only the collision scale in expectation?

**Understanding target.** Combine the constant unconditional success probability of a complete pilot-plus-coherent trial with its expected cost. Explain the renewal identity even when one trial's cost and success are correlated. Obtain almost-sure termination and expected $`O_r(R)`$ total copies while retaining an exact accepted state.

**Dependencies and story role.** M04, M08, M17. The adaptive procedure becomes a complete universal exact algorithm with every consumed copy charged.

**Conceptual connection.** Independence is needed between fresh complete trials, not between cost and success within one trial. Expected instance cost does not imply a deterministic instance-sized copy or memory cap.

**Sources.** Watrous §§1.2.2 and 2.3.2; [expected total consumption](../science/unknown_moment.md#expected-total-consumption-including-retries); [memory and stopping bounds](../science/unknown_moment.md#memory-gates-and-stopping-bounds).

### M19 A Boolean prefilter that preserves phases

**Central question.** Which part of the collision information may be measured safely before compression?

**Understanding target.** Follow reversible sorting, run-count computation, copying one eligibility bit, and reversing all work before measuring that bit. Explain why eligibility is constant within each occupation orbit and therefore preserves coherence among all accepted occupations and output labels.

**Dependencies and story role.** M04–M05, M13. The instrument begins to acquire a concrete circuit while maintaining its exact successful action.

**Conceptual connection.** Measuring a Boolean eligibility flag differs from measuring the repeated label or its multiplicity. The prefilter restricts later compilation to bounded multiplicities without changing the successful map.

**Sources.** Watrous §2.3.2 and §7.1.1; [Boolean eligibility circuit](../science/implementation.md#2-measure-only-a-boolean-eligibility-flag); [instrument domain](../science/implementation.md#1-instrument-to-implement).

### M20 Clean compression with repeated labels

**Central question.** How can a symmetric occupation state become a sorted sparse list without leaking its multiplicities?

**Understanding target.** Identify the inherited Liu–Childs–Gottesman symmetrizer and use its inverse on the accepted subspace. Distinguish the global permutation resource from permutations within equal-label runs. Track normalized stabilizer states and clean work registers so that compression preserves the occupation coefficient exactly.

**Dependencies and story role.** M05, M07, M10, M19. The abstract occupation basis is connected to explicitly held label registers.

**Conceptual connection.** A sorting record cannot simply be discarded. The bounded-run implementation includes preparation and erasure of its permutation resources; no free dimension-sized occupation table or quantum-specified interval state is assumed.

**Sources.** Watrous §7.1.1 for symmetric-space foundations; [charged coherent compression](../science/implementation.md#3-charged-coherent-occupation-compression); [normalization and reversibility](../science/implementation.md#normalization-and-reversibility); [imported symmetrizer attribution](../references/RELATED_WORK.md#nonlinear-filters-qubits-and-implementation).

### M21 Coherent extraction and record erasure

**Central question.** How does the sorted-list circuit realize the Kraus coefficients without recording which output label won?

**Understanding target.** Follow the unique-run scan, controlled removal of $`r`$ repeated entries, positive multiplicity rotation, and reconstruction of the run's position and length from the residual and output. Explain why clearing those records realizes the same exact factorization as the mathematical instrument.

**Dependencies and story role.** M13–M14, M20. The local circuit components are joined into the complete coherent extractor.

**Conceptual connection.** Reversible copying of a computational label within a basis map is not measurement. The final residual may be discarded because factorization has been proved, while the position and multiplicity records must be uncomputed.

**Sources.** Watrous §§2.1.3 and 2.2.2; [sparse extraction and cleanup](../science/implementation.md#4-sparse-extraction-and-cleanup); [residual factorization](../science/implementation.md#5-why-the-residual-can-be-discarded).

### M22 Finite synthesis and total resource accounting

**Central question.** What survives when the ideal extractor is compiled into a finite gate set?

**Understanding target.** Account for all copies, sparse data registers, sorting records, classical pilot storage, known rotations, and synthesis gates. Relate circuit error to the subnormalized accepted output and normalize only after averaging over the complete pilot trial. Understand why independent repetitions preserve that accepted distribution and why the constants depend on fixed $`r`$.

**Dependencies and story role.** M06, M10, M18, M21. The exact instrument and adaptive algorithm become one charged physical implementation.

**Conceptual connection.** A rare pilot transcript need not have a uniformly good conditional error bound. The proved aggregate trial success controls normalization; the success flag alone does not certify exact finite-gate output or hardware noise tolerance.

**Sources.** Watrous §§1.1.3 and 3.3.2–3.3.3, with §2.3.2 for conditioning; [resource bounds](../science/implementation.md#6-gate-memory-and-depth-accounting); [aggregate synthesis error](../science/implementation.md#7-finite-universal-synthesis-and-heralding-error).

### M23 Twirling an unnormalized successful map

**Central question.** Why can a converse analyze a phase-covariant map without restricting the original processor?

**Understanding target.** Start with any successful TNI map and average it using the flat input phases and the phase-multiplied output representation. Track preservation of average success and unnormalized target overlap. Use Choi positivity and character orthogonality to obtain Kraus blocks with $`n=z+re_i`$.

**Dependencies and story role.** M04, M07, M09, M11. The lower-bound argument begins from unrestricted processing and reduces it to a concrete representation problem.

**Conceptual connection.** The twirl is a proof reduction, not an assumed ability to learn the phases. The output representation encodes the specified powered target; changing it to a cloning target changes the problem.

**Sources.** Watrous §§2.2.2 and 7.2.1; [unnormalized-map twirl](../science/converse.md#21-twirl-the-unnormalized-successful-map); [explicit charge decomposition](../science/converse.md#22-an-explicit-charge-decomposition).

### M24 Charges convert coherence into collision weight

**Central question.** What prevents a processor from creating the required phase coherence before collisions become available?

**Understanding target.** Explain why a negative charge can support at most one output label and therefore only baseline overlap with a flat target. Show why every nonnegative charge draws input weight from the $`r`$-collision sector. Combine positivity, trace nonincrease, and multinomial occupation probabilities into the success–fidelity inequality.

**Dependencies and story role.** M03, M07–M08, M23. The representation reduction becomes the physical obstruction behind the copy lower bound.

**Conceptual connection.** Collision weight is bounded as an operator-supported resource, without measuring occupations or assuming a particular circuit. Accepted records and discarded systems do not evade the bound.

**Sources.** Watrous §§1.1.3, 2.2.2, and 7.1.1; [negative charges](../science/converse.md#23-negative-charges-have-a-single-output-label); [collision-sector effect bound](../science/converse.md#24-nonnegative-charges-require-an-input-collision).

### M25 Weighted accuracy and the hard budget lower bound

**Central question.** Which accuracy and success promises make the collision obstruction quantitative?

**Understanding target.** Combine constant success with pointwise or success-weighted conditional fidelity. Translate a trace-distance guarantee using the correct squared-overlap convention. Obtain the robust worst-case $`\Omega_r(N^{1-1/r})`$ hard-budget scale, and understand the explicit counterexample to replacing the weighted average by an unweighted conditional average.

**Dependencies and story role.** M04, M06, M08, M24. The structural converse becomes a theorem with operationally meaningful quantifiers.

**Conceptual connection.** Normalizing each phase-dependent branch before averaging can overvalue accurate but unlikely outputs. The hard family has a trivial basis-measurement distribution, so its obstruction concerns the entire coherent output.

**Sources.** Watrous §§2.3.2 and 3.2.1–3.2.3; [hard-budget consequences](../science/converse.md#3-hard-budget-consequences-and-accuracy-quantifiers); [unweighted-average counterexample](../science/converse.md#why-an-unweighted-conditional-average-is-insufficient).

### M26 Expected budgets without biased conditioning

**Central question.** How can a lower bound survive a random copy count without assuming that a cutoff preserves fidelity?

**Understanding target.** Truncate before copy $`t+1`$ and split retained and removed accepted outputs. Bound the removed centered score $`w-s/N`$ by its probability mass and control that mass with the integer-valued Markov tail. Derive the expected-budget lower bound from average unnormalized accuracy and average expected cost.

**Dependencies and story role.** M04, M08, M25. The converse is matched to the adaptive resource guarantee of the upper algorithm.

**Conceptual connection.** A cutoff can select less accurate branches. Tracking a linear score of subnormalized outputs handles that bias; asserting preservation of conditional fidelity would not.

**Sources.** Watrous §1.2.2 and §2.3.2; [expected-budget theorem and proof](../science/converse.md#4-expected-copy-budgets-including-approximate-output); [adaptive upper guarantee](../science/unknown_moment.md#expected-total-consumption-including-retries).

### M27 Exact profile minimax and its boundary

**Central question.** When does the collision moment itself describe a necessary copy scale?

**Understanding target.** Fix a known amplitude profile with at least two positive entries and retain arbitrary phases. Use exact output purity to eliminate negative-charge contributions, including profiles with zeros. Obtain an $`\Omega_r(S_r^{-1/r})`$ phase-minimax lower bound while distinguishing it from approximate instance optimality.

**Dependencies and story role.** M03, M05, M24–M26. The moment-dependent upper bound receives its precise matching interpretation.

**Conceptual connection.** A positive sum with rank-one output constrains every accepted summand. A one-label profile is degenerate, and a concentrated powered target can be approximated by a known basis state even when the exact phase-sensitive task is costly.

**Sources.** Watrous §§1.1.3 and 2.1.2–2.1.3; [exact profile-minimax theorem](../science/converse.md#5-exact-profile-minimax-lower-bound); [approximate-profile boundary](../science/converse.md#6-boundaries-of-the-claims).

### M28 The attained copy law and its resource cost

**Central question.** What is optimal, and what physical work buys the improvement?

**Understanding target.** Join the hard schedule and adaptive exact upper bounds to the robust and exact-profile converses. Interpret the degree-dependent law $`\Theta_r(N^{1-1/r})`$ and the instance scale $`R`$. Keep copy consumption, realized quantum width, expected gates, finite-synthesis error, and subsequent readout costs separate.

**Dependencies and story role.** M15–M18, M22, M25–M27. The theorem branches and implementation become one global resource account.

**Conceptual connection.** Collective coherent storage enables the copy gain. A matching copy exponent neither implies optimal gate constants nor supplies an application-level advantage over classical computation or a stronger oracle model.

**Sources.** Watrous §§2.1–2.3 and 3.3 as the operational framework; [principal result package](../science/model.md#the-result-package); [charged implementation](../science/implementation.md); [resource interpretation](../science/interpretation.md#a-resource-tradeoff-not-a-free-source).

### M29 Attribution promises and verification

**Central question.** Which ingredients are inherited, and which assumptions prevent neighboring results from being interchangeable?

**Understanding target.** Locate elementary nonlinear filters, coherent collision/index removal, covariant conversion, occupation-shift Choi blocks, and repeated-list symmetrization in their primary sources. Recognize that a known exact Fourier-support window already permits a special supplied-copy shortcut. Distinguish analytical theorems, imported dependencies, and finite verification evidence.

**Dependencies and story role.** M11, M28. The resource account is placed in its actual research setting with its promises and evidence visible.

**Conceptual connection.** A source's headline oracle model may hide a circuit that also works on copies; conversely, possessing a state does not furnish its preparation inverse. Neither a finite pilot histogram nor small numerical checks establish an exact global promise or an asymptotic proof.

**Sources.** Watrous §2.2.2 for operational representations and §7.1.1 for occupation foundations; [related work](../references/RELATED_WORK.md), especially [the Fourier-support predecessor](../references/RELATED_WORK.md#an-exact-fourier-support-predecessor) and [collision/covariance antecedents](../references/RELATED_WORK.md#collision-and-covariance-antecedents); [verification scope](../verification/README.md). The textbook does not supply the project-specific literature comparison.

### M30 The complete scientific story

**Central question.** What does coherent collision processing establish about nonlinear computation on unknown quantum data?

**Understanding target.** Give one connected account from the supplied-state model through multiplicity-corrected exact extraction, unknown-moment adaptation, charged compilation, and phase-covariant necessity. Explain which resource law is attained, which uncertainty makes it necessary, and why fixed degree, pure iid inputs, a specified basis, success weighting, and coherent output remain load-bearing assumptions.

**Dependencies and story role.** M11, M28–M29. This is the global synthesis of the narrative and the complete map.

**Conceptual connection.** Interpret a changed promise or resource and identify which theorem still applies. Preserve both parts of the result: the algorithm constructs a useful pure state, and the converse limits every processor in the specified copy model without claiming unrestricted computational or noise-tolerance advantages.

**Sources.** Watrous §§2.1–2.3, 3.2, and 7.1.1 as the integrated foundation; [scientific route](../science/README.md); [model](../science/model.md); [meaning and limits](../science/interpretation.md); [attribution](../references/RELATED_WORK.md).
