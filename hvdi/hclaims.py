# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
#
# PROPRIETARY (ALL RIGHTS RESERVED): Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
"""Claimed maturity (H) from a corpus of dated public claims.

Two kinds of claim are coded on one 0-4 scale:
  stage      what deployment stage is asserted now
  narrative  how the technology's maturity, momentum or destiny is framed

H is the higher of the stage level and the narrative level. Each level is the
highest rubric level that a strict majority of that kind's claims reach. The
narrative level counts only when at least ``MIN_NARRATIVE`` claims support it,
so that a single editorial cannot set H.

The robustness test resamples the claims themselves (bootstrap) and, for claims
the coder marked as torn, picks the coded or the alternative level at random.
"""

from __future__ import annotations

import csv
import pathlib
import random
from typing import Iterable, Mapping, Optional, Sequence

import hvdi as h

MIN_NARRATIVE = 2
KINDS = ("stage", "narrative")


def majority_level(levels: Sequence[int]) -> int:
    """Highest level k such that more than half of the levels are >= k."""
    vals = [h._check_score(x, "claim level") for x in levels]
    if not vals:
        raise ValueError("majority_level needs at least one level")
    for k in range(h.SCORE_MAX, h.SCORE_MIN - 1, -1):
        if sum(v >= k for v in vals) * 2 > len(vals):
            return k
    return h.SCORE_MIN


def h_from_claims(stage: Sequence[int], narrative: Sequence[int], min_narrative: int = MIN_NARRATIVE) -> dict:
    """H and its two components. Returns stage, narrative (None if too few claims) and H."""
    if min_narrative < 1:
        raise ValueError("min_narrative must be at least 1")
    hs = majority_level(stage) if stage else None
    hn = majority_level(narrative) if len(narrative) >= min_narrative else None
    parts = [x for x in (hs, hn) if x is not None]
    if not parts:
        raise ValueError("no admissible claims: need stage claims or enough narrative claims")
    return dict(stage=hs, narrative=hn, H=max(parts))


def load_claims(path: pathlib.Path) -> dict[str, dict[str, list[tuple[int, Optional[int]]]]]:
    """Read claims.csv; keep rows with include=yes. Returns tech -> kind -> [(level, alt_level)]."""
    out: dict[str, dict[str, list[tuple[int, Optional[int]]]]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["include"].strip().lower() != "yes":
                continue
            kind = row["kind"].strip()
            if kind not in KINDS:
                raise ValueError(f"{row['claim_id']}: unknown kind {kind!r}")
            lvl = int(row["level"])
            alt = int(row["alt_level"]) if row["alt_level"].strip() else None
            h._check_score(lvl, row["claim_id"])
            if alt is not None:
                h._check_score(alt, row["claim_id"] + " alt")
            out.setdefault(row["tech"], {k: [] for k in KINDS})[kind].append((lvl, alt))
    return out


def _draw(rows: Sequence[tuple[int, Optional[int]]], rng: random.Random) -> list[int]:
    """Bootstrap resample of claims; torn claims take their alternative level half the time."""
    picks = [rows[rng.randrange(len(rows))] for _ in rows]
    return [alt if (alt is not None and rng.random() < 0.5) else lvl for lvl, alt in picks]


def monte_carlo_claims(
    claims: Mapping[str, list],
    t: int,
    a: int,
    e: int,
    confs: Mapping[str, str],
    n: int = 20000,
    seed: int = 7,
    conc: float = 4.0,
) -> dict:
    """Verdict shares when H comes from resampled claims and T, A, E and weights vary as in hvdi."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError(f"n must be a positive integer, got {n!r}")
    for k in ("T", "A", "E"):
        if confs.get(k) not in h.P_SHIFT:
            raise ValueError(f"confidence for {k} must be one of {sorted(h.P_SHIFT)}")
    base = dict(T=h._check_score(t, "T"), A=h._check_score(a, "A"), E=h._check_score(e, "E"))
    rng = random.Random(seed)
    out = {"ahead": 0, "aligned": 0, "behind": 0}
    hs: list[int] = []
    ds: list[float] = []
    for _ in range(n):
        st = _draw(claims["stage"], rng) if claims["stage"] else []
        nr = _draw(claims["narrative"], rng) if claims["narrative"] else []
        hv = h_from_claims(st, nr)["H"]
        g = [rng.gammavariate(conc, 1) for _ in range(3)]
        s = sum(g)
        p = {}
        for k in ("T", "A", "E"):
            x = base[k]
            if rng.random() < h.P_SHIFT[confs[k]]:
                x = h.clip(x + (1 if rng.random() < 0.5 else -1))
            p[k] = x
        d = hv - (g[0] * p["T"] + g[1] * p["A"] + g[2] * p["E"]) / s
        hs.append(hv)
        ds.append(d)
        out[h.classify(d)] += 1
    ds.sort()
    return dict(
        p={k: v / n for k, v in out.items()},
        h_share={v: hs.count(v) / n for v in sorted(set(hs))},
        d05=ds[int(0.05 * n)],
        d50=ds[n // 2],
        d95=ds[min(n - 1, int(0.95 * n))],
    )


def scorecard(claims_path: pathlib.Path, cats: Mapping[str, Mapping]) -> list[dict]:
    """H, gap and robustness for every technology that has claims."""
    corpus = load_claims(claims_path)
    rows = []
    for cid, cat in cats.items():
        if cid not in corpus:
            raise ValueError(f"no claims for {cid}")
        c = corpus[cid]
        hc = h_from_claims([x for x, _ in c["stage"]], [x for x, _ in c["narrative"]])
        t, a, e = (cat[k]["v"] for k in ("T", "A", "E"))
        d = h.gap(hc["H"], t, a, e)
        mc = monte_carlo_claims(c, t, a, e, {k: cat[k]["conf"] for k in ("T", "A", "E")})
        rows.append(
            dict(
                id=cid,
                n_stage=len(c["stage"]),
                n_narr=len(c["narrative"]),
                **hc,
                V=h.value(t, a, e),
                D=d,
                verdict=h.classify(d),
                mc=mc,
            )
        )
    return rows


def iter_report(rows: Iterable[dict]) -> Iterable[str]:
    """Plain-text table of the scorecard."""
    yield f"{'tech':13} st nr | Hs Hn H |  V     D    verdict  | ahead aligned behind | H draws"
    for r in rows:
        p = r["mc"]["p"]
        hn = "-" if r["narrative"] is None else r["narrative"]
        hd = " ".join(f"{k}:{v:.0%}" for k, v in r["mc"]["h_share"].items())
        yield (
            f"{r['id']:13} {r['n_stage']:2} {r['n_narr']:2} | {r['stage']}  {hn}  {r['H']} | {r['V']:.2f} "
            f"{r['D']:+.2f}  {r['verdict']:8} | {p['ahead']:5.0%} {p['aligned']:6.0%} {p['behind']:6.0%} | {hd}"
        )
