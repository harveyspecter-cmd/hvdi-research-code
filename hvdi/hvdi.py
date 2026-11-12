# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
# Contact: bpgp25sushant@iima.ac.in
#
# PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
"""HVDI v2 engine: pure functions, no I/O.

Scores are integer rubric levels 0 to 4 for H (claimed), T (technical proof),
A (adoption), Q (capital quality) and E (buyer economics).
V = weighted mean of T, A, E.  D = H - V.  Gates are applied outside the
arithmetic and cannot be averaged away.

Every public function validates its inputs and raises ValueError or TypeError
on bad input; nothing here relies on ``assert``.
"""

from __future__ import annotations

import random
from typing import Iterable, Mapping, Optional, Sequence

LEGS: tuple[str, ...] = ("T", "A", "E")
SCORE_MIN, SCORE_MAX = 0, 4
EQUAL: tuple[float, float, float] = (1 / 3, 1 / 3, 1 / 3)
P_SHIFT: dict[str, float] = {"high": 0.15, "medium": 0.30, "low": 0.45}
GATE_LEVELS = (0, 1, 2)  # 0 open, 1 constraining, 2 binding
_EPS = 1e-9


# ---------- validation helpers ----------
def _check_score(x: int, name: str = "score") -> int:
    """Return x if it is an integer rubric level 0..4, else raise."""
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError(f"{name} must be an integer rubric level, got {x!r}")
    if not SCORE_MIN <= x <= SCORE_MAX:
        raise ValueError(f"{name} must be {SCORE_MIN}..{SCORE_MAX}, got {x}")
    return x


def _check_weights(w: Sequence[float]) -> Sequence[float]:
    """Weights: three non-negative numbers summing to 1."""
    if len(w) != 3:
        raise ValueError(f"need three weights (T, A, E), got {len(w)}")
    if any(x < 0 for x in w) or abs(sum(w) - 1) > _EPS:
        raise ValueError(f"weights must be non-negative and sum to 1, got {tuple(w)}")
    return w


def _check_number(x: float, name: str) -> float:
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number, got {x!r}")
    return x


# ---------- index ----------
def value(t: int, a: int, e: int, w: Sequence[float] = EQUAL) -> float:
    """Proven value V: weighted mean of technical proof, adoption and buyer economics."""
    _check_weights(w)
    for x, n in ((t, "T"), (a, "A"), (e, "E")):
        _check_score(x, n)
    return w[0] * t + w[1] * a + w[2] * e


def gap(h: int, t: int, a: int, e: int, w: Sequence[float] = EQUAL) -> float:
    """Divergence D = H - V. Positive: story ahead of proof. Range -4..+4."""
    return _check_score(h, "H") - value(t, a, e, w)


def classify(d: float, thr: float = 1.0, eps: float = _EPS) -> str:
    """'ahead' if d >= thr, 'behind' if d <= -thr, else 'aligned' (eps absorbs float error)."""
    _check_number(d, "d")
    if thr <= 0:
        raise ValueError("thr must be positive")
    return "ahead" if d >= thr - eps else ("behind" if d <= -thr + eps else "aligned")


def phase(d: float, v: float) -> str:
    """HVDI-derived curve position. Not Gartner's placement."""
    _check_number(d, "d")
    _check_number(v, "v")
    if d >= 1 - _EPS:
        return "rising" if v < 1.5 else "peak"
    if d < 0:
        return "underrated"
    return "plateau" if v >= 3 else "slope"


def q_band(q: int) -> str:
    """Capital-quality band: 0-1 thin, 2 concentrated, 3-4 committed."""
    _check_score(q, "Q")
    return "thin" if q <= 1 else ("concentrated" if q == 2 else "committed")


# ---------- gates and outlook ----------
def gate_applies(g: Mapping, medium: str) -> bool:
    """True if gate g applies to this physical medium ('all' or a list of media)."""
    return g["applies"] == "all" or medium in g["applies"]


def gate_status(
    gates: Mapping[str, Mapping], medium: str, override: Optional[Mapping[str, int]] = None
) -> dict[str, Optional[int]]:
    """Status per gate for one medium; None where the gate does not apply.

    ``override`` replaces statuses for a scenario. Unknown gate names or
    statuses outside 0..2 raise ValueError.
    """
    override = dict(override or {})
    unknown = set(override) - set(gates)
    if unknown:
        raise ValueError(f"override names unknown gates: {sorted(unknown)}")
    out: dict[str, Optional[int]] = {}
    for k, g in gates.items():
        s = override.get(k, g["status"])
        if s not in GATE_LEVELS:
            raise ValueError(f"gate {k!r} status must be 0, 1 or 2, got {s!r}")
        out[k] = s if gate_applies(g, medium) else None
    return out


def worst_gate(st: Mapping[str, Optional[int]]) -> int:
    """Highest applicable gate status; 0 when no gate applies."""
    vals = [v for v in st.values() if v is not None]
    return max(vals) if vals else 0


def momentum(ms: Mapping, q: int, worst: int) -> dict[str, int]:
    """Four outlook components, each -1..+1, and their total. The rule is uncalibrated."""
    _check_score(q, "Q")
    if worst not in GATE_LEVELS:
        raise ValueError(f"worst gate must be 0, 1 or 2, got {worst!r}")
    if ms["punctual"] not in (-1, 0, 1):
        raise ValueError(f"punctual must be -1, 0 or 1, got {ms['punctual']!r}")
    m_mile = 1 if (ms["due_within_12m"] and ms["targets_weak_leg"]) else 0
    m_punc = ms["punctual"]
    m_cap = 1 if q >= 3 else (-1 if q <= 1 else 0)
    m_gate = -1 if worst >= 2 else 0
    return dict(
        milestone=m_mile, punctual=m_punc, capital=m_cap, gate=m_gate, total=m_mile + m_punc + m_cap + m_gate
    )


def projection(cls: str, m: int, worst: int) -> str:
    """Outlook label. A binding gate (2) overrides everything: non-compensatory."""
    if cls not in ("ahead", "aligned", "behind"):
        raise ValueError(f"unknown class {cls!r}")
    if worst >= 2:
        return "blocked"
    if cls == "ahead":
        return "closing" if m >= 1 else ("stalling" if m <= -1 else "uncertain")
    return "holding" if m >= 0 else "at_risk"


def weakest_link(values: Iterable[int]) -> int:
    """Minimum of a non-empty collection of scores."""
    vals = list(values)
    if not vals:
        raise ValueError("weakest_link needs at least one value")
    return min(vals)


def clip(x: int) -> int:
    """Clamp to the rubric range 0..4."""
    return max(SCORE_MIN, min(SCORE_MAX, x))


# ---------- robustness ----------
def monte_carlo(
    scores: Mapping[str, int], confs: Mapping[str, str], n: int = 20000, seed: int = 7, conc: float = 4.0
) -> dict:
    """Share of random re-scorings that keep each verdict.

    Each draw takes weights from Dirichlet(conc) and shifts each of H, T, A, E
    by one level (up or down, clipped to 0..4) with a probability set by that
    cell's confidence (P_SHIFT). Returns verdict shares ``p`` and the 5th, 50th
    and 95th percentile of D. Deterministic for a given seed.
    """
    keys = ("H", "T", "A", "E")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError(f"n must be a positive integer, got {n!r}")
    if conc <= 0:
        raise ValueError("conc must be positive")
    for k in keys:
        if k not in scores or k not in confs:
            raise ValueError(f"scores and confs must both contain {k!r}")
        _check_score(scores[k], k)
        if confs[k] not in P_SHIFT:
            raise ValueError(f"confidence for {k} must be one of {sorted(P_SHIFT)}, got {confs[k]!r}")
    rng = random.Random(seed)
    out = {"ahead": 0, "aligned": 0, "behind": 0}
    ds: list[float] = []
    for _ in range(n):
        g = [rng.gammavariate(conc, 1) for _ in range(3)]
        s = sum(g)
        w = [x / s for x in g]
        p = {}
        for k in keys:
            x = scores[k]
            if rng.random() < P_SHIFT[confs[k]]:
                x = clip(x + (1 if rng.random() < 0.5 else -1))
            p[k] = x
        d = p["H"] - (w[0] * p["T"] + w[1] * p["A"] + w[2] * p["E"])
        ds.append(d)
        out[classify(d)] += 1
    ds.sort()
    return dict(
        p={k: v / n for k, v in out.items()},
        d05=ds[int(0.05 * n)],
        d50=ds[n // 2],
        d95=ds[min(n - 1, int(0.95 * n))],
    )


# ---------- bounded economics ----------
def pj_per_bit(watts: float, bits_per_s: float) -> float:
    """Energy per bit in picojoules. Both inputs must be positive."""
    if watts < 0 or bits_per_s <= 0:
        raise ValueError("watts must be >= 0 and bits_per_s > 0")
    return watts / bits_per_s * 1e12


def breakeven(
    dw: float = 7.5,
    price: float = 0.08,
    pue: float = 1.2,
    years: float = 4,
    rate: float = 0.0,
    cap_cost: float = 0.0,
) -> dict[str, float]:
    """Value per module of a power saving ``dw`` watts.

    price: $/kWh. pue: facility overhead (>= 1). years: service life.
    rate: discount rate (0 = undiscounted). cap_cost: $/W of site capacity freed.
    """
    if dw < 0 or price < 0 or cap_cost < 0:
        raise ValueError("dw, price and cap_cost must be non-negative")
    if pue < 1:
        raise ValueError("pue must be at least 1")
    if years <= 0:
        raise ValueError("years must be positive")
    if rate < 0:
        raise ValueError("rate must be non-negative")
    kwh = dw * 8760 / 1000 * pue
    annual = kwh * price
    pv = annual * years if rate == 0 else annual * (1 - (1 + rate) ** -years) / rate
    return dict(
        kwh_per_year=kwh,
        annual=annual,
        energy_value=pv,
        capacity_value=dw * pue * cap_cost,
        total=pv + dw * pue * cap_cost,
    )


def leverage_breakeven(net_share: float = 0.15, premium: float = 0.20) -> float:
    """Useful-output gain needed for a network costing ``premium`` more (a fraction)
    to pay for itself when the network is ``net_share`` of cluster cost.
    Cost rises by net_share * premium; output must rise by the same fraction."""
    if not 0 < net_share < 1:
        raise ValueError("net_share must be between 0 and 1 (exclusive)")
    if premium < 0:
        raise ValueError("premium must be non-negative")
    return net_share * premium
