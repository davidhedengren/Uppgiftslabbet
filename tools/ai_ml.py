"""Hjälp för AI-bankens kapitel 4 Maskininlärning (2026-11-12).

Figurer (punktdiagram, neuron, nätverk), klassificeringsmatriser och delar i Kunskapsgymmets
format. Bygger på samma delformat som bygg-ai-kunskapsgymmet-2026-11-11.py.
"""
import importlib.util
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _load(name, fil):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fil))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = _load('ai_kg', 'bygg-ai-kunskapsgymmet-2026-11-11.py')
P7 = _load('ai_p7', 'bygg-ai-pafyllnad7-2026-11-11.py')
TI = _load('ai_ti', 'bygg-ai-tillampningar-2026-11-12.py')
from ai_figurer import step, tab, esc  # noqa: E402,F401

B = K.B
p, alt = K.p, K.alt
DEC = 'Svara i decimalform.'
INK = '#111827'


# ---------------------------------------------------------------- tal

def f(x):
    """Tal med decimalkomma och typografiskt minustecken, högst tre decimaler."""
    x = float(x)
    if x == int(x):
        s = str(int(x))
    else:
        s = f'{x:.3f}'.rstrip('0').rstrip('.')
    return s.replace('.', ',').replace('-', '−')


def exakt(fr):
    """Ett bråk (eller heltal) som går att skriva exakt med högst tre decimaler."""
    if isinstance(fr, float):
        assert round(fr, 3) == fr, fr
        return fr
    fr = Fr(fr)
    v = round(float(fr), 3)
    assert Fr(str(v)) == fr, fr
    return v


# ---------------------------------------------------------------- delar

def num(fraga, steps, svar, ledtrad, tn):
    assert isinstance(svar, int), svar
    return K.num(fraga, steps, svar, ledtrad, tn)


def dec(fraga, steps, svar, ledtrad, tn, tol=0):
    """Numerisk del vars svar kan vara ett decimaltal. Instruktionen visas bara i Kunskapsgymmet."""
    svar = svar if tol else exakt(svar)
    d = B.part(p(fraga), steps, f'{f(svar)}.', ledtrad, tn)
    d.update({'svarstyp': 'numeriskt', 'rättSvar': int(svar) if svar == int(svar) else svar, 'tolerans': tol,
              'självrättning': True, 'svarFormat': 'numeriskt', 'svarEnhet': None, 'spel': True,
              '_suf': DEC if svar != int(svar) else None})
    return d


def fv(fraga, rubrik, text, alts, ledtrad, tn, oppen=False):
    """Flerval. oppen=True: förklaringsfråga som är öppen på papper (alternativen bara i Kunskapsgymmet)."""
    for t, _, k in alts:
        assert len(k) > 15, (fraga, t)
    d = K.val(fraga, [step(rubrik, text)], [alt(t, r, k) for t, r, k in alts], ledtrad, tn)
    d['_oppen'] = oppen
    return d


def namn(fraga, steps, svar, ledtrad, tn, suf='Skriv punkternas namn, åtskilda med kommatecken.'):
    d = P7.lst(fraga, steps, svar, ledtrad, tn, suf)
    d['svarFormat'] = 'namnmangd'
    return d


def falt(fraga, steps, svar_txt, ledtrad, tn, etiketter, varden):
    return TI.falt(fraga, steps, svar_txt, ledtrad, tn, etiketter, varden)


def uppgift(id_, omr, familj, intro, parts, ledtrad, formaga):
    oppna = [chr(97 + i) for i, d in enumerate(parts) if d.pop('_oppen', False)]
    u = P7.uppgift(id_, omr, familj, intro, parts, ledtrad, formaga)
    return TI.oppen_pa_papper(u, oppna) if oppna else u


# ---------------------------------------------------------------- klassificeringsmatris

def matris(pos, neg, tp, fn, fp, tn):
    return tab(['', f'Förutsagt: {pos}', f'Förutsagt: {neg}'],
               [[f'<strong>Verkligt: {pos}</strong>', str(tp), str(fn)], [f'<strong>Verkligt: {neg}</strong>', str(fp), str(tn)]])


def matris_n(klasser, rader):
    """Större matris: korta rubriker så att tabellen ryms i mobilbredd."""
    return tab(['Verklig ↓<br>Förutsagd →'] + [f'<strong>{k}</strong>' for k in klasser],
               [[f'<strong>{k}</strong>'] + [str(v) for v in r] for k, r in zip(klasser, rader)])


# ---------------------------------------------------------------- figurer

FORM = {'A': ('#2563eb', 'circle'), 'B': ('#ea580c', 'square'), 'C': ('#16a34a', 'tri'), '?': ('#111827', 'ring')}
LINJEFARG = ['#7c3aed', '#0f766e']


def diagram(punkter, titel, xmax, ymax, xlabel, ylabel, linjer=(), centra=(), steg=1, ystep=None, legend=None, W=360, H=300):
    """punkter: (x, y, klass, etikett). linjer: [(k, m, namn)]. centra: [(x, y, namn)]."""
    ystep = ystep or steg
    ml, mb, mt, mr = 40, 46, 26, 16
    sx = (W - ml - mr) / xmax
    sy = (H - mb - mt) / ymax

    def X(x):
        return ml + x * sx

    def Y(y):
        return H - mb - y * sy
    o = []
    for i in range(0, xmax + 1, steg):
        o.append(f'<line x1="{X(i):.1f}" y1="{Y(0):.1f}" x2="{X(i):.1f}" y2="{Y(ymax):.1f}" stroke="#e5e7eb"/>'
                 f'<text x="{X(i):.1f}" y="{Y(0) + 17:.1f}" text-anchor="middle" font-size="13" fill="#374151">{i}</text>')
    for j in range(0, ymax + 1, ystep):
        o.append(f'<line x1="{X(0):.1f}" y1="{Y(j):.1f}" x2="{X(xmax):.1f}" y2="{Y(j):.1f}" stroke="#e5e7eb"/>'
                 f'<text x="{X(0) - 7:.1f}" y="{Y(j) + 4:.1f}" text-anchor="end" font-size="13" fill="#374151">{j}</text>')
    o.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(xmax):.1f}" y2="{Y(0):.1f}" stroke="#374151" stroke-width="1.5"/>'
             f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(0):.1f}" y2="{Y(ymax):.1f}" stroke="#374151" stroke-width="1.5"/>'
             f'<text x="{X(xmax):.1f}" y="{H - 6}" text-anchor="end" font-size="13" fill="{INK}">{esc(xlabel)}</text>'
             f'<text x="{X(0) - 30:.1f}" y="14" font-size="13" fill="{INK}">{esc(ylabel)}</text>')
    for n, (k, m, namn_) in enumerate(linjer):
        k, m = float(k), float(m)
        x1 = xmax if m + k * xmax <= ymax else (ymax - m) / k
        x0 = 0 if m >= 0 else -m / k
        col = LINJEFARG[n % 2]
        o.append(f'<line x1="{X(x0):.1f}" y1="{Y(m + k * x0):.1f}" x2="{X(x1):.1f}" y2="{Y(m + k * x1):.1f}" stroke="{col}" stroke-width="2.5"/>')
        if namn_:
            o.append(f'<text x="{X(x1) - 4:.1f}" y="{Y(m + k * x1) + (16 if n else -6):.1f}" text-anchor="end" font-size="13" font-weight="bold" fill="{col}">{esc(namn_)}</text>')
    for x, y, kl, et in punkter:
        col, form = FORM[kl]
        cx, cy = X(x), Y(y)
        if form == 'circle':
            o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{col}"/>')
        elif form == 'square':
            o.append(f'<rect x="{cx - 6:.1f}" y="{cy - 6:.1f}" width="12" height="12" fill="{col}"/>')
        elif form == 'tri':
            o.append(f'<polygon points="{cx:.1f},{cy - 7:.1f} {cx + 7:.1f},{cy + 6:.1f} {cx - 7:.1f},{cy + 6:.1f}" fill="{col}"/>')
        else:
            o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="#fff" stroke="{col}" stroke-width="3"/>')
        if et:
            o.append(f'<text x="{cx + 8:.1f}" y="{cy - 8:.1f}" font-size="13" font-weight="bold" fill="{INK}">{esc(et)}</text>')
    for x, y, namn_, *plac in centra:
        cx, cy = X(x), Y(y)
        tx, ty, anc = {'uv': (cx - 10, cy - 9, 'end'), 'nh': (cx + 10, cy + 19, 'start')}[plac[0] if plac else 'uv']
        o.append(f'<path d="M{cx - 7:.1f},{cy - 7:.1f} L{cx + 7:.1f},{cy + 7:.1f} M{cx + 7:.1f},{cy - 7:.1f} L{cx - 7:.1f},{cy + 7:.1f}" '
                 f'stroke="{INK}" stroke-width="3"/><text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anc}" font-size="13" '
                 f'font-weight="bold" fill="{INK}">{esc(namn_)}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(titel)}" '
           f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(titel)}</title>' + ''.join(o) + '</svg>')
    return svg + (p(legend) if legend else '')


SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def neuron_svg(x, w, b, titel, akt='steg'):
    """En neuron: indata x (tal eller None), vikter w, bias b och aktiveringsfunktion."""
    n = len(x)
    H = 80 * n + 10
    yn = 45 + 80 * (n - 1) / 2
    o = []
    for i, (xi, wi) in enumerate(zip(x, w)):
        y = 45 + i * 80
        lab = f'x{i + 1}'.translate(SUB) + (f' = {f(xi)}' if xi is not None else '')
        ly = y + (yn - y) * (120 - 90) / (200 - 90)  # linjens höjd vid textens vänstra kant (x = 120)
        ty = ly - 6 if y < yn else ly - 8 if y == yn else ly + 17
        o.append(f'<rect x="6" y="{y - 18}" width="84" height="36" rx="18" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
                 f'<text x="48" y="{y + 6}" text-anchor="middle" font-size="15" font-weight="bold" fill="{INK}">{lab}</text>'
                 f'<line x1="90" y1="{y}" x2="200" y2="{yn}" stroke="#64748b" stroke-width="2"/>'
                 f'<text x="150" y="{ty:.0f}" text-anchor="middle" font-size="14" font-weight="bold" fill="#7c3aed">'
                 f'{"w" + str(i + 1).translate(SUB)} = {f(wi)}</text>')
    bt = esc(b) if isinstance(b, str) else f(b)
    o.append(f'<circle cx="230" cy="{yn}" r="30" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>'
             f'<text x="230" y="{yn + 8}" text-anchor="middle" font-size="24" fill="{INK}">Σ</text>'
             f'<text x="230" y="{yn - 38}" text-anchor="middle" font-size="14" fill="{INK}">b = {bt}</text>')
    if akt is None:  # bara viktad summa och bias: pilen slutar i z
        o.append(f'<line x1="260" y1="{yn}" x2="300" y2="{yn}" stroke="#64748b" stroke-width="2"/>'
                 f'<text x="306" y="{yn + 5}" font-size="15" font-weight="bold" fill="{INK}">z</text>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 {H}" role="img" aria-label="{esc(titel)}" '
                f'style="width:100%;max-width:340px;height:auto"><title>{esc(titel)}</title>' + ''.join(o) + '</svg>')
    o.append(
             f'<line x1="260" y1="{yn}" x2="290" y2="{yn}" stroke="#64748b" stroke-width="2"/>'
             f'<rect x="290" y="{yn - 20}" width="62" height="40" rx="6" fill="#fff" stroke="#334155" stroke-width="2"/>'
             f'<text x="321" y="{yn + 5}" text-anchor="middle" font-size="14" fill="{INK}">{esc(akt)}</text>'
             f'<line x1="352" y1="{yn}" x2="380" y2="{yn}" stroke="#64748b" stroke-width="2"/>'
             f'<text x="384" y="{yn + 5}" font-size="14" fill="{INK}">ut</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 410 {H}" role="img" aria-label="{esc(titel)}" '
            f'style="width:100%;max-width:410px;height:auto"><title>{esc(titel)}</title>' + ''.join(o) + '</svg>')


def natverk_svg(lager, titel, namn_=None, noder=None):
    """Helt kopplat nätverk. lager: antal neuroner per lager. namn_: rubrik per lager. noder: namn i varje nod."""
    namn_ = namn_ or (['Indata'] + ['Dolt lager'] * (len(lager) - 2) + ['Utdata'])
    W = 120 * len(lager) + 40
    H = 60 + 56 * max(lager)
    xs = [60 + 120 * i for i in range(len(lager))]

    def ys(n):
        top = 50 + (max(lager) - n) * 28
        return [top + 56 * j + 14 for j in range(n)]
    o = []
    for i in range(len(lager) - 1):
        for y1 in ys(lager[i]):
            for y2 in ys(lager[i + 1]):
                o.append(f'<line x1="{xs[i]}" y1="{y1}" x2="{xs[i + 1]}" y2="{y2}" stroke="#94a3b8" stroke-width="1.2"/>')
    farg = ['#dbeafe'] + ['#fef3c7'] * (len(lager) - 2) + ['#dcfce7']
    for i, n in enumerate(lager):
        o.append(f'<text x="{xs[i]}" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="{INK}">{esc(namn_[i])}</text>')
        for j, y in enumerate(ys(n)):
            o.append(f'<circle cx="{xs[i]}" cy="{y}" r="16" fill="{farg[i]}" stroke="#334155" stroke-width="1.8"/>')
            if noder:
                o.append(f'<text x="{xs[i]}" y="{y + 5}" text-anchor="middle" font-size="14" font-weight="bold" fill="{INK}">{esc(noder[i][j])}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(titel)}" '
            f'style="width:100%;max-width:{W}px;height:auto"><title>{esc(titel)}</title>' + ''.join(o) + '</svg>')


def d2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
