"""AI-banken 2026-11-11, fjärde omgången: 20 nya uppgifter, två i varje område.

Informerad sökning tränas bara med girig bäst först och A* (användarbeslut
2026-11-11: UCS ingår inte). Kör efter bygg-ai-pafyllnad-2026-11-11.py:

    python tools/bygg-ai-pafyllnad-2026-11-11.py
    python tools/bygg-ai-pafyllnad2-2026-11-11.py

Skriptet är idempotent. Svaren räknas fram med tools/ai_sokalgoritmer.py och
kontrolleras oberoende i tools/ai-pafyllnad2-2026-11-11.test.js.
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
from ai_figurer import tab, step, maze, search_tree, weighted_graph, game_tree  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402

p, part, alt, task, names, lista, pil = B.p, B.part, B.alt, B.task, B.names, B.lista, B.pil
ASTAR_TIE = B.ASTAR_TIE
BANK = 'uppgifterai.js'


# ---------------------------------------------------------------- kö och stack

def t120():
    intro = p('Avgör om situationen fungerar som en FIFO-kö eller som en stack.')

    def fs(right, fifo_c, stack_c):
        return [alt('FIFO-kö', right == 'FIFO-kö', fifo_c), alt('Stack', right == 'Stack', stack_c)]
    a = part(p('Kunderna i kön till kassan i en affär. Välj ett alternativ.'),
             [step('Den som kom först betalar först', 'Nya kunder ställer sig sist i kön. Det är först in, först ut.')],
             'FIFO-kö.', 'Vem får betala först, den som kom först eller den som kom sist?', 1,
             fs('FIFO-kö', 'Den kund som har väntat längst står först och betalar först.', 'I en stack skulle den som kom sist betala först.'))
    b = part(p('Ångra-knappen i ett ritprogram ångrar alltid den senaste ändringen först. Välj ett alternativ.'),
             [step('Den senaste ändringen ångras först', 'Varje ny ändring läggs överst. Ångra tar bort den översta. Det är sist in, först ut.')],
             'Stack.', 'Vilken ändring ångras först, den äldsta eller den senaste?', 1,
             fs('Stack', 'En FIFO-kö skulle ångra den äldsta ändringen först.', 'Den senaste ändringen ligger överst och ångras först.'))
    c = part(p('Dokument som skickas till en skrivare skrivs ut i den ordning de skickades. Välj ett alternativ.'),
             [step('Det först skickade dokumentet skrivs ut först', 'Det är först in, först ut.')],
             'FIFO-kö.', 'Vilket dokument skrivs ut först?', 1,
             fs('FIFO-kö', 'Dokumenten skrivs ut i samma ordning som de skickades.', 'En stack skulle skriva ut det senast skickade dokumentet först.'))
    d = part(p('En hög med tallrikar där man alltid tar den översta. Välj ett alternativ.'),
             [step('Den översta tallriken lades dit sist', 'Den tas först. Det är sist in, först ut.')],
             'Stack.', 'Vilken tallrik lades i högen senast?', 1,
             fs('Stack', 'Den översta tallriken lades dit sist och tas först.', 'Med en FIFO-kö skulle man ta den tallrik som lades i högen först, längst ner.'))
    return task('1.20', 'ko_stack', 'Kö eller stack i vardagen', intro, [a, b, c, d],
                'Fråga dig om det som kom först eller det som kom senast tas först.', ['begrepp'], 1)


def t121():
    ops = ['+P', '+Q', '-', '+R', '+S', '-', '+T']
    fifo, stack, rows, out_f, out_s = [], [], [], [], []
    for op in ops:
        if op[0] == '+':
            fifo.append(op[1])
            stack.append(op[1])
            rows.append([f'Lägg in {op[1]}', ' '.join(fifo), ' '.join(stack)])
        else:
            out_f.append(fifo.pop(0))
            out_s.append(stack.pop())
            rows.append([f'Ta ut (kön: {out_f[-1]}, stacken: {out_s[-1]})', ' '.join(fifo), ' '.join(stack)])
    assert out_f == ['P', 'Q'] and out_s == ['Q', 'S'] and fifo == ['R', 'S', 'T'] and stack == ['P', 'R', 'T']
    intro = (p('Samma steg görs en gång med en FIFO-kö och en gång med en stack:') +
             p('lägg in P och Q → ta ut en nod → lägg in R och S → ta ut en nod → lägg in T.') +
             p('I tabellen står den nod som tas ut först längst till vänster i kön, och den översta noden längst till höger i stacken.'))
    blank = [[x, '…', '…'] for x in ['Lägg in P', 'Lägg in Q', 'Ta ut', 'Lägg in R', 'Lägg in S', 'Ta ut', 'Lägg in T']]
    a = part(p('Fyll i tabellen.') + tab(['Steg', 'FIFO-kö', 'Stack'], blank),
             [step('Kön tar ut från vänster, stacken från höger', 'I kön tas den äldsta noden ut. I stacken tas den senast inlagda ut.'),
              step('Innehållet efter varje steg', tab(['Steg', 'FIFO-kö', 'Stack'], rows))],
             'Kön slutar som R S T och stacken som P R T.', 'Lägg alltid in nya noder längst till höger. Var tar respektive struktur ut?', 2)
    b = part(p('Vilka noder har tagits ut med FIFO-kön, och vilka med stacken?'),
             [step('FIFO-kön', 'Första uttaget tar P, andra tar Q.'),
              step('Stacken', 'Första uttaget tar Q, som lades in sist. Andra uttaget tar S.')],
             'Kön: P och Q. Stacken: Q och S.', 'Vilken nod står först i kön och vilken ligger överst i stacken vid varje uttag?', 2)
    return task('1.21', 'ko_stack', 'Kö och stack sida vid sida', intro, [a, b],
                'Gör stegen två gånger: en gång där den äldsta noden tas ut och en gång där den senaste tas ut.', ['procedur'])


# ---------------------------------------------------------------- kön under sökningen

TREE_122 = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'E': (290, 185),
                       'F': (60, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('C', 'F')],
                start='S', goals=['F'], width=360,
                title='Sökträd: S har barnen A och B, A har C och D, B har E och C har F. Start S är grön och målet F är rött.')


def t122():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E'], 'C': ['F']}
    qq, rows = ['S'], [['–', 'S']]
    while qq:
        n = qq.pop(0)
        if n != 'F':
            qq += kids.get(n, [])
        rows.append([n, ' '.join(qq) or 'tom'])
        if n == 'F':
            break
    assert [r[0] for r in rows[1:]] == ['S', 'A', 'B', 'C', 'D', 'E', 'F']
    elev = [['–', 'S'], ['S', 'A B'], ['A', 'C D B'], ['C', 'D B F'], ['D', 'B F'], ['B', 'F E'], ['F', 'E']]
    intro = (search_tree(**TREE_122) +
             p('Trädet söks igenom med BFS (vänster gren först). Ali har skrivit kön i en tabell, med nästa nod som tas ut längst till vänster. Ali har gjort ett fel.') +
             tab(['Tas ut', 'Kön efter uttaget'], elev))
    a = part(p('Efter vilket uttag blir kön fel första gången? Välj ett alternativ.'),
             [step('Kontrollera raden där A tas ut', 'Kön var A B. När A tas ut ligger B kvar först, och A:s barn C och D ska läggas in längst bak.'),
              step('Ali lade barnen först', 'Kön C D B betyder att barnen hamnade före B. Så fungerar en stack, inte en FIFO-kö.')],
             'Efter att A har tagits ut.', 'Var ska nya noder hamna i en FIFO-kö?', 2,
             [alt('S', False, 'Efter S är kön A B, vilket stämmer.'),
              alt('A', True, 'C och D ska läggas in efter B, så kön ska vara B C D.'),
              alt('C', False, 'Raden är fel, men den bygger på felet i raden ovanför.'),
              alt('B', False, 'Felet uppstod tidigare.')])
    b = part(p('Gör om tabellen rätt från och med uttaget av A, tills målet tas ut.'),
             [step('Barnen läggs längst bak i kön', tab(['Tas ut', 'Kön efter uttaget'], rows[2:]))],
             'Uttagen blir A, B, C, D, E, F.', 'Börja med kön A B och lägg varje uttagen nods barn längst bak.', 2)
    c = part(p('Med Alis tabell tas F ut som femte nod efter S. Som vilken nod efter S tas F ut med rätt BFS?'),
             [step('Räkna uttagen efter S', 'Med rätt BFS tas A, B, C, D, E och F ut. F är den sjätte noden efter S.'),
              step('Varför senare', 'F ligger på nivå 3. BFS tar ut alla noder på nivå 1 och 2 innan F.')],
             'Som sjätte nod.', 'På vilken nivå ligger F?', 3)
    return task('1.22', 'ko_sokning', 'Hitta felet i kötabellen', intro, [a, b, c],
                'I BFS hamnar nya noder alltid längst bak i kön.', ['procedur', 'begrepp'])


G123 = dict(nodes={'S': (50, 130), 'A': (170, 55), 'B': (170, 205), 'C': (300, 130), 'G': (420, 130)},
            edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'G')])


def t123():
    adj = {'S': ['A', 'B'], 'A': ['C', 'S'], 'B': ['C', 'S'], 'C': ['A', 'B', 'G'], 'G': ['C']}
    qq, seen, rows, adds = ['S'], {'S'}, [['–', 'S']], {}
    while qq:
        n = qq.pop(0)
        if n != 'G':
            for v in sorted(adj[n]):
                if v not in seen:
                    seen.add(v)
                    qq.append(v)
                    adds[v] = adds.get(v, 0) + 1
        rows.append([n, ' '.join(qq) or 'tom'])
        if n == 'G':
            break
    assert [r[0] for r in rows[1:]] == ['S', 'A', 'B', 'C', 'G'] and adds['C'] == 1
    svg = search_tree(G123['nodes'], G123['edges'], 'S', ['G'], 'Graf: S är kopplad till A och B, både A och B är kopplade till C, och C till G.', 470)
    intro = (svg + p('Grafen söks igenom med BFS. En nods grannar läggs in i bokstavsordning. '
                     'En nod som redan har lagts in i kön läggs inte in igen. I tabellen står nästa nod som tas ut längst till vänster.'))
    a = part(p('Fyll i tabellen tills målet tas ut.') + tab(['Tas ut', 'Kön efter uttaget'], [['–', 'S']] + [['…', '…']] * 5),
             [step('S lägger in A och B', 'Grannarna läggs in i bokstavsordning.'),
              step('A lägger in C, men B gör det inte', 'När B tas ut ligger C redan i kön. S har redan lagts in tidigare.'),
              step('Kön efter varje uttag', tab(['Tas ut', 'Kön efter uttaget'], rows))],
             'Noderna tas ut i ordningen S, A, B, C, G.', 'Hoppa över grannar som redan har lagts in i kön.', 2)
    b = part(p('Vilken nod lägger in C i kön? Välj ett alternativ.'),
             [step('A tas ut före B', 'A är först i kön efter S och upptäcker C. När B tas ut finns C redan i kön.')],
             'A.', 'Vilken av C:s grannar tas ut först?', 2,
             [alt('A', True, 'A tas ut före B och lägger in C.'),
              alt('B', False, 'När B tas ut ligger C redan i kön, så den läggs inte in igen.'),
              alt('Både A och B', False, 'C läggs bara in en gång. Annars skulle samma nod kunna tas ut flera gånger.'),
              alt('S', False, 'S är inte granne till C och kan inte lägga in den.')])
    c = part(p('Varför ska en nod som redan har lagts in i kön inte läggas in igen? Välj ett alternativ.'),
             [step('Grafen har en slinga', 'S, A, C och B bildar en slinga. Utan regeln läggs noder in flera gånger, och sökningen kan gå runt i slingan.')],
             'B.', 'Vad händer om du följer slingan S – A – C – B – S?', 2,
             [alt('Annars hittar BFS inte målet.', False, 'Målet hittas ändå här, men sökningen gör onödigt arbete.'),
              alt('Annars läggs samma nod in flera gånger, och sökningen kan gå runt i slingan.', True, 'Regeln gör att varje nod undersöks högst en gång.'),
              alt('Annars blir vägen längre.', False, 'BFS returnerar ändå en kortaste väg, men gör mer arbete.')])
    return task('1.23', 'ko_sokning', 'BFS i en graf med slinga', intro, [a, b, c],
                'Markera en nod som upptäckt när den läggs in i kön, så att den inte läggs in igen.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- BFS

M124 = ['S.#..', '..#.#', '.....', '#.##.', '...#G']


def t124():
    s, g = A.parse(M124)
    r = A.bfs(M124)
    order, path = names(r['order']), names(r['path'])
    assert order[:6] == ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'] and len(path) - 1 == 8 and len(order) == 18
    intro = B.maze(M124, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = part(p('Ange de sex första rutorna som tas ut ur kön.'),
             [step('A1 lägger in A2 och B1', 'Ordningen ↑ → ↓ ← gör att A2 (→) läggs in före B1 (↓).'),
              step('Nästa nivå', 'A2 lägger in B2. B1 lägger in C1. Sedan tas B2 ut och lägger in C2, och C1 tas ut.')],
             lista(order[:6]) + '.', 'Skriv upp kön efter varje uttag.', 2)
    b = part(p('Hur många steg har vägen som BFS returnerar?'),
             [step('BFS ger en kortaste väg', pil(path) + '.'),
              step('Räkna stegen', 'Vägen har 9 rutor och därför 8 steg.')],
             '8 steg.', 'Följ vägen från målet tillbaka till start.', 2)
    c = part(p('Hur många rutor tas ut ur kön, inklusive start och mål?'),
             [step('Ingen vit ruta ligger längre bort än målet', 'Målet ligger 8 steg från start. Alla andra vita rutor ligger närmare och tas ut före målet.'),
              step('Räkna de vita rutorna', 'Labyrinten har 18 rutor som inte är väggar.')],
             '18 rutor.', 'Finns det någon ruta som ligger längre från start än målet?', 2)
    return task('1.24', 'bfs', 'BFS i en 5 × 5-labyrint', intro, [a, b, c],
                'Nya rutor läggs längst bak i kön, och rutorna tas ut i den ordning de lades in.', ['procedur'])


M125 = ['..#..', '.....', '#.S.#', '..#..', 'G....']


def t125():
    s, g = A.parse(M125)
    r = A.bfs(M125)
    first = names(r['snaps'][0][1])
    assert first == ['B3', 'C4', 'C2'] and len(r['path']) - 1 == 4
    intro = B.maze(M125, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = part(p('Vilka rutor läggs in i kön när start tas ut? Skriv dem i den ordning de läggs in.'),
             [step('Pröva grannarna i ordningen ↑ → ↓ ←', 'Uppåt B3, åt höger C4, nedåt D3 är en vägg och åt vänster C2.')],
             'B3, C4, C2.', 'Gå igenom de fyra riktningarna i tur och ordning. Hoppa över väggar.', 1)
    b = part(p('Vilken ruta tas ut efter start? Välj ett alternativ.'),
             [step('Den först inlagda rutan tas ut först', 'B3 lades in först, eftersom ↑ prövas först.')],
             'B3.', 'Vilken ruta står först i kön?', 1,
             [alt('B3', True, 'B3 lades in först och står först i kön.'),
              alt('C2', False, 'C2 ligger närmast målet, men BFS bryr sig inte om var målet ligger.'),
              alt('C4', False, 'C4 lades in som andra ruta.'),
              alt('D3', False, 'D3 är en vägg och kan inte läggas in i kön.')])
    c = part(p('Hur många steg har den kortaste vägen till målet?'),
             [step('Gå mot målet E1', 'C3 → C2 → D2 → E2 → E1.'),
              step('Ingen kortare väg finns', 'Målet ligger 2 rader och 2 kolumner bort, så minst 4 steg behövs.')],
             '4 steg.', 'Hur många rader och kolumner ligger målet från start?', 1)
    return task('1.25', 'bfs', 'Start mitt i labyrinten', intro, [a, b, c],
                'Grannarna läggs in i ordningen ↑ → ↓ ←, och den ruta som lades in först tas ut först.', ['procedur'], 1)


# ---------------------------------------------------------------- DFS

TREE_126 = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'G': (290, 185),
                       'E': (30, 260), 'F': (90, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'G'), ('C', 'E'), ('C', 'F')],
                start='S', goals=['G'], width=360,
                title='Sökträd: S har barnen A och B, A har C och D, C har E och F, och B har målet G.')


def t126():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['G'], 'C': ['E', 'F']}
    dfs_o = []

    def go(n):
        dfs_o.append(n)
        if n == 'G':
            return True
        return any(go(k) for k in kids.get(n, []))
    go('S')
    qq, bfs_o = ['S'], []
    while qq:
        n = qq.pop(0)
        bfs_o.append(n)
        if n == 'G':
            break
        qq += kids.get(n, [])
    assert dfs_o == ['S', 'A', 'C', 'E', 'F', 'D', 'B', 'G'] and bfs_o == ['S', 'A', 'B', 'C', 'D', 'G']
    intro = search_tree(**TREE_126) + p('Trädet söks igenom med DFS och med BFS (vänster gren först).')
    a = part(p('Ange besöksordningen med DFS.'),
             [step('DFS går så djupt som möjligt till vänster', 'S → A → C → E. E har inga barn, så sökningen backar till C och tar F.'),
              step('Backa till A och sedan till S', 'Efter C tar DFS D, sedan B och till sist målet G.')],
             lista(dfs_o) + '.', 'Gå ned i vänster gren så långt det går innan du backar.', 2)
    b = part(p('Ange besöksordningen med BFS.'),
             [step('BFS tar en nivå i taget', 'Nivå 1: A och B. Nivå 2: C, D och G. Sökningen stoppar när G tas ut.')],
             lista(bfs_o) + '.', 'Ta alla noder på en nivå innan nästa nivå.', 2)
    c = part(p('Vilken sökning tar ut färst noder innan målet hittas i det här trädet? Välj ett alternativ.'),
             [step('Jämför antalen', 'DFS tar ut 8 noder och BFS 6 noder.'),
              step('Målet ligger grunt i höger gren', 'DFS går först igenom hela vänstra grenen, medan BFS hittar G redan på nivå 2.')],
             'BFS.', 'Var i trädet ligger målet?', 2,
             [alt('DFS', False, 'DFS går igenom hela vänstra grenen, 4 extra noder, innan den når B.'),
              alt('BFS', True, 'G ligger på nivå 2, så BFS hittar det efter 6 uttag. DFS behöver 8.'),
              alt('Lika många', False, 'DFS tar ut 8 noder och BFS 6.')])
    return task('1.26', 'dfs', 'DFS och BFS i samma träd', intro, [a, b, c],
                'DFS följer en gren ända ned innan den backar. BFS tar en nivå i taget.', ['procedur', 'begrepp'])


M127 = ['S.#', '..#', '#.G']


def t127():
    s, g = A.parse(M127)
    r = A.dfs(M127)
    assert names(r['order']) == ['A1', 'A2', 'B2', 'C2', 'C3'] and names(r['path']) == ['A1', 'A2', 'B2', 'C2', 'C3']
    intro = B.maze(M127, s, g) + p('Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).')
    a = part(p('Vilken ruta besöks som tredje ruta, räknat med start? Välj ett alternativ.'),
             [step('Följ första tillåtna riktning', 'Från A1 kommer → före ↓, så DFS går till A2. Från A2 är → en vägg, så nästa riktning ↓ leder till B2.')],
             'B2.', 'Pröva riktningarna i ordningen ↑ → ↓ ← från varje ny ruta.', 1,
             [alt('B1', False, 'B1 är granne till start, men DFS fortsätter från A2 i stället för att gå tillbaka.'),
              alt('B2', True, 'A1 → A2 → B2. DFS fortsätter alltid från den senaste rutan.'),
              alt('A3', False, 'A3 är en vägg och kan inte besökas.'),
              alt('C2', False, 'C2 besöks som fjärde ruta.')])
    b = part(p('Ange vägen DFS hittar till målet.'),
             [step('Fortsätt nedåt från B2', 'B2 → C2. Från C2 är ↑ redan besökt, och → leder till målet C3.')],
             pil(names(r['path'])) + '.', 'Fortsätt från B2 i ordningen ↑ → ↓ ←.', 1)
    return task('1.27', 'dfs', 'DFS i en liten labyrint', intro, [a, b],
                'DFS fortsätter hela tiden från den senast besökta rutan.', ['procedur'], 1)


# ---------------------------------------------------------------- prioritetsköer

def t223():
    ops = [('P', 3), ('Q', 5), ('M', 3), None, ('S', 1), ('K', 3), None, None, None]

    def run(alpha):
        q, out, t = [], [], 0
        for op in ops:
            if op:
                q.append((op[1], op[0] if alpha else t, op[0]))
                t += 1
            else:
                q.sort()
                out.append(q.pop(0)[2])
        return out
    assert run(False) == ['P', 'S', 'M', 'K'] and run(True)[0] == 'M'
    intro = (p('Noder läggs in i och tas ut ur en prioritetskö enligt följande. Talet inom parentes är nodens värde, och noden med lägst värde tas ut först. '
               'Vid lika värde tas den nod ut som lades in först.') +
             p('Lägg in P(3), Q(5) och M(3) → ta ut en nod → lägg in S(1) och K(3) → ta ut tre noder.'))
    rows = [['Lägg in P(3), Q(5), M(3)', 'P(3) Q(5) M(3)', '–'], ['Ta ut', 'Q(5) M(3)', 'P'], ['Lägg in S(1), K(3)', 'Q(5) M(3) S(1) K(3)', '–'],
            ['Ta ut', 'Q(5) M(3) K(3)', 'S'], ['Ta ut', 'Q(5) K(3)', 'M'], ['Ta ut', 'Q(5)', 'K']]
    a = part(p('I vilken ordning tas noderna ut?'),
             [step('Lägst värde först', 'P och M har båda värdet 3. P lades in först och tas ut först.'),
              step('Kön efter varje steg, i den ordning noderna lades in', tab(['Steg', 'I kön', 'Tas ut'], rows))],
             'P, S, M, K.', 'Skriv upp kön efter varje steg. Vid lika värde: vem lades in först?', 2)
    b = part(p('Vilken nod hade tagits ut först om lika värden i stället avgjordes av alfabetet?'),
             [step('Vid första uttaget ligger P(3), Q(5) och M(3) i kön', 'P och M har lägst värde. M kommer före P i alfabetet.')],
             'M.', 'Vilka noder har lägst värde vid första uttaget?', 2)
    return task('2.23', 'prioritetsko', 'Lika värden avgörs av ordningen', intro, [a, b],
                'Läs regeln för lika värden noga. Den kan skilja sig mellan olika uppgifter.', ['procedur'])


def t224():
    intro = p('Noderna A(3), B(1) och C(2) läggs in i den ordningen. Talet inom parentes är nodens värde. Sedan tas en nod ut.')

    def alts(right, why):
        txt = {'A': 'A lades in först. Det är den nod en FIFO-kö tar ut.', 'B': 'B har lägst värde. Det är den nod en prioritetskö tar ut.',
               'C': 'C lades in sist. Det är den nod en stack tar ut.'}
        return [alt(k, k == right, why if k == right else txt[k]) for k in 'ABC']
    a = part(p('Vilken nod tas ut om strukturen är en FIFO-kö? Välj ett alternativ.'),
             [step('FIFO: först in, först ut', 'A lades in först.')], 'A.', 'Vilken nod lades in först?', 1,
             alts('A', 'A lades in först, och en FIFO-kö tar ut den nod som legat längst.'))
    b = part(p('Vilken nod tas ut om strukturen är en stack? Välj ett alternativ.'),
             [step('LIFO: sist in, först ut', 'C lades in sist.')], 'C.', 'Vilken nod lades in sist?', 1,
             alts('C', 'C lades in sist och ligger överst i stacken.'))
    c = part(p('Vilken nod tas ut om strukturen är en prioritetskö där lägst värde tas ut först? Välj ett alternativ.'),
             [step('Lägst värde först', 'B har värdet 1, lägre än A(3) och C(2).')], 'B.', 'Titta bara på värdena.', 1,
             alts('B', 'B har lägst värde, 1.'))
    d = part(p('Vilken av strukturerna använder A* för att välja nästa nod? Välj ett alternativ.'),
             [step('A* väljer noden med lägst f', 'Därför behövs en prioritetskö sorterad efter f = g + h.')],
             'En prioritetskö.', 'Väljer A* efter när noden lades in eller efter ett värde?', 1,
             [alt('En FIFO-kö', False, 'En FIFO-kö används i BFS. A* väljer efter f-värdet, inte efter när noden lades in.'),
              alt('En stack', False, 'En stack kan användas i DFS.'),
              alt('En prioritetskö', True, 'A* tar alltid ut noden med lägst f, och det gör en prioritetskö.')])
    return task('2.24', 'prioritetsko', 'Tre strukturer, samma noder', intro, [a, b, c, d],
                'Kön, stacken och prioritetskön skiljer sig bara i vilken nod som tas ut.', ['begrepp'], 1)


# ---------------------------------------------------------------- g, h och f

M225 = ['S3..', '.3#.', '...G']
MARK225 = {(0, 2): 'P'}


def t225():
    s, g = A.parse(M225)
    P = (0, 2)
    gP = A.ucs_grid([r[:P[1]] + 'G' + r[P[1] + 1:] if i == P[0] else r.replace('G', '.') for i, r in enumerate(M225)])[0]
    assert gP == 4 and A.manhattan(P, g) == 3
    intro = (B.maze(M225, s, g, MARK225, extra_legend=[('#fff3b0', 'Markerad ruta')]) +
             p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet, g = billigaste kostnad från start). '
               'Att gå in i en lerruta kostar 3 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0.'))
    a = part(p('Bestäm g för P.'),
             [step('Två sätt att nå P', 'Genom leran: A1 → A2 → A3 kostar 3 + 1 = 4. Runt om: A1 → B1 → C1 → C2 → C3 → C4 → B4 → A4 → A3 kostar 8.'),
              step('g är den billigaste kostnaden', 'Vägen genom leran är billigast.')],
             'g = 4.', 'Räkna kostnaden för rutorna du går in i, inte antalet steg.', 2)
    b = part(p('Bestäm f för P. Välj ett alternativ.'),
             [step('h = radskillnad + kolumnskillnad', 'P ligger i A3 och målet i C4: h = 2 + 1 = 3.'),
              step('f = g + h', 'g = 4 enligt den billigaste vägen genom leran: f = 4 + 3 = 7.')],
             '7.', 'Bestäm g och h var för sig och lägg ihop dem.', 2,
             [alt('5', False, 'Du har räknat g som antal steg (2). Lerrutan kostar 3, så g = 4.'),
              alt('7', True, 'g = 4 och h = 3 ger f = 7.'),
              alt('3', False, 'Det är bara h. Du har glömt att lägga till g = 4.'),
              alt('11', False, 'g = 8 gäller vägen runt om, men g är den billigaste kostnaden, 4.')])
    return task('2.25', 'astar_varden', 'f-värde med lera', intro, [a, b],
                'g är vad det har kostat att komma till rutan. Lerrutor kostar mer än vanliga rutor.', ['procedur', 'begrepp'])


M226 = ['S..#G', '.#.#.', '.#...', '...#.']
MARK226 = {(0, 2): 'P', (2, 3): 'Q', (3, 2): 'R'}


def t226():
    s, g = A.parse(M226)
    ds = A.dist_all(M226, s)
    vals = {k: (ds[c], A.manhattan(c, g)) for c, k in MARK226.items()}
    assert vals == {'P': (2, 2), 'Q': (5, 3), 'R': (5, 5)}
    assert A.dist_all(M226, g)[(0, 2)] == 6
    intro = (B.maze(M226, s, g, MARK226, extra_legend=[('#fff3b0', 'Markerad ruta')]) + p(B.ASTAR_GH) +
             p('Elin har räknat ut g, h och f för de markerade rutorna. Ett av värdena är fel.') +
             tab(['Ruta', 'g', 'h', 'f'], [['P', '2', '6', '8'], ['Q', '5', '3', '8'], ['R', '5', '5', '10']]))
    a = part(p('Vilket värde är fel? Välj ett alternativ.'),
             [step('Kontrollera h för P', 'P ligger i A3 och målet i A5: 0 rader och 2 kolumner, h = 2.'),
              step('Elin räknade med väggarna', '6 är antalet steg från P till målet runt väggen. h ska räknas som om väggarna inte fanns.'),
              step('Övriga värden stämmer', 'Q: g = 5, h = 2 + 1 = 3. R: g = 5, h = 3 + 2 = 5.')],
             'h för P.', 'Räkna h för varje ruta och jämför med tabellen.', 3,
             [alt('g för P', False, 'A1 → A2 → A3 är 2 steg, så g = 2 stämmer.'),
              alt('h för P', True, 'h ska vara 2. Elin har räknat de 6 stegen runt väggen.'),
              alt('g för Q', False, 'A1 → A2 → A3 → B3 → C3 → C4 är 5 steg, så g = 5 stämmer.'),
              alt('f för R', False, 'R har g = 5 och h = 5, så f = 10 stämmer.')])
    b = part(p('Vilket är det rätta f-värdet för P?'),
             [step('Rätta h och lägg ihop', 'g = 2 och h = 2 ger f = 2 + 2 = 4.')],
             'f = 4.', 'Använd rätt h och samma g som i tabellen.', 2)
    return task('2.26', 'astar_varden', 'Hitta felet i f-tabellen', intro, [a, b],
                'h räknas som rad- plus kolumnskillnad, utan att ta hänsyn till väggar.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- A*-sökning

M227 = ['....G', '44...', '44...', 'S....']


def t227():
    s, g = A.parse(M227)
    gr, ast = A.greedy(M227), A.astar(M227)
    assert names(gr['path']) == ['D1', 'C1', 'B1', 'A1', 'A2', 'A3', 'A4', 'A5'] and gr['cost'] == 13
    assert names(ast['order'])[:2] == ['D1', 'D2'] and A.path_cost(M227, ast['path']) == 7 and len(ast['path']) == 8
    intro = (B.maze(M227, s, g) + p('Labyrinten söks igenom med girig bäst först och med A* (h = Manhattanavstånd). '
                                    'Att gå in i en isruta kostar 4 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0. '
                                    'Vid lika värde väljs den ruta som kommer först i bokstavsordning.'))
    a = part(p('Bestäm f för de två grannarna C1 och D2 till start.'),
             [step('g för grannarna', 'C1 är en isruta, g = 4. D2 är en vit ruta, g = 1.'),
              step('h till målet A5', 'C1: 2 + 4 = 6. D2: 3 + 3 = 6.'),
              step('f = g + h', 'C1: 4 + 6 = 10. D2: 1 + 6 = 7.')],
             'C1: f = 10. D2: f = 7.', 'g är kostnaden för att gå in i rutan.', 2)
    b = part(p('Vilken av C1 och D2 tar girig bäst först ut först, och vilken tar A* ut först?'),
             [step('Girig bäst först jämför h', 'Båda har h = 6. C1 kommer först i bokstavsordning.'),
              step('A* jämför f', 'D2 har f = 7, lägre än C1:s 10.')],
             'Girig bäst först tar C1. A* tar D2.', 'Vilket värde jämför respektive algoritm?', 2)
    c = part(p('Girig bäst först fortsätter upp genom isen. Vad kostar vägen den hittar, och vad kostar vägen A* hittar?'),
             [step('Girig bäst först', pil(names(gr['path'])) + ': 4 + 4 + 1 + 1 + 1 + 1 + 1 = 13.'),
              step('A* undviker isen', pil(names(ast['path'])) + ': sju vita rutor, kostnad 7.')],
             'Girig bäst först: 13. A*: 7.', 'Räkna kostnaden för varje ruta längs vägarna.', 3)
    return task('2.27', 'astar_sokning', 'Girig bäst först och A* på is', intro, [a, b, c],
                'Girig bäst först ser bara hur nära målet en ruta ligger. A* räknar också med vad vägen hittills har kostat.',
                ['procedur', 'begrepp'])


M228 = ['S...', '.#..', '...G']


def t228():
    s, g = A.parse(M228)
    r = A.astar(M228)
    assert names(r['order']) == ['A1', 'A2', 'A3', 'A4', 'B4', 'C4']
    # öppna listan när målet tas ut
    gg, openl, closed = {s: 0}, {s}, set()
    while openl:
        n = min(openl, key=lambda x: (gg[x] + A.manhattan(x, g), A.manhattan(x, g), A.cname(x)))
        openl.discard(n)
        closed.add(n)
        if n == g:
            break
        for v in A.neigh(M228, n):
            if v not in closed and gg[n] + 1 < gg.get(v, 99):
                gg[v] = gg[n] + 1
                openl.add(v)
    assert sorted(names(openl)) == ['B1', 'B3'] and all(gg[c] + A.manhattan(c, g) == 5 for c in openl)
    intro = B.maze(M228, s, g) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). ' + ASTAR_TIE)
    a = part(p('Ange besöksordningen.'),
             [step('Alla rutor på en kortaste väg har f = 5', 'Start har h = 2 + 3 = 5. A2 och B1 har båda g = 1, h = 4 och f = 5.'),
              step('Lika f och h: bokstavsordningen avgör', 'A2 tas ut före B1. Från A3 har A4 och B3 båda f = 5 och h = 2, och A4 kommer först.'),
              step('Sedan rakt ned', 'B4 har h = 1 och målet h = 0.')],
             lista(names(r['order'])) + '.', 'Räkna g, h och f för grannarna till varje ruta som tas ut.', 3)
    b = part(p('Vilka rutor ligger kvar i öppna listan när målet tas ut?'),
             [step('Rutor som lades in men aldrig togs ut', 'B1 lades in av start och B3 av A3. Båda har f = 5.')],
             'B1 och B3.', 'Vilka grannar lades in men hann inte tas ut?', 3)
    c = part(p('Både B1 och B3 har f = 5, precis som målet. Varför tas målet ut före dem? Välj ett alternativ.'),
             [step('Lika f avgörs av lägst h', 'Målet har h = 0, B3 har h = 2 och B1 har h = 4.')],
             'B.', 'Vilken regel gäller vid lika f?', 3,
             [alt('Målet har lägst f.', False, 'Alla tre har f = 5.'),
              alt('Målet har lägst h, och vid lika f väljs lägst h.', True, 'Målet har h = 0.'),
              alt('Målet lades in i öppna listan först.', False, 'Målet lades in sist, när B4 togs ut.'),
              alt('A* tar alltid ut målet så fort det har lagts in.', False, 'A* tar ut målet först när det har lägst f, och vid lika f lägst h.')])
    return task('2.28', 'astar_sokning', 'Öppna listan när målet tas ut', intro, [a, b, c],
                'Gå igenom reglerna för lika värden i tur och ordning: först f, sedan h, sedan bokstavsordning.', ['procedur', 'begrepp'], 3)


# ---------------------------------------------------------------- viktade vägar

M229 = ['S3..', '.33.', '..3.', '3..G']


def t229():
    s, g = A.parse(M229)
    c, path = A.ucs_grid(M229)
    assert c == 6 and names(path) == ['A1', 'B1', 'C1', 'C2', 'D2', 'D3', 'D4']
    top = ['A1', 'A2', 'A3', 'A4', 'B4', 'C4', 'D4']
    assert A.path_cost(M229, [(ord(x[0]) - 65, int(x[1]) - 1) for x in top]) == 8
    intro = B.maze(M229, s, g) + p('Att gå in i en lerruta kostar 3 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0.')
    a = part(p('Vad kostar den billigaste vägen från start till mål?'),
             [step('Undvik leran om det går', 'Vägen A1 → B1 → C1 → C2 → D2 → D3 → D4 går bara genom vita rutor.'),
              step('Kostnaden', 'Sex vita rutor eller mål, 1 var: 6.')],
             '6.', 'Finns det en väg som inte går genom någon lerruta?', 2)
    b = part(p('Ange den billigaste vägen.'),
             [step('Den enda vägen utan lera', 'D1 är lera, så vägen går in i C2 och ned till D2 innan den fortsätter åt höger.')],
             pil(names(path)) + '.', 'Följ de vita rutorna från start till mål.', 2)
    c = part(p('Vägen A1 → A2 → A3 → A4 → B4 → C4 → D4 har lika många steg. Vad kostar den? Välj ett alternativ.'),
             [step('Vägen går in i en lerruta', 'A2 kostar 3. A3, A4, B4, C4 och målet D4 kostar 1 var.'),
              step('Summera', '3 + 1 + 1 + 1 + 1 + 1 = 8.')],
             '8.', 'Vilka av rutorna längs vägen är lera?', 2,
             [alt('6', False, 'Det är antalet steg. Lerrutan A2 kostar 3, inte 1.'),
              alt('8', True, 'En lerruta (3) och fem rutor som kostar 1 ger 8.'),
              alt('9', False, 'Start kostar 0. Du har räknat med start.'),
              alt('18', False, 'Bara A2 är lera längs vägen. De andra rutorna kostar 1.')])
    return task('2.29', 'viktade_vagar', 'Billigaste vägen genom leran', intro, [a, b, c],
                'Kostnaden för en väg är summan av kostnaderna för rutorna du går in i.', ['procedur'])


G230 = dict(nodes={'S': (50, 150), 'A': (240, 65), 'B': (150, 235), 'C': (330, 235), 'M': (440, 150)},
            edges=[('S', 'A', 2), ('A', 'M', 9), ('S', 'B', 3), ('B', 'C', 2), ('C', 'M', 2)],
            h={'S': 4, 'A': 2, 'B': 4, 'C': 2, 'M': 0})


def t230():
    E, h = G230['edges'], G230['h']
    gr = A.greedy_graph(E, h, 'S', 'M')
    ast = A.astar_graph(E, h, 'S', 'M')
    assert gr['path'] == ['S', 'A', 'M'] and gr['cost'] == 11
    assert ast['path'] == ['S', 'B', 'C', 'M'] and ast['cost'] == 7
    assert [x[0] for x in ast['order']] == ['S', 'A', 'B', 'C', 'M']
    svg = weighted_graph(G230['nodes'], E, 'S', 'M', 'Graf med noderna S, A, B, C och M. Talet vid varje kant är kostnaden, och h står vid varje nod.', 490, h=h)
    intro = svg + p('Grafen söks igenom med girig bäst först och med A*. Talet vid varje kant är kostnaden att gå längs den. '
                    'Värdet h vid varje nod är en uppskattning av kostnaden kvar till målet M.')
    a = part(p('Vilken väg hittar girig bäst först, och vad kostar den?'),
             [step('Från S jämförs bara h', 'A har h = 2 och B har h = 4. A tas ut.'),
              step('Från A läggs målet in', 'M har h = 0 och tas ut direkt. Vägen går via kanten A–M som kostar 9.')],
             'S → A → M, kostnad 2 + 9 = 11.', 'Välj alltid noden med lägst h.', 2)
    b = part(p('Fyll i tabellen med noderna i den ordning A* tar ut dem.') +
             B.tab(['Tas ut', 'g', 'h', 'f'], [['S', '0', '4', '4']] + [['…', '…', '…', '…']] * 4),
             [step('A tas ut först med f = 2 + 2 = 4', 'Då får M g = 2 + 9 = 11 och f = 11.'),
              step('B och sedan C har f = 7', 'B: 3 + 4 = 7. Via B får C g = 5 och f = 5 + 2 = 7.'),
              step('Via C blir M billigare', 'M får g = 5 + 2 = 7 och f = 7, lägre än 11. M tas ut.',
                   B.tab(['Tas ut', 'g', 'h', 'f'], [[n, str(g), str(hh), str(f)] for n, g, hh, f in ast['order']]))],
             'S, A, B, C, M.', 'Räkna f = g + h och sänk g för M när en billigare väg hittas.', 3)
    c = part(p('Varför hittar A* en billigare väg än girig bäst först? Välj ett alternativ.'),
             [step('A* räknar med kostnaden hittills', 'Vägen via A får f = 11 när M läggs in. Vägen via B och C har f = 7, så A* undersöker den först.')],
             'C.', 'Vad tar A* hänsyn till som girig bäst först inte gör?', 2,
             [alt('A* har kortare h-värden.', False, 'Båda använder samma h-värden.'),
              alt('A* undersöker alla noder.', False, 'Här tar A* ut alla noder, men det är inte därför. Den väljer efter f = g + h.'),
              alt('A* räknar också med vad vägen hittills har kostat.', True, 'Den dyra kanten A–M ger hög kostnad g, och då väljer A* vägen via B och C.'),
              alt('Girig bäst först följer alltid kanten med lägst kostnad.', False, 'Girig bäst först tittar inte på kanternas kostnad alls, bara på h.')])
    return task('2.30', 'viktade_vagar', 'Girig bäst först och A* i en graf', intro, [a, b, c],
                'Jämför vad de två algoritmerna sorterar efter: bara h, eller g + h.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- minimax

def t311():
    assert A.minimax([[3, 7], [5, 6], [2, 9]], True) == 5
    assert A.minimax([[3, 7], [5, 6], [2, 1]], True) == 5
    assert A.minimax([[8, 7], [5, 6], [2, 9]], True) == 7
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [3, 7]}, {'n': 'B', 'k': [5, 6]}, {'n': 'C', 'k': [2, 9]}]}
    intro = game_tree(tree, True, 'Spelträd med MAX i roten R och MIN-noderna A, B och C.') + p('Spelträdet söks igenom med minimax.')
    a = part(p('Vilket värde får roten, och vilket drag väljer den?'),
             [step('A, B och C är MIN-noder', 'A = min(3, 7) = 3. B = min(5, 6) = 5. C = min(2, 9) = 2.'),
              step('Roten är en MAX-nod', 'R = max(3, 5, 2) = 5, via B.')],
             'Värdet 5, draget till B.', 'Bestäm först värdena i A, B och C.', 1)
    b = part(p('Lövet L6 ändras från 9 till 1. Vilket drag väljer roten nu? Välj ett alternativ.'),
             [step('C blir ännu sämre för MAX', 'C = min(2, 1) = 1.'),
              step('A och B är oförändrade', 'R = max(3, 5, 1) = 5, fortfarande via B.')],
             'Draget till B.', 'Vilken nod påverkas av ändringen?', 2,
             [alt('Draget till A', False, 'A är oförändrad med värdet 3, lägre än B:s 5.'),
              alt('Draget till B', True, 'Ändringen sänker bara C, som redan var sämst för MAX.'),
              alt('Draget till C', False, 'C får värdet 1, ännu lägre än förut.')])
    c = part(p('I stället ändras lövet L1 från 3 till 8. Övriga löv är som i bilden. Vilket värde får roten?'),
             [step('A får ett nytt värde', 'A = min(8, 7) = 7.'),
              step('Roten väljer nu A', 'R = max(7, 5, 2) = 7.')],
             '7.', 'Räkna om A först.', 2)
    return task('3.11', 'minimax', 'Ett löv ändras', intro, [a, b, c],
                'Ett ändrat löv påverkar bara noderna på vägen från lövet upp till roten.', ['procedur', 'begrepp'])


def t312():
    vals = [[[4, 2], [1, 6]], [[3, 5], [7, 0]]]
    assert A.minimax(vals, True) == 5
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [{'n': 'C', 'k': [4, 2]}, {'n': 'D', 'k': [1, 6]}]},
                            {'n': 'B', 'k': [{'n': 'E', 'k': [3, 5]}, {'n': 'F', 'k': [7, 0]}]}]}
    intro = game_tree(tree, True, 'Spelträd med MAX i roten, MIN-noderna A och B och MAX-noderna C, D, E och F.') + p('Spelträdet söks igenom med minimax.')
    a = part(p('Bestäm värdena i A och B.'),
             [step('C, D, E och F är MAX-noder', 'C = max(4, 2) = 4. D = max(1, 6) = 6. E = max(3, 5) = 5. F = max(7, 0) = 7.'),
              step('A och B är MIN-noder', 'A = min(4, 6) = 4. B = min(5, 7) = 5.')],
             'A = 4, B = 5.', 'Börja på nivån närmast löven.', 2)
    b = part(p('Ange vägen genom trädet när båda spelarna spelar så bra som möjligt (R → … → löv).'),
             [step('Roten väljer B', 'R = max(4, 5) = 5.'),
              step('MIN i B väljer E', 'E = 5 är lägre än F = 7.'),
              step('MAX i E väljer lövet 5', 'max(3, 5) = 5.')],
             'R → B → E → lövet 5 (L6).', 'Följ i varje nod det barn som ger nodens värde.', 2)
    c = part(p('Lövet L7 har värdet 7, det högsta under B. Varför hamnar spelet inte där? Välj ett alternativ.'),
             [step('MIN bestämmer i B', 'MIN väljer det barn som ger lägst värde. F ger 7 och E ger 5, så MIN väljer E.')],
             'B.', 'Vem väljer i nod B?', 3,
             [alt('MAX i roten väljer bort B.', False, 'Roten väljer B, eftersom B = 5 är större än A = 4.'),
              alt('MIN i B väljer E, eftersom E ger 5 och F ger 7.', True, 'MIN väljer alltid det lägsta värdet.'),
              alt('Lövet 7 utvärderas aldrig.', False, 'Minimax utvärderar alla löv.'),
              alt('MAX i F väljer lövet 0.', False, 'MAX väljer 7 i F, men MIN i B väljer inte F.')])
    return task('3.12', 'minimax', 'Vägen genom trädet vid bästa spel', intro, [a, b, c],
                'När alla nodvärden är kända följer man i varje nod det barn som gav nodens värde.', ['procedur', 'begrepp'])


# ---------------------------------------------------------------- alfa–beta

def t313():
    log = []
    assert A.alphabeta([[3, 5], [6, 1, 4], [2, 8]], False, log=log) == 5
    assert [x[1] for x in log if x[0] == 'cut'] == [[1, 4]] and [x[1] for x in log if x[0] == 'leaf'] == [3, 5, 6, 2, 8]
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [3, 5]}, {'n': 'B', 'k': [6, 1, 4]}, {'n': 'C', 'k': [2, 8]}]}
    intro = (game_tree(tree, False, 'Spelträd med MIN i roten R och MAX-noderna A, B och C. Löven heter L1–L7.') +
             p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))
    a = part(p('Vilket värde har β i roten när sökningen går vidare till B?'),
             [step('A undersöks först', 'A är en MAX-nod: A = max(3, 5) = 5.'),
              step('β är det bästa MIN i roten är säker på', 'Roten kan alltid välja A och få 5, så β = 5.')],
             'β = 5.', 'Vilket värde får A?', 3)
    b = part(p('Vilka löv beskärs?'),
             [step('B: L3 = 6 ger α = 6 ≥ β = 5', 'B är en MAX-nod och blir minst 6. MIN i roten har redan 5 via A och väljer aldrig B. L4 och L5 beskärs.'),
              step('C: L6 = 2 ger α = 2 < 5', 'Sökningen fortsätter. L7 = 8 är C:s sista löv, så inget mer kan beskäras.')],
             'L4 och L5.', 'Jämför B:s gräns α efter första lövet med β = 5.', 3)
    c = part(p('Vilket värde får roten?'),
             [step('Rotens barn', 'A = 5. B är minst 6. C = max(2, 8) = 8.'),
              step('Roten är en MIN-nod', 'R = min(5, minst 6, 8) = 5.')],
             '5.', 'Vilket av barnen ger lägst värde?', 2)
    return task('3.13', 'alfa_beta', 'Beskärning med MIN i roten', intro, [a, b, c],
                'När roten är en MIN-nod är det β i roten som avgör om en MAX-nod kan avbrytas.', ['procedur', 'begrepp'])


def t314():
    log = []
    assert A.alphabeta([[2, 7], [1, 3]], True, log=log) == 2
    assert [x[1] for x in log if x[0] == 'leaf'] == [2, 7, 1] and [x[1] for x in log if x[0] == 'cut'] == [[3]]
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [2, 7]}, {'n': 'B', 'k': [1, 3]}]}
    intro = (game_tree(tree, True, 'Spelträd med MAX i roten R och MIN-noderna A och B. Löven heter L1–L4.') +
             p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))
    a = part(p('Hur många löv utvärderas?'),
             [step('A undersöks helt', 'A = min(2, 7) = 2, så α = 2 i roten.'),
              step('B avbryts efter L3', 'L3 = 1 ger β = 1 ≤ α = 2. B kan som mest bli 1, så L4 beskärs.')],
             '3 löv.', 'Jämför B:s första löv med α.', 2)
    b = part(p('Vilka påståenden om alfa–beta stämmer? Välj alla som stämmer.'),
             [step('Samma svar som minimax', 'Beskurna löv kan inte ändra rotens värde. Därför blir värdet 2 med både minimax och alfa–beta.'),
              step('Ordningen spelar roll', 'Om B:s löv hade kommit i ordningen 3, 1 hade båda behövt utvärderas.')],
             'A och C.', 'Tänk på varför det är tillåtet att hoppa över L4.', 3,
             [alt('Alfa–beta ger samma rotvärde som minimax.', True, 'Bara löv som inte kan påverka rotens värde beskärs.'),
              alt('Ett beskuret löv kan ändra rotens värde.', False, 'Då skulle beskärningen ge fel svar. Ett löv beskärs bara när det inte kan påverka resultatet.'),
              alt('Ordningen på barnen påverkar hur mycket som beskärs.', True, 'Med ordningen 3, 1 i B hade båda löven behövt utvärderas.'),
              alt('Alfa–beta beskär alltid minst ett löv.', False, 'I ett träd där inga gränser korsas utvärderas alla löv, till exempel om B:s löv kommer i ordningen 3, 1.')])
    return task('3.14', 'alfa_beta', 'Vad beskärning betyder', intro, [a, b],
                'Ett löv beskärs bara när dess värde inte kan påverka rotens val.', ['procedur', 'begrepp'])


NYA = [t120, t121, t122, t123, t124, t125, t126, t127, t223, t224, t225, t226, t227, t228, t229, t230, t311, t312, t313, t314]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = [f() for f in NYA]
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    assert len({u['id'] for u in bank}) == len(bank)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya i denna omgång.')


if __name__ == '__main__':
    main()
