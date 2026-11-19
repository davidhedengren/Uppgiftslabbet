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


# ---------------------------------------------------------------- inläggning
def efter_forsta_stycket(html, figur):
    i = html.index('</p>') + 4
    return html[:i] + figur + html[i:]


def med_figur(q, figur):
    q = json.loads(json.dumps(q))
    kort = KORT.get(q['id'])  # None: alla delkort
    q['t'] = efter_forsta_stycket(q['t'], figur)
    if q.get('spelIntro') and kort is None:
        q['spelIntro'] = q['spelIntro'] + figur
    for d in q.get('spelDelar') or []:
        if d.get('t') and (kort is None or d['etikett'] in kort):
            d['t'] = efter_forsta_stycket(d['t'], figur)
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
