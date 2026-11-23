"""AI kapitel 2 (A*, girig bäst först, prioritetskö, viktade vägar), handskriven språkomskrivning 2026-11-23.
Körs med tools/sprak/ai_byt.py.

- Sammanhang + ”Labyrinten söks igenom med A* …” i två stycken blir ett stycke där roboten, musen eller spelet söker.
- Inledningar som var metatext (”Frågorna handlar om …”, ”Frågorna jämför …”).
- Prioritetsköerna i vardagen (2.88–2.91): ”Det fungerar som en prioritetskö … Talet inom parentes är värdet.”
  blir en mening om vad talet betyder.
"""


def sok(sista_mening, vem):
    return (f'{sista_mening}</p><p>Labyrinten söks igenom med A* ', f'{sista_mening} {vem} med A* ')


MUS = 'En mus letar efter osten i en labyrint.'
LEV = 'En leveransrobot ska hitta fram till en hylla i ett lager.'
FIGUR = 'En figur i ett datorspel ska ta sig till utgången.'
RADD = 'En räddningsrobot söker igenom ett rasat hus.'
GRAS = 'En gräsklipparrobot ska tillbaka till sin station.'
DRON = 'En drönare flyger mellan hyllorna i ett lager.'
SKATT = 'En spelfigur letar efter en skattkista.'
DAMM = 'En robotdammsugare letar efter sin laddstation.'
LAGER = 'En robot startar i den gröna rutan och ska hämta en låda i den röda rutan.'

R = {
    '2.54': [sok(LAGER, 'Den söker vägen')],
    '2.92': [sok(MUS, 'Den söker')],
    '2.93': [sok(LEV, 'Den söker vägen')],
    '2.94': [sok(FIGUR, 'Spelet söker vägen')],
    '2.95': [sok(RADD, 'Den söker')],
    '2.96': [sok(RADD, 'Den söker')],
    '2.97': [sok(GRAS, 'Den söker vägen')],
    '2.98': [sok(DRON, 'Den söker vägen')],
    '2.99': [sok(SKATT, 'Spelet söker')],
    '2.109': [sok(GRAS, 'Den söker vägen')],
    '2.110': [sok(DRON, 'Den söker vägen')],
    '2.111': [sok(SKATT, 'Spelet söker')],
    '2.112': [sok(DAMM, 'Den söker')],
    '2.67': [('Frågorna handlar om de tre värden som A* använder för varje ruta.',
              'A* räknar ut tre värden för varje ruta: g, h och f.')],
    '2.69': [('Frågorna jämför de två informerade sökningarna girig bäst först och A*.',
              'Girig bäst först och A* är två informerade sökningar.')],
    '2.70': [('Frågorna handlar om vad som skiljer informerade sökningar från oinformerade.',
              'En sökning kan vara informerad eller oinformerad.')],
    '2.71': [('Frågorna handlar om vilka heuristiker A* kan använda och fortfarande hitta den billigaste vägen.',
              'A* hittar inte alltid den billigaste vägen. Det beror på vilken heuristik h som används.')],
    '2.72': [('Frågorna handlar om prioritetsköer och hur A* använder dem.',
              'A* sparar rutorna som ska undersökas i en prioritetskö.')],
    '2.73': [('Frågorna handlar om vägar där rutor eller kanter kostar olika mycket.',
              'I en del labyrinter och grafer kostar rutorna eller kanterna olika mycket.')],
    '2.81': [('Frågorna handlar om heuristiker. En heuristik h är',
              'En heuristik h är')],
    '2.105': [('Frågorna handlar om varför A* använder en prioritetskö för öppna listan.',
               'A* sparar öppna listan i en prioritetskö.')],
    '2.88': [('Talet är antal dagar kvar. Det fungerar som en prioritetskö där lägst värde tas ut först.</p><p>Talet inom '
              'parentes är värdet. Stegen:',
              'Beställningarna står i en prioritetskö där talet inom parentes är antalet dagar kvar och lägst värde '
              'tas ut först. Stegen:')],
    '2.89': [('Lägst tal betyder mest bråttom. Det fungerar som en prioritetskö där lägst värde tas ut först.</p><p>Talet '
              'inom parentes är värdet. Stegen:',
              'Patienterna står i en prioritetskö där talet inom parentes visar hur bråttom det är. Lägst tal tas ut '
              'först. Stegen:')],
    '2.90': [('Talet är laddningen i tiondelar. Det fungerar som en prioritetskö där lägst värde tas ut först.</p><p>Talet '
              'inom parentes är värdet. Stegen:',
              'Batterierna står i en prioritetskö där talet inom parentes är laddningen i tiondelar och lägst värde '
              'tas ut först. Stegen:')],
    '2.91': [('Det fungerar som en prioritetskö där lägst värde tas ut först.</p><p>Talet inom parentes är värdet. Stegen:',
              'Patienterna står i en prioritetskö där talet inom parentes är prioriteten och lägst värde tas ut först. '
              'Stegen:')],
}
