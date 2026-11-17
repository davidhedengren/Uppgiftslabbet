# Ma1 enhetsbyten (omr enhetsbyten), omskrivet för hand 2026-11-17.
# Rättningsinstruktionen "Skriv svaret som ett vanligt tal, inte i tiopotensform." är borttagen ur frågorna.
# Den står kvar i kgInstruktion bara där svaret är ett mycket litet tal, eftersom Kunskapsgymmet då annars kan få
# ett svar i tiopotensform (som rättningen inte godtar).
VANLIGT = 'Skriv svaret som ett decimaltal, utan tiopotens.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.212': {'t': p('Omvandla 3,4 m till cm.')},
    '0.213': {'t': p('Omvandla 850 cm till meter.')},
    '0.214': {'t': p('Hur många meter är 2,75 km?')},
    '0.215': {'t': p('Omvandla 6400 m till km.')},
    '0.216': {'t': p('Hur många gram är 4,2 kg?')},
    '0.217': {'t': p('Omvandla 750 g till kg.')},
    '0.218': {'t': p('Hur många milliliter är 3,5 l?')},
    '0.219': {'t': p('Omvandla 1250 ml till liter.')},
    '0.220': {'t': p('Hur många minuter är 2,4 h?')},
    '0.221': {'t': p('Omvandla 150 min till timmar.')},
    '0.222': {'t': p('Omvandla 0,65 m till mm.')},
    '0.223': {'t': p('Hur många meter är 480 mm?')},
    '0.224': {'t': p('Omvandla 0,032 kg till gram.')},
    '0.225': {'t': p('Hur många gram är 5600 mg?')},
    '0.226': {'t': p('Hur många liter är 1,8 m³?')},
    '0.227': {'t': p('Omvandla 750 l till m³.')},
    '0.228': {'t': p('Lisa ska omvandla <strong>2,5 m²</strong> till <strong>cm²</strong>. Vilket svar är rätt?')},
    '0.229': {'t': p('Omvandla 36000 cm² till m².')},
    '0.230': {'t': p('Hur många timmar är 1,25 dygn?')},
    '0.231': {'t': p('Omvandla 3600 s till minuter.')},
    '0.311': {'t': p('En rektangel är 80 cm lång och 0,3 m bred. Beräkna arean i m².')},
    '0.312': {'t': p('Hur många m² är 0,08 km²?')},
    '0.409': {'t': p('Ett markområde på 0,003 km² ska delas upp i tomter som är 450 m² var. Minst 300 m² behövs till en '
                     'gemensam väg. Hur många hela tomter får plats som mest? Bortse från tomternas form.')},
    '0.410': {'t': p('Hur många sekunder är 2,5 h?')},
    '0.411': {'t': p('Moa skriver: ”45 000 cm² = 450 m², eftersom 100 cm = 1 m.” Förklara vad som är fel med hjälp av en '
                     'kvadrat med sidan 1 m. Hur många m² är 45 000 cm²?')},
    '0.502': {'t': p('Hur många millimeter är 0,48 m?')},
    '0.503': {'t': p('Omvandla 920 mm till meter.')},
    '0.504': {'t': p('Jonas skriver om en längd från kilometer till meter. Vad händer med längden och med talvärdet?')},
    '0.506': {'t': p('Omvandla 38 cm till mm.')},
    '0.507': {'t': p('Hur många centimeter är 465 mm?')},
    '0.508': {'t': p('Omvandla 1,7 dm till cm.')},
    '0.509': {'t': p('Hur många decimeter är 82 cm?')},
    '0.510': {'t': p('Omvandla 0,006 km till meter.')},
    '0.511': {'t': p('En kabel är 2,45 m lång. Den ska klippas i bitar som är 40 cm långa. För varje bit går dessutom 1 cm '
                     'kabel förlorad när man klipper. Hur många bitar kan man som mest få?')},
    '0.514': {'t': p('Hur många milligram är 6,2 g?')},
    '0.515': {'t': p('Omvandla 9350 mg till gram.')},
    '0.516': {'t': p('En burk rymmer högst 0,45 kg pärlor. Pärlorna säljs i påsar med 125 g i varje. Hur många hela påsar kan '
                     'man hälla i den tomma burken?')},
    '0.517': {'t': p('Hur många kilogram är 125 g?')},
    '0.518': {'t': p('Skriv 1,75 h i timmar och minuter.'), 'kg': 'Skriv timmar och minuter i var sitt fält.'},
    '0.519': {'t': p('Ahmed skriver att 2 h 30 min är 2,30 h. Hur många minuter för kort blir tiden om han räknar med 2,30 h?')},
    '0.520': {'t': p('Hur många sekunder är 7 min?')},
    '0.521': {'t': p('Omvandla 540 s till minuter.')},
    '0.522': {'t': p('En maskin ska gå totalt 2,5 dygn. Den går 8 timmar varje arbetsdag. Hur många arbetsdagar tar det?')},
    '0.523': {'t': p('Hur många dygn är 84 h?')},
    '0.524': {'t': p('Omvandla 2,8 l till dl.')},
    '0.525': {'t': p('Hur många liter är 46 dl?')},
    '0.528': {'t': p('Omvandla 3,6 dl till ml.')},
    '0.529': {'t': p('Hur många deciliter är 425 ml?')},
    '0.531': {'t': p('En bordsskiva har arean 3,75 m². Den ska täckas med papper, och varje pappersark har arean 2 500 cm². '
                     'Hur många ark behövs, om arken får klippas och inga bitar överlappar?')},
    '0.532': {'t': p('Omvandla 0,63 dm² till cm².')},
    '0.533': {'t': p('Hur många dm² är 840 cm²?')},
    '0.534': {'t': p('Omvandla 5,7 m² till dm².')},
    '0.535': {'t': p('Hur många m² är 925 dm²?')},
    '0.536': {'t': p('En karta visar ett kvadratiskt område med sidan 2 cm. Kartans skala är 1:1 000. Hur stor är områdets '
                     'verkliga area i m²?')},
    '0.537': {'t': p('Omvandla 1 250 000 m² till km².')},
    '0.538': {'t': p('Hur många mm² är 18 cm²?')},
    '0.539': {'t': p('Omvandla 4600 mm² till cm².')},
    '0.540': {'t': p('Sidan i en kvadrat skrivs om från meter till centimeter, och arean skrivs i kvadratcentimeter i stället för kvadratmeter. '
                     'Vilket påstående om arean stämmer?')},
    '0.542': {'t': p('Hur många mm² är 2,08 dm²?')},
    '0.544': {'t': p('Elsa och Hugo ska omvandla samma area från m² till cm². Elsa multiplicerar talvärdet med 100 och Hugo '
                     'med 10 000. För vilka areor får de samma talvärde? Hur förhåller sig deras svar till varandra för '
                     'alla positiva areor?')},
    '0.545': {'t': p('Omvandla 3,2 dm³ till cm³.')},
    '0.546': {'t': p('Hur många dm³ är 8750 cm³?')},
    '0.547': {'t': p('Omvandla 0,006 m³ till dm³.')},
    '0.548': {'t': p('Hur många m³ är 425 dm³?')},
    '0.549': {'t': p('Omvandla 0,014 m³ till cm³.')},
    '0.550': {'t': p('Hur många m³ är 235 000 cm³?')},
    '0.551': {'t': p('Ett akvarium är 40 cm långt, 25 cm brett och 30 cm högt invändigt. Det fylls med vatten till höjden '
                     '20 cm. Hur många liter vatten finns i akvariet?')},
    '0.552': {'t': p('Omvandla 96 cm³ till dm³.')},
    '0.553': {'t': p('En låda med raka sidor har den invändiga bottenarean 0,08 m². Hur många centimeter hög måste lådan '
                     'vara invändigt för att rymma 12 liter?')},
    '0.554': {'t': p('Leo säger: ”1 m³ är 100 l, eftersom 1 m är 100 cm.” Vilken förklaring visar vad som är fel?')},
    '0.555': {'t': p('En pump fyller ett tomt kärl med 0,45 liter vatten per sekund. Kärlet rymmer 0,018 m³. Hur lång tid '
                     'tar det att fylla kärlet?')},
    '0.556': {'t': p('En tank innehåller 725 liter vatten. Vattnet ska hällas över i kärl som rymmer 0,08 m³ vart. Hur många '
                     'kärl kan fyllas helt, och hur många liter blir över?')},
    '0.557': {'t': p('Två behållare rymmer lika mycket. Den ena rymmer 2 500 cm³ och den andra x liter. Vad är x?')},
    '0.558': {'t': p('En rätblocksformad låda har måtten x, y och z centimeter. Sara påstår att volymen i liter är '
                     'xyz/100. Visa på två olika sätt vilken formel som är rätt, och förklara hur stort Saras fel blir. '
                     'En ny längdenhet är k cm, där k &gt; 0. För vilka k ger produkten av lådans tre mått i den nya '
                     'enheten direkt volymen i liter? Motivera att du har hittat alla möjligheter.')},
    '0.559': {'t': p('En låda är 0,4 m lång, 25 cm bred och 2 dm hög. Omar multiplicerar 0,4 · 25 · 2 och skriver svaret '
                     '20 l. Svaret råkar vara rätt. Förklara varför enhetsfelen tar ut varandra. Fungerar metoden alltid '
                     'när ett mått anges i m, ett i cm och ett i dm?')},
    '0.560': {'t': p('Omvandla 2500 ml till m³.'), 'kg': VANLIGT},
    '0.561': {'t': p('Hur många milliliter är 0,018 m³?')},
    '0.562': {'t': p('Omvandla 75 ml till m³.'), 'kg': VANLIGT},
    '0.565': {'t': p('En tom tank rymmer 0,85 m³. Den fylls från två kranar samtidigt. Den ena kranen ger 12 l/min och den '
                     'andra 500 ml/s. Hur många minuter tar det att fylla tanken?')},
    '0.567': {'t': p('En pump fyller 12 500 ml på 25 s. En annan pump fyller 0,018 m³ på en minut. Hur många liter mer per '
                     'minut ger den snabbare pumpen?')},
    '0.568': {'t': p('En pump ger p ml/s under t minuter, där p och t är positiva. Ta fram en formel för volymen V i m³. '
                     'Emil föreslår V = pt/1 000. Kan Emils formel ge rätt svar för några positiva p och t? Hur förhåller '
                     'sig hans svar till det rätta?')},
    '0.569': {'t': p('Hur många milliliter är 0,000008 m³?')},
    '0.570': {'t': p('Omvandla 2,7 g/cm³ till kg/m³.')},
    '0.571': {'t': p('Ett material har densiteten 0,92 g/cm³. Hur många gram väger en bit av materialet som har volymen '
                     '0,5 liter?')},
    '0.572': {'t': p('Omvandla 7850 kg/m³ till g/cm³.')},
    '0.574': {'t': p('Två material har densiteterna 1,05 g/cm³ och 950 kg/m³. Hur många gram mer väger 2 liter av det tätare '
                     'materialet än 2 liter av det andra?')},
    '0.575': {'t': p('En massiv metallbit har massan 567 g och volymen 50 cm³. Beräkna metallens densitet i kg/m³.')},
    '0.576': {'t': p('Ida säger: ”Om man byter från g/cm³ till kg/m³ blir talvärdet mindre, eftersom kilogram är en större '
                     'enhet.” Förklara varför Ida har fel, och visa vilken omvandlingsfaktor som gäller.')},
    '0.580': {'t': p('Omvandla 5 m/s till km/h.')},
    '0.581': {'t': p('Hur många m/s är 72 km/h?')},
    '0.582': {'t': p('En cyklist håller farten 12,5 m/s i 4 minuter. Hur många kilometer cyklar hon?')},
    '0.583': {'t': p('En bil kör 1,5 km på 90 s med konstant hastighet. Vilken hastighet har bilen i km/h?')},
    '0.584': {'t': p('Anna går med farten 0,8 m/s och Bertil med farten 3 km/h. De startar samtidigt. Hur många meter längre '
                     'har den snabbare av dem gått efter 5 minuter?')},
    '0.585': {'t': p('Filip multiplicerar med 3,6 både när han omvandlar från m/s till km/h och när han omvandlar tillbaka. '
                     'Efter en omvandling åt varje håll får han 129,6 m/s. Vilken hastighet i m/s började han med, och vad '
                     'är den hastigheten i km/h?')},
    '0.586': {'t': p('Nora omvandlar en hastighet från m/s till km/h och sedan tillbaka. I första steget multiplicerar hon '
                     'talvärdet med a och i andra steget med b, där a, b &gt; 0. Hon får alltid tillbaka det tal hon '
                     'började med. Bevisar det att båda omvandlingarna är rätt? Ge ett motexempel, ange när hon alltid får '
                     'tillbaka startvärdet och förklara vilken kontroll som också behövs.')},
    '0.1118': {'t': p('Jämför längderna \\(0{,}4\\,\\text{m}\\), \\(8\\,\\text{cm}\\), \\(70\\,\\text{mm}\\), '
                      '\\(1{,}2\\,\\text{dm}\\) och \\(5\\,\\text{dm}\\).',
                      'a) Vilken längd är längst? Skriv den i meter.', 'b) Vilken längd är kortast? Skriv den i meter.'),
               'd': {'a': {'t': p('Jämför längderna \\(0{,}4\\,\\text{m}\\), \\(8\\,\\text{cm}\\), \\(70\\,\\text{mm}\\), '
                                  '\\(1{,}2\\,\\text{dm}\\) och \\(5\\,\\text{dm}\\).', 'Vilken längd är längst? Skriv den i meter.')},
                     'b': {'t': p('Jämför längderna \\(0{,}4\\,\\text{m}\\), \\(8\\,\\text{cm}\\), \\(70\\,\\text{mm}\\), '
                                  '\\(1{,}2\\,\\text{dm}\\) och \\(5\\,\\text{dm}\\).', 'Vilken längd är kortast? Skriv den i meter.')}}},
    '0.1119': {'t': p('Jämför längderna \\(0{,}3\\,\\text{m}\\), \\(14\\,\\text{cm}\\), \\(95\\,\\text{mm}\\), '
                      '\\(1{,}1\\,\\text{dm}\\) och \\(4\\,\\text{dm}\\).',
                      'a) Vilken längd är längst? Skriv den i meter.', 'b) Vilken längd är kortast? Skriv den i meter.'),
               'd': {'a': {'t': p('Jämför längderna \\(0{,}3\\,\\text{m}\\), \\(14\\,\\text{cm}\\), \\(95\\,\\text{mm}\\), '
                                  '\\(1{,}1\\,\\text{dm}\\) och \\(4\\,\\text{dm}\\).', 'Vilken längd är längst? Skriv den i meter.')},
                     'b': {'t': p('Jämför längderna \\(0{,}3\\,\\text{m}\\), \\(14\\,\\text{cm}\\), \\(95\\,\\text{mm}\\), '
                                  '\\(1{,}1\\,\\text{dm}\\) och \\(4\\,\\text{dm}\\).', 'Vilken längd är kortast? Skriv den i meter.')}}},
    '0.1120': {'t': p('Jämför längderna \\(0{,}65\\,\\text{m}\\), \\(42\\,\\text{cm}\\), \\(180\\,\\text{mm}\\), '
                      '\\(2{,}5\\,\\text{dm}\\) och \\(7\\,\\text{dm}\\).',
                      'a) Vilken längd är längst? Skriv den i meter.', 'b) Vilken längd är kortast? Skriv den i meter.'),
               'd': {'a': {'t': p('Jämför längderna \\(0{,}65\\,\\text{m}\\), \\(42\\,\\text{cm}\\), \\(180\\,\\text{mm}\\), '
                                  '\\(2{,}5\\,\\text{dm}\\) och \\(7\\,\\text{dm}\\).', 'Vilken längd är längst? Skriv den i meter.')},
                     'b': {'t': p('Jämför längderna \\(0{,}65\\,\\text{m}\\), \\(42\\,\\text{cm}\\), \\(180\\,\\text{mm}\\), '
                                  '\\(2{,}5\\,\\text{dm}\\) och \\(7\\,\\text{dm}\\).', 'Vilken längd är kortast? Skriv den i meter.')}}},
    '0.1124': {'t': p('En cyklist håller farten 36 km/h i 20 minuter. Hur många kilometer cyklar hon?')},
    '0.1125': {'t': p('Pelle cyklar med farten 18 km/h i 40 minuter. Hur många kilometer hinner han?')},
    '0.1126': {'t': p('En bil kör med farten 72 km/h i 25 minuter. Hur många kilometer kör bilen?')},
    '0.1136': {'t': p('Det finns 3 rör som är 2,4 m långa. Ur dem kapas 5 bitar som är 85 cm långa. Hur många meter rör '
                      'blir över totalt? Bortse från spill när bitarna kapas.')},
    '0.1137': {'t': p('Alva har 4 brädor som är 1,8 m långa. Hon kapar 6 bitar som är 75 cm långa. Hur många meter bräda blir '
                      'över totalt? Bortse från spill när bitarna kapas.')},
    '0.1138': {'t': p('Det finns 3 kablar som är 2,5 m långa. Ur dem klipps 7 bitar som är 80 cm långa. Hur många meter kabel '
                      'blir över totalt? Bortse från spill när bitarna klipps.')},
    '0.1145': {'t': p('En kran droppar en gång varannan sekund. Varje droppe är 0,25 ml. Hur många liter vatten droppar ut på '
                      'ett år (365 dygn)?')},
    '0.1146': {'t': p('En kran läcker en droppe var tredje sekund. Varje droppe är 0,4 ml. Hur många liter vatten läcker ut på '
                      '30 dygn?')},
    '0.1147': {'t': p('En kran läcker en droppe var femte sekund. Varje droppe är 0,2 ml. Hur många liter vatten läcker ut på '
                      'en vecka?')},
}
