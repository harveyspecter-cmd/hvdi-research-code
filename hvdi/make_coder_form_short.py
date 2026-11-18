"""Short second-coder Google Form: 30 statements, two questions each; no links, speakers or dates shown.

Sample: every claim behind the two story-ahead verdicts (NVLink, native UALink) plus one stage and one
narrative claim for each other technology where available (English quotes only), 30 in all, shuffled.
Writes ../out_final/HVDI_Second_Coder_Form_Short.gs and coder_key_short.csv (never send the key).
"""
import csv
import json
import random

TECH = {"nvlink": "NVLink", "ualink": "UALink (native)", "infiniband": "InfiniBand", "cpo": "Co-packaged optics",
        "uet": "Ultra Ethernet transport", "lpo": "Linear pluggable optics", "aec": "Active electrical cables",
        "eth_scaleup": "Ethernet scale-up", "dpu": "Merchant DPU", "eth_scaleout": "Ethernet scale-out"}
QUOTA = {"eth_scaleout": 2, "infiniband": 2, "eth_scaleup": 2, "uet": 2, "cpo": 2, "lpo": 1, "aec": 1, "dpu": 1}
NOQUOTE = {"UET-03": "Open the link: what does Arista say about Ultra Ethernet (UEC) transport?",
           "UET-06": "Open the link: what does Meta say about Ultra Ethernet (UEC) transport?",
           "N-I01": "Open the link: what does Arista's CEO say about InfiniBand?"}
GIST = {"N-E01": "Ethernet is always the eventual winner and equaliser."}
CONTEXT = {"UET-05": "[Ultra Ethernet is] ", "UAL-1": "[The first UALink switches are] ", "NVL-3": "[NVLink is] ",
           "X-UA2": "[Products using] ", "AEC-4": "[These active electrical cables] ", "UAL-4": "[UALink] ",
           "UN3": "[UALink was] ", "UN4": "[The consortium aims to] ", "ESU-08": "[Ethernet scale-up switches:] ",
           "UAL-3": "[UALink:] ", "IB-05": "[NVIDIA's growth was] ", "UET-02": "[AMD's networking uses] ",
           "X-NV1": "[NVIDIA's NVLink-based Vera Rubin platform:] ", "NVL-4": "[Analysts describe] "}
AFTER = {"NVL-1": " [Vera Rubin = NVIDIA's NVLink rack systems]", "DPU-2": " [Vera Rubin includes NVIDIA's BlueField DPU]",
         "NC2": " [NPO = near-packaged optics]"}
ABOUT = {"nvlink": "NVLink: NVIDIA's own link between AI chips", "ualink": "UALink: an open, multi-vendor link between AI chips",
         "infiniband": "InfiniBand: a network for AI clusters, mostly sold by NVIDIA", "cpo": "Co-packaged optics: optical links built into the chip package",
         "uet": "Ultra Ethernet: a new open standard for AI networks", "lpo": "Linear pluggable optics: simpler, lower-power optical modules",
         "aec": "Active electrical cables: copper cables with chips inside", "eth_scaleup": "Ethernet scale-up: Ethernet used to link AI chips inside a rack",
         "dpu": "DPU: a network card with its own processor", "eth_scaleout": "Ethernet scale-out: Ethernet networks connecting AI racks"}

rows = [x for x in csv.DictReader(open("claims.csv", encoding="utf-8")) if x["include"] == "yes"]
english = lambda x: x["quote"].strip() and all(ord(ch) < 0x2E80 for ch in x["quote"])
pick = [x for x in rows if x["tech"] in ("nvlink", "ualink")]
rng = random.Random(7)
for tech, n in QUOTA.items():
    pool = [x for x in rows if x["tech"] == tech and english(x)]
    rng.shuffle(pool)
    chosen, kinds, levels = [], set(), set()
    for want in ("stage", "narrative"):
        for x in pool:
            if x["kind"] == want and x not in chosen:
                chosen.append(x); break
    for x in pool:  # top up with a different level if the quota allows
        if len(chosen) >= n:
            break
        if x not in chosen and x["level"] not in {c["level"] for c in chosen}:
            chosen.append(x)
    pick += chosen[:n]
assert len(pick) == 30, len(pick)
rng.shuffle(pick)

items = []
for i, x in enumerate(pick, 1):
    q = x["quote"].strip()
    st = CONTEXT.get(x["claim_id"], "") + (q or NOQUOTE[x["claim_id"]]) + AFTER.get(x["claim_id"], "")
    items.append({"code": f"S{i:02d}", "title": f"{i}. Statement: \u201c{st}\u201d", "help": ABOUT[x["tech"]]})
with open("coder_key_short.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["code", "claim_id"]); w.writerows([(it["code"], x["claim_id"]) for it, x in zip(items, pick)])

KINDS = ["Stage: what it has reached today", "Narrative: how good or big it is said to be", "Neither: it only describes features"]
LEVELS = ["0 \u00b7 Narrative only: fading, niche or losing",
          "1 \u00b7 Stage: still being designed  |  Narrative: not ready",
          "2 \u00b7 Stage: shipping or sampling  |  Narrative: a contender",
          "3 \u00b7 Stage: in volume production  |  Narrative: leading",
          "4 \u00b7 Stage: everyone's default choice  |  Narrative: the winner or the standard"]
INTRO = ("30 short statements about AI networking. For each one, answer two quick questions about what the statement SAYS "
         "(not whether it is true). About 20 minutes. No technical knowledge needed. Please do not look anything up.")
GUIDE = ("HOW TO RATE A STATEMENT\n\n"
         "Question 1: what is the statement about?\n"
         "\u2022 STAGE: what the product or technology has reached today.\n"
         "\u2022 NARRATIVE: how good, strong or successful people say it is, or where it is heading.\n"
         "\u2022 A prediction such as 'will become the standard' is NARRATIVE.\n\n"
         "Question 2: pick the level.\n"
         "STAGE:  still being designed = 1  \u00b7  shipping = 2  \u00b7  in volume production = 3  \u00b7  everyone's default = 4\n"
         "NARRATIVE:  fading or niche = 0  \u00b7  not ready = 1  \u00b7  a contender = 2  \u00b7  leading = 3  \u00b7  the winner or the standard = 4\n\n"
         "Words in [square brackets] were added only to say what the statement is about.")
gs = f"""/**
 * HVDI second coder, short form (30 statements, one click each).
 * Run: script.google.com > New project > paste > choose buildHvdiShortForm > Run > allow access > View > Logs.
 * Send ONLY the published link. Keep the edit link and the responses sheet private.
 */
const ITEMS = {json.dumps(items, ensure_ascii=False, indent=1)};
const KINDS = {json.dumps(KINDS, ensure_ascii=False)};
const LEVELS = {json.dumps(LEVELS, ensure_ascii=False)};
const INTRO = {json.dumps(INTRO)};
const GUIDE = {json.dumps(GUIDE, ensure_ascii=False)};

function buildHvdiShortForm() {{
  const form = FormApp.create('Rate 30 statements about AI networking');
  form.setDescription(INTRO).setProgressBar(true).setAllowResponseEdits(true)
      .setConfirmationMessage('Thank you, your answers are saved.');
  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addSectionHeaderItem().setTitle('How to rate').setHelpText(GUIDE);
  ITEMS.forEach(function (it, i) {{
    if (i > 0 && i % 6 === 0) {{
      form.addPageBreakItem().setTitle('Statements ' + (i + 1) + ' to ' + Math.min(i + 6, ITEMS.length)).setHelpText(GUIDE);
    }}
    form.addMultipleChoiceItem().setTitle(it.title).setHelpText(it.help + '\\n\\nQuestion 1: what is the statement about?')
        .setChoiceValues(KINDS).setRequired(true);
    form.addMultipleChoiceItem().setTitle((i + 1) + '. Level')
        .setHelpText('Question 2: pick the level (skip only if you chose Neither).')
        .setChoiceValues(LEVELS);
  }});
  const sheet = SpreadsheetApp.create('HVDI short form responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
  Logger.log('SEND THIS LINK: ' + form.getPublishedUrl());
  Logger.log('Edit link (private): ' + form.getEditUrl());
  Logger.log('Responses sheet (private): ' + sheet.getUrl());
}}
"""
open("../out_final/HVDI_Second_Coder_Form_Short.gs", "w", encoding="utf-8").write(gs)
from collections import Counter
print(Counter(x["tech"] for x in pick), Counter(x["kind"] for x in pick))
