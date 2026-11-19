# Ma5 (matf1), kopia av mato1_alla.py: svarsinstruktioner i hela banken (2026-11-18). Körs före handgenomläsningen område för område.
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
    m = re.search(r'\bi ((?:[a-zåäöA-Z°²³/%µ]+)(?: ?[²³])?)(?=$|[ ,.]| med| och)', low)
    rest = low
    if m and not re.match(r'(enklaste|bråkform|decimalform|potensform|grundpotensform|varje|hela|formatet)', m.group(1)):
        x = inre[m.start(1):m.end(1)]  # behåll versaler (°C, MB/s)
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


_klassa = klassa


def klassa(instr, enh):
    """Förbehandling för Ma3c: tecken, ordning, rutor, enheter som "liter per timme" och heltal med enhet."""
    s = instr.strip()
    extra = []
    if re.search(r'tecken', s):  # "tecken" skrivs aldrig (användarbeslut 2026-11-17)
        s = re.sub(r',? med (rätt )?tecken', '', s)
        extra.append('En minskning skrivs som ett negativt tal.')
    for fras, kgt in [(r'\.? ?Ordningen spelar ingen roll\.?', 'Ordningen spelar ingen roll.'),
                      (r',? (ett värde|en) i varje ruta', 'Skriv ett värde i varje ruta.')]:
        if re.search(fras, s):
            s = re.sub(fras, '', s); extra.append(kgt)
    s = s.strip().rstrip('.') + '.'
    low = s.lower()
    mv = re.fullmatch(r'svara i ([^\s,.]+) med (två|tre) värdesiffror\.', s, re.I)
    if mv and not mv.group(1).lower().startswith('grundpotens'):
        x = mv.group(1)
        kg = '' if (ENH.get(x, x) in enh or x in enh) else f'Svara i {x}.'
        return f'Avrunda till {mv.group(2)} värdesiffror.', ' '.join(k for k in [kg] + extra if k).strip()
    if re.fullmatch(r'svara (avrundat till|med) närmaste heltal\.', low):
        return 'Avrunda till närmaste heltal.', ' '.join(extra)
    mp = re.fullmatch(r'svara med ett positivt tal(?: i ([^\s,.]+))?\.', low)
    if mp:
        x = re.search(r' i ([^\s,.]+)', s).group(1) if mp.group(1) else ''
        kg = 'Svara med ett positivt tal.' + ('' if not x or x in enh else f' Svara i {x}.')
        return '', ' '.join([kg] + extra).strip()
    m = re.fullmatch(r'svara i ([^\s,.]+(?: per [a-zåäö]+)?)(?: med (ett )?heltal)?\.', s, re.I)
    if m:  # bara enhet (ev. heltal)
        x = m.group(1)
        ny = 'Avrunda till heltal.' if m.group(2) is not None or 'heltal' in low else ''
        kg = '' if (ENH.get(x, x) in enh or x in enh or x.replace(' per ', '/') in enh) else f'Svara i {x}.'
        return ny, ' '.join(k for k in [kg] + extra if k).strip()
    if re.fullmatch(r'svara(?: i [^\s,.]+)? med (ett )?heltal( i [^\s,.]+)?\.', low) and re.search(r' i ', low):
        x = re.search(r' i ([^\s,.]+)', s).group(1)
        kg = '' if (ENH.get(x, x) in enh or x in enh) else f'Svara i {x}.'
        return 'Avrunda till heltal.', ' '.join(k for k in [kg] + extra if k).strip()
    if re.match(r'svara med (en|två|tre) decimal', low) and (' och ' in low or ' i grader' in low):
        return re.sub(r' och (\w+) med ', r' och \1 till ', re.sub(r'^Svara med', 'Avrunda till', s)), ' '.join(extra)
    if s == '.':
        return '', ' '.join(extra)
    ny, kg = _klassa(s, enh)
    if ny.startswith('Svara med') and re.match(r'Svara med (en|två|tre) decimal', ny):
        ny = re.sub(r'^Svara med', 'Avrunda till', ny)
    return ny, ' '.join(k for k in [kg] + extra if k).strip()


b = Bank('matf1')
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
# 2.208: punkten i "hh.mm" bryter meningen; hela svarsformatet till kgInstruktion.
R['2.208'] = {'ers': [(' Svara med klockslaget i formatet hh.mm.', '')], 'kg': 'Svara med klockslaget i formatet hh.mm.'}
