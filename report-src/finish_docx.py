"""Apply report formatting to the pandoc output: fonts, spacing, tables, hanging references, page numbers."""
import pathlib
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor

HERE = pathlib.Path(__file__).resolve().parent
FONT = "Times New Roman"
BLACK = RGBColor(0, 0, 0)
BLUE = RGBColor(0x1F, 0x4E, 0x79)


def set_font(run, size=None, bold=None, italic=None, color=BLACK):
    run.font.name = FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    run.font.color.rgb = color
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
    ft = section.footer
    ft.is_linked_to_previous = False
    p = ft.paragraphs[0]
    for old in list(p.runs): old._r.getparent().remove(old._r)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    lead = p.add_run("Beyond the Hype Cycle  |  Sushant Gaurav  |  IIMA BPGP 2025-27 Live Project  |  Page ")
    set_font(lead, 9)
    for kind, val in (("begin", None), ("instr", " PAGE "), ("separate", None), ("text", "1"), ("end", None)):
        r = p.add_run()
        if kind == "instr":
            e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = val; r._r.append(e)
        elif kind == "text":
            r.text = val
        else:
            e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), kind); r._r.append(e)
        set_font(r, 9)


def main(src="raw.docx", out="Beyond_the_Hype_Cycle_Report.docx"):
    d = Document(HERE / src)
    for s in d.sections:
        s.page_width = Cm(21.0); s.page_height = Cm(29.7)
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.54)
        page_number(s)
    for st in d.styles:
        try:
            if st.font is not None:
                st.font.name = FONT; st.font.color.rgb = BLACK
        except (AttributeError, ValueError):
            pass
    for nm, sz in (("Heading 1", 14), ("Heading 2", 14), ("Heading 3", 13), ("Heading 4", 12)):
        try:
            st = d.styles[nm]; st.font.size = Pt(sz); st.font.color.rgb = BLUE; st.font.bold = True
        except KeyError:
            pass
    try:
        d.styles["Footer"].font.size = Pt(9)
    except KeyError:
        pass
    in_refs = False
    first_h = True
    for p in d.paragraphs:
        name = p.style.name
        txt = p.text.strip()
        if name.startswith("Heading"):
            lvl = int(name.split()[-1]) if name.split()[-1].isdigit() else 1
            in_refs = txt == "References"
            if lvl <= 2 and (not first_h) and txt in ("References", "Appendices", "1. Introduction", "Executive Summary"):
                p.insert_paragraph_before().add_run().add_break(WD_BREAK.PAGE)
            first_h = False
            for r in p.runs: set_font(r, {1: 14, 2: 14, 3: 13}.get(lvl, 12), bold=True, italic=False, color=BLUE)
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
        pf.line_spacing = 1.15; pf.space_after = Pt(6)
        if name not in ("Image Caption", "Captioned Figure", "Table Caption") and not txt.startswith("BPGP 2025-27, Indian Institute"):
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if in_refs and txt and not txt.startswith("Ledger identifiers"):
            pf.left_indent = Inches(0.5); pf.first_line_indent = Inches(-0.5); pf.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if name in ("Image Caption", "Captioned Figure", "Table Caption"):
            for r in p.runs: set_font(r, 10, italic=True)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for t in d.tables:
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        borders(t)
        if len(t.columns) >= 10:  # the score table: wide first column, narrow score columns
            widths = [1.65] + [0.36] * 5 + [0.5, 0.55, 0.85, 0.7, 0.7][: len(t.columns) - 6]
            t.autofit = False
            tblPr = t._tbl.tblPr
            for tag in ("w:tblW", "w:tblLayout"):
                for old in tblPr.findall(qn(tag)):
                    tblPr.remove(old)
            tw = OxmlElement("w:tblW"); tw.set(qn("w:w"), str(int(sum(widths) * 1440))); tw.set(qn("w:type"), "dxa"); tblPr.append(tw)
            lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
            for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), widths):
                gc.set(qn("w:w"), str(int(w * 1440)))
            for row in t.rows:
                for cell, w in zip(row.cells, widths):
                    cell.width = Inches(w)
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
