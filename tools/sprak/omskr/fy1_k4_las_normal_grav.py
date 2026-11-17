# Fy1 kap 4 genomläsning: normalkraft och gravitation (2026-11-17).
# Ändrat: modellmeningar ("I en sfäriskt symmetrisk jordmodell", "Behandla kropparna som punktmassor. Avståndet
# mäts mellan deras masscentrum.", "Antag att bollarna är klot med jämnt fördelad massa"), förbehåll före
# situationen, vågens kalibrering i en mening och enhetsdefinition i frågan (4.346).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '4.1': {'ers': [('<p>Allt är i vila.</p><p>En mobiltelefon (200 g) ligger ovanpå', '<p>En mobiltelefon (200 g) ligger stilla ovanpå')]},
    '4.346': {'ers': [(' Massan är jämnt fördelad i kloten.', ''), ('Bestäm gravitationskraftens storlek i nanonewton (1 nN = 10⁻⁹ N).', 'Bestäm gravitationskraftens storlek.')]},
    '4.348': {'ers': [('en sfäriskt symmetrisk planet', 'en planet'), (' Båda lägena ligger utanför planeten och massorna är oförändrade.', '')]},
    '4.351': {'ers': [('en sfäriskt symmetrisk planet', 'en planet')]},
    '4.354': {'ers': [('en sfäriskt symmetrisk planet', 'en planet')]},
    '4.357': {'ers': [(' Kropparna kan behandlas som punktmassor.', '')]},
    '4.362': {'ers': [('I en sfäriskt symmetrisk jordmodell är radien R = 6370 km.', 'Jordens radie är 6370 km.')]},
    '4.365': {'ers': [('I en sfäriskt symmetrisk planetmodell är radien R = 6000 km.', 'En planet har radien 6000 km.')]},
    '4.368': {'ers': [('I en sfäriskt symmetrisk jordmodell är R = 6370 km.', 'Jordens radie är 6370 km.')]},
    '4.374': {'ers': [('Antag att jorden är sfäriskt symmetrisk och bortse från rotation. ', '')]},
    '4.378': {'ers': [(' Anta sfärisk symmetri och bortse från rotation.', '')]},
    '4.379': {'ers': [('Två sfäriskt symmetriska planeter', 'Två planeter')]},
    '4.381': {'ers': [(' Jorden antas sfäriskt symmetrisk. Bortse från rotation. Eleven skriver', ' Hon skriver')]},
    '4.385': {'ers': [(' Alla tre storheter är positiva. En liten testmassa påverkar inte källmassorna. Endast deras gravitation på testmassan beaktas.', '')]},
    '4.738': {'ers': [(' Antag att bollarna är klot med jämnt fördelad massa. De behåller sin form.', '')]},
    '4.745': {'ers': [(' Antag att bollarna är klot med jämnt fördelad massa. De behåller sin form.', '')]},
    '4.749': {'ers': [('En asteroid med jämnt fördelad massa och formen av ett klot har radien', 'En klotformad asteroid har radien')]},
    '4.750': {'ers': [('en asteroid med jämnt fördelad massa och formen av ett klot är', 'en klotformad asteroid är')]},
    '4.188': {'ers': [(' Gör en grov uppskattning genom att behandla dem som punktmassor.', '')]},
    '4.216': {'ers': [('Gör en grov uppskattning genom att behandla dem som punktmassor på avståndet 1,0 m.', 'Avståndet mellan dem är 1,0 m.')]},
    '4.39': {'ers': [('Personen är stilla relativt hissgolvet. Vågens kilogramskala är kalibrerad genom att dividera normalkraften med 9,82 N/kg.',
                      'Vågen visar normalkraften dividerad med 9,82 N/kg.')]},
    '4.90': {'ers': [('<p>Böckerna ligger stilla på ett horisontellt bord.</p><p>Tre böcker staplas på varandra.', '<p>Tre böcker ligger staplade på varandra på ett horisontellt bord.')]},
    '4.94': {'ers': [('<p>Lådorna är i vila.</p><p>En låda', '<p>En låda')]},
    '4.133': {'ers': [('<p>Rita av figuren och sätt ut alla krafter på den undre lådan med namn.</p>', '')]},
    '4.207': {'ers': [('Vågens visning motsvarar normalkraften dividerad med g. Dynamometerns egen tyngd är redan kompenserad.', 'Vågen visar normalkraften dividerad med g.')]},
    '4.217': {'ers': [('Vågen är kalibrerad så att dess kilogramvisning är normalkraften dividerad med 9,82 N/kg.', 'Vågen visar normalkraften dividerad med 9,82 N/kg.')]},
    '4.644': {'ers': [('Vågens kilogramvisning är normalkraften delad med g.', 'Vågen visar normalkraften dividerad med g.')]},
    '4.229': {'ers': [('Ange vågens utslag som normalkraft N. ', '')]},
    '4.475': {'ers': [(' Inga andra krafter än tyngdkraft och normalkraft verkar.', '')]},
    '4.639': {'ers': [('Hur stor är hinkens acceleration (positiv uppåt)?', 'Hur stor är hinkens acceleration?')], 'kg': 'Uppåt räknas som positiv riktning.'},
}
PUNKT = ' Behandla kropparna som punktmassor. Avståndet mäts mellan deras masscentrum.'
b = Bank('fy1')
for u in b.arr:
    if u.get('omr') not in ('gravitation', 'normalkraft'):
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    for v in (f'<p>{PUNKT[1:]}</p>', PUNKT, PUNKT[1:] + ' '):
        if v in alla:
            R.setdefault(u['id'], {'ers': []})['ers'].append((v, ''))
            break
