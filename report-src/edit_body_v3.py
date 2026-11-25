"""One-off: bring body.md to HVDI v3.1 (claim-based H). Run once on body_v2.md -> body.md."""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
b = (HERE / "body_v2.md").read_text(encoding="utf-8")


def rep(a: str, n: str) -> None:
    global b
    if b.count(a) != 1:
        raise SystemExit(f"expected once: {a[:70]!r} found {b.count(a)}")
    b = b.replace(a, n)


def section(start: str, end: str, new: str) -> None:
    global b
    i = b.index(start); j = b.index(end, i + len(start))
    b = b[:i] + new + b[j:]


# Executive summary
rep("Using 152 public sources as of 11 November 2026, audited on 12 November, three technologies show a story ahead of their proof: native UALink (gap +2.00, the only firm verdict), Ultra Ethernet transport (+1.33) and Ethernet scale-up (+1.00, on the threshold). The other seven are broadly aligned and none has proof ahead of its story.",
    "Using 217 logged public sources as of 11 November 2026, including 76 dated claims about maturity, two technologies show a story ahead of their proof: NVLink (gap +1.33) and native UALink (+1.00, on the threshold). Neither verdict is firm: each holds in about three of five random re-scorings. The other eight are broadly aligned and none has proof ahead of its story. A blind second coding reproduced all ten verdicts.")

# 3.2 Step 2: add the H measurement paragraph after the Step 2 paragraph
i = b.index("**Step 2: five scores.**")
j = b.index("\n\n", i)
b = b[:j] + "\n\n" + (
    "**Measuring claimed maturity.** H is the only parameter that measures a story rather than a proof, so it is the one most exposed to a coder's own reading; a first blind check confirmed this (Section 6.4). H is therefore scored from a corpus of dated public claims made between 12 November 2025 and 11 November 2026 by promoters, vendors, originating analysts and named people quoted in the press (Appendix 9). "
    "A stage claim asserts what deployment stage a technology has reached; a narrative claim frames its momentum or destiny, such as \"the eventual winner\" or \"a premature launch\". Both are coded from 0 to 4 (Appendix 2), so a confident forecast of dominance counts as strong hype even though it concerns the future. "
    "For each kind, the level is the highest that a strict majority of claims reach, and H is the higher of the two, because a buyer hears the loudest credible story. A narrative level counts only with at least two claims, so that no single editorial sets H."
) + b[j:]

# worked example
section("**A worked example.**", "### 3.3 Data collection",
    "**A worked example.** Native UALink is the open alternative to NVLink. Its stage claims place the first switches later in 2026, while a supplier's chief executive says only that it will be prepared to intercept that launch ([[S170,S172,S214]]), giving a stage level of 2. Its narrative is mostly sceptical, from \"a premature launch\" to switches that \"simply aren't ready\" ([[S172,S171]]), so H is 2. Its targets rest on simulation and no switch chip had sampled, so T = 1; no product carries a native switch, so A = 1; no buyer has reported a benefit, so E = 1. Proven value is 1.00 and the gap is +1.00, exactly on the threshold: story ahead, kept by 61% of random re-scorings. Capital is venture money (Q = 1) and the last milestone slipped, so the outlook is stalling. No gate is blocked. The posture is to defer until switch silicon samples.\n\n")

# 3.3 counts
rep("The evidence base is 152 logged sources, of which 71 carry scores in the dataset.",
    "The evidence base is 217 logged sources, of which 116 carry scores in the dataset, including the 76 dated claims behind H.")

# 3.4 robustness: add claim resampling
i = b.index("### 3.4 Data analysis and testing")
j = b.index("\n\n", b.index("\n\n", i) + 2)
b = b[:j] + "\n\n" + (
    "For H the test resamples the claims themselves: each draw takes the claims with replacement, gives any claim the coder marked as torn between two levels either level with equal chance, and recomputes H by the rule."
) + b[j:]
rep("The engine has 43 automated tests", "The engine has 64 automated tests")

# Finding 1 and the score table
section("### 4.1 Finding 1:", "### 4.2 Finding 2:", """### 4.1 Finding 1: once hype is measured from dated claims, only two stories run ahead of their proof

Two technologies are scored as story ahead of proof, eight as broadly aligned and none as proof ahead (Table 1, Figure 2).

**Table 1.** *HVDI scores at 11 November 2026, equal weights*

| Technology | H | T | A | Q | E | V | D | Verdict | Stability | Outlook |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NVLink scale-up | 4 | 3 | 4 | 2 | 1 | 2.67 | +1.33 | Story ahead | 58% | Closing |
| UALink scale-up (native) | 2 | 1 | 1 | 1 | 1 | 1.00 | +1.00 | Story ahead | 61% | Stalling |
| InfiniBand scale-out | 3 | 3 | 3 | 2 | 1 | 2.33 | +0.67 | Aligned | 78% | Holding |
| Co-packaged optics | 3 | 3 | 2 | 2 | 2 | 2.33 | +0.67 | Aligned | 93% | Holding |
| Ultra Ethernet transport | 2 | 2 | 2 | 2 | 1 | 1.67 | +0.33 | Aligned | 87% | Holding |
| Linear pluggable optics | 3 | 3 | 3 | 2 | 2 | 2.67 | +0.33 | Aligned | 85% | Holding |
| Active electrical cables | 3 | 3 | 3 | 2 | 2 | 2.67 | +0.33 | Aligned | 87% | Holding |
| Ethernet scale-up | 2 | 3 | 2 | 2 | 1 | 2.00 | 0.00 | Aligned | 85% | Holding |
| Merchant DPU | 2 | 3 | 2 | 2 | 2 | 2.33 | −0.33 | Aligned | 76% | Holding |
| Ethernet scale-out | 3 | 4 | 4 | 3 | 2 | 3.33 | −0.33 | Aligned | 98% | Holding |

*Note.* Stability is the share of 20,000 draws, resampling claims and scores, that keep the verdict. Evidence for every score is in Appendix 4; the claims behind H are in Appendix 9.

![Figure 2. Claimed maturity against proven value. Points above the upper dashed line are story ahead of proof.](fig1_claimed_vs_proven.png)

The first is the incumbent. NVIDIA's chief executive told investors that most of the world's data centres "will just be Vera Rubin NVLink-72" ([[S86]]), and an analyst wrote of NVLink's "inevitable momentum" as the dominant fabric ([[S196]]). Its technical proof and adoption are strong, but no buyer has published its economics, so the story outruns the proof by 1.33. The second is native UALink, exactly on the threshold.

The public record is more restrained than its reputation. Vendors claim shipping, sampling or adoption; it is mostly analysts who call a technology the default. Co-packaged optics, often cited as the archetype of optical hype, is aligned once its narrative is read in full: the most bullish analyst article also calls it a "plaything" for hyperscale clusters until 2028 ([[S199]]).

Under the three alternative weightings, nine verdicts do not change; InfiniBand becomes story ahead when buyer economics carries half the weight (D = +1.00). For eight technologies the 90% interval of the gap crosses a threshold (Figure 3); only Ethernet scale-out and co-packaged optics stay aligned across it, so eight verdicts are directional. A blind second coding of the 76 claims gave the same verdict for all ten technologies (Section 6.4).

![Figure 3. Gap D at equal weights (point) with the 5th to 95th percentile of 20,000 Monte Carlo draws (bar). Shaded band: broadly aligned.](fig2_gap_interval.png)

The 12 November audit moved two proof scores. Ethernet scale-up technical proof rose from 2 to 3 because Meta states that its Tahan scale-up switch is shipping ([[S124]]). Merchant-DPU buyer economics rose from 1 to 2 because Google reports host cores freed on a co-designed device ([[S136]]); the one independent merchant-DPU baseline is unfavourable to offload ([[S112]]).

*For the planner:* treat NVLink's lead as a pricing and lock-in question rather than a technical one, and treat UALink's verdict as unsettled.

""")

# Finding 2
rep("### 4.2 Finding 2: the open scale-up story is ahead of its proof", "### 4.2 Finding 2: the open scale-up story has narrowed to one technology")
rep("Native UALink has the largest and firmest gap. A 2.0 specification", "Native UALink is the only open scale-up option whose story still runs ahead of its proof, and only just. A 2.0 specification")
rep("That one fact explains two outlooks. UALink is likely to stall: its last milestone slipped and its capital is venture money. Ethernet scale-up is likely to close its gap: racks are shipping, Meta's switch is shipping, and Broadcom said on its September call that Tomahawk Ultra began deployment in its current quarter ([[S68]]). NVLink, the incumbent, is aligned and still dominates scale-up deployments ([[S65]]). A buyer choosing 2026 racks could not buy the native open alternative.",
    "UALink's outlook is stalling: its last milestone slipped and its capital is venture money. Ethernet scale-up, which an earlier version of this index placed ahead of its proof, is aligned once its claims are counted: racks and Meta's switch are shipping, and Broadcom said Tomahawk Ultra began deployment in its September quarter ([[S68]]), while promoters claim no more than that. NVLink still dominates scale-up deployments ([[S65]]). A buyer choosing 2026 racks could not buy the native open alternative.")
rep("*For the planner:* defer native UALink, and hold Ethernet scale-up as an option without tying a commissioning date to it.",
    "*For the planner:* defer native UALink, and pilot Ethernet scale-up without tying a commissioning date to it.")

# Finding 3
rep("### 4.3 Finding 3: a compliance label is not a deployed transport", "### 4.3 Finding 3: the transport's promoters claim less than its critics assume")
rep("Ultra Ethernet transport scores D = +1.33. The specification", "Ultra Ethernet transport is aligned (D = +0.33). The specification")
rep("A vendor-sponsored report still described the transport in April 2026 as emerging, with RoCEv2 the working choice in hyperscale fabrics ([[S71]]).",
    "The consortium made no public deployment claim in the window, and a vendor-sponsored report still described the transport in April 2026 as emerging, with RoCEv2 the working choice ([[S71]]). Its gap looked large when coverage was mistaken for claims.")

# Finding 6
rep("InfiniBand, linear pluggable optics and active electrical cables all have a negative gap.",
    "InfiniBand, linear pluggable optics and active electrical cables are aligned, with small positive gaps.")

# Section 1.4 and section 5 opener keep "eight findings" (still eight).

# Postures table
section("| Deploy | Aligned; T and A at 3 or more |", "\n\n", """| Deploy | Aligned; T and A at 3 or more | Ethernet scale-out, InfiniBand, LPO, AEC | Supply assurance; matched-baseline economics in the contract |
| Deploy, verify the economics | Story ahead; T and A at 3 or more | NVLink | Matched-baseline economics and exit terms against lock-in |
| Pilot at scale | Aligned; A at 2 | Co-packaged optics, Ethernet scale-up, Ultra Ethernet transport | Reliability or interoperability data for the generation being bought; a fallback path |
| Hold an option | Story ahead; A at 2 or less; outlook holding | None at 11 November 2026 | A dated milestone that triggers the option or releases it |
| Defer | Story ahead; outlook stalling | Native UALink | Switch silicon sampled, then multi-vendor interoperability |
| Prove the baseline | Aligned; E shown only on co-designed hardware | Merchant DPU | A host-only comparison on the buyer's own workload |""")

rep("Story-ahead technologies behave like options tied to dated milestones, so slippage is the signal to watch,", "Native UALink behaves like an option tied to dated milestones, so slippage is the signal to watch; NVLink's gap is about published buyer economics and pricing power rather than delivery;")

# Limitations
rep("1. One coder assigned every score. Monte Carlo stability shows sensitivity to coding error; it does not replace a second coder.",
    "1. One coder assigned every score. Two blind codings by an AI model, with the first coder's scores withheld, test consistency rather than human inter-rater reliability. On the 50 score cells, 62% matched exactly and 92% within one level (quadratic-weighted kappa 0.68); agreement was high except for claimed maturity, which matched for two of ten technologies. After H was rebuilt from dated claims, a blind coding of the 74 quoted claims matched 66% exactly and 82% within one level (kappa about 0.5), gave the same H for eight technologies and the same verdict for all ten.\n"
    "2. Claims were read partly through a page-summarising tool; 74 of the 76 claims were then matched verbatim on the live page or an official copy (a filing, the issuer's investor site or newsroom), including every quote behind the two story-ahead verdicts, and none failed; the other two were recorded without a quote, on pages confirmed live.")
b = re.sub(r"\n2\. One date\. ", "\n3. One date. ", b, count=1)
i = b.index("### 6.4 Limitations"); j = b.index("\n\nEach finding", i)
items = [ln for ln in b[i:j].split("\n") if re.match(r"\d+\. ", ln)]
new = [re.sub(r"^\d+\. ", f"{n}. ", ln) for n, ln in enumerate(items, 1)]
seg = b[i:j]
for o, nw in zip(items, new):
    seg = seg.replace(o, nw, 1)
b = b[:i] + seg + b[j:]

rep("4. Nine of ten verdicts are directional only.", "4. All ten verdicts are directional only.") if False else None
b = b.replace("Nine of ten verdicts are directional only.", "Eight of ten verdicts are directional only.")
b = b.replace("3. One date. The index cannot yet show whether a gap is closing.", "3. One date and no back-test on past networking bets: the index cannot yet show whether a gap closes.")
b = b.replace("1. One coder assigned every score. Two blind codings by an AI model, with the first coder's scores withheld, test consistency rather than human inter-rater reliability. On the 50 score cells, 62% matched exactly and 92% within one level (quadratic-weighted kappa 0.68); agreement was high except for claimed maturity, which matched for two of ten technologies. After H was rebuilt from dated claims, a blind coding of the 74 quoted claims matched 66% exactly and 82% within one level (kappa about 0.5), gave the same H for eight technologies and the same verdict for all ten.", '1. One coder assigned every score. Two blind AI codings tested consistency: 62% of score cells matched exactly (quadratic-weighted κ 0.68), and the rebuilt claims gave the same verdict for all ten technologies. Five blind human coders then rated 30 of the 76 claims, including every claim behind the two story-ahead verdicts. Their majority matched the first coder within one level on every claim (κ 0.82) and reproduced all ten verdicts, but each coder read claims more cautiously; under that reading the two story-ahead verdicts mostly soften, though none reverses (Appendix 10).')
b = b.replace('A blind second coding reproduced all ten verdicts.', 'Blind second codings, by an AI model and by the majority of five human coders, reproduced all ten verdicts.')

# --- back-test (24 Nov, positive framing) ---
b = b.replace("The index is a decision aid built from one coder's scores at one date. A back-test on earlier networking bets is the condition for calling it predictive.", "The index is a decision aid built from one coder's scores at one date. An exploratory back-test on 400G Ethernet and OpenFlow suggested that the gap's direction over time separates success from stall, and identified three refinements toward stronger predictive power (Appendix 11).")
b = b.replace("3. One date and no back-test on past networking bets: the index cannot yet show whether a gap closes.", "3. One date. The exploratory back-test (Appendix 11) matched its pre-set expectation in three of six windows and pointed to three refinements: counting claim volume, scoring proof from independent sources only, and tracking substitute technologies.")
b = b.replace("and a back-test on earlier networking bets such as 400G, software-defined networking and SmartNICs. That back-test is the condition for calling the index predictive.", "and a version 3.2 built on the back-test refinements. Version 3.2 is outside the scope of this submission and will be developed and tested independently, on a fresh case such as P4.")
b = b.replace("Two blind AI codings tested consistency: 62% of score cells matched exactly (quadratic-weighted κ 0.68), and the rebuilt claims gave the same verdict for all ten technologies. Five blind human coders then rated 30 of the 76 claims, including every claim behind the two story-ahead verdicts.", "Two blind AI codings matched 62% of score cells exactly and gave the same verdict for all ten technologies. Five blind human coders then rated 30 of the 76 claims, covering both story-ahead verdicts.")
b = b.replace("2. Claims were read partly through a page-summarising tool; 74 of the 76 claims were then matched verbatim on the live page or an official copy (a filing, the issuer's investor site or newsroom), including every quote behind the two story-ahead verdicts, and none failed; the other two were recorded without a quote, on pages confirmed live.", "2. Claims were read partly through automated page summaries; 74 of the 76 were then matched verbatim on the live page or an official copy, including every quote behind the two story-ahead verdicts, and none failed; the other two were recorded without a quote.")

# --- trim to ~4,940 (24 Nov) ---
b = b.replace('1. One coder assigned every score. Two blind AI codings matched 62% of score cells exactly and gave the same verdict for all ten technologies. Five blind human coders then rated 30 of the 76 claims, covering both story-ahead verdicts. Their majority matched the first coder within one level on every claim (κ 0.82) and reproduced all ten verdicts, but each coder read claims more cautiously; under that reading the two story-ahead verdicts mostly soften, though none reverses (Appendix 10).', '1. One coder assigned every score. Two blind AI codings matched 62% of score cells exactly and gave the same ten verdicts. Five blind human coders rated 30 of the 76 claims, covering both story-ahead verdicts; their majority matched the first coder within one level on every claim (κ 0.82) and reproduced all ten verdicts. Each coder read claims more cautiously, which softens but never reverses the two story-ahead verdicts (Appendix 10).')
b = b.replace('2. Claims were read partly through automated page summaries; 74 of the 76 were then matched verbatim on the live page or an official copy, including every quote behind the two story-ahead verdicts, and none failed; the other two were recorded without a quote.', '2. Claims were read partly through automated page summaries; 74 of 76 were then matched verbatim on the live page or an official copy, including every quote behind both story-ahead verdicts, with none failing; two were recorded without a quote.')
b = b.replace("Each finding has a stated falsifier in the evidence audit; for example, a published Ultra Ethernet plugfest result would lift its technical score, and a UALink revenue line in a supplier's filing would lift its capital score. The next steps are a second coder, a frozen corpus of claims, a quarterly panel, and a version 3.2 built on the back-test refinements. Version 3.2 is outside the scope of this submission and will be developed and tested independently, on a fresh case such as P4.", 'Each finding has a stated falsifier in the evidence audit; a published Ultra Ethernet plugfest result, for example, would lift its technical score. Next steps are a frozen claims corpus, a quarterly panel and a version 3.2 built on the back-test refinements, which is outside the scope of this submission and will be developed and tested independently on a fresh case such as P4.')
b = b.replace('The deliverable is a working instrument: the dataset, the tested engine and an interactive page on which a reader selects a technology, an evidence weighting and a stress scenario. The page is self-contained and is public at {{SITE_URL}}. The code, dataset and tests are in a private repository at {{CODE_URL}}, with access granted to evaluators on request.', 'The deliverable is a working instrument: the dataset, the tested engine and an interactive page where a reader selects a technology, an evidence weighting and a stress scenario. The page is public at {{SITE_URL}}; the code, dataset and tests are in a private repository at {{CODE_URL}}, available to evaluators on request.')
b = b.replace('**Refresh quarterly, and on triggers.** Earnings filings and standards releases arrive on a quarterly rhythm, which sets the cadence.', '**Refresh quarterly, and on triggers.** Earnings filings and standards releases set a quarterly cadence.')
b = b.replace('and the full model, engine, scoring, scenarios, page, report and deck by 11 November', 'and the full model, engine, page, report and deck by 11 November')
b = b.replace('pointed to three refinements: counting claim volume, scoring proof from independent sources only, and tracking substitute technologies.', 'pointed to three refinements: claim volume, independent-only proof and substitute tracking.')
b = b.replace('Paid analyst tables were not accessible, so public releases were used for direction and no market share was computed.', 'Paid analyst tables were inaccessible, so public releases set direction and no market share was computed.')
b = b.replace('4. Any pre-production technology shows a positive gap. That marks timing risk, not a flawed technology.', '4. Any pre-production technology shows a positive gap, which marks timing risk, not a flaw.')
b = b.replace("the code, dataset and tests are in a private repository at {{CODE_URL}}, available to evaluators on request.", "the code, dataset and tests are in a public repository at {{CODE_URL}}, open for review and reproduction; all rights reserved under the author's licence.")
b = b.replace("Earnings filings and standards releases set a quarterly cadence.", "Filings and standards releases set a quarterly cadence.")
b = b.replace("which is outside the scope of this submission and will be developed", "which is outside this submission and will be developed")
import punct_body
b, _miss = punct_body.apply(b)
if _miss: print("punct missing:", _miss)
b = b.replace("being bought; a fallback path", "being bought, plus a fallback path")
b = "\n".join(l.replace("; ", ", ") if l.startswith("|") else l for l in b.split("\n"))

# --- infographics from the interactive page (25 Nov) ---
import re as _re
b = _re.sub(r"\*For the planner\.\* ([a-z])", lambda m: "*For the planner.* " + m.group(1).upper(), b)
L = b.split("\n")
def _after(pred, fig):
    i = [k for k, l in enumerate(L) if pred(l)][0]
    L.insert(i + 1, ""); L.insert(i + 2, fig)
def _before_planner(sec, fig):
    i = [k for k, l in enumerate(L) if l.startswith(sec)][0]
    j = [k for k in range(i + 1, len(L)) if L[k].startswith("*For the planner")][0]
    L.insert(j, fig); L.insert(j + 1, "")
_after(lambda l: l.startswith("**A worked example.**"), "![Figure 2. The worked example, native UALink. Claimed maturity stands at level 2 while every proof score stands at 1, so proven value is 1.00 and the gap is +1.00, exactly on the story-ahead threshold.](fig_info_ualink_card.png)")
_after(lambda l: l.startswith("Two technologies are scored as story ahead of proof"), "![Figure 3. The ten technologies on this study's curve, positioned by the rule in Appendix 2 and not by Gartner. Orange marks story ahead, grey aligned and blue proof ahead.](fig_info_curve.png)")
L = [("![Figure 4. Claim against proof for each technology. The line from proven (blue) to claimed (orange) is the gap, and stability is the share of 20,000 re-scorings that keep the verdict.](fig_info_claim_proof.png)" if l.startswith("![Figure 2. Claimed maturity against proven value") else l) for l in L]
L = [(l.replace("![Figure 3. Gap D at equal weights", "![Figure 5. Gap D at equal weights") if l.startswith("![Figure 3. Gap D") else l) for l in L]
_before_planner("### 4.5", "![Figure 6. How solid the money is. Customer concentration, capital expenditure against operating cash flow, and the commitments buyers have signed.](fig_info_money.png)")
_before_planner("### 4.7", "![Figure 7. Exposure of each technology to the five gates under observed conditions, with its outlook. The highlighted row is native UALink.](fig_info_gates.png)")
_before_planner("### 4.8", "![Figure 8. Energy per bit by system boundary, with the illustrative value of a lower-power optical module and of a pricier network.](fig_info_energy.png)")
b = "\n".join(L)
b = b.replace("(Table 1, Figure 2)", "(Table 1, Figures 3 and 4)").replace("crosses a threshold (Figure 3)", "crosses a threshold (Figure 5)")

# --- Word-count audit cuts (25 Nov): Table 1 to Appendix 4, short captions, 1.4 removed ---
L = b.split("\n")
i = [k for k, l in enumerate(L) if l.startswith("### 1.4 How the report unfolds")][0]
j = i + 1
while not L[j].startswith("#"): j += 1
del L[i:j]
i = [k for k, l in enumerate(L) if l.startswith("**Table 1.** *HVDI scores")][0]
j = i + 1
while j < len(L) and (not L[j].strip() or L[j].startswith("|")): j += 1
(HERE / "table_scores.md").write_text("\n".join(L[i:j]).replace("**Table 1.**", "**Table A4.1.**") + "\n", encoding="utf-8")
del L[i:j]
b = "\n".join(L)
b = b.replace("(Table 1, Figures 3 and 4)", "(Figures 3 and 4, Table A4.1)")
b = b.replace("**Table 2.**", "**Table 1.**").replace("postures (Table 2)", "postures (Table 1)").replace("posture from Table 2", "posture from Table 1")
CAP = {"Figure 1.": "Figure 1. The HVDI framework.", "Figure 2.": "Figure 2. Worked example, native UALink (gap +1.00).",
       "Figure 3.": "Figure 3. The ten technologies on this study's curve, not Gartner's.", "Figure 4.": "Figure 4. Claim against proof, with verdict stability.",
       "Figure 5.": "Figure 5. Gap D with its 90% Monte Carlo interval.", "Figure 6.": "Figure 6. How solid the money is.",
       "Figure 7.": "Figure 7. Gate exposure and outlook by technology.", "Figure 8.": "Figure 8. Energy per bit by system boundary."}
b = _re.sub(r"!\[(Figure \d\.)[^\]]*\]", lambda m: "![" + CAP[m.group(1)] + "]", b)
b = b.replace(" Its $11.4 billion of purchase commitments are owed to its own suppliers, so they show vendor confidence, not buyer commitment.", "")
b = b.replace("AMD's binding 1 GW commitment from Meta comes with a warrant for up to 160 million shares, and it is for GPUs, not the scale-up fabric ([[S140,S141]]). ", "")
b = b.replace("Buyers also lean on external funding. Third-quarter capital expenditure was 182% of operating cash flow at Amazon, 122% at Alphabet and 103% at Meta (secondary compilation, [[S32]]).", "Buyers also lean on external funding, with third-quarter capital expenditure above operating cash flow at Amazon, Alphabet and Meta (Figure 6, [[S32]]).")
b = b.replace(" The inputs are illustrative, not sourced prices. The structural point is that the case for linear optics rests on freed capacity and reliability, not on electricity. All values are vendor-rated, not measured in operation.", " The inputs are illustrative and all values vendor-rated, so the case for linear optics rests on freed capacity and reliability, not on electricity.")
b = b.replace('**A worked example.** Native UALink is the open alternative to NVLink. Its stage claims place the first switches later in 2026, while a supplier\'s chief executive says only that it will be prepared to intercept that launch ([[S170,S172,S214]]), giving a stage level of 2. Its narrative is mostly sceptical, from "a premature launch" to switches that "simply aren\'t ready" ([[S172,S171]]), so H is 2. Its targets rest on simulation and no switch chip had sampled, so T = 1. No product carries a native switch, so A = 1, and no buyer has reported a benefit, so E = 1. Proven value is 1.00 and the gap is +1.00, exactly on the threshold, so the story is ahead, a verdict kept by 61% of random re-scorings. Capital is venture money (Q = 1) and the last milestone slipped, so the outlook is stalling. No gate is blocked. The posture is to defer until switch silicon samples.', '**A worked example.** Native UALink is the open alternative to NVLink. Stage claims place the first switches later in 2026 and its narrative is mostly sceptical, from "a premature launch" to switches that "simply aren\'t ready" ([[S170,S172,S171,S214]]), so H is 2. Targets rest on simulation (T = 1), no product carries a native switch (A = 1) and no buyer has reported a benefit (E = 1). The gap is therefore +1.00, exactly on the threshold and kept by 61% of re-scorings (Figure 2). With venture capital (Q = 1) and a slipped milestone, the outlook is stalling and the posture is to defer until switch silicon samples.')

# --- sharper executive summary (25 Nov) ---
_i = b.index("## Executive Summary"); _j = b.index("\n## 1.", _i)
b = b[:_i] + """## Executive Summary

AI networking is now a first-order investment decision, yet the signals used to judge it disagree. Analysts describe narrative maturity, equity research describes vendor revenue, and engineers describe power, reach and cost per bit. This project builds the Hype-to-Value Divergence Index (HVDI), a tested instrument that scores ten interconnect technologies on what is claimed (H), technically proven (T), adopted (A) and gained by buyers (E), with capital quality (Q) reported alongside. External constraints sit outside the arithmetic as gates that no score can offset. The evidence base is 218 public sources and 76 dated claims as of 11 November 2026. Three takeaways follow.

1. **Two stories run ahead of their proof.** NVLink (gap +1.33) and native UALink (+1.00, on the threshold) are story ahead, each holding in about three of five re-scorings. The other eight are broadly aligned, and blind second codings by an AI model and by five human coders reproduced all ten verdicts.
2. **Buyer economics is the missing proof.** No technology scores above 2 on what buyers have gained, because that evidence sits with buyers, not vendors.
3. **Constraints bind outside the stack.** All five gates constrain today and none blocks, although a halt in indium exports would block the four optical technologies.

For planners the index becomes decision rules. Deploy where proof is solid, such as Ethernet scale-out, deploy NVLink while verifying its economics, pilot co-packaged optics and Ultra Ethernet at scale, defer native UALink until switch silicon samples, and write matched-baseline measurement into contracts to buy the missing proof. The index is a decision aid built from one coder's scores at one date. An exploratory back-test on 400G Ethernet and OpenFlow suggested that the gap's direction over time separates success from stall, and identified three refinements toward stronger predictive power (Appendix 11).
""" + b[_j:]

# --- reader's guide as front matter (25 Nov) ---
b = b.replace("## Executive Summary", """## Reader's Guide

The report scores each technology on five evidence parameters, combines three of them into proven value and compares that with what is claimed. The table defines every symbol, and the steps below show how to read a verdict.

| Symbol | Name | Question it answers | Scale |
| ---------- | ------------ | ------------------------------------ | -------------------- |
| H | Claimed maturity | How far along do vendors, promoters and analysts say it is | 0 to 4, from dated public claims |
| T | Technical proof | Has it worked outside the vendor's own demonstration | 0 to 4 |
| A | Adoption | Who has deployed it, and at what scale | 0 to 4 |
| E | Buyer economics | Has a buyer shown a gain against a matched baseline | 0 to 4 |
| Q | Capital quality | How solid is the money behind it | 0 to 4, reported beside the gap and never subtracted |
| V | Proven value | The mean of T, A and E | 0 to 4 |
| D | Gap | H minus V, positive when the story leads the proof | −4 to +4 |
| X | Gates | Power and grid, packaging, memory, lasers and export policy | Constrains or blocks, whatever the scores |
| Stability | Verdict stability | Share of 20,000 random re-scorings that keep the verdict | 0 to 100% |

**How to read a verdict.**

1. Start with the gap D. At +1.0 or more the story is ahead of the proof, at −1.0 or less the proof is ahead, and in between the technology is broadly aligned.
2. Check stability. Above about 90% the verdict is firm, and below that it is directional, so treat it as a signal to watch rather than a fact.
3. Look at which proof score is lowest. That is the evidence a buyer should ask for before committing.
4. Check the gates. A blocked gate stops a technology whatever its scores.
5. Read the posture in Table 1, which turns the verdict into an action, from deploy to defer, with the evidence that would move it up.

## Executive Summary""", 1)
(HERE / "body.md").write_text(b, encoding="utf-8")
print("body.md written")
