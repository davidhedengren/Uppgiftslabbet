# Ma1 proportionalitet (omr proportionalitet_grunder), omskrivet för hand 2026-11-17.
# "(Svara i …)" och avrundningskrav är borttagna, eftersom Kunskapsgymmet visar enheten och godtar korrekt
# avrundning. Där enheten är själva poängen står den i frågan ("Hur många kilometer …?"). Ja/nej-frågor får
# "Motivera ditt svar." och rättningsinstruktionen i kgInstruktion.
JANEJ = 'Börja svaret med ja eller nej.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.774': {'t': p('Tabellen visar ett samband.') + '[F1]' +
              p('Kan tabellens värden beskrivas med ett proportionellt samband \\(y=kx\\)? Motivera ditt svar.'),
              'kg': JANEJ},
    '0.775': {'t': p('En karta har skalan 1:25 000. En vandringsled är 7,6 cm på kartan. Hur många kilometer lång är leden i '
                     'verkligheten?')},
    '0.832': {'t': p('En karta har skalan 1:40 000. En sträcka är 7,5 cm på kartan. Hur många kilometer är sträckan i '
                     'verkligheten?')},
    '0.834': {'t': p('En taxiresa kostar 35 kr i startavgift och därefter 15 kr per kilometer. Är priset proportionellt mot '
                     'sträckan? Motivera ditt svar.'), 'kg': JANEJ},
    '0.836': {'t': p('En skrivare skriver ut 18 sidor på 45 sekunder. Hur många sekunder tar det att skriva ut 70 sidor?')},
    '0.837': {'t': p('Ett recept för 8 portioner innehåller 600 g ris. Hur många kilogram ris behövs till 22 portioner?')},
    '0.841': {'t': p('En maskin tillverkar 240 detaljer på 6 minuter. 8 % av detaljerna blir felaktiga och kasseras. Hur många '
                     'godkända detaljer tillverkar maskinen på 17,5 minuter?')},
    '0.982': {'t': p('En karta har skalan 1 : 50 000. Två platser ligger 4 cm från varandra på kartan. Hur många kilometer är '
                     'det mellan dem i verkligheten?')},
    '0.983': {'t': p('En kran fyller en hink på 10 liter på 40 sekunder. Hur många minuter tar det att fylla ett badkar med '
                     '180 liter vatten från samma kran?')},
    '0.985': {'t': p('Under ett åskväder ser Elin blixten och räknar till 7 sekunder innan hon hör åskan. Ljudet färdas 340 m på '
                     'en sekund. Hur många kilometer bort slog blixten ner?')},
    '0.989': {'t': p('Ett modelltåg är byggt i skala 1 : 87. Det riktiga loket är 26,1 m långt. Hur många centimeter lång är '
                     'modellen?')},
    '0.990': {'t': p('Priset på skinka är proportionellt mot vikten, och 350 g kostar 42 kr. Hur många gram skinka får man för '
                     '100 kr?')},
    '0.991': {'t': p('Bil A drar 0,55 liter bensin per mil och bil B drar 6,8 liter per 100 km. Hur många liter mindre bensin '
                     'drar den snålare bilen på en resa som är 250 km?')},
    '0.992': {'t': p('En tom pool med raka väggar fylls med vatten från en pump. Efter 25 minuter är vattnet 18 cm djupt. '
                     'Poolen ska fyllas till djupet 1,35 m. Hur många timmar tar det att fylla poolen?')},
    '0.1037': {'t': p('En karta har skalan 1 : 25 000. Hur många centimeter blir en sträcka på 3,5 km på kartan?')},
    '0.1041': {'t': p('En kran läcker en droppe per sekund, och 20 droppar är 1 ml. Hur många liter vatten läcker ut på ett år '
                      '(365 dygn)?'), 'kg': 'Avrunda till tiotal liter.'},
    '0.1139': {'t': p('En burk energidryck innehåller 355 ml och kostar 23 kr. Vad är priset per liter?')},
    '0.1140': {'t': p('En flaska juice innehåller 500 ml och kostar 18 kr. Vad är literpriset?')},
    '0.1141': {'t': p('En flaska tvål innehåller 750 ml och kostar 49,50 kr. Vad är priset per liter?')},
    '8.18': {'t': p('Två vänner delar lika på en avgift och betalar 210 kr var. Hur mycket mindre hade var och en betalat om '
                    'en vän till hade varit med och de hade delat lika på tre?')},
    '0.1231': {'t': p('Grafen visar priset för lösgodis. Priset är proportionellt mot vikten.') + '<span class="fig">[F1]</span>' +
               p('Vad kostar 5 hg lösgodis?')},
    '0.1232': {'t': p('Bilden visar ett erbjudande i en butik.') + '<span class="fig">[F1]</span>' +
               p('Vad kostar 8 juice, om priset är proportionellt mot antalet?')},
    '0.1234': {'t': p('Tabellen visar ett proportionellt samband \\(y=kx\\).') + '[F1]' +
               p('Bestäm proportionalitetskonstanten \\(k\\).'), 'kg': 'Svara i decimalform.'},
    '0.1235': {'t': p('En cyklist håller farten 18 km/h. Hur långt cyklar hon på 35 minuter?')},
    '0.1236': {'t': p('Receptkortet visar hur mycket mjöl som går åt.') + '<span class="fig">[F1]</span>' +
               p('Hur mycket vetemjöl behövs till 20 muffins?')},
    '0.1237': {'t': p('En euro kostar 11,50 kr. Hur många euro får man för 460 kr?')},
    '0.1238': {'t': p('Graferna visar priset för äpplen i två butiker, A och B.') + '<span class="fig">[F1]</span>' +
               p('Hur mycket billigare är 6 kg äpplen i butik B än i butik A?')},
    '0.1240': {'t': p('Grafen visar hur mycket vatten som finns i ett badkar när det fylls.') + '<span class="fig">[F1]</span>' +
               p('Hur många minuter tar det att fylla en pool med 250 liter vatten, om vattnet rinner lika fort?')},
    '0.1241': {'t': p('En bil drar 0,62 liter bensin per mil. Hur många liter bensin går åt på en resa som är 1 450 km?')},
    '0.1253': {'t': p('Två pumpar fyller en tom tank samtidigt. Pump A ger 45 liter på 3 minuter och pump B 60 liter på '
                      '5 minuter. Hur många minuter tar det att fylla tanken med 300 liter?') + '<span class="fig">[F1]</span>'},
    '0.1255': {'t': p('Grafen visar en vandrings första 1,5 timmar, med en paus. Efter pausen fortsätter gruppen i samma fart '
                      'som före pausen, utan fler stopp. Hur många timmar efter starten har gruppen gått 9 km?')
               + '<span class="fig">[F1]</span>'},
    '0.1256': {'t': p('En färgblandning innehåller 2,4 liter vit färg och 0,8 liter blå färg. Nora råkar hälla i ytterligare '
                      '0,4 liter blå färg. Hur mycket vit färg måste hon tillsätta för att få samma förhållande mellan '
                      'färgerna som förut?')},
    '0.1257': {'t': p('En karta i skala 1:40 000 skrivs ut så att alla längder på papperet blir 80 % av de ursprungliga. '
                      'Vilken skala får den nya utskriften?'), 'kg': 'Skriv bara talet efter 1:.'},
    '0.1258': {'t': p('En drönare har använt 20 % av ett fulladdat batteri för att flyga 12 km. Nu har den 80 % kvar. Batteriet '
                      'laddas ur lika mycket för varje kilometer. Hur långt kan drönaren flyga till om minst 25 % av '
                      'batteriet ska finnas kvar?')},
    '0.1259': {'t': p('Ett liggande foto är 18 cm brett och 12 cm högt. Det ska förstoras, utan att beskäras eller vridas, så '
                      'att det får plats i en ram vars öppning är 44 cm bred och 31 cm hög. Fotot görs så stort som möjligt. '
                      'Hur många centimeter blir det tomt ovanför och under fotot tillsammans?')},
}
