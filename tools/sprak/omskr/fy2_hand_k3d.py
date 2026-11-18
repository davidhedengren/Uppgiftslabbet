# Fy2 laddade partiklar i elektriskt fält och spolar: handgenomläsning 2026-11-18.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FORMEL = r'<p>I ett homogent fält mellan plattorna: \(F=qE\), \(E=\dfrac Ud\). Farten parallellt med plattorna är konstant.</p>'
POL = '<p><strong>nordpol</strong> eller <strong>sydpol</strong></p>'
TYNGD = 'Bortse från tyngdkraften på elektroner och protoner.'
R = {
    '4.17': {'ers': [(r' Elektronmassan är \(9{,}11\cdot10^{-31}\) kg.', '')]},
    '3.189': {'ers': [('Vilket alternativ beskriver fältets riktning i centrum?', 'Åt vilket håll pekar magnetfältet i centrum?')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    alla = ' '.join(falt)
    e = []
    if FORMEL in alla:
        e.append((FORMEL, ''))
    if POL in alla and 'nordpol eller en sydpol' in alla:
        e.append((POL, ''))
    if TYNGD in alla:
        e.append((TYNGD, 'Bortse från tyngdkraften.'))
    if e:
        R.setdefault(u['id'], {}).setdefault('ers', []).extend(e)
