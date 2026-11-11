"""Spelträd för AI-bankens minimax- och alfa–beta-uppgifter.

Ett träd skrivs som nästlade listor med tal i löven, t.ex. [[3, 5], [6, 1, 4]].
Inre noder namnges i nivåordning (R, A, B, C, …) och löven L1, L2, … från
vänster, precis som i ai_figurer.game_tree.
"""


def build(values, root_max):
    names = iter('ABCDEFGHIJKMNOPQSTUVWXYZ')  # L och R används till löv och rot
    leaf_no = [0]
    root = {'name': 'R', 'max': root_max}
    level = [(root, values)]
    while level:
        nxt = []
        for node, v in level:
            node['kids'] = []
            for child in v:
                if isinstance(child, list):
                    k = {'name': next(names), 'max': not node['max']}
                    nxt.append((k, child))
                else:
                    k = {'leaf': child}
                node['kids'].append(k)
        level = nxt

    def number(n):
        if 'leaf' in n:
            leaf_no[0] += 1
            n['name'] = f'L{leaf_no[0]}'
        else:
            for k in n['kids']:
                number(k)
    number(root)
    return root


def to_figure(n):
    if 'leaf' in n:
        return n['leaf']
    return {'n': n['name'], 'k': [to_figure(k) for k in n['kids']]}


def leaves(n):
    return [n['name']] if 'leaf' in n else [x for k in n['kids'] for x in leaves(k)]


def minimax(n):
    if 'leaf' in n:
        return n['leaf']
    vals = [minimax(k) for k in n['kids']]
    n['mm'] = max(vals) if n['max'] else min(vals)
    return n['mm']


def fmt(v):
    return str(v).replace('-', '−')


def alphabeta(root):
    """Returnerar (värde, utvärderade löv, beskärningar, anteckningar per nod).
    En beskärning är (nod, efter barn, α, β, beskurna barn). Anteckningar:
    nod -> dict(kind='exakt'|'gräns', value, kids=[(barn, text)], cut=…)."""
    evaluated, cuts, notes = [], [], {}

    def ab(n, a, b):
        if 'leaf' in n:
            evaluated.append(n['name'])
            return n['leaf'], True
        v = float('-inf') if n['max'] else float('inf')
        kid_txt, cut = [], None
        for i, k in enumerate(n['kids']):
            x, exact = ab(k, a, b)
            if exact:
                kid_txt.append((k['name'], fmt(x)))
            else:
                kid_txt.append((k['name'], ('minst ' if k['max'] else 'högst ') + fmt(x)))
            if n['max']:
                v = max(v, x)
                a = max(a, v)
            else:
                v = min(v, x)
                b = min(b, v)
            if a >= b and i + 1 < len(n['kids']):
                cut = (n['name'], k['name'], a, b, n['kids'][i + 1:])
                cuts.append(cut)
                break
        notes[n['name']] = dict(kind='gräns' if cut else 'exakt', value=v, kids=kid_txt, cut=cut, max=n['max'])
        return v, cut is None

    v, _ = ab(root, float('-inf'), float('inf'))
    return v, evaluated, cuts, notes


def pruned_desc(kids):
    out = []
    for k in kids:
        if 'leaf' in k:
            out.append(k['name'])
        else:
            out.append(f'grenen till {k["name"]} ({", ".join(leaves(k))})')
    return out


def pruned_leaves(cuts):
    return [x for c in cuts for k in c[4] for x in leaves(k)]


def cap(t):
    return t[:1].upper() + t[1:]


def node_line(name, note):
    """En rad som beskriver vad som händer i en nod."""
    vals = [t for _, t in note['kids']]
    op = 'max' if note['max'] else 'min'
    if note['kind'] == 'exakt':
        if all(t.lstrip('−').isdigit() for t in vals):
            return f'{name} = {op}({", ".join(vals)}) = {fmt(note["value"])}.'
        return f'{name}: barnen ger {", ".join(vals)}. {name} = {fmt(note["value"])}.'
    n, after, a, b, rest = note['cut']
    bound = 'minst' if note['max'] else 'högst'
    return (f'{name}: efter {after} är α = {fmt(a)} och β = {fmt(b)}, alltså α ≥ β. '
            f'{cap(" och ".join(pruned_desc(rest)))} beskärs. {name} blir {bound} {fmt(note["value"])}.')


def subtree_lines(n, notes):
    """Rader i den ordning noderna blir klara (efterordning) inom ett delträd."""
    if 'leaf' in n or n['name'] not in notes:
        return []
    out = []
    for k in n['kids']:
        out += subtree_lines(k, notes)
    out.append(node_line(n['name'], notes[n['name']]))
    return out
