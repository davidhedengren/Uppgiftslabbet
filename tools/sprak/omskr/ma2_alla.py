# Ma2: svarsinstruktioner i hela banken (2026-11-18). Körs före handgenomläsningen område för område.
# Lärarens egna matteprov skriver avrundning och form som vanliga meningar ("Avrunda till en decimal.",
# "Svara exakt.", "Svara i bråkform och förkorta så långt som möjligt."), så de står kvar som vanliga meningar.
# Det som bara rättningen behöver ("en i varje svarsfält", "Svara A eller B", enhet som inte visas via svarEnhet)
# flyttas till kgInstruktion. "Välj ett alternativ." och liknande stryks.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

PAREN = re.compile(r' ?\((?:Svara|Ange|Välj|Skriv)[^()]*(?:\([^()]*\)[^()]*)*\)')
MENING = re.compile(r'(?:(?<=[.?!)] )|(?<=<p>)|(?<=<br>)|(?<=</strong> ))'
                    r'(?:Svara [^.?<]*[.?]|Välj (?:ett alternativ|det svar som stämmer|den förklaring som stämmer|rätt förklaring|rätt alternativ)\.'
                    r'|Ange båda lösningarna[^.<]*\.|Ange x-värdet och y-värdet\.|Ange först x[^.<]*\.|Ange de två värdena\.)')
TAL = {'en': 1, 'ett': 1, 'två': 2, 'tre': 3, 'fyra': 4, '1': 1, '2': 2, '3': 3, '4': 4}
ORD = {1: 'en', 2: 'två', 3: 'tre', 4: 'fyra'}
ENH = {'meter': 'm', 'kronor': 'kr', 'kr': 'kr', 'grader': '°', 'minuter': 'min', 'min': 'min', 'procent': '%',
       'timmar': 'h', 'h': 'h', 'sekunder': 's', 's': 's', 'gram': 'g', 'år': 'år', 'liter': 'liter'}


def enheter(u, i=None):
    e = u.get('svarEnhet')
    lista = e if isinstance(e, list) else [e]
    if i is not None and isinstance(e, list):
        lista = [e[i]] if i < len(e) else []
    ut = set()
    for x in lista:
        for y in str(x or '').split(','):
            if y.strip():
                ut.add(y.strip())
    return ut


def avrunda(inre):
    m = re.search(r'\b(en|två|tre|fyra|[1-4]) decimal(er)?\b', inre)
    if m:
        n = TAL[m.group(1)]
        return f'Avrunda till {ORD[n]} decimal{"er" if n > 1 else ""}.'
    m = re.search(r'(två|tre|fyra|[2-4]) värdesiffr', inre)
    if m:
        return f'Avrunda till {ORD[TAL[m.group(1)]]} värdesiffror.'
    if re.search(r'avrundat till heltal|hela kronor|hela procent', inre):
        return 'Avrunda till heltal.'
    return ''


def klassa(instr, enh):
    """instr utan parentes. Returnerar (ny text i uppgiften, kg-text)."""
    inre = instr.strip().rstrip('.?').strip()
    low = inre.lower()
    motivera = 'motivera' in low
    if re.match(r'välj (ett alternativ|det svar som stämmer|den förklaring som stämmer|rätt förklaring|rätt alternativ)$', low):
        return '', ''
    if re.match(r'välj alla', low):
        return '', 'Välj alla alternativ som stämmer.'
    if low.startswith('svara exakt') or low.startswith('svara på formen') or low == 'svara med lg':
        return inre + '.', ''
    if 'digitalt verktyg' in low:
        return avrunda(low), ''
    if 'ja eller nej' in low:
        return ('Motivera ditt svar.' if motivera else ''), 'Svara ja eller nej.'
    m = re.match(r'svara (a eller b|f eller g|en ?, ingen eller oändligt många|med ett namn)', low)
    if m:
        return ('Motivera ditt svar.' if motivera else ''), 'Svara ' + re.sub(r'\s*och motivera.*', '', inre[6:]) + '.'
    if re.fullmatch(r'svara i hela (kronor|procent|gram|meter|timmar|minuter)', low):
        return inre + '.', ''
    if ' för ' in low and 'decimal' in low:  # olika precision för olika storheter
        return re.sub(r'^Svara med', 'Avrunda till', inre) + '.', ''
    ny = avrunda(low)
    # "… och förklara/motivera/visa …" är en del av uppgiften och står kvar
    tillagg = ''
    mm = re.search(r'\boch ((?:förklara|motivera|visa|kontrollera)[^.]*)', inre)
    if mm:
        tillagg = mm.group(1)[0].upper() + mm.group(1)[1:] + '.'
        low = low[:mm.start()]
    kg = ''
    # enhet: "Svara i cm", "Svara i procent med en decimal", "Svara med två decimaler i meter"
    m = re.search(r'\bi ((?:[a-zåäöA-Z°²³/%]+)(?: ?[²³])?)(?=$|[ ,.]| med| och)', low)
    rest = low
    if m and not re.match(r'(enklaste|bråkform|decimalform|potensform|grundpotensform|varje|hela)', m.group(1)):
        x = m.group(1)
        if ENH.get(x, x) not in enh and x not in enh:
            kg = f'Svara i {x}.'
        rest = rest.replace(m.group(0), '')
    rest = re.sub(r'svara|ange|med|och|avrundat till heltal|i hela (kronor|procent|gram|timmar)|'
                  r'\b(en|två|tre|fyra|[1-4]) (decimaler|decimal|värdesiffror)\b|[ ,.]', '', rest)
    if rest:
        if re.search(r'heltal|ett ord|koordinat|\bx\b|lösningarna|svarsfält|bråkform|decimalform|decimaltal|först|'
                     r'median eller|klockslag|kr/km|namn', low):
            kg = (kg + ' ' + inre + '.').strip()
        else:  # en riktig uppgift ("Välj det rimligaste värdet.") står kvar oförändrad
            return instr.strip() if instr.strip().endswith(('.', '?')) else instr.strip() + '.', ''
    return ' '.join(x for x in (ny, tillagg) if x), kg.strip()


b = Bank('ma2')
R = {}
for u in b.arr:
    falt_t = [u.get('t') or '', u.get('spelIntro') or '']
    delar = u.get('spelDelar') or []
    falt = falt_t + [x or '' for d in delar for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    enh = enheter(u)
    e, kg_t, dd = [], [], {}

    def hitta(text):
        return [m.group(0) for m in PAREN.finditer(text)] + [m.group(0) for m in MENING.finditer(text)]

    sett = {}
    for m in dict.fromkeys(hitta(alla)):
        if raw.count(m) != alla.count(m):
            continue
        ny, kg = klassa(m.strip()[1:-1] if m.strip().startswith('(') else m.strip(), enh)
        sett[m] = (ny, kg)
        nyckel = m if m.startswith(' ') or (' ' + m) not in alla else ' ' + m
        e.append((nyckel, (' ' + ny) if (ny and nyckel.startswith(' ')) else ny))
    if not e:
        continue
    # kg för huvuduppgiften och för varje delkort
    for m in hitta(' '.join(till_platshallare(x)[0] for x in falt_t)):
        if m in sett and sett[m][1]:
            kg_t.append(sett[m][1])
    for i, d in enumerate(delar):
        dt = ' '.join(till_platshallare(x or '')[0] for x in (d.get('t'), d.get('fraga')))
        k = []
        for m in hitta(dt):
            if m in sett and sett[m][1]:
                ny, kgt = klassa(m.strip()[1:-1] if m.strip().startswith('(') else m.strip(), enheter(u, i))
                if kgt:
                    k.append(kgt)
        if k:
            dd[d.get('etikett') or chr(97 + i)] = {'kg': ' '.join(dict.fromkeys(k))}
    # tomma meningsrester: dubbla mellanslag och "<p></p>" städas av ersättningarna nedan
    e += [('<p></p>', ''), ('<p> </p>', '')]
    R[u['id']] = {'ers': e}
    if kg_t:
        R[u['id']]['kg'] = ' '.join(dict.fromkeys(kg_t))
    if dd:
        R[u['id']]['d'] = dd
