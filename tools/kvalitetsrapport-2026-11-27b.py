"""Kvalitetsrapporten 2026-11-27, omgång 2: miniräknarflaggorna.

Kunskapsgymmets kontroll ”Miniräknare bör ses över” flaggade 43 matematikuppgifter med `miniräknare: false`. 42 är rätt
bedömda (avrundning, positionssystem, grundpotensform, prefix och procentform, där räknaren tar bort det som prövas, eller
enkel huvudräkning) och förs in i Kunskapsgymmets `KV_RAKNARE_GRANSKADE`. Ma3c 1.980 får miniräknare: parabelmodellen
ger höjden 175/40 = 4,375 m, en uträkning som inte görs snabbt i huvudet, och räknaren tar inte bort modelleringen som
prövas.

  python tools/kvalitetsrapport-2026-11-27b.py [--skriv]
"""
import json
import os
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgiftermato1.js')


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    a = src.index('"id": "1.980"')
    b = src.index('\n}', a)
    bit = src[a:b]
    assert bit.count('"miniräknare": false') == 1
    src = src[:a] + bit.replace('"miniräknare": false', '"miniräknare": true') + src[b:]
    efter = json.loads(src[src.index('['):src.rindex(']') + 1])
    andr = [(x['id'], sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))) for x, y in zip(efter, fore) if x != y]
    assert andr == [('1.980', ['miniräknare'])], andr
    print(andr)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src)


if __name__ == '__main__':
    main()
