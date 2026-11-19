# Ma4 (mato2), kopia av mato1_forenklad.py: "förenklad modell" och liknande (2026-11-18). En modell är alltid en förenkling; ordet stryks.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

REGEX = [
    (r'den förenklade modellen', 'modellen'),
    (r'Den förenklade modellen', 'Modellen'),
    (r'(?<![\w])förenklad[ea]? (?=(?:modell|vinstmodell|linjär|planritning|kommunkarta|värmekurvor))', ''),
]
b = Bank('mato2')
R = {}
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    e = []
    for rx, ny in REGEX:
        for m in re.finditer(r'([^.>]{0,25})(' + rx + ')', alla):
            a = m.group(0)
            c = m.group(1) + ny
            if a in alla and raw.count(a) == alla.count(a) and not any(a == x[0] for x in e):
                e.append((a, c)); alla = alla.replace(a, c)
    if e:
        R[u['id']] = {'ers': e}
