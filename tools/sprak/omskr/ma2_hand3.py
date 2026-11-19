# Ma2: rester efter ma2_alla.py (2026-11-19).
# "Ordningen spelar ingen roll." hörde till svarsfälten och följer med till kgInstruktion.
# 2.69: verktyget nämns inte (ma2-felrapporter-2026-11-06 tillåter högst 15 GeoGebra-omnämnanden).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {'2.69': {'ers': [('GeoGebra har anpassat två modeller till en mätserie:', 'Två modeller har anpassats till en mätserie:')]}}
b = Bank('ma2')
for u in b.arr:
    falt = [u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any('Ordningen spelar ingen roll.' in x for x in falt):
        R[u['id']] = {'ers': [('<p> Ordningen spelar ingen roll.</p>', ''), (' Ordningen spelar ingen roll.', ''), ('Ordningen spelar ingen roll.', '')],
                      'kg': ((u.get('kgInstruktion') or '') + ' Ordningen spelar ingen roll.').strip()}
# 5.95: GeoGebra står inte i frågan (användarbeslut 2026-11-06); frågan om verktyget blir en fråga om metoden.
R['5.95'] = {'ers': [('förklara varför GeoGebra passar för att lösa uppgiften.', 'förklara varför ekvationen är svår att lösa algebraiskt.')]}
