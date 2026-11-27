"""Manuell granskning av Fy1 kap 5 Energi och rörelsemängd (omgång 2), 2026-11-27.

Alla uppgifter i arbete, rörelseenergi, effekt, rörelsemängd, kollisioner och blandat energi är lästa och
kontrollräknade med skript (svar som bara kan läsas av i en figur är inte omräknade). Alla svar stämmer, men 14 svar
var lagrade avrundade i rättSvar, så att Kunskapsgymmet underkände det exakta svaret:

- Heltal (737, 82, 371, 4810, 402, 563, 12200000) behandlar rättningen som exakta. Den som skriver 736,5 J, 82,2 kg
  eller 4805 N blev underkänd.
- Avrundade decimaltal som ligger exakt ett halvt steg från det exakta värdet (76,3 för 76,25, 17,6 för 17,55,
  41,3 för 41,25, −2,84 för −2,835, 1,13 för 1,125, 0,00228 för 0,002275, 0,788 för 0,7875) underkände det exakta
  svaret, eftersom jämförelsen på facits precision är strikt.

Tolv av fallen är FP30-fallen från 2026-10-11, då det rätt avrundade grannvärdet lagrades med en tolerans som
godtog fullvärdet och avvisade den andra grannen. Sedan dess rättar Kunskapsgymmet fysik med svarVardesiffror, som inte
använder toleransen, och användarbeslutet 2026-11-24 säger att ett exakt halvsteg får avrundas åt båda hållen. Med det
avrundade grannvärdet lagrat underkänns därför fullvärdet. Resten av FP30-fallen (5.72, 5.529, 5.533, 5.578, 6.457,
8.523) rättas här på samma sätt.

rättSvar lagras därför oavrundat, som Kunskapsgymmet förutsätter (”rättSvar lagras oavrundat”, index.html). Avrundade
svar godtas fortfarande via svarVardesiffror. Facit (s) är oförändrade. 3.370 a (kap 3) har samma fel och rättas här.

Textändringar: 2.29 e (”Ange energin i joule.” bort), 5.150 (”Moa använder sin θ = 0,060” kunde läsas som ett
possessivt ”sin”), 5.16 b (protonens massa till kgInstruktion, beslut 2026-10-25) och ”Antag” → ”Anta” i kapitel 5.

  python tools/fy1-granskning-kap5-2026-11-27.py [--skriv]
"""
import json
import os
import re
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

# id -> {index i rättSvar (None = skalärt svar): (gammalt, exakt)}
RATT = {
    '3.370': {0: (12200000, (2 * 5e14 * 0.15) ** 0.5)},
    '5.142': {None: (82, 2 * 1900 / 6.8 ** 2)},
    '5.209': {2: (737, 15 * 9.82 * 5.0)},
    '5.505': {2: (76.3, 305 / 4)},
    '5.509': {1: (371, 0.5 * 57 * (7.0 ** 2 - 6.0 ** 2))},
    '5.514': {3: (4810, 0.5 * 0.015 * 310 ** 2 / 0.15)},
    '5.270': {None: (17.6, 260 * 2.25 * 30 / 1000)},
    '5.272': {None: (402, 5200 * 0.73 * 20 / (9.82 * 14) - 150)},
    '5.370': {0: (41.3, 5500 * 3.0 / 400)},
    '5.375': {None: (563, 0.045 * 25.0 / 0.002)},
    '5.381': {0: (-2.84, -0.35 * (5.0 + 3.1))},
    '5.160': {3: (1.13, (1.5 + 3.0 * 1.0) / 4.0)},
    '5.418': {1: (0.00228, 0.5 * 0.25 * 0.79 ** 2 - 0.5 * 0.25 * 0.12 ** 2 - 0.5 * 0.35 * 0.65 ** 2)},
    '5.440': {2: (0.788, 0.0225 * (30 - 23) / 0.2)},
    # övriga verifierade halvsteg från FP30 (2026-10-11), samma problem
    '5.72': {0: (246, 25 * 9.82)},
    '5.529': {1: (213, 85 * 5.0 * 0.5)},
    '5.533': {0: (0.0737, 0.030 * 0.25 * 9.82)},
    '5.578': {0: (3530, ((96000 + 60000) / 20 - 1500 * (0.2 + 0.3)) / 2)},
    '6.457': {1: (246, 0.1 * 9.82 / 0.004)},
    '8.523': {None: (0.563, 9 / 16)},
}

PROTON = 'Protonens massa är 1,673·10⁻²⁷ kg.'
OPS = {
    '2.29': [('byt', ' Ange energin i joule.', '')],
    '5.150': [('byt', 'Moa använder sin θ = 0,060, där θ är backens lutningsvinkel.',
               'Moa räknar med att \\(\\sin\\theta=0{,}060\\), där θ är backens lutningsvinkel.')],
    '5.16': [('byt', 'En proton har massan 1,673 · 10⁻²⁷ kg och farten 2,0 · 10⁶ m/s.', 'En proton har farten 2,0 · 10⁶ m/s.'),
             ('kg', [PROTON], 'b'), ('kg', [PROTON], 'uppgift')],
}


def kg_med(kg, meningar):
    kg = (kg or '').strip()
    for m in meningar:
        if m not in kg:
            kg = (kg + ' ' + m).strip()
    return kg


def texter(q):
    for k in ('t', 'spelIntro'):
        if isinstance(q.get(k), str):
            yield q, k
    for d in q.get('spelDelar') or []:
        for k in ('t', 'fraga'):
            if isinstance(d.get(k), str):
                yield d, k


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    idx = {q['id']: q for q in bank}
    nya = {}

    def hamta(uid):
        if uid not in nya:
            nya[uid] = json.loads(json.dumps(idx[uid]))
        return nya[uid]

    antag = []
    for q0 in bank:
        if q0.get('kap') == 5 and any(re.search(r'\bAntag(?= )', o[k]) for o, k in texter(q0)):
            q = hamta(q0['id'])
            for o, k in texter(q):
                o[k] = re.sub(r'\bAntag(?= )', 'Anta', o[k])
            antag.append(q0['id'])
    for uid, ops in OPS.items():
        q = hamta(uid)
        for op in ops:
            if op[0] == 'byt':
                _, gl, ny = op
                n = 0
                for o, k in texter(q):
                    n += o[k].count(gl)
                    o[k] = o[k].replace(gl, ny)
                assert n >= 1, (uid, gl)
            elif op[0] == 'kg':
                _, meningar, vem = op
                if vem in ('alla', 'uppgift'):
                    q['kgInstruktion'] = kg_med(q.get('kgInstruktion'), meningar)
                for d in q.get('spelDelar') or []:
                    if vem == 'alla' or vem == d['etikett']:
                        d['kgInstruktion'] = kg_med(d.get('kgInstruktion'), meningar)
    for uid, andr in RATT.items():
        q = hamta(uid)
        for i, (gammalt, exakt) in andr.items():
            nu = q['rättSvar'] if i is None else q['rättSvar'][i]
            assert nu == gammalt, (uid, i, nu)
            # det exakta värdet ska ligga nära det lagrade (samma svar, bara oavrundat)
            assert abs(exakt - gammalt) <= abs(gammalt) * 6e-3, (uid, i, exakt)
            if i is None:
                q['rättSvar'] = exakt
            else:
                q['rättSvar'][i] = exakt

    ny_src = src
    for uid, q in nya.items():
        start = ny_src.index('"id": ' + json.dumps(uid))
        indrag = '  ' if ny_src.rfind('\n  {', 0, start) > ny_src.rfind('\n{', 0, start) else ''
        a = ny_src.rfind('\n' + indrag + '{', 0, start) + 1 + len(indrag)
        slut = ny_src.index('\n' + indrag + '}', start) + 2 + len(indrag)
        assert json.loads(ny_src[a:slut]) == idx[uid], uid
        ny_src = (ny_src[:a] + json.dumps(q, ensure_ascii=False, indent=2).replace('\n', '\n' + indrag)
                  + ny_src[slut:])
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = {x['id']: sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k)) for x, y in zip(efter, bank) if x != y}
    assert set(andr) == set(nya), set(andr) ^ set(nya)
    for uid, k in andr.items():
        tillatet = {'rättSvar'} if uid in RATT else set()
        assert not ({'s', 'rättSvar', 'svarEnhet', 'tolerans'} - tillatet) & set(k), (uid, k)
        x = next(e for e in efter if e['id'] == uid)
        for o, kk in texter(x):
            assert '<p></p>' not in o[kk] and 'Antag ' not in o[kk], (uid, kk)
    print(len(andr), 'uppgifter; Antag→Anta i', len(antag), ':', ' '.join(antag))
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)


if __name__ == '__main__':
    main()
