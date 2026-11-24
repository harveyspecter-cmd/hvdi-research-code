"""Add click-to-reveal (fade) builds to the content diagrams of a built deck.

Cards (named shapes) reveal together with the text inside them; charts, tables, pictures and
stand-alone text reveal on their own. Titles, breadcrumbs, footers and slide numbers never animate.
The framework slices (fw1..fw6) reveal in their numbered order."""
import re, sys, zipfile, shutil, os

EMU = 914400


def shapes(xml):
    out = []
    for m in re.finditer(r'<p:(sp|pic|graphicFrame|cxnSp)>(.*?)</p:\1>', xml, re.S):
        body = m.group(2)
        idm = re.search(r'<p:cNvPr id="(\d+)" name="([^"]*)"', body)
        geo = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"\s*/>\s*<a:ext cx="(\d+)" cy="(\d+)"', body)
        if not idm or not geo: continue
        x, y, w, h = (int(v) / EMU for v in geo.groups())
        out.append(dict(kind=m.group(1), id=idm.group(1), name=idm.group(2), x=x, y=y, w=w, h=h, ph='<p:ph' in body))
    return out


def groups(sh):
    keep = [s for s in sh if not s['ph'] and s['name'] not in ('Text 0', 'chapter-tracker') and s['y'] < 6.8 and not s['name'].startswith('Slide Number')]
    fw = sorted([s for s in keep if re.fullmatch(r'fw\d+b?', s['name'])], key=lambda s: s['name'])
    if fw:
        order = {}
        for s in fw: order.setdefault(re.match(r'fw(\d+)', s['name']).group(1), []).append(s['id'])
        return [order[k] for k in sorted(order, key=int)]
    cards = [s for s in keep if s['kind'] == 'sp' and not s['name'].startswith('Text ') and s['w'] > 1.0 and s['h'] > 0.8]
    used, G = set(), []
    for c in cards:
        g = [c['id']]; used.add(c['id'])
        for s in keep:
            if s['id'] in used: continue
            cx, cy = s['x'] + s['w'] / 2, s['y'] + s['h'] / 2
            if c['x'] <= cx <= c['x'] + c['w'] and c['y'] <= cy <= c['y'] + c['h']:
                g.append(s['id']); used.add(s['id'])
        G.append((c['y'], c['x'], g))
    for s in keep:
        if s['id'] not in used: G.append((s['y'], s['x'], [s['id']]))
    G.sort(key=lambda t: (round(t[0] / 0.6), t[1]))
    return [g for _, _, g in G]


def timing(G):
    n = [2]
    def nid():
        n[0] += 1; return n[0]
    pars = []
    for g in G:
        eff = []
        for i, sid in enumerate(g):
            a, b, c = nid(), nid(), nid()
            eff.append(f'<p:par><p:cTn id="{a}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" nodeType="{"clickEffect" if i == 0 else "withEffect"}"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                       f'<p:set><p:cBhvr><p:cTn id="{b}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{sid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
                       f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{c}" dur="400"/><p:tgtEl><p:spTgt spid="{sid}"/></p:tgtEl></p:cBhvr></p:animEffect></p:childTnLst></p:cTn></p:par>')
        o, i2 = nid(), nid()
        pars.append(f'<p:par><p:cTn id="{o}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst><p:par><p:cTn id="{i2}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{"".join(eff)}</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    return ('<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
            '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>' + ''.join(pars) +
            '</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
            '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')


def main(path, first=2):
    tmp = path + '.tmp'
    zin = zipfile.ZipFile(path); zout = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
    report = []
    for item in zin.infolist():
        data = zin.read(item.filename)
        m = re.fullmatch(r'ppt/slides/slide(\d+)\.xml', item.filename)
        if m and int(m.group(1)) >= first:
            x = data.decode('utf8'); x = re.sub(r'<p:timing>.*?</p:timing>', '', x, flags=re.S)
            G = groups(shapes(x))
            if G:
                t = timing(G)
                x = x.replace('</p:clrMapOvr>', '</p:clrMapOvr>' + t, 1) if '</p:clrMapOvr>' in x else x.replace('</p:cSld>', '</p:cSld>' + t, 1)
                report.append((int(m.group(1)), len(G)))
            data = x.encode('utf8')
        zout.writestr(item, data)
    zout.close(); shutil.move(tmp, path)
    print(path, 'clicks per slide', sorted(report))


if __name__ == '__main__':
    for p in sys.argv[1:]: main(p)
