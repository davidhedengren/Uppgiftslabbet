"""Fysik 1 (uppgifter.js), densitet: figurer i uppgifter som saknade figur, 18 november 2026.

Användaren 2026-11-18: fler uppgifter i kapitel 2 ska ha figur, snygga och med färg, men inte generiska och inte när de
inte tillför något. Varje figur nedan är ritad för sin uppgift. Den läggs efter första stycket i frågan (t), sist i
spelIntro och efter första stycket i varje delkort. Inga andra fält ändras. Figurerna avslöjar inga svar: okända storheter
är markerade med ?, och föremål med okänd storlek är inte ritade skalenligt. Se agent/FY1_KAP2_FIGURER_2026-11-18.md.

  python tools/bygg-fy1-densitet-figurer-2026-11-18.py [--skriv] [--ut fil.json]
"""
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import svg, tt, linje, pil, rekt, cirkel, BLA, ORA, GRON, GRA, INK, ROD  # noqa: E402

BANK = 'uppgifter.js'
VATTEN = '#cfe6f5'
JARN, STAL, KOPPAR, ALU, GULD, SILVER = '#8c969e', '#9aa8b4', '#c8773a', '#d5dce2', '#e3b53f', '#cfd3d7'
TRA, LUFT, GLAS = '#d9a868', '#ffffff', '#f7fafc'


# ---------------------------------------------------------------- byggstenar
def path(d, fill='none', stroke=INK, w=2, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" stroke-linejoin="round"{extra}/>'


def ellips(cx, cy, rx, ry, fill='none', stroke=INK, w=2):
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"/>'


def ring(cx, cy, r, fill, stroke=INK, w=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"/>'


def matt_h(x1, x2, y, text, under=False, color=GRA, size=14):
    b = linje(x1, y, x2, y, color, 1.5) + linje(x1, y - 6, x1, y + 6, color, 1.5) + linje(x2, y - 6, x2, y + 6, color, 1.5)
    return b + tt((x1 + x2) / 2, y + 19 if under else y - 8, text, size, fill=INK, halo=True)


def matt_v(x, y1, y2, text, vanster=False, color=GRA, size=14):
    b = linje(x, y1, x, y2, color, 1.5) + linje(x - 6, y1, x + 6, y1, color, 1.5) + linje(x - 6, y2, x + 6, y2, color, 1.5)
    return b + tt(x - 9 if vanster else x + 9, (y1 + y2) / 2 + 5, text, size, 'end' if vanster else 'start', INK, halo=True)


def lada(x, y, w, h, dx, dy, front, top, side, sw=2):
    """Rätblock i snedprojektion: framsidan (x, y, w, h), djupet åt höger och uppåt."""
    b = rekt(x, y, w, h, front, INK, sw, 0)
    b += path(f'M{x},{y} L{x + dx},{y - dy} L{x + w + dx},{y - dy} L{x + w},{y} Z', top, INK, sw)
    b += path(f'M{x + w},{y} L{x + w + dx},{y - dy} L{x + w + dx},{y + h - dy} L{x + w},{y + h} Z', side, INK, sw)
    return b


def cylinder_v(cx, ytop, rx, ry, h, fill, topp=None, sw=2):
    """Stående cylinder. ytop är toppellipsens mitt."""
    b = path(f'M{cx - rx},{ytop} L{cx - rx},{ytop + h} A{rx},{ry} 0 0 0 {cx + rx},{ytop + h} L{cx + rx},{ytop} Z', fill, INK, sw)
    return b + ellips(cx, ytop, rx, ry, topp or fill, INK, sw)


def matglas(x0, niva, vmax, steg, text_steg, vatska=VATTEN, foremal='', H_=180, ybot=222, etikett=True, noll=True):
    """Mätglas med skala. Returnerar (svg, y-funktion)."""
    y = lambda v: ybot - v * H_ / vmax
    b = rekt(x0, y(vmax) - 6, 64, ybot - y(vmax) + 6, GLAS, INK, 2, 4)
    b += f'<rect x="{x0 + 2}" y="{y(niva):.1f}" width="60" height="{ybot - 2 - y(niva):.1f}" fill="{vatska}"/>'
    b += linje(x0 + 2, y(niva), x0 + 62, y(niva), BLA, 2)
    v = 0
    while v <= vmax + 1e-9:
        stor = abs(v / text_steg - round(v / text_steg)) < 1e-9
        b += linje(x0, y(v), x0 + (12 if stor else 7), y(v), INK, 1.3)
        if stor and (noll or v > 0):
            b += tt(x0 - 6, y(v) + 4.5, f'{v:g}', 12, 'end')
        v += steg
    b += foremal
    if etikett:
        b += pil(x0 + 104, y(niva), x0 + 70, y(niva), BLA, 2, 8)
        b += tt(x0 + 108, y(niva) + 5, f'{niva:.1f} ml'.replace('.', ','), 14, 'start', BLA, True)
    return b, y


def vag(cx, y, text):
    """Våg med display. y är vågskålens överkant."""
    b = rekt(cx - 62, y, 124, 10, '#c9d3da', INK, 1.6, 3) + rekt(cx - 56, y + 10, 112, 34, '#e9eef2', INK, 1.6, 4)
    b += rekt(cx - 36, y + 16, 72, 22, '#1f2d36', INK, 1, 3) + tt(cx, y + 32, text, 13, 'middle', '#9ff0b4', True)
    return b


def bubblor(pts):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{BLA}" stroke-width="1.2"/>' for x, y, r in pts)


# ---------------------------------------------------------------- figurer
F = {}


def fig(uid, w, h, label):
    def dek(f):
        F[uid] = svg(w, h, f(), label)
        return f
    return dek


@fig('2.37', 420, 230, 'Genomskärning av en järnkula med ett luftfyllt hålrum inuti. Kulans massa är 1,2 kg och den yttre volymen 0,30 dm³.')
def _():
    b = ring(130, 115, 92, JARN) + ring(138, 108, 46, LUFT, INK, 1.6)
    b += tt(138, 113, 'luft', 13, 'middle', GRA)
    b += pil(268, 64, 186, 92, GRA, 2, 8) + tt(272, 62, 'hålrum', 14, 'start', INK, True)
    b += pil(268, 170, 196, 160, GRA, 2, 8) + tt(272, 168, 'järn', 14, 'start', INK, True) + tt(272, 186, '7,87 g/cm³', 13, 'start')
    b += tt(130, 226, 'm = 1,2 kg,  V = 0,30 dm³', 14, 'middle', INK, True)
    return b


@fig('2.77', 420, 220, 'Genomskärning av ett järnföremål med ett slutet, luftfyllt hålrum. Massan är 500 g och den yttre volymen 90 cm³.')
def _():
    b = path('M60,70 C70,30 170,24 220,40 C270,56 300,90 290,140 C282,186 200,196 140,190 C80,184 50,120 60,70 Z', JARN)
    b += path('M140,92 C150,74 200,72 214,96 C226,118 200,140 172,138 C148,136 132,112 140,92 Z', LUFT, INK, 1.6)
    b += tt(176, 112, 'luft', 13, 'middle', GRA)
    b += pil(322, 70, 220, 96, GRA, 2, 8) + tt(326, 68, 'hålrum', 14, 'start', INK, True)
    b += pil(322, 160, 270, 150, GRA, 2, 8) + tt(326, 158, 'järn', 14, 'start', INK, True) + tt(326, 176, '7,87 g/cm³', 13, 'start')
    b += tt(176, 214, 'm = 500 g,  V = 90 cm³', 14, 'middle', INK, True)
    return b


@fig('2.86', 440, 190, 'Ett majskorn med massan 0,15 g och volymen 0,12 cm³ poppas och blir ett popcorn med volymen 2,4 cm³.')
def _():
    b = path('M86,70 C104,70 112,92 108,112 C104,130 92,138 86,138 C80,138 68,130 64,112 C60,92 68,70 86,70 Z', '#f0b429', INK, 2)
    b += path('M78,80 C82,76 90,76 94,80', 'none', '#fff6d6', 2)
    b += tt(86, 166, 'majskorn', 14, 'middle', INK, True) + tt(86, 184, '0,15 g · 0,12 cm³', 13)
    b += pil(150, 104, 228, 104, ORA, 3) + tt(189, 92, 'poppas', 14, 'middle', ORA, True)
    for (x, y, r) in ((318, 78, 30), (284, 104, 28), (350, 108, 30), (316, 126, 30), (300, 66, 22), (342, 70, 22), (288, 132, 20), (348, 136, 20)):
        b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffaf0" stroke="#c9b48a" stroke-width="1.8"/>'
    b += f'<circle cx="316" cy="104" r="9" fill="#f0b429" stroke="{INK}" stroke-width="1.2"/>'
    b += tt(318, 176, 'popcorn', 14, 'middle', INK, True)
    b += tt(392, 104, '2,4 cm³', 13, 'start')
    return b


@fig('2.87', 360, 230, 'En glasflaska som rymmer 0,50 liter är helt fylld med vatten och har ett tätt lock. Den står i en frys.')
def _():
    b = rekt(40, 20, 280, 196, '#eef6fb', '#7aa3bd', 2.5, 10)
    for (x, y) in ((76, 52), (76, 150), (288, 182)):
        for a in (0, 60, 120):
            dx, dy = 11 * math.cos(math.radians(a)), 11 * math.sin(math.radians(a))
            b += linje(x - dx, y - dy, x + dx, y + dy, '#7aa3bd', 2)
    b += tt(78, 204, 'frys', 14, 'middle', '#4d7a96', True)
    b += path('M160,196 L160,110 C160,92 170,86 172,74 L172,54 L188,54 L188,74 C190,86 200,92 200,110 L200,196 Z', VATTEN, INK, 2)
    b += rekt(168, 40, 24, 16, ROD, INK, 1.8, 3)
    b += pil(236, 46, 196, 48, GRA, 2, 8) + tt(240, 50, 'tätt lock', 13, 'start', INK, True)
    b += tt(180, 160, '0,50 l', 13, 'middle', INK, True, halo=True)
    b += pil(236, 120, 202, 130, GRA, 2, 8) + tt(240, 118, 'vatten', 13, 'start', INK, True) + tt(240, 134, 'ända upp', 13, 'start')
    return b


@fig('2.114', 360, 250, 'En sten ligger på botten av ett mätglas med vatten. Små luftbubblor sitter fast på stenens yta.')
def _():
    sten = (path('M110,214 C108,198 120,188 134,189 C150,189 160,198 158,210 C157,219 146,220 134,220 C120,220 112,220 110,214 Z',
                 '#9b8f80', INK, 1.6)
            + bubblor([(112, 202, 3.5), (124, 189, 3.5), (144, 188, 4), (157, 200, 3.5), (154, 214, 3), (130, 206, 3)]))
    b, y = matglas(100, 60, 100, 5, 20, foremal=sten, etikett=False)
    b += pil(250, 150, 170, 194, GRA, 2, 8) + tt(254, 148, 'luftbubblor', 14, 'start', INK, True)
    b += pil(250, 226, 170, 214, GRA, 2, 8) + tt(254, 230, 'sten', 14, 'start', INK, True)
    b += tt(60, 30, 'ml', 13, 'middle', GRA)
    return b


@fig('2.144', 400, 220, 'Ett block flyter stilla i vatten med 72 procent av sin volym under vattenytan.')
def _():
    b = f'<rect x="20" y="92" width="360" height="118" fill="{VATTEN}"/>' + linje(20, 92, 380, 92, BLA, 2)
    top, h = 92 - 0.28 * 110, 110
    b += lada(140, top, 120, h, 22, 14, '#b7c9a8', '#cfdcc3', '#9fb48f')
    b += f'<rect x="20" y="92" width="360" height="118" fill="{VATTEN}" fill-opacity="0.55"/>' + linje(20, 92, 380, 92, BLA, 2)
    b += linje(298, 92, 298, top + h, ORA, 1.6) + linje(292, 92, 304, 92, ORA, 1.6) + linje(292, top + h, 304, top + h, ORA, 1.6)
    b += tt(308, 150, '72 % av', 13, 'start', ORA, True) + tt(308, 166, 'volymen', 13, 'start', ORA, True)
    b += tt(30, 200, 'vatten 1,00 g/cm³', 13, 'start', BLA, True)
    return b


@fig('2.151', 440, 230, 'Ett föremål med densiteten 0,75 g/cm³ flyter stilla i en okänd vätska med 60 procent av sin volym under ytan.')
def _():
    b = rekt(70, 30, 240, 190, GLAS, INK, 2, 6)
    b += f'<rect x="72" y="100" width="236" height="118" rx="4" fill="#e6d4f0"/>' + linje(72, 100, 308, 100, '#7b4fa0', 2)
    h = 100
    top = 100 - 0.40 * h
    b += cylinder_v(190, top, 34, 10, h, '#f2c48d', '#f7d9b5')
    b += f'<rect x="72" y="100" width="236" height="118" rx="4" fill="#e6d4f0" fill-opacity="0.55"/>' + linje(72, 100, 308, 100, '#7b4fa0', 2)
    b += linje(330, 100, 330, top + h, ORA, 1.6) + linje(324, 100, 336, 100, ORA, 1.6) + linje(324, top + h, 336, top + h, ORA, 1.6)
    b += tt(342, 150, '60 %', 14, 'start', ORA, True) + tt(342, 166, 'under ytan', 13, 'start', ORA, True)
    b += tt(190, top + 50 - 18, '0,75 g/cm³', 12, 'middle', INK, True, halo=True)
    b += tt(110, 200, 'okänd vätska', 13, 'start', '#6a3f8f', True)
    return b


@fig('2.289', 400, 190, 'En träbit flyter stilla i vatten med 80 procent av sin volym under vattenytan.')
def _():
    b = f'<rect x="20" y="80" width="360" height="100" fill="{VATTEN}"/>' + linje(20, 80, 380, 80, BLA, 2)
    h = 70
    top = 80 - 0.20 * h
    b += rekt(100, top, 200, h, TRA, INK, 2, 6)
    for k in range(1, 5):
        yk = top + k * h / 5
        b += path(f'M108,{yk:.1f} C150,{yk - 5:.1f} 200,{yk + 5:.1f} 292,{yk - 2:.1f}', 'none', '#b07f45', 1.2)
    b += f'<rect x="20" y="80" width="360" height="100" fill="{VATTEN}" fill-opacity="0.55"/>' + linje(20, 80, 380, 80, BLA, 2)
    b += linje(320, 80, 320, top + h, ORA, 1.6) + linje(314, 80, 326, 80, ORA, 1.6) + linje(314, top + h, 326, top + h, ORA, 1.6)
    b += tt(330, 110, '80 %', 14, 'start', ORA, True)
    return b


@fig('2.163', 440, 150, 'En cylinderformad järnstång som är 85,8 cm lång och har diametern 2,85 cm.')
def _():
    x0, x1, cy, ry, rx = 120, 410, 70, 18, 7
    b = path(f'M{x0},{cy - ry} L{x1},{cy - ry} A{rx},{ry} 0 0 1 {x1},{cy + ry} L{x0},{cy + ry} Z', JARN, INK, 2)
    b += ellips(x0, cy, rx, ry, '#b3bcc3', INK, 2)
    b += linje(x0 + 10, cy - ry + 6, x1 - 6, cy - ry + 6, '#c9d0d5', 2)
    b += matt_h(x0, x1, cy + ry + 26, '85,8 cm', under=True)
    b += matt_v(x0 - 26, cy - ry, cy + ry, '2,85 cm', vanster=True)
    return b


def _glas_fore_efter(niva0, niva1, vmax, steg, ts, foremal):
    b0, _ = matglas(70, niva0, vmax, steg, ts)
    b1, y = matglas(290, niva1, vmax, steg, ts, foremal=foremal)
    b = b0 + b1 + tt(102, 246, 'före', 14) + tt(322, 246, 'efter', 14) + tt(40, 26, 'ml', 13, 'middle', GRA)
    return b


@fig('2.165', 460, 256, 'Två mätglas. Före: vattnet står vid 78,0 ml. Efter att metallbiten sänkts ner står vattnet vid 83,0 ml.')
def _():
    return _glas_fore_efter(78.0, 83.0, 100, 5, 20, rekt(306, 204, 32, 14, SILVER, INK, 1.5, 2))


@fig('2.285', 460, 256, 'Två mätglas. Före: vattnet står vid 40 ml. Efter att stenen sänkts ner står vattnet vid 60 ml.')
def _():
    sten = path('M300,214 C298,198 314,190 330,192 C346,194 352,204 350,214 C348,222 336,222 324,222 C310,222 302,222 300,214 Z',
                '#9b8f80', INK, 1.6)
    b = _glas_fore_efter(40.0, 60.0, 80, 5, 20, sten)
    return b.replace('40,0 ml', '40 ml').replace('60,0 ml', '60 ml')


@fig('2.166', 440, 260, 'En lektionssal som ett rätblock: 6,0 m lång, 4,3 m bred och 2,6 m hög.')
def _():
    x, y, w, h, dx, dy = 90, 76, 240, 120, 80, 50
    b = lada(x, y, w, h, dx, dy, '#f3efe6', '#e7e1d3', '#e1d9c8')
    b += rekt(114, 116, 30, 80, '#b98b5a', INK, 1.6, 2) + rekt(180, 100, 120, 50, '#d6ebf7', INK, 1.6, 2)
    b += linje(240, 100, 240, 150, INK, 1.2)
    b += matt_h(x, x + w, y + h + 22, '6,0 m', under=True)
    b += tt(x + w + dx / 2 + 14, y + h - dy / 2 + 22, '4,3 m', 14, 'start', INK, halo=True)
    b += linje(x + w + 10, y + h + 6, x + w + dx + 10, y + h - dy + 6, GRA, 1.5)
    b += matt_v(x - 20, y, y + h, '2,6 m', vanster=True)
    return b


@fig('2.168', 300, 300, 'Ett cylindriskt falltorn som är 110 m högt och har diametern 3,50 m. Tornet är fyllt med luft.')
def _():
    b = rekt(0, 0, 300, 268, '#eaf4fb', 'none', 0, 0) + rekt(0, 268, 300, 32, '#cfe3c4', 'none', 0, 0) + linje(0, 268, 300, 268, '#6f9a5b', 2)
    b += cylinder_v(150, 46, 26, 8, 222, '#dfe6ec', '#c5d0d8')
    b += tt(150, 160, 'luft', 13, 'middle', GRA, True, halo=True)
    b += matt_v(210, 46, 268, '110 m')
    b += matt_h(124, 176, 26, '3,50 m')
    return b


@fig('2.179', 460, 190, 'Ett kopparrör sett från änden och från sidan. Ytterdiametern är 3,50 cm, innerdiametern 2,50 cm och längden 1,50 m.')
def _():
    cx, cy, R, r = 90, 92, 56, 40
    b = ring(cx, cy, R, KOPPAR) + ring(cx, cy, r, LUFT)
    b += matt_h(cx - R, cx + R, cy - R - 14, '3,50 cm') + matt_h(cx - r, cx + r, cy + 6, '2,50 cm', under=True)
    b += tt(cx, 182, 'änden', 13, 'middle', GRA, True)
    x0, x1, yc, ry, rx = 200, 430, 92, 22, 8
    b += path(f'M{x0},{yc - ry} L{x1},{yc - ry} A{rx},{ry} 0 0 1 {x1},{yc + ry} L{x0},{yc + ry} Z', KOPPAR, INK, 2)
    b += ellips(x0, yc, rx, ry, '#d99460', INK, 2) + ellips(x0, yc, rx * 0.7, ry * 0.7, LUFT, INK, 1.4)
    b += matt_h(x0, x1, yc + ry + 24, '1,50 m', under=True)
    b += tt(315, 182, 'sidan', 13, 'middle', GRA, True)
    return b


@fig('2.180', 400, 260, 'En metallkub med sidan 5,0 cm. Ett cylinderformat hål med diametern 2,0 cm är borrat rakt igenom från framsidan till baksidan.')
def _():
    x, y, s, dx, dy = 90, 70, 130, 56, 40
    b = lada(x, y, s, s, dx, dy, '#b8c2ca', '#d3dadf', '#9eaab4')
    cx, cy, r = x + s / 2, y + s / 2, 26
    b += ring(cx, cy, r, '#3d4a54', INK, 2)
    b += path(f'M{cx - r * 0.7:.1f},{cy - r * 0.7:.1f} A{r},{r} 0 0 1 {cx + r},{cy}', 'none', '#6b7a86', 2)
    b += matt_h(x, x + s, y + s + 22, '5,0 cm', under=True)
    b += pil(320, 64, cx + 20, cy - 16, GRA, 2, 8) + tt(324, 62, 'hål', 14, 'start', INK, True) + tt(324, 80, 'Ø 2,0 cm', 13, 'start')
    b += tt(324, 104, 'rakt igenom', 13, 'start', GRA)
    return b


@fig('2.181', 420, 220, 'Tvärsnitt av en kabel: en kopparkärna med diametern 2,0 cm och runt den ett 1,0 cm tjockt aluminiumskal.')
def _():
    cx, cy, rk, R = 120, 110, 40, 80
    b = ring(cx, cy, R, ALU) + ring(cx, cy, rk, KOPPAR)
    b += matt_h(cx - rk, cx + rk, cy + 6, '2,0 cm', under=True)
    b += linje(cx + rk, cy - 22, cx + R, cy - 22, GRA, 1.5) + linje(cx + rk, cy - 28, cx + rk, cy - 16, GRA, 1.5) + linje(cx + R, cy - 28, cx + R, cy - 16, GRA, 1.5)
    b += tt(cx + R + 6, cy - 17, '1,0 cm', 13, 'start', INK, halo=True)
    b += pil(268, 56, 166, 58, GRA, 2, 8) + tt(272, 58, 'aluminium', 14, 'start', INK, True) + tt(272, 76, '2,70 g/cm³', 13, 'start')
    b += pil(268, 150, 150, 122, GRA, 2, 8) + tt(272, 148, 'koppar', 14, 'start', INK, True) + tt(272, 166, '8,96 g/cm³', 13, 'start')
    b += tt(120, 212, 'kabeln är 1,0 km lång', 13, 'middle', GRA, True)
    return b


@fig('2.182', 340, 300, 'Ett slutet oljefat. Invändigt är det 85 cm högt och 57 cm i diameter. Plåten är 2,0 mm tjock.')
def _():
    cx, top, rx, ry, h = 140, 40, 70, 18, 180
    b = cylinder_v(cx, top, rx, ry, h, '#2f6fa3', '#4a87b8')
    for yk in (top + 60, top + 120):
        b += path(f'M{cx - rx},{yk} A{rx},{ry} 0 0 0 {cx + rx},{yk}', 'none', '#bcd3e6', 3)
    b += ellips(cx + 30, top, 9, 4, '#1d4a6e', INK, 1.4)
    b += matt_v(cx + rx + 22, top, top + h, '85 cm')
    b += matt_h(cx - rx, cx + rx, top + h + ry + 22, '57 cm', under=True)
    b += pil(290, 74, cx + rx + 2, 84, GRA, 2, 8) + tt(294, 70, 'plåt', 13, 'start', INK, True) + tt(294, 86, '2,0 mm', 13, 'start')
    return b


@fig('2.188', 440, 290, 'Ett mätglas med vätska står på en våg. Vid 87 ml visar vågen 132,4 g. Vid 13 ml visar vågen 49,6 g.')
def _():
    b = ''
    for x0, niva, visn in ((70, 87, '132,4 g'), (290, 13, '49,6 g')):
        g, _ = matglas(x0, niva, 100, 5, 20, vatska='#f6d7a7', H_=180, ybot=222, noll=False)
        b += g + vag(x0 + 32, 230, visn)
    b += tt(40, 26, 'ml', 13, 'middle', GRA)
    return b.replace('87,0 ml', '87 ml').replace('13,0 ml', '13 ml')


@fig('2.190', 450, 220, 'Samma glasflaska vägs tre gånger: tom 35,00 g, fylld med vatten 98,44 g och fylld med en okänd vätska 89,22 g.')
def _():
    b = ''
    for i, (fill, visn, namn) in enumerate(((None, '35,00 g', 'tom'), (VATTEN, '98,44 g', 'vatten'), ('#f3c6c6', '89,22 g', 'okänd vätska'))):
        cx = 75 + i * 150
        d = (f'M{cx - 30},150 L{cx - 30},96 C{cx - 30},80 {cx - 10},74 {cx - 8},62 L{cx - 8},40 L{cx + 8},40 L{cx + 8},62 '
             f'C{cx + 10},74 {cx + 30},80 {cx + 30},96 L{cx + 30},150 Z')
        b += path(d, GLAS, INK, 2)
        if fill:
            b += path(f'M{cx - 28},148 L{cx - 28},96 C{cx - 28},82 {cx - 10},76 {cx - 6},66 L{cx + 6},66 C{cx + 10},76 {cx + 28},82 {cx + 28},96 L{cx + 28},148 Z', fill, 'none', 0)
            b += linje(cx - 6, 66, cx + 6, 66, BLA, 2)
        b += vag(cx, 152, visn) + tt(cx, 216, namn, 14, 'middle', INK, True)
    return b


@fig('2.192', 300, 250, 'Ett cylindriskt mätglas med den inre diametern 3,0 cm. 40 ml vatten hälls i. Vattenytans höjd är okänd.')
def _():
    cx, top, rx, ry = 130, 40, 44, 10
    b = cylinder_v(cx, top, rx, ry, 170, GLAS)
    b += path(f'M{cx - rx + 2},120 L{cx - rx + 2},{top + 170} A{rx},{ry} 0 0 0 {cx + rx - 2},{top + 170} L{cx + rx - 2},120 Z', VATTEN, 'none', 0)
    b += ellips(cx, 120, rx - 2, ry - 1, '#b6d9ef', BLA, 1.6)
    b += ellips(cx, top, rx, ry, 'none', INK, 2)
    b += matt_h(cx - rx, cx + rx, top - 18, '3,0 cm')
    b += matt_v(cx + rx + 22, 120, top + 170, 'h = ?')
    b += tt(cx, 176, '40 ml', 14, 'middle', BLA, True, halo=True)
    return b


@fig('2.196', 440, 250, 'En bägare som väger 150 g tom står på en våg. I den hälls 200 ml vatten och en okänd volym etanol. Vågen visar 512 g.')
def _():
    b = path('M170,92 L178,198 L262,198 L270,92', GLAS, INK, 2)
    b += path('M175,130 L179,196 L261,196 L265,130 Z', '#d7ebf6', 'none', 0) + linje(175, 130, 265, 130, BLA, 2)
    b += vag(220, 200, '512 g') + tt(220, 92 - 8, 'bägare 150 g tom', 13, 'middle', GRA, True)
    b += path('M40,60 L40,120 L100,120 L100,60 Z', VATTEN, INK, 2) + tt(70, 140, 'vatten', 13, 'middle', INK, True) + tt(70, 156, '200 ml', 13)
    b += pil(104, 70, 168, 104, BLA, 2.4, 9)
    b += path('M360,50 L360,120 L400,120 L400,50 L392,50 L392,36 L368,36 L368,50 Z', '#fff3d6', INK, 2)
    b += tt(380, 140, 'etanol', 13, 'middle', INK, True) + tt(380, 156, '? ml', 13)
    b += pil(356, 70, 272, 104, ORA, 2.4, 9)
    return b


def _kula(R_px, r_px, r_text, R_text, okand_r):
    cx, cy = 130, 120
    b = ring(cx, cy, R_px, STAL) + ring(cx, cy, r_px, ALU)
    b += linje(cx, cy, cx + R_px, cy, INK, 1.6, '5 4') + cirkel(cx, cy, 3.5, INK, INK, 1)
    b += tt(cx + R_px + 6, cy + 5, R_text, 14, 'start', INK, True, halo=True)
    b += linje(cx, cy, cx - r_px, cy, INK, 1.6, '5 4')
    b += tt(cx - r_px / 2, cy - 8, r_text, 14, 'middle', INK, True, halo=True)
    b += pil(300, 50, cx + R_px * 0.55, cy - R_px * 0.72, GRA, 2, 8) + tt(304, 48, 'stål', 14, 'start', INK, True) + tt(304, 66, '7,80 g/cm³', 13, 'start')
    b += pil(300, 196, cx + r_px * 0.3, cy + r_px * 0.5, GRA, 2, 8) + tt(304, 200, 'aluminium', 14, 'start', INK, True) + tt(304, 218, '2,70 g/cm³', 13, 'start')
    return b


@fig('2.275', 430, 240, 'Genomskärning av en kula med en aluminiumkärna och ett stålskal. Ytterradien är 3,20 cm och kärnans radie är okänd.')
def _():
    return _kula(96, 62, 'r = ?', '3,20 cm', True)


@fig('2.277', 430, 240, 'Genomskärning av en kula med en aluminiumkärna och ett stålskal. Kärnans radie är hälften av ytterradien R.')
def _():
    return _kula(96, 48, 'R/2', 'R', False)


@fig('2.290', 380, 250, 'En ihålig stålkula med ytterradien 10,0 cm svävar helt under ytan i vatten. Innerradien är okänd.')
def _():
    b = rekt(30, 20, 320, 220, GLAS, INK, 2, 6) + f'<rect x="32" y="44" width="316" height="194" rx="4" fill="{VATTEN}"/>' + linje(32, 44, 348, 44, BLA, 2)
    cx, cy, R, r = 190, 140, 70, 60
    b += ring(cx, cy, R, STAL) + ring(cx, cy, r, LUFT, INK, 1.6)
    b += linje(cx, cy, cx + R, cy, INK, 1.6, '5 4') + cirkel(cx, cy, 3.5, INK, INK, 1)
    b += tt(cx + R + 6, cy + 5, '10,0 cm', 13, 'start', INK, True, halo=True)
    b += linje(cx, cy, cx - r, cy, INK, 1.6, '5 4') + tt(cx - r / 2, cy - 8, 'r = ?', 13, 'middle', INK, True, halo=True)
    b += tt(cx, cy + 34, 'luft', 13, 'middle', GRA)
    b += tt(60, 226, 'vatten', 13, 'start', BLA, True)
    return b


@fig('2.162', 440, 190, 'En stålplåt som är 4,00 m lång, 2,00 m bred och 2,00 cm tjock.')
def _():
    x, y, w, h, dx, dy = 50, 96, 280, 14, 70, 50
    b = lada(x, y, w, h, dx, dy, '#8a99a6', '#b4c0ca', '#7a8995')
    b += matt_h(x, x + w, y + h + 24, '4,00 m', under=True)
    b += linje(x + w + 12, y + h + 4, x + w + dx + 12, y + h - dy + 4, GRA, 1.5) + tt(x + w + dx / 2 + 22, y + h - dy / 2 + 14, '2,00 m', 14, 'start', INK, halo=True)
    b += pil(26, 60, x - 2, y + 4, GRA, 2, 8) + tt(22, 52, '2,00 cm tjock', 13, 'start', INK, True)
    return b


@fig('2.167', 440, 210, 'En bassäng som är 50 m lång, 25 m bred och 2,0 m djup och helt fylld med vatten.')
def _():
    x, y, w, h, dx, dy = 70, 90, 280, 40, 70, 56
    b = lada(x, y, w, h, dx, dy, '#9ccbe6', '#bfe0f2', '#86bcdb')
    for k in range(1, 6):
        t = k / 6
        b += linje(x + dx * t, y - dy * t, x + w + dx * t, y - dy * t, '#ffffff', 1.4, '8 6')
    b += matt_h(x, x + w, y + h + 22, '50 m', under=True)
    b += linje(x + w + 12, y + h + 4, x + w + dx + 12, y + h - dy + 4, GRA, 1.5) + tt(x + w + dx / 2 + 22, y + h - dy / 2 + 14, '25 m', 14, 'start', INK, halo=True)
    b += matt_v(x - 18, y, y + h, '2,0 m', vanster=True)
    return b


@fig('2.203', 460, 160, 'En 1,0 m lång stav med diametern 2,0 cm. De första 0,30 m är guld, nästa 0,40 m aluminium och de sista 0,30 m silver. x räknas från guldändan.')
def _():
    x0, L, cy, ry = 40, 380, 70, 16
    s = L / 1.0
    delar = ((0.0, 0.30, GULD, 'guld'), (0.30, 0.70, ALU, 'aluminium'), (0.70, 1.0, SILVER, 'silver'))
    b = ''
    for a, e, fill, namn in delar:
        b += rekt(x0 + a * s, cy - ry, (e - a) * s, 2 * ry, fill, INK, 1.8, 0) + tt(x0 + (a + e) / 2 * s, cy + 5, namn, 13, 'middle', INK, True)
    for a, e, *_ in delar:
        b += matt_h(x0 + a * s, x0 + e * s, cy - ry - 14, f'{e - a:.2f} m'.replace('.', ','))
    b += pil(x0, cy + ry + 30, x0 + 120, cy + ry + 30, ORA, 2.4, 9) + tt(x0 + 126, cy + ry + 35, 'x', 15, 'start', ORA, True, italic=True)
    b += linje(x0, cy + ry + 22, x0, cy + ry + 38, ORA, 2) + tt(x0, cy + ry + 56, '0', 13, 'middle', ORA, True)
    b += tt(x0 + L, cy + ry + 35, 'Ø 2,0 cm', 13, 'end', GRA, True)
    return b


# ---------------------------------------------------------------- inläggning
def efter_forsta_stycket(html, figur):
    i = html.index('</p>') + 4
    return html[:i] + figur + html[i:]


def nya_falt(q, figur):
    ut = {'t': efter_forsta_stycket(q['t'], figur)}
    if q.get('spelIntro'):
        ut['spelIntro'] = q['spelIntro'] + figur
    ut['delar'] = [efter_forsta_stycket(d['t'], figur) if d.get('t') else None for d in q.get('spelDelar') or []]
    return ut


def ersatt_i_objekt(src, uid, gammal, ny):
    start = src.index(f'"id": "{uid}",')
    slut = src.index('\n  }', start)
    obj = src[start:slut]
    g, n = json.dumps(gammal, ensure_ascii=False), json.dumps(ny, ensure_ascii=False)
    assert obj.count(g) >= 1, (uid, gammal[:60])
    return src[:start] + obj.replace(g, n) + src[slut:]


def main():
    src, bank = H.las(BANK)
    B = {q['id']: q for q in bank}
    andrade = []
    for uid, figur in F.items():
        q = B[uid]
        assert q['omr'] == 'densitet' and '<svg' not in q['t'] and '<svg' not in (q.get('spelIntro') or ''), uid
        nf = nya_falt(q, figur)
        src = ersatt_i_objekt(src, uid, q['t'], nf['t'])
        if 'spelIntro' in nf:
            src = ersatt_i_objekt(src, uid, q['spelIntro'], nf['spelIntro'])
        for d, ny in zip(q.get('spelDelar') or [], nf['delar']):
            if ny is not None and d['t'] != q['t']:
                src = ersatt_i_objekt(src, uid, d['t'], ny)
        q2 = dict(q, **{k: v for k, v in nf.items() if k != 'delar'})
        andrade.append(q2 | {'spelDelar': [dict(d, t=ny) if ny else d for d, ny in zip(q.get('spelDelar') or [], nf['delar'])]} if q.get('spelDelar') else q2)
    ny_bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    NB = {q['id']: q for q in ny_bank}
    for q in andrade:  # bara de avsedda fälten har ändrats
        gammal, ny = B[q['id']], NB[q['id']]
        assert set(gammal) == set(ny), q['id']
        for k in gammal:
            if k in ('t', 'spelIntro'):
                assert ny[k].replace(F[q['id']], '') == gammal[k], (q['id'], k)
            elif k == 'spelDelar':
                for dg, dn in zip(gammal[k], ny[k]):
                    assert {kk: v for kk, v in dn.items() if kk != 't'} == {kk: v for kk, v in dg.items() if kk != 't'}
                    assert dn.get('t', '').replace(F[q['id']], '') == dg.get('t', ''), q['id']
                    assert '<svg' in dn.get('t', '<svg'), q['id']
            else:
                assert gammal[k] == ny[k], (q['id'], k)
    assert len(ny_bank) == len(bank)
    print('figurer', len(F), sorted(F, key=lambda u: int(u.split('.')[1])))
    if '--ut' in sys.argv:
        Path(sys.argv[sys.argv.index('--ut') + 1]).write_text(json.dumps([NB[u] for u in F], ensure_ascii=False), encoding='utf-8')
    if '--skriv' in sys.argv:
        with open(H.ROOT / BANK, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src)


if __name__ == '__main__':
    main()
