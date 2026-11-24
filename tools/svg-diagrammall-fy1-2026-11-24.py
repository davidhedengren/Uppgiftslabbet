"""Fy1:s diagrammall med läsbar text i mobil (agent/SVG_UTSEENDE_2026-11-24.md).

67 diagram i Fy1 (v–t, s–t, a–t, F–Δl, m–V …) kommer från samma generator: ritruta x = 54–486, y = 26–246 i en
viewBox som är 500 bred, y-axelns tal högerjusterade vid x = 46, x-axelns tal centrerade under axeln, y-rubriken uppe
till vänster (x = 16, y = 14) och x-rubriken nere till höger (x = 486, y = 282). I ett 320 px brett mobilkort blev
talen 6–8 px. När bara texten förstorades krockade rubrikerna med översta y-talet och sista x-talet.

Här görs layouten om för hela familjen, med samma storlek på alla tal och rubriker:
- y-axelns tal: font-size 16, centrerade mot sin rutnätslinje (baslinje = linjen + 5,6);
- x-axelns tal: font-size 16, baslinje y = 267;
- y-rubriken: font-size 16, baslinje y = 12 (ovanför översta talet);
- x-rubriken: font-size 16, baslinje y = 291 (under sista talet);
- viewBox börjar på y = −8 och slutar 8 under innehållet och breddas när sista x-talet är brett; height följer
  med i samma proportion.
Andra texter (seriernas namn A, B, P …) ändras inte. Koordinaterna för linjer och kurvor ändras aldrig.

  python tools/svg-diagrammall-fy1-2026-11-24.py [--skriv]
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FIL = os.path.join(ROOT, 'uppgifter.js')
SIG = '<rect x="54" y="26" width="432" height="220" fill="#fff"/>'
FS = 16


def attr(tag, namn):
    m = re.search(r'\s' + namn + r'="([^"]*)"', tag)
    return m.group(1) if m else None


def satt(tag, namn, varde):
    if attr(tag, namn) is None:
        return tag.replace('<text', f'<text {namn}="{varde}"', 1)
    return re.sub(r'(\s' + namn + r'=")[^"]*(")', lambda m: m.group(1) + varde + m.group(2), tag, count=1)


def fmt(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')


def gor_om(svg):
    gridy = sorted({float(m) for m in re.findall(r'<line x1="54" y1="([\d.]+)" x2="486" y2="\1"', svg)})
    if not gridy:
        return svg

    def text(m):
        tag, inne = m.group(1), m.group(2)
        vikt, ank = attr(tag, 'font-weight'), attr(tag, 'text-anchor')
        x, y = float(attr(tag, 'x') or 0), float(attr(tag, 'y') or 0)
        ren = inne.strip()
        if vikt == '400' and ank == 'end' and abs(x - 46) < 0.01 and re.fullmatch(r'[−-]?\d+(?:[,.]\d+)?', ren):
            linje = min(gridy, key=lambda g: abs(g - (y - 4)))
            tag = satt(satt(tag, 'font-size', str(FS)), 'y', fmt(linje + 5.6))
        elif vikt == '400' and ank == 'middle' and 255 < y < 275 and re.fullmatch(r'[−-]?\d+(?:[,.]\d+)?', ren):
            tag = satt(satt(tag, 'font-size', str(FS)), 'y', '267')
        elif vikt == '600' and ank == 'start' and abs(x - 16) < 0.01 and y < 20:
            tag = satt(satt(tag, 'font-size', str(FS)), 'y', '12')
        elif vikt == '600' and ank == 'end' and abs(x - 486) < 0.01 and y > 275:
            tag = satt(satt(tag, 'font-size', str(FS)), 'y', '291')
        return tag + inne + '</text>'
    ny = re.sub(r'(<text\b[^>]*>)([^<]*)</text>', text, svg)
    # viewBox: y från −8, nedre kant minst 299 (8 under x-rubriken), bredden oförändrad
    head = re.match(r'<svg\b[^>]*>', ny).group(0)
    vx, vy, vw, vh = [float(v) for v in attr(head, 'viewBox').split()]
    vy2, vh2 = min(vy, -8), max(vy + vh, 299) - min(vy, -8)
    # breda x-tal längst till höger (”0,25”, ”100”) får plats: monospace ≈ 0,6 · font-size per tecken
    for tal in re.findall(r'<text[^>]*x="486" y="267"[^>]*>([^<]*)</text>', ny):
        hoger = 486 + len(tal.strip()) * FS * 0.6 / 2 + 4
        vw = max(vw, hoger - vx)
    h2 = satt(head.replace('<svg', '<text', 1), 'viewBox', f'{fmt(vx)} {fmt(vy2)} {fmt(vw)} {fmt(vh2)}')
    w = attr(head, 'width')
    if w and attr(head, 'height'):
        h2 = satt(h2, 'height', fmt(float(w) * vh2 / vw))
    return ny.replace(head, h2.replace('<text', '<svg', 1), 1)


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    byten = {}
    for q in bank:
        for lit in re.findall(r'<svg[\s\S]*?</svg>', json.dumps(q, ensure_ascii=False)):
            svg = lit.replace('\\"', '"')
            if SIG not in svg or lit in byten:
                continue
            ny = gor_om(svg)
            if ny != svg:
                byten[lit] = ny.replace('"', '\\"')
    ny_src = src
    n = 0
    for g, b in byten.items():
        n += ny_src.count(g)
        ny_src = ny_src.replace(g, b)
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    utan = lambda q: re.sub(r'<svg[\s\S]*?</svg>', '', json.dumps(q, ensure_ascii=False))
    for a, b in zip(bank, efter):
        assert utan(a) == utan(b), a['id']
    print(len(byten), 'figurer,', n, 'förekomster')
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)
    return byten


if __name__ == '__main__':
    main()
