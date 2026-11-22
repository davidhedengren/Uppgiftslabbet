"""Fy1: ”Bortse från energi som går till kärlet och omgivningen.” → ”Bortse från värmeförluster.” (2026-11-22).

Meningen stod ordagrant i värmeuppgifterna (kalorimetri och blandning) och lät maskinskriven. ”Bortse från
värmeförluster.” är det vanliga uttrycket och betyder samma sak. Dessutom tas ”Bortse från luftmotståndet.” bort i
3.273 och 3.606, där texten redan säger att föremålet faller fritt.

  python tools/sprak/omskr/fy1_bortse_varme.py [--skriv]
"""
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import bankobjekt as B  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
GAMMAL = 'Bortse från energi som går till kärlet och omgivningen.'
NY = 'Bortse från värmeförluster.'
FRITT = {'3.273': ' Bortse från luftmotståndet.', '3.606': ' Bortse från luftmotståndet.'}


def main():
    fil = os.path.join(ROOT, 'uppgifter.js')
    src, bank = B.las(fil)
    nya = {}
    for q in bank:
        k = json.loads(json.dumps(q))
        falt = [(k, 't'), (k, 'spelIntro')] + [(d, f) for d in k.get('spelDelar') or [] for f in ('t', 'fraga')]
        for obj, f in falt:
            if obj.get(f) and GAMMAL in obj[f]:
                obj[f] = obj[f].replace(GAMMAL, NY)
        if q['id'] in FRITT:
            assert 'faller fritt' in k['t'] and FRITT[q['id']] in k['t'], q['id']
            k['t'] = k['t'].replace(FRITT[q['id']], '')
        if k != q:
            nya[q['id']] = k
    assert not B.kontrollera_rundresa(fil, set(nya))
    ny = B.ersatt(src, nya)
    assert GAMMAL not in json.dumps([q.get('t') for q in json.loads(ny[ny.index('['):ny.rindex(']') + 1])], ensure_ascii=False)
    print(len(nya), 'uppgifter')
    if '--skriv' in sys.argv:
        B.skriv(fil, ny)


if __name__ == '__main__':
    main()
