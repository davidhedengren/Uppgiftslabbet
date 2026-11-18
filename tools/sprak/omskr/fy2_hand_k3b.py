# Fy2 jordens magnetfält och induktion: handgenomläsning 2026-11-18.
# Svarsraden "medurs eller moturs" under frågan flyttas till kgInstruktion. Formler i frågan stryks.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

RAD = '<p><strong>medurs</strong> eller <strong>moturs</strong></p>'
JAMNT = 'Magnetflödet gäller för ett varv och ändras jämnt under den angivna tiden.'
R = {
    '3.445': {'ers': [(r'Magnetfältet kring en lång rak ledare är \(B=\dfrac{\mu_0I}{2\pi r}\). ', ''), (r'Magnetfältet kring en lång rak ledare är \(B=\dfrac{\mu_0I}{2\pi r}\).', '')]},
    '3.446': {'ers': [(r'Kraften på en strömförande ledare i ett magnetfält är \(F=BIl\) när ledaren är vinkelrät mot fältet. ', ''), (r'Kraften på en strömförande ledare i ett magnetfält är \(F=BIl\) när ledaren är vinkelrät mot fältet.', '')]},
    '3.539': {'ers': [(r'Magnetfältet från ledningen är \(B=\dfrac{\mu_0I}{2\pi r}\). ', '')]},
    '3.200': {'ers': [('Vilket svar till Mira är korrekt?', 'Har Mira rätt? Motivera.')]},
    '3.201': {'ers': [('Vilket alternativ beskriver strömmen under intervallen 0–1 s, 1–2 s och 2–3 s, i den ordningen?', 'Åt vilket håll går strömmen under intervallen 0–1 s, 1–2 s och 2–3 s?')]},
    '3.531': {'ers': [('Under hur lång tid sammanlagt induceras', 'Under hur lång tid totalt induceras')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    alla = ' '.join(falt)
    if RAD in alla:
        e = R.setdefault(u['id'], {}).setdefault('ers', [])
        e.append((RAD, ''))
        fraga = alla.replace(RAD, '')
        if 'medurs eller moturs' not in fraga:
            R[u['id']]['kg'] = 'Svara medurs eller moturs.'
    if JAMNT in alla:
        R.setdefault(u['id'], {}).setdefault('ers', []).append((JAMNT, 'Flödet gäller ett varv och ändras jämnt.'))
# tomma stycken efter att formeln strukits
for _id in ('3.445', '3.446'):
    R[_id]['ers'].append(('<p></p>', ''))
