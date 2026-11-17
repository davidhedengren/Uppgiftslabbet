# Fy1 kap 4 genomläsning: fjädrar, och "väger nästan ingenting" i hela kapitlet (2026-11-17).
# Ändrat: "ideal fjäder", ledtrådar i frågan ("Vid parallellkoppling har de samma förlängning; vid
# seriekoppling verkar samma dragkraft genom båda.", "Samma dragkraft går genom båda."), förbehåll efter
# frågelistan och svarsformat ("Ange i procent.").
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '4.8': {'ers': [('<p>Bortse från fjädrarnas massa. Vid parallellkoppling har de samma förlängning; vid seriekoppling verkar samma dragkraft genom båda.</p>', '')]},
    '4.17': {'ers': [('<p>Båda fjädrarna följer Hookes lag i det använda området och hålls stilla.</p>', '')]},
    '4.16': {'ers': [('En jämnt uppbyggd fjäder som väger nästan ingenting har fjäderkonstanten k = 60 N/m. Antag att varje del fungerar som en ideal fjäder.',
                      'En jämnt uppbyggd fjäder har fjäderkonstanten k = 60 N/m.')]},
    '4.183': {'ers': [('<p>Bortse från fjäderns massa. Kroppen vid den fria änden står på ett friktionsfritt horisontellt underlag och hålls stilla.</p>', '')]},
    '4.332': {'ers': [(' Samma dragkraft går genom båda.', '')]},
    '4.338': {'ers': [(' Ange i procent.', '')]},
    '4.227': {'ers': [('Trissan är friktionsfri och väger nästan ingenting.', 'Bortse från trissans massa och friktion.'),
                      ('Systemets accelerationens storlek ska vara', 'Accelerationen ska vara')]},
    '4.111': {'ers': [('Trissorna och vajern är friktionsfria och väger nästan ingenting.', 'Bortse från trissornas och vajerns massa och från friktion.')]},
}
b = Bank('fy1')
for u in b.arr:
    if u.get('kap') != 4:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = R.setdefault(u['id'], {'ers': []})['ers']
    for a, c in (('Trissan är friktionsfri och väger nästan ingenting.', 'Bortse från trissans massa och friktion.'),
                 ('En stång som väger nästan ingenting', 'En lätt stång'),
                 ('Två ideala fjädrar', 'Två fjädrar'), ('två vertikala ideala fjädrar', 'två vertikala fjädrar'),
                 ('ideala fjädrar', 'fjädrar'), ('en ideal fjäder', 'en fjäder')):
        if a in alla and not any(a == x[0] or a in x[0] for x in e):
            e.append((a, c))
            alla = alla.replace(a, c)
    if not e:
        del R[u['id']]
