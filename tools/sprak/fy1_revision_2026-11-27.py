"""Fy1-revision 2026-11-27: felrapporter, deluppgiftskedjor, densiteter som eleverna slår upp.

Användaren 2026-11-27: ”Fortsätt revidera språket och uppgifterna i fysik 1. Det är många som är lite konstiga. Börja
med dessa felrapporter och gör sedan liknande ändringar i alla uppgifter, samt det som står i instruktionerna.”
Felrapporter 2026-11-27 09:54: 2.110 (konstigt formulerad), 2.84 (”berätta inte densiteterna, detta ska eleverna slå
upp”), 2.82 (”ta bort bortse från möblernas och personernas …”), 2.55 (”a) och b) är samma?”), 2.52 (”frågan kommer
igen i c) men inte b)”), 3.72 (”formulera om”). Dessutom: ”rullgång” ska bli rullband.

Steg (kör i ordning, var och ett med --skriv):
  rapporter   felrapportuppgifterna och rullgång → rullband (3.234, 2.318)
  ...         (fler steg läggs till nedan)

  python tools/sprak/fy1_revision_2026-11-27.py <steg> [--skriv]
"""
import copy
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sprakverktyg import Bank  # noqa: E402


def objekttext(b, id_, ny):
    """Skriv objektet med originalets indragning (samma metod som tools/formagor/regelpass.py)."""
    gammal = b.text(id_)
    if '\n' not in gammal:
        return json.dumps(ny, ensure_ascii=False, separators=(',', ':'))
    m = re.search(r'\n([ \t]*)"', gammal)
    inre = m.group(1) if m else '  '
    slut = re.search(r'\n([ \t]*)\}\s*$', gammal)
    yttre = slut.group(1) if slut else ''
    rader = json.dumps(ny, ensure_ascii=False, indent=2).split('\n')
    return '\n'.join([rader[0]] + [inre + r[2:] for r in rader[1:-1]] + [yttre + rader[-1]])


def byt(s, gammal, ny, n=1):
    assert s.count(gammal) >= n, (gammal[:80], s.count(gammal))
    return s.replace(gammal, ny)


def delkort(u, et):
    return next(d for d in u['spelDelar'] if d['etikett'] == et)


# ---------------------------------------------------------------- steg: rapporter

def r_2_110(u):
    # Fristående kort som hade tappat sitt sammanhang (”av havsvattnet”), med ledtråd om ”deras sammanlagda massa”.
    u['t'] = '<p>Hur stor volym har 206 g havsvatten?</p>'
    u.pop('kgInstruktion', None)
    u['ledtrad'] = '<p>Slå upp havsvattnets densitet. Hur många kubikcentimeter havsvatten väger tillsammans 206 g?</p>'
    # Formelsamlingarna anger 1,03 eller 1,02–1,025 g/cm³ för havsvatten.
    u['svarVardesiffror'] = 3
    u['svarTabell'] = {'0': [round(206 / 1.025, 1), round(206 / 1.02, 1)]}


def r_2_84(u):
    for falt in ('spelIntro',):
        u[falt] = byt(u[falt], ' Aluminiumets densitet är 2,70 g/cm³.', '')
    for d in u['spelDelar']:
        d['t'] = byt(d['t'], ' Aluminiumets densitet är 2,70 g/cm³.', '')
    u.pop('kgInstruktion', None)
    led = '<p>Slå upp aluminiums densitet. Hur många kubikcentimeter aluminium behövs för att massan ska bli 500 g?</p>'
    u['ledtrad'] = led
    delkort(u, 'a')['ledtrad'] = led
    delkort(u, 'b')['ledtrad'] = ('<p>Bestäm först volymen i kubikcentimeter med hjälp av aluminiums densitet och gör '
                                  'sedan om till liter.</p>')


def r_2_82(u):
    bort = ' Bortse från möblernas och personernas volym.'
    u['t'] = byt(u['t'], bort, '')
    u['spelIntro'] = byt(u['spelIntro'], bort, '')
    for d in u['spelDelar']:
        d['t'] = byt(d['t'], bort, '')
    # Precisionen ligger i svarVardesiffror (Fy1-beslut 2026-10-26), inte i en avrundningsinstruktion.
    u['kgInstruktion'] = byt(u['kgInstruktion'], ' Avrunda till hela kilogram.', '')
    u['svarVardesiffror'] = [3, 3]


def r_2_55(u):
    b = delkort(u, 'b')
    b['t'] = byt(b['t'], '<p>Bestäm densiteten.</p>', '<p>Ange densiteten i kg/m³.</p>')
    b['fraga'] = 'Ange densiteten i kg/m³.'
    b['ledtrad'] = '<p>Bestäm densiteten i g/cm³ och gör om enheten. Hur många kilogram per kubikmeter är 1 g/cm³?</p>'


def r_2_52(u):
    # c visade hela situationen igen med 30 kg. Nu börjar alla delkort likadant och ändringen står i frågan.
    c = delkort(u, 'c')
    a_inl = delkort(u, 'a')['t'].split('<p>Bestäm volymen.</p>')[0]
    fr = 'Hur stor blir radien om klotet i stället ska ha massan 30 kg?'
    c['t'] = a_inl + f'<p>{fr}</p>'
    c['fraga'] = fr
    u['t'] = byt(u['t'], 'Bestäm radien om massan i stället är 30 kg.', fr)


def r_3_72(u):
    u['t'] = ('<p>En sten släpps från samma höjd på jorden och på månen. Hur många gånger längre tid tar fallet på '
              'månen? Bortse från luftmotståndet.</p>')
    # Tyngdaccelerationen slås upp: månen 1,62 (även 1,6 och 1,63) och jorden 9,82 (även 9,81) m/s².
    u['svarTabell'] = {'0': [round((9.82 / 1.6) ** 0.5, 4), round((9.82 / 1.63) ** 0.5, 4), round((9.81 / 1.62) ** 0.5, 4)]}
    u['ledtrad'] = ('<p>Skriv falltiden som funktion av höjden och tyngdaccelerationen. Höjden är densamma, så bara '
                    'tyngdaccelerationen skiljer.</p>')


RULL = [
    ('Ett 90 m långt rullband', None), ('En 90 m lång rullgång', 'Ett 90 m långt rullband'),
    ('relativt själva rullgången', 'relativt rullbandet'), ('för en rullgång med längden', 'för ett rullband med längden'),
    ('En rullgång rör sig', 'Ett rullband på en flygplats rör sig'), ('Hur lång är rullgången?', 'Hur långt är rullbandet?'),
    ('Rullgångens', 'Rullbandets'), ('rullgångens', 'rullbandets'), ('rullgången', 'rullbandet'),
    ('Rullgången', 'Rullbandet'), ('rullgång', 'rullband'),
]


def rullband(u):
    s = json.dumps(u, ensure_ascii=False)
    for a, b in RULL:
        if b is not None:
            s = s.replace(a, b)
    ny = json.loads(s)
    u.clear()
    u.update(ny)
    assert 'rullg' not in json.dumps(u, ensure_ascii=False).lower(), u['id']


def r_3_234(u):
    rullband(u)
    u['t'] = byt(u['t'], 'Rullbandets fart u mäts relativt byggnaden. Personens gångfart v mäts relativt rullbandet. '
                         'Anta konstanta gångfarter, omedelbar vändning och L &gt; 0, v &gt; u ≥ 0.',
                 'Rullbandets fart u mäts relativt golvet och personens fart v relativt rullbandet. Vändningen tar '
                 'ingen tid.') if 'L &gt; 0' in u['t'] else byt(
        u['t'], 'Rullbandets fart u mäts relativt byggnaden. Personens gångfart v mäts relativt rullbandet. Anta '
                'konstanta gångfarter, omedelbar vändning och L > 0, v > u ≥ 0.',
        'Rullbandets fart u mäts relativt golvet och personens fart v relativt rullbandet. Vändningen tar ingen tid.')


def r_7_149(u):
    s = json.dumps(u, ensure_ascii=False)
    s = s.replace('Antag att en kropp med massan 65 kg effekten 200 W och bildar ingen ny värme.',
                  'En kropp med massan 65 kg avger värme med effekten 200 W men bildar ingen ny värme.')
    u.clear(); u.update(json.loads(s))


def r_6_454(u):
    s = json.dumps(u, ensure_ascii=False)
    s = s.replace('luftens tryck i röret vara högst en tjugondel av lufttrycket', 'luftens tryck i röret får vara högst '
                  'en tjugondel av lufttrycket')
    u.clear(); u.update(json.loads(s))


def r_2_379(u):
    """Stilguiden: horisontell i stället för vågrät (språktestet sprak-2026-11-17)."""
    s = json.dumps(u, ensure_ascii=False).replace('flyter vågrätt', 'flyter horisontellt').replace(
        'pontonen ligger vågrätt', 'pontonen ligger horisontellt')
    u.clear(); u.update(json.loads(s))


def r_7_117(u):
    s = json.dumps(u, ensure_ascii=False).replace('0,200 kg is vid 0 °C har smält till 65 %.',
                                                  'Av 0,200 kg is vid 0 °C har 65 % smält.')
    u.clear(); u.update(json.loads(s))


def r_9_216(u):
    # Flervalsstam som slutade med ”…”: en hel fråga i lärarens stil, alternativen oförändrade.
    s = json.dumps(u, ensure_ascii=False).replace('Två isotoper av samma grundämne skiljer sig åt i...',
                                                  'Vad skiljer två isotoper av samma grundämne åt?')
    u.clear(); u.update(json.loads(s))


def r_metatext(u):
    """Stilguiden: ingen metatext (”Fördjupning: …”) och ”GeoGebra” i stället för ”digitalt verktyg”."""
    s = json.dumps(u, ensure_ascii=False)
    # ”Fördjupning: …” står kvar: uttryckligt beslut i fellogg-fy1-2026-11-11 (märkt fördjupning).
    s = s.replace('Bestäm höjden med ett digitalt verktyg.', 'Bestäm höjden med GeoGebra.')
    s = s.replace('Lös ekvationen med ett digitalt verktyg.', 'Lös ekvationen med GeoGebra.')
    s = s.replace('Lägg in de fem punkterna i ett digitalt verktyg', 'Lägg in de fem punkterna i GeoGebra')
    s = s.replace('<p><strong></strong></p>', '').replace('<p></p>', '')
    u.clear(); u.update(json.loads(s))


# Stilguiden: undvik ”kropp” om föremål. Människokroppen (medicin, energi, strålskydd) står kvar.
KROPP_FOREMAL = [('En helt nedsänkt, stel kropp', 'Ett helt nedsänkt, stelt föremål'), ('En stel kropp', 'Ett stelt föremål'),
                 ('en stel kropp', 'ett stelt föremål'), ('På en helt nedsänkt kropp', 'På ett helt nedsänkt föremål'),
                 ('På en nedsänkt kropp', 'På ett nedsänkt föremål'), ('På en kropp', 'På ett föremål'),
                 ('en enda kropp', 'ett enda föremål'), ('denna kropp', 'detta föremål'), ('minst en kropp', 'minst ett föremål'),
                 ('Två kroppar', 'Två föremål'), ('En kropp', 'Ett föremål'), ('en kropp', 'ett föremål'),
                 ('Kroppens', 'Föremålets'), ('kroppens', 'föremålets'), ('Kroppen', 'Föremålet'), ('kroppen', 'föremålet'),
                 ('kropparna', 'föremålen'), ('kroppar', 'föremål'),
                 ('accelerationen 9,0 m/s². Den påverkas', 'accelerationen 9,0 m/s². Det påverkas'),
                 ('lyftkraften 12 N i vatten. Den flyttas', 'lyftkraften 12 N i vatten. Det flyttas'),
                 ('densiteten 600 kg/m³. Den hålls stilla', 'densiteten 600 kg/m³. Det hålls stilla')]
KROPP_PERSON = [('Kalium-40 i en kropp med massan 70 kg', 'Kalium-40 i kroppen hos en person med massan 70 kg'),
                ('En kropp med massan', 'En person med massan'), ('En kropp har massan', 'En person har massan'),
                ('en kropp absorberar', 'en person absorberar'), ('absorberar en kropp', 'absorberar en person'),
                ('Hur stor är kroppens massa?', 'Hur stor är personens massa?'), ('kroppens ekvivalenta dos', 'personens ekvivalenta dos')]


def _byt_lista(u, par):
    s = json.dumps(u, ensure_ascii=False)
    for a, b in par:
        s = s.replace(a, b)
    u.clear(); u.update(json.loads(s))


def r_kropp_foremal(u):
    _byt_lista(u, KROPP_FOREMAL)


def r_kropp_person(u):
    _byt_lista(u, KROPP_PERSON)


def r_2_195(u):
    _byt_lista(u, [('En annan klotformad kropp', 'En annan klotformad himlakropp')])


RAPPORTER = {'2.110': r_2_110, '2.84': r_2_84, '2.82': r_2_82, '2.55': r_2_55, '2.52': r_2_52, '3.72': r_3_72,
             '3.234': r_3_234, '2.318': rullband}

# ---------------------------------------------------------------- steg: densitet
#
# 2.84: ”berätta inte densiteterna, detta ska eleverna slå upp.” Sedan 2026-11-23 står tabellvärden inte i
# Uppgiftslabbets text `t`, men Kunskapsgymmet visade dem fortfarande i kgInstruktion, spelIntro och delkortens
# texter. Nu tas densiteter för fasta ämnen och vätskor bort även där. Gasernas densitet (luft, helium, vätgas)
# beror på temperatur och tryck och står kvar. Värdet måste ligga inom 1 % av ett tabellvärde; andra värden
# (vatten 1030 kg/m³ i en saltsjö, oljans densitet) är uppgiftens egna data.
# Svar räknade med andra vanliga tabellvärden godtas: svarTabell får svaret skalat med (ρ_alt/ρ)^±1 för varje
# borttaget ämne, så att en elev som slår upp till exempel 8,92 i stället för 8,96 g/cm³ inte blir underkänd.

import tabell_till_kg as TK  # noqa: E402

GASER = {'luft', 'helium', 'vätgas'}
ALT = {'vatten': [1000, 998], 'havsvatten': [1025, 1030, 1020], 'koppar': [8960, 8920, 8930, 8940],
       'aluminium': [2700, 2699], 'järn': [7870, 7860, 7900, 7800], 'bly': [11300, 11340, 11350],
       'guld': [19300, 19320], 'silver': [10500, 10490], 'stål': [7800, 7850, 7900], 'etanol': [790, 789, 800],
       'mässing': [8500, 8460, 8400, 8600], 'zink': [7130, 7140], 'tenn': [7290, 7300, 7310], 'is': [917, 920, 916],
       'kvicksilver': [13600, 13550, 13590], 'volfram': [19300, 19250, 19260]}
# Ord som visar vilket ämne ett föremål är gjort av: järnkula, isberg, stålblock, blyvikt …
STAM = [(re.compile(r'\b(?:[Jj]ärn)\w*'), 'järn'), (re.compile(r'\b[Ss]tål\w*'), 'stål'), (re.compile(r'\b[Kk]oppar\w*'), 'koppar'),
        (re.compile(r'\b[Bb]ly\w*'), 'bly'), (re.compile(r'\b[Gg]uld\w*'), 'guld'), (re.compile(r'\b[Ss]il(?:ver|vr)\w*'), 'silver'),
        (re.compile(r'\b[Aa]luminium\w*'), 'aluminium'), (re.compile(r'\b[Mm]ässing\w*'), 'mässing'),
        (re.compile(r'\b[Zz]ink\w*'), 'zink'), (re.compile(r'\b[Tt]enn\w*'), 'tenn'), (re.compile(r'\b[Vv]olfram\w*'), 'volfram'),
        (re.compile(r'\b[Kk]vicksilv\w*'), 'kvicksilver'), (re.compile(r'\b[Ee]tanol\w*'), 'etanol'),
        (re.compile(r'\b[Hh]avsvatt\w*'), 'havsvatten'), (re.compile(r'\b(?:[Ss]öt)?[Vv]att(?:en|net|nets)\b'), 'vatten'),
        (re.compile(r'\b[Ii]s(?:en|berg\w*|bit\w*|kub\w*|block\w*|flak\w*)?\b'), 'is')]
FRAS = re.compile(r'(?:,| och| med| som har) (?:en |den )?densiteten (' + TK.NUM + r') ?(' + TK.ENH_RX + r')(?=[ .,?<])')
MAT = re.compile(r'(?<![^\s>])(?:Materialets|Metallens|Ämnets) densitet är (' + TK.NUM + r') ?(' + TK.ENH_RX + r')\.')


def amnen_i(txt):
    return {amne for rx, amne in STAM if rx.search(re.sub(r'<svg.*?</svg>', '', txt or '', flags=re.S))}
DENS_LOGG = {'borttaget': [], 'blandat': [], 'ledtrad': []}


def si(num, enh):
    v = TK.tal(num)
    return None if v is None or enh not in TK.ENH else v * TK.ENH[enh]


def tabellvarde(amne, v):
    return amne in ALT and v is not None and any(abs(v - r) <= 0.01 * r for r in ALT[amne])


def klausuler(men):
    """[(klausul, (prop, amne), ok, värde)] för en mening, samma uppdelning som tabell_till_kg.dela_mening."""
    satser = [x.strip() for x in re.split(r', och |, | och (?=(?:' + TK.GEN_RX + r'|dess|[Ll]judets|[Tt]yngdacc|'
                                          r'[Ll]ufttrycket|[Yy]ttrycket|[Tt]emperaturen|[Tt]rycket|' + TK.PROP_RX + r'|'
                                          + TK.GRUND_RX + r'|\d|\\\())', men)]
    forra, ut = (None, None), []
    for s in satser:
        forra, ok, _ = TK.sats_ok(s, forra)
        ut.append((s, forra, ok))
    return ut


def densitetsmening(men):
    """None om meningen inte är (bara) tabelldensiteter. Annars ('bort', ämnen, värden) eller ('blandat', …)."""
    if not re.search(r'[Dd]ensitet', men):
        return None
    m = TK.DENS_LISTA.fullmatch(men.rstrip('.'))
    if m and m.group('prop') in ('Densitet', 'Densiteter'):
        poster = [p.strip() for p in re.split(r', | och ', m.group('rest'))]
        amnen, enh = [], None
        for p in reversed(poster):
            mm = TK.LISTPOST.fullmatch(p)
            if not mm:
                return None
            enh = mm.group('enh') or enh
            amnen.append((mm.group('grund'), si(mm.group('num'), enh)))
        if any(a in GASER for a, _ in amnen):
            return None
        return ('bort', amnen) if all(tabellvarde(a, v) for a, v in amnen) else None
    kl = klausuler(men.rstrip('.'))
    if not all(ok for _, _, ok in kl):
        return None
    props = {p for _, (p, _), _ in kl}
    amnen = []
    for s, (p, a), _ in kl:
        nm = re.search(r'(' + TK.NUM + r') ?(' + TK.ENH_RX + r')', s)
        amnen.append((a, si(nm.group(1), nm.group(2)) if nm else None))
    if any(a in GASER for a, _ in amnen):
        return None
    if props != {'rho'}:
        return ('blandat', amnen) if 'rho' in props else None
    return ('bort', amnen) if all(tabellvarde(a, v) for a, v in amnen) else None


MENING = re.compile(r'(?<![^\s>])([A-ZÅÄÖ][^<>]*?\.)(?=\s|<|$)')
INB = re.compile(r' (?:med|som har) (?:en |den )?densiteten (' + TK.NUM + r') ?(' + TK.ENH_RX + r')(?=[ .,?<])')
INB_AMNE = re.compile(r'(vattnet|vatten|havsvatten|havsvattnet|isen|is|kvicksilvret|kvicksilver|etanol|etanolen|'
                      r'koppar|aluminium|järn|bly|guld|silver|stål|mässing|zink|tenn)$')
BEST = {'vattnet': 'vatten', 'havsvattnet': 'havsvatten', 'isen': 'is', 'kvicksilvret': 'kvicksilver', 'etanolen': 'etanol'}


def rensa(txt, id_, falt, borta):
    """Ta bort tabelldensiteter ur en HTML-text. borta samlar (ämne, värde)."""
    if not txt or 'ensitet' not in txt:
        return txt
    ny = txt
    for m in list(MENING.finditer(txt)):
        men = m.group(1)
        r = densitetsmening(men)
        if r is None:
            continue
        typ, amnen = r
        if typ == 'blandat':
            DENS_LOGG['blandat'].append((id_, falt, men))
            continue
        ny = ny.replace(' ' + men, '', 1) if (' ' + men) in ny else ny.replace(men, '', 1)
        borta.extend(amnen)
        DENS_LOGG['borttaget'].append((id_, falt, men))
    for m in list(INB.finditer(ny)):
        fore = ny[:m.start()].split()[-1] if ny[:m.start()].split() else ''
        am = INB_AMNE.search(fore)
        if not am:
            continue
        amne = BEST.get(am.group(1), am.group(1))
        v = si(m.group(1), m.group(2))
        if amne in GASER or not tabellvarde(amne, v):
            continue
        ny = ny.replace(m.group(0), '', 1)
        borta.append((amne, v))
        DENS_LOGG['borttaget'].append((id_, falt, m.group(0).strip()))
    # ”En järnkula med radien 3,0 cm och densiteten 7870 kg/m³”, ”Ett isberg med densiteten 917 kg/m³”:
    # ämnet framgår av meningens ord. Värdet måste stämma med ett av ämnena i meningen.
    for men in [m.group(1) for m in MENING.finditer(ny)]:
        for m in list(FRAS.finditer(men)):
            v = si(m.group(1), m.group(2))
            kand = [a for a in amnen_i(men) if a not in GASER and tabellvarde(a, v)]
            if not kand:
                continue
            ny = ny.replace(men, men.replace(m.group(0), '', 1), 1)
            men = men.replace(m.group(0), '', 1)
            borta.append((kand[0], v))
            DENS_LOGG['borttaget'].append((id_, falt, m.group(0).strip()))
    # ”Materialets densitet är 11340 kg/m³.” när ämnet nämns i samma text
    for m in list(MAT.finditer(ny)):
        v = si(m.group(1), m.group(2))
        kand = [a for a in amnen_i(ny) if a not in GASER and tabellvarde(a, v)]
        if kand:
            ny = ny.replace(' ' + m.group(0), '', 1) if (' ' + m.group(0)) in ny else ny.replace(m.group(0), '', 1)
            borta.append((kand[0], v))
            DENS_LOGG['borttaget'].append((id_, falt, m.group(0)))
    ny = re.sub(r'<p>\s*</p>', '', ny)
    return ny


def alternativ(svar, borta):
    if not isinstance(svar, (int, float)) or isinstance(svar, bool) or svar == 0:
        return []
    ut = set()
    for amne, v in borta:
        for r in ALT.get(amne, []):
            if v and abs(r - v) > 1e-9:
                for k in (1, -1):
                    ut.add(float(f'{svar * (r / v) ** k:.6g}'))
    return sorted(ut)


BLANDAT = {
    'Kopparns densitet är 8,96 g/cm³ och resistiviteten 1,7·10⁻⁸ Ωm.': ('Kopparns resistivitet är 1,7·10⁻⁸ Ωm.', 'koppar', 8960),
    'Aluminiumets densitet är 2,70 g/cm³ och resistiviteten 2,7·10⁻⁸ Ωm.': ('Aluminiumets resistivitet är 2,7·10⁻⁸ Ωm.', 'aluminium', 2700),
    'Etanolens densitet är 0,79 kg/liter och dess specifika värmekapacitet 2400 J/(kg·K).':
        ('Etanolens specifika värmekapacitet är 2400 J/(kg·K).', 'etanol', 790),
    'Isens densitet är 917 kg/m³ och smältvärme är 334 kJ/kg.': ('Isens smältvärme är 334 kJ/kg.', 'is', 917),
}
BLANDAT2 = {  # tabelldensitet tillsammans med uppgiftens egna data: bara tabellvärdet tas bort
    'Luft har densiteten 1,29 kg/m³ och vatten 1000 kg/m³.': ('Luft har densiteten 1,29 kg/m³.', [('vatten', 1000)]),
    'Aluminium har densiteten 2,70 g/cm³ och plasten 1,20 g/cm³.': ('Plasten har densiteten 1,20 g/cm³.', [('aluminium', 2700)]),
    'Densiteterna är 789 kg/m³ för etanol och 998 kg/m³ för vatten.': ('', [('etanol', 789), ('vatten', 998)]),
    'Blyets densitet är 11340 kg/m³, volframets 19300 kg/m³ och vattnets 1000 kg/m³.':
        ('', [('bly', 11340), ('volfram', 19300), ('vatten', 1000)]),
    'Fast järn har densiteten 7 870 kg/m³.': ('', [('järn', 7870)]),
    'Densiteten är 1000 kg/m³ för vatten och 850 kg/m³ för olja.': ('Oljans densitet är 850 kg/m³.', [('vatten', 1000)]),
    'Densiteten är 1000 kg/m³ för vatten och 910 kg/m³ för matolja.': ('Matoljans densitet är 910 kg/m³.', [('vatten', 1000)]),
    'Densitet: luft 1,29 kg/m³, aluminium 2 700 kg/m³.': ('Luftens densitet är 1,29 kg/m³.', [('aluminium', 2700)]),
    'Densitet: vatten 1 000 kg/m³, luft 1,29 kg/m³.': ('Luftens densitet är 1,29 kg/m³.', [('vatten', 1000)]),
    'Densitet: vatten 1 000 kg/m³, luft 1,29 kg/m³, helium 0,179 kg/m³, guld 19 300 kg/m³.':
        ('Densitet: luft 1,29 kg/m³, helium 0,179 kg/m³.', [('vatten', 1000), ('guld', 19300)]),
    'Vatten har densiteten 1,00 g/cm³ och glykol 1,11 g/cm³.': ('Glykol har densiteten 1,11 g/cm³.', [('vatten', 1000)]),
    'Vatten har densiteten 1,00 g/cm³.': ('', [('vatten', 1000)]),
}
LEDTRAD = {'2.155': '<p>Slå upp kopparns densitet. Hur stor volym behöver kopparen ha för att få den givna massan?</p>'}


OCH_DENS = re.compile(r' och (havsvattnets|vattnets|isens|kvicksilvrets|etanolens) densitet (?:är )?(' + TK.NUM + r') ?('
                      + TK.ENH_RX + r')(?=[.,<])')
OCH_GRUND = {'havsvattnets': 'havsvatten', 'vattnets': 'vatten', 'isens': 'is', 'kvicksilvrets': 'kvicksilver',
             'etanolens': 'etanol'}


FORE_DENS = re.compile(r'(Vattnets|Havsvattnets|Isens) densitet är (' + TK.NUM + r') ?(' + TK.ENH_RX + r') och ([a-zåäö])')
FORE_GRUND = {'Vattnets': 'vatten', 'Havsvattnets': 'havsvatten', 'Isens': 'is'}


def och_densitet(txt, id_, falt, borta):
    """”Lufttrycket är 101,3 kPa och vattnets densitet 998 kg/m³.” → ”Lufttrycket är 101,3 kPa.”
    ”Vattnets densitet är 998 kg/m³ och lufttrycket är 101 kPa.” → ”Lufttrycket är 101 kPa.”"""
    for m in list(FORE_DENS.finditer(txt or '')):
        amne, v = FORE_GRUND[m.group(1)], si(m.group(2), m.group(3))
        if tabellvarde(amne, v):
            txt = txt.replace(m.group(0), m.group(4).upper(), 1)
            borta.append((amne, v))
            DENS_LOGG['borttaget'].append((id_, falt, m.group(0)))
    for m in list(OCH_DENS.finditer(txt or '')):
        amne, v = OCH_GRUND[m.group(1)], si(m.group(2), m.group(3))
        if tabellvarde(amne, v):
            txt = txt.replace(m.group(0), '', 1)
            borta.append((amne, v))
            DENS_LOGG['borttaget'].append((id_, falt, m.group(0).strip()))
    return txt


def d_densitet(u):
    """Densiteter bort ur frågetexterna. kgInstruktion lämnas orörd (förtydligande 2026-11-27, se kg_tillbaka)."""
    spar = [(u, u.get('kgInstruktion'))] + [(d, d.get('kgInstruktion')) for d in u.get('spelDelar') or []]
    _d_densitet(u)
    for obj, v in spar:
        if v is None:
            obj.pop('kgInstruktion', None)
        else:
            obj['kgInstruktion'] = v


def _d_densitet(u):
    borta = []
    id_ = u['id']
    for obj, f in [(u, 't'), (u, 'spelIntro'), (u, 'kgInstruktion')] + \
            [(d, g) for d in u.get('spelDelar') or [] for g in ('t', 'fraga', 'kgInstruktion')]:
        if isinstance(obj.get(f), str):
            obj[f] = och_densitet(obj[f], id_, f, borta)
    # Blandade meningar: densiteten tas bort och den andra uppgiften står kvar.
    falt = [(u, 'kgInstruktion'), (u, 'spelIntro')] + [(d, f) for d in u.get('spelDelar') or [] for f in ('t', 'kgInstruktion', 'fraga')]
    for obj, f in falt:
        for gammal, (ny, amne, v) in BLANDAT.items():
            if isinstance(obj.get(f), str) and gammal in obj[f]:
                obj[f] = obj[f].replace(gammal, ny)
                borta.append((amne, v))
        for gammal, (ny, lista) in BLANDAT2.items():
            if isinstance(obj.get(f), str) and gammal in obj[f]:
                obj[f] = obj[f].replace(' ' + gammal, (' ' + ny) if ny else '') if (' ' + gammal) in obj[f] \
                    else obj[f].replace(gammal, ny)
                obj[f] = re.sub(r'<p>\s*</p>', '', obj[f]).strip() if f == 'kgInstruktion' else re.sub(r'<p>\s*</p>', '', obj[f])
                borta.extend(lista)
                DENS_LOGG['borttaget'].append((id_, f, gammal))
        if f == 'kgInstruktion' and obj.get(f) == '':
            del obj[f]
    if id_ in LEDTRAD:
        u['ledtrad'] = LEDTRAD[id_]
    if u.get('kgInstruktion'):
        u['kgInstruktion'] = rensa(u['kgInstruktion'], id_, 'kgInstruktion', borta).strip()
        if not u['kgInstruktion']:
            del u['kgInstruktion']
    if u.get('spelIntro'):
        u['spelIntro'] = rensa(u['spelIntro'], id_, 'spelIntro', borta)
    for d in u.get('spelDelar') or []:
        for f in ('t', 'kgInstruktion'):
            if d.get(f):
                d[f] = rensa(d[f], id_, f'{d["etikett"]}.{f}', borta).strip() if f == 'kgInstruktion' else \
                    rensa(d[f], id_, f'{d["etikett"]}.{f}', borta)
                if f == 'kgInstruktion' and not d[f]:
                    del d[f]
        if isinstance(d.get('fraga'), str):
            d['fraga'] = rensa(d['fraga'], id_, f'{d["etikett"]}.fraga', borta)
    if not borta:
        return
    borta = list({(a, v) for a, v in borta})
    # Ledtrådar som avslöjar det borttagna värdet skrivs om för hand (loggas).
    tal = {f'{v / 1000:.3g}'.replace('.', ',') for _, v in borta} | {f'{v:g}'.replace('.', ',') for _, v in borta}
    for f, led in [('ledtrad', u.get('ledtrad'))] + [(d['etikett'] + '.ledtrad', d.get('ledtrad')) for d in u.get('spelDelar') or []]:
        if isinstance(led, str) and any(re.search(r'(?<![\d,])' + re.escape(x) + r'(?![\d,])', led) for x in tal):
            DENS_LOGG['ledtrad'].append((id_, f, re.sub(r'<[^>]+>', '', led)))
    return  # svarTabell behövs inte när värdet står i kgInstruktion (förtydligande 2026-11-27)
    # svarTabell, samma format som tidigare: {"index": [alternativa svar]}
    def lagg_till(obj, i, svar):
        alt = alternativ(svar, borta)
        if not alt:
            return
        tab = obj.get('svarTabell') or {}
        if isinstance(tab, list):
            tab = {str(k): v for k, v in enumerate(tab) if v}
        tab[str(i)] = sorted(set(tab.get(str(i)) or []) | set(alt))
        obj['svarTabell'] = dict(sorted(tab.items(), key=lambda kv: int(kv[0])))

    rs = u.get('rättSvar')
    if isinstance(rs, list):
        for i, x in enumerate(rs):
            lagg_till(u, i, x)
    else:
        lagg_till(u, 0, rs)
    for d in u.get('spelDelar') or []:
        if 'rättSvar' in d:
            lagg_till(d, 0, d['rättSvar'])


# ---------------------------------------------------------------- steg: kedja
#
# Felrapport 2.52 (”frågan kommer igen i c) men inte b)”). Kunskapsgymmets kedjaDelning visar bara det som skiljer
# en dels text från de föregående. Alla delkort ska därför börja med exakt samma inledning (spelIntro), och det som
# ändras står i delens fråga. Uppgifterna och de handskrivna frågorna står i omskr/fy1_kedjor_2026-11-27.py.
# Övriga uppgifter där kedjan visade situationen igen görs om automatiskt bara när varje mening i delens egen
# inledning står ordagrant i spelIntro (delen hade en förkortad version av samma situation).

import html as _html  # noqa: E402
import importlib.util as _ilu  # noqa: E402

_spec = _ilu.spec_from_file_location('kedjor', os.path.join(HERE, 'omskr', 'fy1_kedjor_2026-11-27.py'))
KJ = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(KJ)
BLOCK = re.compile(r'(<p\b.*?</p>|<span class="fig">.*?</span>|<svg\b.*?</svg>|<table\b.*?</table>|<ol\b.*?</ol>|'
                   r'<ul\b.*?</ul>|<div\b.*?</div>|<figure\b.*?</figure>)', re.S)
KEDJA_LOGG = {'auto': [], 'hand': [], 'hoppat': []}


def block(h):
    h, ut, pos = h or '', [], 0
    for m in BLOCK.finditer(h):
        if h[pos:m.start()].strip():
            ut.append(h[pos:m.start()].strip())
        ut.append(m.group(0))
        pos = m.end()
    if h[pos:].strip():
        ut.append(h[pos:].strip())
    return ut


def _ren(h):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', ' ', h or '', flags=re.S)))).strip()


def _meningar_raa(h):
    """Meningar i delens stycken (HTML behålls inne i meningen)."""
    ut = []
    for b in block(re.sub(r'<span class="fig">.*?</span>|<svg.*?</svg>', '', h or '', flags=re.S)):
        inre = re.sub(r'^<p[^>]*>|</p>$', '', b)
        ut += [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-ZÅÄÖ0-9\\(])', inre) if x.strip()]
    return ut


def visas_igen(u):
    """Sant om kedjan visar situationen igen eller samma fråga i en senare del (som kedjaDelning)."""
    import difflib
    delar = [d for d in u.get('spelDelar') or [] if d.get('t')]
    if len(delar) < 2:
        return False
    listor = [block(d['t']) for d in delar]
    n = lambda s: re.sub(r'\s+', ' ', s).strip()  # noqa: E731
    k = 0
    while all(k < len(l) - 1 and n(l[k]) == n(listor[0][k]) for l in listor):
        k += 1
    kort = []
    for i, l in enumerate(listor):
        m0 = k
        for j in range(i):
            m = k
            while m < len(l) - 1 and m < len(listor[j]) and n(l[m]) == n(listor[j][m]):
                m += 1
            m0 = max(m0, m)
        kort.append(l[m0:])
    visat = [_ren(''.join(x)) for x in kort]
    for i in range(1, len(delar)):
        if visat[i] in visat[:i]:
            return True
        if kort[i] and listor[0] and len(_ren(kort[i][0])) > 40 and \
                difflib.SequenceMatcher(None, _ren(kort[i][0]), _ren(listor[0][0])).ratio() > 0.6:
            return True
    return False


def k_kedja(u):
    id_ = u['id']
    delar = u.get('spelDelar') or []
    intro = u.get('spelIntro') or ''
    if id_ in KJ.HOPPA or u.get('kgFristaendeDelar') or len([d for d in delar if d.get('t')]) < 2:
        return
    spec = KJ.KEDJA.get(id_)
    if spec is None and id_ not in KJ.BEHALL and not visas_igen(u):
        return
    if spec and spec.get('intro'):
        # Ny inledning: figurerna i den gamla följer med.
        figs = re.findall(r'<span class="fig">.*?</span>|<svg\b.*?</svg>', intro, flags=re.S)
        intro = spec['intro'] + ''.join(f for f in figs if f not in spec['intro'])
        u['spelIntro'] = intro
    if not _ren(intro) and '<svg' not in intro:
        KEDJA_LOGG['hoppat'].append((id_, 'ingen inledning'))
        return
    intro_men = set(map(_ren, _meningar_raa(intro)))
    nya = {}
    for d in delar:
        fr_gammal = d.get('fraga') or ''
        if not d.get('t') or not fr_gammal:
            KEDJA_LOGG['hoppat'].append((id_, d.get('etikett'), 'saknar t eller fråga'))
            return
        # Delen får inte ha tabeller eller listor som inte finns i inledningen (de skulle försvinna).
        bl = block(d['t'])
        if any(re.match(r'<(table|ol|ul|div)\b', b) and _ren(b) not in _ren(intro) for b in bl):
            KEDJA_LOGG['hoppat'].append((id_, d['etikett'], 'tabell eller lista i delen'))
            return
        fr_men = set(map(_ren, _meningar_raa(fr_gammal)))
        egna = [m for m in _meningar_raa(d['t']) if _ren(m) not in intro_men and _ren(m) not in fr_men
                and _ren(m) != _ren(fr_gammal) and not _ren(m).endswith('?')]
        val = (spec or {}).get(d['etikett'])
        if val == 's':
            fr = ' '.join(egna + [fr_gammal])
        elif isinstance(val, str):
            fr = val
        else:
            if egna and id_ not in KJ.BEHALL and spec is None:
                KEDJA_LOGG['hoppat'].append((id_, d['etikett'], 'egna meningar: ' + ' '.join(map(_ren, egna))[:120]))
                return
            fr = fr_gammal
        nya[d['etikett']] = fr
    for d in delar:
        if (id_, d['etikett']) in KJ.EGEN_TEXT:
            # Egen text som före ändringen (commit d9c8312), utan inledningens kraftbild.
            if not _FORE:
                import subprocess
                t = subprocess.run(['git', 'show', 'd9c8312:uppgifter.js'], capture_output=True,
                                   cwd=os.path.join(HERE, '..', '..')).stdout.decode('utf-8')
                _FORE.update({x['id']: x for x in json.loads(t[t.index('['):t.rindex(']') + 1])})
            gd = next(x for x in _FORE[id_]['spelDelar'] if x['etikett'] == d['etikett'])
            d['t'], d['fraga'] = gd['t'], gd['fraga']
            continue
        fr = re.sub(r'\s+', ' ', nya[d['etikett']]).strip()
        d['fraga'] = fr
        extra = ''
        if (id_, d['etikett']) in FIGUR_TILLBAKA:  # figuren som lagts tillbaka efter frågan (steget figur)
            extra = ''.join(s for s in re.findall(r'<span class="fig">.*?</span>|<svg\b.*?</svg>', d['t'].split('</p>')[-1],
                                                  flags=re.S) if s not in intro)
        d['t'] = intro + f'<p>{fr}</p>' + extra
    KEDJA_LOGG['hand' if spec else 'auto'].append(id_)


# Delar vars egen figur visar delens ändrade situation (m = ?, 0,10 m, 78 m/s, simmarens drift med ?): figuren
# hämtas ur läget före kedjeändringen (commit d9c8312) och läggs efter frågan.
FIGUR_TILLBAKA = {('4.251', 'b'), ('3.311', 'c'), ('4.245', 'c')}
_FORE = {}


def a_aterstall(u):
    """3.73 och 3.93: delkorten som före kedjeändringen (egna figurer per kort, fellogg 2026-11-04)."""
    import subprocess
    if not _FORE:
        t = subprocess.run(['git', 'show', 'd9c8312:uppgifter.js'], capture_output=True, cwd=os.path.join(HERE, '..', '..')).stdout.decode('utf-8')
        _FORE.update({x['id']: x for x in json.loads(t[t.index('['):t.rindex(']') + 1])})
    for d in u['spelDelar']:
        gd = next(x for x in _FORE[u['id']]['spelDelar'] if x['etikett'] == d['etikett'])
        d['t'], d['fraga'] = gd['t'], gd['fraga']


def f_figur(u):
    import subprocess
    if not _FORE:
        t = subprocess.run(['git', 'show', 'd9c8312:uppgifter.js'], capture_output=True, cwd=os.path.join(HERE, '..', '..')).stdout.decode('utf-8')
        _FORE.update({x['id']: x for x in json.loads(t[t.index('['):t.rindex(']') + 1])})
    for d in u.get('spelDelar') or []:
        if (u['id'], d['etikett']) not in FIGUR_TILLBAKA:
            continue
        gammal = next(x for x in _FORE[u['id']]['spelDelar'] if x['etikett'] == d['etikett'])
        egna = [s for s in re.findall(r'<span class="fig">.*?</span>|<svg\b.*?</svg>', gammal['t'], flags=re.S)
                if s not in (u.get('spelIntro') or '')]
        for s in egna:
            if s not in d['t']:
                d['t'] += s


# ---------------------------------------------------------------- steg: kg_tillbaka
#
# Användaren 2026-11-27 (förtydligande): ”i uppgiftslabbet ska det inte vara med några densiteter som finns i
# formelsamlingen, men i kunskapsgymmet kan de stå för att det ska bli rätt med rättningen, men då finns det ju en egen
# del i koden.” Densiteterna ska alltså stå i kgInstruktion (som bara Kunskapsgymmet visar, sist under frågan) men
# inte i frågetexterna (t, spelIntro, delkortens t och fraga). Steget lägger tillbaka de densiteter som steget
# densitet tog bort, som egna meningar i kgInstruktion på uppgiften och på varje delkort som hade värdet, och
# återställer svarTabell (alternativen behövs inte när värdet står i instruktionen).

GENITIV = {'vatten': 'Vattnets', 'havsvatten': 'Havsvattnets', 'is': 'Isens', 'järn': 'Järnets', 'koppar': 'Kopparns',
           'bly': 'Blyets', 'guld': 'Guldets', 'silver': 'Silvrets', 'aluminium': 'Aluminiumets', 'stål': 'Stålets',
           'etanol': 'Etanolens', 'mässing': 'Mässingens', 'zink': 'Zinkens', 'tenn': 'Tennets',
           'kvicksilver': 'Kvicksilvrets', 'volfram': 'Volframets'}
NUMENH = re.compile(r'(' + TK.NUM + r') ?(' + TK.ENH_RX + r')')


def _densitetsmeningar(gammal_text, ny_text):
    """Densitetsvärden (ämne, talets text, enhet) som finns i gammal_text men inte i ny_text."""
    ut = []
    for m in NUMENH.finditer(re.sub(r'<svg.*?</svg>', '', gammal_text or '', flags=re.S)):
        if m.group(2) not in ('kg/m³', 'g/cm³', 'kg/L', 'kg/l', 'kg/liter', 'kg/dm³', 'g/L', 'g/dm³'):
            continue
        v = si(m.group(1), m.group(2))
        fore = gammal_text[max(0, m.start() - 160):m.start()]
        kand = [a for a in ALT if tabellvarde(a, v) and (a in amnen_i(fore + ' ' + gammal_text[m.end():m.end() + 30]))]
        if not kand:
            continue
        if m.group(0) in (ny_text or ''):
            continue
        ut.append((kand[0], m.group(1).strip(), m.group(2)))
    return list(dict.fromkeys(ut))


def _har_varde(text, x):
    """Står värdet x = (ämne, tal, enhet) redan i texten (1000 och 1 000 räknas lika)?"""
    v = si(x[1], x[2])
    return any(abs((si(m.group(1), m.group(2)) or -1) - v) < 1e-6 * max(1, v) for m in NUMENH.finditer(text or ''))


def _mening(amne, num, enh):
    return f'{GENITIV[amne]} densitet är {num} {enh}.'


GEN_MENING = re.compile(r'(?:' + '|'.join(GENITIV.values()) + r') densitet är (?:' + TK.NUM + r') ?(?:' + TK.ENH_RX + r')\.\s*')
ANDRA_PROP = re.compile(r'resistivitet|värmekapacitet|smältvärme|ångbildningsvärme|lufttryck|\bluft|helium|vätgas|plast|olja', re.I)


def _lagg_kg(obj, meningar):
    gammal = obj.get('kgInstruktion') or ''
    nya = [m for m in meningar if m not in gammal]
    if nya:
        obj['kgInstruktion'] = (' '.join(nya) + (' ' + gammal if gammal else '')).strip()


def _kg_meningar(gammal_kg, varden):
    """Meningar för de saknade värdena: originalets mening ur den gamla kgInstruktion när den bara handlar om
    densiteter (”Aluminium har densiteten 2,70 g/cm³ och stål 7,80 g/cm³.”), annars en ny mening per värde."""
    ut, kvar = [], list(varden)
    for men in re.split(r'(?<=\.)\s+', gammal_kg or ''):
        if not men or ANDRA_PROP.search(men) or 'densitet' not in men.lower():
            continue
        tackta = [x for x in kvar if f'{x[1]} {x[2]}' in men]
        if tackta:
            ut.append(men.strip())
            kvar = [x for x in kvar if x not in tackta]
    return ut + [_mening(*x) for x in kvar]


def t_kg_tillbaka(u):
    import subprocess
    if not _FORE:
        t = subprocess.run(['git', 'show', 'd9c8312:uppgifter.js'], capture_output=True, cwd=os.path.join(HERE, '..', '..')).stdout.decode('utf-8')
        _FORE.update({x['id']: x for x in json.loads(t[t.index('['):t.rindex(']') + 1])})
    g = _FORE.get(u['id'])
    if not g:
        return
    # Meningar som ett tidigare körning av steget har skapat (formen ”Blyets densitet är 11,3 g/cm³.”) tas bort först
    # om de inte stod ordagrant i den gamla instruktionen; sedan läggs värdena till på nytt. Steget blir idempotent.
    def rensa_genererade(obj, kalla):
        kg = obj.get('kgInstruktion')
        if kg:
            ny = GEN_MENING.sub(lambda m: m.group(0) if m.group(0).strip() in (kalla or '') else '', kg).strip()
            if ny:
                obj['kgInstruktion'] = ny
            else:
                obj.pop('kgInstruktion', None)
    rensa_genererade(u, g.get('kgInstruktion'))
    for d in u.get('spelDelar') or []:
        gd = next((x for x in g.get('spelDelar') or [] if x.get('etikett') == d.get('etikett')), {})
        rensa_genererade(d, (gd.get('kgInstruktion') or '') + ' ' + (g.get('kgInstruktion') or ''))
    # Uppgiften: allt som togs bort ur huvudnivåns fält (kgInstruktion, spelIntro, t)
    huvud = []
    for f in ('kgInstruktion', 'spelIntro', 't'):
        huvud += _densitetsmeningar(g.get(f), '')
    # Bara värden som verkligen saknas i nuvarande huvudnivå-texter räknas (t kan ha undantag från 2026-11-23).
    nu_huvud = ' '.join(str(u.get(f) or '') for f in ('kgInstruktion', 'spelIntro'))
    huvud = [x for x in dict.fromkeys(huvud) if not _har_varde(nu_huvud, x)]
    if huvud:
        _lagg_kg(u, _kg_meningar(g.get('kgInstruktion'), huvud))
    for d in u.get('spelDelar') or []:
        gd = next((x for x in g.get('spelDelar') or [] if x.get('etikett') == d.get('etikett')), None)
        if not gd:
            continue
        egna = []
        for f in ('kgInstruktion', 't', 'fraga'):
            egna += _densitetsmeningar(gd.get(f), '')
        nu_del = ' '.join(str(d.get(f) or '') for f in ('kgInstruktion', 't', 'fraga'))
        egna = [x for x in dict.fromkeys(egna) if not _har_varde(nu_del, x)]
        if egna:
            _lagg_kg(d, _kg_meningar((gd.get('kgInstruktion') or '') + ' ' + (g.get('kgInstruktion') or ''), egna))
    # svarTabell som före steget densitet (2.110 och 3.72 behåller sina, de har ingen instruktion)
    if u['id'] not in ('3.72',):
        if 'svarTabell' in g:
            u['svarTabell'] = g['svarTabell']
        else:
            u.pop('svarTabell', None)
        for d in u.get('spelDelar') or []:
            gd = next((x for x in g.get('spelDelar') or [] if x.get('etikett') == d.get('etikett')), {})
            if 'svarTabell' in gd:
                d['svarTabell'] = gd['svarTabell']
            else:
                d.pop('svarTabell', None)


# ---------------------------------------------------------------- steg: tabell
#
# Samma princip för alla tabellvärden (specifik värmekapacitet, smält- och ångbildningsvärme, resistivitet, ljudets
# fart, g på månen och Mars, halveringstider, gasernas densitet): de står i kgInstruktion, inte i Kunskapsgymmets
# frågetexter (spelIntro, delkortens t och fraga). Igenkänningen är tabell_till_kg.rensa_t från 2026-11-23, som
# bara flyttar meningar och inbäddade värden som stämmer med tabellvärdet.

def _rensa_text(html_text):
    """rensa_t utan kravet att en fråga ska finnas kvar (spelIntro har ingen fråga)."""
    vakt = '<p>Hur stor är den?</p>'
    ny, kg, _ = TK.rensa_t((html_text or '') + vakt)
    if ny is None:
        return html_text, []
    assert ny.endswith(vakt), ny[-60:]
    return ny[:-len(vakt)], kg


def m_tabell(u):
    intro = u.get('spelIntro')
    if intro:
        ny, kg = _rensa_text(intro)
        if kg:
            u['spelIntro'] = ny
            _lagg_kg_efter(u, kg)
    for d in u.get('spelDelar') or []:
        kg_del = []
        for f in ('t', 'fraga'):
            if isinstance(d.get(f), str) and d[f]:
                ny, kg = _rensa_text(d[f]) if f == 't' else _rensa_fraga(d[f])
                if kg:
                    d[f] = ny
                    kg_del += kg
        if kg_del:
            _lagg_kg_efter(d, list(dict.fromkeys(kg_del)))


def _rensa_fraga(txt):
    ny, kg = _rensa_text(f'<p>{txt}</p>')
    return re.sub(r'^<p>|</p>$', '', ny).strip(), kg


def _lagg_kg_efter(obj, meningar):
    gammal = obj.get('kgInstruktion') or ''
    nya = [m for m in meningar if m not in gammal and not _har_alla_varden(gammal, m)]
    if nya:
        obj['kgInstruktion'] = (gammal + ' ' + ' '.join(nya)).strip()


def _har_alla_varden(text, mening):
    """Står alla tal med enhet i meningen redan i texten (”1 000” och ”1000” räknas lika)?"""
    vals = [m for m in NUMENH.finditer(mening)]
    if not vals:
        return False
    return all(_har_varde(text, (None, m.group(1).strip(), m.group(2))) for m in vals)


class AllaUppgifter(dict):
    """Steg som gäller alla uppgifter: {id: funktion} skapas när banken har lästs."""


KROPP_IDS_F = ('4.357 4.33 4.84 4.89 4.101 4.409 4.175 4.303 4.216 6.321 6.327 6.328 6.114 6.283 6.315 6.319 6.311 '
               '6.313 6.324 6.317 6.359 6.361').split()
KROPP_IDS_P = '9.44 9.97 9.152 9.173 9.362 9.368 9.379 9.381 9.386 9.387'.split()
STEG = {'kropp': {**{i: r_kropp_foremal for i in KROPP_IDS_F}, **{i: r_kropp_person for i in KROPP_IDS_P}, '2.195': r_2_195},
        'grammatik': {'7.149': r_7_149, '6.454': r_6_454, '2.379': r_2_379, '7.117': r_7_117, '9.216': r_9_216, **{i: r_metatext for i in ('6.190', '2.46')}}, 'rapporter': RAPPORTER, 'densitet': 'alla:d_densitet', 'kedja': 'alla:k_kedja', 'aterstall': {'3.73': a_aterstall, '3.93': a_aterstall}, 'kg_tillbaka': 'alla:t_kg_tillbaka', 'tabell': 'alla:m_tabell', 'figur': {'4.251': f_figur, '3.311': f_figur, '4.245': f_figur}}


def main():
    steg = sys.argv[1]
    b = Bank('fy1')
    Q = {u['id']: u for u in b.arr}
    andrade = 0
    jobb = STEG[steg]
    if isinstance(jobb, str):
        fn = globals()[jobb.split(':')[1]]
        jobb = {u['id']: fn for u in b.arr}
    for id_, f in jobb.items():
        u = copy.deepcopy(Q[id_])
        f(u)
        if u != Q[id_]:
            b.byte[id_] = objekttext(b, id_, u)
            json.loads(b.byte[id_])
            andrade += 1
    print(steg, andrade, 'uppgifter', '(skrivet)' if '--skriv' in sys.argv else '(torrkörning)')
    if steg == 'densitet':
        for k, v in DENS_LOGG.items():
            print(f'\n## {k}: {len(v)}')
            for x in v if k != 'borttaget' else []:
                print('  ', x)
        import collections
        print(collections.Counter(x[2] for x in DENS_LOGG['borttaget']).most_common(80))
    if steg == 'kedja':
        for k, v in KEDJA_LOGG.items():
            print(f'\n## {k}: {len(v)}')
            for x in v if k == 'hoppat' else [v]:
                print('  ', x)
    if '--skriv' in sys.argv:
        b.spara()


if __name__ == '__main__':
    main()
