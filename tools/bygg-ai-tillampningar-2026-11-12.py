"""AI-banken 2026-11-12: C-uppgifter med verklighetsförankring (AI-tillämpningar).

Användaren (2026-11-12): fler uppgifter på C-nivå som kopplas till AI-tillämpningar i stället
för abstrakta träd. Tio uppgifter enligt förslagslistan:

1.107 Vänner i flera led (BFS i ett socialt nätverk)       1.108 Räddningsrobot (BFS jämfört med DFS)
2.117 Navigeringsapp (A* hela vägen)                        2.118 Plockrobot i lager (A* jämfört med BFS)
2.119 Leveransdrönare och flygförbudszoner (g, h, f)        2.120 Reseplanerare (girig bäst först jämfört med A*)
2.121 8-pusslet (h = antal brickor på fel plats)            2.122 Triage på en akutmottagning (prioritetskö)
3.79  Luffarschack (minimax, varför blockera)               3.80  Schackdator (alfa–beta, slagdrag först)

Förklaringsfrågorna står som öppna frågor på papper (`t` och huvudfacit `s` utan alternativ) och
som flerval i Kunskapsgymmet, där varje felaktigt alternativ är ett vanligt missförstånd.
Alla svar räknas fram här och kontrolleras oberoende i tools/ai-tillampningar-2026-11-12.test.js.
Kör efter bygg-ai-pafyllnad10-2026-11-12.py och före omgrupperingen.
"""
import importlib.util
import json
import os
import re
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
from ai_figurer import step, maze, weighted_graph, search_tree, tab, game_tree, esc  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, num, val, lista, pil, names = K.p, K.alt, K.num, K.val, K.lista, K.pil, K.names
lst, uppgift, tree_fig = P7.lst, P7.uppgift, P7.tree_fig
B = K.B
BANK = 'uppgifterai.js'
NO = 'Skriv noderna i ordning, åtskilda med kommatecken.'


def falt(fraga, steps, svar_txt, ledtrad, tn, etiketter, varden):
    d = B.part(p(fraga), steps, svar_txt, ledtrad, tn)
    d.update({'svarstyp': 'flera_delar', 'rättSvar': list(varden), 'tolerans': [0] * len(varden), 'självrättning': True,
              'svarFormat': ['numeriskt'] * len(varden), 'svarEnhet': [None] * len(varden), 'svarEtiketter': list(etiketter),
              'svarsstruktur': 'ordnad', 'spel': True})
    return d


def mangd(fraga, steps, svar, ledtrad, tn, suf):
    d = lst(fraga, steps, svar, ledtrad, tn, suf)
    d['svarFormat'] = 'namnmangd'
    return d


def oppen_pa_papper(u, etiketter):
    """Förklaringsfrågor: öppna på papper, flerval bara i Kunskapsgymmet."""
    for e in etiketter:
        m = re.search(rf'<p>{e}\) (.*?) Välj ett alternativ\.</p>((?:<p class="ul-alt">.*?</p>)*)', u['t'])
        assert m, (u['id'], e)
        u['t'] = u['t'][:m.start()] + f'<p>{e}) {m.group(1)}</p>' + u['t'][m.end():]
        start = u['s'].index(f'<span class="facit-mark">{e})</span>')
        slut = u['s'].find('<div class="facit-del">', start)
        slut = len(u['s']) if slut < 0 else slut
        seg = re.sub(r'<ul>(?:<li>.*?</li>)+</ul>', '', u['s'][start:slut])
        u['s'] = u['s'][:start] + seg + u['s'][slut:]
    return u


# ======================================================================== 1.107 vänner i flera led

NAMN107 = {'A': 'Alva', 'B': 'Bo', 'C': 'Cleo', 'D': 'Dani', 'E': 'Elis', 'F': 'Fia', 'G': 'Gus', 'H': 'Hugo', 'I': 'Isa', 'J': 'Jon'}
E107 = [('A', 'C'), ('A', 'D'), ('A', 'E'), ('C', 'F'), ('D', 'F'), ('D', 'G'), ('E', 'H'), ('F', 'I'), ('G', 'I'), ('H', 'J'), ('I', 'B'), ('J', 'B')]
P107 = {'A': (50, 150), 'C': (160, 55), 'D': (160, 150), 'E': (160, 245), 'F': (280, 95), 'G': (280, 190), 'H': (280, 265),
        'I': (400, 135), 'J': (400, 250), 'B': (510, 190)}


def t1107():
    d = P7.graph_dist(E107, 'A')
    tva = sorted(n for n, v in d.items() if v == 2)
    out, path, _ = P7.graph_bfs(E107, 'A', 'B')
    assert tva == ['F', 'G', 'H'] and d['B'] == 4 and path == ['A', 'C', 'F', 'I', 'B']
    intro = (search_tree(P107, E107, 'A', ['B'], 'Vänskapsnätverk med tio personer. Kanter: Alva–Cleo, Alva–Dani, Alva–Elis, Cleo–Fia, '
                         'Dani–Fia, Dani–Gus, Elis–Hugo, Fia–Isa, Gus–Isa, Hugo–Jon, Isa–Bo och Jon–Bo.', 560)
             + p('Ett socialt nätverk lagrar vilka som är vänner. Varje nod är en person: '
                 + ', '.join(f'{k} = {v}' for k, v in NAMN107.items()) + '. En kant betyder att två personer är vänner.')
             + p('Nätverket föreslår ”personer du kanske känner” för Alva: personer som är vänners vänner, alltså två steg bort. '
                 'Det använder BFS från Alva, och grannar tas i bokstavsordning.'))
    a = mangd('Vilka personer ligger exakt två steg från Alva och föreslås därför för henne?',
              [step('Ett steg från Alva', 'Cleo, Dani och Elis (C, D och E).'),
               step('Deras vänner som inte redan är nämnda', 'Fia via Cleo eller Dani, Gus via Dani och Hugo via Elis.')],
              tva, 'Ta först Alvas vänner. Vilka nya personer når man från dem?', 2, 'Skriv bokstäverna, åtskilda med kommatecken.')
    b = num('Hur många steg har den kortaste kedjan av vänskaper från Alva till Bo?',
            [step('Avstånd från Alva', 'C, D, E: 1. F, G, H: 2. I, J: 3. B: 4.')], d['B'], 'Räkna lager för lager från Alva.', 2)
    c = lst('Vilken kedja från Alva till Bo hittar BFS?',
            [step('Den som först upptäcker en person blir dess förälder', 'C upptäcker F före D. F upptäcker I. I tas ut före J och upptäcker B.'),
             step('Följ föräldrarna bakåt från Bo', pil(path) + '.')],
            path, 'Grannarna tas i bokstavsordning. Vem upptäcker Fia först?', 3, 'Skriv bokstäverna i ordning från Alva till Bo.', vag=True)
    e = val('Varför hittar BFS en kortaste kedja från Alva till Bo?',
            [step('BFS undersöker personerna lager för lager', 'Alla som är ett steg bort undersöks före dem som är två steg bort, och så vidare.'),
             step('Första gången Bo nås', 'Då har alla kortare kedjor redan prövats. Därför är kedjan den kortaste.')],
            [alt('Den undersöker alla som är ett steg bort före dem som är två steg bort, och så vidare', True,
                 'Därför når den Bo första gången längs en kortaste kedja.'),
             alt('Den följer alltid vännen med flest egna vänner', False, 'BFS bryr sig inte om hur många vänner någon har.'),
             alt('Den går så djupt som möjligt i nätverket först', False, 'Det är DFS, som kan hitta en lång kedja först.'),
             alt('Den använder en uppskattning av hur långt det är kvar till Bo', False, 'BFS är oinformerad och använder ingen uppskattning.')],
            'Vilken ordning undersöker BFS personerna i?', 3)
    u = uppgift('1.107', 'bfs', 'BFS i träd och grafer', intro, [a, b, c, e], 'BFS undersöker nätverket lager för lager.', ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['d'])


# ======================================================================== 1.108 räddningsrobot

def t1108():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'C': ['E'], 'E': ['F'], 'B': ['G']}
    bout, bpath, _ = P7.tree_bfs(kids, 'S', ['F', 'G'])
    dout, dpath = P7.tree_dfs(kids, 'S', ['F', 'G'])
    assert bout[-1] == 'G' and len(bout) == 6 and dout[-1] == 'F' and len(dout) == 5
    intro = (tree_fig(kids, 'S', ['F', 'G'], 'Rummen i ett rasat hus som ett träd. Entrén S leder till A och B. A leder till C och D, '
                      'C till E och E till F. B leder till G. Röda rum: F och G, där det finns överlevande.')
             + p('En räddningsrobot söker igenom ett rasat hus. Planritningen är förenklad till ett träd: varje nod är ett rum och '
                 'varje kant en dörr. Det finns överlevande i två rum, F och G. Roboten stannar när den hittar en överlevande. '
                 'Dörrarna prövas från vänster till höger.'))
    a = val('Roboten söker med BFS. I vilket rum hittar den en överlevande?',
            [step('BFS undersöker rummen efter avstånd från entrén', 'G ligger två dörrar bort, F fyra. G nås först.')],
            [alt('Rummet G', True, 'G ligger närmast entrén av de två rummen.'),
             alt('Rummet F', False, 'F ligger fyra dörrar bort. Det är rummet DFS hittar.'),
             alt('Rummet E', False, 'E har ingen överlevande.'),
             alt('Båda samtidigt', False, 'Roboten undersöker ett rum i taget och stannar vid första fyndet.')],
            'Vilket av rummen F och G ligger närmast entrén?', 2)
    b = num('Hur många rum undersöker roboten med BFS, inklusive entrén och rummet med den överlevande?',
            [step('BFS-ordningen', lista(bout) + '.'), step('Antal', f'{len(bout)} rum.')], len(bout), 'Ta rummen nivå för nivå.', 2)
    c = num('Roboten söker i stället med DFS. Hur många rum undersöker den, inklusive entrén och rummet med den överlevande?',
            [step('DFS går in i första korridoren', pil(dout) + '. F hittas innan B undersöks.'), step('Antal', f'{len(dout)} rum.')],
            len(dout), 'Följ den vänstra vägen så långt det går.', 2)
    e = val('Roboten ska hitta den överlevande som är närmast entrén, så att räddarna snabbt kommer fram. Vilken sökning passar bäst, och varför?',
            [step('Närmast entrén betyder färst dörrar', 'BFS undersöker rummen i ordning efter avstånd och hittar därför den närmaste först.'),
             step('DFS kan gå långt in först', f'Här hittar DFS rummet F, fyra dörrar bort, trots att G bara är två dörrar bort.')],
            [alt('BFS, eftersom den undersöker rummen i ordning efter avstånd från entrén', True, 'Den hittar alltid den närmaste överlevande först.'),
             alt('DFS, eftersom den undersöker färre rum', False, 'Här undersöker DFS färre rum, men hittar en överlevande längre bort.'),
             alt('DFS, eftersom den alltid hittar den närmaste', False, 'DFS följer en korridor ända in, oavsett hur långt bort fyndet är.'),
             alt('Det spelar ingen roll, båda hittar samma rum', False, 'BFS hittar G och DFS hittar F.')],
            'Vad betyder ”närmast” i trädet, och vilken sökning tar rummen i den ordningen?', 3)
    u = uppgift('1.108', 'dfs', 'DFS i träd och grafer', intro, [a, b, c, e], 'BFS hittar närmaste fyndet, DFS följer en korridor ända in.',
                ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['d'])


# ======================================================================== 2.117 navigeringsapp

G117 = [('S', 'A', 4), ('A', 'M', 8), ('S', 'B', 3), ('B', 'C', 3), ('C', 'M', 3), ('B', 'D', 5), ('D', 'M', 2)]
H117 = {'S': 7, 'A': 5, 'B': 6, 'C': 3, 'D': 2, 'M': 0}
P117 = {'S': (50, 150), 'A': (220, 50), 'M': (470, 110), 'B': (170, 230), 'C': (330, 180), 'D': (330, 270)}


def t2117():
    r = A.astar_graph(G117, H117, 'S', 'M')
    ordning = [n for n, *_ in r['order']]
    assert ordning == ['S', 'A', 'B', 'C', 'M'] and r['cost'] == 9 and r['path'] == ['S', 'B', 'C', 'M']
    for n in H117:
        assert H117[n] <= A.astar_graph(G117, {k: 0 for k in H117}, n, 'M')['cost']
    intro = (weighted_graph(P117, G117, 'S', 'M', 'Stadskarta: S är skolan och M stationen. Gator med restid i minuter: S–A 4, A–M 8, '
                            'S–B 3, B–C 3, C–M 3, B–D 5 och D–M 2. h: S 7, A 5, B 6, C 3, D 2.', 520, h=H117)
             + p('En navigeringsapp ska visa den snabbaste vägen från skolan S till stationen M. Talet vid varje gata är restiden i '
                 'minuter just nu, och den raka gatan A–M är långsam på grund av köer. Talet h vid varje korsning är fågelvägen till '
                 'stationen omräknad till minuter. Appen använder A*. Vid lika f väljs lägst h.'))
    a = falt('Skolan S tas ut och korsningarna A och B läggs in. Bestäm f för A och för B.',
             [step('A: f = g + h', 'g = 4 och h = 5, så f = 9.'), step('B: f = g + h', 'g = 3 och h = 6, så f = 9.')],
             'f(A) = 9, f(B) = 9.', 'g är restiden från skolan, h fågelvägen kvar.', 2, ['f för A', 'f för B'], [9, 9])
    b = val('Vilken korsning tar appen ut efter S?',
            [step('Lika f', 'A och B har båda f = 9.'), step('Lägst h avgör', 'A har h = 5 och B h = 6. A tas ut.')],
            [alt('Korsningen A', True, 'Lika f, men A har lägre h.'), alt('Korsningen B', False, 'B har lika f men högre h, 6 mot 5.'),
             alt('Stationen M', False, 'M har inte lagts in än.'), alt('Korsningen C', False, 'C nås först från B.')],
            'Jämför f, och vid lika f jämför h.', 2)
    c = lst('I vilken ordning tar appen ut korsningarna, från S till och med M?',
            [step('A tas ut', 'M läggs in via A med g = 12 och f = 12.'),
             step('B och C', 'B (f = 9) lägger in C (g = 6, f = 9) och D (g = 8, f = 10). C tas ut och ger M ett bättre värde: g = 9, f = 9.'),
             step('M tas ut', 'M har nu f = 9, lägre än D:s 10.')],
            ordning, 'Uppdatera M:s f när en snabbare väg hittas.', 3, NO)
    d = num('Hur många minuter tar resan som appen föreslår?', [step('Vägen', 'S → B → C → M.'), step('Restid', '3 + 3 + 3 = 9 minuter.')],
            r['cost'], 'Lägg ihop restiderna längs vägen.', 2)
    e = val('Den raka gatan via A ser kortast ut på kartan. Varför föreslår appen ändå inte den?',
            [step('Restid, inte avstånd', 'Via A tar resan 4 + 8 = 12 minuter, via B och C 9 minuter.'),
             step('A* räknar med g', 'f = g + h tar med restiden hittills. Därför väljs den snabbare vägen, även om den ser längre ut.')],
            [alt('Restiden via A är längre, 12 minuter mot 9, och A* räknar med restiden', True, 'Kortast på kartan är inte samma sak som snabbast.'),
             alt('Appen väljer alltid vägen med flest korsningar', False, 'Antalet korsningar spelar ingen roll, bara restiden.'),
             alt('Fågelvägen från A är för lång', False, 'A har tvärtom lägre h än B. Det är restiden A–M som är för lång.'),
             alt('A* undersöker aldrig A', False, 'A undersöks, men M via A får f = 12 och väljs bort.')],
            'Jämför restiden längs de två vägarna.', 3)
    u = uppgift('2.117', 'astar_sokning', 'A* steg för steg', intro, [a, b, c, d, e], 'A* väljer lägst f = g + h.', ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['e'])


# ======================================================================== 2.118 plockrobot i lager

M118 = ['S......', '.##.##.', '.......', '.##.##.', '......G']


def t2118():
    s, g = A.parse(M118)
    ra, rb = A.astar(M118), A.bfs(M118)
    na, nb_, steg = len(ra['order']), len(rb['order']), len(rb['path']) - 1
    assert (na, nb_, steg) == (11, 27, 10)
    intro = (maze(M118, s, g) + p('En plockrobot i ett lager ska hämta en vara vid hyllan G. De mörka rutorna är hyllor. '
                                   'Varje gång roboten tar ut en ruta måste den räkna, så färre uttag sparar tid och batteri. '
                                   'Roboten jämför BFS (ordning ↑ → ↓ ←) med A* (h = Manhattanavstånd). ' + B.ASTAR_TIE))
    a = num('Hur många steg har den kortaste vägen till varan?', [step('Fem rader och sju kolumner', 'Från A1 till E7 krävs minst 4 + 6 = 10 steg, och det finns en väg utan omväg.')],
            steg, 'Kan roboten gå enbart nedåt och åt höger?', 2)
    b = num('Hur många rutor tar BFS ut, inklusive start och mål?', [step('BFS tar ut rutorna efter avstånd', f'Nästan hela lagret undersöks: {nb_} rutor.')],
            nb_, 'Målet ligger längst bort, så nästan alla rutor tas ut först.', 3)
    c = num('Hur många rutor tar A* ut, inklusive start och mål?',
            [step('A* tar ut rutor med lägst f', f'f = 10 för alla rutor på en kortaste väg. Uttagen: {lista(names(ra["order"]))}.'),
             step('Antal', f'{na} rutor.')], na, 'Rutor som leder bort från målet får högre f.', 3)
    e = val('Varför tar A* ut så mycket färre rutor än BFS i lagret?',
            [step('h styr sökningen', 'Rutor som leder bort från varan får högre f och tas aldrig ut.'),
             step('BFS söker åt alla håll', 'BFS vet inte var varan finns och tar ut alla rutor som ligger närmare start än målet.')],
            [alt('h styr A* mot varan, medan BFS söker lika mycket åt alla håll', True, f'A* tar ut {na} rutor, BFS {nb_}.'),
             alt('A* hittar en kortare väg än BFS', False, 'Båda hittar en väg med 10 steg. Skillnaden är antalet uttag.'),
             alt('BFS går in i varje hylla', False, 'BFS går aldrig in i hyllor, men den undersöker alla gångar.'),
             alt('A* går genom hyllorna', False, 'A* följer också gångarna.')],
            'Vad vet A* som BFS inte vet?', 3)
    u = uppgift('2.118', 'astar_sokning', 'A* steg för steg', intro, [a, b, c, e], 'A* använder h för att söka mot målet.', ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['d'])


# ======================================================================== 2.119 leveransdrönare

M119 = ['S..#..', '...#..', '.....G']


def t2119():
    s, g = A.parse(M119)
    P = (0, 4)
    gv, hv, kvar = A.dist_all(M119, s)[P], A.manhattan(P, g), A.dist_all(M119, g)[P]
    assert (gv, hv, kvar, A.manhattan(s, P)) == (8, 3, 3, 4)
    vag = names(A.bfs(M119, goal=P)['path'])
    intro = (maze(M119, s, g, {P: 'P'}, extra_legend=[('#fff3b0', 'Markerad ruta')])
             + p('En leveransdrönare flyger i ett rutnät över en stad. De mörka rutorna är flygförbudszoner, till exempel runt ett '
                 'sjukhus. Drönaren planerar vägen med A*, där g är antalet rutor från start längs tillåtna rutor och h är '
                 'Manhattanavståndet till leveransplatsen.'))
    a = num('Bestäm h för rutan P.', [step('Rader och kolumner till målet', 'P ligger i A5 och målet i C6: 2 + 1 = 3.')], hv,
            'Räkna rader och kolumner. Förbudszonerna räknas inte.', 1)
    b = num('Bestäm g för rutan P.',
            [step('Förbudszonen måste rundas', f'Den kortaste tillåtna vägen är {pil(vag)}.'), step('Antal steg', f'g = {gv}.')], gv,
            'Drönaren får inte flyga genom de mörka rutorna. Var tar zonen slut?', 3)
    c = num('Bestäm f för rutan P.', [step('f = g + h', f'f = {gv} + {hv} = {gv + hv}.')], gv + hv, 'Lägg ihop g och h.', 3)
    e = val('Rakt fram från start till P är det bara 4 rutor, men g = 8. Vad visar det om g jämfört med h?',
            [step('g följer de tillåtna rutorna', 'g är den verkliga vägen hittills. Den måste runda förbudszonen.'),
             step('h räknar rakt', 'h bortser från zonerna. Därför är h en uppskattning, medan g är verklig kostnad.')],
            [alt('g räknar den verkliga vägen runt zonerna, medan h räknar rakt utan att bry sig om dem', True,
                 'Därför kan g bli mycket större än avståndet rakt fram.'),
             alt('g räknas också som Manhattanavstånd', False, 'Då skulle g vara 4. g följer de tillåtna rutorna.'),
             alt('h är den verkliga vägen kvar och g en uppskattning', False, 'Det är tvärtom: g är verklig, h uppskattad.'),
             alt('Drönaren får flyga genom zonerna om det sparar tid', False, 'Förbudszonerna får aldrig passeras.')],
            'Vad mäter g, och vad mäter h?', 3)
    u = uppgift('2.119', 'astar_varden', 'g, h och f för en ruta', intro, [a, b, c, e], 'g följer tillåtna rutor, h räknas rakt.', ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['d'])


# ======================================================================== 2.120 reseplanerare

G120 = [('S', 'A', 6), ('A', 'M', 15), ('S', 'B', 4), ('B', 'C', 4), ('C', 'M', 4)]
H120 = {'S': 8, 'A': 2, 'B': 7, 'C': 3, 'M': 0}
P120 = {'S': (50, 160), 'A': (330, 60), 'M': (470, 160), 'B': (170, 250), 'C': (330, 250)}


def t2120():
    gr = A.greedy_graph(G120, H120, 'S', 'M')
    ast = A.astar_graph(G120, H120, 'S', 'M')
    assert gr['path'] == ['S', 'A', 'M'] and gr['cost'] == 21 and ast['path'] == ['S', 'B', 'C', 'M'] and ast['cost'] == 12
    intro = (weighted_graph(P120, G120, 'S', 'M', 'Hållplatser i kollektivtrafiken: S hemma, M arenan. Restid i minuter inklusive väntan: '
                            'S–A 6, A–M 15, S–B 4, B–C 4, C–M 4. h: S 8, A 2, B 7, C 3.', 520, h=H120)
             + p('En reseplanerare ska hitta en resa hemifrån S till arenan M. Talet vid varje sträcka är restiden i minuter, '
                 'inklusive väntan vid byten. Vid hållplatsen A är väntan lång, så sträckan A–M tar 15 minuter. '
                 'h är fågelvägen till arenan omräknad till minuter. Planeraren prövar både girig bäst först och A*.'))
    a = val('Vilken hållplats väljer girig bäst först efter S?',
            [step('Girig bäst först jämför bara h', 'A har h = 2 och B h = 7. A ligger närmast arenan på kartan.')],
            [alt('Hållplatsen A', True, 'A har lägst h, 2, och ligger närmast arenan på kartan.'), alt('Hållplatsen B', False, 'B har h = 7, högre än A.'),
             alt('Hållplatsen C', False, 'C nås inte direkt från S.'), alt('Arenan M', False, 'M ligger inte direkt bredvid S.')],
            'Jämför h för grannarna till S.', 1)
    b = num('Hur många minuter tar resan som girig bäst först hittar?',
            [step('Vägen', 'S → A → M.'), step('Restid', '6 + 15 = 21 minuter.')], gr['cost'], 'Lägg ihop restiderna.', 2)
    c = num('Hur många minuter tar resan som A* hittar?',
            [step('A* räknar med restiden hittills', 'Via A får M f = 21, via B och C f = 12.'), step('Vägen', 'S → B → C → M: 4 + 4 + 4 = 12 minuter.')],
            ast['cost'], 'Jämför f = g + h för M längs de två vägarna.', 3)
    e = val('Varför blir resan som girig bäst först hittar så mycket längre?',
            [step('Girig bäst först tittar bara på h', 'Den väljer hållplatsen som ligger närmast arenan på kartan.'),
             step('Den långa väntan syns inte i h', 'A* räknar med g och ser att väntan vid A gör resan dyr.')],
            [alt('Den väljer hållplatsen närmast arenan på kartan men räknar inte med den långa väntan vid A', True,
                 'Den bortser från g, alltså restiden hittills.'),
             alt('Den räknar fel på fågelvägen', False, 'Fågelvägen h är rätt. Det är restiden som inte räknas med.'),
             alt('Den väljer alltid den väg som har flest hållplatser', False, 'Den väljer efter h, inte antal hållplatser.'),
             alt('Den letar efter den resa som har färst byten', False, 'Girig bäst först bryr sig inte om byten, bara om h.')],
            'Vad tar girig bäst först inte hänsyn till?', 3)
    u = uppgift('2.120', 'viktade_vagar', 'Billigaste väg i grafer', intro, [a, b, c, e], 'Girig bäst först jämför h, A* jämför g + h.',
                ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['d'])


# ======================================================================== 2.121 8-pusslet

MAL = '12345678_'


def h_fel(b):
    return sum(1 for i, x in enumerate(b) if x != '_' and x != MAL[i])


def drag(b):
    i = b.index('_')
    r, c = divmod(i, 3)
    ut = []
    for namn, (dr, dc) in (('upp', (-1, 0)), ('höger', (0, 1)), ('ned', (1, 0)), ('vänster', (0, -1))):
        rr, cc = r + dr, c + dc
        if 0 <= rr < 3 and 0 <= cc < 3:
            j = rr * 3 + cc
            nb = list(b)
            nb[i], nb[j] = nb[j], nb[i]
            ut.append((namn, ''.join(nb)))
    return ut


def pussel_svg(lagen, titel, per_rad=3):
    """Pusselbrädor i rader om per_rad, så att de går att läsa på mobil."""
    cs, gap, rubrik = 34, 26, 24
    bredd, hojd = 3 * cs + gap, rubrik + 3 * cs + 14
    W = per_rad * bredd + gap
    parts = []
    for k, (namn, b) in enumerate(lagen):
        x0 = gap + (k % per_rad) * bredd
        y0 = (k // per_rad) * hojd
        parts.append(f'<text x="{x0 + 1.5 * cs}" y="{y0 + 18}" text-anchor="middle" font-size="14" font-weight="bold" fill="#111827">{esc(namn)}</text>')
        for i, ch in enumerate(b):
            r, c = divmod(i, 3)
            x, y = x0 + c * cs, y0 + rubrik + r * cs
            fill = '#e5e7eb' if ch == '_' else '#fff'
            parts.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{fill}" stroke="#334155" stroke-width="1.5"/>')
            if ch != '_':
                parts.append(f'<text x="{x + cs / 2}" y="{y + 23}" text-anchor="middle" font-size="18" font-weight="bold" fill="#111827">{ch}</text>')
    H = ((len(lagen) + per_rad - 1) // per_rad) * hojd
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(titel)}" '
            f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(titel)}</title>' + ''.join(parts) + '</svg>')


def t2121():
    start = '1234_6758'
    nya = drag(start)
    h = {namn: h_fel(b) for namn, b in nya}
    assert h_fel(start) == 2 and h == {'upp': 3, 'höger': 3, 'ned': 1, 'vänster': 3}
    lagen = [('Start', start)] + [(f'Läge {i + 1}', b) for i, (_, b) in enumerate(nya)] + [('Mål', MAL)]
    intro = (pussel_svg(lagen, 'Åttapusslet: startläget, de fyra lägen som nås med ett drag och målläget.')
             + p('I åttapusslet flyttar man brickorna en i taget till den tomma rutan, tills de står i ordning 1–8. '
                 'En AI löser pusslet med A*. Varje drag kostar 1, och h är antalet brickor som står på fel plats '
                 '(den tomma rutan räknas inte).')
             + p('Bilden visar startläget och de fyra lägen som nås med ett drag: läge 1 när den tomma rutan flyttas uppåt, '
                 'läge 2 åt höger, läge 3 nedåt och läge 4 åt vänster.'))
    a = num('Bestäm h för startläget.', [step('Jämför med målet bricka för bricka', '5 och 8 står på fel plats. Övriga står rätt.'),
                                         step('h = 2', 'Två brickor står fel.')], 2, 'Jämför varje bricka med målläget.', 1)
    hv = [h[n] for n, _ in nya]
    b = falt('Bestäm h för de fyra lägena 1–4.',
             [step('Räkna brickor på fel plats i varje läge', ', '.join(f'läge {i + 1}: {v}' for i, v in enumerate(hv)) + '.')],
             ', '.join(f'läge {i + 1}: h = {v}' for i, v in enumerate(hv)).capitalize() + '.', 'Jämför varje läge med målläget.', 2, [f'Läge {i + 1}' for i in range(4)], hv)
    bast = min(range(4), key=lambda i: hv[i])
    c = val('Alla fyra lägena har g = 1. Vilket läge undersöker A* först?',
            [step('f = g + h', ', '.join(f'läge {i + 1}: 1 + {v} = {1 + v}' for i, v in enumerate(hv)) + '.'),
             step('Lägst f', f'Läge {bast + 1} har lägst f.')],
            [alt(f'Läge {i + 1}', i == bast, f'Läge {i + 1} har f = {1 + v}' + (', det lägsta.' if i == bast else f', högre än läge {bast + 1}:s {1 + hv[bast]}.'))
             for i, v in enumerate(hv)],
            'Räkna f = g + h för varje läge.', 2)
    e = val('Varför överskattar h aldrig antalet drag som är kvar till målet?',
            [step('Varje felplacerad bricka måste flyttas', 'En bricka på fel plats måste flyttas minst en gång.'),
             step('Ett drag flyttar en bricka', 'Därför behövs minst lika många drag som det finns felplacerade brickor.')],
            [alt('Varje bricka på fel plats måste flyttas minst en gång, och ett drag flyttar bara en bricka', True,
                 'Därför behövs minst h drag, och h överskattar aldrig.'),
             alt('Varje bricka på fel plats kan flyttas rätt med exakt ett drag', False, 'Ofta behövs flera drag för en bricka.'),
             alt('h räknar också den tomma rutan', False, 'Den tomma rutan räknas inte, just för att h inte ska bli för stort.'),
             alt('h överskattar ibland, men A* fungerar ändå', False, 'h överskattar aldrig. Om den gjorde det kunde A* missa den kortaste lösningen.')],
            'Hur många drag behöver en bricka som står fel minst?', 3)
    u = uppgift('2.121', 'astar_varden', 'Heuristiken h', intro, [a, b, c, e], 'h = antalet brickor på fel plats.', ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['d'])


# ======================================================================== 2.122 triage

PATIENTER = [('A', 0, 2), ('B', 2, 3), ('C', 6, 1), ('D', 14, 2), ('E', 19, 1), ('F', 27, 2), ('G', 35, 1)]


def triage(pat, tid=10):
    vantar, ordning, t, start = [], [], 0, {}
    kvar = sorted(pat, key=lambda x: x[1])
    while kvar or vantar:
        vantar += [x for x in kvar if x[1] <= t]
        kvar = [x for x in kvar if x[1] > t]
        if not vantar:
            t = kvar[0][1]
            continue
        vantar.sort(key=lambda x: (x[2], x[1]))
        x = vantar.pop(0)
        ordning.append(x[0])
        start[x[0]] = t
        t += tid
    return ordning, start


def klocka(m):
    return f'08.{m:02d}' if m < 60 else f'09.{m - 60:02d}'


def t2122():
    ordning, start = triage(PATIENTER)
    vantan_b = start['B'] - 2
    assert ordning == list('ACEDGFB') and vantan_b == 58
    intro = (p('På en akutmottagning finns en läkare. Varje patient får en prioritet när den kommer in, där 1 är mest akut. '
               'När läkaren blir ledig tas den väntande patient som har lägst prioritetssiffra. Vid samma prioritet tas den som '
               'kom först. Varje besök tar 10 minuter, och läkaren börjar klockan 08.00.')
             + tab(['Patient', 'Kommer in', 'Prioritet'], [[n, klocka(t), str(pr)] for n, t, pr in PATIENTER]))
    rader = [[n, klocka(start[n])] for n in ordning]
    a = lst('I vilken ordning träffar patienterna läkaren?',
            [step('Vid varje ledig tid: lägst prioritetssiffra bland dem som väntar', tab(['Patient', 'Börjar'], rader))],
            ordning, 'Skriv upp vilka som väntar varje gång läkaren blir ledig, alltså 08.00, 08.10, 08.20 och så vidare.', 3,
            'Skriv bokstäverna i ordning, åtskilda med kommatecken.')
    b = num('Hur många minuter får patient B vänta från att hon kommer in tills hon träffar läkaren?',
            [step('B kommer in 08.02', f'B träffar läkaren {klocka(start["B"])}, som sista patient.'),
             step('Väntetid', f'{start["B"]} − 2 = {vantan_b} minuter.')], vantan_b, 'När blir B den väntande patient som har lägst siffra?', 3)
    c = val('Varför får B vänta så länge?',
            [step('Prioritetskön tar lägst siffra', 'B har prioritet 3. Hela tiden kommer nya patienter med prioritet 1 eller 2.'),
             step('B går aldrig före', 'Så länge någon med högre prioritet väntar, tas B inte.')],
            [alt('Nya patienter med mer akut prioritet kommer hela tiden och går före', True, 'En prioritetskö tar alltid lägst siffra först.'),
             alt('B kom in sist', False, 'B kom in redan 08.02, som andra patient.'),
             alt('Läkaren tar patienterna i bokstavsordning', False, 'Ordningen styrs av prioriteten, sedan av ankomsttiden.'),
             alt('B:s besök tar längre tid', False, 'Alla besök tar 10 minuter.')],
            'Vilka patienter väntar samtidigt som B?', 3)
    d = val('Vilken ändring av regeln minskar risken att en patient med låg prioritet får vänta mycket länge?',
            [step('Problemet', 'En prioritetskö kan låta samma patient vänta hur länge som helst om nya patienter hela tiden går före.'),
             step('En lösning', 'Låt prioriteten bli mer akut ju längre patienten har väntat. Då kommer alla till slut fram.')],
            [alt('Låt prioriteten bli mer akut ju längre patienten har väntat', True, 'Då kommer även patienter med låg prioritet fram till slut.'),
             alt('Ta alltid den patient som kom först, oavsett prioritet', False, 'Då kan akuta patienter få vänta, vilket är farligt.'),
             alt('Låt läkaren välja patient slumpmässigt', False, 'Slumpen tar inte hänsyn till hur akut någon är.'),
             alt('Ge alla patienter prioritet 1', False, 'Då försvinner hela poängen med prioriteringen.')],
            'Hur kan väntetiden räknas in i prioriteten?', 4)
    u = uppgift('2.122', 'prioritetsko', 'Uttag ur en prioritetskö', intro, [a, b, c, d], 'Vid varje ledig tid tas lägst prioritetssiffra.',
                ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['c', 'd'])


# ======================================================================== 3.79 luffarschack

BRADE = 'X..X.OOXO'
LINJER = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def vinst(b):
    for x, y, z in LINJER:
        if b[x] != '.' and b[x] == b[y] == b[z]:
            return b[x]
    return None


def spelträd(b, tur):
    """Nästlad lista för T.build: barn i ordning efter tomma rutor; löv = +1, 0 eller −1."""
    w = vinst(b)
    if w:
        return 1 if w == 'X' else -1
    if '.' not in b:
        return 0
    nasta = 'O' if tur == 'X' else 'X'
    return [spelträd(b[:i] + tur + b[i + 1:], nasta) for i, c in enumerate(b) if c == '.']


def brade_svg(b, etiketter, titel):
    cs, x0, y0 = 56, 10, 10
    parts = []
    for i, ch in enumerate(b):
        r, c = divmod(i, 3)
        x, y = x0 + c * cs, y0 + r * cs
        parts.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#fff" stroke="#334155" stroke-width="2"/>')
        if ch in 'XO':
            färg = '#1d4ed8' if ch == 'X' else '#b91c1c'
            parts.append(f'<text x="{x + cs / 2}" y="{y + 39}" text-anchor="middle" font-size="32" font-weight="bold" fill="{färg}">{ch}</text>')
        elif i in etiketter:
            parts.append(f'<text x="{x + cs / 2}" y="{y + 36}" text-anchor="middle" font-size="22" fill="#6b7280">{etiketter[i]}</text>')
    W = H = 2 * x0 + 3 * cs
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(titel)}" '
            f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(titel)}</title>' + ''.join(parts) + '</svg>')


def t379():
    tomma = [i for i, c in enumerate(BRADE) if c == '.']
    etiketter = dict(zip(tomma, 'ABC'))
    tree = spelträd(BRADE, 'X')
    r = T.build(tree, True)
    varden = {k['name']: T.minimax(k) for k in r['kids']}
    assert varden == {'A': -1, 'B': 0, 'C': -1} and T.minimax(r) == 0
    assert vinst(BRADE[:2] + 'O' + BRADE[3:]) == 'O'  # O hotar att vinna i ruta B
    intro = (brade_svg(BRADE, etiketter, 'Luffarschack: X i övre vänstra, mellersta vänstra och nedre mittersta rutan. O i mellersta '
                       'högra, nedre vänstra och nedre högra rutan. Tomma rutor: A, B och C.')
             + p('En dator spelar luffarschack som X mot en människa som spelar O. Det är datorns tur. De tomma rutorna heter A, B och C. '
                 'Datorn räknar igenom alla möjliga fortsättningar med minimax. Ett slutläge får värdet +1 om X vinner, 0 vid oavgjort '
                 'och −1 om O vinner.')
             + P6.fig(tree, True, 'Spelträd för de tre tomma rutorna. Roten är datorns drag, nästa nivå människans och sist datorns igen.', spacing=80))
    a = num('Vilket värde får noden A, alltså draget där X lägger i ruta A?',
            [step('Efter X i A har O två val', 'O i B ger tre O i högra kolumnen, så O vinner: −1.'),
             step('A är en MIN-nod', 'O väljer det sämsta för X, alltså −1.')], varden['A'], 'Kan O vinna direkt efter draget?', 2)
    b = val('Vilket drag väljer datorn?',
            [step('Värdena', ', '.join(f'{k} = {v:+d}'.replace('+0', '0').replace('-', '−') for k, v in varden.items()) + '.'),
             step('MAX tar högst', 'B har högst värde, 0.')],
            [alt(f'Draget till {k}', k == 'B', f'{k} har värdet {v:+d}'.replace('+0', '0').replace('-', '−') +
                 ('. Det är det högsta, eftersom det stoppar O.' if k == 'B' else '. O kan då vinna.')) for k, v in varden.items()],
            'Vilken nod har högst värde?', 2)
    c = val('Datorn väljer ett drag som bara leder till oavgjort, värdet 0. Varför försöker den inte vinna i stället?',
            [step('O hotar att vinna', 'O har två i den högra kolumnen. Om X inte lägger i B vinner O direkt.'),
             step('Minimax räknar med bästa motspel', 'Med A eller C kan O vinna. Bästa X kan garantera är oavgjort.')],
            [alt('Med de andra dragen kan O vinna direkt, och minimax räknar med att O spelar sitt bästa drag', True,
                 'Att blockera ger 0, de andra dragen ger −1.'),
             alt('Datorn vill hellre spela oavgjort än vinna', False, 'Minimax väljer +1 om det finns. Här finns inget drag som garanterar vinst.'),
             alt('Datorn räknar bara ett drag framåt', False, 'Datorn räknar igenom alla fortsättningar till spelets slut.'),
             alt('Ruta B ger flest egna möjligheter att vinna', False, 'B ger ingen egen vinst. Den stoppar O:s vinst.')],
            'Vad händer om datorn inte lägger i B?', 3)
    u = uppgift('3.79', 'minimax', 'Tolka och resonera om minimax', intro, [a, b, c], 'Minimax räknar med att motspelaren spelar sitt bästa drag.',
                ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['c'])


# ======================================================================== 3.80 schackdator

VALS380 = [[3, 5], [1, 4], [2, 0, 6]]


def t380():
    r = T.build(VALS380, True)
    v, ev, cuts, notes = T.alphabeta(r)
    assert v == 3 and ev == ['L1', 'L2', 'L3', 'L5'] and T.pruned_leaves(cuts) == ['L4', 'L6', 'L7']
    omv = [VALS380[1], VALS380[2], VALS380[0]]
    v2, ev2, _, _ = T.alphabeta(T.build(omv, True))
    assert v2 == 3 and len(ev2) == 6
    intro = (P6.fig(VALS380, True, 'Spelträd: MAX i roten med dragen A, B och C. A har svaren 3 och 5, B har 1 och 4, C har 2, 0 och 6. '
                    'Löven heter L1–L7.')
             + p('En schackdator har tidsgräns och måste välja drag snabbt. Den har tre drag att välja mellan: A slår ett torn, '
                 'B flyttar kungen och C flyttar en bonde. Talen i löven är datorns bedömning av läget efter motståndarens svar '
                 '(högt är bra för datorn). Datorn söker med alfa–beta-beskärning och undersöker dragen i ordningen A, B, C.'))
    a = num('Vilket värde får draget A?', [step('A är en MIN-nod', 'Motståndaren väljer det sämsta för datorn: min(3, 5) = 3.')], 3,
            'Motståndaren väljer det svar som är sämst för datorn.', 1)
    b = val('Datorn vet att A ger 3. B:s första svar ger 1. Behöver datorn bedöma B:s andra svar, L4?',
            [step('B blir högst 1', 'Motståndaren kan alltid välja svaret som ger 1.'), step('Jämför med A = 3', 'B kan aldrig bli bättre än A, så L4 hoppas över.')],
            [alt('Nej, B kan aldrig bli bättre än A', True, 'B blir högst 1, och A ger redan 3.'),
             alt('Ja, L4 = 4 är bättre än 3', False, 'Motståndaren väljer inte 4 när 1 finns. B blir högst 1.'),
             alt('Ja, alla svar måste alltid bedömas', False, 'Det gäller vanlig minimax, inte alfa–beta.'),
             alt('Nej, eftersom B är ett kungsdrag', False, 'Vilket slags drag det är spelar ingen roll, bara värdena.')],
            'Vad är det bästa B kan ge datorn?', 3)
    c = num('Hur många av C:s tre svar behöver datorn bedöma?',
            [step('C:s första svar ger 2', 'C blir högst 2, sämre än A = 3.'), step('Resten hoppas över', '1 av 3 svar bedöms.')], 1,
            'Jämför C:s första svar med A.', 3)
    d = num('Datorn undersöker i stället dragen i ordningen B, C, A. Hur många slutlägen bedöms totalt?',
            [step('B först', 'B: 1 och 4 bedöms, B = 1.'), step('C', 'C: 2 är bättre än 1, så nästa svar bedöms. 0 ≤ 1, resten hoppas över. Två bedömningar.'),
             step('A sist', 'A: 3 och 5 bedöms. Totalt 2 + 2 + 2 = 6.')], len(ev2), 'Följ alfa–beta från vänster i den nya ordningen.', 4)
    e = val('I ordningen A, B, C bedöms 4 slutlägen, i ordningen B, C, A 6. Varför undersöker schackprogram ofta slagdrag först?',
            [step('Bra drag tidigt', 'Slagdrag är ofta bra. Då får roten tidigt ett högt värde att jämföra med.'),
             step('Fler grenar kan beskäras', 'Varje nytt drag som inte kan slå det värdet avbryts tidigt.')],
            [alt('Bra drag tidigt ger ett högt värde att jämföra med, så fler grenar kan beskäras', True,
                 'Här sparar ordningen A, B, C två bedömningar.'),
             alt('Slagdrag är alltid det bästa draget', False, 'Ett slagdrag kan vara dåligt. Det är ordningen som sparar tid.'),
             alt('Ordningen ändrar vilket drag datorn väljer', False, 'Datorn väljer samma drag, A, i båda ordningarna.'),
             alt('Beskärning fungerar bara för slagdrag', False, 'Beskärning fungerar för alla drag.')],
            'Jämför antalet bedömningar i de två ordningarna.', 3)
    u = uppgift('3.80', 'alfa_beta', 'Beskärningens idé', intro, [a, b, c, d, e], 'Bra drag först ger mer beskärning.', ['procedur', 'resonemang'])
    return oppen_pa_papper(u, ['e'])


NYA = [t1107, t1108, t2117, t2118, t2119, t2120, t2121, t2122, t379, t380]


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
    print(f'{len(NYA)} tillämpningsuppgifter inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
