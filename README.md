# HVDI: Hype-to-Value Divergence Index

Research code for the IIMA BPGP Live Project *Beyond the Hype Cycle: A Techno-Economic Value Chain
Framework for AI Networking and Interconnect Hardware, 2025 to 2030* (Sushant Gaurav, BPGP 2025-27).

The index scores ten AI networking technologies on what is claimed (H), technically proven (T),
adopted (A), financially committed (Q) and gained by buyers (E), and keeps external constraints (X)
outside the arithmetic as gates. Evidence is as of 11 November 2026, audited on 12 November 2026.

**Public repository. Copyright © 2026 Sushant Gaurav. All rights reserved; see `LICENSE`.**

- Interactive page (public): https://harveyspecter-cmd.github.io/hvdi-research/
- This repository: https://github.com/harveyspecter-cmd/hvdi-research-code

## 1. What is here

| Path | Contents |
|---|---|
| `hvdi/hvdi.py` | The engine: pure functions for the index, verdicts, gates, outlook, Monte Carlo and the two bounded economic models. Standard library only. |
| `hvdi/evidence.json` | The dataset: every score with its evidence text, basis, confidence and source IDs; gates; scenarios; the source ledger. **Edit this file to change a score, not the code.** |
| `hvdi/data.py` | Loads and validates `evidence.json`. |
| `hvdi/build.py` | Runs the engine over the dataset; writes `results.txt` (console table), `site/data.json` and `site/index.html`. |
| `hvdi/claims.csv` | The claims corpus behind H: 76 included dated public claims (12 Nov 2025 to 11 Nov 2026), each with claimant, kind (stage or narrative), level, alternative level, quote, URL and source ID. **Edit this file to change an H score.** |
| `hvdi/H_RULE.md` | Rule v3.1 for scoring H from claims: the stage and narrative scales and the aggregation rule. |
| `hvdi/hclaims.py` | Computes H from the claims corpus and runs the claim-resampling Monte Carlo. Standard library only. |
| `hvdi/quote_checks_1611.csv`, `hvdi/quote_checks_1611b.csv`, `hvdi/quote_checks_1811.csv` | Live-page checks of the claims: 74 of 76 verbatim on the live page or an official copy, none failed; the other 2 have no quote (pages confirmed live). |
| `hvdi/test_hvdi.py`, `hvdi/test_hclaims.py` | 64 automated tests. |
| `hvdi/make_coder_workbook.py`, `hvdi/make_coder_form.py` (writes `HVDI_Second_Coder_Form.gs`, a Google Apps Script that builds the same questionnaire as a Google Form), `hvdi/make_coder_form_short.py` (30-statement, one-click Google Form; key `hvdi/coder_key_short.csv`), `hvdi/second_coder_agreement.py` (reads the returned .xlsx or the Form responses as .csv), `hvdi/coder_key.csv` | Blind questionnaire for a human second coder (claims shuffled under neutral codes C01-C76, no first-coder levels), and the script that scores a returned workbook: kind agreement, exact and within-one level agreement, quadratic-weighted kappa, H and verdict per technology. Never send the key or this repo to the coder. |
| `hvdi/template.html` | Source of the interactive page. `build.py` injects the data into it. |
| `hvdi/site/` | The built page (`index.html`, self-contained, no external requests) and `data.json`. |
| `hvdi/make_public.py` | Writes the public copy of the page with identifying text removed. |
| `hvdi/shot.py`, `hvdi/figs.py` | Browser smoke test and screenshots (optional). |
| `hvdi/EVIDENCE_AUDIT.md` | Evidence audit of 12 November 2026: what was checked, what changed, falsifiers. |
| `report-src/` | Report text (`body.md`, `appendix.md`), figures (including the framework diagram, `make_framework_fig.py`) and the scripts that build the Word file. |
| `deck-src/` | Slide source (`build.js`). |

## 2. Requirements

- Python 3.9 or later. The engine itself needs nothing else.
- `pytest` to run the tests.
- Optional: `playwright` and a Chrome or Chromium binary (smoke test), `matplotlib`, `python-docx` and
  `pandoc` (report), Node.js with `pptxgenjs` (deck).

## 3. Quick start: run the framework

```bash
git clone <this repository> && cd hvdi-research-code/hvdi
python3 -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python3 -m pytest -q                 # 1. verify the engine: expect "64 passed"
python3 build.py > results.txt       # 2. score all ten technologies and rebuild the page
cat results.txt                      # 3. read the scorecard
```

Step 2 prints one row per technology (scores, proven value V, gap D, verdict, capital-quality band,
Monte Carlo stability, 90% interval, outlook) and regenerates `site/index.html`. Open that file in any
browser to use the interactive page; it needs no server and no network.

The run is deterministic: the Monte Carlo uses 20,000 draws with seed 7, so `results.txt` and
`site/data.json` are identical on every run for the same `evidence.json`.

## 4. Use the engine directly

```python
import hvdi as h

h.gap(3, 1, 1, 1)                         # 2.0  (H=3; T, A, E = 1)  ->  D = H - mean(T, A, E)
h.classify(2.0)                           # 'ahead'   (D >= +1 story ahead; D <= -1 proof ahead)
h.gap(4, 4, 4, 2, (0.25, 0.25, 0.5))      # 1.0  with economics-heavy weights (T, A, E)

r = h.monte_carlo(dict(H=3, T=1, A=1, E=1),
                  dict(H="high", T="medium", A="medium", E="low"))
r["p"]["ahead"], r["d05"], r["d95"]       # share of draws that keep the verdict; 90% interval of D
```

Scores are integer rubric levels 0 to 4. Anything else raises `TypeError` or `ValueError`:

```python
h.gap(7, 1, 1, 1)        # ValueError: H must be 0..4, got 7
h.gap(2.5, 1, 1, 1)      # TypeError: H must be an integer rubric level
```

## 5. Change a score or add a technology

1. Open `hvdi/evidence.json`. Under `categories`, each technology has five cells (`H`, `T`, `A`, `Q`, `E`):
   `{"v": 3, "basis": "buyer", "conf": "medium", "ev": "what the evidence says", "src": ["S148", "S41"]}`.
2. Edit `v`, and update `basis`, `conf`, `ev` and `src` to match. Every ID in `src` must exist under `sources`;
   add new sources there with the next free ID.
3. **Admission rule:** a score of 3 or more on T, A, Q or E needs a `basis` of buyer, independent tracker or
   filing. Vendor-only evidence stops at 2. The tests enforce this.
4. Run `python3 -m pytest -q`. One test pins the published scores (`test_scores_reproduced_after_16_nov_claims_revision`);
   if you changed a score on purpose, update that test and record the change under `audit_score_changes`.
5. Run `python3 build.py > results.txt` and review the new verdicts.

Gates and stress scenarios are edited the same way under `gates` and `scenarios`.

**H is different.** H is not edited in `evidence.json`; it is computed from `claims.csv` by the rule in `H_RULE.md` (for stage and for narrative claims, the highest level a strict majority reaches; H is the higher of the two; a narrative level needs at least two claims). To change H, add, recode or exclude claims in `claims.csv` (set `include` to `yes` or `no`), then update the H cell in `evidence.json` to match: `build.py` stops with an error if they differ.

## 6. Optional builds

```bash
# Public copy of the page (header and footer reduced to "Confidential Research ©")
cd hvdi && python3 make_public.py            # writes ../site-public/index.html

# Browser smoke test (needs playwright and Chrome at /usr/bin/google-chrome; edit the path in shot.py otherwise)
pip install playwright && python3 shot.py    # expect "ERRORS: [] net-errs: 0"

# Report (Word): needs pandoc, matplotlib, python-docx
cd ../report-src && python3 make_figs.py && python3 make_framework_fig.py ../deck-src && python3 build_report.py && python3 finish_docx.py

# Deck: needs Node.js, pptxgenjs and the apply_theme.js helper (not included in this repository)
cd ../deck-src && npm install pptxgenjs
HVDI_APPLY_THEME=/path/to/apply_theme.js node build.js                      # screen version
HVDI_APPLY_THEME=/path/to/apply_theme.js DECK_THEME=print node build.js     # light print version
```

`report-src/src_rev56.md` is the earlier draft from which the reference list is drawn; keep it beside
`build_report.py`.

## 7. Reading the output

| Field | Meaning |
|---|---|
| V | Proven value: weighted mean of T, A and E (equal weights by default). |
| D | Gap, H − V. +1.0 or more: story ahead of proof. −1.0 or less: proof ahead. Otherwise broadly aligned. |
| Q band | Capital quality: thin (0 to 1), concentrated (2), committed (3 to 4). Reported beside D, never subtracted. |
| Stability | Share of 20,000 random re-scorings that keep the verdict. |
| Outlook | Closing, stalling, holding, at risk or blocked. A transparent rule, not a forecast, and not calibrated. |
| Gates | Power, packaging, memory, lasers, export policy. A blocked gate overrides any score. |

## 8. Limits

One coder scored every cell, at one date; blind AI codings and five blind human coders reproduced all ten
verdicts. Eight of ten verdicts are directional. The outlook rule is uncalibrated. Buyer-side economics
are mostly private. An exploratory back-test on 400G Ethernet and OpenFlow (report, Appendix 11) suggested
that the gap's direction over time separated success from stall, and identified three refinements
(claim volume, independent-only proof, substitute tracking). These form a version 3.2, which is outside
the scope of this submission and will be taken up independently. See `hvdi/EVIDENCE_AUDIT.md` and the report.

## Licence

Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All rights reserved. Proprietary; publicly visible for review.
See `LICENSE`.
