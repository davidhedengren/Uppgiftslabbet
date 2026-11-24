"""Fy1 kopplingar: mängdträning på komplexa (blandade) kopplingar, 8.740– (2026-11-24).

Uppdrag (användaren 2026-11-24): ”skapa fler mängdträningsuppgifter på komplexa kopplingar i fysik 1. Här har eleverna
svårt, så här behövs många olika, varierade kretsar på olika svårighetsnivåer.”

Två delmoment i området `kopplingar`:
- ”Blandade kopplingar” (befintligt): ersättningsresistans för kopplingar med både serie- och parallelldelar.
- ”Ström och spänning i blandade kopplingar” (nytt): grenströmmar, spänningsfördelning, mätare, brytare och effekt.

Nivåer: 1 = ett steg i en blandad krets (knutpunktsregeln, spänningslagen eller Ohms lag för en komponent),
2 = två steg, 3 = hela analysen eller ett resonemang, 4 = nästlade kopplingar och okända storheter ur mätvärden,
5 = problemlösning med flera villkor. Varje uppgift är fristående och har en egen kretsfigur (tools/kretsrit.py).
Alla svar räknas i koden; testet tools/fysik1-komplexa-kopplingar-2026-11-24.test.js räknar om dem oberoende.
Facit följer agent/FACITMALL.md med rubriker skrivna för varje uppgift.

  python tools/bygg-fy1-komplexa-kopplingar-2026-11-24.py [--skriv]
"""
import json
import math
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402
from kretsrit import R, L, M, S, Sakring, Ser, Par, krets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKRIV = '--skriv' in sys.argv
BOK = 'abcdefgh'
F_RES = ('Blandade kopplingar', 'kopplingar__kretsanalys_och_blandade_resistorkopplingar')
F_IU = ('Ström och spänning i blandade kopplingar', 'kopplingar__strom_och_spanning_i_blandade_kopplingar')


# ================================================================ text och tal
def sig(v, n=2):
    if v == 0:
        return '0'
    e = math.floor(math.log10(abs(v)))
    d = n - 1 - e
    txt = f'{round(v, d):.{d}f}' if d > 0 else str(int(round(v, d)))
    return txt.replace('.', ',').replace('-', '−')


def tx(v, n=2):
    return sig(v, n).replace(',', '{,}').replace('−', '-')


def p(t):
    return f'<p>{t}</p>'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def al(*rader):
    return mt('\\begin{aligned}' + '\\\\'.join('&' + r for r in rader) + '\\end{aligned}')


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def delfacit(steg, svar):
    return ('<ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p>')


def fig(html):
    return f'<span class="fig">{html}</span>'


def par(*r):
    return 1 / sum(1 / x for x in r)


def tol(v, n):
    e = math.floor(math.log10(abs(v)))
    return round(0.5 * 10 ** (e - n + 1), 12)


OHM, V, A, W = '\\ \\Omega', '\\ \\mathrm V', '\\ \\mathrm A', '\\ \\mathrm W'
OHMS_LAG = 'Ohms lag: \\(U=RI\\)'
SERIE = 'Seriekoppling: \\(R=R_1+R_2\\)'
PARALLELL = 'Parallellkoppling: \\(\\frac{1}{R}=\\frac{1}{R_1}+\\frac{1}{R_2}\\)'
KNUT = 'Strömmen in i en knutpunkt är lika stor som strömmen ut'
EFFEKT = 'Effekt: \\(P=UI\\)'

NIVA = {1: ('E', '(1/0/0)'), 2: ('E', '(1/0/0)'), 3: ('C', '(0/1/0)'), 4: ('A', '(0/1/1)'), 5: ('A', '(0/0/2)')}
UPPG = []


def uppgift(uid, tn, familj, text, figur, fraga, svar, enhet, steg, svartext, ledtrad, siffror=2,
            formaga=('procedur',), alternativ=None, delar=None, kg=None, niva=None):
    UPPG.append(dict(id=uid, tn=tn, familj=familj, text=text, figur=figur, fraga=fraga, svar=svar, enhet=enhet,
                     steg=steg, svartext=svartext, ledtrad=ledtrad, siffror=siffror, formaga=list(formaga),
                     alternativ=alternativ, delar=delar, kg=kg, niva=niva))


def objekt(u):
    tn = u['tn']
    niva, poang = u['niva'] or NIVA[tn]
    intro = p(u['text']) + fig(u['figur'])
    q = {'id': u['id'], 'kap': 8, 'omr': 'kopplingar', 'niva': niva, 'poang': poang,
         'familj': u['familj'][0], 'familjNyckel': u['familj'][1], 'formaga': u['formaga']}
    if u['delar']:
        d = u['delar']
        q['t'] = intro + '<ol type="a">' + ''.join(f'<li>{x["fraga"]}</li>' for x in d) + '</ol>'
        q['s'] = ('<div class="facit-v2 facit-stegvis">' + ''.join(
            f'<div class="facit-del"><span class="facit-mark">{BOK[i]})</span><div class="facit-arbete">'
            f'{delfacit(x["steg"], x["svartext"])}</div></div>' for i, x in enumerate(d)) + '</div>')
        q['svarstyp'] = 'flera_delar'
        q['rättSvar'] = [x['svar'] for x in d]
        q['tolerans'] = [tol(x['svar'], 2) for x in d]
        q['svarFormat'] = ['numeriskt'] * len(d)
        q['svarEnhet'] = [x['enhet'] for x in d]
        q['svarVardesiffror'] = [2] * len(d)
        q['svarsstruktur'] = 'ordnad'
        q['svarEtiketter'] = [BOK[i] for i in range(len(d))]
        q['spelDelning'] = 'deluppgifter'
        q['spelIntro'] = intro
        q['spelDelar'] = []
        for i, x in enumerate(d):
            n2, p2 = NIVA[x['tn']]
            q['spelDelar'].append({
                'etikett': BOK[i], 'fraga': x['fraga'], 't': intro + (p(x['mellan']) if x.get('mellan') else '') + p(x['fraga']),
                's': '<div class="facit-v2 facit-stegvis"><div class="spel-en-del">' + delfacit(x.get('steg_kort', x['steg']), x['svartext']) + '</div></div>',
                'ledtrad': p(x['ledtrad']), 'niva': n2, 'traningsniva': x['tn'],
                'arbetsinsats': 1 if x['tn'] <= 2 else 2, 'poang': p2})
    else:
        q['t'] = intro + p(u['fraga'])
        q['s'] = facit(u['steg'], u['svartext'])
        if u['alternativ']:
            q['svarstyp'] = 'alternativ'
            q['rättSvar'] = None
            q['tolerans'] = None
            q['visaAlternativ'] = True
            q['alternativ'] = [{'txt': t, 'ratt': r, 'kommentar': k} for t, r, k in u['alternativ']]
        elif u['enhet'] is None:      # antal
            q['svarstyp'] = 'numeriskt'
            q['rättSvar'] = u['svar']
            q['tolerans'] = 0
            q['svarFormat'] = 'numeriskt'
        else:
            q['svarstyp'] = 'numeriskt'
            q['rättSvar'] = u['svar']
            q['tolerans'] = tol(u['svar'], u['siffror'])
            q['svarFormat'] = 'numeriskt'
            q['svarEnhet'] = u['enhet']
            q['svarVardesiffror'] = u['siffror']
    q['självrättning'] = True
    q['ledtrad'] = p(u['ledtrad'])
    q['traningsniva'] = tn
    q['arbetsinsats'] = 1 if tn <= 2 else 2 if tn <= 4 else 3
    q['spel'] = True
    q['miniräknare'] = True
    q['geogebra'] = False
    if u['kg']:
        q['kgInstruktion'] = u['kg']
    return q


def givet(*rader, sokt):
    return li('Givet och sökt', al(*rader), p(f'Sökt: {sokt}.'))


# ================================================================ nivå 1: ett steg i en blandad krets
def niva1():
    uppgift('8.740', 1, F_IU,
            'Resistorn R₁ är seriekopplad med de parallellkopplade resistorerna R₂ och R₃. Batteriets spänning är '
            '12 V, och spänningen över R₁ är 4,0 V.',
            krets(Ser(R('R₁'), Par(R('R₂'), R('R₃'))), '12 V', 'R₁ i serie med de parallellkopplade R₂ och R₃, batteri 12 V'),
            'Hur stor är spänningen över R₃?', 8.0, 'V',
            [givet('U=12\\ \\mathrm V', 'U_1=4{,}0\\ \\mathrm V', sokt='spänningen \\(U_3\\) över R₃'),
             li('Spänningarna längs en slinga runt kretsen summeras till batteriets spänning',
                p('En väg från pluspolen till minuspolen går genom R₁ och sedan genom R₃. R₂ och R₃ har samma '
                  'spänning eftersom de är parallellkopplade.'),
                mt('U_3=U-U_1=12-4{,}0=8{,}0' + V))],
            '8,0 V.', 'Följ en väg från batteriets ena pol till den andra som går genom R₃. Vilka spänningar ligger längs vägen?')

    uppgift('8.741', 1, F_IU,
            'I en leksaksbil lyser tre lampor. Amperemetern A₁ i huvudledningen visar 0,90 A och amperemetern A₂, '
            'som sitter i samma gren som L₂, visar 0,35 A.',
            krets(Ser(M('A', 'A₁'), L('L₁'), Par(Ser(L('L₂'), M('A', 'A₂')), L('L₃'))), '',
                  'Lampan L₁ i serie med två parallella grenar: L₂ med amperemetern A₂ och L₃. A₁ i huvudledningen.'),
            'Hur stor är strömmen genom L₃?', 0.55, 'A',
            [givet('I=0{,}90\\ \\mathrm A', 'I_2=0{,}35\\ \\mathrm A', sokt='strömmen \\(I_3\\) genom L₃'),
             li(f'{KNUT}: \\(I=I_2+I_3\\)',
                p('Hela strömmen går genom L₁ och delar sig sedan mellan grenarna med L₂ och L₃.'),
                mt('I_3=I-I_2=0{,}90-0{,}35=0{,}55' + A))],
            '0,55 A.', 'Strömmen i huvudledningen delar sig i knutpunkten. Hur stor del går genom grenen med L₂?')

    uppgift('8.742', 1, F_RES,
            'R₂ och R₃ är lika stora, 8,0 Ω vardera, och parallellkopplade. R₁ ligger i serie med dem.',
            krets(Ser(R('R₁'), Par(R('R₂', '8,0 Ω'), R('R₃', '8,0 Ω'))), '',
                  'R₁ i serie med två parallellkopplade resistorer på 8,0 Ω'),
            'Vilken ersättningsresistans har R₂ och R₃ tillsammans?', 4.0, 'Ω',
            [givet('R_2=R_3=8{,}0\\ \\Omega', sokt='ersättningsresistansen för R₂ och R₃'),
             li(PARALLELL,
                p('Två lika stora parallellkopplade resistorer ger hälften av den enskilda resistansen, eftersom '
                  'strömmen får två lika breda vägar.'),
                mt('\\frac{1}{R_p}=\\frac{1}{8{,}0}+\\frac{1}{8{,}0}=\\frac{2}{8{,}0}\\quad\\Rightarrow\\quad R_p=4{,}0' + OHM))],
            '4,0 Ω.', 'Strömmen får två lika breda vägar. Blir resistansen större eller mindre än för en resistor?')

    uppgift('8.743', 1, F_RES,
            'En krets har två parallella grenar. I den ena grenen sitter R₁ ensam, i den andra är R₂ = 15 Ω och '
            'R₃ = 25 Ω seriekopplade.',
            krets(Par(R('R₁'), Ser(R('R₂', '15 Ω'), R('R₃', '25 Ω'))), '',
                  'Två grenar: R₁ ensam och R₂ = 15 Ω i serie med R₃ = 25 Ω'),
            'Hur stor resistans har grenen med R₂ och R₃?', 40, 'Ω',
            [givet('R_2=15\\ \\Omega', 'R_3=25\\ \\Omega', sokt='resistansen i grenen med R₂ och R₃'),
             li(SERIE, p('I grenen går samma ström genom båda resistorerna efter varandra.'),
                mt('R=15+25=40' + OHM))],
            '40 Ω.', 'Ligger R₂ och R₃ i serie eller parallellt med varandra?')

    uppgift('8.744', 1, F_IU,
            'R₁ och grenen med R₂ och R₃ är parallellkopplade till ett batteri på 9,0 V. Spänningen över R₂ är 3,6 V.',
            krets(Par(R('R₁'), Ser(R('R₂'), R('R₃'))), '9,0 V', 'R₁ parallellt med R₂ i serie med R₃, batteri 9,0 V'),
            'Hur stor är spänningen över R₃?', 5.4, 'V',
            [givet('U=9{,}0\\ \\mathrm V', 'U_2=3{,}6\\ \\mathrm V', sokt='spänningen \\(U_3\\) över R₃'),
             li('Grenen med R₂ och R₃ har hela batterispänningen: \\(U_2+U_3=U\\)',
                p('Grenen är kopplad direkt mellan batteriets poler, och spänningen delas mellan R₂ och R₃.'),
                mt('U_3=9{,}0-3{,}6=5{,}4' + V))],
            '5,4 V.', 'Hur stor spänning ligger över hela grenen med R₂ och R₃?')

    uppgift('8.745', 1, F_IU,
            'I kretsen är R₁ = 15 Ω, och strömmen genom R₁ är 0,40 A.',
            krets(Ser(R('R₁', '15 Ω'), Par(R('R₂'), Ser(R('R₃'), R('R₄')))), '', 'R₁ = 15 Ω i serie med en parallellkoppling'),
            'Hur stor är spänningen över R₁?', 6.0, 'V',
            [givet('R_1=15\\ \\Omega', 'I_1=0{,}40\\ \\mathrm A', sokt='spänningen \\(U_1\\) över R₁'),
             li(OHMS_LAG, p('Ohms lag gäller för varje resistor för sig, med resistorns egen ström.'),
                mt('U_1=R_1I_1=15\\cdot0{,}40=6{,}0' + V))],
            '6,0 V.', 'Du behöver bara R₁:s egen resistans och ström. Resten av kretsen påverkar inte beräkningen.')

    uppgift('8.746', 1, F_IU,
            'En bils två framlampor är parallellkopplade och får ström genom samma säkring. Strömmen genom varje lampa '
            'är 4,5 A.',
            krets(Ser(Sakring('Säkring'), Par(L('L₁'), L('L₂'))), '12 V', 'Säkring i serie med två parallellkopplade framlampor, 12 V'),
            'Hur stor är strömmen genom säkringen?', 9.0, 'A',
            [givet('I_1=I_2=4{,}5\\ \\mathrm A', sokt='strömmen genom säkringen'),
             li(f'{KNUT}: \\(I=I_1+I_2\\)', p('All ström till båda lamporna passerar säkringen innan den delar sig.'),
                mt('I=4{,}5+4{,}5=9{,}0' + A))],
            '9,0 A.', 'Säkringen sitter före förgreningen. Vilka strömmar går genom den?')

    uppgift('8.747', 1, F_IU,
            'En voltmeter är kopplad över grenen med R₁ och R₂. Grenen är parallellkopplad med R₃, och R₄ ligger i serie '
            'med parallellkopplingen. Voltmetern visar 7,5 V.',
            krets(Ser(Par(Ser(R('R₁'), R('R₂')), R('R₃'), M('V')), R('R₄')), '12 V',
                  'Grenen R₁–R₂ parallellt med R₃ och en voltmeter, i serie med R₄'),
            'Hur stor är spänningen över R₃?', 7.5, 'V',
            [givet('U_{12}=7{,}5\\ \\mathrm V', sokt='spänningen \\(U_3\\) över R₃'),
             li('Parallellkopplade grenar har samma spänning: \\(U_3=U_{12}\\)',
                p('Grenen med R₁ och R₂, R₃ och voltmetern är kopplade mellan samma två knutpunkter.'), mt('U_3=7{,}5' + V))],
            '7,5 V.', 'Mellan vilka två punkter är grenen med R₁ och R₂ kopplad? Mellan vilka är R₃ kopplad?')

    uppgift('8.748', 1, F_RES,
            'Parallellkopplingen av R₁ och R₂ har ersättningsresistansen 6,0 Ω. På var sida om den sitter R₃ = 10 Ω och '
            'R₄ = 5,0 Ω.',
            krets(Ser(R('R₃', '10 Ω'), Par(R('R₁'), R('R₂')), R('R₄', '5,0 Ω')), '', 'R₃ = 10 Ω, parallellkopplade R₁ och R₂ och R₄ = 5,0 Ω i serie', batteri=False),
            'Vilken ersättningsresistans har hela kopplingen mellan A och B?', 21, 'Ω',
            [givet('R_3=10\\ \\Omega', 'R_p=6{,}0\\ \\Omega', 'R_4=5{,}0\\ \\Omega', sokt='ersättningsresistansen mellan A och B'),
             li('Seriekoppling: \\(R=R_3+R_p+R_4\\)', p('Parallellkopplingen kan ersättas av en resistor på 6,0 Ω. Den ligger i serie med R₃ och R₄.'),
                mt('R=10+6{,}0+5{,}0=21' + OHM))],
            '21 Ω.', 'Ersätt parallellkopplingen med en enda resistor. Hur ligger den i förhållande till R₃ och R₄?')

    uppgift('8.749', 1, F_IU,
            'Strömmen genom R₂ är 0,20 A, genom R₃ 0,30 A och genom R₄ 0,15 A.',
            krets(Ser(R('R₁'), Par(R('R₂'), R('R₃'), R('R₄'))), '6,0 V', 'R₁ i serie med tre parallellkopplade resistorer R₂, R₃ och R₄'),
            'Hur stor ström går genom R₁?', 0.65, 'A',
            [givet('I_2=0{,}20\\ \\mathrm A', 'I_3=0{,}30\\ \\mathrm A', 'I_4=0{,}15\\ \\mathrm A', sokt='strömmen \\(I_1\\) genom R₁'),
             li(f'{KNUT}: \\(I_1=I_2+I_3+I_4\\)', p('Strömmen genom R₁ delar sig på tre grenar och samlas sedan igen.'),
                mt('I_1=0{,}20+0{,}30+0{,}15=0{,}65' + A))],
            '0,65 A.', 'R₁ sitter i huvudledningen. Vart tar dess ström vägen efter knutpunkten?')


# ================================================================ nivå 2: två steg
def niva2():
    r = 4 + par(6, 12)
    uppgift('8.750', 2, F_RES, 'Tre resistorer är kopplade som i figuren.',
            krets(Ser(R('R₁', '4,0 Ω'), Par(R('R₂', '6,0 Ω'), R('R₃', '12 Ω'))), '',
                  'R₁ = 4,0 Ω i serie med R₂ = 6,0 Ω parallellt med R₃ = 12 Ω'),
            'Bestäm kopplingens ersättningsresistans.', r, 'Ω',
            [givet('R_1=4{,}0\\ \\Omega', 'R_2=6{,}0\\ \\Omega', 'R_3=12\\ \\Omega', sokt='ersättningsresistansen'),
             li(f'R₂ och R₃ är parallellkopplade. {PARALLELL}', mt('\\frac{1}{R_p}=\\frac{1}{6{,}0}+\\frac{1}{12}=\\frac{3}{12}\\quad\\Rightarrow\\quad R_p=4{,}0' + OHM)),
             li(f'R₁ ligger i serie med parallellkopplingen. {SERIE}', mt('R=4{,}0+4{,}0=8{,}0' + OHM))],
            '8,0 Ω.', 'Börja med den del av kopplingen som bara innehåller parallellkopplade resistorer.')

    uppgift('8.751', 2, F_RES, 'Fyra resistorer är kopplade mellan punkterna A och B.',
            krets(Par(Ser(R('R₁', '10 Ω'), R('R₂', '20 Ω')), R('R₃', '30 Ω')), '', 'Mellan A och B: R₁ = 10 Ω i serie med R₂ = 20 Ω, parallellt med R₃ = 30 Ω', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B.', 15, 'Ω',
            [givet('R_1=10\\ \\Omega', 'R_2=20\\ \\Omega', 'R_3=30\\ \\Omega', sokt='ersättningsresistansen mellan A och B'),
             li(f'R₁ och R₂ sitter i samma gren. {SERIE}', mt('R_{12}=10+20=30' + OHM)),
             li(f'Den grenen är parallellkopplad med R₃. {PARALLELL}',
                p('Två lika stora grenar ger halva resistansen.'), mt('\\frac{1}{R}=\\frac{1}{30}+\\frac{1}{30}\\quad\\Rightarrow\\quad R=15' + OHM))],
            '15 Ω.', 'Räkna först ut resistansen i den gren som har två resistorer.')

    uppgift('8.752', 2, F_RES, 'Två parallellkopplingar är seriekopplade.',
            krets(Ser(Par(R('R₁', '6,0 Ω'), R('R₂', '3,0 Ω')), Par(R('R₃', '4,0 Ω'), R('R₄', '4,0 Ω'))), '',
                  'R₁ = 6,0 Ω parallellt med R₂ = 3,0 Ω, i serie med R₃ = 4,0 Ω parallellt med R₄ = 4,0 Ω', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B.', 4.0, 'Ω',
            [givet('R_1=6{,}0\\ \\Omega', 'R_2=3{,}0\\ \\Omega', 'R_3=R_4=4{,}0\\ \\Omega', sokt='ersättningsresistansen'),
             li(f'Första parallellkopplingen. {PARALLELL}', mt('\\frac{1}{R_{12}}=\\frac{1}{6{,}0}+\\frac{1}{3{,}0}=\\frac{3}{6{,}0}\\quad\\Rightarrow\\quad R_{12}=2{,}0' + OHM)),
             li('Andra parallellkopplingen har två lika stora resistorer', mt('R_{34}=\\frac{4{,}0}{2}=2{,}0' + OHM)),
             li(f'De två delarna ligger i serie. {SERIE}', mt('R=2{,}0+2{,}0=4{,}0' + OHM))],
            '4,0 Ω.', 'Ersätt varje parallellkoppling med en resistor för sig. Hur ligger de sedan?')

    I = 12 / r
    uppgift('8.753', 2, F_IU, 'Kopplingen ansluts till ett batteri på 9,0 V.',
            krets(Ser(Par(R('R₁', '10 Ω'), R('R₂', '15 Ω')), R('R₃', '3,0 Ω')), '9,0 V', 'R₁ = 10 Ω parallellt med R₂ = 15 Ω, i serie med R₃ = 3,0 Ω, 9,0 V'),
            'Hur stor ström går genom batteriet?', 1.0, 'A',
            [givet('U=9{,}0\\ \\mathrm V', 'R_1=10\\ \\Omega', 'R_2=15\\ \\Omega', 'R_3=3{,}0\\ \\Omega', sokt='strömmen \\(I\\) genom batteriet'),
             li('Ersättningsresistans: \\(R=\\left(\\frac{1}{R_1}+\\frac{1}{R_2}\\right)^{-1}+R_3\\)',
                mt('R_p=\\left(\\frac{1}{10}+\\frac{1}{15}\\right)^{-1}=6{,}0' + OHM), mt('R=6{,}0+3{,}0=9{,}0' + OHM)),
             li(f'{OHMS_LAG} för hela kretsen', mt('I=\\frac{U}{R}=\\frac{9{,}0}{9{,}0}=1{,}0' + A))],
            '1,0 A.', 'Batteriet ser hela kopplingen som en enda resistor. Hur stor är den?')

    rp = par(20, 30)
    uppgift('8.754', 2, F_IU,
            'Ett värmeelement har två slingor, R₁ = 20 Ω och R₂ = 30 Ω, som är parallellkopplade. R₃ = 8,0 Ω ligger i '
            'serie med dem. Strömmen i huvudledningen är 1,2 A.',
            krets(Ser(Par(R('R₁', '20 Ω'), R('R₂', '30 Ω')), R('R₃', '8,0 Ω')), '24 V', 'Två slingor 20 Ω och 30 Ω parallellt, i serie med 8,0 Ω'),
            'Hur stor är spänningen över slingorna?', 1.2 * rp, 'V',
            [givet('R_1=20\\ \\Omega', 'R_2=30\\ \\Omega', 'I=1{,}2\\ \\mathrm A', sokt='spänningen över parallellkopplingen'),
             li(PARALLELL, mt('\\frac{1}{R_p}=\\frac{1}{20}+\\frac{1}{30}=\\frac{5}{60}\\quad\\Rightarrow\\quad R_p=12' + OHM)),
             li(f'{OHMS_LAG} för parallellkopplingen', p('Hela huvudströmmen går genom parallellkopplingen.'),
                mt('U_p=R_pI=12\\cdot1{,}2=14{,}4\\approx14' + V))],
            '14 V.', 'Hela strömmen 1,2 A passerar parallellkopplingen. Vilken resistans har den?')

    uppgift('8.755', 2, F_IU, 'Ett batteri på 6,0 V är kopplat till tre resistorer. R₁ sitter ensam i en gren, och R₂ och R₃ sitter i den andra.',
            krets(Par(R('R₁', '15 Ω'), Ser(R('R₂', '10 Ω'), R('R₃', '20 Ω'))), '6,0 V', 'R₁ = 15 Ω parallellt med R₂ = 10 Ω i serie med R₃ = 20 Ω, 6,0 V'),
            'Bestäm strömmen genom R₂.', 0.20, 'A',
            [givet('U=6{,}0\\ \\mathrm V', 'R_2=10\\ \\Omega', 'R_3=20\\ \\Omega', sokt='strömmen \\(I_2\\) genom R₂'),
             li('Grenen med R₂ och R₃ har hela batterispänningen', p('Den är kopplad direkt mellan batteriets poler. R₁ påverkar inte strömmen i grenen.'),
                mt('R_{23}=10+20=30' + OHM)),
             li(f'{OHMS_LAG} för grenen', mt('I_2=\\frac{U}{R_{23}}=\\frac{6{,}0}{30}=0{,}20' + A))],
            '0,20 A.', 'Vilken spänning ligger över grenen där R₂ sitter? Behövs R₁ i beräkningen?')

    uppgift('8.756', 2, F_RES,
            'I ett dockskåp lyser tre lampor från samma batteri. Varje lampa har resistansen 12 Ω. L₁ och L₂ är '
            'seriekopplade, och L₃ är parallellkopplad med dem.',
            krets(Par(Ser(L('L₁', '12 Ω'), L('L₂', '12 Ω')), L('L₃', '12 Ω')), '4,5 V', 'L₁ i serie med L₂, parallellt med L₃, alla 12 Ω'),
            'Hur stor är lampkopplingens ersättningsresistans?', 8.0, 'Ω',
            [givet('R_1=R_2=R_3=12\\ \\Omega', sokt='ersättningsresistansen'),
             li(f'L₁ och L₂ i samma gren. {SERIE}', mt('R_{12}=12+12=24' + OHM)),
             li(f'Grenen parallellt med L₃. {PARALLELL}',
                mt('\\frac{1}{R}=\\frac{1}{24}+\\frac{1}{12}=\\frac{3}{24}\\quad\\Rightarrow\\quad R=8{,}0' + OHM))],
            '8,0 Ω.', 'Vilka lampor har samma ström? Räkna ut den grenens resistans först.')

    uppgift('8.757', 2, F_IU,
            'Strömmen i huvudledningen är 0,60 A. Genom R₂ = 30 Ω går strömmen 0,20 A.',
            krets(Ser(R('R₁'), Par(R('R₂', '30 Ω'), R('R₃'))), '', 'R₁ i serie med R₂ = 30 Ω parallellt med R₃'),
            'Bestäm resistansen R₃.', 15, 'Ω',
            [givet('I=0{,}60\\ \\mathrm A', 'I_2=0{,}20\\ \\mathrm A', 'R_2=30\\ \\Omega', sokt='resistansen \\(R_3\\)'),
             li(f'{OHMS_LAG} för R₂ ger spänningen över parallellkopplingen', mt('U_p=R_2I_2=30\\cdot0{,}20=6{,}0' + V)),
             li(f'{KNUT}: \\(I_3=I-I_2\\)', mt('I_3=0{,}60-0{,}20=0{,}40' + A)),
             li('Ohms lag för R₃: \\(R_3=\\frac{U_p}{I_3}\\)', mt('R_3=\\frac{6{,}0}{0{,}40}=15' + OHM))],
            '15 Ω.', 'R₂ och R₃ har samma spänning. Hur stor är den, och hur stor ström går genom R₃?')

    r3 = par(10, 10, 5)
    uppgift('8.758', 2, F_RES, 'Fem resistorer är kopplade mellan punkterna A och B.',
            krets(Par(R('R₁', '10 Ω'), R('R₂', '10 Ω'), Ser(R('R₃', '2,0 Ω'), R('R₄', '3,0 Ω'))), '',
                  'Tre grenar: 10 Ω, 10 Ω och 2,0 Ω i serie med 3,0 Ω', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B.', r3, 'Ω',
            [givet('R_1=R_2=10\\ \\Omega', 'R_3=2{,}0\\ \\Omega', 'R_4=3{,}0\\ \\Omega', sokt='ersättningsresistansen'),
             li(f'Den tredje grenen. {SERIE}', mt('R_{34}=2{,}0+3{,}0=5{,}0' + OHM)),
             li('Tre parallella grenar: \\(\\frac{1}{R}=\\frac{1}{R_1}+\\frac{1}{R_2}+\\frac{1}{R_{34}}\\)',
                mt('\\frac{1}{R}=\\frac{1}{10}+\\frac{1}{10}+\\frac{1}{5{,}0}=\\frac{4}{10}'), mt('R=\\frac{10}{4}=2{,}5' + OHM))],
            '2,5 Ω.', 'Hur många grenar finns det mellan A och B, och vilken resistans har varje gren?')

    uppgift('8.759', 2, F_IU, 'En spänningsdelare består av R₂ och R₃ i serie. Den är kopplad direkt över ett batteri på 12 V, parallellt med lasten R₁.',
            krets(Par(R('R₁', '6,0 Ω'), Ser(R('R₂', '4,0 Ω'), R('R₃', '8,0 Ω'))), '12 V', 'R₁ = 6,0 Ω parallellt med R₂ = 4,0 Ω i serie med R₃ = 8,0 Ω, 12 V'),
            'Vilken spänning får R₃?', 8.0, 'V',
            [givet('U=12\\ \\mathrm V', 'R_2=4{,}0\\ \\Omega', 'R_3=8{,}0\\ \\Omega', sokt='spänningen \\(U_3\\)'),
             li(f'{OHMS_LAG} för grenen med R₂ och R₃', p('Grenen ligger direkt över batteriet och har därför 12 V.'),
                mt('I_{23}=\\frac{12}{4{,}0+8{,}0}=1{,}0' + A)),
             li('Ohms lag för R₃: \\(U_3=R_3I_{23}\\)', mt('U_3=8{,}0\\cdot1{,}0=8{,}0' + V))],
            '8,0 V.', 'Grenen med R₂ och R₃ har batteriets spänning. Hur fördelas den mellan resistorerna?')

    r4 = 2.2 + par(5.6, 5.6)
    uppgift('8.760', 2, F_RES, 'På ett kretskort är tre resistorer kopplade som i figuren.',
            krets(Ser(R('R₁', '2,2 kΩ'), Par(R('R₂', '5,6 kΩ'), R('R₃', '5,6 kΩ'))), '', 'R₁ = 2,2 kΩ i serie med två parallellkopplade 5,6 kΩ', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B i kΩ.', r4, 'kΩ',
            [givet('R_1=2{,}2\\ \\mathrm{k\\Omega}', 'R_2=R_3=5{,}6\\ \\mathrm{k\\Omega}', sokt='ersättningsresistansen i kΩ'),
             li('Två lika stora parallellkopplade resistorer ger halva resistansen', mt('R_{23}=\\frac{5{,}6}{2}=2{,}8\\ \\mathrm{k\\Omega}')),
             li(SERIE, mt('R=2{,}2+2{,}8=5{,}0\\ \\mathrm{k\\Omega}'))],
            '5,0 kΩ.', 'Du kan räkna direkt i kΩ så länge alla resistanser har samma enhet.')

    uppgift('8.761', 2, F_IU, 'Ett batteri på 9,0 V driver en sensorkrets med tre resistorer.',
            krets(Ser(R('R₁', '1,0 kΩ'), Par(R('R₂', '2,0 kΩ'), R('R₃', '2,0 kΩ'))), '9,0 V', 'R₁ = 1,0 kΩ i serie med två parallellkopplade 2,0 kΩ, 9,0 V'),
            'Hur stor är strömmen genom batteriet i mA?', 4.5, 'mA',
            [givet('U=9{,}0\\ \\mathrm V', 'R_1=1{,}0\\ \\mathrm{k\\Omega}', 'R_2=R_3=2{,}0\\ \\mathrm{k\\Omega}', sokt='strömmen i mA'),
             li('Ersättningsresistans: \\(R=R_1+\\frac{R_2}{2}\\) när R₂ = R₃', mt('R=1{,}0+\\frac{2{,}0}{2}=2{,}0\\ \\mathrm{k\\Omega}=2000' + OHM)),
             li(f'{OHMS_LAG}: \\(I=\\frac{{U}}{{R}}\\)', mt('I=\\frac{9{,}0}{2000}=0{,}0045' + A + '=4{,}5\\ \\mathrm{mA}'))],
            '4,5 mA.', 'Gör om kΩ till Ω innan du delar, eller tänk på vad V/kΩ blir för enhet.')

    uppgift('8.762', 2, F_IU,
            'Tre likadana lampor är kopplade till ett batteri. L₁ sitter i huvudledningen och L₂ och L₃ är parallellkopplade.',
            krets(Ser(L('L₁'), Par(L('L₂'), L('L₃'))), '4,5 V', 'L₁ i serie med parallellkopplade L₂ och L₃'),
            'Vilken lampa lyser starkast?', None, None,
            [li('Strömmen genom L₁ delar sig mellan L₂ och L₃',
                p('Hela strömmen går genom L₁. I knutpunkten delar den sig lika mellan de likadana lamporna L₂ och L₃, '
                  'så de får hälften var.')),
             li('Effekt i en lampa: \\(P=RI^2\\)', p('Med samma resistans ger dubbel ström fyra gånger så stor effekt. L₁ lyser starkast.'))],
            'L₁ lyser starkast.', 'Vilken lampa får hela strömmen, och hur delar sig strömmen sedan?', formaga=('begrepp',),
            alternativ=[('L₁', True, 'Hela strömmen går genom L₁, medan L₂ och L₃ delar på den.'),
                        ('L₂ och L₃ lyser lika starkt som L₁', False, 'L₂ och L₃ får bara halva strömmen var.'),
                        ('L₂', False, 'L₂ får samma ström som L₃, hälften av strömmen genom L₁.'),
                        ('Alla lyser lika starkt', False, 'Lamporna har samma resistans men inte samma ström.')])


# ================================================================ nivå 3: hela analysen
def niva3():
    uppgift('8.763', 3, F_IU,
            'Tre likadana lampor är seriekopplade med ett batteri. En brytare är kopplad parallellt med L₃. Brytaren är '
            'först öppen och sluts sedan.',
            krets(Ser(L('L₁'), L('L₂'), Par(L('L₃'), S('', oppen=True))), '4,5 V', 'L₁, L₂ och L₃ i serie, brytare parallellt med L₃'),
            'Vad händer med L₁ när brytaren sluts?', None, None,
            [li('En sluten brytare parallellt med en lampa kortsluter lampan',
                p('Brytaren har nästan ingen resistans, så strömmen går genom brytaren i stället för genom L₃. L₃ slocknar.')),
             li(f'{OHMS_LAG}: \\(I=\\frac{{U}}{{R}}\\)',
                p('Kretsen får bara två lampors resistans i stället för tre, så strömmen blir större. Hela strömmen går genom '
                  'L₁, som lyser starkare.'))],
            'L₁ lyser starkare.', 'Vilken väg tar strömmen när brytaren är sluten? Hur ändras då kretsens resistans?',
            formaga=('begrepp', 'resonemang'),
            alternativ=[('L₁ lyser starkare', True, 'L₃ kortsluts, resistansen minskar och strömmen genom L₁ ökar.'),
                        ('L₁ lyser svagare', False, 'Brytaren tar bort en lampas resistans ur kretsen, så strömmen ökar.'),
                        ('L₁ lyser lika starkt', False, 'Strömmen genom L₁ beror på hela kretsens resistans, som ändras.'),
                        ('L₁ slocknar', False, 'Det är L₃ som slocknar. L₁ har fortfarande en sluten slinga.')])

    I = 1.5
    uppgift('8.764', 3, F_IU, 'R₄ är kopplad parallellt med en gren som innehåller R₁ och de parallellkopplade R₂ och R₃. Kretsen drivs av 12 V.',
            krets(Par(Ser(R('R₁', '2,0 Ω'), Par(R('R₂', '6,0 Ω'), R('R₃', '3,0 Ω'))), R('R₄', '6,0 Ω')), '12 V',
                  'En gren med R₁ = 2,0 Ω i serie med 6,0 Ω parallellt med 3,0 Ω, och R₄ = 6,0 Ω parallellt med hela grenen'),
            'Hur stor blir strömmen genom R₃?', 2.0, 'A',
            [givet('U=12\\ \\mathrm V', 'R_1=2{,}0\\ \\Omega', 'R_2=6{,}0\\ \\Omega', 'R_3=3{,}0\\ \\Omega', sokt='strömmen \\(I_3\\)'),
             li('Den övre grenen har hela batterispänningen', p('Grenen med R₁, R₂ och R₃ ligger direkt över batteriet. R₄ påverkar inte strömmen i den.')),
             li('Grenens resistans: \\(R_g=R_1+\\left(\\frac{1}{R_2}+\\frac{1}{R_3}\\right)^{-1}\\)',
                mt('R_{23}=\\left(\\frac{1}{6{,}0}+\\frac{1}{3{,}0}\\right)^{-1}=2{,}0' + OHM), mt('R_g=2{,}0+2{,}0=4{,}0' + OHM)),
             li(f'{OHMS_LAG} för grenen och för parallelldelen', mt('I_g=\\frac{12}{4{,}0}=3{,}0' + A), mt('U_{23}=2{,}0\\cdot3{,}0=6{,}0' + V)),
             li('Ohms lag för R₃', mt('I_3=\\frac{6{,}0}{3{,}0}=2{,}0' + A))],
            '2,0 A.', 'Grenen med R₃ ligger direkt över batteriet. Behöver du R₄?')

    uppgift('8.765', 3, F_IU, 'I en krets på 24 V sitter R₁ före och R₄ efter en parallellkoppling av två lika resistorer.',
            krets(Ser(R('R₁', '3,0 Ω'), Par(R('R₂', '8,0 Ω'), R('R₃', '8,0 Ω')), R('R₄', '5,0 Ω')), '24 V',
                  'R₁ = 3,0 Ω, två parallellkopplade 8,0 Ω och R₄ = 5,0 Ω i serie, 24 V'),
            'Beräkna spänningen över R₄.', 10, 'V',
            [givet('U=24\\ \\mathrm V', 'R_1=3{,}0\\ \\Omega', 'R_2=R_3=8{,}0\\ \\Omega', 'R_4=5{,}0\\ \\Omega', sokt='spänningen \\(U_4\\)'),
             li('Ersättningsresistans: \\(R=R_1+\\frac{R_2}{2}+R_4\\) när R₂ = R₃', mt('R=3{,}0+4{,}0+5{,}0=12' + OHM)),
             li(f'{OHMS_LAG} för hela kretsen', mt('I=\\frac{24}{12}=2{,}0' + A)),
             li('Ohms lag för R₄, som har hela strömmen', mt('U_4=5{,}0\\cdot2{,}0=10' + V))],
            '10 V.', 'R₄ har hela huvudströmmen. Hur stor är den?')

    uppgift('8.766', 3, F_IU,
            'Lamporna L₁ (4,0 Ω) och L₂ (8,0 Ω) är seriekopplade, och L₃ (6,0 Ω) är parallellkopplad med dem. En '
            'resistor R = 2,0 Ω sitter i huvudledningen. Batteriets spänning är 6,0 V.',
            krets(Ser(R('R', '2,0 Ω'), Par(Ser(L('L₁', '4,0 Ω'), L('L₂', '8,0 Ω')), L('L₃', '6,0 Ω'))), '6,0 V',
                  'R = 2,0 Ω i serie med grenen L₁ 4,0 Ω och L₂ 8,0 Ω, parallellt med L₃ 6,0 Ω'),
            'Hur stor ström går genom L₁?', 1 / 3, 'A',
            [givet('U=6{,}0\\ \\mathrm V', 'R=2{,}0\\ \\Omega', 'R_1=4{,}0\\ \\Omega', 'R_2=8{,}0\\ \\Omega', 'R_3=6{,}0\\ \\Omega', sokt='strömmen \\(I_1\\)'),
             li('Ersättningsresistans: \\(R_{\\text{tot}}=R+\\left(\\frac{1}{R_1+R_2}+\\frac{1}{R_3}\\right)^{-1}\\)',
                mt('R_p=\\left(\\frac{1}{12}+\\frac{1}{6{,}0}\\right)^{-1}=4{,}0' + OHM), mt('R_{\\text{tot}}=2{,}0+4{,}0=6{,}0' + OHM)),
             li(f'{OHMS_LAG} för hela kretsen och för parallelldelen', mt('I=\\frac{6{,}0}{6{,}0}=1{,}0' + A), mt('U_p=4{,}0\\cdot1{,}0=4{,}0' + V)),
             li('Ohms lag för grenen med L₁ och L₂', mt('I_1=\\frac{4{,}0}{4{,}0+8{,}0}\\approx0{,}33' + A))],
            '0,33 A.', 'L₁ och L₂ har samma ström. Vilken spänning ligger över deras gren?')

    uppgift('8.767', 3, F_IU, 'Amperemetern sitter i samma gren som R₃. Batteriets spänning är 12 V.',
            krets(Ser(R('R₄', '5,0 Ω'), Par(Ser(R('R₁', '10 Ω'), R('R₂', '20 Ω')), Ser(R('R₃', '30 Ω'), M('A')))), '12 V',
                  'R₄ = 5,0 Ω i serie med två grenar: 10 Ω + 20 Ω och 30 Ω med amperemeter'),
            'Vad visar amperemetern?', 0.30, 'A',
            [givet('U=12\\ \\mathrm V', 'R_4=5{,}0\\ \\Omega', 'R_1=10\\ \\Omega', 'R_2=20\\ \\Omega', 'R_3=30\\ \\Omega', sokt='strömmen genom R₃'),
             li('Ersättningsresistans: \\(R=R_4+\\left(\\frac{1}{R_1+R_2}+\\frac{1}{R_3}\\right)^{-1}\\)',
                mt('R_{12}=10+20=30' + OHM), mt('R_p=\\frac{30}{2}=15' + OHM), mt('R=5{,}0+15=20' + OHM)),
             li(f'{OHMS_LAG} för hela kretsen och för parallellkopplingen', mt('I=\\frac{12}{20}=0{,}60' + A), mt('U_p=15\\cdot0{,}60=9{,}0' + V)),
             li('Ohms lag för grenen med R₃', p('Amperemetern har mycket liten resistans.'), mt('I_3=\\frac{9{,}0}{30}=0{,}30' + A))],
            '0,30 A.', 'De två grenarna har lika stor resistans. Hur delar sig strömmen då?')

    p2 = 4.5 ** 2 / 6
    uppgift('8.768', 3, F_IU, 'Batteriets spänning är 18 V.',
            krets(Ser(Par(R('R₁', '6,0 Ω'), Ser(R('R₂', '2,0 Ω'), R('R₃', '4,0 Ω'))), R('R₄', '3,0 Ω')), '18 V',
                  'R₁ = 6,0 Ω parallellt med R₂ = 2,0 Ω i serie med R₃ = 4,0 Ω, i serie med R₄ = 3,0 Ω, 18 V'),
            'Hur stor effekt utvecklas i R₂?', 4.5, 'W',
            [givet('U=18\\ \\mathrm V', 'R_1=6{,}0\\ \\Omega', 'R_2=2{,}0\\ \\Omega', 'R_3=4{,}0\\ \\Omega', 'R_4=3{,}0\\ \\Omega', sokt='effekten \\(P_2\\) i R₂'),
             li('Ersättningsresistans: \\(R=\\left(\\frac{1}{R_1}+\\frac{1}{R_2+R_3}\\right)^{-1}+R_4\\)',
                mt('R_p=\\left(\\frac{1}{6{,}0}+\\frac{1}{6{,}0}\\right)^{-1}=3{,}0' + OHM), mt('R=3{,}0+3{,}0=6{,}0' + OHM)),
             li(OHMS_LAG, mt('I=\\frac{18}{6{,}0}=3{,}0' + A), p('De två grenarna i parallellkopplingen har lika stor resistans och delar strömmen lika.'),
                mt('I_2=\\frac{3{,}0}{2}=1{,}5' + A)),
             li('Effekt: \\(P=RI^2\\)', mt('P_2=2{,}0\\cdot1{,}5^2=4{,}5' + W))],
            '4,5 W.', 'Hur stor del av huvudströmmen går genom grenen där R₂ sitter?')

    uppgift('8.769', 3, F_IU, 'Batteriets spänning är 10 V.',
            krets(Ser(R('R₁', '1,0 Ω'), Par(R('R₂', '2,0 Ω'), R('R₃', '6,0 Ω'))), '10 V', 'R₁ = 1,0 Ω i serie med R₂ = 2,0 Ω parallellt med R₃ = 6,0 Ω'),
            'I vilken resistor utvecklas störst effekt?', None, None,
            [givet('U=10\\ \\mathrm V', 'R_1=1{,}0\\ \\Omega', 'R_2=2{,}0\\ \\Omega', 'R_3=6{,}0\\ \\Omega', sokt='den resistor där effekten är störst'),
             li('Ersättningsresistans: \\(R=R_1+\\left(\\frac{1}{R_2}+\\frac{1}{R_3}\\right)^{-1}\\)',
                mt('R_p=\\left(\\frac{1}{2{,}0}+\\frac{1}{6{,}0}\\right)^{-1}=1{,}5' + OHM), mt('R=1{,}0+1{,}5=2{,}5' + OHM)),
             li(OHMS_LAG, mt('I=\\frac{10}{2{,}5}=4{,}0' + A), al('U_1=1{,}0\\cdot4{,}0=4{,}0' + V, 'U_p=1{,}5\\cdot4{,}0=6{,}0' + V)),
             li('Effekt: \\(P=UI=\\frac{U^2}{R}\\) för varje resistor',
                al('P_1=4{,}0\\cdot4{,}0=16' + W, 'P_2=\\frac{6{,}0^2}{2{,}0}=18' + W, 'P_3=\\frac{6{,}0^2}{6{,}0}=6{,}0' + W))],
            'I R₂.', 'Räkna ut spänningen över och strömmen genom varje resistor. Resistorn med hela strömmen behöver inte vinna.',
            formaga=('procedur', 'resonemang'),
            alternativ=[('I R₂', True, 'R₂ har 6,0 V och 3,0 A, alltså 18 W.'),
                        ('I R₁', False, 'R₁ har hela strömmen 4,0 A men bara 4,0 V, alltså 16 W.'),
                        ('I R₃', False, 'R₃ har störst resistans men minst ström: 1,0 A och 6,0 W.'),
                        ('Lika stor i alla', False, 'Strömmarna och spänningarna är olika, så effekterna blir olika.')])

    uppgift('8.770', 3, F_IU,
            'Tre lika resistorer på 10 Ω är kopplade till ett batteri på 12 V. Brytaren i grenen med R₃ är först '
            'öppen och sluts sedan.',
            krets(Ser(R('R₁', '10 Ω'), Par(R('R₂', '10 Ω'), Ser(R('R₃', '10 Ω'), S('', oppen=True)))), '12 V', 'R₁ i serie med R₂ parallellt med R₃ och en öppen brytare'),
            'Hur mycket ökar strömmen genom batteriet när brytaren sluts?', 0.20, 'A',
            [givet('U=12\\ \\mathrm V', 'R_1=R_2=R_3=10\\ \\Omega', sokt='ökningen av strömmen'),
             li('Brytaren öppen: R₁ och R₂ i serie', mt('I_{\\text{före}}=\\frac{12}{10+10}=0{,}60' + A)),
             li('Brytaren sluten: R₂ och R₃ parallellt, i serie med R₁', mt('R=10+\\frac{10}{2}=15' + OHM), mt('I_{\\text{efter}}=\\frac{12}{15}=0{,}80' + A)),
             li('Skillnad', mt('\\Delta I=0{,}80-0{,}60=0{,}20' + A))],
            '0,20 A.', 'Räkna kretsens resistans med brytaren öppen och med den sluten.')

    uppgift('8.771', 3, F_IU, 'Amperemetern sitter i huvudledningen. Batteriets spänning är 24 V.',
            krets(Ser(M('A'), Par(R('R₁', '6,0 Ω'), R('R₂', '3,0 Ω')), Par(R('R₃', '4,0 Ω'), R('R₄', '4,0 Ω'))), '24 V',
                  '6,0 Ω parallellt med 3,0 Ω, i serie med två parallellkopplade 4,0 Ω, amperemeter i huvudledningen'),
            'Hur stor ström går genom R₂?', 4.0, 'A',
            [givet('U=24\\ \\mathrm V', 'R_1=6{,}0\\ \\Omega', 'R_2=3{,}0\\ \\Omega', 'R_3=R_4=4{,}0\\ \\Omega', sokt='strömmen \\(I_2\\)'),
             li('Ersättningsresistans: \\(R=\\left(\\frac{1}{R_1}+\\frac{1}{R_2}\\right)^{-1}+\\frac{R_3}{2}\\)',
                mt('R_{12}=\\left(\\frac{1}{6{,}0}+\\frac{1}{3{,}0}\\right)^{-1}=2{,}0' + OHM), mt('R=2{,}0+2{,}0=4{,}0' + OHM)),
             li(f'{OHMS_LAG}', mt('I=\\frac{24}{4{,}0}=6{,}0' + A), mt('U_{12}=2{,}0\\cdot6{,}0=12' + V)),
             li('Ohms lag för R₂', mt('I_2=\\frac{12}{3{,}0}=4{,}0' + A))],
            '4,0 A.', 'De två parallellkopplingarna har lika stor resistans. Hur delar de batteriets spänning?')

    R_ = 40
    Ptot = 230 ** 2 / 60
    Pser = (230 / 60) ** 2 * R_
    uppgift('8.772', 3, F_IU,
            'Ett element har tre likadana värmeslingor på 40 Ω vardera och är kopplat till 230 V. Slingorna R₂ och R₃ är '
            'seriekopplade, och R₁ är parallellkopplad med dem.',
            krets(Par(R('R₁', '40 Ω'), Ser(R('R₂', '40 Ω'), R('R₃', '40 Ω'))), '230 V', 'Slingan R₁ parallellt med R₂ och R₃ i serie, alla 40 Ω, 230 V'),
            'Hur stor effekt utvecklas i slingan R₂?', (230 / 80) ** 2 * 40, 'W',
            [givet('U=230\\ \\mathrm V', 'R_1=R_2=R_3=40\\ \\Omega', sokt='effekten i R₂'),
             li('Grenen med R₂ och R₃ har hela spänningen. Seriekoppling: \\(R=R_2+R_3\\)', mt('R_{23}=40+40=80' + OHM)),
             li(f'{OHMS_LAG} för grenen', mt('I_{23}=\\frac{230}{80}\\approx2{,}875' + A)),
             li('Effekt: \\(P=RI^2\\)', mt('P_2=40\\cdot2{,}875^2\\approx330' + W))],
            '3,3·10² W.', 'Vilken spänning ligger över grenen där R₂ sitter? Behövs R₁?')

    uppgift('8.773', 3, F_RES,
            'En resistor R₁ = 10 Ω är seriekopplad med en parallellkoppling av R₂ = 15 Ω och en okänd resistor Rₓ. Hela '
            'kopplingen ska ha ersättningsresistansen 16 Ω.',
            krets(Ser(R('R₁', '10 Ω'), Par(R('R₂', '15 Ω'), R('Rₓ', '?'))), '', 'R₁ = 10 Ω i serie med 15 Ω parallellt med okänd Rₓ', batteri=False),
            'Hur stor ska Rₓ vara?', 10, 'Ω',
            [givet('R_1=10\\ \\Omega', 'R_2=15\\ \\Omega', 'R=16\\ \\Omega', sokt='\\(R_x\\)'),
             li(f'{SERIE} ger parallelldelens resistans', mt('R_p=16-10=6{,}0' + OHM)),
             li(PARALLELL + ' löses för den okända', mt('\\frac{1}{R_x}=\\frac{1}{6{,}0}-\\frac{1}{15}=\\frac{5-2}{30}=\\frac{1}{10}'), mt('R_x=10' + OHM)),
             li('Kontroll', mt('10+\\left(\\frac{1}{15}+\\frac{1}{10}\\right)^{-1}=10+6{,}0=16' + OHM))],
            '10 Ω.', 'Vilken resistans måste parallellkopplingen ha för att hela kopplingen ska bli 16 Ω?')

    I = 6.0 / (3 + 3)
    uppgift('8.774', 3, F_IU,
            'I ett dockskåp lyser fyra lampor från ett batteri på 6,0 V. Taklampan L₁ har resistansen 3,0 Ω, och de tre '
            'vägglamporna L₂, L₃ och L₄ har 9,0 Ω vardera.',
            krets(Ser(L('L₁', '3,0 Ω'), Par(L('L₂', '9,0 Ω'), L('L₃', '9,0 Ω'), L('L₄', '9,0 Ω'))), '6,0 V', 'Taklampa 3,0 Ω i serie med tre parallellkopplade vägglampor på 9,0 Ω'),
            None, None, None, None, None, 'Rita om kretsen med parallellkopplingen ersatt av en lampa.', niva=('C', '(1/1/0)'),
            delar=[
                dict(fraga='Bestäm lampkopplingens ersättningsresistans.', svar=6.0, enhet='Ω', tn=2,
                     steg=[givet('R_1=3{,}0\\ \\Omega', 'R_2=R_3=R_4=9{,}0\\ \\Omega', sokt='ersättningsresistansen'),
                           li('Tre lika parallellkopplade lampor ger en tredjedel av resistansen', mt('R_p=\\frac{9{,}0}{3}=3{,}0' + OHM)),
                           li(SERIE, mt('R=3{,}0+3{,}0=6{,}0' + OHM))],
                     svartext='6,0 Ω.', ledtrad='Vilka lampor delar på strömmen?'),
                dict(fraga='Hur stor ström går genom vägglampan L₂?', svar=1 / 3, enhet='A', tn=3,
                     mellan='Lampkopplingens ersättningsresistans är 6,0 Ω.',
                     steg=[li(f'{OHMS_LAG} för hela kretsen', mt('I=\\frac{6{,}0}{6{,}0}=1{,}0' + A)),
                           li('Strömmen delar sig lika mellan de tre likadana vägglamporna', mt('I_2=\\frac{1{,}0}{3}\\approx0{,}33' + A))],
                     svartext='0,33 A.', ledtrad='Hur stor ström går genom taklampan, och hur delar den sig sedan?')])


# ================================================================ nivå 4–5: nästlade kopplingar och problemlösning
def niva45():
    # 2 + (6 || (4 + (4||4))) vid 10 V
    uppgift('8.775', 4, F_IU, 'Kopplingen har tre nivåer: en parallellkoppling inne i en gren, som i sin tur är parallellkopplad med R₂. Batteriet ger 10 V.',
            krets(Ser(R('R₁', '2,0 Ω'), Par(R('R₂', '6,0 Ω'), Ser(R('R₃', '4,0 Ω'), Par(R('R₄', '4,0 Ω'), R('R₅', '4,0 Ω'))))), '10 V',
                  'R₁ = 2,0 Ω i serie med R₂ = 6,0 Ω parallellt med en gren där R₃ = 4,0 Ω ligger i serie med två parallellkopplade 4,0 Ω'),
            'Bestäm spänningen över R₃.', 4.0, 'V',
            [givet('U=10\\ \\mathrm V', 'R_1=2{,}0\\ \\Omega', 'R_2=6{,}0\\ \\Omega', 'R_3=R_4=R_5=4{,}0\\ \\Omega', sokt='spänningen \\(U_3\\)'),
             li('Ersättningsresistans inifrån och ut: \\(R=R_1+\\left(\\frac{1}{R_2}+\\frac{1}{R_3+R_{45}}\\right)^{-1}\\)',
                mt('R_{45}=\\frac{4{,}0}{2}=2{,}0' + OHM), mt('R_{345}=4{,}0+2{,}0=6{,}0' + OHM),
                mt('R_p=\\frac{6{,}0}{2}=3{,}0' + OHM), mt('R=2{,}0+3{,}0=5{,}0' + OHM)),
             li(f'{OHMS_LAG} för hela kretsen och för parallelldelen', mt('I=\\frac{10}{5{,}0}=2{,}0' + A), mt('U_p=3{,}0\\cdot2{,}0=6{,}0' + V)),
             li('Grenen med R₃: \\(I_{345}=\\frac{U_p}{R_{345}}\\) och \\(U_3=R_3I_{345}\\)', mt('I_{345}=\\frac{6{,}0}{6{,}0}=1{,}0' + A), mt('U_3=4{,}0\\cdot1{,}0=4{,}0' + V))],
            '4,0 V.', 'Förenkla inifrån: den innersta parallellkopplingen först.', formaga=('procedur', 'problemlösning'))

    rx = 1 / (1 / 8 - 1 / 20)
    uppgift('8.776', 4, F_IU,
            'R₁ = 12 Ω är seriekopplad med en parallellkoppling av R₂ = 20 Ω och en okänd resistor Rₓ. Batteriets '
            'spänning är 18 V, och amperemetern i huvudledningen visar 0,90 A.',
            krets(Ser(M('A'), R('R₁', '12 Ω'), Par(R('R₂', '20 Ω'), R('Rₓ', '?'))), '18 V', 'Amperemeter och R₁ = 12 Ω i serie med 20 Ω parallellt med okänd Rₓ, 18 V'),
            'Bestäm Rₓ.', rx, 'Ω',
            [givet('U=18\\ \\mathrm V', 'I=0{,}90\\ \\mathrm A', 'R_1=12\\ \\Omega', 'R_2=20\\ \\Omega', sokt='\\(R_x\\)'),
             li(f'{OHMS_LAG} ger hela kretsens resistans', mt('R=\\frac{18}{0{,}90}=20' + OHM)),
             li(SERIE, mt('R_p=20-12=8{,}0' + OHM)),
             li(PARALLELL + ' löses för \\(R_x\\)', mt('\\frac{1}{R_x}=\\frac{1}{8{,}0}-\\frac{1}{20}=\\frac{3}{40}\\quad\\Rightarrow\\quad R_x=\\frac{40}{3}\\approx13' + OHM))],
            '13 Ω.', 'Amperemetern och batteriet ger hela kretsens resistans. Vad blir kvar för parallellkopplingen?',
            formaga=('problemlösning',))

    uppgift('8.777', 4, F_IU,
            'Batteriets spänning är 12 V. En voltmeter mäter spänningen över R₂. Brytaren i grenen med R₃ är först öppen '
            'och sluts sedan.',
            krets(Ser(R('R₁', '6,0 Ω'), Par(R('R₂', '12 Ω'), Ser(R('R₃', '12 Ω'), S('', oppen=True)), M('V'))), '12 V',
                  'R₁ = 6,0 Ω i serie med R₂ = 12 Ω, R₃ = 12 Ω med brytare och en voltmeter parallellt'),
            'Hur mycket minskar voltmeterns utslag när brytaren sluts?', 2.0, 'V',
            [givet('U=12\\ \\mathrm V', 'R_1=6{,}0\\ \\Omega', 'R_2=R_3=12\\ \\Omega', sokt='minskningen av voltmeterns utslag'),
             li('Brytaren öppen: R₁ och R₂ i serie delar 12 V', mt('I=\\frac{12}{6{,}0+12}=\\frac{2}{3}' + A + ',\\quad U_2=12\\cdot\\frac{2}{3}=8{,}0' + V)),
             li('Brytaren sluten: R₂ och R₃ parallellt', mt('R_p=\\frac{12}{2}=6{,}0' + OHM + ',\\quad I=\\frac{12}{6{,}0+6{,}0}=1{,}0' + A),
                mt('U_p=6{,}0\\cdot1{,}0=6{,}0' + V)),
             li('Skillnad', mt('8{,}0-6{,}0=2{,}0' + V))],
            '2,0 V.', 'Parallellkopplingen får mindre resistans när brytaren sluts. Hur delas då 12 V mellan R₁ och resten?',
            formaga=('procedur', 'resonemang'))

    uppgift('8.778', 4, F_IU,
            'En lampa L är märkt 6,0 V och 0,50 A. Den är parallellkopplad med en resistor R₁ = 24 Ω. Paret '
            'seriekopplas med en resistor Rₓ till ett batteri på 9,0 V.',
            krets(Ser(R('Rₓ', '?'), Par(L('L'), R('R₁', '24 Ω'))), '9,0 V', 'Okänd Rₓ i serie med lampan L parallellt med R₁ = 24 Ω, 9,0 V'),
            'Hur stor ska Rₓ vara för att lampan ska lysa normalt?', 4.0, 'Ω',
            [givet('U=9{,}0\\ \\mathrm V', 'U_L=6{,}0\\ \\mathrm V', 'I_L=0{,}50\\ \\mathrm A', 'R_1=24\\ \\Omega', sokt='\\(R_x\\)'),
             li('Lampan och R₁ har samma spänning, 6,0 V. Ohms lag för R₁', mt('I_1=\\frac{6{,}0}{24}=0{,}25' + A)),
             li(f'{KNUT}', mt('I=0{,}50+0{,}25=0{,}75' + A)),
             li('Spänningen över Rₓ och Ohms lag', mt('U_x=9{,}0-6{,}0=3{,}0' + V), mt('R_x=\\frac{3{,}0}{0{,}75}=4{,}0' + OHM))],
            '4,0 Ω.', 'Lampan ska ha 6,0 V. Vad betyder det för R₁, och hur stor ström går då genom Rₓ?',
            formaga=('problemlösning',))

    uppgift('8.779', 4, F_IU,
            'Tre likadana lampor lyser i kretsen. Glödtråden i L₃ går sönder.',
            krets(Ser(L('L₁'), Par(L('L₂'), L('L₃'))), '6,0 V', 'L₁ i serie med parallellkopplade L₂ och L₃'),
            'Hur ändras ljuset från L₁ och L₂?', None, None,
            [li('Ersättningsresistansen ökar', p('Med en lampas resistans R är kopplingen först \\(R+R/2=1{,}5R\\). Utan L₃ blir den \\(2R\\).')),
             li(OHMS_LAG + ' för hela kretsen',
                p('Strömmen genom L₁ minskar från \\(\\frac{U}{1{,}5R}\\) till \\(\\frac{U}{2R}\\). L₁ lyser svagare.')),
             li('Spänningen över L₂', p('Förut fick L₂ en tredjedel av \\(U\\) (\\(\\frac{R/2}{1{,}5R}\\)), nu hälften. L₂ lyser starkare.'))],
            'L₁ lyser svagare och L₂ starkare.', 'Jämför spänningen över L₂ före och efter: hur stor del av batteriets spänning får den?',
            formaga=('resonemang',),
            alternativ=[('L₁ svagare och L₂ starkare', True, 'Strömmen genom L₁ minskar, men L₂ får större del av spänningen.'),
                        ('Båda lyser svagare', False, 'L₂ får nu större del av spänningen än förut: hälften i stället för en tredjedel.'),
                        ('Båda lyser starkare', False, 'Totala resistansen ökar, så strömmen genom L₁ minskar.'),
                        ('L₁ oförändrad och L₂ starkare', False, 'Strömmen genom L₁ beror på hela kopplingens resistans, som ökar.')])

    uppgift('8.780', 5, F_IU,
            'R₁ = 10 Ω ligger i serie med en parallellkoppling. Den ena grenen är R₂ = 30 Ω, den andra är en okänd '
            'resistor R₃ i serie med R₄ = 10 Ω. Batteriets spänning är 20 V, och en voltmeter över R₄ visar 4,0 V.',
            krets(Ser(R('R₁', '10 Ω'), Par(R('R₂', '30 Ω'), Ser(R('R₃', '?'), Par(R('R₄', '10 Ω'), M('V'))))), '20 V',
                  'R₁ = 10 Ω i serie med R₂ = 30 Ω parallellt med okänd R₃ i serie med R₄ = 10 Ω, voltmeter över R₄'),
            'Bestäm R₃.', 20, 'Ω',
            [givet('U=20\\ \\mathrm V', 'R_1=10\\ \\Omega', 'R_2=30\\ \\Omega', 'R_4=10\\ \\Omega', 'U_4=4{,}0\\ \\mathrm V', sokt='\\(R_3\\)'),
             li('Ohms lag för R₄ ger strömmen i grenen', mt('I_b=\\frac{4{,}0}{10}=0{,}40' + A)),
             li('Uttryck spänningen över parallelldelen och huvudströmmen med \\(R_3\\)',
                mt('U_p=0{,}40\\,(R_3+10)'), mt('I=\\frac{U_p}{30}+0{,}40')),
             li('Spänningslagen: \\(U=R_1I+U_p\\)',
                mt('20=10\\left(\\frac{0{,}40(R_3+10)}{30}+0{,}40\\right)+0{,}40(R_3+10)'),
                mt('16=(R_3+10)\\left(\\frac{4}{30}+0{,}40\\right)=(R_3+10)\\cdot\\frac{16}{30}'),
                mt('R_3+10=30\\quad\\Rightarrow\\quad R_3=20' + OHM)),
             li('Kontroll', p('Grenen har 30 Ω och 0,40 A, alltså 12 V, och R₂ får 0,40 A. Huvudströmmen 0,80 A ger 8,0 V över R₁, och 8,0 + 12 = 20 V.'))],
            '20 Ω.', 'Börja med det du vet säkert: strömmen genom R₄. Uttryck sedan resten med R₃.',
            formaga=('problemlösning',))

    def up(n):
        return 12 * (24 / n) / (4 + 24 / n)
    nmax = max(n for n in range(1, 20) if up(n) >= 9.0)
    uppgift('8.781', 5, F_IU,
            'Ett antal likadana lampor på 24 Ω vardera ska parallellkopplas och matas från ett batteri på 12 V genom en '
            'förkopplingsresistor på 4,0 Ω. Spänningen över lamporna får inte bli lägre än 9,0 V.',
            krets(Ser(R('R', '4,0 Ω'), Par(L('L₁', '24 Ω'), L('L₂', '24 Ω'), L('…'))), '12 V', 'Förkopplingsresistor 4,0 Ω i serie med flera parallellkopplade lampor på 24 Ω'),
            'Hur många lampor kan kopplas in som mest?', nmax, None,
            [givet('U=12\\ \\mathrm V', 'R=4{,}0\\ \\Omega', 'R_L=24\\ \\Omega', 'U_p\\ge9{,}0\\ \\mathrm V', sokt='största antalet lampor \\(n\\)'),
             li('Spänningsdelning: \\(U_p=U\\cdot\\frac{R_p}{R+R_p}\\) med \\(R_p=\\frac{24}{n}\\)',
                mt('U_p=12\\cdot\\frac{24/n}{4{,}0+24/n}=\\frac{288}{4n+24}')),
             li('Villkoret \\(U_p\\ge9{,}0\\ \\mathrm V\\)', mt('\\frac{288}{4n+24}\\ge9\\quad\\Rightarrow\\quad 288\\ge36n+216\\quad\\Rightarrow\\quad n\\le2')),
             li('Kontroll', p('Två lampor: \\(R_p=12\\ \\Omega\\), \\(U_p=12\\cdot\\frac{12}{16}=9{,}0\\) V. Tre lampor: \\(R_p=8{,}0\\ \\Omega\\), \\(U_p=8{,}0\\) V, för lite.'))],
            '2 lampor.', 'Fler parallellkopplade lampor ger mindre resistans. Vad händer då med spänningen över lamporna?',
            formaga=('problemlösning', 'resonemang'))


def main():
    niva1()
    niva2()
    niva3()
    niva45()
    nya = [objekt(u) for u in UPPG]
    src, bank = B.las(ROOT / 'uppgifter.js')
    ids = {q['id'] for q in bank}
    for q in nya:
        assert q['id'] not in ids, q['id']
    sista = max(i for i, q in enumerate(bank) if q.get('kap') == 8)
    spannen = B.spann(src)
    slut = spannen[sista][1]
    prefix = B._prefix(src, spannen[sista][0])
    ny_src = src[:slut] + ''.join(',\n' + B._dump(q, prefix) for q in nya) + src[slut:]
    ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    assert len(ny_bank) == len(bank) + len(nya)
    for q in nya:
        print(q['id'], q['traningsniva'], q['niva'], q['familj'][:12], q['rättSvar'])
    if SKRIV:
        B.skriv(ROOT / 'uppgifter.js', ny_src)
    return nya


if __name__ == '__main__':
    main()
