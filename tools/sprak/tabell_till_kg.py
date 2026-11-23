"""Tabellvärden bort ur Uppgiftslabbets uppgiftstext och in i kgInstruktion (användarbeslut 2026-11-23).

Användaren: ”I kunskapsgymmet kan du ha kvar tabellvärdena så det stämmer med facit, i uppgiftslabbet vill jag inte
att något sånt ska stå, det ska de slå upp själva. I uppgiftslabbet vill jag ha uppgifterna så ”rena” som möjligt.”

Uppgiftslabbet visar bara huvudtexten `t` (och facit). Delkort och `spelIntro` visas bara i Kunskapsgymmet och
ändras därför inte. En mening flyttas från `t` till `kgInstruktion` (som Kunskapsgymmet lägger sist i texten) när
den bara består av tabellvärden: specifik värmekapacitet, smält- och ångbildningsvärme, densitet, resistivitet,
ljudets fart, brytningsindex för vatten/is/luft/vakuum, tyngdacceleration på månen och Mars och halveringstider för
namngivna nuklider. Värdet måste stämma med tabellvärdet (inom några procent), annars är det uppgiftens egna data och
står kvar. Uppgiftsdata (glasets brytningsindex, oljans densitet, en okänd nuklids halveringstid) står kvar.

Inbäddade värden (”… kvicksilver med densiteten 13 600 kg/m³.”, ”vatten (brytningsindex 1,33)”) tas bort ur
meningen och skrivs som egen mening i kgInstruktion.

  python tools/sprak/tabell_till_kg.py fy1|fy2 [--visa N] [--rest] [--skriv]
"""
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import svar_till_kg as S  # noqa: E402

ROOT = S.ROOT
FIL = {'fy1': 'uppgifter.js', 'fy2': 'uppgifter2.js'}

# ämne: (grundform, genitiv)
AMNE = {
    'vatten': 'Vattnets', 'is': 'Isens', 'ånga': 'Ångans', 'vattenånga': 'Vattenångans', 'koppar': 'Kopparns',
    'aluminium': 'Aluminiumets', 'järn': 'Järnets', 'bly': 'Blyets', 'silver': 'Silvrets', 'guld': 'Guldets',
    'mässing': 'Mässingens', 'tenn': 'Tennets', 'zink': 'Zinkens', 'stål': 'Stålets', 'etanol': 'Etanolens',
    'kvicksilver': 'Kvicksilvrets', 'luft': 'Luftens', 'havsvatten': 'Havsvattnets', 'helium': 'Heliumets',
    'vätgas': 'Vätgasens', 'konstantan': 'Konstantanets', 'volfram': 'Volframets', 'nikrom': 'Nikromets',
}
GEN = {}
for grund, gen in AMNE.items():
    for g in {gen, gen.lower(), grund.capitalize() + 's', grund + 's'}:
        GEN[g] = grund
GEN.update({'Koppars': 'koppar', 'koppars': 'koppar', 'Aluminiums': 'aluminium', 'aluminiums': 'aluminium',
            'Järns': 'järn', 'järns': 'järn', 'Blys': 'bly', 'blys': 'bly', 'Zinkets': 'zink', 'zinkets': 'zink'})
# Tabellvärden i SI-grundenhet: J/(kg·K), J/kg, kg/m³, Ωm, m/s, (index), m/s², s
AR = 365.25 * 24 * 3600
TAB = {
    ('c', 'vatten'): [4180, 4190, 4186], ('c', 'is'): [2100, 2200, 2090], ('c', 'ånga'): [2000, 1900, 2010],
    ('c', 'vattenånga'): [2000, 1900, 2010],
    ('c', 'koppar'): [385, 390, 387], ('c', 'aluminium'): [900, 897, 880], ('c', 'järn'): [450, 449, 460],
    ('c', 'bly'): [129, 130, 128], ('c', 'silver'): [235, 236, 240], ('c', 'guld'): [129, 130],
    ('c', 'mässing'): [380, 377, 385], ('c', 'tenn'): [220, 228], ('c', 'zink'): [390, 388],
    ('c', 'stål'): [460, 450, 470, 490, 500], ('c', 'etanol'): [2430, 2440, 2400],
    ('L', 'is'): [334e3, 333e3, 335e3], ('L', 'vatten'): [334e3], ('L', 'bly'): [23e3, 24.7e3, 25e3],
    ('L', 'silver'): [105e3, 88e3, 104e3], ('L', 'koppar'): [205e3, 209e3, 207e3], ('L', 'aluminium'): [397e3, 400e3, 398e3],
    ('L', 'järn'): [276e3, 247e3, 270e3], ('L', 'tenn'): [59e3, 60e3], ('L', 'guld'): [64e3, 63e3],
    ('Lå', 'vatten'): [2260e3, 2257e3, 2256e3], ('Lå', 'etanol'): [840e3, 850e3],
    ('rho', 'vatten'): [1000, 998], ('rho', 'is'): [917, 920, 916, 900], ('rho', 'havsvatten'): [1025, 1030, 1020],
    ('rho', 'kvicksilver'): [13600, 13550, 13500, 13590], ('rho', 'luft'): [1.29, 1.2, 1.3, 1.23, 1.225, 1.25, 1.21],
    ('rho', 'helium'): [0.18, 0.179, 0.17], ('rho', 'vätgas'): [0.09, 0.0899], ('rho', 'järn'): [7870, 7860, 7900, 7800],
    ('rho', 'koppar'): [8920, 8960, 8900, 8930, 8940], ('rho', 'bly'): [11340, 11300, 11350, 11400], ('rho', 'aluminium'): [2700, 2699],
    ('rho', 'guld'): [19300, 19320], ('rho', 'silver'): [10500, 10490], ('rho', 'stål'): [7800, 7850, 7900],
    ('rho', 'etanol'): [790, 789], ('rho', 'mässing'): [8500, 8400, 8600], ('rho', 'zink'): [7140, 7130],
    ('rho', 'tenn'): [7300, 7290],
    ('res', 'koppar'): [1.7e-8, 1.68e-8, 1.72e-8, 1.69e-8], ('res', 'järn'): [9.7e-8, 1.0e-7, 9.6e-8, 9.8e-8],
    ('res', 'aluminium'): [2.7e-8, 2.65e-8, 2.8e-8, 2.82e-8], ('res', 'silver'): [1.6e-8, 1.59e-8],
    ('res', 'konstantan'): [4.9e-7, 5.0e-7, 4.4e-7], ('res', 'volfram'): [5.5e-8, 5.6e-8], ('res', 'nikrom'): [1.1e-6, 1.0e-6, 1.5e-6],
    ('v', 'luft'): [340, 343, 330, 344, 342, 331], ('v', 'vatten'): [1480, 1500, 1450, 1490, 1482],
    ('n', 'vatten'): [1.33], ('n', 'is'): [1.31], ('n', 'luft'): [1.00, 1.0003], ('n', 'vakuum'): [1.0],
    ('g', 'månen'): [1.62, 1.6, 1.63, 1.625], ('g', 'mars'): [3.7, 3.71, 3.72, 3.73], ('g', 'jupiter'): [24.8, 24.79, 25],
    ('T', 'kol-14'): [5730 * AR, 5700 * AR], ('T', 'kobolt-60'): [5.27 * AR, 5.3 * AR, 5.26 * AR],
    ('T', 'jod-131'): [8.02 * 86400, 8.0 * 86400, 8.04 * 86400], ('T', 'cesium-137'): [30 * AR, 30.2 * AR, 30.1 * AR],
    ('T', 'radium-226'): [1600 * AR], ('T', 'radon-222'): [3.82 * 86400, 3.8 * 86400, 3.83 * 86400],
    ('T', 'strontium-90'): [28.8 * AR, 29 * AR, 28.9 * AR], ('T', 'tritium'): [12.3 * AR], ('T', 'väte-3'): [12.3 * AR],
    ('T', 'kalium-40'): [1.25e9 * AR, 1.3e9 * AR, 1.28e9 * AR], ('T', 'uran-238'): [4.47e9 * AR, 4.5e9 * AR, 4.468e9 * AR],
    ('T', 'plutonium-239'): [24100 * AR, 24000 * AR, 24110 * AR], ('T', 'americium-241'): [432 * AR, 433 * AR, 432.2 * AR],
    ('T', 'teknetium-99m'): [6.0 * 3600, 6.01 * 3600], ('T', 'fosfor-32'): [14.3 * 86400, 14.0 * 86400],
}
TOL = {'rho': 0.05, 'v': 0.01, 'n': 0.005, 'g': 0.03}

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')
NUM = (r'(?:\\\([^()]*?\\\)|[−-]?\d[\d  ]*(?:,\d+)?(?:\s?[·⋅×]\s?10(?:[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+|\^\{?-?\d+\}?))?)')
ENH = {
    'J/(kg·K)': 1, 'J/(kg⋅K)': 1, 'J/(kg·°C)': 1, 'J/(kg °C)': 1, 'J/(kg·℃)': 1, 'J/kg·K': 1, 'J/(kg K)': 1,
    'kJ/(kg·K)': 1e3, 'kJ/(kg⋅K)': 1e3, 'kJ/(kg·°C)': 1e3, 'kJ/kg·K': 1e3, 'kJ/(kg K)': 1e3,
    'kJ/kg': 1e3, 'J/kg': 1, 'MJ/kg': 1e6,
    'kg/m³': 1, 'kg/m^3': 1, 'g/cm³': 1e3, 'kg/dm³': 1e3, 'kg/L': 1e3, 'kg/l': 1e3, 'kg/liter': 1e3, 'kg/dm3': 1e3, 'g/L': 1, 'g/dm³': 1,
    'Ωm': 1, 'Ω·m': 1, 'Ω m': 1, 'Ω⋅m': 1, 'Ωmm²/m': 1e-6, 'Ω·mm²/m': 1e-6,
    'm/s²': 1, 'm/s^2': 1, 'm/s': 1, 'km/s': 1e3,
    'år': AR, 'dygn': 86400, 'dagar': 86400, 'timmar': 3600, 'h': 3600, 'minuter': 60, 'min': 60, 's': 1,
}
ENH_RX = '(?:' + '|'.join(re.escape(e) for e in sorted(ENH, key=len, reverse=True)) + ')'
PROP = {
    'specifika värmekapacitet': 'c', 'specifik värmekapacitet': 'c', 'specifika värmekapaciteten': 'c',
    'värmekapacitet': 'c', 'smältvärme': 'L', 'smältvärmet': 'L', 'specifika smältvärme': 'L',
    'ångbildningsvärme': 'Lå', 'ångbildningsvärmet': 'Lå', 'specifika ångbildningsvärme': 'Lå',
    'förångningsvärme': 'Lå', 'densitet': 'rho', 'densiteten': 'rho', 'resistivitet': 'res', 'resistiviteten': 'res',
    'brytningsindex': 'n', 'brytningsindexet': 'n', 'halveringstid': 'T', 'halveringstiden': 'T',
}
PROP_RX = '(?:' + '|'.join(re.escape(p) for p in sorted(PROP, key=len, reverse=True)) + ')'
GEN_RX = '(?:' + '|'.join(re.escape(g) for g in sorted(GEN, key=len, reverse=True)) + ')'
GRUND_RX = '(?:' + '|'.join(re.escape(g) for g in sorted(list(AMNE) + ['vakuum'], key=len, reverse=True)) + ')'
NUKLID = {'Kol-14': 'kol-14', 'C-14': 'kol-14', 'Kobolt-60': 'kobolt-60', 'Co-60': 'kobolt-60', 'Jod-131': 'jod-131',
          'I-131': 'jod-131', 'Cesium-137': 'cesium-137', 'Cs-137': 'cesium-137', 'Radium-226': 'radium-226',
          'Radon-222': 'radon-222', 'Strontium-90': 'strontium-90', 'Tritium': 'tritium', 'Kalium-40': 'kalium-40',
          'Uran-238': 'uran-238', 'U-238': 'uran-238', 'Plutonium-239': 'plutonium-239', 'Americium-241': 'americium-241',
          'Teknetium-99m': 'teknetium-99m', 'Fosfor-32': 'fosfor-32'}


def tal(txt):
    t = txt.strip()
    if t.startswith('\\('):
        t = t[2:-2]
        t = t.replace('{,}', ',').replace('\\cdot', '·').replace('\\,', '').replace('{', '').replace('}', '')
        t = re.sub(r'10\^(-?\d+)', lambda m: '10^' + m.group(1), t)
    t = t.replace('−', '-').replace(' ', '').replace(' ', '')
    m = re.fullmatch(r'(-?\d+(?:,\d+)?)(?:[·⋅×]10(?:\^)?(-?\d+))?', t.translate(SUP))
    if not m:
        return None
    v = float(m.group(1).replace(',', '.'))
    if m.group(2):
        v *= 10 ** int(m.group(2))
    return v


def stammer(prop, amne, num, enh):
    v = tal(num)
    if v is None or enh not in ENH:
        return False
    v *= ENH[enh]
    ref = TAB.get((prop, amne))
    if not ref:
        return False
    tol = TOL.get(prop, 0.04)
    return any(abs(v - r) <= tol * abs(r) + 1e-30 for r in ref)


VIDT = r'(?: vid (?:\d+(?:,\d+)? ?°C|rumstemperatur))?'
SATS = [
    # Vattnets specifika värmekapacitet är 4180 J/(kg·K)   /  … och heliumets (densitet) 0,178 kg/m³  /  dess …
    re.compile(r'(?P<gen>' + GEN_RX + r'|dess)(?: (?P<prop>' + PROP_RX + r'))?(?: (?:i (?P<fas>fast|flytande) form))?' + VIDT + r'(?: (?:är|=))? (?:ungefär |cirka )?(?P<num>' + NUM + r') ?(?P<enh>' + ENH_RX + r')' + VIDT + r'$'),
    # Koppar har densiteten 8,96 g/cm³
    re.compile(r'(?P<grund>' + GRUND_RX.replace('(?:', '(?:(?i:', 1) + r')) har (?:en |den |ett )?(?P<prop>' + PROP_RX + r') (?:ungefär |cirka |omkring )?(?P<num>' + NUM + r') ?(?P<enh>' + ENH_RX + r')?$'),
    # Ljudets fart (i luft) är 340 m/s
    re.compile(r'(?:[Ll]judets (?:fart|hastighet)|[Ll]judfarten)(?: i (?P<grund>luft|vatten))? (?:är|=) (?:ungefär |cirka )?(?P<num>' + NUM + r') ?(?P<enh>m/s)$'),
    # Tyngdaccelerationen (på månen) är 1,62 m/s² (på månen)
    re.compile(r'[Tt]yngdaccelerationen(?: på (?P<pl1>månen|Mars|Jupiter))? (?:är|=) (?P<num>' + NUM + r') ?(?P<enh>m/s²|m/s\^2)(?: på (?P<pl2>månen|Mars|Jupiter))?$'),
    # Kol-14 har halveringstiden 5730 år
    re.compile(r'(?P<nuk>' + '|'.join(re.escape(n) for n in NUKLID) + r')(?: \([^)]*\))? har (?:en )?halveringstid(?:en)? (?:på )?(?P<num>' + NUM + r') ?(?P<enh>år|dygn|dagar|timmar|h|minuter|min)$'),
    # (… och) resistiviteten 1,7·10⁻⁸ Ωm / smältvärmet är 105 kJ/kg – ämnet från förra satsen
    re.compile(r'(?P<prop>' + PROP_RX + r')(?: (?:är|=))? (?P<num>' + NUM + r') ?(?P<enh>' + ENH_RX + r')$'),
    # (Aluminium har densiteten 2,70 g/cm³ och) stål 7,80 g/cm³ – egenskapen från förra satsen
    re.compile(r'(?P<grund>' + GRUND_RX + r') (?P<num>' + NUM + r') ?(?P<enh>' + ENH_RX + r')$'),
    # Resistiviteten är 1,7·10⁻⁸ Ωm för koppar (och 2,7·10⁻⁸ Ωm för aluminium)
    re.compile(r'(?:(?P<prop>[Rr]esistiviteten|[Dd]ensiteten|[Dd]en specifika värmekapaciteten) är )?(?P<num>' + NUM + r') ?(?P<enh>' + ENH_RX + r') för (?P<grund>' + GRUND_RX + r')$'),
]
DENS_LISTA = re.compile(r'(?P<prop>Densitet|Densiteter|Specifik värmekapacitet|Resistivitet): (?P<rest>.+)$')
LISTPOST = re.compile(r'(?P<grund>' + GRUND_RX + r') (?P<num>' + NUM + r')(?: ?(?P<enh>' + ENH_RX + r'))?$')
EGEN = re.compile(r'(?:[Tt]rycket|[Ll]ufttrycket|[Yy]ttrycket|[Ee]lpriset|[Ll]edningen|[Ff]lotten|[Bb]allonghöljet|[Tt]emperaturen)\b[^,]* (?:är|har|antas)\b.*')


def sats_ok(s, forra):
    """forra = (prop, amne) från förra satsen. Returnerar ((prop, amne), ok, fristaende)."""
    fprop, famne = forra
    for i, rx in enumerate(SATS):
        m = rx.fullmatch(s)
        if not m:
            continue
        d = m.groupdict()
        enh = d.get('enh') or ''
        if i == 0:
            amne = famne if d['gen'] == 'dess' else GEN[d['gen']]
            prop = PROP[d['prop']] if d.get('prop') else fprop
            if prop is None or amne is None:
                return (None, None), False, False
            if d.get('fas') == 'fast' and amne == 'vatten':
                amne = 'is'
            return (prop, amne), stammer(prop, amne, d['num'], enh), bool(d.get('prop')) and d['gen'] != 'dess'
        if i == 1:
            amne = d['grund'].lower()
            prop = PROP[d['prop']]
            if prop == 'n':
                v = tal(d['num'])
                return (prop, amne), v is not None and any(abs(v - r) <= 0.005 for r in TAB.get(('n', amne), [])), True
            return (prop, amne), stammer(prop, amne, d['num'], enh), True
        if i == 2:
            return ('v', None), stammer('v', d.get('grund') or 'luft', d['num'], enh), True
        if i == 3:
            pl = (d.get('pl1') or d.get('pl2') or '').lower()
            return ('g', None), bool(pl) and stammer('g', pl, d['num'], enh.replace('^2', '²')), True
        if i == 4:
            return ('T', None), stammer('T', NUKLID[d['nuk']], d['num'], enh), True
        if i == 5:
            prop = PROP.get(d['prop'].lower(), PROP.get(d['prop']))
            return (prop, famne), famne is not None and stammer(prop, famne, d['num'], enh), False
        if i == 6:
            amne = d['grund']
            return (fprop, amne), fprop is not None and stammer(fprop, amne, d['num'], enh), False
        if i == 7:
            p = (d.get('prop') or '').lower()
            prop = {'resistiviteten': 'res', 'densiteten': 'rho', 'den specifika värmekapaciteten': 'c'}.get(p, fprop)
            return (prop, d['grund']), prop is not None and stammer(prop, d['grund'], d['num'], enh), False
    m = DENS_LISTA.fullmatch(s)
    if m:
        prop = {'Densitet': 'rho', 'Densiteter': 'rho', 'Specifik värmekapacitet': 'c', 'Resistivitet': 'res'}[m.group('prop')]
        poster = [p.strip() for p in re.split(r', | och ', m.group('rest'))]
        enh = None
        for p in reversed(poster):
            mm = LISTPOST.fullmatch(p)
            if not mm:
                return (prop, None), False, False
            enh = mm.group('enh') or enh
            if not enh or not stammer(prop, mm.group('grund'), mm.group('num'), enh):
                return (prop, None), False, False
        return (prop, None), True, True
    return (None, None), False, False


def dela_mening(men):
    """(kg-text eller None, behållen text eller None). Hela meningen tabell → (men, None)."""
    satser = [x.strip() for x in re.split(r', och |, | och (?=(?:' + GEN_RX + r'|dess|[Ll]judets|[Tt]yngdacc|[Ll]ufttrycket|'
                                          r'[Yy]ttrycket|[Ee]lpriset|[Ll]edningen|[Ff]lotten|[Bb]allonghöljet|'
                                          r'[Tt]emperaturen|[Tt]rycket|' + PROP_RX + r'|' + GRUND_RX + r'|\d|\\\())', men)]
    if DENS_LISTA.fullmatch(men):
        _, ok, _ = sats_ok(men, (None, None))
        return (men, None) if ok else (None, None)
    forra = (None, None)
    tab, egen = [], []
    for s in satser:
        forra, ok, fri = sats_ok(s, forra)
        if ok:
            tab.append((s, fri))
        elif EGEN.fullmatch(s):
            egen.append(s)
            forra = (None, None)
        else:
            return None, None
    if not egen:
        return men, None
    if not all(fri for _, fri in tab):
        return None, None
    stor = lambda x: x[0].upper() + x[1:]
    # ”vattnets densitet 1000 kg/m³” blir en egen mening: lägg till ”är”
    tab = [(re.sub(r'^(' + GEN_RX + r' ' + PROP_RX + r') (?!är )', r'\1 är ', x), f) for x, f in tab]
    return stor(' och '.join(s for s, _ in tab)), stor(' och '.join(egen))


def mening_ok(men):
    kg, _ = dela_mening(men)
    return kg is not None


TABORD = re.compile(r'värmekapacitet|smältvärme|ångbildningsvärme|förångningsvärme|densitet|resistivitet|'
                    r'brytningsindex|halveringstid|[Ll]judets (?:fart|hastighet)|[Tt]yngdacceleration', re.I)
# Inbäddat: ”… kvicksilver med densiteten 13 600 kg/m³” och ”vatten (brytningsindex 1,33)”
BESTAMD = {'vattnet': 'vatten', 'isen': 'is', 'luften': 'luft', 'kvicksilvret': 'kvicksilver'}
INBADD = re.compile(r'(?P<grund>(?i:vattnet|isen|luften|kvicksilvret)|' + GRUND_RX.replace('(?:', '(?:(?i:', 1) + r'))(?P<del> med (?:en |den )?(?P<prop>densiteten|brytningsindex(?:et)?|'
                    r'resistiviteten|specifika värmekapaciteten) (?P<num>' + NUM + r') ?(?P<enh>' + ENH_RX + r')?'
                    r'| \((?:(?P<prop2>densitet(?:en)?|brytningsindex|n) =? ?)?(?P<num2>' + NUM + r') ?(?P<enh2>' + ENH_RX + r')?\))(?=[ .,?<])')
PROPNAMN = {'c': 'specifika värmekapacitet', 'rho': 'densitet', 'n': 'brytningsindex', 'res': 'resistivitet'}


def inbaddat(men):
    """Tar bort inbäddade tabellvärden. Returnerar (ny mening, [kg-meningar])."""
    kg = []

    def ers(m):
        d = m.groupdict()
        grund = BESTAMD.get(d['grund'].lower(), d['grund'].lower())
        enh0 = d.get('enh') or d.get('enh2') or ''
        prop_txt = d.get('prop') or d.get('prop2') or ('densitet' if enh0 in ('kg/m³', 'g/cm³', 'kg/L', 'kg/dm³') else 'n' if not enh0 else 'okänd')
        if prop_txt == 'okänd':
            return m.group(0)
        num = d.get('num') or d.get('num2')
        enh = d.get('enh') or d.get('enh2') or ''
        prop = 'n' if prop_txt in ('n', 'brytningsindex', 'brytningsindexet') else PROP.get(prop_txt, 'rho' if 'densitet' in prop_txt else None)
        if prop == 'n':
            v = tal(num)
            ok = v is not None and any(abs(v - r) <= 0.005 for r in TAB.get(('n', grund), []))
        else:
            ok = stammer(prop, grund, num, enh)
        if not ok or grund not in AMNE:
            return m.group(0)
        kg.append(f'{AMNE[grund]} {PROPNAMN[prop]} är {num.strip()}' + (f' {enh}' if enh else '') + '.')
        return m.group('grund')
    ny = INBADD.sub(ers, men)

    def ers2(m):
        prop = PROP[m.group('prop')]
        grund = m.group('grund')
        if not stammer(prop, grund, m.group('num'), m.group('enh')):
            return m.group(0)
        kg.append(f"{AMNE[grund]} {PROPNAMN[prop]} är {m.group('num').strip()} {m.group('enh')}.")
        return m.group('fore')
    return SAMMA.sub(ers2, ny), kg


# ”Teet har samma specifika värmekapacitet som vatten, 4,18 kJ/(kg·K).”
SAMMA = re.compile(r'(?P<fore>samma (?P<prop>specifika värmekapacitet|densitet) som (?P<grund>' + GRUND_RX + r')), (?P<num>'
                   + NUM + r') ?(?P<enh>' + ENH_RX + r')(?=[.])')


def rensa_t(t):
    """(ny t, [kg-meningar], [kvarvarande meningar med tabellord]) – ny t är None om inget ändras."""
    if not isinstance(t, str) or not t:
        return None, [], []
    delar = re.split(r'(<svg[\s\S]*?</svg>)', t)
    kg, rest = [], []
    for i in range(0, len(delar), 2):
        bitar = re.split(r'(<[^>]+>)', delar[i])
        for j in range(0, len(bitar), 2):
            txt = bitar[j]
            # meningar: slutar med punkt följd av mellanslag eller slut (decimalkomma används, så punkt avslutar)
            men = re.split(r'(?<=[.?!])(\s+)', txt)
            ut = []
            for k in range(0, len(men), 2):
                m = men[k]
                sep = men[k + 1] if k + 1 < len(men) else ''
                ren = m.strip()
                if ren.endswith('.') and TABORD.search(ren):
                    kgt, kvar = dela_mening(ren[:-1].strip())
                    if kgt is not None:
                        kg.append(kgt + '.')
                        if kvar is None:
                            continue  # mening och dess mellanslag bort
                        lead = m[:len(m) - len(m.lstrip())]
                        ut.append(lead + kvar + '.' + sep)
                        continue
                if TABORD.search(m) or INBADD.search(m) or SAMMA.search(m):
                    ny, kgi = inbaddat(m)
                    if kgi:
                        kg += kgi
                        m = ny
                    elif TABORD.search(m) and re.search(r'\d', m):
                        rest.append(ren)
                ut.append(m + sep)
            bitar[j] = ''.join(ut)
        delar[i] = ''.join(bitar)
    if not kg:
        return None, [], rest
    # städa bara texten utanför figurerna
    for i in range(0, len(delar), 2):
        d = re.sub(r'<p>\s*</p>', '', delar[i])
        d = re.sub(r'\s+</p>', '</p>', d).replace('<p> ', '<p>')
        delar[i] = re.sub(r'  +', ' ', d)
    ny = ''.join(delar)
    assert re.findall(r'<svg[\s\S]*?</svg>', ny) == re.findall(r'<svg[\s\S]*?</svg>', t)
    if not S.UPPMANING.search(S.plain(ny)):
        return None, [], rest + ['[ingen fråga kvar] ' + S.plain(t)[:150]]
    return ny, kg, rest


STAM = {'vatten': r'vatt|sjö|hav|pool|bassäng|dykar|simm|damm|kran|dusch|kastrull|kokar|te\b|kaffe|\bbad|flod|älv|djup|flyter|nedsänk|ubåt|\bis\b|isen|isbit|smält|frys', 'is': r'\bis|sjöis|snö|frys', 'havsvatten': r'\bhav|ubåt|dykar', 'luft': r'luft|ballong|barometer', 'järn': r'järn', 'koppar': r'koppar', 'aluminium': r'alumin', 'bly': r'bly', 'guld': r'guld', 'silver': r'silver', 'kvicksilver': r'kvicksilv|mmhg|barometer', 'etanol': r'etanol|sprit', 'helium': r'helium', 'vätgas': r'vätgas', 'stål': r'stål', 'zink': r'zink', 'mässing': r'mässing'}


def main():
    namn = sys.argv[1]
    fil = os.path.join(ROOT, FIL[namn])
    src = open(fil, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    nya, resten, oklara = {}, [], []
    for q in bank:
        nt, kg, rest = rensa_t(q.get('t'))
        resten += [(q['id'], r) for r in rest]
        if nt is None:
            continue
        k = json.loads(json.dumps(q))
        k['t'] = nt
        # tabellvärdena först, sedan eventuella svarsinstruktioner
        gammal = (k.get('kgInstruktion') or '').strip()
        unika = list(dict.fromkeys(kg))
        k['kgInstruktion'] = S.ny_kg(' '.join(unika), [gammal] if gammal else [])
        kvar = S.plain(nt).lower()
        for men in unika:
            for g, grund in list(GEN.items()) + [(a, a) for a in AMNE]:
                if re.match(re.escape(g) + r'\b', men, re.I) or re.search(r'[:,] ' + re.escape(grund) + r' ', men):
                    stam = STAM.get(grund, grund[:4])
                    if not re.search(stam, kvar):
                        oklara.append((q['id'], grund, men))
                    break
        # Ett flyttat värde som fortfarande syns i texten (”Visa att ρ = 19,3x + 8,93(1 − x)”) hör till uppgiften
        for men in unika:
            for tal_ in re.findall(r'\d+,\d+|\d{3,}', men.replace('\u00a0', '').replace(' ', '')):
                if len(tal_) >= 4 and tal_ in kvar.replace(' ', ''):
                    oklara.append((q['id'], 'värdet syns i texten', tal_))
        if any(o[0] == q['id'] for o in oklara):
            continue  # ämnet nämns bara i tabellmeningen: står kvar
        nya[q['id']] = (q, k)
    print(namn, len(nya), 'uppgifter,', len(resten), 'kvarvarande meningar med tabellord')
    if '--visa' in sys.argv:
        n = int(sys.argv[sys.argv.index('--visa') + 1])
        for uid, (q, k) in list(nya.items())[:n]:
            print(' ', uid, '|', S.plain(k['t'])[:160], '|| KG:', k.get('kgInstruktion'))
    for o in oklara:
        print(' OKLART ÄMNE', *o)
    if '--rest' in sys.argv:
        for uid, r in resten:
            print(' REST', uid, '|', r[:200])
    if '--skriv' in sys.argv and nya:
        S.skriv(fil, src, bank, nya)


if __name__ == '__main__':
    main()
