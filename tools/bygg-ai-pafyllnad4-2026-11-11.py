"""AI-banken 2026-11-11, sjunde omgången: 30 självrättande uppgifter, mest E-nivå.

Fortsatt påfyllnad mot målet 50–100 kort på träningsnivå 1–2 per område.
Kunskapsgymmets format (tal eller ett rätt alternativ per del), nivåer enligt
agent/AI_NIVAINDELNING.md. Nya sammanhang (robot i lager, ångra-knapp,
skrivarkö, akutmottagning) och nya frågeformer (vilken ruta ligger i kön, vilket
löv hamnar spelet i, hur många av rotens barn får exakt värde).

Kör efter bygg-ai-e-uppgifter-2026-11-11.py och före bygg-ai-nivaer-2026-11-11.py.
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
from ai_figurer import tab, step, maze, search_tree, weighted_graph, game_tree  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, num, val, kg_task, names, lista, pil = K.p, K.alt, K.num, K.val, K.kg_task, K.names, K.lista, K.pil
ORD = K.ORD
BANK = 'uppgifterai.js'
MARK = [('#fff3b0', 'Markerad ruta')]
ROBOT = 'Rutnätet visar ett lager. En robot startar i den gröna rutan och ska hämta en låda i den röda rutan.'


def med_sammanhang(u, text):
    """Lägg en sammanhangsmening före ”Labyrinten söks igenom …” i inledning och huvudtext."""
    key = '<p>Labyrinten söks igenom'
    assert u['spelIntro'].count(key) == 1 and u['t'].count(key) == 1, u['id']
    u['spelIntro'] = u['spelIntro'].replace(key, p(text) + key)
    u['t'] = u['t'].replace(key, p(text) + key)
    return u


# ---------------------------------------------------------------- kö och stack

def t144():
    st = ['rita linje', 'fyll färg', 'skriv text', 'flytta figur']
    undone = [st.pop(), st.pop()]
    assert undone == ['flytta figur', 'skriv text'] and len(st) == 2
    intro = (p('Ett ritprogram sparar varje ändring i en stack. Ångra-knappen tar bort den översta ändringen.') +
             p('Ändringarna görs i ordningen: rita linje → fyll färg → skriv text → flytta figur. Sedan trycker du två gånger på Ångra.'))
    a = val('Vilken ändring ångras vid det andra trycket?',
            [step('Den senaste ändringen ligger överst', '”flytta figur” ångras först, sedan ”skriv text”.')],
            [alt('rita linje', False, 'Den gjordes först och ligger nederst i stacken.'), alt('fyll färg', False, 'Den ligger kvar efter två tryck.'),
             alt('skriv text', True, 'Efter att ”flytta figur” ångrats ligger ”skriv text” överst.'),
             alt('flytta figur', False, 'Den ångras vid det första trycket.')],
            'Vilken ändring ligger överst efter det första trycket?', 1)
    b = num('Hur många ändringar finns kvar i stacken?', [step('Fyra ändringar, två ångrade', '4 − 2 = 2.')], 2, 'Varje tryck tar bort en ändring.', 1)
    return kg_task('1.44', 'ko_stack', 'Ångra-knappen som stack', intro, [a, b], 'Ångra tar alltid bort den senaste ändringen.', ['begrepp'], 1)


def t145():
    q = ['Prov', 'Bild', 'Lista']
    first = q.pop(0)
    q.append('Karta')
    assert first == 'Prov' and q == ['Bild', 'Lista', 'Karta']
    intro = (p('En skrivare skriver ut dokument i den ordning de skickas. Dokumenten väntar i en FIFO-kö.') +
             p('Prov, Bild och Lista skickas i den ordningen. Skrivaren skriver ut ett dokument. Sedan skickas Karta.'))
    a = val('Vilket dokument skrivs ut härnäst?',
            [step('Prov är redan utskrivet', 'Kvar i kön står Bild, Lista och sist Karta.')],
            [alt('Bild', True, 'Bild skickades före Lista och Karta och står först i kön.'), alt('Lista', False, 'Lista står efter Bild.'),
             alt('Karta', False, 'Karta skickades sist och står längst bak.'), alt('Prov', False, 'Prov har redan skrivits ut.')],
            'Vilket dokument har väntat längst?', 1)
    b = num('Hur många dokument väntar i kön när Karta har skickats?', [step('Räkna', 'Bild, Lista och Karta: 3 dokument.')], 3,
            'Ett dokument har skrivits ut och ett nytt har tillkommit.', 1)
    return kg_task('1.45', 'ko_stack', 'Skrivarkön', intro, [a, b], 'I en FIFO-kö kommer det dokument först som skickades först.', ['begrepp'], 1)


# ---------------------------------------------------------------- kön under sökningen

TREE_146 = dict(nodes={'S': (200, 35), 'A': (90, 110), 'B': (200, 110), 'C': (310, 110), 'D': (50, 185), 'E': (130, 185),
                       'F': (270, 185), 'G': (350, 185)},
                edges=[('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('A', 'E'), ('C', 'F'), ('C', 'G')],
                start='S', goals=['G'], width=400,
                title='Sökträd: S har barnen A, B och C. A har D och E, C har F och målet G.')


def t146():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D', 'E'], 'C': ['F', 'G']}
    q = ['S']
    for _ in range(2):
        n = q.pop(0)
        q += kids.get(n, [])
    assert q == ['B', 'C', 'D', 'E']
    intro = search_tree(**TREE_146) + p('Trädet söks igenom med BFS (vänster gren först).')
    a = num('Hur många noder ligger i kön direkt efter att A har tagits ut och dess barn lagts in?',
            [step('S tas ut', 'Kön blir A, B, C.'), step('A tas ut', 'D och E läggs in längst bak. Kön blir B, C, D, E.')], 4,
            'Skriv upp kön efter varje uttag.', 2)
    b = val('Vilken nod står först i kön då?',
            [step('Kön är B, C, D, E', 'B lades in före C, D och E.')],
            [alt('B', True, 'B står först. Den lades in när S togs ut.'), alt('D', False, 'D är A:s barn och hamnar längst bak, efter C.'),
             alt('C', False, 'C lades in efter B och står bakom B i kön.'), alt('E', False, 'E lades in sist.')],
            'Nya noder läggs längst bak i kön.', 1)
    return kg_task('1.46', 'ko_sokning', 'Kön efter två uttag', intro, [a, b], 'BFS tar ut noderna i den ordning de lades in.', ['procedur'])


TREE_147 = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'E': (290, 185),
                       'F': (110, 260), 'G': (210, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('D', 'F'), ('D', 'G')],
                start='S', goals=['G'], width=380,
                title='Sökträd: S har barnen A och B. A har C och D, D har F och målet G, och B har E.')


def t147():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E'], 'D': ['F', 'G']}
    st, out = ['S'], []
    while st:
        n = st.pop()
        out.append(n)
        if n == 'G':
            break
        st += list(reversed(kids.get(n, [])))
    assert out == ['S', 'A', 'C', 'D', 'F', 'G'] and st == ['B']
    intro = (search_tree(**TREE_147) + p('Trädet söks igenom med DFS (vänster gren först). Noderna sparas i en stack, '
                                         'och barnen läggs in så att det vänstra barnet hamnar överst.'))
    a = val('Vilken nod tas ut som fjärde nod, räknat med S?',
            [step('Följ vänster gren', 'S, A, C. C har inga barn, så D ligger överst och tas ut som fjärde nod.')],
            [alt('D', True, 'S, A, C och sedan D.'), alt('B', False, 'B ligger nederst i stacken och tas ut först när grenen under A är klar.'),
             alt('F', False, 'F tas ut som femte nod, efter D.'), alt('C', False, 'C tas ut som tredje nod.')],
            'Ta alltid ut den översta noden.', 2)
    b = num('Hur många noder ligger kvar i stacken när målet tas ut?',
            [step('Bara B ligger kvar', 'B lades in av S men hann aldrig tas ut. Hela grenen under A undersöktes först.')], 1,
            'Vilka noder lades in men togs aldrig ut?', 2)
    return kg_task('1.47', 'ko_sokning', 'Stacken när målet hittas', intro, [a, b], 'DFS undersöker hela vänstra grenen innan den går vidare.', ['procedur'])


M148 = ['S..', '.#.', '..G']


def t148():
    s, g = A.parse(M148)
    r = A.bfs(M148)
    assert names(r['snaps'][1][1]) == ['B1', 'A3'] and len(r['snaps'][2][1]) == 2
    intro = maze(M148, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    u = None
    a = val('Vilken ruta läggs in i kön när A2 tas ut?',
            [step('Grannarna till A2', 'Uppåt finns ingen ruta, åt höger A3, nedåt B2 som är en vägg, och åt vänster start, som redan är upptäckt.')],
            [alt('A3', True, 'A3 är den enda nya grannen till A2.'), alt('B2', False, 'B2 är en vägg och kan aldrig läggas in i kön.'),
             alt('A1', False, 'A1 är start och har redan tagits ut.'), alt('B1', False, 'B1 lades in när start togs ut.')],
            'Gå igenom grannarna i ordningen ↑ → ↓ ← och hoppa över väggar och redan upptäckta rutor.', 1)
    b = num('Hur många rutor ligger i kön efter det tredje uttaget?',
            [step('Kön efter varje uttag', tab(['Tas ut', 'Kön efter uttaget'], K.queue_rows(r)[:4])),
             step('Efter det tredje uttaget', 'B1 tas ut och lägger in C1. Kön är A3 och C1.')], 2, 'Skriv upp kön efter varje uttag.', 2)
    u = kg_task('1.48', 'ko_sokning', 'Robotens kö', intro, [a, b], 'Nya rutor läggs längst bak i kön. En ruta läggs bara in en gång.', ['procedur'])
    return med_sammanhang(u, ROBOT)


# ---------------------------------------------------------------- BFS och DFS

M149 = ['.S..#', '.#...', '...#.', '.#..G']
M150 = ['S.#..', '.##..', '....#', '#...G']
M151 = ['S...', '.##.', '.#G.', '....']
M152 = ['S..#.', '.#...', '.#.#.', '...#G']
M153 = ['S.#...', '..#.#.', '......', '.#.#.G']


def t151():
    s, g = A.parse(M151)
    r = A.bfs(M151)
    order = names(r['order'])
    assert order[-2:] == ['D4', 'C3'] and len(r['path']) - 1 == 6
    intro = maze(M151, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = num('Hur många steg från start ligger målet?',
            [step('Målet nås bara från C4 eller D3', 'Ingången till målet C3 är från höger (C4) eller nedifrån (D3).'),
             step('En kortaste väg', pil(names(r['path'])) + ': 6 steg.')], 6, 'Från vilken sida kan man gå in till målet?', 2)
    b = val('Vilken ruta tas ut direkt före målet?',
            [step('De sista uttagen', lista(order[-5:]) + '.'), step('D4 ligger också 6 steg från start', 'D4 lades in före målet och tas därför ut före det.')],
            [alt('D4', True, 'D4 ligger lika långt från start som målet och lades in före målet.'),
             alt('C4', False, 'C4 lägger in målet men tas ut tidigare, som tionde ruta.'),
             alt('D3', False, 'D3 tas ut som elfte ruta.'), alt('B4', False, 'B4 tas ut som åttonde ruta.')],
            'Vilka rutor ligger lika långt från start som målet?', 2)
    return kg_task('1.51', 'bfs', 'Målet i en ficka', intro, [a, b], 'BFS tar ut alla rutor på ett visst avstånd innan nästa avstånd.', ['procedur'])


TREE_154 = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'E': (250, 185),
                       'F': (330, 185)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F')],
                start='S', goals=['D'], width=380,
                title='Sökträd: S har barnen A och B. A har C och målet D, B har E och F.')


def t154():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E', 'F']}
    out = []

    def go(n):
        out.append(n)
        return n == 'D' or any(go(k) for k in reversed(kids.get(n, [])))
    go('S')
    assert out == ['S', 'B', 'F', 'E', 'A', 'D']
    intro = search_tree(**TREE_154) + p('Trädet söks igenom med DFS, men här undersöks den högra grenen först.')
    a = val('Vilken nod besöks som tredje nod, räknat med S?',
            [step('Höger gren först', 'S → B → F. F har inga barn, så sökningen backar till B och tar E.')],
            [alt('F', True, 'Från B går DFS först till det högra barnet F.'), alt('A', False, 'A besöks först när hela högra grenen är klar.'),
             alt('E', False, 'E besöks efter F, eftersom höger gren tas först.'), alt('C', False, 'C besöks aldrig, eftersom D hittas först i A:s högra gren.')],
            'Gå alltid till det högra barnet först.', 2)
    b = num('Hur många noder besöks, inklusive start och mål?', [step('Hela besöksordningen', lista(out) + ': 6 noder.')], 6,
            'Hela högra grenen under B besöks innan A.', 2)
    return kg_task('1.54', 'dfs', 'DFS med höger gren först', intro, [a, b], 'Ordningen mellan barnen avgör vilken gren DFS tar först.', ['procedur'])


# ---------------------------------------------------------------- A*-sökning

M255 = ['....', 'S.#G', '....']
M256 = ['S...', '#.#.', '...G']
M257 = ['S...', '..#.', '...G']


def t255():
    s, g = A.parse(M255)
    f = {A.cname(v): 1 + A.manhattan(v, g) for v in A.neigh(M255, s)}
    assert f == {'A1': 5, 'B2': 3, 'C1': 5}
    intro = maze(M255, s, g) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). Start har just tagits ut.')
    a = val('Vilken av grannarna till start har lägst f?',
            [step('Grannarna har g = 1', 'A1: h = 1 + 3 = 4. B2: h = 2. C1: h = 1 + 3 = 4.'), step('f = g + h', 'A1: 5, B2: 3, C1: 5.')],
            [alt('A1', False, 'A1 har f = 1 + 4 = 5.'), alt('B2', True, 'B2 ligger på samma rad som målet och har f = 3.'),
             alt('C1', False, 'C1 har f = 1 + 4 = 5.')], 'Räkna h för varje granne och lägg till g = 1.', 1)
    b = num('Vilket f-värde har A1?', [step('f = g + h', 'A1 ligger ett steg från start: g = 1. h = 1 + 3 = 4. f = 5.')], 5,
            'Räkna rader och kolumner från A1 till målet.', 1)
    return kg_task('2.55', 'astar_sokning', 'Lägst f bland grannarna', intro, [a, b], 'A* jämför f = g + h för rutorna i öppna listan.', ['procedur'], 1)


def t256():
    s, g = A.parse(M256)
    order = names(A.greedy(M256)['order'])
    assert order[:3] == ['A1', 'A2', 'A3']
    intro = maze(M256, s, g) + p('Labyrinten söks igenom med girig bäst först (h = Manhattanavstånd). Vid lika h väljs den ruta som kommer först i bokstavsordning.')
    a = val('Vilka två rutor tar girig bäst först ut efter start, i ordning?',
            [step('Första steget', 'Start har bara grannen A2, eftersom B1 är en vägg.'),
             step('Andra steget', 'Från A2 läggs A3 (h = 2 + 1 = 3) och B2 (h = 1 + 2 = 3) in. Lika h: A3 kommer först i bokstavsordning.')],
            [alt('A2 och A3', True, 'A2 är enda grannen, och A3 vinner över B2 på bokstavsordningen.'),
             alt('A2 och B2', False, 'B2 har samma h som A3 men kommer efter A3 i bokstavsordning.'),
             alt('B1 och B2', False, 'B1 är en vägg, så start har bara grannen A2.'), alt('A2 och A4', False, 'A4 är inte granne till A2.')],
            'Jämför h. Använd bokstavsordningen bara vid lika h.', 2)
    b = num('Vilket h-värde har A3?', [step('h = radskillnad + kolumnskillnad', 'A3 och målet C4: 2 + 1 = 3.')], 3, 'Räkna rader och kolumner till målet.', 1)
    return kg_task('2.56', 'astar_sokning', 'Girig bäst först två steg', intro, [a, b], 'Girig bäst först tar alltid rutan med lägst h.', ['procedur'])


def t257():
    s, g = A.parse(M257)
    r = A.astar(M257)
    assert names(r['order'])[:2] == ['A1', 'A2']
    openl = {'B1': (1, 4), 'A3': (2, 3), 'B2': (2, 3)}
    assert all(gg + hh == 5 for gg, hh in openl.values())
    intro = maze(M257, s, g) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). ' + K.B.ASTAR_TIE + ' A1 och A2 har tagits ut.')
    a = val('Vilka rutor ligger i öppna listan direkt efter att A2 har tagits ut?',
            [step('Start lade in A2 och B1', 'A2 togs ut, B1 ligger kvar.'), step('A2 lägger in sina nya grannar', 'A3 åt höger och B2 nedåt.')],
            [alt('B1, A3 och B2', True, 'B1 ligger kvar från start, och A2 lägger in A3 och B2.'),
             alt('A3 och B2', False, 'B1 lades in när start togs ut och ligger kvar.'),
             alt('B1 och A3', False, 'B2 är också en ny granne till A2.'), alt('A3, B2 och B3', False, 'B3 är en vägg och kan inte läggas in.')],
            'Vilka rutor har lagts in men inte tagits ut?', 2)
    b = num('Hur många av rutorna i öppna listan har f = 5?',
            [step('f för varje ruta', 'B1: 1 + 4 = 5. A3: 2 + 3 = 5. B2: 2 + 3 = 5.')], 3, 'Räkna f = g + h för varje ruta i öppna listan.', 2)
    return kg_task('2.57', 'astar_sokning', 'Öppna listan efter två uttag', intro, [a, b], 'Öppna listan innehåller rutor som har lagts in men inte tagits ut.', ['procedur'])


M258 = ['S....', '.###.', '.....', '....G']


def t258():
    s, g = A.parse(M258)
    P, Q = (0, 4), (3, 1)
    hP, hQ = A.manhattan(P, g), A.manhattan(Q, g)
    assert (hP, hQ) == (3, 3) and 6 + hP == 9 and 3 + hQ == 6
    intro = (maze(M258, s, g, {P: 'P', Q: 'Q'}, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd).') +
             p('Båda rutorna ligger i öppna listan. P har g = 6 och Q har g = 3.'))
    a = val('Vilken av P och Q tar A* ut först?',
            [step('h för rutorna', 'P i A5: 3 + 0 = 3. Q i D2: 0 + 3 = 3.'), step('f = g + h', 'P: 6 + 3 = 9. Q: 3 + 3 = 6.')],
            [alt('P', False, 'P har samma h men högre g, f = 9.'), alt('Q', True, 'Q har lägst f = 6.'),
             alt('Båda samtidigt', False, 'A* tar ut en ruta i taget.')], 'Lägg ihop det givna g med h.', 2)
    b = num('Hur stort är f för P?', [step('f = g + h', 'f = 6 + 3 = 9.')], 9, 'g är givet. Räkna h.', 1)
    return kg_task('2.58', 'astar_sokning', 'Två rutor i öppna listan', intro, [a, b], 'Samma h kan ge olika f när g skiljer sig.', ['procedur'], 1)


# ---------------------------------------------------------------- g, h och f

M259 = ['S...#', '.#...', '...#.', '.#..G']
M261 = ['S.#..', '..#..', '..#..', '....G']


def t259():
    s, g = A.parse(M259)
    P = (1, 2)
    assert A.manhattan(P, g) == 4
    intro = (maze(M259, s, g, {P: 'P'}, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet).') +
             p('Rutan P har g = 3.'))
    a = num('Hur stort är h för P?', [step('h = radskillnad + kolumnskillnad', 'P ligger i B3 och målet i D5: 2 + 2 = 4.')], 4, 'Räkna rader och kolumner, utan väggar.', 1)
    b = num('Hur stort är f för P?', [step('f = g + h', 'f = 3 + 4 = 7.')], 7, 'Lägg ihop det givna g och h.', 1)
    return kg_task('2.59', 'astar_varden', 'h och f för en ruta i lagret', intro, [a, b], 'f är summan av kostnaden hittills och uppskattningen kvar.', ['procedur'], 1)


def t260():
    rows = ['S.....', '..#...', '..#...', '.....G']
    s, g = A.parse(rows)
    marks = {(0, 4): 'P', (3, 1): 'Q', (2, 4): 'R'}
    h = {k: A.manhattan(c, g) for c, k in marks.items()}
    assert h == {'P': 4, 'Q': 4, 'R': 2}
    intro = maze(rows, s, g, marks, extra_legend=MARK) + p('Labyrinten söks igenom med girig bäst först (h = Manhattanavstånd till målet).')
    a = val('Vilken av rutorna P, Q och R ligger närmast målet enligt h?',
            [step('h för rutorna', 'P i A5: 3 + 1 = 4. Q i D2: 0 + 4 = 4. R i C5: 1 + 1 = 2.')],
            [alt('P', False, 'P ligger 3 rader och 1 kolumn från målet, h = 4.'), alt('Q', False, 'Q ligger på samma rad som målet men fyra kolumner bort, h = 4.'),
             alt('R', True, 'R har lägst h = 2.'), alt('P och Q lika', False, 'P och Q har samma h, men R har lägre.')],
            'Räkna rader och kolumner till målet för varje ruta.', 1)
    b = num('Hur stort är h för Q?', [step('h = radskillnad + kolumnskillnad', 'Q ligger i D2 och målet i D6: 0 + 4 = 4.')], 4, 'Q och målet ligger på samma rad.', 1)
    return kg_task('2.60', 'astar_varden', 'Närmast målet enligt h', intro, [a, b], 'h är antalet rader plus kolumner till målet.', ['procedur'], 1)


def t261():
    s, g = A.parse(M261)
    P = (0, 3)
    gv = A.dist_all(M261, s)[P]
    assert gv == 9 and A.manhattan(P, g) == 4
    intro = maze(M261, s, g, {P: 'P'}, extra_legend=MARK) + p(K.B.ASTAR_GH)
    vp = names(A.bfs(M261, goal=P)['path'])
    a = num('Bestäm g för P, alltså längden på den kortaste vägen från start till P.',
            [step('Väggen i kolumn 3 måste rundas nedtill', pil(vp) + '.'), step('Räkna stegen', f'{len(vp)} rutor ger {gv} steg.')], gv,
            'Var finns en öppning i väggen?', 3)
    b = num('Bestäm f = g + h för P.', [step('h = radskillnad + kolumnskillnad', 'P i A4 och målet i D5: 3 + 1 = 4.'), step('f = g + h', f'f = {gv} + 4 = {gv + 4}.')],
            gv + 4, 'g följer gångarna, h räknas rakt.', 3)
    return kg_task('2.61', 'astar_varden', 'g runt en lång vägg', intro, [a, b], 'g följer gångarna runt väggen, men h räknas rakt.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- viktade vägar

G262 = dict(nodes={'S': (50, 130), 'A': (180, 45), 'B': (180, 215), 'C': (320, 130), 'M': (450, 130)},
            edges=[('S', 'A', 2), ('S', 'B', 4), ('A', 'C', 5), ('B', 'C', 1), ('C', 'M', 2), ('A', 'M', 9)])


def t262():
    costs = {'S → A → M': 11, 'S → A → C → M': 9, 'S → B → C → M': 7}
    assert A.ucs_graph(G262['edges'], 'S', 'M')['cost'] == 7
    svg = weighted_graph(G262['nodes'], G262['edges'], 'S', 'M', 'Graf med noderna S, A, B, C och M. Talet vid varje kant är kostnaden.', 500)
    intro = svg + p('Talet vid varje kant är kostnaden att gå längs den, åt valfritt håll. Tabellen visar tre vägar från S till M.') + tab(['Väg'], [[k] for k in costs])
    a = val('Vilken av de tre vägarna är billigast?',
            [step('Kostnad för varje väg', 'S → A → M: 2 + 9 = 11. S → A → C → M: 2 + 5 + 2 = 9. S → B → C → M: 4 + 1 + 2 = 7.')],
            [alt('S → A → M', False, 'Den har minst antal kanter men kostar 11.'), alt('S → A → C → M', False, 'Den kostar 2 + 5 + 2 = 9.'),
             alt('S → B → C → M', True, 'Den kostar 7, lägst av de tre.')], 'Summera kanterna för varje väg.', 1)
    b = num('Vad kostar den billigaste av de tre vägarna?', [step('Summera', '4 + 1 + 2 = 7.')], 7, 'Lägg ihop talen på kanterna.', 1)
    return kg_task('2.62', 'viktade_vagar', 'Tre vägar i en graf', intro, [a, b], 'Kostnaden för en väg är summan av kanternas tal.', ['procedur'], 1)


M263 = ['S44.', '....', '.3..', '...G']


def t263():
    s, g = A.parse(M263)
    p1 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
    p2 = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
    c1, c2 = A.path_cost(M263, p1), A.path_cost(M263, p2)
    assert (c1, c2) == (12, 6)
    intro = (maze(M263, s, g) + p('Att gå in i en isruta kostar 4, en lerruta 3 och en vit ruta eller målet 1. Start kostar 0.') +
             p('Väg 1 går längs översta raden och sedan ned. Väg 2 går längs vänsterkanten och sedan längs nedersta raden.'))
    a = val('Vilken väg är billigast?',
            [step('Väg 1', 'A2 och A3 är is: 4 + 4 + 1 + 1 + 1 + 1 = 12.'), step('Väg 2', 'Bara vita rutor: 6 steg som kostar 1 var, 6.')],
            [alt('Väg 1', False, 'Väg 1 går genom två isrutor och kostar 12.'), alt('Väg 2', True, 'Väg 2 undviker is och lera och kostar 6.'),
             alt('De kostar lika mycket', False, 'Båda har 6 steg, men väg 1 går genom is.')], 'Leta efter is och lera längs vägarna.', 1)
    b = num('Vad kostar väg 1?', [step('Kostnad för varje ruta', 'A2 4, A3 4, A4 1, B4 1, C4 1 och målet 1.'), step('Summera', '4 + 4 + 1 + 1 + 1 + 1 = 12.')], 12,
            'Start kostar 0.', 1)
    return kg_task('2.63', 'viktade_vagar', 'Två vägar runt isen', intro, [a, b], 'Samma antal steg kan kosta olika mycket.', ['procedur'], 1)


M264 = ['.....', '.#.#.', 'S433G']


def t264():
    s, g = A.parse(M264)
    straight = [s, (2, 1), (2, 2), (2, 3), (2, 4)]
    c, path = A.ucs_grid(M264)
    assert A.path_cost(M264, straight) == 11 and c == 8 and len(path) - 1 == 8
    intro = maze(M264, s, g) + p('Att gå in i en isruta kostar 4, en lerruta 3 och en vit ruta eller målet 1. Start kostar 0.')
    a = num('Vad kostar den raka vägen C1 → C2 → C3 → C4 → C5?', [step('Kostnad för varje ruta', 'C2 4, C3 3, C4 3 och målet 1: 4 + 3 + 3 + 1 = 11.')], 11,
            'Summera kostnaden för rutorna du går in i.', 2)
    b = num('Vad kostar den billigaste vägen från start till mål?',
            [step('Gå runt över rad A', pil(names(path)) + '.'), step('Bara vita rutor', f'{len(path) - 1} steg som kostar 1 var: {c}.')], c,
            'Finns det en väg som undviker is och lera helt?', 3)
    cc = num('Hur många steg har den billigaste vägen?', [step('Räkna stegen', f'{len(path)} rutor ger {len(path) - 1} steg, dubbelt så många som den raka vägen.')],
             len(path) - 1, 'Räkna förflyttningarna längs omvägen.', 3)
    return kg_task('2.64', 'viktade_vagar', 'Den billiga omvägen', intro, [a, b, cc], 'En längre väg kan vara billigare om den undviker dyr terräng.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- prioritetsköer

def t265():
    q, out = [], []
    for op in [('Ali', 3), ('Bea', 1), ('Cem', 2), None, ('Dana', 1), None, None]:
        if op:
            q.append(op)
        else:
            q.sort(key=lambda x: x[1])
            out.append(q.pop(0)[0])
    assert out == ['Bea', 'Dana', 'Cem'] and q == [('Ali', 3)]
    intro = (p('På en akutmottagning får varje patient en prioritet. Lägst tal är mest brådskande och behandlas först.') +
             p('Ali (3), Bea (1) och Cem (2) kommer in. En patient behandlas. Dana (1) kommer in. Sedan behandlas två patienter till.'))
    a = val('Vem behandlas som andra patient?',
            [step('Första patienten', 'Bea har prioritet 1 och behandlas först.'), step('Dana kommer in med prioritet 1', 'Dana har nu lägst tal och behandlas som andra patient.')],
            [alt('Ali', False, 'Ali har prioritet 3 och får vänta längst.'), alt('Cem', False, 'Cem har prioritet 2, men Dana har 1.'),
             alt('Dana', True, 'Dana har prioritet 1, mest brådskande av dem som väntar.'), alt('Bea', False, 'Bea behandlas först.')],
            'Vem har lägst tal bland dem som väntar vid andra behandlingen?', 1)
    b = num('Hur många patienter väntar när de tre behandlingarna är klara?', [step('Bara Ali är kvar', 'Fyra patienter, tre behandlade: 1 kvar.')], 1,
            'Räkna patienter som kommit in och patienter som behandlats.', 1)
    return kg_task('2.65', 'prioritetsko', 'Akutmottagningens kö', intro, [a, b], 'I en prioritetskö avgör prioriteten, inte vem som kom först.', ['begrepp', 'procedur'], 1)


def t266():
    data = {'A': (2, 8), 'B': (5, 2), 'C': (3, 6), 'D': (6, 4), 'E': (1, 9)}
    f = {k: g + h for k, (g, h) in data.items()}
    srt = sorted(f, key=f.get)
    assert f == {'A': 10, 'B': 7, 'C': 9, 'D': 10, 'E': 10} and srt[:2] == ['B', 'C']
    intro = (p('Fem noder ligger i A*:s prioritetskö. Inga nya noder läggs in medan de två första tas ut.') +
             tab(['Nod', 'g', 'h'], [[k, str(g), str(h)] for k, (g, h) in data.items()]))
    a = val('Vilken nod tas ut som andra nod?',
            [step('f = g + h', 'A: 10, B: 7, C: 9, D: 10, E: 10.'), step('Lägst och näst lägst f', 'B tas ut först (7) och C som andra nod (9).')],
            [alt('B', False, 'B har lägst f och tas ut först.'), alt('C', True, 'C har näst lägst f = 9.'),
             alt('E', False, 'E har lägst g men f = 10.'), alt('D', False, 'D har f = 6 + 4 = 10.')], 'Räkna f för alla och sortera.', 2)
    b = num('Vilket f-värde har den nod som tas ut först?', [step('Lägst f', 'B: 5 + 2 = 7.')], 7, 'Räkna g + h för varje nod.', 1)
    return kg_task('2.66', 'prioritetsko', 'Andra uttaget ur A*:s kö', intro, [a, b], 'A* tar ut noderna i ordning efter f.', ['procedur'])


# ---------------------------------------------------------------- minimax och alfa–beta

def t339():
    vals = [[2, 9], [5, 4]]
    assert A.minimax(vals, True) == 4
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': vals[0]}, {'n': 'B', 'k': vals[1]}]}
    intro = game_tree(tree, True, 'Spelträd med MAX i roten R och MIN-noderna A och B. Löven heter L1–L4.') + p('Spelträdet söks igenom med minimax.')
    a = val('I vilket löv hamnar spelet om båda spelarna spelar så bra som möjligt?',
            [step('MIN väljer i A och B', 'A = min(2, 9) = 2. B = min(5, 4) = 4.'), step('MAX väljer i roten', 'R = max(2, 4) = 4 via B, och i B väljer MIN lövet 4.')],
            [alt('L1', False, 'L1 = 2 är A:s värde, men roten väljer B.'), alt('L2', False, 'L2 = 9 är högst, men MIN i A väljer aldrig 9.'),
             alt('L3', False, 'L3 = 5, men MIN i B väljer 4.'), alt('L4', True, 'Roten väljer B, och MIN i B väljer lövet 4.')],
            'Bestäm A och B först. Följ sedan valen från roten.', 2)
    b = num('Vilket värde får roten?', [step('R = max(A, B)', 'R = max(2, 4) = 4.')], 4, 'Roten väljer det största av A och B.', 1)
    return kg_task('3.39', 'minimax', 'Lövet där spelet slutar', intro, [a, b], 'MIN väljer minsta värdet och MAX största.', ['procedur'], 1)


def ab_extra(id_, values, root_max, third, ledtrad):
    r = T.build(values, root_max)
    v, ev, cuts, notes = T.alphabeta(r)
    n = len(T.leaves(r))
    pr = T.pruned_leaves(cuts)
    rot = 'MAX' if root_max else 'MIN'
    intro = game_tree(T.to_figure(r), root_max, f'Spelträd med {rot} i roten R och {n} löv, L1–L{n}.') + p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).')
    a = num('Vilket värde får roten?', [step('Gren för gren', *[x for k in r['kids'] for x in T.subtree_lines(k, notes)], T.node_line('R', notes['R']))],
            v, 'Bestäm först rotens första barn helt.', 2)
    kids = [k['name'] for k in r['kids']]
    if third == 'exakt':
        ex = [k for k in kids if notes[k]['kind'] == 'exakt']
        c = num('Hur många av rotens barn får ett exakt värde?',
                [step('Barn som avbryts får bara en gräns', ', '.join(f'{k}: {"exakt" if notes[k]["kind"] == "exakt" else "gräns"}' for k in kids) + '.')], len(ex),
                'Vilka av rotens barn avbryts av en beskärning?', 4)
    elif third == 'sist':
        last = ev[-1]
        opts = sorted({last, ev[-2], ev[0]} | ({pr[0]} if pr else set()), key=lambda s: int(s[1:]))
        c = val('Vilket löv utvärderas sist?',
                [step('Utvärderade löv i ordning', ', '.join(ev) + '.')],
                [alt(x, x == last, (f'{x} är det sista lövet som utvärderas.' if x == last else
                                    (f'{x} beskärs och utvärderas aldrig.' if x in pr else f'{x} utvärderas tidigare.'))) for x in opts],
                'Tänk på vilka löv som beskärs i slutet av trädet.', 4)
    elif third == 'alfa':
        last = kids[-1]
        prev = [notes[k] for k in kids[:-1]]
        g = max(nt['value'] for nt in prev if nt['kind'] == 'exakt')
        c = num(f'Vilket värde har α i roten när sökningen går vidare till {last}?',
                [step(f'Rotens barn före {last}', ', '.join(f'{k}: {"exakt " if notes[k]["kind"] == "exakt" else ("minst " if notes[k]["max"] else "högst ")}{T.fmt(notes[k]["value"])}' for k in kids[:-1]) + '.'),
                 step('α är det bästa MAX i roten är säker på', f'α = {T.fmt(g)}.')], g, f'Vilka av rotens barn är klara innan {last}?', 4)
    else:
        raise ValueError(third)
    b = num('Hur många löv utvärderas inte?',
            [step(f'I {cc[0]} efter {cc[1]}: α = {T.fmt(cc[2])} ≥ β = {T.fmt(cc[3])}', f'{T.cap(" och ".join(T.pruned_desc(cc[4])))} beskärs.') for cc in cuts] +
            [step('Räkna', f'{", ".join(pr)}: {len(pr)} av {n} löv.')], len(pr), 'Leta efter noder där α ≥ β innan alla barn är undersökta.', 4)
    return kg_task(id_, 'alfa_beta', 'Alfa–beta med direkt rättning', intro, [a, b, c], ledtrad, ['procedur', 'begrepp'])


def build_all():
    out = [t144(), t145(), t146(), t147(), t148(),
           med_sammanhang(K.bfs_task('1.49', 'Robotens sökning', M149, 3, ['avst1', 'k', 'steg'], 'BFS tar ut rutorna i ordning efter avstånd.', (1, 2, 2)), ROBOT),
           K.bfs_task('1.50', 'BFS i en labyrint med flera vägar', M150, 7, ['k', 'avst2', 'antal'], 'Skriv upp kön efter varje uttag.', (2, 1, 2)),
           t151(),
           K.dfs_task('1.52', 'DFS genom en smal gång', M152, 4, 'Gå så långt det går i första tillåtna riktningen.'),
           K.dfs_task('1.53', 'DFS i 4 × 6 med lång omväg', M153, 7, 'DFS kan välja en lång väg om den första riktningen leder dit.'),
           t154(),
           K.astar_task('2.54', 'A* i ett lager', ['S..#', '.#..', '..#.', '...G'], 3, 'Räkna f = g + h för grannarna till varje uttagen ruta.'),
           t255(), t256(), t257(), t258(), t259(), t260(), t261(), t262(), t263(), t264(), t265(), t266(),
           K.mm_kg('3.37', [[4, 8], [6, 2, 9], [5, 7]], True, 'C', 'MIN-noderna väljer minsta värdet, roten största.'),
           K.mm_kg('3.38', [[[3, 7], [6, 1]], [[8, 2], [4, 5]]], False, 'E', 'Tre nivåer: växla mellan min och max.', (2, 2, 2)),
           t339(),
           ab_extra('3.40', [[4, 7], [2, 8], [5, 3], [6, 9]], True, 'exakt', 'Jämför varje MIN-barns första löv med α.'),
           ab_extra('3.41', [[3, 6], [7, 1], [2, 5]], False, 'sist', 'Roten är en MIN-nod. Jämför varje MAX-barns första löv med β.'),
           ab_extra('3.42', [[[2, 5], [6, 1]], [[7, 3], [4, 8]], [[1, 9], [6, 2]]], True, 'alfa', 'Bestäm A helt först. Då vet roten vad den minst kan få.')]
    out[11] = med_sammanhang(out[11], ROBOT)
    return out


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = build_all()
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    assert len({u['id'] for u in bank}) == len(bank)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya i denna omgång.')


if __name__ == '__main__':
    main()
