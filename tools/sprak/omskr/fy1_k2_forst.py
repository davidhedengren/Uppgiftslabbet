# Fy1 kap 2, förhandsomgång 2026-11-18 (körs FÖRE fy1_kap2.py).
# I enheter är målenheten själva uppgiften: den flyttas in i frågan innan generatorn tar bort "(Svara i …)".
# Tomt inledningsstycke "<p>Bestäm.</p>" (medelhastighet) tas bort.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '2.359': {'ers': [('Hur stor är tvärsnittsarean? (Svara i mm².)', 'Hur stor är tvärsnittsarean i mm²?')]},
    '2.360': {'ers': [('Hur långt hinner ljuset färdas i vakuum på en nanosekund? (Svara i cm.)', 'Hur många centimeter hinner ljuset färdas i vakuum på en nanosekund?')]},
    '2.361': {'ers': [('Bestäm kubens volym och kantlängd. (Svara i cm³ och cm med tre värdesiffror.)', 'Bestäm kubens volym i cm³ och kantlängd i cm.')]},
    '2.363': {'ers': [(' (Svara i grundpotensform.)', '')], 'kg': 'Svara i grundpotensform.'},
}
b = Bank('fy1')
for u in b.arr:
    if u.get('kap') != 2:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    if '<p>Bestäm.</p>' in alla:
        R.setdefault(u['id'], {'ers': []})['ers'].append(('<p>Bestäm.</p>', ''))
