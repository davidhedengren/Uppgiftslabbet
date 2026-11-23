"""Felrapport 2026-11-23 16:46, Ma1 4.103 (spår 1c): ”Svårt att veta antalet decimaler. Står ingen vägledning.”

k = √84 − 4 = 2√21 − 4 ≈ 5,165. Facit var 5,17 med toleransen 0,02, så 5,2 och 5 underkändes trots att frågan
inte anger någon precision. Enligt användarbeslutet 2026-10-19 (avrundning utan uttalad precision) är facit nu
det exakta värdet med toleransen 1e-10, som i övriga Ma1-uppgifter. Kunskapsgymmets friAvrundningRatt godtar då
varje korrekt avrundat svar (5, 5,2, 5,17, 5,165) och det exakta uttrycket. Ingen avrundningsinstruktion läggs
till: den hör inte hemma i Uppgiftslabbet (beslut 2026-11-23), och ord som ”decimal” eller ”exakt” i
kgInstruktion skulle stänga av den fria avrundningen i Kunskapsgymmet. Facitets sista steg visar nu exakt
värde och närmevärde.

  python tools/felrapporter-2026-11-23-1646.py [--skriv]
"""
import json
import math
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FIL = os.path.join(ROOT, 'uppgifterma1.js')


def lit(v):
    return json.dumps(v, ensure_ascii=False)


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    start = src.index('"id": "4.103"')
    slut = src.index('\n  }', start)
    bit = src[start:slut]
    q = [x for x in fore if x['id'] == '4.103'][0]

    k = math.sqrt(84) - 4
    assert abs((4 + k) ** 2 + 4 ** 2 - 100) < 1e-9 and 4 + k > 0
    assert abs(k - (2 * math.sqrt(21) - 4)) < 1e-12

    byten = [
        ('"rättSvar": 5.17', '"rättSvar": ' + repr(k)),
        ('"tolerans": 0.02', '"tolerans": 1e-10'),
    ]
    gs = q['s']
    a = '<li><div class="facit-matte">\\[k=\\sqrt{84}-4\\approx5{,}17\\].</div></li>'
    b = ('<li><p class="facit-rubrik">Lös ut \\(k\\) och avrunda</p>'
         '<div class="facit-matte">\\[k=\\sqrt{84}-4=2\\sqrt{21}-4\\approx5{,}17\\]</div></li>')
    assert gs.count(a) == 1
    ns = gs.replace(a, b)
    a2 = '<strong>Svar:</strong> \\(k\\approx5{,}17\\).'
    b2 = '<strong>Svar:</strong> \\(k=\\sqrt{84}-4\\approx5{,}17\\).'
    assert ns.count(a2) == 1
    ns = ns.replace(a2, b2)
    byten.append((lit(gs), lit(ns)))
    for g, n in byten:
        assert bit.count(g) == 1, g[:60]
        bit = bit.replace(g, n)
    ny = src[:start] + bit + src[slut:]
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [(x['id'], sorted(kk for kk in set(x) | set(y) if x.get(kk) != y.get(kk)))
            for x, y in zip(fore, efter) if x != y]
    assert andr == [('4.103', ['rättSvar', 's', 'tolerans'])], andr
    print(andr)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
