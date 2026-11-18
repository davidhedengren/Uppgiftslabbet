"""Fysik 1 (uppgifter.js), densitet: blandningsuppgifter på A-nivå, 18 november 2026.

Felrapport 2026-11-18 11:38, fy1 #2.51: läraren bedömer att uppgifter där man bestämmer hur mycket det finns av
två ämnen ur blandningens densitet hör till A-nivå och vill ha fler sådana uppgifter på A-nivå.

1. Flyttar de fem befintliga uppgifterna av den typen till A (niva, poang, traningsniva): 2.51, 2.90, 2.146,
   2.200 och 2.202. Text, facit och självrättning ändras inte.
2. Lägger till sex nya, tuffare A-uppgifter med egna sammanhang, figur och facit enligt agent/FACITMALL.md.
   Alla tal räknas i skriptet och kontrolleras med assert. Se agent/FY1_DENSITET_A_2026-11-18.md.

  python tools/bygg-fy1-densitet-a-2026-11-18.py [--skriv] [--ut fil.json]
"""
import json
import math
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import (mt, al, p, li, del_, svg, tt, linje, pil, rekt, cirkel, tx,  # noqa: E402
                               BLA, ORA, GRON, GRA, INK, LJUS)

BANK = 'uppgifter.js'
VARIANTER = {}
GIVET = 'Givet och sökt'
VATTEN = '#cfe6f5'
SAMMANSATT = ('Sammansatta och ihåliga föremål', 'densitet__sammansatt_densitet_och_ihaliga_foremal')
FLYT = ('Densitet, flytförmåga och modeller', 'densitet__densitet_och_flytformaga')

# Befintliga uppgifter av typen "bestäm mängden av två ämnen ur blandningens densitet" -> A-nivå.
# id: (poang, traningsniva). 2.90 b är ett kort resonemang om att volymerna inte adderas exakt (C-poäng).
TILL_A = {
    '2.51': ('(0/0/3)', 5),
    '2.90': ('(0/1/2)', 5),
    '2.146': ('(0/0/2)', 4),
    '2.200': ('(0/0/2)', 5),
    '2.202': ('(0/0/2)', 4),
}


def sokt(steg, text):
    assert steg.endswith('</li>')
    return steg[:-5] + p('Sökt: ' + text) + '</li>'


def lika(a, b, tol=1e-9):
    assert abs(a - b) <= tol, (a, b)


# ================================================================ Q1: lödtenn i mätglas
def q1(uid):
    m, v0, v1, rs, rp = 52.0, 30.0, 36.0, 7.29, 11.34
    V = v1 - v0
    x = (V - m / rp) / (1 / rs - 1 / rp)          # tennets massa i gram
    andel = 100 * x / m
    lika(x / rs + (m - x) / rp, V)
    assert 7.29 < m / V < 11.34 and abs(andel - 55.52) < 0.01

    def glas(x0, niva, bit):
        y = lambda v: 222 - v * 3.6
        b = rekt(x0, y(50) - 6, 64, 222 - y(50) + 6, '#f7fafc', INK, 2, 4)
        b += f'<rect x="{x0 + 2}" y="{y(niva):.1f}" width="60" height="{220 - y(niva):.1f}" fill="{VATTEN}"/>'
        b += linje(x0 + 2, y(niva), x0 + 62, y(niva), BLA, 2)
        for v in range(0, 51, 5):
            b += linje(x0, y(v), x0 + (12 if v % 10 == 0 else 7), y(v), INK, 1.3)
            if v % 10 == 0:
                b += tt(x0 - 6, y(v) + 4.5, str(v), 12, 'end')
        if bit:
            b += rekt(x0 + 16, 200, 32, 18, '#7d8a95', INK, 1.5, 2)
        b += pil(x0 + 104, y(niva), x0 + 70, y(niva), BLA, 2, 8)
        b += tt(x0 + 108, y(niva) + 5, f'{tal(niva)} ml', 14, 'start', BLA, True)
        return b

    def fig():
        b = glas(70, v0, False) + glas(290, v1, True)
        b += tt(102, 246, 'före', 14) + tt(322, 246, 'efter', 14)
        b += tt(40, 26, 'ml', 13, 'middle', GRA)
        return svg(460, 256, b, 'Två mätglas med skala i milliliter. Före: vattnet står vid 30,0 ml. Efter att biten av lödtenn '
                                'sänkts ner står vattnet vid 36,0 ml.')

    intro = (p('Lödtenn är en legering av tenn och bly. Arvid har en bit lödtenn som väger 52,0 g. Han sänker ner biten i ett '
               'mätglas med vatten, se figuren.') + fig()
             + p('Tenn har densiteten 7,29 g/cm³ och bly 11,34 g/cm³. Antag att tennets och blyets volymer tillsammans är '
                 'bitens volym.'))
    steg = [sokt(li(GIVET, al(r'm=52{,}0\ \mathrm g', r'\rho_{\mathrm{Sn}}=7{,}29\ \mathrm{g/cm^3}',
                              r'\rho_{\mathrm{Pb}}=11{,}34\ \mathrm{g/cm^3}')),
                 'hur stor del av bitens massa som är tenn, i procent.'),
            li(r'Bitens volym ur mätglaset: \(V=V_{\text{efter}}-V_{\text{före}}\)',
               mt(r'V=36{,}0-30{,}0=6{,}0\ \mathrm{ml}=6{,}0\ \mathrm{cm^3}')),
            li(r'Massorna adderas: \(m_{\mathrm{Sn}}+m_{\mathrm{Pb}}=m\)',
               p('Låt x vara tennets massa i gram. Då väger blyet 52,0 − x gram.')),
            li(r'Volymerna adderas: \(V=\dfrac{m_{\mathrm{Sn}}}{\rho_{\mathrm{Sn}}}+\dfrac{m_{\mathrm{Pb}}}{\rho_{\mathrm{Pb}}}\)',
               p('Varje metalls volym är dess massa delad med dess densitet.'),
               mt(r'\frac{x}{7{,}29}+\frac{52{,}0-x}{11{,}34}=6{,}0')),
            li('Samla termerna med tennets massa',
               al(rf'{tx(1 / rs, 5)}x+{tx(m / rp, 4)}-{tx(1 / rp, 5)}x=6{{,}}0',
                  rf'{tx(1 / rs - 1 / rp, 5)}x={tx(V - m / rp, 4)}',
                  rf'x\approx{tx(x, 1)}\ \mathrm g')),
            li(r'Massprocent: \(\dfrac{m_{\mathrm{Sn}}}{m}\cdot100\,\%\)',
               mt(rf'\frac{{{tx(x, 1)}}}{{52{{,}}0}}\cdot100\,\%\approx{tx(andel, 0)}\,\%')),
            li(r'Kontroll med bitens densitet: \(\rho=\dfrac mV\)',
               mt(rf'\rho=\frac{{52{{,}}0}}{{6{{,}}0}}\approx{tx(m / V, 2)}\ \mathrm{{g/cm^3}}'),
               p('Densiteten ligger mellan tennets och blyets, så en blandning av de två metallerna är möjlig.'))]
    delar = [del_('Hur många procent av bitens massa är tenn?', steg, '56 %.', '', andel, 'A', 5, (0, 1, 2), tol=0.5,
                  enhet='%', vs=2, ratt_txt=['56', '55,5', '56 %'], fel=['44', '66', '50', '8,7', '29'])]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Läs av bitens volym i mätglasen. Kalla tennets massa för x. Vad blir då blyets massa, och vilken volym får '
               'varje metall?', VARIANTER, fy=True, familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma massprocent i en legering ur massa och volym avläst i mätglas'
    return q


# ================================================================ Q2: fetthalten i mjölk
def q2(uid):
    rs, rf, rm = 1.035, 0.92, 1.031
    x = (rs - rm) / (rs - rf)                     # fettets volymandel
    w = rf * x / rm                               # fettets massandel
    lika(rf * x + rs * (1 - x), rm)
    assert abs(100 * x - 3.478) < 1e-3 and abs(100 * w - 3.104) < 1e-3
    lika(round(100 * rf * 0.0348 / rm, 1), 3.1)   # b-kortets givna 3,48 % ger samma svar

    def fig():
        b = rekt(150, 30, 120, 150, '#fbfdff', INK, 2, 8)
        b += f'<rect x="152" y="52" width="116" height="126" rx="6" fill="#f4f1e8"/>'
        for (cx, cy, r) in ((178, 80, 4), (205, 70, 3), (236, 92, 5), (190, 118, 3), (222, 132, 4), (246, 150, 3),
                            (172, 156, 4), (208, 104, 3), (252, 118, 3), (186, 98, 2.5)):
            b += cirkel(cx, cy, r, '#f2c14e', '#b28a1b', 1)
        b += pil(292, 86, 245, 92, ORA, 2, 8) + tt(296, 84, 'fettdroppar', 14, 'start', ORA, True)
        b += tt(296, 102, '0,92 g/cm³', 13, 'start', INK)
        b += pil(292, 148, 262, 140, GRA, 2, 8) + tt(296, 146, 'skummjölk', 14, 'start', GRA, True)
        b += tt(296, 164, '1,035 g/cm³', 13, 'start', INK)
        b += tt(210, 202, 'mjölken: 1,031 g/cm³', 14, 'middle', INK, True)
        return svg(420, 214, b, 'Ett glas mjölk med fettdroppar i skummjölk. Fettet har densiteten 0,92 g/cm³ och skummjölken '
                                '1,035 g/cm³. Mjölken har densiteten 1,031 g/cm³.')

    intro = (p('Mjölk består av skummjölk med små fettdroppar i. Skummjölk har densiteten 1,035 g/cm³ och mjölkfett '
               '0,92 g/cm³. På ett mejeri mäter man densiteten hos ett prov mjölk till 1,031 g/cm³.') + fig()
             + p('Antag att fettets och skummjölkens volymer tillsammans är mjölkens volym.'))
    givet = li(GIVET, al(r'\rho_{\text{skum}}=1{,}035\ \mathrm{g/cm^3}', r'\rho_{\text{fett}}=0{,}92\ \mathrm{g/cm^3}',
                         r'\rho_{\text{mjölk}}=1{,}031\ \mathrm{g/cm^3}'))
    steg_a = [sokt(givet, 'hur stor del av mjölkens volym som är fett.'),
              li('Tänk dig 1 cm³ mjölk',
                 p('Låt x vara fettets volym i cm³. Då är skummjölkens volym 1 − x cm³, och hela provet väger 1,031 g.')),
              li(r'Massa: \(m=\rho V\)', p('Mjölkens massa är fettets massa plus skummjölkens massa.'),
                 mt(r'1{,}031=0{,}92x+1{,}035(1-x)')),
              li('Lös ut fettets volym',
                 al(r'1{,}031=1{,}035-0{,}115x', r'0{,}115x=0{,}004', rf'x=\frac{{0{{,}}004}}{{0{{,}}115}}\approx{tx(x, 4)}'),
                 p(f'Fettet är alltså {tx(x, 4).replace("{,}", ",")} cm³ av varje kubikcentimeter mjölk.')),
              li(r'Volymprocent: \(\dfrac{V_{\text{fett}}}{V}\cdot100\,\%\)', mt(rf'{tx(x, 4)}\cdot100\,\%\approx{tx(100 * x, 1)}\,\%'))]
    givet_b = li(GIVET, al(r'\rho_{\text{fett}}=0{,}92\ \mathrm{g/cm^3}', r'\rho_{\text{mjölk}}=1{,}031\ \mathrm{g/cm^3}'),
                 p('Fettet är 3,48 % av mjölkens volym, alltså 0,0348 cm³ i varje kubikcentimeter mjölk.'))
    steg_b = [sokt(givet_b, 'hur stor del av mjölkens massa som är fett.'),
              li(r'Fettets massa i 1 cm³ mjölk: \(m=\rho V\)', mt(r'm_{\text{fett}}=0{,}92\cdot0{,}0348\approx0{,}0320\ \mathrm g')),
              li(r'Mjölkens massa: \(m=\rho V\)', mt(r'm_{\text{mjölk}}=1{,}031\cdot1=1{,}031\ \mathrm g')),
              li(r'Massprocent: \(\dfrac{m_{\text{fett}}}{m_{\text{mjölk}}}\cdot100\,\%\)',
                 mt(rf'\frac{{0{{,}}0320}}{{1{{,}}031}}\cdot100\,\%\approx{tx(100 * w, 1)}\,\%')),
              li('Varför blir massprocenten mindre än volymprocenten?',
                 p('Fett har lägre densitet än skummjölk. En viss volym fett väger därför mindre än lika mycket skummjölk, '
                   'och fettets andel av massan blir mindre än dess andel av volymen.'))]
    delar = [
        del_('Hur många procent av mjölkens volym är fett?', steg_a, '3,5 %.',
             'Tänk dig 1 cm³ mjölk och kalla fettets volym för x. Vad väger fettet och skummjölken tillsammans?',
             100 * x, 'A', 5, (0, 0, 2), tol=0.05, enhet='%', vs=2, ratt_txt=['3,5', '3,48', '3,5 %'], fel=['0,35', '96,5', '3,1', '0,4']),
        del_('Mejeriet anger fetthalten som andel av massan. Hur många procent av mjölkens massa är fett?', steg_b, '3,1 %.',
             'Hur mycket väger fettet i 1 cm³ mjölk? Jämför med vad hela kubikcentimetern väger.',
             100 * w, 'C', 3, (0, 1, 0), tol=0.05, enhet='%', vs=2, ratt_txt=['3,1', '3,10', '3,1 %'], fel=['3,5', '3,8', '0,031', '96,9'],
             kortfraga='Fettet är 3,48 % av mjölkens volym. Mejeriet anger fetthalten som andel av massan. Hur många procent av '
                       'mjölkens massa är fett?'),
    ]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Utgå från 1 cm³ mjölk. Hur mycket av den volymen kan vara fett för att massan ska bli 1,031 g?', VARIANTER, fy=True,
               familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma volymandel och massandel fett i mjölk ur uppmätt densitet'
    return q


# ================================================================ Q3: kylarvätska
def q3(uid):
    rv, rg, r0, V = 1.00, 1.11, 1.04, 6.0
    x = (r0 - rv) / (rg - rv)                     # glykolens volymandel nu
    y = (0.50 - x) * V / (1 - x)                  # liter som byts mot ren glykol
    lika(x * V - x * y + y, 0.50 * V)
    lika((V * r0 - r0 * y + rg * y) / V, 0.50 * rg + 0.50 * rv)
    assert abs(100 * x - 36.36) < 0.01 and abs(y - 1.2857) < 1e-4
    yb = (0.50 - 0.364) * V / (1 - 0.364)         # med b-kortets givna 36,4 %
    assert round(yb, 1) == round(y, 1) == 1.3

    def dunk(x0, y0, w, h, fill, namn, rho):
        b = rekt(x0, y0, w, h, '#fbfdff', INK, 2, 6)
        b += f'<rect x="{x0 + 2}" y="{y0 + h * 0.25:.1f}" width="{w - 4}" height="{h * 0.75 - 2:.1f}" rx="4" fill="{fill}"/>'
        b += tt(x0 + w / 2, y0 + h + 20, namn, 14, 'middle', INK, True) + tt(x0 + w / 2, y0 + h + 38, rho, 13)
        return b

    def fig():
        b = dunk(30, 60, 90, 100, VATTEN, 'vatten', '1,00 g/cm³')
        b += dunk(150, 60, 90, 100, '#d6ecd2', 'glykol', '1,11 g/cm³')
        b += rekt(286, 40, 120, 120, '#fbfdff', INK, 2, 8)
        b += f'<rect x="288" y="62" width="116" height="96" rx="6" fill="#d9ecdf"/>'
        b += tt(346, 104, 'kylsystem', 14, 'middle', INK, True) + tt(346, 124, '6,0 l', 14, 'middle', INK)
        b += tt(346, 180, 'kylarvätska', 14, 'middle', INK, True) + tt(346, 198, '1,04 g/cm³', 13)
        return svg(440, 208, b, 'Vatten med densiteten 1,00 g/cm³, glykol med densiteten 1,11 g/cm³ och ett kylsystem som rymmer '
                                '6,0 liter kylarvätska med densiteten 1,04 g/cm³.')

    intro = (p('Kylarvätska är en blandning av vatten och glykol. Saras bil har ett kylsystem som rymmer 6,0 liter. Hon mäter '
               'kylarvätskans densitet till 1,04 g/cm³.') + fig()
             + p('Vatten har densiteten 1,00 g/cm³ och glykol 1,11 g/cm³. Antag att vattnets och glykolens volymer tillsammans '
                 'är blandningens volym.'))
    givet = li(GIVET, al(r'V=6{,}0\ \mathrm l', r'\rho_{\text{vatten}}=1{,}00\ \mathrm{g/cm^3}',
                         r'\rho_{\text{glykol}}=1{,}11\ \mathrm{g/cm^3}', r'\rho=1{,}04\ \mathrm{g/cm^3}'))
    steg_a = [sokt(givet, 'hur stor del av kylarvätskans volym som är glykol.'),
              li('Tänk dig 1 cm³ kylarvätska', p('Låt x vara glykolens volym i cm³. Då är vattnets volym 1 − x cm³.')),
              li(r'Massa: \(m=\rho V\)', p('Kubikcentimetern väger 1,04 g, och det är glykolens massa plus vattnets massa.'),
                 mt(r'1{,}04=1{,}11x+1{,}00(1-x)')),
              li('Lös ut glykolens volym',
                 al(r'1{,}04=1{,}00+0{,}11x', rf'x=\frac{{0{{,}}04}}{{0{{,}}11}}\approx{tx(x, 3)}'),
                 mt(rf'{tx(x, 3)}\cdot100\,\%\approx{tx(100 * x, 0)}\,\%'))]
    givet_b = li(GIVET, al(r'V=6{,}0\ \mathrm l', r'\text{glykol nu: }36{,}4\,\%', r'\text{glykol sedan: }50\,\%'),
                 p('Volymandelen 36,4 % står i frågan. Låt y vara antalet liter som tappas ur och ersätts med ren glykol.'))
    steg_b = [sokt(givet_b, 'hur många liter Sara ska tappa ur.'),
              li(r'Glykolens volym nu: \(V_{\text{glykol}}=\text{andel}\cdot V\)', mt(r'0{,}364\cdot6{,}0\approx2{,}18\ \mathrm l')),
              li('Det hon tappar ur är också till 36,4 % glykol',
                 p('När y liter tappas ur försvinner 0,364y liter glykol. Sedan fyller hon på y liter ren glykol. Till slut ska '
                   'hälften av 6,0 liter, alltså 3,0 liter, vara glykol.'),
                 mt(r'2{,}18-0{,}364y+y=3{,}0')),
              li('Lös ut volymen som byts',
                 al(r'0{,}636y=3{,}0-2{,}18', rf'y=\frac{{0{{,}}82}}{{0{{,}}636}}\approx{tx(yb, 2)}\ \mathrm l')),
              li(r'Kontroll med densiteten: \(\rho=\dfrac mV\)',
                 p('Med hälften glykol och hälften vatten blir densiteten 0,50 · 1,11 + 0,50 · 1,00 = 1,055 g/cm³. '
                   'Massan i kylsystemet räknas i kg, eftersom 1 liter av en vätska med densiteten 1,04 g/cm³ väger 1,04 kg.'),
                 mt(rf'\frac{{6{{,}}0\cdot1{{,}}04-{tx(y, 2)}\cdot1{{,}}04+{tx(y, 2)}\cdot1{{,}}11}}{{6{{,}}0}}\approx1{{,}}055\ \mathrm{{g/cm^3}}'))]
    delar = [
        del_('Hur många procent av kylarvätskans volym är glykol?', steg_a, '36 %.',
             'Tänk dig 1 cm³ kylarvätska och kalla glykolens volym för x. Vad väger glykolen och vattnet tillsammans?',
             100 * x, 'A', 4, (0, 1, 1), tol=0.5, enhet='%', vs=2, ratt_txt=['36', '36,4', '36 %'], fel=['64', '3,6', '4', '94']),
        del_('Sara vill att vätskan ska innehålla 50 volymprocent glykol. Hon tappar ur en del av kylarvätskan och fyller på med ren '
             'glykol tills kylsystemet är fullt igen. Hur många liter ska hon tappa ur?', steg_b, '1,3 liter.',
             'Det Sara tappar ur är inte rent vatten, utan samma blandning som finns i kylsystemet. Hur mycket glykol finns kvar efteråt?',
             y, 'A', 5, (0, 0, 2), tol=0.05, enhet='liter', vs=2, ai=3, ratt_txt=['1,3', '1,29', '1,3 liter'],
             fel=['0,82', '3,0', '0,86', '1,1', '2,2'],
             kortfraga='Kylarvätskan innehåller 36,4 volymprocent glykol. Sara vill att den ska innehålla 50 volymprocent glykol. '
                       'Hon tappar ur en del av kylarvätskan och fyller på med ren glykol tills kylsystemet är fullt igen. '
                       'Hur många liter ska hon tappa ur?'),
    ]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Utgå från 1 cm³ kylarvätska. Hur stor del av den kan vara glykol för att massan ska bli 1,04 g?', VARIANTER, fy=True,
               familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma glykolhalt ur densitet och hur mycket som ska bytas för en ny halt'
    return q


# ================================================================ Q4: isbit med infrusen sten som svävar
def q4(uid):
    m, ri, rs, rv = 120.0, 0.917, 2.60, 1.00
    V = m / rv
    x = (m / ri - V) / (1 / ri - 1 / rs)          # stenens massa
    lika(x / rs + (m - x) / ri, V)
    assert abs(x - 15.387) < 1e-3

    def fig():
        b = rekt(60, 30, 300, 170, '#fbfdff', INK, 2, 4)
        b += f'<rect x="62" y="52" width="296" height="146" fill="{VATTEN}"/>' + linje(62, 52, 358, 52, BLA, 2)
        b += '<polygon points="160,92 252,86 262,160 168,168" fill="#eef7fc" stroke="#6c9cb8" stroke-width="2" stroke-linejoin="round"/>'
        b += '<polygon points="196,124 214,116 232,124 230,140 210,146 194,138" fill="#8f8a82" stroke="#5e5a54" stroke-width="1.5"/>'
        b += pil(300, 104, 248, 106, GRA, 2, 8) + tt(304, 108, 'is', 14, 'start', INK, True)
        b += pil(126, 150, 194, 134, GRA, 2, 8) + tt(122, 160, 'sten', 14, 'end', INK, True)
        b += tt(320, 188, 'vatten', 14, 'middle', BLA, True)
        return svg(420, 212, b, 'En isbit med en infrusen sten ligger helt under vattenytan i ett akvarium och varken sjunker '
                                'eller stiger.')

    intro = (p('Leo hittar en isbit med en sten infrusen. Isbiten och stenen väger tillsammans 120 g. När han lägger isbiten i '
               'vatten hamnar den helt under ytan, men den varken sjunker eller stiger, se figuren.') + fig()
             + p('Is har densiteten 0,917 g/cm³, stenen 2,60 g/cm³ och vattnet 1,00 g/cm³.'))
    steg = [sokt(li(GIVET, al(r'm=120\ \mathrm g', r'\rho_{\text{is}}=0{,}917\ \mathrm{g/cm^3}', r'\rho_{\text{sten}}=2{,}60\ \mathrm{g/cm^3}',
                              r'\rho_{\text{vatten}}=1{,}00\ \mathrm{g/cm^3}')), 'stenens massa.'),
            li(r'Ett föremål svävar när medeldensiteten är vätskans: \(\rho=\dfrac mV=\rho_{\text{vatten}}\)',
               p('Isbiten med stenen har alltså medeldensiteten 1,00 g/cm³. Det ger dess volym.'),
               mt(r'V=\frac{m}{\rho}=\frac{120}{1{,}00}=120\ \mathrm{cm^3}')),
            li(r'Volymerna adderas: \(V=\dfrac{m_{\text{sten}}}{\rho_{\text{sten}}}+\dfrac{m_{\text{is}}}{\rho_{\text{is}}}\)',
               p('Låt x vara stenens massa i gram. Då väger isen 120 − x gram.'),
               mt(r'\frac{x}{2{,}60}+\frac{120-x}{0{,}917}=120')),
            li('Samla termerna med stenens massa',
               al(rf'{tx(1 / rs, 4)}x+{tx(m / ri, 2)}-{tx(1 / ri, 4)}x=120', rf'{tx(1 / ri - 1 / rs, 4)}x={tx(m / ri - V, 2)}',
                  rf'x\approx{tx(x, 1)}\ \mathrm g')),
            li('Kontroll: stenens och isens volymer',
               al(rf'V_{{\text{{sten}}}}=\frac{{{tx(x, 2)}}}{{2{{,}}60}}\approx{tx(x / rs, 2)}\ \mathrm{{cm^3}}',
                  rf'V_{{\text{{is}}}}=\frac{{{tx(m - x, 2)}}}{{0{{,}}917}}\approx{tx((m - x) / ri, 2)}\ \mathrm{{cm^3}}'),
               p('Tillsammans blir det 120 cm³, precis som det ska.'))]
    delar = [del_('Hur mycket väger stenen?', steg, '15,4 g.', '', x, 'A', 5, (0, 1, 2), tol=0.05, enhet='g', vs=3,
                  ratt_txt=['15,4', '15', '15,4 g'], fel=['104,6', '10', '46', '120'])]
    q = H.bygg(uid, 2, 'densitet', FLYT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Vad måste isbitens medeldensitet vara när den varken sjunker eller stiger? Vilken volym har den då?', VARIANTER, fy=True,
               familjnyckel=FLYT[1])
    q['typ'] = 'bestämma massan av en infrusen sten när isbiten svävar i vatten'
    return q


# ================================================================ Q5: jordens kärna
def q5(uid):
    R, r, rho, rm = 6370.0, 3480.0, 5510.0, 4500.0
    k = (r / R) ** 3
    rk = (rho - rm * (1 - k)) / k
    lika(rk * k + rm * (1 - k), rho)
    assert abs(100 * k - 16.30) < 0.01 and abs(rk - 10697) < 5
    rkb = (rho - rm * (1 - 0.163)) / 0.163       # med b-kortets givna 16,3 %
    assert round(rkb, -3) == round(rk, -3) == 11000

    def fig(markera=False):
        cx, cy, Rp = 150, 140, 112
        rp = Rp * r / R
        b = f'<circle cx="{cx}" cy="{cy}" r="{Rp}" fill="#e7c9a3" stroke="{INK}" stroke-width="2"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="{rp:.1f}" fill="#d9822b" stroke="{INK}" stroke-width="2"/>'
        b += linje(cx, cy, cx + Rp, cy, INK, 1.6, '5 4') + cirkel(cx, cy, 3.5, INK, INK, 1)
        b += tt(cx + Rp + 6, cy + 5, '6 370 km', 13, 'start', INK, True, halo=True)
        b += linje(cx, cy, cx - rp, cy, INK, 1.6, '5 4')
        b += tt(cx - rp / 2 + 2, cy - 8, '3 480 km', 12, 'middle', INK, True, halo=True)
        b += pil(310, 70, cx + 20, cy - 30, GRA, 2, 8) + tt(314, 66, 'kärna', 14, 'start', INK, True)
        b += tt(314, 84, 'densitet ?', 13, 'start', INK)
        b += pil(310, 210, cx + 82, cy + 58, GRA, 2, 8) + tt(314, 206, 'mantel', 14, 'start', INK, True)
        b += tt(314, 224, '4 500 kg/m³', 13, 'start', INK)
        return svg(440, 270, b, 'Genomskärning av jorden i en enkel modell: en kärna med radien 3 480 km och en mantel ut till '
                                'radien 6 370 km. Manteln har densiteten 4 500 kg/m³. Kärnans densitet är okänd.')

    intro = (p('I en enkel modell består jorden av en kärna och en mantel runt kärnan, se figuren. Jorden har radien 6 370 km och '
               'kärnan radien 3 480 km. Jordens medeldensitet är 5 510 kg/m³ och mantelns medeldensitet är 4 500 kg/m³.') + fig())
    steg_a = [sokt(li(GIVET, al(r'R=6\,370\ \mathrm{km}', r'r=3\,480\ \mathrm{km}')), 'hur stor del av jordens volym som är kärna.'),
              li(r'Klotets volym: \(V=\dfrac{4\pi r^3}{3}\)',
                 p('Kärnans andel är kärnans volym delad med hela jordens volym. Faktorn 4π/3 förkortas bort.'),
                 mt(r'\frac{V_{\text{kärna}}}{V_{\text{jord}}}=\frac{\frac{4\pi r^3}{3}}{\frac{4\pi R^3}{3}}=\left(\frac rR\right)^3')),
              li('Sätt in radierna', mt(rf'\left(\frac{{3\,480}}{{6\,370}}\right)^3\approx{tx(k, 4)}'),
                 p('Enheterna tar ut varandra, så radierna kan sättas in i km.')),
              li(r'Volymprocent: \(\dfrac{V_{\text{kärna}}}{V_{\text{jord}}}\cdot100\,\%\)', mt(rf'{tx(k, 4)}\cdot100\,\%\approx{tx(100 * k, 1)}\,\%'),
                 p('Kärnan sträcker sig mer än halvvägs ut, men den är ändå bara ungefär en sjättedel av volymen.'))]
    givet_b = li(GIVET, al(r'\rho_{\text{jord}}=5\,510\ \mathrm{kg/m^3}', r'\rho_{\text{mantel}}=4\,500\ \mathrm{kg/m^3}'),
                 p('Kärnan är 16,3 % av jordens volym, så manteln är 83,7 %.'))
    steg_b = [sokt(givet_b, 'kärnans medeldensitet.'),
              li('Tänk dig 1 m³ av jorden', p('Den består av 0,163 m³ kärna och 0,837 m³ mantel, och den väger 5 510 kg.')),
              li(r'Massa: \(m=\rho V\)', p('Jordens massa är kärnans massa plus mantelns massa.'),
                 mt(r'5\,510=\rho_{\text{kärna}}\cdot0{,}163+4\,500\cdot0{,}837')),
              li('Lös ut kärnans densitet',
                 al(rf'0{{,}}163\,\rho_{{\text{{kärna}}}}=5\,510-{tx(4500 * 0.837, 1)}',
                    rf'\rho_{{\text{{kärna}}}}=\frac{{{tx(5510 - 4500 * 0.837, 1)}}}{{0{{,}}163}}\approx{rkb:,.0f}\ \mathrm{{kg/m^3}}'.replace(',', r'\,'))),
              li('Är svaret rimligt?',
                 p('Kärnan får mer än dubbelt så stor densitet som manteln och ungefär fyra gånger så stor som vanligt berg '
                   '(cirka 2 700 kg/m³). Det stämmer med att kärnan till största delen är järn och nickel, som pressas ihop av '
                   'det höga trycket djupt inne i jorden.'))]
    delar = [
        del_('Hur många procent av jordens volym är kärna?', steg_a, '16,3 %.',
             'Hur beror ett klots volym på radien? Jämför kärnans volym med hela jordens.',
             100 * k, 'C', 3, (0, 1, 0), tol=0.05, enhet='%', vs=3, ratt_txt=['16,3', '16', '16,3 %'], fel=['54,6', '29,8', '83,7', '0,163']),
        del_('Vilken medeldensitet har kärnan enligt modellen?', steg_b, '1,1·10⁴ kg/m³, alltså cirka 11 000 kg/m³.',
             'Tänk dig 1 m³ av jorden. Hur mycket av den kubikmetern är mantel, och vad väger den delen?',
             rk, 'A', 5, (0, 0, 2), tol=500, enhet='kg/m³', vs=2, ai=3, ratt_txt=['11000', '10700', '1,1·10^4'],
             fel=['5510', '1010', '6200', '33800'],
             kortfraga='Kärnan är 16,3 % av jordens volym. Vilken medeldensitet har kärnan enligt modellen?'),
    ]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Jordens massa är kärnans massa plus mantelns massa. Hur stor del av jordens volym är kärna?', VARIANTER, fy=True,
               familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma kärnans densitet ur jordens medeldensitet i en tvåskiktsmodell'
    return q


# ================================================================ Q6: fiskeflöte med blyvikt
def q6(uid):
    V, rb, rp, rv, f = 12.0, 0.16, 11.3, 1.00, 0.80
    rho = f * rv
    m = rho * V
    vp = (m - rb * V) / (rp - rb)
    mp = rp * vp
    lika(rp * vp + rb * (V - vp), m)
    assert abs(mp - 7.790) < 1e-3

    def fig():
        b = f'<rect x="20" y="96" width="380" height="120" fill="{VATTEN}"/>' + linje(20, 96, 400, 96, BLA, 2)
        bot, h = 196, 125                             # 80 % av höjden (100 px) under ytan vid y = 96
        top = bot - h
        assert abs((bot - 96) / h - f) < 1e-9
        b += f'<rect x="196" y="{top:.1f}" width="28" height="{h - 10:.1f}" rx="12" fill="#f2dcb3" stroke="{INK}" stroke-width="2"/>'
        b += f'<rect x="202" y="{bot - 18:.1f}" width="16" height="18" rx="3" fill="#7d8a95" stroke="{INK}" stroke-width="1.5"/>'
        b += linje(210, top - 22, 210, top, INK, 1.4)
        b += linje(250, 96, 250, bot, ORA, 1.6) + linje(244, 96, 256, 96, ORA, 1.6) + linje(244, bot, 256, bot, ORA, 1.6)
        b += tt(262, 150, '80 % av volymen', 13, 'start', ORA, True) + tt(262, 166, 'under ytan', 13, 'start', ORA, True)
        b += pil(150, 60, 194, 70, GRA, 2, 8) + tt(146, 58, 'balsaträ', 14, 'end', INK, True)
        b += pil(150, 190, 200, 188, GRA, 2, 8) + tt(146, 194, 'bly', 14, 'end', INK, True)
        return svg(420, 226, b, 'Ett fiskeflöte av balsaträ med en liten blyvikt längst ner flyter upprätt i vatten. 80 procent av '
                                'flötets volym är under vattenytan.')

    intro = (p('Ett fiskeflöte är gjort av balsaträ med en liten blyvikt längst ner. Hela flötet har volymen 12,0 cm³. Flötet ska '
               'flyta upprätt med 80 % av sin volym under vattenytan, se figuren.') + fig()
             + p('Balsaträ har densiteten 0,16 g/cm³, bly 11,3 g/cm³ och vatten 1,00 g/cm³.'))
    steg = [sokt(li(GIVET, al(r'V=12{,}0\ \mathrm{cm^3}', r'\rho_{\text{balsa}}=0{,}16\ \mathrm{g/cm^3}', r'\rho_{\text{bly}}=11{,}3\ \mathrm{g/cm^3}',
                              r'\rho_{\text{vatten}}=1{,}00\ \mathrm{g/cm^3}')), 'blyviktens massa.'),
            li(r'Nedsänkt andel: \(\dfrac{V_{\text{under}}}{V}=\dfrac{\rho}{\rho_{\text{vatten}}}\)',
               p('När flötet flyter stilla är lyftkraften lika stor som tyngden. Då är den nedsänkta andelen lika med kvoten mellan '
                 'flötets medeldensitet och vattnets densitet.'),
               mt(r'\rho=0{,}80\cdot1{,}00=0{,}80\ \mathrm{g/cm^3}')),
            li(r'Flötets massa: \(m=\rho V\)', mt(r'm=0{,}80\cdot12{,}0=9{,}6\ \mathrm g')),
            li(r'Massorna adderas: \(m=m_{\text{bly}}+m_{\text{balsa}}\)',
               p('Låt \\(V_{\\text{bly}}\\) vara blyets volym i cm³. Då är balsaträets volym \\(12{,}0-V_{\\text{bly}}\\) cm³.'),
               mt(r'11{,}3V_{\text{bly}}+0{,}16(12{,}0-V_{\text{bly}})=9{,}6')),
            li('Lös ut blyets volym', al(r'11{,}14V_{\text{bly}}+1{,}92=9{,}6',
                                         rf'V_{{\text{{bly}}}}=\frac{{7{{,}}68}}{{11{{,}}14}}\approx{tx(vp, 3)}\ \mathrm{{cm^3}}')),
            li(r'Blyviktens massa: \(m=\rho V\)', mt(rf'm_{{\text{{bly}}}}=11{{,}}3\cdot{tx(vp, 3)}\approx{tx(mp, 1)}\ \mathrm g'),
               p(f'Balsaträet väger då 9,6 − {tx(mp, 1).replace("{,}", ",")} ≈ {tx(m - mp, 1).replace("{,}", ",")} g. Blyvikten är '
                 'alltså tyngre än allt trä i flötet, fast den bara är en liten del av volymen.'))]
    delar = [del_('Hur stor massa ska blyvikten ha?', steg, '7,8 g.', '', mp, 'A', 5, (0, 1, 2), tol=0.05, enhet='g', vs=2,
                  ratt_txt=['7,8', '7,79', '7,8 g'], fel=['0,69', '9,6', '5,3', '1,9'])]
    q = H.bygg(uid, 2, 'densitet', FLYT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Vilken medeldensitet måste flötet ha för att 80 % av volymen ska vara under vattenytan? Vad väger då hela flötet?',
               VARIANTER, fy=True, familjnyckel=FLYT[1])
    q['typ'] = 'bestämma blyviktens massa så att ett flöte flyter med en given andel under ytan'
    return q


def tal(v):
    return f'{v:.1f}'.replace('.', ',')


UPPGIFTER = [q1, q2, q3, q4, q5, q6]


def flytta_till_a(src):
    """Ändrar niva, poang och traningsniva i de befintliga objekten genom att byta bara de raderna."""
    for uid, (poang, tn) in TILL_A.items():
        start = src.index(f'"id": "{uid}",')
        slut = src.index('\n  }', start)
        obj = src[start:slut]
        ny = obj
        ny, n1 = re.subn(r'"niva": "C"', '"niva": "A"', ny, count=1)
        ny, n2 = re.subn(r'"poang": "\([0-9/]+\)"', f'"poang": "{poang}"', ny, count=1)
        ny, n3 = re.subn(r'"traningsniva": \d', f'"traningsniva": {tn}', ny, count=1)
        assert (n1, n2, n3) == (1, 1, 1), uid
        src = src[:start] + ny + src[slut:]
    return src


def main():
    src, bank = H.las(BANK)
    for uid in TILL_A:
        q = next(t for t in bank if t['id'] == uid)
        assert q['omr'] == 'densitet' and q['niva'] in ('C', 'A') and not q.get('spelDelar'), uid
    nasta = H.nasta_id(bank, 2)
    nya = [f(f'2.{nasta + i}') for i, f in enumerate(UPPGIFTER)]
    assert not {q['id'] for q in bank} & {q['id'] for q in nya}
    print('uppgifter', len(nya), 'kort', sum(len(q.get('spelDelar') or [1]) for q in nya), [q['id'] for q in nya])
    if '--ut' in sys.argv:
        Path(sys.argv[sys.argv.index('--ut') + 1]).write_text(json.dumps(nya, ensure_ascii=False), encoding='utf-8')
    if '--skriv' in sys.argv:
        src = flytta_till_a(src)
        H.lagg_till(BANK, src, nya)


if __name__ == '__main__':
    main()
