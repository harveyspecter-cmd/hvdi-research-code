"""Put the supplied cover page, unchanged, in front of the formatted report, in its own section with no footer."""
import copy, pathlib, sys
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docxcompose.composer import Composer

HERE = pathlib.Path(__file__).resolve().parent
TITLE_STYLES = {"Title", "Subtitle", "Author", "Date"}


def freeze_cover(cov):
    """Write the cover's own Normal-style defaults onto each paragraph so the host styles cannot change it."""
    for p in cov.paragraphs:
        pPr = p._p.get_or_add_pPr()
        sp = pPr.find(qn("w:spacing"))
        if sp is None:
            sp = OxmlElement("w:spacing"); pPr.append(sp)
        for k, v in (("w:after", "200"), ("w:line", "276"), ("w:lineRule", "auto")):
            if sp.get(qn(k)) is None: sp.set(qn(k), v)
        targets = [r._r for r in p.runs]
        for rr in targets:
            rPr = rr.get_or_add_rPr()
            f = rPr.find(qn("w:rFonts"))
            if f is None:
                f = OxmlElement("w:rFonts"); rPr.insert(0, f)
            for k in ("w:ascii", "w:hAnsi"):
                if f.get(qn(k)) is None: f.set(qn(k), "Calibri")
            if rPr.find(qn("w:sz")) is None:
                z = OxmlElement("w:sz"); z.set(qn("w:val"), "22"); rPr.append(z)


def main(report="Beyond_the_Hype_Cycle_Report.docx", cover="Live_Project_Cover_Page.docx", out="Beyond_the_Hype_Cycle_Report.docx"):
    rep = Document(HERE / report)
    body = rep.element.body
    # drop the generated title block and the empty paragraphs before the first heading
    for p in list(rep.paragraphs):
        if p.style.name.startswith("Heading"): break
        p._p.getparent().remove(p._p)
    cov = Document(HERE / cover)
    freeze_cover(cov)
    n = len(cov.element.body.findall(qn("w:p")))
    comp = Composer(rep)
    comp.insert(0, cov)
    d = comp.doc
    paras = d.element.body.findall(qn("w:p"))
    last = paras[n - 1]
    # cover section: copy the cover's page setup, no header or footer
    sect = copy.deepcopy(cov.element.body.find(qn("w:sectPr")))
    for ref in sect.findall(qn("w:footerReference")) + sect.findall(qn("w:headerReference")):
        sect.remove(ref)
    pPr = last.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr"); last.insert(0, pPr)
    pPr.append(sect)
    # report section: pages numbered from 1
    final = d.element.body.find(qn("w:sectPr"))
    pg = final.find(qn("w:pgNumType"))
    if pg is None:
        pg = OxmlElement("w:pgNumType"); final.append(pg)
    pg.set(qn("w:start"), "1")
    comp.save(str(HERE / out))
    print("cover merged", n, "paragraphs")


if __name__ == "__main__":
    main(*sys.argv[1:])
