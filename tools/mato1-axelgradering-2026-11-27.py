"""Felrapport 2026-11-27 08:09, Ma3c 1.904 (lärare: ”Graderingen på axlarna ska sitta jämte axeln”).

Graferna från Ma3c-generatorn (`clip-ma3-…`, ram 60–430 × 42–280) ritade talen vid ramens vänster- och nederkant,
fast koordinataxlarna gick genom origo inne i rutan. Skriptet gör om de figurer där minst en koordinataxel ligger
inne i rutan:
- ramlinjen tas bort på den sida där en egen axel finns, och den egna axeln får en pilspets;
- x-talen står under x-axeln och y-talen till vänster om y-axeln, med en vit kant så att de syns över kurvor;
- nollan skrivs en gång vid origo (står y-axeln i ramens vänsterkant står den kvar bland y-talen);
- axelnamnen står vid axlarnas ändar.
Kurvor, punkter, etiketter och rutnät är oförändrade. Talen och axelnamnen ritas sist, ovanpå kurvorna, och den
tomma ytan under diagrammet tas bort. Stapeldiagrammet 1.895 ändras inte (kategorierna hör hemma under staplarna),
och 3.1204 har redan talen vid axlarna.

  python tools/mato1-axelgradering-2026-11-27.py [--skriv]
"""
import json
import os
import re
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgiftermato1.js')
IDS = ['1.865', '1.871', '1.896', '1.904', '1.907', '1.910', '2.1149', '2.1152', '2.1164', '2.1165',
       '2.1166', '2.1169', '2.1173', '3.1195', '3.1197']
X0, X1, Y0, Y1 = 60.0, 430.0, 42.0, 280.0
HALO = ' stroke="white" stroke-width="4" stroke-linejoin="round" paint-order="stroke"'
NAMN = re.compile(r'<text x="[\d.]+" y="[\d.]+" font-family="Arial,sans-serif" font-size="17" text-anchor="(?:start|end)" '
                  r'fill="#243447">([^<]*)</text>')


def tal(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def gor_om(svg, uid):
    hor = [m for m in re.finditer(r'<path d="M60 ([\d.]+)L(?:430|443) \1(?: M435 [\d.]+L443 \1L435 [\d.]+)?" '
                                  r'fill="none" stroke="#243447" stroke-width="2"/>', svg)
           if abs(float(m.group(1)) - Y1) > 0.5]
    ver = [m for m in re.finditer(r'<path d="M([\d.]+) 42L\1 280" fill="none" stroke="#243447" stroke-width="2"/>', svg)
           if abs(float(m.group(1)) - X0) > 0.5]
    assert len(hor) <= 1 and len(ver) <= 1 and (hor or ver), uid
    hor = hor[0] if hor else None
    ver = ver[0] if ver else None
    ay = float(hor.group(1)) if hor else Y1          # x-axelns läge
    ax = float(ver.group(1)) if ver else X0          # y-axelns läge
    ut = svg
    xpil = (f'<path d="M60 {tal(ay)}L443 {tal(ay)} M435 {tal(ay - 4)}L443 {tal(ay)}L435 {tal(ay + 4)}" fill="none" '
            f'stroke="#243447" stroke-width="2"/>')
    ypil = (f'<path d="M{tal(ax)} 280L{tal(ax)} 32 M{tal(ax - 4)} 40L{tal(ax)} 32L{tal(ax + 4)} 40" fill="none" '
            f'stroke="#243447" stroke-width="2"/>')
    ram_x = '<path d="M60 280L443 280" fill="none" stroke="#243447" stroke-width="2"/>'
    ram_y = '<path d="M60 280L60 32" fill="none" stroke="#243447" stroke-width="2"/>'
    # x-axeln: den egna axeln får pil och ramlinjen tas bort, annars blir ramlinjen axel med pil
    if hor:
        ut = ut.replace(ram_x, '').replace(hor.group(0), xpil)
    else:
        assert ut.count(ram_x) == 1, uid
        ut = ut.replace(ram_x, xpil)
    if ver:
        ut = ut.replace(ram_y, '').replace(ver.group(0), ypil)
    else:
        assert ut.count(ram_y) == 1, uid
        ut = ut.replace(ram_y, ypil)
    nolla = False
    etiketter = []

    def xtal(m):
        nonlocal nolla
        x, txt = float(m.group(1)), m.group(2)
        if txt == '0' and abs(x - ax) < 0.5:
            nolla = True
        else:
            etiketter.append(f'<text x="{tal(x)}" y="{tal(ay + 21)}" font-family="Arial,sans-serif" font-size="16" '
                             f'text-anchor="middle" fill="#243447"{HALO}>{txt}</text>')
        return ''

    def ytal(m):
        nonlocal nolla
        y, txt = float(m.group(1)), m.group(2)
        if txt == '0' and abs(y - 5 - ay) < 0.5 and ver:
            nolla = True
        else:
            etiketter.append(f'<text x="{tal(ax - 8)}" y="{tal(y)}" font-family="Arial,sans-serif" font-size="16" '
                             f'text-anchor="end" fill="#243447"{HALO}>{txt}</text>')
        return ''

    ut, nx = re.subn(r'<text x="([\d.]+)" y="302" font-family="Arial,sans-serif" font-size="16" text-anchor="middle" '
                     r'fill="#243447">([^<]*)</text>', xtal, ut)
    ut, ny_ = re.subn(r'<text x="49" y="([\d.]+)" font-family="Arial,sans-serif" font-size="16" text-anchor="end" '
                      r'fill="#243447">([^<]*)</text>', ytal, ut)
    assert nx >= 2 and ny_ >= 2 and nolla, uid
    # Med en egen y-axel skrivs nollan nedanför till vänster om origo. Ligger y-axeln i ramens vänsterkant står
    # nollan kvar i y-talens kolumn, annars krockar den med talet under x-axeln.
    if ver:
        etiketter.append(f'<text x="{tal(ax - 8)}" y="{tal(ay + 21)}" font-family="Arial,sans-serif" font-size="16" '
                         f'text-anchor="end" fill="#243447"{HALO}>0</text>')
    # axelnamn
    namn = list(NAMN.finditer(ut))
    assert len(namn) >= 2, uid
    xn, yn = namn[0], namn[1]
    # kurvetiketter (A, f, g …) till höger om rutan nära x-axelns slut: axelnamnet ställs då under axeln
    upptagen = any(float(x) >= 440 and abs(float(y) - (ay + 6)) < 18
                   for x, y in re.findall(r'<text x="([\d.]+)" y="([\d.]+)"', ut))
    if len(xn.group(1)) <= 2 and upptagen:
        xny = (f'<text x="446" y="{tal(ay + 24)}" font-family="Arial,sans-serif" font-size="17" text-anchor="start" '
               f'fill="#243447">{xn.group(1)}</text>')
    elif len(xn.group(1)) <= 2:
        xny = (f'<text x="448" y="{tal(ay + 6)}" font-family="Arial,sans-serif" font-size="17" text-anchor="start" '
               f'fill="#243447">{xn.group(1)}</text>')
    else:
        xny = (f'<text x="438" y="{tal(ay - 10)}" font-family="Arial,sans-serif" font-size="17" text-anchor="end" '
               f'fill="#243447"{HALO}>{xn.group(1)}</text>')
    yny = (f'<text x="{tal(ax + 10)}" y="30" font-family="Arial,sans-serif" font-size="17" text-anchor="start" '
           f'fill="#243447">{yn.group(1)}</text>')
    ut = ut.replace(xn.group(0), '', 1).replace(yn.group(0), '', 1)
    # talen och axelnamnen ritas sist, ovanpå kurvorna
    ut = ut.replace('</svg>', ''.join(etiketter) + xny + yny + '</svg>')
    # tom yta under diagrammet bort när inget annat ligger där
    lagst = max([float(v) for v in re.findall(r'<text x="[\d.]+" y="([\d.]+)"', ut)] +
                [float(v) for v in re.findall(r'cy="([\d.]+)"', ut)])
    if 'viewBox="0 0 480 345"' in ut and lagst < 306:
        ut = ut.replace('viewBox="0 0 480 345"', 'viewBox="0 0 480 312"').replace(
            '<rect width="480" height="345" fill="white"/>', '<rect width="480" height="312" fill="white"/>')
    return ut


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    ny = src
    figurer = {}
    for q in bank:
        if q['id'] not in IDS:
            continue
        svgs = re.findall(r'<svg[\s\S]*?</svg>', q['t'])
        assert len(svgs) == 1, q['id']
        gammal = svgs[0]
        nysvg = gor_om(gammal, q['id'])
        figurer[q['id']] = (gammal, nysvg)
        a = json.dumps(gammal, ensure_ascii=False)[1:-1]
        b = json.dumps(nysvg, ensure_ascii=False)[1:-1]
        assert ny.count(a) == 1, q['id']
        ny = ny.replace(a, b)
    assert set(figurer) == set(IDS), set(IDS) - set(figurer)
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [(x['id'], sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))) for x, y in zip(efter, bank) if x != y]
    assert sorted(i for i, _ in andr) == sorted(IDS) and all(k == ['t'] for _, k in andr), andr
    if '--visa' in sys.argv:
        ut = sys.argv[sys.argv.index('--visa') + 1]
        os.makedirs(ut, exist_ok=True)
        for uid, (g, n) in figurer.items():
            open(os.path.join(ut, f'{uid}-fore.svg'), 'w', encoding='utf-8').write(g)
            open(os.path.join(ut, f'{uid}-efter.svg'), 'w', encoding='utf-8').write(n)
    print(len(andr), 'figurer')
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
