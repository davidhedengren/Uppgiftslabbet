"""Decimalkomma i figurtexter (agent/SVG_UTSEENDE_2026-11-24.md).

Axeltal och mått i några figurer skrevs med decimalpunkt (”0.5”, ”37.5”, ”11.5°”). Svensk text har decimalkomma,
som i resten av uppgifterna. Bytet görs bara i textinnehållet i <text> och <tspan>, inte i attribut.

Står kvar: multimeterns display i Fy1 8.565, 8.628, 8.629, 8.630 och 8.633 (en display visar punkt) och
klockslagen 09.00–09.40 i Ma1 1.1683.

  python tools/svg-decimalkomma-2026-11-24.py [--skriv]
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PLAN = {
    'uppgifter.js': ['4.229'],
    'uppgifterma1.js': ['4.67', '4.169'],
    'uppgifterma2.js': ['4.387'],
    'uppgiftermato1.js': ['3.552', '3.555', '3.609', '3.642', '3.646', '3.725', '3.728', '3.730', '3.732', '3.755', '3.785'],
    'uppgiftermatf1.js': ['4.133'],
}
TAL = re.compile(r'(?<![\w.])([−-]?\d+)\.(\d+)(?![\w.])')
TEXT = re.compile(r'(<(?:text|tspan)\b[^>]*>)([^<]*)')


def ratta(svg):
    return TEXT.sub(lambda m: m.group(1) + TAL.sub(r'\1,\2', m.group(2)), svg)


def main():
    for fil, ids in PLAN.items():
        path = os.path.join(ROOT, fil)
        src = open(path, encoding='utf-8', newline='').read()
        bank = json.loads(src[src.index('['):src.rindex(']') + 1])
        byten = {}
        for q in bank:
            if q['id'] not in ids:
                continue
            for svg in re.findall(r'<svg[\s\S]*?</svg>', json.dumps(q, ensure_ascii=False)):
                ny = ratta(svg.replace('\\"', '"')).replace('"', '\\"')
                if ny != svg:
                    byten[svg] = ny
        ny_src = src
        for g, n in byten.items():
            assert g in ny_src, fil
            ny_src = ny_src.replace(g, n)
        fore = {q['id']: q for q in bank}
        efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        andr = sorted({q['id'] for q in efter if q != fore[q['id']]})
        assert set(andr) <= set(ids), set(andr) - set(ids)
        utan = lambda q: re.sub(r'<svg[\s\S]*?</svg>', '', json.dumps(q, ensure_ascii=False))
        for q in efter:
            assert utan(q) == utan(fore[q['id']]), q['id']
        print(fil, len(byten), 'figurer i', andr)
        if '--skriv' in sys.argv:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(ny_src)


if __name__ == '__main__':
    main()
