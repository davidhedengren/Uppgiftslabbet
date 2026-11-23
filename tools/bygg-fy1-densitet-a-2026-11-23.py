"""Fysik 1 (uppgifter.js), densitet: fler blandningsuppgifter på A-nivå, 23 november 2026.

Användaren: "Lägg sedan in fler uppgifter inom densitet på A-nivå, t.ex. lite blandningar osv".
Sex nya uppgifter med egna sammanhang, skrivna i lärarens stil (jämför lärarens bronsuppgift: "Du har … g tenn och vill
tillverka brons med densiteten … Hur många gram koppar behöver du tillsätta?"). Facit enligt agent/FACITMALL.md.
Alla tal räknas i skriptet och kontrolleras med assert. Se agent/FY1_DENSITET_A_2026-11-23.md.

  python tools/bygg-fy1-densitet-a-2026-11-23.py [--skriv] [--ut fil.json]
"""
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import (mt, al, p, li, del_, svg, tt, linje, pil, rekt, tx, sv,  # noqa: E402
                               BLA, ORA, GRA, INK)

BANK = 'uppgifter.js'
VARIANTER = {}
GIVET = 'Givet och sökt'
VATTEN = '#cfe6f5'
SAMMANSATT = ('Sammansatta och ihåliga föremål', 'densitet__sammansatt_densitet_och_ihaliga_foremal')
FLYT = ('Densitet, flytförmåga och modeller', 'densitet__densitet_och_flytformaga')


def sokt(steg, text):
    assert steg.endswith('</li>')
    return steg[:-5] + p('Sökt: ' + text) + '</li>'


def lika(a, b, tol=1e-9):
    assert abs(a - b) <= tol, (a, b)


def ellips(cx, cy, rx, ry, fill, stroke=INK, sw=2):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


# ================================================================ Q1: guld och silver till ett smycke
def q1(uid):
    mg, rg, rs, rho = 12.0, 19.3, 10.5, 15.0
    # (mg + x) / (mg/rg + x/rs) = rho  =>  x (1 - rho/rs) = rho*mg/rg - mg
    x = (rho * mg / rg - mg) / (1 - rho / rs)
    lika((mg + x) / (mg / rg + x / rs), rho)
    karat = 24 * mg / (mg + x)
    assert abs(x - 6.238) < 1e-3 and abs(karat - 15.79) < 0.01
    assert round(24 * 12.0 / (12.0 + 6.2)) == 16          # b-kortets givna 6,2 g ger samma svar

    intro = p('Du har 12,0 g guld och vill tillverka en legering av guld och silver med densiteten 15,0 g/cm³. '
              'Guld har densiteten 19,3 g/cm³ och silver 10,5 g/cm³.')
    vg = mg / rg
    steg_a = [sokt(li(GIVET, al(r'm_{\text{guld}}=12{,}0\ \mathrm g', r'\rho_{\text{guld}}=19{,}3\ \mathrm{g/cm^3}',
                                r'\rho_{\text{silver}}=10{,}5\ \mathrm{g/cm^3}', r'\rho=15{,}0\ \mathrm{g/cm^3}')),
                   'silvrets massa.'),
              li(r'Guldets volym: \(V=\dfrac{m}{\rho}\)', mt(rf'V_{{\text{{guld}}}}=\frac{{12{{,}}0}}{{19{{,}}3}}\approx{tx(vg, 4)}\ \mathrm{{cm^3}}')),
              li(r'Legeringens densitet: \(\rho=\dfrac{m_{\text{tot}}}{V_{\text{tot}}}\)',
                 p('Låt x vara silvrets massa i gram. Silvret har då volymen x/10,5 cm³. Både massorna och volymerna läggs ihop.'),
                 mt(rf'15{{,}}0=\frac{{12{{,}}0+x}}{{{tx(vg, 4)}+\dfrac{{x}}{{10{{,}}5}}}}')),
              li('Multiplicera med nämnaren och samla x',
                 al(rf'15{{,}}0\cdot{tx(vg, 4)}+\frac{{15{{,}}0}}{{10{{,}}5}}x=12{{,}}0+x',
                    rf'{tx(rho * vg, 3)}+{tx(rho / rs, 4)}x=12{{,}}0+x',
                    rf'{tx(rho / rs - 1, 4)}x={tx(mg - rho * vg, 3)}',
                    rf'x\approx{tx(x, 2)}\ \mathrm g')),
              li(r'Kontroll: \(\rho=\dfrac{m_{\text{tot}}}{V_{\text{tot}}}\)',
                 mt(rf'\frac{{12{{,}}0+{tx(x, 2)}}}{{{tx(vg, 4)}+{tx(x / rs, 4)}}}\approx{tx((mg + x) / (vg + x / rs), 1)}\ \mathrm{{g/cm^3}}'))]
    steg_b = [sokt(li(GIVET, al(r'm_{\text{guld}}=12{,}0\ \mathrm g', r'm_{\text{silver}}=6{,}2\ \mathrm g')),
                   'guldhalten i karat.'),
              li(r'Legeringens massa: \(m_{\text{tot}}=m_{\text{guld}}+m_{\text{silver}}\)',
                 mt(r'm_{\text{tot}}=12{,}0+6{,}2=18{,}2\ \mathrm g')),
              li(r'Karat: \(24\cdot\dfrac{m_{\text{guld}}}{m_{\text{tot}}}\)',
                 mt(rf'24\cdot\frac{{12{{,}}0}}{{18{{,}}2}}\approx{tx(24 * 12 / 18.2, 1)}'),
                 p('Rent guld är 24 karat. Här är ungefär två tredjedelar av massan guld, så svaret är rimligt.'))]
    delar = [del_('Hur många gram silver ska du blanda i?', steg_a, '6,2 g.',
                  'Hur stor volym har guldet? Kalla silvrets massa för x och skriv både totala massan och totala volymen med x.',
                  x, 'A', 5, (0, 1, 2), tol=0.05, enhet='g', vs=2, ratt_txt=['6,2', '6,24', '6,2 g'], fel=['3,4', '12', '8,6']),
             del_('Guldhalten i karat är 24 gånger guldets andel av legeringens massa. Hur många karat blir legeringen?',
                  steg_b, '16 karat.', 'Hur stor del av legeringens massa är guld?', karat, 'C', 3, (0, 1, 0), tol=0.5, vs=2,
                  kortfraga='Du blandar 12,0 g guld med 6,2 g silver. Guldhalten i karat är 24 gånger guldets andel av '
                            'legeringens massa. Hur många karat blir legeringen?',
                  ratt_txt=['16', '15,8'], fel=['24', '8', '12'])]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Tänk på att både massorna och volymerna läggs ihop när metallerna smälts samman.', VARIANTER, fy=True,
               familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma hur mycket silver som ska blandas med guld för en given densitet'
    return q


# ================================================================ Q2: Arkimedes och kungens krona
def q2(uid):
    m, V, rg, rs = 1000.0, 60.0, 19.3, 10.5
    vguld = m / rg
    x = (V - m / rg) / (1 / rs - 1 / rg)            # silvrets massa i gram
    lika(x / rs + (m - x) / rg, V)
    assert abs(vguld - 51.81) < 0.01 and abs(x - 188.5) < 0.1

    def fig():
        b = rekt(60, 50, 170, 150, '#fbfdff', INK, 2, 4)
        b += f'<rect x="62" y="56" width="166" height="142" fill="{VATTEN}"/>'
        b += linje(62, 56, 228, 56, BLA, 2)
        b += f'<path d="M228 52 L262 58 L262 64 L230 60 Z" fill="#9cc9e6" stroke="{INK}" stroke-width="1.5"/>'
        b += f'<path d="M262 64 Q272 90 276 120" fill="none" stroke="{BLA}" stroke-width="4"/>'
        b += rekt(256, 126, 52, 74, '#fbfdff', INK, 2, 3)
        b += f'<rect x="258" y="172" width="48" height="26" fill="{VATTEN}"/>'
        b += tt(282, 220, '60,0 cm³', 14, 'middle', BLA, True)
        kr = [(110, 170), (110, 135), (122, 150), (135, 128), (148, 150), (161, 128), (174, 150), (186, 135), (186, 170)]
        b += f'<polygon points="{" ".join(f"{a},{c}" for a, c in kr)}" fill="#e8c14a" stroke="#8a6d12" stroke-width="2"/>'
        b += tt(148, 190, 'kronan', 14, 'middle', INK, True)
        b += tt(145, 34, 'kärlet var fyllt till brädden', 13, 'middle', GRA)
        return svg(340, 232, b, 'Kronan ligger i ett kärl som var fyllt till brädden med vatten. Vattnet som rinner över '
                                'samlas i ett mätglas och är 60,0 kubikcentimeter.')

    intro = (p('Kung Hieron hade beställt en krona av rent guld men misstänkte att guldsmeden blandat i silver. Kronan väger '
               '1,00 kg. När den sänks ned i ett kärl som är fyllt till brädden med vatten rinner 60,0 cm³ vatten över, se figuren.')
             + fig() + p('Guld har densiteten 19,3 g/cm³ och silver 10,5 g/cm³.'))
    steg_a = [sokt(li(GIVET, al(r'm=1{,}00\ \mathrm{kg}=1000\ \mathrm g', r'\rho_{\text{guld}}=19{,}3\ \mathrm{g/cm^3}')),
                   'volymen om kronan vore av rent guld.'),
              li(r'Volym: \(V=\dfrac{m}{\rho}\)', mt(rf'V=\frac{{1000}}{{19{{,}}3}}\approx{tx(vguld, 1)}\ \mathrm{{cm^3}}'),
                 p('Kronan tränger undan 60,0 cm³ vatten och har alltså större volym än så. Den kan inte vara av rent guld.'))]
    steg_b = [sokt(li(GIVET, al(r'm=1000\ \mathrm g', r'V=60{,}0\ \mathrm{cm^3}', r'\rho_{\text{guld}}=19{,}3\ \mathrm{g/cm^3}',
                                r'\rho_{\text{silver}}=10{,}5\ \mathrm{g/cm^3}')), 'silvrets massa.'),
              li(r'Massorna läggs ihop: \(m_{\text{silver}}+m_{\text{guld}}=m\)',
                 p('Låt x vara silvrets massa i gram. Då väger guldet 1000 − x gram.')),
              li(r'Volymerna läggs ihop: \(V=\dfrac{m_{\text{silver}}}{\rho_{\text{silver}}}+\dfrac{m_{\text{guld}}}{\rho_{\text{guld}}}\)',
                 p('Kronans volym är lika med det vatten som rann över.'),
                 mt(r'\frac{x}{10{,}5}+\frac{1000-x}{19{,}3}=60{,}0')),
              li('Samla termerna med silvrets massa',
                 al(rf'{tx(1 / rs, 5)}x+{tx(m / rg, 2)}-{tx(1 / rg, 5)}x=60{{,}}0',
                    rf'{tx(1 / rs - 1 / rg, 5)}x={tx(V - m / rg, 2)}',
                    rf'x\approx{tx(x, 0)}\ \mathrm g')),
              li(r'Kontroll: \(V=\dfrac{m}{\rho}\) för varje metall',
                 mt(rf'\frac{{{tx(x, 1)}}}{{10{{,}}5}}+\frac{{{tx(m - x, 1)}}}{{19{{,}}3}}\approx{tx(x / rs, 1)}+{tx((m - x) / rg, 1)}=60{{,}}0'))]
    delar = [del_('Hur stor volym skulle kronan ha om den var av rent guld?', steg_a, f'{sv(vguld, 1)} cm³.',
                  'Använd guldets densitet och kronans massa.', vguld, 'E', 2, (1, 0, 0), tol=0.05, enhet='cm³', vs=3,
                  ratt_txt=['51,8', '52'], fel=['60', '19,3', '95']),
             del_('Hur många gram silver innehåller kronan?', steg_b, f'{sv(round(x), 0)} g.',
                  'Kalla silvrets massa för x. Vilken volym får silvret och vilken volym får guldet?', x, 'A', 5, (0, 1, 2),
                  tol=1.0, enhet='g', vs=3, ratt_txt=['189', '190', '188'], fel=['8,2', '811', '500'])]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Kronans volym är lika med vattnet som rann över. Både massorna och volymerna av guldet och silvret läggs ihop.',
               VARIANTER, fy=True, familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma silverhalten i en krona ur massa och undanträngd vattenvolym'
    return q


# ================================================================ Q3: ägget i saltvattnet
def q3(uid):
    v0, r0, ragg = 400.0, 1.20, 1.08
    x = round((r0 * v0 - ragg * v0) / (ragg - 1.00), 9)   # ml vatten som får hällas i
    lika((r0 * v0 + 1.00 * x) / (v0 + x), ragg)
    assert abs(x - 600) < 1e-9

    def fig():
        b = f'<path d="M90 40 L104 210 L216 210 L230 40" fill="#fbfdff" stroke="{INK}" stroke-width="2"/>'
        b += f'<path d="M95 70 L104 208 L216 208 L225 70 Z" fill="{VATTEN}"/>'
        b += linje(95, 70, 225, 70, BLA, 2)
        b += ellips(160, 94, 22, 30, '#f6ecd8')
        b += pil(272, 96, 186, 92, GRA, 2, 8) + tt(276, 92, 'ägg', 14, 'start', INK, True)
        b += tt(276, 110, '1,08 g/cm³', 13, 'start', INK)
        b += pil(272, 166, 214, 166, GRA, 2, 8) + tt(276, 162, 'saltvatten', 14, 'start', BLA, True)
        b += tt(276, 180, '1,20 g/cm³', 13, 'start', INK)
        return svg(400, 226, b, 'Ett ägg flyter i en kanna med saltvatten. Ägget har densiteten 1,08 g/cm³ och saltvattnet 1,20 g/cm³.')

    intro = (p('Lisa har 400 ml saltvatten med densiteten 1,20 g/cm³ i en kanna. Ett ägg med densiteten 1,08 g/cm³ flyter i '
               'saltvattnet, se figuren. Lisa häller sedan i vanligt vatten, som har densiteten 1,00 g/cm³.') + fig()
             + p('Anta att vätskornas volymer kan adderas.'))
    steg = [sokt(li(GIVET, al(r'V_{\text{salt}}=400\ \mathrm{ml}', r'\rho_{\text{salt}}=1{,}20\ \mathrm{g/cm^3}',
                              r'\rho_{\text{vatten}}=1{,}00\ \mathrm{g/cm^3}', r'\rho_{\text{ägg}}=1{,}08\ \mathrm{g/cm^3}')),
                 'den största volymen vatten Lisa kan hälla i.'),
            li('Ägget flyter så länge vätskan har större densitet än ägget',
               p('När vatten hälls i sjunker vätskans densitet. Gränsen nås när vätskan har samma densitet som ägget, 1,08 g/cm³.')),
            li(r'Saltvattnets massa: \(m=\rho V\)', mt(r'm_{\text{salt}}=1{,}20\cdot400=480\ \mathrm g')),
            li(r'Blandningens densitet: \(\rho=\dfrac{m_{\text{tot}}}{V_{\text{tot}}}\)',
               p('Låt x vara volymen vatten i ml. Vattnet väger x gram.'),
               mt(r'1{,}08=\frac{480+x}{400+x}')),
            li('Lös ut x', al(r'1{,}08(400+x)=480+x', r'432+1{,}08x=480+x', r'0{,}08x=48', r'x=600\ \mathrm{ml}')),
            li('Kontroll', mt(r'\frac{480+600}{400+600}=\frac{1080}{1000}=1{,}08\ \mathrm{g/cm^3}'),
               p('Med mer än 600 ml vatten blir vätskan tunnare än ägget, och ägget sjunker.'))]
    delar = [del_('Hur mycket vatten kan hon högst hälla i för att ägget fortfarande ska flyta?', steg, '600 ml.', '', x, 'A', 5,
                  (0, 1, 2), tol=5, enhet='ml', vs=2, ratt_txt=['600', '0,6 l', '600 ml'], fel=['120', '133', '1000'])]
    q = H.bygg(uid, 2, 'densitet', FLYT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Vilken densitet har vätskan precis när ägget slutar flyta? Kalla vattnets volym för x.', VARIANTER, fy=True,
               familjnyckel=FLYT[1])
    q['typ'] = 'bestämma hur mycket vatten som kan blandas i saltvatten innan ett ägg sjunker'
    return q


# ================================================================ Q4: lättbetong som suger upp vatten
def q4(uid):
    V = 60 * 25 * 20                                  # cm³
    m, rf = 15000.0, 2.40
    vfast = m / rf
    luft = (V - vfast) / V
    vatten = 0.30 * (V - vfast)
    rho = (m + vatten) / V
    assert V == 30000 and abs(100 * luft - 79.17) < 0.01 and abs(rho - 0.7375) < 1e-9
    rho_b = (m + 0.30 * 0.79 * V) / V                 # b-kortets givna 79 % ger samma svar
    assert round(rho_b, 2) == 0.74

    intro = p('Ett block av lättbetong är 60 cm långt, 25 cm brett och 20 cm högt och väger 15,0 kg. Lättbetong är full av små '
              'luftfyllda porer. Det fasta materialet mellan porerna har densiteten 2,40 g/cm³.')
    steg_a = [sokt(li(GIVET, al(r'V=60\cdot25\cdot20\ \mathrm{cm^3}', r'm=15{,}0\ \mathrm{kg}=15\,000\ \mathrm g',
                                r'\rho_{\text{fast}}=2{,}40\ \mathrm{g/cm^3}')), 'hur stor del av blockets volym som är luft.'),
              li(r'Blockets volym: \(V=lbh\)', mt(r'V=60\cdot25\cdot20=30\,000\ \mathrm{cm^3}')),
              li(r'Det fasta materialets volym: \(V=\dfrac{m}{\rho}\)',
                 p('Luften i porerna väger nästan ingenting, så hela massan är fast material.'),
                 mt(r'V_{\text{fast}}=\frac{15\,000}{2{,}40}=6\,250\ \mathrm{cm^3}')),
              li(r'Luftens andel: \(\dfrac{V-V_{\text{fast}}}{V}\cdot100\,\%\)',
                 mt(rf'\frac{{30\,000-6\,250}}{{30\,000}}\cdot100\,\%\approx{tx(100 * luft, 1)}\,\%'))]
    steg_b = [sokt(li(GIVET, al(r'V=30\,000\ \mathrm{cm^3}', r'm=15\,000\ \mathrm g', r'\text{luft: }79\,\%\text{ av volymen}')),
                   'blockets densitet när 30 % av porerna har fyllts med vatten.'),
              li('Porernas volym', mt(r'V_{\text{porer}}=0{,}79\cdot30\,000=23\,700\ \mathrm{cm^3}')),
              li(r'Vattnets massa: \(m=\rho V\)',
                 p('30 % av porvolymen fylls med vatten, som har densiteten 1,00 g/cm³.'),
                 mt(r'm_{\text{vatten}}=1{,}00\cdot0{,}30\cdot23\,700=7\,110\ \mathrm g')),
              li(r'Blockets nya densitet: \(\rho=\dfrac{m}{V}\)',
                 p('Blockets yttre volym är densamma. Bara massan har ökat.'),
                 mt(rf'\rho=\frac{{15\,000+7\,110}}{{30\,000}}\approx{tx(rho_b, 2)}\ \mathrm{{g/cm^3}}'),
                 p('Det torra blocket hade densiteten 0,50 g/cm³. Det våta blocket är fortfarande lättare än vatten.'))]
    delar = [del_('Hur många procent av blockets volym är luft?', steg_a, f'{sv(100 * luft, 0)} %.',
                  'Hur stor volym har det fasta materialet? Jämför med hela blockets volym.', 100 * luft, 'C', 3, (0, 2, 0),
                  tol=0.5, enhet='%', vs=2, ratt_txt=['79', '79,2'], fel=['21', '50', '6,3']),
             del_('Blocket blir liggande ute i regnet. Vatten tränger in och fyller 30 % av porerna. Vilken densitet får blocket då? Vatten har densiteten 1,00 g/cm³.',
                  steg_b, '0,74 g/cm³.', 'Hur stor volym har porerna? Hur mycket väger vattnet som fyller 30 % av dem?',
                  rho, 'A', 5, (0, 0, 2), tol=0.005, enhet='g/cm³', vs=2,
                  kortfraga='Luften är 79 % av blockets volym. Blocket blir liggande ute i regnet. Vatten tränger in och fyller '
                            '30 % av porerna. Vilken densitet får blocket då? Vatten har densiteten 1,00 g/cm³.',
                  ratt_txt=['0,74', '0,7375'], fel=['0,50', '0,80', '1,30'])]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Luften i porerna väger nästan ingenting. Hela blockets massa är alltså det fasta materialet.', VARIANTER, fy=True,
               familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma luftandelen i lättbetong och densiteten när porerna delvis fylls med vatten'
    return q


# ================================================================ Q5: isbit mellan fotogen och vatten
def q5(uid):
    ri, rf, rv = 0.917, 0.800, 1.00
    f = (ri - rf) / (rv - rf)
    lika(rv * f + rf * (1 - f), ri)
    assert abs(100 * f - 58.5) < 1e-9

    def fig():
        b = rekt(70, 30, 180, 190, '#fbfdff', INK, 2, 4)
        b += '<rect x="72" y="60" width="176" height="70" fill="#f7efc6"/>'
        b += f'<rect x="72" y="130" width="176" height="88" fill="{VATTEN}"/>'
        b += linje(72, 60, 248, 60, ORA, 2) + linje(72, 130, 248, 130, BLA, 2, '6 4')
        b += rekt(130, 130 - 0.415 * 54, 56, 54, '#eef8ff', '#6f8fa6', 2, 4)
        b += pil(298, 90, 252, 90, GRA, 2, 8) + tt(302, 86, 'fotogen', 14, 'start', ORA, True)
        b += tt(302, 104, '0,800 g/cm³', 13, 'start', INK)
        b += pil(298, 128, 190, 124, GRA, 2, 8) + tt(302, 132, 'is', 14, 'start', INK, True)
        b += tt(302, 150, '0,917 g/cm³', 13, 'start', INK)
        b += pil(298, 190, 252, 190, GRA, 2, 8) + tt(302, 186, 'vatten', 14, 'start', BLA, True)
        b += tt(302, 204, '1,00 g/cm³', 13, 'start', INK)
        return svg(420, 236, b, 'Ett glas med ett lager fotogen ovanpå vatten. En isbit flyter i gränsen mellan vätskorna, delvis '
                                'i fotogenen och delvis i vattnet, och är helt täckt av fotogen.')

    intro = (p('I ett glas ligger ett lager fotogen ovanpå vatten. Fotogen och vatten blandas inte. En isbit läggs i glaset. Den '
               'sjunker genom fotogenen och flyter i gränsen mellan vätskorna, helt täckt av fotogen, se figuren.') + fig()
             + p('Is har densiteten 0,917 g/cm³, fotogen 0,800 g/cm³ och vatten 1,00 g/cm³.'))
    steg = [sokt(li(GIVET, al(r'\rho_{\text{is}}=0{,}917\ \mathrm{g/cm^3}', r'\rho_{\text{fotogen}}=0{,}800\ \mathrm{g/cm^3}',
                              r'\rho_{\text{vatten}}=1{,}00\ \mathrm{g/cm^3}')), 'hur stor del av isbitens volym som är i vattnet.'),
            li(r'Flytvillkor: \(m_{\text{is}}=m_{\text{undanträngd vätska}}\)',
               p('En kropp som flyter tränger undan lika stor massa vätska som den själv väger. Isbiten tränger undan både vatten och fotogen. Låt isbiten ha volymen V och låt x vara den andel av volymen som '
                 'är i vattnet. Resten, 1 − x, är i fotogenen.')),
            li(r'Massa: \(m=\rho V\)',
               mt(r'0{,}917V=1{,}00\cdot xV+0{,}800\cdot(1-x)V'),
               p('Isbitens volym V finns i varje term och kan förkortas bort.')),
            li('Lös ut x', al(r'0{,}917=x+0{,}800-0{,}800x', r'0{,}200x=0{,}117', rf'x={tx(f, 3)}')),
            li('Rimlighet', p('Isens densitet ligger mellan fotogenens och vattnets, så isbiten måste vara delvis i båda. Den ligger '
                              'lite närmare vattnets densitet, så lite mer än hälften av isbiten är i vattnet.'))]
    delar = [del_('Hur många procent av isbitens volym är i vattnet?', steg, '59 %.', '', 100 * f, 'A', 5, (0, 1, 2), tol=0.6,
                  enhet='%', vs=2, ratt_txt=['59', '58,5', '58 %'], fel=['41', '92', '50'])]
    q = H.bygg(uid, 2, 'densitet', FLYT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Isbiten väger lika mycket som vätskan den tränger undan. Kalla andelen av isbiten som är i vattnet för x.',
               VARIANTER, fy=True, familjnyckel=FLYT[1])
    q['typ'] = 'bestämma hur stor del av en isbit som är i vattnet när den flyter mellan fotogen och vatten'
    return q


# ================================================================ Q6: saft av koncentrat
def q6(uid):
    rk, rv, rs = 1.30, 1.00, 1.06
    k = round((rk - rs) / (rs - rv), 9)               # delar vatten per del koncentrat
    lika((rk + rv * k) / (1 + k), rs)
    assert abs(k - 4) < 1e-9

    intro = p('Saftkoncentrat har densiteten 1,30 g/cm³. Elias blandar koncentrat med vatten och mäter den färdiga saftens '
              'densitet till 1,06 g/cm³. Vatten har densiteten 1,00 g/cm³. Anta att vätskornas volymer kan adderas.')
    steg = [sokt(li(GIVET, al(r'\rho_{\text{konc}}=1{,}30\ \mathrm{g/cm^3}', r'\rho_{\text{vatten}}=1{,}00\ \mathrm{g/cm^3}',
                              r'\rho_{\text{saft}}=1{,}06\ \mathrm{g/cm^3}')), 'antal delar vatten per del koncentrat.'),
            li('Tänk dig 1 dl koncentrat och x dl vatten',
               p('Saften får då volymen 1 + x dl. Räkna i cm³: 1 dl = 100 cm³.')),
            li(r'Massa: \(m=\rho V\)',
               mt(r'm_{\text{saft}}=1{,}30\cdot100+1{,}00\cdot100x=130+100x')),
            li(r'Saftens densitet: \(\rho=\dfrac{m_{\text{tot}}}{V_{\text{tot}}}\)',
               mt(r'1{,}06=\frac{130+100x}{100+100x}')),
            li('Lös ut x', al(r'106+106x=130+100x', r'6x=24', r'x=4')),
            li('Kontroll', mt(r'\frac{130+400}{100+400}=\frac{530}{500}=1{,}06\ \mathrm{g/cm^3}'))]
    delar = [del_('Hur många delar vatten har Elias tagit till en del koncentrat?', steg, '4 delar vatten till 1 del koncentrat.', '',
                  k, 'A', 5, (0, 1, 2), tol=0.05, ratt_txt=['4'], fel=['5', '0,25', '6'])]
    q = H.bygg(uid, 2, 'densitet', SAMMANSATT[0], intro, delar, ('problemlösning', 'modellering'), True, False,
               'Utgå från 1 dl koncentrat och x dl vatten. Vad väger saften och vilken volym har den?', VARIANTER, fy=True,
               familjnyckel=SAMMANSATT[1])
    q['typ'] = 'bestämma blandningsförhållandet mellan koncentrat och vatten ur saftens densitet'
    return q


UPPGIFTER = [q1, q2, q3, q4, q5, q6]


def main():
    src, bank = H.las(BANK)
    nasta = H.nasta_id(bank, 2)
    nya = [f(f'2.{nasta + i}') for i, f in enumerate(UPPGIFTER)]
    assert not {q['id'] for q in bank} & {q['id'] for q in nya}
    print('uppgifter', len(nya), 'kort', sum(len(q.get('spelDelar') or [1]) for q in nya), [q['id'] for q in nya])
    if '--ut' in sys.argv:
        Path(sys.argv[sys.argv.index('--ut') + 1]).write_text(json.dumps(nya, ensure_ascii=False), encoding='utf-8')
    if '--skriv' in sys.argv:
        H.lagg_till(BANK, src, nya)


if __name__ == '__main__':
    main()
