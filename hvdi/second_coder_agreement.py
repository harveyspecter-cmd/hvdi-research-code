"""Compare a returned second-coder workbook with the first coder's claims.csv.

Usage: python3 second_coder_agreement.py <returned .xlsx, or the Google Form responses sheet saved as .csv>
Reports kind agreement, level agreement (exact, within one, quadratic-weighted kappa),
H per technology under rule v3.1, and the verdict each H implies with the published T, A, E.
"""
import csv
import sys
from collections import defaultdict

from openpyxl import load_workbook

import hclaims as hc

KIND = {"Stage": "stage", "Narrative": "narrative", "Not a claim": "none"}


def qwk(a, b, k=5):
    n = len(a)
    if n == 0:
        return float("nan")
    o = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        o[x][y] += 1
    ra = [sum(r) for r in o]
    cb = [sum(o[i][j] for i in range(k)) for j in range(k)]
    num = sum(((i - j) ** 2 / (k - 1) ** 2) * o[i][j] for i in range(k) for j in range(k))
    den = sum(((i - j) ** 2 / (k - 1) ** 2) * ra[i] * cb[j] / n for i in range(k) for j in range(k))
    return 1 - num / den if den else float("nan")


def main(path):
    key = {r["code"]: r["claim_id"] for r in csv.DictReader(open("coder_key.csv", encoding="utf-8"))}
    first = {r["claim_id"]: r for r in csv.DictReader(open("claims.csv", encoding="utf-8"))}
    if path.lower().endswith(".csv"):  # Google Form responses sheet, downloaded as CSV (first response row)
        resp = next(csv.DictReader(open(path, encoding="utf-8")))
        num = {k.split(".")[0]: v for k, v in resp.items() if k and k.split(".")[0].isdigit()}
        if num:  # short form: one combined answer per statement, e.g. "Stage 3  ·  volume production"
            key = {r["code"]: r["claim_id"] for r in csv.DictReader(open("coder_key_short.csv", encoding="utf-8"))}
            rows = []
            for code in sorted(key):
                ans = num.get(str(int(code[1:])), "")
                head = ans.split("\u00b7")[0].strip()
                kind = "Not a claim" if head.startswith("Not a claim") else (head.split()[0] if head else None)
                lvl = int(head.split()[1]) if kind in ("Stage", "Narrative") else None
                rows.append([None, code] + [None] * 6 + [kind, lvl])
            return report(rows, key, first)
        rows = []
        for code in sorted(key):
            kind = resp.get(f"{code} Kind") or None
            lvl = resp.get(f"{code} Level") or None
            rows.append([None, code] + [None] * 6 + [kind, int(lvl) if lvl not in (None, "") else None])
    else:
        ws = load_workbook(path, data_only=True)["4 Coding sheet"]
        rows = list(ws.iter_rows(min_row=2, values_only=True))
    return report(rows, key, first)


def report(rows, key, first):
    kind_same = lvl_a = lvl_b = 0
    a, b = [], []
    second = defaultdict(lambda: {"stage": [], "narrative": []})
    missing = []
    for r in rows:
        code, kind, lvl = r[1], r[8], r[9]
        if not code:
            continue
        cid = key[code]; f = first[cid]
        if kind is None:
            missing.append(code); continue
        k2 = KIND[kind]
        kind_same += k2 == f["kind"]
        if k2 != "none" and lvl is not None:
            second[f["tech"]][k2].append(int(lvl))
            if k2 == f["kind"]:
                a.append(int(f["level"])); b.append(int(lvl))
    n = len(rows) - len(missing)
    exact = sum(x == y for x, y in zip(a, b)); within = sum(abs(x - y) <= 1 for x, y in zip(a, b))
    print(f"rows coded {n}/{len(rows)}; kind agreement {kind_same}/{n} = {kind_same / max(n, 1):.0%}")
    print(f"level, same kind: exact {exact}/{len(a)} = {exact / max(len(a), 1):.0%}; within one {within / max(len(a), 1):.0%}; "
          f"quadratic-weighted kappa {qwk(a, b):.2f}")
    import data as d
    first_claims = hc.load_claims("claims.csv")
    print("tech | H first | H second | D first | D second | verdict first | verdict second")
    same_v = 0
    for t, cl in first_claims.items():
        coded = {key[r[1]] for r in rows if r[8]}
        if not all(cid in coded for cid, f in first.items() if f["tech"] == t and f["include"] == "yes"):
            continue  # H is only reproduced for technologies whose claims were all coded
        h1 = hc.h_from_claims([l for l, _ in cl["stage"]], [l for l, _ in cl["narrative"]])["H"]
        s2 = second[t]
        st = [x for x in s2["stage"] if x > 0]
        h2 = hc.h_from_claims(st, s2["narrative"])["H"]
        c = d.CATS[t] if hasattr(d, "CATS") else None
        v = None
        if c:
            v = sum(c[x]["v"] for x in ("T", "A", "E")) / 3
        verdict = lambda D: "ahead" if D >= 1 else ("proof ahead" if D <= -1 else "aligned")
        if v is None:
            print(t, h1, h2); continue
        d1, d2 = h1 - v, h2 - v
        same_v += verdict(d1) == verdict(d2)
        print(f"{t} | {h1} | {h2} | {d1:+.2f} | {d2:+.2f} | {verdict(d1)} | {verdict(d2)}")
    print(f"verdicts identical: {same_v} of the technologies fully coded")
    if missing:
        print("uncoded rows:", ", ".join(missing))


if __name__ == "__main__":
    main(sys.argv[1])
