"""Kopplade klossar med snören och trissor: modell, lösning och figurer (2026-11-20).

Används av häftet ”Färdighetsträning – Newtons andra lag” (tools/bygg-hafte-newton2-2026-11-20.py) och av
bankuppgifterna i Fy1 newton2 (tools/bygg-fy1-kopplade-klossar-2026-11-20.py).

Ett system är en enda snörkedja. Kropparna ordnas längs snöret från vänster till höger:
vänster hängande kroppar (nerifrån och upp), kroppar på bordet eller golvet (vänster till höger) och höger hängande
kroppar (uppifrån och ned). Positiv riktning är längs kedjan åt höger: vänster hängande kropp uppåt, kropp på bordet
åt höger och höger hängande kropp nedåt. En dragkraft F kan verka åt höger i kedjans högra ände.

Alla samband är linjära i F, m·g och friktionskrafterna, så både algebraiska och numeriska svar räknas exakt med
bråk (fractions.Fraction) utan symbolpaket.
"""
from dataclasses import dataclass, field
from fractions import Fraction as Fr

G = 9.82


# ================================================================ modell
@dataclass
class Kropp:
    k: float            # massa: k·m (häftet) eller k kg (banken)
    plats: str          # 'V' vänster hängande, 'B' bord/golv, 'H' höger hängande
    friktion: float = 0.0
    fnamn: str = ''     # symbol för friktionen i algebraiska svar, t.ex. 'f' eller 'f_1'
    etikett: str = ''   # text i figuren


@dataclass
class System:
    vanster: list = field(default_factory=list)   # uppifrån och ned
    bord: list = field(default_factory=list)      # vänster till höger
    hoger: list = field(default_factory=list)     # uppifrån och ned
    F: float = 0.0                                 # dragkraft åt höger i högra änden (bara utan höger hängande)
    golv: bool = False                             # klossarna ligger på golvet, ingen trissa
    tomtbord: bool = False                         # snöret går över ett bord med en trissa i varje hörn

    def kedja(self):
        return list(reversed(self.vanster)) + self.bord + self.hoger

    def driv(self, kroppar, g=G, F=None):
        """Drivande kraft längs kedjan (utan friktion) för en delmängd av kropparna."""
        d = sum((b.k * g if b.plats == 'H' else -b.k * g if b.plats == 'V' else 0.0) for b in kroppar)
        return d

    def los(self, g=G, m=1.0, F=None):
        """Numerisk lösning: a (längs kedjan) och snörkrafterna i kedjans ordning.

        Massorna är k·m. Friktionen motverkar rörelsen; rörelseriktningen är den som den drivande kraften ger.
        """
        F = self.F if F is None else F
        kedja = self.kedja()
        M = sum(b.k for b in kedja) * m
        driv = sum((b.k * m * g if b.plats == 'H' else -b.k * m * g if b.plats == 'V' else 0.0) for b in kedja) + F
        fr = sum(b.friktion for b in kedja)
        tecken = 1 if driv > 0 else -1
        assert abs(driv) > fr, 'systemet står still: friktionen räcker'
        a = (driv - tecken * fr) / M
        S = []
        for i in range(len(kedja) - 1):
            del_ = kedja[:i + 1]
            md = sum(b.k for b in del_) * m
            dd = sum((b.k * m * g if b.plats == 'H' else -b.k * m * g if b.plats == 'V' else 0.0) for b in del_)
            fd = sum(b.friktion for b in del_)
            # Summan av krafterna på delsystemet längs kedjan: S + dd - tecken*fd = md*a
            S.append(md * a - dd + tecken * fd)
        return a, S

    def symbolisk(self):
        """Algebraiska uttryck: a och snörkrafterna som linjära kombinationer av F, mg och friktionerna.

        Returnerar (a_taljare, n, [S]) där a = a_taljare/(n·m) och varje S är en dict {symbol: Fraction}.
        Symbolen 'mg' betyder m·g. Förutsätter att rörelsen sker åt det håll de drivande krafterna anger.
        """
        kedja = self.kedja()
        n = sum(Fr(b.k).limit_denominator(1000) for b in kedja)
        a, _ = self.los()
        tecken = 1 if a > 0 else -1

        def lin(kroppar, medF):
            d = {}
            if medF and self.F:
                d['F'] = Fr(1)
            for b in kroppar:
                kk = Fr(b.k).limit_denominator(1000)
                if b.plats == 'H':
                    d['mg'] = d.get('mg', 0) + kk
                elif b.plats == 'V':
                    d['mg'] = d.get('mg', 0) - kk
                if b.friktion:
                    d[b.fnamn] = d.get(b.fnamn, 0) - tecken
            return {s: c for s, c in d.items() if c}

        tal = lin(kedja, True)
        S = []
        for i in range(len(kedja) - 1):
            del_ = kedja[:i + 1]
            md = sum(Fr(b.k).limit_denominator(1000) for b in del_)
            uttr = {s: c * md / n for s, c in tal.items()}
            for s, c in lin(del_, False).items():
                uttr[s] = uttr.get(s, 0) - c
            S.append({s: c for s, c in uttr.items() if c})
        return tal, n, S


# ================================================================ LaTeX för algebraiska uttryck
def _koef(c, sym):
    """Term c·sym i LaTeX, utan tecken: F, 2mg, \\frac{mg}{3}, \\frac{4mg}{3}."""
    c = abs(c)
    s = sym
    if c == 1:
        return s
    if c.denominator == 1:
        return f'{c.numerator}{s}'
    return f'\\frac{{{"" if c.numerator == 1 else c.numerator}{s}}}{{{c.denominator}}}'


def latex_lin(d):
    ordning = sorted(d, key=lambda s: {'F': 0, 'mg': 1}.get(s, 2))
    ut = ''
    for i, s in enumerate(ordning):
        c = d[s]
        term = _koef(c, s)
        ut += ('-' if c < 0 else ('' if i == 0 else '+')) + term
    return ut or '0'


def latex_a(tal, n):
    """a = tal/(n m). Rena mg-termer förenklas till g, rena F-termer till F/(n m)."""
    if set(tal) == {'mg'}:
        c = tal['mg'] / n
        return ('-' if c < 0 else '') + _koef(c, 'g')
    if set(tal) == {'F'}:
        c = tal['F'] / n
        return '\\frac{F}{m}' if c == 1 else f'\\frac{{{"" if c.numerator == 1 else c.numerator}F}}{{{c.denominator}m}}'
    nn = '' if n == 1 else str(n)
    return f'\\frac{{{latex_lin(tal)}}}{{{nn}m}}'


def _koefg(c):
    return c


# ================================================================ SVG
INK = '#1f2d3a'
REP = '#3d4752'
FARGER = [  # (ljus, mörk, kant) per kloss
    ('#e3eefb', '#a9c7ec', '#3d6fa8'),
    ('#fdebd6', '#f2bf86', '#b26a1f'),
    ('#e2f3e5', '#a5d6ae', '#2f7d45'),
    ('#ece4f7', '#c3aee6', '#6a48a3'),
    ('#fbe3e1', '#eba9a2', '#a8443a'),
]
RED = '#c0392b'
FONT = 'font-family="Arial,Helvetica,sans-serif"'


def _f(x):
    return f'{x:.1f}'.rstrip('0').rstrip('.')


class Rit:
    """Samlar SVG-element och defs för en figur med unikt id-prefix."""

    def __init__(self, pid):
        self.p = pid
        self.defs = []
        self.bak = []
        self.el = []
        self.fram = []
        self._grad = {}
        self.defs.append(
            f'<filter id="{pid}s" x="-30%" y="-30%" width="160%" height="170%">'
            f'<feDropShadow dx="1.5" dy="2.5" stdDeviation="1.8" flood-color="#1f2d3a" flood-opacity="0.28"/></filter>')
        self.defs.append(
            f'<linearGradient id="{pid}tra" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2bf92"/>'
            f'<stop offset="1" stop-color="#b98653"/></linearGradient>')
        self.defs.append(
            f'<radialGradient id="{pid}met" cx="0.38" cy="0.35" r="0.75"><stop offset="0" stop-color="#ffffff"/>'
            f'<stop offset="0.55" stop-color="#cfd6de"/><stop offset="1" stop-color="#8b97a4"/></radialGradient>')
        self.defs.append(
            f'<pattern id="{pid}str" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<line x1="0" y1="0" x2="0" y2="8" stroke="#8a96a3" stroke-width="1.4"/></pattern>')
        self.defs.append(
            f'<pattern id="{pid}fr" width="6" height="6" patternUnits="userSpaceOnUse">'
            f'<rect width="6" height="6" fill="#6b4a2a" opacity="0.18"/><path d="M0 6 L3 1 L6 6" fill="none" '
            f'stroke="#5a3b1e" stroke-width="1.1"/></pattern>')

    def grad(self, i):
        i %= len(FARGER)
        if i not in self._grad:
            lj, mo, _ = FARGER[i]
            gid = f'{self.p}g{i}'
            self.defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0.35" y2="1"><stop offset="0" stop-color="{lj}"/>'
                             f'<stop offset="1" stop-color="{mo}"/></linearGradient>')
            self._grad[i] = gid
        return self._grad[i]

    def text(self, x, y, s, size=14, anchor='middle', fill=INK, bold=False, italic=False, halo=False, lager=None):
        extra = (' font-weight="bold"' if bold else '') + (' font-style="italic"' if italic else '')
        if halo:
            extra += ' stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round"'
        (lager if lager is not None else self.fram).append(
            f'<text x="{_f(x)}" y="{_f(y)}" fill="{fill}" {FONT} font-size="{size}" text-anchor="{anchor}"{extra}>{s}</text>')

    def linje(self, x1, y1, x2, y2, color=REP, w=1.8, lager=None, cap='round'):
        (lager if lager is not None else self.el).append(
            f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="{cap}"/>')

    def kloss(self, x, y, w, h, i, etikett):
        _, _, kant = FARGER[i % len(FARGER)]
        self.el.append(f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" rx="4" fill="url(#{self.grad(i)})" '
                       f'stroke="{kant}" stroke-width="1.6" filter="url(#{self.p}s)"/>')
        self.el.append(f'<rect x="{_f(x + 3)}" y="{_f(y + 3)}" width="{_f(w - 6)}" height="3" rx="1.5" fill="#fff" opacity="0.55"/>')
        self.el.append(f'<text x="{_f(x + w / 2)}" y="{_f(y + h / 2 + 5)}" fill="{INK}" {FONT} font-size="15" '
                       f'text-anchor="middle" font-weight="bold">{etikett}</text>')

    def trissa(self, cx, cy, r, fastx, fasty):
        """Trissa med axel och fäste till punkten (fastx, fasty)."""
        self.bak.append(f'<line x1="{_f(fastx)}" y1="{_f(fasty)}" x2="{_f(cx)}" y2="{_f(cy)}" stroke="#5b6672" '
                        f'stroke-width="4" stroke-linecap="round"/>')
        self.fram.append(f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="url(#{self.p}met)" stroke="#4d5865" '
                         f'stroke-width="1.6" filter="url(#{self.p}s)"/>')
        self.fram.append(f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r * 0.62)}" fill="none" stroke="#7d8894" stroke-width="1"/>')
        self.fram.append(f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="2.6" fill="#38424d"/>')

    def pil(self, x1, y1, x2, y2, color=RED, w=3.2, head=11):
        import math
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        bx, by = x2 - ux * head, y2 - uy * head
        px, py = -uy * head * 0.5, ux * head * 0.5
        self.fram.append(f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(bx)}" y2="{_f(by)}" stroke="{color}" stroke-width="{w}" '
                         f'stroke-linecap="round"/>')
        self.fram.append(f'<polygon points="{_f(x2)},{_f(y2)} {_f(bx + px)},{_f(by + py)} {_f(bx - px)},{_f(by - py)}" '
                         f'fill="{color}"/>')

    def svg(self, w, h, titel, bredd=None):
        bredd = bredd or w
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {_f(w)} {_f(h)}" width="{_f(bredd)}" '
                f'role="img" aria-label="{titel}" style="max-width:100%;height:auto"><title>{titel}</title>'
                f'<defs>{"".join(self.defs)}</defs><rect width="{_f(w)}" height="{_f(h)}" fill="#fff"/>'
                + ''.join(self.bak) + ''.join(self.el) + ''.join(self.fram) + '</svg>')


def _textbredd(b):
    import re
    return 8.6 * len(re.sub(r'<[^>]+>', '', b.etikett)) + 14


def _bredd(b):
    return max(46 + 9 * min(b.k, 5), _textbredd(b))


def _hang_dim(b):
    return max(38 + 5 * min(b.k, 5), _textbredd(b)), 34 + 4 * min(b.k, 5)


def figur(sys_, pid, titel, snorlappar=True, Ftext='F', skala=1.0, friktionsyta=True):
    """Rita systemet. Snörena märks S₁, S₂, … i kedjans ordning när det finns fler än ett snöre."""
    R = Rit(pid)
    kedja = sys_.kedja()
    nsnoren = len(kedja) - 1 + (0 if not sys_.F else 0)
    lappar = snorlappar and nsnoren >= 2
    nr = iter(range(1, 20))
    SUB = '₀₁₂₃₄₅₆₇₈₉'
    lapp = lambda: 'S' + SUB[next(nr)]
    lappar_ut = []

    def snorlapp(x, y, anchor='middle'):
        if lappar:
            R.text(x, y, lapp(), 13, anchor, '#5a3e8c', bold=True, italic=True, halo=True)
        else:
            next(nr)

    if not sys_.bord and sys_.vanster and sys_.hoger and not sys_.tomtbord:
        # ---------------- Atwood: en trissa i taket
        assert len(sys_.vanster) == 1, 'snörlapparna förutsätter en kropp till vänster'
        cx, cy, r = 150, 66, 36
        R.bak.append(f'<rect x="70" y="10" width="160" height="12" fill="url(#{pid}str)" stroke="#5b6672" stroke-width="1.4"/>')
        R.trissa(cx, cy, r, cx, 22)
        ymax = 0
        for sida, lista in ((-1, sys_.vanster), (1, sys_.hoger)):
            x = cx + sida * r
            y = cy
            for j, b in enumerate(lista):
                w, h = _hang_dim(b)
                topp = y + ((52 if sida < 0 else 84) if j == 0 else 26)
                R.linje(x, y, x, topp)
                if j == 0 and sida == -1:
                    snorlapp(x - 8, (y + topp) / 2 + 4, 'end')
                elif j > 0:
                    snorlapp(x + sida * 8, (y + topp) / 2 + 4, 'start' if sida > 0 else 'end')
                R.kloss(x - w / 2, topp, w, h, kedja.index(b), b.etikett)
                y = topp + h
            ymax = max(ymax, y)
        W, H = 300, ymax + 18
        return R.svg(W, H, titel, W * skala)

    if sys_.golv:
        # ---------------- klossar på golvet, dragkraft åt höger
        gy = 58
        x = 24
        for i, b in enumerate(sys_.bord):
            w, h = _bredd(b), 40
            if i > 0:
                R.linje(x - 28, gy - h / 2, x, gy - h / 2)
                snorlapp(x - 14, gy - h / 2 - 7)
            if b.friktion and friktionsyta:
                R.fram.append(f'<rect x="{_f(x - 6)}" y="{gy - 1}" width="{_f(w + 12)}" height="6" fill="url(#{pid}fr)"/>')
            R.kloss(x, gy - h, w, h, i, b.etikett)
            x += w + 28
        x -= 28
        if sys_.F:
            R.linje(x, gy - 20, x + 12, gy - 20)
            R.pil(x + 12, gy - 20, x + 92, gy - 20)
            R.text(x + 96, gy - 14, Ftext, 15, 'start', RED, bold=True, italic=True)
        W = x + 96 + 12 + 8 * len(Ftext)
        R.bak.append(f'<rect x="10" y="{gy}" width="{_f(W - 20)}" height="12" fill="url(#{pid}str)"/>')
        R.bak.append(f'<line x1="10" y1="{gy}" x2="{_f(W - 10)}" y2="{gy}" stroke="#4d5865" stroke-width="2.4"/>')
        return R.svg(W, gy + 22, titel, W * skala)

    # ---------------- bord med trissa i ena eller båda hörnen
    ty = 56             # bordsskivans överkant
    tjock = 14
    h_kloss = 40
    yr = ty - (h_kloss / 2 if sys_.bord else 12)   # snörets höjd vid klossarna
    rr = 12
    vansterplats = 64 if sys_.vanster else 20
    TL = vansterplats
    x = TL + 28
    pos = []
    for i, b in enumerate(sys_.bord):
        w = _bredd(b)
        pos.append((x, w))
        x += w + 34
    TR = x - 34 + (70 if sys_.hoger else 30)
    if not sys_.bord:
        TR = TL + 190
    # bordsskiva och ben
    benh = 120
    golv = ty + benh
    R.bak.append(f'<rect x="{_f(TL)}" y="{ty}" width="{_f(TR - TL)}" height="{tjock}" rx="3" fill="url(#{pid}tra)" '
                 f'stroke="#8a5d33" stroke-width="1.2" filter="url(#{pid}s)"/>')
    for bx in (TL + 26, TR - 34):
        R.bak.append(f'<rect x="{_f(bx)}" y="{ty + tjock}" width="10" height="{benh - tjock}" fill="url(#{pid}tra)" '
                     f'stroke="#8a5d33" stroke-width="1"/>')
    # klossar på bordet och snören mellan dem
    for i, ((x, w), b) in enumerate(zip(pos, sys_.bord)):
        if b.friktion and friktionsyta:
            R.fram.append(f'<rect x="{_f(x - 6)}" y="{ty}" width="{_f(w + 12)}" height="6" fill="url(#{pid}fr)"/>')
        R.kloss(x, ty - h_kloss, w, h_kloss, len(sys_.vanster) + i, b.etikett)
    # vänster sida (snöret från första bordsklossen över vänster trissa)
    ymax = golv
    if sys_.vanster:
        cx, cy = TL - 10, yr + rr
        R.trissa(cx, cy, rr, TL + 2, ty + 3)
        R.linje(pos[0][0] if pos else TR + 10, yr, cx, yr)
        xh = cx - rr
        y = cy
        tops = []
        for j, b in enumerate(sys_.vanster):
            w, h = _hang_dim(b)
            topp = y + (50 if j == 0 else 26)
            R.linje(xh, y, xh, topp)
            tops.append((y, topp))
            R.kloss(xh - w / 2, topp, w, h, len(sys_.vanster) - 1 - j, b.etikett)
            y = topp + h
        ymax = max(ymax, y + 20)
        # lappar i kedjans ordning: nedersta snöret först
        for (y0, y1) in reversed(tops[1:]):
            snorlapp(xh - 8, (y0 + y1) / 2 + 4, 'end')
        snorlapp(xh - 8, (tops[0][0] + tops[0][1]) / 2 + 4, 'end')
    for i in range(1, len(pos)):
        x0 = pos[i - 1][0] + pos[i - 1][1]
        R.linje(x0, yr, pos[i][0], yr)
        snorlapp((x0 + pos[i][0]) / 2, yr - 7)
    if sys_.hoger:
        cx, cy = TR + 10, yr + rr
        R.trissa(cx, cy, rr, TR - 2, ty + 3)
        if pos:
            x0 = pos[-1][0] + pos[-1][1]
            R.linje(x0, yr, cx, yr)
        xh = cx + rr
        y = cy
        for j, b in enumerate(sys_.hoger):
            w, h = _hang_dim(b)
            topp = y + (50 if j == 0 else 26)
            R.linje(xh, y, xh, topp)
            snorlapp(xh + 8, (y + topp) / 2 + 4, 'start')
            R.kloss(xh - w / 2, topp, w, h, len(sys_.vanster) + len(sys_.bord) + j, b.etikett)
            y = topp + h
        ymax = max(ymax, y + 20)
        xmax = xh + 40
    else:
        xmax = TR + 20
        if sys_.F:
            x0 = pos[-1][0] + pos[-1][1]
            R.pil(x0, yr, x0 + 70, yr)
            R.text(x0 + 74, yr + 5, Ftext, 15, 'start', RED, bold=True, italic=True)
    golv = ymax
    xmin = 0
    W = max(xmax, TR + 20) + 10
    R.bak.insert(0, f'<rect x="4" y="{_f(golv)}" width="{_f(W - 8)}" height="10" fill="url(#{pid}str)"/>'
                    f'<line x1="4" y1="{_f(golv)}" x2="{_f(W - 4)}" y2="{_f(golv)}" stroke="#4d5865" stroke-width="2.2"/>')
    # benen ska nå golvet
    R.bak = [e.replace(f'height="{benh - tjock}"', f'height="{_f(golv - ty - tjock)}"') for e in R.bak]
    return R.svg(W, golv + 14, titel, W * skala)


# ================================================================ friläggningsfigur
KRAFTFARG = {'g': '#2e7d4f', 'N': '#2f6fb3', 'S': '#6a48a3', 'F': RED, 'f': '#d4762c'}


def frilagg(pid, etikett, krafter, fargindex=0, bredd=None):
    """Friläggning av en kloss. krafter: lista (riktning 'u'/'d'/'l'/'r', LaTeX-fri text, längd, typ)."""
    R = Rit(pid)
    w, h = 64, 40
    cx, cy = 120, 95
    R.kloss(cx - w / 2, cy - h / 2, w, h, fargindex, etikett)
    for rikt, text, L, typ in krafter:
        c = KRAFTFARG[typ]
        if rikt == 'u':
            R.pil(cx, cy - h / 2, cx, cy - h / 2 - L, c)
            R.text(cx + 9, cy - h / 2 - L + 12, text, 14, 'start', c, bold=True, italic=True, halo=True)
        elif rikt == 'd':
            R.pil(cx, cy + h / 2, cx, cy + h / 2 + L, c)
            R.text(cx + 9, cy + h / 2 + L - 2, text, 14, 'start', c, bold=True, italic=True, halo=True)
        elif rikt == 'r':
            R.pil(cx + w / 2, cy, cx + w / 2 + L, cy, c)
            R.text(cx + w / 2 + L, cy - 9, text, 14, 'end', c, bold=True, italic=True, halo=True)
        elif rikt == 'l':
            R.pil(cx - w / 2, cy, cx - w / 2 - L, cy, c)
            R.text(cx - w / 2 - L, cy - 9, text, 14, 'start', c, bold=True, italic=True, halo=True)
    return R.svg(240, 190, f'Friläggning av klossen {etikett}', bredd or 240)


def _sub(bas, sub):
    return f'{bas}<tspan font-size="10" dy="3">{sub}</tspan>'


def frilagg_kedja(sys_, pid, snornamn=None, titel='Friläggning', endast=None):
    """Alla kroppar frilagda bredvid varandra. Pilarna är inte skalenliga.

    snornamn: namn på snörkrafterna i kedjans ordning (standard S, eller S₁, S₂ … vid flera snören).
    """
    kedja = sys_.kedja()
    n = len(kedja) - 1
    if snornamn is None:
        snornamn = ['S'] if n == 1 else [f'S{"₁₂₃₄"[i]}' for i in range(n)]
    a, _ = sys_.los()
    framat = a >= 0
    R = Rit(pid)
    bredd = 180
    cy = 110
    h = 36
    valda = list(range(len(kedja))) if endast is None else list(endast)
    for plats, i in enumerate(valda):
        b = kedja[i]
        w = max(58, _textbredd(b))
        cx = 90 + plats * bredd
        R.kloss(cx - w / 2, cy - h / 2, w, h, i, b.etikett)
        fore = snornamn[i - 1] if i > 0 else None
        efter = snornamn[i] if i < n else None
        lila, gron = KRAFTFARG['S'], KRAFTFARG['g']

        def upp(x, L, text, c):
            R.pil(x, cy - h / 2, x, cy - h / 2 - L, c)
            R.text(x + 7, cy - h / 2 - L + 11, text, 13, 'start', c, bold=True, italic=True, halo=True)

        def ned(x, L, text, c, vanster=False):
            R.pil(x, cy + h / 2, x, cy + h / 2 + L, c)
            R.text(x - 7 if vanster else x + 7, cy + h / 2 + L - 1, text, 13, 'end' if vanster else 'start', c,
                   bold=True, italic=True, halo=True)

        def sid(rikt, y, L, text, c, under=False):
            x0 = cx + w / 2 if rikt == 'r' else cx - w / 2
            x1 = x0 + L if rikt == 'r' else x0 - L
            R.pil(x0, y, x1, y, c)
            R.text((x0 + x1) / 2, y + 17 if under else y - 8, text, 13, 'middle', c, bold=True, italic=True, halo=True)

        if b.plats == 'B':
            upp(cx, 40, _sub('F', 'N'), KRAFTFARG['N'])
            ned(cx, 40, _sub('F', 'g'), gron)
            if fore:
                sid('l', cy - 6, 46, fore, lila)
            if efter:
                sid('r', cy - 6, 46, efter, lila)
            if sys_.F and i == len(kedja) - 1:
                sid('r', cy - 6, 56, 'F', KRAFTFARG['F'])
            if b.friktion:
                sid('l' if framat else 'r', cy + 10, 38, _sub('F', 'f'), KRAFTFARG['f'], under=True)
        else:
            uppat = fore if b.plats == 'H' else efter
            nedat = efter if b.plats == 'H' else fore
            if uppat:
                upp(cx, 48, uppat, lila)
            if nedat:
                ned(cx - 12, 36, nedat, lila, vanster=True)
                ned(cx + 12, 54, _sub('F', 'g'), gron)
            else:
                ned(cx, 54, _sub('F', 'g'), gron)
    W = bredd * len(valda) + (40 if sys_.F and len(kedja) - 1 in valda else 0)
    return R.svg(W, 210, titel, W)
