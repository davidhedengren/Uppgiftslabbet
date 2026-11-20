# Ma5 handgenomläsning, kombinatorik (2026-11-20): stycket <p class="svarformat-info"> bort ur uppgiftstexten.
# Tomma stycken (rester efter matf1_las1.py) tas bort, "Avrundade svar ska ha minst två värdesiffror." flyttas till kgInstruktion.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

TOM = '<p class="svarformat-info"><em></em></p>'
AVR_T = '<p class="svarformat-info"><em>Avrundade svar ska ha minst två värdesiffror.</em></p>'
AVR = 'Avrundade svar ska ha minst två värdesiffror.'


def kg_med(gammal, ny):
    g = (gammal or '').strip()
    return g if ny in g else (g + ' ' + ny).strip()


R = {}
for u in Bank('matf1').arr:
    t = u.get('t') or ''
    delar = u.get('spelDelar') or []
    alla = t + ''.join((d.get('t') or '') + (d.get('fraga') or '') for d in delar)
    ers = [(x, '') for x in (TOM, AVR_T) if x in alla]
    if not ers:
        continue
    p = {'ers': ers}
    if AVR_T in t:
        p['kg'] = kg_med(u.get('kgInstruktion'), AVR)
    d = {}
    for dk in delar:
        if AVR_T in (dk.get('t') or '') + (dk.get('fraga') or '') or (AVR_T in t and dk.get('kgInstruktion')):
            if dk.get('etikett'):
                d[dk['etikett']] = {'kg': kg_med(dk.get('kgInstruktion'), AVR)}
    if d:
        p['d'] = d
    R[u['id']] = p
R.setdefault('1.548', {'ers': []})['ers'].append(('exakt 4 krona.', 'exakt 4 kronor.'))
