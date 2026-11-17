# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
# Contact: bpgp25sushant@iima.ac.in
#
# PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
"""Tests for the claim-based H rule and its robustness test."""

import pytest

import hclaims as hc

CF = dict(T="medium", A="medium", E="low")


@pytest.mark.parametrize(
    "levels,expected",
    [
        ([3], 3),
        ([2, 3, 3], 3),
        ([2, 2, 3], 2),
        ([3, 4], 3),
        ([4, 4], 4),
        ([0, 3, 4], 3),
        ([1, 1, 2, 2], 1),
        ([0, 0, 4], 0),
        ([3, 3, 4, 4], 3),
        ([4, 4, 4, 3], 4),
    ],
)
def test_majority_level(levels, expected):
    assert hc.majority_level(levels) == expected


def test_majority_level_rejects_bad_input():
    with pytest.raises(ValueError):
        hc.majority_level([])
    with pytest.raises(ValueError):
        hc.majority_level([5])
    with pytest.raises(TypeError):
        hc.majority_level([2.5])


def test_h_is_max_of_stage_and_narrative():
    assert hc.h_from_claims([2, 2, 3], [4, 4]) == dict(stage=2, narrative=4, H=4)
    assert hc.h_from_claims([3, 3], [0, 1]) == dict(stage=3, narrative=0, H=3)


def test_single_narrative_claim_is_ignored():
    assert hc.h_from_claims([2], [4]) == dict(stage=2, narrative=None, H=2)


def test_narrative_alone_is_enough_when_no_stage_claims():
    assert hc.h_from_claims([], [3, 3])["H"] == 3


def test_no_admissible_claims_raises():
    with pytest.raises(ValueError):
        hc.h_from_claims([], [4])
    with pytest.raises(ValueError):
        hc.h_from_claims([2], [2], min_narrative=0)


def test_h_never_below_either_component():
    import itertools

    for st in itertools.product(range(5), repeat=3):
        for nr in itertools.product(range(5), repeat=2):
            r = hc.h_from_claims(list(st), list(nr))
            assert r["H"] >= r["stage"] and r["H"] >= r["narrative"]


def test_monte_carlo_claims_deterministic_and_bounded():
    claims = dict(stage=[(2, None), (3, 2), (2, None)], narrative=[(4, 3), (4, None)])
    a = hc.monte_carlo_claims(claims, 3, 2, 2, CF, n=3000)
    b = hc.monte_carlo_claims(claims, 3, 2, 2, CF, n=3000)
    assert a == b
    assert sum(a["p"].values()) == pytest.approx(1)
    assert sum(a["h_share"].values()) == pytest.approx(1)
    assert set(a["h_share"]) <= {2, 3, 4}
    assert -4 <= a["d05"] <= a["d95"] <= 4


def test_unanimous_claims_give_fixed_h():
    claims = dict(stage=[(3, None)] * 4, narrative=[])
    r = hc.monte_carlo_claims(claims, 1, 1, 1, CF, n=500)
    assert r["h_share"] == {3: 1.0}


def test_monte_carlo_claims_rejects_bad_input():
    claims = dict(stage=[(2, None)], narrative=[])
    with pytest.raises(ValueError):
        hc.monte_carlo_claims(claims, 3, 2, 2, CF, n=0)
    with pytest.raises(ValueError):
        hc.monte_carlo_claims(claims, 3, 2, 2, dict(CF, E="certain"))
    with pytest.raises(ValueError):
        hc.monte_carlo_claims(claims, 9, 2, 2, CF)


def test_load_claims_filters_and_validates(tmp_path):
    p = tmp_path / "c.csv"
    p.write_text(
        "claim_id,tech,kind,level,alt_level,include\n"
        "a,uet,stage,2,,yes\nb,uet,narrative,3,2,yes\nc,uet,stage,4,,no\n"
    )
    out = hc.load_claims(p)
    assert out == {"uet": {"stage": [(2, None)], "narrative": [(3, 2)]}}
    p.write_text("claim_id,tech,kind,level,alt_level,include\nx,uet,hype,2,,yes\n")
    with pytest.raises(ValueError):
        hc.load_claims(p)
