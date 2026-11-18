# Fy2 hela banken, riktad omgång 2026-11-18. Kopia av fy1_kap4.py för uppgifter2.js.
# Regelmässiga byten som gäller hela kapitlet (bara utanför SVG-figurer):
#  - flervalsfraser och "(Svara i X.)" där X är en svarsenhet;
#  - modellmeningar om snören och trissor ersätts av lärarens egen form (4.106):
#    "Bortse från snörets och trissans massa och från friktionen.";
#  - "Bara tyngdkraften och snörkraften verkar." tas bort (eleven ser själv vilka krafter som verkar);
#  - "masslös" före fjäder/rep/snöre/vajer tas bort, "sträckt" i uppräkningar likaså;
#  - vågrät/lodrät heter horisontell/vertikal;
#  - "en låda på 30 kg" heter "en låda med massan 30 kg" (personer: "som väger").
# Riktningstecken, "från vila", "sammanlagd", "En elev" och bestämd form ("lådan på 125 kg") granskas för
# hand i fy1_k4_<område>.py. GRANSKA skrivs ut när skriptet körs direkt.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare, fran_platshallare

ALT = ['(Markera det korrekta alternativet.)', 'Markera det korrekta alternativet.', '(Välj ett alternativ.)', 'Välj ett alternativ.']
SYN = {'timmar': 'h', 'sekunder': 's', 'meter': 'm', 'procent': '%', 'grader': '°', 'minuter': 'min'}

# Längre fraser först. (gammal, ny)
FRASER = [
    ('Snöret är masslöst och sträckt. Trissan är masslös och friktionsfri. Bortse från luftmotstånd.',
     'Bortse från luftmotstånd, snörets och trissans massa och friktionen i trissan.'),
    ('Snöret är masslöst och sträckt. Trissan är masslös och friktionsfri.', 'Bortse från snörets och trissans massa och från friktionen.'),
    ('Snörena är masslösa, sträckta och vågräta vid bordet. Trissorna är masslösa och friktionsfria.',
     'Snörena är horisontella vid bordet. Bortse från snörenas och trissornas massa och från friktionen i trissorna.'),
    ('Snören och trissor är masslösa och friktionsfria.', 'Bortse från snörenas och trissornas massa och från friktionen i trissorna.'),
    ('Snöret och trissan är masslösa och trissan är friktionsfri.', 'Bortse från snörets och trissans massa och från friktionen.'),
    ('Snöret är masslöst och spänt, och trissan är masslös och friktionsfri.', 'Bortse från snörets och trissans massa och från friktionen.'),
    ('Trissan är masslös och friktionsfri.', 'Bortse från trissans massa och friktion.'),
    ('Trissorna är masslösa och friktionsfria.', 'Bortse från trissornas massa och friktion.'),
    ('Snöret är masslöst och sträckt.', 'Bortse från snörets massa.'),
    ('Snörena är masslösa, sträckta och vågräta vid bordet.', 'Snörena är horisontella vid bordet.'),
    ('Snöret är vågrätt vid klossen och masslöst.', 'Snöret är horisontellt vid klossen.'),
    ('Snöret är vågrätt vid lådan, masslöst och sträckt.', 'Snöret är horisontellt vid lådan.'),
    ('Snörena är masslösa och sitter symmetriskt.', 'Snörena sitter symmetriskt.'),
    ('Systemet är i vila och trådarna masslösa.', 'Systemet är i vila.'),
    ('Det masslösa snöret är spänt och upphängningen är fast.', 'Upphängningen är fast.'),
    (' Snöret är masslöst.', ''),
    (' Bara tyngdkraften och snörkraften verkar.', ''),
    (' Bara snörkraften och tyngdkraften verkar.', ''),
    (' På kulan verkar snörets spännkraft och tyngdkraften.', ''),
    ('ett vågrätt, sträckt, masslöst snöre', 'ett horisontellt snöre'),
    ('Ett vågrätt, sträckt, masslöst snöre', 'Ett horisontellt snöre'),
    ('ett vågrätt och masslöst snöre', 'ett horisontellt snöre'),
    ('Ett masslöst, sträckt snöre går vågrätt', 'Ett snöre går horisontellt'),
    ('Ett masslöst snöre går', 'Ett snöre går'),
    ('en masslös och friktionsfri trissa', 'en trissa'),
    ('en fast, masslös och friktionsfri trissa', 'en fast trissa'),
    ('en fast friktionsfri trissa', 'en fast trissa'),
    ('En masslös dynamometerfjäder', 'En dynamometerfjäder'),
    ('En masslös fjäder', 'En fjäder'), ('en masslös fjäder', 'en fjäder'),
    ('Två masslösa fjädrar', 'Två fjädrar'), ('två masslösa fjädrar', 'två fjädrar'),
    ('lodräta masslösa fjädrar', 'vertikala fjädrar'),
    ('två masslösa rep', 'två rep'), ('symmetriska masslösa vajrar', 'symmetriska vajrar'),
    ('En lodrät masslös stav', 'En lätt, vertikal stav'),
]

# "sammanlagd" -> "resulterande" om krafter, annars "total". Längre först.
SAMMANLAGD = [
    ('den sammanlagda vågräta kraften', 'den resulterande horisontella kraften'),
    ('den sammanlagda kraften', 'den resulterande kraften'), ('Den sammanlagda kraften', 'Den resulterande kraften'),
    ('konstant sammanlagd kraft', 'konstant resulterande kraft'), ('Samma sammanlagda kraft', 'Samma resulterande kraft'),
    ('sammanlagda bromskraften', 'totala bromskraften'), ('sammanlagda massan', 'totala massan'),
    ('sammanlagda stödjande kraft', 'totala stödjande kraft'), ('den sammanlagda kraften från', 'den totala kraften från'),
]
# "från vila": "släpps från vila" -> "släpps", annars "från stillastående".
VILA = [('släpps från vila', 'släpps'), ('Släpps från vila', 'Släpps'), ('från vila', 'från stillastående')]
# Riktningsmeningar -> kgInstruktion (gäller huvuduppgiften och alla delkort).
RIKTNING = [
    ('Välj höger som positivt.', 'Höger räknas som positiv riktning.'),
    ('Höger är positiv riktning.', 'Höger räknas som positiv riktning.'),
    ('Höger är positivt.', 'Höger räknas som positiv riktning.'),
    ('Välj höger som positiv riktning.', 'Höger räknas som positiv riktning.'),
    ('Välj uppåt som positiv riktning.', 'Uppåt räknas som positiv riktning.'),
    ('Uppåt är positiv riktning.', 'Uppåt räknas som positiv riktning.'),
    ('Uppåt är positivt.', 'Uppåt räknas som positiv riktning.'),
    ('Välj ursprunglig färdriktning som positiv.', 'Den ursprungliga färdriktningen räknas som positiv.'),
]
RIKTNING_I_FRAGA = [(' med uppåt som positiv riktning', 'Uppåt räknas som positiv riktning.'),
                    (' med uppåt positivt', 'Uppåt räknas som positiv riktning.'),
                    (' med höger som positiv riktning', 'Höger räknas som positiv riktning.')]

PERSON =r'(?:person|man|kvinna|pojke|flicka|hoppare|cyklist|klättrare|skidåkare|löpare|astronaut|dykare|förare|passagerare|gymnast|brottare|skridskoåkare|lindansare|fallskärmshoppare|elev|lärare|barn|bergsklättrare)'
PA_KG = re.compile(r'\b(En|en|Ett|ett|Två|två|Tre|tre) ([a-zåäö-]+) på (\d[\d ,]*\s?(?:kg|g|ton))(?: och (\d[\d ,]*\s?(?:kg|g|ton)))?( vardera)?(?![\w²³])')


def ord_byten(text):
    """vågrät/lodrät -> horisontell/vertikal, som (gammal, ny)-par för hela ord."""
    par = []
    for m in re.finditer(r'\b([VvLl])(ågrät|odrät)(t|a)?\b', text):
        gammal = m.group(0)
        ny = ('horisontell' if m.group(2) == 'ågrät' else 'vertikal') + (m.group(3) or '')
        if m.group(1).isupper():
            ny = ny[0].upper() + ny[1:]
        par.append((gammal, ny))
        # med omgivande text (för när samma ord också står i en SVG-figur)
        fore = re.search(r'[^<>]{0,30}$', text[:m.start()]).group(0)
        efter = re.match(r'[^<>]{0,12}', text[m.end():]).group(0)
        par.append((fore + gammal + efter, fore + ny + efter))
    return par


def massa_byten(text):
    par = []
    for m in PA_KG.finditer(text):
        art, nomen, m1, m2, vardera = m.groups()
        if re.fullmatch(PERSON + r'(?:en|er|na)?', nomen):
            ny = f'{art} {nomen} som väger {m1}' + (f' och {m2}' if m2 else '') + (vardera or '')
        elif m2:
            ny = f'{art} {nomen} med massorna {m1} och {m2}'
        else:
            ny = f'{art} {nomen} med massan {m1}' + (vardera or '')
        par.append((m.group(0), ny))
    return par


def texter(u):
    yield u.get('t') or ''
    yield u.get('spelIntro') or ''
    for d in u.get('spelDelar') or []:
        yield d.get('t') or ''
        yield d.get('fraga') or ''


def utan_svg(s):
    return re.sub(r'<svg.*?</svg>', ' ', s, flags=re.S)


def enheter(u):
    e = set()
    def w(x):
        if isinstance(x, list):
            [w(y) for y in x]
        elif x:
            e.add(str(x))
    w(u.get('svarEnhet'))
    for d in u.get('spelDelar') or []:
        w(d.get('svarEnhet'))
    return e


def bort(alla, fras):
    for v in (f'<p>{fras}</p>', f' {fras}', f'{fras} ', fras):
        if v in alla:
            return (v, '')
    return None


b = Bank('fy2')
R, GRANSKA = {}, []
for u in b.arr:
    if False:
        continue
    id_ = u['id']
    alla = ' '.join(till_platshallare(x)[0] for x in texter(u))
    raw = alla
    ers = []

    def lagg(a, c):
        # bara om frasen finns utanför figurerna och lika många gånger som i hela texten
        if a and a in alla and raw.count(a) == alla.count(a) and not any(a == x[0] for x in ers):
            ers.append((a, c))
            return True
        return False

    for f in ALT:
        e = bort(alla, f)
        if e and not any(e[0] in x[0] or x[0] in e[0] for x in ers):
            lagg(*e)
    if ' ()' in alla:
        lagg(' ()', '')
    for a, c in FRASER:
        if a in alla and not any(a in x[0] for x in ers):
            lagg(a, c)
    kg = None
    for a, k in RIKTNING:
        e = bort(alla, a)
        if e and lagg(*e):
            kg = k
    for a, k in RIKTNING_I_FRAGA:
        if lagg(a, ''):
            kg = k
    if kg and ' med tecken' in alla:
        lagg(' med tecken', '')
    for a, c in SAMMANLAGD:
        if a in alla and not any(a in x[0] or x[0] in a for x in ers):
            lagg(a, c)
    tmp = alla
    for a, c in VILA:  # i ordning: "släpps från vila" först, sedan resterande "från vila"
        if a in tmp and raw.count(a) == alla.count(a):
            ers.append((a, c))
            tmp = tmp.replace(a, c)
    if re.search(r'\bAnta att', alla):
        lagg('Anta att', 'Antag att')
    rest = alla
    for a, c in ers:
        rest = rest.replace(a, c)
    enh = enheter(u)
    for m in re.finditer(r'\(Svara i ([^)]*?)\.\)', rest):
        x = m.group(1)
        if SYN.get(x, x) in enh or x == 'hela N':
            e = bort(rest, m.group(0))
            if e:
                lagg(*e)
        else:
            GRANSKA.append((id_, u.get('omr'), m.group(0)))
    rest2 = rest
    for a, c in ers:
        rest2 = rest2.replace(a, c)
    for a, c in massa_byten(rest2):
        lagg(a, c)
    for a, c in ord_byten(rest2):
        lagg(a, c)
    # för handgranskning
    for rx in (r'[^.>]*positiv[^.<]*\.', r'[^.>]*med tecken[^.<]*[.?]', r'[^.>]*från vila[^.<]*[.?]', r'[^.>]*[Ss]ammanlagd[^.<]*[.?]',
               r'[^.>]*\b[Ee]n elev\b[^.<]*[.?]', r'[^.>]*\b[a-zåäö]+n på \d[\d ,]*\s?(?:kg|g|ton)\b[^.<]*[.?]', r'[^.>]*Räkna (?:bara )?med[^.<]*\.',
               r'[^.>]*\bmodell[^.<]*[.?]', r'[^.>]*Bara [a-zåäö]+ och [a-zåäö]+ verkar[^.<]*\.'):
        for m in set(re.findall(rx, rest2)):
            GRANSKA.append((id_, u.get('omr'), m.strip()))
    if ers or kg:
        # Byten görs på platshållartexten ([F1] för figurer/tabeller), så att figurerna aldrig ändras.
        def byt(x):
            t = till_platshallare(x)[0]
            for a, c in ers:
                t = t.replace(a, c)
            return t
        post = {}
        if byt(u.get('t')) != till_platshallare(u.get('t'))[0]:
            post['t'] = byt(u.get('t'))
        if u.get('spelIntro') is not None and byt(u['spelIntro']) != till_platshallare(u['spelIntro'])[0]:
            post['intro'] = byt(u['spelIntro'])
        dd = {}
        for i, d in enumerate(u.get('spelDelar') or []):
            et = d.get('etikett') or chr(97 + i)
            q = {}
            if d.get('t') and byt(d['t']) != till_platshallare(d['t'])[0]:
                q['t'] = byt(d['t'])
            if d.get('fraga') and byt(d['fraga']) != till_platshallare(d['fraga'])[0]:
                q['f'] = fran_platshallare(byt(d['fraga']), till_platshallare(d['fraga'])[1], id_)
                if d.get('t') and 't' not in q:
                    q['t'] = till_platshallare(d['t'])[0]
            if kg:
                q['kg'] = kg
            if q:
                dd[et] = q
        if dd:
            post['d'] = dd
        if kg:
            post['kg'] = kg
        if post:
            R[id_] = post

if __name__ == '__main__':
    omr = sys.argv[1:]
    for g in GRANSKA:
        if not omr or g[1] in omr:
            print('GRANSKA', *g)
