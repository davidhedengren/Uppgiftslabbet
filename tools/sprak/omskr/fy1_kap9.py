# Fy1 kapitel 9 (kärnfysik och strålning), handgranskat 2026-11-17.
# Varje träff i listan k9_traffar (rättningsinstruktioner, flervalsfraser, "sammanlagd", "från vila",
# "en elev", "på X kg") är läst och beslutad per uppgift nedan. Enheten visas i Kunskapsgymmet via
# svarEnhet, så "(Svara i X.)" tas bort när X är uppgiftens svarEnhet.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

ALT = ['Markera det korrekta alternativet.', '(Välj ett alternativ.)']

# Uppgifter där "(Svara i …)" bara upprepar svarEnhet (granskat mot listan): tas bort.
SVARA_BORT = {
    '9.153': 'mJ', '9.122': 'procent', '9.9': 'J', '9.12': 'keV', '9.13': 'cm', '9.14': 'timmar', '9.165': 'µSv',
    '9.166': 'µSv/h', '9.16': 'mil', '9.21': 'C med rätt tecken', '9.27': 'µg', '9.128': 'minuter', '9.31': 'u',
    '9.218': 'MeV', '9.220': 'MeV', '9.132': 'procent', '9.221': 'MeV', '9.42': 'MW', '9.168': 'mJ', '9.169': 'µSv/h',
    '9.46': 'kg/s', '9.56': 'GBq', '9.57': 'kBq', '9.140': 'timmar', '9.222': 'MeV', '9.227': 'MeV', '9.230': 'MeV',
    '9.233': 'MeV', '9.65': 'MeV', '9.234': 'J', '9.236': 'MeV', '9.237': 'MeV', '9.68': 'MeV', '9.239': 'MeV',
    '9.80': 'miljarder år', '9.145': 'timmar', '9.88': 'minuter', '9.171': 'µSv/h', '9.91': 'µSv/h', '9.175': 'µSv/h',
    '9.179': 'µSv', '9.93': 'cm', '9.183': 'µSv/h', '9.184': 'cm', '9.185': 'µSv', '9.96': 'µSv/h', '9.188': 'timmar',
    '9.191': 'µSv', '9.98': 'µSv', '9.192': 'µSv', '9.103': 'MWh', '9.104': 'mg', '9.201': 'MW', '9.119': 'MeV',
    '9.389': 'u', '9.390': 'MeV', '9.396': 'MeV', '9.398': 'MeV', '9.400': 'MeV', '9.407': 'J', '9.408': 'kg',
    '9.409': 'kg', '9.411': 'J', '9.413': 's', '9.253': 'minuter', '9.255': 'procent', '9.332': 'år', '9.333': 'minuter',
    '9.339': 'timmar', '9.341': 'Bq', '9.346': 'Bq', '9.350': 'kg', '9.353': 'kg', '9.359': 'J', '9.360': 'W',
    '9.424': 'år', '9.427': 'år', '9.259': 'µSv', '9.363': 'K', '9.370': 'dygn', '9.372': 'µSv', '9.373': 'J',
    '9.374': 'timmar', '9.261': 'enheten e', '9.262': 'enheten e', '9.263': 'enheten e', '9.264': 'enheten e',
    '9.265': 'enheten e', '9.417': 'kg/s', '9.418': 'J', '9.420': 'som en kvot', '9.296': 'MBq', '9.298': 'keV',
    '9.300': 'procent', '9.302': 'MBq', '9.437': 'procent', '9.439': 'h', '9.440': 'MBq', '9.441': 'med ett antal',
    '9.448': 'med ett heltal', '9.458': 'GeV', '9.459': 'pJ', '9.460': 'MW', '9.461': 'MeV', '9.467': 'MeV',
    '9.468': 'GJ', '9.470': 'µJ', '9.471': 'MeV', '9.475': 'MHz', '9.476': 'cm', '9.477': 'eV', '9.478': 'eV',
    '9.481': 'keV', '9.484': 'procent', '9.485': 'cm', '9.492': 'cm', '9.503': 'MeV', '9.504': 'MBq', '9.505': 'grader',
    '9.509': 'h', '9.513': 'dygn', '9.518': 'MeV', '9.519': 'GJ', '9.523': 'u', '9.524': 'enheten e', '9.525': 'procent',
    '9.526': 'pm', '9.527': 'pm', '9.531': 'nN', '9.537': 'MeV', '9.539': 'nm', '9.541': 'nm', '9.542': 'pm',
    '9.544': 'procent', '9.545': 'cm', '9.546': 'procent', '9.549': 'cm', '9.550': 'MBq', '9.551': 'h', '9.552': 'MBq',
    '9.553': 'mSv', '9.554': 'pm', '9.555': 'kV', '9.557': 'MeV', '9.558': 'MeV', '9.560': 'MeV', '9.563': 'MeV',
    '9.564': 'TJ', '9.566': 'MeV', '9.567': 'MeV', '9.568': 'procent', '9.570': 'MeV med två decimaler',
    '9.571': 'MeV', '9.572': 'u', '9.574': 'MeV', '9.575': 'MeV', '9.576': 'kJ', '9.577': 'cm',
    '9.580': 'eV med en decimal', '9.583': 'pm', '9.585': 'keV',
}
# 9.58 och 9.94 har två olika instruktioner.
SVARA_FLERA = {'9.58': ['kBq', 'minuter'], '9.94': ['mSv', 'µSv']}

# Instruktioner som rättningen behöver: flyttas till kgInstruktion.
TILL_KG = {
    '9.49': ('(Svara i den ordningen.)', 'Svara i den ordningen.'),
    '9.337': ('(Svara som decimaltal.)', 'Svara i decimalform.'),
    '9.340': ('(Svara som bråk eller decimaltal.)', 'Svara med bråk eller decimaltal.'),
    '9.582': ('(Svara med två heltal.)', 'Svara med två heltal.'),
}

# Handskrivna meningsbyten.
EXTRA = {
    '9.8': [('sammanlagda vilomassa', 'totala vilomassa')],
    '9.10': [('sammanlagda massa', 'totala massa')],
    '9.15': [('den sammanlagda ekvivalenta dosen', 'den totala ekvivalenta dosen')],
    '9.31': [('Vilken sammanlagd massa har en fri väteatom och en fri neutron?', 'Hur stor massa har en fri väteatom och en fri neutron tillsammans?')],
    '9.150': [('deras sammanlagda aktivitet', 'deras totala aktivitet')],
    '9.89': [('Bestäm den sammanlagda ekvivalenta dosen i mSv.', 'Hur stor är den totala ekvivalenta dosen?')],
    '9.178': [('Bestäm den sammanlagda ekvivalenta dosen i mSv.', 'Hur stor är den totala ekvivalenta dosen?')],
    '9.186': [('Bestäm den sammanlagda ekvivalenta dosen i mSv.', 'Hur stor är den totala ekvivalenta dosen?')],
    '9.189': [('Bestäm den sammanlagda ekvivalenta dosen i mSv.', 'Hur stor är den totala ekvivalenta dosen?')],
    '9.111': [('Plutonium-239 alfasönderfaller från vila till uran-235 och helium-4.', 'En stillastående plutonium-239-kärna alfasönderfaller till uran-235 och helium-4.'),
              ('En kärna sönderfaller från vila i två partiklar.', 'En stillastående kärna sönderfaller i två partiklar.'),
              ('Plutonium-239 alfasönderfaller från vila.', 'En stillastående plutonium-239-kärna alfasönderfaller.')],
    '9.119': [('den sammanlagda rörelseenergin', 'den totala rörelseenergin'),
              ('Radium-226 alfasönderfaller från vila.', 'En stillastående radium-226-kärna alfasönderfaller.'),
              ('deras sammanlagda rörelseenergi i MeV', 'deras totala rörelseenergi')],
    'GY25-FY1-STD-02': [('deras sammanlagda laddning', 'deras totala laddning')],
    'GY25-FY1-VET-02': [('En elev säger att', 'Ali säger att')],
    '9.389': [('den sammanlagda massan hos fyra fria väteatomer och tre fria neutroner', 'den totala massan hos fyra fria väteatomer och tre fria neutroner'),
              ('den sammanlagda massan hos fyra väteatomer och tre neutroner', 'den totala massan hos fyra väteatomer och tre neutroner')],
    '9.403': [('Bestäm fragmentens sammanlagda atommassa i u.', 'Hur stor är fragmentens totala atommassa?')],
    '9.372': [('Den sammanlagda dosen', 'Den totala dosen')],
    '9.373': [('Hur stor sammanlagd energi avges', 'Hur stor energi avges totalt')],
    '9.385': [('En tumör på 0,015 kg', 'En tumör med massan 0,015 kg')],
    '9.386': [('En kropp på 62 kg', 'En person som väger 62 kg')],
    '9.298': [('Hur stor är den sammanlagda energin hos fotonerna?', 'Hur stor är fotonernas totala energi?')],
    '9.438': [('Hur stor blir den sammanlagda dosen där?', 'Hur stor blir den totala dosen där?')],
    '9.449': [('En elev säger:', 'Saga säger:')],
    '9.451': [('den sammanlagda elektriska laddningen noll', 'den totala elektriska laddningen noll')],
    '9.490': [('En elev undersöker en strålkälla.', 'Oscar undersöker en strålkälla.')],
    '9.508': [('Hur stor blir den sammanlagda dosen i tumören?', 'Hur stor blir den totala dosen i tumören?')],
    '9.523': [('Den sammanlagda massan före', 'Den totala massan före')],
}


def texter(u):
    yield u.get('t') or ''
    yield u.get('spelIntro') or ''
    for d in u.get('spelDelar') or []:
        yield d.get('t') or ''
        yield d.get('fraga') or ''


def bort(u, fras):
    """Hitta hur frasen sitter i texten och ta bort den med rätt mellanrum eller stycke."""
    alla = ' '.join(texter(u))
    for v in (f'<p>{fras}</p>', f' {fras}', f'{fras} ', fras):
        if v in alla:
            return (v, '')
    return None  # redan borttagen (omkörning)


b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') != 9:
        continue
    id_ = u['id']
    ers, kg = [], None
    alla = ' '.join(texter(u))
    for f in ALT:
        if f in alla:
            ers.append(bort(u, f))
    for x in ([SVARA_BORT[id_]] if id_ in SVARA_BORT else []) + SVARA_FLERA.get(id_, []):
        fr = f'(Svara {x}.)' if x.startswith(('som ', 'med ')) else f'(Svara i {x}.)'
        ers.append(bort(u, fr))
    if id_ in TILL_KG:
        fr, kg = TILL_KG[id_]
        ers.append(bort(u, fr))
    ers += [e for e in EXTRA.get(id_, []) if e[0] in alla]
    ers = [e for e in ers if e]
    if ers or kg:
        R[id_] = {'ers': ers}
        if kg:
            R[id_]['kg'] = kg

# "Räkna bara med (det) radioaktiva sönderfall(et)" (granskat 2026-11-17).
for _id, _a, _c in [('9.296', 'Räkna bara med radioaktivt sönderfall.', 'Bortse från att kroppen gör sig av med ämnet på andra sätt.'),
                    ('9.440', ' Räkna bara med radioaktivt sönderfall.', ''),
                    ('9.443', ' Räkna bara med radioaktivt sönderfall.', ''),
                    ('9.550', ' Räkna bara med det radioaktiva sönderfallet.', '')]:
    if _a in ' '.join(texter(b.obj(_id))):
        R.setdefault(_id, {'ers': []})['ers'].append((_a, _c))
R.setdefault('9.49', {'ers': []})['d'] = {'c': {'kg': 'Svara i den ordningen.'}}
R['9.49']['kg'] = 'Svara i den ordningen.'
