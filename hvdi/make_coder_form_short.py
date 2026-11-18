"""Short, uncluttered second-coder Google Form: 30 claims, one click per statement.

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
    title = f"“{q}”" if q else NOQUOTE[x["claim_id"]]
    if x["claim_id"] in GIST:
        title += f"  (English: {GIST[x['claim_id']]})"
    who = x["claimant"].split(" via ")[0]
    items.append({"code": f"S{i:02d}", "title": f"{i}. {title}",
                  "help": f"{TECH[x['tech']]}  ·  {x['date']}  ·  {who}\n{x['url']}"})
with open("coder_key_short.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["code", "claim_id"]); w.writerows([(it["code"], x["claim_id"]) for it, x in zip(items, pick)])

CHOICES = ["Stage 1  ·  a standard or spec is being written",
           "Stage 2  ·  launched, sampling or shipping",
           "Stage 3  ·  volume production",
           "Stage 4  ·  the default choice",
           "Narrative 0  ·  declining or niche",
           "Narrative 1  ·  not ready yet",
           "Narrative 2  ·  a contender",
           "Narrative 3  ·  leading",
           "Narrative 4  ·  the default, or the inevitable winner",
           "Not a claim  ·  only describes features"]
INTRO = ("30 short statements about AI networking technologies. For each, pick the ONE option that best matches what the "
         "statement SAYS, not whether it is true. About 20 minutes. No technical knowledge needed. Please work alone.")
GUIDE = ("STAGE = what it has reached now.   NARRATIVE = how strong it is, or where it is heading.\n\n"
         "• 'shipping' = Stage 2,  'volume production' = Stage 3\n"
         "• 'leading' = Narrative 3,  'the standard' or 'will inevitably win' = Narrative 4\n"
         "• 'not ready' = Narrative 1\n"
         "• a confident forecast ('will become the standard') is Narrative\n"
         "• if a statement does two things, rate its main point")

gs = f"""/**
 * HVDI second coder, short form (30 statements, one click each).
 * Run: script.google.com > New project > paste > choose buildHvdiShortForm > Run > allow access > View > Logs.
 * Send ONLY the published link. Keep the edit link and the responses sheet private.
 */
const ITEMS = {json.dumps(items, ensure_ascii=False, indent=1)};
const CHOICES = {json.dumps(CHOICES, ensure_ascii=False)};
const INTRO = {json.dumps(INTRO)};
const GUIDE = {json.dumps(GUIDE, ensure_ascii=False)};

function buildHvdiShortForm() {{
  const form = FormApp.create('Rate 30 statements about AI networking');
  form.setDescription(INTRO).setProgressBar(true).setAllowResponseEdits(true)
      .setConfirmationMessage('Thank you, your answers are saved.');
  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addSectionHeaderItem().setTitle('How to choose').setHelpText(GUIDE);
  ITEMS.forEach(function (it, i) {{
    if (i > 0 && i % 6 === 0) {{
      form.addPageBreakItem().setTitle('Statements ' + (i + 1) + ' to ' + Math.min(i + 6, ITEMS.length)).setHelpText(GUIDE);
    }}
    form.addMultipleChoiceItem().setTitle(it.title).setHelpText(it.help)
        .setChoiceValues(CHOICES).setRequired(true);
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
