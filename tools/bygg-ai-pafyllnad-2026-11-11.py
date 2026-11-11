"""AI-banken 2026-11-11, tredje omgången.

1. Lärarkommentarer i Uppgiftslabbets felrapport 09:31 (AI 1.01, 1.03, 1.04):
   enhetlig inledning ”Labyrinten/Trädet/Grafen/Spelträdet söks igenom med …”,
   grön startnod och röda målnoder i sökträden, tydligare text om vad som läggs
   in och tas ut, snygga tabeller (class="data").
2. 26 nya uppgifter i bankens tio områden. Alla svar räknas fram med
   tools/ai_sokalgoritmer.py och kontrolleras dessutom oberoende i
   tools/ai-pafyllnad-2026-11-11.test.js.

Kör från repots rot: python tools/bygg-ai-pafyllnad-2026-11-11.py
Skriptet är idempotent: ändringar i befintliga uppgifter görs bara en gång och
nya uppgifter ersätts om de redan finns.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ai_figurer import (tab, step, facit, maze, search_tree, weighted_graph,  # noqa: E402
                        game_tree, box_queue, box_stack)
import ai_sokalgoritmer as A  # noqa: E402

BANK = 'uppgifterai.js'
NIVA = {1: 'E', 2: 'E', 3: 'C', 4: 'C', 5: 'A'}
POANG = {'E': '1/0/0', 'C': '0/1/0', 'A': '0/0/1'}
ARROW = ' → '


def names(cells):
    return [A.cname(c) for c in cells]


def lista(xs):
    return ', '.join(xs)


def pil(xs):
    return ARROW.join(xs)


# ---------------------------------------------------------------------------
# Del- och uppgiftsbyggare
# ---------------------------------------------------------------------------

def alt(txt, ratt, kommentar):
    return {'txt': txt, 'ratt': ratt, 'kommentar': kommentar}


def alt_html(alts):
    """Alternativ som A., B., … i samma form som appens egen alternativvisning.
    <ol> visas i appen som a), b), … och krockar då med deluppgifternas bokstäver."""
    return ''.join(f'<p class="ul-alt"><strong>{chr(65 + i)}.</strong> {a["txt"]}</p>' for i, a in enumerate(alts))


def part(fraga, steps, svar, ledtrad, tn, alts=None):
    alts = alts or []
    niva = NIVA[tn]
    return {
        'fraga': fraga,
        's': facit(steps, svar, alts),
        'ledtrad': f'<p>{ledtrad}</p>',
        'alternativ': alts,
        'visaAlternativ': bool(alts),
        'traningsniva': tn,
        'arbetsinsats': 1,
        'niva': niva,
        'poang': POANG[niva],
        'miniräknare': True,
        'geogebra': False,
        'självrättning': False,
        'spel': False,
        'svarstyp': 'manuell',
        'rättSvar': None,
        'tolerans': None,
    }


def task(id_, omr, familj, intro, parts, ledtrad, formaga, arbetsinsats=2):
    t = intro
    s = '<div class="facit-v2 facit-stegvis">'
    for i, p in enumerate(parts):
        et = chr(97 + i)
        p['etikett'] = et
        fr = p['fraga']
        assert fr.startswith('<p>'), id_
        t += '<p>' + et + ') ' + fr[3:]
        if p['alternativ']:
            t += alt_html(p['alternativ'])
        s += f'<div class="facit-del"><span class="facit-mark">{et})</span><div class="facit-arbete">{p["s"]}</div></div>'
    s += '</div>'
    nivaer = [p['niva'] for p in parts]
    niva = 'A' if 'A' in nivaer else 'C' if 'C' in nivaer else 'E'
    sum3 = [sum(int(p['poang'].split('/')[k]) for p in parts) for k in range(3)]
    return {
        'id': id_, 'kap': int(id_.split('.')[0]), 'omr': omr, 'niva': niva,
        'poang': '/'.join(map(str, sum3)), 'familj': familj, 'formaga': formaga,
        'traningsniva': max(p['traningsniva'] for p in parts), 'arbetsinsats': arbetsinsats,
        'miniräknare': True, 'geogebra': False, 'spel': False, 'självrättning': False,
        'svarstyp': 'manuell', 'rättSvar': None, 'tolerans': None,
        't': t, 's': s, 'ledtrad': f'<p>{ledtrad}</p>', 'spelIntro': intro,
        'spelDelning': 'deluppgifter', 'spelDelar': parts,
    }


def p(x):
    return f'<p>{x}</p>'


# ---------------------------------------------------------------------------
# Del 1: lärarkommentarerna – enhetliga formuleringar i befintliga uppgifter
# ---------------------------------------------------------------------------

ASTAR_TIE = 'Vid lika f väljs lägst h, och vid lika h den ruta som kommer först i bokstavsordning.'
ASTAR_GH = 'Labyrinten söks igenom med A* (h = Manhattanavstånd till målet, g = kortaste vägkostnad från start).'

INTRO_BYTEN = {
    '1.01': [('<p>BFS. Ordning: ↑ → ↓ ←.</p>', '<p>Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).</p>')],
    '1.06': [('<p>BFS. Ordning: ↑ → ↓ ←.</p>', '<p>Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).</p>')],
    '1.08': [('<p>BFS. Ordning: ↑ → ↓ ←.</p>', '<p>Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).</p>')],
    '1.02': [('<p>DFS. Ordning: ↑ → ↓ ←.</p>', '<p>Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).</p>')],
    '1.07': [('<p>DFS. Ordning: ↑ → ↓ ←.</p>', '<p>Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).</p>')],
    '2.01': [('<p>A*. Använd Manhattanavstånd och kortaste vägkostnad g.</p>', p(ASTAR_GH))],
    '2.06': [('<p>A*. Manhattanavstånd och kortaste vägkostnad g.</p>', p(ASTAR_GH))],
    '2.07': [('<p>A*. Manhattanavstånd och kortaste vägkostnad g.</p>', p(ASTAR_GH))],
    '2.08': [('<p>A*. Manhattanavstånd och kortaste vägkostnad g.</p>', p(ASTAR_GH))],
    '2.02': [('<p>A*. Manhattanavstånd. Vid lika f: lägst h, sedan rutnamn.</p>',
              p('Labyrinten söks igenom med A* (h = Manhattanavstånd). ' + ASTAR_TIE))],
    '2.09': [('<p>Utgå från sökläget. Manhattanavstånd; vid lika f väljs lägst h.</p>',
              p('Labyrinten söks igenom med girig bäst först och med A* (h = Manhattanavstånd). Vid lika f väljs lägst h. '
                'Bilden och tabellen visar hur långt sökningen har kommit.'))],
    '2.10': [('<p>Is: 4 per ruta. Backe: 5. Vanlig väg och mål: 1. Start: 0. A* med Manhattanavstånd.</p>',
              p('Labyrinten söks igenom med A* (h = Manhattanavstånd). Att gå in i en isruta kostar 4, '
                'en backruta 5 och en vit ruta eller målet 1. Start kostar 0.'))],
    '2.11': [('<p>Is: 4 per ruta. Vanlig väg och mål: 1. Start: 0. Manhattanavstånd.</p>',
              p('Labyrinten söks igenom med A* (h = Manhattanavstånd). Att gå in i en isruta kostar 4 '
                'och en vit ruta eller målet 1. Start kostar 0.'))],
    '1.04': [('<p>BFS. Start S, mål G. Vänster gren först. Skriv kön med nästa uttag till vänster.</p>',
              p('Trädet söks igenom med BFS (vänster gren först). I tabellen skrivs kön med nästa nod som tas ut längst till vänster.'))],
    '1.05': [('<p>DFS. Start S, mål G. Vänster gren först. Skriv kön med nästa uttag till höger.</p>',
              p('Trädet söks igenom med DFS (vänster gren först). Noderna sparas i en stack. '
                'I tabellen skrivs stacken med nästa nod som tas ut längst till höger.'))],
    '1.09': [('<p>Start A. Röda noder är mål. Barn läggs i bokstavsordning.</p>',
              p('Trädet söks igenom med BFS och med DFS. En nods barn läggs in i kön eller stacken i bokstavsordning. '
                'Sökningen stoppar när ett mål tas ut.'))],
    '3.03': [('<p>Alfa–beta. Sök från vänster till höger.</p>',
              p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))],
    '3.04': [('<p>Sök från vänster till höger.</p>', p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))],
    '3.05': [('<p>Sök från vänster till höger.</p>', p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))],
    '1.03': [('<p>in A · in B · in C · ut · in D · ut · ut · in E · ut · ut</p>',
              p('Noder läggs in och tas ut enligt följande:') +
              p('lägg in A, B och C → ta ut en nod → lägg in D → ta ut två noder → lägg in E → ta ut två noder.') +
              p('Samma steg görs en gång med en FIFO-kö och en gång med en stack.'))],
    '2.04': [('<p>Lägsta tal tas ut först.</p><p>in A(5) · in B(3) · in C(7) · ut · in D(2) · in E(6) · ut · ut · in F(1) · ut · ut · ut</p>',
              p('Noder läggs in i och tas ut ur en prioritetskö enligt följande. Talet inom parentes är nodens värde, '
                'och noden med lägst värde tas ut först.') +
              p('Lägg in A(5), B(3) och C(7) → ta ut en nod → lägg in D(2) och E(6) → ta ut två noder → '
                'lägg in F(1) → ta ut tre noder.'))],
    '2.05': [('<table>', p('Tabellen visar tre rutor som ligger i öppna listan under en sökning.') + '<table>')],
}
# Minimaxträden saknade inledning; lägg till samma typ av mening.
INTRO_TILLAGG = {'3.01': p('Spelträdet söks igenom med minimax.'), '3.02': p('Spelträdet söks igenom med minimax.')}

FRAGA_BYTEN = {
    '1.03': [('<p>I vilken ordning tas noderna ut ur en FIFO-kö?</p>', '<p>Stegen görs med en FIFO-kö. I vilken ordning tas noderna ut?</p>'),
             ('<p>I vilken ordning tas noderna ut ur en stack?</p>', '<p>Stegen görs med en stack. I vilken ordning tas noderna ut?</p>')],
    '1.04': [('<p>Fyll i tabellen. Startkö: S.</p>', '<p>Fyll i tabellen tills målet tas ut.</p>')],
    '1.05': [('<p>Fyll i tabellen. Startkö: S.</p>', '<p>Fyll i tabellen tills målet tas ut.</p>'),
             ('<p>Vilka noder ligger kvar i kön när målet tas ut?</p>', '<p>Vilka noder ligger kvar i stacken när målet tas ut?</p>')],
}

LEDTRAD_BYTEN = {  # huvudledtrådar som var kopierade från labyrintuppgifterna
    '1.03': 'Skriv upp vad som ligger i kön, respektive stacken, efter varje steg.',
    '1.04': 'En nod som läggs in hamnar sist i kön. Nästa nod som tas ut är den som står först.',
    '1.05': 'Barnen läggs på stacken så att det vänstra barnet hamnar överst. Nästa nod som tas ut är den som ligger överst.',
    '2.04': 'Skriv upp vilka noder som ligger i kön, med sina värden, efter varje steg.',
    '2.05': 'f är summan av g och h. Girig bäst först jämför bara h.',
}

TREE_104 = dict(nodes={'S': (160, 35), 'A': (80, 110), 'B': (240, 110), 'C': (40, 185), 'D': (120, 185),
                       'E': (200, 185), 'F': (280, 185), 'G': (200, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'), ('E', 'G')],
                start='S', goals=['G'], width=320,
                title='Sökträd: S har barnen A och B, A har C och D, B har E och F, E har G. Start S är grön och målet G är rött.')
TREE_109 = dict(nodes={'A': (210, 35), 'B': (110, 110), 'C': (310, 110), 'D': (60, 185), 'E': (160, 185),
                       'F': (260, 185), 'G': (360, 185), 'H': (25, 260), 'I': (65, 260), 'J': (105, 260),
                       'K': (235, 260), 'L': (285, 260)},
                edges=[('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('D', 'H'), ('D', 'I'),
                       ('D', 'J'), ('F', 'K'), ('F', 'L')],
                start='A', goals=['D', 'K'], width=400,
                title='Sökträd med start A (grön) och två mål, D och K (röda).')


def table_class(html):
    """Ger äldre tabeller bankens tabellstil och vänsterställda celler, som tab()."""
    def fix(m):
        t = m.group(0).replace('<table>', '<table class="data">', 1)
        return t.replace('<th>', '<th style="text-align:left">').replace('<td>', '<td style="text-align:left">')
    return re.sub(r'<table>[\s\S]*?</table>', fix, html)


M203 = ['S55G', '.##.', '....']


def rebuild_203(u):
    """2.03 utan UCS: girig bäst först jämförs med A* (användarbeslut 2026-11-11)."""
    s_, g_ = A.parse(M203)
    gr, ast = A.greedy(M203), A.astar(M203)
    assert names(gr['path']) == ['A1', 'A2', 'A3', 'A4'] and gr['cost'] == 11
    assert names(ast['path']) == ['A1', 'B1', 'C1', 'C2', 'C3', 'C4', 'B4', 'A4'] and A.path_cost(M203, ast['path']) == 7
    svg = re.search(r'<svg[\s\S]*?</svg>', u['spelIntro']).group(0)
    intro = svg + p('Labyrinten söks igenom med girig bäst först och med A* (h = Manhattanavstånd). '
                    'Att gå in i en ruta med en femma kostar 5 och att gå in i en vit ruta eller målet kostar 1. Start kostar 0.')
    a = part(p('Ange vägen och kostnaden med girig bäst först.'),
             [step('Girig bäst först jämför bara h', 'Från A1 har A2 h = 2 och B1 h = 4. A2 väljs, sedan A3 (h = 1) och målet.'),
              step('Summera kostnaderna längs vägen', 'A2 och A3 kostar 5 var och målet 1: 5 + 5 + 1 = 11.')],
             'A1 → A2 → A3 → A4, kostnad 11.', 'Jämför bara h när nästa ruta väljs.', 4)
    b = part(p('Ange vägen och kostnaden med A*.'),
             [step('A* jämför f = g + h', 'Från start får A2 f = 5 + 2 = 7 och B1 f = 1 + 4 = 5. B1 tas ut först.'),
              step('Den övre vägen blir för dyr', 'A3 får g = 5 + 5 = 10 och f = 10 + 1 = 11. Rutorna längs den nedre vägen har f = 7 hela vägen, så A* följer den till målet.'),
              step('Summera kostnaderna längs vägen', 'Sju steg som kostar 1 var ger kostnaden 7.')],
             'A1 → B1 → C1 → C2 → C3 → C4 → B4 → A4, kostnad 7.', 'Räkna f = g + h, där g är den samlade kostnaden hittills.', 4)
    c = part(p('Varför blir kostnaderna olika?'),
             [step('Girig bäst först jämför bara h', 'Den ser inte att rutorna med femmor är dyra, eftersom den inte räknar med vad vägen hittills har kostat.'),
              step('A* räknar också med kostnaden hittills', 'Med f = g + h får den dyra övre vägen högre f än den längre men billigare vägen runt väggarna.')],
             'Girig bäst först tar inte hänsyn till kostnaden hittills, men det gör A*. Den kortaste vägen i antal steg behöver inte vara billigast.',
             'Vad tar respektive algoritm hänsyn till när nästa ruta väljs?', 4)
    ny = task('2.03', 'viktade_vagar', u['familj'], intro, [a, b, c],
              'Jämför kostnaden för den korta övre vägen med den längre vägen runt väggarna.', ['procedur', 'resonemang'], 3)
    # Tidigare område och delmoment (omgrupperingen 2026-11-11) följer med, så att elevresultat flyttas.
    for k in ('omrTidigare', 'familjTidigare'):
        if k in u:
            ny[k] = u[k]
    return ny


# Kunskapsgymmets svarsinstruktion i parentes (bygg-ai-sjalvrattning-2026-11-11.py) står efter
# frågan i delkortet. Den ska inte hindra att kontrollen vid omkörning känner igen frågan.
KG_INSTR = re.compile(r' \((?:Skriv|Svara|Ange noden|Ta beskärningarna)[^)]*\)(?=</p>)')


def utan_kg(f):
    return KG_INSTR.sub('', f)


def revidera(u):
    i = u['id']
    if i == '2.03':
        return rebuild_203(u)
    for old, new in INTRO_BYTEN.get(i, []):
        if new.replace('<table>', '') in u['spelIntro']:
            continue
        assert u['t'].count(old) == 1 and u['spelIntro'].count(old) == 1, (i, old)
        u['t'] = u['t'].replace(old, new)
        u['spelIntro'] = u['spelIntro'].replace(old, new)
    if i in INTRO_TILLAGG and INTRO_TILLAGG[i] not in u['spelIntro']:
        u['spelIntro'] += INTRO_TILLAGG[i]
        assert u['t'].endswith('</div>', 0, u['t'].index('<p>a)')), i
        k = u['t'].index('<p>a)')
        u['t'] = u['t'][:k] + INTRO_TILLAGG[i] + u['t'][k:]
    for old, new in FRAGA_BYTEN.get(i, []):
        hit = [d for d in u['spelDelar'] if old in d['fraga']]
        if not hit:
            assert any(new in utan_kg(d['fraga']) for d in u['spelDelar']), (i, old)
            continue
        hit[0]['fraga'] = hit[0]['fraga'].replace(old, new)
        u['t'] = u['t'].replace('<p>' + hit[0]['etikett'] + ') ' + old[3:], '<p>' + hit[0]['etikett'] + ') ' + new[3:])
    if i in LEDTRAD_BYTEN:
        u['ledtrad'] = p(LEDTRAD_BYTEN[i])
    if i in ('1.04', '1.05'):
        stack = i == '1.05'
        rubr = 'Stacken efter uttaget' if stack else 'Kön efter uttaget'
        tom = tab(['Tas ut', rubr], [['–', 'S']] + [['…', '…']] * (7 if stack else 8))
        u['t'] = re.sub(r'<table>[\s\S]*?</table>', tom, u['t'], count=1)
        d = u['spelDelar'][0]
        d['fraga'] = re.sub(r'<table>[\s\S]*?</table>', tom, d['fraga'], count=1)
        # facit: samma kolumnrubrik, startrad och tabellstil
        for obj in (u, d):
            obj['s'] = obj['s'].replace('<table><thead><tr><th>Tas ut</th><th>Kön efter uttaget</th></tr></thead><tbody>',
                                        '<table><thead><tr><th>Tas ut</th><th>' + rubr + '</th></tr></thead><tbody><tr><td>–</td><td>S</td></tr>')
        svg = search_tree(**TREE_104)
        for key in ('t', 'spelIntro'):
            u[key] = re.sub(r'<svg[\s\S]*?</svg>', lambda m: svg, u[key], count=1)
    if i == '1.09':
        svg = search_tree(**TREE_109)
        for key in ('t', 'spelIntro'):
            u[key] = re.sub(r'<svg[\s\S]*?</svg>', lambda m: svg, u[key], count=1)
    # Alternativlistor i huvudtexten: A., B., … i stället för <ol> (se alt_html).
    for d in u['spelDelar']:
        if d.get('alternativ'):
            lst = '<ol type="A">' + ''.join(f'<li>{a["txt"]}</li>' for a in d['alternativ']) + '</ol>'
            if lst in u['t']:
                assert u['t'].count(lst) <= 2, i
                u['t'] = u['t'].replace(lst, alt_html(d['alternativ']), 1)
    assert '<ol type="A">' not in u['t'], i
    # Alla tabeller i AI-banken får bankens tabellstil.
    for key in ('t', 's', 'spelIntro'):
        u[key] = table_class(u[key])
    for d in u['spelDelar']:
        for key in ('fraga', 's'):
            d[key] = table_class(d[key])
    return u


# ---------------------------------------------------------------------------
# Del 2: nya uppgifter
# ---------------------------------------------------------------------------

def t110():
    intro = (box_queue(['K', 'M', 'P'], 'FIFO-kö med K först, sedan M och sist P.') +
             p('Bilden visar en FIFO-kö. Sedan görs följande steg:') +
             p('lägg in R → ta ut en nod → ta ut en nod → lägg in S.'))
    q = ['K', 'M', 'P']
    rows = [['Från början', 'K M P']]
    out = []
    for op in ['+R', '-', '-', '+S']:
        if op[0] == '+':
            q.append(op[1])
            rows.append([f'Lägg in {op[1]}', ' '.join(q)])
        else:
            out.append(q.pop(0))
            rows.append([f'Ta ut {out[-1]}', ' '.join(q)])
    assert out == ['K', 'M'] and q == ['P', 'R', 'S']
    a = part(p('Vilken nod tas ut först? Välj ett alternativ.'),
             [step('FIFO: först in, först ut',
                   'Den nod som har legat längst i kön tas ut först. Det är K, som står först i kön.')],
             'K.', 'Vilken nod har legat längst i kön?', 1,
             [alt('K', True, 'K står först i kön och har väntat längst. I en FIFO-kö tas den ut först.'),
              alt('P', False, 'P står sist av de tre från början. Att ta ut den sist inlagda noden gäller en stack, inte en FIFO-kö.'),
              alt('R', False, 'R läggs in i kön sist och hamnar längst bak.')])
    b = part(p('Vilka noder ligger i kön när alla fyra stegen är gjorda? Skriv dem i ordning, med den som står först i kön till vänster.'),
             [step('Nya noder hamnar sist och uttag sker först i kön', tab(['Steg', 'Kön efter steget'], rows)),
              step('Två uttag tar bort K och M', 'R och S läggs in bakom P, så P står först.')],
             'P, R, S.', 'Skriv upp kön efter varje steg. En ny nod hamnar längst till höger.', 1)
    return task('1.10', 'ko_stack', 'FIFO-kö i en bild', intro, [a, b],
                'I en FIFO-kö läggs nya noder in längst bak och tas ut längst fram.', ['procedur'], 1)


def t111():
    intro = (box_stack(['D', 'H', 'B'], 'Stack med D nederst, H i mitten och B överst.') +
             p('Bilden visar en stack. Sedan görs följande steg:') +
             p('ta ut en nod → lägg in X → lägg in Y → ta ut en nod → ta ut en nod.'))
    st, out, rows = ['D', 'H', 'B'], [], [['Från början', 'D H B']]
    for op in ['-', '+X', '+Y', '-', '-']:
        if op[0] == '+':
            st.append(op[1])
            rows.append([f'Lägg in {op[1]}', ' '.join(st)])
        else:
            out.append(st.pop())
            rows.append([f'Ta ut {out[-1]}', ' '.join(st)])
    assert out == ['B', 'Y', 'X'] and st == ['D', 'H']
    a = part(p('I vilken ordning tas noderna ut?'),
             [step('LIFO: sist in, först ut', 'Den översta noden tas alltid ut. I tabellen står stacken med den översta noden längst till höger.',
                   tab(['Steg', 'Stacken efter steget'], rows))],
             'B, Y, X.', 'Den nod som ligger överst tas ut. En ny nod läggs överst.', 1)
    b = part(p('Vilken nod ligger överst i stacken när alla stegen är gjorda?'),
             [step('X och Y tas ut igen', 'X och Y läggs överst men tas ut i de två sista stegen. Kvar finns D och H, med H överst.')],
             'H.', 'Vilka noder lades in och togs ut igen?', 1)
    c = part(p('Vilka påståenden stämmer? Välj alla som stämmer.'),
             [step('En stack tar ut den senast inlagda noden', 'Därför fortsätter en sökning med stack från den nod som hittades senast och går på djupet, som DFS.'),
              step('En FIFO-kö tar ut den äldsta noden', 'Det gör att BFS undersöker noderna nivå för nivå.')],
             'A och B.', 'Tänk på i vilken ordning en stack lämnar ifrån sig noderna.', 1,
             [alt('I en stack tas den senast inlagda noden ut först.', True, 'Det kallas sist in, först ut (LIFO).'),
              alt('DFS kan använda en stack för att hålla reda på noderna.', True, 'Med en stack fortsätter sökningen från den senast hittade noden, och då går den på djupet.'),
              alt('BFS använder en stack.', False, 'BFS använder en FIFO-kö, så att noderna tas ut nivå för nivå.'),
              alt('I en stack tas den nod ut som har legat där längst.', False, 'Det beskriver en FIFO-kö. I en stack ligger den äldsta noden nederst och tas ut sist.')])
    return task('1.11', 'ko_stack', 'Stack i en bild', intro, [a, b, c],
                'I en stack läggs nya noder överst, och det är alltid den översta noden som tas ut.', ['procedur', 'begrepp'])


def t112():
    intro = (p('Noder läggs in i och tas ut ur en okänd datastruktur enligt följande:') +
             p('lägg in A → lägg in B → ta ut en nod → lägg in C → lägg in D → ta ut tre noder.') +
             p('Noderna tas ut i ordningen B, D, C, A.'))
    ops = ['+A', '+B', '-', '+C', '+D', '-', '-', '-']

    def run(kind):
        s, out = [], []
        for op in ops:
            if op[0] == '+':
                s.append(op[1])
            elif kind == 'stack':
                out.append(s.pop())
            elif kind == 'fifo':
                out.append(s.pop(0))
            else:
                s.sort()
                out.append(s.pop(0))
        return out
    assert run('stack') == ['B', 'D', 'C', 'A'] and run('fifo') == ['A', 'B', 'C', 'D'] and run('prio')[0] == 'A'
    a = part(p('Vilken datastruktur användes? Välj ett alternativ.'),
             [step('Första uttaget avslöjar strukturen', 'Vid första uttaget ligger A och B i strukturen. B tas ut, alltså den nod som lades in sist.'),
              step('Kontrollera resten med sist in, först ut', 'Efter att C och D lagts in ligger A, C och D i stacken med D överst. Tre uttag ger D, C och A.')],
             'En stack.', 'Vilka noder finns i strukturen vid första uttaget, och vilken av dem tas ut?', 2,
             [alt('En FIFO-kö', False, 'En FIFO-kö hade gett A vid första uttaget, eftersom A lades in först.'),
              alt('En stack', True, 'B lades in sist före första uttaget och tas ut först. Sedan tas D, C och A ut i omvänd ordning mot hur de lades in.'),
              alt('En prioritetskö där den nod som kommer först i alfabetet tas ut först', False, 'Då hade A tagits ut vid första uttaget, eftersom A kommer före B i alfabetet.')])
    b = part(p('I vilken ordning hade noderna tagits ut om samma steg hade gjorts med en FIFO-kö?'),
             [step('FIFO: först in, först ut', 'Vid första uttaget står A först i kön och tas ut. Sedan står B, C och D i kön i den ordningen.',
                   tab(['Steg', 'Kön efter steget'], [['Lägg in A och B', 'A B'], ['Ta ut A', 'B'], ['Lägg in C och D', 'B C D'], ['Ta ut tre noder', 'tom']]))],
             'A, B, C, D.', 'I en FIFO-kö tas noderna ut i samma ordning som de lades in.', 1)
    return task('1.12', 'ko_stack', 'Vilken struktur användes?', intro, [a, b],
                'Titta på första uttaget. Vilken av de inlagda noderna kom ut?', ['begrepp', 'resonemang'])


M113 = ['S..', '.#.', '..G']


def t113():
    s, g = A.parse(M113)
    r = A.bfs(M113)
    assert names(r['order']) == ['A1', 'A2', 'B1', 'A3', 'C1', 'B3', 'C2', 'C3']
    assert names(r['path']) == ['A1', 'A2', 'A3', 'B3', 'C3']
    intro = (maze(M113, s, g) +
             p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←). En ruta läggs in i kön när den upptäcks första gången. '
               'I tabellen skrivs kön med nästa ruta som tas ut längst till vänster.'))
    rows = [['–', 'A1']] + [[A.cname(n), ' '.join(names(q)) or 'tom'] for n, q in r['snaps']]
    a = part(p('Fyll i tabellen tills målet tas ut.') + tab(['Tas ut', 'Kön efter uttaget'], [['–', 'A1']] + [['…', '…']] * 8),
             [step('A1 tas ut och dess grannar A2 och B1 läggs in', 'Grannarna prövas i ordningen ↑ → ↓ ←. A2 (→) läggs in före B1 (↓).'),
              step('Varje uttag lägger nya grannar längst bak i kön', tab(['Tas ut', 'Kön efter uttaget'], rows)),
              step('En ruta som redan har upptäckts läggs inte in igen', 'När C2 tas ut ligger C3 redan i kön, eftersom B3 hittade den först.')],
             'Rutorna tas ut i ordningen ' + lista(names(r['order'])) + '.',
             'Pröva grannarna i ordningen ↑ → ↓ ←. Hoppa över väggar och rutor som redan har upptäckts.', 2)
    b = part(p('Vilken väg returnerar BFS?'),
             [step('Varje ruta minns vilken ruta som lade in den', 'C3 lades in av B3, B3 av A3, A3 av A2 och A2 av A1.')],
             pil(names(r['path'])) + '.', 'Gå baklänges från målet: vilken ruta lade in målet i kön?', 2)
    c = part(p('Det finns två lika korta vägar till målet. Varför returnerar BFS vägen via A3 och inte vägen via C1? Välj ett alternativ.'),
             [step('→ kommer före ↓ i grannordningen', 'Från A1 läggs A2 in före B1. Därför ligger rutorna längs den övre vägen före rutorna längs den nedre vägen i kön, hela vägen fram till målet.'),
              step('B3 hinner först', 'B3 tas ut före C2 och lägger in målet C3. C3 får då B3 som föregångare.')],
             'B.', 'Jämför när B3 och C2 tas ut ur kön.', 3,
             [alt('Vägen via A3 är kortare.', False, 'Båda vägarna har 4 steg.'),
              alt('B3 tas ut före C2, så B3 lägger in C3 i kön först.', True, 'C3 får B3 som föregångare. När C2 tas ut senare ligger C3 redan i kön och läggs inte in igen.'),
              alt('BFS väljer alltid vägen längs den översta raden.', False, 'Det finns ingen sådan regel. Det är grannordningen som avgör vilken av de lika korta vägarna som hittas först.'),
              alt('C1 besöks aldrig.', False, 'C1 tas ut som femte ruta, men vägen via C1 når inte målet först.')])
    return task('1.13', 'ko_sokning', 'Kön när en labyrint söks igenom', intro, [a, b, c],
                'Nya rutor läggs längst bak i kön. En ruta som redan har upptäckts läggs inte in igen.', ['procedur', 'begrepp'])


TREE_114 = dict(nodes={'S': (200, 35), 'A': (80, 110), 'B': (200, 110), 'C': (320, 110), 'D': (40, 185), 'E': (120, 185),
                       'F': (200, 185), 'G': (280, 185), 'H': (360, 185)},
                edges=[('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'F'), ('C', 'G'), ('C', 'H')],
                start='S', goals=['F'], width=400,
                title='Sökträd: S har barnen A, B och C. A har D och E, B har F, C har G och H. Start S är grön och målet F är rött.')


def t114():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D', 'E'], 'B': ['F'], 'C': ['G', 'H']}
    q, rows = ['S'], [['–', 'S']]
    while q:
        n = q.pop(0)
        if n != 'F':
            q += kids.get(n, [])
        rows.append([n, ' '.join(q) or 'tom'])
        if n == 'F':
            break
    assert [r[0] for r in rows[1:]] == ['S', 'A', 'B', 'C', 'D', 'E', 'F'] and q == ['G', 'H']
    svg = search_tree(**TREE_114)
    intro = (svg + p('Trädet söks igenom med BFS (vänster gren först). Kön skrivs med nästa nod som tas ut längst till vänster. '
                     'Tabellen visar början av sökningen.') + tab(['Tas ut', 'Kön efter uttaget'], rows[:3]))
    a = part(p('Vilken nod tas ut härnäst? Välj ett alternativ.'),
             [step('Nästa uttag är den första noden i kön', 'Kön är B C D E. B står längst till vänster.')],
             'B.', 'Vilken nod står först i kön?', 1,
             [alt('B', True, 'B står först i kön. I BFS tas noderna ut i den ordning de lades in.'),
              alt('D', False, 'D är A:s barn och ligger en nivå längre ned. Att fortsätta med A:s barn direkt är DFS.'),
              alt('E', False, 'E lades in sist. Att ta ut den senast inlagda noden gäller en stack.'),
              alt('F', False, 'F är målet, men F har inte lagts in i kön ännu. Det sker först när B tas ut.')])
    b = part(p('Fortsätt tabellen tills målet tas ut.'),
             [step('B lägger in målet F sist i kön', 'När B tas ut läggs F in bakom C, D och E.'),
              step('Noderna som står före F i kön tas ut först', tab(['Tas ut', 'Kön efter uttaget'], rows[3:])),
              step('D och E har inga barn', 'När D och E tas ut läggs inget nytt in, så F flyttar fram i kön.')],
             'Uttagen fortsätter B, C, D, E, F.', 'Lägg in varje uttagen nods barn längst bak i kön.', 2)
    c = part(p('Hur många noder ligger kvar i kön när målet tas ut?'),
             [step('C:s barn läggs in efter F', 'G och H lades in när C togs ut, alltså efter F. De hinner inte tas ut innan sökningen stoppar vid F.')],
             '2 noder, G och H.', 'Vilka noder lades in efter målet?', 2)
    return task('1.14', 'ko_sokning', 'Fortsätt kön i ett sökträd', intro, [a, b, c],
                'BFS tar ut noderna i samma ordning som de lades in. En nods barn läggs längst bak i kön.', ['procedur'])


M115 = ['S.#.', '.#..', '...#', '#..G']


def t115():
    s, g = A.parse(M115)
    d = A.dist_all(M115, s)
    four = sorted(A.cname(c) for c, v in d.items() if v == 4)
    assert four == ['C3', 'D2'] and d[g] == 6 and d[(0, 3)] == 7
    r = A.bfs(M115)
    assert 'A4' not in names(r['order']) and 'B4' in names(r['order'])
    grid = [[chr(65 + rr)] + [('vägg' if M115[rr][c] == '#' else str(d[(rr, c)])) for c in range(4)] for rr in range(4)]
    intro = maze(M115, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    dist_tab = tab(['', '1', '2', '3', '4'], grid)
    a = part(p('Vilka rutor ligger exakt 4 steg från start?'),
             [step('Räkna steg utåt från start', 'Grannarna till start ligger 1 steg bort. Deras nya grannar ligger 2 steg bort, och så vidare. Tabellen visar antal steg för varje vit ruta.', dist_tab),
              step('Rutorna med talet 4', 'C2 ligger 3 steg bort. Dess nya grannar C3 och D2 ligger 4 steg bort.')],
             'C3 och D2.', 'Skriv antal steg från start i varje vit ruta. Börja med 0 i start.', 2)
    b = part(p('Hur många steg har den kortaste vägen till målet?'),
             [step('Målet D4 nås från D3', 'D3 ligger 5 steg från start, så målet ligger 6 steg bort.'),
              step('En kortaste väg', pil(names(r['path'])) + '.')],
             '6 steg.', 'Vilken granne till målet ligger närmast start?', 1)
    c = part(p('Vilken vit ruta tas aldrig ut ur kön innan BFS tar ut målet? Välj ett alternativ.'),
             [step('BFS tar ut rutorna i ordning efter avstånd', 'A4 kan bara nås via B4 och ligger därför 7 steg från start. Målet ligger 6 steg bort och tas ut innan någon ruta som ligger 7 steg bort.')],
             'A4.', 'Hur många steg från start ligger A4?', 3,
             [alt('A4', True, 'A4 ligger 7 steg från start, längre bort än målet på 6 steg.'),
              alt('B4', False, 'B4 ligger 6 steg från start, lika långt som målet, och tas ut före målet.'),
              alt('B3', False, 'B3 ligger 5 steg från start och tas ut innan någon ruta som ligger 6 steg bort.'),
              alt('D3', False, 'D3 ligger på vägen till målet och tas ut före det.')])
    return task('1.15', 'bfs', 'Avstånd från start', intro, [a, b, c],
                'Rutorna närmast start ligger 1 steg bort. Deras grannar som inte redan har fått ett tal ligger 2 steg bort, och så vidare.',
                ['procedur', 'begrepp'])


M116 = ['S...', '.##.', '...G']


def t116():
    s, g = A.parse(M116)
    r1 = A.bfs(M116)
    r2 = A.bfs(M116, order=(A.LEFT, A.DOWN, A.RIGHT, A.UP))
    top, bottom = names(r1['path']), names(r2['path'])
    assert top == ['A1', 'A2', 'A3', 'A4', 'B4', 'C4'] and bottom == ['A1', 'B1', 'C1', 'C2', 'C3', 'C4'] and len(r1['order']) == 10
    intro = maze(M116, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = part(p('Ange vägen BFS returnerar.'),
             [step('Det finns två vägar med 5 steg', 'Den övre vägen går via A4 och den nedre via C3. Båda har 5 steg.'),
              step('→ före ↓ gör att den övre vägen kommer först', 'A2 läggs in före B1. Därför tas B4 ut före C3, och B4 lägger in målet C4 i kön.')],
             pil(top) + '.', 'Vilken av A2 och B1 läggs in i kön först?', 2)
    b = part(p('Hur många rutor tas ut ur kön, inklusive start och mål?'),
             [step('Målet ligger längst bort från start', 'Målet ligger 5 steg bort. Alla andra vita rutor ligger närmare start och tas ut före målet.'),
              step('Uttagsordning', lista(names(r1['order'])) + '.')],
             '10 rutor.', 'Finns det någon vit ruta som ligger längre från start än målet?', 2)
    c = part(p('Grannordningen ändras till ← ↓ → ↑. Vilken väg returnerar BFS då? Välj ett alternativ.'),
             [step('← ↓ → ↑ gör att den nedre vägen kommer först', 'Från A1 läggs B1 in före A2. Samma sak upprepas på varje nivå, så C3 tas ut före B4 och lägger in målet.')],
             pil(bottom) + '.', 'Vilken av A2 och B1 läggs in i kön först med den nya ordningen?', 3,
             [alt('Samma väg som med ↑ → ↓ ←', False, 'Nu läggs B1 in före A2. Rutorna längs den nedre vägen hamnar då före rutorna längs den övre vägen i kön.'),
              alt(pil(bottom), True, 'C3 tas ut före B4 och lägger in målet först. Vägen har också 5 steg.'),
              alt('En längre väg än förut', False, 'När alla steg kostar lika mycket hittar BFS alltid en kortaste väg, oavsett grannordning.'),
              alt('Ingen väg hittas', False, 'Målet kan nås. Grannordningen påverkar bara vilken av de kortaste vägarna som returneras.')])
    return task('1.16', 'bfs', 'Två lika korta vägar', intro, [a, b, c],
                'När två vägar är lika långa avgör grannordningen vilken av dem BFS hittar först.', ['procedur', 'begrepp'])


M117 = ['S.#.', '..#.', '#...', '.#.G']


def t117():
    s, g = A.parse(M117)
    r = A.dfs(M117)
    order, path = names(r['order']), names(r['path'])
    assert order == ['A1', 'A2', 'B2', 'C2', 'C3', 'C4', 'B4', 'A4', 'D4']
    assert path == ['A1', 'A2', 'B2', 'C2', 'C3', 'C4', 'D4']
    intro = maze(M117, s, g) + p('Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).')
    a = part(p('Ange besöksordningen.'),
             [step('Från A1 till C4 finns bara en möjlig fortsättning', 'A1 → A2 → B2 → C2 → C3 → C4.'),
              step('I C4 kommer ↑ före ↓', 'DFS går först upp till B4 och A4. A4 är en återvändsgränd, så sökningen backar till C4 och går ned till målet D4.')],
             lista(order) + '.', 'Gå så långt som möjligt i första tillåtna riktningen. Backa när det inte finns någon obesökt granne.', 2)
    b = part(p('Ange vägen till målet.'),
             [step('Återvändsgränden ingår inte i vägen', 'När DFS backar från A4 och B4 tas de bort från den aktuella vägen.')],
             pil(path) + '.', 'Följ vägen från målet tillbaka till start.', 2)
    c = part(p('Vilka besökta rutor ingår inte i vägen?'),
             [step('Jämför besöksordningen med vägen', 'Nio rutor besöks och sju av dem ingår i vägen.')],
             'B4 och A4.', 'Vilka rutor besökte DFS innan den backade?', 2)
    return task('1.17', 'dfs', 'Besökta rutor utanför vägen', intro, [a, b, c],
                'Gå så långt du kan i första tillåtna riktningen. Backa först när det inte finns någon obesökt granne.', ['procedur'])


M118 = ['S...', '.#..', '.#.#', '...G']


def t118():
    s, g = A.parse(M118)
    r1 = A.dfs(M118)
    r2 = A.dfs(M118, order=(A.DOWN, A.RIGHT, A.UP, A.LEFT))
    p1, p2 = names(r1['path']), names(r2['path'])
    assert p1 == ['A1', 'A2', 'A3', 'A4', 'B4', 'B3', 'C3', 'D3', 'D4'] and p2 == ['A1', 'B1', 'C1', 'D1', 'D2', 'D3', 'D4']
    assert len(r1['order']) == 9 and len(r2['order']) == 7 and len(A.bfs(M118)['path']) - 1 == 6
    intro = maze(M118, s, g) + p('Labyrinten söks igenom med DFS två gånger, med olika grannordning.')
    a = part(p('Ange vägen DFS hittar med ordningen ↑ → ↓ ←. Hur många steg har vägen?'),
             [step('Det finns ingen ruta ovanför, så → styr först', 'DFS går åt höger längs rad A till A4.'),
              step('Från A4 finns bara en väg vidare', 'A4 → B4 → B3 → C3 → D3 → D4. DFS hittar målet utan att behöva backa.')],
             pil(p1) + ', 8 steg.', 'Pröva grannarna i ordningen ↑ → ↓ ← och gå direkt till den första obesökta grannen.', 2)
    b = part(p('Ange vägen DFS hittar med ordningen ↓ → ↑ ←. Hur många steg har vägen?'),
             [step('↓ kommer först, så DFS går nedåt längs kolumn 1', 'A1 → B1 → C1 → D1.'),
              step('I D1 finns ingen ruta nedanför', 'Nästa riktning är →, och DFS går D2 → D3 → D4.')],
             pil(p2) + ', 6 steg.', 'Gå nedåt så länge det går.', 2)
    c = part(p('Med ordningen ↑ → ↓ ← hittar DFS en väg med 8 steg, och med ordningen ↓ → ↑ ← en väg med 6 steg. Vilka påståenden stämmer? Välj alla som stämmer.'),
             [step('Jämför de två vägarna', 'Samma labyrint ger en väg med 8 steg och en med 6 steg. Det är grannordningen som avgör vilken väg DFS hittar.'),
              step('BFS hittar en kortaste väg', 'När varje steg kostar lika mycket hittar BFS en väg med minst antal steg, här 6.')],
             'B och C.', 'Jämför vägarna från a) och b) med varandra.', 3,
             [alt('DFS hittar alltid den kortaste vägen.', False, 'Med ordningen ↑ → ↓ ← hittar DFS en väg med 8 steg, fast det finns en med 6 steg.'),
              alt('Grannordningen kan ändra vilken väg DFS hittar.', True, 'De två ordningarna ger olika vägar i samma labyrint.'),
              alt('BFS hade hittat en väg med 6 steg.', True, 'BFS hittar en kortaste väg när alla steg kostar lika mycket, och den kortaste vägen har 6 steg.'),
              alt('Med ordningen ↓ → ↑ ← besöker DFS fler rutor.', False, 'Den besöker 7 rutor, alla på vägen. Med ↑ → ↓ ← besöks 9 rutor.')])
    return task('1.18', 'dfs', 'Grannordningen styr DFS', intro, [a, b, c],
                'Pröva grannarna i den ordning som anges och gå vidare direkt till den första obesökta grannen.', ['procedur', 'begrepp'])


M119 = ['S..#.', '.#...', '.#.#.', '...#G']


def t119():
    s, g = A.parse(M119)
    r = A.dfs(M119)
    order = names(r['order'])
    assert order == ['A1', 'A2', 'A3', 'B3', 'B4', 'B5', 'A5', 'C5', 'D5']
    white = sum(ch != '#' for row in M119 for ch in row)
    assert white == 15 and white - len(order) == 6
    intro = maze(M119, s, g) + p('Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).')
    a = part(p('I vilken ruta hamnar DFS i en återvändsgränd för första gången? Välj ett alternativ.'),
             [step('Följ första tillåtna riktning', 'A1 → A2 → A3 → B3 → B4 → B5. Från B5 kommer ↑ först, så DFS går till A5.'),
              step('A5 har inga obesökta grannar', 'Ovanför och till höger finns inga rutor, nedanför ligger B5 som redan är besökt och till vänster finns en vägg.')],
             'A5.', 'Följ DFS ruta för ruta. Var tar det stopp första gången?', 2,
             [alt('A5', True, 'DFS går B5 → A5 eftersom ↑ prövas först. Där finns ingen obesökt granne.'),
              alt('B5', False, 'Från B5 finns fortfarande en obesökt granne nedåt, C5.'),
              alt('C3', False, 'C3 besöks aldrig. DFS går från B3 till B4 innan ↓ hinner prövas.'),
              alt('B1', False, 'B1 besöks aldrig, eftersom DFS går åt höger från A1.')])
    b = part(p('Vilken ruta besöks direkt efter den första återvändsgränden?'),
             [step('DFS backar till B5 och prövar nästa riktning', 'I B5 har ↑ redan prövats och → leder utanför labyrinten. Nästa riktning är ↓, till C5.'),
              step('Att backa är inget nytt besök', 'B5 är redan besökt. Nästa nya ruta i besöksordningen är C5.')],
             'C5.', 'Till vilken ruta backar DFS, och vilka riktningar återstår där?', 2)
    c = part(p('Hur många rutor som inte är väggar besöks aldrig?'),
             [step('Räkna rutorna som inte är väggar', 'Labyrinten har 15 rutor som inte är väggar, inklusive start och mål.'),
              step('Räkna de besökta rutorna', 'DFS besöker ' + lista(order) + ', alltså 9 rutor. B1, C1, D1, D2, D3 och C3 besöks aldrig.')],
             '6 rutor.', 'Hur många rutor besöker DFS innan den når målet?', 2)
    return task('1.19', 'dfs', 'När DFS måste backa', intro, [a, b, c],
                'DFS backar till den senaste rutan som fortfarande har en obesökt granne.', ['procedur', 'begrepp'])


def t212():
    intro = (p('Noder läggs in i och tas ut ur en prioritetskö enligt följande. Talet inom parentes är nodens värde, och noden med lägst värde tas ut först. '
               'Vid lika värde tas den nod ut som kommer först i alfabetet.') +
             p('Lägg in M(4), L(2) och K(4) → ta ut en nod → lägg in N(1) → ta ut tre noder.'))
    q, out = [], []
    for op in [('M', 4), ('L', 2), ('K', 4), None, ('N', 1), None, None, None]:
        if op:
            q.append(op)
        else:
            q.sort(key=lambda x: (x[1], x[0]))
            out.append(q.pop(0)[0])
    assert out == ['L', 'N', 'K', 'M']
    rows = [['Lägg in M(4), L(2) och K(4)', 'K(4) L(2) M(4)', '–'], ['Ta ut en nod', 'K(4) M(4)', 'L'],
            ['Lägg in N(1)', 'K(4) M(4) N(1)', '–'], ['Ta ut', 'K(4) M(4)', 'N'], ['Ta ut', 'M(4)', 'K'], ['Ta ut', 'tom', 'M']]
    a = part(p('I vilken ordning tas noderna ut?'),
             [step('Lägst värde först', 'L har lägst värde av de tre första noderna. Sedan läggs N(1) in och har lägst värde av alla.'),
              step('Kön efter varje steg', tab(['Steg', 'I kön', 'Tas ut'], rows))],
             'L, N, K, M.', 'Skriv upp alla noder i kön, med sina värden, efter varje steg.', 1)
    b = part(p('Varför tas K ut före M? Välj ett alternativ.'),
             [step('Lika värden avgörs av alfabetet', 'K och M har båda värdet 4. Enligt regeln tas den som kommer först i alfabetet ut, alltså K.')],
             'B.', 'Jämför värdena för K och M. Vilken regel gäller vid lika värden?', 1,
             [alt('M lades in först och har därför väntat längst.', False, 'Väntetiden spelar ingen roll i en prioritetskö. Om den avgjorde skulle M tas ut före K.'),
              alt('K och M har samma värde, och K kommer först i alfabetet.', True, 'Värdet avgör först. När värdena är lika används alfabetet.'),
              alt('K har lägre värde än M.', False, 'Båda har värdet 4.')])
    return task('2.12', 'prioritetsko', 'Lika värden i prioritetskön', intro, [a, b],
                'Jämför först värdena. Alfabetet används bara när två noder har samma värde.', ['procedur'])


def t213():
    intro = (p('Under en A*-sökning innehåller prioritetskön noderna i tabellen. Noden med lägst f tas ut först. '
               'Vid lika f tas den nod ut som kommer först i alfabetet.') +
             tab(['Nod', 'f'], [['B', '9'], ['C', '7'], ['D', '8']]) +
             p('C tas ut. Från C hittas en ny väg till B med f = 6. Dessutom läggs en ny nod E in med f = 8.'))
    a = part(p('Vilket f-värde ska B ha i kön efter att den nya vägen hittats? Välj ett alternativ.'),
             [step('A* sparar den bästa vägen hittills', 'Den nya vägen till B ger f = 6, som är lägre än det gamla värdet 9. B uppdateras därför till f = 6.')],
             '6.', 'Vilken av de två vägarna till B är bäst?', 1,
             [alt('9', False, '9 hör till den gamla, dyrare vägen till B.'),
              alt('6', True, 'Den nya vägen är bättre, och A* sparar den bästa vägen hittills.'),
              alt('15', False, 'f-värden för olika vägar läggs inte ihop. B får värdet för den bästa vägen.')])
    b = part(p('B ligger nu i kön med f = 6. Vilken nod tas ut härnäst? Välj ett alternativ.'),
             [step('Kön efter att C tagits ut', tab(['Nod', 'f'], [['B', '6'], ['D', '8'], ['E', '8']])),
              step('Lägst f tas ut', 'B har nu f = 6, det lägsta värdet i kön.')],
             'B.', 'Skriv upp kön med de nya värdena.', 2,
             [alt('B', True, 'B har nu f = 6, det lägsta värdet i kön.'),
              alt('D', False, 'D har f = 8, men B har fått det lägre värdet 6.'),
              alt('E', False, 'E är den senast inlagda noden. I en prioritetskö avgör värdet, inte när noden lades in.'),
              alt('C', False, 'C har redan tagits ut ur kön.')])
    c = part(p('Vilken nod tas ut efter B?'),
             [step('D och E har samma värde', 'Efter att B tagits ut ligger D(8) och E(8) kvar. Båda har f = 8.'),
              step('Lika f avgörs av alfabetet', 'D kommer före E i alfabetet.')],
             'D.', 'Vilka noder ligger kvar, och vilken regel gäller vid lika f?', 2)
    return task('2.13', 'prioritetsko', 'Ett bättre värde hittas', intro, [a, b, c],
                'När en bättre väg till en nod hittas ska noden ligga i kön med det lägre värdet.', ['procedur', 'begrepp'])


def t214():
    data = {'P': (2, 9), 'Q': (5, 3), 'R': (4, 5), 'T': (8, 1)}
    f = {k: g + h for k, (g, h) in data.items()}
    assert min(data, key=lambda k: data[k][1]) == 'T' and min(f, key=f.get) == 'Q'
    intro = (p('Fyra noder ligger i prioritetskön. Tabellen visar kostnaden hittills g och uppskattningen h av kostnaden kvar till målet.') +
             tab(['Nod', 'g', 'h'], [[k, str(g), str(h)] for k, (g, h) in data.items()]))

    def alts(right, why):
        txt = {'P': 'P har lägst g = 2. Varken girig bäst först eller A* väljer efter bara g.',
               'Q': 'Q har lägst f = g + h = 8. Det är A*:s val.',
               'R': 'R har varken lägst h eller lägst f.', 'T': 'T har lägst h = 1. Det är valet för girig bäst först.'}
        return [alt(k, k == right, why if k == right else txt[k]) for k in 'PQRT']
    a = part(p('Bestäm f = g + h för varje nod.'),
             [step('Lägg ihop g och h', 'P: 2 + 9 = 11. Q: 5 + 3 = 8. R: 4 + 5 = 9. T: 8 + 1 = 9.')],
             'P: 11, Q: 8, R: 9, T: 9.', 'Lägg ihop kostnaden hittills och uppskattningen kvar.', 1)
    b = part(p('Vilken nod tar girig bäst först ut först? Välj ett alternativ.'),
             [step('Girig bäst först jämför bara h', 'Den väljer den nod som verkar ligga närmast målet. h är 9, 3, 5 och 1.')],
             'T.', 'Vilket av värdena g och h tittar girig bäst först på?', 1, alts('T', 'Girig bäst först jämför bara h, och T har lägst h = 1.'))
    c = part(p('Vilken nod tar A* ut först? Välj ett alternativ.'),
             [step('A* jämför f = g + h', 'P: 2 + 9 = 11. Q: 5 + 3 = 8. R: 4 + 5 = 9. T: 8 + 1 = 9.'),
              step('Lägst f vinner', 'Q har lägst f = 8. T ligger närmast målet men har redan kostat mycket, g = 8.')],
             'Q.', 'Räkna ut g + h för varje nod.', 2, alts('Q', 'A* jämför f = g + h, och Q har lägst f = 8.'))
    return task('2.14', 'prioritetsko', 'Girig bäst först och A* väljer olika', intro, [a, b, c],
                'Girig bäst först sorterar kön efter h, och A* sorterar efter f = g + h.', ['procedur', 'begrepp'])


M215 = ['......', 'S.#..G', '..#...', '...#..']
MARK215 = {(0, 1): 'P', (3, 4): 'Q', (2, 4): 'R'}


def t215():
    s, g = A.parse(M215)
    h = {k: A.manhattan(c, g) for c, k in MARK215.items()}
    assert h == {'P': 5, 'Q': 3, 'R': 2}, h
    intro = maze(M215, s, g, MARK215, extra_legend=[('#fff3b0', 'Markerad ruta')]) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet).')
    a = part(p('Bestäm h för P, Q och R.'),
             [step('h = radskillnad + kolumnskillnad', 'Målet ligger i B6. Väggarna räknas inte.'),
              step('Räkna för varje ruta', 'P i A2: 1 rad och 4 kolumner från målet, h = 1 + 4 = 5.',
                   'Q i D5: 2 rader och 1 kolumn från målet, h = 2 + 1 = 3.',
                   'R i C5: 1 rad och 1 kolumn från målet, h = 1 + 1 = 2.')],
             'P: h = 5, Q: h = 3, R: h = 2.', 'Räkna hur många rader och kolumner rutan ligger från målet.', 1)
    b = part(p('Vilken av de markerade rutorna har lägst h? Välj ett alternativ.'),
             [step('Jämför avstånden till målet', 'P ligger 5, Q 3 och R 2 rader och kolumner från målet sammanlagt.')],
             'R.', 'Vilken markerad ruta ligger närmast målet om man bortser från väggarna?', 1,
             [alt('P', False, 'P ligger 4 kolumner från målet och har h = 5, det högsta värdet.'),
              alt('Q', False, 'Q har h = 3. R ligger en rad närmare målet.'),
              alt('R', True, 'R ligger en rad och en kolumn från målet, h = 2.'),
              alt('Alla har samma h', False, 'h beror på hur långt rutan ligger från målet, och det skiljer sig mellan rutorna.')])
    return task('2.15', 'astar_varden', 'h för tre markerade rutor', intro, [a, b],
                'Manhattanavståndet är antalet rader plus antalet kolumner mellan rutan och målet.', ['procedur'], 1)


M216 = ['S....', '.###.', '.#G#.', '.#...', '.....']
MARK216 = {(0, 2): 'P'}


def t216():
    s, g = A.parse(M216)
    dg = A.dist_all(M216, g)
    ds = A.dist_all(M216, s)
    P = (0, 2)
    assert A.manhattan(P, g) == 2 and ds[P] == 2 and dg[P] == 8
    intro = maze(M216, s, g, MARK216, extra_legend=[('#fff3b0', 'Markerad ruta')]) + p(ASTAR_GH)
    a = part(p('Bestäm h och f för P.'),
             [step('h = radskillnad + kolumnskillnad', 'P ligger i A3 och målet i C3: 2 rader och 0 kolumner, h = 2.'),
              step('g längs en kortaste väg från start', 'A1 → A2 → A3 ger g = 2.'),
              step('f = g + h', 'f = 2 + 2 = 4.')],
             'h = 2, f = 4.', 'h räknas utan väggar, men g följer gångarna.', 2)
    b = part(p('Hur många steg är det i verkligheten från P till målet?'),
             [step('Väggarna stänger målet uppåt och åt sidorna', 'Målet C3 kan bara nås nedifrån, från D3.'),
              step('Gå runt till höger', 'A3 → A4 → A5 → B5 → C5 → D5 → D4 → D3 → C3.')],
             '8 steg.', 'Från vilket håll går det att komma in till målet?', 2)
    c = part(p('P har h = 2, men det är 8 steg från P till målet. Vilka påståenden stämmer? Välj alla som stämmer.'),
             [step('h kan aldrig vara för stort', 'Varje steg ändrar raden eller kolumnen med 1. Därför behövs minst h steg, men väggar kan göra vägen längre.'),
              step('Jämför för P', 'P har h = 2 men 8 steg kvar. f = 4, medan en väg via P kostar 2 + 8 = 10 steg.')],
             'B och D.', 'Jämför h med det verkliga antalet steg från b).', 3,
             [alt('h tar hänsyn till väggarna.', False, 'Manhattanavståndet räknar bara rad- och kolumnskillnad. Väggarna mellan P och målet syns inte i h.'),
              alt('h är aldrig större än det verkliga antalet steg kvar.', True, 'Varje steg ändrar raden eller kolumnen med 1, så minst h steg behövs.'),
              alt('Ett lågt h betyder att målet går snabbt att nå.', False, 'P har h = 2, men det krävs 8 steg.'),
              alt('f för P underskattar hur lång en väg via P blir.', True, 'f = 4, men en väg via P kräver 2 + 8 = 10 steg.')])
    return task('2.16', 'astar_varden', 'Nära målet men långt att gå', intro, [a, b, c],
                'h räknas som om väggarna inte fanns. Jämför med hur man faktiskt måste gå.', ['procedur', 'begrepp'])


M217 = ['#..#G', '#.#..', '.....', 'S...#']


def t217():
    s, g = A.parse(M217)
    r = A.astar(M217)
    order, path = names(r['order']), names(r['path'])
    assert order == ['D1', 'C1', 'C2', 'B2', 'A2', 'A3', 'C3', 'C4', 'B4', 'B5', 'A5']
    assert path == ['D1', 'C1', 'C2', 'C3', 'C4', 'B4', 'B5', 'A5']
    intro = maze(M217, s, g) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). ' + ASTAR_TIE)
    a = part(p('Bestäm g, h och f för de två grannarna till start.'),
             [step('Grannarna till D1 är C1 och D2', 'Båda ligger ett steg från start, så g = 1.'),
              step('h = radskillnad + kolumnskillnad till A5', 'C1: 2 + 4 = 6. D2: 3 + 3 = 6.'),
              step('f = g + h', 'C1: f = 1 + 6 = 7. D2: f = 1 + 6 = 7.')],
             'C1: g = 1, h = 6, f = 7. D2: g = 1, h = 6, f = 7.', 'Målet ligger i A5. Räkna rader och kolumner dit.', 2)
    b = part(p('Vilken av grannarna till start tas ut först? Välj ett alternativ.'),
             [step('Lika f och lika h', 'C1 och D2 har båda f = 7 och h = 6.'),
              step('Bokstavsordningen avgör', 'C1 kommer före D2.')],
             'C1.', 'Gå igenom reglerna för lika värden i tur och ordning.', 2,
             [alt('C1', True, 'Båda har f = 7 och h = 6. Då avgör bokstavsordningen, och C1 kommer före D2.'),
              alt('D2', False, 'D2 har samma f och h som C1, men kommer efter C1 i bokstavsordning.'),
              alt('Båda tas ut samtidigt', False, 'A* tar ut en ruta i taget.')])
    tab_rows = [['D1', 'C1 (1, 6, 7), D2 (1, 6, 7)'], ['C1', 'C2 (2, 5, 7), D2'], ['C2', 'B2 (3, 4, 7), C3 (3, 4, 7), D2'],
                ['B2', 'A2 (4, 3, 7), C3, D2'], ['A2', 'A3 (5, 2, 7), C3, D2'], ['A3', 'C3, D2'],
                ['C3', 'C4 (4, 3, 7), D2, D3 (4, 5, 9)'], ['C4', 'B4 (5, 2, 7), C5 (5, 2, 7), D2, D3, D4 (5, 4, 9)'],
                ['B4', 'B5 (6, 1, 7), C5, D2, D3, D4'], ['B5', 'A5 (7, 0, 7), C5, D2, D3, D4'], ['A5', 'målet tas ut']]
    c = part(p('Ange besöksordningen.'),
             [step('Nästan alla rutor har f = 7', 'Därför avgör lägst h oftast valet, och ibland bokstavsordningen.'),
              step('Öppna listan efter varje uttag, med (g, h, f)', tab(['Tas ut', 'Öppna listan efteråt'], tab_rows)),
              step('B2 före C3 leder in i en återvändsgränd', 'B2 och C3 har samma f och h. B2 kommer först i bokstavsordning, så A* går B2 → A2 → A3. A3 ligger nära målet men har en vägg på höger sida. Därefter fortsätter A* från C3.')],
             lista(order) + '.', 'Gör en tabell med g, h och f för rutorna i öppna listan.', 3)
    d = part(p('Vilka besökta rutor ingår inte i den väg som A* returnerar?'),
             [step('Vägen till målet', pil(path) + '.'),
              step('Jämför med besöksordningen', 'Elva rutor besöks och åtta av dem ingår i vägen.')],
             'B2, A2 och A3.', 'Vilka rutor ledde inte vidare mot målet?', 3)
    return task('2.17', 'astar_sokning', 'A* och en återvändsgränd nära målet', intro, [a, b, c, d],
                'Håll reda på g, h och f för alla rutor i öppna listan. Använd reglerna för lika värden i tur och ordning.', ['procedur'], 3)


def t218():
    data = {'K': (4, 6), 'L': (6, 3), 'M': (3, 8), 'N': (5, 4)}
    f = {k: g + h for k, (g, h) in data.items()}
    assert f == {'K': 10, 'L': 9, 'M': 11, 'N': 9}
    intro = (p('Under en A*-sökning innehåller öppna listan rutorna i tabellen. Vid lika f väljs lägst h.') +
             tab(['Ruta', 'g', 'h'], [[k, str(g), str(h)] for k, (g, h) in data.items()]))
    a = part(p('Bestäm f för varje ruta.'),
             [step('f = g + h', 'K: 4 + 6 = 10. L: 6 + 3 = 9. M: 3 + 8 = 11. N: 5 + 4 = 9.')],
             'K: 10, L: 9, M: 11, N: 9.', 'Lägg ihop kostnaden hittills och uppskattningen kvar.', 1)
    b = part(p('Vilken ruta tas ut härnäst? Välj ett alternativ.'),
             [step('Lägst f', 'L och N har båda f = 9, det lägsta värdet.'),
              step('Lika f avgörs av lägst h', 'L har h = 3 och N har h = 4.')],
             'L.', 'Vilka rutor har lägst f? Vilken regel gäller då?', 2,
             [alt('K', False, 'K har f = 10, högre än L och N.'),
              alt('L', True, 'L och N har lägst f = 9, och L har lägst h av dem.'),
              alt('M', False, 'M har lägst g = 3, men A* jämför f = g + h. M har f = 11.'),
              alt('N', False, 'N har också f = 9, men h = 4 är högre än L:s h = 3.')])
    c = part(p('L tas ut. Då läggs grannen P in i öppna listan med g = 7 och h = 1. Vilken ruta tas ut efter L?'),
             [step('Öppna listan efter att L tagits ut', 'K: f = 10. M: f = 11. N: f = 9. P: f = 7 + 1 = 8.'),
              step('Lägst f vinner', 'P har lägst f = 8.')],
             'P.', 'Räkna ut f för P och jämför med de rutor som ligger kvar.', 2)
    return task('2.18', 'astar_sokning', 'Nästa uttag ur öppna listan', intro, [a, b, c],
                'A* tar alltid ut rutan med lägst f = g + h ur öppna listan.', ['procedur'])


M219 = ['S....', '.....', '..##.', '....G']


def t219():
    s, g = A.parse(M219)
    b_ = A.bfs(M219)
    a_ = A.astar(M219)
    assert len(b_['order']) == 18 and names(a_['order']) == ['A1', 'A2', 'A3', 'A4', 'A5', 'B5', 'C5', 'D5']
    assert len(b_['path']) - 1 == 7 == len(a_['path']) - 1
    intro = maze(M219, s, g) + p('Labyrinten söks igenom först med BFS (ordning ↑ → ↓ ←) och sedan med A* (h = Manhattanavstånd). ' + ASTAR_TIE)
    a = part(p('Hur många rutor tar BFS ut ur kön, inklusive start och mål?'),
             [step('Målet ligger längst bort från start', 'Målet D5 ligger 7 steg från start. Ingen annan vit ruta ligger lika långt bort.'),
              step('BFS tar ut alla rutor som ligger närmare', 'Labyrinten har 18 vita rutor. Alla tas ut, och målet sist.')],
             '18 rutor.', 'Ligger någon vit ruta längre från start än målet?', 2)
    b = part(p('Ange besöksordningen för A*.'),
             [step('Rutor på en kortaste väg har f = 7', 'Start har h = 3 + 4 = 7. Varje steg mot målet ökar g med 1 och minskar h med 1.'),
              step('Lika f avgörs av h och sedan bokstavsordning', 'A2 och B1 har båda f = 7 och h = 6. A2 kommer först. Samma sak upprepas längs rad A.'),
              step('Från A5 går vägen rakt ned', 'B5, C5 och D5 har allt lägre h.')],
             lista(names(a_['order'])) + '.', 'Räkna f för grannarna till varje uttagen ruta. Vilka regler gäller vid lika f?', 3)
    c = part(p('BFS tar ut 18 rutor och A* tar ut 8 rutor. Varför tar A* ut färre rutor än BFS? Välj ett alternativ.'),
             [step('Ordningen skiljer sig', 'BFS tar ut rutorna i ordning efter avstånd från start. A* sorterar efter f = g + h och väljer därför rutor som leder mot målet.'),
              step('Båda hittar en väg med 7 steg', 'Skillnaden ligger i hur många rutor som undersöks på vägen.')],
             'A.', 'Vad sorterar BFS efter, och vad sorterar A* efter?', 2,
             [alt('h gör att A* undersöker rutor som leder mot målet först.', True, 'A* sorterar efter f = g + h. Rutor som leder bort från målet får högre f och hinner inte tas ut.'),
              alt('A* får gå genom väggarna.', False, 'A* tar bara samma tillåtna steg som BFS. Det är ordningen som skiljer.'),
              alt('A* hittar en kortare väg än BFS.', False, 'Båda hittar en väg med 7 steg.'),
              alt('BFS räknar väggarna som rutor.', False, 'BFS tar bara ut vita rutor. Den tar ut alla 18 eftersom målet ligger längst bort från start.')])
    return task('2.19', 'astar_sokning', 'A* jämfört med BFS', intro, [a, b, c],
                'Jämför vilka rutor de två sökningarna undersöker innan målet tas ut.', ['procedur', 'begrepp'], 3)


G220 = dict(nodes={'S': (50, 130), 'A': (170, 45), 'B': (170, 215), 'C': (320, 45), 'D': (320, 215), 'M': (440, 130)},
            edges=[('S', 'A', 2), ('S', 'B', 5), ('A', 'B', 2), ('A', 'C', 6), ('B', 'C', 3), ('B', 'D', 3), ('C', 'M', 1), ('D', 'M', 4)])


def t220():
    r = A.ucs_graph(G220['edges'], 'S', 'M')  # kontroll av billigaste väg, inte elevens metod
    assert r['cost'] == 8 and r['path'] == ['S', 'A', 'B', 'C', 'M']
    svg = weighted_graph(G220['nodes'], G220['edges'], 'S', 'M', 'Graf med noderna S, A, B, C, D och M. Talet vid varje kant är kostnaden.', 490)
    intro = svg + p('Grafen visar vägar mellan platser. Talet vid varje kant är kostnaden att gå längs den, åt valfritt håll.')
    paths = [['S → A → C → M', '2 + 6 + 1 = 9'], ['S → B → C → M', '5 + 3 + 1 = 9'], ['S → A → B → C → M', '2 + 2 + 3 + 1 = 8'],
             ['S → B → D → M', '5 + 3 + 4 = 12'], ['S → A → B → D → M', '2 + 2 + 3 + 4 = 11']]
    a = part(p('Vad kostar den billigaste vägen från start till mål?'),
             [step('Kostnaden är summan av kanternas tal', tab(['Väg', 'Kostnad'], paths)),
              step('Den billigaste vägen till B går via A', 'S → A → B kostar 2 + 2 = 4, billigare än kanten S–B som kostar 5. Det gör vägen via A, B och C billigast.')],
             '8.', 'Hitta först det billigaste sättet att komma till B.', 2)
    b = part(p('Ange den billigaste vägen.'),
             [step('Jämför vägarna', 'Bara S → A → B → C → M kostar 8. Alla andra vägar kostar 9 eller mer.'),
              step('Kontrollera delvägarna', 'Till B: 2 + 2 = 4 via A. Till C: 4 + 3 = 7 via B. Till M: 7 + 1 = 8.')],
             'S → A → B → C → M.', 'Följ den billigaste vägen nod för nod från start.', 2)
    c = part(p('Vilka påståenden stämmer? Välj alla som stämmer.'),
             [step('Antal kanter och kostnad är olika saker', 'Vägarna med tre kanter kostar 9 eller 12. Den billigaste vägen har fyra kanter och kostar 8.'),
              step('Den billigaste vägen till B', 'S → A → B kostar 4, medan kanten S–B kostar 5.')],
             'B och D.', 'Jämför antalet kanter med kostnaden för vägarna.', 2,
             [alt('Vägen med minst antal kanter är också billigast.', False, 'S → A → C → M och S → B → C → M har bara tre kanter men kostar 9.'),
              alt('En väg med fler kanter kan vara billigare.', True, 'S → A → B → C → M har fyra kanter och kostar 8.'),
              alt('BFS hade hittat den billigaste vägen här.', False, 'BFS letar efter minst antal kanter, inte lägst kostnad. Den hade hittat en väg med tre kanter, som kostar mer.'),
              alt('Det billigaste sättet att komma till B går via A.', True, 'S → A → B kostar 2 + 2 = 4, billigare än kanten S–B som kostar 5.')])
    return task('2.20', 'viktade_vagar', 'Billigaste vägen i en graf', intro, [a, b, c],
                'Kostnaden för en väg är summan av talen på kanterna. Fler kanter kan ändå ge lägre kostnad.', ['procedur', 'begrepp'])


G221 = dict(nodes={'S': (50, 150), 'A': (170, 65), 'B': (170, 235), 'C': (320, 65), 'D': (320, 235), 'M': (440, 150)},
            edges=[('S', 'A', 1), ('S', 'B', 4), ('A', 'C', 2), ('A', 'B', 2), ('B', 'D', 1), ('C', 'D', 5), ('C', 'M', 6), ('D', 'M', 2)],
            h={'S': 5, 'A': 4, 'B': 3, 'C': 5, 'D': 2, 'M': 0})


def t221():
    r = A.astar_graph(G221['edges'], G221['h'], 'S', 'M')
    assert r['order'] == [('S', 0, 5, 5), ('A', 1, 4, 5), ('B', 3, 3, 6), ('D', 4, 2, 6), ('M', 6, 0, 6)]
    assert r['path'] == ['S', 'A', 'B', 'D', 'M'] and r['open'] == ['C'] and r['g']['C'] == 3
    svg = weighted_graph(G221['nodes'], G221['edges'], 'S', 'M',
                         'Graf med noderna S, A, B, C, D och M. Talet vid varje kant är kostnaden, och h står vid varje nod.', 490, h=G221['h'])
    intro = svg + p('Grafen söks igenom med A*. Talet vid varje kant är kostnaden att gå längs den, åt valfritt håll. '
                    'Värdet h vid varje nod är en uppskattning av kostnaden kvar till målet M.')
    rows = [[n, str(g), str(h), str(f)] for n, g, h, f in r['order']]
    a = part(p('Fyll i tabellen med noderna i den ordning de tas ut och deras g, h och f.') +
             tab(['Tas ut', 'g', 'h', 'f'], [['S', '0', '5', '5']] + [['…', '…', '…', '…']] * 4),
             [step('Från S: A får f = 1 + 4 = 5 och B får f = 4 + 3 = 7', 'A har lägst f och tas ut.'),
              step('Via A blir B billigare', 'S → A → B kostar 1 + 2 = 3, så B får g = 3 och f = 3 + 3 = 6. C får g = 1 + 2 = 3 och f = 3 + 5 = 8.'),
              step('B tas ut med f = 6', 'Via B får D g = 3 + 1 = 4 och f = 4 + 2 = 6.'),
              step('D tas ut med f = 6, och sedan målet', 'Via D får M g = 4 + 2 = 6 och f = 6 + 0 = 6. M har lägre f än C (8) och tas ut.',
                   tab(['Tas ut', 'g', 'h', 'f'], rows))],
             'S, A, B, D, M med f = 5, 5, 6, 6, 6.', 'Räkna f = g + h för varje ny granne. Sänk g när du hittar en billigare väg till en nod.', 3)
    b = part(p('Ange vägen A* returnerar och dess kostnad.'),
             [step('Följ vilken nod som gav varje g-värde', 'M fick g = 6 via D, D fick 4 via B, B fick 3 via A och A fick 1 från S.')],
             'S → A → B → D → M, kostnad 6.', 'Vilken nod gav M dess g-värde?', 2)
    c = part(p('B får först g = 4. Varför har B g = 3 när den tas ut? Välj ett alternativ.'),
             [step('En billigare väg ersätter en dyrare', 'Kanten S–B kostar 4, men vägen S → A → B kostar 1 + 2 = 3. A* sparar den lägre kostnaden, och f sjunker från 7 till 6.')],
             'A.', 'Finns det en annan väg till B än kanten S–B?', 2,
             [alt('Vägen S → A → B kostar 1 + 2 = 3, och det lägre värdet ersätter 4.', True, 'A* uppdaterar g när en billigare väg hittas.'),
              alt('A* drar av 1 för varje nod som tas ut.', False, 'g ändras bara när en billigare väg hittas.'),
              alt('B nås via den direkta kanten S–B.', False, 'Den kanten kostar 4, inte 3.'),
              alt('g är antalet kanter till B.', False, 'g är summan av kostnaderna. S → A → B har två kanter men kostar 3.')])
    d = part(p('Vilken nod läggs in i kön men tas aldrig ut? Välj ett alternativ.'),
             [step('C får f = 8', 'C läggs in när A tas ut, med g = 3 och f = 3 + 5 = 8.'),
              step('Målet tas ut innan C', 'Målet M tas ut med f = 6. Sökningen stoppar då, och C hinner aldrig tas ut.')],
             'C.', 'Jämför f för C med f för målet.', 3,
             [alt('A', False, 'A tas ut som andra nod, med f = 5.'),
              alt('B', False, 'B tas ut som tredje nod, med f = 6.'),
              alt('C', True, 'C har f = 8. Målet tas ut med f = 6 innan C, och då stoppar sökningen.'),
              alt('D', False, 'D tas ut som fjärde nod, med f = 6.')])
    return task('2.21', 'viktade_vagar', 'A* steg för steg i en graf', intro, [a, b, c, d],
                'Ta alltid ut noden med lägst f = g + h. Sänk en nods g när en billigare väg dit hittas.', ['procedur', 'begrepp'], 3)


M222 = ['S33..', '.#3#.', '..3.G']


def t222():
    s, g = A.parse(M222)

    def cost(path):
        cells = [(ord(x[0]) - 65, int(x[1:]) - 1) for x in path.split(' → ')]
        return sum(A.cost(M222, c) for c in cells[1:])
    v = {1: 'A1 → A2 → A3 → A4 → A5 → B5 → C5', 2: 'A1 → B1 → C1 → C2 → C3 → C4 → C5', 3: 'A1 → A2 → A3 → B3 → C3 → C4 → C5'}
    k = {i: cost(x) for i, x in v.items()}
    assert k == {1: 10, 2: 8, 3: 14} and A.ucs_grid(M222)[0] == 8
    intro = (maze(M222, s, g) +
             p('I labyrinten kostar det 3 att gå in i en lerruta och 1 att gå in i en vit ruta eller målet. Start kostar 0. Tabellen visar tre vägar från start till mål.') +
             tab(['Väg', 'Rutor'], [[f'Väg {i}', x] for i, x in v.items()]))
    a = part(p('Vad kostar väg 1?'),
             [step('Väg 1 går in i två lerrutor', 'A2 och A3 kostar 3 var. A4, A5, B5 och målet C5 kostar 1 var.'),
              step('Summera', '3 + 3 + 1 + 1 + 1 + 1 = 10.')],
             '10.', 'Räkna kostnaden för varje ruta du går in i, men inte för start.', 1)
    b = part(p('Vad kostar väg 3?'),
             [step('Väg 3 går in i fyra lerrutor', 'A2, A3, B3 och C3 kostar 3 var. C4 och målet C5 kostar 1 var.'),
              step('Summera', '3 + 3 + 3 + 3 + 1 + 1 = 14.')],
             '14.', 'Hur många lerrutor går väg 3 in i?', 1)
    c = part(p('Vilken väg är billigast? Välj ett alternativ.'),
             [step('Väg 2 har bara en lerruta', 'B1, C1, C2, C4 och C5 kostar 1 var och C3 kostar 3: 1 + 1 + 1 + 3 + 1 + 1 = 8.'),
              step('Jämför', 'Väg 1 kostar 10, väg 2 kostar 8 och väg 3 kostar 14.')],
             'Väg 2.', 'Räkna kostnaden för väg 2 och jämför.', 1,
             [alt('Väg 1', False, 'Väg 1 kostar 10, eftersom den går in i två lerrutor.'),
              alt('Väg 2', True, 'Väg 2 går bara in i en lerruta och kostar 8.'),
              alt('Väg 3', False, 'Väg 3 går in i fyra lerrutor och kostar 14.'),
              alt('Alla kostar lika mycket eftersom de har lika många steg', False, 'Alla vägar har 6 steg, men stegen kostar olika mycket beroende på vilken ruta man går in i.')])
    return task('2.22', 'viktade_vagar', 'Kostnaden för tre vägar', intro, [a, b, c],
                'Lägg ihop kostnaden för varje ruta du går in i längs vägen.', ['procedur'], 1)


def t306():
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [3, 8]}, {'n': 'B', 'k': [5, 2, 4]}, {'n': 'C', 'k': [6, 7]}]}
    assert A.minimax([[3, 8], [5, 2, 4], [6, 7]], False) == 5
    intro = game_tree(tree, False, 'Spelträd med MIN i roten R och tre MAX-noder A, B och C.', leaf_names=False) + p('Spelträdet söks igenom med minimax.')
    a = part(p('Vilket värde får B?'),
             [step('B är en MAX-nod', 'B = max(5, 2, 4) = 5.')],
             '5.', 'Titta på triangeln vid B. Väljer B största eller minsta värdet?', 1)
    b = part(p('Vilket värde får roten R?'),
             [step('A, B och C är MAX-noder', 'A = max(3, 8) = 8. B = max(5, 2, 4) = 5. C = max(6, 7) = 7.'),
              step('Roten är en MIN-nod', 'R = min(8, 5, 7) = 5.')],
             '5.', 'Bestäm först värdena i A, B och C.', 1)
    c = part(p('Vilket drag väljer MIN i roten? Välj ett alternativ.'),
             [step('MIN väljer barnet med lägst värde', 'A ger 8, B ger 5 och C ger 7. B ger lägst värde.')],
             'Draget till B.', 'Jämför värdena i rotens tre barn.', 2,
             [alt('Draget till A', False, 'A har värdet 8, det största värdet. MAX hade valt A, men i roten väljer MIN.'),
              alt('Draget till B', True, 'B har värdet 5, det minsta av 8, 5 och 7.'),
              alt('Draget till C', False, 'C har värdet 7, högre än B:s 5.'),
              alt('Draget mot lövet 2', False, 'Lövet 2 ligger under B, men där väljer MAX. MAX tar 5, inte 2.')])
    return task('3.06', 'minimax', 'MIN i roten', intro, [a, b, c],
                'Arbeta från löven och uppåt. Kontrollera triangeln i varje nod.', ['procedur', 'begrepp'])


def t307():
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [4, 6]}, {'n': 'B', 'k': ['x', 7]}]}
    for x in range(-5, 15):
        assert (min(x, 7) > 4) == (x >= 5)
    assert max(min(4, 6), min(10, 7)) == 7
    intro = (game_tree(tree, True, 'Spelträd med MAX i roten R och MIN-noderna A och B. Ett löv har det okända värdet x.', leaf_names=False) +
             p('Spelträdet söks igenom med minimax. Ett av löven har det okända värdet x.'))
    a = part(p('Vilket värde får A?'),
             [step('A är en MIN-nod', 'A = min(4, 6) = 4.')],
             '4.', 'Väljer A största eller minsta värdet?', 1)
    b = part(p('Antag att x = 10. Vilket värde får roten?'),
             [step('B är en MIN-nod', 'B = min(10, 7) = 7.'),
              step('Roten är en MAX-nod', 'A = min(4, 6) = 4. R = max(4, 7) = 7.')],
             '7.', 'Bestäm B först, sätt sedan in A och B i roten.', 2)
    c = part(p('För vilka heltal x får B ett större värde än A?'),
             [step('B = min(x, 7) och A = 4', 'Villkoret är min(x, 7) > 4.'),
              step('Två fall', 'Om x ≥ 7 blir B = 7, som är större än 4. Om x < 7 blir B = x, och då krävs x > 4.'),
              step('Sammanfatta för heltal', 'B > 4 gäller precis när x ≥ 5.')],
             'x ≥ 5.', 'Pröva några värden på x, till exempel 3, 5 och 9.', 3)
    return task('3.07', 'minimax', 'Ett okänt lövvärde', intro, [a, b, c],
                'Skriv B:s värde som min(x, 7) och jämför med A.', ['procedur', 'resonemang'])


def t308():
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [{'n': 'C', 'k': [-2, 4]}, 1]}, {'n': 'B', 'k': [{'n': 'D', 'k': [3, -5]}, {'n': 'E', 'k': [0, 2, -1]}]}]}
    assert A.minimax([[[-2, 4], 1], [[3, -5], [0, 2, -1]]], True) == 2
    intro = (game_tree(tree, True, 'Spelträd med MAX i roten R, MIN-noderna A och B och MAX-noderna C, D och E. Ett löv sitter direkt under A.', leaf_names=False) +
             p('Spelträdet söks igenom med minimax.'))
    a = part(p('Bestäm värdena i C, D och E.'),
             [step('C, D och E är MAX-noder', 'C = max(−2, 4) = 4. D = max(3, −5) = 3. E = max(0, 2, −1) = 2.')],
             'C = 4, D = 3, E = 2.', 'Vilket är det största värdet under varje nod? Var noga med minustecknen.', 2)
    b = part(p('Bestäm värdena i A, B och roten R.'),
             [step('A har ett barn som är en nod och ett barn som är ett löv', 'A är en MIN-nod: A = min(C, 1) = min(4, 1) = 1.'),
              step('B är en MIN-nod', 'B = min(D, E) = min(3, 2) = 2.'),
              step('Roten är en MAX-nod', 'R = max(1, 2) = 2.')],
             'A = 1, B = 2, R = 2.', 'Lövet under A jämförs på samma sätt som värdet i C.', 2)
    c = part(p('Vilket drag väljer roten? Välj ett alternativ.'),
             [step('MAX väljer barnet med högst värde', 'A ger 1 och B ger 2.')],
             'Draget till B.', 'Jämför värdena i A och B.', 2,
             [alt('Draget till A', False, 'A har värdet 1. Lövet 4 under C nås aldrig, eftersom MIN i A väljer 1.'),
              alt('Draget till B', True, 'B har värdet 2, högre än A:s 1.'),
              alt('Båda dragen är lika bra', False, 'A ger 1 och B ger 2, så B är bättre för MAX.')])
    return task('3.08', 'minimax', 'Ojämnt spelträd med negativa värden', intro, [a, b, c],
                'Ett löv kan sitta högre upp i trädet. Det jämförs med de andra barnens värden som vanligt.', ['procedur'])


def t309():
    vals = [[5, 9, 7], [4, 8, 6], [10, 3, 11]]
    log = []
    assert A.alphabeta(vals, True, log=log) == 5
    leaves = [x[1] for x in log if x[0] == 'leaf']
    assert leaves == [5, 9, 7, 4, 10, 3] and [x[1] for x in log if x[0] == 'cut'] == [[8, 6], [11]]
    tree = {'n': 'R', 'k': [{'n': n, 'k': v} for n, v in zip('ABC', vals)]}
    intro = (game_tree(tree, True, 'Spelträd med MAX i roten R och MIN-noderna A, B och C med tre löv var, L1–L9.') +
             p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))
    a = part(p('Vilket värde får roten?'),
             [step('Rotens barn är MIN-noder', 'A = min(5, 9, 7) = 5. B kan som mest bli 4, eftersom L4 = 4. C kan som mest bli 3, eftersom L8 = 3.'),
              step('Roten väljer det högsta värdet', 'Inget barn ger mer än A, så R = 5.')],
             '5.', 'Bestäm först A:s värde.', 2)
    b = part(p('Vilka löv beskärs?'),
             [step('A undersöks helt', 'A = min(5, 9, 7) = 5. Roten vet nu att den kan få minst 5, så α = 5.'),
              step('B: L4 = 4 ger β = 4 ≤ α = 5', 'B kan inte bli större än 4. Roten väljer ändå A, så L5 och L6 beskärs.'),
              step('C: L7 = 10 och sedan L8 = 3', 'Efter L7 är β = 10 > 5, så sökningen fortsätter. Efter L8 är β = 3 ≤ 5, så L9 beskärs.')],
             'L5, L6 och L9.', 'Jämför efter varje löv i B och C den bästa gränsen hittills med α = 5.', 3)
    c = part(p('Hur många löv utvärderas? Välj ett alternativ.'),
             [step('Räkna de löv som inte beskärs', 'L1, L2, L3, L4, L7 och L8 utvärderas.')],
             '6 löv.', 'Utgå från vilka löv som beskärs.', 3,
             [alt('9', False, 'Det är alla löv. Vanlig minimax utvärderar alla, men alfa–beta beskär tre av dem.'),
              alt('7', False, 'C kan också avbrytas: efter L8 = 3 är β = 3 ≤ α = 5, så L9 beskärs.'),
              alt('6', True, 'Tre löv beskärs, L5, L6 och L9, så 9 − 3 = 6 löv utvärderas.'),
              alt('3', False, 'A måste undersökas helt för att roten ska få gränsen α = 5. B och C måste också undersökas med minst ett löv var.')])
    return task('3.09', 'alfa_beta', 'Tre MIN-noder under roten', intro, [a, b, c],
                'När en MIN-nod hittar ett värde som är högst α behöver resten av dess barn inte undersökas.', ['procedur', 'begrepp'])


def t310():
    log = []
    assert A.alphabeta([[6, 9], [4, 8, 7]], True, log=log) == 6
    assert [x[1] for x in log if x[0] == 'cut'] == [[8, 7]]
    log2 = []
    A.alphabeta([[6, 9], [8, 7, 4]], True, log=log2)
    assert [x[1] for x in log2 if x[0] == 'leaf'] == [6, 9, 8, 7, 4] and not [x for x in log2 if x[0] == 'cut']
    tree = {'n': 'R', 'k': [{'n': 'A', 'k': [6, 9]}, {'n': 'B', 'k': [4, 8, 7]}]}
    intro = (game_tree(tree, True, 'Spelträd med MAX i roten R och MIN-noderna A och B. Löven heter L1–L5.') +
             p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).'))
    a = part(p('Vilket värde har α i roten när sökningen går vidare till B?'),
             [step('A undersöks först', 'A är en MIN-nod: A = min(6, 9) = 6.'),
              step('α är det bästa roten är säker på', 'Roten kan alltid välja A och få 6, så α = 6.')],
             'α = 6.', 'Vilket värde får A?', 2)
    b = part(p('Varför behöver L4 och L5 inte utvärderas? Välj ett alternativ.'),
             [step('B är en MIN-nod', 'När L3 = 4 är utvärderat vet man att B kan som mest bli 4, eftersom MIN väljer det minsta värdet.'),
              step('Jämför med α', 'Roten får redan 6 via A. Eftersom 4 < 6 väljer roten aldrig B, vad L4 och L5 än är.')],
             'A.', 'Hur stort kan B:s värde högst bli efter L3?', 3,
             [alt('B kan som mest få värdet 4, och roten får redan 6 via A.', True, 'MIN i B väljer 4 eller något ännu mindre. Det kan aldrig slå A:s 6.'),
              alt('L4 och L5 är större än L3.', False, 'Det vet man inte förrän löven har utvärderats. Beskärningen sker innan.'),
              alt('MIN väljer alltid det första lövet.', False, 'MIN väljer det minsta värdet bland alla barn. Men B kan inte bli större än 4, så resten spelar ingen roll för roten.'),
              alt('Roten har redan hittat det högsta möjliga värdet.', False, 'Roten vet bara att A ger 6. Det är jämförelsen med B:s gräns 4 som gör att B kan avbrytas.')])
    c = part(p('B:s löv byter ordning till 8, 7, 4. Hur många av B:s löv utvärderas nu?'),
             [step('Följ B:s gräns β efter varje löv', '8 ger β = 8 > 6. 7 ger β = 7 > 6. Sökningen måste fortsätta båda gångerna.'),
              step('Det sista lövet ger 4', 'Först nu är β = 4 ≤ 6, men då finns inga fler löv att beskära.')],
             '3 löv, alltså alla.', 'Jämför β med α = 6 efter varje löv i den nya ordningen.', 3)
    return task('3.10', 'alfa_beta', 'Ordningen avgör beskärningen', intro, [a, b, c],
                'Beskärning sker när en MIN-nods gräns β blir högst lika stor som rotens α.', ['procedur', 'begrepp', 'resonemang'])


NYA = [t110, t111, t112, t113, t114, t115, t116, t117, t118, t119,
       t212, t213, t214, t215, t216, t217, t218, t219, t220, t221, t222,
       t306, t307, t308, t309, t310]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    bank = [revidera(u) for u in bank]
    nya = [f() for f in NYA]
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    assert len({u['id'] for u in bank}) == len(bank)
    out = src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:]
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(out)
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya.')


if __name__ == '__main__':
    main()
