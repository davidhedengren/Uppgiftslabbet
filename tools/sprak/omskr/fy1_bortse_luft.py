"""Fy1: onödiga ”Bortse från luftmotståndet.” bort (språkgranskning 2026-11-22).

Lärarens prov skriver ”Bortse från …” cirka 2 gånger per 10 000 ord, Fy1 skrev det 35 gånger. Förbehållet tas bort
där luftmotståndet inte påverkar svaret i en gymnasieuppgift: lådor, klossar, puckar, curlingstenar och pulkor som
glider långsamt på ett underlag med friktion, eller ligger stilla. Varje uppgift är läst och beslutad för sig.

Står kvar: uppgifter där eleven ska rita krafterna (förbehållet avgör vilka krafter som ritas: 4.87, 4.132, 4.196,
4.221, 4.258, 4.407, 4.415), och snabba människor och fordon där luftmotståndet faktiskt spelar roll (skidåkare,
snowboard, slalom, bilar i hög fart: 4.442, 4.445, 4.528, 4.537, 4.578, 4.585, 4.616, 4.618–4.622, 4.680, 5.112,
5.171, 5.373, 5.493, 5.495, 5.519).

  python tools/sprak/omskr/fy1_bortse_luft.py [--skriv]
"""
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import bankobjekt as B  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BORT = ['4.47', '4.102', '4.105', '4.176', '4.282', '4.321', '4.394', '4.441', '4.531', '4.532', '4.533', '4.536',
        '4.542', '4.579', '4.589', '4.612', '4.613', '4.851', '5.489', '5.517', '5.518', '5.536']
MENING = re.compile(r' ?Bortse från luftmotstånd(?:et)?\.(?= |<|$)')


def rensa(t):
    ny = MENING.sub('', t)
    ny = re.sub(r'<p>\s*</p>', '', ny).replace('<p> ', '<p>')
    return ny


def main():
    fil = os.path.join(ROOT, 'uppgifter.js')
    src, bank = B.las(fil)
    Q = {q['id']: q for q in bank}
    nya = {}
    for uid in BORT:
        q = json.loads(json.dumps(Q[uid]))
        fore = json.dumps(q, ensure_ascii=False)
        q['t'] = rensa(q['t'])
        if q.get('spelIntro'):
            q['spelIntro'] = rensa(q['spelIntro'])
        for d in q.get('spelDelar') or []:
            for k in ('t', 'fraga'):
                if d.get(k):
                    d[k] = rensa(d[k])
        efter = json.dumps(q, ensure_ascii=False)
        assert efter != fore, uid
        for k in ('t', 'spelIntro'):
            assert not MENING.search(q.get(k) or ''), (uid, k)
        assert '<p></p>' not in efter, uid
        nya[uid] = q
    assert not B.kontrollera_rundresa(fil, set(nya))
    ny = B.ersatt(src, nya)
    nb = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [q['id'] for q, r in zip(nb, bank) if q != r]
    assert sorted(andr) == sorted(BORT), set(andr) ^ set(BORT)
    print(len(andr), 'uppgifter')
    if '--skriv' in sys.argv:
        B.skriv(fil, ny)


if __name__ == '__main__':
    main()
