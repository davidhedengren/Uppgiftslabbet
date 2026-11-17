# Fy1 kap 4 genomläsning: kraftmoment (2026-11-17).
# Ändrat: "som väger nästan ingenting" (heter "lätt"), ledtrådar i frågan ("Plankans egen tyngd ger inget
# moment."), dubbla uppmaningar, metatext ("Sök gränsen till tippning.") och krystade meningar.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '4.76': {'ers': [(' Plankans egen tyngd ger inget moment.', '')]},
    '4.245': {'ers': [(' Beräkna momentet kring en stödjepunkt vid väggen.', '')]},
    '4.128': {'ers': [('Figuren visar två alternativa lägen; krafterna verkar inte samtidigt.', 'Krafterna verkar inte samtidigt.')]},
    '4.218': {'ers': [(' Sök gränsen till tippning.', '')]},
    '4.79': {'ers': [('Vinden trycker på skylten med en kraft som kan räknas som om den angriper 1,2 m över marken.', 'Vindens kraft på skylten angriper 1,2 m över marken.')]},
    '4.68': {'ers': [('istället för', 'i stället för')]},
    '4.295': {'ers': [('Antag att förflyttningarna sker långsamt mellan lägen där allt står stilla.', 'Personen går långsamt.')]},
    '4.505': {'ers': [('Anna på 18 kg och Britta på 24 kg sitter på en 3,0 m lång gungbräda.', 'Anna väger 18 kg och Britta 24 kg. De sitter på en 3,0 m lång gungbräda.')]},
}
LATT = [(r'En horisontell (stång|balk|gungbräda) som väger nästan ingenting', r'En lätt, horisontell \1'),
        (r'En ([\d,]+ m lång) (gungbräda|stång|planka) som väger nästan ingenting', r'En lätt, \1 \2'),
        (r'en (planka|stång|bräda) som väger nästan ingenting', r'en lätt \1')]
b = Bank('fy1')
for u in b.arr:
    if u.get('kap') != 4:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = R.setdefault(u['id'], {'ers': []})['ers']
    for rx, ny in LATT:
        for m in set(re.findall(rx, alla)):
            m0 = re.search(rx, alla).group(0)
            e.append((m0, re.sub(rx, ny, m0)))
            alla = alla.replace(m0, re.sub(rx, ny, m0))
    if not e:
        del R[u['id']]
