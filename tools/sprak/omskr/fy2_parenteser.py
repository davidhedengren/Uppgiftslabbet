# Fy2: parenteser som fy2_alla.py inte tog (2026-11-18). Körs efter fy2_alla.py.
#  - "(Svara med ett tal.)", "(Svara med ett decimaltal.)" och rena precisionskrav tas bort.
#  - Svarsformat som rättningen behöver (ord, ordning, kategorier) flyttas till kgInstruktion, utan parentes.
#  - Krav som hör till uppgiften ("både i joule och i elektronvolt") står kvar som en vanlig mening.
#  - Övriga enhetsuppräkningar ("(Svara i m och Hz.)") tas bort; Kunskapsgymmet visar svarEnhet per delkort.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

PAREN = re.compile(r' ?\((?:Svara|Ange|Välj)[^()]*(?:\([^()]*\)[^()]*)*\)')
BEHALL = {  # blir vanlig mening i texten
    '(Ange svaret både i joule och i elektronvolt.)': 'Ange svaret både i joule och i elektronvolt.',
    '(Ange svaret både enligt oss på jorden och enligt Pelle.)': 'Ange svaret både enligt oss på jorden och enligt Pelle.',
    '(Svara också i km/h.)': 'Ange svaret också i km/h.',
}
TILL_KG = re.compile(r'maximum|minimum|förstärk|försvag|släckning|A–F|i fas|motfas|ordningen|först|ordet|lika\.|faktorn för|'
                     r'positivt tal|värdet på n|namnet på|synvinklar|osäkerheten|den vita|ordningsnumret|en faktor|'
                     r'XXXINGETXXX', re.I)
PRECISION = re.compile(r'decimal|värdesiffr|hela grader|ett tal\b|decimaltal', re.I)


def ren_kg(p):
    t = p.strip()[1:-1].strip()
    t = re.sub(r'\s*med (en|två|tre|fem) (decimaler?|värdesiffror)', '', t)
    if not t.endswith('.'):
        t += '.'
    return t[0].upper() + t[1:]


b = Bank('fy2')
R = {}
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    e, kg = [], []
    for m in list(dict.fromkeys(x.group(0) for x in PAREN.finditer(alla))):
        if raw.count(m) != alla.count(m):
            continue
        p = m.strip()
        if p in BEHALL:
            e.append((m, ' ' + BEHALL[p]))
        elif TILL_KG.search(p):
            e.append((m, '')); kg.append(ren_kg(p))
        else:
            e.append((m, ''))  # enhet eller precision
    if e:
        R[u['id']] = {'ers': e}
        if kg:
            k = ' '.join(dict.fromkeys(kg))
            R[u['id']]['kg'] = k
            dd = {}
            for i, d in enumerate(u.get('spelDelar') or []):
                dt = (d.get('t') or '') + (d.get('fraga') or '')
                hit = [x for x in kg if any(m.strip()[1:-1].startswith(x[:12]) or True for m in [])]
                if any(TILL_KG.search(x.group(0)) for x in PAREN.finditer(dt)):
                    dd[d.get('etikett') or chr(97 + i)] = {'kg': ' '.join(dict.fromkeys(ren_kg(x.group(0)) for x in PAREN.finditer(dt) if TILL_KG.search(x.group(0))))}
            if dd:
                R[u['id']]['d'] = dd
