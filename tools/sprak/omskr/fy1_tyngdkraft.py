# Fy1 tyngdkraft (omr tyngdkraft), omskrivet för hand 2026-11-17.
FIG = '<span class="fig">[F1]</span>'
MANEN = 'Tyngdaccelerationen är 1,62 m/s² på månen.'
MARS = 'Tyngdaccelerationen är 3,71 m/s² på Mars.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def kort(ctx, fraga):
    return {'t': p(ctx, fraga), 'f': fraga}


R = {
    '4.347': {'t': p('På en främmande planet är tyngdaccelerationen 4,2 m/s². Hur stor är tyngdkraften på ett föremål som väger 15 kg där?')},
    '4.350': {'t': p('På en främmande planet är g = 5,7 m/s². Tyngdkraften på ett föremål är där 136,8 N. Hur stor massa har föremålet?')},
    '4.23': {'t': p('En robot väger 45 kg. Den ska användas på fyra olika himlakroppar där tyngdaccelerationen är 9,82 m/s², 1,62 m/s², 3,71 m/s² och 24,8 m/s².',
                    'a) Hur stor är tyngdkraften på roboten på varje himlakropp?',
                    'b) Var behövs störst kraft för att lyfta roboten med konstant fart?', 'c) Har robotens massa ändrats?')},
    '4.24': {
        'intro': p('Ett föremål påverkas av tyngdkraften 588 N på jorden. Föremålet skickas till Venus.'),
        'd': {'a': kort('Ett föremål påverkas av tyngdkraften 588 N på jorden.', 'Hur stor massa har föremålet?'),
              'b': {'f': 'Hur stor är tyngdkraften på föremålet på Venus?'}}},
    '4.356': {'t': p('Ett föremål som väger 18 kg flyttas från en plats där tyngdaccelerationen är 3,7 m/s² till en plats där den är 7,4 m/s². Hur mycket ökar tyngdkraften?')},
    '4.37': {
        'fore': p('En sten som väger 3,0 kg påverkas av tyngdkraften 24,6 N på en främmande planet.'),
        'li': ['Hur stor är tyngdaccelerationen på planeten?', 'Hur stor är tyngdkraften på stenen på jorden?', 'Vilken massa ska ett föremål ha för att påverkas av tyngdkraften 24,6 N på jorden?'],
        'intro': p('En sten som väger 3,0 kg påverkas av tyngdkraften 24,6 N på en främmande planet.'),
        'd': {'a': {'f': 'Hur stor är tyngdaccelerationen på planeten?'},
              'b': kort('En sten väger 3,0 kg.', 'Hur stor är tyngdkraften på stenen på jorden?'),
              'c': kort('Ett föremål påverkas av tyngdkraften 24,6 N på jorden.', 'Hur stor massa har föremålet?')}},
    '4.187': {
        'fore': p('En astronaut väger 65 kg och reser från jorden till månen. ' + MANEN),
        'li': ['Hur stor är tyngdkraften på astronauten på månen?', 'Hur stor är tyngdkraften på astronauten på jorden?', 'Hur stor massa har astronauten på månen?'],
        'intro': p('En astronaut väger 65 kg och reser från jorden till månen. ' + MANEN),
        'd': {'a': {'f': 'Hur stor är tyngdkraften på astronauten på månen?'},
              'b': {'f': 'Hur stor är tyngdkraften på astronauten på jorden?'},
              'c': kort('En astronaut väger 65 kg på jorden och reser till månen. ' + MANEN, 'Hur stor massa har astronauten på månen?')}},
    '4.190': {
        'fore': p('En robot som väger 78 kg skickas till Mars. ' + MARS),
        'li': ['Hur stor är tyngdkraften på roboten på Mars?', 'Hur många gånger större är tyngdkraften på roboten på jorden än på Mars?'],
        'intro': p('En robot som väger 78 kg skickas till Mars. ' + MARS),
        'd': {'a': kort('En robot som väger 78 kg står på Mars. ' + MARS, 'Hur stor är tyngdkraften på roboten?'),
              'b': {'f': 'Hur många gånger större är tyngdkraften på roboten på jorden än på Mars?'}}},
    '4.208': {
        'li': ['Hur stor är tyngdkraften på astronauten på jorden?', 'Hur stor är tyngdkraften på astronauten på månen?',
               'Hur stor massa har astronauten på månen?', 'Astronauten står stilla på plan mark på månen. Hur stor är normalkraften?'],
        'd': {'d': {'f': 'Astronauten står stilla på plan mark på månen. Hur stor är normalkraften?'}}},
    '4.215': {
        'fore': p('En person väger 70 kg. ' + MANEN),
        'li': ['Hur stor är tyngdkraften på personen på jorden och på månen?', 'Hur stor massa har personen på månen? Förklara skillnaden mellan massa och tyngdkraft.']},
    '4.467': {'t': p('En hink med vatten väger 5,0 kg. Hur stor är tyngdkraften på hinken?')},
    '4.468': {'t': p('En fågelholk hänger stilla i en krok. Kroken håller upp holken med kraften 147 N. Hur stor massa har holken?')},
    '4.469': {'t': p('En astronaut reser från jorden till månen, där tyngdaccelerationen är mindre. Vad händer med astronautens massa och tyngd?')},
    '4.470': {'t': p('Marsbilen Perseverance väger 1025 kg. Hur stor är tyngdkraften på den på Mars? ' + MARS)},
    '4.471': {'t': p('På en förpackning står ”Nettovikt 12 kg”. I fysiken är tyngd en kraft. Hur stor är innehållets tyngd?')},
    '4.472': {'t': p('En provtagningsutrustning har tyngden 196 N på jorden. Den ska skickas till månen. Hur stor är dess tyngd på månen? ' + MANEN)},
    '4.473': {'t': p('Vilken storhet mäts i enheten newton?')},
    '4.474': {'t': p('På en planet hänger en vikt som väger 4,0 kg stilla i en kraftmätare. Kraftmätaren visar 14,8 N. Hur stor är tyngdaccelerationen på planeten?')},
    '4.498': {'t': p('Ett föremål hängs i en fjädervåg på jorden, och fjädervågen visar 4,90 N. ' + MANEN,
                     '<strong>a)</strong> Vad visar fjädervågen på månen?',
                     '<strong>b)</strong> Föremålet vägs i stället på en balansvåg, där det jämförs med vikter. Vilken massa visar balansvågen på månen?')},
    '4.503': {'t': p('En astronaut hoppar rakt upp på jorden och lyfter då tyngdpunkten 0,40 m. Hur högt kommer astronauten på Mars om astronauten hoppar med samma fart? ' + MARS + ' Bortse från luftmotståndet.')},
    '4.758': {'t': p('Diagrammet visar sambandet mellan massa och tyngdkraft på en främmande planet. Tyngdkraften på ett föremål är 24 N. Hur stor massa har föremålet?') + FIG},
    '4.759': {'t': p('En boll har släppts och faller. Vilken bild visar krafterna på bollen under fallet? Bortse från luftmotståndet.') + FIG},
    '4.760': {'t': p('Två föremål hänger stilla i var sin kraftmätare på samma planet. Vad visar kraftmätaren vid B?') + FIG},
    '4.761': {'t': p('Diagrammet jämför två planeter. Hur många gånger större tyngdkraft påverkas ett föremål av på planet B än på planet A?') + FIG},
    '4.762': {'t': p('Två bollar släpps från samma höjd. Pilarna visar tyngdkrafterna. Vad gäller för bollarnas acceleration? Bortse från luftmotståndet.') + FIG},
    '4.763': {'t': p('Tre bollar med samma massa är på samma höjd. Pilarna visar deras hastigheter just då. Boll B vänder och har hastigheten noll. Vilken boll påverkas av störst tyngdkraft?') + FIG},
    '4.881': {'t': p('På en planet har man mätt tyngdkraften på föremål med olika massa. Diagrammet visar resultatet.') + FIG + p('Hur stor är tyngdaccelerationen på planeten?')},
    '4.883': {'t': p('En provlåda hänger stilla i en kraftmätare på månen. Kraftmätaren visar 81 N. Tyngdaccelerationen på månen är 1,62 N/kg.') + FIG + p('Hur stor massa har lådan?')},
    '4.884': {'t': p('En bil väger 1,5 ton.') + FIG + p('Hur stor är tyngdkraften på bilen?')},
    '4.885': {'t': p(r'Ett paket har tyngden 35 N på månen, där \(g=1{,}62\) m/s². Hur stor tyngd har paketet på jorden?')},
    '4.886': {'t': p(r'En astronaut orkar lyfta en låda med tyngden 400 N på jorden. Hur stor massa kan astronauten lyfta med samma kraft på månen, där \(g=1{,}62\) m/s²?')},
    '4.887': {'t': p('Ett föremål hänger stilla i en kraftmätare. På jorden visar kraftmätaren 12,0 N och på månen 2,03 N. Hur stor är tyngdaccelerationen på månen?')},
    '4.888': {'t': p('Låda A står på jorden och låda B på månen. Båda har tyngden 300 N. Tyngdaccelerationen är 9,82 m/s² på jorden och 1,62 m/s² på månen. Hur många gånger större massa har B än A?')},
    '4.889': {'t': p('En fjädervåg visar olika värden för samma föremål på jorden och på månen. En balansvåg, som jämför föremålet med vikter, visar däremot samma värde. Varför?')},
    '4.890': {'t': p(r'En marsbil väger 900 kg. Hur mycket mindre är tyngdkraften på den på Mars än på jorden? På Mars är \(g=3{,}71\) m/s².')},
    '4.897': {'t': p('En astronaut väger 100 kg med utrustning. På en planet visar en kraftmätare att tyngdkraften på astronauten är 2,48 kN. Vilken planet är det? Använd formelsamlingen.')},
    '4.898': {'t': p('En lastbil med last påverkas av tyngdkraften 0,15 MN. Hur stor massa har lastbilen med last?')},
    '4.899': {'t': p('En tom hink väger 0,80 kg. Den fylls med 8,0 liter vatten. Hur stor är tyngdkraften på hinken med vatten?')},
    '4.900': {'t': p('Låda A väger 12 kg och står på månen. Låda B väger 2,0 kg och står på jorden. Vilken låda påverkas av störst tyngdkraft? ' + MANEN)},
    '4.901': {'t': p('En kraftmätare kan visa högst 50 N. Hur stor massa kan man som mest hänga i den på jorden och på månen? ' + MANEN)},
}
