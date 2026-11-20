"""Handläsning av Ma1 kapitel 1 (2026-11-20), efter första omgången 2026-11-17.

29 faktoriseringsuppgifter slutade med samma mening "Bryt ut största gemensamma faktor med positiv
heltalskoefficient." Frågan heter nu som i lärarens prov "Faktorisera … genom att bryta ut största möjliga faktor."
och kravet på positiv faktor (som självrättningen behöver, t.ex. −12x + 18 = 6(3 − 2x)) ligger i kgInstruktion.
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

GAMMAL = re.compile(r'Faktorisera (\\\(.*?\\\))\. Bryt ut största gemensamma faktor med positiv heltalskoefficient\.')
KG = 'Den faktor du bryter ut ska vara positiv.'
R = {}
for u in Bank('ma1').arr:
    alla = ' '.join([u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = []
    for m in GAMMAL.finditer(alla):
        par = (m.group(0), f'Faktorisera {m.group(1)} genom att bryta ut största möjliga faktor.')
        if par not in e:
            e.append(par)
    if e:
        kg = (u.get('kgInstruktion') or '').strip()
        R[u['id']] = {'ers': e, 'kg': kg if KG in kg else (kg + ' ' + KG).strip()}
