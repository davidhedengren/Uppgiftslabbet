"""Specifika ledtrådar i spelträdsuppgifterna 3.81–3.255 (språkomskrivningen steg 3, 2026-11-23).

Byggskriptet tools/bygg-ai-speltrad-nivaer-2026-11-23.py bygger nu ledtrådar som nämner uppgiftens egna löv och
sökningens väg (led_minimax, led_beskarning, led_ab5). Det här skriptet kör byggskriptet, kontrollerar att text,
svar och facit är exakt desamma som i banken (byggskriptet är deterministiskt) och byter bara `ledtrad` i
uppgiften och i dess delkort. Övriga språkändringar i banken påverkas inte.

  python tools/sprak/ai_speltrad_ledtradar.py [--skriv]
"""
import collections
import copy
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402

FIL = os.path.abspath(os.path.join(HERE, '..', '..', 'uppgifterai.js'))
spec = importlib.util.spec_from_file_location('bygg', os.path.join(HERE, '..', 'bygg-ai-speltrad-nivaer-2026-11-23.py'))
BY = importlib.util.module_from_spec(spec)
sys.argv_spar, sys.argv = sys.argv, [sys.argv[0]]
spec.loader.exec_module(BY)
sys.argv = sys.argv_spar


def main():
    src, bank = B.las(FIL)
    Q = {u['id']: u for u in bank}
    nya = {}
    for g in BY.alla():
        u = Q[g['id']]
        for k in ('t', 's', 'rättSvar', 'spelIntro'):
            assert u[k] == g[k], (g['id'], k)
        assert [d['fraga'] for d in u['spelDelar']] == [d['fraga'] for d in g['spelDelar']], g['id']
        ny = copy.deepcopy(u)
        ny['ledtrad'] = g['ledtrad']
        for d, gd in zip(ny['spelDelar'], g['spelDelar']):
            d['ledtrad'] = gd['ledtrad']
        if ny != u:
            nya[u['id']] = ny
    upprepade = collections.Counter(n['ledtrad'] for n in nya.values())
    flest = upprepade.most_common(1)[0] if upprepade else (None, 0)
    print(f'{len(nya)} ledtrådar byts; vanligaste ny ledtråd står i {flest[1]} uppgifter')
    for id_ in ['3.81', '3.111', '3.141', '3.166', '3.191', '3.192', '3.216', '3.240']:
        if id_ in nya:
            print(' ', id_, nya[id_]['ledtrad'])
    ny_src = B.ersatt(src, nya)
    if '--skriv' in sys.argv:
        B.skriv(FIL, ny_src)
        print('skrivet')


if __name__ == '__main__':
    main()
