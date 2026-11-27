"""Kvalitetsrapporten 2026-11-27, omgång 2: figuretiketter som en linje eller cirkel går igenom.

Kunskapsgymmets kvalitetsgranskning (med förbättrad krockkontroll, se agent/KVALITETSRAPPORT_2026-11-27.md) flaggade
etiketter som står på en linje eller cirkel: hastighet längs en kastbana, mått på måttlinjer, r₂ på en streckad sträcka,
−1 på enhetscirkeln, mängdnamn på Venndiagrammens cirklar, gradtal på asymptoter och liknande. Placeringen är oftast
avsiktlig, men linjen går genom texten. Varje figur har granskats visuellt.

1. Etiketterna i `svg-etikettkant-2026-11-27.json` (119 uppgifter, 172 etiketter) får en vit kant:
   stroke="#fff", stroke-width ≈ 0,22 · textstorleken (minst 2,5), stroke-linejoin="round" och paint-order="stroke".
   Linjen bryts då bakom texten, och ingenting flyttas. På vit bakgrund syns kanten inte.
2. Sex etiketter flyttas, eftersom en vit kant inte räcker:
   - Ma1 2.56, 2.58 och Ma2 2.210, 2.413: funktionsetiketten ”f” stod där kurvan korsar x-axeln. Den flyttas till
     kurvans övre högra gren.
   - Ma3c 3.501: ”2x+1” låg på gränsetiketten ”3” överst. Den flyttas upp till vänster om linjen.
   - Ma4 4.589: punktetiketten ”−3” låg på axelns tal ”−3”. Den flyttas rakt upp ovanför punkten.

  python tools/svg-etikettkant-2026-11-27.py [--skriv]
"""
import html
import json
import os
import re
import sys

ROT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
LISTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg-etikettkant-2026-11-27.json')
TEXT = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)


def innehall(inre):
    return html.unescape(re.sub(r'<[^>]+>', '', inre)).strip()


def med_kant(attr):
    if re.search(r'\sstroke=', attr) or 'paint-order' in attr:
        return None
    m = re.search(r'font-size="([\d.]+)', attr) or re.search(r'font-size:\s*([\d.]+)', attr)
    fs = float(m.group(1)) if m else 16.0
    w = max(2.5, round(0.22 * fs, 1))
    return attr + f' stroke="#fff" stroke-width="{w:g}" stroke-linejoin="round" paint-order="stroke"'


def kanta_svg(svg, etiketter):
    traff = set()

    def byt(m):
        txt = innehall(m.group(2))
        if not any(txt == e or (len(e) == 24 and txt.startswith(e)) for e in etiketter):
            return m.group(0)
        ny = med_kant(m.group(1))
        if ny is None:
            return m.group(0)
        traff.add(txt[:24])
        return f'<text{ny}>{m.group(2)}</text>'
    return TEXT.sub(byt, svg), traff


def kurvpunkt(svg, farg, andel):
    """Punkt på kurvan (path med given stroke-färg) vid andel av x-intervallet."""
    for m in re.finditer(r'<path\b[^>]*>', svg):
        p = m.group(0)
        if farg.lower() not in p.lower():
            continue
        d = re.search(r'\sd="([^"]+)"', p).group(1)
        pts = [(float(a), float(b)) for a, b in re.findall(r'([-\d.]+)[ ,]([-\d.]+)', d)]
        if len(pts) < 20:
            continue
        x0, x1 = pts[0][0], pts[-1][0]
        mal = x0 + andel * (x1 - x0)
        return min(pts, key=lambda q: abs(q[0] - mal))
    raise ValueError('kurvan hittades inte')


def flytta_f(svg):
    m = re.search(r'<text([^>]*)x="391.60" y="(192.67|207.86)"([^>]*)>f</text>', svg)
    assert m, 'f-etiketten saknas'
    px, py = kurvpunkt(svg, '#2F6FAE', 0.9)
    ny = f'<text{m.group(1)}x="{px - 10:.2f}" y="{py + 4:.2f}" text-anchor="end"{m.group(3)}>f</text>'
    return svg.replace(m.group(0), ny)


FLYTT = {
    ('uppgifterma1.js', '2.56'): flytta_f,
    ('uppgifterma1.js', '2.58'): flytta_f,
    ('uppgifterma2.js', '2.210'): flytta_f,
    ('uppgifterma2.js', '2.413'): flytta_f,
    ('uppgiftermato1.js', '3.501'): lambda s: s.replace(
        '<text x="361" y="37" text-anchor="end" font-size="14.08" fill="#2D70B3">2x+1</text>',
        '<text x="250" y="62" text-anchor="end" font-size="14.08" fill="#2D70B3">2x+1</text>'),
    ('uppgiftermato2.js', '4.589'): lambda s: s.replace(
        '<text x="154.7" y="158.0" font-family="Arial,sans-serif" font-size="15" font-weight="bold" fill="#172b3a">−3</text>',
        '<text x="164.7" y="128.0" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" font-weight="bold" fill="#172b3a">−3</text>'),
}


def strangar(v, ut):
    if isinstance(v, str):
        ut.append(v)
    elif isinstance(v, list):
        for x in v:
            strangar(x, ut)
    elif isinstance(v, dict):
        for x in v.values():
            strangar(x, ut)
    return ut


def main():
    lista = json.load(open(LISTA, encoding='utf-8'))
    per_bank = {}
    for x in lista:
        per_bank.setdefault(x['bank'], {})[x['id']] = x['etiketter']
    for b, i in FLYTT:
        per_bank.setdefault(b, {})
    totalt = 0
    for bank, mal in sorted(per_bank.items()):
        fil = os.path.join(ROT, bank)
        src = open(fil, encoding='utf-8', newline='').read()
        data = json.loads(src[src.index('['):src.rindex(']') + 1])
        idx = {str(q['id']): q for q in data}
        byten = {}
        for uid, etiketter in mal.items():
            q = idx[uid]
            svgs = {s for t in strangar(q, []) for s in re.findall(r'<svg[\s\S]*?</svg>', t)}
            hittade = set()
            for s in svgs:
                ny, traff = kanta_svg(s, etiketter)
                hittade |= traff
                if ny != s:
                    byten[s] = ny
            saknas = [e for e in etiketter if not any(h == e or h.startswith(e) for h in hittade)]
            if saknas:
                print('  inte kantade (har redan kant eller annan form):', bank, uid, saknas)
        for (b, uid), fn in FLYTT.items():
            if b != bank:
                continue
            q = idx[uid]
            svgs = {s for t in strangar(q, []) for s in re.findall(r'<svg[\s\S]*?</svg>', t)}
            for s in svgs:
                bas = byten.get(s, s)
                ny = fn(bas)
                assert ny != bas, (bank, uid)
                byten[s] = ny
        ny_src = src
        for gl, ny in byten.items():
            a = json.dumps(gl, ensure_ascii=False)[1:-1]
            n = ny_src.count(a)
            assert n >= 1, gl[:80]
            ny_src = ny_src.replace(a, json.dumps(ny, ensure_ascii=False)[1:-1])
        efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        andrade = [x['id'] for x, y in zip(efter, data) if x != y]
        tillatna = set(mal) | {i for b, i in FLYTT if b == bank}
        assert set(map(str, andrade)) <= tillatna, set(map(str, andrade)) - tillatna
        print(bank, 'figurer', len(byten), 'uppgifter', len(andrade))
        totalt += len(byten)
        if '--skriv' in sys.argv:
            with open(fil, 'w', encoding='utf-8', newline='') as fh:
                fh.write(ny_src)
    print('totalt figurer', totalt)


if __name__ == '__main__':
    main()
