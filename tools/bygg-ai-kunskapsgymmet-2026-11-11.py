"""AI-banken 2026-11-11, sjätte omgången: 30 självrättande uppgifter för Kunskapsgymmet.

Användarens önskemål: fler varierade uppgifter, anpassade så att de på sikt kan
användas i Kunskapsgymmet. Varje del har därför ett svar som kan rättas
automatiskt, i samma format som de självrättande fysik- och matematikbankerna:

- `numeriskt`: heltal (antal, steg, kostnad, g/h/f, nodvärde), tolerans 0;
- `alternativ`: ett rätt alternativ, varje alternativ med kommentar.

Huvuduppgiften har `svarstyp:"flera_delar"`, `rättSvar` som lista i delarnas
ordning, `svarsstruktur:"ordnad"`, `spel:true` och `självrättning:true`. Listor
och vägar efterfrågas inte som fritext, eftersom de inte kan rättas säkert.

Kör efter de tidigare byggskripten (se AI_KUNSKAPSGYMMET_2026-11-11.md).
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_spec = importlib.util.spec_from_file_location('ai_omg3', os.path.join(HERE, 'bygg-ai-pafyllnad-2026-11-11.py'))
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)
from ai_figurer import tab, step, maze, search_tree, weighted_graph, game_tree, box_queue, box_stack  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, names, lista, pil = B.p, B.alt, B.names, B.lista, B.pil
BANK = 'uppgifterai.js'
ORD = {1: 'första', 2: 'andra', 3: 'tredje', 4: 'fjärde', 5: 'femte', 6: 'sjätte', 7: 'sjunde', 8: 'åttonde', 9: 'nionde', 10: 'tionde'}
ASTAR = 'Labyrinten söks igenom med A* (h = Manhattanavstånd). ' + B.ASTAR_TIE
LEFT = 'text-align:left'


# ---------------------------------------------------------------- Kunskapsgymmet-format

def num(fraga, steps, svar, ledtrad, tn):
    d = B.part(p(fraga), steps, f'{T.fmt(svar)}.', ledtrad, tn)
    d.update({'svarstyp': 'numeriskt', 'rättSvar': svar, 'tolerans': 0, 'självrättning': True,
              'svarFormat': 'numeriskt', 'svarEnhet': None, 'spel': True})
    return d


def val(fraga, steps, alts, ledtrad, tn):
    right = [a for a in alts if a['ratt']]
    assert len(right) == 1, fraga
    d = B.part(p(fraga + ' Välj ett alternativ.'), steps, right[0]['txt'] + '.', ledtrad, tn, alts)
    d.update({'svarstyp': 'alternativ', 'rättSvar': right[0]['txt'], 'tolerans': None, 'självrättning': True,
              'svarFormat': None, 'svarEnhet': None, 'spel': True})
    return d


def kg_task(id_, omr, familj, intro, parts, ledtrad, formaga, arbetsinsats=2):
    u = B.task(id_, omr, familj, intro, parts, ledtrad, formaga, arbetsinsats)
    u.update({'spel': True, 'självrättning': True, 'svarstyp': 'flera_delar',
              'rättSvar': [d['rättSvar'] for d in parts], 'tolerans': [d['tolerans'] for d in parts],
              'svarFormat': [d['svarFormat'] for d in parts], 'svarEnhet': [None for _ in parts],
              'svarsstruktur': 'ordnad', 'svarEtiketter': [d['etikett'] for d in parts]})
    return u


def position_comment(x, order, k, what='ruta', verb='tas ut'):
    if x in order:
        return f'{x} {verb} som {ORD.get(order.index(x) + 1, str(order.index(x) + 1) + ":e")} {what}.'
    never = 'tas aldrig ut' if verb == 'tas ut' else 'besöks aldrig'
    return f'{x} {never} innan sökningen stoppar.'


def kth_alts(order, k, extra, what='ruta', verb='tas ut', other=None):
    """Alternativ för frågan ”vilken … som nummer k”: rätt svar, grannar i ordningen och en extra feltanke.
    extra[0] är den ruta som den andra algoritmen (other) skulle ta som nummer k."""
    right = order[k - 1]
    cand = [order[k - 2], order[k]] + [x for x in extra if x not in (right, order[k - 2], order[k])][:1]
    opts = sorted(set([right] + cand))

    def kom(x):
        if x == right:
            return f'{x} {verb} som {ORD[k]} {what}.'
        c = position_comment(x, order, k, what, verb)
        if other and x == extra[0]:
            c += f' Det är den ruta som {other} skulle ta som {ORD[k]}.'
        return c
    return [alt(x, x == right, kom(x)) for x in opts]


def queue_rows(r):
    return [['Från början', A.cname(r['order'][0])]] + [[A.cname(n), ' '.join(names(q)) or 'tom'] for n, q in r['snaps']]


# ---------------------------------------------------------------- kö och stack

def t132():
    q = ['A', 'B', 'C', 'D']
    out = [q.pop(0), q.pop(0)]
    q.append('E')
    assert out == ['A', 'B'] and q == ['C', 'D', 'E']
    intro = p('Noder läggs in i en FIFO-kö och tas ut enligt följande:') + p('lägg in A, B, C och D → ta ut två noder → lägg in E.')
    a = val('Vilken nod står först i kön när stegen är gjorda?',
            [step('A och B tas ut', 'De lades in först. Kvar i kön står C, D och sedan E längst bak.')],
            [alt('A', False, 'A lades in först och har redan tagits ut.'), alt('C', True, 'C är den äldsta noden som är kvar i kön.'),
             alt('D', False, 'D står efter C i kön.'), alt('E', False, 'E lades in sist och står längst bak.')],
            'Vilka noder tas ut vid de två uttagen?', 1)
    b = num('Hur många noder ligger i kön när stegen är gjorda?',
            [step('Fyra in, två ut och en in till', '4 − 2 + 1 = 3. Kön är C, D, E.')], 3,
            'Räkna hur många noder som läggs in och hur många som tas ut.', 1)
    return kg_task('1.32', 'ko_stack', 'Kön efter några steg', intro, [a, b], 'I en FIFO-kö tas den nod ut som har legat längst.', ['procedur'], 1)


def t133():
    intro = (box_stack(['C', 'F', 'H', 'K'], 'Stack med C nederst och K överst.') + p('Bilden visar en stack. Noder tas ut en i taget.'))
    a = num('Hur många noder måste tas ut innan C kan tas ut?',
            [step('C ligger nederst', 'K, H och F ligger ovanpå C och måste tas ut först.')], 3, 'Hur många noder ligger ovanpå C?', 1)
    b = val('Vilken nod ligger överst efter två uttag?',
            [step('De två översta tas ut', 'K och H tas ut. Då ligger F överst.')],
            [alt('C', False, 'C ligger nederst och tas ut sist.'), alt('F', True, 'K och H tas ut, och F blir den översta.'),
             alt('H', False, 'H tas ut vid det andra uttaget.'), alt('K', False, 'K ligger överst från början och tas ut först.')],
            'Vilka två noder ligger överst från början?', 1)
    return kg_task('1.33', 'ko_stack', 'Uttag ur en stack', intro, [a, b], 'I en stack kan bara den översta noden tas ut.', ['procedur', 'begrepp'], 1)


def t134():
    ops = ['+P', '+Q', '+R', '-', '+S', '-', '-', '-']

    def run(lifo):
        s, out = [], []
        for op in ops:
            if op[0] == '+':
                s.append(op[1])
            else:
                out.append(s.pop() if lifo else s.pop(0))
        return out
    fifo, stack = run(False), run(True)
    assert fifo == ['P', 'Q', 'R', 'S'] and stack == ['R', 'S', 'Q', 'P']
    intro = p('Samma steg görs en gång med en FIFO-kö och en gång med en stack:') + p('lägg in P, Q och R → ta ut en nod → lägg in S → ta ut tre noder.')
    opts = lambda right, kom: [alt(x, x == right, kom[x]) for x in 'PQRS']  # noqa: E731
    a = val('Vilken nod tas ut som tredje nod med FIFO-kön?',
            [step('FIFO tar ut i samma ordning som noderna lades in', 'P, Q, R och sist S.')],
            opts('R', {'P': 'P lades in först och tas därför ut först.', 'Q': 'Q tas ut som andra nod.', 'R': 'R lades in som tredje nod och tas ut som tredje.',
                       'S': 'S lades in sist och tas ut sist.'}), 'I vilken ordning lades noderna in?', 1)
    b = val('Vilken nod tas ut som tredje nod med stacken?',
            [step('Första uttaget tar R', 'R ligger överst. Sedan läggs S in överst.'),
             step('De tre sista uttagen', 'S, sedan Q och sist P.')],
            opts('Q', {'P': 'P ligger nederst och tas ut sist.', 'Q': 'Efter R och S ligger Q överst.',
                       'R': 'R låg överst vid det första uttaget och togs ut först.', 'S': 'S tas ut som andra nod.'}), 'Skriv upp stacken efter varje steg.', 2)
    return kg_task('1.34', 'ko_stack', 'Tredje uttaget med kö och stack', intro, [a, b],
                   'Gör stegen två gånger: en gång där den äldsta noden tas ut och en gång där den senaste tas ut.', ['procedur'])


# ---------------------------------------------------------------- kön under sökningen

TREE_135 = dict(nodes={'S': (200, 35), 'A': (90, 110), 'B': (200, 110), 'C': (310, 110), 'D': (50, 185), 'E': (130, 185),
                       'F': (200, 185), 'G': (270, 185), 'H': (350, 185), 'I': (130, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'F'), ('C', 'G'), ('C', 'H'), ('E', 'I')],
                start='S', goals=['I'], width=400,
                title='Sökträd: S har barnen A, B och C. A har D och E, B har F, C har G och H, och E har målet I.')


def t135():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D', 'E'], 'B': ['F'], 'C': ['G', 'H'], 'E': ['I']}
    q, out, rows, longest = ['S'], [], [['Från början', 'S']], 1
    while q:
        n = q.pop(0)
        out.append(n)
        if n == 'I':
            rows.append([n, ' '.join(q) or 'tom'])
            break
        q += kids.get(n, [])
        longest = max(longest, len(q))
        rows.append([n, ' '.join(q) or 'tom'])
    assert out == ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] and longest == 5
    intro = search_tree(**TREE_135) + p('Trädet söks igenom med BFS (vänster gren först).')
    a = num('Hur många noder ligger som mest i kön samtidigt?',
            [step('Kön efter varje uttag', tab(['Tas ut', 'Kön efter uttaget'], rows)),
             step('Den längsta kön', 'Efter att C har tagits ut ligger D, E, F, G och H i kön.')], 5,
            'Skriv upp kön efter varje uttag och räkna noderna.', 2)
    b = val('Vilken nod tas ut direkt före målet I?',
            [step('I läggs in sist', 'I är barn till E och läggs in efter G och H. Därför tas G och H ut innan I.')],
            [alt('E', False, 'E lägger in I, men därefter tas F, G och H ut innan I.'), alt('F', False, 'F tas ut som sjunde nod.'),
             alt('H', True, 'H lades in före I och tas ut direkt före målet.'), alt('D', False, 'D tas ut som femte nod.')],
            'I vilken ordning lades G, H och I in i kön?', 2)
    return kg_task('1.35', 'ko_sokning', 'Den längsta kön', intro, [a, b],
                   'En nods barn läggs längst bak i kön. Kön kan bli lång när många noder på samma nivå har barn.', ['procedur'])


TREE_136 = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'E': (250, 185),
                       'F': (330, 185), 'G': (250, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'), ('E', 'G')],
                start='S', goals=['G'], width=380,
                title='Sökträd: S har barnen A och B. A har C och D, B har E och F, och E har målet G.')


def t136():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E', 'F'], 'E': ['G']}
    st, out, rows = ['S'], [], [['Från början', 'S']]
    while st:
        n = st.pop()
        out.append(n)
        if n != 'G':
            st += list(reversed(kids.get(n, [])))
        rows.append([n, ' '.join(st) or 'tom'])
        if n == 'G':
            break
    assert out == ['S', 'A', 'C', 'D', 'B', 'E', 'G'] and rows[2][1] == 'B D C'
    intro = (search_tree(**TREE_136) + p('Trädet söks igenom med DFS (vänster gren först). Noderna sparas i en stack, '
                                         'och barnen läggs in så att det vänstra barnet hamnar överst.'))
    a = val('Vilken nod ligger överst i stacken direkt efter att A har tagits ut och dess barn lagts in?',
            [step('S lägger in B och A', 'A hamnar överst och tas ut.'),
             step('A lägger in D och C', 'C läggs in sist och hamnar överst. Stacken är B, D, C med C överst.')],
            [alt('B', False, 'B ligger nederst. Den lades in av S före A:s barn.'), alt('C', True, 'C är A:s vänstra barn och läggs in sist.'),
             alt('D', False, 'D läggs in före C och ligger under C.'), alt('E', False, 'E läggs in först när B tas ut.')],
            'I vilken ordning läggs A:s barn in för att det vänstra ska hamna överst?', 2)
    b = num('Hur många noder har tagits ut ur stacken när målet tas ut, inklusive start och mål?',
            [step('Stacken efter varje uttag', tab(['Tas ut', 'Stacken efter uttaget'], rows)),
             step('Räkna uttagen', lista(out) + ': 7 noder. F tas aldrig ut.')], 7, 'Gå igenom hela vänstra grenen innan B.', 2)
    return kg_task('1.36', 'ko_sokning', 'Överst i stacken', intro, [a, b],
                   'Den översta noden tas ut. Barnen läggs på stacken i omvänd ordning, så att det vänstra barnet tas ut först.', ['procedur'])


M137 = ['S...', '.#.#', '...G']


def t137():
    s, g = A.parse(M137)
    r = A.bfs(M137)
    order = names(r['order'])
    longest = max(len(q) for _, q in r['snaps'])
    assert order == ['A1', 'A2', 'B1', 'A3', 'C1', 'A4', 'B3', 'C2', 'C3', 'C4'] and longest == 3
    intro = maze(M137, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = val('Vilka rutor ligger i kön direkt efter att start har tagits ut?',
            [step('Pröva grannarna i ordningen ↑ → ↓ ←', 'Uppåt finns ingen ruta. Åt höger A2, nedåt B1, åt vänster ingen ruta.')],
            [alt('A2 och B1', True, 'A2 (→) och B1 (↓) är de enda grannarna till start.'), alt('A2, B1 och B2', False, 'B2 är en vägg och kan aldrig läggas in i kön.'),
             alt('Bara A2', False, 'B1 är också granne till start.'), alt('A2 och A3', False, 'A3 ligger två steg från start.')],
            'Vilka grannar har start?', 1)
    b = num('Hur många rutor ligger som mest i kön samtidigt?',
            [step('Kön efter varje uttag', tab(['Tas ut', 'Kön efter uttaget'], queue_rows(r))),
             step('Den längsta kön', 'Kön är som längst 3 rutor, till exempel A4, B3 och C2 efter att C1 har tagits ut.')], 3,
            'Skriv upp kön efter varje uttag och räkna rutorna.', 2)
    c = val('Vilken ruta tas ut direkt före målet?',
            [step('De sista uttagen', 'Efter C2 tas C3 ut, och C3 lägger in målet C4.')],
            [alt('C3', True, 'C3 lägger in målet och tas ut direkt före det.'), alt('B3', False, 'B3 tas ut som sjunde ruta.'),
             alt('C2', False, 'C2 tas ut som åttonde ruta, före C3.'), alt('A4', False, 'A4 tas ut som sjätte ruta.')],
            'Vilken av målets grannar läggs in i kön?', 2)
    return kg_task('1.37', 'ko_sokning', 'Kön i en 3 × 4-labyrint', intro, [a, b, c],
                   'Nya rutor läggs längst bak i kön. En ruta som redan har upptäckts läggs inte in igen.', ['procedur'])


# ---------------------------------------------------------------- BFS och DFS i labyrinter

def bfs_task(id_, familj, rows, k, questions, ledtrad, tn=(2, 2, 2)):
    s, g = A.parse(rows)
    r = A.bfs(rows)
    order, path = names(r['order']), names(r['path'])
    dfs_order = names(A.dfs(rows)['order'])
    intro = maze(rows, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    parts = []
    for q, t in zip(questions, tn):
        if q == 'steg':
            parts.append(num('Hur många steg har vägen som BFS hittar?',
                             [step('Följ föregångarna från målet', pil(path) + '.'), step('Räkna stegen', f'{len(path)} rutor ger {len(path) - 1} steg.')],
                             len(path) - 1, 'Vägen har ett steg färre än antalet rutor på den.', t))
        elif q == 'k':
            qr = queue_rows(r)[:k]
            parts.append(val(f'Vilken ruta tas ut ur kön som {ORD[k]} ruta?',
                             [step('Kön efter varje uttag', tab(['Tas ut', 'Kön efter uttaget'], qr)),
                              step(f'{order[k - 1]} står först i kön', f'Efter att {order[k - 2]} har tagits ut står {order[k - 1]} först i kön och tas ut som {ORD[k]} ruta.')],
                             kth_alts(order, k, [dfs_order[k - 1]] + order[k + 1:], other='DFS'),
                             'Skriv upp kön efter varje uttag. Nya rutor läggs längst bak.', t))
        elif q == 'antal':
            parts.append(num('Hur många rutor tas ut ur kön, inklusive start och mål?',
                             [step('Hela uttagsordningen', lista(order) + '.')], len(order), 'Räkna alla rutor som tas ut fram till och med målet.', t))
        elif q.startswith('avst'):
            dd = A.dist_all(rows, s)
            n = int(q[4:])
            cells = sorted(A.cname(c) for c, v in dd.items() if v == n)
            parts.append(num(f'Hur många rutor ligger exakt {n} steg från start?',
                             [step('Räkna steg utåt från start', f'Rutorna {n} steg bort: {", ".join(cells)}.')], len(cells),
                             'Rutorna närmast start ligger 1 steg bort, deras nya grannar 2 steg bort, och så vidare.', t))
        else:
            raise ValueError(q)
    return kg_task(id_, 'bfs', familj, intro, parts, ledtrad, ['procedur'])


def dfs_task(id_, familj, rows, k, ledtrad, tn=(2, 2, 2, 3)):
    s, g = A.parse(rows)
    r = A.dfs(rows)
    order, path = names(r['order']), names(r['path'])
    bfs_order = names(A.bfs(rows)['order'])
    short = len(A.bfs(rows)['path']) - 1
    intro = maze(rows, s, g) + p('Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).')
    a = val(f'Vilken ruta besöks som {ORD[k]} ruta, räknat med start?',
            [step('DFS fortsätter alltid från den senast besökta rutan', 'Grannarna prövas i ordningen ↑ → ↓ ←, och DFS backar bara när det tar stopp.'),
             step(f'De {k} första besöken', pil(order[:k]) + '.')], kth_alts(order, k, [bfs_order[k - 1]] + order[k + 1:], verb='besöks', other='BFS'),
            'DFS fortsätter alltid från den senast besökta rutan.', tn[0])
    b = num('Hur många rutor besöker DFS, inklusive start och mål?',
            [step('Hela besöksordningen', lista(order) + '.')], len(order), 'Räkna även rutor i återvändsgränder.', tn[1])
    c = num('Hur många steg har vägen som DFS hittar?',
            [step('Rutor i återvändsgränder ingår inte', pil(path) + '.'), step('Räkna stegen', f'{len(path)} rutor ger {len(path) - 1} steg.')],
            len(path) - 1, 'Vägen består bara av rutorna från start till mål, utan återvändsgränder.', tn[2])
    same = len(path) - 1 == short
    d = val('Är vägen som DFS hittar en av de kortaste vägarna?',
            [step('Jämför med BFS', f'BFS hittar en kortaste väg med {short} steg. DFS-vägen har {len(path) - 1} steg.')],
            [alt('Ja', same, ('Ingen väg är kortare än ' + str(short) + ' steg.') if same else f'Det finns en väg med {short} steg.'),
             alt('Nej', not same, (f'DFS-vägen har {len(path) - 1} steg, men en kortaste väg har bara {short}.') if not same
                 else f'DFS-vägen har {short} steg, lika många som en kortaste väg.')],
            'Hur många steg har en kortaste väg?', tn[3])
    return kg_task(id_, 'dfs', familj, intro, [a, b, c, d], ledtrad, ['procedur', 'begrepp'])


TREE_142 = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'E': (250, 185),
                       'F': (330, 185), 'G': (120, 260), 'H': (200, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'), ('D', 'G'), ('D', 'H')],
                start='S', goals=['F'], width=380,
                title='Sökträd: S har barnen A och B. A har C och D, D har G och H, och B har E och målet F.')


def t142():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E', 'F'], 'D': ['G', 'H']}
    out = []

    def go(n):
        out.append(n)
        return n == 'F' or any(go(k) for k in kids.get(n, []))
    go('S')
    assert out == ['S', 'A', 'C', 'D', 'G', 'H', 'B', 'E', 'F']
    intro = search_tree(**TREE_142) + p('Trädet söks igenom med DFS (vänster gren först).')
    a = val('Vilken nod besöks som femte nod, räknat med start?',
            [step('DFS går ned i vänster gren', 'S → A → C. C har inga barn, så sökningen backar till A och tar D, sedan G.')],
            [alt('G', True, 'S, A, C, D och sedan G.'), alt('B', False, 'B besöks först när hela grenen under A är klar.'),
             alt('H', False, 'H besöks som sjätte nod, efter G.'), alt('D', False, 'D besöks som fjärde nod.')],
            'Gå så djupt som möjligt till vänster innan du backar.', 2)
    b = num('Hur många noder besöks, inklusive start och mål?',
            [step('Hela besöksordningen', lista(out) + '.')], 9, 'Hela vänstra grenen besöks innan B.', 2)
    return kg_task('1.42', 'dfs', 'DFS i ett sökträd', intro, [a, b], 'DFS följer en gren ända ned innan den backar.', ['procedur'])


# ---------------------------------------------------------------- prioritetsköer

def t235():
    q, out = [], []
    for op in [('G', 6), ('H', 2), ('K', 5), None, ('M', 1), None, None]:
        if op:
            q.append(op)
        else:
            q.sort(key=lambda x: x[1])
            out.append(q.pop(0)[0])
    assert out == ['H', 'M', 'K'] and q == [('G', 6)]
    intro = (p('Noder läggs in i och tas ut ur en prioritetskö. Talet inom parentes är nodens värde, och noden med lägst värde tas ut först.') +
             p('Lägg in G(6), H(2) och K(5) → ta ut en nod → lägg in M(1) → ta ut två noder.'))
    a = val('Vilken nod tas ut vid det tredje uttaget?',
            [step('Första uttaget', 'H har lägst värde, 2.'), step('Efter att M(1) lagts in', 'M tas ut vid det andra uttaget och K(5) vid det tredje.')],
            [alt('G', False, 'G har värdet 6 och ligger kvar sist.'), alt('H', False, 'H tas ut vid det första uttaget.'),
             alt('K', True, 'Efter H och M har K lägst värde.'), alt('M', False, 'M tas ut vid det andra uttaget.')],
            'Skriv upp kön före varje uttag.', 1)
    b = num('Vilket värde har den nod som ligger kvar i kön?',
            [step('Bara G ligger kvar', 'G har värdet 6, det högsta, och tas aldrig ut.')], 6, 'Vilken nod har aldrig lägst värde vid ett uttag?', 1)
    return kg_task('2.35', 'prioritetsko', 'Tredje uttaget ur prioritetskön', intro, [a, b], 'Vid varje uttag tas noden med lägst värde.', ['procedur'], 1)


def t236():
    data = {'P': (4, 7), 'Q': (6, 3), 'R': (2, 9), 'S': (5, 6)}
    f = {k: g + h for k, (g, h) in data.items()}
    assert f == {'P': 11, 'Q': 9, 'R': 11, 'S': 11}
    intro = (p('Under en A*-sökning ligger rutorna i tabellen i öppna listan.') + tab(['Ruta', 'g', 'h'], [[k, str(g), str(h)] for k, (g, h) in data.items()]))
    a = val('Vilken ruta tar A* ut härnäst?',
            [step('f = g + h', 'P: 11, Q: 9, R: 11, S: 11.'), step('Lägst f', 'Q har f = 9.')],
            [alt('P', False, 'P har f = 4 + 7 = 11.'), alt('Q', True, 'Q har lägst f = 6 + 3 = 9.'),
             alt('R', False, 'R har lägst g, men f = 2 + 9 = 11.'), alt('S', False, 'S har f = 5 + 6 = 11.')],
            'Räkna ut f för varje ruta.', 1)
    b = num('Vilket f-värde har den rutan?', [step('f = g + h', 'Q: 6 + 3 = 9.')], 9, 'Lägg ihop g och h.', 1)
    return kg_task('2.36', 'prioritetsko', 'Lägst f i öppna listan', intro, [a, b], 'A* tar alltid ut rutan med lägst f = g + h.', ['procedur'], 1)


def t237():
    data = {'B': (3, 5), 'D': (4, 4), 'F': (6, 2), 'H': (2, 7)}
    f = {k: g + h for k, (g, h) in data.items()}
    assert f == {'B': 8, 'D': 8, 'F': 8, 'H': 9}
    intro = (p('Under en A*-sökning ligger noderna i tabellen i prioritetskön. Vid lika f väljs lägst h.') +
             tab(['Nod', 'g', 'h'], [[k, str(g), str(h)] for k, (g, h) in data.items()]))
    a = num('Hur många av noderna har det lägsta f-värdet?',
            [step('f = g + h', 'B: 8, D: 8, F: 8, H: 9.'), step('Lägst f är 8', 'B, D och F har f = 8.')], 3, 'Räkna ut f för varje nod.', 2)
    b = val('Vilken nod tas ut först?',
            [step('Lika f avgörs av lägst h', 'B har h = 5, D h = 4 och F h = 2.')],
            [alt('B', False, 'B har f = 8 men högst h av de tre, 5.'), alt('D', False, 'D har f = 8 och h = 4.'),
             alt('F', True, 'F har lägst h = 2 bland noderna med f = 8.'), alt('H', False, 'H har lägst g men f = 9.')],
            'Jämför h för noderna med lägst f.', 2)
    return kg_task('2.37', 'prioritetsko', 'Lika f och lägst h', intro, [a, b], 'Jämför först f. Om flera har samma f avgör h.', ['procedur'])


# ---------------------------------------------------------------- g, h och f

def ghf_task(id_, familj, rows, mark, ledtrad, terrain='', variant=''):
    s, g = A.parse(rows)
    if terrain:
        tmp = [r[:mark[1]] + 'G' + r[mark[1] + 1:] if i == mark[0] else r.replace('G', '.') for i, r in enumerate(rows)]
        gv = A.ucs_grid(tmp)[0]
    else:
        gv = A.dist_all(rows, s)[mark]
    hv = A.manhattan(mark, g)
    intro = (maze(rows, s, g, {mark: 'P'}, extra_legend=[('#fff3b0', 'Markerad ruta')]) + p(B.ASTAR_GH) + (p(terrain) if terrain else ''))
    mn, gn = A.cname(mark), A.cname(g)
    if terrain:
        vp = names(A.ucs_grid(tmp)[1])
    else:
        vp = names(A.bfs(rows, goal=mark)['path'])
    a = num('Bestäm g för P.', [step('g följer gångarna från start', f'Den billigaste vägen till P ({mn}) är {pil(vp)}. Den kostar {gv}.')], gv,
            'Räkna kostnaden längs gångarna, inte rakt genom väggar.', 2)
    b = num('Bestäm h för P.', [step('h = radskillnad + kolumnskillnad', f'P ligger i {mn} och målet i {gn}: '
                                     f'{abs(mark[0] - g[0])} + {abs(mark[1] - g[1])} = {hv}.')], hv, 'Räkna rader och kolumner till målet, utan väggar.', 1)
    c = num('Bestäm f för P.', [step('f = g + h', f'f = {gv} + {hv} = {gv + hv}.')], gv + hv, 'Lägg ihop g och h.', 1)
    if variant == 'gap':
        rest = A.dist_all(rows, g)[mark]
        c = num('Hur många steg längre är den verkliga vägen från P till målet än h?',
                [step('Den verkliga vägen från P till målet', f'Längs gångarna är det {rest} steg från P till målet.'),
                 step('Jämför med h', f'{rest} − {hv} = {rest - hv}. h räknar inte med väggarna och blir därför för litet.')],
                rest - hv, 'Räkna stegen från P till målet längs gångarna.', 3)
    return kg_task(id_, 'astar_varden', familj, intro, [a, b, c], ledtrad, ['procedur'])


# ---------------------------------------------------------------- A*-sökning

def astar_task(id_, familj, rows, k, ledtrad):
    s, g = A.parse(rows)
    r = A.astar(rows)
    order = names(r['order'])
    bfs_order = names(A.bfs(rows)['order'])
    rowsT = [[A.cname(c), str(r['g'][c]), str(A.manhattan(c, g)), str(r['g'][c] + A.manhattan(c, g))] for c in r['order']]
    intro = maze(rows, s, g) + p(ASTAR)
    a = val(f'Vilken ruta tas ut ur öppna listan som {ORD[k]} ruta?',
            [step('Uttag med g, h och f', tab(['Tas ut', 'g', 'h', 'f'], rowsT[:k + 1]))], kth_alts(order, k, [bfs_order[k - 1]] + order[k + 1:], other='BFS'),
            'Räkna f = g + h för grannarna till varje uttagen ruta.', 3)
    b = num('Hur många rutor tas ut ur öppna listan, inklusive start och mål?',
            [step('Hela uttagsordningen', lista(order) + '.')], len(order), 'Fortsätt tills målet tas ut.', 3)
    cost = r['g'][g]
    c = num('Vad kostar vägen som A* returnerar?',
            [step('Vägen', pil(names(r['path'])) + '.'), step('Kostnaden', f'Alla steg kostar 1, så kostnaden är {cost}.')], cost,
            'Kostnaden är g för målet.', 2)
    return kg_task(id_, 'astar_sokning', familj, intro, [a, b, c], ledtrad, ['procedur'])


M242 = ['.....G', '3.3...', '3.3...', 'S.....']


def t242():
    s, g = A.parse(M242)
    gr, ast = A.greedy(M242), A.astar(M242)
    assert gr['cost'] > A.path_cost(M242, ast['path'])
    intro = (maze(M242, s, g) + p('Labyrinten söks igenom med girig bäst först och med A* (h = Manhattanavstånd). '
                                  'Att gå in i en lerruta kostar 3 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0. '
                                  'Vid lika värde väljs den ruta som kommer först i bokstavsordning.'))
    a = num('Vad kostar vägen som girig bäst först hittar?',
            [step('Girig bäst först jämför bara h', pil(names(gr['path'])) + '.'),
             step('Summera kostnaderna', ' + '.join(str(A.cost(M242, c)) for c in gr['path'][1:]) + f' = {gr["cost"]}.')], gr['cost'],
            'Följ lägst h från start och summera kostnaderna.', 3)
    ac = A.path_cost(M242, ast['path'])
    b = num('Vad kostar vägen som A* hittar?',
            [step('A* jämför f = g + h', pil(names(ast['path'])) + '.'), step('Bara vita rutor', f'{len(ast["path"]) - 1} steg som kostar 1 var: {ac}.')], ac,
            'A* räknar med vad leran kostar.', 3)
    return kg_task('2.42', 'astar_sokning', 'Girig bäst först och A* i lera', intro, [a, b],
                   'Girig bäst först ser bara h. A* räknar också med kostnaden hittills.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- viktade vägar

M244 = ['S4..', '.4.3', '...G']


def t244():
    s, g = A.parse(M244)
    c, path = A.ucs_grid(M244)
    given = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
    gc = A.path_cost(M244, given)
    assert gc == 4 + 1 + 1 + 3 + 1 and c == 5
    intro = (maze(M244, s, g) + p('Att gå in i en isruta kostar 4, en lerruta 3 och en vit ruta eller målet 1. Start kostar 0.'))
    a = num('Vad kostar vägen A1 → A2 → A3 → A4 → B4 → C4?',
            [step('Kostnad för varje ruta', 'A2 (is) 4, A3 1, A4 1, B4 (lera) 3 och målet 1.'), step('Summera', f'4 + 1 + 1 + 3 + 1 = {gc}.')], gc,
            'Start kostar 0. Räkna alla rutor du går in i.', 1)
    b = num('Vad kostar den billigaste vägen från start till mål?',
            [step('Gå ned och sedan åt höger', pil(names(path)) + '.'), step('Bara vita rutor', f'{len(path) - 1} steg som kostar 1 var: {c}.')], c,
            'Finns det en väg utan is och lera?', 2)
    return kg_task('2.44', 'viktade_vagar', 'Is och lera på vägen', intro, [a, b], 'Kostnaden för en väg är summan av kostnaderna för rutorna du går in i.', ['procedur'], 1)


G245 = dict(nodes={'S': (50, 130), 'A': (170, 45), 'B': (170, 215), 'C': (310, 130), 'M': (440, 130)},
            edges=[('S', 'A', 3), ('S', 'B', 1), ('A', 'C', 2), ('B', 'C', 6), ('B', 'A', 1), ('C', 'M', 2), ('A', 'M', 8)])


def t245():
    r = A.ucs_graph(G245['edges'], 'S', 'M')
    assert r['cost'] == 6 and r['path'] == ['S', 'B', 'A', 'C', 'M']
    svg = weighted_graph(G245['nodes'], G245['edges'], 'S', 'M', 'Graf med noderna S, A, B, C och M. Talet vid varje kant är kostnaden.', 490)
    intro = svg + p('Grafen visar vägar mellan platser. Talet vid varje kant är kostnaden att gå längs den, åt valfritt håll.')
    a = num('Vad kostar den billigaste vägen från start till mål?',
            [step('Billigast till A går via B', 'S → B → A kostar 1 + 1 = 2, billigare än kanten S–A som kostar 3.'),
             step('Vidare via C', 'S → B → A → C → M kostar 1 + 1 + 2 + 2 = 6.')], 6, 'Hitta först det billigaste sättet att komma till A.', 2)
    b = num('Hur många kanter har den billigaste vägen?',
            [step('Räkna kanterna', 'S → B → A → C → M har 4 kanter.')], 4, 'Räkna pilarna i vägen.', 2)
    return kg_task('2.45', 'viktade_vagar', 'Billigaste vägen med en omväg', intro, [a, b],
                   'En väg med fler kanter kan vara billigare än en direkt kant.', ['procedur', 'begrepp'])


G246 = dict(nodes={'S': (50, 150), 'A': (170, 65), 'B': (170, 235), 'C': (320, 65), 'D': (320, 235), 'M': (440, 150)},
            edges=[('S', 'A', 2), ('S', 'B', 3), ('A', 'C', 3), ('B', 'D', 2), ('C', 'M', 2), ('D', 'M', 4), ('A', 'B', 1)],
            h={'S': 6, 'A': 4, 'B': 5, 'C': 2, 'D': 3, 'M': 0})


def t246():
    E, h = G246['edges'], G246['h']
    for x, y, w in E:
        assert abs(h[x] - h[y]) <= w
    r = A.astar_graph(E, h, 'S', 'M')
    order = [x[0] for x in r['order']]
    assert order == ['S', 'A', 'C', 'M'] and r['cost'] == 7
    # Lägst f ska vara entydigt vid varje uttag, eftersom uppgiften inte anger någon regel för lika värden.
    adj = {}
    for x, y, w in E:
        adj.setdefault(x, []).append((y, w))
        adj.setdefault(y, []).append((x, w))
    g, openl, closed = {'S': 0}, {'S'}, set()
    while openl:
        fmin = min(g[n] + h[n] for n in openl)
        best = [n for n in openl if g[n] + h[n] == fmin]
        assert len(best) == 1, best
        n = best[0]
        openl.discard(n)
        closed.add(n)
        if n == 'M':
            break
        for v, w in adj[n]:
            if v not in closed and g[n] + w < g.get(v, 99):
                g[v] = g[n] + w
                openl.add(v)
    svg = weighted_graph(G246['nodes'], E, 'S', 'M', 'Graf med noderna S, A, B, C, D och M. Talet vid varje kant är kostnaden, och h står vid varje nod.', 490, h=h)
    intro = svg + p('Grafen söks igenom med A*. Talet vid varje kant är kostnaden att gå längs den, åt valfritt håll. '
                    'Värdet h vid varje nod är en uppskattning av kostnaden kvar till målet M.')
    rows = [[n, str(g), str(hh), str(f)] for n, g, hh, f in r['order']]
    a = val('Vilken nod tar A* ut efter S?',
            [step('Grannarna till S', 'A: f = 2 + 4 = 6. B: f = 3 + 5 = 8.')],
            [alt('A', True, 'A har lägst f = 6.'), alt('B', False, 'B har f = 3 + 5 = 8.'),
             alt('C', False, 'C har inte lagts in i kön ännu.'), alt('M', False, 'Målet har inte lagts in i kön ännu.')],
            'Räkna f = g + h för grannarna till S.', 2)
    b = num('Hur många noder tar A* ut, inklusive start och mål?',
            [step('Uttag med g, h och f', tab(['Tas ut', 'g', 'h', 'f'], rows)), step('B och D tas aldrig ut', 'Deras f-värden är högre än målets 7.')], 4,
            'Fortsätt tills målet tas ut.', 3)
    c = num('Vad kostar vägen som A* returnerar?', [step('Vägen', 'S → A → C → M: 2 + 3 + 2 = 7.')], 7, 'Kostnaden är g för målet.', 2)
    return kg_task('2.46', 'viktade_vagar', 'A* i en graf, rättas direkt', intro, [a, b, c], 'Ta alltid ut noden med lägst f = g + h.', ['procedur'])


# ---------------------------------------------------------------- minimax och alfa–beta

def mm_kg(id_, values, root_max, node_q, ledtrad, tn=(1, 2, 2)):
    r = T.build(values, root_max)
    info = {}

    def mmv(n):
        if 'leaf' in n:
            return n['leaf']
        vals = [mmv(k) for k in n['kids']]
        v = max(vals) if n['max'] else min(vals)
        info[n['name']] = (n['max'], vals, v)
        return v
    v = mmv(r)
    line = lambda nm: f'{nm} = {"max" if info[nm][0] else "min"}({", ".join(T.fmt(x) for x in info[nm][1])}) = {T.fmt(info[nm][2])}.'  # noqa: E731
    rot = 'MAX' if root_max else 'MIN'
    intro = game_tree(T.to_figure(r), root_max, f'Spelträd med {rot} i roten R och {len(T.leaves(r))} löv.', leaf_names=False) + p('Spelträdet söks igenom med minimax.')
    sub = [n for n in info if n != 'R']
    sub_lines = [line(n) for n in sub]
    a = num(f'Vilket värde får {node_q}?', [step(f'{node_q} är en {"MAX" if info[node_q][0] else "MIN"}-nod', line(node_q))],
            info[node_q][2], f'Är {node_q} en MAX- eller en MIN-nod?', tn[0])
    b = num('Vilket värde får roten?', [step('Från löven till roten', *sub_lines, line('R'))], v, 'Arbeta från löven och uppåt.', tn[1])
    kids = [k['name'] for k in r['kids']]
    best = [k for k in kids if info[k][2] == v]
    assert len(best) == 1, id_
    c = val('Vilket drag väljer roten?',
            [step(f'Roten väljer det {"största" if root_max else "minsta"} värdet', ', '.join(f'{k} ger {T.fmt(info[k][2])}' for k in kids) + '.')],
            [alt(f'Draget till {k}', k == best[0], f'{k} har värdet {T.fmt(info[k][2])}' + (f', det {"största" if root_max else "minsta"} av rotens barn.' if k == best[0] else
                 f', men roten väljer det {"största" if root_max else "minsta"} värdet, {T.fmt(v)}.')) for k in kids],
            'Vilket av rotens barn ger rotens värde?', tn[2])
    return kg_task(id_, 'minimax', 'Minimax med direkt rättning', intro, [a, b, c], ledtrad, ['procedur'])


def ab_kg(id_, values, root_max, ledtrad, tn=(2, 3, 3), third='leaf'):
    r = T.build(values, root_max)
    v, ev, cuts, notes = T.alphabeta(r)
    pr = T.pruned_leaves(cuts)
    n = len(T.leaves(r))
    rot = 'MAX' if root_max else 'MIN'
    intro = game_tree(T.to_figure(r), root_max, f'Spelträd med {rot} i roten R och {n} löv, L1–L{n}.') + B.p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).')
    a = num('Vilket värde får roten?', [step('Gren för gren', *[x for k in r['kids'] for x in T.subtree_lines(k, notes)], T.node_line('R', notes['R']))],
            v, 'Bestäm först rotens första barn helt.', tn[0])
    b = num('Hur många löv beskärs?',
            [step(f'I {c[0]} efter {c[1]}: α = {T.fmt(c[2])} ≥ β = {T.fmt(c[3])}', f'{T.cap(" och ".join(T.pruned_desc(c[4])))} beskärs.') for c in cuts] +
            [step('Räkna', f'{", ".join(pr)}: {len(pr)} löv.')], len(pr), 'Leta efter noder där α ≥ β innan alla barn är undersökta.', tn[1])
    first = cuts[0]
    if third == 'count':
        c = num('Hur många löv utvärderas?', [step('Löven som inte beskärs', f'{", ".join(ev)}: {len(ev)} av {n} löv.')], len(ev),
                'Utgå från antalet löv som beskärs.', tn[2])
        return kg_task(id_, 'alfa_beta', 'Alfa–beta med direkt rättning', intro, [a, b, c], ledtrad, ['procedur', 'begrepp'])
    if third == 'node':
        inner = [k['name'] for k in r['kids']]
        c = val('I vilken nod sker den första beskärningen?',
                [step('Följ sökningen från vänster', f'Första gången α ≥ β blir sant är i {first[0]}, efter {first[1]}: α = {T.fmt(first[2])} och β = {T.fmt(first[3])}.')],
                [alt(x, x == first[0], (f'Efter {first[1]} är α ≥ β i {x}.' if x == first[0] else
                                        f'{x} undersöks {"helt" if notes[x]["kind"] == "exakt" else "men avbryts senare"}.')) for x in inner],
                'Gå igenom löven från vänster och uppdatera α och β efter varje löv.', tn[2])
        return kg_task(id_, 'alfa_beta', 'Alfa–beta med direkt rättning', intro, [a, b, c], ledtrad, ['procedur', 'begrepp'])
    leaf_opts = [pr[0], ev[-1], ev[0], [x for x in T.leaves(r) if x not in pr and x not in (ev[-1], ev[0])][0]]
    c = val('Vilket av löven behöver aldrig utvärderas?',
            [step(f'Första beskärningen sker i {first[0]}', f'Efter {first[1]} är α = {T.fmt(first[2])} och β = {T.fmt(first[3])}. {T.cap(" och ".join(T.pruned_desc(first[4])))} beskärs.')],
            [alt(x, x == pr[0], (f'{x} beskärs i {first[0]} och behöver aldrig utvärderas.' if x == pr[0] else f'{x} utvärderas av alfa–beta.')) for x in sorted(set(leaf_opts), key=lambda s: int(s[1:]))],
            'Vilken nod avbryts först?', tn[2])
    return kg_task(id_, 'alfa_beta', 'Alfa–beta med direkt rättning', intro, [a, b, c], ledtrad, ['procedur', 'begrepp'])


# ---------------------------------------------------------------- lista över uppgifter

M138 = ['S..#.', '.#...', '...#.', '.#..G']
M139 = ['.#...', 'S..#.', '.#...', '...#G']
M140 = ['S.#.', '...#', '#...', '..#G']
M141 = ['S..#', '.#..', '.#.#', '...G']
M143 = ['S.#..', '.....', '#.##.', '...#G']
M238 = ['S...#', '.##..', '...#.', '#...G']
M239 = ['S3..', '.#3.', '..#G']
M240 = ['S....', '.###.', '.#G..', '.###.', '.....']
M241 = ['S..#', '.#..', '...G']
M243 = ['...G', '.#.#', 'S...']


def build_all():
    out = [t132(), t133(), t134(), t135(), t136(), t137(),
           bfs_task('1.38', 'BFS med direkt rättning', M138, 5, ['steg', 'k', 'antal'], 'BFS tar ut rutorna i ordning efter avstånd från start.'),
           bfs_task('1.39', 'Avstånd i en labyrint', M139, 4, ['avst2', 'steg', 'k'], 'Räkna steg utåt från start, en nivå i taget.', (1, 2, 2)),
           bfs_task('1.40', 'Kön i en liten labyrint', M140, 6, ['k', 'antal', 'avst3'], 'Skriv upp kön efter varje uttag.', (2, 2, 2)),
           dfs_task('1.41', 'DFS med direkt rättning', M141, 5, 'Gå så långt det går i första tillåtna riktningen. Backa när det tar stopp.'),
           t142(),
           dfs_task('1.43', 'DFS och återvändsgränder', M143, 6, 'DFS backar till den senaste rutan som har en obesökt granne.'),
           t235(), t236(), t237(),
           ghf_task('2.38', 'g, h och f för en ruta', M238, (0, 3), 'g följer gångarna, h räknas rakt.'),
           ghf_task('2.39', 'g, h och f med lera', M239, (0, 3), 'Lerrutor kostar mer än vanliga rutor.',
                    terrain='Att gå in i en lerruta kostar 3 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0.'),
           ghf_task('2.40', 'g och h på var sin sida om väggen', M240, (2, 0), 'P ligger nära målet, men vägen dit kan vara lång.', variant='gap'),
           astar_task('2.41', 'A* med direkt rättning', M241, 4, 'Räkna g, h och f för varje ny granne.'),
           t242(),
           astar_task('2.43', 'A* från ett hörn', M243, 5, 'Vid lika f: lägst h och sedan bokstavsordning.'),
           t244(), t245(), t246(),
           mm_kg('3.31', [[7, 3], [5, 6], [2, 8]], True, 'B', 'MIN-noderna väljer det minsta värdet, roten det största.'),
           mm_kg('3.32', [[[4, 1], [6, 2]], [[3, 9], [5, 0]]], False, 'D', 'Tre nivåer: arbeta nedifrån och växla mellan max och min.', (2, 2, 2)),
           mm_kg('3.33', [[[2, -3], [-1, 4], 1], [[5, -2], [0, 3]]], True, 'A', 'Var noga med minustecknen.', (2, 3, 3)),
           ab_kg('3.34', [[5, 8], [3, 9], [6, 4]], True, 'När ett MIN-barn får ett löv som är högst α kan resten av barnet hoppas över.', (1, 2, 2)),
           ab_kg('3.35', [[[6, 1], [7, 2]], [[4, 4], [8, 5]]], True, 'Gränserna förs ned genom trädet.', third='count'),
           ab_kg('3.36', [[2, 6, 4], [7, 1], [8, 3, 5]], False, 'Roten är en MIN-nod. Jämför med β i roten.', (2, 3, 3), third='node')]
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
