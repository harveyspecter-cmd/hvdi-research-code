"""Write a Google Apps Script that builds the blind second-coder questionnaire as a Google Form.

Same 76 claims, same shuffle (seed 42) and same codes C01-C76 as the Excel workbook, so coder_key.csv applies to both.
"""
import csv
import json
import random

TECH = {"nvlink": "NVLink (NVIDIA scale-up link)", "ualink": "UALink, native (open scale-up link)",
        "infiniband": "InfiniBand (scale-out network)", "cpo": "Co-packaged optics (CPO)",
        "uet": "Ultra Ethernet transport (UEC)", "lpo": "Linear pluggable optics (LPO)",
        "aec": "Active electrical cables (AEC)", "eth_scaleup": "Ethernet for scale-up (ESUN, SUE)",
        "dpu": "Merchant DPU / SmartNIC", "eth_scaleout": "Ethernet for scale-out AI networks"}
GIST = {"N-E01": "Ethernet is always the eventual winner and equaliser.",
        "N-S01": "What is ESUN, the new standard competing with NVLink? (headline)",
        "N-U02": "...to compete better with InfiniBand."}
NOQUOTE = {"UET-03": "No single quote. Open the link: what does Arista say about Ultra Ethernet (UEC) transport?",
           "UET-06": "No single quote. Open the link: what does Meta say about Ultra Ethernet (UEC) transport?",
           "N-I01": "No single quote. Open the link: what does Arista's CEO say about InfiniBand?"}

claims = [x for x in csv.DictReader(open("claims.csv", encoding="utf-8")) if x["include"] == "yes"]
random.Random(42).shuffle(claims)
key = {r["code"]: r["claim_id"] for r in csv.DictReader(open("coder_key.csv", encoding="utf-8"))}
rows = []
for i, x in enumerate(claims, 1):
    code = f"C{i:02d}"
    assert key[code] == x["claim_id"], "coder_key.csv out of step: rerun make_coder_workbook.py"
    q = x["quote"].strip()
    extra = NOQUOTE.get(x["claim_id"], GIST.get(x["claim_id"], ""))
    lines = [f"Technology: {TECH[x['tech']]}", f"Date: {x['date']}", f"Who said it: {x['claimant']} ({x['claimant_type']})",
             "", f"Quote: “{q}”" if q else "Quote: (no single quote)"]
    if extra:
        lines.append(("English gist: " if x["claim_id"] in GIST else "") + extra)
    lines += ["", f"Link: {x['url']}"]
    rows.append({"code": code, "text": "\n".join(lines)})

INTRO = """Time needed: about 3 hours. You do not need networking knowledge.

WHAT THIS IS
A research project measures 'hype': how mature and how successful people SAY ten AI networking technologies are. We collected 76 public statements made between Nov 2025 and Nov 2026 by companies, analysts and journalists. You will rate each one independently, so we can check that our own ratings are not one person's opinion.

FOR EACH STATEMENT
1. KIND. Stage = it says what the technology has reached NOW (shipping, in production, available, a standard being written). Narrative = it says how strong or successful it is, or where it is heading (leading, the winner, not ready, losing ground). Not a claim = it only describes features or design.
2. LEVEL 0 to 4 from the scale on the next page (skip if 'Not a claim').
3. OTHER LEVEL only if you hesitated between two.
4. CONFIDENCE, and an optional NOTE.

RULES
- Rate only what the statement SAYS, not whether you believe it.
- Work alone. Do not look at the project report, slides or website, and do not search the web for opinions.
- If a statement does two things, rate its main point.
- A confident forecast ('will become the standard') is Narrative 3 or 4, even though it is about the future.
- Open the link only if the quote is unclear or the statement says 'No single quote'.
- Your answers save only when you press Submit at the end. Use 'Edit after submit' if you need a break: submit, then reopen your link."""

SCALE = """STAGE: what has it reached now?
0  No deployment claim (choose 'Not a claim' instead)
1  A standard or specification is being written, or a product for a generation more than 12 months away   e.g. 'The 2.0 specification is published'
2  Launched, available, sampling, first shipments, or deploying within 12 months   e.g. 'X is now shipping to customers'
3  Volume or mass production, or running in production at customers   e.g. 'X is in volume production'
4  Claimed as THE default choice   e.g. 'X is the default for every new cluster'

NARRATIVE: how strong, or where heading?
0  Declining, abandoned, only a niche, or losing share with no growth   e.g. 'X is being phased out'
1  Not ready yet, premature, a long-term possibility, an open question   e.g. 'X simply isn't ready'
2  A promising contender or challenger; or growing but losing share   e.g. 'X is emerging as a real alternative'
3  Leading, winning most of the market, gaining momentum, or will dominate in about 2 years   e.g. 'X is the leading choice'
4  Explicitly the default or standard now, or the inevitable winner   e.g. 'X will inevitably win'

TIPS: 'Leading' is 3. 'Default' or 'the standard' is 4. 'Shipping' is 2; 'volume production' is 3. 'Not ready' is Narrative 1. Feature descriptions are 'Not a claim'."""

PRACTICE = """Practice with an imaginary 'Technology Z' (answers shown):
- 'Z switches entered volume production this quarter.' (a vendor)  ->  Stage 3
- 'Z is the inevitable winner of the data-centre fabric war.' (an analyst)  ->  Narrative 4
- 'Z is a promising challenger, but buyers say it is not ready.' (a journalist)  ->  Narrative 1 (main point: not ready); other level 2
- 'Z uses a new congestion scheme with 30% lower latency.' (a vendor)  ->  Not a claim
- 'The consortium published the Z 1.0 specification.'  ->  Stage 1"""

gs = f"""/**
 * HVDI blind second-coder questionnaire. Builds a Google Form with {len(rows)} statements.
 * How to run: script.google.com > New project > paste this file > select buildHvdiCoderForm > Run > allow access.
 * The log prints the form's edit link and the link to send to the coder. Responses go to a linked Google Sheet.
 * Do not share the edit link, the response sheet or the answer key with the coder.
 */
const CLAIMS = {json.dumps(rows, ensure_ascii=False, indent=1)};
const INTRO = {json.dumps(INTRO)};
const SCALE = {json.dumps(SCALE)};
const PRACTICE = {json.dumps(PRACTICE)};
const PER_PAGE = 4;

function buildHvdiCoderForm() {{
  const form = FormApp.create('HVDI second coder questionnaire');
  form.setDescription(INTRO)
      .setCollectEmail(false)
      .setAllowResponseEdits(true)
      .setProgressBar(true)
      .setShowLinkToRespondAgain(false)
      .setConfirmationMessage('Thank you. Your ratings are saved.');
  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addPageBreakItem().setTitle('The scale (keep this page in mind; it is repeated at the top of every page)');
  form.addSectionHeaderItem().setTitle('Scale').setHelpText(SCALE);
  form.addSectionHeaderItem().setTitle('Practice').setHelpText(PRACTICE);
  CLAIMS.forEach(function (c, i) {{
    if (i % PER_PAGE === 0) {{
      const last = Math.min(i + PER_PAGE, CLAIMS.length);
      form.addPageBreakItem().setTitle('Statements ' + (i + 1) + ' to ' + last + ' of ' + CLAIMS.length)
          .setHelpText('Scale reminder: Stage 1 spec, 2 shipping, 3 volume production, 4 default. Narrative 1 not ready, 2 contender, 3 leading, 4 default or inevitable winner.');
    }}
    form.addSectionHeaderItem().setTitle(c.code).setHelpText(c.text);
    form.addMultipleChoiceItem().setTitle(c.code + ' Kind')
        .setChoiceValues(['Stage', 'Narrative', 'Not a claim']).setRequired(true);
    form.addMultipleChoiceItem().setTitle(c.code + ' Level')
        .setHelpText('Leave blank only if you chose Not a claim.')
        .setChoiceValues(['0', '1', '2', '3', '4']);
    form.addMultipleChoiceItem().setTitle(c.code + ' Other level (only if torn)')
        .setChoiceValues(['0', '1', '2', '3', '4']);
    form.addMultipleChoiceItem().setTitle(c.code + ' Confidence')
        .setChoiceValues(['High', 'Medium', 'Low']).setRequired(true);
    form.addTextItem().setTitle(c.code + ' Note (optional)');
  }});
  form.addPageBreakItem().setTitle('Finish');
  form.addTextItem().setTitle('Hours taken');
  form.addParagraphTextItem().setTitle('Any statements you found hard (codes)');
  const sheet = SpreadsheetApp.create('HVDI second coder responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
  Logger.log('Edit link (keep private): ' + form.getEditUrl());
  Logger.log('Send this link to the coder: ' + form.getPublishedUrl());
  Logger.log('Responses sheet (keep private): ' + sheet.getUrl());
}}
"""
open("../out_final/HVDI_Second_Coder_Form.gs", "w", encoding="utf-8").write(gs)
print(len(rows), "statements;", len(gs.split()), "words")
