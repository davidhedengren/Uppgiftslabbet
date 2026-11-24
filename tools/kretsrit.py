"""Kopplingsscheman som SVG för Fy1 (komplexa kopplingar, 2026-11-24).

En krets byggs av block som läggs ut automatiskt:

    R('R₁', '12 Ω')        resistor (namn ovanför, värde under)
    Sakring('Säkring')     säkring
    L('L₁', '6,0 Ω')       lampa
    M('A') / M('V', 'V₁')  amperemeter eller voltmeter (bokstav i cirkeln, ev. namn ovanför)
    S(oppen=True)          brytare
    Ser(a, b, …)           seriekoppling (vågrätt)
    Par(a, b, …)           parallellkoppling (grenarna under varandra)

    krets(Ser(R('R₁', '4 Ω'), Par(R('R₂', '6 Ω'), R('R₃', '12 Ω'))), '12 V', titel='…')

Batteriet ritas på den nedre ledningen med pluspolen till vänster (lång platta) och spänningen under. Ledningarna är
raka, noderna med tre ledningar har prickar, och ingen ledning går förbi en komponent. Ramen är högst cirka 400 enheter
bred så att texten blir minst cirka 12 px i ett 320 px brett mobilkort (agent/FELMONSTER_OCH_BESLUT.md, 2026-11-24).
"""
from html import escape

FARG = '#243447'
FS = 15            # etiketter
FS_VARDE = 14      # värden under komponenten
FONT = 'Arial,sans-serif'
PAD = 14           # vågrätt avstånd mellan block och samlingsskena i en parallellkoppling
VGAP = 14          # lodrätt avstånd mellan grenar


def tb(txt, fs):
    """Ungefärlig textbredd (Arial)."""
    bred = sum(0.62 if c in 'ΩWMm' else 0.32 if c in 'il1,. ' else 0.56 for c in txt)
    return bred * fs


class Del:
    """Ett block med bredd w, höjd över ledningen a och under ledningen d. rita(x, y) ritar med vänster
    anslutning i (x, y) och höger i (x + w, y)."""
    w = a = d = 0

    def rita(self, x, y, ut):
        raise NotImplementedError


class Komp(Del):
    def __init__(self, namn='', varde='', kropp=44):
        self.namn, self.varde = namn, varde
        self.kropp = kropp
        self.w = max(kropp + 24, tb(namn, FS) + 10, tb(varde, FS_VARDE) + 10)
        self.a = 12 + (22 if namn else 0)
        self.d = 12 + (22 if varde else 0)

    def etiketter(self, cx, y, ut, over=12, under=12):
        if self.namn:
            ut.append(text(cx, y - over - 8, self.namn, FS, 'middle', vikt='bold'))
        if self.varde:
            ut.append(text(cx, y + under + 19, self.varde, FS_VARDE, 'middle'))

    def ledare(self, x, y, k0, k1, ut):
        ut.append(linje(x, y, k0, y))
        ut.append(linje(k1, y, x + self.w, y))


class R(Komp):
    def __init__(self, namn='', varde='', farg='#fff'):
        super().__init__(namn, varde, 44)
        self.farg = farg
        self.a = 8 + (24 if namn else 0)
        self.d = 8 + (24 if varde else 0)

    def rita(self, x, y, ut):
        cx = x + self.w / 2
        k0, k1 = cx - 22, cx + 22
        self.ledare(x, y, k0, k1, ut)
        ut.append(f'<rect x="{f(k0)}" y="{f(y - 8)}" width="44" height="16" fill="{self.farg}" stroke="{FARG}" stroke-width="2"/>')
        self.etiketter(cx, y, ut, 8, 8)


class Sakring(R):
    """Säkring: rektangel med en linje genom (IEC)."""
    def rita(self, x, y, ut):
        super().rita(x, y, ut)
        cx = x + self.w / 2
        ut.append(linje(cx - 22, y, cx + 22, y))


class L(Komp):
    def __init__(self, namn='', varde=''):
        super().__init__(namn, varde, 28)
        self.a = 14 + (22 if namn else 0)
        self.d = 14 + (22 if varde else 0)

    def rita(self, x, y, ut):
        cx = x + self.w / 2
        self.ledare(x, y, cx - 14, cx + 14, ut)
        ut.append(f'<circle cx="{f(cx)}" cy="{f(y)}" r="14" fill="#fff" stroke="{FARG}" stroke-width="2"/>')
        r = 9.9
        ut.append(f'<path d="M{f(cx - r)} {f(y - r)} L{f(cx + r)} {f(y + r)} M{f(cx - r)} {f(y + r)} L{f(cx + r)} {f(y - r)}" '
                  f'stroke="{FARG}" stroke-width="2"/>')
        self.etiketter(cx, y, ut, 14, 14)


class M(Komp):
    """Mätare: 'A' eller 'V'."""
    def __init__(self, typ='A', namn=''):
        super().__init__(namn, '', 30)
        self.typ = typ
        self.a = 15 + (22 if namn else 0)
        self.d = 15

    def rita(self, x, y, ut):
        cx = x + self.w / 2
        self.ledare(x, y, cx - 15, cx + 15, ut)
        ut.append(f'<circle cx="{f(cx)}" cy="{f(y)}" r="15" fill="#f0f6fc" stroke="{FARG}" stroke-width="2"/>')
        ut.append(text(cx, y + 5.5, self.typ, 16, 'middle', vikt='bold'))
        if self.namn:
            ut.append(text(cx, y - 23, self.namn, FS, 'middle', vikt='bold'))


class S(Komp):
    """Brytare, öppen eller sluten."""
    def __init__(self, namn='', oppen=True):
        super().__init__(namn, '', 36)
        self.oppen = oppen
        self.a = 16 + (20 if namn else 0)
        self.d = 6

    def rita(self, x, y, ut):
        cx = x + self.w / 2
        k0, k1 = cx - 18, cx + 18
        self.ledare(x, y, k0, k1, ut)
        ut.append(f'<circle cx="{f(k0)}" cy="{f(y)}" r="3" fill="{FARG}"/><circle cx="{f(k1)}" cy="{f(y)}" r="3" fill="{FARG}"/>')
        slut = (k1, y - 14) if self.oppen else (k1, y)
        ut.append(linje(k0, y, slut[0], slut[1]))
        if self.namn:
            ut.append(text(cx, y - 22, self.namn, FS, 'middle', vikt='bold'))


class Tråd(Del):
    def __init__(self, w=20):
        self.w, self.a, self.d = w, 4, 4

    def rita(self, x, y, ut):
        ut.append(linje(x, y, x + self.w, y))


class Ser(Del):
    def __init__(self, *delar):
        # En parallellkoppling i början eller slutet av en seriegren får en kort ledning, så att dess samlingsskena
        # inte hamnar tätt intill en yttre parallellkopplings skena.
        delar = list(delar)
        if len(delar) > 1 and isinstance(delar[-1], Par):
            delar.append(Tråd(14))
        if len(delar) > 1 and isinstance(delar[0], Par):
            delar.insert(0, Tråd(14))
        self.delar = delar
        self.w = sum(d.w for d in delar)
        self.a = max(d.a for d in delar)
        self.d = max(d.d for d in delar)

    def rita(self, x, y, ut):
        for d in self.delar:
            d.rita(x, y, ut)
            x += d.w


class Par(Del):
    def __init__(self, *grenar):
        self.grenar = grenar
        inre = max(g.w for g in grenar)
        self.inre = inre
        self.w = inre + 2 * PAD
        self.a = grenar[0].a
        h = 0
        self.ys = []
        for i, g in enumerate(grenar):
            if i:
                h += grenar[i - 1].d + VGAP + g.a
            self.ys.append(h)
        self.d = h + grenar[-1].d

    def rita(self, x, y, ut):
        xl, xr = x + PAD, x + self.w - PAD
        ut.append(linje(x, y, xl, y))
        ut.append(linje(xr, y, x + self.w, y))
        botten = y + self.ys[-1]
        ut.append(linje(xl, y, xl, botten))
        ut.append(linje(xr, y, xr, botten))
        for i, g in enumerate(self.grenar):
            yy = y + self.ys[i]
            extra = self.inre - g.w
            gx = xl + extra / 2
            if extra > 0:
                ut.append(linje(xl, yy, gx, yy))
                ut.append(linje(gx + g.w, yy, xr, yy))
            g.rita(gx, yy, ut)
            if i < len(self.grenar) - 1:      # tre ledningar möts: prick
                ut.append(prick(xl, yy))
                ut.append(prick(xr, yy))


def f(v):
    return ('%.1f' % v).rstrip('0').rstrip('.')


def linje(x1, y1, x2, y2):
    return f'<path d="M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}" stroke="{FARG}" stroke-width="2" fill="none"/>'


def prick(x, y):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="3.5" fill="{FARG}"/>'


def text(x, y, t, fs, anchor='start', vikt='normal', farg=FARG):
    v = ' font-weight="bold"' if vikt == 'bold' else ''
    return (f'<text x="{f(x)}" y="{f(y)}" font-family="{FONT}" font-size="{fs}" text-anchor="{anchor}"{v} '
            f'fill="{farg}">{escape(t, quote=False)}</text>')


def krets(nat, spanning='', titel='Kopplingsschema', batteri=True, punkter=None):
    """Hela kretsen: nätet på den övre ledningen, batteriet på den nedre.
    punkter: {'A': 'fore'/'efter'} markerar anslutningspunkter före/efter nätet (för uppgifter utan batteri)."""
    ut = []
    m = 16
    x0 = m + 4
    y0 = m + nat.a + 4
    xn = x0 + 18
    x1 = xn + nat.w + 18
    yb = y0 + nat.d + (40 if batteri else 0)
    if batteri:
        ut.append(linje(x0, y0, xn, y0))
        nat.rita(xn, y0, ut)
        ut.append(linje(xn + nat.w, y0, x1, y0))
        ut.append(linje(x0, y0, x0, yb))
        ut.append(linje(x1, y0, x1, yb))
        bx = (x0 + x1) / 2
        ut.append(linje(x0, yb, bx - 5, yb))
        ut.append(linje(bx + 5, yb, x1, yb))
        ut.append(f'<path d="M{f(bx - 5)} {f(yb - 16)} L{f(bx - 5)} {f(yb + 16)}" stroke="{FARG}" stroke-width="2"/>')
        ut.append(f'<path d="M{f(bx + 5)} {f(yb - 9)} L{f(bx + 5)} {f(yb + 9)}" stroke="{FARG}" stroke-width="5"/>')
        ut.append(text(bx - 16, yb - 10, '+', 15, 'middle'))
        ut.append(text(bx + 17, yb - 10, '−', 15, 'middle'))
        if spanning:
            ut.append(text(bx, yb + 34, spanning, FS, 'middle', vikt='bold'))
        h = yb + (46 if spanning else 26)
        w = x1 + m
    else:
        # bara nätet mellan två anslutningspunkter
        ut.append(linje(x0, y0, xn, y0))
        nat.rita(xn, y0, ut)
        ut.append(linje(xn + nat.w, y0, x1, y0))
        for x, namn in ((x0, (punkter or {}).get('v', 'A')), (x1, (punkter or {}).get('h', 'B'))):
            ut.append(f'<circle cx="{f(x)}" cy="{f(y0)}" r="5" fill="#fff" stroke="{FARG}" stroke-width="2"/>')
            ut.append(text(x, y0 + 24 if nat.d < 30 else y0 - 12, namn, FS, 'middle', vikt='bold'))
        h = y0 + nat.d + m + 8
        w = x1 + m
    titel = escape(titel)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(w)}" height="{f(h)}" viewBox="0 0 {f(w)} {f(h)}" '
            f'role="img" aria-label="{titel}" style="width:100%;max-width:{f(min(w * 1.15, 460))}px;height:auto">'
            f'<title>{titel}</title><rect x="1" y="1" width="{f(w - 2)}" height="{f(h - 2)}" rx="10" fill="#fff" '
            f'stroke="#dce4ed"/>' + ''.join(ut) + '</svg>')
