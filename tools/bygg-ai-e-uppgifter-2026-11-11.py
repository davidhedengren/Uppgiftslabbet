"""AI-banken 2026-11-11: sju korta E-uppgifter i Kunskapsgymmets format.

Användarbeslut: banken ska ha många E-uppgifter. Efter nivåindelningen
(AI_NIVAINDELNING.md) hade A*-sökning, g/h/f och viktade vägar mest C. Här
läggs E-uppgifter till: ett steg med given regel, h för en ruta, f när g är
givet eller följer en rak väg och kostnaden för givna vägar.

Kör efter bygg-ai-kunskapsgymmet-2026-11-11.py och före bygg-ai-nivaer-2026-11-11.py.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_spec = importlib.util.spec_from_file_location('ai_kg', os.path.join(HERE, 'bygg-ai-kunskapsgymmet-2026-11-11.py'))
K = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(K)
from ai_figurer import step, maze, weighted_graph  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402

p, alt, num, val, kg_task = K.p, K.alt, K.num, K.val, K.kg_task
BANK = 'uppgifterai.js'
MARK = [('#fff3b0', 'Markerad ruta')]


def t247():
    rows = ['..#.', '.S..', '.#.G']
    s, g = A.parse(rows)
    nb = {A.cname(v): (1, A.manhattan(v, g)) for v in A.neigh(rows, s)}
    f = {k: a + b for k, (a, b) in nb.items()}
    assert f == {'A2': 5, 'B3': 3, 'B1': 5} and A.cname(A.astar(rows)['order'][1]) == 'B3'
    intro = maze(rows, s, g) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). Start har just tagits ut, och dess grannar har lagts in i öppna listan.')
    a = val('Vilken ruta tar A* ut härnäst?',
            [step('Grannarna till start har g = 1', 'A2: h = 2 + 2 = 4, f = 5. B3: h = 1 + 1 = 2, f = 3. B1: h = 1 + 3 = 4, f = 5.'),
             step('Lägst f tas ut', 'B3 har f = 3.')],
            [alt('A2', False, 'A2 har f = 1 + 4 = 5.'), alt('B1', False, 'B1 har f = 1 + 4 = 5.'),
             alt('B3', True, 'B3 ligger närmast målet och har lägst f = 3.'), alt('C2', False, 'C2 är en vägg och kan inte läggas in i öppna listan.')],
            'Räkna f = g + h för starts grannar. Alla har g = 1.', 2)
    b = num('Vilket f-värde har B3?', [step('f = g + h', 'B3 ligger ett steg från start, g = 1. h = 1 + 1 = 2. f = 1 + 2 = 3.')], 3,
            'g är 1 för en granne till start.', 1)
    return kg_task('2.47', 'astar_sokning', 'A*:s första val', intro, [a, b], 'A* tar ut den ruta i öppna listan som har lägst f = g + h.', ['procedur'], 1)


def t248():
    rows = ['S..G', '.#..', '....']
    s, g = A.parse(rows)
    assert A.cname(A.greedy(rows)['order'][1]) == 'A2'
    intro = maze(rows, s, g) + p('Labyrinten söks igenom med girig bäst först (h = Manhattanavstånd).')
    a = val('Vilken ruta tar girig bäst först ut efter start?',
            [step('Jämför h för grannarna till start', 'A2: h = 0 + 2 = 2. B1: h = 1 + 3 = 4.'), step('Lägst h vinner', 'A2 ligger närmast målet.')],
            [alt('A2', True, 'A2 har lägst h = 2.'), alt('B1', False, 'B1 har h = 4, längre från målet.'),
             alt('B2', False, 'B2 är en vägg och kan inte läggas in i öppna listan.'), alt('A3', False, 'A3 är inte granne till start.')],
            'Girig bäst först jämför bara h.', 1)
    b = num('Vilket h-värde har den rutan?', [step('h = radskillnad + kolumnskillnad', 'A2 och målet A4 ligger på samma rad, två kolumner isär: h = 2.')], 2,
            'Räkna rader och kolumner till målet.', 1)
    return kg_task('2.48', 'astar_sokning', 'Girig bäst först tar ett steg', intro, [a, b], 'Girig bäst först väljer den ruta som verkar ligga närmast målet.', ['procedur'], 1)


def t249():
    rows = ['S....', '.#.#.', '.....', '...#G']
    s, g = A.parse(rows)
    P, Q = (0, 2), (2, 3)
    assert A.manhattan(P, g) == 5 and A.manhattan(Q, g) == 2
    intro = maze(rows, s, g, {P: 'P', Q: 'Q'}, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet).')
    a = num('Bestäm h för P.', [step('h = radskillnad + kolumnskillnad', 'P ligger i A3 och målet i D5: 3 + 2 = 5.')], 5, 'Räkna rader och kolumner, utan väggar.', 1)
    b = num('Bestäm h för Q.', [step('h = radskillnad + kolumnskillnad', 'Q ligger i C4 och målet i D5: 1 + 1 = 2.')], 2, 'Räkna rader och kolumner, utan väggar.', 1)
    return kg_task('2.49', 'astar_varden', 'h för två rutor', intro, [a, b], 'Manhattanavståndet är antalet rader plus antalet kolumner till målet.', ['procedur'], 1)


def t250():
    rows = ['S.#..', '..#..', '.....', '....G']
    s, g = A.parse(rows)
    P = (0, 3)
    gv = A.dist_all(rows, s)[P]
    assert gv == 7 and A.manhattan(P, g) == 4
    intro = (maze(rows, s, g, {P: 'P'}, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet).') +
             p('Den kortaste vägen från start till P går runt väggen och har g = 7.'))
    a = num('Bestäm h för P.', [step('h = radskillnad + kolumnskillnad', 'P ligger i A4 och målet i D5: 3 + 1 = 4.')], 4, 'h räknas utan väggar.', 1)
    b = num('Bestäm f för P.', [step('f = g + h', 'g = 7 är givet och h = 4: f = 7 + 4 = 11.')], 11, 'Använd det givna g-värdet.', 2)
    return kg_task('2.50', 'astar_varden', 'f när g är givet', intro, [a, b], 'f = g + h, där g är kostnaden hittills och h uppskattningen kvar.', ['procedur'], 1)


def t251():
    rows = ['S...', '....', '...G']
    s, g = A.parse(rows)
    P = (1, 2)
    assert A.dist_all(rows, s)[P] == 3 and A.manhattan(P, g) == 2
    intro = maze(rows, s, g, {P: 'P'}, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet). Labyrinten har inga väggar.')
    a = num('Bestäm g för P, alltså antalet steg från start till P.', [step('Inga väggar är i vägen', 'P ligger 1 rad och 2 kolumner från start: g = 3.')], 3, 'Räkna stegen från start till P.', 1)
    b = num('Bestäm h för P.', [step('h = radskillnad + kolumnskillnad', 'P ligger i B3 och målet i C4: 1 + 1 = 2.')], 2, 'Räkna rader och kolumner till målet.', 1)
    c = num('Bestäm f = g + h för P.', [step('g och h', 'g = 3 (B3 ligger 1 rad och 2 kolumner från start) och h = 2.'), step('f = g + h', 'f = 3 + 2 = 5.')], 5,
            'Bestäm g och h och lägg ihop dem.', 2)
    return kg_task('2.51', 'astar_varden', 'g, h och f utan väggar', intro, [a, b, c], 'Utan väggar i vägen är g antalet steg rakt från start.', ['procedur'], 1)


G252 = dict(nodes={'S': (50, 130), 'A': (240, 45), 'B': (240, 215), 'M': (430, 130)},
            edges=[('S', 'A', 4), ('A', 'M', 3), ('S', 'B', 2), ('B', 'M', 6), ('A', 'B', 1)])


def t252():
    r = A.ucs_graph(G252['edges'], 'S', 'M')
    assert r['cost'] == 6 and r['path'] == ['S', 'B', 'A', 'M']
    svg = weighted_graph(G252['nodes'], G252['edges'], 'S', 'M', 'Graf med noderna S, A, B och M. Talet vid varje kant är kostnaden.', 480)
    intro = svg + p('Talet vid varje kant är kostnaden att gå längs den, åt valfritt håll.')
    a = num('Vad kostar vägen S → A → M?', [step('Summera kanterna', '4 + 3 = 7.')], 7, 'Lägg ihop talen på kanterna längs vägen.', 1)
    b = val('Vilken av vägarna S → A → M och S → B → M är billigast?',
            [step('Jämför', 'S → A → M kostar 4 + 3 = 7. S → B → M kostar 2 + 6 = 8.')],
            [alt('S → A → M', True, 'Den kostar 7, mindre än 8.'), alt('S → B → M', False, 'Den kostar 2 + 6 = 8.'),
             alt('Lika billiga', False, 'De kostar 7 och 8.')], 'Räkna ut kostnaden för båda vägarna.', 1)
    c = num('Vad kostar den billigaste vägen från S till M?',
            [step('Pröva också vägen via båda A och B', 'S → B → A → M kostar 2 + 1 + 3 = 6.'), step('Jämför', '6 är mindre än 7 och 8.')], 6,
            'Det finns en väg med tre kanter som är billigare än båda vägarna ovan.', 2)
    return kg_task('2.52', 'viktade_vagar', 'Kostnaden för vägar i en liten graf', intro, [a, b, c], 'Kostnaden för en väg är summan av talen på kanterna.', ['procedur'], 1)


def t253():
    rows = ['S33.', '..3.', '...G']
    s, g = A.parse(rows)
    path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
    assert A.path_cost(rows, path) == 9
    intro = maze(rows, s, g) + p('Att gå in i en lerruta kostar 3 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0.')
    a = num('Hur många lerrutor går vägen A1 → A2 → A3 → A4 → B4 → C4 genom?',
            [step('Lerrutorna längs vägen', 'A2 och A3 är lera.')], 2, 'Leta efter rutor med siffran 3 längs vägen.', 1)
    b = num('Vad kostar vägen A1 → A2 → A3 → A4 → B4 → C4?',
            [step('Kostnad för varje ruta', 'A2 3, A3 3, A4 1, B4 1 och målet 1.'), step('Summera', '3 + 3 + 1 + 1 + 1 = 9.')], 9,
            'Start kostar 0. Räkna alla rutor du går in i.', 1)
    return kg_task('2.53', 'viktade_vagar', 'Lerrutor längs en väg', intro, [a, b], 'Lägg ihop kostnaden för varje ruta du går in i.', ['procedur'], 1)


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = [t247(), t248(), t249(), t250(), t251(), t252(), t253()]
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    assert len({u['id'] for u in bank}) == len(bank)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya E-uppgifter.')


if __name__ == '__main__':
    main()
