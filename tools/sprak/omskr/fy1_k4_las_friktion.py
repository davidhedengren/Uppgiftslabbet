# Fy1 kap 4 genomläsning: friktion och lutande plan (2026-11-17).
# Ändrat: "Glidfriktionen är den enda bromsande kraften och är konstant." (heter "Bortse från luftmotstånd."),
# förbehåll som säger vilka krafter som verkar, metatext efter frågelistan, precision och enhet i frågan,
# "komponent" (heter komposant), "statiska friktionstalet" (heter vilofriktionstalet).
# Rättar också 4.105, där fy1_k4_rest.py skrev "Bortse från friktion" i en friktionsuppgift.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '4.105': {'ers': [('Soffan dras horisontellt över ett horisontellt golv. Bortse från friktion och luftmotstånd.', 'Soffan dras horisontellt över ett horisontellt golv. Bortse från luftmotstånd.')]},
    '4.100': {'ers': [('<p>Friktionstalet gäller vilofriktion, alltså innan lådan börjar glida. Den horisontella kraften ökas långsamt.</p>', ''),
                      ('Friktionstalet mellan låda och hissgolv är 0,25.', 'Vilofriktionstalet mellan låda och hissgolv är 0,25. En horisontell kraft F ökas långsamt.')]},
}
GENERELLT = [
    (' Glidfriktionen är den enda bromsande kraften och är konstant.', ' Bortse från luftmotstånd.'),
    (' Friktionen är den enda bromsande kraften och är konstant.', ' Bortse från luftmotstånd.'),
    (' Inga andra vertikala krafter än tyngdkraft och normalkraft verkar.', ''),
    (' Bara tyngdkraft och kontaktkrafter från planet verkar.', ' Bortse från luftmotstånd.'),
    (' Inga andra krafter än tyngdkraft, normalkraft och friktion verkar.', ' Bortse från luftmotstånd.'),
    ('<p>Anta horisontell väg, konstant retardation och att däck–väg-kraften är den enda horisontella kraften. I b söker du det effektiva friktionstal som bromsningen motsvarar.</p>',
     '<p>Vägen är horisontell och retardationen konstant.</p>'),
    ('<p>I sista delen ökas vinkeln långsamt medan klossen ännu ligger stilla, fram till glidgränsen. Friktionstalet är oförändrat och klossen kan inte välta.</p>',
     '<p>Klossen kan inte välta.</p>'),
    ('<p>Planet lutar 25° som i figuren. Endast tyngdkraft och kontaktkrafter från planet verkar.</p>', '<p>Planet lutar 25°.</p>'),
    ('Bestäm accelerationen nedför backen i m/s² med tre värdesiffror.', 'Bestäm accelerationen nedför backen.'),
    (' Bestäm bromssträckan i hela meter.', ' Bestäm bromssträckan.'),
    ('Hur stor är bilens retardation, alltså hur snabbt minskar farten?', 'Hur stor är bilens retardation?'),
    ('Det statiska friktionstalet', 'Vilofriktionstalet'),
    ('Pelle skjuter en pulka med Stina på, sammanlagt 55,0 kg,', 'Pelle skjuter en pulka med Stina på, som tillsammans väger 55,0 kg,'),
    ('Hur stor är friktionskraften i N?', 'Hur stor är friktionskraften?'),
    ('Hur stor är den horisontella kraften i N?', 'Hur stor är den horisontella kraften?'),
    ('Hur stor är kraften i repet i N?', 'Hur stor är kraften i repet?'),
    ('komponenter', 'komposanter'), ('komponenten', 'komposanten'), ('komponent', 'komposant'),
]
b = Bank('fy1')
for u in b.arr:
    if u.get('kap') != 4:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = R.setdefault(u['id'], {'ers': []})['ers']
    for x in e:
        alla = alla.replace(x[0], x[1])
    for a, c in GENERELLT:
        if a in alla:
            e.append((a, c))
            alla = alla.replace(a, c)
    if not e:
        del R[u['id']]
