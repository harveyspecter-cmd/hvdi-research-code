# Beyond the Hype Cycle: A Techno-Economic Value Chain Framework for AI Networking and Interconnect Hardware, 2025 to 2030

Live Project Report · IIMA BPGP 2025-27 · Area: Information Systems

Nov 11, 2026 · @Sushant Gaurav

## Executive summary

AI networking is a first-order investment decision, yet vendor narrative, revenue and engineering evidence disagree. This report builds the Hype-to-Value Divergence Index (HVDI), which scores ten interconnect technologies on what is claimed, what is technically proven, who has adopted it, how solid the money is and what buyers have gained, and keeps external constraints outside the arithmetic as gates. Using 152 public sources as of 11 November 2026, three technologies show a story ahead of their proof: native UALink (gap +2.00, the only firm verdict), Ultra Ethernet transport (+1.33) and Ethernet scale-up (+1.00, on the threshold). The other seven are broadly aligned and none has proof ahead of talk. No technology scores above 2 on buyer economics, because that evidence sits with buyers. All five external gates constrain today and none is blocked; an indium export halt would block the four optical technologies. The proposed solution is a set of decision rules: deploy the aligned technologies with matched-baseline measurement in the contract, pilot co-packaged optics, hold options on Ethernet scale-up and Ultra Ethernet transport, defer native UALink, and prove the DPU baseline on the buyer's own workload. The index is a decision aid built on one analyst's scores at one date; a back-test is the condition for calling it predictive.

Section map: Introduction and problem statement (1); objective and scope (2, 3); methodology (4); data collection and analysis (5, 6); findings (7); proposed solutions and implementation suggestions (8); execution, challenges and roadblocks (9); references and appendix.

## 1. Introduction

AI networking has become a first-order investment decision, yet the signals used to judge it disagree. Analysts describe technologies by narrative maturity, equity research by vendor revenue, and engineers by power, reach and cost per bit. A planner who reads one signal alone will misallocate capital.

The scale is settled. The four largest hyperscalers guide to roughly $720 to 740 billion of 2026 capital expenditure (forecast; secondary compilation, S32). Switch sales in AI back-end networks passed front-end networks for the first time in the second quarter of 2026 (estimate, S29). Hyperscalers sold more than $370.7 billion of bonds in 2026 to 4 November, about one-fifth of US investment-grade issuance (estimate, S57).

What is unsettled is which parts of the interconnect stack have earned their narrative. Exploratory research showed how easily the signals are mixed. The proposal's $15.4 billion market figure described all Ethernet switching, not data-center switching; NVIDIA's 21.5% share was of data-center Ethernet switch revenue, not AI networking; and a widely quoted grid-queue figure described generation projects, not data-center load (S01, S05).

### 1.1 Problem statement (handout section 3)

The managerial problem is specific. How should an infrastructure planner allocate investment across networking options when vendor narrative, capital, deployable infrastructure and workload value mature at different speeds?

This report answers with the Hype-to-Value Divergence Index (HVDI). It scores ten interconnect technologies on what is claimed, what is technically proven, who has adopted it, how solid the money behind it is, and what buyers have gained, and it keeps external constraints outside the arithmetic as gates. The work is rooted in Information Systems thinking on alignment and value realization (Henderson & Venkatraman, 1993; Soh & Markus, 1995).

## 2. Objective

The aim is to design the HVDI, test it, and apply it to the AI network hardware value chain as it stood on 11 November 2026.

1. For each technology, how far does claimed maturity exceed or trail evidenced maturity?
2. Which evidence is missing: technical, adoption, or buyer economics?
3. How solid is the capital behind each technology, and which external gates can block it regardless of readiness?
4. How stable are the verdicts when scores and weights are perturbed?

The outputs are a classified and stress-tested scorecard, decision rules for infrastructure planners, silicon investors and capacity policymakers, and a public interactive tool. The index is a decision aid. A positive gap does not show that a technology is a poor bet or that any security is mispriced.

## 3. Project scope

The unit of analysis is technology by buyer type by generation by date. This report scores a hyperscale buyer on evidence available on 11 November 2026.

Ten technologies are scored: Ethernet scale-out (800G, RoCEv2), InfiniBand scale-out, Ultra Ethernet transport, NVLink scale-up, native UALink scale-up, Ethernet scale-up (SUE, ESUN, UALink over Ethernet), merchant DPUs, co-packaged optics, linear pluggable optics, and active electrical cables.

High-bandwidth memory and advanced packaging are treated as gates, not scored technologies. GPU ranking and application-layer AI economics are out of scope. The 2025 to 2030 horizon holds observations to late 2026 and scenarios beyond.

| Research question | Evidence | Method | Managerial output |
| --- | --- | --- | --- |
| Claim versus proof | Vendor and analyst claims; specifications; trackers; operator disclosures | Rubric coding on a shared 0 to 4 scale; gap D | Verdict per technology |
| Missing evidence | Buyer-side reliability, power and cost results | Leg diagnostics | What proof to demand |
| Capital and gates | Filings, bond data, supply and policy sources | Capital-quality score; non-compensatory gates; scenarios | Sequencing and exposure |
| Robustness | Scores and confidence grades | Alternative weights; 20,000-draw Monte Carlo | Stability per verdict |

## 4. Methodology

The HVDI measures the distance between claimed and evidenced maturity on one shared scale, scores capital quality beside it, and keeps external constraints out of the arithmetic.

### 4.1 Position against prior work

The Gartner Hype Cycle places a technology on one curve that blends visibility with maturity (Fenn & Raskino, 2008). Reviews find no stated measurement basis and unevenly spaced stages (Steinert & Leifer, 2010; Dedehayir & Steinert, 2016), and hype patterns differ by technology (van Lente et al., 2013). Readiness levels measure engineering maturity but not expectations (Mankins, 2009).

Measuring the gap is not new. Kim et al. (2026) define a Maturity-Expectation Gap from expert surveys for generative AI in public R&D review. Choi and Geum (2025) quantify Hype Cycle technologies on technology, market and expectation dimensions. Cao et al. (2025) build a news-attention hype index for equities.

The HVDI's contribution is therefore specific:

1. **Documented evidence, graded by who holds it.** A score of 3 or more requires proof from a buyer, an independent tracker or a filing. Vendor marketing alone stops at 2.
2. **Capital quality as its own measure.** Money is scored for how committed and how concentrated it is, and is never counted as proof.
3. **Non-compensatory gates.** Following the ecosystem view that an innovation cannot create value until its complements are ready (Adner & Kapoor, 2010; Teece, 1986), a blocked gate overrides any score.
4. **A tested, reproducible instrument.** Scores, rules and sensitivity are in code with automated tests.

Construction follows the OECD and JRC sequence: framework, indicators, weighting, sensitivity (OECD & JRC, 2008). The claims of novelty rest on a limited literature search and should be read as provisional.

### 4.2 Six parameters

| Level | H: claimed | T: technical proof | A: adoption | Q: capital quality | E: buyer economics |
| --- | --- | --- | --- | --- | --- |
| 0 | Little or no claim | None | None | No committed capital | None |
| 1 | A future promise | Specification or simulation | Announced or sampling | Venture or strategic capital only | Vendor claim only |
| 2 | Imminent or early | Vendor or lab demonstration | Pilot or single buyer | Revenue, but concentrated, single-buyer or vendor-financed | One buyer-reported benefit or bounded vendor comparison |
| 3 | In production | Independent or buyer-side proof at scale | Two or more buyers | Several buyers with binding commitments | Buyer benefit against a matched baseline |
| 4 | The default | Multi-generation, operator-documented | Dominant share | As 3, low concentration, multi-year record | Lifecycle economics at several buyers |

The sixth parameter, X, is a set of gates: site power and grid, advanced packaging, high-bandwidth memory, indium phosphide lasers, and export policy. Each is open, constraining or blocked, and applies only to the technologies exposed to it. Lasers, for example, gate optical technologies and not copper ones.

### 4.3 Index, verdict and curve position

```latex
V = w_T T + w_A A + w_E E, \qquad D = H - V
```

Equal weights are the baseline. D of +1.0 or more means the story is ahead; -1.0 or less means the proof is ahead; between, broadly aligned. One rung is the threshold because it is the smallest step a coder can distinguish.

Curve position is derived from the scores, not taken from Gartner: D of +1 or more with V below 1.5 is "promise outruns proof"; with V of 1.5 or more, "peak claims"; negative D is "proof outruns talk"; otherwise V below 3 is "earning it" and 3 or more is "earned".

### 4.4 Outlook rule

The outlook is a transparent rule, not a forecast: +1 for a dated milestone within twelve months that addresses the weakest evidence leg, +1 or -1 for whether the last milestone arrived on time, and +1 or -1 for capital quality of 3 or more, or 1 or less. A blocked gate overrides the sum. The rule has not been calibrated against outcomes.

### 4.5 Robustness and testing

Each verdict is recomputed under three alternative weightings and under a 20,000-draw Monte Carlo test. Weights are drawn from a Dirichlet distribution centred on equal weights, and each score shifts one step up or down with probability 0.15, 0.30 or 0.45 for high, medium or low confidence. Stability is the share of draws that keep the baseline verdict.

The engine has 25 automated tests: exhaustive bounds and monotonicity over every score combination, threshold edges, gate override, hand-calculated energy and break-even values, data integrity, the evidence-admission rule, and Monte Carlo reproducibility. Regression was set aside: ten technologies at one date cannot support causal inference.

### 4.6 Course concepts applied

| Course (term) | Concept | Use |
| --- | --- | --- |
| TBIT (3) | Business-IT alignment; why IT projects fail | Buyer-economics leg; buyer capability |
| Strategic Management (3) | Value chain; complements | Technology map; gates |
| Managerial Economics (1) | Market structure; information asymmetry | Proprietary versus open fabrics; private buyer economics |
| FRA (1), FM (3) | Segment reporting; commitments; funding mix | Capital-quality score |
| SAMD (1) | Index construction; simulation | Weights, thresholds, Monte Carlo |

## 5. Data collection

All data are public and secondary: 152 logged entries (identifiers S01 to S152; S19 is split in two and S64 was never assigned), of which 29 come from the exploratory dossier of 16 October 2026, 42 were added by 11 November 2026 and 81 by the evidence audit of 12 November 2026. Of these, 71 carry scores in the dataset. No primary data, employer information or purchased report was used.

| Class | Examples | Used for | Limit |
| --- | --- | --- | --- |
| Filings and institutional data | SEC 10-Q and 8-K exhibits, Berkeley Lab | Revenue, commitments, concentration | Check period and scope |
| Standards | UEC, UALink, OCP ESUN | What is specified and when | A specification is not a deployment |
| Peer-reviewed and conference papers | Meta at SIGCOMM 2024 and ECOC 2025 | Production experience, reliability | Workload-specific |
| Originating analyst releases | Dell'Oro, IDC, Cignal AI, TrendForce, Crehan | Market estimates and forecasts | Paid tables not read |
| Vendor documents and calls | Broadcom, Arista, Credo, AMD | Specifications, guidance | Interested party |
| Secondary reports | Trade press, conference write-ups | Operator talks not available in primary form | Confidence capped at medium |

A number is used only with a named publisher, date, period, unit and denominator, and is labelled as a reported result, analyst estimate, specification, forecast or gap. Missing evidence is recorded as missing, never as zero.

Three reliability notes apply. Most sources added in November were read as search excerpts or mirrors, not full pages, although the key filings and Meta posts behind the changed scores were re-checked on 12 November; Meta's 800G cable deck and the Credo, AMD, Astera and Arista filings supplied on 12 November were read in full; Meta's linear-optics slides, the Futuriom report and the Ultra Ethernet 1.1 specification were read in full. Operator results from the OCP Global Summit 2026 reached this study mainly through Meta's own posts and second-hand write-ups (S120, S39). Gartner's Hype Cycle positions were not accessed, so the claimed-maturity score uses this study's rubric and says nothing about Gartner's placement.

## 6. Analysis and findings: data analysis

Three technologies are scored as story ahead of proof, seven as broadly aligned, and none as proof ahead. Only one verdict, native UALink, is near-certain under random re-scoring; Ethernet scale-up sits exactly on the threshold.

### 6.1 Scores

| Technology | H | T | A | Q | E | V | D | Verdict | Stability | Outlook |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UALink scale-up (native) | 3 | 1 | 1 | 1 | 1 | 1.00 | +2.00 | Story ahead | 99% | Likely to stall |
| Ultra Ethernet transport | 3 | 2 | 2 | 2 | 1 | 1.67 | +1.33 | Story ahead | 74% | Likely to close |
| Ethernet scale-up | 3 | 3 | 2 | 2 | 1 | 2.00 | +1.00 | Story ahead, on threshold | 51% | Likely to close |
| Merchant DPU | 3 | 3 | 2 | 2 | 2 | 2.33 | +0.67 | Aligned | 67% | Likely to hold |
| Ethernet scale-out | 4 | 4 | 4 | 3 | 2 | 3.33 | +0.67 | Aligned | 81% | Likely to hold |
| Co-packaged optics | 3 | 3 | 2 | 2 | 2 | 2.33 | +0.67 | Aligned | 73% | Likely to hold |
| NVLink scale-up | 3 | 3 | 4 | 2 | 1 | 2.67 | +0.33 | Aligned | 78% | Likely to hold |
| InfiniBand scale-out | 2 | 3 | 3 | 2 | 1 | 2.33 | -0.33 | Aligned | 81% | Likely to hold |
| Linear pluggable optics | 2 | 3 | 3 | 2 | 2 | 2.67 | -0.67 | Aligned | 70% | Likely to hold |
| Active electrical cables | 2 | 3 | 3 | 2 | 2 | 2.67 | -0.67 | Aligned | 64% | Likely to hold |

Stability is the share of 20,000 Monte Carlo draws that keep the verdict. Evidence for every score is in Appendix A.

### 6.2 Robustness

Under the three alternative weightings, eight verdicts do not change. Ethernet scale-out becomes story ahead when buyer economics carries half the weight (D = +1.00), and Ethernet scale-up becomes aligned when technical proof does (D = +0.75). The 90% interval for UALink's gap is +1.00 to +3.00, entirely on the story-ahead side. For every other technology the interval crosses a threshold. The honest reading is one firm verdict and nine that are directional, with stability from 51% to 81%; Ethernet scale-up, at exactly +1.00, is close to a coin toss.

**Evidence audit.** On 12 November 2026 the 18 evidence cells with low confidence, a vendor-only basis or no source were re-researched against filings, standards bodies, operator publications and tracker releases, and the claims behind them were re-checked at or near origin. Two scores moved, both up on new evidence: Ethernet scale-up technical proof from 2 to 3, because Meta states that its Tahan Ethernet scale-up switch is shipping (S124), and merchant-DPU buyer economics from 1 to 2, because Google reports host cores freed against on-host baselines on a co-designed device (S136). Most other cells changed basis, confidence or wording. Ethernet scale-up capital quality stays at 2: AMD's 8-K of 24 February 2026, read at origin, states that Meta made a binding commitment to buy the initial 1 GW of Instinct GPU products, with a warrant for up to 160 million shares that vests in tranches from the first GW shipped (S140). The 6 GW total is not stated as binding, no warrant shares had vested at 26 September 2026 (S141), and the commitment is for GPUs, not the scale-up fabric. Four results are confirmed absences: no independent Ultra Ethernet measurement (S73, S75), no native UALink switch in a shipped rack (S98), no separable DPU revenue (S116), and no buyer-reported economics for any scale-up fabric. Meta reports parity, not benefit, between its RoCE and InfiniBand clusters (S87), and the one independent merchant-DPU baseline is unfavourable to offload (S112). Remaining weak cells reflect a thin public record. Meta's linear-optics slides were read in full (S137); its 800G cable deck was read in full (S148): it reports firmware and link-training failures found only at cluster level and gives qualitative cost and power comparisons but no unit counts, so cable economics stay at score 2.

### 6.3 Capital quality

Only Ethernet scale-out reaches level 3. Arista's 10-Q at 30 September 2026 shows remaining performance obligations of about $8.6 billion and deferred revenue of $6.84 billion, both owed by buyers, against $3.66 billion of quarterly revenue, and the company names more than 100 customers for its AI switches (S139, S30). Its $11.4 billion of non-cancellable purchase commitments are owed to its own suppliers, so they show vendor confidence, not buyer commitment. Broadcom's AI networking was about 27% of its $16.7 billion AI semiconductor revenue in the quarter to 2 August 2026, computed as the remainder after the 73% custom-accelerator share stated on the call (estimate, S68).

Elsewhere, real revenue rests on few payers. Credo's 10-Q for the quarter to 1 August 2026 shows two customers at 43% and 28% of revenue, 71% together, down from 49% and 32% (81%) in the year to 2 May 2026 (S147, S142). NVIDIA's 10-Q shows its three largest direct customers at 44% of first-half fiscal 2027 revenue (S143), and it held $42 billion of unlisted equity stakes, some in its own customers, at the end of April 2026 (S54, S58). Native UALink has attracted venture and acquisition capital but no recognized product revenue was found.

Buyers are leaning on external funding. Third-quarter capex was 182% of operating cash flow at Amazon, 122% at Alphabet and 103% at Meta (secondary compilation, S32).

### 6.4 Gates and scenarios

| Gate | Evidence | Status |
| --- | --- | --- |
| Site power and grid | Grid-connection waits above four years in primary US markets; transformer lead times above 160 weeks; Microsoft built less than guided because capacity arrived late (S62, S31) | Constraining |
| Advanced packaging | CoWoS supply about 20% short of demand in mid-2026, narrowing toward 10% by year end; concentrated in Taiwan (S60) | Constraining |
| High-bandwidth memory | One supplier's HBM4 ramp moved to the third quarter; 2026 shipment outlook cut from 4.5 to 4.0 billion gigabits (S43) | Constraining |
| Indium phosphide lasers | A leading supplier ships about 30% below demand, with capacity committed through 2027 (S61) | Constraining, optics only |
| Export policy | Case-by-case licensing for certain AI chips to China since 15 January 2026, with a 25% tariff proclamation (S59) | Constraining |

No gate is blocked today. Four exposure scenarios were run. A halt in indium exports blocks the four optical technologies and leaves the six copper or protocol technologies untouched. A Taiwan packaging disruption, tighter export rules or worse grid delays block all ten. These are exposure tests and predict nothing.

### 6.5 Energy per bit

Rated switch energy per bit fell about 4.7 times across four generations of Tomahawk-based systems, from 58.4 to 12.5 picojoules per bit at typical load without optics (S46 to S49). Retimed optical modules improved about 2 times, from roughly 40 at 100G to 18.8 to 20.0 at 800G (S50, S52). A linear 800G module is rated at 10.6 (S51).

The boundary changes the answer more than the generation does. The same Tomahawk 5 switch reads 12.5 pJ/bit with copper cables at typical load and 43.3 at maximum load with optics (S49). Sixty-four retimed modules at 16 W account for 1,024 W of the 1,578 W difference. All values are vendor-rated, not measured in operation.

### 6.6 Two bounded economic models

**Value of a linear-optics saving.** A linear module is rated 7.5 W below a retimed one. At $0.08 per kWh, a facility overhead of 1.2 and a four-year life, the energy saved is 78.8 kWh a year, worth $25.23 per module over its life. If freed site capacity is valued at $8 per watt, that adds $72.00. The inputs are illustrative scenarios, not sourced prices; the conclusion is structural. On electricity alone the saving is small, so the case for linear optics rests on freed capacity and reliability.

**Network leverage.** If the network is 15% of cluster cost, a network priced 20% higher raises total cost by 3.0%. It pays for itself if useful output rises by 3.0%. Published estimates put networking at roughly 10% to 25% of cluster cost; these are secondary and vary by design. Small utilization gains justify large premiums, which is why the missing buyer-economics evidence matters so much.

## 7. Analysis and findings: results

### 7.1 The open scale-up story is ahead of its proof, and the first product shipped without it

Native UALink has the largest and firmest gap (D = +2.00, 99% stable). A 2.0 specification was published in April 2026 before any 1.0 silicon shipped; the consortium chair expected chips in labs in the second half of 2026 and products in 2027 (S33). Performance targets rest on modelling and simulation (S34). AMD's first Helios racks, shipping from late in the third quarter of 2026, run their scale-up domain over UALink-over-Ethernet on Broadcom silicon because native UALink switch chips are still in validation (S63).

That one fact explains two outlooks. UALink is likely to stall: its last milestone slipped and its capital is venture money. Ethernet scale-up is likely to close its gap (D = +1.00, on the threshold): racks are shipping, Meta states that its Tahan Ethernet scale-up switch is shipping (S124), and Broadcom said on 2 September that Tomahawk Ultra began deployment in its current quarter, August to October 2026 (S68). NVLink, the incumbent, is aligned (D = +0.33) and still dominates scale-up deployments (S65). A buyer choosing 2026 racks could not buy the native open alternative.

### 7.2 A compliance label is not a deployed transport

Ultra Ethernet transport scores D = +1.33. The specification was released in June 2025 and reached version 1.1 on 12 October 2026, and compliant NICs are announced, and one buyer, Oracle, has stated an intent to deploy them (S44, S78); compliance is self-attested under Section 8 of the specification itself, with no published test-lab result (S72, S73). A vendor-sponsored analyst report (sponsors DriveNets, Arrcus and Nokia) still described it in April 2026 as an emerging standard, with RoCEv2 the working choice in hyperscale fabrics (S71). Its outlook is positive because compliant NICs ship inside the Helios racks.

### 7.3 Buyer economics is the weakest proof everywhere

No technology scores above 2 on buyer economics, including Ethernet scale-out, which scores 4 on technical proof and adoption. Public sources show that buyers deploy and expand; they do not show matched-baseline cost, energy or downtime. The evidence exists but sits with buyers, an information asymmetry in the Managerial Economics sense. The leverage model in Section 6.6 shows why this matters: a 3% output gain can justify a 20% network premium, and nobody outside the buyer can verify the 3%.

### 7.4 Real revenue, few payers

Nine of ten technologies score 2 or less on capital quality. Active electrical cables illustrate the pattern: production-scale revenue, yet two customers supplied 71% of it in the quarter to 1 August 2026 (S147) and 81% in fiscal 2026 (S142). InfiniBand and NVLink inherit NVIDIA's concentration and its financial ties to customers. Concentration is not hype, but it means a single buyer's pause would change the picture faster than any technical event.

### 7.5 Quieter technologies are not over-told

InfiniBand, linear pluggable optics and active electrical cables all have a negative gap. InfiniBand sales more than tripled in the first quarter of 2026 against a narrative of decline (S11). Meta reports, from about 4,000 linear modules on one fabric hop over four months, roughly 2 times fewer link interruptions and 2.6 times fewer service-affecting failures than retimed optics at the same link mode, at 100G per lane (S137). It is one operator's limited deployment, not independent replication. These verdicts are directional (64% to 81% stable).

### 7.6 Co-packaged optics is closer to aligned than its reputation

CPO scores D = +0.67. Meta's evaluation, presented at ECOC 2025, logged one million flap-free port-hours; a follow-up reported 15 switches run for nine months, 36 million device-hours, and about 65% lower optics power (S66). Initial deployments arrived in 2026 as analysts forecast in 2025 (S37, S36). Two cautions: the evidence is from the 51.2 Tb/s generation, and adoption remains the weak leg.

### 7.7 Constraints are real but not yet blocking

All five gates are constraining and none is blocked. Interconnect readiness is not what limits value realization in late 2026; delivered capacity, packaging, memory and lasers are. The indium scenario shows a structural asymmetry: copper-based technologies are insulated from the optical supply chain's single largest material risk.

### 7.8 Hypotheses

| Hypothesis | Result |
| --- | --- |
| H1 Narrative leads deployment for some fabrics | Supported for UALink, Ultra Ethernet transport, Ethernet scale-up; not for CPO |
| H2 Link speed poorly predicts useful benefit | Not tested: no matched goodput data |
| H3 Efficiency depends on boundary | Supported for rated power (12.5 versus 43.3 pJ/bit) |
| H4 Open standards do not instantly remove lock-in | Supported |
| H5 Capex can precede value without proving overinvestment | Not testable at one date |
| H6 Inference changes rather than reduces demand | Not tested |
| H7 Supplier growth can coexist with weak buyer returns | Indeterminate: buyer economics not public |
| H8 External constraints delay realization | Supported |

## 8. Proposed solutions and implementation suggestions (handout sections 6 and 7)

### 8.1 Proposed solution: decision rules for infrastructure planners

| Posture | Condition | Technologies today | Require before moving up |
| --- | --- | --- | --- |
| Deploy | Aligned; T and A at 3 or more | Ethernet scale-out, NVLink, InfiniBand, LPO, AEC | Supply assurance; matched-baseline economics in the contract |
| Pilot at scale | Aligned; A at 2 | Co-packaged optics | Reliability data for the generation being bought; pluggable fallback |
| Hold an option | Story ahead; outlook closing | Ethernet scale-up, Ultra Ethernet transport | Hardware that can carry the standard; no commissioning date tied to it |
| Defer | Story ahead; outlook stalling | Native UALink | Switch silicon sampled, then multi-vendor interoperability |
| Prove the baseline | Aligned; E at 2, shown only on co-designed hardware | Merchant DPU | A host-only comparison on the buyer's workload |

Three practices follow. Buy the missing proof: write matched-baseline measurement into contracts, since economics is the weakest leg everywhere. Schedule by gate, not by product: plan around time to energized capacity and component allocation. Re-score on triggers: each technology has an observable event that moves a score, such as native UALink silicon sampling or a second named CPO buyer at 102.4 Tb/s.

### 8.2 Silicon investors

Revenue is earned mainly in the aligned technologies. Story-ahead technologies behave like options tied to dated milestones, so slippage is the signal to watch. Capital quality deserves equal attention: customer concentration, vendor financing and deferred revenue can move reported results without any change in the technology. The index says nothing about valuation and is not investment advice.

### 8.3 Capacity policymakers

The constraint in late 2026 is delivered capacity. Interconnection-queue totals describe generation projects, not data-center demand (S05). The scenario results identify where exposure is concentrated: advanced packaging in one geography and a laser material under export control.

### 8.4 Implementation artifact

The deliverable is a working instrument: the dataset, the tested engine and a public interactive page on which a reader selects a technology, an evidence weighting and a stress scenario. A planning team can refresh the scores each quarter. Two analysts should score independently before results are used for a decision.

## 9. Execution, challenges and limitations

| Window | Work completed |
| --- | --- |
| September 2026 | Topic selection and proposal |
| To 16 October 2026 | Exploratory dossier: claim audit, 28 sources, index design |
| To 11 November 2026 | 42 further sources; six-parameter model; engine and tests; ten technologies scored; scenarios; interactive page; report and deck |

**Challenges.** Paid analyst tables were not accessible, so public releases were used for direction and no market share was computed. Gartner's positions were unavailable, so the study uses its own rubric. No transaction prices are public, so cost per gigabit could not be computed; two bounded models replace it. The planned regression was dropped because ten technologies at one date cannot support it.

**Limitations.**

1. Project analysis assigned every score, with no second coder. Monte Carlo stability shows sensitivity to coding error; it does not replace a second coder.
2. One date. The index cannot yet show whether a gap is closing.
3. Any pre-production technology shows a positive gap. That marks timing risk, not a flawed technology.
4. Nine of ten verdicts are directional only, and Ethernet scale-up sits on the threshold.
5. The outlook rule is uncalibrated and the scenarios test exposure, not likelihood.
6. Narrative coding is judgement; no frozen corpus of claims was assembled.
7. Capital quality is observed at company level and attached to technologies by judgement.
8. Most November sources were read as excerpts. The novelty claims rest on a limited literature search.

**Next steps.** A second coder with a reported agreement statistic; a frozen claims corpus; a quarterly panel; and a back-test on earlier networking bets such as 400G, software-defined networking and SmartNICs, which would show whether a large gap predicted later slippage. That back-test is the condition for calling the index predictive.

## 10. References

Bracketed IDs match the project's evidence ledger. The appendix and references are outside the word count.

### Academic and methodological

- Adner, R., & Kapoor, R. (2010). Value creation in innovation ecosystems. *Strategic Management Journal, 31*(3), 306-333.
- Cao, Z., Wunkaew, W., & Geman, H. (2025). *The Hype Index: An NLP-driven measure of market news attention* (arXiv:2506.06329).
- Choi, W., & Geum, Y. (2025). Quantifying the hype cycle: Data-driven mapping for identifying emerging technologies. *Proceedings of IEEE IEEM 2025*, 484-488.
- Dedehayir, O., & Steinert, M. (2016). The hype cycle model: A review and future directions. *Technological Forecasting and Social Change, 108*, 28-41.
- Fenn, J., & Raskino, M. (2008). *Mastering the hype cycle*. Harvard Business Press.
- Gangidi, A., et al. (2024). RDMA over Ethernet for distributed AI training at Meta scale. *Proceedings of ACM SIGCOMM 2024*. \[S10\]
- Henderson, J. C., & Venkatraman, N. (1993). Strategic alignment. *IBM Systems Journal, 32*(1), 4-16.
- Kim, D., Kang, S., & Hong, A. (2026). Bridging the maturity-expectation gap. *Technovation, 149*, 103374.
- Mankins, J. C. (2009). Technology readiness assessments: A retrospective. *Acta Astronautica, 65*(9-10), 1216-1223.
- OECD & European Commission Joint Research Centre. (2008). *Handbook on constructing composite indicators*. OECD Publishing. \[S21\]
- Soh, C., & Markus, M. L. (1995). How IT creates business value: A process theory synthesis. *Proceedings of ICIS 1995*, 29-41.
- Steinert, M., & Leifer, L. (2010). Scrutinizing Gartner's hype cycle approach. *Proceedings of PICMET 2010*.
- Teece, D. J. (1986). Profiting from technological innovation. *Research Policy, 15*(6), 285-305.
- van Lente, H., Spitters, C., & Peine, A. (2013). Comparing technological hype cycles. *Technological Forecasting and Social Change, 80*(8), 1615-1628.

### Market, company, standards and policy sources

- Arista Networks. (2026, November). Q3 2026 results and Form 10-Q. [8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000252/ex991q326-earningsrelease.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000254/anet-20260930.htm) \[S30, S55\]
- Arista Networks. 7060X, 7060X4, 7060X5 and 7060X6 data sheets and guides. [7060X6](https://www.arista.com/assets/data/pdf/Datasheets/7060X6-Datasheet.pdf) \[S46 to S49\]
- Broadcom. (2025, October 1). Meta test results confirm one million flap-free CPO port hours. [Release](https://investors.broadcom.com/node/63616/pdf) \[S66\]
- Broadcom. (2026, September 2). Q3 FY2026 earnings call. [Summary](https://www.marketbeat.com/instant-alerts/transcript-broadcom-q3-earnings-call-highlights-2026-09-02/) \[S68\]
- Cignal AI. (2025, February 27). Co-packaged optics: Inevitable but not imminent. [Release](https://cignal.ai/2025/02/co-packaged-optics-inevitable-but-not-imminent/) \[S37\]
- Credo. (2026). Results for quarters to May and August 2026. [Coverage](https://www.nasdaq.com/articles/credo-technology-stock-outlook-hinges-ai-and-optical-scale) \[S41, S56\]
- Dell'Oro Group. (2026). AI back-end network releases of 4 February, 2 June and 3 September, and OCP 2026 blog. [Q2 release](https://www.delloro.com/news/ai-back-end-networks-switch-sales-surpass-front-end-networks-for-the-first-time-in-2q2026/) \[S11, S29, S36, S65\]
- EC&M citing JLL; Reuters. (2026). Grid-connection waits and transformer lead times. [Article](https://www.ecmag.com/magazine/articles/article-detail/how-long-does-it-take-to-power-a-data-center) \[S62\]
- FS; Jabil. 800G linear and retimed module power. [Jabil data sheet](https://www.jabil.com/dam/jcr:9134ce1b-c889-4d8e-9d7e-fdaa513e5c5e/Jabil_800G%20OSFP%20DR8_DR8+%20OpticalTransceiver_10.pdf) \[S50, S51\]
- Jander, M. (2026, April 22). Top trends in networking for AI: Connectivity from AI clusters to the edge. Futuriom (sponsored by DriveNets, Arrcus and Nokia). [Article](https://www.futuriom.com/articles/news/top-trends-in-networking-for-ai-connectivity-from-ai-clusters-to-the-edge/2026/04) \[S71\]
- IDC. (2026). Ethernet switch market, Q1 and Q2 2026. [Q2 article](https://www.idc.com/resource-center/blog/ethernet-switch-market-surges-43-4-to-18-9b-in-2q26-as-ai-infrastructure-demand-drives-record-datacenter-spending) \[S01, S02\]
- Morgan Lewis. (2026, January 16). BIS revises export review policy for advanced AI chips. [Note](https://www.morganlewis.com/pubs/2026/01/bis-revises-export-review-policy-for-advanced-ai-chips-destined-for-china-and-macau) \[S59\]
- NVIDIA. (2026). Form 10-Q for the quarter ended 26 July 2026. [Filing](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm) \[S54\]
- Rand, J., et al. (2026). *Queued up: 2026 edition*. Lawrence Berkeley National Laboratory. \[S05\]
- Redmond Magazine. (2026, October 30). Microsoft revenue jumps 19%. [Article](https://redmondmag.com/articles/2026/10/30/microsoft-revenue-jumps-as-azure-and-ai-demand--fuel-growth.aspx) \[S31\]
- Simple Tech Trend. (2026, October). OCP Global Summit 2026 session write-ups. [Series](https://www.simpletechtrend.com/en/post/ocp-global-summit-2026-npo-buyers-cpo-timeline-en) \[S39\]
- TBR; Fierce Network. (2026). AMD Helios and UALink over Ethernet. [Report](https://tbri.com/special-reports/amd-enters-the-execution-phase-of-its-full-stack-ai-strategy/) \[S63\]
- Tech Insider citing Reuters and LSEG. (2026, November). Hyperscaler bond issuance. [Article](https://tech-insider.org/big-tech-us-corporate-bond-record-1-88-trillion-2026/) \[S57\]
- The Register. (2026, April 7). UALink 2.0 specification before 1.0 silicon. [Article](https://www.theregister.com/2026/04/07/ualink_2_specs/) \[S33\]
- Tom's Hardware. (2025, 2026). AMD Pollara 400; indium phosphide shortage. [Article](https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory) \[S44, S61\]
- TrendForce. (2026). HBM4 ramp, 23 June; CoWoS supply gap, 15 June. [Article](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-rep) \[S43, S60\]
- UALink Consortium. (2026, January). White paper. [PDF](https://ualinkconsortium.org/wp-content/uploads/2026/01/UALink_White_Paper_Publication_FINAL_UPDATED.pdf) \[S34\]
- Ultra Ethernet Consortium. (2025, June 11). Specification 1.0 release. [Release](https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/) \[S07\]
- Capex and financing compilations (secondary). [Tracker](https://walnutinvest.com/stats/ai-capex-statistics); [Axios](https://axios.com/2026/07/27/nvidia-openai-financing-ai-jensen-huang-ssi) \[S32, S58\]

**Sources added by the evidence audit (12 November 2026).** The full ledger, S72 to S152, with source class and read status, is in the code package (EVIDENCE\_AUDIT.md).

- Advanced Micro Devices. (2026, February 24). Form 8-K (Meta agreement and warrant). Read through a third-party mirror. [Mirror](https://www.boardroomalpha.com/sec/amd-8-k-2026-02-24-0000002488-26-000045) \[S104\]

  Advanced Micro Devices. (2026, February 24). Form 8-K (Meta agreement and warrant). [Filing](https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000045/amd-20260223.htm) \[S140\]

  Advanced Micro Devices. (2026, November 4). Form 10-Q for the quarter ended September 26, 2026. [Filing](https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000191/amd-20260926.htm) \[S141\]

  Arista Networks, Inc. (2026). Form 10-Q for the quarter ended September 30, 2026. [Filing](https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000254/anet-20260930.htm) \[S139\]
- Chen, X., et al. (2024). Demystifying datapath accelerator enhanced off-path SmartNIC. arXiv:2402.03041. [Preprint](https://arxiv.org/html/2402.03041v4) \[S112\]
- Humphries, J. T., et al. (2025). Wave: Offloading resource management to SmartNIC cores. *Proceedings of ASPLOS '25*. [Paper](https://arxiv.org/abs/2408.17351v4) \[S136\]
- Hoefler, T., et al. (2025). *Ultra Ethernet's design principles and architectural innovations* (arXiv:2508.08906v1). [Preprint](https://arxiv.org/abs/2508.08906v1) \[S138\]

  Credo Technology Group Holding Ltd. (2026). Form 10-K for the fiscal year ended May 2, 2026. [Filing](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf) \[S142\]

  NVIDIA Corporation. (2026). Form 10-Q for the quarter ended July 26, 2026. [Filing copy](https://www.opencapital.sh/filings/0001045810-26-000075.md) \[S143\]

  Broadcom Inc. (2026). Form 10-Q for the quarter ended August 2, 2026. [Filing](https://investors.broadcom.com/static-files/96641754-401f-4090-a4ab-210728c83a28) \[S144\]

  Yekani, A., & Wang, Q. (2026, October). *Operating linear pluggable optics at hyperscale: From link management to production reliability* \[Conference session\]. OCP Global Summit 2026. [Index](https://www.opencompute.org/?p=245678) \[S137\]
- Credo Technology Group Holding Ltd. (2026). Form 10-Q for the quarter ended August 1, 2026. [Investor relations](https://investors.credosemi.com) \[S147\]
- Yu, J., & Chakravarty, A. (n.d.). Large-scale deployment of 800Gb/s active electrical cables (AEC) in Meta data centers for AI applications \[Conference slides\]. Open Compute Project, AI Open Data Center. [Index](https://www.opencompute.org/?p=245678) \[S148\]
- Advanced Micro Devices, Inc. (2025). Form 8-K, event date October 5, 2025 (OpenAI warrant). [Filing](https://www.sec.gov/Archives/edgar/data/2488/000119312525230895/) \[S149\]
- Astera Labs, Inc. (2026). Form 8-K, Exhibit 99.1: Third quarter 2026 financial results. [Filing](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm) \[S150\]
- Ultra Ethernet Consortium. (2025). Transport matrix and checklist, revision 1.0; PHY and link-layer matrix and checklist, revision 1.0 \[Workbooks\]. [Site](https://ultraethernet.org/) \[S151\]
- Ultra Ethernet Consortium. (2025). Test bed recommendations, revision 1.0 \[Member document, paraphrased only\]. [Site](https://ultraethernet.org/) \[S152\]
- Meta. (2024, March 12). Building Meta's GenAI infrastructure. [Post](https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/) \[S87\]
- Meta. (2026, October 12). OCP Summit 2026: Powering AI with open innovations in scale-up, scale-out and scale-across networks. [Post](https://engineering.fb.com/2026/10/12/open-source/ocp-summit-2026-powering-ai-with-open-innovations-in-scale-up-scale-out-and-scale-across-networks/) \[S124\]
- Meta. (2026, October 26). OCP Summit 2026: Meta networking talks. [Post](https://engineering.fb.com/2026/10/26/open-source/ocp-summit-2026-meta-networking-talks/) \[S120\]
- Network World. (2026, October 14). Ultra Ethernet 1.1 extends the specification to scale-up networks. [Article](https://www.networkworld.com/article/4235340/ultra-ethernet-1-1-extends-the-specification-to-scale-up-networks-and-adds-programmable-congestion-control.html) \[S75\]
- NVIDIA. (2026, February 25). Form 8-K, fourth quarter and fiscal 2026 results. [Filing copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001045810/5f86707e-03f3-4e5e-b9bd-048e42123723.pdf) \[S116\]
- Oracle. (2025, June 12). Oracle and AMD collaborate to help customers deliver breakthrough performance for large-scale AI and agentic workloads. [Release](https://www.oracle.com/sa-ar/news/announcement/oracle-and-amd-collaborate-to-help-customers-deliver-breakthrough-performance-for-large-scale-ai-and-agentic-workloads-2025-06-12/) \[S78\]
- Reuters. (2026, November 4). AMD's OpenAI, Meta chip deals trigger $1 billion quarterly charge. [Syndicated copy](https://business-standard.com/world-news/amd-s-openai-meta-chip-deals-trigger-1-billion-quarterly-charge-126110400389_1.html) \[S105\]
- ServeTheHome. (2026, August 3). AMD Helios architecture deep dive. [Article](https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/4/) \[S98\]
- Ultra Ethernet Consortium. (2026). Compliance. [Page](https://ultraethernet.org/compliance/) \[S73\]

## Appendix A. Scoring rationale

| Technology | Decisive evidence |
| --- | --- |
| Ethernet scale-out | Operator-documented production; two-thirds of AI-cluster switch sales; $8.6B remaining performance obligations at one vendor; no public matched-baseline economics (S10, S11, S29, S139) |
| InfiniBand | 800G shipping in volume; sales tripled in Q1 2026; single vendor with concentrated customers (S11, S54) |
| Ultra Ethernet transport | Specification June 2025; self-attested NICs; one buyer's stated intent (S78); RoCEv2 still the working choice (S07, S44, S71) |
| NVLink | Dominates scale-up deployments; single vendor; no buyer economics admitted (S65, S54) |
| UALink (native) | Simulation-based targets; switch silicon in validation; first racks shipped on Ethernet instead; venture capital only (S33, S34, S63) |
| Ethernet scale-up | Meta states its Tahan Ethernet scale-up switch is shipping; vendor deployment statements; ESUN requirements; first Helios racks late 2026 (S124, S19b, S63, S68) |
| Merchant DPU | Production at cloud providers; two buyers dominate; mostly self-built; Google reports host cores freed on a co-designed device while an independent lab study is unfavourable to offload (S42, S67, S136, S112) |
| Co-packaged optics | Buyer-run reliability tests; early 2026 deployments; small volumes; one buyer-reported benefit (S66, S36, S38, S39) |
| Linear pluggable optics | Buyer-reported production data; a second deployment still to verify (S39) |
| Active electrical cables | Volume revenue; buyer-described fleet deployment (Meta, 800G, three qualified suppliers); two largest customers are 71% of revenue in the quarter to 1 August 2026 and 81% in fiscal 2026 (S148, S147, S142, S41) |

Full score-by-score evidence, confidence grades and source links are in the project dataset and on the interactive page.
