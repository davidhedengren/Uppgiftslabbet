"""Fysik 1 (uppgifter.js), kapitel 4 Kraft: figurer i uppgifter som saknade figur, 19 november 2026.

Fortsättning på kapitel 2 och 3 (tools/bygg-fy1-kap3-figurer-2026-11-19.py, agent/FY1_KAP3_FIGURER_2026-11-19.md),
med samma regler. Figurerna visar föremålen och de krafter som är givna i texten, men inte de krafter som söks
(normalkraft, kraft mellan föremål, spännkraft) och inga färdiga kraftfigurer när eleven ska rita dem själv.
Se agent/FY1_KAP4_FIGURER_2026-11-19.md.

  python tools/bygg-fy1-kap4-figurer-2026-11-19.py [--skriv] [--ut fil.json]
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
EFTER = {}


def fig(uid, w, h, label, kort=None):
    def dek(f):
        F[uid] = svg(w, h, f(), label)
        if kort is not None:
            KORT[uid] = kort
        return f
    return dek


def skridsko(x, y, color, s=1.0):
    """Person på skridskor; (x, y) är isens nivå."""
    b = gubbe(x, y - 6 * s, color, s)
    return b + linje(x - 12 * s, y - 2, x + 6 * s, y - 2, INK, 2) + linje(x + 2 * s, y - 2, x + 16 * s, y - 2, INK, 2)


def is_yta(W, y):
    return rekt(0, y, W, 24, '#e3f1fa', 'none', 0, 0) + linje(0, y, W, y, '#8fb7d0', 2)


def golv(W, y):
    b = rekt(0, y, W, 20, '#d9c7a6', 'none', 0, 0) + linje(0, y, W, y, INK, 2)
    for x in range(10, W, 24):
        b += linje(x, y + 2, x - 10, y + 18, '#b9a07a', 1)
    return b


def vagn(x, y, w, h, fill, text=''):
    b = rekt(x, y - h - 10, w, h, fill, INK, 1.8, 4) + cirkel(x + 12, y - 6, 6, INK, '#fff', 1.4) + cirkel(x + w - 12, y - 6, 6, INK, '#fff', 1.4)
    if text:
        b += tt(x + w / 2, y - h / 2 - 5, text, 13, 'middle', '#fff', True)
    return b


# ================================================================ Newtons tredje lag
@fig('4.463', 400, 170, 'Två elever står på skridskor på blank is. Eleven med massan 50 kg trycker eleven med massan 75 kg med kraften 150 N.')
def _():
    b = is_yta(400, 140) + skridsko(150, 140, BLA) + skridsko(230, 140, ORA, 1.15)
    b += linje(160, 108, 216, 108, INK, 2) + pil(170, 70, 250, 70, ROD, 3) + tt(210, 60, '150 N på 75 kg-eleven', 12, 'middle', ROD, True)
    b += tt(150, 162, '50 kg', 13, 'middle', BLA, True) + tt(232, 162, '75 kg', 13, 'middle', ORA, True)
    return b


@fig('4.464', 400, 200, 'En astronaut med massan 90 kg svävar fritt i en rymdstation och knuffar en verktygslåda med massan 15 kg med kraften 45 N.')
def _():
    b = rekt(0, 0, 400, 200, '#eef2f7', 'none', 0, 0) + rekt(10, 10, 380, 180, 'none', '#b7bec4', 2, 18)
    b += ring(130, 70, 16, '#ffffff') + rekt(116, 86, 28, 50, '#ffffff', INK, 2, 8)
    b += linje(144, 100, 196, 100, INK, 3) + linje(122, 136, 112, 168, INK, 3) + linje(138, 136, 146, 168, INK, 3)
    b += rekt(200, 86, 44, 30, '#e07a5f', INK, 2, 3) + rekt(214, 80, 16, 8, '#5d6b75', INK, 1.4, 2)
    b += pil(250, 60, 320, 60, ROD, 3) + tt(326, 65, '45 N', 14, 'start', ROD, True)
    b += tt(130, 186, 'astronaut 90 kg', 12, 'middle', INK, True) + tt(222, 140, '15 kg', 12, 'middle', INK, True)
    return b


@fig('4.465', 420, 150, 'Två vagnar på ett friktionsfritt spår med en hoptryckt fjäder mellan sig. Vagn A har massan 2,0 kg och vagn B massan 3,0 kg.')
def _():
    b = linje(10, 128, 410, 128, INK, 3) + vagn(90, 128, 80, 40, '#5b9bd5', 'A') + vagn(240, 128, 100, 46, '#e07a5f', 'B')
    pts = ' '.join(f'{170 + i * 7.0:.1f},{98 + (8 if i % 2 else -8)}' for i in range(11))
    b += f'<polyline points="170,98 {pts} 240,98" fill="none" stroke="{GRA}" stroke-width="2"/>'
    b += tt(130, 40, '2,0 kg', 13, 'middle', BLA, True) + tt(290, 34, '3,0 kg', 13, 'middle', ORA, True)
    b += tt(205, 70, 'fjäder', 12, 'middle', GRA, True)
    return b


@fig('4.496', 440, 220, 'Två lådor i kontakt på ett friktionsfritt golv. Låda 1 väger 4,0 kg och låda 2 väger 6,0 kg. I a skjuts låda 1 med 20 N, i b skjuts låda 2 från andra hållet med 20 N.')
def _():
    b = ''
    for y, rubrik, fran_vanster in ((20, 'a)', True), (120, 'b)', False)):
        b += tt(20, y + 20, rubrik, 14, 'start', INK, True) + linje(40, y + 80, 420, y + 80, INK, 2)
        b += rekt(160, y + 40, 50, 40, '#f2c48d', INK, 1.8, 2) + tt(185, y + 65, '1', 14, 'middle', INK, True)
        b += rekt(210, y + 26, 70, 54, '#9cc3e4', INK, 1.8, 2) + tt(245, y + 58, '2', 14, 'middle', INK, True)
        if fran_vanster:
            b += pil(80, y + 60, 156, y + 60, ROD, 3) + tt(118, y + 50, '20 N', 13, 'middle', ROD, True)
        else:
            b += pil(360, y + 54, 284, y + 54, ROD, 3) + tt(322, y + 44, '20 N', 13, 'middle', ROD, True)
        b += tt(185, y + 32, '4,0 kg', 11, 'middle', GRA, True) + tt(245, y + 20, '6,0 kg', 11, 'middle', GRA, True)
    return b


@fig('4.501', 460, 150, 'Ett lok drar två vagnar med massan 40 ton vardera på ett horisontellt spår med accelerationen 0,50 m/s².')
def _():
    b = linje(10, 120, 450, 120, INK, 3)
    b += vagn(40, 120, 90, 40, '#c9d0d5', '40 ton') + linje(130, 98, 160, 98, INK, 3) + vagn(160, 120, 90, 40, '#c9d0d5', '40 ton')
    b += linje(250, 98, 280, 98, INK, 3)
    b += path('M280,110 L280,62 L330,62 L330,46 L360,46 L360,62 L380,72 L380,110 Z', '#e07a5f', INK, 2)
    b += cirkel(300, 114, 7, INK, '#fff', 1.4) + cirkel(356, 114, 7, INK, '#fff', 1.4) + tt(330, 92, 'lok', 13, 'middle', '#fff', True)
    b += pil(390, 40, 446, 40, GRON, 3) + tt(418, 30, 'a = 0,50 m/s²', 12, 'middle', GRON, True)
    b += tt(145, 140, 'koppling ?', 11, 'middle', ORA, True) + tt(265, 140, 'koppling ?', 11, 'middle', ORA, True)
    return b


@fig('4.896', 460, 160, 'Elsa drar en pulka med massan 20 kg med den horisontella kraften 90 N. En pulka med massan 10 kg är fäst med ett rep bakom.')
def _():
    b = rekt(0, 120, 460, 40, '#f3f7fa', 'none', 0, 0) + linje(0, 120, 460, 120, '#b7cad6', 2)
    for x, w, text in ((40, 90, '10 kg'), (180, 120, '20 kg')):
        b += path(f'M{x},{120 - 26} L{x + w},{120 - 26} L{x + w + 10},{120 - 6} L{x},{120 - 6} Z', '#5b9bd5', INK, 1.6)
        b += linje(x, 116, x + w + 10, 116, INK, 2) + tt(x + w / 2, 84, text, 13, 'middle', INK, True)
    b += linje(140, 106, 180, 106, ORA, 2) + tt(160, 98, 'rep', 11, 'middle', ORA, True)
    b += linje(310, 106, 370, 92, INK, 2) + gubbe(390, 120, INK, 0.9)
    b += pil(320, 52, 400, 52, ROD, 3) + tt(360, 42, '90 N', 13, 'middle', ROD, True)
    return b


@fig('4.894', 440, 150, 'En lastbil med massan 12 ton och en personbil med massan 1,2 ton krockar. Kraften från lastbilen på personbilen är i medel 60 kN.')
def _():
    b = rekt(10, 110, 420, 26, VAG, INK, 1.4, 2)
    b += rekt(60, 50, 120, 50, '#e9eef2', INK, 2, 2) + path('M180,62 L216,62 L226,78 L226,100 L180,100 Z', '#5b9bd5', INK, 2)
    for x in (80, 150, 210):
        b += cirkel(x, 106, 8, INK, '#fff', 1.6)
    b += bil(230, 110, '#e07a5f', 70)
    b += tt(140, 40, 'lastbil 12 ton', 13, 'middle', INK, True) + tt(265, 70, 'personbil 1,2 ton', 12, 'start', INK, True)
    b += pil(200, 24, 266, 24, ROD, 3) + tt(272, 29, '60 kN på personbilen', 12, 'start', ROD, True)
    return b


# ================================================================ normalkraft
@fig('4.477', 340, 210, 'En träningsvikt med massan 10 kg står på golvet. Kevin drar rakt uppåt i handtaget med kraften 40 N.')
def _():
    b = golv(340, 180)
    b += path('M130,180 C110,180 104,150 116,130 C126,114 154,114 164,130 C176,150 170,180 150,180 Z', '#3d4a54', INK, 2)
    b += path('M124,124 C124,90 156,90 156,124', 'none', '#3d4a54', 8) + tt(140, 160, '10 kg', 13, 'middle', '#fff', True)
    b += pil(140, 96, 140, 36, ROD, 3) + tt(150, 56, '40 N', 14, 'start', ROD, True)
    return b


@fig('4.478', 340, 200, 'Två böcker ligger staplade på ett bord. Den undre boken har massan 1,2 kg och den övre 0,80 kg.')
def _():
    b = rekt(40, 150, 260, 14, '#b98b5a', INK, 2, 2) + rekt(60, 164, 14, 30, '#9b6f43', INK, 1.4, 0) + rekt(266, 164, 14, 30, '#9b6f43', INK, 1.4, 0)
    b += rekt(110, 114, 130, 36, '#5b9bd5', INK, 2, 3) + tt(175, 138, '1,2 kg', 13, 'middle', '#fff', True)
    b += rekt(126, 86, 100, 28, '#e07a5f', INK, 2, 3) + tt(176, 106, '0,80 kg', 13, 'middle', '#fff', True)
    return b


@fig('4.502', 460, 190, 'En låda med massan 20 kg står på golvet. I a dras den i ett rep med 80 N snett uppåt, 30° över horisontellt. I b trycks den med 80 N snett nedåt, 30° under horisontellt.')
def _():
    b = golv(460, 150)
    b += linje(248, 20, 248, 150, '#c9d3da', 1.5, '4 4')
    for x0, rubrik, upp in ((20, 'a)', True), (250, 'b)', False)):
        bx = x0 + 40 if upp else x0 + 120
        b += tt(x0, 30, rubrik, 14, 'start', INK, True)
        b += rekt(bx, 100, 70, 50, '#f2c48d', INK, 2, 2) + tt(bx + 35, 130, '20 kg', 12, 'middle', INK, True)
        th = math.radians(30)
        if upp:
            sx, sy = x0 + 110, 112
            ex, ey = sx + 90 * math.cos(th), sy - 90 * math.sin(th)
            b += pil(sx, sy, ex, ey, ROD, 3) + tt(ex + 4, ey - 4, '80 N', 13, 'start', ROD, True)
            b += linje(sx, sy, sx + 70, sy, GRA, 1.2, '4 3')
            b += tt(sx + 56, sy - 6, '30°', 12, 'start', ORA, True)
        else:
            ex, ey = x0 + 120, 112
            sx, sy = ex - 90 * math.cos(th), ey - 90 * math.sin(th)
            b += pil(sx, sy, ex, ey, ROD, 3) + tt((sx + ex) / 2 + 8, (sy + ey) / 2 - 16, '80 N', 13, 'start', ROD, True)
            b += linje(ex - 70, ey, ex, ey, GRA, 1.2, '4 3') + tt(ex - 64, ey - 6, '30°', 12, 'start', ORA, True)
    return b


@fig('4.207', 420, 240, 'En vikt står på en våg som visar 423 g. En dynamometer drar sedan vertikalt uppåt i vikten tills vågen visar 257 g.', kort=['a'])
def _():
    b = ''
    for x0, visn, dyn in ((40, '423 g', False), (240, '257 g', True)):
        b += D.vag(x0 + 70, 190, visn)
        b += rekt(x0 + 50, 150, 40, 40, '#8c969e', INK, 2, 3)
        if dyn:
            b += linje(x0 + 70, 150, x0 + 70, 116, INK, 2) + rekt(x0 + 60, 30, 20, 86, '#f7fafc', INK, 1.8, 6)
            for y in range(40, 112, 10):
                b += linje(x0 + 62, y, x0 + 70, y, GRA, 1)
            b += tt(x0 + 90, 74, 'dynamometer', 12, 'start', INK, True) + tt(x0 + 90, 92, 'visar ?', 12, 'start', ORA, True)
        b += tt(x0 + 70, 20 if not dyn else 18, 'före' if not dyn else 'när dynamometern drar', 12, 'middle', GRA, True)
    return b


@fig('4.217', 300, 260, 'En person med massan 68 kg står på en våg i en hiss. Vågen visar 75 kg.')
def _():
    b = rekt(60, 20, 180, 220, '#eef2f5', INK, 3, 4) + linje(150, 0, 150, 20, INK, 2)
    b += gubbe(150, 200, INK, 1.4) + rekt(110, 200, 80, 14, '#dfe6ec', INK, 1.6, 4)
    b += rekt(126, 216, 48, 18, '#1f2d36', INK, 1.2, 3) + tt(150, 230, '75 kg', 12, 'middle', '#9ff0b4', True)
    b += tt(150, 254, 'personen: 68 kg', 12, 'middle', INK, True) + tt(262, 130, 'a = ?', 14, 'middle', ORA, True)
    return b


@fig('4.646', 320, 260, 'Två vikter med massan 3,50 kg var hänger under varandra i snören från taket i en hiss. Det övre snöret bär båda vikterna.')
def _():
    b = rekt(60, 20, 200, 230, '#eef2f5', INK, 3, 4) + rekt(60, 20, 200, 12, '#8c969e', INK, 2, 0)
    b += linje(160, 32, 160, 90, INK, 2) + rekt(136, 90, 48, 40, '#5b9bd5', INK, 2, 3) + tt(160, 115, '3,50 kg', 11, 'middle', '#fff', True)
    b += linje(160, 130, 160, 170, INK, 2) + rekt(136, 170, 48, 40, '#5b9bd5', INK, 2, 3) + tt(160, 195, '3,50 kg', 11, 'middle', '#fff', True)
    b += tt(170, 64, 'övre snöret', 11, 'start', ORA, True) + tt(170, 154, 'nedre snöret', 11, 'start', GRA, True)
    return b


@fig('4.642', 360, 250, 'En fisk med massan 5,0 kg hänger i en lina 1,8 m under en brygga. Linan tål högst 54 N.')
def _():
    b = f'<rect x="0" y="150" width="360" height="100" fill="{VATTEN}"/>' + linje(0, 150, 360, 150, BLA, 2)
    b += rekt(0, 40, 200, 16, '#b98b5a', INK, 2, 2) + rekt(30, 56, 12, 120, '#9b6f43', INK, 1.4, 0) + rekt(160, 56, 12, 120, '#9b6f43', INK, 1.4, 0)
    b += linje(120, 40, 120, 200, INK, 1.4)
    b += path('M100,206 C110,196 132,196 140,206 L150,198 L150,214 L140,206 C132,216 110,216 100,206 Z', '#9aa4ab', INK, 1.6)
    b += matt_v(240, 40, 206, '1,8 m') + tt(130, 236, 'fisk 5,0 kg', 12, 'middle', INK, True)
    b += tt(300, 30, 'linan tål', 12, 'middle', ORA, True) + tt(300, 46, 'högst 54 N', 12, 'middle', ORA, True)
    return b


@fig('4.816', 340, 200, 'Moa trycker en bok horisontellt mot en vägg med kraften 30 N. Boken hålls stilla.')
def _():
    b = rekt(250, 0, 90, 200, '#d9d3c7', 'none', 0, 0) + linje(250, 0, 250, 200, INK, 2)
    for y in range(10, 200, 24):
        b += linje(252, y, 268, y + 14, '#b7ad97', 1)
    b += rekt(232, 60, 18, 80, '#e07a5f', INK, 2, 2) + tt(222, 156, 'bok', 12, 'middle', INK, True)
    b += path('M150,92 L226,92 L230,100 L226,108 L150,108 Z', '#f0c9a8', INK, 1.6)
    b += pil(80, 70, 180, 70, ROD, 3) + tt(130, 60, '30 N', 14, 'middle', ROD, True)
    return b


# ================================================================ gravitation
@fig('4.74', 400, 270, 'Jorden med radien 6371 km och en satellit 400 km över jordytan. Satellitens avstånd från jordens centrum är okänt.', kort=['b', 'c'])
def _():
    cx, cy, R = 150, 160, 100
    b = ring(cx, cy, R, '#7fb3d5') + tt(cx, cy + 40, 'jorden', 13, 'middle', '#1f4e6e', True)
    sx, sy = cx + R + 70, cy - 70
    b += linje(cx, cy, sx, sy, GRA, 1.4, '5 4') + cirkel(cx, cy, 3.5, INK, INK, 1)
    ang = math.atan2(cy - sy, sx - cx)
    px, py = cx + R * math.cos(ang), cy - R * math.sin(ang)
    b += linje(cx, cy, px, py, INK, 2) + tt(cx + 12, cy + 24, 'R = 6371 km', 12, 'start', INK, True, halo=True)
    b += linje(px, py, sx, sy, ROD, 2.6) + tt((px + sx) / 2 + 10, (py + sy) / 2 + 14, '400 km', 12, 'start', ROD, True, halo=True)
    b += rekt(sx - 8, sy - 8, 16, 16, '#d9dde1', INK, 1.6, 2) + linje(sx - 20, sy, sx + 20, sy, '#3a6ea5', 4)
    b += tt(sx + 4, sy - 18, 'satellit 1200 kg', 12, 'middle', INK, True)
    b += tt(150, 36, 'avstånd från centrum till satelliten ?', 12, 'middle', ORA, True, halo=True)
    return b


@fig('4.354', 300, 290, 'En planet med radien R och en sond på höjden R över planetens yta.')
def _():
    cx, cy, R = 150, 200, 76
    b = ring(cx, cy, R, '#c9a27a') + cirkel(cx, cy, 3.5, INK, INK, 1)
    b += linje(cx, cy, cx, cy - R, INK, 2) + tt(cx + 8, cy - R / 2 + 5, 'R', 15, 'start', INK, True, italic=True, halo=True)
    b += linje(cx, cy - R, cx, cy - 2 * R, ROD, 2.4) + tt(cx + 8, cy - 1.5 * R + 5, 'R', 15, 'start', ROD, True, italic=True, halo=True)
    b += rekt(cx - 9, cy - 2 * R - 18, 18, 18, '#d9dde1', INK, 1.6, 2) + tt(cx + 16, cy - 2 * R - 6, 'sond', 13, 'start', INK, True)
    b += cirkel(cx, cy - R, 3, ROD, ROD, 1) + tt(cx - 10, cy - R - 6, 'ytan', 11, 'end', GRA, True)
    return b


@fig('4.379', 460, 170, 'Två planeter med massorna 5,0·10²⁴ kg och 1,6·10²⁴ kg och centrumavståndet 85 000 km. Punkten där gravitationsfälten tar ut varandra ligger mellan dem.')
def _():
    x1, x2, y = 70, 400, 80
    b = rekt(0, 0, 460, 170, '#1d2733', 'none', 0, 0)
    b += ring(x1, y, 40, '#5b9bd5', '#cfe6f5', 2) + ring(x2, y, 24, '#e07a5f', '#f8d3c8', 2)
    b += tt(x1, y + 5, 'M₁', 15, 'middle', '#fff', True) + tt(x2, y + 5, 'M₂', 14, 'middle', '#fff', True)
    xp = x1 + (x2 - x1) * 0.52  # schematiskt, inte skalenligt (svaret är 0,639 av avståndet)
    b += cirkel(xp, y, 5, '#f9c74f', '#fff', 1.4) + tt(xp, y - 14, 'P', 14, 'middle', '#f9c74f', True)
    b += linje(x1, 130, x2, 130, '#cfe6f5', 1.5) + linje(x1, 124, x1, 136, '#cfe6f5', 1.5) + linje(x2, 124, x2, 136, '#cfe6f5', 1.5)
    b += tt((x1 + x2) / 2, 152, '85 000 km', 13, 'middle', '#ffffff', True)
    b += linje(x1, 108, xp, 108, '#f9c74f', 1.5, '5 4') + tt((x1 + xp) / 2, 102, 'x = ?', 13, 'middle', '#f9c74f', True)
    b += tt(x1, 30, '5,0·10²⁴ kg', 12, 'middle', '#cfe6f5', True) + tt(x2, 42, '1,6·10²⁴ kg', 12, 'middle', '#f8d3c8', True)
    return b


@fig('4.753', 440, 160, 'Två föremål med massorna 200 kg och 500 kg är 2,00 m från varandra. En sten med massan 50 kg ligger på linjen mellan dem.')
def _():
    x1, x2, y = 60, 380, 80
    b = ring(x1, y, 26, '#9aa4ab') + ring(x2, y, 36, '#6b7a86') + tt(x1, y + 5, '200 kg', 11, 'middle', '#fff', True) + tt(x2, y + 5, '500 kg', 12, 'middle', '#fff', True)
    b += path('M214,90 C208,80 214,70 222,70 C232,70 236,80 230,90 Z', '#8f8a82', INK, 1.4) + tt(222, 60, 'sten 50 kg', 12, 'middle', INK, True)
    b += matt_h(x1, x2, 140, '2,00 m', under=False)
    return b


@fig('4.738', 360, 170, 'Två identiska bollar med radien 12 cm ligger så att de nuddar varandra.')
def _():
    b = linje(10, 150, 350, 150, INK, 2)
    for cx in (120, 240):
        b += ring(cx, 90, 60, '#e9a33b')
        b += cirkel(cx, 90, 3, INK, INK, 1)
    b += linje(120, 90, 120 - 60, 90, INK, 1.6, '5 4') + tt(90, 82, '12 cm', 12, 'middle', INK, True, halo=True)
    return b


@fig('4.739', 400, 270, 'Jorden är lite tillplattad: radien är 6 378 km vid ekvatorn och 6 357 km vid nordpolen. Tillplattningen är överdriven i figuren.')
def _():
    cx, cy = 180, 140
    b = ellips(cx, cy, 120, 100, '#7fb3d5', INK, 2) + cirkel(cx, cy, 3.5, INK, INK, 1)
    b += linje(cx, cy, cx + 120, cy, INK, 1.8, '5 4') + tt(cx + 60, cy - 8, '6 378 km', 12, 'middle', INK, True, halo=True)
    b += linje(cx, cy, cx, cy - 100, ROD, 1.8, '5 4') + tt(cx + 8, cy - 56, '6 357 km', 12, 'start', ROD, True, halo=True)
    b += gubbe(cx, cy - 100, INK, 0.5) + tt(cx + 12, cy - 112, 'nordpolen', 12, 'start', INK, True)
    b += cirkel(cx + 120, cy, 4, ROD, INK, 1) + tt(cx + 128, cy + 20, 'ekvatorn', 12, 'start', INK, True)
    b += tt(cx, 262, 'tillplattningen är överdriven', 11, 'middle', GRA)
    return b


@fig('4.188', 460, 170, 'Två fartyg med massan 5,0·10⁷ kg vardera. Avståndet mellan deras masscentrum är 200 m.')
def _():
    b = f'<rect x="0" y="110" width="460" height="60" fill="{VATTEN}"/>' + linje(0, 110, 460, 110, BLA, 2)
    for x in (30, 290):
        b += path(f'M{x},96 L{x + 140},96 L{x + 124},124 L{x + 14},124 Z', '#5d6b75', INK, 2) + rekt(x + 40, 72, 50, 24, '#e9eef2', INK, 1.6, 2)
        b += cirkel(x + 70, 104, 3.5, '#f9c74f', INK, 1)
    b += linje(100, 150, 360, 150, INK, 1.5) + linje(100, 144, 100, 156, INK, 1.5) + linje(360, 144, 360, 156, INK, 1.5)
    b += tt(230, 144, '200 m mellan masscentrum', 12, 'middle', INK, True, halo=True)
    b += tt(100, 60, '5,0·10⁷ kg', 12, 'middle', INK, True) + tt(360, 60, '5,0·10⁷ kg', 12, 'middle', INK, True)
    return b


# ================================================================ tyngdkraft
def kraftmatare(x, y_topp, visn, vikt_text, fill='#8c969e'):
    b = linje(x, y_topp - 20, x, y_topp, INK, 2) + rekt(x - 12, y_topp, 24, 90, '#f7fafc', INK, 1.8, 6)
    for yy in range(y_topp + 10, y_topp + 84, 10):
        b += linje(x - 10, yy, x - 2, yy, GRA, 1)
    b += linje(x, y_topp + 90, x, y_topp + 110, INK, 2) + rekt(x - 18, y_topp + 110, 36, 30, fill, INK, 1.8, 3)
    b += tt(x, y_topp + 130, vikt_text, 11, 'middle', '#fff', True)
    b += tt(x + 20, y_topp + 48, visn, 13, 'start', ORA, True)
    return b


@fig('4.474', 300, 210, 'På en planet hänger en vikt med massan 4,0 kg stilla i en kraftmätare som visar 14,8 N.')
def _():
    b = rekt(80, 10, 140, 10, '#5d6b75', INK, 1.6, 2) + kraftmatare(150, 40, 'visar 14,8 N', '4,0 kg')
    return b


@fig('4.498', 440, 230, 'Samma föremål vägs på månen. a) I en fjädervåg, som på jorden visar 4,90 N. b) På en balansvåg, där det jämförs med vikter.')
def _():
    b = tt(20, 24, 'a)', 14, 'start', INK, True) + tt(240, 24, 'b)', 14, 'start', INK, True)
    b += rekt(50, 30, 120, 8, '#5d6b75', INK, 1.4, 2) + kraftmatare(110, 58, 'på jorden: 4,90 N', '', '#e07a5f')
    b += tt(110, 224, 'på månen: ?', 12, 'middle', ORA, True)
    b += path('M310,190 L300,210 L360,210 L350,190 Z', '#9aa4ab', INK, 1.6) + linje(330, 190, 330, 90, INK, 3) + linje(260, 90, 400, 90, INK, 3)
    b += path('M310,86 L330,74 L350,86', 'none', INK, 2)
    for x, fill, text in ((262, '#e07a5f', 'föremål'), (398, '#9aa4ab', 'vikter')):
        b += linje(x, 90, x - 20, 130, GRA, 1.4) + linje(x, 90, x + 20, 130, GRA, 1.4) + path(f'M{x - 28},130 L{x + 28},130 L{x + 20},140 L{x - 20},140 Z', '#c9d0d5', INK, 1.4)
        b += rekt(x - 12, 114, 24, 16, fill, INK, 1.2, 2) + tt(x, 158, text, 12, 'middle', INK, True)
    b += tt(330, 224, 'massa ?', 12, 'middle', ORA, True)
    return b


@fig('4.887', 380, 230, 'Samma föremål hänger i en kraftmätare. På jorden visar kraftmätaren 12,0 N och på månen 2,03 N.')
def _():
    b = rekt(20, 10, 160, 10, '#5d6b75', INK, 1.6, 2) + rekt(200, 10, 160, 10, '#5d6b75', INK, 1.6, 2)
    b += kraftmatare(90, 40, '12,0 N', '', '#e07a5f') + kraftmatare(270, 40, '2,03 N', '', '#e07a5f')
    b += tt(100, 210, 'på jorden', 13, 'middle', BLA, True) + tt(280, 210, 'på månen', 13, 'middle', GRA, True)
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
        assert q['kap'] == 4, uid
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
