# Fy1 kap 4: rättelser efter testkörningen 2026-11-17.
# "en massa på 0,80 kg" blev "en massa med massan 0,80 kg" i generatorn; det heter nu "en vikt med massan".
# 4.329 fick ett kommatecken kvar när riktningen flyttades till kgInstruktion.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') != 4 and u.get('omr') != 'kraftvektorer':
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    ers = []
    for a, c in (('En massa med massan', 'En vikt med massan'), ('en massa med massan', 'en vikt med massan')):
        if a in alla:
            ers.append((a, c))
    if ers:
        R[u['id']] = {'ers': ers}
R['4.329'] = {'ers': [('handen,.', 'handen.')]}
