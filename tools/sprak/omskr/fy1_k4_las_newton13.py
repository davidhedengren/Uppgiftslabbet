# Fy1 kap 4 genomläsning: Newtons första och tredje lag (2026-11-17).
# Ändrat: förbehåll som stod före själva situationen, förklarande stycken efter frågelistan (metatext som
# "I sista delen jämförs …", "Figuren är en förenklad skiss"), standardmeningen om att märka krafter med
# angreppspunkt, "komponent" (heter komposant) och dubbla uppmaningar.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '4.32': {'ers': [('<p>Lådan står på ett horisontellt golv och har bara kontakt med golvet och Johans händer. Bortse från luftmotstånd.</p><p>Johan trycker på en stor låda med kraften 350 N åt höger, men lådan står helt stilla.</p>',
                      '<p>Johan trycker på en stor låda med kraften 350 N åt höger, men lådan står helt stilla. Lådan står på ett horisontellt golv. Bortse från luftmotstånd.</p>')]},
    '4.52': {'ers': [('<p>Snörena sitter symmetriskt.</p><p>Figuren visar en låda som hänger stilla i två snören.</p>',
                      '<p>Figuren visar en låda som hänger stilla i två snören. Snörena sitter symmetriskt.</p>')]},
    '4.66': {'ers': [('<p>Lampan är i vila och upphängningen symmetrisk.</p><p>En lampa med massan 4,0 kg hänger i två lika långa snören.',
                      '<p>En lampa med massan 4,0 kg hänger stilla i två lika långa snören.')]},
    '4.86': {'ers': [('<p>I del a–c bortser vi från mätarnas massor. I del d har mätarna sin egen massa ovanför fjädern som mäter, så varje mätare visar kraften i sin nedre krok.</p><p>Två likadana dynamometrar hängs i serie under ett stativ. Underst hänger en vikt med massan 2,0 kg. Allt hänger stilla.</p>',
                      '<p>Två likadana dynamometrar hängs i serie under ett stativ. Underst hänger en vikt med massan 2,0 kg. Allt hänger stilla. Bortse från dynamometrarnas massa i a–c.</p>'),
                     ('Anta i stället att varje dynamometer själv väger 0,10 kg. Vad visar de då?',
                      'Antag i stället att varje dynamometer väger 0,10 kg och visar kraften i sin nedre krok. Vad visar de då?')]},
    '4.87': {'ers': [('<p>Bortse från luftmotstånd. Isytan är horisontell.</p><p>En puck glider åt höger över en isyta. Ingen knuffar den längre. Friktionen mot isen är liten men inte noll.</p>',
                      '<p>En puck glider åt höger över en horisontell isyta. Ingen knuffar den längre. Friktionen mot isen är liten men inte noll. Bortse från luftmotstånd.</p>')]},
    '4.92': {'ers': [('<p>Personerna och rullbrädorna startar från stillastående. De angivna massorna inkluderar respektive rullbräda. Knuffkraften antas vara konstant under kontakten.</p><p>Två personer står på var sin rullbräda och knuffar ifrån varandra. Den ena väger 50 kg och den andra 75 kg.',
                      '<p>Två personer står stilla på var sin rullbräda och knuffar ifrån varandra. Med rullbrädan väger den ena 50 kg och den andra 75 kg.')]},
    '4.95': {'ers': [('<p>Bussen bromsar med konstant acceleration. Muggen är från början stilla relativt bordet. Bortse från luftmotstånd.</p><p>En buss kör i 50 km/h. Föraren bromsar och bussen står stilla efter 4,0 s.',
                      '<p>En buss kör i 50 km/h. Föraren bromsar med konstant retardation och bussen står stilla efter 4,0 s.')]},
    '4.139': {'ers': [('<p>Ballongen är stilla och snöret spänt. När vinden ändras jämförs två jämviktslägen med samma lyftkraft, tyngd och horisontella vindriktning.</p>', '')]},
    '4.141': {'ers': [('Frilägg lampan tillsammans med ringen. Bortse från snörenas massa. 0° &lt; α, β &lt; 90°.', 'Bortse från snörenas massa.')]},
    '4.231': {'ers': [('<p>Titta på ett ögonblick när farkostens massa är 800 kg. Bortse från andra yttre krafter.</p>', '<p>Bortse från tyngdkraften.</p>')]},
    '4.233': {'ers': [('<p>I c hålls kraftens storlek 180 N konstant och vinkeln ökar inom intervallet 0°–90°.</p>', '')]},
    '4.259': {'ers': [('<p>Upphängningen är symmetrisk, med tavlans tyngdpunkt mitt mellan fästena. Båda snörena bildar vinkeln θ med horisontell riktning, där 0° &lt; θ &lt; 90°.</p>',
                       '<p>Upphängningen är symmetrisk.</p>')]},
    '4.260': {'ers': [('<p>I sista delen jämförs nya stilla lägen där det undre snöret fortfarande är horisontellt och det övre snörets vinkel från lodlinjen ökar.</p>', '')]},
    '4.404': {'ers': [(' Du får inte bortse från luftmotstånd och rullmotstånd.', '')]},
    '4.405': {'ers': [('Rita och namnge krafterna på föremålet och namnge alla yttre krafter på föremålet.', 'Rita och namnge alla krafter på pulkan.')]},
    '4.421': {'ers': [(' Figuren är en förenklad skiss av läget.', '')]},
    '4.232': {'ers': [('Antag att personen har ordnat sin kroppsställning så att hon inte tippar; undersök bara risken att glida.', 'Antag att personen inte tippar.')]},
    '4.171': {'ers': [('Ballongen ligger stilla mot ett horisontellt tak utan att vara fastklistrad i en idrottshall.', 'Ballongen ligger stilla mot det horisontella taket i en idrottshall.')]},
    '4.230': {'ers': [('komponent framåt', 'komposant framåt'), ('sidokomponenterna', 'sidokomposanterna')]},
}
for _i in ('4.671', '4.672', '4.673', '4.674'):
    R[_i] = {'ers': [('<p>Bortse från snörenas och trissornas massa och från friktionen i trissorna.</p>', '')]}

# Standardmeningen om att märka krafter (hela kapitlet).
STANDARD = ('Rita av figuren och sätt ut alla krafter som verkar på den markerade kroppen. Märk ut varje kraft med namn och rita pilen från rätt angreppspunkt.',
            'Rita av figuren och sätt ut alla krafter med namn.')
b = Bank('fy1')
for u in b.arr:
    if u.get('kap') != 4:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    if STANDARD[0] in alla:
        R.setdefault(u['id'], {'ers': []})['ers'].append(STANDARD)
# 4.133: "den markerade kroppen" är den undre lådan; skriv ut det i stället för standardmeningen.
R['4.133'] = {'ers': [(' Den undre lådan är markerad.', ''), (STANDARD[0], 'Rita av figuren och sätt ut alla krafter på den undre lådan med namn.')]}
