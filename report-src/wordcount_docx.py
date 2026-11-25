"""Word-style count of the report body (Executive Summary to the end of Section 6), as Word shows it."""
import re, sys, docx
def count(path):
    d = docx.Document(path); on = False; done = False; c = dict(prose=0, captions=0, tables=0, headings=0)
    for el in d.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, d); t = p.text.strip(); st = p.style.name
            if st.startswith('Heading') and not on and not done: on = True
            if st.startswith('Heading') and t == 'References': on = False; done = True
            if not on or not t: continue
            k = 'headings' if st.startswith('Heading') else 'captions' if re.match(r'^(Figure|Table) \d+\.', t) else 'prose'
            c[k] += len(t.split())
        elif tag == 'tbl' and on:
            c['tables'] += sum(len(x.text.split()) for r in docx.table.Table(el, d).rows for x in r.cells)
    c['total'] = sum(c.values()); return c
if __name__ == '__main__': print(count(sys.argv[1] if len(sys.argv) > 1 else 'Beyond_the_Hype_Cycle_Report.docx'))
