"""Fysik 1 (uppgifter.js), kapitel 3 Rörelse: figurer i uppgifter som saknade figur, 19 november 2026.

Fortsättning på kapitel 2 (tools/bygg-fy1-kap2-figurer-2026-11-18.py, agent/FY1_KAP2_FIGURER_2026-11-18.md), med
samma regler. Varje figur är ritad för sin uppgift. Den läggs efter första stycket i frågan (t), sist i spelIntro och
efter första stycket i varje delkort. Delkort med egna, avskalade texter får figuren bara när de har samma data
(`KORT`). Inga andra fält ändras. Okända storheter markeras med ?. Riktningsval (”positiv riktning”) skrivs inte i
figuren, eftersom de bara står i kgInstruktion (språkomskrivningen 2026-11-18). Se agent/FY1_KAP3_FIGURER_2026-11-19.md.

  python tools/bygg-fy1-kap3-figurer-2026-11-19.py [--skriv] [--ut fil.json]
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


def _ladda(namn, fil):
    spec = importlib.util.spec_from_file_location(namn, HERE / fil)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K2 = _ladda('kap2fig', 'bygg-fy1-kap2-figurer-2026-11-18.py')
D = K2.D
path, ellips, ring, matt_h, matt_v, lada = D.path, D.ellips, D.ring, D.matt_h, D.matt_v, D.lada
gubbe, bil, flagga, VAG, GRAS = K2.gubbe, K2.bil, K2.flagga, K2.VAG, K2.GRAS
VATTEN = D.VATTEN

ROOT = HERE.parent
BANK = 'uppgifter.js'
F = {}
KORT = {}


def fig(uid, w, h, label, kort=None):
    def dek(f):
        F[uid] = svg(w, h, f(), label)
        if kort is not None:
            KORT[uid] = kort
        return f
    return dek


def boll(x, y, r, fill, stroke=INK):
    return ring(x, y, r, fill, stroke, 2)


def ruta(x, y, w, h, rubrik):
    return rekt(x, y, w, h, '#f7fafc', '#c9d3da', 1.4, 8) + tt(x + w / 2, y + 18, rubrik, 13, 'middle', GRA, True)


# ================================================================ acceleration
@fig('3.213', 360, 230, 'En telefon faller med farten 3,55 m/s nedåt ner i ett tjockt, mjukt skydd och stannar på 0,026 s.')
def _():
    b = rekt(60, 170, 240, 50, '#f2c48d', INK, 2, 14)
    for x in range(80, 290, 30):
        b += path(f'M{x},176 C{x + 8},186 {x + 16},186 {x + 22},176', 'none', '#d39a5c', 1.4)
    b += rekt(160, 70, 40, 72, '#2b2f36', INK, 2, 6) + rekt(165, 78, 30, 56, '#9cc3e4', 'none', 0, 3)
    b += pil(230, 60, 230, 150, BLA, 3) + tt(240, 100, '3,55 m/s', 14, 'start', BLA, True)
    b += tt(180, 206, 'mjukt skydd', 13, 'middle', '#7a4a1a', True)
    b += tt(180, 30, 'stannar på 0,026 s', 13, 'middle', INK, True)
    return b


@fig('3.214', 440, 210, 'En bil rör sig åt höger med 15,0 m/s före en kollision och åt vänster med 2,60 m/s efteråt.')
def _():
    b = ''
    for y, rubrik in ((14, 'före kollisionen'), (112, 'efter kollisionen')):
        b += ruta(10, y, 420, 88, rubrik) + linje(20, y + 76, 420, y + 76, VAG, 3)
        b += rekt(386, y + 26, 28, 50, '#a39b8f', INK, 1.6, 2)
    b += bil(150, 90, '#5b9bd5') + pil(214, 64, 300, 64, BLA, 3) + tt(306, 69, '15,0 m/s', 14, 'start', BLA, True)
    b += bil(300, 188, '#5b9bd5') + pil(290, 162, 230, 162, ORA, 3) + tt(224, 167, '2,60 m/s', 14, 'end', ORA, True)
    return b


@fig('3.215', 420, 220, 'En basketboll rör sig nedåt med 5,4 m/s före studsen mot golvet och uppåt med 3,8 m/s efter studsen.')
def _():
    b = rekt(20, 180, 380, 30, '#d9b38c', INK, 1.6, 0)
    for x in range(40, 400, 40):
        b += linje(x, 180, x - 10, 210, '#b98b5a', 1.2)
    b += boll(120, 110, 26, '#e07a3a') + path('M94,110 L146,110 M120,84 L120,136', 'none', '#7a3a10', 1.4)
    b += pil(120, 30, 120, 80, BLA, 3) + tt(132, 50, '5,4 m/s', 14, 'start', BLA, True) + tt(120, 162, 'före studsen', 12, 'middle', GRA, True)
    b += boll(290, 110, 26, '#e07a3a') + path('M264,110 L316,110 M290,84 L290,136', 'none', '#7a3a10', 1.4)
    b += pil(290, 80, 290, 30, ORA, 3) + tt(302, 50, '3,8 m/s', 14, 'start', ORA, True) + tt(290, 162, 'efter studsen', 12, 'middle', GRA, True)
    b += tt(205, 24, 'kontakttid 55 ms', 12, 'middle', INK, True)
    return b


@fig('3.216', 440, 170, 'En tennisboll kommer med 30 m/s mot en racket och lämnar den med 30 m/s rakt tillbaka. Kontakttiden är 4,7 ms.')
def _():
    b = ellips(330, 85, 34, 52, '#f7fafc', INK, 3) + linje(330, 137, 330, 166, '#5d3a1a', 7)
    for i in range(-3, 4):
        b += linje(330 + i * 9, 40, 330 + i * 9, 130, '#c9d3da', 1) + linje(300, 85 + i * 13, 360, 85 + i * 13, '#c9d3da', 1)
    b += boll(270, 85, 12, '#d4e157')
    b += pil(90, 66, 240, 66, BLA, 3) + tt(165, 56, 'in: 30 m/s', 14, 'middle', BLA, True)
    b += pil(240, 106, 90, 106, ORA, 3) + tt(165, 128, 'ut: 30 m/s', 14, 'middle', ORA, True)
    b += tt(165, 156, 'kontakttid 4,7 ms', 12, 'middle', INK, True)
    return b


@fig('3.217', 440, 210, 'Under kontakten bromsas klubbhuvudet från 57 m/s till 44 m/s, medan bollen går från stillastående till 46 m/s.')
def _():
    b = ''
    for y, rubrik, vk, vb in ((10, 'före kontakten', '57 m/s', None), (110, 'efter kontakten', '44 m/s', '46 m/s')):
        b += ruta(10, y, 420, 90, rubrik) + linje(20, y + 80, 420, y + 80, '#6f9a5b', 3)
        b += rekt(60, y + 44, 44, 20, '#5d6b75', INK, 1.6, 4) + linje(70, y + 44, 40, y + 26, '#8c969e', 4)
        b += pil(110, y + 54, 170, y + 54, BLA, 3) + tt(176, y + 59, vk, 14, 'start', BLA, True)
        bx = 280 if vb is None else 320
        b += boll(bx, y + 70, 9, '#ffffff')
        if vb:
            b += pil(334, y + 70, 394, y + 70, ORA, 3) + tt(364, y + 60, vb, 14, 'middle', ORA, True)
        else:
            b += tt(bx, y + 52, 'stilla', 12, 'middle', GRA, True)
    return b


@fig('3.218', 440, 210, 'Två testvagnar kolliderar på en rak bana. Före: vagn 1 har +6,75 m/s och vagn 2 står stilla. Efter: vagn 1 står stilla och vagn 2 har +5,60 m/s.', kort=[])
def _():
    b = ''
    for y, rubrik, v1, v2 in ((10, 'före', '+6,75 m/s', None), (110, 'efter (40,0 ms senare)', None, '+5,60 m/s')):
        b += ruta(10, y, 420, 90, rubrik) + linje(20, y + 78, 420, y + 78, VAG, 3)
        b += rekt(150, y + 44, 70, 26, '#5b9bd5', INK, 1.6, 4) + tt(185, y + 62, '1', 13, 'middle', '#fff', True)
        b += rekt(226, y + 44, 70, 26, '#e07a5f', INK, 1.6, 4) + tt(261, y + 62, '2', 13, 'middle', '#fff', True)
        for x in (164, 206, 240, 282):
            b += cirkel(x, y + 72, 5, INK, '#fff', 1.2)
        if v1:
            b += pil(60, y + 57, 140, y + 57, BLA, 3) + tt(100, y + 47, v1, 13, 'middle', BLA, True)
        if v2:
            b += pil(306, y + 57, 386, y + 57, ORA, 3) + tt(346, y + 47, v2, 13, 'middle', ORA, True)
    return b


@fig('3.223', 440, 220, 'En cyklist passerar en markering med hastigheten +12 m/s, vänder och passerar samma markering 45 s senare med hastigheten −12 m/s.')
def _():
    b = ''
    for y, rubrik, rikt, v in ((10, 't = 0', 1, '+12 m/s'), (114, 't = 45 s', -1, '−12 m/s')):
        b += ruta(10, y, 420, 96, rubrik) + linje(20, y + 82, 420, y + 82, VAG, 4)
        b += linje(220, y + 30, 220, y + 90, ROD, 2.4) + rekt(212, y + 26, 16, 10, ROD, INK, 1, 1)
        cx = 220 - 28 * rikt
        b += cirkel(cx - 14, y + 70, 10, 'none', INK, 2) + cirkel(cx + 14, y + 70, 10, 'none', INK, 2)
        b += linje(cx - 14, y + 70, cx + 2, y + 52, INK, 2) + linje(cx + 2, y + 52, cx + 14, y + 70, INK, 2)
        if rikt > 0:
            b += pil(250, y + 50, 340, y + 50, BLA, 3) + tt(346, y + 55, v, 14, 'start', BLA, True)
        else:
            b += pil(190, y + 50, 100, y + 50, ORA, 3) + tt(94, y + 55, v, 14, 'end', ORA, True)
    b += tt(232, 52, 'markering', 11, 'start', ROD, True)
    return b


@fig('3.226', 440, 200, 'Två motorcyklar kör österut. Under 4,0 s accelererar A med 2,0 m/s² österut och B med 4,0 m/s² västerut.')
def _():
    b = ''
    for y, namn, fill, a, rikt in ((60, 'A', '#5b9bd5', '2,0 m/s²', 1), (140, 'B', '#e07a5f', '4,0 m/s²', -1)):
        b += linje(20, y + 18, 420, y + 18, VAG, 4)
        b += path(f'M180,{y + 4} L230,{y + 4} L246,{y + 12} L170,{y + 12} Z', fill, INK, 1.6)
        b += cirkel(182, y + 14, 7, INK, '#fff', 1.6) + cirkel(234, y + 14, 7, INK, '#fff', 1.6)
        b += tt(160, y + 10, namn, 15, 'end', INK, True)
        if rikt > 0:
            b += pil(260, y - 6, 340, y - 6, GRON, 3) + tt(346, y - 1, 'a = ' + a, 13, 'start', GRON, True)
        else:
            b += pil(250, y - 16, 170, y - 16, GRON, 3) + tt(164, y - 11, 'a = ' + a, 13, 'end', GRON, True)
    b += pil(370, 22, 420, 22, INK, 2, 8) + tt(366, 27, 'öster', 13, 'end', INK)
    b += tt(220, 192, 'båda kör österut', 12, 'middle', GRA, True)
    return b


@fig('3.210', 440, 210, 'En vagn skjuts uppför ett lutande plan med farten 4,50 m/s. Accelerationen 1,05 m/s² är riktad nedför planet.')
def _():
    b = path('M20,190 L420,190 L420,50 Z', GRAS, INK, 2)
    ang = math.atan2(140, 400)
    ux, uy = math.cos(ang), -math.sin(ang)
    nx, ny = uy, -ux
    px, py = 20 + ux * 160, 190 + uy * 160
    hjul = [(px + ux * 8, py + uy * 8), (px + ux * 40, py + uy * 40)]
    kropp = [(px + ux * a + nx * d, py + uy * a + ny * d) for a, d in ((0, 8), (48, 8), (48, 34), (0, 34))]
    b += D.path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in kropp) + ' Z', '#f2c48d', INK, 1.8)
    for x, y in hjul:
        b += cirkel(x + nx * 5, y + ny * 5, 6, INK, '#fff', 1.4)
    sx, sy = px + ux * 60 + nx * 22, py + uy * 60 + ny * 22
    b += pil(sx, sy, sx + ux * 90, sy + uy * 90, BLA, 3)
    b += tt(sx + ux * 45 + nx * 30, sy + uy * 45 + ny * 30, 'v₀ = 4,50 m/s', 14, 'middle', BLA, True, halo=True)
    ax, ay = px + ux * 24 + nx * 58, py + uy * 24 + ny * 58
    b += pil(ax, ay, ax - ux * 70, ay - uy * 70, ORA, 3)
    b += tt(ax - ux * 30 + nx * 16, ay - uy * 30 + ny * 16, 'a = 1,05 m/s² nedför', 13, 'middle', ORA, True, halo=True)
    return b


@fig('3.360', 460, 190, 'Bil B kör med 20 m/s förbi den stillastående bilen A. A startar 2,0 s senare med accelerationen 2,5 m/s² åt samma håll.')
def _():
    b = rekt(10, 110, 440, 40, VAG, INK, 1.5, 2) + linje(14, 130, 446, 130, '#fff', 1.5, '12 9')
    b += bil(40, 148, '#5b9bd5') + tt(67, 104, 'A står still', 12, 'middle', BLA, True)
    b += bil(120, 128, '#e07a5f') + pil(182, 96, 260, 96, ORA, 3) + tt(266, 101, 'B: 20 m/s', 14, 'start', ORA, True)
    b += linje(67, 150, 67, 168, GRA, 1.5) + tt(67, 184, 'start', 12, 'middle', GRA, True)
    b += tt(30, 30, 'A startar 2,0 s efter att B passerat, med a = 2,5 m/s²', 13, 'start', INK, True)
    b += flagga(420, 110, 'ikapp ?')
    return b


@fig('3.203', 440, 260, 'En planet i en ellipsformad bana runt en stjärna. Planetens hastighet i x-led är +20,9 km/s vid ett tillfälle och −18,5 km/s 2,16 år senare.')
def _():
    cx, cy, rx, ry = 220, 135, 160, 96
    b = ellips(cx, cy, rx, ry, 'none', GRA, 1.6).replace('/>', ' stroke-dasharray="6 5"/>')
    b += ring(cx - 50, cy, 18, '#f9c74f', '#e09f1f', 2) + tt(cx - 50, cy + 36, 'stjärna', 12, 'middle', GRA, True)
    b += ring(cx, cy - ry, 9, '#5b9bd5', INK, 1.6) + pil(cx + 12, cy - ry, cx + 90, cy - ry, BLA, 3)
    b += tt(cx + 96, cy - ry + 5, 'vₓ = +20,9 km/s', 13, 'start', BLA, True, halo=True)
    b += ring(cx, cy + ry, 9, '#5b9bd5', INK, 1.6) + pil(cx - 12, cy + ry, cx - 90, cy + ry, ORA, 3)
    b += tt(cx - 96, cy + ry + 5, 'vₓ = −18,5 km/s', 13, 'end', ORA, True, halo=True)
    b += tt(cx + 18, cy + ry + 22, '2,16 år senare', 12, 'start', GRA, True)
    b += pil(330, 236, 400, 236, INK, 2, 8) + tt(406, 241, 'x', 14, 'start', INK, True, italic=True)
    return b


# ================================================================ rörelse med konstant acceleration (konstacc)
# Figuren läggs efter stycket som slutar med denna text i stället för efter första stycket.
EFTER = {'3.400': 'landar på marken.</p>', '3.387': '45 s efter B.</p>'}


@fig('3.30', 420, 240, 'En sten kastas rakt nedåt med farten 8,0 m/s från en bro som är 22 m över vattenytan.')
def _():
    b = f'<rect x="0" y="190" width="420" height="50" fill="{VATTEN}"/>' + linje(0, 190, 420, 190, BLA, 2)
    b += rekt(0, 40, 300, 16, '#9aa4ab', INK, 2, 0) + rekt(250, 56, 30, 134, '#b7bec4', INK, 2, 0)
    b += rekt(0, 30, 300, 10, '#c9d0d5', INK, 1.4, 0)
    b += cirkel(150, 70, 8, '#8f8a82', INK, 1.4) + pil(150, 80, 150, 140, BLA, 3) + tt(160, 118, '8,0 m/s', 14, 'start', BLA, True)
    b += matt_v(340, 56, 190, '22 m')
    return b


@fig('3.63', 460, 170, 'En cyklist med farten 9,0 m/s. Under reaktionstiden 0,70 s rullar cykeln med samma fart, sedan bromsar den med 3,5 m/s².')
def _():
    b = rekt(10, 100, 440, 16, VAG, INK, 1.4, 2)
    b += cirkel(30, 88, 10, 'none', INK, 2) + cirkel(58, 88, 10, 'none', INK, 2) + linje(30, 88, 46, 70, INK, 2) + linje(46, 70, 58, 88, INK, 2)
    b += pil(72, 60, 130, 60, BLA, 3) + tt(136, 65, '9,0 m/s', 13, 'start', BLA, True)
    b += rekt(60, 120, 150, 14, '#9cc3e4', INK, 1.2, 0) + rekt(210, 120, 220, 14, '#f2c48d', INK, 1.2, 0)
    b += tt(135, 152, 'reaktionstid 0,70 s', 12, 'middle', BLA, True) + tt(320, 152, 'bromsar 3,5 m/s²', 12, 'middle', ORA, True)
    b += tt(245, 30, 'stoppsträcka ?', 13, 'middle', INK, True)
    return b


@fig('3.68', 340, 300, 'En hiss åker uppåt i tre faser: den accelererar med 0,70 m/s² till 2,6 m/s, åker med 2,6 m/s i 5,0 s och bromsar med 0,70 m/s² till stillastående.')
def _():
    b = rekt(40, 20, 90, 270, '#eef2f5', INK, 2, 0)
    for y0, h, fill, text in ((206, 84, '#cfe6f5', 'accelererar 0,70 m/s²'), (106, 100, '#e3f1d9', '2,6 m/s i 5,0 s'), (20, 86, '#f8e0c8', 'bromsar 0,70 m/s²')):
        b += rekt(42, y0, 86, h, fill, 'none', 0, 0) + tt(146, y0 + h / 2 + 5, text, 13, 'start', INK, True)
        b += linje(40, y0, 130, y0, GRA, 1.2, '4 3')
    b += rekt(55, 240, 60, 46, '#8c969e', INK, 2, 3) + rekt(62, 246, 20, 34, '#c9d0d5', INK, 1, 0) + rekt(88, 246, 20, 34, '#c9d0d5', INK, 1, 0)
    b += tt(85, 236, 'start', 11, 'middle', GRA, True)
    return b


@fig('3.86', 360, 250, 'En hiss åker uppåt med 2,0 m/s. En mutter lossnar från hissens tak, 2,6 m ovanför hissgolvet.')
def _():
    b = rekt(40, 20, 180, 220, '#eef2f5', INK, 3, 4) + rekt(40, 20, 180, 14, '#8c969e', INK, 2, 0) + rekt(40, 226, 180, 14, '#8c969e', INK, 2, 0)
    b += path('M124,34 L136,34 L139,42 L130,47 L121,42 Z', '#c9a400', INK, 1.4)
    b += pil(130, 52, 130, 110, GRA, 2, 8).replace('stroke="#526777"', 'stroke="#526777" stroke-dasharray="5 4"')
    b += tt(140, 76, 'mutter', 13, 'start', INK, True)
    b += matt_v(70, 34, 226, '2,6 m', vanster=False)
    b += pil(280, 200, 280, 60, BLA, 3) + tt(290, 120, 'hissen', 13, 'start', BLA, True) + tt(290, 138, '2,0 m/s', 13, 'start', BLA, True)
    return b


@fig('3.118', 360, 280, 'Anna kastar en boll rakt uppåt med 9,0 m/s från höjden 1,5 m över marken.')
def _():
    b = rekt(0, 250, 360, 30, GRAS, 'none', 0, 0) + linje(0, 250, 360, 250, '#6f9a5b', 2)
    b += cirkel(120, 156, 11, INK, INK, 1) + linje(120, 167, 120, 214, INK, 3) + linje(120, 214, 108, 250, INK, 3) + linje(120, 214, 132, 250, INK, 3)
    b += linje(120, 180, 140, 170, INK, 3) + linje(140, 170, 146, 162, INK, 3)
    b += cirkel(148, 156, 8, '#e07a3a', INK, 1.4)
    b += pil(170, 150, 170, 70, BLA, 3) + tt(180, 110, '9,0 m/s', 14, 'start', BLA, True)
    b += linje(148, 140, 148, 40, GRA, 1.4, '4 4') + tt(158, 36, 'högsta punkt ?', 12, 'start', GRA, True)
    b += matt_v(60, 156, 250, '1,5 m', vanster=True)
    return b


@fig('3.124', 440, 240, 'En backhoppare startar från stillastående överst i ansatsen och har farten 23 m/s efter 68 m.')
def _():
    b = path('M30,40 C120,60 220,150 330,190 L420,196', 'none', '#7aa3bd', 10)
    b += path('M30,40 C120,60 220,150 330,190 L420,196', 'none', '#eef6fb', 5)
    b += gubbe(40, 40, BLA, 0.7) + tt(58, 22, 'start', 12, 'start', GRA, True)
    b += cirkel(330, 186, 6, ORA, INK, 1.2) + pil(340, 182, 400, 192, ORA, 3) + tt(396, 178, '23 m/s', 14, 'end', ORA, True)
    b += tt(250, 78, '68 m längs ansatsen', 13, 'middle', INK, True, halo=True)
    return b


@fig('3.162', 360, 270, 'En linjal hålls vertikalt mellan tummen och pekfingret och släpps. Linjalen faller 18 cm innan den fångas.')
def _():
    b = rekt(150, 20, 40, 230, '#f2dcb3', INK, 2, 2)
    for cm in range(0, 31, 2):
        y = 30 + cm * 7
        b += linje(150, y, 150 + (14 if cm % 10 == 0 else 8), y, INK, 1.2)
        if cm % 10 == 0:
            b += tt(186, y + 4, str(cm), 11, 'end', INK)
    b += path('M120,52 C112,48 104,52 106,60 L146,64 L146,54 Z', '#f0c9a8', INK, 1.4)
    b += path('M220,52 C228,48 236,52 234,60 L194,64 L194,54 Z', '#f0c9a8', INK, 1.4)
    b += tt(244, 46, 'fingrarna', 12, 'start', GRA, True)
    b += pil(310, 70, 310, 196, BLA, 3) + tt(300, 128, 'faller', 13, 'end', BLA, True) + tt(300, 144, '18 cm', 13, 'end', BLA, True)
    b += tt(170, 266, 'reaktionstid ?', 13, 'middle', ORA, True)
    return b


@fig('3.170', 320, 300, 'En boll kastas uppåt från marken med 18 m/s samtidigt som en annan boll släpps 45 m ovanför.')
def _():
    b = rekt(0, 270, 320, 30, GRAS, 'none', 0, 0) + linje(0, 270, 320, 270, '#6f9a5b', 2)
    b += cirkel(130, 260, 9, '#e07a3a', INK, 1.4) + pil(150, 260, 150, 196, BLA, 3) + tt(158, 232, '18 m/s', 13, 'start', BLA, True)
    b += cirkel(130, 30, 9, '#5b9bd5', INK, 1.4) + tt(148, 34, 'släpps', 13, 'start', INK, True)
    b += linje(130, 44, 130, 246, GRA, 1.2, '4 4') + tt(90, 150, 'möts ?', 13, 'end', ORA, True)
    b += matt_v(250, 30, 270, '45 m')
    return b


@fig('3.172', 460, 166, 'En bil kör i 80 km/h. Ett hinder står stilla 60 m framför bilens front.')
def _():
    b = rekt(10, 90, 440, 30, VAG, INK, 1.4, 2) + linje(14, 105, 446, 105, '#fff', 1.5, '12 9')
    b += bil(20, 102, '#5b9bd5') + pil(80, 60, 150, 60, BLA, 3) + tt(156, 65, '80 km/h', 14, 'start', BLA, True)
    b += path('M412,100 L412,64 C412,54 430,54 430,64 L430,100 Z', '#8f8a82', INK, 1.6) + tt(421, 50, 'hinder', 12, 'middle', INK, True)
    b += matt_h(74, 412, 152, '60 m', under=False)
    return b


@fig('3.177', 460, 170, 'Två vagnar på parallella raka banor. Den främre håller 6,0 m/s och ligger 30 m före. Den bakre startar från stillastående med 1,5 m/s².')
def _():
    b = ''
    for y in (60, 120):
        b += linje(10, y, 450, y, VAG, 4)
    b += rekt(30, 96, 50, 22, '#e07a5f', INK, 1.6, 3) + cirkel(42, 120, 5, INK, '#fff', 1.2) + cirkel(68, 120, 5, INK, '#fff', 1.2)
    b += tt(55, 146, 'startar, a = 1,5 m/s²', 12, 'start', ORA, True)
    b += rekt(30 + 160, 36, 50, 22, '#5b9bd5', INK, 1.6, 3) + cirkel(202, 60, 5, INK, '#fff', 1.2) + cirkel(228, 60, 5, INK, '#fff', 1.2)
    b += pil(250, 46, 320, 46, BLA, 3) + tt(326, 51, '6,0 m/s', 13, 'start', BLA, True)
    b += linje(80, 90, 80, 30, GRA, 1.2, '4 3') + linje(190, 90, 190, 30, GRA, 1.2, '4 3')
    b += linje(80, 24, 190, 24, GRA, 1.5) + tt(135, 18, '30 m', 13, 'middle', INK, True)
    b += tt(400, 96, 'jämsides ?', 13, 'middle', INK, True)
    return b


@fig('3.378', 460, 170, 'En bil kör i 50 km/h och är 35 m från stopplinjen vid ett trafikljus.')
def _():
    b = rekt(10, 96, 440, 34, VAG, INK, 1.4, 2) + linje(14, 113, 446, 113, '#fff', 1.5, '12 9')
    b += bil(20, 110, '#5b9bd5') + pil(80, 70, 150, 70, BLA, 3) + tt(156, 75, '50 km/h', 14, 'start', BLA, True)
    b += linje(330, 96, 330, 130, '#fff', 4) + tt(330, 148, 'stopplinje', 12, 'middle', INK, True)
    b += linje(360, 96, 360, 40, INK, 3) + rekt(350, 16, 20, 50, '#2b2f36', INK, 1.4, 4)
    for i, fill in enumerate((ROD, '#5a4a2a', '#2a4a2a')):
        b += cirkel(360, 25 + i * 15, 5, fill, INK, 0.8)
    b += matt_h(74, 330, 160, '35 m', under=False)
    return b


@fig('3.379', 460, 150, 'En golfboll puttas mot hålet med farten 2,52 m/s. Hålet är 4,80 m bort.')
def _():
    b = rekt(0, 30, 460, 100, '#7cbf72', 'none', 0, 6)
    b += cirkel(40, 80, 7, '#ffffff', INK, 1.4) + pil(52, 80, 130, 80, BLA, 3) + tt(90, 70, '2,52 m/s', 13, 'middle', BLA, True)
    b += ellips(410, 82, 12, 5, '#1d3320', INK, 1.4) + linje(410, 82, 410, 34, INK, 2) + path('M410,34 L432,40 L410,46 Z', ROD, INK, 1)
    b += matt_h(40, 410, 118, '4,80 m', under=False)
    return b


@fig('3.391', 460, 170, 'Två bilar kör åt samma håll med 18 m/s. Avståndet mellan den bakre bilens front och den främre bilens bakände är 16,0 m.')
def _():
    b = rekt(10, 90, 440, 30, VAG, INK, 1.4, 2) + linje(14, 105, 446, 105, '#fff', 1.5, '12 9')
    b += bil(40, 102, '#e07a5f', 70) + bil(300, 102, '#5b9bd5', 70)
    b += linje(110, 130, 110, 146, GRA, 1.5) + linje(300, 130, 300, 146, GRA, 1.5) + linje(110, 140, 300, 140, GRA, 1.5) + tt(205, 160, '16,0 m', 13, 'middle', INK, True)
    b += tt(75, 40, 'bakre: 18 m/s', 13, 'middle', ORA, True) + tt(75, 56, '0,50 s, sedan 4,0 m/s²', 11, 'middle', ORA)
    b += tt(335, 40, 'främre: 18 m/s', 13, 'middle', BLA, True) + tt(335, 56, 'bromsar 6,0 m/s²', 11, 'middle', BLA)
    b += pil(380, 76, 440, 76, INK, 2, 8)
    return b


@fig('3.400', 380, 300, 'En boll kastas rakt uppåt med 35 m/s från kanten av ett 7,0 m högt tak och landar sedan på marken bredvid huset.')
def _():
    b = rekt(0, 270, 380, 30, GRAS, 'none', 0, 0) + linje(0, 270, 380, 270, '#6f9a5b', 2)
    b += rekt(60, 190, 140, 80, '#f2dcb3', INK, 2, 0) + path('M50,190 L130,150 L210,190 Z', '#b55a3c', INK, 2)
    b += rekt(80, 220, 30, 50, '#b98b5a', INK, 1.4, 0)
    b += cirkel(214, 182, 7, '#e07a3a', INK, 1.4)
    b += pil(214, 172, 214, 110, BLA, 3) + tt(204, 136, '35 m/s', 14, 'end', BLA, True)
    b += path('M222,104 C224,40 250,40 254,104 L254,262', 'none', GRA, 1.4, ' stroke-dasharray="5 4"')
    b += matt_v(44, 190, 270, '7,0 m', vanster=True)
    return b


@fig('3.406', 360, 280, 'En raket startar från marken. Under de första 4,0 s ökar farten uppåt med 15 m/s varje sekund. Sedan stängs motorn av.')
def _():
    b = rekt(0, 250, 360, 30, GRAS, 'none', 0, 0) + linje(0, 250, 360, 250, '#6f9a5b', 2)
    b += path('M110,120 L130,90 L150,120 L150,210 L110,210 Z', '#e9eef2', INK, 2) + path('M110,190 L94,214 L110,210 Z', ROD, INK, 1.4)
    b += path('M150,190 L166,214 L150,210 Z', ROD, INK, 1.4) + cirkel(130, 140, 8, '#9cc3e4', INK, 1.2)
    b += path('M118,212 L130,244 L142,212 Z', '#f9c74f', '#e09f1f', 1.2)
    b += tt(190, 120, 'motorn på i 4,0 s:', 13, 'start', INK, True) + tt(190, 138, 'farten ökar 15 m/s', 13, 'start', BLA, True)
    b += tt(190, 154, 'varje sekund', 13, 'start', BLA, True)
    b += tt(190, 190, 'sedan motorn av', 13, 'start', INK, True) + tt(190, 206, 'tills den landar', 13, 'start', GRA)
    return b


@fig('3.387', 460, 160, 'En rak väg med punkterna A, B och C. AB = 476 m och BC = 855 m. Bilen passerar A med 24 m/s, har 10 m/s i B och når C 45 s efter B.', kort=['b', 'c'])
def _():
    x0, k = 30, 400 / (476 + 855)
    xa, xb, xc = x0, x0 + 476 * k, x0 + (476 + 855) * k
    b = rekt(10, 70, 440, 20, VAG, INK, 1.4, 2)
    for x, namn, v in ((xa, 'A', '24 m/s'), (xb, 'B', '10 m/s'), (xc, 'C', None)):
        b += linje(x, 62, x, 98, INK, 2.4) + tt(x, 54, namn, 15, 'middle', INK, True)
        if v:
            b += tt(x + 6, 40, v, 12, 'start', BLA, True)
    b += matt_h(xa, xb, 120, '476 m', under=False) + matt_h(xb, xc, 120, '855 m', under=False)
    b += tt((xb + xc) / 2, 150, 'B till C: 45 s', 12, 'middle', ORA, True)
    return b


# ================================================================ hastighet som vektor (vektorer)
def bage(cx, cy, r, fran, till, color=ORA, w=2):
    """Vinkelbåge från riktningen fran till riktningen till (grader moturs från öster), ritad som polyline."""
    n = 24
    pts = [(cx + r * math.cos(math.radians(fran + (till - fran) * i / n)), cy - r * math.sin(math.radians(fran + (till - fran) * i / n)))
           for i in range(n + 1)]
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def kompassvektor(theta, ref, vinkeltext, vtext, W=380, H=300):
    """Axlar med väderstreck och en vektor i riktningen theta (grader moturs från öster) med vinkeln mot ref markerad."""
    cx, cy, L, A = W / 2, H / 2, 110, 120
    b = pil(cx - A, cy, cx + A, cy, INK, 1.6, 9) + pil(cx, cy + A, cx, cy - A, INK, 1.6, 9)
    b += tt(cx + A + 4, cy + 18, 'x', 14, 'end', INK, True, italic=True) + tt(cx - 10, cy - A + 6, 'y', 14, 'end', INK, True, italic=True)
    b += tt(cx + A - 2, cy - 8, 'öster', 12, 'end', GRA, True) + tt(cx - A, cy - 8, 'väster', 12, 'start', GRA, True)
    sida = 1 if math.cos(math.radians(theta)) <= 0.05 else -1  # ordet på motsatt sida om vektorn
    b += tt(cx + sida * 10, cy - A + 36, 'norr', 12, 'start' if sida > 0 else 'end', GRA, True)
    b += tt(cx + sida * 10, cy + A - 2, 'söder', 12, 'start' if sida > 0 else 'end', GRA, True)
    ex, ey = cx + L * math.cos(math.radians(theta)), cy - L * math.sin(math.radians(theta))
    b += pil(cx, cy, ex, ey, BLA, 3.4, 12)
    lx, ly = cx + (L + 22) * math.cos(math.radians(theta)), cy - (L + 22) * math.sin(math.radians(theta))
    if abs(math.cos(math.radians(theta))) < 0.4:  # nästan lodrät vektor: etiketten vid sidan av spetsen
        lx, ly = ex - 12 * (1 if math.cos(math.radians(theta)) <= 0 else -1) * 3, ey + (14 if math.sin(math.radians(theta)) < 0 else -6)
    b += tt(lx, ly + 5, vtext, 14, 'middle', BLA, True, halo=True)
    b += bage(cx, cy, 46, ref, theta)
    mid = math.radians((ref + theta) / 2)
    rt = 64 if abs(theta - ref) >= 25 else 80
    sida_v = math.copysign(1, ref - theta)  # liten vinkel: etiketten på andra sidan referensaxeln
    if abs(theta - ref) < 25:
        mid = math.radians(ref + sida_v * 12)
    b += tt(cx + rt * math.cos(mid), cy - rt * math.sin(mid) + 5, vinkeltext, 14, 'middle', ORA, True, halo=True)
    return b


@fig('3.638', 380, 300, 'Axlar där x pekar österut och y norrut. Båtens hastighet, 15 m/s, pekar 30° söder om väster.')
def _():
    return kompassvektor(210, 180, '30°', '15 m/s')


@fig('3.711', 380, 300, 'Axlar där x pekar österut och y norrut. Kajakens hastighet, 12 km/h, pekar 40° väster om norr.')
def _():
    return kompassvektor(130, 90, '40°', '12 km/h')


@fig('3.713', 380, 300, 'Axlar där x pekar österut och y norrut. Fiskebåtens hastighet, 6,0 m/s, pekar 15° väster om söder.')
def _():
    return kompassvektor(255, 270, '15°', '6,0 m/s')


@fig('3.677', 380, 300, 'Axlar där x pekar österut och y norrut. Vinden, 15 m/s, blåser mot nordost, 45° från öster.')
def _():
    return kompassvektor(45, 0, '45°', '15 m/s')


def alv(H=210, ström='', y1=40, y2=170):
    b = rekt(0, 0, 440, y1, GRAS, 'none', 0, 0) + rekt(0, y2, 440, H - y2, GRAS, 'none', 0, 0)
    b += f'<rect x="0" y="{y1}" width="440" height="{y2 - y1}" fill="{VATTEN}"/>' + linje(0, y1, 440, y1, '#6f9a5b', 2) + linje(0, y2, 440, y2, '#6f9a5b', 2)
    return b


@fig('3.689', 440, 210, 'En älv där strömmen går längs stranden med 2,0 m/s. Båten är riktad 30° ut från strandkanten, nedströms, med farten 5,0 m/s genom vattnet.')
def _():
    b = alv()
    x0, y0 = 80, 166
    th = math.radians(30)
    b += pil(x0, y0, x0 + 150 * math.cos(th), y0 - 150 * math.sin(th), BLA, 3.4, 12)
    b += tt(x0 + 100, y0 - 92, '5,0 m/s genom vattnet', 13, 'middle', BLA, True, halo=True)
    b += linje(x0, y0, x0 + 90, y0, GRA, 1.4, '4 3') + bage(x0, y0, 52, 0, 30) + tt(x0 + 70, y0 - 12, '30°', 13, 'start', ORA, True, halo=True)
    b += pil(290, 140, 400, 140, '#3d6d8c', 2.6, 9) + tt(345, 130, 'ström 2,0 m/s', 13, 'middle', '#3d6d8c', True, halo=True)
    b += tt(220, 196, 'strandkant', 12, 'middle', '#3f6b32', True)
    return b


@fig('3.723', 440, 210, 'En båt rör sig 4,0 m/s rakt över en älv och driver samtidigt 1,2 m/s med strömmen. Avvikelsen från rakt över är okänd.')
def _():
    b = alv()
    x0, y0 = 160, 166
    b += pil(x0, y0, x0, 52, BLA, 3.4, 12) + tt(x0 - 10, 110, '4,0 m/s', 13, 'end', BLA, True, halo=True) + tt(x0 - 10, 126, 'rakt över', 12, 'end', BLA, halo=True)
    b += pil(x0, y0 - 4, x0 + 80, y0 - 4, '#3d6d8c', 3, 10) + tt(x0 + 90, y0 - 10, '1,2 m/s med strömmen', 12, 'start', '#3d6d8c', True, halo=True)
    b += tt(x0 + 40, 76, 'avvikelse ?', 13, 'start', ORA, True, halo=True)
    return b


@fig('3.732', 400, 280, 'Ett flygplan håller 250 m/s rakt norrut genom luften. Vinden blåser med 40 m/s mot nordost, 45° mellan öster och norr.')
def _():
    cx, cy = 120, 230
    b = pil(cx, cy, cx, 50, BLA, 3.4, 12) + tt(cx - 10, 140, '250 m/s', 14, 'end', BLA, True) + tt(cx - 10, 158, 'norrut', 12, 'end', BLA)
    b += path(f'M{cx},{cy - 12} L{cx - 22},{cy + 6} L{cx + 22},{cy + 6} Z', '#d9dde1', INK, 1.4) + path(f'M{cx - 4},{cy - 30} L{cx + 4},{cy - 30} L{cx + 4},{cy + 14} L{cx - 4},{cy + 14} Z', '#d9dde1', INK, 1.4)
    wx, wy = 250, 200
    b += pil(wx, wy, wx + 90 * math.cos(math.radians(45)), wy - 90 * math.sin(math.radians(45)), GRON, 3.4, 12)
    b += linje(wx, wy, wx + 90, wy, GRA, 1.4, '4 3') + bage(wx, wy, 40, 0, 45) + tt(wx + 54, wy - 12, '45°', 13, 'start', ORA, True, halo=True)
    b += tt(wx + 60, wy - 82, 'vind 40 m/s', 13, 'start', GRON, True)
    b += pil(340, 270, 380, 270, INK, 2, 8) + tt(336, 274, 'öster', 12, 'end', GRA) + pil(30, 270, 30, 230, INK, 2, 8) + tt(38, 236, 'norr', 12, 'start', GRA)
    return b


@fig('3.656', 440, 230, 'En vandrare går först 400 m österut och sedan 300 m i riktningen 60° norr om öster. Avståndet fågelvägen är okänt.')
def _():
    k = 0.48
    x0, y0 = 40, 190
    x1, y1 = x0 + 400 * k, y0
    x2, y2 = x1 + 300 * k * math.cos(math.radians(60)), y1 - 300 * k * math.sin(math.radians(60))
    b = rekt(0, 0, 440, 230, '#f4f1e8', 'none', 0, 0)
    b += pil(x0, y0, x1, y1, BLA, 3, 10) + tt((x0 + x1) / 2, y0 + 20, '400 m österut', 13, 'middle', BLA, True)
    b += pil(x1, y1, x2, y2, BLA, 3, 10) + tt(x2 + 10, (y1 + y2) / 2, '300 m', 13, 'start', BLA, True)
    b += linje(x1, y1, x1 + 80, y1, GRA, 1.4, '4 3') + bage(x1, y1, 34, 0, 60) + tt(x1 + 48, y1 - 12, '60°', 13, 'start', ORA, True, halo=True)
    b += linje(x0, y0, x2, y2, ORA, 2, '6 5') + tt((x0 + x2) / 2 - 14, (y0 + y2) / 2 - 8, '?', 16, 'end', ORA, True, halo=True)
    b += cirkel(x0, y0, 5, INK, INK, 1) + tt(x0, y0 + 20, 'start', 12, 'middle', GRA, True)
    b += pil(380, 60, 420, 60, INK, 2, 8) + tt(376, 64, 'öster', 12, 'end', GRA) + pil(400, 110, 400, 72, INK, 2, 8) + tt(408, 90, 'norr', 12, 'start', GRA)
    return b


@fig('3.730', 400, 290, 'En orienterare springer 3,0 km österut, 2,0 km norrut och 4,0 km mot sydväst. Avståndet från starten är okänt.')
def _():
    k = 50
    x0, y0 = 110, 200
    p1 = (x0 + 3 * k, y0)
    p2 = (p1[0], p1[1] - 2 * k)
    p3 = (p2[0] - 4 * k * math.cos(math.radians(45)), p2[1] + 4 * k * math.sin(math.radians(45)))
    b = rekt(0, 0, 400, 290, '#f4f1e8', 'none', 0, 0)
    b += pil(x0, y0, *p1, BLA, 3, 10) + tt((x0 + p1[0]) / 2, y0 + 20, '3,0 km', 13, 'middle', BLA, True, halo=True)
    b += pil(*p1, *p2, BLA, 3, 10) + tt(p1[0] + 10, (p1[1] + p2[1]) / 2, '2,0 km', 13, 'start', BLA, True, halo=True)
    b += pil(*p2, *p3, BLA, 3, 10) + tt((p2[0] + p3[0]) / 2 - 16, (p2[1] + p3[1]) / 2 - 16, '4,0 km mot sydväst', 13, 'end', BLA, True, halo=True)
    b += linje(x0, y0, *p3, ORA, 2, '5 4') + tt((x0 + p3[0]) / 2 - 10, (y0 + p3[1]) / 2 + 20, '?', 16, 'end', ORA, True, halo=True)
    b += path(f'M{x0},{y0 - 10} L{x0 + 10},{y0 + 8} L{x0 - 10},{y0 + 8} Z', 'none', ROD, 2) + tt(x0 - 14, y0 - 6, 'start', 12, 'end', ROD, True)
    b += pil(330, 40, 370, 40, INK, 2, 8) + tt(326, 44, 'öster', 12, 'end', GRA) + pil(350, 90, 350, 52, INK, 2, 8) + tt(358, 70, 'norr', 12, 'start', GRA)
    return b


@fig('3.705', 440, 210, 'En tennisboll serveras med farten 45 m/s riktad 12° under det horisontella.')
def _():
    b = rekt(0, 170, 440, 40, '#5a8f4e', 'none', 0, 0) + rekt(300, 120, 6, 50, '#ffffff', INK, 1, 0) + linje(303, 120, 303, 170, INK, 1)
    for y in range(124, 170, 8):
        b += linje(300, y, 306, y, '#9aa4ab', 1)
    x0, y0 = 70, 60
    b += cirkel(x0, y0, 7, '#d4e157', INK, 1.4)
    th = math.radians(-12)
    b += pil(x0 + 8, y0, x0 + 8 + 170 * math.cos(th), y0 - 170 * math.sin(th), BLA, 3, 11)
    b += tt(x0 + 110, y0 + 58, '45 m/s', 14, 'middle', BLA, True, halo=True)
    b += linje(x0 + 8, y0, x0 + 200, y0, GRA, 1.4, '4 3') + bage(x0 + 8, y0, 110, 0, -12) + tt(x0 + 130, y0 - 6, '12°', 13, 'start', ORA, True, halo=True)
    return b


@fig('3.676', 440, 190, 'Ett flygplan flyger med farten 240 m/s och stiger i vinkeln 6° mot marken.')
def _():
    b = rekt(0, 160, 440, 30, GRAS, 'none', 0, 0) + linje(0, 160, 440, 160, '#6f9a5b', 2)
    x0, y0 = 60, 120
    th = math.radians(6)
    b += path(f'M{x0 - 30},{y0 + 2} L{x0 + 10},{y0 - 2} L{x0 + 16},{y0 - 1} L{x0 + 10},{y0 + 4} L{x0 - 30},{y0 + 6} Z', '#d9dde1', INK, 1.4)
    b += path(f'M{x0 - 26},{y0 + 2} L{x0 - 32},{y0 - 12} L{x0 - 22},{y0 + 1} Z', '#d9dde1', INK, 1.2)
    b += pil(x0 + 18, y0, x0 + 18 + 300 * math.cos(th), y0 - 300 * math.sin(th), BLA, 3, 11)
    b += tt(x0 + 200, y0 - 36, '240 m/s', 14, 'middle', BLA, True, halo=True)
    b += linje(x0 + 18, y0, x0 + 340, y0, GRA, 1.4, '4 3') + bage(x0 + 18, y0, 200, 0, 6) + tt(x0 + 226, y0 - 4, '6°', 13, 'start', ORA, True, halo=True)
    return b


@fig('3.7', 460, 170, 'Ett tåg kör i 90 km/h. Inne i tåget rullas en boll framåt i mittgången med 1,5 m/s i förhållande till golvet.')
def _():
    b = linje(10, 150, 450, 150, INK, 3) + rekt(40, 50, 360, 90, '#e7eef4', INK, 2, 14)
    for x in (80, 150, 290, 360):
        b += cirkel(x, 146, 9, INK, '#fff', 2)
    for x in range(70, 380, 56):
        b += rekt(x, 66, 36, 26, '#cfe6f5', INK, 1.2, 3)
    b += linje(50, 128, 390, 128, '#b7bec4', 2) + cirkel(180, 122, 6, '#e07a3a', INK, 1.2)
    b += pil(190, 112, 250, 112, ORA, 2.6, 9) + tt(256, 116, '1,5 m/s mot golvet', 12, 'start', ORA, True, halo=True)
    b += pil(330, 30, 420, 30, BLA, 3) + tt(326, 35, 'tåget 90 km/h', 13, 'end', BLA, True)
    return b


@fig('3.52', 460, 150, 'Stafettväxling. Mottagaren är 6,0 m före den inkommande löparen och springer 9,2 m/s. Den inkommande löparen springer 8,5 m/s.')
def _():
    b = rekt(0, 100, 460, 40, '#d9734e', 'none', 0, 0) + linje(0, 100, 460, 100, '#fff', 2) + linje(0, 140, 460, 140, '#fff', 2)
    b += gubbe(120, 120, BLA, 0.9) + gubbe(280, 120, ORA, 0.9)
    b += pil(132, 60, 196, 60, BLA, 2.6, 9) + tt(120, 40, 'inkommande 8,5 m/s', 12, 'middle', BLA, True)
    b += pil(292, 60, 362, 60, ORA, 2.6, 9) + tt(300, 40, 'mottagare 9,2 m/s', 12, 'middle', ORA, True)
    b += linje(120, 128, 120, 146, '#fff', 1.6) + linje(280, 128, 280, 146, '#fff', 1.6) + linje(120, 137, 280, 137, '#fff', 1.6)
    b += tt(200, 133, '6,0 m', 13, 'middle', '#fff', True)
    return b


@fig('3.82', 460, 170, 'En bil som kör 27,5 m/s kör om en lastbil som kör 23,0 m/s. Bilen måste förflytta sig 95 m i förhållande till lastbilen.', kort=['b', 'c'])
def _():
    b = rekt(10, 70, 440, 70, VAG, INK, 1.4, 2) + linje(14, 105, 446, 105, '#fff', 1.6, '14 10')
    b += rekt(200, 110, 140, 26, '#e9eef2', INK, 1.6, 2) + rekt(340, 112, 30, 22, '#5b9bd5', INK, 1.6, 3)
    for x in (220, 250, 320, 356):
        b += cirkel(x, 138, 6, INK, '#fff', 1.4)
    b += pil(380, 124, 440, 124, BLA, 2.6, 9) + tt(410, 160, 'lastbil 23,0 m/s', 12, 'middle', BLA, True)
    b += bil(100, 98, '#e07a5f') + pil(160, 82, 210, 82, ORA, 2.6, 9) + tt(140, 60, 'bil 27,5 m/s', 12, 'middle', ORA, True)
    b += tt(330, 40, '95 m i förhållande till lastbilen', 12, 'middle', INK, True)
    return b


@fig('3.95', 460, 180, 'Två tåg 60 km från varandra kör mot varandra med 90 km/h vardera. En fluga flyger med 120 km/h fram och tillbaka mellan dem.')
def _():
    b = linje(10, 140, 450, 140, INK, 3)
    b += path('M20,90 L110,90 L130,110 L130,136 L20,136 Z', '#5b9bd5', INK, 2) + path('M440,90 L350,90 L330,110 L330,136 L440,136 Z', '#e07a5f', INK, 2)
    b += pil(80, 70, 140, 70, BLA, 2.6, 9) + tt(80, 60, '90 km/h', 12, 'middle', BLA, True)
    b += pil(380, 70, 320, 70, ORA, 2.6, 9) + tt(380, 60, '90 km/h', 12, 'middle', ORA, True)
    b += path('M134,104 L180,48 L226,96 L262,58 L290,92 L310,70', 'none', GRA, 1.4, ' stroke-dasharray="4 3"')
    b += cirkel(134, 104, 4, INK, INK, 1) + tt(230, 34, 'flugan 120 km/h', 12, 'middle', INK, True)
    b += matt_h(130, 330, 166, '60 km', under=False)
    return b


# ---------------------------------------------------------------- inläggning
def efter_forsta_stycket(html, figur, efter=None):
    i = (html.index(efter) + len(efter)) if efter and efter in html else html.index('</p>') + 4
    return html[:i] + figur + html[i:]


def med_figur(q, figur):
    q = json.loads(json.dumps(q))
    kort = KORT.get(q['id'])  # None: alla delkort
    efter = EFTER.get(q['id'])
    q['t'] = efter_forsta_stycket(q['t'], figur, efter)
    if q.get('spelIntro') and (kort is None or q['id'] in EFTER):
        q['spelIntro'] = q['spelIntro'] + figur
    for d in q.get('spelDelar') or []:
        if d.get('t') and (kort is None or d['etikett'] in kort):
            d['t'] = efter_forsta_stycket(d['t'], figur, efter)
    return q


def main():
    src, bank = B.las(ROOT / BANK)
    Q = {q['id']: q for q in bank}
    klara = {uid for uid, figur in F.items() if figur in Q[uid]['t']}
    nya = {}
    for uid, figur in F.items():
        if uid in klara:
            continue
        q = Q[uid]
        assert q['kap'] == 3, uid
        assert '<svg' not in q['t'] and '<svg' not in (q.get('spelIntro') or ''), uid
        assert 'positiv' not in figur, uid
        nya[uid] = med_figur(q, figur)
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
        Path(sys.argv[sys.argv.index('--ut') + 1]).write_text(json.dumps([q for q in ny_bank if q['id'] in F], ensure_ascii=False), encoding='utf-8')
    if '--skriv' in sys.argv:
        B.skriv(ROOT / BANK, ny_src)


if __name__ == '__main__':
    main()
