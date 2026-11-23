"""Byt exakta delsträngar i uppgifternas textfält, för vilken bank som helst (2026-11-23).

Skriptfilen har BYT = {id: [(gammal, ny), ...]}. Varje par byts i `t`, `spelIntro`, `kgInstruktion` och i
delkortens `t`, `fraga` och `kgInstruktion`, och måste träffa minst en gång. Paren tillämpas i ordning. Facit, svar
och alla andra fält är oförändrade. KG = {id: {'': text, 'b': text}} lägger till (eller förlänger) `kgInstruktion`
på uppgiften ('') eller på ett delkort, när en svarsinstruktion flyttas ur texten.

  python tools/sprak/byt_falt.py <bank> <skript.py> [--skriv]
"""
import copy
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402
from sprakverktyg import FIL  # noqa: E402

FALT = ('t', 'spelIntro', 'kgInstruktion')
DFALT = ('t', 'fraga', 'kgInstruktion')


def main():
    kod, skript = sys.argv[1], sys.argv[2]
    fil = os.path.join(HERE, '..', '..', FIL[kod])
    spec = importlib.util.spec_from_file_location('omskr', skript)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    src, bank = B.las(fil)
    Q = {u['id']: u for u in bank}
    nya = {}
    for id_, par in m.BYT.items():
        ny = copy.deepcopy(nya.get(id_, Q[id_]))
        for gammal, nytt in par:
            traff = 0
            for obj, falt in [(ny, FALT)] + [(d, DFALT) for d in ny.get('spelDelar') or []]:
                for k in falt:
                    if isinstance(obj.get(k), str) and gammal in obj[k]:
                        traff += 1
                        obj[k] = obj[k].replace(gammal, nytt)
            assert traff, f'{id_}: hittades inte: {gammal[:70]}'
        for etikett, text in getattr(m, 'KG', {}).get(id_, {}).items():
            obj = ny if etikett == '' else next(d for d in ny['spelDelar'] if d.get('etikett') == etikett)
            if obj.get('kgInstruktion'):
                if text not in obj['kgInstruktion']:
                    obj['kgInstruktion'] = obj['kgInstruktion'].rstrip() + ' ' + text
            else:
                obj['kgInstruktion'] = text
        for k in Q[id_]:
            if k not in FALT + ('spelDelar',):
                assert ny[k] == Q[id_][k], (id_, k)
        nya[id_] = ny
    for id_ in set(getattr(m, 'KG', {})) - set(m.BYT):
        raise AssertionError(f'{id_}: KG utan BYT')
    try:
        ny_src = B.ersatt(src, nya)
    except ValueError:
        # kompakt bankfil (ett objekt per rad utan indrag, t.ex. Ma2): byt strängliteralerna med sprakverktyg.Bank
        from sprakverktyg import Bank
        b = Bank(kod)
        for id_, ny in nya.items():
            gammal = Q[id_]
            par = [(gammal[k], ny[k], k) for k in FALT if isinstance(gammal.get(k), str) and gammal[k] != ny[k]]
            for d0, d1 in zip(gammal.get('spelDelar') or [], ny.get('spelDelar') or []):
                par += [(d0[k], d1[k]) for k in DFALT if isinstance(d0.get(k), str) and d0[k] != d1[k]]
            tillagg = [(ny['t'], 'kgInstruktion', ny['kgInstruktion'])] \
                if ny.get('kgInstruktion') and 'kgInstruktion' not in gammal else []
            b.ersatt(id_, [p for p in par if p[2:] != ('kgInstruktion',) or 'kgInstruktion' in gammal], tillagg)
        if '--skriv' in sys.argv:
            b.spara()
        print(len(nya), 'uppgifter (kompakt fil)', '(skrivet)' if '--skriv' in sys.argv else '(torrkörning)')
        return
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    print(len(nya), 'uppgifter', '(skrivet)' if '--skriv' in sys.argv else '(torrkörning)')
    if '--skriv' in sys.argv:
        B.skriv(fil, ny_src)


if __name__ == '__main__':
    main()
