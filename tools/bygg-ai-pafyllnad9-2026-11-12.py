"""AI-banken 2026-11-12, punkt 2 i granskningen: uppgifter på C- och A-nivå för prov, och
E-uppgifter i alfa–beta.

Granskningen 2026-11-12 visade att köer och stackar samt prioritetsköer nästan saknade C,
att A-uppgifter bara fanns i alfa–beta och att alfa–beta nästan saknade E-uppgifter.
Elva konstruerade uppgifter:

- C, köer och stackar: 1.97 vilka uttagsordningar en stack kan ge, 1.98 vilken struktur och
  barnordning som gav en viss sökordning.
- C, prioritetsköer: 2.104 A*:s öppna lista när målet får ett lägre f, 2.105 varför A*
  behöver en prioritetskö.
- A, sökning: 1.99 DFS med olika grannordning (generalisera), 2.106 värdera tre heuristiker,
  2.107 för vilka kostnader k en väg lönar sig, 2.108 vad som alltid gäller för girig bäst först.
- E, alfa–beta: 3.70–3.72 nodvärden, rotvärde och en begreppsfråga i små träd.

Nivåerna för A-delarna och begreppsfrågorna sätts i nivåskriptets OVERRIDE.
Svaren kontrolleras oberoende i tools/ai-pafyllnad9-2026-11-12.test.js.
Kör efter bygg-ai-pafyllnad8-2026-11-11.py.
"""
import importlib.util
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _load(name, fil):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fil))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = _load('ai_kg', 'bygg-ai-kunskapsgymmet-2026-11-11.py')
P6 = _load('ai_p6', 'bygg-ai-pafyllnad6-2026-11-11.py')
P7 = _load('ai_p7', 'bygg-ai-pafyllnad7-2026-11-11.py')
from ai_figurer import step, maze, weighted_graph, tab  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, num, val, lista, pil, names = K.p, K.alt, K.num, K.val, K.lista, K.pil, K.names
lst, uppgift, tree_fig = P7.lst, P7.uppgift, P7.tree_fig
BANK = 'uppgifterai.js'
NO = 'Skriv noderna i ordning, åtskilda med kommatecken.'
U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)


# ======================================================================== C: köer och stackar

def stackordningar(nodes):
    """Alla uttagsordningar en stack kan ge när noderna läggs in i given ordning."""
    out = set()

    def gå(i, st, ut):
        if len(ut) == len(nodes):
            out.add(tuple(ut))
            return
        if i < len(nodes):
            gå(i + 1, st + [nodes[i]], ut)
        if st:
            gå(i, st[:-1], ut + [st[-1]])
    gå(0, [], [])
    return out


def t197():
    möjliga = stackordningar('ABCD')
    assert ('B', 'A', 'D', 'C') in möjliga and ('C', 'A', 'B', 'D') not in möjliga and len(möjliga) == 14
    intro = p('Noderna A, B, C och D ska läggas in i en stack i just den ordningen: först A, sedan B, C och D. '
              'Mellan inläggningarna får man ta ut noder när man vill.')
    a = val('Kan stacken ge uttagsordningen B, A, D, C?',
            [step('Pröva en följd av steg', 'Lägg in A och B. Ta ut B och sedan A. Lägg in C och D. Ta ut D och sedan C.'),
             step('Det fungerar', 'Uttagen blir B, A, D, C.')],
            [alt('Ja', True, 'In A, in B, ut B, ut A, in C, in D, ut D, ut C ger just den ordningen.'),
             alt('Nej', False, 'Det går: ta ut B och A innan C och D läggs in.')],
            'Försök hitta en följd av in och ut som ger ordningen.', 3)
    b = val('Kan stacken ge uttagsordningen C, A, B, D?',
            [step('C ska ut först', 'Då måste A, B och C ha lagts in, med B ovanpå A.'),
             step('A kan inte komma före B', 'Efter att C tagits ut ligger B överst. B måste tas ut före A.')],
            [alt('Nej, B ligger ovanpå A när C har tagits ut', True, 'En stack kan bara ta ut den översta noden.'),
             alt('Ja, om D läggs in först', False, 'D får inte läggas in före C, ordningen in är bestämd.'),
             alt('Ja, en stack kan ge alla ordningar', False, 'Ordningen C, A, B, D är omöjlig, eftersom B ligger över A.'),
             alt('Nej, en stack måste alltid ta ut A först', False, 'Det gäller en FIFO-kö. En stack kan ge till exempel B, A, D, C.')],
            'Hur ser stacken ut precis när C har tagits ut?', 3)
    c = val('Noderna läggs i stället in i en FIFO-kö i samma ordning. Kan kön ge någon annan uttagsordning än A, B, C, D?',
            [step('FIFO: först in, först ut', 'Oavsett när uttagen görs tas A ut först, sedan B, C och D.')],
            [alt('Nej, kön ger alltid A, B, C, D', True, 'En FIFO-kö behåller ordningen från inläggningen.'),
             alt('Ja, om man väntar med att ta ut', False, 'Väntan ändrar inte ordningen i en FIFO-kö.'),
             alt('Ja, kön kan ge samma ordningar som stacken', False, 'Stacken kan vända på ordningen, men inte kön.'),
             alt('Det beror på hur många noder som ligger i kön', False, 'Antalet noder i kön påverkar inte ordningen.')],
            'Vilken nod tas alltid ut först ur en FIFO-kö?', 3)
    return uppgift('1.97', 'ko_stack', 'Kö, stack och sökning i teorin', intro, [a, b, c],
                   'En stack kan bara ta ut den översta noden.', ['resonemang', 'begrepp'])


def t198():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E', 'F']}

    def kör(stack, hoger_overst=False):
        s, ut = ['S'], []
        while s:
            n = s.pop() if stack else s.pop(0)
            ut.append(n)
            if n == 'F':
                break
            barn = kids.get(n, [])
            s.extend(barn if (not stack or hoger_overst) else list(reversed(barn)))
        return ut
    o1, o2, o3 = kör(False), kör(True), kör(True, True)
    assert o1 == list('SABCDEF') and o2 == list('SACDBEF') and o3 == list('SBF')
    intro = tree_fig(kids, 'S', ['F'], 'Sökträd med S överst. S har A och B, A har C och D, B har E och målet F.') + \
        p('Trädet söks igenom tre gånger, och sökningen stoppar när F tas ut. Varje gång läggs en nods barn in i en '
          'datastruktur när noden tas ut. Ordningen som noderna tas ut i skiljer sig mellan sökningarna.')
    a = val(f'Den första sökningen tar ut noderna i ordningen {lista(o1)}. Vilken datastruktur användes?',
            [step('Nivå för nivå', 'Först S, sedan A och B, sedan C, D, E och F. Det är BFS.'),
             step('BFS använder en FIFO-kö', 'Barnen läggs längst bak och tas ut i den ordning de lades in.')],
            [alt('En FIFO-kö', True, 'Nivå för nivå är just BFS med en FIFO-kö.'),
             alt('En stack', False, 'En stack skulle gå ned i en gren innan B undersöks.'),
             alt('En prioritetskö sorterad efter h', False, 'Trädet har inga h-värden, och ordningen är ren nivåordning.'),
             alt('Det går inte att avgöra', False, 'Ordningen avslöjar strukturen: alla noder på en nivå tas ut innan nästa.')],
            'Tas en hel nivå ut innan nästa påbörjas?', 3)
    b = val(f'Den andra sökningen tar ut noderna i ordningen {lista(o2)}. Vilken datastruktur användes?',
            [step('Hela vänstra grenen först', 'Efter A tas C och D ut innan B. Det är DFS.'),
             step('DFS använder en stack', 'Den senast inlagda noden tas ut först.')],
            [alt('En stack', True, 'DFS med en stack går ned i A-grenen innan B.'),
             alt('En FIFO-kö', False, 'En FIFO-kö skulle ta ut B direkt efter A.'),
             alt('En prioritetskö sorterad efter f', False, 'Det finns inga f-värden i trädet.'),
             alt('Två köer', False, 'En enda stack räcker för att ge den ordningen.')],
            'Tas B ut direkt efter A, eller först när A:s barn är klara?', 3)
    c = val(f'Den tredje sökningen tar ut noderna i ordningen {lista(o3)}. Vad gäller för den sökningen?',
            [step('Djupet först, men höger gren först', 'Efter S kommer B och sedan B:s högra barn F, innan A och E.'),
             step('Barnen läggs på i bokstavsordning', 'Det högra barnet läggs sist och hamnar överst i stacken.')],
            [alt('En stack där det högra barnet hamnar överst', True, 'Därför tas B ut före A och F före E.'),
             alt('En FIFO-kö där barnen läggs in från höger', False, 'En kö skulle ta ut A före B:s barn, nivå för nivå.'),
             alt('En stack där det vänstra barnet hamnar överst', False, 'Då skulle A tas ut direkt efter S.'),
             alt('En prioritetskö efter bokstavsordning', False, 'Då skulle A tas ut före B.')],
            'Vilken nod tas ut direkt efter S, och vad säger det om ordningen i stacken?', 3)
    return uppgift('1.98', 'ko_stack', 'Kö, stack och sökning i teorin', intro, [a, b, c],
                   'Uttagsordningen avslöjar om det är en kö eller en stack.', ['resonemang', 'begrepp'])


# ======================================================================== A: DFS och grannordning

M199 = ['S.#..', '...#.', '.#...', '...#G']


def t199():
    s, g = A.parse(M199)
    r1, r2 = A.dfs(M199, (U, R, D, L)), A.dfs(M199, (D, R, U, L))
    b = A.bfs(M199)
    n1, n2, nb = len(r1['path']) - 1, len(r2['path']) - 1, len(b['path']) - 1
    assert (n1, n2, nb) == (7, 9, 7)
    intro = maze(M199, s, g) + p('Labyrinten söks igenom med DFS två gånger, med två olika grannordningar.')
    a = num('Hur många steg har vägen som DFS hittar med grannordningen ↑ → ↓ ←?',
            [step('Vägen', pil(names(r1['path'])) + '.'), step('Räkna stegen', f'{n1} steg.')], n1,
            'Pröva alltid uppåt först, sedan höger, nedåt och vänster.', 3)
    b_ = num('Hur många steg har vägen som DFS hittar med grannordningen ↓ → ↑ ←?',
             [step('Vägen', pil(names(r2['path'])) + '.'), step('Räkna stegen', f'{n2} steg.')], n2,
             'Nu prövas nedåt först. Följ den grenen så långt det går.', 3)
    c = val('Vilket påstående stämmer för alla labyrinter, inte bara den här?',
            [step('Jämför', f'Med olika grannordning hittade DFS {n1} och {n2} steg. BFS hittar alltid en väg med färst steg, här {nb}.'),
             step('Generalisera', 'DFS stoppar vid den första vägen den hittar, och vilken väg det blir beror på grannordningen. '
                                  'BFS tar ut rutorna efter avstånd, så längden på BFS-vägen beror inte på ordningen.')],
            [alt('Vilken väg DFS hittar beror på grannordningen, men BFS-vägen har alltid färst steg', True,
                 'Ordningen styr DFS, medan BFS alltid når målet först längs en kortaste väg.'),
             alt('DFS hittar alltid kortaste vägen om man börjar åt höger', False,
                 'Det finns labyrinter där höger först leder in i en lång omväg.'),
             alt('Grannordningen ändrar också hur många steg BFS-vägen har', False,
                 'Ordningen kan ändra vilken av flera lika korta vägar BFS väljer, men inte längden.'),
             alt('DFS hittar alltid en längre väg än BFS', False, f'Med ↑ → ↓ ← hittade DFS här en lika kort väg, {n1} steg.')],
            'Tänk på hur BFS och DFS väljer ordning, inte bara på den här labyrinten.', 4)
    return uppgift('1.99', 'dfs', 'DFS i labyrinter', intro, [a, b_, c], 'Grannordningen styr vilken gren DFS följer först.',
                   ['procedur', 'resonemang'])


# ======================================================================== C: prioritetsköer

G2104 = [('S', 'A', 1), ('S', 'B', 4), ('A', 'B', 1), ('A', 'M', 7), ('B', 'C', 1), ('C', 'M', 1)]
H2104 = {'S': 4, 'A': 3, 'B': 2, 'C': 1, 'M': 0}
P2104 = {'S': (50, 140), 'A': (170, 50), 'B': (200, 220), 'C': (340, 200), 'M': (450, 90)}


def astar_logg(edges, h, s, m):
    adj = {}
    for x, y, w in edges:
        adj.setdefault(x, []).append((y, w))
        adj.setdefault(y, []).append((x, w))
    g, open_, closed, ut, logg = {s: 0}, {s}, set(), [], []
    while open_:
        n = min(open_, key=lambda x: (g[x] + h[x], h[x], x))
        open_.discard(n)
        closed.add(n)
        ut.append(n)
        if n == m:
            break
        for v, w in sorted(adj[n]):
            if v not in closed and g[n] + w < g.get(v, 10 ** 9):
                g[v] = g[n] + w
                open_.add(v)
                logg.append((n, v, g[v], g[v] + h[v]))
    return ut, logg, g


def t2104():
    ut, logg, g = astar_logg(G2104, H2104, 'S', 'M')
    fm = [f for _, v, _, f in logg if v == 'M']
    assert ut == ['S', 'A', 'B', 'C', 'M'] and fm == [8, 4] and g['M'] == 4
    intro = (weighted_graph(P2104, G2104, 'S', 'M', 'Graf med noderna S, A, B, C och målet M. Kanter: S–A 1, S–B 4, A–B 1, '
                            'A–M 7, B–C 1 och C–M 1. h: S 4, A 3, B 2, C 1, M 0.', 500, h=H2104)
             + p('Grafen söks igenom med A*. Öppna listan är en prioritetskö där lägst f = g + h tas ut först. '
                 'Om en nod som redan ligger i kön nås via en billigare väg, får den nya, lägre värden.'))
    rader = [[n, v, str(gv), str(f)] for n, v, gv, f in logg]
    a = lst('I vilken ordning tas noderna ut ur prioritetskön, fram till och med M?',
            [step('Läggs in eller uppdateras', tab(['Uttagen nod', 'Granne', 'g', 'f'], rader)),
             step('Lägst f vid varje uttag', 'S (f = 4), A (f = 4), B (f = 4 efter uppdateringen), C (f = 4) och sist M (f = 4).')],
            ut, 'Skriv upp kön med f efter varje uttag. Uppdatera f när en billigare väg hittas.', 3, NO)
    b = P7.B.part(p('Vilket f har M när M läggs in i kön första gången, och vilket f har M när M tas ut?'),
                  [step('Första gången, via A', 'g = 1 + 7 = 8 och f = 8 + 0 = 8.'),
                   step('Billigare väg via B och C', 'g = 1 + 1 + 1 + 1 = 4 och f = 4. M får det nya värdet innan den tas ut.')],
                  'Första gången f = 8, när M tas ut f = 4.', 'Följ vägen S → A → M och sedan vägen via B och C.', 3)
    b.update({'svarstyp': 'flera_delar', 'rättSvar': fm, 'tolerans': [0, 0], 'självrättning': True, 'svarFormat': ['numeriskt'] * 2,
              'svarEnhet': [None, None], 'svarEtiketter': ['Första gången', 'När M tas ut'], 'svarsstruktur': 'ordnad', 'spel': True})
    c = val('Varför tas M inte ut direkt när den ligger i kön med f = 8?',
            [step('Andra noder har lägre f', 'B och C har f = 4 och tas ut först.'),
             step('Under tiden hittas en billigare väg', 'Via C får M f = 4. A* returnerar därför vägen med kostnad 4, inte 8.')],
            [alt('B och C har lägre f och tas ut först, och via C hittas en billigare väg till M', True,
                 'Därför hittar A* vägen med kostnad 4 i stället för 8.'),
             alt('M har högst h och tas därför ut sist', False, 'M har h = 0, det lägsta. Det är f som avgör.'),
             alt('Målet tas alltid ut sist i A*', False, 'Målet tas ut när det har lägst f, oavsett hur många noder som är kvar.'),
             alt('M lades in efter B och C och får vänta på sin tur', False, 'En prioritetskö tar ut lägst f, inte den som lades in först.')],
            'Jämför f för M med f för de andra noderna i kön.', 3)
    return uppgift('2.104', 'prioritetsko', 'Prioritetskön i girig bäst först och A*', intro, [a, b, c],
                   'En nod i kön kan få lägre f om en billigare väg hittas.', ['procedur', 'resonemang'])


def t2105():
    intro = p('Frågorna handlar om varför A* använder en prioritetskö för öppna listan.')
    a = val('Vad händer om A* använder en vanlig FIFO-kö i stället för en prioritetskö?',
            [step('En FIFO-kö bryr sig inte om f', 'Noderna tas ut i den ordning de läggs in. Sökningen går då nivå för nivå, som BFS.')],
            [alt('Noderna tas ut i den ordning de lades in, och f-värdena används inte', True,
                 'Sökningen blir som BFS och kan missa den billigaste vägen när stegen kostar olika.'),
             alt('Ingenting, A* fungerar likadant', False, 'A* behöver ta ut lägst f. Det gör inte en FIFO-kö.'),
             alt('A* blir snabbare, eftersom en kö är enklare', False, 'Den kan bli enklare, men den väljer inte längre den mest lovande noden.'),
             alt('Sökningen blir som DFS', False, 'DFS kräver en stack. En FIFO-kö ger BFS.')],
            'Vilken nod tar en FIFO-kö ut?', 3)
    b = val('Varför kan A* behöva ändra f för en nod som redan ligger i öppna listan?',
            [step('Samma nod kan nås på flera sätt', 'Om en billigare väg till noden hittas blir g lägre, och då också f.')],
            [alt('En billigare väg till noden har hittats, så g och f blir lägre', True,
                 'Noden ska då sorteras efter det nya, lägre f-värdet.'),
             alt('h för noden ändras under sökningen', False, 'h är en uppskattning som bara beror på noden och målet.'),
             alt('Noden har legat för länge i kön', False, 'En prioritetskö sorterar efter f, inte efter tid i kön.'),
             alt('Målet har flyttats', False, 'Målet ligger fast under hela sökningen.')],
            'Vad i f = g + h kan ändras när en ny väg hittas?', 3)
    return uppgift('2.105', 'prioritetsko', 'Prioritetskön i girig bäst först och A*', intro, [a, b],
                   'A* tar alltid ut den nod som har lägst f just nu.', ['begrepp', 'resonemang'])


# ======================================================================== A: värdera heuristiker

M2106 = ['S.....', '.##.#.', '...#..', '.#...G']


def t2106():
    s, g = A.parse(M2106)
    P = (3, 3)
    sann = A.dist_all(M2106, g)
    h1, h2, h3 = A.manhattan(P, g), 2 * A.manhattan(P, g), abs(P[1] - g[1])
    assert (h1, h2, h3, sann[P]) == (2, 4, 2, 2)
    # h1 och h3 överskattar aldrig, h2 överskattar i P; h1 är aldrig mindre än h3.
    for c, d in sann.items():
        assert abs(c[1] - g[1]) <= A.manhattan(c, g) <= d
    intro = (maze(M2106, s, g, {P: 'P'}, extra_legend=[('#fff3b0', 'Markerad ruta')]) +
             p('Tre heuristiker föreslås för A* i labyrinten:') +
             p('h₁ = Manhattanavståndet till målet, h₂ = 2 · Manhattanavståndet och h₃ = antalet kolumner till målet.'))
    a = num('Bestäm h₂ för rutan P.', [step('Manhattanavståndet från P', 'P ligger i D4 och målet i D6: 0 + 2 = 2.'),
                                        step('h₂ är det dubbla', 'h₂ = 2 · 2 = 4.')], h2, 'Räkna först Manhattanavståndet.', 1)
    b = num('Hur många steg är det i verkligheten från P till målet?', [step('Längs gångarna', 'P → D5 → D6: 2 steg.')], sann[P],
            'Följ gången från P till målet.', 1)
    c = val('Vilken av heuristikerna kan överskatta hur långt det är kvar?',
            [step('Jämför med verkligheten i P', f'h₂ = {h2}, men det är bara {sann[P]} steg kvar.'),
             step('h₁ och h₃', 'Manhattanavståndet är aldrig längre än den verkliga vägen, och antalet kolumner är aldrig större än Manhattanavståndet.')],
            [alt('h₂', True, f'I P är h₂ = {h2} men det är bara {sann[P]} steg kvar.'),
             alt('h₁', False, 'Manhattanavståndet räknar som om det inte fanns några väggar och är därför aldrig för stort.'),
             alt('h₃', False, 'Antalet kolumner är aldrig större än Manhattanavståndet, och därmed aldrig för stort.'),
             alt('Ingen av dem', False, 'h₂ överskattar till exempel i P.')],
            'Jämför h med det verkliga antalet steg kvar i en ruta nära målet.', 4)
    d = val('h₁ och h₃ överskattar aldrig. Vilken av dem hjälper A* mest att välja rätt ruta?',
            [step('h₁ är aldrig mindre än h₃', 'Manhattanavståndet räknar både rader och kolumner, h₃ bara kolumner.'),
             step('Närmare den verkliga kostnaden', 'En heuristik som inte överskattar hjälper mer ju närmare den ligger det verkliga avståndet.')],
            [alt('h₁, eftersom den ligger närmare det verkliga avståndet', True,
                 'h₁ är aldrig mindre än h₃ men heller aldrig för stor, så den skiljer bättre mellan rutorna.'),
             alt('h₃, eftersom den är mindre', False, 'Ett mindre h ger mindre hjälp. Med h = 0 överallt får A* ingen hjälp alls av h.'),
             alt('De hjälper exakt lika mycket', False, 'I rutor på olika rader ger h₁ mer information än h₃.'),
             alt('h₂, eftersom den är störst', False, 'h₂ överskattar, och då kan A* missa den billigaste vägen.')],
            'Vilken av h₁ och h₃ ligger närmast det verkliga avståndet?', 4)
    return uppgift('2.106', 'astar_varden', 'Heuristiken h', intro, [a, b, c, d],
                   'En bra heuristik överskattar aldrig men ligger nära det verkliga avståndet.', ['procedur', 'resonemang'])


# ======================================================================== A: när lönar sig vägen?

G2107 = [('S', 'A', 'k'), ('A', 'M', 'k'), ('S', 'B', 2), ('B', 'C', 2), ('C', 'M', 2)]
P2107 = {'S': (50, 150), 'A': (240, 50), 'M': (430, 150), 'B': (160, 230), 'C': (320, 230)}


def t2107():
    via_a = lambda k: 2 * k  # noqa: E731
    via_b = 6
    assert [k for k in range(1, 10) if via_a(k) < via_b] == [1, 2]
    intro = (weighted_graph(P2107, G2107, 'S', 'M', 'Graf: S–A och A–M kostar k var. S–B, B–C och C–M kostar 2 var.', 480)
             + p('Grafen visar vägar från S till M. Kanterna S–A och A–M kostar k var, där k är ett positivt heltal. '
                 'De andra kanterna kostar 2.'))
    a = num('Anta att k = 4. Vad kostar vägen S → A → M?', [step('Två kanter som kostar k', '4 + 4 = 8.')], 8, 'Lägg ihop kanternas kostnader.', 1)
    b = num('Vad kostar vägen S → B → C → M?', [step('Tre kanter som kostar 2', '2 + 2 + 2 = 6.')], 6, 'Lägg ihop kanternas kostnader.', 1)
    c = val('För vilka heltal k är vägen via A billigast?',
            [step('Ställ upp villkoret', 'Vägen via A kostar 2k och vägen via B och C kostar 6. Via A är billigast när 2k < 6, alltså k < 3.'),
             step('Heltal', 'k = 1 och k = 2. Med k = 3 kostar båda vägarna 6.')],
            [alt('k ≤ 2', True, '2k < 6 gäller för k = 1 och k = 2.'),
             alt('k ≤ 3', False, 'Med k = 3 kostar båda vägarna 6, så vägen via A är inte billigast.'),
             alt('k ≥ 3', False, 'Med stort k blir vägen via A dyr, till exempel 8 när k = 4.'),
             alt('k < 6', False, 'Vägen via A har två kanter som kostar k, så kostnaden är 2k, inte k.')],
            'Skriv kostnaden för båda vägarna med k och jämför.', 4)
    return uppgift('2.107', 'viktade_vagar', 'Billigaste väg i grafer', intro, [a, b, c],
                   'Skriv kostnaden för varje väg med k och jämför.', ['procedur', 'resonemang'])


# ======================================================================== A: girig bäst först i alla labyrinter

M2108 = ['S333G', '.....']


def t2108():
    s, g = A.parse(M2108)
    gr, ast = A.greedy(M2108), A.astar(M2108)
    ka = A.path_cost(M2108, ast['path'])
    assert gr['cost'] == 10 and ka == 6 and A.ucs_grid(M2108)[0] == 6
    intro = (maze(M2108, s, g) + p('Labyrinten söks igenom med girig bäst först och med A* (h = Manhattanavstånd). '
                                    'Att gå in i en lerruta (3) kostar 3 och att gå in i en vit ruta eller målet kostar 1.'))
    a = num('Vad kostar vägen som girig bäst först hittar?',
            [step('Lägst h hela vägen', f'Girig bäst först går rakt åt höger: {pil(names(gr["path"]))}.'),
             step('Summera', '3 + 3 + 3 + 1 = 10.')], gr['cost'], 'Girig bäst först väljer alltid grannen med lägst h.', 2)
    b = num('Vad kostar vägen som A* hittar?',
            [step('A* räknar med g', f'Vägen runt leran: {pil(names(ast["path"]))}.'), step('Summera', 'Sex vita rutor: 6.')], ka,
            'Jämför kostnaden för vägen genom leran med vägen runt den.', 2)
    c = val('Vilket påstående om girig bäst först stämmer i alla labyrinter, inte bara den här?',
            [step('Girig bäst först jämför bara h', 'Den bortser från vad vägen hittills har kostat, g.'),
             step('Slutsats', 'Därför kan den hitta en dyrare väg än A*, men den behöver inte göra det.')],
            [alt('Den kan hitta en dyrare väg än A*, eftersom den bortser från g', True,
                 'Här kostar dess väg 10 mot A*:s 6. I andra labyrinter kan vägarna bli lika billiga.'),
             alt('Den hittar alltid en dyrare väg än A*', False, 'I en labyrint utan terräng och väggar hittar den ofta lika billig väg.'),
             alt('Den hittar alltid en väg med färst steg', False, 'Den kan gå in i återvändsgränder och omvägar, eftersom den bara jämför h.'),
             alt('Den tar alltid ut fler rutor än A*', False, 'Girig bäst först tar ofta ut färre rutor, eftersom den styr rakt mot målet.')],
            'Vad tar girig bäst först inte hänsyn till?', 4)
    return uppgift('2.108', 'astar_sokning', 'Girig bäst först jämfört med A*', intro, [a, b, c],
                   'Girig bäst först jämför bara h, A* jämför f = g + h.', ['procedur', 'resonemang'])


# ======================================================================== E: alfa–beta

AB_E = [
    ('3.70', [[3, 7], [2, 9], [8, 5]], True, 'En spelagent i ett brädspel har räknat fram talen i löven.',
     ('Får roten samma värde med alfa–beta som med vanlig minimax?', 'Beskärning ändrar inte rotens värde',
      'Alfa–beta hoppar bara över grenar som inte kan påverka rotens val. Värdet blir detsamma som med minimax.',
      [('Ja, beskärningen ändrar aldrig rotens värde', True, 'Bara grenar som inte kan påverka resultatet hoppas över.'),
       ('Nej, alfa–beta ger ett högre värde', False, 'Alfa–beta ger samma värde, men snabbare.'),
       ('Nej, alfa–beta ger ett lägre värde', False, 'Beskärningen tar inte bort något som kunde ha ändrat svaret.'),
       ('Det beror på hur många löv som beskärs', False, 'Värdet är detsamma oavsett hur mycket som beskärs.')])),
    ('3.71', [[4, 1], [6, 2], [3, 8]], False, 'I ett kortspel för två har talen i löven räknats fram för slutlägena.',
     ('Vad är syftet med att beskära grenar?', 'Spara arbete',
      'Grenar som inte kan ändra rotens val behöver inte undersökas. Sökningen blir snabbare med samma svar.',
      [('Att slippa undersöka grenar som inte kan ändra rotens val', True, 'Det sparar tid utan att ändra svaret.'),
       ('Att hitta ett bättre värde än minimax', False, 'Värdet blir detsamma som med minimax.'),
       ('Att ta bort de drag som är sämst för MAX', False, 'Det är inte dragen som tas bort, utan undersökningen av dem.'),
       ('Att göra trädet mindre innan spelet börjar', False, 'Trädet är detsamma. Det är sökningen som hoppar över delar.')])),
    ('3.72', [[5, 9, 6], [2, 8, 7]], True, 'En dator spelar luffarschack och bedömer slutlägena med tal.',
     ('Vilken metod bygger alfa–beta-beskärning på?', 'Alfa–beta är minimax med beskärning',
      'Alfa–beta räknar samma värden som minimax, men hoppar över grenar som inte kan påverka resultatet.',
      [('Minimax', True, 'Alfa–beta är minimax där onödiga grenar hoppas över.'),
       ('Bredden först (BFS)', False, 'BFS är en sökning efter en väg, inte en metod för spelträd.'),
       ('A*', False, 'A* söker en väg med en heuristik och används inte för spelträd.'),
       ('Girig bäst först', False, 'Girig bäst först söker en väg med h, inte ett bästa drag i ett spel.')])),
]


def ab_e(id_, vals, root_max, sammanhang, begrepp):
    r = T.build(vals, root_max)
    v, ev, cuts, notes = T.alphabeta(r)
    assert cuts and v == T.minimax(r)
    A_ = r['kids'][0]
    av = T.minimax(A_)
    ro, bn = ('MAX', 'MIN') if root_max else ('MIN', 'MAX')
    op = 'min' if root_max else 'max'
    n = len(T.leaves(r))
    intro = (P6.fig(vals, root_max, f'Spelträd med {ro} i roten och {bn}-noderna {", ".join(k["name"] for k in r["kids"])}. Löven heter L1–L{n}.')
             + p(sammanhang) + P6.AB)
    a = num('Vilket värde får A?', [step(f'A är en {bn}-nod', f'A = {op}({", ".join(T.fmt(x["leaf"]) for x in A_["kids"])}) = {T.fmt(av)}.')], av,
            f'Väljer {bn} största eller minsta värdet?', 1)
    barnv = [T.minimax(k) for k in r['kids']]
    b = num('Vilket värde får roten?',
            [step('Barnens värden med minimax', ', '.join(f'{k["name"]} = {T.fmt(x)}' for k, x in zip(r['kids'], barnv)) + '.'),
             step(f'{ro} i roten', f'Roten = {"max" if root_max else "min"} av dem = {T.fmt(v)}. Alfa–beta ger samma värde.')], v,
            'Bestäm varje barns värde och välj sedan som roten.', 1)
    fr, rub, txt, alts = begrepp
    c = P6.mc(fr, rub, txt, alts, 'Vad gör alfa–beta jämfört med vanlig minimax?', 1)
    return uppgift(id_, 'alfa_beta', 'Rotvärde och beskurna löv', intro, [a, b, c], 'Rotvärdet räknas som med minimax.', ['procedur', 'begrepp'])


NYA = [t197, t198, t199, t2104, t2105, t2106, t2107, t2108] + [lambda x=x: ab_e(*x) for x in AB_E]


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
    print(f'{len(NYA)} uppgifter inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
