"""Fysik 1 (uppgifter.js): andra omgången A-uppgifter på träningsnivå 4–5, 11 november 2026.

Sex uppgifter i centrala områden som saknade kort på nivå 5: friktion, rörelseenergi, effekt, värme, vektorer och
rörelsemängd. Varje uppgift är handskriven med egen situation, figur och facit enligt agent/FACITMALL.md.
Alla tal räknas i skriptet och kontrolleras med assert. Se agent/A_UPPGIFTER_2026-11-11.md.

  python tools/bygg-a-uppgifter-fy1-2026-11-11.py [--skriv] [--varianter fil.json]
"""
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import (mt, al, p, li, del_, Plot, svg, tt, linje, pil, rekt, cirkel, tx,  # noqa: E402
                               BLA, ORA, GRON, GRA, INK, ROD, LJUS)

BANK = 'uppgifter.js'
VARIANTER = {}
g = 9.82
NYCKEL = {}
GIVET = 'Givet och sökt'
VATTEN = '#cfe6f5'


def sokt(steg, text):
    """Lägger till vad som söks sist i steget Givet och sökt."""
    assert steg.endswith('</li>')
    return steg[:-5] + p('Sökt: ' + text) + '</li>'


def tusen(v):
    """Heltal med smalt mellanrum som tusentalsavgränsare, för LaTeX."""
    return f'{v:,.0f}'.replace(',', r'\,')


def matt(x1, x2, y, text, over=True, color=GRA):
    """Måttlinje med ändstreck och text."""
    b = linje(x1, y, x2, y, color, 1.6) + linje(x1, y - 6, x1, y + 6, color, 1.6) + linje(x2, y - 6, x2, y + 6, color, 1.6)
    return b + tt((x1 + x2) / 2, y - 8 if over else y + 18, text, 14, fill=INK)


# ================================================================ Q1: låda som glider på ett lastbilsflak (friktion)
def q1(uid):
    a_max = 0.50 * g
    a_lada = 0.40 * g
    a_rel = 6.5 - a_lada
    t = math.sqrt(2 * 2.5 / a_rel)
    t_stopp = 20 / 6.5
    assert abs(a_max - 4.91) < 1e-9 and abs(a_lada - 3.928) < 1e-9 and abs(t - 1.39424) < 1e-4 and t < t_stopp
    # Kontroll i vägens system: lådan och framstammen möts efter tiden t.
    assert abs((20 * t - a_lada * t * t / 2) - (20 * t - 6.5 * t * t / 2) - 2.5) < 1e-9

    def fig():
        b = linje(10, 164, 446, 164, GRA, 2)
        b += rekt(58, 112, 276, 12, '#cfd8df') + rekt(326, 62, 8, 50, '#9fb0bd') + rekt(334, 66, 72, 58, '#dfe8ee')
        b += rekt(350, 74, 40, 22, '#fff', GRA, 1.4)
        for cx in (104, 146, 372):
            b += cirkel(cx, 146, 17, INK, '#fff', 2) + cirkel(cx, 146, 6, '#9fb0bd', '#fff', 1)
        b += rekt(150, 72, 44, 40, '#f3d9bf', INK) + tt(172, 97, '40 kg', 13)
        b += matt(194, 326, 52, '2,5 m')
        b += pil(250, 22, 330, 22, GRON, 3) + tt(244, 27, 'körriktning', 14, 'end', GRON, True)
        b += tt(232, 186, 'lastbilen bromsar', 14, fill=GRA)
        return svg(456, 196, b, 'En lastbil sedd från sidan. På flaket står en låda på 40 kg. Avståndet från lådans framkant till '
                                'flakets framstam är 2,5 m. Lastbilen kör åt höger och bromsar.')

    def krafter():
        b = rekt(40, 150, 240, 10, '#cfd8df') + rekt(120, 90, 80, 60, '#f3d9bf', INK)
        b += pil(160, 120, 160, 196, ROD) + tt(168, 196, 'mg', 15, 'start', ROD, True)
        b += pil(160, 90, 160, 26, BLA) + tt(168, 34, 'N', 15, 'start', BLA, True)
        b += pil(120, 144, 52, 144, ORA) + tt(50, 132, 'F', 15, 'start', ORA, True) + tt(61, 137, 'f', 11, 'start', ORA, True)
        b += pil(216, 76, 270, 76, GRON, 2.4, 9) + tt(243, 66, 'lådan glider', 13, fill=GRON)
        return svg(320, 210, b, 'Krafterna på lådan medan den glider framåt på flaket: tyngdkraften mg nedåt, normalkraften N uppåt '
                                'och glidfriktionen bakåt, mot glidriktningen.')

    intro = (p('En låda på 40 kg står löst på ett lastbilsflak, 2,5 m bakom flakets framstam. Vilofriktionstalet mellan lådan och flaket är '
               '0,50 och glidfriktionstalet är 0,40. Lastbilen kör i 72 km/h på en rak och vågrät väg när föraren börjar bromsa.') + fig())
    givet = li(GIVET, al(r'm=40\ \mathrm{kg}', r'\mu_s=0{,}50\quad\mu_k=0{,}40', r's=2{,}5\ \mathrm m'),
               p('Positiv riktning är framåt, i körriktningen.'))
    givet_bc = li(GIVET, al(r'm=40\ \mathrm{kg}', r'\mu_k=0{,}40', r's=2{,}5\ \mathrm m', r'a_{\text{lastbil}}=-6{,}5\ \mathrm{m/s^2}'),
                  p('Positiv riktning är framåt, i körriktningen. En retardation är därför negativ.'))
    glid = li(r'Glidfriktionen: \(F_f=\mu_kN\)', krafter(),
              p('Lådan glider framåt på flaket, så glidfriktionen är riktad bakåt. Flaket är vågrätt, och då är \\(N=mg\\).'),
              mt(rf'F_f=0{{,}}40\cdot40\cdot9{{,}}82\approx{tx(0.4 * 40 * g, 0)}\ \mathrm N'))
    n2 = li(r'Newtons andra lag: \(a=\tfrac{F_R}{m}\)', p('Glidfriktionen är den enda vågräta kraften på lådan.'),
            mt(rf'a=\frac{{-{tx(0.4 * 40 * g, 1)}}}{{40}}\approx-{tx(a_lada, 2)}\ \mathrm{{m/s^2}}'))
    steg_a = [sokt(givet, 'den största retardation lastbilen kan ha utan att lådan börjar glida.'),
              li(r'Vilofriktionen är som störst \(F_{\max}=\mu_sN\)',
                 p('För att följa med flaket måste lådan bromsas lika mycket som lastbilen. Den enda vågräta kraften på lådan är '
                   'vilofriktionen från flaket. Flaket är vågrätt, och då är \\(N=mg\\).'), mt(r'F_{\max}=\mu_smg')),
              li(r'Newtons andra lag: \(F_R=ma\)', al(r'\mu_smg=ma_{\max}', r'a_{\max}=\mu_sg=0{,}50\cdot9{,}82', rf'a_{{\max}}\approx{tx(a_max, 1)}\ \mathrm{{m/s^2}}'),
                 p('Massan förkortas bort. Bromsar lastbilen hårdare än så räcker inte vilofriktionen, och lådan börjar glida.'))]
    steg_b = [sokt(givet_bc, 'lådans retardation medan den glider.'), glid,
              li(r'Newtons andra lag: \(a=\tfrac{F_R}{m}\)', p('Glidfriktionen är den enda vågräta kraften på lådan.'),
                 mt(rf'a=\frac{{-{tx(0.4 * 40 * g, 1)}}}{{40}}\approx-{tx(a_lada, 2)}\ \mathrm{{m/s^2}}'),
                 p('Lådan bromsas alltså med 3,9 m/s². Det är mindre än lastbilens 6,5 m/s².'))]
    steg_c = [sokt(givet_bc, 'tiden tills lådan slår i framstammen.'), glid, n2,
              li('Jämför lådans rörelse med flakets',
                 p('Både lådan och flaket bromsas, men flaket bromsas mer. Sett från flaket accelererar lådan därför framåt med skillnaden.'),
                 mt(rf'a_{{\text{{rel}}}}=6{{,}}5-{tx(a_lada, 2)}={tx(a_rel, 2)}\ \mathrm{{m/s^2}}'),
                 p('När bromsningen börjar har lådan och flaket samma fart. Sett från flaket startar lådan alltså från vila.')),
              li(r'Sträckformeln från vila: \(s=\tfrac{at^2}{2}\)',
                 al(rf'2{{,}}5=\frac{{{tx(a_rel, 2)}\cdot t^2}}{{2}}', rf't=\sqrt{{\frac{{2\cdot2{{,}}5}}{{{tx(a_rel, 2)}}}}}\approx{tx(t, 2)}\ \mathrm s')),
              li('Kontroll: lastbilen bromsar fortfarande',
                 p(f'Lastbilen kör i 72 km/h = 20 m/s och behöver 20/6,5 ≈ {tx(t_stopp, 1).replace("{,}", ",")} s för att stanna. '
                   'Lådan slår i framstammen efter 1,4 s, medan lastbilen ännu bromsar. Beräkningen gäller alltså.'))]
    delar = [
        del_('Vilken är den största retardation lastbilen kan ha utan att lådan börjar glida?', steg_a, '4,9 m/s².',
             'Vilken kraft är det som bromsar lådan när den följer med flaket? Hur stor kan den kraften bli som mest?',
             a_max, 'C', 3, (0, 1, 0), tol=0.05, enhet='m/s²', vs=2, ratt_txt=['4,9', '4,91', '4,9 m/s²'], fel=['3,9', '0,50', '196', '6,5']),
        del_('Lastbilen bromsar med 6,5 m/s², och lådan glider framåt på flaket. Hur stor är lådans retardation medan den glider?',
             steg_b, '3,9 m/s².', 'Vilken är den enda vågräta kraften på lådan när den glider? Använd Newtons andra lag.',
             a_lada, 'C', 3, (0, 1, 0), tol=0.05, enhet='m/s²', vs=2, ratt_txt=['3,9', '3,93', '3,9 m/s²'], fel=['4,9', '6,5', '2,6', '157']),
        del_('Lastbilen bromsar med 6,5 m/s², och lådan glider framåt på flaket. Hur lång tid tar det innan lådan slår i framstammen?',
             steg_c, '1,4 s.', 'Både lådan och flaket bromsas, men olika mycket. Hur rör sig lådan sedd från flaket?',
             t, 'A', 5, (0, 0, 2), tol=0.05, enhet='s', vs=2, ai=3, ratt_txt=['1,4', '1,39', '1,4 s'], fel=['0,88', '1,1', '1,6', '3,1', '0,38'],
             kortfraga='Lastbilen bromsar med 6,5 m/s², och lådan glider framåt på flaket. Lådans retardation är då 3,93 m/s². '
                       'Hur lång tid tar det innan lådan slår i framstammen?'),
    ]
    return H.bygg(uid, 4, 'friktion', 'Friktion och Newtons andra lag', intro, delar, ('problemlösning', 'modellering'), True, False,
                  'Det är friktionen från flaket som bromsar lådan. Jämför lådans retardation med lastbilens.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['friktion|Friktion och Newtons andra lag'])


# ================================================================ Q2: fart vid hindret (rörelseenergi)
def q2(uid):
    mm, F, tr = 1500.0, 11200.0, 0.80
    v50, v70 = 50 / 3.6, 70 / 3.6
    s_b = mm * v50 ** 2 / (2 * F)
    s_r = v50 * tr
    d = s_r + s_b
    s_r70 = v70 * tr
    kvar = d - s_r70
    E0 = mm * v70 ** 2 / 2
    E = E0 - F * kvar
    v = math.sqrt(2 * E / mm)
    assert abs(s_b - 12.917) < 2e-3 and abs(d - 24.029) < 2e-3 and abs(v * 3.6 - 57.098) < 2e-3 and kvar > 0
    # Kontroll med rörelseformler: a = F/m och v² = v0² − 2as.
    assert abs(v ** 2 - (v70 ** 2 - 2 * (F / mm) * kvar)) < 1e-9 and abs(v50 ** 2 - 2 * (F / mm) * s_b) < 1e-9
    kvar_k = 24.0 - s_r70          # delkortet anger 24,0 m
    v_k = math.sqrt(2 * (E0 - F * kvar_k) / mm)
    assert abs(v_k * 3.6 - v * 3.6) < 0.06 and f'{v_k * 3.6:.3g}' == f'{v * 3.6:.3g}' == '57.1'

    def bil(x, y, farg='#dfe8ee'):
        return (rekt(x, y - 16, 62, 16, farg, INK, 1.6) + f'<path d="M{x + 12} {y - 16} L{x + 20} {y - 30} H{x + 44} L{x + 52} {y - 16} Z" fill="{farg}" '
                f'stroke="{INK}" stroke-width="1.6"/>' + cirkel(x + 14, y, 7, INK, '#fff', 1.5) + cirkel(x + 48, y, 7, INK, '#fff', 1.5))

    def fig():
        b = linje(10, 96, 446, 96, GRA, 2) + bil(22, 89)
        b += rekt(404, 62, 14, 34, '#8a6a4a', INK, 1.4) + cirkel(411, 50, 20, '#7fb58a', INK, 1.4) + tt(411, 22, 'träd', 14)
        b += linje(84, 100, 84, 138, GRA, 1.2, '4 3') + linje(232, 100, 232, 138, GRA, 1.2, '4 3') + linje(404, 100, 404, 138, GRA, 1.2, '4 3')
        b += matt(84, 232, 128, 'reaktionssträcka', False) + matt(232, 404, 128, 'bromssträcka', False)
        b += tt(158, 164, '(0,80 s, konstant fart)', 13, fill=GRA) + tt(318, 164, '(bromskraft 11,2 kN)', 13, fill=GRA)
        return svg(456, 176, b, 'En bil på en väg med ett träd över vägen längre fram. Sträckan fram till trädet är uppdelad i '
                                'reaktionssträckan, där farten är konstant i 0,80 s, och bromssträckan, där bromskraften är 11,2 kN.')

    def jamfor():
        k = 244 / d
        b = ''
        for i, (namn, r, br, slut) in enumerate((('50 km/h', s_r, s_b, 'stannar'), ('70 km/h', s_r70, kvar_k, '57 km/h'))):
            y = 36 + i * 76
            b += tt(10, y - 8, namn, 14, 'start', bold=True)
            b += rekt(10, y, r * k, 28, '#e4ecf1', GRA, 1.2) + rekt(10 + r * k, y, br * k, 28, '#f6d9c3', ORA, 1.2)
            b += tt(10 + r * k / 2, y + 19, f'{r:.1f} m'.replace('.', ','), 14) + tt(10 + r * k + br * k / 2, y + 19, f'{br:.1f} m'.replace('.', ','), 14)
            b += tt(264, y + 19, slut, 14, 'start', ROD if i else GRON, True)
        b += linje(256, 18, 256, 146, INK, 2) + tt(256, 164, 'trädet', 14)
        b += rekt(10, 178, 14, 12, '#e4ecf1', GRA, 1.2) + tt(30, 189, 'reaktionssträcka', 14, 'start')
        b += rekt(10, 198, 14, 12, '#f6d9c3', ORA, 1.2) + tt(30, 209, 'bromssträcka', 14, 'start')
        return svg(336, 220, b, 'Sträckan fram till trädet vid två farter. Vid 50 km/h är reaktionssträckan 11,1 m och bromssträckan 12,9 m, '
                                'och bilen stannar vid trädet. Vid 70 km/h är reaktionssträckan 15,6 m och det återstår bara 8,4 m att bromsa på, '
                                'så bilen har farten 57 km/h vid trädet.')

    intro = (p('En bil på 1 500 kg kör på en rak och vågrät landsväg. Föraren upptäcker ett träd som har fallit över vägen. Det tar 0,80 s '
               'innan hon börjar bromsa, och under den tiden är farten oförändrad. Sedan bromsas bilen av en konstant kraft på 11,2 kN.') + fig())
    givet = li(GIVET, al(r'm=1\,500\ \mathrm{kg}', r'F=11{,}2\ \mathrm{kN}=11\,200\ \mathrm N', r't_r=0{,}80\ \mathrm s',
                         r'v_0=50\ \mathrm{km/h}=\tfrac{50}{3{,}6}\ \mathrm{m/s}\approx13{,}9\ \mathrm{m/s}'))
    givet_c = li(GIVET, al(r'm=1\,500\ \mathrm{kg}', r'F=11{,}2\ \mathrm{kN}=11\,200\ \mathrm N', r't_r=0{,}80\ \mathrm s',
                           r'v_0=70\ \mathrm{km/h}=\tfrac{70}{3{,}6}\ \mathrm{m/s}\approx19{,}4\ \mathrm{m/s}',
                           r'\text{avstånd till trädet: }24{,}0\ \mathrm m'))
    arbete = li(r'Bromskraftens arbete tar bort rörelseenergin: \(Fs=\tfrac{mv_0^2}{2}\)',
                p('Bromskraften är riktad mot rörelsen. När bilen står stilla har hela rörelseenergin blivit värme i bromsarna.'),
                al(r's=\frac{mv_0^2}{2F}=\frac{1\,500\cdot13{,}89^2}{2\cdot11\,200}', rf's\approx{tx(s_b, 1)}\ \mathrm m'))
    steg_a = [sokt(givet, 'bromssträckan från 50 km/h.'), arbete[:-5] + p('De givna värdena har två värdesiffror, så svaret avrundas till 13 m.') + '</li>']
    steg_b = [sokt(givet, 'avståndet till trädet när föraren upptäcker det.'),
              li(r'Under reaktionstiden är farten konstant: \(s=vt\)', mt(rf's_r=13{{,}}89\cdot0{{,}}80\approx{tx(s_r, 1)}\ \mathrm m')), arbete,
              li('Lägg ihop reaktionssträckan och bromssträckan', mt(rf'{tx(s_r, 1)}+{tx(s_b, 1)}={tx(d, 1)}\ \mathrm m'),
                 p('Två värdesiffror ger 24 m.'))]
    steg_c = [sokt(givet_c, 'bilens fart när den når trädet.'),
              li(r'Reaktionssträckan blir längre: \(s=vt\)', mt(rf's_r=19{{,}}44\cdot0{{,}}80\approx{tx(s_r70, 1)}\ \mathrm m'),
                 p(f'Det återstår 24,0 − {tx(s_r70, 1).replace("{,}", ",")} = {tx(kvar_k, 1).replace("{,}", ",")} m att bromsa på.')),
              li(r'Arbete och energi: \(\tfrac{mv_0^2}{2}-Fs=\tfrac{mv^2}{2}\)',
                 p('Bromskraften hinner bara ta bort en del av rörelseenergin innan bilen är framme vid trädet.'),
                 al(rf'\frac{{mv_0^2}}{{2}}=\frac{{1\,500\cdot19{{,}}44^2}}{{2}}\approx{E0 / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}',
                    rf'Fs=11\,200\cdot{tx(kvar_k, 2)}\approx{F * kvar_k / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}',
                    rf'\frac{{mv^2}}{{2}}={E0 / 1000:.1f}-{F * kvar_k / 1000:.1f}={(E0 - F * kvar_k) / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}')),
              li('Lös ut farten och räkna om till km/h',
                 al(rf'v=\sqrt{{\frac{{2\cdot{tusen(E0 - F * kvar_k)}}}{{1\,500}}}}\approx{tx(v_k, 1)}\ \mathrm{{m/s}}',
                    rf'{tx(v_k, 1)}\cdot3{{,}}6\approx{tx(v_k * 3.6, 0)}\ \mathrm{{km/h}}'), jamfor(),
                 p('Utgångsfarten var bara 20 km/h högre, men bilen har ändå högre fart vid trädet än 50 km/h. Reaktionssträckan blir längre, '
                   'och rörelseenergin växer med kvadraten på farten.'))]
    delar = [
        del_('Hur lång är bromssträckan om farten är 50 km/h när bromsningen börjar?', steg_a, '13 m.',
             'Hur mycket rörelseenergi har bilen? Hela den energin ska tas bort av bromskraftens arbete.',
             s_b, 'C', 3, (0, 1, 0), tol=0.5, enhet='m', vs=2, ratt_txt=['13', '12,9', '13 m', '12,92'], fel=['11', '24', '19', '14', '170']),
        del_('Vid 50 km/h stannar bilen precis framför trädet. Hur långt bort var trädet när föraren upptäckte det?', steg_b, '24 m.',
             'Sträckan består av två delar: en där farten är konstant och en där bilen bromsar.',
             d, 'C', 4, (0, 1, 0), tol=0.5, enhet='m', vs=2, ratt_txt=['24', '24,0', '24 m', '24,03'], fel=['13', '11', '54', '40', '25']),
        del_('Vilken fart har bilen när den når trädet, om farten i stället är 70 km/h när föraren upptäcker det? (Svara i km/h.)', steg_c,
             '57 km/h.', 'Hur lång sträcka finns kvar att bromsa på när reaktionssträckan är avklarad? Hur mycket rörelseenergi hinner '
             'bromskraften ta bort på den sträckan?', v * 3.6, 'A', 5, (0, 0, 2), tol=0.5, enhet='km/h', vs=2, ai=3,
             ratt_txt=['57', '57,1', '57 km/h', '57,10'], fel=['20', '49', '16', '70', '0', '56'],
             kortfraga='Trädet låg 24,0 m bort när föraren upptäckte det. Vilken fart har bilen när den når trädet, om farten är 70 km/h '
                       'när föraren upptäcker det? (Svara i km/h.)'),
    ]
    return H.bygg(uid, 5, 'rorelseenergi', 'Nettoarbete och energiförluster', intro, delar, ('problemlösning', 'modellering'), True, False,
                  'Bromskraftens arbete minskar bilens rörelseenergi. Glöm inte sträckan som bilen rullar innan bromsningen börjar.',
                  VARIANTER, fy=True, familjnyckel=NYCKEL['rorelseenergi|Nettoarbete och energiförluster'])


# ================================================================ Q3: länspump i källare (effekt och verkningsgrad)
def q3(uid):
    mm = 998 * 6.0 * 4.0 * 0.25
    Ep = mm * g * 3.2
    Ek = mm * 7.0 ** 2 / 2
    Eel = 750 * 720.0
    eta = (Ep + Ek) / Eel
    Ek2 = mm * 3.0 ** 2 / 2
    t2 = (Ep + Ek2) / eta / 750
    t2_k = (Ep + Ek2) / 0.620 / 750
    assert abs(mm - 5988) < 1e-9 and abs(Ep - 188166.9) < 0.1 and abs(eta - 0.62014) < 1e-4 and abs(t2 / 60 - 7.708) < 2e-3
    assert abs(t2_k - t2) < 1 and 0 < eta < 1 and f'{t2_k / 60:.3g}' == f'{t2 / 60:.3g}' == '7.71'

    def fig():
        b = rekt(0, 74, 440, 156, '#efe6d8', 'none', 0, 0) + rekt(150, 74, 164, 126, '#fff', 'none', 0, 0)
        b += linje(0, 74, 150, 74, INK, 2) + linje(314, 74, 440, 74, INK, 2)
        b += linje(150, 74, 150, 200, INK, 3) + linje(314, 74, 314, 200, INK, 3) + linje(150, 200, 314, 200, INK, 3)
        b += rekt(152, 170, 160, 29, VATTEN, 'none', 0, 0) + linje(152, 170, 312, 170, BLA, 1.6)
        b += rekt(170, 178, 28, 18, '#9fb0bd', INK, 1.4)
        b += ('<polyline points="198,187 292,187 292,56 346,56" fill="none" stroke="#3d5a6c" stroke-width="5" stroke-linejoin="round"/>')
        b += pil(346, 56, 398, 56, BLA, 3) + tt(372, 42, '7,0 m/s', 14, fill=BLA, bold=True)
        b += tt(232, 108, 'källare', 14, fill=GRA) + tt(232, 126, '6,0 m × 4,0 m', 14)
        b += tt(232, 162, '25 cm vatten', 13, fill=BLA, bold=True)
        b += linje(118, 170, 150, 170, GRA, 1.2, '4 3') + linje(118, 56, 292, 56, GRA, 1.2, '4 3')
        b += linje(112, 56, 112, 170, GRA, 1.6) + linje(106, 56, 118, 56, GRA, 1.6) + linje(106, 170, 118, 170, GRA, 1.6)
        b += tt(104, 118, '3,2 m', 14, 'end')
        b += tt(184, 220, 'pump, 750 W', 13, fill=INK)
        return svg(440, 230, b, 'En källare i genomskärning med 25 cm vatten på golvet. Golvytan är 6,0 m gånger 4,0 m. En pump på 750 W '
                                'står i vattnet. En slang leder upp till marken och mynnar 3,2 m över vattenytan, där vattnet sprutar ut '
                                'med farten 7,0 m/s.')

    def stapel():
        k = 196 / Eel
        rader = (('elenergi', Eel, '#f3e3b5', ORA), ('lägesenergi', Ep, VATTEN, BLA), ('rörelseenergi', Ek, '#d9ecd9', GRON),
                 ('förluster', Eel - Ep - Ek, '#eceff1', GRA))
        b = ''
        for i, (namn, e, fyll, kant) in enumerate(rader):
            y = 14 + i * 36 + (10 if i else 0)
            b += tt(10, y + 18, namn, 14, 'start', bold=not i) + rekt(112, y, e * k, 26, fyll, kant, 1.6)
            b += tt(112 + e * k + 8, y + 18, f'{e / 1000:.0f} kJ', 14, 'start', bold=not i)
        b += linje(10, 52, 366, 52, GRA, 1.2)
        b += linje(104, 66, 104, 124, INK, 1.6) + linje(98, 66, 104, 66, INK, 1.6) + linje(98, 124, 104, 124, INK, 1.6)
        b += tt(188, 182, f'nyttig energi: {Ep / 1000:.0f} + {Ek / 1000:.0f} = {(Ep + Ek) / 1000:.0f} kJ', 14)
        return svg(376, 194, b, f'Staplar som visar hur elenergin 540 kJ fördelas: {Ep / 1000:.0f} kJ blir lägesenergi, {Ek / 1000:.0f} kJ blir '
                                f'rörelseenergi och {(Eel - Ep - Ek) / 1000:.0f} kJ är förluster. Den nyttiga energin är '
                                f'{(Ep + Ek) / 1000:.0f} kJ, alltså 62 % av elenergin.')

    intro = (p('Efter ett skyfall står det 25 cm vatten på golvet i en källare. Golvytan är 6,0 m × 4,0 m. Vattnet pumpas ut genom en slang '
               'som mynnar 3,2 m över vattenytan, och det lämnar slangen med farten 7,0 m/s. Pumpen drar 750 W el, och det tar 12 minuter att '
               'tömma källaren. Vattnets densitet är 998 kg/m³. Räkna med att allt vatten lyfts 3,2 m.') + fig())
    massa = [r'V=6{,}0\cdot4{,}0\cdot0{,}25=6{,}0\ \mathrm{m^3}', r'm=\rho V=998\cdot6{,}0=5\,988\ \mathrm{kg}', r'h=3{,}2\ \mathrm m']
    givet_a = li(GIVET, al(*massa))
    givet_b = li(GIVET, al(*massa, r'v=7{,}0\ \mathrm{m/s}', r'P=750\ \mathrm W', r't=12\ \mathrm{min}=720\ \mathrm s'))
    givet_c = li(GIVET, al(*massa, r'v=3{,}0\ \mathrm{m/s}', r'P=750\ \mathrm W', r'\eta=62{,}0\ \%=0{,}620'))
    lage = li(r'Lägesenergi: \(E_p=mgh\)', al(r'E_p=5\,988\cdot9{,}82\cdot3{,}2', rf'E_p\approx{Ep / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}'))
    steg_a = [sokt(givet_a, 'ökningen av vattnets lägesenergi.'),
              li(r'Lägesenergi: \(E_p=mgh\)', al(r'E_p=5\,988\cdot9{,}82\cdot3{,}2', rf'E_p\approx{Ep / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}'),
                 p('De givna värdena har två värdesiffror, så svaret avrundas till 190 kJ.'))]
    steg_b = [sokt(givet_b, 'andelen av elenergin som blir lägesenergi och rörelseenergi hos vattnet.'), lage,
              li(r'Rörelseenergi: \(E_k=\tfrac{mv^2}{2}\)', p('Vattnet har fart när det lämnar slangen. Den rörelseenergin har pumpen också gett vattnet.'),
                 mt(rf'E_k=\frac{{5\,988\cdot7{{,}}0^2}}{{2}}\approx{Ek / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}')),
              li(r'Tillförd elenergi: \(E=Pt\)', al(r'E_{\text{el}}=750\cdot720=540\,000\ \mathrm J', r'E_{\text{el}}=540\ \mathrm{kJ}')),
              li(r'Verkningsgrad: \(\eta=\tfrac{E_{\text{nyttig}}}{E_{\text{tillförd}}}\)',
                 al(rf'\eta=\frac{{{Ep / 1000:.1f}+{Ek / 1000:.1f}}}{{540}}'.replace('.', '{,}'), rf'\eta\approx{tx(eta, 3)}\approx62\ \%'), stapel())]
    steg_c = [sokt(givet_c, 'tiden för att tömma källaren när vattnet lämnar slangen med 3,0 m/s.'),
              li(r'Nyttig energi: \(E=mgh+\tfrac{mv^2}{2}\)', p('Vattnet lyfts lika högt som förut, men det får mindre rörelseenergi.'),
                 al(r'E=5\,988\cdot9{,}82\cdot3{,}2+\frac{5\,988\cdot3{,}0^2}{2}',
                    rf'E\approx{Ep / 1000:.1f}+{Ek2 / 1000:.1f}={(Ep + Ek2) / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}')),
              li(r'Verkningsgraden ger elenergin: \(E_{\text{el}}=\tfrac{E}{\eta}\)',
                 mt(rf'E_{{\text{{el}}}}=\frac{{{(Ep + Ek2) / 1000:.1f}}}{{0{{,}}620}}\approx{(Ep + Ek2) / 0.620 / 1000:.1f}'.replace('.', '{,}') + r'\ \mathrm{kJ}')),
              li(r'Tiden ur \(E=Pt\)', al(rf't=\frac{{{tusen((Ep + Ek2) / 0.620)}}}{{750}}\approx{t2_k:.0f}\ \mathrm s', rf'\frac{{{t2_k:.0f}}}{{60}}\approx{tx(t2_k / 60, 1)}\ \mathrm{{min}}'),
                 p('Pumpningen går fortare, eftersom en mindre del av energin går åt till att ge vattnet fart.'))]
    delar = [
        del_('Hur mycket ökar vattnets lägesenergi när det pumpas upp? (Svara i kJ.)', steg_a, '190 kJ.',
             'Bestäm först vattnets volym och massa. Hur högt lyfts vattnet?', Ep / 1000, 'C', 3, (0, 1, 0), tol=5, enhet='kJ', vs=2,
             ratt_txt=['190', '188', '188,2', '190 kJ'], fel=['150', '330', '19', '540', '59', '210']),
        del_('Hur stor andel av elenergin blir lägesenergi och rörelseenergi hos vattnet? (Svara i procent.)', steg_b, '62 %.',
             'Vattnet får både lägesenergi och rörelseenergi. Jämför summan med den elenergi som pumpen har dragit under 12 minuter.',
             eta * 100, 'C', 4, (0, 1, 0), tol=0.5, enhet='%', vs=2, ratt_txt=['62', '62,0', '62 %', '62%'], fel=['35', '27', '38', '0,62', '161', '65']),
        del_('Med ett grövre munstycke lämnar vattnet slangen med bara 3,0 m/s. Hur lång tid tar det då att tömma källaren, om pumpens '
             'eleffekt och verkningsgrad är oförändrade? (Svara i minuter.)', steg_c, '7,7 min.',
             'Hur mycket nyttig energi behövs nu? Använd verkningsgraden för att bestämma hur mycket elenergi det motsvarar.',
             t2 / 60, 'A', 5, (0, 0, 2), tol=0.05, enhet='min', vs=2, ai=3, ratt_txt=['7,7', '7,71', '7,7 min'],
             fel=['12', '5,2', '463', '4,6', '8,6', '7,9'],
             kortfraga='Pumpens verkningsgrad är 62,0 %. Med ett grövre munstycke lämnar vattnet slangen med bara 3,0 m/s. Hur lång tid tar det '
                       'då att tömma källaren, om pumpens eleffekt och verkningsgrad är oförändrade? (Svara i minuter.)'),
    ]
    return H.bygg(uid, 5, 'effekt', 'Verkningsgrad', intro, delar, ('problemlösning', 'modellering'), True, False,
                  'Pumpen ger vattnet både lägesenergi och rörelseenergi. Jämför den nyttiga energin med elenergin.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['effekt|Verkningsgrad'])


# ================================================================ Q4: te, mugg och mjölk (värmebalans)
def q4(uid):
    Cte, Cm = 4.18 * 0.25, 0.80 * 0.30
    T1 = (Cte * 95 + Cm * 20) / (Cte + Cm)
    mj = (Cte + Cm) * (T1 - 60) / (3.9 * (60 - 6))
    mj_k = (Cte + Cm) * (81.0 - 60) / (3.9 * 54)
    assert abs(T1 - 80.9922) < 1e-3 and abs(mj - 0.12809) < 1e-4 and abs(mj_k - 0.12813) < 1e-4 and f'{mj:.3g}' == f'{mj_k:.3g}'
    assert abs(Cte * (95 - T1) - Cm * (T1 - 20)) < 1e-9 and abs((Cte + Cm) * (T1 - 60) - 3.9 * mj * 54) < 1e-9

    def fig():
        b = rekt(120, 70, 96, 96, '#f4f1ea', INK, 2.4, 8) + rekt(128, 84, 80, 74, '#c98f4e', 'none', 0, 4)
        b += f'<path d="M216 92 C252 92 252 144 216 144" fill="none" stroke="{INK}" stroke-width="7"/>'
        b += f'<path d="M216 92 C252 92 252 144 216 144" fill="none" stroke="#f4f1ea" stroke-width="3"/>'
        for x in (148, 168, 188):
            b += f'<path d="M{x} 62 C{x - 8} 50 {x + 8} 42 {x} 28" fill="none" stroke="{GRA}" stroke-width="1.6" stroke-linecap="round"/>'
        b += linje(168, 120, 96, 120, GRA, 1.2) + tt(92, 114, 'te', 14, 'end', bold=True) + tt(92, 132, '0,25 kg, 95 °C', 13, 'end')
        b += linje(160, 166, 160, 186, GRA, 1.2) + tt(168, 196, 'porslinsmugg, 0,30 kg, 20 °C', 13)
        b += rekt(316, 74, 58, 92, '#fff', INK, 2) + polygon_tak(316, 74, 58) + tt(345, 116, 'mjölk', 14, bold=True) + tt(345, 136, '6 °C', 13)
        return svg(440, 208, b, 'En porslinsmugg på 0,30 kg med temperaturen 20 °C fylls med 0,25 kg te som är 95 °C. Bredvid står ett '
                                'mjölkpaket med temperaturen 6 °C.')

    def polygon_tak(x, y, w):
        return f'<polygon points="{x},{y} {x + w / 2},{y - 22} {x + w},{y}" fill="#fff" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>'

    intro = (p('Maja häller 0,25 kg te med temperaturen 95 °C i en porslinsmugg på 0,30 kg. Muggen har temperaturen 20 °C. Te och mugg får '
               'snabbt samma temperatur, innan någon energi hinner avges till omgivningen. Teet har samma specifika värmekapacitet som vatten, '
               '4,18 kJ/(kg·K). För porslin är den 0,80 kJ/(kg·K) och för mjölk 3,9 kJ/(kg·K).') + fig())
    givet_a = li(GIVET, al(r'm_{\text{te}}=0{,}25\ \mathrm{kg},\quad T_{\text{te}}=95\ ^\circ\mathrm C',
                           r'm_{\text{mugg}}=0{,}30\ \mathrm{kg},\quad T_{\text{mugg}}=20\ ^\circ\mathrm C',
                           r'c_{\text{te}}=4{,}18\ \mathrm{kJ/(kg\cdot K)}', r'c_{\text{porslin}}=0{,}80\ \mathrm{kJ/(kg\cdot K)}'))
    givet_b = li(GIVET, al(r'm_{\text{te}}=0{,}25\ \mathrm{kg},\quad m_{\text{mugg}}=0{,}30\ \mathrm{kg}',
                           r'c_{\text{te}}=4{,}18\ \mathrm{kJ/(kg\cdot K)}', r'c_{\text{porslin}}=0{,}80\ \mathrm{kJ/(kg\cdot K)}',
                           r'c_{\text{mjölk}}=3{,}9\ \mathrm{kJ/(kg\cdot K)}', r'\text{te och mugg: }81{,}0\ ^\circ\mathrm C',
                           r'\text{mjölk: }6\ ^\circ\mathrm C', r'\text{sluttemperatur: }60\ ^\circ\mathrm C'))
    steg_a = [sokt(givet_a, 'den gemensamma temperaturen \\(T\\) hos te och mugg.'),
              li(r'Värmeenergi \(E=cm\Delta T\): avgiven energi är lika med upptagen energi',
                 p('Teet svalnar och avger energi. Muggen blir varmare och tar upp lika mycket energi.'),
                 al(r'4{,}18\cdot0{,}25\cdot(95-T)', r'\qquad=0{,}80\cdot0{,}30\cdot(T-20)', r'1{,}045\cdot(95-T)=0{,}240\cdot(T-20)')),
              li(r'Multiplicera in och samla termerna med \(T\)',
                 al(r'99{,}275-1{,}045T=0{,}240T-4{,}80', r'104{,}075=1{,}285T', rf'T=\frac{{104{{,}}075}}{{1{{,}}285}}\approx{tx(T1, 1)}\ ^\circ\mathrm C'),
                 p('Muggen sänker alltså teets temperatur med 14 grader.'))]
    steg_b = [sokt(givet_b, 'mjölkens massa \\(m\\).'),
              li(r'Te och mugg svalnar tillsammans: \(E=cm\Delta T\) för båda',
                 p('När mjölken hälls i svalnar både teet och muggen från 81,0 °C till 60 °C.'),
                 al(r'E=(4{,}18\cdot0{,}25+0{,}80\cdot0{,}30)', r'\qquad\cdot(81{,}0-60)', rf'E=1{{,}}285\cdot21{{,}}0\approx{tx((Cte + Cm) * 21.0, 1)}\ \mathrm{{kJ}}')),
              li('Mjölken tar upp samma energi när den värms från 6 °C till 60 °C',
                 al(rf'3{{,}}9\cdot m\cdot(60-6)={tx((Cte + Cm) * 21.0, 1)}', rf'm=\frac{{{tx((Cte + Cm) * 21.0, 1)}}}{{210{{,}}6}}\approx{tx(mj_k, 3)}\ \mathrm{{kg}}'),
                 p('Det är 128 g, drygt en deciliter mjölk. Två värdesiffror ger 130 g.'))]
    delar = [
        del_('Vilken gemensam temperatur får teet och muggen?', steg_a, '81 °C.',
             'Teet avger energi och muggen tar upp lika mycket. Skriv ett uttryck för vardera energin med den okända temperaturen T.',
             T1, 'C', 4, (0, 2, 0), tol=0.5, enhet='°C', vs=2, ratt_txt=['81', '81,0', '81 °C', '80,99'], fel=['58', '95', '75', '88', '57,5', '79']),
        del_('Maja vill dricka teet när det är 60 °C. Hon häller därför i mjölk som är 6 °C. Hur mycket mjölk behövs? (Svara i gram.)',
             steg_b, '130 g.', 'Både teet och muggen svalnar när mjölken hälls i. Den energi de avger värmer mjölken.',
             mj * 1000, 'A', 5, (0, 0, 2), tol=5, enhet='g', vs=2, ai=3, ratt_txt=['130', '128', '130 g', '128 g', '128,1'],
             fel=['110', '0,13', '150', '89', '25', '120'],
             kortfraga='Teet och muggen har fått den gemensamma temperaturen 81,0 °C. Maja vill dricka teet när det är 60 °C. Hon häller därför '
                       'i mjölk som är 6 °C. Hur mycket mjölk behövs? (Svara i gram.)'),
    ]
    return H.bygg(uid, 7, 'varme', 'Värmebalans och termisk jämvikt', intro, delar, ('problemlösning', 'modellering'), True, False,
                  'Energin som de varma föremålen avger är lika stor som energin som de kalla tar upp. Muggen ska också räknas med.',
                  VARIANTER, fy=True, familjnyckel=NYCKEL['varme|Värmebalans och termisk jämvikt'])


# ================================================================ Q5: ambulanshelikopter i sidvind (vektorer)
def q5(uid):
    th = math.degrees(math.asin(15 / 60))
    v1 = math.sqrt(60 ** 2 - 15 ** 2)
    t1 = 90000 / v1
    w = 15 * math.cos(math.radians(45))
    th2 = math.degrees(math.asin(w / 60))
    v2 = 60 * math.cos(math.radians(th2)) + w
    t2 = 90000 / v2
    assert abs(th - 14.4775) < 1e-3 and abs(t1 / 60 - 25.820) < 1e-3 and abs(th2 - 10.182) < 1e-3 and abs(t2 / 60 - 21.533) < 2e-3
    # Kontroll med vektoraddition: östkomposanten ska bli noll i båda fallen.
    assert abs(-60 * math.sin(math.radians(th)) + 15) < 1e-9 and abs(-60 * math.sin(math.radians(th2)) + w) < 1e-9

    def fig():
        b = pil(40, 96, 40, 36, INK, 2.4, 10) + tt(40, 26, 'N', 15, bold=True)
        b += linje(210, 222, 210, 52, GRA, 1.6, '6 5') + cirkel(210, 222, 6, BLA) + tt(222, 240, 'start', 14, 'start')
        b += rekt(196, 24, 28, 28, '#fff', ROD, 2) + linje(210, 30, 210, 46, ROD, 4) + linje(202, 38, 218, 38, ROD, 4) + tt(232, 43, 'sjukhus', 14, 'start')
        b += tt(222, 142, '90 km', 14, 'start')
        for y in (96, 136, 176):
            b += pil(70, y, 138, y, ORA, 2.6, 10)
        b += tt(104, 80, 'vind 15 m/s', 14, fill=ORA, bold=True)
        return svg(340, 252, b, 'Karta med norr uppåt. Helikoptern startar nedtill och ska flyga 90 km rakt norrut till ett sjukhus. '
                                'Vinden blåser 15 m/s från väst, alltså åt öster.')

    def triangel(vx, vy, label, beskr, theta):
        k = 3.0
        O = (176, 250)
        P = (O[0] - vx * k, O[1] - (vy_luft := math.sqrt(3600 - vx ** 2)) * k)
        Q = (O[0], P[1] - vy * k)
        b = pil(*O, *P, BLA, 3) + pil(*P, *Q, ORA, 3) + pil(*O, *Q, GRON, 3)
        b += tt(P[0] - 10, (O[1] + P[1]) / 2, '60 m/s', 14, 'end', BLA, True) + tt(P[0] - 10, (O[1] + P[1]) / 2 + 17, 'genom luften', 13, 'end', BLA)
        b += tt((P[0] + Q[0]) / 2 + (0 if vy == 0 else 14), P[1] - 10 - (vy * k) / 2 - (0 if vy == 0 else 8), label, 14, 'middle' if vy == 0 else 'end', ORA, True)
        b += tt(O[0] + 12, (O[1] + Q[1]) / 2, 'över marken', 13, 'start', GRON, True) + tt(O[0] + 12, (O[1] + Q[1]) / 2 + 17, '(rakt norrut)', 13, 'start', GRON)
        halv = math.radians(theta / 2)
        r1, r2 = 104, 128
        a1 = (O[0] - r1 * math.sin(math.radians(theta)), O[1] - r1 * math.cos(math.radians(theta)))
        b += f'<path d="M{O[0]:.1f} {O[1] - r1:.1f} A{r1} {r1} 0 0 0 {a1[0]:.1f} {a1[1]:.1f}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
        b += tt(O[0] - r2 * math.sin(halv), O[1] - r2 * math.cos(halv) + 5, 'θ', 14, 'middle', INK, True)
        return svg(330, 270, b, beskr)

    tri1 = lambda: triangel(15, 0, 'vind 15 m/s', 'Vektortriangel. Helikopterns hastighet genom luften, 60 m/s, pekar snett åt nordväst. Vindens hastighet, '
                            '15 m/s österut, läggs till i spetsen. Summan, hastigheten över marken, pekar rakt norrut. Vinkeln theta ligger '
                            'mellan hastigheten genom luften och norr.', th)
    tri2 = lambda: triangel(w, w, 'vind 15 m/s', 'Vektortriangel när vinden blåser mot nordost. Helikopterns hastighet genom luften, 60 m/s, pekar lite '
                            'åt väster om norr. Vindens hastighet läggs till i spetsen och pekar snett uppåt höger. Summan pekar rakt norrut '
                            'och är längre än 60 m/s.', th2)

    intro = (p('En ambulanshelikopter ska flyga rakt norrut till ett sjukhus som ligger 90 km bort. Helikopterns fart genom luften är 60 m/s. '
               'Det blåser 15 m/s från väst, så luften rör sig österut.') + fig())
    givet = li(GIVET, al(r'v_{\text{luft}}=60\ \mathrm{m/s}', r'v_{\text{vind}}=15\ \mathrm{m/s}\ \text{österut}', r's=90\ \mathrm{km}=90\,000\ \mathrm m'),
               p('Hastigheten över marken är summan av helikopterns hastighet genom luften och vindens hastighet. Summan ska peka rakt norrut.'))
    givet_c = li(GIVET, al(r'v_{\text{luft}}=60\ \mathrm{m/s}', r'v_{\text{vind}}=15\ \mathrm{m/s}\ \text{mot nordost}', r's=90\ \mathrm{km}=90\,000\ \mathrm m'),
                 p('Vind från sydväst blåser mot nordost, mitt emellan norr och öst. Hastigheten över marken ska fortfarande peka rakt norrut.'))
    summa = li('Rita vektorsumman', tri1(), p('Piloten måste rikta helikoptern snett mot vinden. De tre hastigheterna bildar en rätvinklig triangel, '
                                              'där hastigheten genom luften är hypotenusan och vindens hastighet står mot vinkeln \\(\\theta\\).'))
    steg_a = [sokt(givet, 'vinkeln \\(\\theta\\) väster om norr som helikoptern ska riktas i.'), summa,
              li(r'Sinus för vinkeln: \(\sin\theta=\tfrac{v_{\text{vind}}}{v_{\text{luft}}}\)',
                 al(r'\sin\theta=\frac{15}{60}=0{,}25', rf'\theta=\sin^{{-1}}(0{{,}}25)\approx{tx(th, 1)}^\circ'), p('Två värdesiffror ger 14°.'))]
    steg_b = [sokt(givet, 'flygtiden.'), summa,
              li(r'Pythagoras sats ger farten över marken: \(v^2=v_{\text{luft}}^2-v_{\text{vind}}^2\)',
                 al(r'v=\sqrt{60^2-15^2}', rf'v\approx{tx(v1, 1)}\ \mathrm{{m/s}}')),
              li(r'Konstant fart: \(t=\tfrac sv\)', al(rf't=\frac{{90\,000}}{{{tx(v1, 1)}}}\approx{t1:.0f}\ \mathrm s', rf'\frac{{{t1:.0f}}}{{60}}\approx{tx(t1 / 60, 0)}\ \mathrm{{min}}'))]
    steg_c = [sokt(givet_c, 'flygtiden när vinden blåser från sydväst.'),
              li(r'Dela upp vinden i komposanter: \(v_x=v\cos45^\circ\) och \(v_y=v\sin45^\circ\)',
                 al(rf'\text{{österut: }}15\cdot\cos45^\circ\approx{tx(w, 1)}\ \mathrm{{m/s}}', rf'\text{{norrut: }}15\cdot\sin45^\circ\approx{tx(w, 1)}\ \mathrm{{m/s}}'), tri2()),
              li('Helikoptern måste ta ut vindens del österut',
                 p('Helikopterns hastighet genom luften ska ha en lika stor del västerut.'),
                 al(rf'60\cdot\sin\theta={tx(w, 1)}', rf'\theta\approx{tx(th2, 1)}^\circ')),
              li('Farten norrut är summan av helikopterns och vindens delar norrut',
                 al(rf'v=60\cdot\cos{tx(th2, 1)}^\circ+{tx(w, 1)}', rf'v\approx{tx(60 * math.cos(math.radians(th2)), 1)}+{tx(w, 1)}={tx(v2, 1)}\ \mathrm{{m/s}}')),
              li(r'Konstant fart: \(t=\tfrac sv\)', al(rf't=\frac{{90\,000}}{{{tx(v2, 1)}}}\approx{t2:.0f}\ \mathrm s', rf'\frac{{{t2:.0f}}}{{60}}\approx{tx(t2 / 60, 0)}\ \mathrm{{min}}'),
                 p('Nu hjälper vinden till norrut. Flygningen går därför fortare än i vindstilla väder, då den tar 25 min.'))]
    delar = [
        del_('Hur många grader väster om norr måste piloten rikta helikoptern för att den ska färdas rakt norrut?', steg_a, '14°.',
             'Hastigheten över marken är summan av hastigheten genom luften och vindens hastighet. Rita de tre hastigheterna som en triangel.',
             th, 'C', 3, (0, 1, 0), tol=0.5, enhet='°', vs=2, ratt_txt=['14', '14,5', '14°', '14,48'], fel=['76', '15', '4', '75,5', '0,25']),
        del_('Hur lång tid tar flygningen till sjukhuset? (Svara i minuter.)', steg_b, '26 min.',
             'Helikoptern är riktad snett mot vinden. Hur stor blir då farten över marken, rakt norrut?',
             t1 / 60, 'C', 4, (0, 1, 0), tol=0.5, enhet='min', vs=2, ratt_txt=['26', '25,8', '26 min', '25,82'], fel=['25', '24', '20', '1549', '33']),
        del_('En annan dag blåser det i stället 15 m/s från sydväst. Hur lång tid tar flygningen norrut till sjukhuset då? (Svara i minuter.)',
             steg_c, '22 min.', 'Dela upp vindens hastighet i en del österut och en del norrut. Vilken del måste helikoptern ta ut, och vilken hjälper till?',
             t2 / 60, 'A', 5, (0, 0, 2), tol=0.5, enhet='min', vs=2, ai=3, ratt_txt=['22', '21,5', '22 min', '21,53'], fel=['26', '25', '21', '23', '30', '19']),
    ]
    return H.bygg(uid, 3, 'vektorer', 'Relativ hastighet', intro, delar, ('problemlösning', 'modellering'), True, False,
                  'Hastigheten över marken är vektorsumman av hastigheten genom luften och vindens hastighet.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['vektorer|Relativ hastighet'])


# ================================================================ Q6: puck och kraft–tid-graf (rörelsemängd)
def q6(uid):
    mm = 0.170
    kraft = lambda u: 450 * u if u <= 2 else (900 if u <= 6 else max(0.0, 900 - 450 * (u - 6)))
    I = sum(kraft((i + 0.5) * 8 / 80000) * 8 / 80000 for i in range(80000)) / 1000
    v = -18 + I / mm
    I0 = mm * 18
    tc = 2 + (I0 - 0.9) / 900 * 1000
    assert abs(I - 5.4) < 1e-6 and abs(v - 13.7647) < 1e-3 and abs(tc - 4.4) < 1e-9 and 2 <= tc <= 6
    assert abs(0.9 + 900 * (tc - 2) / 1000 - I0) < 1e-9

    def graf(till=None, beskr=''):
        P = Plot(0, 9, 0, 1000, W=420, H=280, ml=54).axlar(xt=range(0, 9, 2), yt=(300, 600, 900), xlabel='t (ms)', ylabel='F (N)')
        if till:
            P.fyll(kraft, lambda u: 0, 0, till, BLA, 0.22)
        P.kurva(kraft, 0, 8, BLA)
        if till and till < 8:
            P.streck(till, 0, till, 900, ORA, 2, '5 4').text(till + 0.2, 640, '4,4 ms', ORA, 15, 'start', True)
            P.text(1.3, 70, '0,9 Ns', INK, 15, 'middle', True).text(3.15, 420, '2,16 Ns', INK, 15, 'middle', True)
        elif till:
            P.text(1.3, 70, '0,9 Ns', INK, 15, 'middle', True).text(4, 420, '3,6 Ns', INK, 15, 'middle', True).text(6.7, 70, '0,9 Ns', INK, 15, 'middle', True)
            P.streck(2, 0, 2, 900).streck(6, 0, 6, 900)
        return P.svg(beskr)

    bas = ('Kraften från klubban på pucken som funktion av tiden. Kraften ökar jämnt från 0 till 900 N under de första 2 ms, är 900 N '
           'från 2 ms till 6 ms och minskar sedan jämnt till 0 vid 8 ms.')
    intro = (p('En ishockeypuck på 170 g glider rakt mot en spelare med farten 18 m/s. Spelaren slår tillbaka pucken rakt åt motsatt håll. '
               'Diagrammet visar kraften från klubban på pucken under slaget. Bortse från friktionen mot isen.') + graf(None, bas))
    givet = li(GIVET, al(r'm=170\ \mathrm g=0{,}170\ \mathrm{kg}', r'v_0=-18\ \mathrm{m/s}'),
               p('Positiv riktning är den riktning som klubbans kraft har, bort från spelaren. Pucken kommer mot spelaren och har därför '
                 'negativ hastighet före slaget.'))
    givet_a = li(GIVET, p('Kraften avläses i diagrammet: den ökar jämnt till 900 N på 2 ms, är konstant till 6 ms och minskar jämnt till noll vid 8 ms.'),
                 mt(r'1\ \mathrm{ms}=0{,}001\ \mathrm s'))
    areal = li(r'Impulsen är arean under kraft–tid-grafen: \(I=F\Delta t\)', graf(8, bas + ' Arean under grafen är skuggad och uppdelad i en '
               'triangel med arean 0,9 Ns, en rektangel med arean 3,6 Ns och en triangel med arean 0,9 Ns.'),
               p('Dela arean i en triangel, en rektangel och en triangel.'),
               al(r'I=\frac{900\cdot0{,}002}{2}+900\cdot0{,}004', r'\qquad+\frac{900\cdot0{,}002}{2}', r'I=0{,}9+3{,}6+0{,}9=5{,}4\ \mathrm{Ns}'))
    steg_a = [sokt(givet_a, 'impulsen från klubban på pucken.'), areal]
    steg_b = [sokt(givet, 'puckens fart efter slaget.'), areal,
              li(r'Impulslagen: \(I=mv-mv_0\)', al(r'5{,}4=0{,}170\cdot v-0{,}170\cdot(-18)', r'5{,}4=0{,}170\cdot v+3{,}06',
                                                  rf'v=\frac{{2{{,}}34}}{{0{{,}}170}}\approx{tx(v, 1)}\ \mathrm{{m/s}}'),
                 p('Hastigheten är positiv. Pucken rör sig alltså bort från spelaren, med farten 14 m/s.'))]
    steg_c = [sokt(givet, 'tiden från att klubban träffar pucken tills pucken står stilla.'),
              li(r'Impulslagen: \(I=mv-mv_0\) med \(v=0\)', p('Så här stor impuls behövs för att stoppa pucken:'),
                 mt(r'I=0-0{,}170\cdot(-18)=3{,}06\ \mathrm{Ns}')),
              li('Jämför med arean under de första 2 ms', mt(r'\frac{900\cdot0{,}002}{2}=0{,}9\ \mathrm{Ns}'),
                 p('Det räcker inte. Det återstår 3,06 − 0,9 = 2,16 Ns, och den impulsen kommer medan kraften är 900 N.')),
              li(r'Konstant kraft: \(I=F\Delta t\)',
                 al(r'\Delta t=\frac{2{,}16}{900}=0{,}0024\ \mathrm s=2{,}4\ \mathrm{ms}', r't=2{,}0+2{,}4=4{,}4\ \mathrm{ms}'),
                 graf(tc, bas + ' Arean från 0 till 4,4 ms är skuggad: en triangel med arean 0,9 Ns och en rektangel med arean 2,16 Ns.'),
                 p('Tiden 4,4 ms ligger i den del där kraften är konstant, mellan 2 ms och 6 ms. Antagandet stämmer alltså.'))]
    delar = [
        del_('Hur stor impuls ger klubban pucken under hela slaget?', steg_a, '5,4 Ns.',
             'Vad betyder arean under en kraft–tid-graf? Tänk på att tiden står i millisekunder.',
             I, 'C', 3, (0, 1, 0), tol=0.05, enhet='Ns', vs=2, ratt_txt=['5,4', '5,40', '5,4 Ns'], fel=['7,2', '5400', '3,6', '3,06', '6,3']),
        del_('Vilken fart har pucken efter slaget?', steg_b, '14 m/s.',
             'Impulsen ändrar puckens rörelsemängd. Tänk på att pucken byter riktning, så hastigheten före slaget är negativ.',
             v, 'C', 4, (0, 1, 0), tol=0.5, enhet='m/s', vs=2, ratt_txt=['14', '13,8', '14 m/s', '13,76'], fel=['32', '50', '18', '49,8', '31,8'],
             kortfraga='Klubban ger pucken impulsen 5,4 Ns under slaget. Vilken fart har pucken efter slaget?'),
        del_('Hur lång tid efter att klubban träffar pucken står pucken stilla ett ögonblick? (Svara i ms.)', steg_c, '4,4 ms.',
             'Hur stor impuls krävs för att stoppa pucken? Hur långt in i slaget har arean under grafen blivit så stor?',
             tc, 'A', 5, (0, 0, 2), tol=0.05, enhet='ms', vs=2, ai=3, ratt_txt=['4,4', '4,40', '4,4 ms'], fel=['3,4', '2,4', '4,0', '4,5', '6,8', '0,0044']),
    ]
    return H.bygg(uid, 5, 'rorelsemangd', 'Impuls och medelkraft', intro, delar, ('problemlösning', 'begrepp'), True, False,
                  'Arean under kraft–tid-grafen är impulsen, och impulsen är lika med ändringen av puckens rörelsemängd.', VARIANTER, fy=True,
                  familjnyckel=NYCKEL['rorelsemangd|Impuls och medelkraft'])


UPPGIFTER = [(4, q1), (5, q2), (5, q3), (7, q4), (3, q5), (5, q6)]


def main():
    src, bank = H.las(BANK)
    antal = {}
    for q in bank:
        if q.get('familjNyckel'):
            k = f"{q['omr']}|{q['familj']}"
            antal.setdefault(k, {}).setdefault(q['familjNyckel'], 0)
            antal[k][q['familjNyckel']] += 1
    for k, v in antal.items():  # delmomentets vanligaste nyckel
        NYCKEL[k] = max(v, key=v.get)
    nasta, nya = {}, []
    for kap, funk in UPPGIFTER:
        nasta.setdefault(kap, H.nasta_id(bank, kap))
        nya.append(funk(f'{kap}.{nasta[kap]}'))
        nasta[kap] += 1
    assert not {q['id'] for q in bank} & {q['id'] for q in nya}
    print('uppgifter', len(nya), 'kort', sum(len(q.get('spelDelar') or [1]) for q in nya), [q['id'] for q in nya])
    print('nycklar', [q['familjNyckel'] for q in nya])
    if '--varianter' in sys.argv:
        Path(sys.argv[sys.argv.index('--varianter') + 1]).write_text(json.dumps(VARIANTER, ensure_ascii=False, indent=1), encoding='utf-8')
    if '--ut' in sys.argv:
        Path(sys.argv[sys.argv.index('--ut') + 1]).write_text(json.dumps(nya, ensure_ascii=False), encoding='utf-8')
    if '--skriv' in sys.argv:
        H.lagg_till(BANK, src, nya)


if __name__ == '__main__':
    main()
