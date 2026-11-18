# Fy1 kap 3 genomläsning: hela kapitlet (ensamt "Bestäm." och dubbla förbehåll) och konstant acceleration
# (2026-11-18). Ändrat: tomt inledningsstycke "<p>Bestäm.</p>", samma förbehåll två gånger, modellmeningar
# ("Pröva om en modell …", "Modellen fortsätter även efter vändningen."), data efter frågorna (3.45),
# "Ange tecknet.", "istället", "Anta konstant …", "En elev".
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

E = {
    '3.43': [(' Positiv riktning är samma som den positiva hastighetsriktningen.', '')],
    '3.45': [('En sten släpps från taket på ett hus.', 'En sten släpps från taket på ett hus, 18 m över marken.'), ('<p>Stenen släpps 18 m över marken.</p>', '')],
    '3.161': [('Räkna med att ljudet hinner upp så snabbt att du kan bortse från den tiden.', 'Bortse från tiden det tar för ljudet att komma upp.')],
    '3.162': [('<p>Räkna tiden tills du griper linjalen som din reaktionstid.</p>', '')],
    '3.73': [(' Räkna även ut hur lång sträcka modellen skulle kräva om startbanan inte tog slut efter 800 m.', ''),
             (' Räkna med en tillräckligt lång startbana.', '')],
    '3.75': [(' Diagrammet visar bollens vertikala hastighet.', '')],
    '3.89': [(' Ange tecknet.', '')],
    '3.86': [('istället', 'i stället')],
    '3.157': [('istället', 'i stället'), ('Anta konstant retardation under hela bromsningen.', 'Antag att retardationen är konstant.')],
    '3.63': [('Anta konstant retardation under bromsningen och samma reaktionstid i båda fallen.', 'Antag att retardationen är konstant och att reaktionstiden är densamma i båda fallen.')],
    '3.188': [(' Ange det beräknade gränsvärdet.', '')],
    '3.222': [('När har A fyra gånger så stor fart som B? (Räkna tiden från A:s släpp.)', 'Hur lång tid efter att A släpptes har A fyra gånger så stor fart som B?')],
    '3.392': [('I d) ska g bestämmas från mätningen. ', '')],
    '3.167': [('b) Pröva om en modell med start från stillastående och konstant acceleration passar värdena och bestäm i så fall modellens acceleration.',
               'b) Undersök om värdena passar med start från stillastående och konstant acceleration. Bestäm i så fall accelerationen.')],
    '3.65': [('Antag att kulan startar från stillastående och pröva en modell med konstant acceleration.', 'Antag att kulan startar från stillastående och har konstant acceleration.')],
    '3.69': [('Antag att samma modell gäller även under den fjärde sekunden.', 'Antag att accelerationen är densamma även under den fjärde sekunden.')],
    '3.255': [('Modellen fortsätter även efter vändningen.', 'Accelerationen är densamma även efter vändningen.')],
    '3.253': [('En elev räknar medelfarten', 'Leo räknar medelfarten')],
    '3.187': [('En elev säger:', 'Klara säger:')],
    '3.176': [('Fordonen rör sig i samma riktning och behandlas som punkter.', 'Fordonen kör åt samma håll.')],
}
b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') != 3:
        continue
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    alla = ' '.join(falt)
    e = [x for x in E.get(u['id'], []) if x[0] in alla]
    if '<p>Bestäm.</p>' in alla:
        e.append(('<p>Bestäm.</p>', ''))
    # samma förbehåll två gånger i huvudtexten: ta bort det fristående stycket
    t = u.get('t') or ''
    if '<p>Bortse från luftmotståndet.</p>' in t and t.count('Bortse från luftmotstånd') >= 2:
        e.append(('<p>Bortse från luftmotståndet.</p>', ''))
    if e:
        R[u['id']] = {'ers': e}
