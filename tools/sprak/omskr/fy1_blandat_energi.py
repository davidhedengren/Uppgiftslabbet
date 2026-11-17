# Fy1 blandade energiuppgifter (omr blandat_energi), omskrivet för hand 2026-11-17.
# Många uppgifter är på A-nivå där modellvillkoren behövs; där rättas bara AI-mönstren.
FIG = '<span class="fig">[F1]</span>'
H = 'Höger räknas som positiv riktning.'
U = 'Uppåt räknas som positiv riktning.'
F = 'Framåt räknas som positiv riktning.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def kort(ctx, fraga):
    return {'t': p(ctx, fraga), 'f': fraga}


R = {
    '2.36': {'t': p('En bensinbil förbrukar 0,58 liter bensin per mil. Bensin ger 9,7 kWh per liter. En elbil använder 18 kWh per 100 km.',
                    'a) Hur många liter bensin går åt på 100 km?', 'b) Hur mycket energi tillförs bensinbilen på 100 km?',
                    'c) Jämför den tillförda energin för de två bilarna på 100 km.'),
             'intro': p('En bensinbil förbrukar 0,58 liter bensin per mil. Bensin ger 9,7 kWh per liter. En elbil använder 18 kWh per 100 km.')},
    '3.58': {
        'li': ['Hur stor andel av energin finns kvar efter varje studs?', 'Hur högt kommer bollen efter fem studsar?',
               'Hur lång sträcka färdas bollen totalt innan den ligger stilla?'],
        'efter': p('Bortse från luftmotståndet. Du får använda summan r + r² + r³ + … = r/(1 − r), som gäller för 0 &lt; r &lt; 1.')},
    '5.90': {
        'fore': p('En person som väger 70 kg står stilla på friktionsfri is och håller en boll som väger 3,0 kg. Personen kastar bollen horisontellt framåt med farten 8,0 m/s.'),
        'li': ['Vilken hastighet får personen efter kastet?',
               'Beräkna personens och bollens rörelseenergi efter kastet. Förklara hur de kan ha rörelseenergi fast den totala rörelsemängden är noll.']},
    '5.91': {
        'intro': p('En bil kör med den konstanta farten 25 m/s på en plan väg. Motorns nyttiga effekt är 30 kW.'),
        'd': {'a': {'f': 'Hur stor är drivkraften?'},
              'b': {'t': p('En bil kör med konstant fart på en plan väg. Drivkraften är 1200 N.', 'Hur stora är de bromsande krafterna tillsammans?'),
                    'f': 'Drivkraften är 1200 N. Hur stora är de bromsande krafterna tillsammans?'},
              'c': {'f': 'Hur stort arbete uträttar motorn på 1,0 km?'}}},
    '5.92': {
        'fore': p('En boll som väger 0,40 kg rullar åt höger med farten 3,0 m/s och studsar mot en vägg. Den studsar tillbaka med samma fart. Studsen varar i 12 ms.') + FIG,
        'li': ['Hur stor rörelsemängd har bollen före och efter studsen? Hur stor är väggens medelkraft på bollen?',
               'Hugo påstår: ”Rörelseenergin bevaras, alltså bevaras också bollens rörelsemängd.” Har han rätt? Motivera ditt svar.']},
    '5.93': {
        'fore': p('En vagn som väger 2,0 kg står stilla. Grafen visar den resulterande kraften på vagnen: 2,0 N åt höger under 0–2,0 s, noll under 2,0–3,0 s, 2,5 N åt vänster under 3,0–5,0 s och sedan noll.') + FIG,
        'li': ['Vilken hastighet har vagnen vid t = 2,0 s och vid t = 5,0 s?',
               'När under tiden med kraften åt vänster är rörelseenergin minst? Hur stor är den minsta rörelseenergin, och hur stor är rörelseenergin vid t = 5,0 s?',
               'Förklara varför en kraft åt vänster inte alltid minskar rörelseenergin.']},
    '5.94': {
        'fore': p('Ett hammarhuvud som väger 0,60 kg rör sig med farten 6,0 m/s och träffar en spik. Hammaren stannar efter 8,0 mm.'),
        'li': ['Hur stor rörelseenergi har hammaren innan den träffar spiken, och hur stor är bromskraften i genomsnitt över stoppsträckan?',
               'Kan du beräkna hur lång tid inbromsningen tar med de här uppgifterna? Motivera ditt svar.',
               'Hur lång tid tar inbromsningen om bromskraften är konstant?']},
    '5.95': {
        'intro': p('En cyklist och cykeln väger tillsammans 80 kg. Cyklisten rullar från stillastående nedför en 90 m lång backe som är 12 m hög och har farten 12 m/s längst ner. Cyklisten trampar inte.'),
        'd': {'a': kort('En cyklist och cykeln väger tillsammans 80 kg. Cyklisten rullar nedför en backe som är 12 m hög.', 'Hur mycket minskar lägesenergin?'),
              'b': kort('En cyklist och cykeln väger tillsammans 80 kg. Cyklisten rullar från stillastående nedför en backe som är 12 m hög och har farten 12 m/s längst ner. Cyklisten trampar inte.', 'Hur mycket mekanisk energi omvandlas till andra energiformer?'),
              'c': {'t': p('Längs en 90 m lång backe omvandlas 3667,2 J mekanisk energi till andra energiformer av bromsande krafter.', 'Hur stor är den bromsande kraften i genomsnitt?'),
                    'f': 'Längs backen omvandlas 3667,2 J mekanisk energi till andra energiformer. Hur stor är den bromsande kraften i genomsnitt?'}}},
    '5.96': {
        'fore': p('En skidlift drar skidåkare uppför en 800 m lång backe som lutar 25°. Varje minut börjar fyra åkare åka upp. Varje åkare väger 85 kg. Liften går med farten 2,0 m/s, och friktionstalet mellan skidorna och snön är 0,040. Liften har gått länge på det här sättet.'),
        'li': ['Hur stor medeleffekt krävs för att dra åkarna uppför backen?',
               'Liftens fart fördubblas, men det börjar fortfarande fyra åkare åka upp varje minut. Hur påverkas antalet åkare i backen och den medeleffekt som krävs?']},
    '5.97': {
        'intro': p('En fjäder står vertikalt och är hoptryckt 0,12 m. Fjäderkonstanten är 500 N/m. En kula som väger 0,080 kg ligger löst ovanpå fjädern. När fjädern släpps skjuts kulan rakt uppåt. Bortse från luftmotståndet.'),
        'd': {'b': {'f': 'Vilken fart har kulan när den lämnar fjädern?'},
              'c': {'f': 'Hur högt över startläget kommer kulan?'}}},
    '5.98': {
        'intro': p('En kloss som väger 6,0 kg glider på ett golv. Under 8,0 m minskar farten från 4,5 m/s till 3,0 m/s. Friktionskraften är konstant.'),
        'd': {'a': {'f': 'Hur stor är friktionskraften?'}, 'b': {'f': 'Hur stort är friktionstalet?'}}},
    '5.99': {
        'intro': p('En fjäder med fjäderkonstanten 250 N/m är hoptryckt 0,12 m. Fjädern skjuter iväg en vagn som väger 0,80 kg och står stilla. Vagnen fastnar sedan i en annan vagn som väger 1,20 kg och står stilla. Fram till krocken är spåret friktionsfritt. Efter krocken bromsas vagnarna av en konstant kraft och stannar efter 1,50 m.') + FIG,
        'd': {'a': kort('En fjäder med fjäderkonstanten 250 N/m är hoptryckt 0,12 m. Fjädern skjuter iväg en vagn som väger 0,80 kg och står stilla. Bortse från friktion.', 'Vilken fart får vagnen?'),
              'b': kort('En fjäder med fjäderkonstanten 250 N/m är hoptryckt 0,12 m. Fjädern skjuter iväg en vagn som väger 0,80 kg och står stilla. Vagnen fastnar sedan i en annan vagn som väger 1,20 kg och står stilla. Bortse från friktion.[F1]', 'Vilken fart har vagnarna efter krocken?'),
              'c': {'f': 'Hur stor är bromskraften efter krocken?'}}},
    '5.100': {
        'intro': p('En gevärskula som väger 0,020 kg har farten 150 m/s och tränger 0,080 m in i en träplanka innan den stannar. Räkna med att bromskraften är konstant.'),
        'd': {'a': {'f': 'Hur stor är bromskraften?'},
              'b': kort('En gevärskula med farten 150 m/s bromsas till stillastående på 0,080 m. Bromskraften är konstant.', 'Hur lång tid tar inbromsningen?')}},
    '5.101': {'t': p('En kloss som väger 2,0 kg glider från stillastående nedför en friktionsfri bana. Banan är 0,80 m hög och planar ut längst ner. Där fastnar klossen i en kloss som väger 3,0 kg och ligger stilla. Klossarna glider sedan 1,20 m på plant underlag innan de stannar.') + FIG + p('Hur stort är friktionstalet på det plana underlaget?')},
    '5.102': {
        'fore': p('En kloss som väger 30 kg släpps på ett 4,0 m långt plan som lutar 25° och börjar glida nedför. Friktionstalet är 0,20.') + FIG,
        'li': ['Vilken fart har klossen längst ner? Använd energiprincipen.',
               'Kontrollera svaret med Newtons andra lag. Förklara varför massan inte påverkar slutfarten.']},
    '5.103': {
        'fore': p('En gevärskula skjuts horisontellt in i en träkloss som hänger stilla i en lätt tråd. Kulan fastnar. Bortse från luftmotståndet.'),
        'li': ['En kula med massan m fastnar i en kloss med massan M. Ta fram hur stor andel av kulans rörelseenergi som finns kvar direkt efter träffen.',
               'Kulan väger 0,012 kg och klossen 2,0 kg. Efter träffen svänger klossen upp 0,18 m. Vilken fart hade kulan före träffen?',
               'Nora använder energiprincipen ända från kulans rörelse före träffen till klossens högsta läge. Förklara vad som blir fel. Hur stor andel av rörelseenergin omvandlas vid träffen?']},
    '5.104': {'t': p('En vagn som väger 0,50 kg rullar på ett spår och fastnar i en vagn som står stilla. Direkt efter krocken är vagnarnas totala rörelseenergi 25 % av rörelseenergin före krocken.', 'Hur stor massa har den andra vagnen?')},
    '5.105': {'t': p('En hockeypuck som väger 0,25 kg och har farten 3,2 m/s krockar rakt med en puck som väger 0,40 kg och ligger stilla. Stöten är elastisk.', 'Hur många procent av den ursprungliga rörelseenergin får den andra pucken?')},
    '5.106': {'t': p('En kloss som väger 6,0 kg har farten 4,0 m/s när den kommer in på en 3,0 m lång sträcka där friktionstalet är 0,15. Efter den sträckan är underlaget friktionsfritt. Där trycker klossen ihop en fjäder med fjäderkonstanten 1200 N/m.') + FIG + p('Hur mycket trycks fjädern ihop som mest?')},
    '5.107': {
        'fore': p('En person som väger 60 kg hoppar ner på golvet. Tyngdpunkten faller 1,20 m innan fötterna når golvet. Sedan sjunker tyngdpunkten ytterligare antingen 0,020 m eller 0,40 m innan personen står still. Räkna med att golvets kraft är konstant under inbromsningen. Bortse från luftmotståndet.'),
        'li': ['Hur stor är golvets kraft på personen i de två fallen?',
               'Jämför golvets kraft med den resulterande bromsande kraften. Varför blir golvets kraft mindre när stoppsträckan är längre?']},
    '5.108': {
        'fore': p('En slangbella ger en kula som väger 0,025 kg rörelseenergin 12 J. Vid ett horisontellt skott tar accelerationen 0,040 s. Bortse från luftmotståndet.'),
        'li': ['Vilken fart har kulan?', 'Hur stor är den resulterande kraften på kulan i genomsnitt under skottet?',
               'Kulan skjuts i stället rakt uppåt och har rörelseenergin 12 J när den lämnar slangbellan. Hur högt kommer kulan?'],
        'intro': p('En slangbella ger en kula som väger 0,025 kg rörelseenergin 12 J. Vid ett horisontellt skott tar accelerationen 0,040 s. Bortse från luftmotståndet.'),
        'd': {'a': {'t': p('En kula som väger 0,025 kg lämnar en slangbella med rörelseenergin 12 J.', 'Vilken fart har kulan?')},
              'b': kort('En kula som väger 0,025 kg skjuts iväg horisontellt med en slangbella. Accelerationen tar 0,040 s, och kulan får rörelseenergin 12 J.', 'Hur stor är den resulterande kraften på kulan i genomsnitt under skottet?'),
              'c': kort('En kula som väger 0,025 kg skjuts rakt uppåt med en slangbella och har rörelseenergin 12 J när den lämnar slangbellan. Bortse från luftmotståndet.', 'Hur högt över slangbellan kommer kulan?')}},
    '5.109': {
        'fore': p('En hockeypuck som väger 0,17 kg ligger stilla. En klubba slår till pucken i 0,050 s, och kraften på pucken är i genomsnitt 90 N.') + FIG,
        'li': ['Vilken fart och rörelseenergi får pucken?',
               'Går det att bestämma hur långt pucken rör sig medan klubban slår? Visa med två olika kraftförlopp eller ett tydligt resonemang.',
               'Hur långt rör sig pucken under slaget om kraften är konstant?']},
    '5.110': {
        'intro': p('En modellraket väger 1,20 kg. Den startar från stillastående, och motorn ger en konstant kraft på 18,0 N rakt uppåt i 1,50 s. Sedan slutar motorn, och raketen fortsätter uppåt. Räkna med att massan inte ändras och bortse från luftmotståndet.'),
        'd': {'a': {'t': p('En modellraket väger 1,20 kg. Motorn ger kraften 18,0 N rakt uppåt.', 'Hur stor är den resulterande kraften på raketen medan motorn är igång?'),
                    'f': 'Hur stor är den resulterande kraften på raketen medan motorn är igång?', 'kg': U},
              'b': kort('En modellraket som väger 1,20 kg startar från stillastående. Motorn ger en konstant kraft på 18,0 N rakt uppåt i 1,50 s. Räkna med att massan inte ändras och bortse från luftmotståndet.', 'Vilken fart har raketen när motorn slutar?'),
              'c': {'f': 'Hur högt över startpunkten kommer raketen?'}}},
    '5.111': {
        'fore': p('En boll som väger 0,25 kg kastas rakt uppåt med farten 12 m/s. Bortse från luftmotståndet.'),
        'li': ['Hur högt kommer bollen, och hur lång tid tar det?', 'Visa att tyngdkraftens impuls fram till den högsta punkten är lika stor som ändringen av bollens rörelsemängd.']},
    '5.112': {
        'intro': p('En skidåkare glider med farten 14 m/s på plan mark och stannar efter 22 m. Friktionskraften är konstant. Bortse från luftmotståndet.'),
        'd': {'a': {'f': 'Hur stort är friktionstalet?'},
              'b': kort('En skidåkare glider med farten 14 m/s och bromsas till stillastående på 22 m med konstant retardation.', 'Hur lång tid tar det innan skidåkaren stannar?')}},
    '5.113': {
        'fore': p('En bil som väger 850 kg kör på en plan väg. Motorns nyttiga effekt är konstant 6,0 kW, och luftmotstånd och friktion bromsar med konstant 80 N.'),
        'li': ['Hur stor är drivkraften och accelerationen vid 5,0 m/s och vid 10 m/s?', 'Vilken är den högsta fart bilen kan nå?',
               'Förklara varför man inte kan räkna med konstant effekt ända från stillastående.']},
    '5.114': {
        'intro': p('En rulltrappa tar i genomsnitt 30 personer per minut upp 6,0 m. Varje person väger 65 kg. Av den elektriska energin blir 70 % lägesenergi hos personerna.'),
        'd': {'a': kort('En rulltrappa tar personer 6,0 m uppåt. Varje person väger 65 kg, och 30 personer kommer upp per minut.', 'Hur stor medeleffekt krävs för att öka personernas lägesenergi?'),
              'b': {'t': p('En rulltrappa ger den nyttiga effekten 1914,9 W. Verkningsgraden är 0,70.', 'Hur stor elektrisk effekt tar rulltrappan emot?'),
                    'f': 'Den nyttiga effekten är 1914,9 W och verkningsgraden 0,70. Hur stor elektrisk effekt tar rulltrappan emot?'}}},
    '5.115': {
        'intro': p('En sten som väger 3,0 kg faller 8,0 m ner i en sandlåda. Stenen tränger sedan 0,15 m ner i sanden innan den stannar. Bortse från luftmotståndet. Tyngdkraften verkar även när stenen bromsas i sanden.'),
        'd': {'a': {'t': p('En sten faller 8,0 m ner mot en sandlåda. Bortse från luftmotståndet.', 'Vilken fart har stenen precis innan den träffar sanden?')},
              'b': {'f': 'Hur stor är sandens kraft på stenen i genomsnitt under inbromsningen?'}}},
    '5.116': {'t': p('En fjäder med fjäderkonstanten 900 N/m är hoptryckt 0,150 m. Fjädern skjuter iväg en vagn som väger 1,80 kg och står stilla. Vagnen passerar sedan en 2,40 m lång sträcka där friktionstalet är 0,120. Direkt efter den sträckan fastnar vagnen i en annan vagn som väger 1,20 kg och står stilla. Utanför sträckan finns ingen friktion.', 'Vilken fart har vagnarna efter krocken?')},
    '5.117': {
        'fore': p('En passagerare som väger 75 kg åker med farten 14 m/s när bilen krockar. Passageraren bromsas till stillastående. Jämför två fall.'),
        'li': ['Hur stor är den resulterande kraften på passageraren i genomsnitt om inbromsningen tar 0,12 s?',
               'Hur stor är den resulterande kraften på passageraren i genomsnitt om inbromsningen tar 0,020 s?'],
        'intro': p('En passagerare som väger 75 kg åker med farten 14 m/s när bilen krockar. Passageraren bromsas till stillastående. Jämför två fall.'),
        'd': {'a': kort('En passagerare som väger 75 kg åker med farten 14 m/s och bromsas till stillastående på 0,12 s.', 'Hur stor är den resulterande kraften i genomsnitt på passageraren under inbromsningen?'),
              'b': kort('En passagerare som väger 75 kg åker med farten 14 m/s och bromsas till stillastående på 0,020 s.', 'Hur stor är den resulterande kraften i genomsnitt på passageraren under inbromsningen?')}},
    '5.118': {
        'fore': p('En järnvägsvagn som väger 40 000 kg rullar åt höger med farten 1,50 m/s och kopplas ihop med en vagn som väger 20 000 kg och står stilla. Kopplingen tar 0,50 s.') + FIG,
        'li': ['Hur stor är vagnarnas totala rörelsemängd före krocken?', 'Vilken hastighet får vagnarna efter krocken?',
               'Hur mycket rörelseenergi förloras vid krocken?', 'Vagnen som stod stilla får farten 1,00 m/s. Hur stor är kraften mellan vagnarna i genomsnitt under de 0,50 s kopplingen tar?'],
        'intro': p('En järnvägsvagn som väger 40 000 kg rullar åt höger med farten 1,50 m/s och kopplas ihop med en vagn som väger 20 000 kg och står stilla. Kopplingen tar 0,50 s.') + FIG,
        'd': {'a': kort('En järnvägsvagn som väger 40 000 kg rullar med farten 1,5 m/s mot en vagn som står stilla.', 'Hur stor är vagnarnas totala rörelsemängd före krocken?'),
              'b': kort('En järnvägsvagn som väger 40 000 kg rullar med farten 1,5 m/s mot en vagn som väger 20 000 kg och står stilla. Vagnarna kopplas ihop.[F1]', 'Vilken hastighet får vagnarna efter krocken?'),
              'c': kort('En järnvägsvagn som väger 40 000 kg rullar med farten 1,5 m/s mot en vagn som väger 20 000 kg och står stilla. Vagnarna kopplas ihop.[F1]', 'Hur mycket rörelseenergi förloras vid krocken?'),
              'd': kort('En järnvägsvagn som väger 20 000 kg står stilla och får farten 1,00 m/s när en annan vagn kopplas ihop med den. Kopplingen tar 0,50 s.', 'Hur stor är kraften mellan vagnarna i genomsnitt?')}},
    '5.119': {
        'fore': p('En vagn som väger 200 kg rullar med farten 4,0 m/s. Från en ficka ovanför faller sand rakt ner i vagnen, 12 kg varje sekund. Sanden stannar i vagnen. Bortse från friktion.') + FIG,
        'li': ['Vilken fart har vagnen efter 10 s om den får rulla fritt?',
               'Vagnen ska i stället hållas kvar på farten 4,0 m/s. Hur stor dragkraft och effekt krävs?',
               'Hur stor del av dragarbetet varje sekund blir rörelseenergi när farten hålls konstant? Förklara vart resten tar vägen.']},
    '5.120': {
        'intro': p('En lastbil som väger 12 000 kg kör med den konstanta farten 15 m/s uppför en 2000 m lång backe som lutar 4,0°. Luftmotstånd och friktion bromsar med 2500 N.'),
        'd': {'a': kort('En lastbil som väger 12 000 kg kör med konstant fart uppför en backe som lutar 4,0°. Luftmotstånd och friktion bromsar med 2500 N.', 'Hur stor är drivkraften?'),
              'b': kort('En lastbil som väger 12 000 kg kör med den konstanta farten 15 m/s uppför en backe som lutar 4,0°. Luftmotstånd och friktion bromsar med 2500 N.', 'Hur stor nyttig effekt ger motorn?'),
              'c': kort('En lastbil som väger 12 000 kg kör med konstant fart 2000 m uppför en backe som lutar 4,0°. Luftmotstånd och friktion bromsar med 2500 N.', 'Hur stort arbete uträttar motorn i backen?')}},
    '5.121': {
        'fore': p('Två personer som väger 60 kg och 75 kg står stilla på friktionsfri is. Den första kastar en boll som väger 2,0 kg horisontellt till den andra med farten 6,0 m/s. Den andra fångar bollen och håller kvar den.') + FIG,
        'li': ['Vilken hastighet får den som kastar, och vilken hastighet får den som fångar bollen?',
               'Hur mycket rörelseenergi omvandlas när bollen fångas? Förklara varför kastarens rörelseenergi inte ska räknas som en förlust vid fångsten.']},
    '5.122': {
        'fore': p('En drönare som väger 1,8 kg stiger rakt uppåt med den konstanta farten 4,0 m/s. Batteriet har 40 Wh energi att använda. När drönaren stiger går 55 % av batteriets energi till att öka drönarens lägesenergi.') + FIG,
        'li': ['Hur stor effekt går till att öka lägesenergin, och hur stor effekt ger batteriet?',
               'Hur länge räcker batteriet när drönaren stiger så här?',
               'Felix sätter v = 0 i mgv och drar slutsatsen att drönaren inte behöver någon energi när den håller samma höjd. Har han rätt? Motivera ditt svar.']},
    '5.123': {
        'intro': p('En låda som väger 45 kg står stilla och dras sedan 6,0 m uppför ett plan som lutar 15°. Dragkraften är konstant och parallell med planet. Friktionstalet är 0,25. Efter 6,0 m har lådan farten 3,0 m/s.') + FIG,
        'd': {'a': {'f': 'Hur stor är dragkraften?'}, 'b': {'f': 'Hur stor effekt har dragkraften precis efter 6,0 m?'}}},
    '5.124': {
        'intro': p('En fotboll som väger 0,43 kg ligger stilla och sparkas iväg horisontellt. Bollen får farten 25 m/s, och sparken tar 9,0 ms.'),
        'd': {'a': {'f': 'Hur stor är den resulterande kraften på bollen i genomsnitt?'},
              'b': {'f': 'Hur stor medeleffekt går till att öka bollens rörelseenergi under sparken?'}}},
    '5.125': {
        'intro': p('En kanot med paddlare väger tillsammans 95 kg och glider framåt med farten 2,5 m/s. Under ett paddeltag som varar 0,80 s ger vattnet kanoten en impuls på 60 Ns framåt.'),
        'd': {'a': kort('En kanot med paddlare väger tillsammans 95 kg och glider framåt med farten 2,5 m/s. Under ett paddeltag ger vattnet kanoten en impuls på 60 Ns framåt.', 'Hur stor rörelsemängd har kanoten efter paddeltaget?'),
              'b': kort('En kanot med paddlare väger tillsammans 95 kg och glider framåt med farten 2,5 m/s. Under ett paddeltag ger vattnet kanoten en impuls på 60 Ns framåt.', 'Vilken hastighet har kanoten efter paddeltaget?'),
              'c': kort('Under ett paddeltag som varar 0,80 s ger vattnet en kanot en impuls på 60 Ns framåt.', 'Hur stor kraft påverkar vattnet kanoten med i genomsnitt?')}},
    '5.126': {
        'intro': p('En cyklist och cykeln väger tillsammans 90 kg. Cyklisten bromsar från 7,0 m/s till stillastående på 12 m. Bromskraften är konstant.'),
        'd': {'a': {'f': 'Hur stor är bromskraften?'},
              'b': kort('En cyklist bromsar från 7,0 m/s till stillastående på 12 m med konstant retardation.', 'Hur lång tid tar inbromsningen?')}},
    '5.127': {
        'fore': p('En fallskärmshoppare väger 85 kg med utrustning och faller rakt nedåt med den konstanta farten 6,0 m/s i 40 s.'),
        'li': ['Hur stort är luftmotståndet, och hur stor är dess effekt?',
               'Hur mycket minskar lägesenergin på 40 s? Förklara varför rörelseenergin ändå inte ändras.']},
    '5.128': {
        'fore': p('En pendelkula som väger 0,50 kg hänger i en 1,60 m lång tråd. Kulan dras upp 0,30 m över sitt lägsta läge och släpps. Bortse från luftmotståndet.') + FIG,
        'li': ['Vilken fart har kulan i det lägsta läget, och hur stor är trådens kraft på kulan där?',
               'Majken påstår att trådens kraft är lika stor som tyngdkraften i det lägsta läget. Förklara varför det inte stämmer.']},
    '5.129': {
        'fore': p('En vagn som väger 4,0 kg rullar med farten 3,0 m/s mot en vagn som väger 2,0 kg och står stilla. Vagnarna fastnar i varandra.') + FIG,
        'li': ['Vilken fart har vagnarna efter krocken?',
               'Hur mycket rörelseenergi förloras? Förklara varför det inte betyder att energi har försvunnit.']},
    '5.130': {
        'fore': p('Två klossar med massorna m och M krockar rakt. Klossen M står stilla, och klossen m har farten u.'),
        'li': ['Visa att impulsen på M är dubbelt så stor om stöten är elastisk som om klossarna fastnar i varandra.',
               'Vad kan du säga om medelkrafterna om krockarna tar lika lång tid? Gäller samma sak för de största krafterna?',
               'Kontrollera förhållandet mellan impulserna för m = 2,0 kg, M = 3,0 kg och u = 4,0 m/s.']},
    '5.131': {
        'intro': p('En låda som väger 18 kg står stilla och dras sedan 12 m över ett golv med en horisontell kraft på 55 N. Friktionskraften är 30 N.'),
        'd': {'a': kort('En horisontell kraft på 55 N drar en låda 12 m över ett golv.', 'Hur stort arbete uträttar dragkraften?'),
              'b': kort('En låda glider 12 m över ett golv. Friktionskraften är 30 N.', 'Hur stort arbete uträttar friktionskraften?'),
              'c': {'f': 'Vilken fart har lådan efter 12 m?'}}},
    '5.132': {
        'intro': p('En golfboll som väger 0,045 kg släpps från 2,50 m höjd och studsar upp till 1,60 m. Studsen varar i 0,80 ms. Höjderna gäller bollens tyngdpunkt, räknat från dess läge när bollen nuddar golvet. Bortse från luftmotståndet.') + FIG,
        'd': {'a': {'t': p('En boll släpps och tyngdpunkten faller 2,50 m innan bollen träffar golvet. Bortse från luftmotståndet.', 'Vilken hastighet har bollen precis innan studsen?'),
                    'f': 'Vilken hastighet har bollen precis innan studsen?', 'kg': U},
              'b': {'t': p('Efter en studs stiger bollens tyngdpunkt 1,60 m från sitt läge när bollen nuddar golvet. Bortse från luftmotståndet.', 'Vilken hastighet har bollen precis efter studsen?'),
                    'f': 'Vilken hastighet har bollen precis efter studsen?', 'kg': U},
              'c': {'f': 'Hur stor är golvets kraft på bollen i genomsnitt under studsen?'},
              'd': {'t': p('En boll släpps från 2,50 m höjd och studsar upp till 1,60 m. Höjderna gäller tyngdpunkten, räknat från läget när bollen nuddar golvet. Bortse från luftmotståndet.') + '[F1]' + p('Hur många procent av den mekaniska energin omvandlas vid studsen?'),
                    'f': 'Hur många procent av den mekaniska energin omvandlas vid studsen?'}}},
    '5.133': {
        'intro': p('En bil som väger 1500 kg drar ett släp som väger 800 kg med den konstanta farten 25 m/s på en plan väg. Motorns nyttiga effekt är 22 kW. Sedan bromsar bilen och stannar efter 60 m.'),
        'd': {'a': kort('En bil som väger 1500 kg och ett släp som väger 800 kg kör tillsammans i 25 m/s.', 'Hur stor är deras totala rörelsemängd?'),
              'c': kort('En bil med släp väger tillsammans 2300 kg. Bilen bromsar från 25 m/s till stillastående på 60 m.', 'Hur stor är den totala bromsande kraften i genomsnitt?')}},
    '5.134': {
        'fore': p('En kloss som väger 0,80 kg glider åt höger med farten 5,0 m/s mot en ramp som väger 2,4 kg och står stilla. Rampen kan glida fritt på underlaget. Rampens yta är krökt och börjar horisontellt, så klossen glider mjukt upp på den. Rampen är så hög att klossen vänder innan toppen. Det finns ingen friktion.') + FIG,
        'li': ['Vilken hastighet har rampen, och hur högt har klossen kommit, när klossen för ett ögonblick står stilla i förhållande till rampen?',
               'Vilka hastigheter har klossen och rampen när klossen glider av rampen igen? Välj den lösning som är fysikaliskt rimlig och motivera.']},
    '5.165': {
        'fore': p('Ett vattenkraftverk har fallhöjden 18 m. Varje sekund passerar 5,0 m³ vatten. Vattnets densitet är 1000 kg/m³. Kraftverket ger eleffekten 800 kW. Vattnet står nästan stilla i de stora magasinen ovanför och nedanför kraftverket.'),
        'li': ['Hur stor effekt motsvarar vattnets minskning av lägesenergi? Hur stor är kraftverkets verkningsgrad?',
               'Vid turbinens inlopp har vattnet farten 12 m/s. Räcker den uppgiften och flödet för att bestämma vattnets kraft på turbinen? Motivera ditt svar.']},
    '5.166': {
        'intro': p('Grafen visar hastigheten för en bil som väger 1000 kg och kör längs en rak väg.') + '[F1]',
        'd': {'a': kort('Grafen visar hastigheten för en bil som väger 1000 kg och kör längs en rak väg.[F1]', 'Hur stor rörelseenergi har bilen vid t = 4 s?'),
              'b': {'t': p('Grafen visar hastigheten för en bil som väger 1000 kg och kör längs en rak väg.[F1]', 'Hur stor är den resulterande kraften på bilen under 5–6 s?'),
                    'f': 'Hur stor är den resulterande kraften på bilen under 5–6 s?', 'kg': F},
              'c': kort('Grafen visar hastigheten för en bil som kör längs en rak väg.[F1]', 'Hur lång sträcka kör bilen under 0–6 s?'),
              'd': kort('Grafen visar hastigheten för en bil som väger 1000 kg och kör längs en rak väg.[F1]', 'Hur stort arbete uträttar den resulterande kraften under 5–6 s?')}},
    '5.167': {
        'fore': p('En elmotorcykel med förare väger 260 kg. På en plan väg är motorns nyttiga effekt konstant 18 kW, och luftmotstånd och friktion bromsar med konstant 50 N. Farten ökar från 5,0 m/s till 25 m/s.'),
        'li': ['Hur stor är drivkraften och accelerationen vid 5,0 m/s och vid 25 m/s?', 'Hur mycket ökar rörelseenergin?',
               'Wilma delar ökningen av rörelseenergin med motorns effekt för att beräkna hur lång tid accelerationen tar. Förklara varför hon får för kort tid. Vilket arbete har hon glömt?']},
    '5.168': {'t': p('En hiss med last väger 900 kg. Den accelererar uppåt från stillastående till 2,0 m/s på 3,0 s. Av motorns elektriska effekt blir 80 % mekanisk effekt i hissvajern. Hissen har ingen motvikt. Bortse från friktion.', 'Hur stor är den största elektriska effekten under accelerationen?')},
    '5.170': {
        'intro': p('En boll som väger 0,20 kg släpps från 1,8 m höjd och studsar upp till 1,1 m. Höjderna gäller tyngdpunkten, räknat från läget när bollen nuddar golvet. Bortse från luftmotståndet.'),
        'd': {'a': {'t': p('En boll släpps och tyngdpunkten faller 1,8 m innan bollen träffar golvet. Bortse från luftmotståndet.', 'Vilken fart har bollen precis innan studsen?'),
                    'f': 'Vilken fart har bollen precis innan studsen?'},
              'b': {'t': p('Efter en studs stiger bollens tyngdpunkt 1,1 m från sitt läge när bollen nuddar golvet. Bortse från luftmotståndet.', 'Vilken fart har bollen precis efter studsen?'),
                    'f': 'Vilken fart har bollen precis efter studsen?'},
              'c': {'f': 'Hur mycket mekanisk energi omvandlas vid studsen?'},
              'd': kort('En boll släpps så att tyngdpunkten faller 1,8 m före studsen och stiger 1,1 m efter studsen. Bortse från luftmotståndet.', 'Hur många procent av den mekaniska energin omvandlas vid studsen?')}},
    '5.171': {
        'fore': p('En snowboardåkare som väger 80 kg börjar glida från stillastående nedför en 120 m lång backe som lutar 20°. Friktionstalet är 0,080. Bortse från luftmotståndet.') + FIG,
        'li': ['Hur stort arbete uträttar tyngdkraften och friktionskraften? Vilken fart har åkaren längst ner? Använd energiprincipen.',
               'Kontrollera slutfarten med Newtons andra lag och förklara varför de två metoderna ger samma svar.']},
    '5.172': {
        'fore': p('En person som väger 65 kg gör ett bungyhopp från en bro. Det elastiska repet är 18 m långt när det inte är sträckt. När det sträcks fungerar det som en fjäder med fjäderkonstanten 62 N/m. Bortse från luftmotståndet. Det finns tillräckligt med fri höjd under bron.') + FIG,
        'li': ['Vilken fart har personen när repet börjar sträckas, och hur långt under bron är den lägsta punkten?',
               'Hur stor är repets största kraft på personen? Hur många gånger större än tyngdkraften är den?',
               'Var är farten störst, och hur stor är den? Förklara varför den punkten inte är den lägsta punkten.']},
    '5.173': {'t': p('En simhoppare hoppar från en trampolin 3,0 m över vattenytan och har farten 2,0 m/s rakt uppåt när hon lämnar trampolinen. Vilken fart har hon när hon når vattnet? Bortse från luftmotståndet.')},
    '5.174': {
        'fore': p('Bil A väger 1000 kg och kör med farten 20 m/s rakt in i bil B, som väger 1200 kg och står stilla. Jämför två förenklade fall: bilarna fastnar i varandra, eller stöten är elastisk.'),
        'li': ['Vilka hastigheter får bilarna i de två fallen?',
               'Efter krocken bromsas varje bil som rör sig av en kraft som är μ gånger bilens tyngd. Samma μ gäller i båda fallen. Jämför hur långt bil B glider.',
               'Visa att förhållandet mellan bromssträckorna inte beror på bilarnas massor.']},
    '5.219': {'fore': p('En cyklist och cykeln väger tillsammans 80 kg. Cyklisten färdas från A, som ligger 50 m över en vald nollnivå, till C, som ligger 25 m över samma nivå. Vägen är 1200 m lång och färden tar 109 s. Cyklistens nyttiga medeleffekt är 40 W, och luftmotstånd och friktion bromsar i genomsnitt med 20 N.')},
    '5.220': {'t': p('En bil som väger 1,5 ton kör uppför en backe i 1,0 min. Motorns nyttiga medeleffekt är 13 kW, och farten ökar från 7,0 m/s till 24 m/s. Motorn uträttar också 80 kJ arbete mot friktion och luftmotstånd.', 'Hur mycket högre upp kommer bilen?')},
    '5.225': {
        'intro': p('Petra och cykeln väger tillsammans 72 kg. Backen stiger 2 m för varje 21 m längs vägen. Luftmotstånd och friktion bromsar med konstant 25 N.'),
        'd': {'a': {'f': 'Hur stor effekt krävs för att Petra ska cykla uppför backen med den konstanta farten 5,0 m/s?'},
              'b': {'f': 'Petra rullar nedför backen utan att trampa. Hon har farten 5,0 m/s i början. Vilken fart har hon efter 180 m?'}}},
    '5.238': {'t': p('En låda som väger 2,0 kg dras uppför ett plan som lutar 30° med en konstant kraft på 49 N parallellt med planet. Friktionstalet är 0,50. I punkten A har lådan farten 10 m/s. Punkten B ligger 4,0 m längre upp.', 'Vilken fart har lådan i B? Använd energiprincipen.')},
    '5.239': {
        'intro': p('En bil som väger 1230 kg kör 615 m uppför en rak backe där tan θ = 0,225. På 50 s ökar farten från 6,0 m/s till 20 m/s. Luftmotstånd och friktion bromsar med konstant 400 N.'),
        'd': {'a': kort('En bil som väger 1230 kg kör 615 m uppför en rak backe där tan θ = 0,225. Farten ökar från 6,0 m/s till 20 m/s. Luftmotstånd och friktion bromsar med konstant 400 N.', 'Hur stort nyttigt arbete uträttar motorn?'),
              'b': {'f': 'Hur stor är motorns nyttiga medeleffekt?'}}},
    '5.240': {'t': p('Ett föremål som väger 5,0 kg dras 7,0 m över ett golv med en horisontell kraft på 47 N. Friktionstalet är 0,50. Efter 7,0 m har föremålet fyra gånger så stor fart som i början.', 'Vilken fart hade föremålet i början?')},
    '5.241': {'li': ['Ta fram den gemensamma farten när den hängande vikten har sjunkit sträckan l.'], 'fore': p('En kloss med massan m ligger på ett friktionsfritt plan som lutar 30°. Den är förbunden med en tråd som går över en trissa till en hängande vikt med massan 3m. Tråden kan inte töjas, och tråden och trissan är lätta. Vikten släpps.') + FIG},
    '5.242': {
        'fore': p('I en uppgift står det att en bil som väger 1300 kg ökar farten från 10 m/s till 30 m/s på 30 s i en uppförsbacke där sin θ = 0,10. Motorns nyttiga effekt sägs vara konstant 30 kW, och luftmotstånd och friktion bromsar med konstant 400 N.'),
        'li': ['Hanna använder energiprincipen och får att bilen kommer ungefär 23 m högre upp. Kontrollera beräkningen och avgör om rörelsen ändå är möjlig.',
               'Vilken är den högsta fart bilen kan nå enligt modellen? Kontrollera slutsatsen även med sträcka och energi.']},
    '5.243': {'t': p('En bil som väger 2000 kg kör 110 m uppför en rak backe som lutar 5,7°. På 10 s ökar farten från 10 m/s till 12 m/s. Motorns nyttiga medeleffekt är 30 kW. Luftmotstånd och friktion bromsar med en konstant kraft.', 'Hur stor är den bromsande kraften?')},
    '5.244': {'fore': p('En låda som väger 120 kg dras uppför ett plan där tan α = 3/4. Dragkraften är 1,50 kN och bildar vinkeln α med planet. Friktionskraften är konstant 180 N. Lådan har farten 5,0 m/s från början.') + FIG,
              'li': ['Vilken fart har lådan efter 10 m uppför planet?', 'Kontrollera att normalkraften är positiv, så att lådan hela tiden har kontakt med planet.']},
    '5.245': {'fore': p('I figuren är AB vertikal och har längden x. BC är en kvartscirkel med radien x. Banan från A till C är friktionsfri. Sträckan CD är horisontell och har längden d, och där finns friktion. En liten kloss släpps i A och stannar precis i D.') + FIG,
              'li': ['Ta fram klossens fart mitt på sträckan CD.', 'Förklara varför svaret inte beror på längden d.']},
    '5.246': {'li': ['Ta fram den gemensamma farten när den hängande vikten har sjunkit sträckan l.'], 'fore': p('En kloss med massan m ligger på ett plan där tan θ = 4/3. Den är förbunden med en tråd som går över en trissa till en hängande vikt med massan 4m. Tråden kan inte töjas, och tråden och trissan är lätta. Vikten släpps och drar klossen uppför planet. Friktionstalet mellan klossen och planet är 7/24.') + FIG},
    '5.247': {'fore': p('En pärla A som väger 0,10 kg kan glida utan friktion längs en vertikal stång. En lätt tråd går från A över en liten trissa, 0,50 m från stången, till en hängande vikt B som väger 0,25 kg. Från början är A i samma höjd som trissan, och B hänger 1,50 m under trissan. Tråden är 2,0 m lång och kan inte töjas. Pärlan släpps.') + FIG,
              'li': ['Hur långt sjunker A innan den vänder för första gången? Kontrollera att svaret är möjligt med trådens längd.']},
    '5.248': {'fore': p('En kloss skjuts uppför ett plan med farten u. Planet lutar vinkeln θ och friktionstalet är μ. Klossen stannar och glider sedan tillbaka ner till startpunkten. Antag att μ &lt; tan θ.'),
              'li': ['Ta fram förhållandet mellan farten v när klossen är tillbaka vid startpunkten och startfarten u.',
                     'Vilket villkor måste gälla för att klossen ska börja glida nedåt igen? Kontrollera svaret för fallet utan friktion.']},
    '5.249': {'t': p('En pump pumpar vatten från en stor sjö till ett utlopp 10 m över vattenytan. Pumpen ger vattnet den nyttiga effekten 900 W. Vattnet lämnar utloppet med farten 20 m/s. Vattnets densitet är 1000 kg/m³. Bortse från förluster i röret.', 'Hur stor är utloppets tvärsnittsarea?')},
    '5.250': {'fore': p('En kloss har farten u i punkten P och glider uppför ett plan som lutar vinkeln θ. Klossen stannar i punkten Q och glider sedan nedför igen. Friktionstalet är μ, och μ &lt; tan θ. Planet är tillräckligt långt.'),
              'li': ['Klossen har farten u igen i punkten R nedanför P. Ta fram sträckan PR.', 'Vad händer med resultatet när μ närmar sig noll och när μ närmar sig tan θ?']},
    '5.637': {
        'intro': p('En kloss som väger 0,40 kg trycks mot en fjäder med fjäderkonstanten 800 N/m, så att fjädern trycks ihop 12 cm. När klossen släpps skjuts den iväg över ett bord. Från den punkt där klossen lämnar fjädern finns friktion på en 60 cm lång sträcka, med friktionstalet 0,25. Sedan kommer en friktionsfri ramp. Under fjädern finns ingen friktion.') + FIG,
        'd': {'b': {'f': 'Hur högt över bordet kommer klossen på rampen?'},
              'c': {'f': 'Klossen glider fram och tillbaka tills den stannar. Hur långt från rampens fot stannar den?'}}},
}
R['5.169'] = {'fore': p(r'En raket står stilla ute i rymden, långt från planeter och stjärnor. Hastigheterna mäts från samma fasta punkt om inget annat sägs. Raketen väger 20 000 kg från början. Motorn sprutar ut 80 kg gas varje sekund bakåt med farten 3000 m/s i förhållande till raketen. Raketen kan beskrivas med \(F=\dot m u\) och \(\Delta v=u\ln(m_0/m)\), där \(\dot m\) är mängden gas i kg/s och u är gasens fart i förhållande till raketen.')}
