"""Handgranskning av Ma1 kapitel 6: kalkylprogram, samhällsliv, programmering, modeller och grafisk lösning (2026-11-20).

Telegramstil ("Procentuell ökning?", "Andel till boende?") blir hela frågor. "Använd GeoGebra"/"med GeoGebra"/"med räknare"
tas bort ur frågan (verktygstaggen räcker, användarbeslut 2026-11-06); "utan GeoGebra" i 6.69 c står kvar som kontrast.
Svarsformer i parentes blir vanlig mening eller tas bort när programmets utskrift redan bestämmer formen.
"""
GG = ' med GeoGebra.'
R = {
    '6.123': {'ers': [('Boende 9 000, mat 3 600, resor 1 800.', 'Boende kostar 9 000 kr, mat 3 600 kr och resor 1 800 kr.'),
                      ('a) Hur mycket återstår?', 'a) Hur mycket pengar återstår?'),
                      ('b) Andel till boende?', 'b) Hur stor andel av budgeten går till boende?'),
                      ('c) Andel som återstår?', 'c) Hur stor andel av budgeten återstår?'),
                      ('>Hur mycket återstår?<', '>Hur mycket pengar återstår?<'),
                      ('>Andel till boende?<', '>Hur stor andel av budgeten går till boende?<'),
                      ('>Andel som återstår?<', '>Hur stor andel av budgeten återstår?<')]},
    '6.125': {'ers': [('Hur stor procent är kvar?', 'Hur många procent av pengarna har du kvar?')]},
    '6.126': {'ers': [('A kostar 180 kr/mån + 12 kr/användning. B kostar 360 kr/mån. Från hur många användningar är B billigare?',
                       'Med abonnemang A betalar du 180 kr per månad plus 12 kr för varje gång du använder tjänsten. Abonnemang B kostar 360 kr per månad. Från hur många användningar per månad är B billigare?')]},
    '6.129': {'ers': [('En utgift ökar från 2400 till 2640 kr. Procentuell ökning?', 'En utgift ökar från 2 400 kr till 2 640 kr. Med hur många procent ökar utgiften?')]},
    '6.131': {'ers': [('En vara kostar 1600 kr och rabatteras 25 %. Nytt pris?', 'En vara kostar 1 600 kr och priset sänks med 25 %. Vad blir det nya priset?')]},
    '6.132': {'ers': [('Du sparar 12 % av 18 500 kr. Hur mycket?', 'Du får 18 500 kr i månaden och sparar 12 %. Hur mycket sparar du?')]},
    '6.13': {'ers': [(' Svara med ett positivt tal om värdet ökar och ett negativt om det minskar.', '')],
             'kg': 'En minskning skrivs som ett negativt tal.'},
    '6.116': {'ers': [(' Använd digitalt verktyg.', '')]},
    '6.12': {'ers': [(GG, '.')]},
    '6.65': {'ers': [(GG, '.')]},
    '6.71': {'ers': [(GG, '.')]},
    '6.32': {'ers': [('Använd GeoGebra för att bestämma när modellerna har samma värde.', 'När har modellerna samma värde?')]},
    '6.64': {'ers': [(r'Lös ekvationen \(M(t)=100\) med GeoGebra.', r'Lös ekvationen \(M(t)=100\).')]},
    '6.66': {'ers': [(r'Använd GeoGebra för att bestämma alla tidpunkter \(0\le t\le20\) då modellerna är lika.', r'Bestäm alla tidpunkter \(0\le t\le20\) då modellerna har samma värde.')]},
    '6.67': {'ers': [('Använd GeoGebra för att bestämma x-koordinaten', 'Bestäm x-koordinaten')]},
    '6.68': {'ers': [(r'Använd GeoGebra för att bestämma \(p\) så att', r'Bestäm \(p\) så att')]},
    '6.69': {'ers': [(r'\(4{,}5x-7{,}2=23{,}4\) med GeoGebra.', r'\(4{,}5x-7{,}2=23{,}4\).'),
                     (r'\(4{,}5x-7{,}2=23,4\) med GeoGebra.', r'\(4{,}5x-7{,}2=23{,}4\).'),
                     (r'och \(y=9-1{,}1x\) med GeoGebra.', r'och \(y=9-1{,}1x\).'),
                     (r'Ekvationen \(4{,}5x-7{,}2=23,4\) har lösningen \(x=6,8\).', r'Ekvationen \(4{,}5x-7{,}2=23{,}4\) har lösningen \(x=6{,}8\).')]},
    '6.70': {'ers': [(r'för \(0\le x\le20\) med GeoGebra.', r'för \(0\le x\le20\).')]},
    '6.63': {'ers': [(r'\(2{,}7x+4{,}1=19,5\) med räknare.', r'\(2{,}7x+4{,}1=19{,}5\).')]},
    '6.72': {'ers': [(r'\(4{,}7x-3{,}2=18,9\) med räknare.', r'\(4{,}7x-3{,}2=18{,}9\).')]},
    '6.424': {'ers': [(' (Svara med en decimal.)', '')]},
    '6.441': {'ers': [(' (Svara med två decimaler.)', '')]},
    '6.458': {'ers': [('(Svara med två decimaler.)', 'Avrunda till två decimaler.')]},
    '6.14': {'ers': [('Beräkna kapitalet efter fyra år. Svara med två decimaler.', 'Beräkna kapitalet efter fyra år. Avrunda till två decimaler.')]},
    '6.425': {'ers': [('Vilken rad är fel? ()', 'Vilken rad är fel?')]},
}
# språktestet: "sammanlagd" heter "total"
R['6.105'] = {'ers': [('den sammanlagda produktionen', 'den totala produktionen')]}
R['6.118'] = {'ers': [('sammanlagda befolkning', 'totala befolkning')]}
