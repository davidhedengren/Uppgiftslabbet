"""Mellanslag efter fetstilt delbokstav: ”<strong>a)</strong>Bestäm” → ”<strong>a)</strong> Bestäm” (2026-11-24).

I Fy1 (262) och Fy2 (2) stod delbokstaven tätt mot texten, så att korten visade ”a)Bestäm …”. Resten av bankerna
har redan mellanslag (cirka 930 förekomster). Bytet gäller alla strängar (fråga, delkort, facit, ledtråd) och ändrar
bara visningen. Skriptet kontrollerar att varje ändrad sträng blir identisk när mellanslaget tas bort igen.

  python tools/sprak/omskr/mellanslag_delbokstav_2026-11-24.py [--skriv]
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
BANKER = ['uppgifter.js', 'uppgifter2.js']
RX = re.compile(r'(<strong>[a-h]\)</strong>)(?=[A-ZÅÄÖa-zåäö\\(0-9])')


def main():
    for fil in BANKER:
        path = os.path.join(ROOT, fil)
        src = open(path, encoding='utf-8', newline='').read()
        fore = json.loads(src[src.index('['):src.rindex(']') + 1])
        ny, n = RX.subn(r'\1 ', src)
        efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
        assert len(fore) == len(efter)
        andr = 0
        for a, b in zip(fore, efter):
            if a != b:
                andr += 1
                assert json.loads(json.dumps(b, ensure_ascii=False).replace('</strong> ', '</strong>')) == \
                    json.loads(json.dumps(a, ensure_ascii=False).replace('</strong> ', '</strong>')), a['id']
        print(fil, n, 'ställen i', andr, 'uppgifter')
        if '--skriv' in sys.argv:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(ny)


if __name__ == '__main__':
    main()
