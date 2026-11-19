# Ma5 genomläsning (2026-11-19): svarsformatet för sannolikheter är en instruktion för svarsrutan och står i
# kgInstruktion (på papper får eleven svara i valfri form).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FRASER = ['Du kan svara med exakt bråk, decimaltal eller procent.', 'Du kan svara med ett exakt uttryck, ett decimaltal eller procent.']
R = {'4.344': {'ers': [(r"och ange tecknet på \(P'\) för", r"och avgör om \(P'\) är positiv eller negativ för")]}}
for u in Bank('matf1').arr:
    delar = u.get('spelDelar') or []
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in delar for x in (d.get('t'), d.get('fraga'))]
    for f in FRASER:
        if any(f in x for x in falt):
            p = R.setdefault(u['id'], {'ers': []})
            p['ers'] += [('<p>' + f + '</p>', ''), (' ' + f, ''), (f + ' ', ''), (f, '')]
            if f in (u.get('t') or ''):
                p['kg'] = ((u.get('kgInstruktion') or '') + ' ' + f).strip()
            dd = {}
            for i, d in enumerate(delar):
                if f in (d.get('t') or '') + (d.get('fraga') or ''):
                    dd[d.get('etikett') or chr(97 + i)] = {'kg': ((d.get('kgInstruktion') or '') + ' ' + f).strip()}
            if dd:
                p['d'] = dd
