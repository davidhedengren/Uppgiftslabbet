# Matte (alla banker), 2026-11-19: kvarvarande instruktioner om svarsrutor flyttas från uppgiftstexten till kgInstruktion.
# Körs per bank: SPRAKBANK=mato1 python tools/sprak/apply.py mato1 tools/sprak/omskr/matte_svarsrutor.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

BANK = os.environ.get('SPRAKBANK', 'mato1')
FRASER = {  # text i uppgiften -> text i kgInstruktion
    'Ordningen spelar ingen roll.': 'Ordningen spelar ingen roll.',
    'Ange det mindre värdet först.': 'Ange det mindre värdet först.',
    'Ange båda x-värdena, en i varje ruta.': 'Skriv ett x-värde i varje ruta.',
    'Ange ett x-värde i varje ruta.': 'Skriv ett x-värde i varje ruta.',
    'Ange ett värde i varje ruta.': 'Skriv ett värde i varje ruta.',
    'Ange värdena i var sitt fält.': 'Skriv ett värde i varje fält.',
}


def kg_med(gammal, nya):
    ut = (gammal or '').strip()
    for n in nya:
        if n not in ut:
            ut = (ut + ' ' + n).strip()
    return ut


R = {}
for u in Bank(BANK).arr:
    ers, kg_u, d = [], [], {}
    t = u.get('t') or ''
    for f, k in FRASER.items():
        if f in t:
            ers.append((' ' + f, '') if (' ' + f) in t else (f, ''))
            kg_u.append(k)
    for dk in u.get('spelDelar') or []:
        txt = (dk.get('t') or '') + ' ' + (dk.get('fraga') or '')
        nya = []
        for f, k in FRASER.items():
            if f in txt:
                par = (' ' + f, '') if (' ' + f) in txt else (f, '')
                if par not in ers:
                    ers.append(par)
                nya.append(k)
        if nya and dk.get('etikett'):
            d[dk['etikett']] = {'kg': kg_med(dk.get('kgInstruktion'), nya)}
    if ers:
        p = {'ers': ers}
        if kg_u:
            p['kg'] = kg_med(u.get('kgInstruktion'), kg_u)
        if d:
            p['d'] = d
        R[u['id']] = p
