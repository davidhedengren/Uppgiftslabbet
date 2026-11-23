"""Handskrivna språkändringar i AI-banken (2026-11-23).

AI-banken har a)-stycken i `t` i stället för <ol>, och samma mening står ofta i `t`, `spelIntro` och ett delkorts
`fraga`. Därför skrivs ändringarna som par (gammal delsträng, ny delsträng) per uppgift, och paret byts i alla
textfält där det står: `t`, `spelIntro`, delkortens `t` och `fraga`. Varje par måste träffa minst en gång.
Facit (`s`), svar och alternativ ändras inte, utom med nyckeln '@s' (par som bara byts i huvudfacit och delkortens
facit) eller '@kg' (ny `kgInstruktion` per delkortsetikett: {'a': 'text'}).

Omskrivningsfilen har en ordlista R = {id: [(gammal, ny), ...]}, eventuellt med {'@s': [...], '@kg': {...}} som
sista element.

  python tools/sprak/ai_byt.py tools/sprak/omskr/ai_ml_grunder.py [--skriv]
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

FIL = os.path.abspath(os.path.join(HERE, '..', '..', 'uppgifterai.js'))
TEXT = ('t', 'spelIntro')
DTEXT = ('t', 'fraga')


def ladda(fil):
    spec = importlib.util.spec_from_file_location('omskr', fil)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.R


def tillampa(u, par):
    ny = copy.deepcopy(u)
    extra = par[-1] if par and isinstance(par[-1], dict) else {}
    par = [p for p in par if not isinstance(p, dict)]
    for gammal, nytt in par:
        traff = 0
        for k in TEXT:
            if ny.get(k) and gammal in ny[k]:
                traff += ny[k].count(gammal)
                ny[k] = ny[k].replace(gammal, nytt)
        for d in ny.get('spelDelar') or []:
            for k in DTEXT:
                if d.get(k) and gammal in d[k]:
                    traff += d[k].count(gammal)
                    d[k] = d[k].replace(gammal, nytt)
        assert traff, f'{u["id"]}: hittades inte: {gammal[:70]}'
    for gammal, nytt in extra.get('@s', []):
        traff = 0
        for obj in [ny] + list(ny.get('spelDelar') or []):
            if obj.get('s') and gammal in obj['s']:
                traff += 1
                obj['s'] = obj['s'].replace(gammal, nytt)
        assert traff, f'{u["id"]}: facit: hittades inte: {gammal[:70]}'
    for etikett, kg in extra.get('@kg', {}).items():
        d = next(d for d in ny['spelDelar'] if d.get('etikett') == etikett)
        d['kgInstruktion'] = kg
    return ny


def main():
    R = ladda(sys.argv[1])
    src, bank = B.las(FIL)
    Q = {u['id']: u for u in bank}
    nya = {}
    for id_, par in R.items():
        u = Q[id_]
        ny = tillampa(u, par)
        for k in u:
            if k not in ('t', 'spelIntro', 'spelDelar', 's'):
                assert ny[k] == u[k], (id_, k)
        nya[id_] = ny
    ny_src = B.ersatt(src, nya)
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    print(len(nya), 'uppgifter ändrade' + (' (skrivet)' if '--skriv' in sys.argv else ' (torrkörning)'))
    if '--skriv' in sys.argv:
        B.skriv(FIL, ny_src)


if __name__ == '__main__':
    main()
