# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
#
# PROPRIETARY (ALL RIGHTS RESERVED): Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
"""Evidence dataset loader.

All scores, evidence text, gates, scenarios and sources live in ``evidence.json``
so that they can be reviewed and edited without touching code. This module loads
that file, checks its shape, and exposes it under the names the engine uses.

Each score cell is ``{"v": level 0-4, "basis": who holds the evidence,
"conf": "high" | "medium" | "low", "ev": evidence text, "src": [ledger IDs]}``.
"""

from __future__ import annotations

import json
import pathlib

_PATH = pathlib.Path(__file__).resolve().parent / "evidence.json"
_RAW = json.loads(_PATH.read_text(encoding="utf-8"))

ASOF: str = _RAW["asof"]
AUDIT: str = _RAW["audit"]
WEIGHTS: dict[str, tuple[float, ...]] = {k: tuple(v) for k, v in _RAW["weights"].items()}
WEIGHT_NAMES: dict[str, str] = _RAW["weight_names"]
CATS: dict[str, dict] = _RAW["categories"]
GATES: dict[str, dict] = _RAW["gates"]
SCENARIOS: dict[str, dict] = _RAW["scenarios"]
ACTORS: list[dict] = _RAW["actors"]
ENERGY: list = [tuple(e) if isinstance(e, list) else e for e in _RAW["energy"]]
AUDIT_SCORE_CHANGES: list[tuple] = [tuple(c) for c in _RAW["audit_score_changes"]]
SOURCES: dict[str, tuple[str, str]] = {k: (v["text"], v["url"]) for k, v in _RAW["sources"].items()}

PARAMS = ("H", "T", "A", "Q", "E")
CONFIDENCE = ("high", "medium", "low")


def validate() -> None:
    """Raise ValueError if the data file breaks a structural rule."""
    for cid, cat in CATS.items():
        for p in PARAMS:
            cell = cat.get(p)
            if not isinstance(cell, dict):
                raise ValueError(f"{cid}.{p}: missing score cell")
            if not isinstance(cell["v"], int) or not 0 <= cell["v"] <= 4:
                raise ValueError(f"{cid}.{p}: score must be an integer 0..4")
            if cell["conf"] not in CONFIDENCE:
                raise ValueError(f"{cid}.{p}: unknown confidence {cell['conf']!r}")
            missing = [s for s in cell["src"] if s not in SOURCES]
            if missing:
                raise ValueError(f"{cid}.{p}: sources not in ledger: {missing}")
    for name, w in WEIGHTS.items():
        if len(w) != 3 or abs(sum(w) - 1) > 1e-9:
            raise ValueError(f"weights {name!r} must be three numbers summing to 1")


validate()
