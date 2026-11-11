"""Hjälpfunktioner för A-uppgifterna 2026-11-10: facit enligt agent/FACITMALL.md, SVG-figurer och bankformat.

Importeras av tools/bygg-a-uppgifter-ma3c-2026-11-10.py och tools/bygg-a-uppgifter-fy1-2026-11-10.py.
"""
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOK = 'abcdefgh'

# ---------------------------------------------------------------- text och facit
def m(t):
    return f'\\({t}\\)'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def al(*rader):
    """Flera rader under varandra (mobil): varje rad börjar med &."""
    return mt('\\begin{aligned}' + '\\\\'.join('&' + r for r in rader) + '\\end{aligned}')


def p(t):
    return f'<p>{t}</p>'


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def delad(facitlista):
    return ('<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{BOK[i]})</span><div class="facit-arbete">{f}</div></div>'
        for i, f in enumerate(facitlista)) + '</div>')


def tx(v, d):
    """Tal i LaTeX med decimalkomma."""
    return f'{v:.{d}f}'.replace('.', '{,}')


def sv(v, d=0):
    """Tal i löptext med decimalkomma och riktigt minustecken."""
    return f'{v:.{d}f}'.replace('.', ',').replace('-', '−')


# ---------------------------------------------------------------- SVG
INK, BLA, ORA, GRON, ROD, GRA, LJUS = '#203746', '#0b6fa4', '#b25c17', '#22764a', '#b13b19', '#526777', '#edf4f8'
FONT = 'font-family="Arial,sans-serif"'


def svg(w, h, body, label):
    return (f'<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{label}" style="max-width:100%;height:auto"><title>{label}</title>'
            f'<rect width="{w}" height="{h}" fill="#fff"/>{body}</svg></span>')


def tt(x, y, s, size=15, anchor='middle', fill=INK, bold=False, halo=False, italic=False):
    extra = (' font-weight="bold"' if bold else '') + (' font-style="italic"' if italic else '')
    if halo:
        extra += ' stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round"'
    return f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" {FONT} font-size="{size}" text-anchor="{anchor}"{extra}>{s}</text>'


def linje(x1, y1, x2, y2, color=INK, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w}"{d}/>'


def pil(x1, y1, x2, y2, color=ROD, w=3, head=11):
    """Pil från (x1, y1) till spetsen (x2, y2)."""
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    bx, by = x2 - ux * head, y2 - uy * head
    nx, ny = -uy * head * 0.45, ux * head * 0.45
    return (linje(x1, y1, bx, by, color, w)
            + f'<polygon points="{x2:.1f},{y2:.1f} {bx + nx:.1f},{by + ny:.1f} {bx - nx:.1f},{by - ny:.1f}" fill="{color}"/>')


def polygon(pts, fill='none', stroke=INK, w=2, opacity=None):
    o = f' fill-opacity="{opacity}"' if opacity is not None else ''
    return (f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}"{o} stroke="{stroke}" '
            f'stroke-width="{w}" stroke-linejoin="round"/>')


def rekt(x, y, w, h, fill=LJUS, stroke=INK, sw=2, rx=3):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def cirkel(x, y, r, fill=ORA, stroke='#fff', sw=1.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def tal(v):
    s = f'{v:g}'.replace('.', ',').replace('-', '−')
    return s


class Plot:
    """Koordinatsystem för grafer. Kurvor klipps mot ritytan."""

    def __init__(self, x0, x1, y0, y1, W=420, H=300, ml=46, mr=18, mo=18, mb=40):
        self.x0, self.x1, self.y0, self.y1, self.W, self.H = x0, x1, y0, y1, W, H
        self.ml, self.mr, self.mo, self.mb = ml, mr, mo, mb
        self.ut = []

    def X(self, x):
        return self.ml + (x - self.x0) / (self.x1 - self.x0) * (self.W - self.ml - self.mr)

    def Y(self, y):
        return self.mo + (self.y1 - y) / (self.y1 - self.y0) * (self.H - self.mo - self.mb)

    def axlar(self, xt=(), yt=(), xlabel='x', ylabel='y', rut=True, siffror=True):
        X, Y = self.X, self.Y
        ax = Y(0) if self.y0 <= 0 <= self.y1 else Y(self.y0)
        ay = X(0) if self.x0 <= 0 <= self.x1 else X(self.x0)
        if rut:
            for v in xt:
                self.ut.append(linje(X(v), Y(self.y0), X(v), Y(self.y1), '#d7e0e7', 1))
            for v in yt:
                self.ut.append(linje(X(self.x0), Y(v), X(self.x1), Y(v), '#d7e0e7', 1))
        self.ut.append(pil(X(self.x0), ax, X(self.x1) + 10, ax, INK, 1.6, 9))
        self.ut.append(pil(ay, Y(self.y0), ay, Y(self.y1) - 10, INK, 1.6, 9))
        for v in xt:
            self.ut.append(linje(X(v), ax - 4, X(v), ax + 4, INK, 1.4))
            if siffror and v != 0:
                self.ut.append(tt(X(v), ax + 18, tal(v), 13, halo=True))
        for v in yt:
            self.ut.append(linje(ay - 4, Y(v), ay + 4, Y(v), INK, 1.4))
            if siffror and v != 0:
                self.ut.append(tt(ay - 8, Y(v) + 4.5, tal(v), 13, 'end', halo=True))
        self.ut.append(tt(X(self.x1) + 8, ax - 9, xlabel, 14, 'end', italic=len(xlabel) == 1))
        self.ut.append(tt(ay + 9, Y(self.y1) - 2, ylabel, 14, 'start', italic=len(ylabel) == 1))
        return self

    def _punkter(self, f, a, b, n=240):
        seg, segs = [], []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            y = f(x)
            if self.y0 - 1e-9 <= y <= self.y1 + 1e-9:
                seg.append((self.X(x), self.Y(y)))
            elif seg:
                segs.append(seg)
                seg = []
        if seg:
            segs.append(seg)
        return segs

    def kurva(self, f, a=None, b=None, color=BLA, w=2.6, dash=None):
        a = self.x0 if a is None else a
        b = self.x1 if b is None else b
        d = f' stroke-dasharray="{dash}"' if dash else ''
        for seg in self._punkter(f, a, b):
            self.ut.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in seg)}" fill="none" stroke="{color}" '
                           f'stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"{d}/>')
        return self

    def fyll(self, f, g, a, b, color=BLA, op=0.22, n=120):
        upp = [(self.X(a + (b - a) * i / n), self.Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
        ner = [(self.X(a + (b - a) * i / n), self.Y(g(a + (b - a) * i / n))) for i in range(n, -1, -1)]
        self.ut.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in upp + ner)}" fill="{color}" fill-opacity="{op}" stroke="none"/>')
        return self

    def punkt(self, x, y, etikett='', dx=8, dy=-8, color=ORA, anchor='start', size=14):
        self.ut.append(cirkel(self.X(x), self.Y(y), 5, color))
        if etikett:
            self.ut.append(tt(self.X(x) + dx, self.Y(y) + dy, etikett, size, anchor, color, bold=True, halo=True))
        return self

    def streck(self, x1, y1, x2, y2, color=GRA, w=1.6, dash='5 4'):
        self.ut.append(linje(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), color, w, dash))
        return self

    def text(self, x, y, s, color=INK, size=14, anchor='middle', bold=False):
        self.ut.append(tt(self.X(x), self.Y(y), s, size, anchor, color, bold=bold, halo=True))
        return self

    def svg(self, label):
        return svg(self.W, self.H, ''.join(self.ut), label)


# ---------------------------------------------------------------- bankformat
def las(fil):
    src = (ROOT / fil).read_text(encoding='utf-8')
    return src, json.loads(src[src.index('['):src.rindex(']') + 1])


def nasta_id(bank, kap):
    return 1 + max(int(str(q['id']).split('.')[1]) for q in bank if re.fullmatch(rf'{kap}\.\d+', str(q['id'])))


def lagg_till(fil, src, nya):
    """Lägger nya uppgifter sist i banken, i bankens indragna JSON-format."""
    end = src.rindex(']')
    ny = src[:end].rstrip() + ',\n' + json.dumps(nya, ensure_ascii=False, indent=2)[1:-1].strip('\n') + '\n' + src[end:]
    json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    with open(ROOT / fil, 'w', encoding='utf-8', newline='') as fh:
        fh.write(ny)


def del_(fraga, steg, svar, ledtrad, ratt, niva, tn, poang, fmt='numeriskt', tol=1e-9, kortfraga=None, enhet=None, vs=None,
         ai=2, ratt_txt=(), fel=()):
    """En deluppgift. fraga visas i huvuduppgiften, kortfraga (om given) i delkortet med behövda mellanresultat."""
    return dict(fraga=fraga, kortfraga=kortfraga or fraga, steg=steg, svar=svar, ledtrad=ledtrad, ratt=ratt, niva=niva, tn=tn,
                poang=poang, fmt=fmt, tol=tol, enhet=enhet, vs=vs, ai=ai, ratt_txt=list(ratt_txt), fel=list(fel))


def _poang(delar, fy):
    e, c, a = (sum(d['poang'][k] for d in delar) for k in range(3))
    return f'({e}/{c}/{a})' if fy else f'{e}/{c}/{a}'


def _p1(po, fy):
    return ('(%d/%d/%d)' if fy else '%d/%d/%d') % tuple(po)


def bygg(uid, kap, omr, familj, intro, delar, formaga, mr, gg, ledtrad, varianter, fy=False, kurs=None, familjnyckel=None):
    """Bygger bankobjektet. Matematikbanken och fysikbanken har något olika fält."""
    hogst = max(delar, key=lambda d: d['tn'])
    bas = dict(id=uid, kap=kap, omr=omr)
    if not fy:
        bas['kurs'] = kurs
    bas['familj'] = familj
    if fy:
        bas['familjNyckel'] = familjnyckel
    bas.update(niva='A' if any(d['poang'][2] for d in delar) else 'C', poang=_poang(delar, fy), traningsniva=hogst['tn'],
               arbetsinsats=3, formaga=list(formaga), miniräknare=mr, geogebra=gg, spel=True, självrättning=True)
    for i, d in enumerate(delar):
        varianter[uid + (BOK[i] if len(delar) > 1 else '')] = dict(ratt=d['ratt_txt'], fel=d['fel'])
    if len(delar) == 1:
        d = delar[0]
        bas.update(t=intro + p(d['fraga']), s=facit(d['steg'], d['svar']), ledtrad=p(ledtrad), rättSvar=d['ratt'],
                   svarstyp='numeriskt' if d['fmt'] == 'numeriskt' else 'uttryck', svarFormat=d['fmt'],
                   tolerans=d['tol'] if d['fmt'] == 'numeriskt' else None)
        if d['enhet']:
            bas['svarEnhet'] = d['enhet']
        if fy and d['vs'] is not None:
            bas['svarVardesiffror'] = d['vs']
        return bas
    if fy:
        t = intro + '<ol type="a">' + ''.join(f'<li>{d["fraga"]}</li>' for d in delar) + '</ol>'
    else:
        t = intro + ''.join(f'<p>{BOK[i]}) {d["fraga"]}</p>' for i, d in enumerate(delar))
    nast = lambda d, v: ([v] * len(d['ratt']) if isinstance(d['ratt'], list) else v)
    bas.update(t=t, s=delad([facit(d['steg'], d['svar']) for d in delar]), ledtrad=p(ledtrad),
               rättSvar=[d['ratt'] for d in delar], svarFormat=[nast(d, d['fmt']) for d in delar],
               tolerans=[nast(d, d['tol'] if d['fmt'] == 'numeriskt' else None) for d in delar],
               svarstyp='flera_delar', svarsstruktur='ordnad', svarEtiketter=list(BOK[:len(delar)]))
    if any(d['enhet'] for d in delar):
        bas['svarEnhet'] = [d['enhet'] for d in delar]
    if fy:
        bas['svarVardesiffror'] = [d['vs'] for d in delar]
    bas.update(spelDelning='deluppgifter', spelIntro=intro, spelDelar=[])
    for i, d in enumerate(delar):
        kort = dict(etikett=BOK[i], fraga=d['kortfraga'])
        if fy:
            kort['t'] = intro + p(d['kortfraga'])
        kort.update(s=facit(d['steg'], d['svar']), ledtrad=p(d['ledtrad']), niva='A' if d['poang'][2] else ('C' if d['poang'][1] else 'E'),
                    poang=_p1(d['poang'], fy), traningsniva=d['tn'], arbetsinsats=d['ai'])
        bas['spelDelar'].append(kort)
    return bas
