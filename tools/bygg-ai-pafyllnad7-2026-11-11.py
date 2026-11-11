"""AI-banken 2026-11-11, nionde omgången: BFS och DFS i träd och grafer.

Användarens önskemål (2026-11-11): fler uppgifter om träd med BFS och DFS. Tolv nya
uppgifter, sex i delmomentet ”BFS i träd och grafer” och sex i ”DFS i träd och grafer”,
med olika sammanhang (sökträd, graf med slingor, tunnelbanekarta, mappar, beslutsträd)
och olika frågeformer (antal, ordningsföljd, väg, flerval).

Svar som är en ordningsföljd eller väg rättas i Kunskapsgymmet med formatet
`namnordning`. Uppgiftens text `t` är skriven för papper; svarsinstruktionen i parentes
läggs bara i delkortets fråga (se CLAUDE.md, AI-banken).

Alla svar räknas fram här och kontrolleras oberoende i
tools/ai-pafyllnad7-2026-11-11.test.js. Grannar och barn tas i bokstavsordning
(vänster gren först i träden). En nod läggs in i kön högst en gång.

Kör efter bygg-ai-sjalvrattning-2026-11-11.py och före bygg-ai-omgruppering-2026-11-11.py.
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
from ai_figurer import step, search_tree  # noqa: E402

p, alt, num, val, kg_task, lista, pil = K.p, K.alt, K.num, K.val, K.kg_task, K.lista, K.pil
B = K.B
BANK = 'uppgifterai.js'
BFS_FAM, DFS_FAM = 'BFS i träd och grafer', 'DFS i träd och grafer'


# ---------------------------------------------------------------- sökningar

def tree_bfs(kids, start, goals):
    q, out, par, snaps = [start], [], {}, []
    while q:
        n = q.pop(0)
        out.append(n)
        if n in goals:
            break
        for k in kids.get(n, []):
            par[k] = n
            q.append(k)
        snaps.append((n, list(q)))
    path = [out[-1]]
    while path[0] in par:
        path.insert(0, par[path[0]])
    return out, path, snaps


def tree_dfs(kids, start, goals):
    out, stack = [], []

    def go(n):
        out.append(n)
        stack.append(n)
        if n in goals or any(go(k) for k in kids.get(n, [])):
            return True
        stack.pop()
        return False
    go(start)
    return out, stack


def adj_of(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    return {k: sorted(v) for k, v in adj.items()}


def graph_bfs(edges, start, goal):
    adj, q, seen, out, par, added = adj_of(edges), [start], {start}, [], {}, {}
    while q:
        n = q.pop(0)
        out.append(n)
        if n == goal:
            break
        added[n] = []
        for v in adj[n]:
            if v not in seen:
                seen.add(v)
                par[v] = n
                q.append(v)
                added[n].append(v)
    path = [goal]
    while path[0] in par:
        path.insert(0, par[path[0]])
    return out, path, added


def graph_dfs(edges, start, goal):
    adj, seen, out, stack = adj_of(edges), set(), [], []

    def go(n):
        seen.add(n)
        out.append(n)
        stack.append(n)
        if n == goal or any(v not in seen and go(v) for v in adj[n]):
            return True
        stack.pop()
        return False
    go(start)
    return out, stack


def graph_dist(edges, start):
    adj, d, q = adj_of(edges), {start: 0}, [start]
    while q:
        n = q.pop(0)
        for v in adj[n]:
            if v not in d:
                d[v] = d[n] + 1
                q.append(v)
    return d


# ---------------------------------------------------------------- figurer och delar

def layout(kids, root, unit=70, lvl=72, top=35, margin=40):
    """Lager för lager: löven får jämna avstånd, en förälder hamnar mitt över sina barn."""
    pos, leaves = {}, []

    def walk(n, d):
        ch = kids.get(n, [])
        for k in ch:
            walk(k, d + 1)
        if not ch:
            leaves.append(n)
            x = margin + (len(leaves) - 1) * unit
        else:
            x = (pos[ch[0]][0] + pos[ch[-1]][0]) / 2
        pos[n] = (round(x), top + d * lvl)
    walk(root, 0)
    width = 2 * margin + (len(leaves) - 1) * unit
    return pos, width


def tree_fig(kids, start, goals, title):
    nodes, width = layout(kids, start)
    edges = [(a, b) for a, bs in kids.items() for b in bs]
    return search_tree(nodes, edges, start, goals, title, max(width, 300))


def lst(fraga, steps, svar, ledtrad, tn, suf, vag=False):
    """Del vars svar är en ordningsföljd. svar: lista med namn."""
    d = B.part(p(fraga), steps, (pil(svar) if vag else lista(svar)) + '.', ledtrad, tn)
    d.update({'svarstyp': 'kort_text', 'rättSvar': ', '.join(svar), 'tolerans': None, 'självrättning': True,
              'svarFormat': 'namnordning', 'svarEnhet': None, 'spel': True, '_suf': suf})
    return d


def uppgift(id_, omr, familj, intro, parts, ledtrad, formaga):
    u = kg_task(id_, omr, familj, intro, parts, ledtrad, formaga)
    for d in u['spelDelar']:
        suf = d.pop('_suf', None)
        if suf:
            i = d['fraga'].index('</p>')
            d['fraga'] = d['fraga'][:i] + f' ({suf})' + d['fraga'][i:]
    return u


NO = 'Skriv noderna i ordning, åtskilda med kommatecken.'
NV = 'Skriv noderna längs vägen, från start till mål.'


# ======================================================================== BFS i träd och grafer

def t165():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D', 'E'], 'B': ['F'], 'C': ['G', 'H'], 'D': ['I'], 'F': ['J'], 'G': ['K']}
    out, path, _ = tree_bfs(kids, 'S', ['J'])
    assert out == ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] and path == ['S', 'B', 'F', 'J']
    niva2 = [k for n in kids['S'] for k in kids.get(n, [])]
    assert len(niva2) == 5
    intro = tree_fig(kids, 'S', ['J'], 'Sökträd med S överst. S har barnen A, B och C. A har D och E, B har F, C har G och H. '
                     'D har I, F har målet J och G har K.') + p('Trädet söks igenom med BFS (vänster gren först).')
    a = num('Hur många noder ligger exakt två steg under S?',
            [step('Barnen till A, B och C', 'A har D och E, B har F, C har G och H. Det är 2 + 1 + 2 = 5 noder.')], 5,
            'Börja med S:s barn och räkna sedan deras barn.', 1)
    b = lst('I vilken ordning tas noderna ut ur kön, fram till och med målet?',
            [step('Nivå 0 och nivå 1', 'S tas ut först, sedan A, B och C.'),
             step('Nivå 2 tas ut från vänster till höger', 'D, E, F, G och H. Deras barn hamnar längst bak i kön.'),
             step('Nivå 3 tills målet', 'I lades in före J, så I tas ut före J. Sedan tas J ut och sökningen stoppar.')],
            out, 'Ta alla noder på en nivå innan du går vidare till nästa nivå.', 3, NO)
    c = lst('Vilken väg till målet returnerar BFS?',
            [step('Följ föräldrarna bakåt från målet', 'J lades in av F, F av B och B av S.')], path,
            'Vilken nod lade in J i kön?', 2, NV, vag=True)
    return uppgift('1.65', 'bfs', BFS_FAM, intro, [a, b, c], 'BFS tar ut noderna nivå för nivå.', ['procedur'])


def t166():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E', 'F'], 'C': ['G'], 'D': ['H', 'I'], 'E': ['J']}
    out, _, snaps = tree_bfs(kids, 'S', ['H'])
    efter_d = dict(snaps)['D']
    assert efter_d == ['E', 'F', 'G', 'H', 'I'] and out == ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    intro = tree_fig(kids, 'S', ['H'], 'Sökträd med S överst. S har A och B. A har C och D, B har E och F. C har G, '
                     'D har målet H och I, E har J.') + p('Trädet söks igenom med BFS (vänster gren först). '
                                                           'Nya noder läggs in längst bak i kön.')
    a = lst('D tas ut och dess barn läggs in. Vilka noder ligger då i kön, från den som tas ut först till den som står längst bak?',
            [step('Uttagen före D', 'S, A, B och C tas ut först. Kön efter C är D, E, F och G.'),
             step('D tas ut och lägger in sina barn', 'D:s barn H och I läggs in längst bak. Kön blir E, F, G, H och I.')],
            efter_d, 'Skriv upp kön efter varje uttag. Nya noder hamnar längst bak.', 2,
            'Skriv noderna åtskilda med kommatecken.')
    b = num('Hur många noder tas ut ur kön, inklusive S och målet H?',
            [step('E, F och G står före H i kön', 'De tas ut innan H. Uttagen är ' + lista(out) + '.'),
             step('Räkna', f'Det är {len(out)} noder.')], len(out),
            'Målet tas ut först när noderna som står före det i kön har tagits ut.', 2)
    return uppgift('1.66', 'bfs', BFS_FAM, intro, [a, b], 'En FIFO-kö tar ut den nod som har legat längst.', ['procedur'])


G167 = [('S', 'A'), ('S', 'B'), ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'G'), ('E', 'G')]
P167 = {'S': (50, 130), 'A': (150, 55), 'B': (150, 205), 'C': (265, 55), 'D': (265, 205), 'E': (370, 55), 'G': (370, 205)}


def t167():
    out, path, added = graph_bfs(G167, 'S', 'G')
    assert added['C'] == ['E'] and out == ['S', 'A', 'B', 'C', 'D', 'E', 'G'] and path == ['S', 'B', 'D', 'G']
    intro = (search_tree(P167, G167, 'S', ['G'], 'Graf med noderna S, A, B, C, D, E och målet G. Kanter: S–A, S–B, A–B, A–C, '
                         'B–D, C–D, C–E, D–G och E–G.', 420)
             + p('Grafen söks igenom med BFS. En nods grannar läggs in i bokstavsordning, och en nod som redan har '
                 'lagts in i kön läggs inte in igen.'))
    a = val('Vilka noder läggs in i kön när C tas ut?',
            [step('C:s grannar är A, D och E', 'A har redan tagits ut, och D lades in när B togs ut. Bara E är ny.')],
            [alt('Bara E', True, 'A och D finns redan i sökningen, så bara E läggs in.'),
             alt('D och E', False, 'D lades redan in av B och läggs inte in igen.'),
             alt('A, D och E', False, 'A är redan uttagen. En nod läggs in högst en gång.'),
             alt('Inga noder', False, 'E har ännu inte lagts in, så E läggs in nu.')],
            'Vilka av C:s grannar har redan lagts in i kön?', 2)
    b = lst('I vilken ordning tas noderna ut ur kön, fram till och med målet?',
            [step('S och dess grannar', 'S tas ut och lägger in A och B.'),
             step('A och B', 'A lägger in C (B finns redan). B lägger in D.'),
             step('C och D', 'C lägger in E. D lägger in G.'),
             step('E och sedan G', 'E har inga nya grannar. Sedan tas G ut och sökningen stoppar.')],
            out, 'Skriv upp kön efter varje uttag och hoppa över noder som redan har lagts in.', 2, NO)
    c = num('Hur många kanter har vägen som BFS returnerar?',
            [step('Följ föräldrarna bakåt', 'G lades in av D, D av B och B av S. Vägen är ' + pil(path) + '.'),
             step('Räkna kanterna', f'{len(path)} noder ger {len(path) - 1} kanter.')], len(path) - 1,
            'Vilken nod lade in G i kön?', 2)
    return uppgift('1.67', 'bfs', BFS_FAM, intro, [a, b, c], 'I en graf med slingor läggs varje nod in i kön bara en gång.',
                   ['procedur', 'begrepp'])


G168 = [('S', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'M'), ('S', 'D'), ('D', 'E'), ('E', 'M'), ('D', 'F'), ('F', 'M')]
P168 = {'S': (45, 130), 'A': (130, 45), 'B': (240, 45), 'C': (350, 45), 'M': (430, 130), 'D': (150, 165),
        'E': (300, 130), 'F': (300, 215)}


def t168():
    out, path, _ = graph_bfs(G168, 'S', 'M')
    assert path == ['S', 'D', 'E', 'M'] and graph_dist(G168, 'S')['M'] == 3
    intro = (search_tree(P168, G168, 'S', ['M'], 'Tunnelbanekarta med hållplatserna S, A, B, C, D, E, F och M. '
                         'Linjer: S–A–B–C–M, S–D, D–E–M och D–F–M.', 470)
             + p('Kartan visar hållplatser i en tunnelbana. Wilma åker från S till M och vill passera så få '
                 'hållplatser som möjligt. Hon låter en app söka med BFS, där grannarna tas i bokstavsordning.'))
    a = num('Hur många steg (sträckor mellan två hållplatser) har resan med färst steg?',
            [step('Jämför vägarna', 'S → A → B → C → M har 4 steg. S → D → E → M och S → D → F → M har 3 steg.')], 3,
            'Räkna sträckorna längs några olika vägar från S till M.', 2)
    b = lst('Vilken väg returnerar BFS?',
            [step('E tas ut före F', 'D lägger in E och F i bokstavsordning. E tas ut först och lägger in M.'),
             step('Följ föräldrarna bakåt', 'M lades in av E, E av D och D av S.')], path,
            'Två vägar är lika korta. Vilken av D:s grannar tas ut först?', 2, NV, vag=True)
    c = val('Sträckan D–E tar 12 minuter och alla andra sträckor 2 minuter. Är vägen som BFS hittar då säkert den snabbaste?',
            [step('BFS räknar steg', 'BFS hittar en väg med färst steg, men tar inte hänsyn till hur lång tid varje sträcka tar.'),
             step('Jämför tiderna', 'S → D → E → M tar 2 + 12 + 2 = 16 minuter. S → D → F → M tar 6 minuter.')],
            [alt('Nej, BFS räknar hållplatser, inte minuter', True, 'S → D → F → M tar 6 minuter, mindre än BFS-vägens 16.'),
             alt('Ja, BFS hittar alltid den snabbaste vägen', False, 'Det gäller bara när alla steg kostar lika mycket.'),
             alt('Ja, för att den har färst steg', False, 'Färst steg är inte samma sak som kortast tid när sträckorna tar olika lång tid.'),
             alt('Nej, BFS hittar ingen väg alls', False, 'BFS hittar en väg till M, men inte nödvändigtvis den snabbaste.')],
            'Vad är det BFS räknar när den letar efter den kortaste vägen?', 3)
    return uppgift('1.68', 'bfs', BFS_FAM, intro, [a, b, c], 'BFS hittar en väg med färst steg.', ['procedur', 'resonemang'])


def t169():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['Q'], 'C': ['P']}
    out, path, _ = tree_bfs(kids, 'S', ['P', 'Q'])
    dout, dpath = tree_dfs(kids, 'S', ['P', 'Q'])
    assert out[-1] == 'Q' and len(out) == 6 and dout[-1] == 'P'
    intro = tree_fig(kids, 'S', ['P', 'Q'], 'Sökträd med S överst. S har A och B. A har C och D, C har målet P och B har målet Q.') + \
        p('Trädet har två mål, P och Q. Sökningen stoppar när ett mål tas ut. Barnen tas från vänster till höger.')
    a = val('Vilket mål hittar BFS?',
            [step('Q ligger närmare start', 'Q ligger två steg från S och P tre steg. BFS tar ut nivå 2 före nivå 3.')],
            [alt('Målet Q', True, 'Q ligger på nivå 2 och tas ut innan P har tagits ut.'),
             alt('Målet P', False, 'P ligger på nivå 3. Det är målet som DFS hittar.'),
             alt('Båda samtidigt', False, 'Noderna tas ut en i taget, och sökningen stoppar vid första målet.'),
             alt('Inget mål', False, 'Båda målen kan nås från S.')],
            'Vilket mål ligger på lägst nivå?', 1)
    b = num('Hur många noder tar BFS ut, inklusive S och målet?',
            [step('Uttagen', lista(out) + '. C:s barn P står efter Q i kön.'), step('Räkna', f'{len(out)} noder.')], len(out),
            'Skriv upp kön efter varje uttag.', 2)
    c = val('Vilket mål hittar DFS (vänster gren först)?',
            [step('DFS går ned i vänster gren', 'S → A → C → P. P är ett mål, så sökningen stoppar innan B undersöks.')],
            [alt('Målet P', True, 'DFS går ned genom A och C och når P innan den kommer till B.'),
             alt('Målet Q', False, 'Q ligger under B, som DFS inte hinner till.'),
             alt('Noden D', False, 'D är inget mål, och DFS hittar P innan den når D.'),
             alt('Inget mål', False, 'DFS når P längs den vänstra grenen.')],
            'Följ den vänstra grenen så långt det går.', 2)
    return uppgift('1.69', 'bfs', BFS_FAM, intro, [a, b, c], 'BFS hittar målet på lägst nivå, DFS det första målet längs grenen.',
                   ['procedur', 'begrepp'])


def t170():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D'], 'B': ['E', 'F'], 'C': ['G'], 'E': ['H']}
    out, _, _ = tree_bfs(kids, 'S', ['G'])
    assert out == ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    intro = tree_fig(kids, 'S', ['G'], 'Mappträd med S överst. S har mapparna A, B och C. A har D, B har E och F, '
                     'C har G och E har H. Filen ligger i G.') + \
        p('Varje nod är en mapp på en dator. Ett program letar efter en fil, som ligger i mappen G. '
          'Programmet söker med BFS och öppnar undermapparna från vänster till höger.')
    a = val('Vilken mapp undersöks som femte, räknat med S?',
            [step('Nivå för nivå', 'S är först. Sedan A, B och C. Femte mappen är A:s undermapp D.')],
            [alt('Mappen D', True, 'S, A, B, C och sedan D.'), alt('Mappen C', False, 'C undersöks som fjärde mapp.'),
             alt('Mappen E', False, 'E undersöks som sjätte mapp.'), alt('Mappen H', False, 'H ligger på nivå 3 och undersöks aldrig, eftersom filen hittas före.')],
            'Vilka mappar ligger direkt under S?', 1)
    b = num('Hur många mappar undersöks, inklusive S och mappen med filen?',
            [step('Uttagen', lista(out) + '.'), step('Räkna', f'{len(out)} mappar. H undersöks inte.')], len(out),
            'H ligger djupare än G. Undersöks H innan filen hittas?', 2)
    return uppgift('1.70', 'bfs', BFS_FAM, intro, [a, b], 'BFS undersöker mapparna nivå för nivå.', ['procedur'])


# ======================================================================== DFS i träd och grafer

def t171():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'C': ['E'], 'D': ['F', 'G'], 'B': ['H'], 'G': ['M']}
    out, path = tree_dfs(kids, 'S', ['M'])
    assert out == ['S', 'A', 'C', 'E', 'D', 'F', 'G', 'M'] and path == ['S', 'A', 'D', 'G', 'M']
    utanfor = [n for n in out if n not in path]
    assert utanfor == ['C', 'E', 'F']
    intro = tree_fig(kids, 'S', ['M'], 'Sökträd med S överst. S har A och B. A har C och D, C har E, D har F och G, '
                     'G har målet M och B har H.') + p('Trädet söks igenom med DFS (vänster gren först).')
    a = lst('Ange i vilken ordning noderna besöks, fram till och med målet.',
            [step('Ned i vänster gren', 'S → A → C → E. E har inga barn, så DFS backar till A.'),
             step('Nästa barn till A', 'D besöks, sedan D:s vänstra barn F. F har inga barn, så DFS backar till D.'),
             step('G och målet', 'G besöks och sedan M, som är målet.')],
            out, 'Gå så djupt som möjligt till vänster. Backa när en nod saknar obesökta barn.', 2, NO)
    b = num('Hur många av de besökta noderna ingår inte i vägen till målet?',
            [step('Vägen till målet', pil(path) + '.'), step('Besökta noder utanför vägen', lista(utanfor) + f', alltså {len(utanfor)}.')],
            len(utanfor), 'Jämför besöksordningen med vägen från S till M.', 2)
    c = lst('Vilken väg till målet hittar DFS?',
            [step('Noderna DFS står i när målet hittas', 'S, A, D och G leder ned till M.')], path,
            'Vilka noder ligger mellan S och M i trädet?', 1, NV, vag=True)
    return uppgift('1.71', 'dfs', DFS_FAM, intro, [a, b, c], 'DFS följer en gren ända ned innan den backar.', ['procedur'])


def t172():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E', 'F'], 'D': ['G']}
    stack, out, snaps = ['S'], [], {}
    while stack:
        n = stack.pop()
        out.append(n)
        if n == 'F':
            break
        stack.extend(reversed(kids.get(n, [])))
        snaps[n] = list(stack)
    assert snaps['A'] == ['B', 'D', 'C'] and out == ['S', 'A', 'C', 'D', 'G', 'B', 'E', 'F']
    intro = tree_fig(kids, 'S', ['F'], 'Sökträd med S överst. S har A och B. A har C och D, D har G och B har E och målet F.') + \
        p('Trädet söks igenom med DFS och en stack. En nods barn läggs på stacken så att det vänstra barnet hamnar överst. '
          'Nästa nod som tas ut är den översta.')
    a = lst('A tas ut och dess barn läggs på stacken. Vilka noder ligger då i stacken, från den nedersta till den översta?',
            [step('S tas ut', 'S:s barn läggs på: först B, sedan A överst.'),
             step('A tas ut', 'Kvar ligger B. A:s barn läggs på: först D, sedan C överst. Stacken är B, D, C.')],
            snaps['A'], 'Det vänstra barnet ska hamna överst, så det läggs på sist.', 2,
            'Skriv noderna åtskilda med kommatecken.')
    b = val('Vilken nod tas ut som sjätte, räknat med S?',
            [step('Uttagen i ordning', lista(out) + '.'), step('Sjätte uttaget', 'B tas ut när hela A-grenen är klar.')],
            [alt('Noden B', True, 'S, A, C, D och G tas ut först. Sedan ligger B överst.'),
             alt('Noden G', False, 'G tas ut som femte nod.'), alt('Noden E', False, 'E tas ut som sjunde nod, efter B.'),
             alt('Noden F', False, 'F tas ut sist, som åttonde nod.')],
            'Skriv upp stacken efter varje uttag.', 2)
    return uppgift('1.72', 'dfs', DFS_FAM, intro, [a, b], 'I en stack tas den senast inlagda noden ut först.', ['procedur'])


G173 = [('S', 'A'), ('S', 'C'), ('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'G'), ('E', 'G')]
P173 = {'S': (50, 130), 'A': (150, 45), 'B': (260, 45), 'D': (370, 45), 'C': (205, 165), 'E': (310, 215), 'G': (420, 160)}


def t173():
    out, path = graph_dfs(G173, 'S', 'G')
    kortast = graph_dist(G173, 'S')['G']
    assert out == ['S', 'A', 'B', 'C', 'E', 'G'] and len(path) - 1 == 5 and kortast == 3
    intro = (search_tree(P173, G173, 'S', ['G'], 'Graf med noderna S, A, B, C, D, E och målet G. Kanter: S–A, S–C, A–B, B–C, '
                         'B–D, C–E, D–G och E–G.', 470)
             + p('Grafen söks igenom med DFS. Grannarna tas i bokstavsordning, och en nod som redan har besökts besöks inte igen.'))
    a = lst('Ange i vilken ordning noderna besöks, fram till och med målet.',
            [step('Från S', 'S:s grannar är A och C. A kommer först i bokstavsordning.'),
             step('Vidare från A och B', 'A går vidare till B. B:s grannar är A, C och D. A är besökt, så C kommer före D.'),
             step('Vidare från C', 'C:s obesökta granne är E, och E leder till målet G.')],
            out, 'Ta alltid den första obesökta grannen i bokstavsordning.', 2, NO)
    b = num('Hur många kanter har vägen som DFS hittar?',
            [step('Vägen', pil(path) + '.'), step('Räkna kanterna', f'{len(path)} noder ger {len(path) - 1} kanter.')],
            len(path) - 1, 'Varje nod på vägen utom start har en kant in till sig.', 2)
    c = val('Har vägen som DFS hittar färst möjliga kanter?',
            [step('Jämför med en annan väg', 'S → C → E → G har bara 3 kanter.'),
             step('Varför DFS tog en omväg', 'DFS gick först till A, eftersom A kommer före C i bokstavsordning, och fortsatte på djupet.')],
            [alt('Nej, S → C → E → G har bara 3 kanter', True, 'DFS stoppar vid första vägen den hittar, inte den kortaste.'),
             alt('Ja, DFS hittar alltid en väg med färst kanter', False, 'Det gäller BFS. DFS kan gå en lång omväg först.'),
             alt('Ja, det finns ingen kortare väg till G', False, 'Vägen via C och E är kortare.'),
             alt('Nej, den kortaste vägen har 4 kanter', False, 'Det finns en väg med 3 kanter: S → C → E → G.')],
            'Finns det en väg från S till G som går via C direkt?', 3)
    return uppgift('1.73', 'dfs', DFS_FAM, intro, [a, b, c], 'DFS i en graf: gå vidare till första obesökta grannen, backa vid stopp.',
                   ['procedur', 'resonemang'])


def t174():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D', 'E'], 'D': ['F'], 'B': ['G', 'H'], 'H': ['M'], 'C': ['I']}
    out, _ = tree_dfs(kids, 'S', ['M'])
    alla = set(kids) | {k for v in kids.values() for k in v}
    aldrig = sorted(alla - set(out))
    assert out == ['S', 'A', 'D', 'F', 'E', 'B', 'G', 'H', 'M'] and aldrig == ['C', 'I']
    intro = tree_fig(kids, 'S', ['M'], 'Beslutsträd med S överst. S har A, B och C. A har D och E, D har F. B har G och H, '
                     'H har målet M. C har I.') + \
        p('En robot planerar hur den ska ta sig ur ett rum. Varje nod i trädet är ett läge, och barnen är lägen den kan nå '
          'därifrån. Roboten söker med DFS och prövar barnen från vänster till höger.')
    a = num('Hur många lägen besöks, inklusive S och målet M?',
            [step('Besöksordningen', lista(out) + '.'), step('Räkna', f'{len(out)} lägen.')], len(out),
            'Följ grenarna från vänster och backa vid återvändsgränder.', 2)
    b = val('F är den första återvändsgränden. Vilket läge besöks direkt efter F?',
            [step('Backa till närmaste läge med obesökt barn', 'D har inga fler barn, men A har E. Därför besöks E.')],
            [alt('Läget E', True, 'DFS backar till A, som har det obesökta barnet E.'),
             alt('Läget B', False, 'B besöks först när hela A-grenen är klar, alltså efter E.'),
             alt('Läget G', False, 'G ligger under B och besöks senare.'),
             alt('Läget S', False, 'S är redan besökt. DFS backar bara förbi den.')],
            'Vilken nod ovanför F har fortfarande ett obesökt barn?', 2)
    c = num('Hur många lägen i trädet besöks aldrig?',
            [step('Alla lägen', f'Trädet har {len(alla)} lägen.'),
             step('Besökta och obesökta', f'{len(out)} besöks. {lista(aldrig)} besöks aldrig, eftersom målet hittas under B.')],
            len(aldrig), 'Hinner DFS fram till C innan målet hittas?', 2)
    return uppgift('1.74', 'dfs', DFS_FAM, intro, [a, b, c], 'DFS backar till närmaste läge som har ett obesökt barn.', ['procedur'])


def t175():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D'], 'D': ['M'], 'B': ['E', 'F'], 'C': ['G', 'H']}
    dout, _ = tree_dfs(kids, 'S', ['M'])
    bout, _, _ = tree_bfs(kids, 'S', ['M'])
    assert dout == ['S', 'A', 'D', 'M'] and len(bout) == 10
    intro = tree_fig(kids, 'S', ['M'], 'Sökträd med S överst. S har A, B och C. A har D och D har målet M. B har E och F, C har G och H.') + \
        p('Trädet söks igenom en gång med DFS och en gång med BFS. Barnen tas från vänster till höger.')
    a = num('Hur många noder besöker DFS, inklusive S och målet?',
            [step('DFS går rakt ned i vänster gren', 'S → A → D → M. Målet hittas direkt.')], len(dout),
            'Följ den vänstra grenen.', 1)
    b = num('Hur många noder tar BFS ut, inklusive S och målet?',
            [step('Nivå för nivå', 'Nivå 0: S. Nivå 1: A, B, C. Nivå 2: D, E, F, G, H. Nivå 3: M.'),
             step('Räkna', f'1 + 3 + 5 + 1 = {len(bout)} noder.')], len(bout),
            'BFS måste ta ut hela nivå 2 innan målet på nivå 3.', 3)
    c = val('Varför hittar DFS målet med färre besökta noder i det här trädet?',
            [step('Målets placering', 'Målet ligger djupt i den första grenen som DFS går in i.'),
             step('BFS går på bredden', 'BFS måste först ta ut alla noder på nivå 1 och 2.')],
            [alt('Målet ligger djupt i den första gren som DFS går in i', True, 'DFS når det direkt, medan BFS först tar hela nivå 1 och 2.'),
             alt('DFS hittar alltid målet med färre besökta noder', False, 'Om målet hade legat under C hade DFS besökt fler noder.'),
             alt('BFS hittar inte målet', False, 'BFS hittar målet, men först efter 10 uttag.'),
             alt('DFS använder en uppskattning av avståndet till målet', False, 'DFS är oinformerad och använder ingen uppskattning.')],
            'Var ligger målet jämfört med den gren som DFS börjar i?', 3)
    return uppgift('1.75', 'dfs', DFS_FAM, intro, [a, b, c], 'Vilken sökning som går snabbast beror på var målet ligger.',
                   ['procedur', 'resonemang'])


def t176():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'C': ['E', 'F'], 'B': ['M']}
    vanster, _ = tree_dfs(kids, 'S', ['M'])
    hoger, _ = tree_dfs({k: list(reversed(v)) for k, v in kids.items()}, 'S', ['M'])
    assert vanster == ['S', 'A', 'C', 'E', 'F', 'D', 'B', 'M'] and hoger == ['S', 'B', 'M']
    intro = tree_fig(kids, 'S', ['M'], 'Sökträd med S överst. S har A och B. A har C och D, C har E och F. B har målet M.') + \
        p('Trädet söks igenom med DFS två gånger: en gång med vänster gren först och en gång med höger gren först.')
    a = num('Hur många noder besöks med vänster gren först, inklusive S och målet?',
            [step('Besöksordningen', lista(vanster) + '.'), step('Räkna', f'{len(vanster)} noder.')], len(vanster),
            'Hela A-grenen besöks innan B.', 2)
    b = num('Hur många noder besöks med höger gren först, inklusive S och målet?',
            [step('Besöksordningen', lista(hoger) + '. B är S:s högra barn, och målet ligger under B.')], len(hoger),
            'Vilket barn till S undersöks först nu?', 1)
    c = val('Vad avgör hur många noder DFS besöker innan målet i det här trädet?',
            [step('Samma träd, olika ordning', f'Med vänster först besöks {len(vanster)} noder, med höger först {len(hoger)}.'),
             step('Slutsats', 'DFS följer den första grenen helt innan den prövar nästa. Ordningen avgör vilken gren som kommer först.')],
            [alt('I vilken ordning barnen undersöks', True, 'Med höger gren först når DFS målet direkt.'),
             alt('Hur många mål trädet har', False, 'Trädet har bara ett mål i båda sökningarna.'),
             alt('Om sökningen använder en kö eller en prioritetskö', False, 'Båda sökningarna är DFS med samma datastruktur.'),
             alt('Ingenting, DFS besöker alltid lika många noder', False, 'Antalet blev 8 respektive 3 i samma träd.')],
            'Jämför svaren i a och b.', 3)
    return uppgift('1.76', 'dfs', DFS_FAM, intro, [a, b, c], 'DFS följer den första grenen helt innan nästa prövas.',
                   ['procedur', 'resonemang'])


NYA = [t165, t166, t167, t168, t169, t170, t171, t172, t173, t174, t175, t176]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    for f in NYA:
        u = f()
        for d in u['spelDelar']:
            for x in d.get('alternativ', []):
                assert len(x['kommentar']) > 15, (u['id'], x)
        old = next((k for k, x in enumerate(bank) if x['id'] == u['id']), None)
        if old is None:
            bank.append(u)
        else:
            bank[old] = u
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(NYA)} uppgifter (1.65–1.76) inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
