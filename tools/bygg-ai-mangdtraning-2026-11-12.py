"""AI-banken 2026-11-12: mängdträning i alla områden.

Användarbeslut 2026-11-12: ”Det är bra med lite mängdträning också, så det behöver inte
vara helt olika, utan variera labyrinter/träd och siffror.” 44 uppgifter som följer
beprövade mallar men har nya labyrinter, träd, tal och sammanhang:

- Köer och stackar 1.77–1.82, BFS i labyrinter 1.83–1.86, DFS i labyrinter 1.87–1.90,
  BFS i träd 1.91–1.93, DFS i träd 1.94–1.96.
- Prioritetsköer 2.88–2.91, g/h/f för en ruta 2.92–2.95, A*:s första steg 2.96–2.99,
  vägkostnad i labyrinter 2.100–2.103.
- Minimax 3.62–3.65, beskärning med stöd 3.66–3.69.

Labyrinter, träd och tal slumpas med fasta frön, och varje uppgift måste uppfylla villkor
(nåbart mål, lagom lång väg, entydigt svar, inga lika värden utan regel). Rubrikerna i
facit beskriver vad som händer i just den uppgiften, med uppgiftens rutor och tal.
Mallarna bfs_task, dfs_task, ghf_task och mm_kg kommer från tidigare omgångar.

Svaren kontrolleras oberoende i tools/ai-mangdtraning-2026-11-12.test.js.
Kör efter bygg-ai-pafyllnad8-2026-11-11.py och före bygg-ai-omgruppering-2026-11-11.py.
"""
import importlib.util
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _load(name, fil):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fil))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = _load('ai_kg', 'bygg-ai-kunskapsgymmet-2026-11-11.py')
P4 = _load('ai_p4', 'bygg-ai-pafyllnad4-2026-11-11.py')
P6 = _load('ai_p6', 'bygg-ai-pafyllnad6-2026-11-11.py')
P7 = _load('ai_p7', 'bygg-ai-pafyllnad7-2026-11-11.py')
from ai_figurer import step, maze, box_queue, box_stack, tab  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, num, val, lista, pil, names, ORD = K.p, K.alt, K.num, K.val, K.lista, K.pil, K.names, K.ORD
lst, uppgift, tree_fig, tree_bfs, tree_dfs = P7.lst, P7.uppgift, P7.tree_fig, P7.tree_bfs, P7.tree_dfs
BANK = 'uppgifterai.js'
NO = 'Skriv noderna i ordning, åtskilda med kommatecken.'

SAMMANHANG = [
    'En robotdammsugare letar efter sin laddstation.', 'En mus letar efter osten i en labyrint.',
    'En leveransrobot ska hitta fram till en hylla i ett lager.', 'En figur i ett datorspel ska ta sig till utgången.',
    'En räddningsrobot söker igenom ett rasat hus.', 'En gräsklipparrobot ska tillbaka till sin station.',
    'En drönare flyger mellan hyllorna i ett lager.', 'En spelfigur letar efter en skattkista.',
]


# ---------------------------------------------------------------- generatorer

def labyrint(rng, R, C, tathet, minvag):
    """Slumpad labyrint: start i vänster kolumn, mål i höger kolumn, nåbart med minst minvag steg."""
    while True:
        g = [['#' if rng.random() < tathet else '.' for _ in range(C)] for _ in range(R)]
        s, m = (rng.randrange(R), 0), (rng.randrange(R), C - 1)
        g[s[0]][s[1]], g[m[0]][m[1]] = 'S', 'G'
        rows = [''.join(r) for r in g]
        d = A.dist_all(rows, s)
        if m in d and d[m] >= minvag:
            return rows


def med_terrang(rng, rows, n):
    """Byt n öppna rutor (inte start eller mål) mot lera, som kostar 3."""
    oppna = [(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == '.']
    g = [list(r) for r in rows]
    for r, c in rng.sample(oppna, n):
        g[r][c] = '3'
    return [''.join(r) for r in g]


def slumptrad(rng, n_min, n_max):
    """Sökträd med S överst och bokstäverna A, B, … i bredd-först-ordning. Målet är ett löv på djup 2–3."""
    while True:
        kids, nivaer, namn = {}, [['S']], iter('ABCDEFGHIJKMNOPQ')
        for djup in range(3):
            ny = []
            for n in nivaer[-1]:
                k = rng.choice([0, 1, 2, 2, 3]) if djup < 2 else rng.choice([0, 0, 1, 2])
                if djup == 0:
                    k = max(k, 2)
                barn = [next(namn) for _ in range(k)]
                if barn:
                    kids[n] = barn
                ny += barn
            nivaer.append(ny)
        alla = [x for niv in nivaer for x in niv]
        lov = [x for niv in nivaer[2:] for x in niv if x not in kids]
        if n_min <= len(alla) <= n_max and lov:
            return kids, rng.choice(lov)


def sok_fram(seed, bygg, villkor):
    rng = random.Random(seed)
    for _ in range(5000):
        x = bygg(rng)
        if villkor(x):
            return x
    raise RuntimeError(f'inget fall för frö {seed}')


# ======================================================================== köer och stackar

KO_SAMMANHANG = ['Utskrifterna till en skrivare väntar i en FIFO-kö.', 'Kunderna vid en kassa står i en FIFO-kö.',
                 'Meddelanden till en server hamnar i en FIFO-kö.']
STACK_SAMMANHANG = ['Ångra-stegen i ett ritprogram sparas i en stack.', 'Lådorna i ett staplat förråd bildar en stack.',
                    'Sidorna som bakåtknappen i en webbläsare går tillbaka till sparas i en stack.']


def ko_stack_task(id_, seed, stack, sammanhang):
    def bygg(rng):
        bokst = rng.sample('ABCDEFGHJKMNPQSTUVWXYZ', 6)
        start, nya = bokst[:3], bokst[3:]
        ops, i = [], 0
        for _ in range(rng.choice([5, 6])):
            if (rng.random() < 0.5 and i < len(nya)) or not ops:
                ops.append(nya[i])
                i += 1
            else:
                ops.append(None)
        return start, ops

    def kor(x):
        start, ops = x
        s, ut = list(start), []
        for o in ops:
            if o:
                s.append(o)
            elif s:
                ut.append(s.pop() if stack else s.pop(0))
            else:
                return None
        return ut, s

    def villkor(x):
        r = kor(x)
        return r and 2 <= len(r[0]) <= 3 and len(r[1]) >= 2 and sum(1 for o in x[1] if o) >= 2

    start, ops = sok_fram(seed, bygg, villkor)
    ut, kvar = kor((start, ops))
    stegtext = ' → '.join(f'lägg in {o}' if o else 'ta ut en nod' for o in ops)
    figur = box_stack(start, f'Stack med {", ".join(start)} nerifrån och upp.') if stack else \
        box_queue(start, f'FIFO-kö med {", ".join(start)}, där {start[0]} står först.')
    struktur = 'stacken' if stack else 'kön'
    intro = figur + p(sammanhang + (' Bilden visar stacken just nu, med den översta noden överst.' if stack else
                                    ' Bilden visar kön just nu, med den nod som tas ut först längst till vänster.')) + \
        p(f'Sedan görs följande steg: {stegtext}.')
    # Facit: läget efter varje steg
    s, rader = list(start), []
    for o in ops:
        if o:
            s.append(o)
            rader.append([f'Lägg in {o}', ', '.join(s)])
        else:
            x = s.pop() if stack else s.pop(0)
            rader.append([f'Ta ut ({x})', ', '.join(s) or 'tom'])
    rubr = 'Stacken nerifrån och upp' if stack else 'Kön, först till vänster'
    a = lst('I vilken ordning tas noderna ut?',
            [step(f'{"Den översta noden tas ut" if stack else "Den nod som står först tas ut"} vid varje uttag',
                  tab(['Steg', rubr], rader))],
            ut, 'Skriv upp ' + struktur + ' efter varje steg.', 1, NO)
    sista = kvar[-1] if stack else kvar[0]
    fraga_b = 'Vilken nod ligger överst i stacken när stegen är gjorda?' if stack else 'Vilken nod står först i kön när stegen är gjorda?'
    andra = [x for x in start + [o for o in ops if o] if x != sista]
    rng = random.Random(seed + 1)
    distr = rng.sample(andra, 3)

    def kommentar(x):
        if x == sista:
            return f'{x} ligger {"överst" if stack else "först"} bland noderna som är kvar: {", ".join(kvar)}.'
        if x in ut:
            return f'{x} har redan tagits ut och finns inte kvar i {struktur}.'
        return f'{x} finns kvar, men {"under " + sista if stack else "efter " + sista}.'
    b = val(fraga_b, [step(f'Kvar i {struktur}', ', '.join(kvar) + (' (nerifrån och upp).' if stack else ' (först till vänster).'))],
            [alt(f'Noden {x}', x == sista, kommentar(x)) for x in sorted([sista] + distr)],
            'Vilka noder är kvar efter alla steg?', 1)
    return uppgift(id_, 'ko_stack', 'Kö och stack steg för steg', intro, [a, b],
                   'I en stack tas den senast inlagda noden ut först.' if stack else 'I en FIFO-kö tas den äldsta noden ut först.', ['procedur'])


# ======================================================================== BFS och DFS

def maze_villkor_bfs(k, avst):
    def ok(rows):
        r = A.bfs(rows)
        d = A.dist_all(rows, A.parse(rows)[0])
        return len(r['order']) >= k + 2 and 2 <= sum(1 for v in d.values() if v == avst) <= 4
    return ok


def bfs_drill(id_, seed, k, avst, fragor, tn, sammanhang, R=4, C=6):
    rows = sok_fram(seed, lambda rng: labyrint(rng, R, C, 0.28, C), maze_villkor_bfs(k, avst))
    q = [f if f != 'avst' else f'avst{avst}' for f in fragor]
    u = K.bfs_task(id_, 'BFS i labyrinter', rows, k, q, 'Skriv upp kön efter varje uttag. Nya rutor läggs längst bak.', tn)
    return P4.med_sammanhang(u, sammanhang)


def dfs_drill(id_, seed, k, sammanhang, R=4, C=6):
    def ok(rows):
        r = A.dfs(rows)
        return len(r['order']) >= k + 2
    rows = sok_fram(seed, lambda rng: labyrint(rng, R, C, 0.3, C), ok)
    u = K.dfs_task(id_, 'DFS i labyrinter', rows, k, 'DFS fortsätter alltid från den senast besökta rutan och backar vid stopp.')
    return P4.med_sammanhang(u, sammanhang)


TRAD_SAMMANHANG = ['Trädet visar vilka rum i ett museum som leder vidare till vilka.',
                   'Trädet visar hur mapparna på ett USB-minne ligger i varandra.',
                   'Trädet visar vilka lägen ett pussel kan nå från startläget.']


def trad_drill(id_, seed, dfs, sammanhang):
    def ok(x):
        kids, mal = x
        o = (tree_dfs if dfs else tree_bfs)(kids, 'S', [mal])[0]
        return 5 <= len(o) <= 9
    kids, mal = sok_fram(seed, lambda rng: slumptrad(rng, 9, 13), ok)
    alla = ['S'] + [k for v in kids.values() for k in v]
    beskr = ', '.join(f'{n} har {" och ".join(", ".join(v).rsplit(", ", 1))}' for n, v in kids.items())
    alg = 'DFS' if dfs else 'BFS'
    intro = tree_fig(kids, 'S', [mal], f'Sökträd med S överst. {beskr}. Målet är {mal}.') + \
        p(f'{sammanhang} Trädet söks igenom med {alg} (vänster gren först), och sökningen stoppar när {mal} hittas.')
    if dfs:
        ordning, vag = tree_dfs(kids, 'S', [mal])
        a = lst('I vilken ordning besöks noderna, fram till och med målet?',
                [step('DFS går ned längs grenen längst till vänster', f'Den första grenen: {pil(ordning[:3])} …'),
                 step('Backa vid noder utan obesökta barn', f'Hela besöksordningen: {lista(ordning)}.')],
                ordning, 'Gå så djupt som möjligt till vänster. Backa när en nod saknar obesökta barn.', 2, NO)
        b_txt, b_steg = 'Hur många noder besöks aldrig?', 'besöks'
    else:
        ordning, vag, _ = tree_bfs(kids, 'S', [mal])
        a = lst('I vilken ordning tas noderna ut ur kön, fram till och med målet?',
                [step('S och sedan S:s barn', f'S tas ut först, sedan {lista(kids["S"])}.'),
                 step('Nivå för nivå, från vänster till höger', f'Hela uttagsordningen: {lista(ordning)}.')],
                ordning, 'Ta alla noder på en nivå innan du går vidare till nästa nivå.', 2, NO)
        b_txt, b_steg = 'Hur många noder tas aldrig ut?', 'tas ut'
    aldrig = [n for n in alla if n not in ordning]
    b = num(b_txt, [step(f'Trädet har {len(alla)} noder', f'{len(ordning)} av dem {b_steg} innan sökningen stoppar.'),
                    step('Resten', (f'{lista(aldrig)}: ' if aldrig else '') + f'{len(aldrig)} noder.')],
            len(aldrig), 'Räkna alla noder i trädet och dra bort dem som hinner undersökas.', 2)
    c = lst('Vilken väg till målet hittar sökningen?',
            [step('Följ trädet från målet upp till S', f'{pil(vag)}.')], vag,
            f'Vilken nod ligger direkt ovanför {mal}?', 1, 'Skriv noderna längs vägen, från start till mål.', vag=True)
    omr, fam = ('dfs', 'DFS i träd och grafer') if dfs else ('bfs', 'BFS i träd och grafer')
    return uppgift(id_, omr, fam, intro, [a, b, c], f'{alg} {"följer en gren ända ned" if dfs else "tar en nivå i taget"}.', ['procedur'])


# ======================================================================== prioritetsköer

PRIO_SAMMANHANG = ['Ett tvätteri tvättar först den beställning som ska vara klar tidigast. Talet är antal dagar kvar.',
                   'En tandläkare tar först den patient som har mest bråttom. Lägst tal betyder mest bråttom.',
                   'En robot laddar först det batteri som har minst laddning kvar. Talet är laddningen i tiondelar.',
                   'Patienterna på en vårdcentral sorteras efter prioritet, där 1 är mest bråttom.']


def prio_task(id_, seed, sammanhang):
    def bygg(rng):
        bokst = rng.sample('ABCDEFGHJKMNPQSTUVWXYZ', 6)
        ops = [(bokst[0], rng.randint(1, 9)), (bokst[1], rng.randint(1, 9)), (bokst[2], rng.randint(1, 9)), None,
               (bokst[3], rng.randint(1, 9)), (bokst[4], rng.randint(1, 9)), None, None]
        return ops

    def kor(ops):
        q, out = [], []
        for o in ops:
            if o:
                q.append(o)
            else:
                q.sort(key=lambda x: (x[1], x[0]))
                out.append(q.pop(0))
        return out, q

    def ok(ops):
        out, q = kor(ops)
        vals = [o[1] for o in ops if o]
        return len(set(vals)) == len(vals) and len(q) == 2
    ops = sok_fram(seed, bygg, ok)
    out, kvar = kor(ops)
    steg = ' → '.join(f'lägg in {o[0]}({o[1]})' if o else 'ta ut en nod' for o in ops)
    intro = p(sammanhang + ' Det fungerar som en prioritetskö där lägst värde tas ut först.') + \
        p(f'Talet inom parentes är värdet. Stegen: {steg}.')
    q, rader = [], []
    for o in ops:
        if o:
            q.append(o)
        else:
            q.sort(key=lambda x: (x[1], x[0]))
            x = q.pop(0)
            rader.append([f'{x[0]}({x[1]})', ', '.join(f'{n}({v})' for n, v in sorted(q, key=lambda y: y[1])) or 'tom'])
    a = lst('I vilken ordning tas de tre noderna ut?',
            [step('Lägst värde vid varje uttag', tab(['Tas ut', 'Kvar i kön'], rader))], [n for n, _ in out],
            'Vid varje uttag: leta upp lägst värde bland noderna som finns i kön just då.', 1, NO)
    b = num('Vilket värde har den nod som tas ut sist?', [step('Tredje uttaget', f'{out[2][0]} har värdet {out[2][1]}.')], out[2][1],
            'Vilken nod tas ut vid det tredje uttaget?', 1)
    c = num('Vilket är det lägsta värdet bland noderna som är kvar efter alla steg?',
            [step('Kvar i kön', ', '.join(f'{n}({v})' for n, v in kvar) + f'. Lägst är {min(v for _, v in kvar)}.')],
            min(v for _, v in kvar), 'Vilka två noder har inte tagits ut?', 1)
    return uppgift(id_, 'prioritetsko', 'Uttag ur en prioritetskö', intro, [a, b, c], 'Prioritetskön tar alltid ut lägst värde.', ['procedur'])


# ======================================================================== g, h och f

def ghf_drill(id_, seed, sammanhang):
    """Markerad ruta P som nås längs en rak väg utan omväg: g = Manhattanavståndet från start (E-nivå)."""
    def bygg(rng):
        rows = labyrint(rng, 5, 6, 0.25, 6)
        s, g = A.parse(rows)
        d = A.dist_all(rows, s)
        kand = [c for c, v in d.items() if v == A.manhattan(s, c) and 2 <= v <= 5 and A.manhattan(c, g) >= 2]
        return rows, (rng.choice(kand) if kand else None)
    rows, mark = sok_fram(seed, bygg, lambda x: x[1] is not None)
    u = K.ghf_task(id_, 'g, h och f för en ruta', rows, mark, 'g räknas längs gångarna från start, h rakt till målet.')
    return P4.med_sammanhang(u, sammanhang)


# ======================================================================== A*:s första steg

def astar_e_task(id_, seed, sammanhang):
    def bygg(rng):
        return labyrint(rng, 4, 6, 0.28, 6)

    def ok(rows):
        s, g = A.parse(rows)
        nb = A.neigh(rows, s)
        f = sorted(1 + A.manhattan(v, g) for v in nb)
        return len(nb) >= 2 and f[0] < f[1]
    rows = sok_fram(seed, bygg, ok)
    s, g = A.parse(rows)
    nb = sorted(A.neigh(rows, s), key=A.cname)
    f = {A.cname(v): 1 + A.manhattan(v, g) for v in nb}
    h = {A.cname(v): A.manhattan(v, g) for v in nb}
    basta = min(f, key=f.get)
    vag = A.bfs(rows)['path']
    intro = maze(rows, s, g) + p(sammanhang) + p(K.ASTAR)
    sn = A.cname(s)
    falt = [(f'f för {n}', f[n]) for n in f]
    d_a = K.B.part(p(f'Start ligger i {sn}. Bestäm f = g + h för var och en av grannarna {" och ".join(", ".join(f).rsplit(", ", 1))}.'),
                   [step('Grannarna ligger ett steg från start', 'Därför har alla g = 1.'),
                    step('h = radskillnad + kolumnskillnad till målet ' + A.cname(g),
                         ' '.join(f'{n}: 1 + {h[n]} = {f[n]}.' for n in f))],
                   ', '.join(f'f({n}) = {v}' for n, v in falt) + '.', 'g är antalet steg från start, h räknas rakt till målet.', 2)
    d_a.update({'svarstyp': 'flera_delar', 'rättSvar': [v for _, v in falt], 'tolerans': [0] * len(falt), 'självrättning': True,
                'svarFormat': ['numeriskt'] * len(falt), 'svarEnhet': [None] * len(falt), 'svarEtiketter': [e for e, _ in falt],
                'svarsstruktur': 'ordnad', 'spel': True})
    b = val('Vilken ruta tar A* ut ur öppna listan efter start?',
            [step('Lägst f vinner', ', '.join(f'{n} har f = {f[n]}' for n in f) + f'. {basta} har lägst f.')],
            [alt(f'Rutan {n}', n == basta, f'{n} har f = {f[n]}' + (', det lägsta.' if n == basta else f', högre än {basta}:s {f[basta]}.'))
             for n in f] + [alt(f'Rutan {A.cname(g)}', False, 'Målet ligger inte bredvid start och kan inte tas ut redan nu.')],
            'Jämför f för grannarna.', 2)
    c = num('Hur många steg har vägen som A* hittar?',
            [step('A* hittar en kortaste väg här', 'Alla steg kostar 1 och h överskattar aldrig.'),
             step('En kortaste väg', f'{pil(names(vag))}: {len(vag) - 1} steg.')], len(vag) - 1,
            'Räkna stegen längs den kortaste vägen genom gångarna.', 2)
    return uppgift(id_, 'astar_sokning', 'A* steg för steg', intro, [d_a, b, c], 'A* tar ut den ruta i öppna listan som har lägst f.', ['procedur'])


# ======================================================================== vägkostnad

def kostnad_task(id_, seed, sammanhang):
    def bygg(rng):
        rows = labyrint(rng, 4, 6, 0.18, 6)
        return med_terrang(rng, rows, rng.choice([3, 4, 5]))

    def bast_bland_kortaste(rows):
        s, g = A.parse(rows)
        d = A.dist_all(rows, s)
        best = {s: 0}
        for c in sorted(d, key=d.get):
            for v in A.neigh(rows, c):
                if d.get(v) == d[c] + 1:
                    best[v] = min(best.get(v, 10 ** 9), best[c] + A.cost(rows, v))
        return d[g], best[g]

    def ok(rows):
        bfsv = A.bfs(rows)['path']
        kost, _ = A.ucs_grid(rows)
        return kost is not None and any(A.cost(rows, c) == 3 for c in bfsv[1:])
    rows = sok_fram(seed, bygg, ok)
    bfsv = A.bfs(rows)['path']
    vk = A.path_cost(rows, bfsv)
    kost, billig = A.ucs_grid(rows)
    steg, kost_kortast = bast_bland_kortaste(rows)
    s, g = A.parse(rows)
    intro = maze(rows, s, g) + p(sammanhang + ' Att gå in i en lerruta (3) kostar 3 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0.')
    lera = [A.cname(c) for c in bfsv[1:] if A.cost(rows, c) == 3]
    a = num(f'Vad kostar vägen {pil(names(bfsv))}?',
            [step('Lerrutor på vägen', (lista(lera) + f' kostar 3 var, {len(lera)} · 3 = {3 * len(lera)}.') if lera else 'Vägen går inte genom någon lerruta.'),
             step('Övriga rutor', f'{len(bfsv) - 1 - len(lera)} rutor kostar 1 var. Totalt {vk}.')], vk,
            'Start räknas inte. Varje ruta du går in i kostar 1 eller 3.', 1)
    b = num('Vad kostar den billigaste vägen från start till mål?',
            [step('En väg som undviker så mycket lera som möjligt', f'{pil(names(billig))}.'), step(f'Summera rutorna: {kost}', 'Ingen annan väg kostar mindre.')], kost,
            'Pröva vägar som går runt lerrutorna och jämför kostnaderna.', 2)
    lika = kost == kost_kortast
    c = val(f'De kortaste vägarna i antal steg har {steg} steg. Kostar någon av dem lika lite som den billigaste vägen?',
            [step('Billigast bland de kortaste vägarna', f'Den billigaste vägen med {steg} steg kostar {kost_kortast}.'),
             step(f'Den billigaste vägen totalt kostar {kost}', ('Det är lika mycket, så en av de kortaste vägarna är också billigast.' if kost == kost_kortast else f'Det är mindre än {kost_kortast}, så den billigaste vägen är en omväg runt leran.'))],
            [alt('Ja, en av de kortaste vägarna är också billigast', lika,
                 f'En väg med {steg} steg kostar {kost_kortast}, lika mycket som den billigaste.' if lika else
                 f'Den billigaste vägen med {steg} steg kostar {kost_kortast}, mer än {kost}.'),
             alt('Nej, den billigaste vägen går en omväg runt leran', not lika,
                 f'Omvägen kostar {kost}, mindre än {kost_kortast}.' if not lika else
                 f'Ingen omväg behövs, en väg med {steg} steg kostar redan {kost}.')],
            'Jämför kostnaden för den billigaste vägen med kostnaden för vägarna med färst steg.', 2)
    return uppgift(id_, 'viktade_vagar', 'Vägkostnad i labyrinter', intro, [a, b, c], 'Kostnaden är summan av rutorna man går in i.', ['procedur'])


# ======================================================================== minimax och beskärning med stöd

SPEL_SAMMANHANG = [
    'Två spelare turas om i ett enkelt brädspel. Talen i löven är MAX:s poäng när spelet är slut.',
    'En schackdator räknar några drag framåt. Talen i löven är datorns bedömning av slutläget.',
    'I ett kortspel för två väljer spelarna kort i tur och ordning. Talen visar MAX:s poäng i slutläget.',
    'En spelagent i luffarschack bedömer slutlägena med tal, där högt är bra för MAX.',
    'Två elever spelar ett tärningsfritt räknespel. Talen i löven är vad MAX vinner, negativt betyder att MAX förlorar.',
    'En dator spelar fyra i rad mot en människa. Talen i löven är datorns bedömning av slutläget.',
    'I ett strategispel planerar en spelagent sina drag. Talen i löven är MAX:s poäng.',
    'Två robotar spelar ett spel där de turas om att flytta. Talen i löven är MAX:s poäng.',
]


def med_spel(u, text):
    """Lägg en sammanhangsmening före ”Spelträdet söks igenom …” i inledning och huvudtext."""
    key = '<p>Spelträdet söks igenom'
    assert u['spelIntro'].count(key) == 1 and u['t'].count(key) == 1, u['id']
    u['spelIntro'] = u['spelIntro'].replace(key, p(text) + key)
    u['t'] = u['t'].replace(key, p(text) + key)
    return u


def mm_drill(id_, seed, form, root_max):
    def bygg(rng):
        def lov():
            return rng.randint(-9, 9)
        if form == '3x2':
            return [[lov(), lov()] for _ in range(3)]
        if form == '2x3':
            return [[lov(), lov(), lov()] for _ in range(2)]
        return [[[lov(), lov()], [lov(), lov()]] for _ in range(2)]

    def ok(v):
        r = T.build(v, root_max)
        barn = [T.minimax(k) for k in r['kids']]
        rot = T.minimax(r)
        alla = json.dumps(v).replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        return barn.count(rot) == 1 and len(set(alla)) == len(alla)
    v = sok_fram(seed, bygg, ok)
    r = T.build(v, root_max)
    inre = [k['name'] for k in r['kids']]
    nod = random.Random(seed).choice(inre if form != '3niv' else [kk['name'] for k in r['kids'] for kk in k['kids']])
    tn = (1, 2, 2) if form != '3niv' else (2, 2, 2)
    u = K.mm_kg(id_, v, root_max, nod, 'Arbeta från löven och uppåt. MAX tar största, MIN minsta värdet.', tn)
    u['familj'] = 'Minimaxvärden och bästa drag'
    return u


def stod_task(id_, seed, root_max):
    """Två nivåer med två löv per nod. A är undersökt, B:s första löv är känt. Ett beslut: behöver L4 undersökas?"""
    def bygg(rng):
        return [[rng.randint(1, 9), rng.randint(1, 9)], [rng.randint(1, 9), rng.randint(1, 9)]]

    def ok(v):
        alla = [x for k in v for x in k]
        a_v = min(v[0]) if root_max else max(v[0])
        b_v = min(v[1]) if root_max else max(v[1])
        return len(set(alla)) == 4 and a_v != b_v and v[1][0] != a_v
    v = sok_fram(seed, bygg, ok)
    r = T.build(v, root_max)
    val_, ev, cuts, notes = T.alphabeta(r)
    a_v = min(v[0]) if root_max else max(v[0])
    l3 = v[1][0]
    kap = (l3 <= a_v) if root_max else (l3 >= a_v)
    assert kap == bool(T.pruned_leaves(cuts) == ['L4'])
    ro, bn = ('MAX', 'MIN') if root_max else ('MIN', 'MAX')
    intro = (P6.fig(v, root_max, f'Spelträd med {ro} i roten och {bn}-noderna A och B. Löven heter L1–L4.') + P6.AB +
             p(f'Sökningen har undersökt A och just utvärderat B:s första löv, L3 = {l3}.'))
    op = 'min' if root_max else 'max'
    a = num('Vilket värde får A?', [step(f'A är en {bn}-nod', f'A = {op}({v[0][0]}, {v[0][1]}) = {a_v}.')], a_v,
            f'Väljer {bn} största eller minsta värdet?', 1)
    if root_max:
        grans, jamf = f'B blir högst {l3}', ('B kan inte bli bättre för MAX än A' if kap else 'B kan fortfarande bli bättre än A')
    else:
        grans, jamf = f'B blir minst {l3}', ('B kan inte bli bättre för MIN än A' if kap else 'B kan fortfarande bli bättre än A')
    b = val('Behöver lövet L4 undersökas?',
            [step(f'B är en {bn}-nod: {grans}', f'{bn} väljer {l3} eller något {"mindre" if root_max else "större"}.'),
             step(f'Jämför med A = {a_v}', jamf + '.')],
            [alt('Nej, roten väljer A vad L4 än är', kap,
                 f'{grans}, så B kan inte bli bättre för {ro} än A = {a_v}.' if kap else
                 f'{grans} räcker inte: B kan fortfarande bli bättre för {ro} än A = {a_v}, beroende på L4.'),
             alt('Ja, L4 kan ändra vilket drag roten väljer', not kap,
                 f'B kan fortfarande få ett värde som är bättre för {ro} än A = {a_v}, så L4 måste undersökas.' if not kap else
                 f'{grans}, och det kan aldrig slå A = {a_v} för {ro}. L4 behövs inte.')],
            f'Jämför det bästa B kan ge {ro} med A.', 3)
    c = num('Vilket värde får roten?', [step('Rotens val', f'A = {a_v}, B = {T.minimax(r["kids"][1])}. Roten får {val_}.')], val_,
            f'{ro} väljer det {"största" if root_max else "minsta"} värdet.', 1)
    return uppgift(id_, 'alfa_beta', 'Beskärningens idé', intro, [a, b, c], 'Jämför vad B högst eller minst kan bli med A.', ['procedur', 'begrepp'])


# ======================================================================== träningsnivå 1 (granskningen 2026-11-12, punkt 3)

RIKTNING = {(-1, 0): 'uppåt', (0, 1): 'åt höger', (1, 0): 'nedåt', (0, -1): 'åt vänster'}


def dfs_n1_task(id_, seed, sammanhang):
    """DFS i ett steg: grannar till start, första besöket och nästa besök från en given ruta."""
    def bygg(rng):
        return labyrint(rng, 4, 6, 0.3, 6)

    def nasta(rows):
        r = A.dfs(rows)['order']
        for i in range(2, len(r) - 1):
            if A.manhattan(r[i], r[i + 1]) == 1 and len(A.neigh(rows, r[i])) >= 3:
                return i
        return None

    def ok(rows):
        s, _ = A.parse(rows)
        return len(A.neigh(rows, s)) >= 2 and nasta(rows) is not None
    rows = sok_fram(seed, bygg, ok)
    s, g = A.parse(rows)
    ordning = A.dfs(rows)['order']
    nb = A.neigh(rows, s)
    forsta = nb[0]
    i = nasta(rows)
    X, nxt = ordning[i], ordning[i + 1]
    besokta = set(ordning[:i + 1])
    xn, sn = A.cname(X), A.cname(s)
    intro = maze(rows, s, g) + p(sammanhang) + p('Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).')
    a = num(f'Start ligger i {sn}. Hur många öppna grannar har startrutan?',
            [step(f'Grannarna till {sn}', ', '.join(f'{RIKTNING[(c[0] - s[0], c[1] - s[1])]}: {A.cname(c)}' for c in nb) + '.')],
            len(nb), 'Titta uppåt, åt höger, nedåt och åt vänster. Väggar och kanten räknas inte.', 1)
    b = val('Vilken ruta besöker DFS direkt efter start?',
            [step('Första tillåtna riktningen', f'Ordningen är ↑ → ↓ ←. Den första öppna grannen är {A.cname(forsta)} '
                                                f'({RIKTNING[(forsta[0] - s[0], forsta[1] - s[1])]}).')],
            [alt(f'Rutan {A.cname(c)}', c == forsta,
                 f'{A.cname(c)} ligger {RIKTNING[(c[0] - s[0], c[1] - s[1])]} och ' +
                 ('är den första öppna grannen i ordningen.' if c == forsta else 'prövas först senare i ordningen ↑ → ↓ ←.'))
             for c in nb],
            'Pröva riktningarna i ordningen ↑ → ↓ ←.', 1)
    grannar = A.neigh(rows, X)
    c = val(f'DFS har just kommit till rutan {xn}. Vilken ruta besöks härnäst?',
            [step(f'Grannarna till {xn} i ordningen ↑ → ↓ ←',
                  ', '.join(f'{A.cname(v)} ({"redan besökt" if v in besokta else "obesökt"})' for v in grannar) + '.'),
             step('Den första obesökta grannen', f'{A.cname(nxt)} besöks härnäst.')],
            [alt(f'Rutan {A.cname(v)}', v == nxt,
                 f'{A.cname(nxt)} är den första obesökta grannen i ordningen ↑ → ↓ ←.' if v == nxt else
                 (f'{A.cname(v)} är redan besökt.' if v in besokta else f'{A.cname(v)} kommer senare i ordningen ↑ → ↓ ←.'))
             for v in grannar],
            'Hoppa över grannar som redan är besökta.', 1)
    return uppgift(id_, 'dfs', 'DFS i labyrinter', intro, [a, b, c], 'DFS går till den första obesökta grannen i ordningen ↑ → ↓ ←.', ['procedur'])


def astar_n1_task(id_, seed, sammanhang):
    """A* i ett steg: h för start, f för en granne och vilken granne som har lägst f."""
    def ok(rows):
        s, g = A.parse(rows)
        f = sorted(1 + A.manhattan(v, g) for v in A.neigh(rows, s))
        return len(f) >= 2 and f[0] < f[1]
    rows = sok_fram(seed, lambda rng: labyrint(rng, 4, 6, 0.28, 6), ok)
    s, g = A.parse(rows)
    nb = sorted(A.neigh(rows, s), key=A.cname)
    f = {A.cname(v): 1 + A.manhattan(v, g) for v in nb}
    basta = min(f, key=f.get)
    X = random.Random(seed).choice(nb)
    xn, sn, gn = A.cname(X), A.cname(s), A.cname(g)
    hs = A.manhattan(s, g)
    intro = maze(rows, s, g) + p(sammanhang) + p(K.ASTAR)
    a = num(f'Bestäm h för startrutan {sn}.',
            [step(f'Rader och kolumner från {sn} till målet {gn}', f'{abs(s[0] - g[0])} + {abs(s[1] - g[1])} = {hs}.')], hs,
            'Räkna rader och kolumner till målet. Väggar räknas inte.', 1)
    b = num(f'Bestäm f för rutan {xn}, som ligger bredvid start.',
            [step('g = 1', f'{xn} ligger ett steg från start.'),
             step(f'f = g + h = 1 + {f[xn] - 1}', f'h = {abs(X[0] - g[0])} + {abs(X[1] - g[1])} = {f[xn] - 1}, så f = {f[xn]}.')], f[xn],
            'g är antalet steg från start, h räknas rakt till målet.', 1)
    c = val('Vilken av grannarna till start har lägst f?',
            [step('f för grannarna', ', '.join(f'{n}: {v}' for n, v in f.items()) + f'. Lägst har {basta}.')],
            [alt(f'Rutan {n}', n == basta, f'{n} har f = {f[n]}' + (', det lägsta.' if n == basta else f', mer än {basta}:s {f[basta]}.'))
             for n in f],
            'Alla grannar har g = 1. Jämför h.', 1)
    return uppgift(id_, 'astar_sokning', 'A* steg för steg', intro, [a, b, c], 'f = g + h, och A* väljer lägst f.', ['procedur'])


# ======================================================================== flera terrängtyper (punkt 5)

TERRANG = {'3': 'lera', '4': 'is', '5': 'backe'}


def terrang_task(id_, seed, sorter, sammanhang):
    """Vägkostnad med två eller tre terrängtyper. Kostnaden är siffran i rutan."""
    def bygg(rng):
        rows = labyrint(rng, 4, 6, 0.15, 6)
        oppna = [(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == '.']
        g = [list(r) for r in rows]
        for k, (r, c) in enumerate(rng.sample(oppna, 6)):
            g[r][c] = sorter[k % len(sorter)]
        return [''.join(r) for r in g]

    def ok(rows):
        v = A.bfs(rows)['path']
        typer = {rows[r][c] for r, c in v[1:-1]}
        kost, _ = A.ucs_grid(rows)
        return kost is not None and len(typer & set(sorter)) >= 2 and A.path_cost(rows, v) > kost
    rows = sok_fram(seed, bygg, ok)
    s, g = A.parse(rows)
    v = A.bfs(rows)['path']
    vk = A.path_cost(rows, v)
    kost, billig = A.ucs_grid(rows)
    kostnad_txt = ', '.join(f'{TERRANG[t]} {t}' for t in sorter)
    intro = maze(rows, s, g) + p(sammanhang + f' Att gå in i en ruta med terräng kostar talet i rutan ({kostnad_txt}). '
                                 'Att gå in i en vit ruta eller målet kostar 1, och start kostar 0.')
    delar = [f'{A.cname(c)}: {A.cost(rows, c)}' for c in v[1:]]
    a = num(f'Vad kostar vägen {pil(names(v))}?',
            [step('Kostnad för varje ruta på vägen', ', '.join(delar) + '.'), step(f'Summa: {vk}', 'Start räknas inte.')], vk,
            'Lägg ihop kostnaden för varje ruta du går in i.', 1)
    b = num('Vad kostar den billigaste vägen från start till mål?',
            [step('En väg som undviker de dyraste rutorna', f'{pil(names(billig))}.'),
             step(f'Summa: {kost}', ', '.join(f'{A.cname(c)}: {A.cost(rows, c)}' for c in billig[1:]) + '.')], kost,
            'Jämför några vägar och leta efter en väg runt de dyraste rutorna.', 2)
    sparar = vk - kost
    c = num(f'Hur mycket billigare är den billigaste vägen än vägen {pil(names(v))}?',
            [step('Skillnaden', f'{vk} − {kost} = {sparar}.')], sparar, 'Använd svaren på de två föregående frågorna.', 1)
    return uppgift(id_, 'viktade_vagar', 'Vägkostnad i labyrinter', intro, [a, b, c], 'Kostnaden är summan av rutorna man går in i.', ['procedur'])


# ======================================================================== lista

def alla():
    S = SAMMANHANG
    out = []
    for i, (id_, stack) in enumerate([('1.77', False), ('1.78', True), ('1.79', False), ('1.80', True), ('1.81', False), ('1.82', True)]):
        ctx = (STACK_SAMMANHANG if stack else KO_SAMMANHANG)[i // 2]
        out.append(ko_stack_task(id_, 7700 + i, stack, ctx))
    out += [bfs_drill('1.83', 8301, 5, 2, ['avst', 'k', 'steg'], (1, 2, 2), S[0]),
            bfs_drill('1.84', 8402, 6, 3, ['k', 'avst', 'antal'], (2, 1, 2), S[1]),
            bfs_drill('1.85', 8503, 4, 2, ['avst', 'steg', 'k'], (1, 2, 2), S[2], R=5, C=5),
            bfs_drill('1.86', 8604, 7, 3, ['k', 'steg', 'avst'], (2, 2, 1), S[3], R=4, C=7)]
    out += [dfs_drill('1.87', 8701, 4, S[4]), dfs_drill('1.88', 8802, 5, S[5]),
            dfs_drill('1.89', 8903, 6, S[6], R=5, C=5), dfs_drill('1.90', 9004, 3, S[7], R=4, C=7)]
    out += [trad_drill(f'1.{91 + i}', 9100 + i, False, TRAD_SAMMANHANG[i]) for i in range(3)]
    out += [trad_drill(f'1.{94 + i}', 9400 + i, True, TRAD_SAMMANHANG[i]) for i in range(3)]
    out += [prio_task(f'2.{88 + i}', 8800 + i, PRIO_SAMMANHANG[i]) for i in range(4)]
    out += [ghf_drill(f'2.{92 + i}', 9200 + i, S[i + 1]) for i in range(4)]
    out += [astar_e_task(f'2.{96 + i}', 9600 + i, S[(i + 4) % 8]) for i in range(4)]
    out += [kostnad_task(f'2.{100 + i}', 10000 + i, S[(i + 2) % 8]) for i in range(4)]
    G = SPEL_SAMMANHANG
    out += [med_spel(mm_drill('3.62', 6201, '3x2', True), G[0]), med_spel(mm_drill('3.63', 6302, '2x3', False), G[1]),
            med_spel(mm_drill('3.64', 6403, '3niv', True), G[2]), med_spel(mm_drill('3.65', 6504, '3niv', False), G[3])]
    out += [med_spel(stod_task(f'3.{66 + i}', 6600 + i, i % 2 == 0), G[4 + i]) for i in range(4)]
    # Granskningen 2026-11-12: träningsnivå 1 i DFS och A* (punkt 3) och fler terrängtyper (punkt 5)
    out += [dfs_n1_task(f'1.{100 + i}', 10100 + i, S[(i + 3) % 8]) for i in range(4)]
    out += [astar_n1_task(f'2.{109 + i}', 10900 + i, S[(i + 5) % 8]) for i in range(4)]
    out += [terrang_task(f'2.{113 + i}', 11300 + i, so, S[(i + 6) % 8])
            for i, so in enumerate([['3', '4'], ['4', '5'], ['3', '5'], ['3', '4', '5']])]
    return out


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = alla()
    for u in nya:
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
    print(f'{len(nya)} uppgifter för mängdträning inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
