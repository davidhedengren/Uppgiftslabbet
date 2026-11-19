# Matte (alla fyra banker): "Polynomet är p(x) = …" / "Funktionen är f(x) = …" heter "Polynomet p ges av p(x) = …"
# (stilguiden, 2026-11-19). Körs per bank: python tools/sprak/apply.py <bank> tools/sprak/omskr/matte_ges_av.py
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

BANK = os.environ.get('SPRAKBANK', 'mato1')
RX = re.compile(r'(Polynomet|Polynomfunktionen|Funktionen) är \\\(([A-Za-z])\(([a-z])\)=')
R = {}
for u in Bank(BANK).arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    e = []
    for x in falt:
        for m in RX.finditer(x):
            a = m.group(0)
            c = f'{m.group(1)} \\({m.group(2)}\\) ges av \\({m.group(2)}({m.group(3)})='
            if (a, c) not in e:
                e.append((a, c))
    if e:
        R[u['id']] = {'ers': e}
