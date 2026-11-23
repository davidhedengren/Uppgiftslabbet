"""AI kapitel 1 (BFS, DFS, kö och stack), handskriven språkomskrivning 2026-11-23. Körs med tools/sprak/ai_byt.py.

- Uppgifter med ett sammanhang (robot, mus, drönare …) fick ”Labyrinten söks igenom med …” i ett eget stycke efter
  sammanhanget. Nu är det roboten, musen eller spelet som söker, i samma stycke. Standardmeningen i rena
  labyrintuppgifter står kvar (låst i ai-pafyllnad-2026-11-11.test.js och tydlig).
- Inledningar som var metatext (”Frågorna handlar om …”).
- ”den funna vägen” och ”med den översta noden överst”.
"""


def sok(sista_mening, vem, alg):
    """sista_mening: sammanhangets sista mening; vem: t.ex. 'Den söker' eller 'Spelet söker vägen'."""
    return (f'{sista_mening}</p><p>Labyrinten söks igenom med {alg} (ordning ↑ → ↓ ←).',
            f'{sista_mening} {vem} med {alg} (ordning ↑ → ↓ ←).')


LAGER = 'En robot startar i den gröna rutan och ska hämta en låda i den röda rutan.'
FIGUR = 'En figur i ett datorspel ska ta sig till utgången.'
RADD = 'En räddningsrobot söker igenom ett rasat hus.'
GRAS = 'En gräsklipparrobot ska tillbaka till sin station.'
DRON = 'En drönare flyger mellan hyllorna i ett lager.'
STACK = ('Bilden visar stacken just nu, med den översta noden överst.', 'Bilden visar stacken just nu.')
FUNNA = ('Hur många steg har den funna vägen?', 'Hur många steg har vägen?')

R = {
    '1.06': [FUNNA],
    '1.07': [FUNNA],
    '1.48': [sok(LAGER, 'Den söker vägen', 'BFS')],
    '1.49': [sok(LAGER, 'Den söker vägen', 'BFS')],
    '1.55': [('Frågorna handlar om bredden först-sökning (BFS) i en labyrint.',
              'En labyrint ska sökas igenom med bredden först-sökning (BFS).')],
    '1.56': [('Frågorna handlar om djupet först-sökning (DFS).',
              'En labyrint ska sökas igenom med djupet först-sökning (DFS).')],
    '1.57': [('Frågorna handlar om hur kön används när en labyrint söks igenom med BFS.',
              'När en labyrint söks igenom med BFS sparas rutorna som ska undersökas i en kö.')],
    '1.58': [('Frågorna handlar om skillnaden mellan oinformerade och informerade sökningar.',
              'Sökalgoritmer kan vara oinformerade eller informerade.')],
    '1.59': [('Frågorna handlar om vilken datastruktur en sökning använder.',
              'BFS och DFS sparar noderna som ska undersökas i olika datastrukturer.')],
    '1.60': [('Frågorna handlar om vad grannordningen betyder för BFS och DFS. Grannordningen',
              'Grannordningen')],
    '1.78': [STACK],
    '1.80': [STACK],
    '1.82': [STACK],
    '1.83': [sok('En robotdammsugare letar efter sin laddstation.', 'Den söker', 'BFS')],
    '1.84': [sok('En mus letar efter osten i en labyrint.', 'Den söker', 'BFS')],
    '1.85': [sok('En leveransrobot ska hitta fram till en hylla i ett lager.', 'Den söker vägen', 'BFS')],
    '1.86': [sok(FIGUR, 'Spelet söker vägen', 'BFS')],
    '1.87': [sok(RADD, 'Den söker', 'DFS')],
    '1.88': [sok(GRAS, 'Den söker vägen', 'DFS')],
    '1.89': [sok(DRON, 'Den söker vägen', 'DFS')],
    '1.90': [sok('En spelfigur letar efter en skattkista.', 'Spelet söker', 'DFS')],
    '1.100': [sok(FIGUR, 'Spelet söker vägen', 'DFS')],
    '1.101': [sok(RADD, 'Den söker', 'DFS')],
    '1.102': [sok(GRAS, 'Den söker vägen', 'DFS')],
    '1.103': [sok(DRON, 'Den söker vägen', 'DFS')],
}
