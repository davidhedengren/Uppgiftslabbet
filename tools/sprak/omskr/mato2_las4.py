# Ma4 handgenomläsning: kapitel 4, komplexa tal och polynom (2026-11-19).
# "4-1i" skrivs "4-i"; "moniskt" och "ledande koefficient" är inte kursens ord; svarsformer till kgInstruktion.
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

POL = r'<p>Du kan använda \(r(\cos v+i\sin v)\) eller \(re^{iv}\). Ett reellt slutresultat får skrivas som ett reellt tal.</p>'
KPOL = 'Du kan svara på formen r(cos v + i sin v) eller re^(iv). Ett reellt svar får skrivas som ett reellt tal.'
R = {
    '4.63': {'ers': [(r'b) Markera mentalt var \(\bar z_1\) ligger och ange talet.', r'b) Var ligger \(\bar z_1\)? Ange talet.')]},
    '4.100': {'ers': [(r'<p>Alla \(z=x+iy\) som uppfyller</p><p>\[|z-1|=2|z+1|.\]</p>', r'<p>Alla \(z=x+iy\) som uppfyller</p><p>\[|z-1|=2|z+1|\]</p><p>bildar en cirkel.</p>'),
                      ('<p>bildar en cirkel. Härled cirkelns ekvation', '<p>Härled cirkelns ekvation')]},
    '4.09': {'ers': [(POL, '')], 'kg': KPOL, 'd': {e: {'kg': KPOL} for e in 'abcd'}},
    '4.117': {'ers': [(POL, '')], 'kg': KPOL, 'd': {e: {'kg': KPOL} for e in 'abc'}},
    '4.91': {'ers': [(r' Ett rent imaginärt svar får skrivas som \(bi\).', '')],
             'kg': 'Ett rent imaginärt svar får skrivas som bi.', 'd': {e: {'kg': 'Ett rent imaginärt svar får skrivas som bi.'} for e in 'abc'}},
    '4.620': {'ers': [('ett tredjegradspolynom med ledande koefficient 1.', r'ett tredjegradspolynom där koefficienten framför \(x^3\) är 1.')]},
    '4.437': {'ers': [('Bestäm ett moniskt tredjegradspolynom med reella koefficienter som har rötterna 2 och 1+i.',
                       r'Bestäm ett tredjegradspolynom med reella koefficienter, koefficienten 1 framför \(x^3\) och rötterna \(2\) och \(1+i\).')]},
    '4.447': {'ers': [('Ett moniskt polynom har reella koefficienter och rötterna', 'Ett polynom har reella koefficienter och koefficienten 1 framför den högsta potensen. Polynomet har rötterna')]},
}
RX = re.compile(r'(?<=[0-9])([+-])1i(?=\\\))')
for u in Bank('mato2').arr:
    falt = [u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    for x in falt:
        for m in re.finditer(r'\\\([^()]*?[0-9][+-]1i\\\)', x):
            a = m.group(0)
            par = (a, RX.sub(lambda k: k.group(1) + 'i', a))
            e = R.setdefault(u['id'], {}).setdefault('ers', [])
            if par not in e:
                e.append(par)
