"""Build the blind questionnaire workbook for the human second coder (no first-coder levels inside)."""
import csv
import random
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

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

ORANGE, GREY, BLUE = "E8601C", "F2F1EC", "DCE9F7"
H1, B = Font(bold=True, size=14), Font(bold=True)
WRAP = Alignment(wrap_text=True, vertical="top")
thin = Border(*(Side(style="thin", color="BDBAB0"),) * 4)

wb = Workbook()
r = wb.active
r.title = "1 Read me first"
lines = [
    ("Second coder questionnaire: how strongly is each technology talked up?", H1),
    ("Time needed: about 3 hours. You do not need networking knowledge.", B),
    ("", None),
    ("What this is", B),
    ("A research project measures 'hype': how mature and how successful people SAY ten AI networking technologies are. "
     "We collected 76 public statements (quotes) made between Nov 2025 and Nov 2026 by companies, analysts and journalists. "
     "We need a second, independent person to rate each statement, so we can check that our own ratings are not just one person's opinion.", None),
    ("", None),
    ("What you do, for each row in sheet '4 Coding sheet'", B),
    ("1. Read the quote (and the English gist if the quote is not in English). Open the link only if the quote alone is unclear, or the row says 'No single quote'.", None),
    ("2. Column I, KIND: choose 'Stage' if the quote says what the technology has reached NOW (shipping, in production, available, a standard being written). "
     "Choose 'Narrative' if it says how strong, how successful or where it is heading (leading, the winner, not ready, losing ground). "
     "Choose 'Not a claim' if it only describes features or design and says nothing about adoption or success.", None),
    ("3. Column J, LEVEL 0 to 4: use the scale in sheet '2 Scales' for the kind you chose. If you chose 'Not a claim', leave the level blank.", None),
    ("4. Column K, OTHER LEVEL: only if you hesitated between two levels, put the other one here. Otherwise leave blank.", None),
    ("5. Column L, CONFIDENCE: High, Medium or Low.", None),
    ("6. Column M, NOTE: optional. One line on anything odd (for example, the quote does not match the page).", None),
    ("", None),
    ("Rules, please follow them", B),
    ("- Rate only what the statement SAYS, not whether you believe it is true.", None),
    ("- Work alone. Do not look at the project report, slides or website, and do not search the web for opinions.", None),
    ("- If one statement does two things, rate its main point.", None),
    ("- A confident forecast ('will become the standard') is a Narrative claim at level 3 or 4, even though it is about the future.", None),
    ("- Do the practice rows in sheet '3 Practice' first and compare with the answers given there.", None),
    ("- When finished, save the file and send it back. Do not change columns A to H.", None),
]
for i, (t, f) in enumerate(lines, 1):
    c = r.cell(i, 1, t); c.alignment = WRAP
    if f: c.font = f
r.column_dimensions["A"].width = 120
for i in range(1, len(lines) + 1):
    r.row_dimensions[i].height = 48 if len(lines[i - 1][0]) > 120 else 20

s = wb.create_sheet("2 Scales")
hdr = ["Level", "STAGE: what has it reached now?", "Example (stage)", "NARRATIVE: how strong or where heading?", "Example (narrative)"]
rows = [
    ("0", "No deployment claim at all (rate as 'Not a claim' instead)", "-", "Declining, abandoned, only a niche, or losing share with no growth", "'X is being phased out'"),
    ("1", "A standard or specification is being written, or a product for a generation more than 12 months away", "'The 2.0 specification is published'", "Not ready yet, premature, a long-term possibility, an open question", "'X simply isn't ready'"),
    ("2", "Launched, available, sampling, first shipments, or deploying within 12 months", "'X is now shipping to customers'", "A promising contender or challenger; or growing but losing share to others", "'X is emerging as a real alternative'"),
    ("3", "In volume or mass production, or running in production at customers", "'X is in volume production'", "Leading, winning most of the market, gaining momentum, or will dominate in about 2 years", "'X is the leading choice'"),
    ("4", "Claimed as THE default choice", "'X is the default for every new cluster'", "Explicitly the default or standard now, or the inevitable winner", "'X will inevitably win'"),
]
s.append(hdr)
for row in rows:
    s.append(list(row))
for col, w in zip("ABCDE", (7, 42, 30, 42, 30)):
    s.column_dimensions[col].width = w
for row in s.iter_rows():
    for c in row:
        c.alignment = WRAP; c.border = thin
for c in s[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=ORANGE)
s.append([]); s.append(["Tips", "'Leading' is 3. 'Default' or 'the standard' is 4. 'Shipping' is 2; 'volume production' is 3. 'Not ready' is narrative 1. Feature descriptions ('a new architecture that...') are 'Not a claim'."])
s.cell(s.max_row, 1).font = B; s.cell(s.max_row, 2).alignment = WRAP
s.merge_cells(start_row=s.max_row, start_column=2, end_row=s.max_row, end_column=5); s.row_dimensions[s.max_row].height = 45

p = wb.create_sheet("3 Practice")
p.append(["Statement (invented, about an imaginary 'Technology Z')", "Kind", "Level", "Why"])
for q in [("'Technology Z switches entered volume production this quarter.' (a vendor)", "Stage", 3, "Volume production = stage 3"),
          ("'Z is the inevitable winner of the data-centre fabric war.' (an analyst)", "Narrative", 4, "Inevitable winner = narrative 4"),
          ("'Z is a promising challenger, but buyers say it is not ready for training clusters.' (a journalist)", "Narrative", 1, "Main point is 'not ready' = 1; other level 2"),
          ("'Z uses a new lossless congestion scheme with 30% lower latency.' (a vendor)", "Not a claim", "", "Describes a feature; says nothing about adoption or success"),
          ("'The consortium published the Z 1.0 specification.' (a consortium)", "Stage", 1, "Specification work = stage 1")]:
    p.append(list(q))
for col, w in zip("ABCD", (80, 14, 8, 50)):
    p.column_dimensions[col].width = w
for row in p.iter_rows():
    for c in row:
        c.alignment = WRAP; c.border = thin
for c in p[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=ORANGE)

claims = [x for x in csv.DictReader(open("claims.csv", encoding="utf-8")) if x["include"] == "yes"]
random.Random(42).shuffle(claims)
k = wb.create_sheet("4 Coding sheet")
cols = ["Row", "Code", "Technology", "Date", "Who said it", "Type of speaker", "Quote (exact words)", "English gist / instruction",
        "KIND", "LEVEL 0-4", "OTHER LEVEL", "CONFIDENCE", "NOTE", "Link"]
k.append(cols)
for i, x in enumerate(claims, 1):
    q = x["quote"].strip()
    k.append([i, f"C{i:02d}", TECH[x["tech"]], x["date"], x["claimant"], x["claimant_type"], q or "(no single quote)",
              NOQUOTE.get(x["claim_id"], GIST.get(x["claim_id"], "")), None, None, None, None, None, x["url"]])
    k.cell(i + 1, 14).hyperlink = x["url"]; k.cell(i + 1, 14).style = "Hyperlink"
widths = (5, 9, 24, 11, 26, 14, 60, 30, 14, 9, 9, 12, 26, 40)
for j, w in enumerate(widths, 1):
    k.column_dimensions[k.cell(1, j).column_letter].width = w
for row in k.iter_rows():
    for c in row:
        c.alignment = WRAP; c.border = thin
for c in k[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=ORANGE if c.column >= 9 and c.column <= 13 else "555555")
for i in range(2, len(claims) + 2):
    for j in range(9, 14):
        k.cell(i, j).fill = PatternFill("solid", fgColor=BLUE)
k.freeze_panes = "C2"
n = len(claims) + 1
for formula, col in (('"Stage,Narrative,Not a claim"', "I"), ('"0,1,2,3,4"', "J"), ('"0,1,2,3,4"', "K"), ('"High,Medium,Low"', "L")):
    dv = DataValidation(type="list", formula1=formula, allow_blank=True); k.add_data_validation(dv); dv.add(f"{col}2:{col}{n}")

d = wb.create_sheet("5 Done")
d.append(["Coder name"]); d.append(["Date finished"]); d.append(["Hours taken"]); d.append(["Any rows you found hard (row numbers)"])
d.column_dimensions["A"].width = 40; d.column_dimensions["B"].width = 50
for c in d["A"]:
    c.font = B
with open("coder_key.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["code", "claim_id"]); w.writerows([(f"C{i:02d}", x["claim_id"]) for i, x in enumerate(claims, 1)])
wb.save("../out_final/HVDI_Second_Coder_Questionnaire.xlsx")
print(len(claims), "claims")
