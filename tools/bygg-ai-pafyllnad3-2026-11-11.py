"""AI-banken 2026-11-11, femte omgången: övningsblad.

1. Tabeller som eleven fyller i får tomma, rymliga celler i stället för ”…”, och
   startraden heter ”Från början” i stället för ”–” (användarens återkoppling).
2. Granskning för AI 1: BFS- och A*-uppgifterna säger ”tas ut ur kön/öppna
   listan” i stället för det tvetydiga ”besöks”; ”Girig” med liten bokstav.
3. 24 nya uppgifter: 12 alfa–beta-träd i tre svårighetsgrader, 4 minimaxträd
   och en uppgift i vart och ett av de övriga åtta områdena.

Kör efter de två tidigare byggskripten:

    python tools/bygg-ai-pafyllnad-2026-11-11.py
    python tools/bygg-ai-pafyllnad2-2026-11-11.py
    python tools/bygg-ai-pafyllnad3-2026-11-11.py
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_spec = importlib.util.spec_from_file_location('ai_omg3', os.path.join(HERE, 'bygg-ai-pafyllnad-2026-11-11.py'))
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)
from ai_figurer import tab, step, maze, search_tree, game_tree  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, part, alt, task, names, lista, pil = B.p, B.part, B.alt, B.task, B.names, B.lista, B.pil
BANK = 'uppgifterai.js'
AB_INTRO = p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).')
MM_INTRO = p('Spelträdet söks igenom med minimax.')

# ---------------------------------------------------------------- 1. tabeller

BLANK = '<td style="text-align:left;min-width:7em;height:2.6em"></td>'
OLD_BLANK = '<td style="text-align:left;min-width:4.5em;height:2.2em"></td>'


def enkla_tabeller(html):
    html = html.replace('<td style="text-align:left">…</td>', BLANK).replace(OLD_BLANK, BLANK)

    def startrad(m):
        t = m.group(0)
        if '<thead><tr><th style="text-align:left">Tas ut</th>' in t:
            t = t.replace('<tr><td style="text-align:left">–</td>', '<tr><td style="text-align:left">Från början</td>')
        return t
    return re.sub(r'<table class="data">[\s\S]*?</table>', startrad, html)


# ---------------------------------------------------------------- 2. formuleringar

FRAGOR = {
    '1.01': [('<p>Ange besöksordningen.</p>', '<p>Ange i vilken ordning rutorna tas ut ur kön.</p>'),
             ('<p>Hur många rutor besöks, inklusive start och mål?</p>', '<p>Hur många rutor tas ut ur kön, inklusive start och mål?</p>')],
    '1.06': [('<p>Ange besöksordningen.</p>', '<p>Ange i vilken ordning rutorna tas ut ur kön.</p>')],
    '1.08': [('<p>Hur många rutor besöks?</p>', '<p>Hur många rutor tas ut ur kön?</p>')],
    '1.09': [('<p>Ange besöksordning och returnerad väg med BFS.</p>',
              '<p>Ange i vilken ordning BFS tar ut noderna ur kön, och vilken väg som returneras.</p>')],
    '2.02': [('<p>Ange besöksordningen.</p>', '<p>Ange i vilken ordning rutorna tas ut ur öppna listan.</p>'),
             ('<p>Hur många rutor besöks, inklusive start och mål?</p>', '<p>Hur många rutor tas ut ur öppna listan, inklusive start och mål?</p>')],
    '2.09': [('<p>Vilken ruta besöks härnäst med Girig bäst först? Välj ett alternativ.</p>',
              '<p>Vilken ruta tas ut härnäst med girig bäst först? Välj ett alternativ.</p>'),
             ('<p>Vilken ruta besöks härnäst med A*? Välj ett alternativ.</p>',
              '<p>Vilken ruta tas ut härnäst med A*? Välj ett alternativ.</p>')],
    '2.17': [('<p>Ange besöksordningen.</p>', '<p>Ange i vilken ordning rutorna tas ut ur öppna listan.</p>'),
             ('<p>Vilka besökta rutor ingår inte i den väg som A* returnerar?</p>',
              '<p>Vilka uttagna rutor ingår inte i den väg som A* returnerar?</p>')],
    '2.19': [('<p>Ange besöksordningen för A*.</p>', '<p>Ange i vilken ordning A* tar ut rutorna ur öppna listan.</p>')],
    '2.28': [('<p>Ange besöksordningen.</p>', '<p>Ange i vilken ordning rutorna tas ut ur öppna listan.</p>')],
}


# Kunskapsgymmets svarsinstruktion i parentes (bygg-ai-sjalvrattning-2026-11-11.py) står efter
# frågan i delkortet. Den ska inte hindra att kontrollen vid omkörning känner igen frågan.
KG_INSTR = re.compile(r' \((?:Skriv|Svara|Ange noden|Ta beskärningarna)[^)]*\)(?=</p>)')


def utan_kg(f):
    return KG_INSTR.sub('', f)


def revidera(u):
    for old, new in FRAGOR.get(u['id'], []):
        hit = [d for d in u['spelDelar'] if d['fraga'].startswith(old)]
        if not hit:
            assert any(utan_kg(d['fraga']).startswith(new) for d in u['spelDelar']), (u['id'], old)
            continue
        d = hit[0]
        d['fraga'] = new + d['fraga'][len(old):]
        a, b = '<p>' + d['etikett'] + ') ' + old[3:], '<p>' + d['etikett'] + ') ' + new[3:]
        assert u['t'].count(a) == 1, (u['id'], a)
        u['t'] = u['t'].replace(a, b)
    for key in ('t', 's', 'spelIntro'):
        u[key] = enkla_tabeller(u[key])
    for d in u['spelDelar']:
        d['fraga'] = enkla_tabeller(d['fraga'])
        d['s'] = enkla_tabeller(d['s'])
    return u


# ---------------------------------------------------------------- 3a. alfa–beta-träd

def ab_facit_root(r, notes, val):
    steps = []
    for k in r['kids']:
        if 'leaf' in k:
            continue
        nt = notes.get(k['name'])
        if nt is None:
            continue
        if nt['kind'] == 'exakt':
            rubr = f'Grenen till {k["name"]} undersöks helt: {k["name"]} = {T.fmt(nt["value"])}'
        else:
            rubr = f'Grenen till {k["name"]} avbryts: {k["name"]} blir {"minst" if nt["max"] else "högst"} {T.fmt(nt["value"])}'
        steps.append(step(rubr, *T.subtree_lines(k, notes)))
    op = 'MAX' if r['max'] else 'MIN'
    steps.append(step(f'Roten är en {op}-nod', T.node_line('R', notes['R'])))
    return steps


def ab_facit_cuts(cuts, notes):
    steps = []
    for name, after, a, b, rest in cuts:
        mx = notes[name]['max']
        if mx:
            why = f'{name} är en MAX-nod och blir minst {T.fmt(a)}. MIN ovanför är redan säker på högst {T.fmt(b)} och väljer aldrig {name}.'
        else:
            why = f'{name} är en MIN-nod och blir högst {T.fmt(b)}. MAX ovanför är redan säker på minst {T.fmt(a)} och väljer aldrig {name}.'
        steps.append(step(f'I {name} efter {after}: α = {T.fmt(a)} ≥ β = {T.fmt(b)}',
                          why, f'Därför beskärs {" och ".join(T.pruned_desc(rest))}.'))
    return steps


def ab_task(id_, familj, values, root_max, levels, third, ledtrad):
    r = T.build(values, root_max)
    val, ev, cuts, notes = T.alphabeta(r)
    assert val == T.minimax(T.build(values, root_max))
    nleaves = len(T.leaves(r))
    pr = T.pruned_leaves(cuts)
    desc = [d for c in cuts for d in T.pruned_desc(c[4])]
    rot = 'MAX' if root_max else 'MIN'
    title = f'Spelträd med {rot} i roten R och {nleaves} löv, L1–L{nleaves}.'
    intro = game_tree(T.to_figure(r), root_max, title) + AB_INTRO
    a = part(p('Vilket värde får roten?'), ab_facit_root(r, notes, val), f'{T.fmt(val)}.',
             'Arbeta från vänster. Bestäm först värdet i rotens första barn.', levels[0])
    b = part(p('Vilka grenar kan beskäras? Ange de löv som aldrig behöver utvärderas.'),
             ab_facit_cuts(cuts, notes) + [step('Alla beskurna löv', f'{", ".join(pr)}, totalt {len(pr)} av {nleaves} löv.')],
             T.cap('; '.join(desc)) + '.', 'Jämför efter varje utvärderat barn nodens gräns med α eller β ovanför.', levels[1])
    c = third(r, val, ev, cuts, notes, levels[2])
    return task(id_, 'alfa_beta', familj, intro, [a, b, c], ledtrad, ['procedur', 'begrepp'])


def q_drag(r, val, ev, cuts, notes, tn, extra=''):
    kids = [k for k in r['kids']]
    best = [k['name'] for k in kids if notes.get(k['name'], {}).get('kind') == 'exakt' and notes[k['name']]['value'] == val]
    assert len(best) == 1
    op = 'största' if r['max'] else 'minsta'
    txt = ', '.join(f'{n} ger {t}' for n, t in notes['R']['kids'])
    return part(p('Vilket drag väljer roten' + extra + '?'),
                [step(f'Roten väljer det {op} värdet', txt + '.')],
                f'Draget till {best[0]}' + (f', med värdet {T.fmt(val)}.' if extra else '.'),
                'Vilket av rotens barn ger rotens värde?', tn)


def q_antal(r, val, ev, cuts, notes, tn):
    n = len(T.leaves(r))
    return part(p('Hur många löv utvärderas?'),
                [step('Räkna löven som inte beskärs', f'{", ".join(ev)} utvärderas.')],
                f'{len(ev)} av {n} löv.', 'Utgå från vilka löv som beskärs.', tn)


def q_gräns(child, letter):
    def q(r, val, ev, cuts, notes, tn):
        idx = [k.get('name') for k in r['kids']].index(child)
        prev = [notes[k['name']] for k in r['kids'][:idx]]
        if r['max']:
            g = max(nt['value'] for nt in prev if nt['kind'] == 'exakt')
        else:
            g = min(nt['value'] for nt in prev if nt['kind'] == 'exakt')
        lines = [f'{k["name"]}: {"exakt " + T.fmt(nt["value"]) if nt["kind"] == "exakt" else ("minst " if nt["max"] else "högst ") + T.fmt(nt["value"])}.'
                 for k, nt in zip(r['kids'][:idx], prev)]
        bound = 'det bästa MAX i roten är säker på' if r['max'] else 'det bästa MIN i roten är säker på'
        return part(p(f'Vilket värde har {letter} i roten när sökningen går vidare till {child}?'),
                    [step(f'Rotens barn före {child}', *lines), step(f'{letter} är {bound}', f'{letter} = {T.fmt(g)}.')],
                    f'{letter} = {T.fmt(g)}.', f'Vilka barn till roten är klara innan {child} undersöks?', tn)
    return q


def q_nodvärde(node):
    def q(r, val, ev, cuts, notes, tn):
        nt = notes[node]
        assert nt['kind'] == 'exakt'
        return part(p(f'Vilket värde får {node}?'), [step(f'{node} undersöks helt', T.node_line(node, nt))],
                    f'{T.fmt(nt["value"])}.', f'Är {node} en MAX- eller en MIN-nod?', tn)
    return q


def q_första(r, val, ev, cuts, notes, tn):
    name, after, a, b, rest = cuts[0]
    return part(p('I vilken nod sker den första beskärningen?'),
                [step('Följ sökningen från vänster', f'Den första nod där α ≥ β blir sant är {name}, efter {after}: α = {T.fmt(a)} och β = {T.fmt(b)}.')],
                f'I {name}.', 'Gå igenom löven från vänster och uppdatera α och β efter varje löv.', tn)


def q_sparar(r, val, ev, cuts, notes, tn):
    n = len(T.leaves(r))
    return part(p('Hur många löv sparar alfa–beta jämfört med minimax utan beskärning?'),
                [step('Minimax utvärderar alla löv', f'Trädet har {n} löv.'),
                 step('Alfa–beta utvärderar färre', f'{len(ev)} löv utvärderas, så {n} − {len(ev)} = {n - len(ev)} löv sparas.')],
                f'{n - len(ev)} löv.', 'Räkna löven som beskärs.', tn)


def q_hel_gren(node_cut):
    def q(r, val, ev, cuts, notes, tn):
        cut = [c for c in cuts if c[0] == node_cut][0]
        name, after, a, b, rest = cut
        whole = [k['name'] for k in rest if 'leaf' not in k][0]
        mx = notes[name]['max']
        right = (f'{name} kan som mest bli {T.fmt(b)}, och roten har redan {T.fmt(a)}.' if not mx
                 else f'{name} blir minst {T.fmt(a)}, och roten har redan {T.fmt(b)}.')
        alts = [alt(right, True, 'Inget som finns under ' + whole + ' kan ändra rotens val, så hela grenen kan hoppas över.'),
                alt(f'Alla löv under {whole} är mindre än de löv som redan har utvärderats.', False,
                    'Det vet man inte, eftersom löven under ' + whole + ' aldrig utvärderas. Beskärningen sker innan.'),
                alt(f'{whole} ligger längst till höger och undersöks därför aldrig.', False,
                    'Placeringen avgör inte. Det är jämförelsen mellan α och β som gör att grenen kan beskäras.'),
                alt('Alfa–beta undersöker bara den första grenen under varje nod.', False,
                    'Alfa–beta fortsätter så länge α < β. Här blir α ≥ β redan efter ' + after + '.')]
        return part(p(f'Varför kan hela grenen till {whole} beskäras? Välj ett alternativ.'),
                    [step(f'I {name} efter {after}: α = {T.fmt(a)} och β = {T.fmt(b)}', right),
                     step('Då spelar resten av grenen ingen roll', f'Oavsett värdena under {whole} ändras inte rotens val.')],
                    'A.', f'Hur bra kan {name} som bäst bli för spelaren ovanför?', tn, alts)
    return q


def q_alfa_i(node):
    def q(r, val, ev, cuts, notes, tn):
        cut = [c for c in cuts if c[0] == node][0]
        name, after, a, b, rest = cut
        return part(p(f'Vilka värden har α och β i noden {node} när beskärningen sker?'),
                    [step(f'Följ gränserna ned till {node}', f'Efter {after} är α = {T.fmt(a)} och β = {T.fmt(b)} i {node}.'),
                     step('Villkoret för beskärning', f'{T.fmt(a)} ≥ {T.fmt(b)}, så resten av {node}:s barn beskärs.')],
                    f'α = {T.fmt(a)}, β = {T.fmt(b)}.', f'α och β förs ned från roten till {node} och uppdateras efter varje barn.', tn)
    return q


def q_exakt(r, val, ev, cuts, notes, tn):
    ex = [k['name'] for k in r['kids'] if notes[k['name']]['kind'] == 'exakt']
    gr = [k['name'] for k in r['kids'] if notes[k['name']]['kind'] != 'exakt']
    lines = [f'{k["name"]}: ' + ('exakt ' + T.fmt(notes[k['name']]['value']) if notes[k['name']]['kind'] == 'exakt'
                                 else ('minst ' if notes[k['name']]['max'] else 'högst ') + T.fmt(notes[k['name']]['value'])) + '.'
             for k in r['kids']]
    return part(p('Vilka av rotens barn får ett exakt värde, och vilka får bara en gräns?'),
                [step('En nod som avbryts får bara en gräns', *lines)],
                f'Exakt: {", ".join(ex)}. Bara gräns: {", ".join(gr)}.', 'Vilka av rotens barn avbröts av en beskärning?', tn)


def q_alla_snitt(r, val, ev, cuts, notes, tn):
    lines = [f'{c[0]} (efter {c[1]}): α = {T.fmt(c[2])}, β = {T.fmt(c[3])}.' for c in cuts]
    return part(p('I vilka noder sker beskärningar, och vilka värden har α och β där?'),
                [step('Beskärning sker där α ≥ β', *lines)],
                ' '.join(lines), 'Leta efter noder där gränsen från ovan och nodens eget bästa värde möts.', tn)


AB = [
    # id, familj, värden, MAX i roten, nivåer (a, b, c), tredje fråga, ledtråd
    ('3.15', 'Rotvärde och beskärning – lätt', [[3, 7], [2, 9]], True, (1, 2, 2), lambda *x: q_drag(*x),
     'Bestäm A först. Fundera sedan på hur stort B kan bli efter sitt första löv.'),
    ('3.16', 'Rotvärde och beskärning – lätt', [[6, 8], [7, 9], [4, 5]], True, (1, 2, 2), q_antal,
     'Ett MIN-barn som får ett lågt löv kan inte längre slå roten bästa alternativ.'),
    ('3.17', 'Rotvärde och beskärning – lätt', [[4, 6], [7, 2, 9]], False, (1, 2, 2), q_gräns('B', 'β'),
     'Roten är en MIN-nod. Ett MAX-barn som får ett högt löv kan inte längre bli rotens val.'),
    ('3.18', 'Rotvärde och beskärning – lätt', [[2, 5, 3], [4, 1], [6, 8]], False, (1, 2, 2), q_nodvärde('B'),
     'Roten är en MIN-nod och vill ha så lågt värde som möjligt.'),
    ('3.19', 'Rotvärde och beskärning – medel', [[6, 9, 8], [3, 10, 7], [7, 2, 12]], True, (2, 3, 3), q_första,
     'Efter A vet roten att den kan få minst A:s värde. Jämför varje nytt löv i B och C med det.'),
    ('3.20', 'Rotvärde och beskärning – medel', [[5, 2, 3], [9, 4, 6], [6, 7, 1]], False, (2, 3, 3), q_sparar,
     'Roten är en MIN-nod. Jämför varje nytt löv i B och C med A:s värde.'),
    ('3.21', 'Rotvärde och beskärning – medel', [[[5, 7], [9, 6]], [[3, 2], [4, 8]]], True, (2, 3, 3), q_hel_gren('B'),
     'Gränserna förs ned genom trädet. En beskärning kan ske både nära löven och högre upp.'),
    ('3.22', 'Rotvärde och beskärning – medel', [[[4, -1], [-2, -3]], [[5, 1], [-3, 2]]], False, (2, 3, 3), q_alfa_i('D'),
     'Var noga med minustecknen. −3 är mindre än −2.'),
    ('3.23', 'Rotvärde och beskärning – svår', [[[0, 1], [3, 3]], [[0, 0], [9, 9]], [[6, 5], [8, 2]]], True, (3, 4, 4), q_exakt,
     'Håll isär exakta värden och gränser. En nod som avbryts får bara en gräns.'),
    ('3.24', 'Rotvärde och beskärning – svår', [[[12, 10], [5, 6], [14, 7]], [[11, 11], [13, 12], [6, 4]]], False, (3, 4, 4), q_alla_snitt,
     'Roten är en MIN-nod. När B:s första barn blir för högt kan resten av B hoppas över.'),
    ('3.25', 'Rotvärde och beskärning – svår', [[[5, 9, -5], [4, -1]], [[1, -6], [1, -1, 5]], [[-1, -5], [8, -1]]], True, (3, 4, 4), q_gräns('C', 'α'),
     'Bestäm A helt först. Då vet roten vad den minst kan få.'),
    ('3.26', 'Rotvärde och beskärning – svår', [[[12, 3], [-1, 5]], [[8, 10], [10, 5, -5]], [[-4, 2, -2], [3, 5]]], False, (3, 4, 4),
     q_nodvärde('C'),
     'Roten är en MIN-nod. Följ β i roten och jämför med varje MAX-barn.'),
]


# ---------------------------------------------------------------- 3b. minimaxträd

def mm_values(n, out):
    if 'leaf' in n:
        return n['leaf']
    vals = [mm_values(k, out) for k in n['kids']]
    v = max(vals) if n['max'] else min(vals)
    out[n['name']] = (n['max'], vals, v)
    return v


def mm_line(name, info):
    mx, vals, v = info
    return f'{name} = {"max" if mx else "min"}({", ".join(T.fmt(x) for x in vals)}) = {T.fmt(v)}.'


def mm_task(id_, values, root_max, groups, third, levels, ledtrad):
    r = T.build(values, root_max)
    info = {}
    val = mm_values(r, info)
    rot = 'MAX' if root_max else 'MIN'
    nl = len(T.leaves(r))
    intro = game_tree(T.to_figure(r), root_max, f'Spelträd med {rot} i roten R och {nl} löv.', leaf_names=(third == 'väg')) + MM_INTRO
    parts = []
    for (q, nodes), tn in zip(groups, levels):
        typer = {info[n][0] for n in nodes}
        assert len(typer) == 1, (id_, nodes)
        typ = 'MAX' if typer.pop() else 'MIN'
        namn = ', '.join(nodes[:-1]) + ' och ' + nodes[-1]
        parts.append(part(p(q), [step(f'{namn} är {typ}-noder', *[mm_line(n, info[n]) for n in nodes])],
                          ', '.join(f'{n} = {T.fmt(info[n][2])}' for n in nodes) + '.', ledtrad, tn))
    kids = [k for k in r['kids'] if 'leaf' not in k]
    best = [k['name'] for k in r['kids'] if 'leaf' not in k and info[k['name']][2] == val]
    assert len(best) == 1
    op = 'största' if root_max else 'minsta'
    if third == 'drag':
        parts.append(part(p('Vilket värde får roten, och vilket drag väljer den?'),
                          [step(f'Roten väljer det {op} värdet', mm_line('R', info['R']))],
                          f'Värdet {T.fmt(val)}, draget till {best[0]}.', 'Jämför värdena i rotens barn.', levels[-1]))
    else:
        path, lines, n = ['R'], [], r
        while 'leaf' not in n:
            v = info[n['name']][2]
            kids = [k for k in n['kids'] if (k['leaf'] if 'leaf' in k else info[k['name']][2]) == v]
            assert len(kids) == 1, id_
            k = kids[0]
            label = k['name'] if 'leaf' not in k else f'lövet {T.fmt(k["leaf"])} ({k["name"]})'
            lines.append(f'{n["name"]} har värdet {T.fmt(v)}, som kommer från {label}.')
            path.append(label)
            n = k
        parts.append(part(p('Ange vägen genom trädet när båda spelarna spelar så bra som möjligt (R → … → löv).'),
                          [step('Följ i varje nod det barn som ger nodens värde', *lines)],
                          ' → '.join(path) + '.', 'Börja i roten och gå hela tiden till det barn som har samma värde som noden.', levels[-1]))
    return task(id_, 'minimax', 'Minimax – träd att lösa', intro, parts,
                'Arbeta från löven och uppåt. Triangeln visar om noden väljer största eller minsta värdet.', ['procedur'])


MM = [
    ('3.27', [[4, 9], [6, 3], [8, 7]], False, [('Vilka värden får MAX-noderna A, B och C?', ['A', 'B', 'C'])], 'drag', (1, 1)),
    ('3.28', [[[3, -2], [5, 1]], [[-4, 6], [2, 0]]], True,
     [('Bestäm värdena i C, D, E och F.', ['C', 'D', 'E', 'F']), ('Bestäm värdena i A och B.', ['A', 'B'])], 'väg', (2, 2, 2)),
    ('3.29', [[[2, 7], [5, 3]], [[6, 1], [4, 9]], [[8, 3], [5, 6]]], False,
     [('Bestäm värdena i MIN-noderna D–I.', ['D', 'E', 'F', 'G', 'H', 'I']), ('Bestäm värdena i A, B och C.', ['A', 'B', 'C'])], 'drag', (2, 2, 3)),
    ('3.30', [[4, [2, 7, 1]], [[5, 3], 6, [-1, 8]]], True,
     [('Bestäm värdena i C, D och E.', ['C', 'D', 'E']), ('Bestäm värdena i A och B.', ['A', 'B'])], 'väg', (2, 2, 3)),
]


# ---------------------------------------------------------------- 3c. övriga områden

def t128():
    st, out, rows = [], [], []
    steps = ['+A', '+B', '-', '+C', '+D', '+E', '-', '-', '+F']
    lbl = {'-': 'Ta ut'}
    for op in steps:
        if op[0] == '+':
            st.append(op[1])
        else:
            out.append(st.pop())
        rows.append([lbl.get(op, f'Lägg in {op[1:]}') + (f' ({out[-1]})' if op == '-' else ''), ' '.join(st)])
    assert out == ['B', 'E', 'D'] and st == ['A', 'C', 'F']
    intro = (p('Noder läggs in i och tas ut ur en stack enligt stegen i tabellen. Den översta noden står längst till höger.'))
    blank = [[('Lägg in ' + op[1]) if op[0] == '+' else 'Ta ut', '…'] for op in steps]
    a = part(p('Fyll i tabellen.') + tab(['Steg', 'Stacken efter steget'], blank),
             [step('Ny nod läggs överst, uttag tar den översta', tab(['Steg', 'Stacken efter steget'], rows))],
             'Stacken slutar som A C F, med F överst.', 'Nya noder hamnar längst till höger. Uttag tar alltid noden längst till höger.', 1)
    b = part(p('Vilka noder har tagits ut, i ordning?'),
             [step('Det första uttaget', 'B ligger överst och tas ut.'),
              step('Två uttag efter C, D och E', 'E ligger överst, sedan D.')],
             'B, E, D.', 'Vilken nod ligger överst vid varje uttag?', 1)
    return task('1.28', 'ko_stack', 'Stacken i en tabell', intro, [a, b],
                'I en stack tas alltid den senast inlagda noden ut först.', ['procedur'], 1)


TREE_129 = dict(nodes={'S': (200, 35), 'A': (80, 110), 'B': (200, 110), 'C': (320, 110), 'D': (80, 185), 'E': (160, 185),
                       'F': (240, 185), 'G': (320, 185)},
                edges=[('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'G')],
                start='S', goals=['G'], width=400,
                title='Sökträd: S har barnen A, B och C. A har D, B har E och F, och C har målet G.')


def t129():
    kids = {'S': ['A', 'B', 'C'], 'A': ['D'], 'B': ['E', 'F'], 'C': ['G']}
    st, rows, out = ['S'], [['–', 'S']], []
    while st:
        n = st.pop()
        out.append(n)
        if n != 'G':
            st += list(reversed(kids.get(n, [])))
        rows.append([n, ' '.join(st) or 'tom'])
        if n == 'G':
            break
    assert out == ['S', 'A', 'D', 'B', 'E', 'F', 'C', 'G']
    intro = (search_tree(**TREE_129) +
             p('Trädet söks igenom med DFS (vänster gren först). Noderna sparas i en stack, och barnen läggs in så att det vänstra barnet hamnar överst. '
               'I tabellen står den översta noden längst till höger.'))
    a = part(p('Fyll i tabellen tills målet tas ut.') + tab(['Tas ut', 'Stacken efter uttaget'], [['–', 'S']] + [['…', '…']] * 8),
             [step('S lägger C, B och A på stacken', 'A hamnar överst och tas ut först.'),
              step('Stacken efter varje uttag', tab(['Tas ut', 'Stacken efter uttaget'], rows))],
             'Noderna tas ut i ordningen ' + lista(out) + '.', 'Ta alltid ut den översta noden. Lägg dess barn i omvänd ordning, så att det vänstra hamnar överst.', 2)
    b = part(p('Hur många noder tas ut ur stacken, inklusive start och mål?'),
             [step('Målet ligger i den sista grenen', 'DFS går först igenom hela grenen under A och hela grenen under B.'),
              step('Räkna uttagen', lista(out) + ': 8 noder.')],
             '8 noder.', 'I vilken gren ligger målet?', 2)
    return task('1.29', 'ko_sokning', 'Stacken när ett träd söks igenom', intro, [a, b],
                'Den översta noden tas ut. Barnen läggs på stacken i omvänd ordning, så att det vänstra barnet tas ut först.', ['procedur'])


M130 = ['S..#.', '.#...', '...#.', '#.#.G']


def t130():
    s, g = A.parse(M130)
    r = A.bfs(M130)
    order, path = names(r['order']), names(r['path'])
    assert order == ['A1', 'A2', 'B1', 'A3', 'C1', 'B3', 'C2', 'B4', 'C3', 'D2', 'B5', 'A5', 'C5', 'D5']
    assert path == ['A1', 'A2', 'A3', 'B3', 'B4', 'B5', 'C5', 'D5']
    assert all('D4' not in names(q) for _, q in r['snaps']) and 'D4' not in order
    intro = maze(M130, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = part(p('Ange i vilken ordning rutorna tas ut ur kön, fram till och med målet.'),
             [step('Nivå för nivå från start', 'A1 lägger in A2 och B1. Sedan kommer rutorna två steg bort (A3, C1), tre steg bort (B3, C2) och så vidare.'),
              step('Hela ordningen', lista(order) + '.')],
             lista(order) + '.', 'Skriv upp kön efter varje uttag och lägg nya rutor längst bak.', 2)
    b = part(p('Ange vägen BFS returnerar och antalet steg.'),
             [step('Följ föregångarna från målet', 'D5 ← C5 ← B5 ← B4 ← B3 ← A3 ← A2 ← A1.'),
              step('Räkna stegen', '8 rutor ger 7 steg.')],
             pil(path) + ', 7 steg.', 'Vilken ruta lade in målet i kön?', 2)
    c = part(p('Vilken ruta läggs aldrig in i kön? Välj ett alternativ.'),
             [step('D4 nås bara från målet', 'D4 har väggar ovanför och till vänster och kan bara nås från målet D5. Sökningen stoppar när målet tas ut, så D4 läggs aldrig in.')],
             'D4.', 'Vilka grannar har D4?', 3,
             [alt('D4', True, 'D4 nås bara via målet, och sökningen stoppar när målet tas ut.'),
              alt('A5', False, 'A5 läggs in av B5 och tas ut före målet.'),
              alt('D2', False, 'D2 läggs in av C2 och tas ut.'),
              alt('C3', False, 'C3 läggs in och tas ut innan målet.')])
    return task('1.30', 'bfs', 'BFS i 4 × 5 med en dold ruta', intro, [a, b, c],
                'BFS tar ut rutorna i ordning efter avstånd från start.', ['procedur'])


M131 = ['S.#..', '...#.', '.#...', '.#.#G']


def t131():
    s, g = A.parse(M131)
    r = A.dfs(M131)
    order, path = names(r['order']), names(r['path'])
    assert order == ['A1', 'A2', 'B2', 'B3', 'C3', 'C4', 'C5', 'B5', 'A5', 'A4', 'D5']
    assert path == ['A1', 'A2', 'B2', 'B3', 'C3', 'C4', 'C5', 'D5'] and len(A.bfs(M131)['path']) - 1 == 7
    intro = maze(M131, s, g) + p('Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).')
    a = part(p('Ange besöksordningen.'),
             [step('Följ första tillåtna riktning', 'A1 → A2 → B2 → B3 → C3 → C4 → C5.'),
              step('I C5 kommer ↑ före ↓', 'DFS går upp till B5, A5 och A4. A4 är en återvändsgränd, så sökningen backar till C5 och går ned till målet.')],
             lista(order) + '.', 'Gå så långt det går i första tillåtna riktningen. Backa när det tar stopp.', 2)
    b = part(p('Ange vägen DFS hittar och antalet steg.'),
             [step('Återvändsgränden ingår inte', 'B5, A5 och A4 tas bort från vägen när DFS backar.'),
              step('Räkna stegen', '8 rutor ger 7 steg.')],
             pil(path) + ', 7 steg.', 'Vilka rutor ligger kvar på vägen när målet nås?', 2)
    c = part(p('Hittar BFS en kortare väg i samma labyrint? Välj ett alternativ.'),
             [step('Den kortaste vägen', 'Målet ligger 3 rader och 4 kolumner bort, så minst 7 steg behövs. DFS-vägen har redan 7 steg.')],
             'Nej, båda vägarna har 7 steg.', 'Hur många steg behövs minst för att nå målet?', 3,
             [alt('Ja, BFS hittar alltid en kortare väg än DFS.', False, 'BFS hittar en kortaste väg, men DFS kan råka hitta en lika kort.'),
              alt('Nej, båda vägarna har 7 steg.', True, 'Ingen väg kan vara kortare än 3 + 4 = 7 steg.'),
              alt('Ja, BFS hittar en väg med 6 steg.', False, 'Målet ligger 3 rader och 4 kolumner bort, så minst 7 steg behövs.')])
    return task('1.31', 'dfs', 'DFS hittar en kortaste väg', intro, [a, b, c],
                'DFS hittar en väg, men inte alltid den kortaste. Jämför med det minsta antalet steg som behövs.', ['procedur', 'begrepp'])


def t231():
    ops = [('A', 4), ('B', 2), ('C', 6), None, ('D', 1), ('E', 3), None, None]
    q, out = [], []
    for op in ops:
        if op:
            q.append(op)
        else:
            q.sort(key=lambda x: x[1])
            out.append(q.pop(0)[0])
    assert out == ['B', 'D', 'E'] and q == [('A', 4), ('C', 6)]
    rows = [[str(i + 1), f'Lägg in {o[0]}({o[1]})' if o else 'Ta ut'] for i, o in enumerate(ops)]
    intro = (p('Noder läggs in i och tas ut ur en prioritetskö enligt tabellen. Talet inom parentes är nodens värde, och noden med lägst värde tas ut först.') +
             tab(['Steg', 'Händelse'], rows))
    a = part(p('Vilka noder tas ut, i ordning?'),
             [step('Steg 4', 'I kön finns A(4), B(2) och C(6). B har lägst värde.'),
              step('Steg 7 och 8', 'I kön finns A(4), C(6), D(1) och E(3). D tas ut först och sedan E.')],
             'B, D, E.', 'Skriv upp vad som ligger i kön före varje uttag.', 1)
    b = part(p('Vilka noder ligger kvar i kön efter steg 8?'),
             [step('A och C har aldrig lägst värde vid ett uttag', 'De har värdena 4 och 6.')],
             'A(4) och C(6).', 'Vilka noder har tagits ut?', 1)
    return task('2.31', 'prioritetsko', 'Prioritetskön i en tabell', intro, [a, b],
                'Vid varje uttag jämförs värdena på alla noder som ligger i kön just då.', ['procedur'], 1)


M232 = ['S....', '.#.#.', '...#.', '#.#.G']
MARK232 = {(0, 3): 'P', (2, 1): 'Q', (3, 3): 'R'}


def t232():
    s, g = A.parse(M232)
    d = A.dist_all(M232, s)
    v = {k: (d[c], A.manhattan(c, g)) for c, k in MARK232.items()}
    assert v == {'P': (3, 4), 'Q': (3, 4), 'R': (8, 1)}
    intro = (maze(M232, s, g, MARK232, extra_legend=[('#fff3b0', 'Markerad ruta')]) + p(B.ASTAR_GH))
    a = part(p('Fyll i tabellen.') + tab(['Ruta', 'g', 'h', 'f'], [[k, '…', '…', '…'] for k in 'PQR']),
             [step('g följer gångarna från start', 'P: A1 → A2 → A3 → A4, g = 3. Q: A1 → B1 → C1 → C2, g = 3. '
                   'R nås bara via målsidan: A1 → A2 → A3 → A4 → A5 → B5 → C5 → D5 → D4, g = 8.'),
              step('h = radskillnad + kolumnskillnad till D5', 'P: 3 + 1 = 4. Q: 1 + 3 = 4. R: 0 + 1 = 1.'),
              step('f = g + h', tab(['Ruta', 'g', 'h', 'f'], [['P', '3', '4', '7'], ['Q', '3', '4', '7'], ['R', '8', '1', '9']]))],
             'P: 3, 4, 7. Q: 3, 4, 7. R: 8, 1, 9.', 'Räkna g längs gångarna men h rakt, utan väggar.', 2)
    b = part(p('Vilken av rutorna har högst f? Välj ett alternativ.'),
             [step('Jämför f', 'P och Q har f = 7, R har f = 9.'),
              step('Lågt h räcker inte', 'R ligger bredvid målet men har kostat mycket att nå, g = 8.')],
             'R.', 'Jämför f-värdena från tabellen.', 2,
             [alt('P', False, 'P har f = 3 + 4 = 7.'),
              alt('Q', False, 'Q har f = 3 + 4 = 7.'),
              alt('R', True, 'R har lägst h, men g = 8 gör att f = 9 blir högst.')])
    return task('2.32', 'astar_varden', 'g, h och f för tre rutor', intro, [a, b],
                'g är kostnaden längs gångarna, h är avståndet rakt till målet utan väggar.', ['procedur', 'begrepp'])


M233 = ['.S..', '.#.#', '...G']


def t233():
    s, g = A.parse(M233)
    r = A.astar(M233)
    assert names(r['order']) == ['A2', 'A3', 'A4', 'B3', 'C3', 'C4'] and names(r['path']) == ['A2', 'A3', 'B3', 'C3', 'C4']
    rows = [[A.cname(c), str(r['g'][c]), str(A.manhattan(c, g)), str(r['g'][c] + A.manhattan(c, g))] for c in r['order']]
    intro = maze(M233, s, g) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). ' + B.ASTAR_TIE)
    a = part(p('Fyll i tabellen med rutorna i den ordning de tas ut ur öppna listan.') +
             tab(['Tas ut', 'g', 'h', 'f'], [['A2', '0', '4', '4']] + [['…', '…', '…', '…']] * 5),
             [step('A3 har lägre f än A1', 'A3: 1 + 3 = 4. A1: 1 + 5 = 6.'),
              step('A4 och B3 har samma f och h', 'Båda har f = 4 och h = 2. A4 kommer först i bokstavsordning, men är en återvändsgränd.'),
              step('Sedan B3, C3 och målet', tab(['Tas ut', 'g', 'h', 'f'], rows))],
             'A2, A3, A4, B3, C3, C4.', 'Räkna g, h och f för varje ny granne. Vid lika f: lägst h, sedan bokstavsordning.', 3)
    b = part(p('Vilken uttagen ruta ingår inte i vägen som A* returnerar?'),
             [step('Vägen', pil(names(r['path'])) + '.'),
              step('A4 leder inte vidare', 'Under A4 finns en vägg, så A4 har inga nya grannar.')],
             'A4.', 'Vilken ruta valdes på grund av bokstavsordningen?', 2)
    return task('2.33', 'astar_sokning', 'A* i en tabell', intro, [a, b],
                'Alla rutor på en kortaste väg har samma f här. Då avgör h och sedan bokstavsordningen.', ['procedur'])


M234 = ['.....', '.###.', 'S43.G']


def t234():
    s, g = A.parse(M234)
    c, path = A.ucs_grid(M234)
    straight = [(2, 1), (2, 2), (2, 3), (2, 4)]
    assert c == 8 and len(path) - 1 == 8 and A.path_cost(M234, [s] + straight) == 9
    assert A.path_cost(M234, A.astar(M234)['path']) == 8
    intro = maze(M234, s, g) + p('Att gå in i en isruta kostar 4, en lerruta 3 och en vit ruta eller målet 1. Start kostar 0.')
    a = part(p('Vägen rakt åt höger, C1 → C2 → C3 → C4 → C5, är kortast i antal steg. Vad kostar den?'),
             [step('Kostnad för varje ruta', 'C2 (is) 4, C3 (lera) 3, C4 1 och målet C5 1.'),
              step('Summera', '4 + 3 + 1 + 1 = 9.')],
             '9.', 'Räkna kostnaden för varje ruta du går in i.', 1)
    b = part(p('Vad kostar den billigaste vägen, och hur många steg har den?'),
             [step('Gå runt över rad A', pil(names(path)) + '.'),
              step('Bara vita rutor', '8 steg som kostar 1 var ger kostnaden 8.')],
             'Kostnad 8, 8 steg.', 'Finns det en väg som undviker både is och lera?', 2)
    c = part(p('Vilken väg returnerar A* med h = Manhattanavstånd? Välj ett alternativ.'),
             [step('A* hittar den billigaste vägen', 'h är aldrig större än den verkliga kostnaden kvar, eftersom varje ruta kostar minst 1. Då hittar A* den billigaste vägen.')],
             'Vägen över rad A, kostnad 8.', 'Vad räknar A* med: antal steg eller kostnad?', 3,
             [alt('Den raka vägen, eftersom den har minst antal steg', False, 'A* räknar med kostnaden g, inte antalet steg. Den raka vägen kostar 9.'),
              alt('Vägen över rad A, kostnad 8', True, 'A* jämför f = g + h och hittar den billigaste vägen.'),
              alt('Ingen väg, eftersom isen blockerar', False, 'Isen är dyr men går att gå på.')])
    return task('2.34', 'viktade_vagar', 'Kort väg eller billig väg', intro, [a, b, c],
                'Jämför kostnaden för den raka vägen med kostnaden för omvägen.', ['procedur', 'begrepp'])


NYA = [t128, t129, t130, t131, t231, t232, t233, t234]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = [f() for f in NYA]
    nya += [ab_task(*x) for x in AB]
    for id_, vals, rm, groups, third, levels in MM:
        nya.append(mm_task(id_, vals, rm, groups, third, levels, 'Börja på nivån närmast löven och arbeta uppåt.'))
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    bank = [revidera(u) for u in bank]
    assert len({u['id'] for u in bank}) == len(bank)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya i denna omgång.')


if __name__ == '__main__':
    main()
