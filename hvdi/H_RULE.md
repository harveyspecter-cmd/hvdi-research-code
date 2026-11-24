# H coding rule, version 3.1 (16 Nov 2026)

Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved. Proprietary; publicly visible for review.

H measures the story told about a technology's maturity and destiny for hyperscale AI buyers, at the cut-off of 11 November 2026, from dated public claims made between 12 November 2025 and 11 November 2026. Claims are listed in `claims.csv`; the rule is implemented in `hclaims.py`.

## Step 1: classify each claim

- **Stage claim:** asserts what deployment stage the technology has reached now (shipping, sampling, in production, available, specification complete).
- **Narrative claim:** frames the technology's maturity, momentum, market position or destiny beyond a factual status ("eventual winner", "inevitable", "the standard", "dominant", "leading", "fastest-growing", "losing share", "niche", "not ready").
- **Not a claim:** architectural, functional or value statements that assert no adoption, momentum or deployment ("not as an upgrade, but as a rethink"). These are recorded and excluded.

If a claim does both, classify it by its main point.

## Step 2: code each claim 0 to 4

| Level | Stage claim | Narrative claim |
|---|---|---|
| 0 | No deployment claim (excluded) | Absolute decline, niche restriction, abandonment, or losing share with no offsetting growth |
| 1 | Specification or standardisation work, or a product for a future generation more than 12 months out | Not ready yet, a premature launch, a long-term possibility or an open question |
| 2 | Launched, available, sampling, initial shipping, or deploying within 12 months | A promising contender or emerging challenger; or growing in absolute terms while losing relative share |
| 3 | Volume or mass production, or in production operation at customers | Leading, winning majority share, gaining momentum, or set to dominate within about two years |
| 4 | Claimed as the default choice | Explicitly the default or standard now, or the inevitable eventual winner |

A confident forecast of dominance ("will become the standard") is a narrative claim at 3 or 4, even though it concerns the future.

## Admissible claimants
Promoters and consortia, vendors, originating analysts, and named people quoted in the trade press. Trade press in its own editorial voice is admissible for narrative claims only, and is flagged.

## Aggregation
- Stage level: the highest level that a strict majority of stage claims reach.
- Narrative level: the same rule on narrative claims, used only when at least two narrative claims exist.
- H = the higher of the two. Reason: hype is the loudest credible story a buyer hears; a restrained stage claim does not cancel a confident narrative.
- Robustness: claims are resampled with replacement and claims marked as torn take their alternative level half the time (`monte_carlo_claims`).

## Changes from version 3
Version 3.1 applies six clarifications proposed by a blind second coder on 13 November 2026: "not ready" named at narrative 1; shipping separated from volume production; specification work at stage 1; growing-but-losing-share at narrative 1-2; architectural statements excluded; leading (3) separated from default (4).
