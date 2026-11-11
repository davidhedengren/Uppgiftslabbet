"""SVG- och HTML-hjälp för AI-bankens uppgifter (påfyllnad 2026-11-11).

Följer AI-bankens befintliga figurformat: mörka 1,5 px rutlinjer med
non-scaling-stroke, grön start (#22a05a), rött mål (#d94343), färgförklaring
i varje figur, MAX som uppåtriktad och MIN som nedåtriktad triangel.
"""
import html

GREEN, RED, WALL, INK = '#22a05a', '#d94343', '#334155', '#111827'
TERRAIN = {'3': ('#d6b98c', 'Lera'), '4': ('#c4d7ef', 'Is'), '5': ('#f4ba88', 'Backe')}


def esc(s):
    return html.escape(str(s), quote=True)


def cname(r, c):
    return chr(65 + r) + str(c + 1)


def legend(items, x0, y, size, font, gap):
    """items: [(färg, text)]. Returnerar svg-text och slut-x."""
    out, x = [], x0
    for fill, label in items:
        out.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{fill}" stroke="{WALL}" stroke-width="0.8"/>'
                   f'<text x="{x + size + 7}" y="{y + size - 2}" font-size="{font}" fill="{INK}">{esc(label)}</text>')
        x += size + 7 + int(len(label) * font * 0.62) + gap
    return ''.join(out), x


def maze(rows, start, goal, marks=None, title='', extra_legend=None):
    """rows: strängar med '#' (vägg), '.' (gång) eller siffra (terrängkostnad).
    start/goal: (rad, kolumn). marks: {(r,c): 'P'} markerade rutor."""
    marks = marks or {}
    R, C = len(rows), len(rows[0])
    cs, x0, y0, hy, lx, font = 52, 39, 34, 24, 20, 16
    parts = []
    for c in range(C):
        parts.append(f'<text x="{x0 + c * cs + cs // 2}" y="{hy}" text-anchor="middle" font-size="{font}" fill="{INK}">{c + 1}</text>')
    terr_used = []
    for r in range(R):
        parts.append(f'<text x="{lx}" y="{y0 + r * cs + 32}" text-anchor="middle" font-size="{font}" fill="{INK}">{chr(65 + r)}</text>')
        for c in range(C):
            ch = rows[r][c]
            x, y = x0 + c * cs, y0 + r * cs
            fill = '#fff'
            if ch == '#':
                fill = WALL
            elif ch in TERRAIN:
                fill = TERRAIN[ch][0]
                if ch not in terr_used:
                    terr_used.append(ch)
            if (r, c) == start:
                fill = GREEN
            if (r, c) == goal:
                fill = RED
            parts.append(f'<rect data-cell="{cname(r, c)}" x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{fill}" stroke="{WALL}" stroke-width="1.5" vector-effect="non-scaling-stroke"/>')
            if ch in TERRAIN and (r, c) not in (start, goal):
                parts.append(f'<text x="{x + cs // 2}" y="{y + 33}" text-anchor="middle" font-size="18" font-weight="bold" fill="{INK}">{ch}</text>')
            if (r, c) in marks:
                parts.append(f'<rect x="{x + 7}" y="{y + 7}" width="{cs - 14}" height="{cs - 14}" fill="#fff3b0" stroke="#8a6500" stroke-width="2"/>'
                             f'<text x="{x + cs // 2}" y="{y + 33}" text-anchor="middle" font-size="19" font-weight="bold" fill="{INK}">{esc(marks[(r, c)])}</text>')
    ly = y0 + R * cs + 19
    items = [(GREEN, 'Start'), (RED, 'Mål')]
    items += [(TERRAIN[t][0], f'{TERRAIN[t][1]} ({t})') for t in terr_used]
    items += extra_legend or []
    leg, endx = legend(items, x0, ly, 14, 14, 26)
    parts.append(leg)
    W = max(x0 + C * cs + 6, endx)
    H = ly + 27
    label = f'Labyrint med {R} rader (A–{chr(64 + R)}) och {C} kolumner (1–{C}). Grön ruta är start, röd ruta är mål, mörka rutor är väggar.'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label)}" '
           f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(title or label)}</title>' + ''.join(parts) + '</svg>')
    return f'<div style="overflow-x:auto">{svg}</div>'


def search_tree(nodes, edges, start, goals, title, width):
    """Sökträd med namngivna noder. Start grön, mål röda, färgförklaring under."""
    parts = []
    for a, b in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="2"/>')
    for n, (x, y) in nodes.items():
        fill, txt, stroke = '#fff', INK, WALL
        if n == start:
            fill, txt, stroke = GREEN, '#fff', '#14532d'
        elif n in goals:
            fill, txt, stroke = RED, '#fff', '#7f1d1d'
        parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
                     f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="18" font-weight="bold" fill="{txt}">{esc(n)}</text>')
    ly = max(y for _, y in nodes.values()) + 32
    leg, endx = legend([(GREEN, 'Start'), (RED, 'Mål')], 20, ly, 14, 14, 26)
    parts.append(leg)
    H = ly + 26
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" role="img" aria-label="{esc(title)}" '
           f'style="width:100%;max-width:{width}px;height:auto"><title>{esc(title)}</title>' + ''.join(parts) + '</svg>')
    return svg


def weighted_graph(nodes, edges, start, goal, title, width):
    """Graf med kantvikter. edges: [(a, b, vikt)]."""
    parts = []
    for a, b, w in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="2.5"/>')
    for a, b, w in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        parts.append(f'<rect x="{mx - 13:.0f}" y="{my - 13:.0f}" width="26" height="24" rx="5" fill="#fff" stroke="#94a3b8"/>'
                     f'<text x="{mx:.0f}" y="{my + 5:.0f}" text-anchor="middle" font-size="16" font-weight="bold" fill="{INK}">{w}</text>')
    for n, (x, y) in nodes.items():
        fill, txt, stroke = '#fff', INK, WALL
        if n == start:
            fill, txt, stroke = GREEN, '#fff', '#14532d'
        elif n == goal:
            fill, txt, stroke = RED, '#fff', '#7f1d1d'
        parts.append(f'<circle cx="{x}" cy="{y}" r="20" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
                     f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="18" font-weight="bold" fill="{txt}">{esc(n)}</text>')
    ly = max(y for _, y in nodes.values()) + 36
    leg, _ = legend([(GREEN, 'Start'), (RED, 'Mål')], 20, ly, 14, 14, 26)
    parts.append(leg)
    H = ly + 26
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" role="img" aria-label="{esc(title)}" '
           f'style="width:100%;max-width:{width}px;height:auto"><title>{esc(title)}</title>' + ''.join(parts) + '</svg>')
    return f'<div style="overflow-x:auto">{svg}</div>'


def game_tree(tree, root_max, title, leaf_names=True, spacing=60):
    """tree: {'n': namn, 'k': [barn]} eller ett lövvärde (tal eller text).
    Löv numreras L1, L2, … från vänster om leaf_names."""
    leaves = []

    def count(t):
        if isinstance(t, dict):
            for k in t['k']:
                count(k)
        else:
            leaves.append(t)
    count(tree)
    W = max(420, len(leaves) * spacing + 40)
    pos, parts, lines = {}, [], []
    idx = [0]

    def place(t, depth, mx):
        y = 60 + depth * 88
        if not isinstance(t, dict):
            x = 20 + spacing / 2 + idx[0] * spacing + (W - 40 - len(leaves) * spacing) / 2
            idx[0] += 1
            return (x, y, None)
        xs = [place(k, depth + 1, not mx) for k in t['k']]
        x = sum(p[0] for p in xs) / len(xs)
        for p in xs:
            lines.append((x, y, p[0], p[1]))
        parts.append((t['n'], x, y, mx))
        return (x, y, t['n'])
    place(tree, 0, root_max)
    out = []
    for x1, y1, x2, y2 in lines:
        out.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" stroke="#64748b" stroke-width="1.8"/>')
    for name, x, y, mx in parts:
        if mx:
            pts = f'{x:.1f},{y - 19} {x + 22:.1f},{y + 16} {x - 22:.1f},{y + 16}'
            out.append(f'<polygon points="{pts}" fill="#dbf5f1" stroke="#14857f" stroke-width="2.5"/>')
        else:
            pts = f'{x - 22:.1f},{y - 16} {x + 22:.1f},{y - 16} {x:.1f},{y + 19}'
            out.append(f'<polygon points="{pts}" fill="#fff0d9" stroke="#b86b16" stroke-width="2.5"/>')
        out.append(f'<text x="{x + 27:.1f}" y="{y + 6}" font-size="17" fill="#334155">{esc(name)}</text>')
    # löv
    idx[0] = 0
    leaf_pos = []

    def leafpos(t, depth):
        y = 60 + depth * 88
        if not isinstance(t, dict):
            x = 20 + spacing / 2 + idx[0] * spacing + (W - 40 - len(leaves) * spacing) / 2
            idx[0] += 1
            leaf_pos.append((x, y, t))
            return
        for k in t['k']:
            leafpos(k, depth + 1)
    leafpos(tree, 0)
    maxy = 0
    for i, (x, y, v) in enumerate(leaf_pos, 1):
        style = ' font-style="italic"' if isinstance(v, str) else ''
        val = esc(str(v).replace('-', '−'))
        out.append(f'<rect x="{x - 18:.1f}" y="{y - 16}" width="36" height="32" rx="3" fill="#fff" stroke="#64748b"/>'
                   f'<text x="{x:.1f}" y="{y + 7}" text-anchor="middle" font-size="18" fill="{INK}"{style}>{val}</text>')
        if leaf_names:
            out.append(f'<text x="{x:.1f}" y="{y + 34}" text-anchor="middle" font-size="12" fill="#475569">L{i}</text>')
        maxy = max(maxy, y)
    out.append('<polygon points="20,7 29,23 11,23" fill="#dbf5f1" stroke="#14857f"/><text x="38" y="22" font-size="14" fill="#334155">MAX</text>'
               '<polygon points="110,7 128,7 119,23" fill="#fff0d9" stroke="#b86b16"/><text x="137" y="22" font-size="14" fill="#334155">MIN</text>')
    H = maxy + (44 if leaf_names else 28)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H}" role="img" aria-label="Spelträd. Uppåtriktad triangel är MAX, nedåtriktad är MIN." '
           f'style="width:100%;max-width:{W:.0f}px;min-width:{min(W, 420):.0f}px;height:auto"><title>{esc(title)}</title>' + ''.join(out) + '</svg>')
    return f'<div style="overflow-x:auto">{svg}</div>'


def box_queue(items, title):
    """FIFO-kö som rad av rutor: först i kön till vänster."""
    n = len(items)
    bw, x0, y0 = 54, 110, 40
    W = x0 + n * bw + 120
    out = []
    for i, it in enumerate(items):
        x = x0 + i * bw
        out.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="50" fill="#fff" stroke="{WALL}" stroke-width="2"/>'
                   f'<text x="{x + bw // 2}" y="{y0 + 33}" text-anchor="middle" font-size="22" font-weight="bold" fill="{INK}">{esc(it)}</text>')
    xr = x0 + n * bw
    out.append(f'<line x1="{x0 - 12}" y1="{y0 + 25}" x2="{x0 - 70}" y2="{y0 + 25}" stroke="{INK}" stroke-width="2.5"/>'
               f'<polygon points="{x0 - 80},{y0 + 25} {x0 - 66},{y0 + 18} {x0 - 66},{y0 + 32}" fill="{INK}"/>'
               f'<text x="{x0 - 45}" y="{y0 + 76}" text-anchor="middle" font-size="14" fill="{INK}">tas ut</text>'
               f'<line x1="{xr + 80}" y1="{y0 + 25}" x2="{xr + 22}" y2="{y0 + 25}" stroke="{INK}" stroke-width="2.5"/>'
               f'<polygon points="{xr + 12},{y0 + 25} {xr + 26},{y0 + 18} {xr + 26},{y0 + 32}" fill="{INK}"/>'
               f'<text x="{xr + 50}" y="{y0 + 76}" text-anchor="middle" font-size="14" fill="{INK}">läggs in</text>'
               f'<text x="{x0}" y="{y0 - 12}" font-size="14" fill="{INK}">först i kön</text>'
               f'<text x="{xr}" y="{y0 - 12}" text-anchor="end" font-size="14" fill="{INK}">sist i kön</text>')
    H = y0 + 90
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}" '
            f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(title)}</title>' + ''.join(out) + '</svg>')


def box_stack(items_bottom_up, title):
    """Stack som stapel av rutor, översta noden överst."""
    n = len(items_bottom_up)
    bh, x0, y0, bw = 46, 60, 34, 70
    out = []
    for i, it in enumerate(reversed(items_bottom_up)):
        y = y0 + i * bh
        out.append(f'<rect x="{x0}" y="{y}" width="{bw}" height="{bh}" fill="#fff" stroke="{WALL}" stroke-width="2"/>'
                   f'<text x="{x0 + bw // 2}" y="{y + 31}" text-anchor="middle" font-size="22" font-weight="bold" fill="{INK}">{esc(it)}</text>')
    yb = y0 + n * bh
    out.append(f'<path d="M{x0 - 8},{y0 - 6} V{yb + 4} H{x0 + bw + 8} V{y0 - 6}" fill="none" stroke="{INK}" stroke-width="2.5"/>'
               f'<line x1="{x0 + bw + 70}" y1="{y0 + 23}" x2="{x0 + bw + 16}" y2="{y0 + 23}" stroke="{INK}" stroke-width="2"/>'
               f'<polygon points="{x0 + bw + 8},{y0 + 23} {x0 + bw + 20},{y0 + 17} {x0 + bw + 20},{y0 + 29}" fill="{INK}"/>'
               f'<text x="{x0 + bw + 76}" y="{y0 + 20}" font-size="14" fill="{INK}">överst: läggs in</text>'
               f'<text x="{x0 + bw + 76}" y="{y0 + 38}" font-size="14" fill="{INK}">och tas ut här</text>'
               f'<text x="{x0 + bw + 20}" y="{yb - 14}" font-size="14" fill="{INK}">nederst</text>')
    W, H = x0 + bw + 200, yb + 20
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}" '
            f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(title)}</title>' + ''.join(out) + '</svg>')


# ---------- HTML ----------

def tab(head, rows):
    """Tabell i bankens stil (class="data"), vänsterställd så att köer läses naturligt."""
    st = ' style="text-align:left"'
    h = ''.join(f'<th{st}>{x}</th>' for x in head)
    b = ''.join('<tr>' + ''.join(f'<td{st}>{x}</td>' for x in r) + '</tr>' for r in rows)
    return f'<table class="data"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def step(rubrik, *body):
    inner = ''.join(b if b.startswith('<') else f'<p>{b}</p>' for b in body)
    return f'<li><p class="facit-rubrik">{rubrik}</p>{inner}</li>'


def facit(steps, svar, alts=None):
    s = '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steps) + '</ol>'
    s += f'<p class="facit-svar"><strong>Svar:</strong> {svar}</p>'
    if alts:
        s += '<ul>' + ''.join(f'<li><strong>{chr(65 + i)}:</strong> {a["kommentar"]}</li>' for i, a in enumerate(alts)) + '</ul>'
    return s + '</div>'
