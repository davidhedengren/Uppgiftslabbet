# Fy2 fjädrar: handgenomläsning 2026-11-18.
# Formelraden "Hookes lag: F=kx. Lagrad energi i en fjäder: ..." stryks ur frågorna (formler står i formelsamlingen,
# som i Fy1). Engelskinspirerade "En 6,0 kg last" skrivs "En last med massan 6,0 kg".
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FORMEL = r'<p>Hookes lag: \(F=kx\). Lagrad energi i en fjäder: \(E_p=\dfrac{kx^2}{2}\).</p>'
R = {
    '2.3': {'ers': [('En massa med massan 0,40 kg', 'En vikt med massan 0,40 kg')]},
    '2.9': {'ers': [('En 6,0 kg plattform hänger', 'En plattform med massan 6,0 kg hänger')]},
    '2.11': {'ers': [('En 1,5 kg kloss skjuts', 'En kloss med massan 1,5 kg skjuts')]},
    '2.14': {'ers': [('En 6,0 kg last ska ge', 'En last med massan 6,0 kg ska ge')]},
    '2.15': {'ers': [('En 500 kg vagn kör 4,0 m/s mot', 'En vagn med massan 500 kg kör med farten 4,0 m/s mot')]},
    '2.183': {'ers': [('Bestäm systemets effektiva fjäderkonstant.', 'Bestäm den totala fjäderkonstanten.')]},
    '2.184': {'ers': [('kopplas i parallell.', 'kopplas parallellt.'), ('Bestäm systemets effektiva fjäderkonstant.', 'Bestäm den totala fjäderkonstanten.')]},
    '2.185': {'ers': [('belastas med en massa med massan 1,5 kg', 'belastas med en vikt med massan 1,5 kg'), ('den totala utsträckningen i jämvikt', 'den totala förlängningen i jämvikt')]},
    '2.450': {'ers': [('skjuter en 20,0 g tung sten', 'skjuter en sten som väger 20,0 g')]},
    '2.452': {'ers': [('skjuter 100 g tunga pilar', 'skjuter pilar som väger 100 g')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(FORMEL in x for x in falt):
        R.setdefault(u['id'], {}).setdefault('ers', []).append((FORMEL, ''))
