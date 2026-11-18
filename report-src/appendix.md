## Appendices

### Appendix 1. Research matrix

| Research question | Evidence | Method | Managerial output |
| --- | --- | --- | --- |
| Claim versus proof | Vendor and analyst claims; specifications; trackers; operator disclosures | Rubric coding on a shared 0 to 4 scale; gap D | Verdict per technology |
| Missing evidence | Buyer-side reliability, power and cost results | Leg diagnostics | What proof to demand |
| Capital and gates | Filings, bond data, supply and policy sources | Capital-quality score; non-compensatory gates; scenarios | Sequencing and exposure |
| Robustness | Scores and confidence grades | Alternative weights; 20,000-draw Monte Carlo | Stability per verdict |

### Appendix 2. Scoring rubric

| Level | H: claimed (summary; full scales below) | T: technical proof | A: adoption | Q: capital quality | E: buyer economics |
| --- | --- | --- | --- | --- | --- |
| 0 | Little or no claim | None | None | No committed capital | None |
| 1 | A future promise | Specification or simulation | Announced or sampling | Venture or strategic capital only | Vendor claim only |
| 2 | Imminent or early | Vendor or lab demonstration | Pilot or single buyer | Revenue, but concentrated, single-buyer or vendor-financed | One buyer-reported benefit or bounded vendor comparison |
| 3 | In production | Independent or buyer-side proof at scale | Two or more buyers | Revenue from several buyers backed by binding commitments | Buyer benefit against a matched baseline |
| 4 | The default | Multi-generation, operator-documented | Dominant share | As 3, low concentration, multi-year record | Lifecycle economics at several buyers |

**Claimed maturity (H) in full.** H is coded from dated public claims (Appendix 9), each classified as a stage claim (what deployment stage is asserted now) or a narrative claim (how the technology's maturity, momentum or destiny is framed). Architectural or value statements that assert no adoption, momentum or deployment are recorded but not counted.

| Level | Stage claim | Narrative claim |
| --- | --- | --- |
| 0 | No deployment claim (not counted) | Absolute decline, niche restriction, abandonment, or losing share with no offsetting growth |
| 1 | Specification or standardisation work, or a product more than 12 months out | Not ready yet, a premature launch, a long-term possibility or an open question |
| 2 | Launched, available, sampling, initial shipping, or deploying within 12 months | A promising contender or emerging challenger; or growing while losing relative share |
| 3 | Volume production, or in production at customers | Leading, winning majority share, gaining momentum, or set to dominate within about two years |
| 4 | Claimed as the default choice | Explicitly the default or standard now, or the inevitable eventual winner |

For each kind, the level is the highest that a strict majority of claims reach; the narrative level counts only with at least two narrative claims; H is the higher of the stage and narrative levels. This is version 3.1 of the rule, which incorporates six clarifications proposed by a blind second coder.

Curve position is derived from the scores, not taken from Gartner: D of +1 or more with V below 1.5 is "promise outruns proof"; with V of 1.5 or more, "peak claims"; negative D is "proof outruns talk"; otherwise V below 3 is "earning it" and 3 or more is "earned".

### Appendix 3. Source classes and course concepts

| Class | Examples | Used for | Limit |
| --- | --- | --- | --- |
| Filings and institutional data | SEC 10-K, 10-Q and 8-K; Berkeley Lab | Revenue, commitments, concentration | Check period and scope |
| Standards | Ultra Ethernet Consortium, UALink Consortium, OCP | What is specified and when | A specification is not a deployment |
| Peer-reviewed and conference papers | Meta at SIGCOMM 2024; ASPLOS 2025 | Production experience, reliability | Workload-specific |
| Originating analyst releases | Dell'Oro, IDC, Cignal AI, TrendForce | Market estimates and forecasts | Paid tables not read |
| Vendor documents and calls | Broadcom, Arista, Credo, AMD | Specifications, guidance | Interested party |
| Secondary reports | Trade press, conference write-ups | Operator talks not available in primary form | Confidence capped at medium |

| Course (term) | Concept | Use |
| --- | --- | --- |
| TBIT (3) | Business-IT alignment; why IT projects fail | Buyer-economics leg; buyer capability |
| Strategic Management (3) | Value chain; complements | Technology map; gates |
| Managerial Economics (1) | Market structure; information asymmetry | Proprietary versus open fabrics; private buyer economics |
| FRA (1), FM (3) | Segment reporting; commitments; funding mix | Capital-quality score |
| SAMD (1) | Index construction; simulation | Weights, thresholds, Monte Carlo |

### Appendix 4. Scoring rationale

| Technology | Decisive evidence |
| --- | --- |
| Ethernet scale-out | Operator-documented production; about two-thirds of AI-cluster switch sales; $8.6 billion of remaining performance obligations at one vendor; no public matched-baseline economics ([[S10,S29,S139]]) |
| InfiniBand | 800G shipping in volume; sales tripled in Q1 2026; single vendor with concentrated customers ([[S11,S54]]) |
| Ultra Ethernet transport | Specification 1.1; self-attested compliance; one buyer's stated intent; RoCEv2 still the working choice ([[S72,S73,S78,S71]]) |
| NVLink | Dominates scale-up deployments; single vendor; no buyer economics admitted ([[S65,S54]]) |
| UALink (native) | Simulation-based targets; switch silicon in validation; first racks shipped on Ethernet instead; no product revenue disclosed ([[S33,S34,S63,S150]]) |
| Ethernet scale-up | Meta states its switch is shipping; vendor deployment statements; first Helios racks late 2026; binding GPU commitment sits beside supplier equity ([[S124,S68,S63,S140]]) |
| Merchant DPU | Production at cloud providers, mostly self-built; Google reports host cores freed on a co-designed device; an independent study is unfavourable to offload; no separable revenue ([[S67,S136,S112,S116]]) |
| Co-packaged optics | Buyer-run reliability tests; early 2026 deployments; small volumes; one buyer-reported benefit ([[S66,S36,S39]]) |
| Linear pluggable optics | Buyer-reported production data from one operator; limited deployment ([[S137,S39]]) |
| Active electrical cables | Buyer-described fleet deployment with three suppliers; volume revenue; two customers 71% of quarterly revenue ([[S148,S147,S142]]) |

### Appendix 5. Gates

| Gate | Evidence | Status |
| --- | --- | --- |
| Site power and grid | Grid-connection waits above four years in primary US markets; transformer lead times above 160 weeks; Microsoft built less than guided because capacity arrived late ([[S62,S31]]) | Constraining |
| Advanced packaging | CoWoS supply about 20% short of demand in mid-2026; concentrated in Taiwan ([[S60]]) | Constraining |
| High-bandwidth memory | One supplier's HBM4 ramp moved to the third quarter; 2026 shipment outlook cut from 4.5 to 4.0 billion gigabits ([[S43]]) | Constraining |
| Indium phosphide lasers | A leading supplier ships about 30% below demand, with capacity committed through 2027 ([[S61]]) | Constraining, optics only |
| Export policy | Case-by-case licensing for certain AI chips to China since 15 January 2026 ([[S59]]) | Constraining |

### Appendix 6. Hypotheses

| Hypothesis | Result |
| --- | --- |
| H1 Narrative leads deployment for some fabrics | Supported for NVLink and native UALink; not for co-packaged optics, Ultra Ethernet transport or Ethernet scale-up once hype is scored from dated claims |
| H2 Link speed poorly predicts useful benefit | Not tested: no matched goodput data |
| H3 Efficiency depends on boundary | Supported for rated power (12.5 versus 43.3 pJ/bit) |
| H4 Open standards do not instantly remove lock-in | Supported |
| H5 Capex can precede value without proving overinvestment | Not testable at one date |
| H6 Inference changes rather than reduces demand | Not tested |
| H7 Supplier growth can coexist with weak buyer returns | Indeterminate: buyer economics not public |
| H8 External constraints delay realization | Supported |

### Appendix 7. Execution plan

| Window | Work completed |
| --- | --- |
| September 2026 | Topic selection and proposal |
| To 16 October 2026 | Exploratory dossier: claim audit, first sources, index design |
| To 11 November 2026 | Six-parameter model; engine and tests; ten technologies scored; scenarios; interactive page; report and deck |
| 12 November 2026 | Evidence audit: filings and operator documents read at origin; two scores revised; 152 sources logged |
| 12 to 16 November 2026 | Blind second coding; claimed maturity rebuilt from 76 dated claims; rubric version 3.1; quotes checked against live pages; 217 sources logged |

### Appendix 8. Declarations

**Data.** All data are public and secondary. No primary data, employer information or purchased report was used. The full source ledger (S01 to S217), the claims corpus (Appendix 9), the dataset, the code and its tests accompany this report. Interactive page: {{SITE_URL}}. Code repository (private; access on request): {{CODE_URL}}.

**Use of AI assistance.** An AI assistant (Claude, Anthropic) was used to search for and retrieve public sources, extract figures from documents, draft and edit text, and write and test code. The author set the research design, supplied primary documents, reviewed the outputs and is responsible for all judgements and any errors.

**Originality.** This report is the author's own work for the IIMA BPGP Live Project. All sources are cited.

### Appendix 9. Claims corpus for claimed maturity (H)

Each row is one dated public claim used to score H, coded on the scales in Appendix 2. Quotes and notes are in `claims.csv` in the code repository.

{{CLAIMS_TABLE}}
