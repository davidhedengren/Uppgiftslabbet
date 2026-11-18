# Fy2 svängningar: handgenomläsning 2026-11-18.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FORMEL = (r'<p>Harmonisk svängning: \(y=A\sin\omega t\), \(v=A\omega\cos\omega t\), \(a=-\omega^2y\), med \(\omega=2\pi f\). '
          r'Största fart \(A\omega\), största acceleration \(A\omega^2\).</p>')
R = {
    '2.16': {'ers': [('En massa med massan 0,25 kg', 'En vikt med massan 0,25 kg')]},
    '2.23': {'ers': [('Massan i ett fjäder-system fyrdubblas medan samma fjäder används.', 'En vikt svänger i en fjäder. Vikten byts mot en med fyra gånger så stor massa.')]},
    '2.24': {'ers': [('En massa med massan 0,45 kg', 'En vikt med massan 0,45 kg'), ('Massan dras ned lite', 'Vikten dras ned lite')]},
    '2.25': {'ers': [('En 0,60 kg kloss svänger', 'En kloss med massan 0,60 kg svänger')]},
    '2.26': {'ers': [('En 0,40 kg kloss sitter', 'En kloss med massan 0,40 kg sitter')]},
    '2.29': {'ers': [('En 0,50 kg oscillator har', 'En oscillator med massan 0,50 kg har')]},
    '2.306': {'ers': [(' (Negativt värde betyder under jämviktsläget.)', '')],
              'kg': 'Ett negativt värde betyder under jämviktsläget.', 'd': {'a': {'kg': 'Ett negativt värde betyder under jämviktsläget.'}}},
    '2.507': {'ers': [('(SI-enheter)', '(meter, sekunder)')]},
    '2.508': {'ers': [('(SI-enheter)', '(meter, sekunder)')]},
    '2.509': {'ers': [('(SI-enheter)', '(m/s, s)')]},
    '2.510': {'ers': [('(SI-enheter, vinklar i radianer).', '(meter, sekunder). Räkna i radianer.')]},
    '2.522': {'ers': [('Ett föremål (2,7 kg) hänger i en fjäder (310 N/m).', 'Ett föremål med massan 2,7 kg hänger i en fjäder med fjäderkonstanten 310 N/m.')]},
    '2.523': {'ers': [('En stålkula (885 g) hänger stilla i en fjäder (184 N/m).', 'En stålkula med massan 885 g hänger stilla i en fjäder med fjäderkonstanten 184 N/m.')]},
    '2.525': {'ers': [('En radio (5,24 kg) skakas', 'En radio med massan 5,24 kg skakas')]},
    '2.526': {'ers': [('i en fjädervåg (16 N/m) och', 'i en fjädervåg med fjäderkonstanten 16 N/m och')]},
    '2.528': {'ers': [('En vikt (250 g) fästs', 'En vikt med massan 250 g fästs')]},
    '2.531': {'ers': [('En kula (0,60 kg) svänger', 'En kula med massan 0,60 kg svänger')]},
    '2.533': {'ers': [('En leksak (150 g) i en fjäder (300 N/m) har', 'En leksak med massan 150 g svänger i en fjäder med fjäderkonstanten 300 N/m. Den har')]},
    '2.536': {'ers': [('En kloss (400 g) i en horisontell fjäder (46,0 N/m) dras', 'En kloss med massan 400 g sitter i en horisontell fjäder med fjäderkonstanten 46,0 N/m. Klossen dras')]},
    '2.537': {'ers': [('En vikt (2,0 kg) i en horisontell fjäder (98 N/m) dras', 'En vikt med massan 2,0 kg sitter i en horisontell fjäder med fjäderkonstanten 98 N/m. Vikten dras')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(FORMEL in x for x in falt):
        R.setdefault(u['id'], {}).setdefault('ers', []).insert(0, (FORMEL, ''))
