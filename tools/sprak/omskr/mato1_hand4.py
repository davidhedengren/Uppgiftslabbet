# Ma3c: "Miniräknare får användas." är metatext; flaggan miniräknare styr verktyget (2026-11-19).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank
M = 'Miniräknare får användas.'
R = {}
for u in Bank('mato1').arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(M in x for x in falt):
        R[u['id']] = {'ers': [('<p>' + M + '</p>', ''), (' ' + M, ''), (M + ' ', ''), (M, ''), ('<p></p>', '')]}
# "Behåll oavrundade värden i mellanleden." är också metatext (stilguiden); facit visar hur man räknar.
B = '<p>Behåll oavrundade värden i mellanleden.</p>'
for u in Bank('mato1').arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(B in x for x in falt):
        R.setdefault(u['id'], {'ers': []})['ers'].append((B, ''))
