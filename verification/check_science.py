#!/usr/bin/env python3
"""Independent finite checks for coherent powers; Python standard library only.

These checks verify finite algebra, reversible list maps and charge inequalities.
They do not prove asymptotic theorems or execute the inherited quantum symmetrizer.
"""
from __future__ import annotations

import argparse
import cmath
from collections import Counter, defaultdict
from functools import lru_cache
import itertools
import json
import math
from pathlib import Path
import random

TOL = 3e-11


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def occupations(total, dimension):
    if dimension == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in occupations(total - first, dimension - 1):
            yield (first,) + tail


def normalize(alpha):
    norm = math.sqrt(sum(abs(z) ** 2 for z in alpha))
    return tuple(z / norm for z in alpha)


def multinomial_amplitude(alpha, n):
    count = math.factorial(sum(n)) / math.prod(math.factorial(k) for k in n)
    return math.sqrt(count) * math.prod(z ** k for z, k in zip(alpha, n))


def q_by_strings(p, length, r):
    """Direct ordered-sample enumeration, independent of occupation formulas."""
    value = 0.0
    for sequence in itertools.product(range(len(p)), repeat=length):
        if max(Counter(sequence).values(), default=0) < r:
            value += math.prod(p[i] for i in sequence)
    return value


def success_by_strings(p, t, r):
    constant = math.factorial(2 * r - 1) / math.factorial(r - 1)
    value = 0.0
    for sequence in itertools.product(range(len(p)), repeat=t):
        counts = Counter(sequence)
        heavy = [k for k in counts.values() if k >= r]
        if len(heavy) == 1 and heavy[0] <= 2 * r - 1:
            k = heavy[0]
            effect = math.factorial(k) / math.factorial(k - r) / constant
            value += effect * math.prod(p[i] for i in sequence)
    return value


def check_instrument(alpha, t, r):
    n_dim = len(alpha)
    p = tuple(abs(z) ** 2 for z in alpha)
    moment = sum(x ** r for x in p)
    target = tuple(z ** r / math.sqrt(moment) for z in alpha)
    constant = math.factorial(2 * r - 1) / math.factorial(r - 1)
    states = list(occupations(t, n_dim))
    vector = {n: multinomial_amplitude(alpha, n) for n in states}
    effects = defaultdict(float)
    density = [[0j for _ in alpha] for _ in alpha]
    max_branch_error = 0.0
    accepted_inputs = set()
    for residual in occupations(t - r, n_dim):
        if max(residual) >= r:
            continue
        output = []
        for i in range(n_dim):
            source = list(residual)
            source[i] += r
            source = tuple(source)
            coefficient = math.sqrt(
                math.factorial(residual[i] + r)
                / math.factorial(residual[i]) / constant
            )
            effects[source] += coefficient ** 2
            require(source not in accepted_inputs, "Accepted occupation repeated")
            accepted_inputs.add(source)
            output.append(coefficient * vector[source])
        scalar = math.sqrt(
            math.factorial(t) / constant
            / math.prod(math.factorial(k) for k in residual)
        ) * math.prod(z ** k for z, k in zip(alpha, residual))
        max_branch_error = max(
            max_branch_error,
            max(abs(output[i] - scalar * alpha[i] ** r)
                for i in range(n_dim)),
        )
        for i in range(n_dim):
            for j in range(n_dim):
                density[i][j] += output[i] * output[j].conjugate()
    success = sum(density[i][i].real for i in range(n_dim))
    formula = (
        math.factorial(t) / math.factorial(t - r)
        * moment / constant * q_by_strings(p, t - r, r)
    )
    direct = success_by_strings(p, t, r)
    density_error = max(
        abs(density[i][j] - success * target[i] * target[j].conjugate())
        for i in range(n_dim) for j in range(n_dim)
    )
    effect_max = max(effects.values(), default=0.0)
    require(effect_max <= 1 + TOL, "Kraus effect exceeds identity")
    require(max_branch_error < TOL, "Residual factorization fails")
    require(density_error < TOL, "Accepted density is not target ray")
    require(abs(success - formula) < TOL, "Multinomial success identity fails")
    require(abs(success - direct) < TOL, "Ordered-sample success disagrees")
    return {
        "N": n_dim, "t": t, "r": r, "success": success,
        "branch_error": max_branch_error, "density_error": density_error,
        "formula_error": abs(success - formula),
        "ordered_sample_error": abs(success - direct),
        "max_effect": effect_max,
    }


def check_extraction():
    cases = 0
    for n_dim in range(2, 5):
        for r in range(2, 5):
            for t in range(r, min(9, (r - 1) * n_dim + r) + 1):
                for occupation in occupations(t, n_dim):
                    heavy = [i for i, k in enumerate(occupation) if k >= r]
                    if len(heavy) != 1:
                        continue
                    label = heavy[0]
                    k = occupation[label]
                    if k > 2 * r - 1:
                        continue
                    original = [i for i, count in enumerate(occupation)
                                for _ in range(count)]
                    start = original.index(label)  # zero-based version of b
                    working = list(original)
                    for j in range(t - r):
                        if start <= j:
                            working[j], working[j + r] = working[j + r], working[j]
                    expected = list(original)
                    del expected[start:start + r]
                    require(working[:t - r] == expected, "Suffix extraction wrong")
                    require(working[t - r:] == [label] * r, "Tail labels not equal")
                    require([x ^ label for x in working[t - r:]] == [0] * r,
                            "XOR tail erasure fails")
                    reconstructed_start = sum(x < label for x in expected)
                    reconstructed_k = r + sum(x == label for x in expected)
                    require((reconstructed_start, reconstructed_k) == (start, k),
                            "Run record cannot be uncomputed")
                    cases += 1
    return cases


def check_charge_bound(n_dim, t, r, rng):
    states = list(occupations(t, n_dim))
    amplitude = {
        n: math.sqrt(math.factorial(t)
                     / math.prod(math.factorial(k) for k in n)
                     / n_dim ** t)
        for n in states
    }
    blocks = defaultdict(list)
    effect = defaultdict(float)
    for n in states:
        for i in range(n_dim):
            charge = list(n)
            charge[i] -= r
            charge = tuple(charge)
            value = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
            blocks[charge].append([i, n, value])
            effect[n] += abs(value) ** 2
    for items in blocks.values():
        for entry in items:
            entry[2] /= math.sqrt(max(1.0, effect[entry[1]]))
    success = overlap = 0.0
    for charge, items in blocks.items():
        if min(charge) < 0:
            require(len({item[0] for item in items}) == 1,
                    "Negative charge has multiple output labels")
        else:
            require(all(max(item[1]) >= r for item in items),
                    "Nonnegative charge uses collision-free input")
        y = [0j] * n_dim
        for i, n, coefficient in items:
            y[i] += coefficient * amplitude[n]
        trace = sum(abs(z) ** 2 for z in y)
        weight = abs(sum(y)) ** 2 / n_dim
        if min(charge) < 0:
            require(abs(weight - trace / n_dim) < TOL,
                    "Negative charge fidelity baseline fails")
        success += trace
        overlap += weight
    collision = sum(abs(amplitude[n]) ** 2 for n in states if max(n) >= r)
    rhs = success / n_dim + (1 - 1 / n_dim) * collision
    union = 0.0 if t < r else math.comb(t, r) * n_dim ** (1 - r)
    require(success <= 1 + TOL, "Random map is not trace nonincreasing")
    require(overlap <= rhs + TOL, "Charge success-fidelity bound fails")
    require(collision <= union + TOL, "Collision union bound fails")
    return {"N": n_dim, "t": t, "r": r, "gap": rhs - overlap}


def pilot_distribution(p, r):
    """Exact finite Markov-chain enumeration of the first-collision time."""
    n_dim = len(p)
    transient = {(0,) * n_dim: 1.0}
    law = defaultdict(float)
    for step in range(1, (r - 1) * n_dim + 2):
        following = defaultdict(float)
        for counts, mass in transient.items():
            for i, pi in enumerate(p):
                if not pi:
                    continue
                if counts[i] == r - 1:
                    law[step] += mass * pi
                else:
                    updated = list(counts)
                    updated[i] += 1
                    following[tuple(updated)] += mass * pi
        transient = following
    require(not transient, "Pilot fails pigeonhole stopping bound")
    require(abs(sum(law.values()) - 1) < TOL, "Pilot law is not normalized")
    return dict(law)


def check_pilot(p, r):
    law = pilot_distribution(p, r)
    n_dim = len(p)

    @lru_cache(None)
    def remaining(counts):
        result = 1.0
        for i, pi in enumerate(p):
            if pi and counts[i] < r - 1:
                updated = list(counts)
                updated[i] += 1
                result += pi * remaining(tuple(updated))
        return result

    mean = sum(t * mass for t, mass in law.items())
    require(abs(mean - remaining((0,) * n_dim)) < TOL,
            "Pilot law and independent mean recursion disagree")
    moment = sum(pi ** r for pi in p)
    scale = moment ** (-1 / r)
    a_r = 6 * math.factorial(r)
    interval_mass = sum(mass for t, mass in law.items()
                        if scale / 2 <= t <= 8 * a_r * scale)
    require(mean <= a_r * scale + TOL, "Pilot mean bound fails")
    require(interval_mass >= 0.75 - TOL, "Pilot central event bound fails")
    return {"p": p, "r": r, "mean": mean, "R": scale,
            "central_probability": interval_mass}


def check_unweighted_counterexample():
    b = 1 / math.sqrt(3)
    count = 16384
    success = overlap = conditional = minimum = 0.0
    minimum = 1.0
    for j in range(count):
        phase = 2 * math.pi * j / count
        e = cmath.exp(1j * phase)
        y0 = (1 - b * e) / (math.sqrt(2) * (1 + b))
        y1 = (e - b) / (math.sqrt(2) * (1 + b))
        s = abs(y0) ** 2 + abs(y1) ** 2
        w = abs((y0 + e.conjugate() ** 2 * y1) / math.sqrt(2)) ** 2
        success += s / count
        overlap += w / count
        conditional += w / s / count
        minimum = min(minimum, s)
    expected = 0.5 + 1 / (3 * math.sqrt(3))
    require(abs(overlap / success - 0.5) < TOL, "Weighted average is wrong")
    require(abs(conditional - expected) < TOL, "Conditional-average formula wrong")
    require(abs(minimum - ((1 - b) / (1 + b)) ** 2) < TOL,
            "Minimum success formula wrong")
    return {"weighted_fidelity": overlap / success,
            "unweighted_conditional_fidelity": conditional,
            "minimum_success": minimum}


def run():
    rng = random.Random(20261031)
    power = []
    for n_dim, t, r in [
        (2, 2, 2), (2, 3, 2), (2, 4, 2), (2, 5, 2),
        (3, 4, 2), (4, 5, 2), (3, 3, 3), (3, 5, 3),
        (4, 6, 3), (2, 4, 4), (3, 7, 4),
    ]:
        profiles = [
            normalize([complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
                       for _ in range(n_dim)]),
            normalize([cmath.exp(0.731j * i) for i in range(n_dim)]),
            tuple([1 + 0j] + [0j] * (n_dim - 1)),
        ]
        if n_dim > 2:
            profiles.append(normalize([1 + 0j, -0.7j] + [0j] * (n_dim - 2)))
        power.extend(check_instrument(alpha, t, r) for alpha in profiles)
    extraction_cases = check_extraction()
    charge = [
        check_charge_bound(n_dim, t, r, rng)
        for n_dim in range(2, 5) for r in range(2, 5)
        for t in range(7) for _ in range(3)
    ]
    pilot = [
        check_pilot(p, r)
        for p in [(0.5, 0.5), (0.97, 0.03), (1.0, 0.0),
                  (1 / 3, 1 / 3, 1 / 3), (0.6, 0.3, 0.1),
                  (0.7, 0.3, 0.0), (0.25, 0.25, 0.25, 0.25)]
        for r in range(2, 5)
    ]
    counterexample = check_unweighted_counterexample()
    return {
        "status": "pass",
        "scope": "finite algebra, ordered-sample identities, reversible list maps, "
                 "charge bounds, pilot stopping laws, and accuracy counterexample",
        "counts": {"power_cases": len(power), "extraction_cases": extraction_cases,
                   "charge_maps": len(charge), "pilot_laws": len(pilot)},
        "maximum_branch_error": max(x["branch_error"] for x in power),
        "maximum_density_error": max(x["density_error"] for x in power),
        "maximum_formula_error": max(x["formula_error"] for x in power),
        "maximum_ordered_sample_error": max(x["ordered_sample_error"] for x in power),
        "minimum_charge_bound_slack": min(x["gap"] for x in charge),
        "counterexample": counterexample,
        "power_cases": power,
        "pilot_laws": pilot,
        "limits": ["No numerical proof of asymptotic bounds",
                   "No end-to-end gate-level execution of the inherited symmetrizer",
                   "No certification of novelty or physical hardware performance"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Write the complete finite-check report")
    args = parser.parse_args()
    report = run()
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n")
    summary = {key: value for key, value in report.items()
               if key not in {"power_cases", "pilot_laws"}}
    print(json.dumps(summary, indent=2))
