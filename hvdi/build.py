# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
# Contact: bpgp25sushant@iima.ac.in
#
# PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
import json
import pathlib

import data as d
import hclaims as hc
import hvdi as h

CLAIMS = hc.load_claims(pathlib.Path(__file__).resolve().parent / "claims.csv")


def compute():
    out = {
        "asof": d.ASOF,
        "cats": [],
        "gates": d.GATES,
        "scenarios": d.SCENARIOS,
        "weights": d.WEIGHT_NAMES,
        "actors": d.ACTORS,
        "energy": [dict(label=a, lo=b, hi=c, group=g, src=s) for a, b, c, g, s in d.ENERGY],
        "sources": {k: dict(t=v[0], u=v[1]) for k, v in d.SOURCES.items()},
    }
    for cid, c in d.CATS.items():
        sc = {k: c[k]["v"] for k in "HTAQE"}
        cf = {k: c[k]["conf"] for k in "HTAE"}
        byw = {}
        for wk, w in d.WEIGHTS.items():
            v = h.value(sc["T"], sc["A"], sc["E"], w)
            g = sc["H"] - v
            byw[wk] = dict(V=round(v, 2), D=round(g, 2), cls=h.classify(g), phase=h.phase(g, v))
        # H comes from the claims corpus, so robustness resamples the claims themselves (hclaims.py)
        mc = hc.monte_carlo_claims(CLAIMS[cid], sc["T"], sc["A"], sc["E"], {k: cf[k] for k in "TAE"})
        hres = hc.h_from_claims(
            [x for x, _ in CLAIMS[cid]["stage"]], [x for x, _ in CLAIMS[cid]["narrative"]]
        )
        if hres["H"] != sc["H"]:
            raise SystemExit(
                f"{cid}: H in evidence.json ({sc['H']}) differs from the claims corpus ({hres['H']})"
            )
        base = byw["equal"]["cls"]
        bysc = {}
        for sk, s in d.SCENARIOS.items():
            st = h.gate_status(d.GATES, c["medium"], s["set"])
            worst = h.worst_gate(st)
            m = h.momentum(c["milestone"], sc["Q"], worst)
            bysc[sk] = dict(gates=st, worst=worst, m=m, proj=h.projection(base, m["total"], worst))
        legs = {k: sc[k] for k in "TAE"}
        weak = min(legs, key=legs.get)
        out["cats"].append(
            dict(
                id=cid,
                name=c["name"],
                sub=c["sub"],
                layer=c["layer"],
                medium=c["medium"],
                scores={k: c[k] for k in "HTAQE"},
                byw=byw,
                qband=h.q_band(sc["Q"]),
                weak=weak,
                stability=round(mc["p"][base], 3),
                mc={k: round(v, 3) for k, v in mc["p"].items()},
                d05=round(mc["d05"], 2),
                d95=round(mc["d95"], 2),
                hclaims=dict(
                    stage=hres["stage"],
                    narrative=hres["narrative"],
                    n_stage=len(CLAIMS[cid]["stage"]),
                    n_narr=len(CLAIMS[cid]["narrative"]),
                    h_share={str(k): round(v, 3) for k, v in mc["h_share"].items()},
                ),
                milestone=c["milestone"],
                bysc=bysc,
            )
        )
    return out


RUBRIC = {
    "H": [
        "Little or no claim",
        "A future promise",
        "Imminent or early adoption",
        "In production and solving the problem",
        "The default; contest settled",
    ],
    "T": [
        "None",
        "Specification, datasheet or simulation",
        "Vendor or lab demonstration",
        "Independent or buyer-side evidence at production scale",
        "Multi-generation, documented by operators",
    ],
    "A": [
        "None",
        "Announced, sampling or design wins",
        "Pilot or single-buyer production",
        "Production at two or more buyers",
        "Dominant share or repeat expansion",
    ],
    "Q": [
        "No committed capital found",
        "Venture or strategic capital and announcements only",
        "Recognized revenue, but concentrated, single-buyer or vendor-financed",
        "Revenue from several buyers backed by binding commitments",
        "As level 3, with low concentration and a multi-year record",
    ],
    "E": [
        "None",
        "Vendor-claimed benefit only",
        "One buyer-reported benefit, or a bounded vendor comparison",
        "Buyer-reported benefit against a matched baseline",
        "Documented lifecycle economics at several buyers",
    ],
}


def breakeven_table():
    t = {}
    for p in (0.05, 0.08, 0.12):
        for pue in (1.1, 1.2, 1.4):
            for y in (3, 4, 5):
                for cc in (0, 8, 12):
                    b = h.breakeven(7.5, p, pue, y, 0.0, cc)
                    t[f"{p}|{pue}|{y}|{cc}"] = dict(
                        kwh=round(b["kwh_per_year"], 1),
                        annual=round(b["annual"], 2),
                        energy=round(b["energy_value"], 2),
                        cap=round(b["capacity_value"], 2),
                        total=round(b["total"], 2),
                    )
    return t


if __name__ == "__main__":
    o = compute()
    o["rubric"] = RUBRIC
    o["breakeven"] = breakeven_table()
    o["leverage"] = {
        f"{s}|{p}": round(h.leverage_breakeven(s, p) * 100, 1)
        for s in (0.1, 0.15, 0.2)
        for p in (0.1, 0.2, 0.3, 0.5)
    }
    json.dump(o, open("site/data.json", "w"), indent=1)
    tpl = open("template.html").read()
    assert "/*DATA*/" in tpl
    open("site/index.html", "w").write(
        tpl.replace("/*DATA*/", json.dumps(o, separators=(",", ":")).replace("</", "<\\/"))
    )
    print(
        f"{'category':26}  H T A Q E    V     D   class    phase       Qband        stab  D90%        proj(base)  M"
    )
    for c in o["cats"]:
        s = c["scores"]
        b = c["byw"]["equal"]
        p = c["bysc"]["base"]
        print(
            f"{c['name']:26}  {s['H']['v']} {s['T']['v']} {s['A']['v']} {s['Q']['v']} {s['E']['v']}  {b['V']:.2f} {b['D']:+.2f}  {b['cls']:8} {b['phase']:11} {c['qband']:12} {c['stability']:.2f}  [{c['d05']:+.2f},{c['d95']:+.2f}]  {p['proj']:10} {p['m']['total']:+d}"
        )
    print("\nscenario projections:")
    for sk in d.SCENARIOS:
        print(f" {sk:8}", {c["id"]: c["bysc"][sk]["proj"] for c in o["cats"]})
    print("\nweight-preset class changes:")
    for c in o["cats"]:
        cl = {wk: c["byw"][wk]["cls"] for wk in d.WEIGHTS}
        if len(set(cl.values())) > 1:
            print(" ", c["name"], cl)
