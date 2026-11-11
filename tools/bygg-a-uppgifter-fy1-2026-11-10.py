"""Fysik 1 (uppgifter.js): åtta välkonstruerade A-uppgifter på träningsnivå 4–5 i centrala områden, 10 november 2026.

Varje uppgift är handskriven med egen situation, figur och facit enligt agent/FACITMALL.md (givet och sökt, formeln i
rubriken, insättning med enheter, svarsrad). Alla tal räknas i skriptet och kontrolleras med assert.
Se agent/A_UPPGIFTER_2026-11-10.md.

  python tools/bygg-a-uppgifter-fy1-2026-11-10.py [--skriv] [--varianter fil.json]
"""
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import (m, mt, al, p, li, del_, Plot, svg, tt, linje, pil, polygon, rekt, cirkel, tx, sv,  # noqa: E402
                               BLA, ORA, GRON, GRA, INK, ROD, LJUS)

BANK = 'uppgifter.js'
VARIANTER = {}
g = 9.82
NYCKEL = {}
GIVET = 'Givet och sökt'


def U(x):
    return f'\\ \\mathrm{{{x}}}'


def sokt(steg, text):
    """Lägger till vad som söks sist i steget Givet och sökt."""
    assert steg.endswith('</li>')
    return steg[:-5] + p('Sökt: ' + text) + '</li>'


def fjader(x1, x2, y, varv=7, amp=8):
    """Sicksackfjäder mellan x1 och x2."""
    pts = [(x1, y)]
    n = varv * 2
    for i in range(1, n):
        pts.append((x1 + (x2 - x1) * i / n, y + (amp if i % 2 else -amp)))
    pts.append((x2, y))
    return f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>'


# ================================================================ P1: persontåg bakom godståg (konstacc, möte och ikapp)
def p1(uid):
    v1, v2, s0, tr = 108 / 3.6, 36 / 3.6, 600.0, 1.0
    gap = s0 - (v1 - v2) * tr
    a = (v1 - v2) ** 2 / (2 * gap)
    t = (v1 - v2) / a
    assert gap == 580 and abs(a - 200 / 580) < 1e-12 and abs(t - 58) < 1e-9
    # Gränsfallet: lägena är lika precis när farterna är lika.
    assert abs((v1 * t - a * t * t / 2) - (gap + v2 * t)) < 1e-9 and abs(v1 - a * t - v2) < 1e-9

    def fig():
        b = linje(16, 118, 444, 118, GRA, 3)
        b += rekt(28, 84, 120, 34, '#dbe9f4') + tt(88, 106, 'Persontåg', 14)
        b += rekt(312, 84, 120, 34, '#f3e3d3') + tt(372, 106, 'Godståg', 14)
        b += pil(52, 66, 136, 66, GRON, 3) + tt(94, 56, '108 km/h', 14, fill=GRON, bold=True)
        b += pil(346, 66, 398, 66, GRON, 3) + tt(372, 56, '36 km/h', 14, fill=GRON, bold=True)
        b += linje(148, 146, 312, 146, INK, 1.6) + linje(148, 138, 148, 154, INK, 1.6) + linje(312, 138, 312, 154, INK, 1.6)
        b += tt(230, 166, '600 m', 14)
        return svg(460, 178, b, 'Ett persontåg kör i 108 km/h på ett spår. 600 m längre fram på samma spår kör ett godståg åt samma håll i 36 km/h.')

    def graf():
        P = Plot(0, 80, 0, 1600, W=420, H=310, ml=56).axlar(xt=range(0, 81, 20), yt=range(0, 1601, 400), xlabel='t (s)', ylabel='s (m)')
        P.kurva(lambda u: gap + v2 * u, color=ORA).kurva(lambda u: v1 * u - a * u * u / 2, color=BLA)
        P.streck(58, 0, 58, 1160).punkt(58, 1160, 't = 58 s', -10, -10, INK, 'end')
        P.text(9, 830, 'godståget', ORA, 14, 'start', True).text(30, 520, 'persontåget', BLA, 14, 'start', True)
        return P.svg('Lägena som funktion av tiden från att bromsningen börjar. Persontågets kurva når precis upp till godstågets '
                     'räta linje vid t = 58 s och ligger annars under den.')

    intro = (p('Ett persontåg kör i 108 km/h på ett rakt spår. Föraren upptäcker ett godståg 600 m längre fram på samma spår. '
               'Godståget kör åt samma håll med den konstanta farten 36 km/h. Förarens reaktionstid är 1,0 s. Därefter bromsar '
               'persontåget med konstant retardation.') + fig())
    givet = li(GIVET, al(r'v_1=108\ \mathrm{km/h}=30\ \mathrm{m/s}', r'v_2=36\ \mathrm{km/h}=10\ \mathrm{m/s}', r't_r=1{,}0\ \mathrm s'),
               p('Positiv riktning är färdriktningen.'))
    steg_a = [sokt(givet, 'avståndet mellan tågen när bromsningen börjar.'),
              li(r'Konstant fart under reaktionstiden: \(s=vt\)', al(r's_1=30\cdot1{,}0=30\ \mathrm m', r's_2=10\cdot1{,}0=10\ \mathrm m')),
              li('Avståndet minskar med skillnaden mellan sträckorna', mt(r'600-(30-10)=580\ \mathrm m'))]
    steg_b = [sokt(givet, 'den minsta retardationen.'),
              li('Avståndet när bromsningen börjar', p('Under reaktionstiden kör persontåget 30 m och godståget 10 m.'),
                 mt(r'600-(30-10)=580\ \mathrm m')),
              li('Farligaste ögonblicket: när tågen har samma fart',
                 p('Så länge persontåget är snabbare än godståget krymper avståndet. När farterna är lika är avståndet som minst. '
                   'I gränsfallet är avståndet då precis noll.')),
              li(r'Hastighetsformeln: \(v=v_0+at\) ger tiden till samma fart',
                 p(r'Kalla retardationens storlek för \(a\), så att persontågets acceleration är \(-a\).'), al(r'10=30-at', r't=\frac{20}{a}')),
              li(r'Sträckformeln: \(s=v_0t+\tfrac{at^2}{2}\) för persontåget och \(s=vt\) för godståget',
                 p('I gränsfallet har persontåget kört precis 580 m längre än godståget.'),
                 al(r'30t-\frac{at^2}{2}=580+10t', r'20t-\frac{at^2}{2}=580')),
              li(r'Sätt in \(t=\tfrac{20}{a}\) och lös ut \(a\)',
                 al(r'\frac{400}{a}-\frac{200}{a}=580', r'\frac{200}{a}=580', r'a=\frac{200}{580}\approx0{,}345\ \mathrm{m/s^2}')),
              li('Grafisk kontroll: lägena som funktion av tiden',
                 p(r'Tiden räknas från att bromsningen börjar. Med \(a=0{,}345\ \mathrm{m/s^2}\) når persontågets kurva precis upp till godstågets linje efter 58 s. '
                   'Med större retardation möts kurvorna aldrig.'), graf()),
              li(r'Alternativ: räkna relativt godståget med tidlösa formeln \(v^2=v_0^2+2as\)',
                 p('Sett från godståget närmar sig persontåget med 20 m/s och ska stanna på 580 m.'),
                 al(r'0=20^2-2a\cdot580', r'a=\frac{400}{1160}\approx0{,}345\ \mathrm{m/s^2}'))]
    delar = [
        del_('Hur långt är det mellan tågen när persontåget börjar bromsa?', steg_a, '580 m.',
             'Båda tågen rör sig under reaktionstiden. Hur mycket längre hinner persontåget än godståget?',
             int(gap), 'C', 3, (0, 1, 0), tol=0.5, enhet='m', vs=None, ratt_txt=['580', '580 m'], fel=['570', '600', '590']),
        del_('Vilken är den minsta retardation som gör att tågen inte kolliderar?', steg_b, '0,345 m/s².',
             'Persontåget behöver inte stanna. I vilket ögonblick är avståndet mellan tågen som minst?',
             a, 'A', 5, (0, 0, 2), tol=0.0005, enhet='m/s²', vs=3, ai=3,
             ratt_txt=['0,345', '0,34', '0,3448', '0,345 m/s²'], fel=['0,78', '0,75', '0,69', '0,4']),
    ]
    return H.bygg(uid, 3, 'konstacc', 'Möte och ikapp', intro, delar, ('problemlösning',), True, False,
                  'Räkna om farterna till m/s. Tänk på att godståget också rör sig hela tiden.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['konstacc|Möte och ikapp'])


# ================================================================ P2: hiss med våg (newton2)
def p2(uid):
    mm = 70.0
    a1 = (82 - 70) * g / mm
    v = a1 * 2.5
    s1 = a1 * 2.5 ** 2 / 2
    s2 = v * 6.0
    a3 = (61 - 70) * g / mm
    t3 = v / -a3
    s3 = v ** 2 / (2 * -a3)
    tot = s1 + s2 + s3
    assert abs(a1 - 1.683429) < 1e-6 and abs(v - 4.208571) < 1e-6 and abs(tot - 37.526429) < 1e-5 and abs(t3 - 10 / 3) < 1e-9
    assert abs(tot - (0.5 * 2.5 * v + 6.0 * v + 0.5 * t3 * v)) < 1e-9  # arean under v–t-grafen

    def fig():
        b = rekt(34, 18, 112, 160, '#f6f9fb') + rekt(66, 150, 48, 10, '#cfd8df')
        b += cirkel(90, 70, 11, '#fff', INK, 2) + linje(90, 81, 90, 124) + linje(90, 92, 74, 108) + linje(90, 92, 106, 108)
        b += linje(90, 124, 78, 150) + linje(90, 124, 102, 150)
        b += pil(166, 150, 166, 46, GRON, 3) + tt(172, 40, 'uppåt', 14, 'start', GRON, True)
        b += tt(90, 196, 'våg', 13, fill=GRA)
        for i, (tid, kg) in enumerate((('de första 2,5 s', '82 kg'), ('därefter i 6,0 s', '70 kg'), ('tills hissen stannar', '61 kg'))):
            y = 34 + i * 48
            b += rekt(236, y, 204, 38, '#fff', GRA, 1.4) + tt(246, y + 24, tid, 13.5, 'start') + tt(430, y + 24, kg, 15, 'end', BLA, True)
        b += tt(338, 22, 'Vågen visar', 14, bold=True)
        return svg(456, 206, b, 'En person står på en våg i en hiss som åker uppåt. Vågen visar 82 kg under 0 till 2,5 s, därefter 70 kg '
                                'i 6,0 s och sedan 61 kg tills hissen stannar.')

    def graf():
        P = Plot(0, 13, 0, 5.5, W=420, H=290).axlar(xt=range(0, 13, 2), yt=range(0, 6), xlabel='t (s)', ylabel='v (m/s)')
        f = lambda u: a1 * u if u <= 2.5 else (v if u <= 8.5 else max(0.0, v + a3 * (u - 8.5)))
        P.fyll(f, lambda u: 0, 0, 8.5 + t3, BLA, 0.18).kurva(f, 0, 8.5 + t3, BLA)
        P.streck(2.5, 0, 2.5, v).streck(8.5, 0, 8.5, v)
        P.text(1.6, 0.6, 's₁', INK, 15, 'middle', True).text(5.5, 2.0, 's₂', INK, 15, 'middle', True).text(9.5, 0.9, 's₃', INK, 15, 'middle', True)
        return P.svg('Hissens fart som funktion av tiden. Farten ökar jämnt till 4,2 m/s på 2,5 s, är konstant i 6,0 s och minskar sedan '
                     'jämnt till noll på 3,3 s. Sträckan är arean under grafen.')

    intro = (p('Elsa, som väger 70 kg, står på en badrumsvåg i en hiss. Hissen startar från vila på bottenvåningen och åker uppåt. '
               'Vågen visar 82 kg under de första 2,5 s, därefter 70 kg i 6,0 s och till sist 61 kg tills hissen stannar.') + fig())
    givet = li(GIVET, p('Vågen mäter normalkraften. När den visar 82 kg är normalkraften lika stor som tyngden av 82 kg. '
                        'Positiv riktning är uppåt.'),
               al(r'N=82\cdot9{,}82=805{,}2\ \mathrm N', r'mg=70\cdot9{,}82=687{,}4\ \mathrm N'))
    n2 = li(r'Newtons andra lag: \(F_R=ma\) med \(F_R=N-mg\)',
            mt(rf'a_1=\frac{{805{{,}}2-687{{,}}4}}{{70}}\approx{tx(a1, 2)}\ \mathrm{{m/s^2}}'))
    fart = li(r'Hastighetsformeln: \(v=v_0+at\) från vila', mt(rf'v={tx(a1, 3)}\cdot2{{,}}5\approx{tx(v, 2)}\ \mathrm{{m/s}}'))
    steg_a = [sokt(givet, 'accelerationen under de första 2,5 s.'), n2]
    steg_b = [sokt(givet, 'hissens högsta fart.'), n2, fart,
              li('Därefter ökar farten inte mer', p('När vågen visar 70 kg är normalkraften lika stor som tyngdkraften, så farten är '
                                                    'konstant. När vågen visar 61 kg bromsar hissen. Den högsta farten nås alltså efter 2,5 s.'))]
    steg_c = [sokt(givet, 'hur högt hissen har åkt när den stannar.'), n2, fart,
              li(r'Sträckformeln från vila: \(s=\tfrac{at^2}{2}\) under accelerationen',
                 mt(rf's_1=\frac{{{tx(a1, 3)}\cdot2{{,}}5^2}}{{2}}\approx{tx(s1, 2)}\ \mathrm m')),
              li(r'Konstant fart: \(s=vt\) medan vågen visar 70 kg', mt(rf's_2={tx(v, 3)}\cdot6{{,}}0\approx{tx(s2, 2)}\ \mathrm m')),
              li(r'Newtons andra lag under inbromsningen: \(a=\tfrac{N-mg}{m}\)', p('Nu visar vågen 61 kg, så normalkraften är mindre än tyngdkraften.'),
                 al(r'a_3=\frac{(61-70)\cdot9{,}82}{70}', rf'a_3\approx{tx(a3, 3)}\ \mathrm{{m/s^2}}')),
              li(r'Tidlösa formeln: \(v^2=v_0^2+2as\) tills hissen står stilla',
                 al(rf'0={tx(v, 3)}^2-2\cdot{tx(-a3, 3)}\cdot s_3', rf's_3\approx{tx(s3, 2)}\ \mathrm m')),
              li('Lägg ihop de tre sträckorna', mt(rf's={tx(s1, 2)}+{tx(s2, 2)}+{tx(s3, 2)}\approx{tx(tot, 1)}\ \mathrm m'),
                 p('De givna värdena har två värdesiffror, så svaret avrundas till 38 m.')),
              li('Kontroll: sträckan är arean under v–t-grafen', graf())]
    delar = [
        del_('Hur stor är hissens acceleration under de första 2,5 s?', steg_a, '1,7 m/s².',
             'Vågen visar hur stor normalkraften är. Vilka krafter verkar på Elsa?', a1, 'C', 3, (0, 1, 0), tol=0.05,
             enhet='m/s²', vs=2, ratt_txt=['1,7', '1,68', '1,7 m/s²'], fel=['11,5', '1,2', '9,82']),
        del_('Vilken är hissens högsta fart?', steg_b, '4,2 m/s.',
             'Under vilken del av resan ökar farten? Bestäm accelerationen där med Newtons andra lag.', v, 'C', 3, (0, 1, 0),
             tol=0.05, enhet='m/s', vs=2, ratt_txt=['4,2', '4,21', '4,2 m/s'], fel=['2,5', '1,7', '14,3']),
        del_('Hur högt över bottenvåningen stannar hissen?', steg_c, '38 m.',
             'Dela upp resan i tre delar: acceleration, konstant fart och inbromsning. Bestäm sträckan för varje del.',
             tot, 'A', 5, (0, 0, 2), tol=0.5, enhet='m', vs=2, ai=3, ratt_txt=['38', '37,5', '38 m', '37,53'],
             fel=['30', '25', '45', '31']),
    ]
    return H.bygg(uid, 4, 'newton2', 'F = ma', intro, delar, ('problemlösning', 'modellering'), True, False,
                  'Vågen visar inte Elsas massa utan hur stor normalkraften är.', VARIANTER, fy=True, familjnyckel=NYCKEL['newton2|F = ma'])


# ================================================================ P3: kloss upp och ned för lutande plan
def p3(uid):
    al_, mu, v0 = math.radians(25), 0.30, 6.0
    au = g * (math.sin(al_) + mu * math.cos(al_))
    s = v0 ** 2 / (2 * au)
    an = g * (math.sin(al_) - mu * math.cos(al_))
    v = math.sqrt(2 * an * s)
    assert abs(au - 6.820091) < 1e-5 and abs(s - 2.639261) < 1e-5 and abs(an - 1.480126) < 1e-5 and abs(v - 2.795153) < 1e-5
    assert math.tan(al_) > mu
    # Energikontroll: friktionens arbete upp och ned är skillnaden i rörelseenergi (per kg).
    assert abs((v0 ** 2 - v ** 2) / 2 - 2 * mu * g * math.cos(al_) * s) < 1e-9

    def fig(krafter):
        x0, y0, L = 40, 210, 380
        x1, y1 = x0 + L * math.cos(al_), y0 - L * math.sin(al_)
        b = polygon([(x0, y0), (x1, y0), (x1, y1)], '#f2f5f8', INK)
        ux, uy = math.cos(al_), -math.sin(al_)       # uppför planet
        nx, ny = -math.sin(al_), -math.cos(al_)      # ut från planet
        lage = 215 if krafter else 150
        cx, cy = x0 + lage * ux, y0 + lage * uy
        hörn = [(cx - 28 * ux, cy - 28 * uy), (cx + 28 * ux, cy + 28 * uy), (cx + 28 * ux + 34 * nx, cy + 28 * uy + 34 * ny),
                (cx - 28 * ux + 34 * nx, cy - 28 * uy + 34 * ny)]
        b += polygon(hörn, '#dbe9f4', INK)
        mx, my = cx + 17 * nx, cy + 17 * ny
        b += f'<path d="M {x0 + 62:.1f} {y0} A 62 62 0 0 0 {x0 + 62 * math.cos(al_):.1f} {y0 - 62 * math.sin(al_):.1f}" fill="none" stroke="{INK}" stroke-width="1.6"/>'
        b += tt(x0 + 84, y0 - 12, '25°', 15)
        if krafter:
            b += pil(mx, my, mx, my + 70, ROD) + tt(mx + 9, my + 52, 'mg', 15, 'start', ROD, True, True)
            b += pil(mx, my, mx + 70 * nx, my + 70 * ny, GRON) + tt(mx + 78 * nx - 8, my + 78 * ny + 4, 'N', 15, 'end', GRON, True)
            b += pil(mx, my, mx - 78 * ux, my - 78 * uy, ORA)
            b += tt(mx - 62 * ux + 20 * nx, my - 62 * uy + 20 * ny, 'friktion', 14, 'end', ORA, True, True)
            b += pil(cx + 50 * ux + 44 * nx, cy + 50 * uy + 44 * ny, cx + 112 * ux + 44 * nx, cy + 112 * uy + 44 * ny, BLA)
            b += tt(cx + 80 * ux + 60 * nx, cy + 80 * uy + 60 * ny, 'rörelse', 14, 'middle', BLA, True)
            lab = ('Krafterna på klossen när den glider uppför planet: tyngdkraften mg rakt nedåt, normalkraften N vinkelrätt ut från planet '
                   'och friktionskraften nedför planet, mot rörelsen.')
        else:
            b += pil(cx + 40 * ux + 46 * nx, cy + 40 * uy + 46 * ny, cx + 122 * ux + 46 * nx, cy + 122 * uy + 46 * ny, BLA)
            b += tt(cx + 82 * ux + 62 * nx, cy + 82 * uy + 62 * ny, '6,0 m/s', 15, 'middle', BLA, True)
            b += tt(x1 - 96, y0 - 18, 'friktionstal 0,30', 14, fill=GRA)
            lab = 'En kloss på ett plan som lutar 25° mot horisontalplanet. Klossen rör sig uppför planet med farten 6,0 m/s. Friktionstalet är 0,30.'
        return svg(460, 232, b, lab)

    intro = (p('En kloss skjuts iväg uppför ett plan som lutar 25° mot horisontalplanet. Klossen har farten 6,0 m/s när den släpps. '
               'Friktionstalet mellan klossen och planet är 0,30, både när klossen glider och när den är i vila.') + fig(False))
    givet = li(GIVET, al(r'v_0=6{,}0\ \mathrm{m/s}', r'\alpha=25^\circ', r'\mu=0{,}30'), p('Positiv riktning är uppför planet.'))
    kraft_upp = li('Krafter längs planet när klossen glider uppåt',
                   p(r'Tyngdkraftens komponent \(mg\sin\alpha\) och friktionskraften \(F_f=\mu N\) pekar båda nedför planet. '
                     r'Normalkraften är \(N=mg\cos\alpha\).'), fig(True))
    n2_upp = li(r'Newtons andra lag: \(F_R=ma\)', p('Massan förkortas bort.'),
                al(r'ma=-mg\sin\alpha-\mu mg\cos\alpha', r'a=-9{,}82\cdot(\sin25^\circ+0{,}30\cdot\cos25^\circ)', rf'a\approx-{tx(au, 2)}\ \mathrm{{m/s^2}}'))
    tidlos = li(r'Tidlösa formeln: \(v^2=v_0^2+2as\) till vändpunkten, där \(v=0\)',
                al(rf'0=6{{,}}0^2-2\cdot{tx(au, 2)}\cdot s', rf's=\frac{{36}}{{2\cdot{tx(au, 2)}}}\approx{tx(s, 2)}\ \mathrm m'))
    steg_a = [sokt(givet, 'sträckan uppför planet till vändpunkten.'), kraft_upp, n2_upp, tidlos]
    steg_b = [sokt(givet, 'farten när klossen är tillbaka i startpunkten.'),
              li('Sträckan uppför planet', p(r'Uppåt bromsas klossen av både tyngdkraftens komponent och friktionen.'),
                 al(r'a=-9{,}82\cdot(\sin25^\circ+0{,}30\cdot\cos25^\circ)', rf'a\approx-{tx(au, 2)}\ \mathrm{{m/s^2}}',
                    rf's=\frac{{6{{,}}0^2}}{{2\cdot{tx(au, 2)}}}\approx{tx(s, 2)}\ \mathrm m')),
              li(r'Glider klossen ned igen? Jämför \(mg\sin\alpha\) med största vilofriktionen \(\mu mg\cos\alpha\)',
                 p(r'Klossen glider när \(\tan\alpha&gt;\mu\). Här är \(\tan25^\circ\approx0{,}47\), som är större än 0,30. Klossen glider alltså ned.')),
              li(r'Newtons andra lag nedför planet: \(F_R=ma\)', p('Nu pekar friktionen uppför planet, mot rörelsen.'),
                 al(r'a=9{,}82\cdot(\sin25^\circ-0{,}30\cdot\cos25^\circ)', rf'a\approx{tx(an, 2)}\ \mathrm{{m/s^2}}')),
              li(r'Tidlösa formeln från vila: \(v^2=2as\)',
                 mt(rf'v=\sqrt{{2\cdot{tx(an, 2)}\cdot{tx(s, 2)}}}\approx{tx(v, 1)}\ \mathrm{{m/s}}')),
              li('Rimlighet', p('Farten är lägre än 6,0 m/s eftersom friktionen har omvandlat rörelseenergi till värme både på vägen upp och på vägen ned.'))]
    delar = [
        del_('Hur långt uppför planet glider klossen innan den vänder?', steg_a, '2,6 m.',
             'Rita krafterna på klossen. Åt vilket håll pekar friktionen när klossen glider uppåt?', s, 'C', 4, (0, 2, 0),
             tol=0.05, enhet='m', vs=2, ratt_txt=['2,6', '2,64', '2,6 m'], fel=['4,3', '1,8', '6,8']),
        del_('Klossen glider sedan ned igen. Vilken fart har den när den är tillbaka i startpunkten?', steg_b, '2,8 m/s.',
             'Friktionen byter riktning när klossen vänder. Accelerationen nedför planet är därför inte lika stor som uppför.',
             v, 'A', 5, (0, 0, 2), tol=0.05, enhet='m/s', vs=2, ai=3, ratt_txt=['2,8', '2,80', '2,8 m/s'],
             fel=['6,0', '6', '4,7', '3,9']),
    ]
    return H.bygg(uid, 4, 'lutande_plan', 'Glidning på lutande plan', intro, delar, ('problemlösning',), True, False,
                  'Rita krafterna på klossen och dela upp tyngdkraften i en del längs planet och en del vinkelrätt mot planet.',
                  VARIANTER, fy=True, familjnyckel=NYCKEL['lutande_plan|Glidning på lutande plan'])


# ================================================================ P4: fjäder, sträv yta och ramp (energi)
def p4(uid):
    mm, k, xx, mu, d = 0.40, 800.0, 0.12, 0.25, 0.60
    E0 = k * xx ** 2 / 2
    W = mu * mm * g * d
    E1 = E0 - W
    v = math.sqrt(2 * E1 / mm)
    h = E1 / (mm * g)
    stot = E0 / (mu * mm * g)
    hela = int(stot // d)
    rest = stot - hela * d
    assert abs(E0 - 5.76) < 1e-12 and abs(W - 0.5892) < 1e-12 and abs(v - 5.0847) < 1e-4 and abs(h - 1.31640) < 1e-4
    assert hela == 9 and abs(rest - 0.46558) < 1e-4 and hela % 2 == 1  # udda antal passager: klossen är vid rampens fot

    def fig():
        y = 150
        b = linje(20, y, 300, y, INK, 2.4) + f'<path d="M 300 {y} Q 370 {y} 440 60" fill="none" stroke="{INK}" stroke-width="2.4"/>'
        b += rekt(14, 96, 12, 54, '#cfd8df') + fjader(26, 86, 132) + rekt(86, 114, 36, 36, '#dbe9f4') + tt(104, 108, '0,40 kg', 13)
        b += rekt(160, y, 140, 9, ORA, ORA, 0, 0) + linje(160, y - 8, 160, y + 20, GRA, 1.4, '4 3')
        b += tt(230, y + 30, 'strävt, 60 cm', 14, fill=ORA, bold=True) + tt(230, y + 48, 'friktionstal 0,25', 13, fill=ORA)
        b += tt(52, 170, '800 N/m', 13) + tt(400, 150, 'friktionsfri ramp', 13, fill=GRA)
        b += tt(140, 84, 'fjäderns ospända läge', 12.5, 'start', GRA) + linje(160, 90, 160, y - 10, GRA, 1.2, '4 3')
        return svg(460, 206, b, 'En kloss på 0,40 kg trycks mot en hoptryckt fjäder med fjäderkonstanten 800 N/m. Från fjäderns ospända läge '
                                'är bordet strävt i 60 cm, med friktionstalet 0,25. Därefter följer en friktionsfri ramp som svänger uppåt.')

    intro = (p('En kloss på 0,40 kg trycks mot en fjäder med fjäderkonstanten 800 N/m, så att fjädern trycks ihop 12 cm. När klossen släpps '
               'skjuts den iväg över ett vågrätt bord. Från den punkt där klossen lämnar fjädern är bordet strävt i 60 cm, med friktionstalet '
               '0,25 mot klossen. Därefter följer en friktionsfri ramp. Under fjädern är bordet också friktionsfritt.') + fig())
    givet = li(GIVET, al(r'm=0{,}40\ \mathrm{kg}', r'k=800\ \mathrm{N/m}', r'x=12\ \mathrm{cm}=0{,}12\ \mathrm m', r's=60\ \mathrm{cm}=0{,}60\ \mathrm m', r'\mu=0{,}25'))
    fj = li(r'Fjäderns energi: \(E=\tfrac{kx^2}{2}\)', mt(r'E=\frac{800\cdot0{,}12^2}{2}=5{,}76\ \mathrm J'))
    fr = li(r'Friktionens arbete på den sträva delen: \(W=F_f\cdot s=\mu mg\cdot s\)',
            al(r'W=0{,}25\cdot0{,}40\cdot9{,}82\cdot0{,}60', rf'W\approx{tx(W, 3)}\ \mathrm J'))
    kvar = li('Energin som finns kvar vid rampens fot', mt(rf'E_1=5{{,}}76-{tx(W, 3)}\approx{tx(E1, 3)}\ \mathrm J'))
    steg_a = [sokt(givet, 'farten vid rampens fot.'), fj, fr, kvar,
              li(r'Rörelseenergi: \(E_k=\tfrac{mv^2}{2}\)', al(rf'\frac{{0{{,}}40\cdot v^2}}{{2}}={tx(E1, 3)}', rf'v=\sqrt{{\frac{{2\cdot{tx(E1, 3)}}}{{0{{,}}40}}}}\approx{tx(v, 2)}\ \mathrm{{m/s}}'))]
    steg_b = [sokt(givet, 'höjden över bordet i högsta punkten.'), fj, fr, kvar,
              li(r'Lägesenergi i högsta punkten: \(E_p=mgh\)', p('Rampen är friktionsfri, så all energi som är kvar blir lägesenergi.'),
                 al(rf'0{{,}}40\cdot9{{,}}82\cdot h={tx(E1, 3)}', rf'h=\frac{{{tx(E1, 3)}}}{{0{{,}}40\cdot9{{,}}82}}\approx{tx(h, 2)}\ \mathrm m'))]
    steg_c = [sokt(givet, 'var på den sträva delen klossen stannar.'), fj,
              li('Bara den sträva delen tar energi från klossen', p('Fjädern och rampen ger tillbaka all energi. Klossen stannar när friktionen har omvandlat hela fjäderenergin till värme.')),
              li(r'Total glidsträcka på den sträva delen: \(E=\mu mg\cdot s_{\text{tot}}\)',
                 mt(rf's_{{\text{{tot}}}}=\frac{{5{{,}}76}}{{0{{,}}25\cdot0{{,}}40\cdot9{{,}}82}}\approx{tx(stot, 3)}\ \mathrm m')),
              li('Dela upp i hela passager på 0,60 m', mt(rf'{tx(stot, 3)}=9\cdot0{{,}}60+{tx(rest, 3)}'),
                 p('Klossen passerar den sträva delen nio hela gånger och glider sedan 0,47 m in på den tionde passagen.')),
              li('Var börjar den tionde passagen?',
                 p('Passage 1, 3, 5, 7 och 9 går från fjädern mot rampen. Efter den nionde passagen är klossen vid rampens fot. Den glider '
                   'upp på rampen, vänder och börjar den tionde passagen från rampens fot, i riktning mot fjädern.'))]
    delar = [
        del_('Vilken fart har klossen när den når rampens fot första gången?', steg_a, '5,1 m/s.',
             'Jämför fjäderns energi med det arbete som friktionen uträttar på den sträva delen.', v, 'C', 4, (0, 2, 0),
             tol=0.05, enhet='m/s', vs=2, ratt_txt=['5,1', '5,08', '5,1 m/s'], fel=['5,4', '5,37', '4,8']),
        del_('Hur högt över bordet når klossen på rampen? (Svara i m.)', steg_b, '1,3 m.',
             'Rampen är friktionsfri. Vilken energiform har klossen i sin högsta punkt?', h, 'C', 4, (0, 1, 0),
             tol=0.05, enhet='m', vs=2, ratt_txt=['1,3', '1,32', '1,3 m'], fel=['1,5', '1,47', '0,60']),
        del_('Klossen glider fram och tillbaka tills den stannar. Hur långt från rampens fot stannar den? (Svara i m.)', steg_c, '0,47 m.',
             'Var förlorar klossen energi? Hur lång sträcka kan den sammanlagt glida där?', rest, 'A', 5, (0, 0, 2),
             tol=0.005, enhet='m', vs=2, ai=3, ratt_txt=['0,47', '0,466', '0,47 m'], fel=['0,13', '0,14', '5,87', '0,60']),
    ]
    return H.bygg(uid, 5, 'blandat_energi', 'Blandat – energi och rörelsemängd', intro, delar, ('problemlösning',), True, False,
                  'Följ energin: fjäderenergi, friktionens arbete, rörelseenergi och lägesenergi.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['blandat_energi|Blandat – energi och rörelsemängd'])


# ================================================================ P5: isärskjutning med friktion (kollisioner)
def p5(uid):
    mA, mB, mu, sA = 0.60, 0.40, 0.20, 1.6
    vA = math.sqrt(2 * mu * g * sA)
    vB = mA * vA / mB
    sB = vB ** 2 / (2 * mu * g)
    EA, EB = mA * vA ** 2 / 2, mB * vB ** 2 / 2
    assert abs(vA - 2.50695) < 1e-5 and abs(vB - 3.760425) < 1e-5 and abs(sB - 3.6) < 1e-9 and abs(EB / (EA + EB) - 0.6) < 1e-12

    def fig():
        y = 132
        b = linje(16, y, 444, y, INK, 2.4)
        b += rekt(150, y - 46, 62, 46, '#dbe9f4') + tt(181, y - 26, 'A', 16, bold=True) + tt(181, y - 9, '0,60 kg', 11.5)
        b += fjader(212, 262, y - 22, 5, 7)
        b += rekt(262, y - 38, 48, 38, '#f3e3d3') + tt(286, y - 21, 'B', 16, bold=True) + tt(286, y - 6, '0,40 kg', 10.5)
        b += pil(140, y - 24, 70, y - 24, GRON) + pil(320, y - 20, 398, y - 20, GRON)
        b += tt(230, y + 26, 'friktionstal 0,20 mot golvet', 13.5, fill=GRA)
        return svg(460, 172, b, 'Två klossar på ett vågrätt golv med en hoptryckt fjäder mellan sig. Kloss A på 0,60 kg skjuts åt vänster '
                                'och kloss B på 0,40 kg åt höger.')

    intro = (p('Två klossar, A på 0,60 kg och B på 0,40 kg, står stilla på ett vågrätt golv med en hoptryckt fjäder mellan sig. När fjädern '
               'släpps skjuts klossarna åt var sitt håll. Det går så fort att friktionen inte hinner påverka under själva isärskjutningen. '
               'Sedan glider klossarna tills de stannar. Friktionstalet mot golvet är 0,20 för båda. Kloss A glider 1,6 m.') + fig())
    givet = li(GIVET, al(r'm_A=0{,}60\ \mathrm{kg}', r'm_B=0{,}40\ \mathrm{kg}', r'\mu=0{,}20', r's_A=1{,}6\ \mathrm m'))
    broms = li(r'Friktionen bromsar: \(F_f=\mu mg\) och Newtons andra lag \(F_R=ma\)', p('Massan förkortas bort, så båda klossarna har samma retardation.'),
               mt(r'a=\mu g=0{,}20\cdot9{,}82=1{,}964\ \mathrm{m/s^2}'))
    fartA = li(r'Tidlösa formeln: \(v^2=v_0^2+2as\) för kloss A, som stannar',
               al(r'0=v_A^2-2\cdot1{,}964\cdot1{,}6', rf'v_A=\sqrt{{6{{,}}285}}\approx{tx(vA, 2)}\ \mathrm{{m/s}}'))
    rm = li(r'Rörelsemängden bevaras: \(m_Av_A=m_Bv_B\)', p('Före isärskjutningen står klossarna stilla, så den totala rörelsemängden är noll även efteråt.'),
            mt(rf'v_B=\frac{{0{{,}}60\cdot{tx(vA, 3)}}}{{0{{,}}40}}\approx{tx(vB, 2)}\ \mathrm{{m/s}}'))
    steg_a = [sokt(givet, 'den fart kloss A får av fjädern.'), broms, fartA]
    steg_b = [sokt(givet, 'hur långt kloss B glider.'), broms, fartA, rm,
              li(r'Tidlösa formeln: \(v^2=v_0^2+2as\) för kloss B', mt(rf's_B=\frac{{{tx(vB, 2)}^2}}{{2\cdot1{{,}}964}}\approx3{{,}}6\ \mathrm m')),
              li('Kontroll med förhållanden', p(r'B får 1,5 gånger så stor fart som A. Bromssträckan växer med farten i kvadrat: \(1{,}5^2\cdot1{,}6=3{,}6\ \mathrm m\).'))]
    steg_c = [li(r'Rörelsemängden bevaras: \(m_Av_A=m_Bv_B\)', p(r'Klossarna får lika stor rörelsemängd \(p\), åt motsatta håll.')),
              li(r'Rörelseenergi uttryckt med rörelsemängd: \(E_k=\tfrac{mv^2}{2}=\tfrac{p^2}{2m}\)',
                 p('Med samma rörelsemängd får den lättare klossen mest energi.'), mt(r'\frac{E_B}{E_A}=\frac{m_A}{m_B}=\frac{0{,}60}{0{,}40}=1{,}5')),
              li(r'Andelen av fjäderns energi som B får', mt(r'\frac{E_B}{E_A+E_B}=\frac{1{,}5}{1+1{,}5}=0{,}60=60\ \%')),
              li('Kontroll med farterna', al(rf'E_A=\frac{{0{{,}}60\cdot{tx(vA, 3)}^2}}{{2}}\approx{tx(EA, 2)}\ \mathrm J',
                                            rf'E_B=\frac{{0{{,}}40\cdot{tx(vB, 3)}^2}}{{2}}\approx{tx(EB, 2)}\ \mathrm J',
                                            rf'\frac{{{tx(EB, 2)}}}{{{tx(EA, 2)}+{tx(EB, 2)}}}\approx0{{,}}60'))]
    delar = [
        del_('Vilken fart fick kloss A av fjädern?', steg_a, '2,5 m/s.',
             'Kloss A bromsas bara av friktionen. Vilken retardation ger den?', vA, 'C', 3, (0, 1, 0), tol=0.05, enhet='m/s',
             vs=2, ratt_txt=['2,5', '2,51', '2,5 m/s'], fel=['1,8', '3,8', '6,3']),
        del_('Hur långt glider kloss B innan den stannar?', steg_b, '3,6 m.',
             'Jämför klossarnas farter direkt efter isärskjutningen. Vilken storhet är lika stor för båda?', sB, 'C', 4, (0, 2, 0),
             tol=0.05, enhet='m', vs=2, ratt_txt=['3,6', '3,6 m', '3,60'], fel=['2,4', '1,6', '1,1', '1,07']),
        del_('Hur stor andel av fjäderns energi fick kloss B? (Svara i procent.)', steg_c, '60 %.',
             'Klossarna får lika stor rörelsemängd. Får de då också lika stor rörelseenergi?', 60, 'A', 5, (0, 0, 1), tol=0.5, enhet='%',
             vs=2, ai=3, ratt_txt=['60', '60 %', '60%'], fel=['40', '50', '69']),
    ]
    return H.bygg(uid, 5, 'kollisioner', 'Rekyl och isärskjutning', intro, delar, ('problemlösning',), True, False,
                  'Börja med kloss A: friktionen bestämmer hur långt en kloss glider vid en viss startfart.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['kollisioner|Rekyl och isärskjutning'])


# ================================================================ P6: cylinder med kolv som vänds (gaslagen, Boyles lag)
def p6(uid):
    mk, A, h1, p0 = 2.0, 15e-4, 12.0, 101.3e3
    dp = mk * g / A
    pa, pb = p0 + dp, p0 - dp
    h2 = h1 * pa / pb
    assert abs(dp - 13093.33) < 0.01 and abs(pa - 114393.3) < 0.1 and abs(pb - 88206.7) < 0.1 and abs(h2 - 15.5625) < 1e-3

    def fig():
        b = ''
        for x, upp in ((70, True), (290, False)):
            b += linje(x, 30, x, 190, INK, 2.4) + linje(x + 90, 30, x + 90, 190, INK, 2.4)
            if upp:
                b += linje(x, 190, x + 90, 190, INK, 2.4) + rekt(x + 3, 92, 84, 16, '#9fb3c2', INK, 1.6, 2)
                b += rekt(x + 2, 108, 86, 81, '#e2eef6', 'none', 0, 0) + tt(x + 45, 154, 'luft', 14)
                b += linje(x + 104, 108, x + 104, 190, GRA, 1.4) + linje(x + 98, 108, x + 110, 108, GRA, 1.4) + linje(x + 98, 190, x + 110, 190, GRA, 1.4)
                b += tt(x + 112, 154, '12,0 cm', 13.5, 'start') + tt(x + 45, 84, 'kolv 2,0 kg', 13) + tt(x + 45, 212, 'kolven överst', 13, fill=GRA)
            else:
                b += linje(x, 30, x + 90, 30, INK, 2.4) + rekt(x + 3, 136, 84, 16, '#9fb3c2', INK, 1.6, 2)
                b += rekt(x + 2, 31, 86, 105, '#e2eef6', 'none', 0, 0) + tt(x + 45, 90, 'luft', 14)
                b += linje(x + 104, 30, x + 104, 136, GRA, 1.4) + linje(x + 98, 30, x + 110, 30, GRA, 1.4) + linje(x + 98, 136, x + 110, 136, GRA, 1.4)
                b += tt(x + 112, 88, '?', 16, 'start', ORA, True) + tt(x + 45, 212, 'cylindern vänd', 13, fill=GRA)
        b += pil(206, 110, 262, 110, GRA, 2.2)
        return svg(460, 222, b, 'Till vänster en lodrät cylinder med kolven överst och en 12,0 cm hög luftpelare under kolven. Till höger samma '
                                'cylinder vänd upp och ned: luften finns ovanför kolven, som hänger under den, och luftpelaren är högre.')

    intro = (p('En lodrät cylinder är stängd med en lättrörlig och tät kolv. Kolven har massan 2,0 kg och arean 15 cm². Under kolven finns '
               'instängd luft som bildar en 12,0 cm hög pelare. Lufttrycket utanför är 101,3 kPa, och temperaturen är hela tiden densamma.') + fig())
    givet = li(GIVET, al(r'm=2{,}0\ \mathrm{kg}', r'A=15\ \mathrm{cm^2}=15\cdot10^{-4}\ \mathrm{m^2}', r'p_0=101{,}3\ \mathrm{kPa}', r'h_1=12{,}0\ \mathrm{cm}'))
    kolv = li(r'Kolvens tyngd ger trycket \(p=\tfrac FA\)', al(r'\frac{mg}{A}=\frac{2{,}0\cdot9{,}82}{15\cdot10^{-4}}', r'\phantom{\frac{mg}{A}}\approx13\,090\ \mathrm{Pa}=13{,}09\ \mathrm{kPa}'))
    upp = li('Kraftjämvikt för kolven när den ligger överst', p('Luften i cylindern måste bära både lufttrycket utifrån och kolvens tyngd.'),
             al(r'p_1=p_0+\frac{mg}{A}', rf'p_1=101{{,}}3+13{{,}}09\approx{tx(pa / 1000, 1)}\ \mathrm{{kPa}}'))
    steg_a = [sokt(givet, 'trycket i den instängda luften.'), kolv, upp]
    steg_b = [sokt(givet, 'luftpelarens höjd när cylindern är vänd.'), kolv, upp,
              li('Kraftjämvikt för kolven när cylindern är vänd', p('Nu bär lufttrycket utifrån både kolvens tyngd och trycket från den instängda luften.'),
                 al(r'p_2=p_0-\frac{mg}{A}', rf'p_2=101{{,}}3-13{{,}}09\approx{tx(pb / 1000, 2)}\ \mathrm{{kPa}}')),
              li(r'Boyles lag: \(p_1V_1=p_2V_2\)', p(r'Temperaturen och gasmängden är oförändrade. Volymen är \(V=A\cdot h\), och arean förkortas bort.'),
                 al(r'p_1h_1=p_2h_2', rf'h_2=\frac{{{tx(pa / 1000, 2)}\cdot12{{,}}0}}{{{tx(pb / 1000, 2)}}}\approx{tx(h2, 1)}\ \mathrm{{cm}}')),
              li('Rimlighet', p('Trycket i luften blir lägre när kolven hänger under den, så luften tar större plats.'))]
    delar = [
        del_('Hur stort är trycket i den instängda luften? (Svara i kPa.)', steg_a, '114,4 kPa.',
             'Vilka krafter verkar på kolven? Den ligger stilla.', pa / 1000, 'C', 4, (0, 2, 0), tol=0.05, enhet='kPa', vs=4,
             ratt_txt=['114,4', '114', '114,4 kPa', '114,39'], fel=['13,1', '101,3', '88,2', '121']),
        del_('Cylindern vänds upp och ned, så att kolven hänger under luften. Hur hög blir luftpelaren då? (Svara i cm.)', steg_b, '15,6 cm.',
             'Hur ändras trycket i luften när kolven hänger under den i stället för att ligga ovanpå?', h2, 'A', 5, (0, 0, 2),
             tol=0.05, enhet='cm', vs=3, ai=3, ratt_txt=['15,6', '15,56', '15,6 cm', '16'], fel=['12,0', '9,25', '13,6', '10,6']),
    ]
    return H.bygg(uid, 6, 'gaslagen', 'Boyles lag', intro, delar, ('problemlösning', 'begrepp'), True, False,
                  'Kolven ligger stilla, så krafterna på den tar ut varandra. Tryck gånger area ger kraft.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['gaslagen|Boyles lag'])


# ================================================================ P7: isbitar i dryck (fasändring)
def p7(uid):
    mi, n, ci, cv, ls, md, Ti, Td = 0.018, 3, 2.10, 4.18, 334.0, 0.33, 18.0, 22.0
    q_varm, q_smalt = ci * n * mi * Ti, ls * n * mi
    q_is = q_varm + q_smalt
    q_dryck = cv * md * Td
    T = (q_dryck - q_is) / (cv * (md + n * mi))
    per = ci * mi * Ti + ls * mi
    antal = math.ceil(q_dryck / per)
    assert abs(q_varm - 2.0412) < 1e-9 and abs(q_smalt - 18.036) < 1e-9 and abs(q_dryck - 30.3468) < 1e-9
    assert q_dryck > q_is and abs(T - 6.39803) < 1e-4 and antal == 5 and 4 * per < q_dryck < 5 * per
    def fig():
        skala = 8.6  # px per kJ
        x0 = 150
        b = ''
        for i, (namn, kj, farg) in enumerate((('drycken avger', q_dryck, ORA), ('4 isbitar tar upp', 4 * per, BLA), ('5 isbitar tar upp', 5 * per, BLA))):
            y = 26 + i * 44
            b += tt(x0 - 8, y + 19, namn, 13.5, 'end') + rekt(x0, y, kj * skala, 28, farg, farg, 0, 2)
            b += tt(x0 + 10, y + 19, sv(kj, 1) + ' kJ', 13.5, 'start', '#fff', True)
        b += linje(x0 + q_dryck * skala, 14, x0 + q_dryck * skala, 162, ORA, 1.6, '5 4') + linje(x0, 14, x0, 162, INK, 1.6)
        return svg(500, 172, b, 'Stapeldiagram. Drycken avger 30,3 kJ när den kyls till 0 °C. Fyra isbitar kan ta upp 26,8 kJ, vilket är för lite. '
                                'Fem isbitar kan ta upp 33,5 kJ, vilket räcker.')

    intro = p('Tre isbitar på 18 g vardera tas ur en frys där temperaturen är −18 °C. De läggs i ett glas med 0,33 kg läsk som har '
              'temperaturen 22 °C. Räkna med att läsken har samma värmeegenskaper som vatten, och bortse från värmeutbytet med glaset och '
              'omgivningen. Isens specifika värmekapacitet är 2,10 kJ/(kg·K), vattnets är 4,18 kJ/(kg·K) och isens smältvärme är 334 kJ/kg.')
    givet = li(GIVET, al(r'm_{\text{is}}=3\cdot0{,}018=0{,}054\ \mathrm{kg}', r'm_{\text{dryck}}=0{,}33\ \mathrm{kg}',
                         r'c_{\text{is}}=2{,}10\ \mathrm{kJ/(kg\cdot K)}', r'c_{\text{vatten}}=4{,}18\ \mathrm{kJ/(kg\cdot K)}', r'l_s=334\ \mathrm{kJ/kg}'))
    varm = li(r'Uppvärmning av isen till 0 °C: \(Q=cm\Delta T\)', mt(rf'Q_1=2{{,}}10\cdot0{{,}}054\cdot18\approx{tx(q_varm, 2)}\ \mathrm{{kJ}}'))
    smalt = li(r'Smältning av isen: \(Q=l_sm\)', mt(rf'Q_2=334\cdot0{{,}}054\approx{tx(q_smalt, 2)}\ \mathrm{{kJ}}'))
    summa = li('Sammanlagd energi', mt(rf'Q_1+Q_2={tx(q_varm, 2)}+{tx(q_smalt, 2)}\approx{tx(q_is, 2)}\ \mathrm{{kJ}}'))
    dryck = li(r'Energi som drycken kan avge ned till 0 °C: \(Q=cm\Delta T\)', mt(rf'Q=4{{,}}18\cdot0{{,}}33\cdot22\approx{tx(q_dryck, 2)}\ \mathrm{{kJ}}'))
    steg_a = [sokt(givet, 'energin som krävs för att värma och smälta isen.'), varm, smalt, summa]
    steg_b = [sokt(givet, 'dryckens sluttemperatur.'), varm, smalt, summa, dryck,
              li('Smälter all is?', p(rf'Ja. Drycken kan avge {sv(q_dryck, 2)} kJ, vilket är mer än de {sv(q_is, 2)} kJ som isen behöver.')),
              li('Värmebalans: avgiven energi = upptagen energi', p(r'Drycken svalnar från 22 °C till sluttemperaturen \(T\). Isen värms och smälter, och '
                                                                    'smältvattnet värms sedan från 0 °C till samma temperatur.'),
                 al(r'4{,}18\cdot0{,}33\cdot(22-T)', rf'={tx(q_is, 2)}+4{{,}}18\cdot0{{,}}054\cdot T')),
              li(r'Lös ut \(T\)', al(rf'{tx(q_dryck, 2)}-1{{,}}379T={tx(q_is, 2)}+0{{,}}226T', rf'{tx(q_dryck - q_is, 2)}=1{{,}}605T', rf'T\approx{tx(T, 1)}\ ^\circ\mathrm C'))]
    steg_c = [li(GIVET, al(r'm=0{,}018\ \mathrm{kg\ per\ isbit}', r'm_{\text{dryck}}=0{,}33\ \mathrm{kg}', r'c_{\text{is}}=2{,}10\ \mathrm{kJ/(kg\cdot K)}',
                           r'c_{\text{vatten}}=4{,}18\ \mathrm{kJ/(kg\cdot K)}', r'l_s=334\ \mathrm{kJ/kg}'),
                 p('Sökt: det minsta antalet isbitar som kyler drycken till 0 °C.')),
              dryck,
              li(r'Energi som en isbit kan ta upp: \(Q=cm\Delta T+l_sm\)', p('Isbiten värms först till 0 °C och smälter sedan.'),
                 al(r'Q=2{,}10\cdot0{,}018\cdot18+334\cdot0{,}018', rf'Q\approx{tx(per, 2)}\ \mathrm{{kJ}}')),
              li('Antal isbitar', mt(rf'\frac{{{tx(q_dryck, 2)}}}{{{tx(per, 2)}}}\approx{tx(q_dryck / per, 2)}'),
                 p(rf'Fyra isbitar tar bara upp {sv(4 * per, 1)} kJ och räcker inte. Med fem isbitar når drycken 0 °C, och en del av isen blir kvar osmält.'),
                 fig())]
    delar = [
        del_('Hur mycket energi krävs för att värma de tre isbitarna till 0 °C och smälta dem? (Svara i kJ.)', steg_a, '20,1 kJ.',
             'Isen måste först värmas till 0 °C innan den kan smälta. Räkna de två stegen var för sig.', q_is, 'C', 3, (0, 1, 0),
             tol=0.05, enhet='kJ', vs=3, ratt_txt=['20,1', '20', '20,1 kJ', '20,08'], fel=['18,0', '2,04', '22,1', '20100']),
        del_('Vilken temperatur får drycken när all is har smält och temperaturen har jämnats ut?', steg_b, '6,4 °C.',
             'Smältvattnet från isen är 0 °C och måste också värmas upp till sluttemperaturen.', T, 'C', 4, (0, 2, 0),
             tol=0.05, enhet='°C', vs=2, ratt_txt=['6,4', '6,40', '6,4 °C'], fel=['7,4', '7,45', '5,2', '0']),
        del_('Hur många isbitar behövs minst för att drycken ska kylas ända ned till 0 °C?', steg_c, '5 isbitar.',
             'Hur mycket energi måste drycken avge för att nå 0 °C, och hur mycket kan en isbit ta upp?', antal, 'A', 5, (0, 0, 1),
             tol=0, enhet=None, vs=None, ai=3, ratt_txt=['5', '5 isbitar', '5 st'], fel=['4', '6', '4,5', '3']),
    ]
    return H.bygg(uid, 7, 'fasandring', 'Energikedjor och värmebalans med fasövergång', intro, delar, ('problemlösning',), True, False,
                  'Isen tar upp energi i två steg: först värms den till 0 °C, sedan smälter den.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['fasandring|Energikedjor och värmebalans med fasövergång'])


# ================================================================ P8: krets med inre resistans (kopplingar)
def p8(uid):
    E, ri, R1, R2, R3 = 12.0, 0.50, 4.0, 6.0, 12.0
    Rp = 1 / (1 / R2 + 1 / R3)
    I = E / (R1 + Rp + ri)
    Upol = E - ri * I
    Up = Rp * I
    P3 = Up ** 2 / R3
    I2 = (E - 11.0) / ri
    Ry = 11.0 / I2
    Rx = 1 / (1 / (Ry - R1) - 1 / R2)
    assert abs(Rp - 4) < 1e-12 and abs(I - 12 / 8.5) < 1e-12 and abs(Upol - 11.294118) < 1e-6 and abs(P3 - 2.657439) < 1e-6
    assert abs(I2 - 2) < 1e-12 and abs(Ry - 5.5) < 1e-12 and abs(Rx - 2) < 1e-9
    # Kontroll av c: med 2,0 Ω blir polspänningen 11,0 V.
    assert abs((E - ri * E / (R1 + 1 / (1 / R2 + 1 / Rx) + ri)) - 11.0) < 1e-9

    def fig():
        def res(x, y, lod, namn, varde):
            if lod:
                return (rekt(x - 11, y - 28, 22, 56, '#fff', INK) + tt(x + 18, y - 3, namn, 14, 'start', bold=True) + tt(x + 18, y + 15, varde, 13, 'start'))
            return rekt(x - 30, y - 11, 60, 22, '#fff', INK) + tt(x, y - 20, f'{namn} = {varde}', 14, bold=True)
        b = linje(60, 44, 150, 44) + linje(210, 44, 350, 44) + linje(60, 196, 350, 196)
        b += linje(60, 44, 60, 92) + linje(60, 148, 60, 196)
        b += rekt(30, 84, 60, 72, 'none', GRA, 1.4, 6) + linje(44, 100, 76, 100, INK, 2.2) + linje(52, 108, 68, 108, INK, 4)
        b += linje(60, 92, 60, 100) + linje(60, 108, 60, 118) + rekt(52, 118, 16, 28, '#fff', INK, 1.8) + linje(60, 146, 60, 148)
        b += tt(26, 100, '+', 15, 'end') + tt(98, 112, '12,0 V', 13.5, 'start') + tt(98, 132, '0,50 Ω', 13.5, 'start') + tt(98, 152, 'batteri', 12.5, 'start', GRA)
        b += res(180, 44, False, 'R₁', '4,0 Ω')
        for x, namn, varde in ((270, 'R₂', '6,0 Ω'), (350, 'R₃', '12 Ω')):
            b += linje(x, 44, x, 92) + linje(x, 148, x, 196) + res(x, 120, True, namn, varde)
        b += cirkel(270, 44, 3.5, INK, INK, 0) + cirkel(270, 196, 3.5, INK, INK, 0)
        return svg(440, 224, b, 'Kopplingsschema. Ett batteri med ems 12,0 V och inre resistansen 0,50 Ω är kopplat till resistorn R1 på 4,0 Ω. '
                                'I serie med R1 ligger en parallellkoppling av R2 på 6,0 Ω och R3 på 12 Ω.')

    intro = (p('Ett batteri med ems 12,0 V och inre resistansen 0,50 Ω är kopplat till tre resistorer enligt figuren. Resistorn R₁ = 4,0 Ω '
               'ligger i serie med parallellkopplingen av R₂ = 6,0 Ω och R₃ = 12 Ω.') + fig())
    givet = li(GIVET, al(r'\mathcal E=12{,}0\ \mathrm V', r'r=0{,}50\ \Omega', r'R_1=4{,}0\ \Omega', r'R_2=6{,}0\ \Omega', r'R_3=12\ \Omega'))
    par = li(r'Parallellkoppling: \(\tfrac1{R_p}=\tfrac1{R_2}+\tfrac1{R_3}\)', al(r'\frac1{R_p}=\frac1{6{,}0}+\frac1{12}=\frac14', r'R_p=4{,}0\ \Omega'))
    ser = li(r'Seriekoppling: \(R_y=R_1+R_p\)', mt(r'R_y=4{,}0+4{,}0=8{,}0\ \Omega'))
    strom = li(r'Ohms lag för hela kretsen: \(I=\dfrac{\mathcal E}{R_y+r}\)', mt(rf'I=\frac{{12{{,}}0}}{{8{{,}}0+0{{,}}50}}\approx{tx(I, 3)}\ \mathrm A'))
    steg_a = [sokt(givet, 'batteriets polspänning.'), par, ser, strom,
              li(r'Polspänning: \(U=\mathcal E-rI\)', mt(rf'U=12{{,}}0-0{{,}}50\cdot{tx(I, 3)}\approx{tx(Upol, 2)}\ \mathrm V'))]
    steg_b = [sokt(givet, 'effekten i R₃.'), par, ser, strom,
              li(r'Spänningen över parallellkopplingen: \(U_p=R_pI\)', p('Samma spänning ligger över R₂ och R₃.'),
                 mt(rf'U_p=4{{,}}0\cdot{tx(I, 3)}\approx{tx(Up, 3)}\ \mathrm V')),
              li(r'Effekt: \(P=\dfrac{U^2}{R}\)', mt(rf'P_3=\frac{{{tx(Up, 3)}^2}}{{12}}\approx{tx(P3, 2)}\ \mathrm W'))]
    steg_c = [li(GIVET, al(r'\mathcal E=12{,}0\ \mathrm V', r'r=0{,}50\ \Omega', r'U=11{,}0\ \mathrm V', r'R_1=4{,}0\ \Omega', r'R_2=6{,}0\ \Omega'),
                 p(r'Sökt: resistansen \(R_x\) hos den nya resistorn.')),
              li(r'Polspänningen ger strömmen: \(U=\mathcal E-rI\)', al(r'11{,}0=12{,}0-0{,}50\cdot I', r'I=2{,}0\ \mathrm A')),
              li(r'Ohms lag för den yttre kretsen: \(R_y=\dfrac UI\)', mt(r'R_y=\frac{11{,}0}{2{,}0}=5{,}5\ \Omega')),
              li(r'Seriekoppling: \(R_p=R_y-R_1\)', mt(r'R_p=5{,}5-4{,}0=1{,}5\ \Omega')),
              li(r'Parallellkoppling: \(\tfrac1{R_p}=\tfrac1{R_2}+\tfrac1{R_x}\)',
                 al(r'\frac1{R_x}=\frac1{1{,}5}-\frac1{6{,}0}=0{,}50\ \Omega^{-1}', r'R_x=2{,}0\ \Omega')),
              li('Kontroll', p(r'Med \(R_x=2{,}0\ \Omega\) är \(R_p=1{,}5\ \Omega\) och strömmen \(\tfrac{12{,}0}{4{,}0+1{,}5+0{,}50}=2{,}0\ \mathrm A\). '
                               r'Polspänningen blir \(12{,}0-0{,}50\cdot2{,}0=11{,}0\ \mathrm V\).'))]
    delar = [
        del_('Hur stor är batteriets polspänning?', steg_a, '11,3 V.',
             'Bestäm först kretsens sammanlagda resistans och strömmen genom batteriet.', Upol, 'C', 3, (0, 1, 0), tol=0.05,
             enhet='V', vs=3, ratt_txt=['11,3', '11,29', '11,3 V'], fel=['12', '12,0', '11,7', '5,65']),
        del_('Hur stor effekt utvecklas i R₃?', steg_b, '2,7 W.',
             'Vilken spänning ligger över parallellkopplingen? Den är inte lika stor som polspänningen.', P3, 'C', 4, (0, 2, 0),
             tol=0.05, enhet='W', vs=2, ratt_txt=['2,7', '2,66', '2,7 W'], fel=['10,6', '5,3', '23,9', '12']),
        del_('R₃ byts mot en annan resistor, så att polspänningen blir 11,0 V. Vilken resistans har den nya resistorn?', steg_c,
             '2,0 Ω.', 'Hur stor måste strömmen vara för att polspänningen ska bli 11,0 V?', Rx, 'A', 5, (0, 0, 2),
             tol=0.05, enhet='Ω', vs=2, ai=3, ratt_txt=['2,0', '2', '2,0 Ω', '2 Ω'], fel=['1,5', '5,5', '12', '3,0']),
    ]
    return H.bygg(uid, 8, 'kopplingar', 'Kretsanalys och blandade resistorkopplingar', intro, delar, ('problemlösning',), True, False,
                  'Ersätt först parallellkopplingen med en enda resistor.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['kopplingar|Kretsanalys och blandade resistorkopplingar'])


UPPGIFTER = [(3, p1), (4, p2), (4, p3), (5, p4), (5, p5), (6, p6), (7, p7), (8, p8)]


def main():
    src, bank = H.las(BANK)
    for q in bank:
        if q.get('familjNyckel'):
            NYCKEL[f"{q['omr']}|{q['familj']}"] = q['familjNyckel']
    nasta, nya = {}, []
    for kap, funk in UPPGIFTER:
        nasta.setdefault(kap, H.nasta_id(bank, kap))
        nya.append(funk(f'{kap}.{nasta[kap]}'))
        nasta[kap] += 1
    assert not {q['id'] for q in bank} & {q['id'] for q in nya}
    print('uppgifter', len(nya), 'kort', sum(len(q.get('spelDelar') or [1]) for q in nya), [q['id'] for q in nya])
    if '--varianter' in sys.argv:
        Path(sys.argv[sys.argv.index('--varianter') + 1]).write_text(json.dumps(VARIANTER, ensure_ascii=False, indent=1), encoding='utf-8')
    if '--skriv' in sys.argv:
        H.lagg_till(BANK, src, nya)


if __name__ == '__main__':
    main()
