# Ma1 prefix (omr prefix), omskrivet för hand 2026-11-17.
# "Skriv svaret som ett vanligt tal, inte i tiopotensform." står bara kvar i kgInstruktion där svaret är mycket
# stort eller litet, eftersom formatet decimalform inte godtar tiopotenser. Mallarna "Två tunna skikt …",
# "tolkas det av misstag som …" och kapningsuppgifterna har fått egna sammanhang.
VANLIGT = 'Skriv svaret som ett vanligt tal, utan tiopotens.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.240': {'t': p('Omvandla 3,2 kW till W.')},
    '0.241': {'t': p('Hur många ampere är 450 mA?')},
    '0.242': {'t': p('Omvandla 0,075 MW till kW.')},
    '0.243': {'t': p('Hur många meter är 2,4 mm?')},
    '0.244': {'t': p('Ett hårstrå är 8,5 µm tjockt. Hur många meter är det?'), 'kg': VANLIGT},
    '0.245': {'t': p('Omvandla 0,36 kV till V.')},
    '0.246': {'t': p('En radiostation sänder på frekvensen 5,2 MHz. Hur många hertz är det?'), 'kg': VANLIGT},
    '0.247': {'t': p('Hur många kilowatt är 7500 W?')},
    '0.248': {'t': p('Kim ska omvandla 0,0045 A till mA. Vilket svar är rätt?')},
    '0.249': {'t': p('En processor har klockfrekvensen 2,8 GHz. Hur många MHz är det?')},
    '0.250': {'t': p('Omvandla 0,015 m till mm.')},
    '0.251': {'t': p('Hur många milligram är 640 µg?')},
    '0.325': {'t': p('Ett laboratorium har 0,015 g av ett ämne. Varje analys kräver 2,5 µg av ämnet, och analyserna görs i '
                     'omgångar med 800 analyser i varje. Hur många hela omgångar räcker ämnet till?')},
    '0.327': {'t': p('En mätare gör 250 mätningar per sekund, och varje mätning tar 2 400 byte i minnet. Minnet är tomt och '
                     'rymmer 9 MB (1 MB = 1 000 000 byte). Hur många hela sekunder kan mätaren mäta innan minnet är fullt?')},
    '0.332': {'t': p('En förpackning består av ett lager papp som är 0,12 mm tjockt och ett lager plastfilm som är 85 µm tjockt. '
                     'Hur många sådana förpackningar kan man som mest stapla på varandra om högen får vara högst 2 mm?')},
    '0.412': {'t': p('En laddare drar effekten 2 mW. Elias läser fel och räknar med 2 MW. Hur blir effekten han räknar med '
                     'jämfört med den riktiga?')},
    '0.417': {'t': p('En tråd är 1,05 m lång. Den kapas i bitar som är 2,5 mm långa. För varje bit försvinner dessutom 0,5 mm '
                     'tråd vid kapningen. Hur många hela bitar kan man få?')},
    '0.613': {'t': p('Hur många meter är 4,7 km?')},
    '0.614': {'t': p('Omvandla 250 mg till gram.')},
    '0.615': {'t': p('Ett kraftverk ger effekten 0,85 MW. Hur många kilowatt är det?')},
    '0.616': {'t': p('Omvandla 62 µm till mm.')},
    '0.617': {'t': p('En film är 3,4 GB stor. Hur många MB är det?')},
    '0.618': {'t': p('Omvandla 750 mL till L.')},
    '0.619': {'t': p('Hur många millisekunder är 0,042 s?')},
    '0.620': {'t': p('Omvandla 18 cm till meter.')},
    '0.621': {'t': p('Hur många newton är 2,6 kN?')},
    '0.622': {'t': p('Omvandla 95 nm till µm.')},
    '0.641': {'t': p('En fil som är 18 MB laddas ned med hastigheten 750 kB per sekund (1 MB = 1 000 kB). Hur lång tid tar '
                     'nedladdningen?')},
    '0.663': {'t': p('Ett lock består av ett lager papper som är 0,15 mm tjockt och ett lager aluminiumfolie som är 60 µm '
                     'tjockt. Hur många lock får som mest plats i en hög som är 3 mm hög?')},
    '0.664': {'t': p('En väggskiva består av en träskiva som är 2,5 cm tjock och en gipsskiva som är 4 mm tjock. Hur många '
                     'sådana väggskivor kan man som mest lägga på varandra om högen får vara högst 0,5 m?')},
    '0.665': {'t': p('Ett skyddsglas till en mobil består av ett glaslager som är 0,8 mm tjockt och en skyddsfilm som är 350 µm '
                     'tjock. Hur många skyddsglas ryms som mest i en ask som är 25 mm hög?')},
    '0.666': {'t': p('På ett kretskort läggs ett kopparlager som är 12 µm tjockt och ett lackskikt som är 0,004 mm tjockt. Hur '
                     'många sådana dubbla skikt ryms som mest i en tjocklek på 0,5 mm?')},
    '0.667': {'t': p('Ett golv läggs med laminat som är 3,2 mm tjockt ovanpå en matta som är 0,9 mm tjock. Hur många '
                     'sådana golvbitar med matta kan man stapla på varandra om högen får vara högst 8 cm?')},
    '0.668': {'t': p('En trätrall består av en planka som är 0,045 m tjock och en gummilist som är 15 mm tjock. Hur många '
                     'trallar kan man som mest stapla på varandra i ett förråd som är 1,2 m högt?')},
    '0.669': {'t': p('Ett busskort består av ett plastkort som är 250 µm tjockt och en skyddsfilm som är 0,1 mm tjock. '
                     'Hur många busskort får som mest plats i en hög som är 9 mm hög?')},
    '0.670': {'t': p('En bänkskiva består av en träskiva som är 1,8 cm tjock och en filtmatta som är 6 mm tjock. Hur många '
                     'bänkskivor kan man som mest stapla på varandra om högen får vara högst 0,75 m?')},
    '0.671': {'t': p('Ett kuvert består av en kartongbit som är 0,6 mm tjock och en bubbelfilm som är 900 µm tjock. Hur många '
                     'kuvert får som mest plats i en låda som är 4,5 cm hög?')},
    '0.672': {'t': p('Ett etikettark består av ett papper som är 0,125 mm tjockt och en plastfilm som är 75 µm tjock. Hur många '
                     'ark får som mest plats i en hög som är 2,4 mm hög?')},
    '0.673': {'t': p('En pipett tar upp <strong>5 µL</strong>. Saga skriver av misstag <strong>5 mL</strong> i sin beräkning. '
                     'Hur blir volymen hon räknar med jämfört med den riktiga?')},
    '0.674': {'t': p('En sats väger <strong>3 kg</strong>. Ali skriver av misstag <strong>3 mg</strong> i sin beräkning. '
                     'Hur blir massan han räknar med jämfört med den riktiga?')},
    '0.675': {'t': p('En detalj i ett datorchip är <strong>8 nm</strong> bred. Någon skriver av misstag <strong>8 mm</strong>. '
                     'Hur blir bredden i beräkningen jämfört med den riktiga?')},
    '0.676': {'t': p('En fil är <strong>250 MB</strong> stor. Wilma skriver av misstag <strong>250 kB</strong> när hon räknar på '
                     'nedladdningen. Hur blir filstorleken hon räknar med jämfört med den riktiga?')},
    '0.677': {'t': p('En fördröjning i ett nätverk är <strong>4 ms</strong>. I en beräkning råkar den skrivas som '
                     '<strong>4 s</strong>. Hur blir tiden i beräkningen jämfört med den riktiga?')},
    '0.678': {'t': p('En dos av ett läkemedel är <strong>12 µg</strong>. Någon läser fel och skriver <strong>12 g</strong>. '
                     'Hur blir massan som skrivs jämfört med den riktiga?')},
    '0.679': {'t': p('Strömmen genom en lysdiod är <strong>7 mA</strong>. Adam skriver av misstag <strong>7 µA</strong>. '
                     'Hur blir strömmen han räknar med jämfört med den riktiga?')},
    '0.680': {'t': p('Ett kraftverk ger <strong>0,5 GW</strong>. I en rapport har det blivit <strong>0,5 kW</strong>. Hur blir '
                     'effekten i rapporten jämfört med den riktiga?')},
    '0.681': {'t': p('En spalt är <strong>60 mm</strong> bred. Lova skriver av misstag <strong>60 µm</strong>. Hur blir '
                     'bredden hon räknar med jämfört med den riktiga?')},
    '0.682': {'t': p('Ett prov innehåller <strong>9 ng</strong> av ett ämne. I en beräkning råkar det skrivas som '
                     '<strong>9 mg</strong>. Hur blir massan i beräkningen jämfört med den riktiga?')},
    '0.683': {'t': p('En tråd är 2,4 m lång. Den kapas i bitar som är 3 mm långa. För varje bit försvinner dessutom 0,4 mm '
                     'tråd vid kapningen. Hur många hela bitar kan man få?')},
    '0.684': {'t': p('En metallstång är 0,96 m lång. En smed sågar den i bitar som är 5 mm långa. Sågbladet tar bort 1 mm '
                     'för varje bit som sågas av. Hur många hela bitar kan smeden få?')},
    '0.685': {'t': p('En list är 1,5 m lång och ska kapas till distanser som är 4,5 mm långa. För varje distans som kapas '
                     'försvinner 0,5 mm av listen. Hur många hela distanser blir det?')},
    '0.686': {'t': p('En laserskärare skär en plastremsa som är 3,2 m lång i bitar som är 7 mm långa. Lasern bränner bort '
                     '1 mm för varje bit den skär av. Hur många hela bitar kan man få?')},
    '0.687': {'t': p('En kabel som är 0,84 m lång klipps i bitar som är 2 mm långa. För varje bit går 0,8 mm kabel förlorad '
                     'vid klippet. Hur många hela bitar blir det?')},
    '0.688': {'t': p('En metallstång är 2,1 m lång. Ellen sågar den i bitar som är 6 mm långa. Sågbladet tar bort 1 mm för '
                     'varje bit som sågas av. Hur många hela bitar kan hon få?')},
    '0.689': {'t': p('En list är 1,26 m lång och ska kapas till distanser som är 3,5 mm långa. För varje distans som kapas '
                     'försvinner 0,7 mm av listen. Hur många hela distanser blir det?')},
    '0.690': {'t': p('En laserskärare skär en plastremsa som är 0,72 m lång i bitar som är 1,5 mm långa. Lasern bränner bort '
                     '0,3 mm för varje bit den skär av. Hur många hela bitar kan man få?')},
    '0.691': {'t': p('En kabel som är 4,5 m lång klipps i bitar som är 9 mm långa. För varje bit går 1 mm kabel förlorad vid '
                     'klippet. Hur många hela bitar blir det?')},
    '0.692': {'t': p('En metallstång är 1,68 m lång. En smed sågar den i bitar som är 4 mm långa. Sågbladet tar bort 0,8 mm '
                     'för varje bit som sågas av. Hur många hela bitar kan smeden få?')},
    '0.1070': {'t': p('Ljuset färdas med hastigheten 300 Mm/s, alltså 300 megameter per sekund.',
                      '<strong>a)</strong> Hur många nanosekunder tar det för ljuset att färdas 1 m?',
                      '<strong>b)</strong> En processor arbetar med klockfrekvensen 3 GHz, alltså 3 miljarder klockcykler per '
                      'sekund. Hur många centimeter hinner ljuset färdas under en klockcykel?'),
               'kg': 'Svara med två decimaler i a.'},
    '0.1077': {'t': p('Ett mobilbatteri har kapaciteten 4 500 mAh och spänningen 3,8 V. Energin i joule får man genom att '
                      'multiplicera spänningen med laddningen i ampersekunder (As).',
                      'Hur många kilojoule energi lagrar batteriet?'),
               'kg': 'Svara med en decimal.'},
    '0.1262': {'t': p('Ett virus har diametern 120 nm. Hur många hela virus får plats i rad på en sträcka som är 1 mm?')},
    '0.1263': {'t': p('En del av ett datorchip är en kvadrat med arean 25 mm². Den fylls med kvadratiska transistorer med '
                      'sidan 50 nm. Hur många transistorer får plats?'),
               'kg': 'Svara i grundpotensform.'},
    '0.1264': {'t': p('Ett vindkraftverk har effekten 3,6 MW när det går för fullt. Under ett år motsvarar produktionen '
                      '2 400 timmar med full effekt. Hur många GWh energi producerar verket på ett år?')},
}
