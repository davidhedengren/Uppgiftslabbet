"""Fy1 newton2: kopplade klossar med snören och trissor, 4.979–4.1004 (2026-11-20).

Uppdrag: lägg in uppgifterna ur lärarens häfte ”Färdighetsträning – Newtons andra lag” (4.979–4.993, samma
uppställningar med m = 1,0 kg och F = 10 N) och fler liknande på olika nivåer (4.994–4.1004). Varje uppgift är
fristående: massor, krafter och friktion står i texten, och figuren visar uppställningen.

Facit följer agent/FACITMALL.md: Givet och sökt, friläggning, Newtons andra lag i rubriken, insättning och svarsrad.
Rubrikerna är skrivna för varje uppgift. Delkort börjar med samma inledning och figur och får behövda mellanresultat
(accelerationen med fyra värdesiffror) i frågan.

  python tools/bygg-fy1-kopplade-klossar-2026-11-20.py [--skriv]
"""
import json
import math
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402
from newton2_klossar import Kropp, System, figur, frilagg_kedja, Rit, RED, KRAFTFARG, G  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKRIV = '--skriv' in sys.argv
g = G
FAMILJ = 'Kopplade klossar med snören och trissor'
NYCKEL = 'newton2__kopplade_klossar_med_snoren_och_trissor'
BOK = 'abcdefgh'


# ================================================================ text och tal
def sig(v, n):
    """v med n värdesiffror som text med decimalkomma (10 → 10, 2,333 → 2,3, 2655 → 2 700)."""
    if v == 0:
        return '0'
    e = math.floor(math.log10(abs(v)))
    d = n - 1 - e
    if d > 0:
        txt = f'{round(v, d):.{d}f}'
    else:
        txt = str(int(round(v, d)))
        if abs(int(txt)) >= 10000:
            txt = f'{int(txt):,}'.replace(',', ' ')
    return txt.replace('.', ',').replace('-', '−')


def tx(v, n):
    """Samma tal i LaTeX."""
    return sig(v, n).replace(',', '{,}').replace(' ', '\\,').replace('−', '-')


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


def huvudfacit(delar):
    return ('<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{BOK[i]})</span><div class="facit-arbete">{d}</div></div>'
        for i, d in enumerate(delar)) + '</div>')


def fig(html):
    return f'<span class="fig">{html}</span>'


def fbd(sys_, pid, endast=None, namn=None):
    titel = 'Friläggning av klossen' if endast and len(endast) == 1 else 'Friläggning av klossarna'
    return '<div class="facit-figur">' + frilagg_kedja(sys_, pid, namn, titel, endast) + '</div>'


NEWTON = 'F_{\\text{res}}=ma'
NEWTON_TOT = 'F_{\\text{res}}=m_{\\text{tot}}\\,a'
UNIT_A = '\\ \\mathrm{m/s^2}'
UNIT_N = '\\ \\mathrm N'


def kg(k):
    return Kropp(k, 'B', etikett=f'{sig(k, 2)} kg')


def K(k, plats, fr=0.0, et=None):
    return Kropp(k, plats, fr, 'f', et or f'{sig(k, 2)} kg')


# ================================================================ uppgiftsbyggare
UPPG = []
ENKLA_A = {'4.984', '4.986', '4.988', '4.991'}


def uppgift(uid, intro, figurhtml, delar, ledtrad, formaga=('modellering', 'procedur'), mr=True):
    """delar: lista av dict(fraga, mellan, svar, enhet, siffror, niva, tn, poang, steg, steg_kort, svartext, ledtrad)."""
    if uid in ENKLA_A:
        # Accelerationen är ett steg med hela systemet (skillnad i tyngd delat med total massa): E, träningsnivå 2.
        delar[0].update(niva='E', tn=2, poang='(1/0/0)')
    UPPG.append(dict(id=uid, intro=intro, fig=figurhtml, delar=delar, ledtrad=ledtrad, formaga=list(formaga), mr=mr))


def poangsumma(ps):
    t = [0, 0, 0]
    for x in ps:
        for i, v in enumerate(re.findall(r'\d+', x)):
            t[i] += int(v)
    return f'({t[0]}/{t[1]}/{t[2]})'


def niva_max(ns):
    return 'A' if 'A' in ns else 'C' if 'C' in ns else 'E'


def tol(v, n):
    e = math.floor(math.log10(abs(v)))
    return round(0.5 * 10 ** (e - n + 1), 12)


def objekt(u):
    intro = u['intro']
    fg = fig(u['fig'])
    spelintro = intro + fg
    d = u['delar']
    q = {'id': u['id'], 'kap': 4, 'omr': 'newton2'}
    q['niva'] = niva_max([x['niva'] for x in d])
    q['poang'] = poangsumma([x['poang'] for x in d])
    if len(d) == 1:
        x = d[0]
        q['t'] = spelintro + p(x['fraga'])
        q['s'] = facit(x['steg'], x['svartext'])
    else:
        q['t'] = spelintro + '<ol type="a">' + ''.join(f'<li>{x["fraga"]}</li>' for x in d) + '</ol>'
        q['s'] = huvudfacit([delfacit(x['steg'], x['svartext']) for x in d])
    q['familj'] = FAMILJ
    q['familjNyckel'] = NYCKEL
    q['formaga'] = u['formaga']
    q['ledtrad'] = p(u['ledtrad'])
    q['traningsniva'] = max(x['tn'] for x in d)
    q['arbetsinsats'] = 1 if q['traningsniva'] <= 2 else 2 if q['traningsniva'] <= 4 else 3
    q['miniräknare'] = u['mr']
    q['geogebra'] = False
    q['spel'] = True
    q['självrättning'] = True
    if len(d) == 1:
        x = d[0]
        q['svarstyp'] = 'numeriskt' if x.get('format', 'numeriskt') == 'numeriskt' else 'uttryck'
        q['rättSvar'] = x['svar']
        q['svarFormat'] = x.get('format', 'numeriskt')
        if q['svarFormat'] == 'numeriskt':
            q['tolerans'] = tol(x['svar'], x['siffror'])
            q['svarEnhet'] = x['enhet']
            q['svarVardesiffror'] = x['siffror']
        else:
            q['tolerans'] = None
    else:
        q['svarstyp'] = 'flera_delar'
        q['rättSvar'] = [x['svar'] for x in d]
        q['svarFormat'] = [x.get('format', 'numeriskt') for x in d]
        q['tolerans'] = [tol(x['svar'], x['siffror']) if x.get('format', 'numeriskt') == 'numeriskt' else None for x in d]
        q['svarEnhet'] = [x.get('enhet') for x in d]
        if all(x.get('format', 'numeriskt') == 'numeriskt' for x in d):
            q['svarVardesiffror'] = [x['siffror'] for x in d]
        q['svarsstruktur'] = 'ordnad'
        q['svarEtiketter'] = [BOK[i] for i in range(len(d))]
        q['spelDelning'] = 'deluppgifter'
        q['spelIntro'] = spelintro
        q['spelDelar'] = []
        for i, x in enumerate(d):
            kortt = spelintro + (p(x['mellan']) if x.get('mellan') else '') + p(x['fraga'])
            q['spelDelar'].append({
                'etikett': BOK[i], 'fraga': x['fraga'], 't': kortt,
                's': '<div class="facit-v2 facit-stegvis"><div class="spel-en-del">'
                     + delfacit(x.get('steg_kort', x['steg']), x['svartext']) + '</div></div>',
                'ledtrad': p(x['ledtrad']), 'niva': x['niva'], 'traningsniva': x['tn'],
                'arbetsinsats': 1 if x['tn'] <= 2 else 2 if x['tn'] <= 4 else 3, 'poang': x['poang']})
    return q


def del_(fraga, svar, enhet, siffror, niva, tn, poang, steg, svartext, ledtrad, mellan='', steg_kort=None, **kw):
    d = dict(fraga=fraga, svar=svar, enhet=enhet, siffror=siffror, niva=niva, tn=tn, poang=poang, steg=steg,
             svartext=svartext, ledtrad=ledtrad, mellan=mellan)
    if steg_kort is not None:
        d['steg_kort'] = steg_kort
    d.update(kw)
    return d


def acc_kalla(a, kort):
    """Hur accelerationen från en tidigare del nämns i huvudfacit respektive på delkortet."""
    return (p(f'Accelerationen är given: \\(a={tx(a, 4)}{UNIT_A}\\).') if kort
            else p(f'Accelerationen från a): \\(a\\approx{tx(a, 4)}{UNIT_A}\\).'))


def mellan_a(a, subjekt='Klossarna'):
    return f'{subjekt} accelererar med {sig(a, 4)} m/s².'


# ================================================================ 4.979–4.993: häftets uppgifter
def hafte():
    # ---- 4.979 (häftet 1): en kloss
    s = System(bord=[kg(1.0)], F=10, golv=True)
    a, _ = s.los()
    uppgift('4.979',
            p('En kloss med massan 1,0 kg ligger på ett horisontellt golv. Klossen dras åt höger med en horisontell '
              'kraft på 10 N. Bortse från friktion.'),
            figur(s, 'k979', 'En kloss på 1,0 kg dras åt höger med kraften 10 N.', Ftext='10 N'),
            [del_('Hur stor acceleration får klossen?', a, 'm/s²', 2, 'E', 1, '(1/0/0)',
                  [li(f'Newtons andra lag: \\({NEWTON}\\)',
                      p('Golvet är friktionsfritt, så dragkraften är den resulterande kraften.'),
                      mt(f'a=\\frac{{F}}{{m}}=\\frac{{10}}{{1{{,}}0}}=10{UNIT_A}'))],
                  '10 m/s².', '')],
            'Vilken kraft är den resulterande kraften när golvet saknar friktion?')

    # ---- 4.980 (häftet 2): två klossar, kraften på den tunga
    s = System(bord=[kg(1.0), kg(2.0)], F=10, golv=True)
    a, (S,) = s.los()
    intro = p('Två klossar med massorna 1,0 kg och 2,0 kg ligger på ett horisontellt golv och är sammanbundna med ett '
              'snöre. Klossen på 2,0 kg dras åt höger med en horisontell kraft på 10 N. Bortse från friktion.')
    stegS = lambda kort: [
        li('Frilägg klossen på 1,0 kg', fbd(s, 'f980b' + ('k' if kort else ''), [0]),
           p('Lodrätt tar normalkraften och tyngdkraften ut varandra. Vågrätt verkar bara snörkraften \\(S\\).'),
           acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           mt(f'S=m_1a=1{{,}}0\\cdot{tx(a, 4)}\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.980', intro, figur(s, 'k980', 'Två sammanbundna klossar på 1,0 kg och 2,0 kg dras åt höger med 10 N.',
                                  Ftext='10 N'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'E', 2, '(1/0/0)',
                  [li('Givet och sökt', al('m_1=1{,}0\\ \\mathrm{kg}', 'm_2=2{,}0\\ \\mathrm{kg}', 'F=10\\ \\mathrm N'),
                      p('Positiv riktning åt höger. Sökt: den gemensamma accelerationen \\(a\\).')),
                   li(f'Newtons andra lag för båda klossarna tillsammans: \\({NEWTON_TOT}\\)',
                      p('Snörkraften drar den ena klossen framåt och den andra bakåt lika mycket, så den tar ut sig. '
                        'Bara \\(F\\) driver klossarna.'),
                      mt(f'a=\\frac{{F}}{{m_1+m_2}}=\\frac{{10}}{{1{{,}}0+2{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Se de två klossarna som en enda kropp. Vilken yttre kraft driver den?'),
             del_('Hur stor är kraften i snöret mellan klossarna?', S, 'N', 2, 'C', 3, '(0/1/0)', stegS(False),
                  f'{sig(S, 2)} N.', 'Frilägg den kloss som bara har en vågrät kraft.', mellan=mellan_a(a),
                  steg_kort=stegS(True))],
            'Börja med hela systemet och frilägg sedan en kloss i taget.')

    # ---- 4.981 (häftet 3): tre klossar
    s = System(bord=[kg(1.0), kg(2.0), kg(3.0)], F=10, golv=True)
    a, (S1, S2) = s.los()
    intro = p('Tre klossar med massorna 1,0 kg, 2,0 kg och 3,0 kg ligger i en rad på ett horisontellt golv och är '
              'sammanbundna med snören. Klossen på 3,0 kg dras åt höger med en horisontell kraft på 10 N. Bortse från '
              'friktion. Snöret mellan klossarna på 1,0 kg och 2,0 kg kallas \\(S_1\\) och snöret mellan klossarna på '
              '2,0 kg och 3,0 kg kallas \\(S_2\\).')
    s1 = lambda kort: [
        li('Frilägg klossen på 1,0 kg', fbd(s, 'f981b' + ('k' if kort else ''), [0]),
           p('Bara snörkraften \\(S_1\\) drar klossen framåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           mt(f'S_1=1{{,}}0\\cdot{tx(a, 4)}\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Se klossarna på 1,0 kg och 2,0 kg som en kropp', fbd(s, 'f981c' + ('k' if kort else ''), [0, 1]),
           p('Snöret \\(S_1\\) ligger inuti den kroppen. Bara \\(S_2\\) drar den framåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för de två klossarna: \\({NEWTON}\\)',
           mt(f'S_2=(1{{,}}0+2{{,}}0)\\cdot{tx(a, 4)}\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.981', intro, figur(s, 'k981', 'Tre klossar på 1,0 kg, 2,0 kg och 3,0 kg i rad dras åt höger med 10 N.',
                                  Ftext='10 N'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'E', 2, '(1/0/0)',
                  [li('Givet och sökt', al('m_1=1{,}0\\ \\mathrm{kg},\\ m_2=2{,}0\\ \\mathrm{kg},\\ m_3=3{,}0\\ \\mathrm{kg}',
                                           'F=10\\ \\mathrm N'),
                      p('Positiv riktning åt höger. Sökt: den gemensamma accelerationen.')),
                   li(f'Newtons andra lag för alla tre klossarna: \\({NEWTON_TOT}\\)',
                      p('Snörkrafterna är inre krafter och tar ut varandra.'),
                      mt(f'a=\\frac{{10}}{{1{{,}}0+2{{,}}0+3{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Hur stor är den sammanlagda massan som kraften 10 N ska accelerera?'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 3, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Vilken kloss påverkas bara av \\(S_1\\) i vågrät led?', mellan=mellan_a(a), steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 3, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  '\\(S_2\\) drar fler än en kloss. Vilka?', mellan=mellan_a(a), steg_kort=s2(True))],
            'Hela systemet ger accelerationen. Snörkraften i ett snöre ger det som finns bakom snöret samma acceleration.')

    # ---- 4.982 (häftet 4): en kloss med friktion
    s = System(bord=[K(1.0, 'B', 1.0)], F=10, golv=True)
    a, _ = s.los()
    uppgift('4.982',
            p('En kloss med massan 1,0 kg dras åt höger längs ett horisontellt golv med en horisontell kraft på 10 N. '
              'Friktionskraften på klossen är 1,0 N.'),
            figur(s, 'k982', 'En kloss på 1,0 kg dras åt höger med 10 N på ett golv med friktion.', Ftext='10 N'),
            [del_('Hur stor acceleration får klossen?', a, 'm/s²', 2, 'E', 2, '(1/0/0)',
                  [li('Resulterande kraft: dragkraften minus friktionskraften',
                      p('Friktionskraften verkar mot rörelsen, alltså åt vänster.'),
                      mt('F_{\\text{res}}=10-1{,}0=9{,}0\\ \\mathrm N')),
                   li(f'Newtons andra lag: \\({NEWTON}\\)', mt(f'a=\\frac{{9{{,}}0}}{{1{{,}}0}}=9{{,}}0{UNIT_A}'))],
                  '9,0 m/s².', '')],
            'Åt vilket håll verkar friktionskraften, och hur stor blir då den resulterande kraften?')

    # ---- 4.983 (häftet 5): två klossar med olika friktion
    s = System(bord=[K(1.0, 'B', 1.0), K(2.0, 'B', 2.0)], F=10, golv=True)
    a, (S,) = s.los()
    intro = p('Två klossar med massorna 1,0 kg och 2,0 kg ligger på ett horisontellt golv och är sammanbundna med ett '
              'snöre. Klossen på 2,0 kg dras åt höger med en horisontell kraft på 10 N. Friktionskraften är 1,0 N på '
              'klossen på 1,0 kg och 2,0 N på klossen på 2,0 kg.')
    stS = lambda kort: [
        li('Frilägg klossen på 1,0 kg', fbd(s, 'f983b' + ('k' if kort else ''), [0]),
           p('Snörkraften \\(S\\) drar framåt och friktionskraften 1,0 N bromsar.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al('S-1{,}0=1{,}0\\cdot ' + tx(a, 4), f'S={tx(a, 4)}+1{{,}}0\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.983', intro, figur(s, 'k983', 'Två sammanbundna klossar på 1,0 kg och 2,0 kg dras åt höger med 10 N på ett '
                                  'golv med friktion.', Ftext='10 N'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('m_1=1{,}0\\ \\mathrm{kg},\\ f_1=1{,}0\\ \\mathrm N',
                                           'm_2=2{,}0\\ \\mathrm{kg},\\ f_2=2{,}0\\ \\mathrm N', 'F=10\\ \\mathrm N'),
                      p('Positiv riktning åt höger. Sökt: den gemensamma accelerationen.')),
                   li(f'Newtons andra lag för båda klossarna: \\({NEWTON_TOT}\\)',
                      p('Dragkraften driver framåt. Båda friktionskrafterna bromsar. Snörkraften tar ut sig.'),
                      mt(f'a=\\frac{{10-1{{,}}0-2{{,}}0}}{{1{{,}}0+2{{,}}0}}=\\frac{{7{{,}}0}}{{3{{,}}0}}\\approx'
                         f'{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Vilka krafter driver och vilka bromsar hela systemet?'),
             del_('Hur stor är kraften i snöret mellan klossarna?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False),
                  f'{sig(S, 2)} N.', 'Frilägg den lätta klossen. Glöm inte dess friktion.', mellan=mellan_a(a),
                  steg_kort=stS(True))],
            'Räkna först accelerationen för hela systemet och frilägg sedan en kloss.')

    # ---- 4.984 (häftet 6): Atwood m, 2m
    s = System(vanster=[K(1.0, 'V')], hoger=[K(2.0, 'H')])
    a, (S,) = s.los()
    intro = p('Två klossar med massorna 1,0 kg och 2,0 kg hänger i var sin ände av ett snöre som går över en trissa. '
              'Klossarna släpps från stillastående. Bortse från snörets och trissans massa och från friktion i trissan.')
    stS = lambda kort: [
        li('Frilägg den lätta klossen', fbd(s, 'f984b' + ('k' if kort else ''), [0]),
           p('Klossen på 1,0 kg accelererar uppåt. Snörkraften drar uppåt och tyngdkraften nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al(f'S-mg=ma', f'S=m(g+a)=1{{,}}0\\cdot(9{{,}}82+{tx(a, 4)})\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.984', intro, figur(s, 'k984', 'Klossar på 1,0 kg och 2,0 kg hänger över en trissa.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('m_1=1{,}0\\ \\mathrm{kg}', 'm_2=2{,}0\\ \\mathrm{kg}'),
                      p('Den tyngre klossen sjunker. Positiv riktning: nedåt för klossen på 2,0 kg och uppåt för '
                        'klossen på 1,0 kg. Sökt: accelerationen.')),
                   li(f'Newtons andra lag längs snöret: \\({NEWTON_TOT}\\)',
                      p('Skillnaden mellan tyngdkrafterna driver systemet. Snörkraften tar ut sig.'),
                      mt(f'a=\\frac{{(2{{,}}0-1{{,}}0)\\cdot9{{,}}82}}{{1{{,}}0+2{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Vilken del av tyngdkrafterna driver systemet, och hur stor massa ska den accelerera?'),
             del_('Hur stor är snörkraften?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False), f'{sig(S, 2)} N.',
                  'Klossen på 1,0 kg accelererar uppåt. Ska snörkraften då vara större eller mindre än dess tyngd?',
                  mellan=mellan_a(a), steg_kort=stS(True))],
            'Frilägg båda klossarna och välj positiv riktning medurs runt trissan.')

    # ---- 4.985 (häftet 7): Atwood m mot 2m + 4m
    s = System(vanster=[K(1.0, 'V')], hoger=[K(2.0, 'H'), K(4.0, 'H')])
    a, (S1, S2) = s.los()
    intro = p('Ett snöre går över en trissa. I den vänstra änden hänger en kloss med massan 1,0 kg. I den högra änden '
              'hänger en kloss med massan 2,0 kg, och under den hänger en kloss med massan 4,0 kg i ett annat snöre. '
              'Klossarna släpps från stillastående. Bortse från snörenas och trissans massa och från friktion i '
              'trissan. Snöret över trissan kallas \\(S_1\\) och snöret mellan klossarna på 2,0 kg och 4,0 kg '
              'kallas \\(S_2\\).')
    s1 = lambda kort: [
        li('Frilägg klossen på 1,0 kg', fbd(s, 'f985b' + ('k' if kort else ''), [0]),
           p('Den accelererar uppåt: \\(S_1\\) uppåt och tyngdkraften nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           mt(f'S_1=m(g+a)=1{{,}}0\\cdot(9{{,}}82+{tx(a, 4)})\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Frilägg den nedersta klossen på 4,0 kg', fbd(s, 'f985c' + ('k' if kort else ''), [2]),
           p('Den accelererar nedåt: tyngdkraften nedåt och \\(S_2\\) uppåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 4,0 kg: \\({NEWTON}\\)',
           al('mg-S_2=ma', f'S_2=m(g-a)=4{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.985', intro, figur(s, 'k985', 'En kloss på 1,0 kg hänger till vänster om en trissa och klossar på 2,0 kg '
                                  'och 4,0 kg under varandra till höger.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{vänster: }1{,}0\\ \\mathrm{kg}',
                                           '\\text{höger: }2{,}0\\ \\mathrm{kg}+4{,}0\\ \\mathrm{kg}=6{,}0\\ \\mathrm{kg}'),
                      p('Höger sida är tyngst och sjunker. Positiv riktning medurs runt trissan. Sökt: accelerationen.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('Snörkrafterna tar ut varandra. Skillnaden mellan tyngdkrafterna på de två sidorna driver.'),
                      mt(f'a=\\frac{{(6{{,}}0-1{{,}}0)\\cdot9{{,}}82}}{{1{{,}}0+2{{,}}0+4{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Räkna ihop massan på varje sida om trissan.'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 4, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Vilken kloss påverkas bara av \\(S_1\\) och sin tyngd?', mellan=mellan_a(a), steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 4, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  'Frilägg klossen som bara hänger i \\(S_2\\).', mellan=mellan_a(a), steg_kort=s2(True))],
            'Hela systemet har samma accelerationsstorlek. Frilägg sedan den kloss som bara har en snörkraft.')

    # ---- 4.986 (häftet 8): bord 2m, hängande m
    s = System(bord=[K(2.0, 'B')], hoger=[K(1.0, 'H')])
    a, (S,) = s.los()
    intro = p('En kloss med massan 2,0 kg ligger på ett horisontellt bord. Ett snöre går från klossen över en trissa vid '
              'bordskanten till en hängande kloss med massan 1,0 kg. Bortse från friktion och från snörets och trissans massa.')
    stS = lambda kort: [
        li('Frilägg klossen på bordet', fbd(s, 'f986b' + ('k' if kort else ''), [0]),
           p('Normalkraften och tyngdkraften tar ut varandra. Bara snörkraften drar klossen mot kanten.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 2,0 kg: \\({NEWTON}\\)',
           mt(f'S=2{{,}}0\\cdot{tx(a, 4)}\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.986', intro, figur(s, 'k986', 'En kloss på 2,0 kg på ett bord är kopplad över en trissa till en hängande '
                                  'kloss på 1,0 kg.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{på bordet: }2{,}0\\ \\mathrm{kg}', '\\text{hängande: }1{,}0\\ \\mathrm{kg}'),
                      p('Positiv riktning längs snöret: mot kanten för klossen på bordet och nedåt för den hängande. '
                        'Sökt: accelerationen.')),
                   li(f'Newtons andra lag längs snöret: \\({NEWTON_TOT}\\)',
                      p('Bara den hängande klossens tyngd driver. Klossen på bordet har ingen kraft längs snöret utom S.'),
                      mt(f'a=\\frac{{1{{,}}0\\cdot9{{,}}82}}{{2{{,}}0+1{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Vilken kraft drar hela systemet, och vilken massa ska den accelerera?'),
             del_('Hur stor är snörkraften?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False), f'{sig(S, 2)} N.',
                  'Klossen på bordet är lättast att frilägga.', mellan=mellan_a(a), steg_kort=stS(True))],
            'Frilägg klossen på bordet och den hängande klossen. De har samma accelerationsstorlek.')

    # ---- 4.987 (häftet 9): bord 2m, hängande m och 3m
    s = System(bord=[K(2.0, 'B')], hoger=[K(1.0, 'H'), K(3.0, 'H')])
    a, (S1, S2) = s.los()
    intro = p('En kloss med massan 2,0 kg ligger på ett horisontellt bord. Ett snöre \\(S_1\\) går från klossen över en '
              'trissa vid bordskanten till en hängande kloss med massan 1,0 kg. Under den hänger en kloss med massan '
              '3,0 kg i ett snöre \\(S_2\\). Bortse från friktion och från snörenas och trissans massa.')
    s1 = lambda kort: [
        li('Frilägg klossen på bordet', fbd(s, 'f987b' + ('k' if kort else ''), [0]), p('Bara \\(S_1\\) drar den framåt.'),
           acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 2,0 kg: \\({NEWTON}\\)',
           mt(f'S_1=2{{,}}0\\cdot{tx(a, 4)}\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Frilägg den nedersta klossen på 3,0 kg', fbd(s, 'f987c' + ('k' if kort else ''), [2]),
           p('Tyngdkraften drar nedåt och \\(S_2\\) uppåt. Klossen accelererar nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 3,0 kg: \\({NEWTON}\\)',
           al('mg-S_2=ma', f'S_2=3{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.987', intro, figur(s, 'k987', 'En kloss på 2,0 kg på ett bord. Över en trissa hänger klossar på 1,0 kg och '
                                  '3,0 kg under varandra.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{på bordet: }2{,}0\\ \\mathrm{kg}',
                                           '\\text{hängande: }1{,}0\\ \\mathrm{kg}+3{,}0\\ \\mathrm{kg}=4{,}0\\ \\mathrm{kg}'),
                      p('Positiv riktning längs snöret, nedåt för de hängande klossarna. Sökt: accelerationen.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('De två hängande klossarnas tyngd driver alla tre klossarna.'),
                      mt(f'a=\\frac{{4{{,}}0\\cdot9{{,}}82}}{{2{{,}}0+1{{,}}0+3{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Båda de hängande klossarna drar systemet.'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 4, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Vilken kloss påverkas bara av \\(S_1\\) längs rörelsen?', mellan=mellan_a(a), steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 4, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  'Frilägg klossen som bara hänger i \\(S_2\\).', mellan=mellan_a(a), steg_kort=s2(True))],
            'Se först alla klossar som ett system och frilägg sedan en kloss i taget.')

    # ---- 4.988 (häftet 10): bord 3m och 2m, hängande m
    s = System(bord=[K(3.0, 'B'), K(2.0, 'B')], hoger=[K(1.0, 'H')])
    a, (S1, S2) = s.los()
    intro = p('Två klossar med massorna 3,0 kg och 2,0 kg ligger på ett horisontellt bord och är sammanbundna med ett '
              'snöre \\(S_1\\). Från klossen på 2,0 kg går ett snöre \\(S_2\\) över en trissa vid bordskanten till en '
              'hängande kloss med massan 1,0 kg. Bortse från friktion och från snörenas och trissans massa.')
    s1 = lambda kort: [
        li('Frilägg klossen på 3,0 kg', fbd(s, 'f988b' + ('k' if kort else ''), [0]), p('Bara \\(S_1\\) drar den framåt.'),
           acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 3,0 kg: \\({NEWTON}\\)',
           mt(f'S_1=3{{,}}0\\cdot{tx(a, 4)}\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Frilägg den hängande klossen', fbd(s, 'f988c' + ('k' if kort else ''), [2]),
           p('Tyngdkraften nedåt och \\(S_2\\) uppåt. Klossen accelererar nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al('mg-S_2=ma', f'S_2=1{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.988', intro, figur(s, 'k988', 'Klossar på 3,0 kg och 2,0 kg på ett bord, kopplade över en trissa till en '
                                  'hängande kloss på 1,0 kg.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{på bordet: }3{,}0\\ \\mathrm{kg}+2{,}0\\ \\mathrm{kg}',
                                           '\\text{hängande: }1{,}0\\ \\mathrm{kg}'),
                      p('Positiv riktning längs snöret. Sökt: accelerationen.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('Bara den hängande klossens tyngd driver, men den ska accelerera alla tre klossarna.'),
                      mt(f'a=\\frac{{1{{,}}0\\cdot9{{,}}82}}{{3{{,}}0+2{{,}}0+1{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Hur stor massa ska den hängande klossens tyngd accelerera?'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 3, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Klossen längst bort från trissan har bara en kraft längs rörelsen.', mellan=mellan_a(a),
                  steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 3, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  'Frilägg den hängande klossen.', mellan=mellan_a(a), steg_kort=s2(True))],
            'Snörkraften närmast trissan drar fler klossar än den längst bort. Vilken bör vara störst?')

    # ---- 4.989 (häftet 11): bord m med friktion, hängande 2m
    s = System(bord=[K(1.0, 'B', 1.0)], hoger=[K(2.0, 'H')])
    a, (S,) = s.los()
    intro = p('En kloss med massan 1,0 kg ligger på ett horisontellt bord. Ett snöre går från klossen över en trissa vid '
              'bordskanten till en hängande kloss med massan 2,0 kg. Friktionskraften på klossen på bordet är 1,0 N. '
              'Bortse från snörets och trissans massa.')
    stS = lambda kort: [
        li('Frilägg klossen på bordet', fbd(s, 'f989b' + ('k' if kort else ''), [0]),
           p('Snörkraften drar mot kanten och friktionskraften 1,0 N bromsar.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al('S-1{,}0=1{,}0\\cdot a', f'S=1{{,}}0\\cdot{tx(a, 4)}+1{{,}}0\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.989', intro, figur(s, 'k989', 'En kloss på 1,0 kg på ett bord med friktion, kopplad över en trissa till en '
                                  'hängande kloss på 2,0 kg.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{på bordet: }1{,}0\\ \\mathrm{kg},\\ f=1{,}0\\ \\mathrm N',
                                           '\\text{hängande: }2{,}0\\ \\mathrm{kg}'),
                      p('Positiv riktning längs snöret. Sökt: accelerationen.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('Den hängande klossens tyngd driver och friktionen bromsar.'),
                      mt(f'a=\\frac{{2{{,}}0\\cdot9{{,}}82-1{{,}}0}}{{1{{,}}0+2{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Vilken kraft driver systemet och vilken bromsar?'),
             del_('Hur stor är snörkraften?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False), f'{sig(S, 2)} N.',
                  'Frilägg klossen på bordet och ta med friktionen.', mellan=mellan_a(a), steg_kort=stS(True))],
            'Frilägg båda klossarna. Friktionen verkar bara på klossen på bordet.')

    # ---- 4.990 (häftet 12): bord m med friktion, hängande 3m och 2m
    s = System(bord=[K(1.0, 'B', 1.0)], hoger=[K(3.0, 'H'), K(2.0, 'H')])
    a, (S1, S2) = s.los()
    intro = p('En kloss med massan 1,0 kg ligger på ett horisontellt bord. Ett snöre \\(S_1\\) går från klossen över en '
              'trissa vid bordskanten till en hängande kloss med massan 3,0 kg. Under den hänger en kloss med massan '
              '2,0 kg i ett snöre \\(S_2\\). Friktionskraften på klossen på bordet är 1,0 N. Bortse från snörenas och '
              'trissans massa.')
    s1 = lambda kort: [
        li('Frilägg klossen på bordet', fbd(s, 'f990b' + ('k' if kort else ''), [0]),
           p('\\(S_1\\) drar mot kanten och friktionskraften 1,0 N bromsar.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al('S_1-1{,}0=1{,}0\\cdot a', f'S_1=1{{,}}0\\cdot{tx(a, 4)}+1{{,}}0\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Frilägg den nedersta klossen på 2,0 kg', fbd(s, 'f990c' + ('k' if kort else ''), [2]),
           p('Tyngdkraften nedåt och \\(S_2\\) uppåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 2,0 kg: \\({NEWTON}\\)',
           al('mg-S_2=ma', f'S_2=2{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.990', intro, figur(s, 'k990', 'En kloss på 1,0 kg på ett bord med friktion. Över en trissa hänger klossar '
                                  'på 3,0 kg och 2,0 kg under varandra.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 4, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{på bordet: }1{,}0\\ \\mathrm{kg},\\ f=1{,}0\\ \\mathrm N',
                                           '\\text{hängande: }3{,}0\\ \\mathrm{kg}+2{,}0\\ \\mathrm{kg}'),
                      p('Positiv riktning längs snöret. Sökt: accelerationen.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('Tyngden av de två hängande klossarna driver och friktionen bromsar.'),
                      mt(f'a=\\frac{{5{{,}}0\\cdot9{{,}}82-1{{,}}0}}{{1{{,}}0+3{{,}}0+2{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Räkna ihop de hängande massorna. Vilken kraft bromsar?'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 4, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Frilägg klossen på bordet.', mellan=mellan_a(a), steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 4, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  'Frilägg klossen längst ned.', mellan=mellan_a(a), steg_kort=s2(True))],
            'Börja med hela systemet. Välj sedan klossar som bara har en okänd snörkraft.')

    # ---- 4.991 (häftet 13): över bordet med två trissor, 3m mot m
    s = System(vanster=[K(3.0, 'V')], hoger=[K(1.0, 'H')], tomtbord=True)
    a, (S,) = s.los()
    a = abs(a)
    intro = p('Ett snöre ligger över ett bord och går över en trissa vid varje bordskant. I den vänstra änden hänger en '
              'kloss med massan 3,0 kg och i den högra en kloss med massan 1,0 kg. Klossarna släpps från stillastående. '
              'Bortse från friktion och från snörets och trissornas massa.')
    stS = lambda kort: [
        li('Frilägg den lätta klossen', fbd(s, 'f991b' + ('k' if kort else ''), [1]),
           p('Klossen på 1,0 kg accelererar uppåt: snörkraften uppåt och tyngdkraften nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al('S-mg=ma', f'S=1{{,}}0\\cdot(9{{,}}82+{tx(a, 4)})\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.991', intro, figur(s, 'k991', 'Ett snöre över ett bord med en trissa vid varje kant. Till vänster hänger '
                                  '3,0 kg och till höger 1,0 kg.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{vänster: }3{,}0\\ \\mathrm{kg}', '\\text{höger: }1{,}0\\ \\mathrm{kg}'),
                      p('Den vänstra klossen är tyngst och sjunker. Positiv riktning längs snöret åt vänster. Sökt: '
                        'accelerationen.')),
                   li(f'Newtons andra lag längs snöret: \\({NEWTON_TOT}\\)',
                      p('Bordet påverkar inte snöret, eftersom trissorna saknar friktion. Skillnaden mellan '
                        'tyngdkrafterna driver.'),
                      mt(f'a=\\frac{{(3{{,}}0-1{{,}}0)\\cdot9{{,}}82}}{{3{{,}}0+1{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Vilken sida sjunker, och vilken kraft driver?'),
             del_('Hur stor är snörkraften?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False), f'{sig(S, 2)} N.',
                  'Frilägg den lätta klossen som åker uppåt.', mellan=mellan_a(a), steg_kort=stS(True))],
            'Snöret är detsamma hela vägen, så snörkraften är lika stor i båda ändarna.')

    # ---- 4.992 (häftet 14): m vänster, 2m på bordet, 3m höger
    s = System(vanster=[K(1.0, 'V')], bord=[K(2.0, 'B')], hoger=[K(3.0, 'H')])
    a, (S1, S2) = s.los()
    intro = p('En kloss med massan 2,0 kg ligger på ett horisontellt bord. Från klossen går ett snöre \\(S_1\\) över en '
              'trissa vid den vänstra bordskanten till en hängande kloss med massan 1,0 kg, och ett snöre \\(S_2\\) över '
              'en trissa vid den högra kanten till en hängande kloss med massan 3,0 kg. Bortse från friktion och från '
              'snörenas och trissornas massa.')
    s1 = lambda kort: [
        li('Frilägg den vänstra klossen på 1,0 kg', fbd(s, 'f992b' + ('k' if kort else ''), [0]),
           p('Den accelererar uppåt: \\(S_1\\) uppåt och tyngdkraften nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 1,0 kg: \\({NEWTON}\\)',
           al('S_1-mg=ma', f'S_1=1{{,}}0\\cdot(9{{,}}82+{tx(a, 4)})\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Frilägg den högra klossen på 3,0 kg', fbd(s, 'f992c' + ('k' if kort else ''), [2]),
           p('Den accelererar nedåt: tyngdkraften nedåt och \\(S_2\\) uppåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 3,0 kg: \\({NEWTON}\\)',
           al('mg-S_2=ma', f'S_2=3{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.992', intro, figur(s, 'k992', 'En kloss på 2,0 kg på ett bord med en trissa vid varje kant. Till vänster '
                                  'hänger 1,0 kg och till höger 3,0 kg.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{vänster: }1{,}0\\ \\mathrm{kg}', '\\text{på bordet: }2{,}0\\ \\mathrm{kg}',
                                           '\\text{höger: }3{,}0\\ \\mathrm{kg}'),
                      p('Den högra sidan är tyngst. Positiv riktning längs snöret åt höger. Sökt: accelerationen.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('Tyngden av klossen till höger drar åt ett håll och tyngden av klossen till vänster åt det andra.'),
                      mt(f'a=\\frac{{(3{{,}}0-1{{,}}0)\\cdot9{{,}}82}}{{1{{,}}0+2{{,}}0+3{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Två tyngdkrafter drar åt var sitt håll längs snöret.'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 4, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Frilägg den vänstra klossen.', mellan=mellan_a(a), steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 4, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  'Frilägg den högra klossen.', mellan=mellan_a(a), steg_kort=s2(True))],
            'Klossen på bordet har en snörkraft åt varje håll. Varför kan de inte vara lika stora?')

    # ---- 4.993 (häftet 15): 2m vänster, 4m på bordet med friktion, 3m höger
    s = System(vanster=[K(2.0, 'V')], bord=[K(4.0, 'B', 4.0)], hoger=[K(3.0, 'H')])
    a, (S1, S2) = s.los()
    intro = p('En kloss med massan 4,0 kg ligger på ett horisontellt bord. Från klossen går ett snöre \\(S_1\\) över en '
              'trissa vid den vänstra bordskanten till en hängande kloss med massan 2,0 kg, och ett snöre \\(S_2\\) över '
              'en trissa vid den högra kanten till en hängande kloss med massan 3,0 kg. Friktionskraften på klossen på '
              'bordet är 4,0 N. Bortse från snörenas och trissornas massa.')
    s1 = lambda kort: [
        li('Frilägg den vänstra klossen på 2,0 kg', fbd(s, 'f993b' + ('k' if kort else ''), [0]),
           p('Den accelererar uppåt: \\(S_1\\) uppåt och tyngdkraften nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 2,0 kg: \\({NEWTON}\\)',
           al('S_1-mg=ma', f'S_1=2{{,}}0\\cdot(9{{,}}82+{tx(a, 4)})\\approx{tx(S1, 2)}{UNIT_N}'))]
    s2 = lambda kort: [
        li('Frilägg den högra klossen på 3,0 kg', fbd(s, 'f993c' + ('k' if kort else ''), [2]),
           p('Den accelererar nedåt: tyngdkraften nedåt och \\(S_2\\) uppåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för klossen på 3,0 kg: \\({NEWTON}\\)',
           al('mg-S_2=ma', f'S_2=3{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S2, 2)}{UNIT_N}'))]
    uppgift('4.993', intro, figur(s, 'k993', 'En kloss på 4,0 kg på ett bord med friktion och en trissa vid varje kant. '
                                  'Till vänster hänger 2,0 kg och till höger 3,0 kg.'),
            [del_('Hur stor acceleration får klossarna?', a, 'm/s²', 2, 'C', 4, '(0/1/0)',
                  [li('Givet och sökt', al('\\text{vänster: }2{,}0\\ \\mathrm{kg}',
                                           '\\text{på bordet: }4{,}0\\ \\mathrm{kg},\\ f=4{,}0\\ \\mathrm N',
                                           '\\text{höger: }3{,}0\\ \\mathrm{kg}'),
                      p('Tyngdkrafternas skillnad är \\((3{,}0-2{,}0)\\cdot9{,}82=9{,}82\\) N, mer än friktionskraften. '
                        'Systemet rör sig alltså åt höger, och friktionen verkar åt vänster. Positiv riktning åt höger.')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('Skillnaden mellan tyngdkrafterna driver och friktionen bromsar.'),
                      mt(f'a=\\frac{{(3{{,}}0-2{{,}}0)\\cdot9{{,}}82-4{{,}}0}}{{2{{,}}0+4{{,}}0+3{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Avgör först åt vilket håll systemet rör sig. Då vet du åt vilket håll friktionen verkar.'),
             del_('Hur stor är snörkraften \\(S_1\\)?', S1, 'N', 2, 'C', 4, '(0/1/0)', s1(False), f'{sig(S1, 2)} N.',
                  'Frilägg den vänstra klossen.', mellan=mellan_a(a), steg_kort=s1(True)),
             del_('Hur stor är snörkraften \\(S_2\\)?', S2, 'N', 2, 'C', 4, '(0/1/0)', s2(False), f'{sig(S2, 2)} N.',
                  'Frilägg den högra klossen.', mellan=mellan_a(a), steg_kort=s2(True))],
            'Jämför tyngdkrafternas skillnad med friktionskraften innan du ställer upp ekvationerna.')


# ================================================================ 4.994–4.1004: nya uppgifter
def kranfigur(pid):
    R = Rit(pid)
    R.bak.append(f'<rect x="20" y="10" width="200" height="14" rx="3" fill="#e2b04a" stroke="#9a7220" stroke-width="1.2"/>')
    R.bak.append('<rect x="104" y="24" width="32" height="14" rx="2" fill="#6b7682"/>')
    R.linje(120, 38, 120, 120, '#3d4752', 2)
    R.fram.append('<path d="M120 120 q-8 0 -8 8 q0 8 8 8" fill="none" stroke="#3d4752" stroke-width="3"/>')
    R.linje(120, 136, 96, 160, '#3d4752', 1.6)
    R.linje(120, 136, 144, 160, '#3d4752', 1.6)
    R.el.append(f'<rect x="60" y="160" width="120" height="26" rx="3" fill="url(#{pid}g4)" stroke="#a8443a" '
                f'stroke-width="1.6" filter="url(#{pid}s)"/>')
    R.grad(4)
    R.text(120, 178, '250 kg', 15, 'middle', '#1f2d3a', bold=True)
    R.pil(206, 196, 206, 136, '#0b6fa4', 3)
    R.text(214, 172, 'a', 16, 'start', '#0b6fa4', bold=True, italic=True)
    return R.svg(250, 205, 'En kran lyfter en balk på 250 kg. Balken accelererar uppåt.')


def nya():
    # ---- 4.994 E: leksakståg, bara accelerationen
    s = System(bord=[K(0.20, 'B', et='vagn'), K(0.20, 'B', et='vagn'), K(0.60, 'B', et='lok')], F=1.5, golv=True)
    a, _ = s.los()
    uppgift('4.994',
            p('Ett leksakslok med massan 0,60 kg drar två vagnar som väger 0,20 kg var. Loket och vagnarna är '
              'sammankopplade och rullar på ett horisontellt golv. Den drivande kraften på loket är 1,5 N. Bortse från '
              'friktion och luftmotstånd.'),
            figur(s, 'k994', 'Ett leksakslok drar två vagnar åt höger med den drivande kraften 1,5 N.', Ftext='1,5 N'),
            [del_('Hur stor acceleration får tåget?', a, 'm/s²', 2, 'E', 2, '(1/0/0)',
                  [li('Hela tågets massa', mt('m_{\\text{tot}}=0{,}60+0{,}20+0{,}20=1{,}0\\ \\mathrm{kg}')),
                   li(f'Newtons andra lag för hela tåget: \\({NEWTON_TOT}\\)',
                      p('Kopplingskrafterna mellan vagnarna tar ut varandra. Bara den drivande kraften verkar framåt.'),
                      mt(f'a=\\frac{{1{{,}}5}}{{1{{,}}0}}=1{{,}}5{UNIT_A}'))],
                  '1,5 m/s².', '')],
            'Kopplingarna mellan vagnarna är inre krafter. Vilken massa ska den drivande kraften accelerera?')

    # ---- 4.995 E: dragkrok, givet a
    s = System(bord=[K(2.0, 'B', et='släp 450 kg'), K(4.0, 'B', et='bil')], golv=True)
    S = 450 * 1.2
    uppgift('4.995',
            p('En bil drar en släpvagn med massan 450 kg längs en horisontell väg. Bilen och släpvagnen accelererar med '
              '1,2 m/s². Bortse från friktion och luftmotstånd på släpvagnen.'),
            figur(s, 'k995', 'En bil drar en släpvagn på 450 kg åt höger.'),
            [del_('Hur stor kraft verkar på släpvagnen från dragkroken?', S, 'N', 2, 'E', 1, '(1/0/0)',
                  [li(f'Newtons andra lag för släpvagnen: \\({NEWTON}\\)',
                      p('Dragkroken är den enda vågräta kraften på släpvagnen.'),
                      mt(f'F=450\\cdot1{{,}}2=540{UNIT_N}'))],
                  '540 N.', '')],
            'Frilägg bara släpvagnen. Vilken kraft ger den accelerationen?')

    # ---- 4.996 E: kran lyfter balk
    S = 250 * (g + 0.80)
    uppgift('4.996',
            p('En kran lyfter en stålbalk med massan 250 kg i en vajer. Balken accelererar uppåt med 0,80 m/s².'),
            kranfigur('k996'),
            [del_('Hur stor är kraften i vajern?', S, 'N', 2, 'E', 2, '(1/0/0)',
                  [li('Frilägg balken', p('Vajern drar uppåt med kraften \\(S\\) och tyngdkraften \\(mg\\) drar nedåt. '
                                          'Positiv riktning uppåt.')),
                   li(f'Newtons andra lag för balken: \\({NEWTON}\\)',
                      al('S-mg=ma', 'S=m(g+a)=250\\cdot(9{,}82+0{,}80)', 'S\\approx2\\,655\\ \\mathrm N\\approx2{,}7\\ \\mathrm{kN}'))],
                  '2,7·10³ N, alltså 2,7 kN.', '')],
            'Balken accelererar uppåt. Ska vajerkraften vara större eller mindre än balkens tyngd?')

    # ---- 4.997 E: labbvagn och hängande vikt, bara a
    s = System(bord=[K(0.80, 'B', et='0,80 kg')], hoger=[K(0.20, 'H', et='0,20 kg')])
    a, _ = s.los()
    uppgift('4.997',
            p('I en laboration rullar en vagn med massan 0,80 kg på en horisontell bänk. Ett snöre går från vagnen över en '
              'trissa vid bänkens kant till en vikt med massan 0,20 kg. Bortse från friktion och från snörets och '
              'trissans massa.'),
            figur(s, 'k997', 'En vagn på 0,80 kg på en bänk dras av en hängande vikt på 0,20 kg.'),
            [del_('Hur stor acceleration får vagnen?', a, 'm/s²', 2, 'E', 2, '(1/0/0)',
                  [li('Den hängande viktens tyngd driver systemet',
                      mt('F_g=0{,}20\\cdot9{,}82=1{,}964\\ \\mathrm N')),
                   li(f'Newtons andra lag för vagnen och vikten: \\({NEWTON_TOT}\\)',
                      mt(f'a=\\frac{{1{{,}}964}}{{0{{,}}80+0{{,}}20}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', '')],
            'Viktens tyngd ska accelerera både vikten och vagnen.')

    # ---- 4.998 C: byggarbetsplats, hink och motvikt över trissa
    s = System(vanster=[K(18, 'V', et='18 kg')], hoger=[K(22, 'H', et='22 kg')])
    a, (S,) = s.los()
    intro = p('På en byggarbetsplats hänger en hink med murbruk och en motvikt i var sin ände av ett rep som går över en '
              'trissa. Hinken väger 18 kg och motvikten 22 kg. Systemet släpps från stillastående. Bortse från repets och '
              'trissans massa och från friktion i trissan.')
    stS = lambda kort: [
        li('Frilägg hinken', fbd(s, 'f998b' + ('k' if kort else ''), [0]),
           p('Hinken accelererar uppåt: repkraften uppåt och tyngdkraften nedåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för hinken: \\({NEWTON}\\)',
           al('S-mg=ma', f'S=18\\cdot(9{{,}}82+{tx(a, 4)})\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.998', intro, figur(s, 'k998', 'En hink på 18 kg och en motvikt på 22 kg hänger över en trissa.'),
            [del_('Hur stor acceleration får hinken?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li('Givet och sökt', al('m_{\\text{hink}}=18\\ \\mathrm{kg}', 'm_{\\text{motvikt}}=22\\ \\mathrm{kg}'),
                      p('Motvikten sjunker och hinken lyfts. Sökt: accelerationen.')),
                   li(f'Newtons andra lag längs repet: \\({NEWTON_TOT}\\)',
                      mt(f'a=\\frac{{(22-18)\\cdot9{{,}}82}}{{22+18}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Hur stor är skillnaden mellan tyngdkrafterna?'),
             del_('Hur stor är kraften i repet?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False), f'{sig(S, 2)} N.',
                  'Frilägg hinken. Den accelererar uppåt.', mellan=mellan_a(a, 'Hinken och motvikten'),
                  steg_kort=stS(True))],
            'Behandla hinken och motvikten som klossarna i ett snöre över en trissa.')

    # ---- 4.999 C: friktionstal
    fr = 0.30 * 4.0 * g
    s = System(bord=[K(4.0, 'B', fr, et='4,0 kg')], hoger=[K(2.0, 'H', et='2,0 kg')])
    a, (S,) = s.los()
    intro = p('En låda med massan 4,0 kg ligger på ett horisontellt bord. Ett snöre går från lådan över en trissa vid '
              'bordskanten till en hängande vikt med massan 2,0 kg. Glidfriktionstalet mellan lådan och bordet är 0,30. '
              'Bortse från snörets och trissans massa.')
    stS = lambda kort: [
        li('Frilägg den hängande vikten', fbd(s, 'f999b' + ('k' if kort else ''), [1]),
           p('Den accelererar nedåt: tyngdkraften nedåt och snörkraften uppåt.'), acc_kalla(a, kort)),
        li(f'Newtons andra lag för vikten: \\({NEWTON}\\)',
           al('mg-S=ma', f'S=2{{,}}0\\cdot(9{{,}}82-{tx(a, 4)})\\approx{tx(S, 2)}{UNIT_N}'))]
    uppgift('4.999', intro, figur(s, 'k999', 'En låda på 4,0 kg på ett bord med friktion dras av en hängande vikt på 2,0 kg.'),
            [del_('Hur stor acceleration får lådan?', a, 'm/s²', 2, 'C', 4, '(0/2/0)',
                  [li('Friktionskraften: \\(F_f=\\mu F_N\\)',
                      p('Bordet är horisontellt, så normalkraften är lika stor som lådans tyngd.'),
                      mt(f'F_f=0{{,}}30\\cdot4{{,}}0\\cdot9{{,}}82\\approx{tx(fr, 4)}{UNIT_N}')),
                   li(f'Newtons andra lag för lådan och vikten: \\({NEWTON_TOT}\\)',
                      p('Viktens tyngd driver och friktionen bromsar.'),
                      mt(f'a=\\frac{{2{{,}}0\\cdot9{{,}}82-{tx(fr, 4)}}}{{4{{,}}0+2{{,}}0}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Räkna först ut friktionskraften på lådan.'),
             del_('Hur stor är snörkraften?', S, 'N', 2, 'C', 3, '(0/1/0)', stS(False), f'{sig(S, 2)} N.',
                  'Den hängande vikten saknar friktion och är lättast att frilägga.', mellan=mellan_a(a, 'Lådan och vikten'),
                  steg_kort=stS(True))],
            'Friktionen bromsar bara lådan på bordet.', formaga=('modellering', 'procedur', 'problemlösning'))

    # ---- 4.1000 C: okänd hängande massa ur uppmätt acceleration
    M, am = 1.5, 2.4
    mh = M * am / (g - am)
    s = System(bord=[K(1.5, 'B', et='1,5 kg')], hoger=[K(0.5, 'H', et='m = ?')])
    uppgift('4.1000',
            p('En vagn med massan 1,5 kg rullar på en horisontell bana. Ett snöre går från vagnen över en trissa vid banans '
              'slut till en hängande vikt. Vagnens acceleration mäts till 2,4 m/s². Bortse från friktion och från snörets '
              'och trissans massa.'),
            figur(s, 'k1000', 'En vagn på 1,5 kg på en bana dras av en hängande vikt med okänd massa.'),
            [del_('Hur stor massa har den hängande vikten?', mh, 'kg', 2, 'C', 4, '(0/2/0)',
                  [li('Givet och sökt', al('M=1{,}5\\ \\mathrm{kg}', 'a=2{,}4\\ \\mathrm{m/s^2}'),
                      p('Sökt: viktens massa \\(m\\).')),
                   li(f'Newtons andra lag för vagnen: \\({NEWTON}\\)', p('Bara snörkraften drar vagnen.'),
                      mt('S=Ma=1{,}5\\cdot2{,}4=3{,}6\\ \\mathrm N')),
                   li(f'Newtons andra lag för vikten: \\({NEWTON}\\)',
                      p('Vikten accelererar nedåt med samma acceleration.'),
                      al('mg-S=ma', 'm(g-a)=S', f'm=\\frac{{3{{,}}6}}{{9{{,}}82-2{{,}}4}}\\approx{tx(mh, 2)}\\ \\mathrm{{kg}}'))],
                  f'{sig(mh, 2)} kg.', '')],
            'Använd vagnen för att få snörkraften. Ställ sedan upp Newtons andra lag för vikten.',
            formaga=('modellering', 'problemlösning'))

    # ---- 4.1001 A: algebraiskt, m och 3m över trissa
    s = System(vanster=[Kropp(1, 'V', etikett='<tspan font-style="italic">m</tspan>')],
               hoger=[Kropp(3, 'H', etikett='3<tspan font-style="italic">m</tspan>')])
    intro = p('Två klossar med massorna \\(m\\) och \\(3m\\) hänger i var sin ände av ett snöre över en trissa och släpps '
              'från stillastående. Bortse från snörets och trissans massa och från friktion i trissan.')
    sys_tal = lambda kort: [
        li('Frilägg klossarna \\(m\\) och \\(3m\\)', fbd(s, 'f1001a' + ('k' if kort else ''))),
        li(f'Newtons andra lag för varje kloss: \\({NEWTON}\\)',
           p('Positiv riktning medurs runt trissan: uppåt för \\(m\\) och nedåt för \\(3m\\).'),
           mt('\\begin{cases}S-mg=ma & (1)\\\\ 3mg-S=3ma & (2)\\end{cases}')),
        li('Addera ekvationerna, så försvinner \\(S\\)', al('2mg=4ma', 'a=\\frac{g}{2}'))]
    stS = lambda kort: [
        li(f'Newtons andra lag för den lätta klossen: \\({NEWTON}\\)',
           p('Klossen \\(m\\) accelererar uppåt: \\(S-mg=ma\\).'),
           p('Accelerationen ' + ('är given: ' if kort else 'från a): ') + '\\(a=\\tfrac{g}{2}\\).')),
        li('Lös ut \\(S\\) och sätt in \\(a\\)', al('S=mg+ma=mg+m\\cdot\\frac{g}{2}', 'S=\\frac{3mg}{2}'))]
    uppgift('4.1001', intro, figur(s, 'k1001', 'Klossar med massorna m och 3m hänger över en trissa.'),
            [del_('Uttryck accelerationen med \\(g\\).', 'g/2', None, 2, 'A', 4, '(0/0/1)', sys_tal(False),
                  '\\(a=\\tfrac{g}{2}\\).', 'Ställ upp en ekvation för varje kloss och addera dem.', format='uttryck'),
             del_('Uttryck snörkraften med \\(m\\) och \\(g\\).', '3*m*g/2', None, 2, 'A', 5, '(0/0/1)', stS(False),
                  '\\(S=\\tfrac{3mg}{2}\\).', 'Använd ekvationen för den lätta klossen.',
                  mellan='Klossarnas acceleration är \\(a=\\tfrac{g}{2}\\).', steg_kort=stS(True), format='uttryck')],
            'Lös uppgiften utan siffror. Låt \\(m\\) stå kvar som en bokstav.', formaga=('modellering', 'resonemang'))

    # ---- 4.1002 A: vilken massa ger en viss acceleration (två trissor och friktion)
    m1, m2, f, a_mal = 2.0, 3.0, 5.0, 1.5
    Mh = (m1 * g + f + (m1 + m2) * a_mal) / (g - a_mal)
    s = System(vanster=[K(2.0, 'V', et='2,0 kg')], bord=[K(3.0, 'B', 5.0, et='3,0 kg')], hoger=[K(4.0, 'H', et='M = ?')])
    uppgift('4.1002',
            p('En låda med massan 3,0 kg ligger på ett horisontellt bord. Från lådan går ett snöre över en trissa vid den '
              'vänstra bordskanten till en hängande vikt med massan 2,0 kg, och ett annat snöre över en trissa vid den '
              'högra kanten till en hängande vikt med massan \\(M\\). Friktionskraften på lådan är 5,0 N. Bortse från '
              'snörenas och trissornas massa.'),
            figur(s, 'k1002', 'En låda på 3,0 kg på ett bord. Till vänster hänger 2,0 kg och till höger en okänd massa M.'),
            [del_('Hur stor ska massan \\(M\\) vara för att lådan ska accelerera åt höger med 1,5 m/s²?', Mh, 'kg', 2, 'A',
                  5, '(0/1/2)',
                  [li('Givet och sökt', al('m_1=2{,}0\\ \\mathrm{kg}\\ \\text{(vänster)},\\ m_2=3{,}0\\ \\mathrm{kg}',
                                           'f=5{,}0\\ \\mathrm N,\\ a=1{,}5\\ \\mathrm{m/s^2}\\ \\text{åt höger}'),
                      p('Lådan rör sig åt höger, så friktionen verkar åt vänster. Positiv riktning åt höger. Sökt: \\(M\\).')),
                   li(f'Newtons andra lag för hela systemet: \\({NEWTON_TOT}\\)',
                      p('\\(Mg\\) drar åt höger, \\(m_1g\\) och friktionen åt vänster.'),
                      mt('Mg-m_1g-f=(m_1+m_2+M)\\,a')),
                   li('Samla \\(M\\) på ena sidan', al('M(g-a)=m_1g+f+(m_1+m_2)\\,a',
                                                       'M=\\frac{2{,}0\\cdot9{,}82+5{,}0+5{,}0\\cdot1{,}5}{9{,}82-1{,}5}',
                                                       f'M\\approx{tx(Mh, 2)}\\ \\mathrm{{kg}}')),
                   li('Kontroll: sätt tillbaka \\(M\\) i Newtons andra lag',
                      mt(f'a=\\frac{{{tx(Mh, 4)}\\cdot9{{,}}82-19{{,}}64-5{{,}}0}}{{2{{,}}0+3{{,}}0+{tx(Mh, 4)}}}'
                         f'\\approx1{{,}}5\\ \\mathrm{{m/s^2}}'))],
                  f'{sig(Mh, 2)} kg.', '')],
            'Ställ upp Newtons andra lag för hela systemet med \\(M\\) som obekant. \\(M\\) finns både i den drivande '
            'kraften och i massan.', formaga=('problemlösning', 'modellering'))

    # ---- 4.1003 C: fart när vikten når golvet
    s = System(bord=[K(2.0, 'B', 3.0, et='2,0 kg')], hoger=[K(1.5, 'H', et='1,5 kg')])
    a, _ = s.los()
    v = math.sqrt(2 * a * 0.60)
    intro = p('En kloss med massan 2,0 kg ligger på ett horisontellt bord. Ett snöre går från klossen över en trissa vid '
              'bordskanten till en hängande vikt med massan 1,5 kg. Friktionskraften på klossen är 3,0 N. Vikten hänger '
              '0,60 m över golvet och släpps från stillastående. Bortse från snörets och trissans massa.')
    stv = lambda kort: [
        li('Givet och sökt', al('v_0=0', 's=0{,}60\\ \\mathrm m', f'a\\approx{tx(a, 4)}{UNIT_A}'),
           p(('Accelerationen är given i frågan.' if kort else 'Accelerationen från a).') + ' Sökt: farten \\(v\\).')),
        li('Tidlösa formeln: \\(v^2=v_0^2+2as\\)', p('Tiden är inte given.'),
           mt(f'v=\\sqrt{{2\\cdot{tx(a, 4)}\\cdot0{{,}}60}}\\approx{tx(v, 2)}\\ \\mathrm{{m/s}}'))]
    uppgift('4.1003', intro, figur(s, 'k1003', 'En kloss på 2,0 kg på ett bord med friktion, kopplad över en trissa till en '
                                   'hängande vikt på 1,5 kg.'),
            [del_('Hur stor acceleration får vikten?', a, 'm/s²', 2, 'C', 3, '(0/1/0)',
                  [li(f'Newtons andra lag för klossen och vikten: \\({NEWTON_TOT}\\)',
                      p('Viktens tyngd driver och friktionen bromsar.'),
                      mt(f'a=\\frac{{1{{,}}5\\cdot9{{,}}82-3{{,}}0}}{{2{{,}}0+1{{,}}5}}\\approx{tx(a, 2)}{UNIT_A}'))],
                  f'{sig(a, 2)} m/s².', 'Vilken kraft driver och vilken bromsar?'),
             del_('Hur stor fart har vikten när den når golvet?', v, 'm/s', 2, 'C', 4, '(0/2/0)', stv(False),
                  f'{sig(v, 2)} m/s.', 'Accelerationen är konstant. Vilken rörelseformel saknar tiden?',
                  mellan=mellan_a(a, 'Klossen och vikten'), steg_kort=stv(True))],
            'Räkna först ut accelerationen med Newtons andra lag och använd den sedan i en rörelseformel.',
            formaga=('modellering', 'problemlösning'))

    # ---- 4.1004 A: dragkraften ur två snörkrafter
    s = System(bord=[K(1.0, 'B', et='1,0 kg'), K(2.0, 'B', et='m = ?'), K(2.0, 'B', et='2,0 kg')], F=1, golv=True)
    a4 = 4.0 / 1.0
    m2 = 10.0 / a4 - 1.0
    Ftot = (1.0 + m2 + 2.0) * a4
    uppgift('4.1004',
            p('Tre klossar ligger i en rad på ett horisontellt golv utan friktion och är sammanbundna med snören. Den '
              'främsta klossen dras åt höger med en kraft \\(F\\). Den bakersta klossen väger 1,0 kg, den mellersta har '
              'okänd massa och den främsta väger 2,0 kg. Snörkraften \\(S_1\\) mellan den bakersta och den mellersta '
              'klossen är 4,0 N, och snörkraften \\(S_2\\) mellan den mellersta och den främsta är 10 N.'),
            figur(s, 'k1004', 'Tre klossar i rad dras åt höger med kraften F. Den mellersta har okänd massa.', Ftext='F'),
            [del_('Hur stor är kraften \\(F\\)?', Ftot, 'N', 2, 'A', 5, '(0/1/2)',
                  [li(f'Den bakersta klossen ger accelerationen: \\({NEWTON}\\)',
                      p('Bara \\(S_1\\) drar den bakersta klossen.'), mt('a=\\frac{S_1}{m_1}=\\frac{4{,}0}{1{,}0}=4{,}0\\ '
                                                                     '\\mathrm{m/s^2}')),
                   li('\\(S_2\\) drar de två bakre klossarna', al('S_2=(m_1+m_2)\\,a', 'm_1+m_2=\\frac{10}{4{,}0}=2{,}5\\ '
                                                                  '\\mathrm{kg}', 'm_2=1{,}5\\ \\mathrm{kg}')),
                   li(f'Newtons andra lag för alla tre klossarna: \\({NEWTON_TOT}\\)',
                      mt(f'F=(1{{,}}0+1{{,}}5+2{{,}}0)\\cdot4{{,}}0={tx(Ftot, 2)}{UNIT_N}')),
                   li('Kontroll med den främsta klossen', mt('F-S_2=2{,}0\\cdot4{,}0\\ \\Rightarrow\\ F=10+8{,}0=18\\ \\mathrm N'))],
                  f'{sig(Ftot, 2)} N.', '')],
            'Börja med den kloss där du känner både massan och den enda vågräta kraften.',
            formaga=('problemlösning', 'resonemang'))


def main():
    hafte()
    nya()
    nya_obj = [objekt(u) for u in UPPG]
    src, bank = B.las(ROOT / 'uppgifter.js')
    ids = {q['id'] for q in bank}
    for q in nya_obj:
        assert q['id'] not in ids, q['id']
    # Lägg de nya uppgifterna sist i kapitel 4
    sista = max(i for i, q in enumerate(bank) if q.get('kap') == 4)
    spannen = B.spann(src)
    slut = spannen[sista][1]
    prefix = B._prefix(src, spannen[sista][0])
    till = ''.join(',\n' + B._dump(q, prefix) for q in nya_obj)
    ny_src = src[:slut] + till + src[slut:]
    ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    assert len(ny_bank) == len(bank) + len(nya_obj)
    for q in nya_obj:
        print(q['id'], q['niva'], q['poang'], q['traningsniva'], q['rättSvar'])
    if SKRIV:
        B.skriv(ROOT / 'uppgifter.js', ny_src)
    return nya_obj


if __name__ == '__main__':
    main()
