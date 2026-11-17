# Fy1 kap 9: nuklider, genomläsning 2026-11-17. Tar också bort proton-, neutron- och väteatommassor ur
# frågorna om massdefekt och bindningsenergi (användarbeslut 2026-10-25: konstanter slås upp i
# formelsamlingen; formelsamlingens värden är desamma som facit räknar med).
# Ändrat i övrigt: decimalpunkt, "1 protoner", precisionskrav, definitioner ("alltså protoner och neutroner"),
# "Avogadros konstant används", modellmeningar och dubblerade frågor.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


KONSTANTER = [
    (' Väteatomens massa är 1,007825 u och neutronens massa 1,008665 u.', ''),
    (' Väteatomens massa är 1,007825 u och en fri neutrons massa 1,008665 u.', ''),
    (' Massan hos en fri proton är 1,007276 u och hos en fri neutron 1,008665 u.', ''),
    (' En väteatom har massan 1,007825 u och en neutron 1,008665 u.', ''),
    (' En fri proton har massan 1,007276 u och en fri neutron 1,008665 u.', ''),
    (' En neutron har massan 1,008665 u.', ''),
    ('Kväve-13 har massan 13,0057386 u och en neutron 1,0086649 u.', 'Kväve-13 har massan 13,0057386 u.'),
    ('Kol-13 har massan 13,0033548 u och en väteatom 1,0078250 u.', 'Kol-13 har massan 13,0033548 u.'),
    ('En fri väteatom har massan 1,0078250 u och en fri neutron 1,0086649 u. ', ''),
    ('Uranatomens massa är 235,0439231 u och neutronens 1,008665 u', 'Uranatomens massa är 235,0439231 u'),
]
# Bara nuklider (massdefekt och bindningsenergi), där massorna fungerar som konstanter. I fusion och fission
# står neutron- och vätemassan i samma lista som reaktionens övriga atommassor och behålls.
KONST_IDS = ['9.20', '9.31', '9.61', '9.62', '9.233', '9.235', '9.236', '9.68', '9.239', '9.389', '9.398',
             '9.570', '9.571', '9.572', '9.574']

R = {
    '9.19': {'ers': [('a) Beräkna antalet atomer i 1,0 g järn och visa hur Avogadros konstant används.', 'a) Hur många atomer finns i 1,0 g järn?'),
                     ('b) Beräkna antalet atomer i en järnspik med massan 3,5 g.', 'b) Hur många atomer finns i en järnspik med massan 3,5 g?')]},
    '9.20': {'ers': [('massdefekten 0.030377 u', 'massdefekten 0,030377 u')]},
    '9.61': {'ers': [('massdefekten 0.042132 u', 'massdefekten 0,042132 u')]},
    '9.62': {'ers': [('massdefekten 0.528464 u', 'massdefekten 0,528464 u')]},
    '9.22': {'ers': [('.  Bestäm massan i kg', '. Bestäm massan i kg'),
                     ('a) Omvandla 1,000000 u till kg och motsvarande energi i MeV.', 'a) Hur många kg är 1,000000 u, och vilken energi i MeV motsvarar massan?'),
                     ('b) Omvandla 0,030000 u till kg och motsvarande energi i MeV.', 'b) Hur många kg är 0,030000 u, och vilken energi i MeV motsvarar massan?'),
                     ('c) Omvandla 4,002602 u till kg och motsvarande energi i MeV.', 'c) Hur många kg är 4,002602 u, och vilken energi i MeV motsvarar massan?')]},
    '9.32': {'ers': [('<p>b) Bestäm massdefekten.</p>', '<p>b) Bestäm massdefekten i kg.</p>')]},
    '9.35': {'ers': [('och uran-238 har 238,050788 u.', 'och uran-238 har atommassan 238,050788 u.'),
                     ('Jämför värdena: vilken kärna är hårdare bunden per nukleon?', 'Vilken av kärnorna har störst bindningsenergi per nukleon?')]},
    '9.218': {'t': p('En kol-12-kärna har 12 nukleoner och bindningsenergin 92,16 MeV. Hur stor är bindningsenergin per nukleon?')},
    '9.220': {'t': p('En järn-56-kärna har 56 nukleoner och bindningsenergin 492,2 MeV. Hur stor är bindningsenergin per nukleon?')},
    '9.221': {'t': p('En helium-4-kärna har 4 nukleoner och bindningsenergin 28,28 MeV. Hur stor är bindningsenergin per nukleon?')},
    '9.222': {'t': p('En kväve-14-kärna har 14 nukleoner och bindningsenergin 104,7 MeV. Hur stor är bindningsenergin per nukleon?')},
    '9.230': {'ers': [('Hur mycket större är den högre energin per nukleon?', 'Hur stor är skillnaden?')]},
    '9.233': {'ers': [('En kärna har 1 protoner och 1 neutroner.', 'En kärna har en proton och en neutron.'),
                      ('</p><p>Bestäm bindningsenergin.', ' Bestäm bindningsenergin.')]},
    '9.236': {'ers': [('</p><p>Bestäm bindningsenergin per nukleon.', ' Bestäm bindningsenergin per nukleon.')]},
    '9.239': {'ers': [('</p><p>Bestäm bindningsenergin per nukleon.', ' Bestäm bindningsenergin per nukleon.')]},
    '9.68': {'ers': [('</p><p>Bestäm bindningsenergin per nukleon.', ' Bestäm bindningsenergin per nukleon.')]},
    '9.390': {'ers': [('</p><p>Bestäm bindningsenergin.', ' Bestäm bindningsenergin.')]},
    '9.396': {'ers': [('u. </p><p>Bestäm bindningsenergin per nukleon.', 'u. Bestäm bindningsenergin per nukleon.')]},
    '9.392': {'ers': [('</p><p>Massdefekten är 0,17507 u.', ' Massdefekten är 0,17507 u.')]},
    '9.397': {'ers': [('</p><p>Bindningsenergin är 1,118 GeV.', ' Bindningsenergin är 1,118 GeV.')]},
    '9.235': {'ers': [('<br>(Ange svaret med fem decimaler.)', '')]},
    '9.391': {'ers': [('2 protoner, 1 neutroner', '2 protoner, 1 neutron'), ('1 protoner, 2 neutroner', '1 proton, 2 neutroner')]},
    '9.65': {'ers': [('b) I en förenklad fissionsmodell ger en uran-238-kärna produkter med 8,50 MeV per nukleon.', 'b) Antag att en uran-238-kärna klyvs och att produkterna har 8,50 MeV per nukleon.'),
                     ('I en förenklad fissionsmodell har alla 238 nukleoner efteråt bindningsenergin 8,50 MeV per nukleon.', 'Antag att kärnan klyvs och att produkterna har bindningsenergin 8,50 MeV per nukleon.')]},
    '9.66': {'ers': [('Modellera kärnan som ett klot och uppskatta kärnmassan till atommassan 55,935 u.', 'Antag att kärnan är ett klot med massan 55,935 u.'),
                     ('Modellera kärnan som ett klot.', 'Antag att kärnan är ett klot.'),
                     ('m³.  Bestäm', 'm³. Bestäm')]},
    '9.234': {'ers': [('I en modell ökar bindningsenergin med 0,85 MeV per nukleon.', 'I en kärnreaktion ökar bindningsenergin med 0,85 MeV per nukleon.'),
                      ('när 1,00 mol sådana kärnor genomgår processen?', 'när 1,00 mol kärnor reagerar?')]},
    '9.211': {'ers': [(r'För nukliden \(^{37}_{17}\mathrm{Cl}\), bestäm antalet neutroner.', r'Hur många neutroner har nukliden \(^{37}_{17}\mathrm{Cl}\)?')]},
    '9.242': {'ers': [(r'För \(^{14}_{6}\mathrm C\), vilket är masstalet?', r'Vilket masstal har \(^{14}_{6}\mathrm C\)?')]},
    '9.214': {'ers': [('Uran-238 har atomnummer 92.', 'Uran-238 har atomnumret 92.')]},
}

b = Bank('fy1')


def texter(u):
    yield u.get('t') or ''
    yield u.get('spelIntro') or ''
    for d in u.get('spelDelar') or []:
        yield d.get('t') or ''
        yield d.get('fraga') or ''


for _id in KONST_IDS:
    alla = ' '.join(texter(b.obj(_id)))
    e = [(a, c) for a, c in KONSTANTER if a in alla]
    if e:
        R.setdefault(_id, {'ers': []})['ers'] = e + R.get(_id, {}).get('ers', [])
