# Fy1 kap 3: rättelser efter testkörningen 2026-11-18.
# 3.461 har meningen "Österut räknas som positiv riktning." som etikett i figuren; kgInstruktion formuleras
# därför lite annorlunda. När riktningen flyttades till kgInstruktion blev ",." kvar i några uppgifter.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {'3.461': {'kg': 'Öster räknas som positiv riktning.'}}
b = Bank('fy1')
for u in b.arr:
    if u.get('kap') != 3:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    if ',.' in alla:
        R.setdefault(u['id'], {})['ers'] = [(',.', '.')]
