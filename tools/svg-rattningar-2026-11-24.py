"""Figurrättningar efter SVG-granskningen 2026-11-24 (agent/SVG_UTSEENDE_2026-11-24.md).

1. Gemena attribut: ”viewbox” → ”viewBox”, ”preserveaspectratio” → ”preserveAspectRatio”, ”markerwidth” →
   ”markerWidth”, ”refx” → ”refX” osv. (Fy2, Ma1, Ma3c, Ma4). Attributen hade skrivits om av en HTML-tolkare. Webbläsaren rättar dem när figuren står direkt i HTML, men
   inte när figuren tolkas som XML (granskningsverktyget, export), där hela innehållet då hamnar utanför bilden.
2. Fy1 9.434: ett tidigare skript hade bytt bindestreck mot typografiskt minus inne i SVG-attribut
   (dy="−6" font−size="10"), så exponenten i 10⁻¹⁰ visades som ”10−10” i full storlek.
3. Ma3c 1.911 (facit): ”<” i figurens titel och etikett skrivs &lt;, så att figuren är giltig XML.
4. Ma5 4.84 och 4.109: riktningsfältet ritades till y = −1 och x-axelns tal under bildens nedre kant (y ≈ 305–352
   i en ram som slutar på 310), medan de översta 50 enheterna var tomma. Ramen flyttas till y = 45–363.
   Ma5 4.110 har y-axeln högre upp (innehåll i y = −1…312) och får ramen y = −6…316.

Bara strängliteralerna byts, och skriptet kontrollerar att inget annat än figurerna ändras.

  python tools/svg-rattningar-2026-11-24.py [--skriv]
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BANKER = ['uppgifter.js', 'uppgifter2.js', 'uppgifterma1.js', 'uppgifterma2.js', 'uppgiftermato1.js',
          'uppgiftermato2.js', 'uppgiftermatf1.js', 'uppgifterai.js']
SVG = re.compile(r'<svg[\s\S]*?</svg>')
RAM_GL = ('width="460" height="310" viewBox="0 0 460 310"', '<rect width="460" height="310" fill="white"/>')
RAM_NY = ('width="460" height="318" viewBox="0 45 460 318"', '<rect x="0" y="45" width="460" height="318" fill="white"/>')
RAM_4110 = ('width="460" height="322" viewBox="0 -6 460 322"', '<rect x="0" y="-6" width="460" height="322" fill="white"/>')


KAMEL = ['viewBox', 'preserveAspectRatio', 'markerWidth', 'markerHeight', 'markerUnits', 'refX', 'refY', 'gradientUnits',
         'gradientTransform', 'patternUnits', 'patternContentUnits', 'patternTransform', 'textLength', 'lengthAdjust',
         'stdDeviation', 'clipPathUnits', 'startOffset', 'maskUnits', 'maskContentUnits', 'spreadMethod', 'pathLength']
KAMEL_RX = re.compile(r'(\s)(' + '|'.join(k.lower() for k in KAMEL) + r')(?==)')
KAMEL_MAP = {k.lower(): k for k in KAMEL}


def ratta_svg(svg, fil):
    # gemena SVG-attribut i alla element (bara inne i taggar)
    ny = re.sub(r'<[a-zA-Z][^<>]*>', lambda t: KAMEL_RX.sub(lambda m: m.group(1) + KAMEL_MAP[m.group(2)], t.group(0)), svg)
    if fil == 'uppgifter.js' and 'font−size' in ny:
        ny = ny.replace('font−size=', 'font-size=')
        ny = re.sub(r'dy=(\\?")−', r'dy=\1-', ny)
    if fil == 'uppgiftermato1.js' and 'Volymen V(x) = x(20 − 2x)(16 − 2x) för 0 < x < 8' in ny:
        ny = ny.replace('för 0 < x < 8', 'för 0 &lt; x &lt; 8')
    if fil == 'uppgiftermatf1.js' and 'Riktningsfält till y-prim' in ny:
        # 4.110 (y' = x − y) har y-axeln högre upp: innehållet ligger i y = −1…312, inte 50…352.
        mal = RAM_4110 if 'y-prim lika med x minus y' in ny else RAM_NY
        for esc in ('"', '\\"'):   # figurerna står ibland JSON-kodade (\")
            for kalla in (RAM_GL, RAM_NY):
                gl = [x.replace('"', esc) for x in kalla]
                if gl[0] in ny and kalla != mal:
                    assert ny.count(gl[0]) == 1 and ny.count(gl[1]) == 1
                    nya = [x.replace('"', esc) for x in mal]
                    ny = ny.replace(gl[0], nya[0]).replace(gl[1], nya[1])
    return ny


def main():
    for fil in BANKER:
        path = os.path.join(ROOT, fil)
        src = open(path, encoding='utf-8', newline='').read()
        fore = json.loads(src[src.index('['):src.rindex(']') + 1])
        n = 0

        def ers(m):
            nonlocal n
            ny = ratta_svg(m.group(0), fil)
            if ny != m.group(0):
                n += 1
            return ny
        ny_src = SVG.sub(ers, src)
        efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        andr = []
        for a, b in zip(fore, efter):
            if a != b:
                andr.append(a['id'])
                # utanför figurerna är allt oförändrat
                ta = SVG.sub('', json.dumps(a, ensure_ascii=False))
                tb = SVG.sub('', json.dumps(b, ensure_ascii=False))
                assert ta == tb, a['id']
        print(fil, n, 'figurförekomster i', len(andr), 'uppgifter', andr[:8] if len(andr) < 9 else '')
        if '--skriv' in sys.argv:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(ny_src)


if __name__ == '__main__':
    main()
