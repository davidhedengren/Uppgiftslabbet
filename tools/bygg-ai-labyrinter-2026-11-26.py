"""AI-banken 2026-11-26: labyrinter med riktiga väggar och fler g(n)-, h(n)- och f(n)-uppgifter.

Användaren: ”Det är lite för många labyrinter där som inte är labyrinter, alltså det är inga väggar. Gör om dessa
och lägg till fler uppgifter av typen 'Bestäm g(n) för rutan P', 'bestäm h(n) för rutan …' och 'bestäm f(n) för
rutan …'. Jag vill ha varierade labyrinter men liknande uppgifter.”

1. OMBYGGDA (samma id, nivå per delkort, familj, delmoment och förmågor; nytt innehåll och facit): uppgifter vars
   labyrint hade 0 väggar (2.27, 2.29, 2.42, 2.44, 2.51, 2.53, 2.63, 2.108) eller 1 vägg i ett större rutnät
   (1.104, 2.25, 2.28, 2.48, 2.55, 2.57, 2.75). 1.105 och 1.106 handlar om öppna rutnät och står kvar, liksom
   3 × 3-rutnäten i 1.13 och 1.48.
2. NYA 2.123–2.152: g(n), h(n) och f(n) för en markerad ruta i varierade labyrinter (4 × 4 till 6 × 7, några med
   lera eller is). Väggarna tvingar oftast fram en omväg, så att g(n) skiljer sig från Manhattanavståndet.

Labyrinterna slumpas med fasta frön under villkor (väggar på 15–35 % av rutorna, en väg till målet, uppgiftens
egna villkor). Svaren räknas med tools/ai_sokalgoritmer.py och kontrolleras igen innan något skrivs. Texterna skrivs
direkt med f(n)-notationen och utan ”Välj ett alternativ.” (språkomskrivningen 2026-11-23/24).

  python tools/bygg-ai-labyrinter-2026-11-26.py [--skriv]
Kör därefter bygg-ai-omgruppering-2026-11-11.py (sorterar och placerar) och bygg-ai-nivaer-2026-11-11.py.
"""
import copy
import importlib.util
import json
import os
import random
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'sprak'))


def _ladda(namn, fil):
    spec = importlib.util.spec_from_file_location(namn, os.path.join(HERE, fil))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


K = _ladda('kg', 'bygg-ai-kunskapsgymmet-2026-11-11.py')
FGH = _ladda('fgh', os.path.join('sprak', 'ai_fgh_n.py'))
B, A = K.B, K.A
maze, step, tab = K.maze, K.step, K.tab
alt, names, pil, lista, p = B.alt, B.names, B.pil, B.lista, B.p
from ai_labyrintdidaktik import vald_karta
import bankobjekt as BO  # noqa: E402

BANK = os.path.join(HERE, '..', 'uppgifterai.js')
MARK = [('#fff3b0', 'Markerad ruta')]
TERR = {'3': 'lerruta', '4': 'isruta', '5': 'backruta'}
KOST = {'3': 3, '4': 4, '5': 5}


# ---------------------------------------------------------------- labyrinter

def labyrint(rng, R, C, vagg=(0.18, 0.32), terr='', hörn=None, omvag=True):
    """Slumpa en labyrint: start och mål i olika delar av rutnätet, väggar och eventuell terräng."""
    for _ in range(4000):
        g = [['.'] * C for _ in range(R)]
        if hörn == 'inre':
            s = (rng.randrange(1, R - 1), rng.randrange(1, C - 1))
        else:
            s = rng.choice([(R - 1, 0), (0, 0), (rng.randrange(R), 0)])
        mal = rng.choice([(0, C - 1), (R - 1, C - 1), (rng.randrange(R), C - 1)])
        if A.manhattan(s, mal) < max(R, C):
            continue
        celler = [(r, c) for r in range(R) for c in range(C) if (r, c) not in (s, mal)]
        rng.shuffle(celler)
        nv = round(rng.uniform(*vagg) * R * C)
        for r, c in celler[:nv]:
            g[r][c] = '#'
        i = nv
        for ch in terr:
            r, c = celler[i]
            g[r][c] = ch
            i += 1
        g[s[0]][s[1]], g[mal[0]][mal[1]] = 'S', 'G'
        rows = [''.join(x) for x in g]
        b = A.bfs(rows)['path']
        if b and sum(x.count('#') for x in rows) >= 3 and (not omvag or len(b) - 1 > A.manhattan(s, mal)):
            return rows
    raise RuntimeError('ingen labyrint')


def sok(fro, villkor, **kw):
    rng = random.Random(fro)
    for _ in range(3000):
        R, C = kw.get('storlek') or rng.choice([(4, 5), (5, 5), (5, 6), (4, 6), (6, 6), (5, 7), (6, 7), (4, 4)])
        rows = labyrint(rng, R, C, kw.get('vagg', (0.18, 0.32)), kw.get('terr', ''), kw.get('hörn'), kw.get('omvag', True))
        res = villkor(rows, rng)
        if res:
            return rows, res
    raise RuntimeError(f'inget som uppfyller villkoren (frö {fro})')


def oppna(rows):
    return [(r, c) for r, x in enumerate(rows) for c, ch in enumerate(x) if ch not in '#SG']


def billigast(rows, mal):
    """g för en ruta: billigaste kostnad från start (terräng räknas), samt vägen."""
    tmp = [x.replace('G', '.') for x in rows]
    tmp[mal[0]] = tmp[mal[0]][:mal[1]] + 'G' + tmp[mal[0]][mal[1] + 1:]
    return A.ucs_grid(tmp)


def astar_spar(rows):
    """Som ai_sokalgoritmer.astar, men med öppna listan efter varje uttag."""
    start, goal = A.parse(rows)
    g, parent, closed, out, openl, efter = {start: 0}, {}, set(), [], {start}, []
    f = lambda x: g[x] + A.manhattan(x, goal)  # noqa: E731
    while openl:
        n = min(openl, key=lambda x: (f(x), A.manhattan(x, goal), A.cname(x)))
        openl.discard(n)
        closed.add(n)
        out.append(n)
        if n == goal:
            efter.append(set(openl))
            break
        for v in A.neigh(rows, n):
            if v in closed:
                continue
            alt_ = g[n] + A.cost(rows, v)
            if alt_ < g.get(v, 10 ** 9):
                g[v] = alt_
                parent[v] = n
                openl.add(v)
        efter.append(set(openl))
    return dict(order=out, path=A.path_from(parent, goal), g=g, efter=efter)


def kost_text(rows):
    ch = sorted({c for x in rows for c in x if c in TERR})
    if not ch:
        return ''
    delar = [f'{KOST[c]} att gå in i en {TERR[c]}' for c in ch] + ['1 att gå in i en vit ruta eller målet']
    return 'Det kostar ' + ', '.join(delar[:-1]) + ' och ' + delar[-1] + '. Startrutan kostar inget.'


def runt(rows, dyr, billig):
    """Facitrubrik: vilka dyra rutor den billigaste vägen går runt."""
    undvik = [c for c in dyr[1:] if A.cost(rows, c) > 1 and c not in billig]
    ord_ = sorted({TERR[rows[r][c]] for r, c in undvik})
    slag = {'lerruta': 'lerrutorna', 'isruta': 'isrutorna', 'backruta': 'backrutorna'}
    if len(undvik) == 1:
        return f'Den billigaste vägen går runt {TERR[rows[undvik[0][0]][undvik[0][1]]]}n {A.cname(undvik[0])}'
    namn = ' och '.join([', '.join(names(undvik[:-1])), A.cname(undvik[-1])])
    return f'Den billigaste vägen går runt {" och ".join(slag[x] for x in ord_)} {namn}'


def summa(rows, vag):
    return ' + '.join(str(A.cost(rows, c)) for c in vag[1:])


# ---------------------------------------------------------------- delar

def num(fraga, steg, svar, led, tn):
    return K.num(fraga, steg, svar, led, tn)


def val(fraga, steg, alts, led, tn):
    d = K.val(fraga, steg, alts, led, tn)
    d['fraga'] = d['fraga'].replace(' Välj ett alternativ.', '')
    return d


def namn_del(fraga, steg, svar, led, tn, fmt, kg):
    d = B.part(p(fraga), steg, svar + '.', led, tn)
    d.update({'svarstyp': 'kort_text', 'rättSvar': svar, 'tolerans': None, 'självrättning': True,
              'svarFormat': fmt, 'svarEnhet': None, 'spel': True, 'kgInstruktion': kg})
    return d


def cell_alts(ratt, andra, kommentar):
    opts = sorted(set([ratt] + andra))[:4]
    if ratt not in opts:
        opts = sorted(set([ratt] + andra[:3]))
    return [alt(x, x == ratt, kommentar(x)) for x in opts]


# ---------------------------------------------------------------- g(n), h(n), f(n)

G_LED_RAK = 'Räkna stegen från start till {L}. Här behöver vägen inte gå runt någon vägg.'


def g_rad(vag, L, mn):
    """Facitrad för g(n) när vägen till rutan går utan omväg."""
    return f'Från start till {L} ({mn}) går en väg utan omväg: {pil(names(vag))}. Den har {len(vag) - 1} steg.'


def ghf_delar(rows, mark, L, tn=(2, 1, 1), bara=('g', 'h', 'f')):
    s, goal = A.parse(rows)
    gv, vag = billigast(rows, mark)
    hv = A.manhattan(mark, goal)
    mn, gn = A.cname(mark), A.cname(goal)
    terr = any(c in TERR for x in rows for c in x)
    delar = []
    rak = not terr and gv == A.manhattan(s, mark)
    if 'g' in bara:
        rad = (f'Den billigaste vägen från start till {L} ({mn}) är {pil(names(vag))}. Den kostar {summa(rows, vag)} = {gv}.'
               if terr else g_rad(vag, L, mn) if rak else
               f'Den kortaste vägen från start till {L} ({mn}) går runt väggarna: {pil(names(vag))}. '
               f'Den har {len(vag) - 1} steg.')
        delar.append(num(f'Bestäm g(n) för rutan {L}.',
                         [step('g(n) = kostnaden för den billigaste vägen från start till n', rad)], gv,
                         G_LED_RAK.format(L=L) if rak else
                         f'Följ gångarna från start till {L}. Väggarna går inte att passera.' if not terr else
                         f'Pröva vägar från start till {L} och jämför vad de kostar. Väggarna går inte att passera.',
                         tn[0]))
    if 'h' in bara:
        delar.append(num(f'Bestäm h(n) för rutan {L}.',
                         [step('h(n) = radskillnad + kolumnskillnad till målet',
                               f'{L} ligger i {mn} och målet i {gn}: {abs(mark[0] - goal[0])} + {abs(mark[1] - goal[1])} = '
                               f'{hv}. Väggarna räknas inte.')], hv,
                         f'Räkna rader och kolumner från {L} till målet, som om väggarna inte fanns.', tn[1]))
    if 'f' in bara:
        rubrik = 'f(n) = g(n) + h(n)'
        rad = f'f({L}) = g({L}) + h({L}) = {gv} + {hv} = {gv + hv}.'
        delar.append(num(f'Bestäm f(n) för rutan {L}.', [step(rubrik, rad)], gv + hv,
                         f'Bestäm först g(n) och h(n) för {L} och lägg ihop dem.', tn[2]))
    return delar, gv, hv


SAMMANHANG = [
    'En lagerrobot står i startrutan och ska hämta en låda som står i målrutan.',
    'En robotdammsugare står i sin laddstation i startrutan och ska städa i hallen, som är målrutan.',
    'En mus börjar i startrutan och letar sig fram till en ostbit i målrutan.',
    'En spelfigur i ett datorspel ska ta sig från startrutan till skattkistan i målrutan.',
    'En gräsklipparrobot ska köra från garaget i startrutan till ett hörn av gräsmattan i målrutan.',
    'En leveransrobot på ett sjukhus kör mediciner från apoteket i startrutan till en avdelning i målrutan.',
    'En drönare flyger mellan hyllorna i ett lager, från startrutan till utgången i målrutan.',
    'En räddningsrobot tar sig in i ett rasat hus, från ingången i startrutan till en instängd person i målrutan.',
    'En hund springer genom en hinderbana från startrutan till en godbit i målrutan.',
    'En självkörande truck ska flytta en pall från startrutan till lastkajen i målrutan.',
    'En servitörsrobot på en restaurang kör från köket i startrutan till ett bord i målrutan.',
    'En robot i en skoltävling ska köra genom banan från startrutan till mållinjen i målrutan.',
    'En bagagevagn på en flygplats kör från incheckningen i startrutan till ett plan i målrutan.',
    'En brandrobot tar sig genom en rökfylld byggnad från startrutan till målrutan.',
    'En robot i ett växthus börjar i startrutan och ska vattna en planta i målrutan.',
    'En robotbil i ett parkeringshus letar sig från infarten i startrutan till en ledig plats i målrutan.',
]
ASTAR_TEXT = [
    'Vägen söks med A*. Här är h(n) Manhattanavståndet från rutan n till målet och g(n) kostnaden för den '
    'billigaste vägen från start till n.',
    'Vägen planeras med A*, där g(n) är kostnaden för den billigaste vägen från start till rutan n och h(n) är '
    'Manhattanavståndet från n till målet.',
]


def ghf_intro(rows, mark, L, i):
    """i väljer sammanhang och formulering, så att ingen uppgiftstext upprepas."""
    s, goal = A.parse(rows)
    kt = kost_text(rows)
    text = SAMMANHANG[i % len(SAMMANHANG)] + ' ' + ASTAR_TEXT[i // len(SAMMANHANG) % 2]
    return maze(rows, s, goal, {mark: L}, extra_legend=MARK) + p(text) + (p(kt) if kt else '')


def rak_till(rows, c):
    """Sant när billigaste vägen från start till c varken går runt väggar eller genom terräng."""
    s, _ = A.parse(rows)
    gv, vag = billigast(rows, c)
    return bool(vag) and gv == A.manhattan(s, c) and all(A.cost(rows, x) == 1 for x in vag[1:])


def ghf_villkor(omvag=True, terr=False, rak=False):
    def v(rows, rng):
        s, goal = A.parse(rows)
        kand = []
        for c in oppna(rows):
            gv, vag = billigast(rows, c)
            if not vag or A.manhattan(c, goal) == 0:
                continue
            steg = len(vag) - 1
            if steg < 2:
                continue
            if rak:
                if steg >= 3 and rak_till(rows, c):
                    kand.append(c)
                continue
            dv = gv - A.manhattan(s, c)
            if omvag and dv < 2 and not terr:
                continue
            if terr and gv == steg:      # terrängen ska påverka g
                continue
            kand.append(c)
        return rng.choice(sorted(kand)) if kand else None
    return v


# ---------------------------------------------------------------- uppgiftsmallar för de ombyggda

def byt_i(del_, par):
    """Kopiera ett befintligt delkort och byt siffrorna i dess kommentarer och facit mot den nya labyrintens."""
    t = json.dumps(del_, ensure_ascii=False)
    for monster, ny in par:
        t, n = re.subn(monster, lambda m: ny, t)
        assert n >= 1, monster
    return json.loads(t)


def g_ghf(old, fro, i, terr='', delar=('g', 'h', 'f'), rak=False):
    # rak: E-uppgift, så g(n) ska följa en väg utan omväg (AI_NIVAINDELNING: g runt väggar är C).
    rows, mark = sok(fro, ghf_villkor(omvag=not terr, terr=bool(terr), rak=rak), terr=terr)
    tn = tuple(d.get('traningsniva', 2) for d in old['spelDelar']) + (1, 1, 1)
    parts, gv, hv = ghf_delar(rows, mark, 'P', tn, delar)
    return K.kg_task(old['id'], old['omr'], old['familj'], ghf_intro(rows, mark, 'P', i), parts,
                     'g(n) följer gångarna från start, h(n) räknas rakt till målet.', old['formaga']), rows


def g_vikt(old, fro, typ):
    def villkor(rows, rng):
        uc, up = A.ucs_grid(rows)
        b = A.bfs(rows)['path']
        bc = A.path_cost(rows, b)
        lera = sum(1 for c in b[1:] if A.cost(rows, c) > 1)
        if typ in ('2.29', '2.44', '2.63') and not (bc > uc and b != up):
            return None
        if typ == '2.53' and lera < 1:
            return None
        return dict(uc=uc, up=up, b=b, bc=bc, lera=lera)
    terr = {'2.29': '333', '2.44': '3344', '2.53': '333', '2.63': '3344'}[typ]
    rows, r = sok(fro, villkor, terr=terr, vagg=(0.15, 0.25))
    s, goal = A.parse(rows)
    intro = maze(rows, s, goal) + p(kost_text(rows))
    tn = [d['traningsniva'] for d in old['spelDelar']]
    bt = pil(names(r['b']))
    if typ == '2.29':
        a = num('Vad kostar den billigaste vägen från start till mål?',
                [step(runt(rows, r['b'], r['up']), pil(names(r['up'])) + '.'),
                 step('Summera kostnaderna', f'{summa(rows, r["up"])} = {r["uc"]}.')], r['uc'],
                'Jämför vägar runt den dyra terrängen med vägar genom den.', tn[0])
        b = namn_del('Ange den billigaste vägen.', [step(runt(rows, r['b'], r['up']), pil(names(r['up'])) + f', som kostar {r["uc"]}.')],
                     lista(names(r['up'])), 'Börja vid start och undvik de dyra rutorna där det går.', tn[1], 'namnordning',
                     'Skriv rutorna längs vägen, från start till mål.')
        steg = len(r['b']) - 1
        fel = []
        for x in (steg, r['uc'], r['bc'] + 1, r['bc'] - 1, r['bc'] + 2):
            if x != r['bc'] and x not in fel and len(fel) < 3:
                fel.append(x)
        jmf = 'lika många steg som' if len(r['b']) == len(r['up']) else 'färre steg än'
        c = val(f'Vägen {bt} har {jmf} den billigaste vägen. Vad kostar den?',
                [step('Summera kostnaderna längs vägen', f'{summa(rows, r["b"])} = {r["bc"]}.')],
                [alt(str(x), x == r['bc'], f'Rätt: {summa(rows, r["b"])} = {r["bc"]}.' if x == r['bc'] else
                     ('Det är antalet steg. Lerrutorna kostar mer än 1.' if x == steg else
                      'Det är den billigaste vägens kostnad, men den här vägen går genom dyr terräng.' if x == r['uc'] else
                      'Räkna kostnaden för varje ruta du går in i en gång till.'))
                 for x in sorted([r['bc']] + fel)], 'Lägg ihop kostnaden för varje ruta du går in i.', tn[2])
        parts = [a, b, c]
    elif typ == '2.44':
        a = num(f'Vad kostar vägen {bt}?', [step('Summera kostnaderna längs vägen', f'{summa(rows, r["b"])} = {r["bc"]}.')],
                r['bc'], 'Start kostar 0. Räkna alla rutor du går in i.', tn[0])
        b = num('Vad kostar den billigaste vägen från start till mål?',
                [step(runt(rows, r['b'], r['up']), pil(names(r['up'])) + '.'), step('Summera kostnaderna', f'{summa(rows, r["up"])} = {r["uc"]}.')],
                r['uc'], 'Jämför vägar genom den dyra terrängen med vägar runt den.', tn[1])
        parts = [a, b]
    elif typ == '2.53':
        a = num(f'Hur många lerrutor går vägen {bt} genom?',
                [step('Räkna lerrutorna längs vägen', ', '.join(A.cname(c) for c in r['b'][1:] if A.cost(rows, c) > 1) + '.')],
                r['lera'], 'Gå längs vägen och räkna de bruna rutorna.', tn[0])
        b = num(f'Vad kostar vägen {bt}?', [step('Summera kostnaderna', f'{summa(rows, r["b"])} = {r["bc"]}.')], r['bc'],
                'Lägg ihop kostnaden för varje ruta du går in i.', tn[1])
        parts = [a, b]
    else:  # 2.63: två vägar
        intro += p(f'Väg 1: {bt}.') + p(f'Väg 2: {pil(names(r["up"]))}.')
        billig = 'Väg 2'
        a = val('Vilken väg är billigast?',
                [step('Väg 1', f'{summa(rows, r["b"])} = {r["bc"]}.'), step('Väg 2', f'{summa(rows, r["up"])} = {r["uc"]}.')],
                [alt('Väg 1', False, f'Väg 1 går genom dyr terräng och kostar {r["bc"]}. Väg 2 kostar bara {r["uc"]}.'),
                 alt('Väg 2', True, f'Väg 2 kostar {r["uc"]} och väg 1 {r["bc"]}.'),
                 alt('De kostar lika mycket', False, f'Väg 1 kostar {r["bc"]} och väg 2 {r["uc"]}.')],
                'Räkna ut vad varje väg kostar.', tn[0])
        b = num('Vad kostar väg 1?', [step('Summera kostnaderna', f'{summa(rows, r["b"])} = {r["bc"]}.')], r['bc'],
                'Lägg ihop kostnaden för varje ruta du går in i.', tn[1])
        parts = [a, b]
        assert billig
    return K.kg_task(old['id'], old['omr'], old['familj'], intro, parts, 'Kostnaden för en väg är summan av rutorna man går in i.',
                     old['formaga']), rows


def g_girig_astar(old, fro, typ):
    terr = '4444' if typ == '2.27' else '3333'

    def villkor(rows, rng):
        gr, ast = A.greedy(rows), A.astar(rows)
        ac = A.path_cost(rows, ast['path'])
        if gr['cost'] <= ac:
            return None
        if typ == '2.27':
            s, _ = A.parse(rows)
            nb = A.neigh(rows, s)
            hs = [A.manhattan(c, A.parse(rows)[1]) for c in nb]
            fs = [A.cost(rows, c) + h for c, h in zip(nb, hs)]
            if len(nb) < 2 or len(set(hs)) < len(hs) or len(set(fs)) < len(fs) or gr['order'][1] == ast['order'][1]:
                return None
        return dict(gr=gr, ast=ast, ac=ac)
    rows, r = sok(fro, villkor, terr=terr, vagg=(0.15, 0.25))
    s, goal = A.parse(rows)
    intro = maze(rows, s, goal) + p('Labyrinten söks igenom med girig bäst först och med A* (h(n) = Manhattanavstånd). '
                                    + kost_text(rows) + ' Vid lika värde väljs den ruta som kommer först i bokstavsordning.')
    tn = [d['traningsniva'] for d in old['spelDelar']]
    gr, ast, ac = r['gr'], r['ast'], r['ac']
    a_cost = num('Vad kostar vägen som girig bäst först hittar?',
                 [step('Girig bäst först jämför bara h(n)', pil(names(gr['path'])) + '.'),
                  step('Summera kostnaderna', f'{summa(rows, gr["path"])} = {gr["cost"]}.')], gr['cost'],
                 'Följ lägst h(n) från start och summera kostnaderna.', tn[0])
    b_cost = num('Vad kostar vägen som A* hittar?',
                 [step('A* jämför f(n) = g(n) + h(n)', pil(names(ast['path'])) + '.'),
                  step('Summera kostnaderna', f'{summa(rows, ast["path"])} = {ac}.')], ac, 'A* räknar med vad terrängen kostar.',
                 tn[1] if len(tn) > 1 else tn[0])
    if typ == '2.27':
        nb = sorted(A.neigh(rows, s), key=A.cname)
        h = {c: A.manhattan(c, goal) for c in nb}
        f = {c: A.cost(rows, c) + h[c] for c in nb}
        g1, a1 = A.cname(gr['order'][1]), A.cname(ast['order'][1])
        a = val('Vilken granne till start tar girig bäst först ut först?',
                [step('Girig bäst först väljer lägst h(n)', ', '.join(f'h({A.cname(c)}) = {h[c]}' for c in nb) + '.')],
                [alt(A.cname(c), A.cname(c) == g1, f'h({A.cname(c)}) = {h[c]}' + ('. Lägst h(n).' if A.cname(c) == g1 else
                     ', inte lägst. Girig bäst först bryr sig inte om vad rutan kostar.')) for c in nb],
                'Jämför bara grannarnas h(n).', tn[0])
        b = val('Vilken granne till start tar A* ut först?',
                [step('A* väljer lägst f(n) = g(n) + h(n)', ', '.join(f'f({A.cname(c)}) = {A.cost(rows, c)} + {h[c]} = {f[c]}' for c in nb) + '.')],
                [alt(A.cname(c), A.cname(c) == a1, f'f({A.cname(c)}) = {f[c]}' + ('. Lägst f(n).' if A.cname(c) == a1 else
                     ', inte lägst. Kostnaden för att gå in i rutan räknas med i g(n).')) for c in nb],
                'Räkna f(n) = g(n) + h(n) för grannarna. g(n) är kostnaden för att gå in i rutan.', tn[1])
        a_cost['traningsniva'] = tn[2]
        parts = [a, b, a_cost]
    elif typ == '2.108':
        c = byt_i(old['spelDelar'][2], [(r'Här kostar dess väg \d+ mot A\*:s \d+\.',
                                          f'Här kostar dess väg {gr["cost"]} mot A*:s {ac}.')])
        parts = [a_cost, b_cost, c]
    else:
        parts = [a_cost, b_cost]
    return K.kg_task(old['id'], old['omr'], old['familj'], intro, parts,
                     'Girig bäst först ser bara h(n). A* räknar också med kostnaden hittills.', old['formaga']), rows


def g_astar(old, fro, typ):
    def villkor(rows, rng):
        r = astar_spar(rows)
        s, goal = A.parse(rows)
        fv = lambda c: r['g'][c] + A.manhattan(c, goal)  # noqa: E731
        if typ == '2.28':
            kvar = r['efter'][-1]
            lika = [c for c in kvar if fv(c) == r['g'][goal]]
            return dict(r=r, kvar=kvar, lika=lika) if 2 <= len(kvar) <= 5 and lika and 5 <= len(r['order']) <= 11 else None
        if typ == '2.55':
            nb = A.neigh(rows, s)
            fs = sorted(1 + A.manhattan(c, goal) for c in nb)
            return dict(r=r, nb=nb) if len(nb) >= 2 and fs[0] < fs[1] else None
        if typ == '2.57':
            kvar = r['efter'][1] if len(r['efter']) > 1 else set()
            return dict(r=r, kvar=kvar) if 2 <= len(kvar) <= 4 else None
    hörn = 'inre' if typ == '2.55' else None
    rows, d = sok(fro, villkor, hörn=hörn, vagg=(0.15, 0.28))
    s, goal = A.parse(rows)
    r = d['r']
    fv = lambda c: r['g'][c] + A.manhattan(c, goal)  # noqa: E731
    tn = [x['traningsniva'] for x in old['spelDelar']]
    rader = [[A.cname(c), str(r['g'][c]), str(A.manhattan(c, goal)), str(fv(c))] for c in r['order']]
    if typ == '2.28':
        intro = maze(rows, s, goal) + p('Labyrinten söks igenom med A* (h(n) = Manhattanavstånd). ' + B.ASTAR_TIE.replace(
            'lika f', 'lika f(n)').replace('lägst h', 'lägst h(n)').replace('lika h', 'lika h(n)'))
        order = lista(names(r['order']))
        a = namn_del('Ange i vilken ordning rutorna tas ut ur öppna listan.',
                     [step('Uttag med g(n), h(n) och f(n)', tab(['Tas ut', 'g(n)', 'h(n)', 'f(n)'], rader))], order,
                     'Räkna f(n) = g(n) + h(n) för grannarna till varje uttagen ruta.', tn[0], 'namnordning',
                     'Skriv rutorna i ordning, åtskilda med kommatecken.')
        kvar = sorted(names(d['kvar']))
        b = namn_del('Vilka rutor ligger kvar i öppna listan när målet tas ut?',
                     [step('Inlagda men inte uttagna', ', '.join(f'{A.cname(c)} (f(n) = {fv(c)})' for c in sorted(d['kvar'], key=A.cname)) + '.')],
                     lista(kvar), 'Vilka rutor har lagts in i öppna listan men aldrig tagits ut?', tn[1], 'namnmangd',
                     'Skriv rutorna, åtskilda med kommatecken.')
        x = A.cname(sorted(d['lika'], key=A.cname)[0])
        c = val(f'{x} ligger kvar i öppna listan med samma f(n) som målet. Varför tas målet ut före {x}?',
                [step('Lika f(n): lägst h(n) går först', f'Målet har h(n) = 0, och {x} har h(n) = {A.manhattan(sorted(d["lika"], key=A.cname)[0], goal)}.')],
                [alt('Målet har lägst h(n), och vid lika f(n) väljs lägst h(n)', True, 'Rätt. h(n) är alltid 0 i målet.'),
                 alt('Målet lades in i öppna listan först', False, 'Ordningen rutorna lades in i spelar ingen roll i A*.'),
                 alt(f'{x} kan inte nå målet', False, f'Det gör ingen skillnad: {x} har samma f(n), men högre h(n).'),
                 alt('A* tar alltid ut målet så fort det har lagts in', False, 'Nej, målet tas ut först när det har lägst f(n).')],
                'Vad säger regeln för lika värden?', tn[2])
        parts = [a, b, c]
    elif typ == '2.55':
        intro = maze(rows, s, goal) + p('Labyrinten söks igenom med A* (h(n) = Manhattanavstånd). Start har just tagits ut.')
        nb = sorted(d['nb'], key=A.cname)
        f = {c: 1 + A.manhattan(c, goal) for c in nb}
        bast = min(nb, key=lambda c: (f[c], A.cname(c)))
        a = val('Vilken av grannarna till start har lägst f(n)?',
                [step('f(n) = g(n) + h(n) för grannarna', ', '.join(f'f({A.cname(c)}) = 1 + {A.manhattan(c, goal)} = {f[c]}' for c in nb) + '.')],
                [alt(A.cname(c), c == bast, f'f({A.cname(c)}) = {f[c]}' + ('. Det är lägst.' if c == bast else
                     f', högre än f({A.cname(bast)}) = {f[bast]}.')) for c in nb],
                'Alla grannar har g(n) = 1. Jämför h(n).', tn[0])
        annan = max(nb, key=lambda c: (f[c], A.cname(c)))
        b = num(f'Vilket f(n)-värde har {A.cname(annan)}?',
                [step('f(n) = g(n) + h(n)', f'g({A.cname(annan)}) = 1 och h({A.cname(annan)}) = {A.manhattan(annan, goal)}, så f({A.cname(annan)}) = {f[annan]}.')],
                f[annan], f'Räkna g(n) och h(n) för {A.cname(annan)} och lägg ihop dem.', tn[1])
        parts = [a, b]
    else:  # 2.57
        o1 = A.cname(r['order'][1])
        intro = maze(rows, s, goal) + p('Labyrinten söks igenom med A* (h(n) = Manhattanavstånd). ' + B.ASTAR_TIE.replace(
            'lika f', 'lika f(n)').replace('lägst h', 'lägst h(n)').replace('lika h', 'lika h(n)') + f' Start och {o1} har tagits ut.')
        kvar = sorted(d['kvar'], key=A.cname)
        ratt = ' och '.join([', '.join(names(kvar[:-1])), A.cname(kvar[-1])]) if len(kvar) > 1 else A.cname(kvar[0])
        andra = [c for c in oppna(rows) if c not in d['kvar'] and c not in r['order'][:2]]
        rng = random.Random(fro)
        fel = []
        for _ in range(20):
            x = sorted(set(rng.sample(kvar, max(1, len(kvar) - 1)) + rng.sample(andra, 1)), key=A.cname)
            t = ' och '.join([', '.join(names(x[:-1])), A.cname(x[-1])]) if len(x) > 1 else A.cname(x[0])
            if t != ratt and t not in fel:
                fel.append(t)
            if len(fel) == 3:
                break
        a = val(f'Vilka rutor ligger i öppna listan direkt efter att {o1} har tagits ut?',
                [step('Inlagda men inte uttagna', ratt + '.')],
                sorted([alt(ratt, True, 'Rätt: grannarna till start och till ' + o1 + ' som inte har tagits ut.')] +
                       [alt(t, False, 'Jämför med grannarna till start och till ' + o1 + '. Väggar och uttagna rutor ligger inte i listan.') for t in fel],
                       key=lambda x: x['txt']),
                'Öppna listan innehåller rutor som har lagts in men inte tagits ut.', tn[0])
        mn = min(fv(c) for c in kvar)
        b = num(f'Hur många av rutorna i öppna listan har f(n) = {mn}?',
                [step('f(n) för rutorna i öppna listan', ', '.join(f'f({A.cname(c)}) = {fv(c)}' for c in kvar) + '.')],
                sum(1 for c in kvar if fv(c) == mn), 'Räkna f(n) = g(n) + h(n) för varje ruta i listan.', tn[1])
        parts = [a, b]
    return K.kg_task(old['id'], old['omr'], old['familj'], intro, parts, 'A* tar alltid ut rutan med lägst f(n).',
                     old['formaga']), rows


def g_girig(old, fro, typ):
    def villkor(rows, rng):
        s, goal = A.parse(rows)
        nb = A.neigh(rows, s)
        hs = sorted(A.manhattan(c, goal) for c in nb)
        if len(nb) < (3 if typ == '2.75' else 2) or hs[0] == hs[1]:
            return None
        return nb
    rows, nb = sok(fro, villkor, hörn='inre' if typ == '2.75' else None, vagg=(0.18, 0.3))
    s, goal = A.parse(rows)
    nb = sorted(nb, key=A.cname)
    h = {c: A.manhattan(c, goal) for c in nb}
    forst = min(nb, key=lambda c: (h[c], A.cname(c)))
    tn = [x['traningsniva'] for x in old['spelDelar']]
    intro = maze(rows, s, goal) + p('Labyrinten söks igenom med girig bäst först (h(n) = Manhattanavstånd).')
    vagg = [c for c in [(s[0] + dr, s[1] + dc) for dr, dc in A.STD] if 0 <= c[0] < len(rows) and 0 <= c[1] < len(rows[0])
            and rows[c[0]][c[1]] == '#']
    alts = [alt(A.cname(c), c == forst, f'h({A.cname(c)}) = {h[c]}' + ('. Lägst h(n), så den tas ut först.' if c == forst else
                f', högre än h({A.cname(forst)}) = {h[forst]}.')) for c in nb]
    if vagg and len(alts) < 4:
        alts.append(alt(A.cname(vagg[0]), False, f'{A.cname(vagg[0])} är en vägg och läggs aldrig i öppna listan.'))
    alts = sorted(alts, key=lambda x: x['txt'])
    a_val = val('Vilken ruta tar girig bäst först ut efter start?',
                [step('Girig bäst först väljer lägst h(n)', ', '.join(f'h({A.cname(c)}) = {h[c]}' for c in nb) + '.')], alts,
                'Jämför grannarnas Manhattanavstånd till målet.', tn[0] if typ == '2.48' else tn[1])
    h_num = num('Vilket h(n)-värde har den rutan?',
                [step('h(n) = radskillnad + kolumnskillnad', f'{A.cname(forst)} till målet {A.cname(goal)}: '
                      f'{abs(forst[0] - goal[0])} + {abs(forst[1] - goal[1])} = {h[forst]}.')], h[forst],
                'Räkna rader och kolumner till målet.', tn[-1])
    if typ == '2.75':
        a = num('Hur många grannar har start?', [step('Öppna rutor runt start', ', '.join(names(nb)) + '.')], len(nb),
                'Titta uppåt, åt höger, nedåt och åt vänster. Väggar räknas inte.', tn[0])
        parts = [a, a_val, h_num]
    else:
        parts = [a_val, h_num]
    return K.kg_task(old['id'], old['omr'], old['familj'], intro, parts, 'Girig bäst först väljer lägst h(n).',
                     old['formaga']), rows


def g_bfs(old, fro):
    def villkor(rows, rng):
        b = A.bfs(rows)['path']
        uc, up = A.ucs_grid(rows)
        bc = A.path_cost(rows, b)
        return dict(b=b, bc=bc, uc=uc, up=up) if bc > uc else None
    rows, r = sok(fro, villkor, terr='3333', vagg=(0.15, 0.25))
    s, goal = A.parse(rows)
    intro = maze(rows, s, goal) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←). ' + kost_text(rows)
                                    + ' BFS bryr sig inte om kostnaden, bara om antalet steg.')
    tn = [x['traningsniva'] for x in old['spelDelar']]
    a = num('Vad kostar vägen som BFS hittar?', [step('BFS hittar en väg med färst steg', pil(names(r['b'])) + '.'),
                                                 step('Summera kostnaderna', f'{summa(rows, r["b"])} = {r["bc"]}.')],
            r['bc'], 'Hitta vägen med färst steg och lägg ihop kostnaderna.', tn[0])
    b = num('Vad kostar den billigaste vägen?', [step(runt(rows, r['b'], r['up']), pil(names(r['up'])) + '.'),
                                                 step('Summera kostnaderna', f'{summa(rows, r["up"])} = {r["uc"]}.')],
            r['uc'], 'Finns det en väg runt leran?', tn[1])
    c = byt_i(old['spelDelar'][2], [(r'Här kostar BFS-vägen \d+, men den billigaste vägen bara \d+\.',
                                      f'Här kostar BFS-vägen {r["bc"]}, men den billigaste vägen bara {r["uc"]}.'),
                                     (r'Här är BFS-vägen dyrare: \d+ mot \d+\.',
                                      f'Här är BFS-vägen dyrare: {r["bc"]} mot {r["uc"]}.')])
    return K.kg_task(old['id'], old['omr'], old['familj'], intro, [a, b, c], 'BFS hittar färst steg, inte lägst kostnad.',
                     old['formaga']), rows


OMBYGG = {
    '2.51': lambda o: g_ghf(o, 2051, 30, rak=True),
    '2.25': lambda o: g_ghf(o, 2025, 31, terr='333', delar=('g', 'f')),
    '2.29': lambda o: g_vikt(o, 2029, '2.29'), '2.44': lambda o: g_vikt(o, 2044, '2.44'),
    '2.53': lambda o: g_vikt(o, 2053, '2.53'), '2.63': lambda o: g_vikt(o, 2063, '2.63'),
    '2.27': lambda o: g_girig_astar(o, 2027, '2.27'), '2.42': lambda o: g_girig_astar(o, 2042, '2.42'),
    '2.108': lambda o: g_girig_astar(o, 2108, '2.108'),
    '2.28': lambda o: g_astar(o, 2028, '2.28'), '2.55': lambda o: g_astar(o, 2055, '2.55'),
    '2.57': lambda o: g_astar(o, 2057, '2.57'),
    '2.48': lambda o: g_girig(o, 2048, '2.48'), '2.75': lambda o: g_girig(o, 2075, '2.75'),
    '1.104': lambda o: g_bfs(o, 1104),
}
INNEHALL = {'t', 'spelIntro', 's', 'ledtrad', 'spelDelar', 'rättSvar', 'tolerans', 'svarFormat', 'svarEnhet',
            'svarEtiketter', 'svarsstruktur', 'svarstyp'}
DELMETA = {'niva', 'traningsniva', 'poang', 'etikett'}


def ombyggd(old):
    ny, rows = OMBYGG[old['id']](old)
    ut = copy.deepcopy(old)
    for k in INNEHALL:
        if k in ny:
            ut[k] = ny[k]
    assert len(ut['spelDelar']) == len(old['spelDelar']), old['id']
    for dn, do in zip(ut['spelDelar'], old['spelDelar']):
        for k in DELMETA:
            if k in do:
                dn[k] = do[k]
    return ut, rows


# ---------------------------------------------------------------- nya g/h/f-uppgifter

NYA = []
for i in range(30):
    nr = 123 + i
    L = ['P', 'P', 'Q', 'P', 'R', 'P', 'X', 'P'][i % 8]
    NYA.append((f'2.{nr}', L, i))


def ny_ghf(id_, L, i):
    rows, (mark,) = vald_karta(id_)
    # g(n) går runt väggar eller genom terräng: C enligt AI_NIVAINDELNING (rättat 2026-11-26), h(n) är E.
    parts, gv, hv = ghf_delar(rows, mark, L, (3, 1, 3))
    if any(ch in TERR for row in rows for ch in row):
        girig, astar = A.greedy(rows)['path'], A.astar(rows)['path']
        cg, ca = A.path_cost(rows, girig), A.path_cost(rows, astar)
        assert len(astar) > len(girig) and ca < cg
        fraga = ('Hur mycket lägre blir vägkostnaden med A* än med girig bäst först?' if i % 2 else
                 'Hur många extra steg går A* på den billigare vägen jämfört med girig bäst först?')
        svar = cg-ca if i%2 else len(astar)-len(girig)
        parts.append(num(fraga, [step('Vägen med girig bäst först', f'{pil(names(girig))}. {len(girig)-1} steg, kostnad {cg}.'),
                                step('Vägen med A*', f'{pil(names(astar))}. {len(astar)-1} steg, kostnad {ca}.')],
                         svar, 'Spåra båda sökningarna. Skriv antal steg och kostnad var för sig.', 3))
    u = K.kg_task(id_, 'astar_varden', 'g, h och f för en ruta', ghf_intro(rows, mark, L, i), parts,
                  'g(n) följer gångarna från start, h(n) räknas rakt till målet.', ['procedur'], 1)
    return u, rows


# ---------------------------------------------------------------- enklare: g(n), h(n) och f(n) i flera rutor (E)
#
# Användaren 2026-11-26: ”Jag saknar uppgifter med A* och greedy där uppgiften är 'Bestäm f(n), g(n) och h(n)' i lite
# olika rutor … jag vill ha lite enklare också där man bara ska bestämma dessa värden i olika rutor.”
# Två eller tre markerade rutor i en labyrint utan terräng. Rutor där g(n) efterfrågas nås utan omväg (E enligt
# AI_NIVAINDELNING); väggarna finns ändå, och vägen till målet går runt dem.

BOKSTAVER = [('P', 'Q', 'R'), ('K', 'L', 'M'), ('X', 'Y', 'Z'), ('T', 'U', 'V')]
ASTAR_FLERA = ('Vägen söks med A*. g(n) är kostnaden för den billigaste vägen från start till rutan n, och h(n) är '
               'Manhattanavståndet från n till målet. Varje steg kostar 1.')


def g_del(rows, c, L, tn):
    gv, vag = billigast(rows, c)
    return num(f'Bestäm g(n) för rutan {L}.',
               [step('g(n) = kostnaden för den billigaste vägen från start till n', g_rad(vag, L, A.cname(c)))], gv,
               G_LED_RAK.format(L=L), tn)


def h_del(rows, c, L, tn):
    _, goal = A.parse(rows)
    hv = A.manhattan(c, goal)
    return num(f'Bestäm h(n) för rutan {L}.',
               [step('h(n) = radskillnad + kolumnskillnad till målet',
                     f'{L} ligger i {A.cname(c)} och målet i {A.cname(goal)}: {abs(c[0] - goal[0])} + {abs(c[1] - goal[1])} '
                     f'= {hv}. Väggarna räknas inte.')], hv,
               f'Räkna rader och kolumner från {L} till målet, som om väggarna inte fanns.', tn)


def f_text(rows, c, L):
    _, goal = A.parse(rows)
    gv, vag = billigast(rows, c)
    hv = A.manhattan(c, goal)
    return gv, hv, f'f({L}) = g({L}) + h({L}) = {gv} + {hv} = {gv + hv}'


def f_del(rows, c, L, tn, g_visad):
    """f(n) för en ruta. Har g(n) för rutan inte efterfrågats i en tidigare del visar facit också g och h."""
    _, goal = A.parse(rows)
    gv, hv, rad = f_text(rows, c, L)
    steg = [step('h(n): radskillnad + kolumnskillnad till målet',
                 f'{L} ligger i {A.cname(c)} och målet i {A.cname(goal)}: {abs(c[0] - goal[0])} + {abs(c[1] - goal[1])} = {hv}.'),
            step('f(n) = g(n) + h(n)', rad + '.')]
    if not g_visad:
        _, vag = billigast(rows, c)
        steg = [step('g(n): stegen från start', g_rad(vag, L, A.cname(c)))] + steg
    return num(f'Bestäm f(n) för rutan {L}.', steg, gv + hv,
               f'Bestäm g(n) och h(n) för {L} och lägg ihop dem.', tn)


def rutval_alts(celler, varde, namn, vinnare, forklaring):
    return [alt(f'Rutan {L}', c == vinnare,
                f'{namn}({L}) = {varde[c]}' + ('. Det är lägst, så ' + forklaring if c == vinnare else
                                               f', högre än {namn}({dict((c2, L2) for c2, L2 in celler)[vinnare]}) = '
                                               f'{varde[vinnare]}.'))
            for c, L in celler]


def flera_villkor(mall):
    """Välj markerade rutor. A*-mallarna kräver rutor utan omväg där g(n) efterfrågas."""
    def v(rows, rng):
        s, goal = A.parse(rows)
        if any(ch in TERR for x in rows for ch in x):
            return None
        rak = [c for c in oppna(rows) if A.manhattan(s, c) >= 2 and A.manhattan(c, goal) >= 1 and rak_till(rows, c)]
        nas = [c for c in oppna(rows) if billigast(rows, c)[1] and A.manhattan(c, goal) >= 1]
        n = 2 if mall in ('T3', 'G2') else 3
        pool = rak if mall in ('T1', 'T2', 'T3', 'G2') else nas
        if len(pool) < n + 2:
            return None
        for _ in range(60):
            cs = rng.sample(pool, n)
            if any(A.manhattan(a, b) < 2 for i, a in enumerate(cs) for b in cs[i + 1:]):
                continue
            h = [A.manhattan(c, goal) for c in cs]
            f = [billigast(rows, c)[0] + A.manhattan(c, goal) for c in cs]
            if mall == 'T1':
                # g för P, h för Q, f för R: R:s väg ska ha minst tre steg, så att f inte blir för litet
                if billigast(rows, cs[2])[0] < 3 or len(set(h)) < 2:
                    continue
            if mall == 'T2' and (f[0] == f[1] or len(set(h)) < 2):
                continue
            if mall == 'T3' and (f[0] == f[1]):
                continue
            if mall == 'G1' and len(set(h)) < 3:
                continue
            if mall == 'G2':
                if h[0] == h[1] or f[0] == f[1] or (h[0] < h[1]) == (f[0] < f[1]):
                    continue
            return cs
        return None
    return v


def ny_flera(id_, fro, mall, bokst, i):
    rows, cs = (vald_karta(id_) if mall.startswith("G") else sok(fro, flera_villkor(mall), vagg=(0.18, 0.3)))
    s, goal = A.parse(rows)
    celler = list(zip(cs, bokst))
    marks = {c: L for c, L in celler}
    ctx = SAMMANHANG[(i * 7 + 3) % len(SAMMANHANG)]
    if mall in ('T1', 'T2', 'T3'):
        omr, familj = 'astar_varden', 'g, h och f för en ruta'
        text = ctx + ' ' + ASTAR_FLERA
        (c1, L1), (c2, L2) = celler[:2]
        if mall == 'T1':
            c3, L3 = celler[2]
            parts = [g_del(rows, c1, L1, 1 if billigast(rows, c1)[0] <= 3 else 2), h_del(rows, c2, L2, 1),
                     f_del(rows, c3, L3, 2, False)]
            led = 'g(n) räknar stegen från start, h(n) räknar rakt till målet, och f(n) är summan.'
        elif mall == 'T2':
            parts = [f_del(rows, c1, L1, 2, False), f_del(rows, c2, L2, 2, False)]
            fv = {c: billigast(rows, c)[0] + A.manhattan(c, goal) for c in cs[:2]}
            vin = min(cs[:2], key=lambda c: fv[c])
            fr = ', '.join(f_text(rows, c, L)[2] for c, L in celler[:2])
            fel_lika = alt('De har samma f(n)', False, f'Nej: {fr}.')
            parts.append(val(f'Vilken av rutorna {L1} och {L2} har lägst f(n)?',
                             [step('Jämför f(n) = g(n) + h(n)', fr + '.')],
                             rutval_alts(celler[:2], fv, 'f', vin, 'A* tar ut den först av de två.') + [fel_lika],
                             'Räkna f(n) för båda rutorna och jämför.', 2))
            led = 'f(n) är g(n) + h(n). Den ruta som har lägst f(n) tas ut först av A*.'
        else:
            parts = [g_del(rows, c1, L1, 1 if billigast(rows, c1)[0] <= 3 else 2), f_del(rows, c1, L1, 2, True),
                     g_del(rows, c2, L2, 1 if billigast(rows, c2)[0] <= 3 else 2), f_del(rows, c2, L2, 2, True)]
            led = 'Räkna stegen från start för g(n) och lägg till Manhattanavståndet till målet för f(n).'
    else:
        omr, familj = 'astar_varden', 'Heuristiken h'
        hv = {c: A.manhattan(c, goal) for c in cs}
        if mall == 'G1':
            namnlista = f'{bokst[0]}, {bokst[1]} och {bokst[2]}'
            text = (ctx + ' Vägen söks med girig bäst först, där h(n) är Manhattanavståndet från rutan n till målet. '
                    f'Just nu ligger rutorna {namnlista} i öppna listan.')
            vin = min(cs, key=lambda c: hv[c])
            hr = ', '.join(f'h({L}) = {hv[c]}' for c, L in celler)
            parts = [h_del(rows, c, L, 1) for c, L in celler]
            parts.append(val('Vilken av rutorna tar girig bäst först ut härnäst?',
                             [step('Girig bäst först tar ut rutan med lägst h(n)', hr + '.')],
                             rutval_alts(celler, hv, 'h', vin, 'den tas ut härnäst.'),
                             'Girig bäst först jämför bara h(n).', 1))
            led = 'Girig bäst först tar alltid ut den ruta i öppna listan som har lägst h(n).'
        else:  # G2: girig bäst först och A* väljer olika
            (c1, L1), (c2, L2) = celler
            text = (ctx + f' Anta att rutorna {L1} och {L2} ligger i öppna listan. h(n) är Manhattanavståndet från rutan n '
                    'till målet och g(n) kostnaden för den billigaste vägen från start till n. Varje steg kostar 1.')
            fv = {c: billigast(rows, c)[0] + hv[c] for c in cs}
            hvin, fvin = min(cs, key=lambda c: hv[c]), min(cs, key=lambda c: fv[c])
            hr = ', '.join(f'h({L}) = {hv[c]}' for c, L in celler)
            fr = ', '.join(f_text(rows, c, L)[2] for c, L in celler)
            parts = [h_del(rows, c1, L1, 1), h_del(rows, c2, L2, 1),
                     val('Vilken av rutorna tar girig bäst först ut först?',
                         [step('Girig bäst först jämför bara h(n)', hr + '.')],
                         rutval_alts(celler, hv, 'h', hvin, 'girig bäst först tar ut den först.'),
                         'Jämför h(n) för rutorna.', 1),
                     val('Vilken av rutorna tar A* ut först?',
                         [step('g(n): stegen från start', ' '.join(g_rad(billigast(rows, c)[1], L, A.cname(c))
                                                                   for c, L in celler)),
                          step('A* jämför f(n) = g(n) + h(n)', fr + '.')],
                         rutval_alts(celler, fv, 'f', fvin, 'A* tar ut den först.'),
                         'Räkna stegen från start till varje ruta, g(n), och lägg till h(n).', 2)]
            led = 'Girig bäst först ser bara h(n). A* räknar också med g(n), vägen hittills.'
    intro = maze(rows, s, goal, marks, extra_legend=[('#fff3b0', 'Markerade rutor')]) + p(text)
    u = K.kg_task(id_, omr, familj, intro, parts, led, ['procedur'], 1)
    return u, rows


FLERA = []
for i in range(20):
    FLERA.append((f'2.{153 + i}', 25300 + i, ['T1', 'T2', 'T3'][i % 3], BOKSTAVER[i % 4], i))
for j in range(16):
    FLERA.append((f'2.{173 + j}', 25500 + j, ['G1', 'G2'][j % 2], BOKSTAVER[(j // 2) % 4], 20 + j))


def efterbehandla(u):
    """f(n)-notation (ai_fgh_n) på allt som kommer från de äldre hjälpfunktionerna."""
    FGH.byt_obj(u)
    for d in u.get('spelDelar') or []:
        FGH.byt_obj(d)
    for k in ('t', 'spelIntro'):
        u[k] = u[k].replace(' Välj ett alternativ.', '')
    return u


def kontroll(u, rows):
    """Svaren räknas om oberoende av mallarna där det går: g/h/f-delar mot labyrinten."""
    s, goal = A.parse(rows)
    walls = sum(x.count('#') for x in rows)
    assert walls >= 2, u['id']
    markerade = {lab: cn for cn, lab in re.findall(
        r'data-cell="([A-Z]\d+)"[^>]*/><rect[^>]*fill="#fff3b0"[^>]*/><text[^>]*>([A-Z])</text>', u['spelIntro'])}
    for d in u['spelDelar']:
        m = re.search(r'Bestäm ([ghf])\(n\) för rutan ([A-Z])\.', d['fraga'])
        if not m:
            continue
        cn = markerade[m.group(2)]
        cell = (ord(cn[0]) - 65, int(cn[1:]) - 1)
        gv, _ = billigast(rows, cell)
        hv = A.manhattan(cell, goal)
        assert d['rättSvar'] == {'g': gv, 'h': hv, 'f': gv + hv}[m.group(1)], (u['id'], d['etikett'])


def main():
    src, bank = BO.las(BANK)
    Q = {u['id']: u for u in bank}
    nya, statistik = {}, []
    for id_ in OMBYGG:
        u, rows = ombyggd(Q[id_])
        efterbehandla(u)
        kontroll(u, rows)
        nya[id_] = u
        statistik.append((id_, len(rows), len(rows[0]), sum(x.count('#') for x in rows)))
    tillagg = []
    jobb = [(a[0], lambda a=a: ny_ghf(*a)) for a in NYA]
    jobb += [(id_, lambda a=(id_, fro, mall, bokst, i): ny_flera(*a)) for id_, fro, mall, bokst, i in FLERA]
    for id_, bygg in jobb:
        u, rows = bygg()
        efterbehandla(u)
        kontroll(u, rows)
        if id_ in Q:            # omkörning: uppgiften finns redan och ersätts på sin plats
            nya[id_] = u
        else:
            tillagg.append(u)
        statistik.append((id_, len(rows), len(rows[0]), sum(x.count('#') for x in rows)))
    for id_, R, C, w in statistik:
        print(f'{id_:6} {R}x{C} väggar {w}')
    ny_src = BO.ersatt(src, nya)
    if tillagg:
        j = ny_src.rindex(']')
        mellan = ''.join(',\n' + BO._dump(u) for u in tillagg)
        ny_src = ny_src[:j].rstrip() + mellan + '\n' + ny_src[j:]
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    print(len(nya), 'ombyggda,', len(tillagg), 'nya', '(skrivet)' if '--skriv' in sys.argv else '(torrkörning)')
    if '--skriv' in sys.argv:
        BO.skriv(BANK, ny_src)


if __name__ == '__main__':
    main()
