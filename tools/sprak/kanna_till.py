"""”känna” i betydelsen ”veta om” skrivs ”känna till” (användaren 2026-11-24: ”räcker det inte att känna spänningen”
→ ”känna till”). Alla förekomster lästes för hand innan regeln skrevs.

Ändras: ”känner/känna X” → ”känner/känna till X”, även efter du/man/vi och adverben redan, alltså, dessutom och
inte (”Vilka sidor känner du?” → ”… känner du till?”, ”den känner du inte” → ”den känner du inte till”).
Ändras inte: ”känner (du) igen”, ”känner av”, ”känns”, redan ”känner till”, och fysikens ”känna” = påverkas av en
kraft (UNDANTAG). Två meningar skrivs om för hand (SPECIAL). Alla textfält ändras, även facit, ledtrådar,
alternativ och rättSvar (samma ändring som alternativen).

  python tools/sprak/kanna_till.py [--skriv]
"""
import copy
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import bankobjekt as B  # noqa: E402
from sprakverktyg import FIL, Bank  # noqa: E402

UNDANTAG = {('fy1', '4.133'), ('fy1', '9.274'), ('fy1', '9.535'), ('fy2', '1.15'), ('fy2', '3.308'),
            ('ai', '1.107')}  # 1.107: ”personer du kanske känner” = känna en person
SPECIAL = {
    ('ma2', '2.616'): [('faktorer som vi känner logaritmen för', 'faktorer vars logaritmer vi känner till')],
    ('mato2', '1.537'): [('vars sinus och cosinus du känner exakt', 'vars exakta sinus- och cosinusvärden du känner till')],
}
META = {'id', 'omr', 'familj', 'typ', 'familjNyckel', 'familjTidigare', 'omrTidigare', 'delmoment'}
RX = re.compile(r'\b([Kk]änn(?:er|a))\b((?:\s+(?:du|man|vi))?)((?:\s+(?:redan|alltså|dessutom|inte))*)')


def byt(s):
    ut, pos = [], 0
    for m in RX.finditer(s):
        efter = s[m.end():]
        nasta = re.match(r'\s*(\w+)', efter)
        klausul = re.split(r'[.?!]', efter, maxsplit=1)[0]
        if (nasta and nasta.group(1) in ('till', 'igen', 'av', 'sig', 'efter', 'på')) or re.search(r'\bigen\b', klausul):
            continue
        ut.append(s[pos:m.end()] + ' till')
        pos = m.end()
    ut.append(s[pos:])
    return ''.join(ut)


def walk(o):
    if isinstance(o, str):
        return byt(o)
    if isinstance(o, list):
        return [walk(x) for x in o]
    if isinstance(o, dict):
        return {k: (v if k in META else walk(v)) for k, v in o.items()}
    return o


def strangar(a, b, ut):
    """Par (gammal, ny) för varje ändrad sträng."""
    if isinstance(a, str):
        if a != b:
            ut.append((a, b))
    elif isinstance(a, list):
        for x, y in zip(a, b):
            strangar(x, y, ut)
    elif isinstance(a, dict):
        for k in a:
            strangar(a[k], b[k], ut)


def main():
    skriv = '--skriv' in sys.argv
    totalt = 0
    for kod in ['fy1', 'fy2', 'ma1', 'ma2', 'mato1', 'mato2', 'matf1', 'ai']:
        fil = os.path.join(HERE, '..', '..', FIL[kod])
        src, bank = B.las(fil)
        nya = {}
        for u in bank:
            if (kod, u['id']) in UNDANTAG:
                continue
            ny = u
            if (kod, u['id']) in SPECIAL:   # handskrivna meningar först; regeln hoppar sedan över ”känner till”
                txt = json.dumps(ny, ensure_ascii=False)
                for g, n in SPECIAL[(kod, u['id'])]:
                    assert g in txt, (kod, u['id'], g)
                    txt = txt.replace(g, n)
                ny = json.loads(txt)
            ny = walk(ny)
            if ny != u:
                nya[u['id']] = ny
        for id_, ny in nya.items():
            par = []
            strangar(next(x for x in bank if x['id'] == id_), ny, par)
            for g, n in par:
                print(f'{kod} {id_}: …{re.sub("<[^>]+>", " ", n)[max(0, n.find("känn") - 50):n.find("känn") + 60]}…')
        totalt += len(nya)
        if not nya:
            continue
        # Formatbevarande: bankobjekt bara om alla berörda objekt skrivs tillbaka i exakt samma form,
        # annars strängliteralerna en och en (Ma1 har objekt med avvikande indrag, Ma2 är kompakt).
        try:
            rund = B.kontrollera_rundresa(fil, set(nya))
        except ValueError:
            rund = ['kompakt']
        if not rund:
            ny_src = B.ersatt(src, nya)
            json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
            if skriv:
                B.skriv(fil, ny_src)
        else:
            b = Bank(kod)
            for id_, ny in nya.items():
                par = []
                strangar(b.obj(id_), ny, par)
                b.ersatt(id_, par)
            if skriv:
                b.spara()
    print(totalt, 'uppgifter', '(skrivet)' if skriv else '(torrkörning)')


if __name__ == '__main__':
    main()
