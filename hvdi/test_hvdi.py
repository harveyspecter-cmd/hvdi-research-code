# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
# Contact: bpgp25sushant@iima.ac.in
#
# PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
import itertools, math, random, pytest
import hvdi as h, data as d


# ---------- arithmetic ----------
def test_value_and_gap_known():
    assert h.value(4, 4, 2) == pytest.approx(10 / 3)
    assert h.gap(3, 1, 1, 1) == pytest.approx(2.0)
    assert h.gap(4, 4, 4, 2, (0.25, 0.25, 0.5)) == pytest.approx(1.0)


def test_weights_must_sum_to_one():
    with pytest.raises(ValueError):
        h.value(1, 1, 1, (0.5, 0.5, 0.5))


def test_bounds_exhaustive():
    for H, T, A, E in itertools.product(range(5), repeat=4):
        for w in d.WEIGHTS.values():
            g = h.gap(H, T, A, E, w)
            assert -4 - 1e-9 <= g <= 4 + 1e-9


def test_monotonic_exhaustive():
    for H, T, A, E in itertools.product(range(4), repeat=4):
        for w in d.WEIGHTS.values():
            g = h.gap(H, T, A, E, w)
            assert h.gap(H + 1, T, A, E, w) > g
            assert (
                h.gap(H, T + 1, A, E, w) < g and h.gap(H, T, A + 1, E, w) < g and h.gap(H, T, A, E + 1, w) < g
            )


def test_equal_weight_permutation_invariant():
    for T, A, E in itertools.product(range(5), repeat=3):
        vs = {round(h.value(*p), 12) for p in itertools.permutations((T, A, E))}
        assert len(vs) == 1


def test_classify_thresholds():
    assert h.classify(1.0) == "ahead" and h.classify(0.999) == "aligned"
    assert h.classify(-1.0) == "behind" and h.classify(-0.999) == "aligned"
    assert h.classify(-2.0) == "behind" and h.classify(2.0) == "ahead"


def test_classify_float_edge():  # 3 - (3+2+1)/3 must be exactly 'ahead'
    assert h.classify(h.gap(3, 3, 2, 1)) == "ahead"


def test_phase_rules():
    assert h.phase(2.0, 1.0) == "rising" and h.phase(1.33, 1.67) == "peak"
    assert (
        h.phase(0.67, 2.33) == "slope"
        and h.phase(0.67, 3.33) == "plateau"
        and h.phase(-0.33, 2.33) == "underrated"
    )


# ---------- gates, momentum, projection ----------
def test_gate_applicability():
    st = h.gate_status(d.GATES, "copper")
    assert st["lasers"] is None and st["power"] == 1
    st = h.gate_status(d.GATES, "optics", {"lasers": 2})
    assert st["lasers"] == 2 and h.worst_gate(st) == 2


def test_gate_noncompensatory():
    m = h.momentum(dict(due_within_12m=True, targets_weak_leg=True, punctual=1), 4, 2)
    assert h.projection("ahead", m["total"], 2) == "blocked" and h.projection("aligned", 9, 2) == "blocked"


def test_momentum_components():
    m = h.momentum(dict(due_within_12m=True, targets_weak_leg=False, punctual=-1), 1, 1)
    assert m == dict(milestone=0, punctual=-1, capital=-1, gate=0, total=-2)


def test_weakest_link():
    assert h.weakest_link([3, 4, 1, 2]) == 1


# ---------- engineering and economics ----------
def test_pj_per_bit():
    assert h.pj_per_bit(640, 51.2e12) == pytest.approx(12.5)
    assert h.pj_per_bit(2218, 51.2e12) == pytest.approx(43.32, abs=0.01)
    assert h.pj_per_bit(3820, 102.4e12) == pytest.approx(37.30, abs=0.01)
    assert h.pj_per_bit(8.5, 800e9) == pytest.approx(10.625)


def test_breakeven_hand_calc():
    b = h.breakeven(7.5, 0.08, 1.2, 4)
    assert b["kwh_per_year"] == pytest.approx(78.84) and b["annual"] == pytest.approx(6.3072)
    assert b["energy_value"] == pytest.approx(25.2288)


def test_breakeven_discounting_and_linearity():
    assert h.breakeven(rate=0.08)["energy_value"] < h.breakeven(rate=0)["energy_value"]
    assert h.breakeven(dw=15)["total"] == pytest.approx(2 * h.breakeven(dw=7.5)["total"])
    assert h.breakeven(cap_cost=10)["capacity_value"] == pytest.approx(7.5 * 1.2 * 10)
    b = h.breakeven(rate=1e-9)
    assert b["energy_value"] == pytest.approx(h.breakeven()["energy_value"], rel=1e-6)


def test_actor_ratios():
    a = {(x["actor"], x["metric"]): x["value"] for x in d.ACTORS}
    assert (
        a[("Amazon", "Capex / operating cash flow")] == 182
        and a[("Alphabet", "Capex / operating cash flow")] == 122
        and a[("Meta", "Capex / operating cash flow")] == 103
    )
    assert (
        43 + 28 == a[("Credo", "Top-2 customer share of revenue")]
        and 16 + 15 + 13 == a[("NVIDIA", "Top-3 direct customer share of revenue")]
    )


# ---------- data integrity ----------
KEYS = ("H", "T", "A", "Q", "E")


def test_scores_valid_and_sourced():
    for cid, c in d.CATS.items():
        for k in KEYS:
            x = c[k]
            assert isinstance(x["v"], int) and 0 <= x["v"] <= 4, (cid, k)
            assert x["conf"] in h.P_SHIFT and x["why"]
            for sid in x["src"]:
                assert sid in d.SOURCES, (cid, k, sid)
        for sid in c["milestone"]["src"]:
            assert sid in d.SOURCES


def test_admission_rule():
    for cid, c in d.CATS.items():
        for k in ("T", "A", "Q", "E"):
            x = c[k]
            if x["v"] >= 3:
                assert x["basis"] in ("buyer", "independent", "filing"), (cid, k)
            if x["v"] >= 3:
                assert x["src"], (cid, k)
            if x["v"] >= 2:
                assert x["basis"] != "none", (cid, k)


def test_gate_sources_and_scenarios():
    for g in d.GATES.values():
        assert g["status"] in (0, 1, 2) and all(sid in d.SOURCES for sid in g["src"])
    for sc in d.SCENARIOS.values():
        assert set(sc["set"]) <= set(d.GATES)


# ---------- robustness properties ----------
def test_monte_carlo_reproducible_and_normalized():
    sc = dict(H=3, T=1, A=1, E=1)
    cf = dict(H="high", T="high", A="high", E="high")
    r1 = h.monte_carlo(sc, cf, n=4000, seed=1)
    r2 = h.monte_carlo(sc, cf, n=4000, seed=1)
    assert r1 == r2 and sum(r1["p"].values()) == pytest.approx(1) and r1["d05"] <= r1["d50"] <= r1["d95"]


def test_monte_carlo_seed_stability():
    sc = dict(H=3, T=3, A=2, E=2)
    cf = dict(H="medium", T="medium", A="medium", E="medium")
    ps = [h.monte_carlo(sc, cf, n=20000, seed=s)["p"]["aligned"] for s in (1, 2, 3, 4, 5)]
    assert max(ps) - min(ps) < 0.02


def test_monte_carlo_no_noise_limit():
    old = dict(h.P_SHIFT)
    h.P_SHIFT.update(high=0.0)
    try:
        r = h.monte_carlo(dict(H=3, T=1, A=1, E=1), dict(H="high", T="high", A="high", E="high"), n=2000)
        assert r["p"]["ahead"] == 1.0 and r["d05"] == pytest.approx(2.0) and r["d95"] == pytest.approx(2.0)
    finally:
        h.P_SHIFT.update(old)


def test_scores_reproduced_after_16_nov_claims_revision():
    assert h.leverage_breakeven(0.15, 0.20) == pytest.approx(0.03) and h.leverage_breakeven(0.2, 0) == 0
    assert h.leverage_breakeven(0.10, 0.5) < h.leverage_breakeven(0.20, 0.5)
    assert round((1 - 0.73) * 100) == 27 and (1 - 0.73) * 16.7 == pytest.approx(4.509)
    exp = {
        "nvlink": 4 / 3,
        "ualink": 1.0,
        "infiniband": 2 / 3,
        "cpo": 2 / 3,
        "uet": 1 / 3,
        "lpo": 1 / 3,
        "aec": 1 / 3,
        "eth_scaleup": 0.0,
        "dpu": -1 / 3,
        "eth_scaleout": -1 / 3,
    }
    for k, v in exp.items():
        c = d.CATS[k]
        assert h.gap(c["H"]["v"], c["T"]["v"], c["A"]["v"], c["E"]["v"]) == pytest.approx(v)


def test_h_cells_match_claims_corpus():
    import pathlib

    import hclaims as hc

    corpus = hc.load_claims(pathlib.Path(__file__).resolve().parent / "claims.csv")
    for cid, c in d.CATS.items():
        st = [x for x, _ in corpus[cid]["stage"]]
        nr = [x for x, _ in corpus[cid]["narrative"]]
        assert c["H"]["v"] == hc.h_from_claims(st, nr)["H"], cid
        assert c["H"]["basis"] == "claims" and c["H"]["src"], cid


def test_every_evidence_cell_cites_a_logged_source():
    import data as d

    for k, c in d.CATS.items():
        for p in "HTAQE":
            assert c[p]["src"], (k, p)
            for sid in c[p]["src"]:
                assert sid in d.SOURCES, (k, p, sid)


def test_audit_leaves_no_unsourced_or_baseless_high_score():
    import data as d

    for k, c in d.CATS.items():
        for p in "TAQE":
            if c[p]["v"] >= 3:
                assert c[p]["basis"] in ("buyer", "independent", "filing"), (k, p)


# ---------- edge cases and input validation (added 12 Nov review) ----------
OK = dict(H=3, T=1, A=1, E=1)
CF = dict(H="low", T="low", A="low", E="low")


@pytest.mark.parametrize("bad", [7, -1, 5])
def test_scores_outside_rubric_rejected(bad):
    with pytest.raises(ValueError):
        h.gap(bad, 1, 1, 1)
    with pytest.raises(ValueError):
        h.value(1, bad, 1)
    with pytest.raises(ValueError):
        h.q_band(bad)


@pytest.mark.parametrize("bad", [2.5, "3", None, True])
def test_non_integer_scores_rejected(bad):
    with pytest.raises(TypeError):
        h.gap(bad, 1, 1, 1)


@pytest.mark.parametrize("w", [(1.5, -0.25, -0.25), (0.5, 0.5), (0.2, 0.2, 0.2)])
def test_bad_weights_rejected(w):
    with pytest.raises(ValueError):
        h.value(1, 1, 1, w)


def test_extreme_gaps_and_boundaries():
    assert h.gap(4, 0, 0, 0) == 4 and h.gap(0, 4, 4, 4) == pytest.approx(-4)
    assert h.classify(h.gap(4, 0, 0, 0)) == "ahead"
    assert h.classify(h.gap(0, 4, 4, 4)) == "behind"
    assert h.classify(0) == "aligned"
    with pytest.raises(TypeError):
        h.classify(None)
    with pytest.raises(ValueError):
        h.classify(0.5, thr=0)


def test_monte_carlo_rejects_bad_input():
    with pytest.raises(ValueError):
        h.monte_carlo(OK, CF, n=0)
    with pytest.raises(ValueError):
        h.monte_carlo(OK, dict(CF, H="certain"))
    with pytest.raises(ValueError):
        h.monte_carlo(dict(OK, H=9), CF)
    with pytest.raises(ValueError):
        h.monte_carlo({"H": 3}, CF)
    with pytest.raises(ValueError):
        h.monte_carlo(OK, CF, conc=0)


def test_monte_carlo_smallest_run_and_clipping():
    r = h.monte_carlo(OK, CF, n=1)
    assert sum(r["p"].values()) == pytest.approx(1) and r["d05"] == r["d95"]
    top = h.monte_carlo(dict(H=4, T=0, A=0, E=0), CF, n=2000)
    assert -4 <= top["d05"] <= top["d95"] <= 4


def test_economics_reject_bad_input():
    with pytest.raises(ValueError):
        h.pj_per_bit(10, 0)
    with pytest.raises(ValueError):
        h.pj_per_bit(-1, 1e9)
    for kw in (dict(years=-1), dict(years=0), dict(pue=0.9), dict(dw=-1), dict(rate=-0.1), dict(price=-1)):
        with pytest.raises(ValueError):
            h.breakeven(**kw)
    for a in ((0, 0.2), (1, 0.2), (0.15, -0.1)):
        with pytest.raises(ValueError):
            h.leverage_breakeven(*a)
    assert h.breakeven(dw=0)["total"] == 0 and h.pj_per_bit(0, 1e9) == 0


def test_gates_reject_bad_input_and_handle_empty():
    g = {"power": dict(status=1, applies="all")}
    assert h.worst_gate({}) == 0 and h.worst_gate({"a": None}) == 0
    assert h.gate_status(g, "copper", {"power": 2}) == {"power": 2}
    with pytest.raises(ValueError):
        h.gate_status(g, "copper", {"nosuch": 2})
    with pytest.raises(ValueError):
        h.gate_status(g, "copper", {"power": 3})
    with pytest.raises(ValueError):
        h.weakest_link([])
    with pytest.raises(ValueError):
        h.projection("unknown", 0, 0)
    assert h.projection("ahead", 5, 2) == "blocked"  # a binding gate beats any momentum


def test_engine_does_not_use_assert_for_validation():
    import ast, inspect

    tree = ast.parse(inspect.getsource(h))
    assert not [n for n in ast.walk(tree) if isinstance(n, ast.Assert)]


def test_every_public_function_documented_and_typed():
    import inspect

    for name, f in inspect.getmembers(h, inspect.isfunction):
        if name.startswith("_") or f.__module__ != h.__name__:
            continue
        assert f.__doc__, name
        assert "return" in f.__annotations__, name


def test_data_file_validation_catches_bad_rows(monkeypatch):
    import copy

    bad = copy.deepcopy(d.CATS)
    first = next(iter(bad))
    bad[first]["T"]["v"] = 9
    monkeypatch.setattr(d, "CATS", bad)
    with pytest.raises(ValueError):
        d.validate()
    bad[first]["T"]["v"] = 2
    bad[first]["T"]["src"] = ["S999"]
    with pytest.raises(ValueError):
        d.validate()
