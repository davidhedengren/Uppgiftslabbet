# Fy1 kap 4 genomläsning: blandat – rörelse och kraft (2026-11-17).
# Ändrat: dubbla upplysningar ("Där är fjädern 24 cm längre än obelastad längd."), metatext, enhet i
# frågan där den är SI, "på X kg", "sammanlagt" och "inga andra vertikala krafter …".
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

GENERELLT = [
    (' Där är fjädern 24 cm längre än obelastad längd.', ''),
    (' Jämviktsläget motsvarar fjäderns obelastade längd.', ''),
    (' Bortse från övergången exakt vid 4,0 s.', ''),
    ('Ett flygplan på 4,0 · 10⁴ kg', 'Ett flygplan med massan 4,0 · 10⁴ kg'),
    ('Anta konstant acceleration.', 'Antag att accelerationen är konstant.'),
    ('Vad visar vågen i N?', 'Vad visar vågen?'),
    ('Luft- och rullmotståndet är sammanlagt 400 N.', 'Luft- och rullmotståndet är tillsammans 400 N.'),
    ('En motorcykel med förare på sammanlagt 220 kg', 'En motorcykel med förare, som tillsammans väger 220 kg,'),
    (' och inga andra vertikala krafter än tyngdkraften och normalkraften verkar', ''),
    ('Bestäm hissens acceleration i m/s².', 'Bestäm hissens acceleration.'),
    ('Bestäm accelerationen just nu i m/s²', 'Bestäm accelerationen just nu'),
]
b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') != 4:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = []
    for a, c in GENERELLT:
        if a in alla:
            e.append((a, c))
            alla = alla.replace(a, c)
    if e:
        R[u['id']] = {'ers': e}
