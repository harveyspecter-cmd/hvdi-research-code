# Beyond the Hype Cycle: HVDI v3.1

Static, selection-only site plus the tested model behind it. Evidence cut-off 11 Nov 2026. Scores are provisional (single coder; blind AI and human second codings reproduced all ten verdicts).

## View it
- Locally: double-click `site/index.html`. No server needed. (The Switzer font loads from Fontshare when online; offline it falls back to the system font.)
- GitHub Pages: create a repository, upload `site/index.html` to the repository root as `index.html`, then Settings > Pages > Deploy from a branch > `main` / root. The page appears at `https://<user>.github.io/<repo>/`.

## Files
- `evidence.json`: the dataset (scores, evidence text, gates, scenarios, sources). Edit this file, not code.
- `data.py`: loads and validates `evidence.json`.
- `make_public.py`: writes the public copy of the page (`../site-public/index.html`) with identifying text removed.
- `hvdi.py`: engine (value, gap, classification, curve position, gates, outlook rule, Monte Carlo, break-even).
- `claims.csv`: 76 dated public claims behind H; `H_RULE.md`: the rule (v3.1); `hclaims.py`: H from claims and the claim-resampling Monte Carlo.
- `test_hvdi.py`, `test_hclaims.py`: 64 tests (arithmetic, gates, economics, data integrity, admission rule, robustness, input validation and edge cases). Run `python3 -m pytest -q`.
- `build.py`: computes everything and writes `site/index.html` from `template.html`. Run `python3 build.py` after any change.
- `results.txt`: last computed table.

## Model in one screen
- Scores 0-4: H claimed, T technical, A adoption, Q capital quality, E buyer economics.
- V = weighted mean(T, A, E); gap D = H - V; D >= +1 story ahead, D <= -1 proof ahead.
- Q is scored but not in D. Gates X (open / constraining / blocked) sit outside the arithmetic; a blocked gate overrides the outlook.
- Outlook rule (uncalibrated): milestone (+1 if dated and aimed at the weakest leg) + punctuality (+1/-1) + capital (Q>=3: +1, Q<=1: -1); blocked gate => blocked.
- H from claims: stage and narrative claims coded 0-4; per kind, the highest level a strict majority reaches; H = max(stage, narrative); narrative counts only with 2+ claims.
- Robustness: 20,000 draws, claims resampled with replacement (torn claims take their alternative level half the time), weights ~ Dirichlet(4,4,4), each score shifted +-1 with probability 0.15 / 0.30 / 0.45 for high / medium / low confidence.

## Evidence audit, 12 Nov 2026
The 18 weakest evidence cells were re-researched. Two scores changed (Ethernet scale-up T 2 to 3, DPU E 1 to 2; see `audit_score_changes` in `evidence.json`); the rest changed basis, confidence, wording or sources (the `_P` block at the end of `data.py`). 92 sources are in the dataset (S147 to S152 added on 12 Nov from the final nine uploads; no score changed), each with its class and how it was read. `EVIDENCE_AUDIT.md` is the full cell-by-cell record with falsifiers and the list of documents still to read at origin.

## Running

Python 3.9 or later. The engine uses the standard library only. `pip install -r requirements.txt`, then `python3 -m pytest -q` and `python3 build.py > results.txt` (writes `site/index.html` and `site/data.json`). The page has no external dependencies and opens from a file or any static host.

## Links

- Interactive page (public): https://harveyspecter-cmd.github.io/hvdi-research/
- Code repository: https://github.com/harveyspecter-cmd/hvdi-research-code

## Licence

Proprietary; publicly visible for review. Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All rights reserved. See `LICENSE`.
