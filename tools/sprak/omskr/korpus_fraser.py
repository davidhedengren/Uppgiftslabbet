"""Formuleringar som i lärarens egna prov (korpus 375 filer, uppladdad 2026-11-23).

Jämförelsen med korpusen (`tools/sprak/jamfor.py`) visade fraser som är vanliga i bankerna men saknas i lärarens
prov, där läraren i stället skriver på ett annat sätt:

- Fy1: ”En ruta motsvarar 10 N.” (97 uppgifter, aldrig i korpusen) → ”Skala: 1 ruta = 10 N.” (lärarens prov:
  ”Skala: 1 ruta = 5,0 N.”).
- Fy1: ”Bortse från värmeförluster.” → ”Bortse från eventuella värmeförluster till omgivningen.” (lärarens prov).
- Ma1: ”Faktorisera … genom att bryta ut största möjliga faktor.” → ”Bryt ut största möjliga faktor …” (lärarens
  prov: ”Bryt ut största möjliga faktor”).

Bytena görs bara i elevtext (`t`, `spelIntro`, delkortens `t` och `fraga`) utanför figurer. Bara strängliteralerna
byts, så filens format behålls, och skriptet kontrollerar att inga andra fält ändras.

  python tools/sprak/omskr/korpus_fraser.py [--skriv]
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

BYTEN = {
    'uppgifter.js': [
        (re.compile(r'En ruta motsvarar ([^.<]{1,20})\.'), r'Skala: 1 ruta = \1.'),
        (re.compile(r'Bortse från värmeförluster\.'), 'Bortse från eventuella värmeförluster till omgivningen.'),
    ],
    'uppgifterma1.js': [
        (re.compile(r'Faktorisera (\\\(.*?\\\)) genom att bryta ut största möjliga faktor\.'),
         r'Bryt ut största möjliga faktor ur \1.'),
        (re.compile(r'Faktorisera (?:uttrycken )?genom att bryta ut största möjliga faktor\.'),
         'Bryt ut största möjliga faktor.'),
    ],
}
FALT = ('t', 'spelIntro')
DELFALT = ('t', 'fraga')


def byt_text(t, regler):
    """Byt utanför <svg>…</svg>."""
    delar = re.split(r'(<svg[\s\S]*?</svg>)', t)
    for i in range(0, len(delar), 2):
        for pat, ny in regler:
            delar[i] = pat.sub(ny, delar[i])
    return ''.join(delar)


def main():
    for fil, regler in BYTEN.items():
        path = os.path.join(ROOT, fil)
        src = open(path, encoding='utf-8', newline='').read()
        bank = json.loads(src[src.index('['):src.rindex(']') + 1])
        byten = []   # (gammal sträng, ny sträng)
        andrade = set()
        for q in bank:
            objs = [(q, FALT)] + [(d, DELFALT) for d in q.get('spelDelar') or []]
            for obj, falt in objs:
                for f in falt:
                    v = obj.get(f)
                    if not isinstance(v, str):
                        continue
                    ny = byt_text(v, regler)
                    if ny != v:
                        byten.append((v, ny))
                        andrade.add(q['id'])
        ny_src = src
        for g, n in sorted(set(byten), key=lambda x: -len(x[0])):
            lg, ln = json.dumps(g, ensure_ascii=False), json.dumps(n, ensure_ascii=False)
            assert lg in ny_src, fil
            ny_src = ny_src.replace(lg, ln)
        nb = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        for q, r in zip(nb, bank):
            if q != r:
                assert q['id'] in andrade, q['id']
                for k in set(q) | set(r):
                    if k != 'spelDelar' and q.get(k) != r.get(k):
                        assert k in FALT, (q['id'], k)
        print(fil, len(andrade), 'uppgifter')
        if '--skriv' in sys.argv:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(ny_src)


if __name__ == '__main__':
    main()
