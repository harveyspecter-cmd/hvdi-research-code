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
(HERE / "body.md").write_text(b, encoding="utf-8")
print("body.md written")
