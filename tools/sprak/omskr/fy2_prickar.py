"""Fy2 HR-diagram: ”De små prickarna är verkliga stjärnor: närbelägna stjärnor och kända ljusstarka stjärnor.”
→ ”De små prickarna i diagrammet är verkliga stjärnor.” (språkgranskning 2026-11-22). Meningen stod ordagrant i 27
uppgifter och lät som en bildtext. Bara strängliteralerna byts, så filens format behålls.

  python tools/sprak/omskr/fy2_prickar.py [--skriv]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIL = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'uppgifter2.js'))
GAMMAL = 'De små prickarna är verkliga stjärnor: närbelägna stjärnor och kända ljusstarka stjärnor.'
NY = 'De små prickarna i diagrammet är verkliga stjärnor.'


def main():
    src = open(FIL, encoding='utf-8').read()
    n = src.count(GAMMAL)
    ny = src.replace(GAMMAL, NY)
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [q['id'] for q, r in zip(efter, fore) if q != r]
    for q, r in zip(efter, fore):
        if q != r:
            assert json.dumps(q, ensure_ascii=False).replace(NY, GAMMAL) == json.dumps(r, ensure_ascii=False), q['id']
    print(n, 'förekomster i', len(andr), 'uppgifter')
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
