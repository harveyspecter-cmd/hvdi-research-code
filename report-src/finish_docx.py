"""Apply report formatting to the pandoc output: fonts, spacing, tables, hanging references, page numbers."""
import pathlib
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HERE = pathlib.Path(__file__).resolve().parent
FONT = "Times New Roman"
BLACK = RGBColor(0, 0, 0)


def set_font(run, size=None, bold=None, italic=None):
    run.font.name = FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    run.font.color.rgb = BLACK
    if size: run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic


def borders(table):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for edge, sz in (("top", "8"), ("bottom", "8"), ("insideH", "4")):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), sz); e.set(qn("w:space"), "0"); e.set(qn("w:color"), "000000")
        b.append(e)
    tblPr.append(b)


def page_number(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), tag); r._r.append(f)
        else:
            i = OxmlElement("w:instrText"); i.set(qn("xml:space"), "preserve"); i.text = text; r._r.append(i)
    set_font(r, 10)


def main(src="raw.docx", out="Beyond_the_Hype_Cycle_Report.docx"):
    d = Document(HERE / src)
    for s in d.sections:
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(1)
        page_number(s)
    for st in d.styles:
        try:
            if st.font is not None:
                st.font.name = FONT; st.font.color.rgb = BLACK
        except (AttributeError, ValueError):
            pass
    in_refs = False
    first_h = True
    for p in d.paragraphs:
        name = p.style.name
        txt = p.text.strip()
        if name.startswith("Heading"):
            lvl = int(name.split()[-1]) if name.split()[-1].isdigit() else 1
            in_refs = txt == "References"
            if lvl <= 2 and (first_h or txt in ("References", "Appendices", "1. Introduction")):
                p.insert_paragraph_before().add_run().add_break(WD_BREAK.PAGE)
            first_h = False
            for r in p.runs: set_font(r, {1: 14, 2: 13}.get(lvl, 12), bold=True, italic=False)
            p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            continue
        if name in ("Title", "Subtitle", "Author", "Date"):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs: set_font(r, 18 if name == "Title" else 13, bold=(name == "Title"))
            if name == "Title": p.paragraph_format.space_before = Pt(120)
            continue
        for r in p.runs: set_font(r, 12)
        pf = p.paragraph_format
        if txt.startswith("BPGP 2025-27, Indian Institute"):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pf.line_spacing = 1.5; pf.space_after = Pt(6)
        if in_refs and txt and not txt.startswith("Ledger identifiers"):
            pf.left_indent = Inches(0.5); pf.first_line_indent = Inches(-0.5); pf.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if name in ("Image Caption", "Captioned Figure", "Table Caption"):
            for r in p.runs: set_font(r, 10, italic=True)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for t in d.tables:
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        borders(t)
        for ri, row in enumerate(t.rows):
            for c in row.cells:
                for p in c.paragraphs:
                    p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_after = Pt(2)
                    for r in p.runs: set_font(r, 9, bold=(ri == 0) or None)
    for shp in d.inline_shapes:
        if shp.width > Inches(6.3):
            ratio = shp.height / shp.width; shp.width = Inches(6.3); shp.height = int(Inches(6.3) * ratio)
    d.save(HERE / out)
    print("saved", out)


if __name__ == "__main__":
    main(*sys.argv[1:])
