"""Fysik 1 (uppgifter.js), kapitel 2: figurer i medelhastighet, mätnoggrannhet och enheter, 18 november 2026.

Fortsättning på tools/bygg-fy1-densitet-figurer-2026-11-18.py (samma regler, se agent/FY1_KAP2_FIGURER_2026-11-18.md).
Varje figur är ritad för sin uppgift. Den läggs efter första stycket i frågan (t), sist i spelIntro och efter
första stycket i varje delkort. Inga andra fält ändras. Okända storheter är markerade med ?.

  python tools/bygg-fy1-kap2-figurer-2026-11-18.py [--skriv] [--ut fil.json]
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import bankobjekt as B  # noqa: E402
from a_uppgifter_hjalp import svg, tt, linje, pil, rekt, cirkel, BLA, ORA, GRON, GRA, INK, ROD  # noqa: E402

_spec = importlib.util.spec_from_file_location('densfig', HERE / 'bygg-fy1-densitet-figurer-2026-11-18.py')
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)
path, ellips, ring, matt_h, matt_v, lada, cylinder_v = D.path, D.ellips, D.ring, D.matt_h, D.matt_v, D.lada, D.cylinder_v
VATTEN = D.VATTEN

ROOT = HERE.parent
BANK = 'uppgifter.js'
VAG, GRAS, HIMMEL = '#9aa4ab', '#cfe3c4', '#eaf4fb'
F = {}


def fig(uid, w, h, label):
    def dek(f):
        F[uid] = svg(w, h, f(), label)
        return f
    return dek


def gubbe(x, y, color=INK, s=1.0):
    """Enkel figur som står med fötterna i (x, y)."""
    h = 46 * s
    b = cirkel(x, y - h, 6 * s, color, color, 1)
    b += linje(x, y - h + 6 * s, x, y - 18 * s, color, 2.4) + linje(x, y - 18 * s, x - 7 * s, y, color, 2.4)
    b += linje(x, y - 18 * s, x + 7 * s, y, color, 2.4) + linje(x - 9 * s, y - 32 * s, x + 9 * s, y - 32 * s, color, 2.4)
    return b


def bil(x, y, fill, w=54):
    """Bil sedd från sidan, hjulen står på y."""
    b = path(f'M{x},{y - 8} L{x},{y - 20} L{x + w * 0.22},{y - 20} L{x + w * 0.34},{y - 32} L{x + w * 0.7},{y - 32} '
             f'L{x + w * 0.82},{y - 20} L{x + w},{y - 20} L{x + w},{y - 8} Z', fill, INK, 1.8)
    return b + cirkel(x + w * 0.22, y - 6, 6, INK, '#fff', 1.5) + cirkel(x + w * 0.78, y - 6, 6, INK, '#fff', 1.5)


def flagga(x, y, text):
    b = linje(x, y, x, y - 34, INK, 2) + path(f'M{x},{y - 34} L{x + 18},{y - 28} L{x},{y - 22} Z', ROD, INK, 1.2)
    return b + tt(x + 10, y - 40, text, 13, 'middle', INK, True)


# ================================================================ medelhastighet
@fig('3.9', 440, 220, 'En cyklist cyklar 2,0 km uppför en backe med farten 12 km/h och sedan samma väg ner igen med farten 28 km/h.')
def _():
    b = path('M30,190 L410,190 L410,70 Z', GRAS, INK, 2)
    ux, uy = 380 / math.hypot(380, 120), -120 / math.hypot(380, 120)
    nx, ny = uy, -ux  # normal uppåt till vänster om backen
    def langs(t, d):
        return 30 + ux * t + nx * d, 190 + uy * t + ny * d
    x1, y1 = langs(90, 18); x2, y2 = langs(290, 18)
    b += pil(x1, y1, x2, y2, BLA, 3)
    x1, y1 = langs(290, 46); x2, y2 = langs(90, 46)
    b += pil(x1, y1, x2, y2, ORA, 3)
    b += tt(150, 70, 'nedför 28 km/h', 14, 'middle', ORA, True, halo=True)
    b += tt(300, 170, 'uppför 12 km/h', 14, 'middle', BLA, True, halo=True)
    b += tt(330, 140, '2,0 km', 14, 'middle', INK, True, halo=True)
    return b


@fig('3.51', 440, 170, 'En person går 32 m österut och sedan 14 m västerut längs samma raka gång. Hela förloppet tar 24 s.')
def _():
    x0, k = 60, 9.0
    b = rekt(30, 96, 380, 14, '#e8e2d4', '#b7ad97', 1.5, 3) + gubbe(x0, 94)
    b += linje(x0, 86, x0, 120, GRA, 1.5, '4 3') + tt(x0, 136, 'start', 13, 'middle', GRA, True)
    b += pil(x0, 50, x0 + 32 * k, 50, BLA, 3) + tt(x0 + 16 * k, 40, '32 m österut', 14, 'middle', BLA, True)
    b += pil(x0 + 32 * k, 72, x0 + 18 * k, 72, ORA, 3) + tt(x0 + 25 * k, 90, '14 m västerut', 13, 'middle', ORA, True, halo=True)
    b += linje(x0 + 32 * k, 44, x0 + 32 * k, 78, GRA, 1.2, '3 3')
    b += pil(370, 150, 410, 150, INK, 2, 8) + tt(366, 155, 'öster', 13, 'end', INK)
    b += tt(220, 158, 'tid totalt: 24 s', 13, 'middle', GRA, True)
    return b


@fig('3.97', 440, 200, 'Två bilar kör samma sträcka. Bil 1 håller 100 km/h hela vägen. Bil 2 kör första halvan i 80 km/h och andra halvan i 120 km/h.')
def _():
    b = ''
    for y, namn in ((70, 'bil 1'), (150, 'bil 2')):
        b += rekt(50, y, 360, 16, VAG, INK, 1.5, 2) + linje(54, y + 8, 406, y + 8, '#fff', 1.5, '10 8')
        b += tt(44, y + 13, namn, 13, 'end', INK, True)
    b += bil(56, 68, '#5b9bd5') + bil(56, 148, '#e07a5f')
    b += tt(230, 52, '100 km/h hela vägen', 14, 'middle', BLA, True)
    b += linje(230, 124, 230, 172, INK, 1.6, '5 4') + tt(230, 196, 'halva sträckan', 12, 'middle', GRA)
    b += tt(140, 134, '80 km/h', 14, 'middle', ORA, True) + tt(320, 134, '120 km/h', 14, 'middle', ORA, True)
    b += flagga(410, 70, 'mål') + flagga(410, 150, 'mål')
    return b


@fig('3.125', 440, 214, 'En båt ska ta sig 850 m längs en flod. Strömmen är 1,3 m/s. Båten går 4,2 m/s i stilla vatten.')
def _():
    b = rekt(0, 40, 440, 18, GRAS, 'none', 0, 0) + rekt(0, 150, 440, 18, GRAS, 'none', 0, 0)
    b += f'<rect x="0" y="58" width="440" height="92" fill="{VATTEN}"/>'
    for x in (40, 160):
        b += pil(x, 132, x + 60, 132, '#5b8fb0', 2, 8)
    b += tt(250, 138, 'ström 1,3 m/s', 13, 'start', '#3d6d8c', True, halo=True)
    b += path('M150,86 L230,86 L246,100 L230,114 L150,114 Z', '#f4f1e8', INK, 2)
    b += tt(196, 104, '4,2 m/s', 12, 'middle', INK, True)
    b += tt(330, 86, 'medströms →', 13, 'start', BLA, True) + tt(110, 86, '← motströms', 13, 'end', ORA, True)
    b += matt_h(40, 400, 200, '850 m')
    b += tt(220, 30, '4,2 m/s gäller i stilla vatten', 12, 'middle', GRA)
    return b


@fig('3.130', 440, 200, 'En person står 85 m från en vertikal klippvägg och klappar i händerna. Ekot hörs 0,50 s senare.')
def _():
    b = rekt(0, 160, 440, 40, GRAS, 'none', 0, 0) + linje(0, 160, 440, 160, '#6f9a5b', 2)
    b += path('M360,160 L366,40 L392,26 L440,22 L440,160 Z', '#a39b8f', INK, 2)
    b += gubbe(60, 160)
    for r in (14, 24):
        b += path(f'M{80 + r * 0.2},{120 - r * 0.6} A{r},{r} 0 0 1 {80 + r * 0.2},{120 + r * 0.6}', 'none', BLA, 1.8)
    b += pil(110, 100, 352, 100, BLA, 2.4, 9) + tt(230, 92, 'ljudet', 13, 'middle', BLA, True)
    b += pil(352, 124, 110, 124, ORA, 2.4, 9) + tt(230, 142, 'ekot', 13, 'middle', ORA, True, halo=True)
    b += matt_h(60, 362, 184, '85 m', under=False)
    b += tt(220, 26, 'ekot hörs 0,50 s efter klappen', 13, 'middle', INK, True)
    return b


@fig('3.133', 460, 170, 'Ett 100-meterslopp med splittider: 0–30 m på 4,20 s, 30–60 m på 2,70 s och 60–100 m på 3,80 s.')
def _():
    x0, k = 40, 3.8
    b = rekt(x0, 70, 100 * k, 40, '#d9734e', INK, 1.5, 0)
    for y in (82, 98):
        b += linje(x0, y, x0 + 100 * k, y, '#fff', 1.4)
    for m in (0, 30, 60, 100):
        b += linje(x0 + m * k, 60, x0 + m * k, 120, INK, 2.4) + tt(x0 + m * k, 52, f'{m} m', 13, 'middle', INK, True)
    for a, e, t in ((0, 30, '4,20 s'), (30, 60, '2,70 s'), (60, 100, '3,80 s')):
        b += matt_h(x0 + a * k + 3, x0 + e * k - 3, 138, t, under=True)
    b += gubbe(x0 + 10, 108, INK, 0.8)
    return b


@fig('3.234', 460, 220, 'En 90 m lång rullgång rör sig åt höger med 0,80 m/s. En person går 1,20 m/s relativt rullgången, först med rullgången och sedan tillbaka.')
def _():
    b = rekt(40, 120, 380, 22, '#5d6b75', INK, 2, 10)
    for x in range(56, 410, 22):
        b += linje(x, 124, x, 138, '#8a98a3', 1.5)
    b += pil(150, 184, 310, 184, GRA, 2.6, 9) + tt(230, 208, 'rullgången u = 0,80 m/s', 13, 'middle', INK, True)
    b += gubbe(90, 120, BLA)
    b += pil(120, 56, 400, 56, BLA, 2.6, 9) + tt(260, 46, 'dit: med rullgången', 13, 'middle', BLA, True)
    b += pil(400, 82, 120, 82, ORA, 2.6, 9) + tt(260, 100, 'tillbaka: mot rullgången', 13, 'middle', ORA, True, halo=True)
    b += tt(450, 20, 'v = 1,20 m/s relativt rullgången', 12, 'end', GRA)
    b += matt_h(40, 420, 154, '90 m', under=True, size=13)
    return b


@fig('3.103', 440, 210, 'En blixt slår ner långt bort. Du ser blixten och hör åskan 6,0 sekunder senare. Avståndet är okänt.')
def _():
    b = rekt(0, 0, 440, 160, '#38475a', 'none', 0, 0) + rekt(0, 160, 440, 50, '#5f7a52', 'none', 0, 0)
    b += path('M60,10 L96,10 L80,62 L104,62 L58,154 L70,86 L46,86 Z', '#ffd84d', '#c9a400', 1.5)
    b += gubbe(390, 168, '#fff')
    b += pil(110, 70, 370, 110, '#ffe680', 2, 8) + tt(240, 74, 'ljus', 13, 'middle', '#ffe680', True)
    b += pil(110, 132, 370, 132, '#9fd3ff', 2, 8) + tt(240, 150, 'ljud 340 m/s', 13, 'middle', '#9fd3ff', True)
    b += linje(80, 190, 390, 190, '#fff', 1.5) + linje(80, 184, 80, 196, '#fff', 1.5) + linje(390, 184, 390, 196, '#fff', 1.5)
    b += tt(235, 204, 'avstånd ?', 13, 'middle', '#fff', True)
    b += tt(430, 30, 'åskan hörs', 12, 'end', '#fff') + tt(430, 46, '6,0 s efter blixten', 12, 'end', '#fff')
    return b


@fig('3.236', 460, 190, 'En resa på 180 km: 90 km i 90 km/h, sedan ett stopp på 12 minuter och därefter 90 km till.')
def _():
    b = rekt(30, 80, 190, 16, VAG, INK, 1.5, 2) + rekt(250, 80, 190, 16, VAG, INK, 1.5, 2)
    b += linje(34, 88, 216, 88, '#fff', 1.5, '10 8') + linje(254, 88, 436, 88, '#fff', 1.5, '10 8')
    b += cirkel(235, 88, 15, ROD, '#fff', 2) + tt(235, 93, 'P', 14, 'middle', '#fff', True)
    b += tt(235, 128, 'stopp 12 min', 13, 'middle', ROD, True)
    b += tt(125, 70, '90 km i 90 km/h', 14, 'middle', BLA, True) + tt(345, 70, '90 km i ? km/h', 14, 'middle', ORA, True)
    b += matt_h(30, 440, 176, '180 km, önskad medelfart 100 km/h', under=False, size=13)
    return b


@fig('3.235', 460, 150, 'En sträcka delad i tre delar: en fjärdedel körs i 50 km/h, en tredjedel i 80 km/h och resten med farten v.')
def _():
    x0, L = 30, 400
    delar = ((0, 1 / 4, '#9cc3e4', '¼ av sträckan', '50 km/h'), (1 / 4, 1 / 4 + 1 / 3, '#f2c48d', '⅓ av sträckan', '80 km/h'),
             (1 / 4 + 1 / 3, 1.0, '#c6e2b5', 'resten', 'v = ?'))
    b = ''
    for a, e, fill, namn, fart in delar:
        b += rekt(x0 + a * L, 60, (e - a) * L, 34, fill, INK, 1.6, 0)
        b += tt(x0 + (a + e) / 2 * L, 82, fart, 14, 'middle', INK, True)
        b += tt(x0 + (a + e) / 2 * L, 48, namn, 13, 'middle', GRA, True)
    b += tt(230, 130, 'medelfart över hela sträckan: 75 km/h', 14, 'middle', INK, True)
    return b


@fig('3.101', 400, 300, 'En satellit går i en cirkelbana 700 km över jordytan med farten 7,5 km/s. Jordens radie är 6371 km.')
def _():
    cx, cy, R, h = 170, 160, 92, 40
    b = f'<circle cx="{cx}" cy="{cy}" r="{R + h}" fill="none" stroke="{GRA}" stroke-width="1.6" stroke-dasharray="6 5"/>'
    b += ring(cx, cy, R, '#7fb3d5') + tt(cx, cy - R / 2, 'jorden', 14, 'middle', '#1f4e6e', True)
    b += linje(cx, cy, cx + R, cy, INK, 1.6, '5 4') + cirkel(cx, cy, 3.5, INK, INK, 1)
    b += tt(cx + R / 2, cy - 8, '6371 km', 13, 'middle', INK, True, halo=True)
    b += linje(cx + R, cy, cx + R + h, cy, ROD, 2) + tt(cx + R + h + 14, cy + 26, '700 km', 13, 'start', ROD, True, halo=True)
    sx, sy = cx + R + h, cy
    b += rekt(sx - 8, sy - 8, 16, 16, '#d9dde1', INK, 1.6, 2) + linje(sx - 20, sy, sx + 20, sy, '#3a6ea5', 4)
    b += pil(sx, sy - 14, sx, sy - 80, BLA, 2.6, 9) + tt(sx + 8, sy - 60, '7,5 km/s', 13, 'start', BLA, True)
    return b


@fig('2.296', 440, 170, 'Lars cyklar hemifrån till affären med 12 km/h, handlar i 15 minuter och cyklar hem med 9,0 km/h. Han är borta 50 minuter.')
def _():
    b = path('M40,96 L40,70 L64,50 L88,70 L88,96 Z', '#f2dcb3', INK, 2) + tt(64, 116, 'hemma', 13, 'middle', INK, True)
    b += rekt(350, 58, 64, 38, '#cfe6f5', INK, 2, 2) + rekt(344, 50, 76, 12, ROD, INK, 1.5, 2) + tt(382, 116, 'affären', 13, 'middle', INK, True)
    b += tt(382, 134, 'handlar 15 min', 12, 'middle', GRA)
    b += pil(100, 66, 338, 66, BLA, 2.6, 9) + tt(219, 56, 'dit 12 km/h', 14, 'middle', BLA, True)
    b += pil(338, 88, 100, 88, ORA, 2.6, 9) + tt(219, 106, 'hem 9,0 km/h', 14, 'middle', ORA, True, halo=True)
    b += matt_h(64, 382, 156, 'avstånd ?', under=False, size=13)
    b += tt(220, 22, 'borta totalt 50 min', 13, 'middle', INK, True)
    return b


@fig('2.304', 440, 190, 'Ett slag på ena änden av en 5,00 m lång järnstång. Ljudet når en mikrofon i andra änden först genom järnet och sedan genom luften, med 13,7 ms mellanrum.')
def _():
    b = rekt(60, 120, 320, 12, '#8c969e', INK, 1.8, 2)
    b += rekt(26, 96, 18, 40, '#b07f45', INK, 1.5, 2) + rekt(14, 88, 42, 14, '#5d6b75', INK, 1.5, 2)
    b += rekt(388, 112, 16, 28, '#3d4a54', INK, 1.5, 6) + linje(396, 140, 396, 168, INK, 2)
    b += tt(396, 104, 'mikrofon', 12, 'middle', INK, True)
    b += pil(70, 146, 376, 146, GRA, 2.4, 9) + tt(223, 164, 'genom järnet (först)', 13, 'middle', INK, True)
    b += pil(70, 82, 376, 82, BLA, 2.4, 9) + tt(223, 72, 'genom luften 340 m/s (sedan)', 13, 'middle', BLA, True)
    b += matt_h(60, 380, 30, '5,00 m') + tt(20, 184, 'ljuden når mikrofonen med 13,7 ms mellanrum', 13, 'start', ORA, True)
    return b


@fig('2.313', 460, 206, 'Ett båtrace på 2,0 km. Båt A kör 4,0 m/s de första 1 500 m och 3,1 m/s resten. Båt B kör 3,6 m/s de första 1 200 m och 3,9 m/s resten.')
def _():
    x0, k = 50, 0.19
    b = f'<rect x="{x0}" y="40" width="{2000 * k:.1f}" height="120" fill="{VATTEN}"/>'
    for y, namn, s1, v1, v2, fill in ((60, 'A', 1500, '4,0 m/s', '3,1 m/s', '#e07a5f'), (120, 'B', 1200, '3,6 m/s', '3,9 m/s', '#5b9bd5')):
        b += rekt(x0, y, s1 * k, 22, fill, INK, 1.4, 0) + rekt(x0 + s1 * k, y, (2000 - s1) * k, 22, fill, INK, 1.4, 0)
        b += f'<rect x="{x0 + s1 * k:.1f}" y="{y}" width="{(2000 - s1) * k:.1f}" height="22" fill="#fff" fill-opacity="0.45"/>'
        b += tt(x0 - 8, y + 16, namn, 15, 'end', INK, True)
        b += tt(x0 + s1 * k / 2, y + 16, v1, 13, 'middle', INK, True) + tt(x0 + (s1 + 2000) / 2 * k, y + 16, v2, 13, 'middle', INK, True)
        b += tt(x0 + s1 * k, y - 4, f'{s1:,} m'.replace(',', ' '), 11, 'middle', GRA)
    b += matt_h(x0, x0 + 2000 * k, 194, '2,0 km', under=False)
    return b


@fig('2.320', 460, 190, 'En boj sänder ljudpulser var 5,0 s. Ljudet går 1 500 m/s i vattnet. En ubåt kör mot bojen med 40 km/h.')
def _():
    b = f'<rect x="0" y="40" width="460" height="150" fill="{VATTEN}"/>' + linje(0, 40, 460, 40, BLA, 2)
    b += path('M40,40 L40,22 L56,22 L56,40 Z', ROD, INK, 1.5) + linje(48, 40, 48, 70, INK, 1.5) + cirkel(48, 74, 6, '#ffd84d', INK, 1.5)
    for r in (70, 150, 230):
        b += path(f'M{48 + r * 0.6},{74 - r * 0.25} A{r},{r} 0 0 1 {48 + r * 0.6},{74 + r * 0.45}', 'none', BLA, 2)
    b += tt(240, 180, 'pulser var 5,0 s, 1 500 m/s', 13, 'start', '#2b5e80', True, halo=True)
    b += path('M340,120 C340,106 360,100 400,100 C430,100 446,108 446,120 C446,132 430,140 400,140 C360,140 340,134 340,120 Z', '#4a5864', INK, 2)
    b += rekt(380, 88, 20, 14, '#4a5864', INK, 1.6, 2)
    b += pil(334, 120, 270, 120, ORA, 3) + tt(300, 108, '40 km/h', 13, 'middle', ORA, True, halo=True)
    return b


# ================================================================ mätnoggrannhet (matnogg)
@fig('2.234', 360, 170, 'En digital våg med en vikt på vågskålen. Displayen visar 83,42 g.')
def _():
    b = rekt(80, 60, 200, 16, '#c9d3da', INK, 1.8, 4) + rekt(70, 76, 220, 74, '#e9eef2', INK, 2, 10)
    b += rekt(120, 90, 120, 40, '#1f2d36', INK, 1.5, 4) + tt(180, 118, '83,42 g', 22, 'middle', '#9ff0b4', True)
    b += path('M150,60 L156,30 L204,30 L210,60 Z', '#b9a07a', INK, 1.8)
    return b


@fig('2.15', 460, 220, 'Två sätt att mäta pappersarkets tjocklek: ett ark i ett skjutmått, 0,10 mm, eller en bunt med 500 ark, 52 mm.')
def _():
    b = rekt(30, 60, 170, 14, '#c9d0d5', INK, 1.6, 2) + rekt(30, 74, 14, 60, '#c9d0d5', INK, 1.6, 0)
    b += rekt(70, 74, 14, 60, '#c9d0d5', INK, 1.6, 0) + rekt(70, 56, 46, 22, '#e9eef2', INK, 1.4, 2)
    b += rekt(44, 92, 26, 4, '#ffffff', INK, 1, 0)
    for x in range(90, 196, 8):
        b += linje(x, 60, x, 66 if (x - 90) % 40 else 70, INK, 1)
    b += tt(115, 160, 'ett ark', 14, 'middle', INK, True) + tt(115, 178, '0,10 ± 0,02 mm', 13)
    for i in range(14):
        y = 70 + i * 5
        b += rekt(250, y, 110, 5, '#ffffff' if i % 2 else '#f4f1e8', '#b7ad97', 0.8, 0)
    b += linje(372, 70, 372, 140, GRA, 1.5) + linje(366, 70, 378, 70, GRA, 1.5) + linje(366, 140, 378, 140, GRA, 1.5)
    b += tt(390, 110, '52 ± 1 mm', 14, 'start', INK)
    b += tt(305, 160, 'bunt med 500 ark', 14, 'middle', INK, True)
    b += tt(115, 34, 'metod a', 13, 'middle', GRA, True) + tt(305, 34, 'metod b', 13, 'middle', GRA, True)
    return b


@fig('2.243', 360, 220, 'En pendel svänger fram och tillbaka. Tiden för 10 svängningar mäts med ett tidtagarur till 14,8 s.')
def _():
    b = rekt(40, 20, 160, 10, '#8c969e', INK, 1.6, 2)
    b += path('M120,30 L84,150', 'none', INK, 1.6) + ring(84, 150, 13, '#e07a5f')
    b += path('M120,30 L156,150', 'none', GRA, 1.2, ' stroke-dasharray="4 4"') + ring(156, 150, 13, 'none', GRA, 1.2)
    b += path('M80,176 A130,130 0 0 0 160,176', 'none', BLA, 2) + pil(150, 178, 162, 175, BLA, 2, 7)
    b += ring(280, 110, 44, '#f7fafc') + rekt(272, 56, 16, 12, '#8c969e', INK, 1.4, 2)
    b += tt(280, 116, '14,8 s', 18, 'middle', INK, True) + tt(280, 180, '10 svängningar', 14, 'middle', INK, True)
    return b


@fig('2.245', 360, 170, 'En personvåg vars display visar 72,40 kg. Vågen visar alltid 0,20 kg för mycket.')
def _():
    b = rekt(90, 30, 180, 120, '#dfe6ec', INK, 2, 22) + rekt(130, 44, 100, 34, '#1f2d36', INK, 1.5, 4)
    b += tt(180, 68, '72,40 kg', 18, 'middle', '#9ff0b4', True)
    b += path('M128,96 C128,90 150,88 158,96 L156,136 C150,142 132,142 128,134 Z', '#c9d3da', INK, 1.2)
    b += path('M232,96 C232,90 210,88 202,96 L204,136 C210,142 228,142 232,134 Z', '#c9d3da', INK, 1.2)
    b += tt(180, 166, 'visar alltid 0,20 kg för mycket', 13, 'middle', ROD, True)
    return b


@fig('2.251', 440, 150, 'Två lägen på en mätlinje: 1,4 m och 8,62 m från nollpunkten. Avståndet mellan dem är okänt.')
def _():
    x0, k = 30, 38
    b = pil(x0, 70, x0 + 10.4 * k, 70, INK, 1.8, 9)
    for m in range(0, 11):
        b += linje(x0 + m * k, 64, x0 + m * k, 76, INK, 1.4) + tt(x0 + m * k, 94, str(m), 12, 'middle', GRA)
    b += tt(x0 + 10.4 * k + 4, 74, 'm', 13, 'start', GRA)
    for v, namn in ((1.4, '1,4 m'), (8.62, '8,62 m')):
        b += cirkel(x0 + v * k, 70, 6, ORA, '#fff', 1.5) + tt(x0 + v * k, 52, namn, 13, 'middle', ORA, True)
    b += matt_h(x0 + 1.4 * k, x0 + 8.62 * k, 134, 'avstånd ?', under=False, size=13)
    return b


@fig('2.255', 330, 250, 'En cylinder med radien 2,50 ± 0,02 cm och höjden 10,0 ± 0,1 cm.')
def _():
    cx, top, rx, ry, h = 120, 40, 50, 14, 170
    b = cylinder_v(cx, top, rx, ry, h, '#cfe0ec', '#e3eef5')
    b += linje(cx, top, cx + rx, top, INK, 1.6, '5 4') + cirkel(cx, top, 3, INK, INK, 1)
    b += tt(cx + rx / 2, top - ry - 5, 'r', 15, 'middle', INK, True)
    b += matt_v(cx + rx + 20, top, top + h, 'h = 10,0 ± 0,1 cm', size=13)
    b += tt(120, 240, 'r = 2,50 ± 0,02 cm', 13, 'middle', INK, True)
    return b


def termometer(x, y_topp, niva, text, fill=ROD):
    """Termometer med vätskepelare; niva 0..1 av skalan."""
    h = 120
    b = rekt(x - 7, y_topp, 14, h, '#f7fafc', INK, 1.6, 7) + ring(x, y_topp + h + 8, 11, fill)
    b += rekt(x - 3, y_topp + h * (1 - niva), 6, h * niva + 4, fill, 'none', 0, 2)
    return b + tt(x, y_topp - 8, text, 13, 'middle', INK, True, halo=True)


@fig('2.258', 460, 230, 'En termometer visar 0,8 °C i smältande is och 100,6 °C i kokande vatten. Vilken verklig temperatur motsvarar avläsningen 50,7 °C?')
def _():
    b = path('M30,120 L38,200 L118,200 L126,120', '#e3f1fa', INK, 2)
    for (x, y) in ((50, 160), (80, 172), (96, 148), (60, 186)):
        b += rekt(x, y, 18, 16, '#ffffff', '#8fb7d0', 1.2, 3)
    b += termometer(78, 48, 0.12, 'visar 0,8 °C') + tt(78, 220, 'smältande is (0 °C)', 12, 'middle', GRA, True)
    b += path('M180,120 L188,200 L268,200 L276,120', VATTEN, INK, 2)
    for x in (204, 228, 250):
        b += cirkel(x, 186, 4, '#ffffff', BLA, 1)
    b += termometer(228, 48, 0.9, 'visar 100,6 °C') + tt(228, 220, 'kokande vatten (100 °C)', 12, 'middle', GRA, True)
    b += termometer(380, 48, 0.5, 'visar 50,7 °C') + tt(380, 220, 'verklig temperatur ?', 12, 'middle', ORA, True)
    return b


@fig('2.269', 440, 170, 'En tunn tråd är lindad 40 täta varv runt en penna. Lindningens totala bredd är 12,6 ± 0,1 mm.')
def _():
    b = path('M20,70 L330,70 L360,85 L330,100 L20,100 Z', '#f2c94c', INK, 1.8) + path('M330,70 L360,85 L330,100 Z', '#f2dcb3', INK, 1.4)
    b += rekt(20, 70, 22, 30, '#e8a0a0', INK, 1.4, 0)
    x1, n = 100, 40
    for i in range(n):
        x = x1 + i * 4.5
        b += f'<line x1="{x:.1f}" y1="66" x2="{x + 2:.1f}" y2="104" stroke="#b5651d" stroke-width="2.6"/>'
    x2 = x1 + n * 4.5
    b += matt_h(x1, x2, 132, '12,6 ± 0,1 mm', under=True)
    b += tt((x1 + x2) / 2, 52, '40 varv', 14, 'middle', '#8a4a12', True)
    return b


@fig('2.49', 440, 230, 'Ett bägarglas med vatten på en våg som visar hela gram. Vid start visar vågen 312 g och efter 30 minuter 309 g.')
def _():
    b = ''
    for cx, visn, namn, niva in ((110, '312 g', 'vid start', 92), (330, '309 g', 'efter 30 min', 98)):
        b += path(f'M{cx - 44},70 L{cx - 38},168 L{cx + 38},168 L{cx + 44},70', '#f7fafc', INK, 2)
        b += path(f'M{cx - 42},{niva} L{cx - 37},166 L{cx + 37},166 L{cx + 42},{niva} Z', VATTEN, 'none', 0) + linje(cx - 42, niva, cx + 42, niva, BLA, 2)
        b += D.vag(cx, 170, visn) + tt(cx, 50, namn, 14, 'middle', INK, True)
    b += pil(190, 120, 250, 120, GRA, 2.4, 9) + tt(220, 108, '30 min', 12, 'middle', GRA, True)
    return b


@fig('2.45', 460, 190, 'En granstam som modelleras som en cylinder. Omkretsen är 1,45 ± 0,02 m och längden 12,0 ± 0,3 m.')
def _():
    x0, x1, cy, ry, rx = 70, 400, 90, 40, 16
    b = path(f'M{x0},{cy - ry} L{x1},{cy - ry} A{rx},{ry} 0 0 1 {x1},{cy + ry} L{x0},{cy + ry} Z', '#8b5a2b', INK, 2)
    for y in (cy - 22, cy - 4, cy + 16):
        b += path(f'M{x0 + 30},{y} C{x0 + 120},{y - 4} {x0 + 220},{y + 5} {x1 - 20},{y - 2}', 'none', '#6d4420', 1.4)
    b += ellips(x0, cy, rx, ry, '#e2b77a', INK, 2)
    for r in (8, 18, 28):
        b += ellips(x0, cy, rx * r / 40, r, 'none', '#b07f45', 1.1)
    b += path(f'M{x0 + 40},{cy - ry} A{rx},{ry} 0 0 1 {x0 + 40},{cy + ry}', 'none', ORA, 3)
    b += tt(x0 + 52, cy + ry + 22, 'omkrets 1,45 ± 0,02 m', 13, 'start', ORA, True)
    b += matt_h(x0, x1, cy - ry - 18, 'längd 12,0 ± 0,3 m')
    return b


@fig('2.271', 440, 222, 'Metod A: en cirkulär skivas diameter mäts till 120,0 ± 0,5 mm. Metod B: skivans kontur ritas på rutpapper.')
def _():
    b = ring(110, 112, 70, '#f2c48d') + linje(40, 112, 180, 112, INK, 1.6, '5 4')
    b += tt(110, 104, 'd = 120,0 ± 0,5 mm', 12, 'middle', INK, True, halo=True) + tt(110, 212, 'metod A', 13, 'middle', GRA, True)
    for i in range(0, 161, 10):
        b += linje(250 + i, 32, 250 + i, 192, '#bcd6e8', 1) + linje(250, 32 + i, 410, 32 + i, '#bcd6e8', 1)
    b += f'<circle cx="330" cy="112" r="70" fill="#f2c48d" fill-opacity="0.45" stroke="{INK}" stroke-width="2"/>'
    b += tt(330, 212, 'metod B: rutpapper', 13, 'middle', GRA, True)
    return b


# ---------------------------------------------------------------- inläggning
def efter_forsta_stycket(html, figur):
    i = html.index('</p>') + 4
    return html[:i] + figur + html[i:]


def med_figur(q, figur):
    q = json.loads(json.dumps(q))
    q['t'] = efter_forsta_stycket(q['t'], figur)
    if q.get('spelIntro'):
        q['spelIntro'] = q['spelIntro'] + figur
    for d in q.get('spelDelar') or []:
        if d.get('t'):
            d['t'] = efter_forsta_stycket(d['t'], figur)
    return q


def main():
    src, bank = B.las(ROOT / BANK)
    Q = {q['id']: q for q in bank}
    nya = {}
    klara = {uid for uid, figur in F.items() if figur in Q[uid]['t']}
    for uid, figur in F.items():
        if uid in klara:
            continue
        q = Q[uid]
        assert q['omr'] in ('medelhastighet', 'matnogg', 'enheter'), uid
        assert '<svg' not in q['t'] and '<svg' not in (q.get('spelIntro') or ''), uid
        nya[uid] = med_figur(q, figur)
        for d in nya[uid].get('spelDelar') or []:
            assert '<svg' in d.get('t', '<svg'), uid
    assert not B.kontrollera_rundresa(ROOT / BANK, set(nya))
    ny_src = B.ersatt(src, nya)
    ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    assert [q['id'] for q in ny_bank] == [q['id'] for q in bank]
    for ny, gammal in zip(ny_bank, bank):  # bara figuren har lagts till
        if ny['id'] not in nya:
            assert ny == gammal
            continue
        fg = F[ny['id']]
        assert set(ny) == set(gammal)
        for k in gammal:
            if k in ('t', 'spelIntro'):
                assert ny[k].replace(fg, '', 1) == gammal[k], (ny['id'], k)
            elif k == 'spelDelar':
                for dn, dg in zip(ny[k], gammal[k]):
                    assert {a: v for a, v in dn.items() if a != 't'} == {a: v for a, v in dg.items() if a != 't'}
                    assert dn.get('t', '').replace(fg, '', 1) == dg.get('t', ''), ny['id']
            else:
                assert ny[k] == gammal[k], (ny['id'], k)
    print('figurer', len(F), 'redan inlagda', len(klara), 'nya', list(nya))
    if '--ut' in sys.argv:
        Path(sys.argv[sys.argv.index('--ut') + 1]).write_text(json.dumps([q for q in ny_bank if q['id'] in nya], ensure_ascii=False), encoding='utf-8')
    if '--skriv' in sys.argv:
        B.skriv(ROOT / BANK, ny_src)


if __name__ == '__main__':
    main()
