"""Deluppgiftskedjor i Fy1 (2026-11-27, felrapport 2.52: ”frågan kommer igen i c) men inte b)”).

Kunskapsgymmet visar delkorten som en kedja a → b → c och visar bara det som skiljer varje dels text från de
föregående. När en del hade en egen, förkortad inledning (ofta a på träningsnivå 1) eller ett ändrat tal i
inledningen (2.52 c: 30 kg i stället för 15 kg) visades hela situationen igen. Regeln sedan 2026-11 är att alla
delkort börjar med exakt samma inledning (spelIntro) och att det som ändras, och behövda mellanresultat, står i
delens fråga.

KEDJA = {id: {etikett: fråga}}: 's' = delens egna meningar (det som inte står i inledningen) följt av den gamla
frågan; en sträng = ny fråga, skriven för hand; utelämnad etikett = frågan är oförändrad. 'intro' byter spelIntro
(bara Kunskapsgymmet). HOPPA = uppgifter vars inledning bara är ett förbehåll eller en instruktion, där delarna är
fristående situationer och visas hela, som avsett.
"""

# 3.73 och 3.93: varje delkort har en egen figur med bara delens givna värden (fellogg 2026-11-04) och behålls.
HOPPA = {'3.73', '3.93', '3.392', '5.209', '5.476', '5.477', '5.488', '6.458', '6.483', '6.539', '7.140', '8.482', '4.597', '5.558',
         '5.564', '6.505'}

# Delar med ett ändrat kraftläge behåller sin egen text utan inledningens kraftbild (beslut som skyddas av
# fysik1-newton2 och fysik1-kapitel4: ett ensamt delkort får inte visa en kraftbild som motsäger frågan).
EGEN_TEXT = {('4.31', 'c'), ('4.31', 'd'), ('4.53', 'd'), ('4.88', 'd'), ('4.98', 'c'), ('4.206', 'c'), ('4.237', 'd')}

# Genomlästa: delarnas egna inledningar är förkortade versioner av samma situation, så frågorna behålls och
# delarna får den gemensamma inledningen.
BEHALL = set('''3.89 3.146 3.193 3.200 3.202 3.208 3.311 3.390 4.29 4.30 4.112 4.153 4.155 4.166 4.168 4.169 4.187 4.190
4.208 4.279 4.286 4.519 4.529 4.569 4.624 4.635 4.680 5.14 5.18 5.24 5.36 5.60 5.62 5.77 5.84 5.91 5.95 5.99 5.120
5.126 5.132 5.138 5.160 5.166 5.170 5.211 5.214 5.228 5.239 5.382 5.398 5.413 5.431 5.461 5.474 5.484 5.528 5.530
5.533 5.534 5.565 5.583 6.4 6.15 6.16 6.22 6.73 6.74 6.87 6.113 6.115 6.117 6.118 6.119 6.122 6.125 6.201 6.367 6.448
6.468 6.508 6.543 7.194 8.120 9.91 3.93 4.650 4.653 4.700 5.108 5.149 5.222 5.224 5.418 5.438 5.439 5.480 5.499
5.511 7.82 7.102 7.159 7.223 7.224 4.577 9.96 7.144 8.406 4.644'''.split())

KEDJA = {
    '2.17': {},  # c: ”Ange rätblockets densitet i kg/m³.” (annan session, 23a4c99)
    '2.26': {},  # d: ”Ange kubens densitet i kg/m³.” (annan session, 23a4c99)
    '3.46': {'c': 'En person går i stället nedåt i rulltrappan med 0,75 m/s i förhållande till trappstegen. '
                  'Vilken hastighet har personen relativt marken?'},
    '3.73': {'intro': '<p>Ett flygplan startar från stillastående och accelererar med 2,5 m/s² längs en 800 m lång '
                      'startbana. Planet lyfter när farten är 65 m/s.</p>',
             'a': 'Hur lång tid tar det att nå 65 m/s?',
             'b': 'Hur lång sträcka skulle behövas för att nå 65 m/s?',
             'c': 'Vilken fart har planet när det har rullat 800 m?',
             'd': 'Vilken konstant acceleration skulle behövas för att farten ska bli 65 m/s efter 800 m?'},
    '3.93': {'b': 'Accelerationen är 2,0 m/s². Hur lång tid tar det att nå lyftfarten?',
             'c': 'Ett tyngre flygplan har samma acceleration, 2,0 m/s², men behöver farten 78 m/s för att lyfta. '
                  'Hur lång startsträcka behöver det?'},
    '3.197': {'a': 's', 'b': 's', 'c': 's', 'd': 's', 'e': 's'},
    '3.199': {'b': 'Kundvagnen har farten 2,30 m/s när inbromsningen börjar. Hur mycket minskar farten per sekund?'},
    '3.218': {'a': 'Bestäm den första vagnens medelacceleration.', 'b': 'Bestäm den andra vagnens medelacceleration.'},
    '3.311': {'c': 'Det tar 50 s att simma över. Hur långt nedströms driver simmaren?'},
    '3.375': {'b': 'Den högsta farten är 25,28 m/s. Hur lång tid går från fartökningens början tills bilen står still?',
              'c': 'Den högsta farten är 25,28 m/s. Hur långt kör bilen totalt?'},
    '3.386': {'a': 's', 'b': 's', 'c': 's', 'd': 'Hur lång tid tar det för bilen i c att öka farten från 11 m/s till 29 m/s?'},
    '4.31': {'c': 'Hur stor blir kraftsumman om båda krafterna är riktade åt höger?'},
    '4.37': {'c': 'Ett annat föremål påverkas av tyngdkraften 24,6 N på jorden. Hur stor massa har det?'},
    '4.165': {'d': 'I en annan krock bromsas samma bil från 14 m/s till stillastående på 0,20 m. Hur stor är bromskraften då?'},
    '4.281': {'d': 'Med en passagerare är massan 300 kg. Hur stor blir accelerationen med samma kraftsumma, 660 N?'},
    '4.526': {'a': 'Den första klossen har massan 1,97 kg och dras med 9,2 N. Bestäm glidfriktionstalet.',
              'b': 'Den andra klossen har massan 8,8 kg och glidfriktionstalet är 0,25. Vilken dragkraft krävs?',
              'c': 'För den tredje klossen är glidfriktionstalet 0,67 och dragkraften 75 N. Vilken massa har klossen?'},
    '4.564': {'c': 'Lådorna byter plats, så att kraften på 650 N trycker lådan på 125 kg mot lådan på 65 kg. '
                   'Hur stor är kontaktkraften på lådan på 65 kg då?'},
    '4.583': {'b': 'Friktionskraften är 5,292 N. Bestäm glidfriktionstalet.',
              'c': 'Klossen släpps och glider nedför planet. Glidfriktionstalet är 0,11. Bestäm accelerationen nedför planet.'},
    '4.625': {'b': 'Dragrepet går av när skidåkaren är på väg uppför. Hur stor är accelerationen längs backen direkt efteråt?'},
    '4.629': {'b': 'Kraften i vajern är 5,96 kN. Hur stor är normalkraften från vägen?'},
    '4.650': {'b': 'Snöret drar med 35,34 N. Bestäm B:s massa.'},
    '4.654': {'c': 'Motorn slutar driva och bilens bromsar ger 400 N bakåt. Bestäm kraften från kopplingen på släpet.'},
    '4.700': {'intro': '<p>En förare med massan 68 kg bromsas från 95 km/h till stillastående. Bromsaccelerationen är '
                       'konstant och har storleken \\(30g\\).</p>'},
    '4.718': {'c': 'Bollen kastas i stället uppåt. På väg upp är luftmotståndet 21 N. Bestäm accelerationens storlek.'},
    '5.23': {'c': 's'},
    '5.24': {'d': 'Vilken fart skulle pulkan få vid foten om det inte fanns någon friktion eller något luftmotstånd?'},
    '5.32': {'a': 'Hur stor rörelsemängd har bollen före studsen?', 'b': 'Hur stor rörelsemängd har bollen efter studsen?'},
    '5.45': {'a': 'Hur stor lägesenergi har fågeln på 15 m höjd, räknat från marken?',
             'b': 'Hur stor lägesenergi har fågeln på 30 m höjd, räknat från marken?'},
    '5.46': {'a': 's', 'b': 's', 'c': 's'},
    '5.72': {'c': 'Tolv likadana lådor lyfts 1,8 m var. Hur stort är det totala lyftarbetet?'},
    '5.108': {'c': 'Kulan skjuts i stället rakt uppåt. Hur högt över slangbellan kommer den?'},
    '5.117': {'a': 'Hur stor är den resulterande kraften på passageraren i genomsnitt om inbromsningen tar 0,12 s?',
              'b': 'Hur stor är den resulterande kraften på passageraren i genomsnitt om inbromsningen tar 0,020 s?'},
    '5.118': {'d': 'Efter kopplingen har vagnarna farten 1,00 m/s. Hur stor är kraften mellan vagnarna i genomsnitt '
                   'under kopplingen?'},
    '5.147': {'c': 'Körningen tar 1,6 timmar. Hur stor medeleffekt tas ut ur batteriet?'},
    '5.149': {'a': 'Lampan lyser i 15 minuter. Hur mycket elektrisk energi tar den emot?',
              'b': 'Lampan lyser i 6,0 timmar. Hur många kWh tar den emot?'},
    '5.157': {'a': 'Det ena föremålet har massan 12 kg. Vilken fart har det?',
              'b': 'Det andra föremålet har farten 3,0 m/s. Hur stor massa har det?'},
    '5.189': {'a': 'En kraft på 178 N skjuter kärran 3,00 m. Hur stort arbete gör kraften?',
              'b': 'En kraft på 120 N gör arbetet 534 J på kärran. Hur långt flyttas kärran?',
              'c': 'En kraft gör arbetet 534 J när kärran flyttas 2,5 m. Hur stor är kraften?'},
    '5.194': {'a': 'Lådan lyfts 5,0 m rakt uppåt. Hur stort arbete uträttar lyftkraften?',
              'b': 'Lådan dras i stället 5,0 m över ett golv. Friktionstalet är 0,55. Hur stort arbete uträttar dragkraften?'},
    '5.222': {'b': 'Friktionen omvandlar 34,21 J mekanisk energi mellan A och B. Hur stort är friktionstalet?'},
    '5.224': {'b': 'Planet lutar i stället 40° och startfarten är 8,0 m/s. Den bromsande kraften är 1,4457 N. '
                   'Hur långt upp längs planet kommer klossen?'},
    '5.418': {'b': 'Puck A hade farten 0,79 m/s före krocken. Hur mycket rörelseenergi omvandlas till andra energiformer?'},
    '5.438': {'b': 'De glider vidare med farten 4,0 m/s. Hur mycket minskar deras totala rörelseenergi?'},
    '5.439': {'b': 'Efter krocken har den tyngre vagnen farten 5,0 m/s. Hur mycket ändras den totala rörelseenergin?'},
    '5.480': {'c': 'Hon hoppar i stället med farten 3,00 m/s snett uppåt. Vilken fart har hon precis innan hon når vattnet?'},
    '5.499': {'c': 'På en annan plats har vandraren lägesenergin 1,60 MJ. På vilken höjd över havet är vandraren?'},
    '5.511': {'b': 'Flygplanet får 164 MJ rörelseenergi. Hur stor är den resulterande kraften framåt i genomsnitt?',
              'c': 'De två motorerna ger en kraft på 117 kN var. Hur lång startsträcka skulle behövas om det inte fanns '
                   'något motstånd?',
              'd': 'Senare stiger flygplanet 10,5 km med konstant fart. Hur stort arbete går åt till att öka lägesenergin?'},
    '5.513': {'a': 'Hur mycket ökar rörelseenergin när farten ökar från 5,0 m/s till 10,0 m/s?',
              'b': 'Hur mycket ökar rörelseenergin när farten ökar från 10,0 m/s till 15,0 m/s?'},
    '6.469': {'intro': '<p>Föremålen hänger i en kraftmätare och hålls helt under ytan vid mätningen i vatten. Bortse '
                       'från luftens lyftkraft.</p>', 'a': 's', 'b': 's', 'c': 's'},
    '6.470': {'a': 's', 'b': 's', 'c': 's'},
    '6.474': {'a': 's', 'b': 's'},
    '6.480': {'a': 's', 'b': 's', 'c': 's', 'd': 's'},
    '6.482': {'a': 's', 'b': 's', 'c': 's'},
    '6.496': {'a': 's', 'b': 's', 'c': 's'},
    '6.506': {'a': 'Heliumets densitet är 0,179 kg/m³. En heliumballong ska precis kunna bära 180 kg last och ett hölje '
                   'med massan 10 kg. Vilken volym behövs?',
              'b': 'Vätgasens densitet är 0,090 kg/m³. En vätgasballong ska precis kunna bära 180 kg last och ett hölje '
                   'med massan 10 kg. Vilken volym behövs?',
              'c': 'Heliumets densitet är 0,179 kg/m³. En klotformad heliumballong har radien 7,15 m. Hölje och nät väger '
                   'tillsammans 930 kg. Hur stor last kan den bära?',
              'd': 'Heliumets densitet är 0,179 kg/m³. En klotformad heliumballong ska precis kunna bära 7,70 ton last. '
                   'Hölje, korg och nät väger tillsammans 196 kg. Vilken radie behövs?'},
    '7.45': {'a': 'Hur mycket energi avges när vattnet svalnar från 5,0 °C till 0 °C?',
             'b': 'Hur mycket energi avges när vattnet fryser vid 0 °C?',
             'c': 'Hur mycket energi avges när isen svalnar från 0 °C till −3,0 °C?'},
    '7.82': {'c': 'Sluttemperaturen blir 24,355 °C med koppar och 29,489 °C med aluminium. Hur mycket högre blir '
                  'sluttemperaturen i aluminiumförsöket?'},
    '7.102': {'b': 'Uppvärmningen kräver 33,44 kJ. Hur många gånger större är energin för förångningen än energin för '
                   'uppvärmningen?'},
    '7.137': {'a': 's', 'b': 's', 'c': 's'},
    '7.139': {'a': 's', 'b': 's', 'c': 's'},
    '7.159': {'a': 'Värmaren är på i 2 minuter. Vilken temperatur får vattnet?'},
    '7.166': {'a': 's', 'b': 's'},
    '7.167': {'a': 's', 'b': 's'},
    '7.176': {'a': 's', 'b': 's', 'c': 's'},
    '7.177': {'a': 's', 'b': 's', 'c': 's'},
    '7.218': {'a': 's', 'b': 's', 'c': 's'},
    '7.221': {'a': 's', 'b': 's', 'c': 's'},
    '7.223': {'a': 'Isen blandas med 200 g vatten vid 35 °C. Vilken blir sluttemperaturen?',
              'b': 'Hur mycket vatten vid 35 °C behövs för att precis smälta isen?'},
    '7.224': {'a': 'Silvret kyls till 20 °C i vatten som från början är 10 °C och som också får temperaturen 20 °C. '
                   'Hur mycket vatten behövs?',
              'b': 'Hur mycket vatten behöver förångas om silvret i stället kyls till 100 °C genom att vatten vid '
                   '10 °C värms och förångas vid 100 °C?'},
    '8.101': {'c': 's'},
    '5.565': {'b': 'Bilen kör i stället uppför en backe och kommer 3,00 m högre upp under fartökningen. Hur lång tid '
                   'tar det då att nå 15,0 m/s?'},
    '5.583': {'a': 'Hur stor effekt krävs när vagnen dras med den konstanta farten 2,20 m/s?'},
    '5.574': {'a': 'Cyklisten rullar utan att trampa nedför en backe som lutar 3,0° och håller den konstanta farten '
                   '3,5 m/s. Bestäm k.',
              'b': 'Anta att k = 3,4 kg/m. Hur stor effekt krävs för att cykla med den konstanta farten 2,0 m/s uppför '
                   'en backe som lutar 1,5°?'},
    '5.482': {'a': 's', 'b': 's'},
    '5.508': {'b': 's'},
    '4.604': {'b': 's'},
    '5.405': {'a': 'Båten ligger först stilla. Vilken fart får båten med Olle?',
              'b': 'Båten rör sig i stället först mot bryggan med farten 2,0 m/s. Vilken fart får båten med Olle?',
              'c': 'Båten rör sig i stället först bort från bryggan med farten 2,0 m/s. Vilken fart får båten med Olle?'},
    '5.440': {'a': 'Pilen fastnar i äpplet. Vilken fart får pilen och äpplet?',
              'b': 'Pilen fastnar i äpplet, och efteråt är farten 3,03 m/s. Hur mycket rörelseenergi omvandlas till '
                   'andra energiformer?',
              'c': 'Pilen går i stället rakt igenom äpplet och fortsätter åt samma håll med farten 23 m/s. Vilken fart '
                   'får äpplet?'},
    '5.453': {'b': 'Det nedre steget får farten 4 500 m/s framåt. Hur mycket ökar stegens totala rörelseenergi?'},
    # Delfrågor som själva upprepade inledningens data (kapitel 8 och 9)
    '8.13': {'b': 'Den yttre resistansen är 0,60 Ω. Bestäm effekten i resistorn.'},
    '8.27': {'a': 'Hur stor laddning motsvarar batteriets kapacitet?',
             'b': 'Batteriet kan ge laddningen 7 200 C. Hur mycket energi kan det ge?',
             'c': 'Batteriet driver strömmen 150 mA. Hur länge räcker det?'},
    '8.156': {'a': 'Hur stor laddning motsvarar batteriets kapacitet?',
              'b': 'Batteriet kan ge laddningen 7 200 C. Hur mycket energi kan det ge?',
              'c': 'Batteriet driver strömmen 450 mA. Hur länge räcker det?'},
    '8.44': {'a': 'Bestäm det inre spänningsfallet.',
             'b': 'Det inre spänningsfallet är 0,60 V. Bestäm polspänningen.',
             'c': 'Polspänningen är 8,4 V. Bestäm den yttre resistansen.',
             'd': 'Batteriet kopplas bort från kretsen. Vilken är polspänningen då?'},
    '8.45': {'a': 'Vilken total elektrisk effekt ger batteriet?',
             'b': 'Vilken effekt blir värme inne i batteriet?',
             'c': 'Batteriet ger totalt 36 W, och 3,6 W blir värme inne i batteriet. Vilken effekt går till den yttre '
                  'kretsen?',
             'd': 'Av den totala effekten 36 W går 32,4 W till den yttre kretsen. Hur många procent är det?'},
    '8.87': {'a': 'Bestäm spänningen över var och en av resistorerna.',
             'b': 'Bestäm strömmen genom var och en av resistorerna.',
             'c': 'Bestäm ersättningsresistansen.'},
    '8.93': {'b': 'Batteriet driver en resistor på 2,7 Ω. Bestäm strömmen.',
             'c': 'Strömmen är 0,50 A. Bestäm polspänningen.'},
    '8.97': {'a': 'Hur långt räcker batteriet utan kupévärme?',
             'b': 'Hur mycket energi använder kupévärmaren när bilen kör 100 km?',
             'c': 'Med kupévärme använder bilen 20,5 kWh per 100 km. Hur långt räcker batteriet?'},
    '8.99': {'a': 'Batterierna seriekopplas med resistorn. Bestäm strömmen.',
             'b': 'Batterierna parallellkopplas och kopplas till resistorn. Bestäm strömmen genom resistorn.',
             'c': 'Resistorn får strömmen 0,625 A med seriekopplade batterier och 0,245 A med parallellkopplade. Vilken '
                  'koppling ger störst effekt i resistorn?'},
    '8.456': {'a': 'Vilken effekt blir värme i ledningen vid 12 kV?', 'b': 'Vilken effekt blir värme i ledningen vid 50 kV?'},
    '9.2': {'a': 'Hur många procent passerar ett 3,6 cm tjockt blyskikt?',
            'b': 'Hur många procent passerar ett 6 cm tjockt blyskikt?'},
    '9.13': {'a': 'Hur många procent passerar ett 2,4 cm tjockt blyskikt?',
             'b': 'Hur många procent passerar ett 6 cm tjockt blyskikt?',
             'c': 'Hur tjockt blyskikt behövs för att bara 1,0 % ska passera?'},
    '9.21': {'a': 'Hur många elektroner finns kvar?', 'b': 'Vilken laddning får jonen?',
             'c': 'Vad händer med atomkärnan?'},
    '9.27': {'a': 'Hur mycket av isotopen återstår efter 30 minuter?',
             'b': 'Hur mycket av isotopen återstår efter 45 minuter?'},
    '9.41': {'a': 'Bestäm aktiviteten efter 5,27 år.', 'b': 'Bestäm aktiviteten efter 10,5 år.',
             'c': 'Bestäm aktiviteten efter 15,8 år.'},
    '9.58': {'b': 'Hur lång tid från nu tar det innan aktiviteten är 500 Bq?'},
    '9.72': {'a': 'Bestäm den frigjorda energin när kalium-40 beta-minus-sönderfaller till kalcium-40.',
             'b': 'Bestäm den frigjorda energin när kalium-40 blir argon-40, först genom beta-plus och sedan genom '
                  'elektroninfångning.'},
    '9.94': {'a': 'Vilken dos blir det på 40 år?', 'b': 'Vilken dos blir det per dygn?'},
    '9.329': {'a': 'Baryonen har laddningen +2 e. Hur många u-kvarkar har den?',
              'b': 'Baryonen har laddningen −1 e. Hur många u-kvarkar har den?'},
    # Delkort med samma fråga två gånger (2.55-typen)
    '4.88': {'d': 'Kraften på 20 N verkar i stället åt vänster på den högra klossen. Hur stor är kontaktkraften mellan '
                  'klossarna då?'},
    '4.98': {'c': 'Personen drar i stället rakt uppåt i lådan med 40 N. Hur stor är normalkraften från golvet då?'},
    '4.245': {'c': 'Avståndet mellan stödjepunkterna ändras till 0,10 m. Hur stor blir den horisontella kraften från '
                   'övre stödjepunkten?'},
    '4.570': {'c': 'Massorna byter plats: lådan på bordet har massan 3,0 kg och den hängande vikten 5,0 kg. '
                   'Bestäm accelerationen.'},
    '4.574': {'b': 'Accelerationen är 2,29 m/s². Hur stor är kraften i snöret till den hängande vikten?',
              'c': 'Accelerationen är 2,29 m/s². Hur stor är kraften i snöret mellan lådorna?'},
    '4.596': {'b': 'Vikten accelererar uppåt med 2,269 m/s². Hur stor är kraften i snöret?',
              'c': 'Massorna byter plats: lådan på planet har massan 3,6 kg och den hängande vikten 21 kg, som faller '
                   'nedåt. Bestäm accelerationen.'},
    '4.632': {'b': 'Vikten accelererar nedåt med 4,078 m/s². Hur stor är kraften i snöret?',
              'c': 'Massorna byter plats: lådan på planet har massan 5,0 kg och den hängande vikten 3,0 kg. '
                   'Bestäm accelerationen.'},
    '4.653': {'c': 'Bilen drar släpet uppför en backe med lutningen 5,0° och konstant fart. Luftmotståndet är detsamma. '
                   'Hur stor är kopplingskraften?',
              'd': 'Bilen drar släpet uppför en backe med lutningen 5,0° och konstant fart. Luftmotståndet är detsamma. '
                   'Vilken drivande kraft krävs?'},
    '4.749': {'b': 's', 'c': 'Samma sten släpps 1,0 m över asteroidens yta. Hur lång tid tar fallet där?'},
    '5.140': {'b': 'Hur många hela steg räcker energin till om all energi blir lägesenergi?',
              'c': 'Hur många hela steg räcker energin till om 20 % av energin blir lägesenergi?'},
    '6.76': {'b': 'Linorna har volymen 41,56 cm³. Hur stor massa har den mindre täta linan?',
             'c': 'Linorna har volymen 41,56 cm³. Hur stor massa har den tätare linan?'},
}
