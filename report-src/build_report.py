"""Assemble the Live Project report: APA in-text citations, reference list, figures, docx."""
import csv
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "src_rev56.md").read_text(encoding="utf-8")
SITE_URL = "https://harveyspecter-cmd.github.io/hvdi-research/"
CODE_URL = "https://github.com/harveyspecter-cmd/hvdi-research-code"

_refs = SRC[SRC.find("## 10. References"):SRC.find("## Appendix A")]
_lines = [l[2:].strip() for l in _refs.split("\n") if l.startswith("- ")]


def ex(tag: str) -> str:
    """Existing reference entry carrying this ledger tag, links flattened to plain URLs."""
    hits = [l for l in _lines if re.search(r"\\\[[^\]]*\b" + tag + r"\b[^\]]*\\\]\s*$", l)]
    if len(hits) != 1:
        raise SystemExit(f"{tag}: {len(hits)} existing entries")
    e = re.sub(r"\s*\\\[[^\]]*\\\]\s*$", "", hits[0])
    e = re.sub(r"\[([^\]]*)\]\((https?://[^)]+)\)", r"\2", e)
    return e.replace("\\[", "[").replace("\\]", "]").strip()


def exa(start: str) -> str:
    """Existing academic entry (no ledger tag) by its opening words."""
    hits = [l for l in _lines if l.startswith(start)]
    if len(hits) != 1:
        raise SystemExit(f"{start}: {len(hits)} entries")
    return hits[0]


SEC = "https://www.sec.gov/Archives/edgar/data/"
# key -> (in-text citation, reference entry). Keys are ledger IDs or academic keys.
R = {
    # ---- academic and methodological ----
    "adner2010": ("Adner & Kapoor, 2010", "Adner, R., & Kapoor, R. (2010). Value creation in innovation ecosystems: How the structure of technological interdependence affects firm performance in new technology generations. *Strategic Management Journal, 31*(3), 306–333."),
    "akerlof1970": ("Akerlof, 1970", "Akerlof, G. A. (1970). The market for \"lemons\": Quality uncertainty and the market mechanism. *The Quarterly Journal of Economics, 84*(3), 488–500."),
    "borup2006": ("Borup et al., 2006", "Borup, M., Brown, N., Konrad, K., & van Lente, H. (2006). The sociology of expectations in science and technology. *Technology Analysis & Strategic Management, 18*(3–4), 285–298."),
    "cao2025": ("Cao et al., 2025", exa("Cao, Z.")),
    "choi2025": ("Choi & Geum, 2025", exa("Choi, W.")),
    "dedehayir2016": ("Dedehayir & Steinert, 2016", exa("Dedehayir")),
    "cohen1968": ("Cohen, 1968", "Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin, 70*(4), 213–220."),
    "fleiss1971": ("Fleiss, 1971", "Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. *Psychological Bulletin, 76*(5), 378–382."),
    "krippendorff2004": ("Krippendorff, 2004", "Krippendorff, K. (2004). *Content analysis: An introduction to its methodology* (2nd ed.). Sage."),
    "landis1977": ("Landis & Koch, 1977", "Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174."),
    "fenn2008": ("Fenn & Raskino, 2008", "Fenn, J., & Raskino, M. (2008). *Mastering the hype cycle: How to choose the right innovation at the right time*. Harvard Business Press."),
    "henderson1993": ("Henderson & Venkatraman, 1993", "Henderson, J. C., & Venkatraman, N. (1993). Strategic alignment: Leveraging information technology for transforming organizations. *IBM Systems Journal, 32*(1), 4–16."),
    "hevner2004": ("Hevner et al., 2004", "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105."),
    "kim2026": ("Kim et al., 2026", exa("Kim, D.")),
    "mankins2009": ("Mankins, 2009", exa("Mankins")),
    "soh1995": ("Soh & Markus, 1995", exa("Soh, C.")),
    "spence1973": ("Spence, 1973", "Spence, M. (1973). Job market signaling. *The Quarterly Journal of Economics, 87*(3), 355–374."),
    "steinert2010": ("Steinert & Leifer, 2010", exa("Steinert")),
    "swanson1997": ("Swanson & Ramiller, 1997", "Swanson, E. B., & Ramiller, N. C. (1997). The organizing vision in information systems innovation. *Organization Science, 8*(5), 458–474."),
    "teece1986": ("Teece, 1986", "Teece, D. J. (1986). Profiting from technological innovation: Implications for integration, collaboration, licensing and public policy. *Research Policy, 15*(6), 285–305."),
    "vanlente2013": ("van Lente et al., 2013", "van Lente, H., Spitters, C., & Peine, A. (2013). Comparing technological hype cycles: Towards a theory. *Technological Forecasting and Social Change, 80*(8), 1615–1628."),
    "wang2010": ("Wang, 2010", "Wang, P. (2010). Chasing the hottest IT: Effects of information technology fashion on organizations. *MIS Quarterly, 34*(1), 63–85."),
    "S21": ("OECD & European Commission Joint Research Centre, 2008", ex("S21")),
    "S10": ("Gangidi et al., 2024", ex("S10")),
    "S112": ("Chen et al., 2024", ex("S112")),
    "S136": ("Humphries et al., 2025", ex("S136")),
    # ---- filings ----
    "S140": ("Advanced Micro Devices, 2026a", "Advanced Micro Devices, Inc. (2026a). *Form 8-K, event date February 23, 2026* [Meta agreement and warrant]. U.S. Securities and Exchange Commission. https://ir.amd.com/financial-information/sec-filings"),
    "S141": ("Advanced Micro Devices, 2026b", "Advanced Micro Devices, Inc. (2026b). *Form 10-Q for the quarter ended September 26, 2026*. U.S. Securities and Exchange Commission. https://ir.amd.com/financial-information/sec-filings"),
    "S30": ("Arista Networks, 2026a", "Arista Networks, Inc. (2026a). *Form 8-K, Exhibit 99.1: Third quarter 2026 financial results*. U.S. Securities and Exchange Commission. " + SEC + "0001596532/000159653226000252/ex991q326-earningsrelease.htm"),
    "S139": ("Arista Networks, 2026b", "Arista Networks, Inc. (2026b). *Form 10-Q for the quarter ended September 30, 2026*. U.S. Securities and Exchange Commission. " + SEC + "0001596532/000159653226000254/anet-20260930.htm"),
    "S150": ("Astera Labs, 2026", ex("S150")),
    "S142": ("Credo Technology Group, 2026a", "Credo Technology Group Holding Ltd. (2026a). *Form 10-K for the fiscal year ended May 2, 2026*. U.S. Securities and Exchange Commission. https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf"),
    "S147": ("Credo Technology Group, 2026b", "Credo Technology Group Holding Ltd. (2026b). *Form 10-Q for the quarter ended August 1, 2026*. U.S. Securities and Exchange Commission. https://investors.credosemi.com"),
    "S116": ("NVIDIA, 2026a", "NVIDIA Corporation. (2026a). *Form 8-K: Fourth quarter and fiscal 2026 results*. U.S. Securities and Exchange Commission. https://d18rn0p25nwr6d.cloudfront.net/CIK-0001045810/5f86707e-03f3-4e5e-b9bd-048e42123723.pdf"),
    "S54": ("NVIDIA, 2026b", "NVIDIA Corporation. (2026b). *Form 10-Q for the quarter ended July 26, 2026*. U.S. Securities and Exchange Commission. " + SEC + "0001045810/000104581026000075/nvda-20260726.htm"),
    # ---- standards bodies and operators ----
    "S152": ("Ultra Ethernet Consortium, 2025", "Ultra Ethernet Consortium. (2025). *Test bed recommendations* (Revision 1.0) [Member document; paraphrased only]. https://ultraethernet.org/"),
    "S72": ("Ultra Ethernet Consortium, 2026b", "Ultra Ethernet Consortium. (2026b). *Ultra Ethernet specification* (Version 1.1). https://ultraethernet.org/specification"),
    "S73": ("Ultra Ethernet Consortium, 2026a", "Ultra Ethernet Consortium. (2026a). *Compliance*. https://ultraethernet.org/compliance/"),
    "S34": ("UALink Consortium, 2026", "UALink Consortium. (2026). *UALink white paper*. https://ualinkconsortium.org/wp-content/uploads/2026/01/UALink_White_Paper_Publication_FINAL_UPDATED.pdf"),
    "S87": ("Meta, 2024", ex("S87")),
    "S124": ("Meta, 2026a", ex("S124").replace("(2026, October 12)", "(2026a, October 12)")),
    "S120": ("Meta, 2026b", ex("S120").replace("(2026, October 26)", "(2026b, October 26)")),
    "S137": ("Yekani & Wang, 2026", "Yekani, A., & Wang, Q. (2026, October). *Operating linear pluggable optics at hyperscale: From link management to production reliability* [Conference session slides]. OCP Global Summit 2026. https://www.opencompute.org/?p=245678"),
    "S148": ("Yu & Chakravarty, n.d.", ex("S148")),
    "S78": ("Oracle, 2025", ex("S78")),
    "S05": ("Rand et al., 2026", ex("S05")),
    # ---- analyst releases ----
    "S65": ("Dell'Oro Group, 2026a", "Dell'Oro Group. (2026a, February 4). *AI back-end switch market will push past $100 billion by 2030* [Press release]. https://www.delloro.com/news/ai-back-end-switch-market-will-push-past-100-billion-by-2030/"),
    "S11": ("Dell'Oro Group, 2026b", "Dell'Oro Group. (2026b, June 2). *Ethernet extends lead in AI scale-out networks despite strong InfiniBand rebound* [Press release]. https://www.delloro.com/news/ethernet-extends-lead-in-ai-scale-out-networks-despite-strong-infiniband-rebound/"),
    "S29": ("Dell'Oro Group, 2026c", "Dell'Oro Group. (2026c, September 3). *AI back-end networks switch sales surpass front-end networks for the first time in 2Q2026* [Press release]. https://www.delloro.com/news/ai-back-end-networks-switch-sales-surpass-front-end-networks-for-the-first-time-in-2q2026/"),
    "S67": ("Dell'Oro Group, 2026d", "Dell'Oro Group. (2026d, October). *It is not just about faster NICs* [Blog post]. https://www.delloro.com/it-is-not-just-about-faster-nics/"),
    "S36": ("Dell'Oro Group, 2026e", "Dell'Oro Group. (2026e, October). *OCP 2026: Optics takes center stage in enabling the next wave of AI networking and high-speed switching* [Blog post]. https://www.delloro.com/ocp-2026-optics-takes-center-stage-in-enabling-the-next-wave-of-ai-networking-and-high-speed-switching/"),
    "S01": ("IDC, 2026", "IDC. (2026). *Ethernet switch market surges 43.4% to $18.9B in 2Q26 as AI infrastructure demand drives record datacenter spending* [Blog post]. https://www.idc.com/resource-center/blog/ethernet-switch-market-surges-43-4-to-18-9b-in-2q26-as-ai-infrastructure-demand-drives-record-datacenter-spending"),
    "S37": ("Cignal AI, 2025", ex("S37")),
    "S60": ("TrendForce, 2026a", "TrendForce. (2026a, June 15). [News report on the CoWoS supply and demand gap]. https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-rep"),
    "S43": ("TrendForce, 2026b", "TrendForce. (2026b, June 23). [News report on HBM4 ramp strategies at memory suppliers]. https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/"),
    "S63": ("Technology Business Research, 2026", "Technology Business Research. (2026). *AMD enters the execution phase of its full-stack AI strategy* [Special report]. https://tbri.com/special-reports/amd-enters-the-execution-phase-of-its-full-stack-ai-strategy/"),
    "S71": ("Jander, 2026", ex("S71")),
    # ---- vendor documents ----
    "S46": ("Arista Networks, n.d.-a", "Arista Networks, Inc. (n.d.-a). *7060X and 7260X series data sheet*. https://www.arista.com/assets/data/pdf/Datasheets/7060X_7260X_DS.pdf"),
    "S47": ("Arista Networks, n.d.-b", "Arista Networks, Inc. (n.d.-b). *7060X4 series data sheet*. https://www.arista.com/assets/data/pdf/Datasheets/7060X4-Datasheet.pdf"),
    "S48": ("Arista Networks, n.d.-c", "Arista Networks, Inc. (n.d.-c). *7060X5 series quick start guide*. https://www.arista.com/assets/data/pdf/qsg/qsg-books/QS_7060X5.pdf"),
    "S49": ("Arista Networks, n.d.-d", "Arista Networks, Inc. (n.d.-d). *7060X6 series data sheet*. https://www.arista.com/assets/data/pdf/Datasheets/7060X6-Datasheet.pdf"),
    "S66": ("Broadcom, 2025", ex("S66")),
    "S68": ("Broadcom, 2026", ex("S68")),
    "S50": ("Jabil, n.d.", "Jabil. (n.d.). *800G OSFP DR8/DR8+ optical transceiver* [Data sheet]. https://www.jabil.com/dam/jcr:9134ce1b-c889-4d8e-9d7e-fdaa513e5c5e/Jabil_800G%20OSFP%20DR8_DR8+%20OpticalTransceiver_10.pdf"),
    "S51": ("FS, n.d.", "FS. (n.d.). *What is the LPO transceiver?* [Blog post]. https://www.fs.com/blog/what-is-the-lpo-transceiver-8.html"),
    # ---- press and secondary ----
    "S57": ("Tech Insider, 2026", "Tech Insider. (2026, November). [Article on 2026 US corporate bond issuance by large technology companies, citing Reuters and LSEG data]. https://tech-insider.org/big-tech-us-corporate-bond-record-1-88-trillion-2026/"),
    "S32": ("Walnut Invest, 2026", "Walnut Invest. (2026). *AI capex statistics* [Data compilation from company releases]. https://walnutinvest.com/stats/ai-capex-statistics"),
    "S62": ("Electrical Contractor Magazine, 2026", "Electrical Contractor Magazine. (2026). *How long does it take to power a data center?* https://www.ecmag.com/magazine/articles/article-detail/how-long-does-it-take-to-power-a-data-center"),
    "S31": ("Redmond Magazine, 2026", ex("S31")),
    "S33": ("The Register, 2026", ex("S33")),
    "S59": ("Morgan Lewis, 2026", ex("S59")),
    "S61": ("Tom's Hardware, 2026", "Tom's Hardware. (2026). [Article on the indium phosphide shortage, reporting remarks by Lumentum's chief executive]. https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory"),
    "S98": ("ServeTheHome, 2026", ex("S98")),
    "S39": ("Simple Tech Trend, 2026", ex("S39")),
}


# ---- claims corpus sources (S153 onward), generated from hvdi/new_sources.csv ----
ALIAS = {"Arista": "Arista Networks", "AMD": "Advanced Micro Devices", "Dell'Oro Group": "Dell'Oro Group",
         "Credo": "Credo Technology Group", "Marvell": "Marvell Technology", "IDC": "IDC",
         "NVIDIA and Marvell": "NVIDIA", "Lightwave": "Lightwave", "Futurum Group": "Futurum Group"}
MONTHS = "January February March April May June July August September October November December".split()


def _author(pub: str) -> str:
    """Organisation as APA author: drop bylines in brackets and relays ("via ...")."""
    a = re.split(r"\s*\(|,\s*via\s|\s+via\s", pub)[0].strip().rstrip(",")
    a = a.split(" / ")[0].strip()
    return ALIAS.get(a, a)


def _add_corpus_sources() -> None:
    path = HERE.parent / "hvdi" / "new_sources.csv"
    if not path.exists():
        return
    rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r["source_id"] not in R]
    new = {}
    for r in rows:
        y, mo, dd = (r["date"] + "--").split("-")[:3]
        year = y if y.isdigit() else "n.d."
        when = year if not (mo.isdigit() and dd.isdigit()) else f"{year}, {MONTHS[int(mo) - 1]} {int(dd)}"
        c0 = r["class"].lower()
        cls = ("Earnings call transcript" if "earnings call" in c0 else "Press release" if "press release" in c0
               else "Blog post" if "blog" in c0 else "Research note" if "analyst" in c0
               else "Sponsored article" if "sponsored" in c0 else "Article" if "trade" in c0 else "Web page")
        new[r["source_id"]] = dict(author=_author(r["publisher"]), year=year, when=when, title=r["title"].strip(),
                                   url=r["url"].strip(), cls=cls, date=r["date"])
    # APA year suffixes across existing and new entries that share author and year
    groups = {}
    for k, (intext, _) in R.items():
        if ", " in intext:
            a, y = intext.rsplit(", ", 1)
            groups.setdefault((a, y[:4]), []).append(("0", k))
    for k, v in new.items():
        groups.setdefault((v["author"], v["year"]), []).append((v["date"] or "9", k))
    for (a, y), members in groups.items():
        if len(members) < 2:
            members = members
        letters = len(members) > 1
        members.sort(key=lambda m: (m[0] != "0", R[m[1]][0] if m[0] == "0" else m[0]))
        for i, (_, k) in enumerate(members):
            suf = chr(97 + i) if letters and y != "n.d." else ("-" + chr(97 + i) if letters else "")
            if k in new:
                v = new[k]
                when = v["when"].replace(v["year"], v["year"] + suf, 1)
                entry = f"{v['author']}. ({when}). *{v['title']}* [{v['cls']}]. {v['url']}"
                R[k] = (f"{v['author']}, {v['year']}{suf}", entry)
            elif letters:
                intext, entry = R[k]
                base = re.sub(r"(\d{4})[a-z]?$", r"\1", intext.rsplit(", ", 1)[1])
                if base == y:
                    R[k] = (f"{a}, {y}{suf}", re.sub(r"\((\d{4})[a-z]?", lambda m: f"({m.group(1)}{suf}", entry, count=1))


R.update({
    "S75": ("Network World, 2026", "Network World. (2026, October 14). *Ultra Ethernet 1.1 extends the specification to scale-up networks and adds programmable congestion control* [Article]. https://www.networkworld.com/article/4235340/ultra-ethernet-1-1-extends-the-specification-to-scale-up-networks-and-adds-programmable-congestion-control.html"),
    "S83": ("Broadcom, 2026", "Broadcom. (2026, September 2). *Q3 fiscal year 2026 earnings call* [Earnings call transcript, via Webull]. https://www.webull.com/news/15511095937917952"),
    "S86": ("NVIDIA, 2026", "NVIDIA. (2026, August 26). *Q2 fiscal year 2027 earnings call* [Earnings call transcript]. https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"),
})
_add_corpus_sources()


def cite(m: re.Match) -> str:
    keys = [k.strip() for k in m.group(1).split(",")]
    for k in keys:
        if k not in R:
            raise SystemExit(f"no reference for {k}")
        USED.add(k)
    parts = sorted({R[k][0] for k in keys}, key=str.lower)
    # merge same-author runs: "Dell'Oro Group, 2026b; Dell'Oro Group, 2026e" -> "Dell'Oro Group, 2026b, 2026e"
    out, last = [], None
    for p in parts:
        a, y = p.rsplit(", ", 1)
        if a == last:
            out[-1] += ", " + y
        else:
            out.append(p)
        last = a
    return "; ".join(out)


USED: set = set()
NARRATIVE = {"kim2026": "Kim et al. (2026)", "choi2025": "Choi and Geum (2025)", "cao2025": "Cao et al. (2025)"}


def render(text: str) -> str:
    # "(estimate, [[S29]])" style: citation already inside parentheses
    text = re.sub(r"\(([^()\[\]]*?)\[\[([^\]]+)\]\]\)", lambda m: "(" + m.group(1) + cite(re.match(r"(.*)", m.group(2))) + ")", text)
    text = re.sub(r"\(\[\[([^\]]+)\]\]\)", lambda m: "(" + cite(m) + ")", text)
    if "[[" in text:
        raise SystemExit("unrendered citation: " + text[text.find("[["):][:60])
    for k, n in NARRATIVE.items():
        if n in text:
            USED.add(k)
    return text


def words(md: str) -> int:
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"^\|[ -:|]+\|$", "", md, flags=re.M)
    return len(re.sub(r"[#*|_]", " ", md).split())


TECH = {"eth_scaleout": "Ethernet scale-out", "infiniband": "InfiniBand", "uet": "Ultra Ethernet transport",
        "nvlink": "NVLink", "ualink": "Native UALink", "eth_scaleup": "Ethernet scale-up", "dpu": "Merchant DPU",
        "cpo": "Co-packaged optics", "lpo": "Linear pluggable optics", "aec": "Active electrical cables"}
SAME_DOC = {"S83": "S68"}  # two transcript copies of one Broadcom call: cite the one already in the report


def claims_table() -> str:
    """Markdown table of the included claims, citing each source."""
    path = HERE.parent / "hvdi" / "claims.csv"
    rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r["include"] == "yes"]
    order = list(TECH)
    rows.sort(key=lambda r: (order.index(r["tech"]), r["kind"] != "stage", r["date"]))
    out = ["| Technology | ID | Date | Claimant | Kind | Level | Source |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows:
        who = re.sub(r"\s+", " ", r["claimant"].replace("|", "/")).strip().replace("; ", ", and ").replace(": ", ", ")
        sid = SAME_DOC.get(r["source_id"], r["source_id"])
        lvl = r["level"] + (f" (or {r['alt_level']})" if r["alt_level"].strip() else "")
        out.append(f"| {TECH[r['tech']]} | {r['claim_id']} | {r['date']} | {who} | {r['kind']} | {lvl} | ([[{sid}]]) |")
    return "\n".join(out)


def main() -> None:
    body = render((HERE / "body.md").read_text(encoding="utf-8")).replace("{{SITE_URL}}", SITE_URL).replace("{{CODE_URL}}", CODE_URL)
    app = render((HERE / "appendix.md").read_text(encoding="utf-8").replace("{{CLAIMS_TABLE}}", claims_table()).replace("{{TABLE_SCORES}}", (HERE / "table_scores.md").read_text(encoding="utf-8"))).replace("{{SITE_URL}}", SITE_URL).replace("{{CODE_URL}}", CODE_URL)
    entries = sorted(((R[k][1], k) for k in USED), key=lambda e: re.sub(r"[^a-z0-9 ]", "", e[0].lower()))
    ref = ["## References", "",
           "Ledger identifiers in square brackets (S01 to S218) link each entry to the project's source ledger and dataset.", ""]
    for e, k in entries:
        ref.append(e + (f" [{k}]" if k.startswith("S") else ""))
        ref.append("")
    title = ("---\ntitle: \"Beyond the Hype Cycle: A Techno-Economic Value Chain Framework for AI Networking and "
             "Interconnect Hardware, 2025 to 2030\"\nsubtitle: \"Live Project Report\"\nauthor: \"Sushant Gaurav\"\n"
             "date: \"12 November 2026\"\n---\n\n"
             "BPGP 2025-27, Indian Institute of Management Ahmedabad. Area: Information Systems. "
             "Evidence as of 11 November 2026; evidence audit of 12 November 2026.\n\n")
    full = title + body + "\n\n" + "\n".join(ref) + "\n" + app
    (HERE / "Beyond_the_Hype_Cycle_Report.md").write_text(full, encoding="utf-8")
    nb = words(body)
    nb_notables = words("\n".join(l for l in body.split("\n") if not l.startswith("|")))
    stats = dict(body_words_incl_tables=nb, body_words_excl_tables=nb_notables, references=len(entries),
                 academic=sum(1 for _, k in entries if not k.startswith("S")) )
    print(json.dumps(stats))
    (HERE / "stats.json").write_text(json.dumps(stats))
    for sec in re.split(r"\n(?=## )", body):
        print(f"  {sec.splitlines()[0][:40]:40} {words(sec)}")
    subprocess.run(["pandoc", str(HERE / "Beyond_the_Hype_Cycle_Report.md"), "-o", str(HERE / "raw.docx"),
                    "--resource-path", str(HERE), "--from", "markdown+pipe_tables+implicit_figures+autolink_bare_uris"], check=True)


if __name__ == "__main__":
    main()
