# Ma1 bråkform (omr brakform), omskrivet för hand 2026-11-17.
# "Ange a och b." och liknande står i kgInstruktion. "Välj ett alternativ." och "(Svara …)" är borttagna.
TN = 'Skriv täljaren och nämnaren i var sitt fält.'
FIG = '<span class="fig">[F1]</span>'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.03': {'t': p('Hur stor del av rektangeln är blå? Svara med ett bråk i enklaste form.') + '[F1]', 'kg': TN},
    '0.06': {'t': p('En pizza delas i åtta bitar som inte är lika stora. Tre bitar äts upp. Kan den del av pizzan som ätits '
                    'vara mindre än, lika med respektive större än \\(\\frac38\\)?'),
             'kg': 'Svaren står i ordningen mindre än, lika med, större än.'},
    '0.30': {'t': p('Skriv 0,125 som ett bråk i enklaste form.'), 'kg': TN},
    '0.126': {'t': p('Ett bråk kan förkortas till \\(\\frac7{12}\\). Summan av bråkets täljare och nämnare är 57.',
                     'Vilket är bråket?'), 'kg': TN},
    '0.132': {'t': p('Vilket av bråken \\(\\frac{17}{23}\\) och \\(\\frac{20}{27}\\) är störst? Motivera ditt svar utan att '
                     'skriva bråken i decimalform.')},
    '0.155': {'t': p('En sträcka består av tre delar. Den första delen är \\(\\frac25\\) av hela sträckan. Den andra delen är '
                     '\\(\\frac34\\) så lång som den första. Den tredje delen är 42 m.', 'Hur lång är hela sträckan?')},
    '0.306': {'t': p('Vilket bråk ligger närmast 1?')},
    '0.591': {'t': p('Amir säger: ”Om man lägger samma positiva tal till täljaren och nämnaren blir bråket större.”',
                     'Undersök påståendet för \\(\\frac{a}{b}\\) och \\(\\frac{a+k}{b+k}\\), där \\(a\\), \\(b\\) och \\(k\\) är '
                     'positiva tal. När ökar värdet, när minskar det och när är det oförändrat?',
                     'Johanna säger: ”Det nya värdet ligger alltid mellan det gamla värdet och 1.” Formulera ett påstående '
                     'som stämmer, även när värdena är lika, och bevisa det. Det räcker inte med exempel.')},
    '0.941': {'t': p('Vilket av talen är störst?')},
    '0.1200': {'t': p('En paj är delad i 8 lika stora bitar. De färgade bitarna har ätits upp.') + FIG +
               p('Hur stor del av pajen har ätits upp? Svara med ett bråk.')},
    '0.1201': {'t': p('Rektangeln är indelad i lika stora rutor.') + FIG +
               p('Hur stor del av rektangeln är färgad? Svara med ett bråk i enklaste form.')},
    '0.1202': {'t': p('Tallinjen är delad i lika stora delar.') + FIG + p('Vilket tal markerar P? Skriv talet i decimalform.')},
    '0.1203': {'t': p('En pizza är delad i 12 lika stora bitar. Efter middagen finns de bitar kvar som visas i figuren.') + FIG +
               p('Hur stor del av pizzan har ätits? Svara med ett bråk i enklaste form.')},
    '0.1206': {'t': p('I en klass med 25 elever cyklar \\(\\frac35\\) till skolan. Hur många elever cyklar?')},
    '0.1209': {'t': p('Vilket tal ska stå i rutan? \\(\\frac46=\\frac{\\square}{15}\\)')},
    '0.1210': {'t': p('En chokladkaka har 18 rutor. Lina äter \\(\\frac13\\) av kakan. Omar äter sedan en tredjedel av det som '
                      'finns kvar.') + FIG + p('Hur stor del av hela kakan finns kvar till sist? Svara med ett bråk.')},
    '0.1211': {'t': p('En vattentank är fylld till \\(\\frac25\\). Då innehåller den 18 liter.') + FIG +
               p('Hur många liter rymmer tanken när den är full?')},
    '0.1212': {'t': p('Den stora triangeln är delad i lika stora trianglar.') + FIG +
               p('Hur stor del av den stora triangeln är färgad? Svara med ett bråk.')},
}
