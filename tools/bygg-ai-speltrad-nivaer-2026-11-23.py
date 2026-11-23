"""AI-banken 2026-11-23: många spelträd i olika storlekar, en uppgift per nivå och träd.

Användarbeslut 2026-11-23: ”Jag vill att banken ska ha massor av uppgifter med olika träd i olika storlekar,
där de på nivå 1 bara ska bestämma rotnodens värde, nivå 2 samma sak fast större träd, nivå 3 ska man kunna
bestämma vilken gren som beskärs, nivå 4 samma sak när det är fler grenar och lite större träd, nivå 5 ska man
kunna bestämma olika noders alfa- och betavärden.”

  Nivå 1 (E)  3.81–3.110   rotens minimaxvärde, två nivåer, 4–7 löv
  Nivå 2 (E)  3.111–3.140  rotens minimaxvärde, tre nivåer eller breda träd, 8–14 löv, ojämna träd
  Nivå 3 (C)  3.141–3.165  alfa–beta: vilken gren beskärs (en beskärning), två nivåer, 5–9 löv
  Nivå 4 (A)  3.166–3.190  alfa–beta: vilka grenar beskärs (minst två beskärningar), tre nivåer, 8–14 löv
  Nivå 5 (A)  3.191–3.215  alfa–beta: α och β i en given nod (när sökningen går in i noden eller när den beskär)

De 135 grunduppgifterna har spelsammanhang. Därtill 40 uppgifter med enkla tillämpningar (3.216–3.255, åtta per nivå
i samma ordning): butik och konkurrent, säljare och köpare, robotar som samlar batterier, vaktrobot och inkräktare,
drönare och vind, sparare och börs m.fl. Användaren 2026-11-23: ”lägga in mycket enkla kontexter … så man kan förstå
att dessa abstrakta värden kan tillämpas” och ”inte bara ersätta, utan kanske skapa några fler bara med tillämpningar”.
Kontexten säger vem som är MAX och MIN, vem som väljer först och vad talen betyder; facit säger vad rotens värde betyder.

Varje uppgift är ett fristående kort med en fråga. Träden slumpas med fasta frön och måste uppfylla villkor
(olika lövvärden, inget träd två gånger, rotens värde är inte bara största eller minsta lövet, rätt antal
beskärningar). Facit följer FACITMALL: regeln i rubriken (t.ex. ”MIN-nod: värdet = min(barnens värden)”),
beräkningen nod för nod och trädet med alla värden. Alfa–beta räknas med en egen spårning som jämförs med
ai_speltrad.alphabeta.

  python tools/bygg-ai-speltrad-nivaer-2026-11-23.py [--skriv]
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ai_figurer import step, facit, esc, INK  # noqa: E402
import ai_speltrad as T  # noqa: E402

BANK = os.path.join(HERE, '..', 'uppgifterai.js')
SKRIV = '--skriv' in sys.argv
INF = float('inf')
POANG = {'E': '1/0/0', 'C': '0/1/0', 'A': '0/0/1'}
NIVA = {1: 'E', 2: 'E', 3: 'C', 4: 'A', 5: 'A'}

def _vinst(vem, enhet):
    def f(v):
        if v >= 0:
            return f'{vem} kan räkna med en vinst på {v} {enhet} om båda väljer så bra de kan.'
        return f'{vem} måste räkna med en förlust på {-v} {enhet} om båda väljer så bra de kan.'
    return f


def _robotar(v):
    if v > 0:
        return f'Om båda robotarna väljer så bra de kan får den blå roboten {v} fler batterier än den röda.'
    if v < 0:
        return f'Om båda robotarna väljer så bra de kan får den röda roboten {-v} fler batterier än den blå.'
    return 'Om båda robotarna väljer så bra de kan får de lika många batterier.'


def _sparare(v):
    if v >= 0:
        return f'Spararen kan räkna med en vinst på {v} hundra kronor, även om börsen går så dåligt som möjligt.'
    return f'Spararen måste räkna med en förlust på {-v} hundra kronor om börsen går så dåligt som möjligt.'


def _stickor(v):
    if v > 0:
        return f'Om båda spelar så bra de kan vinner Ada med {v} poäng.'
    if v < 0:
        return f'Om båda spelar så bra de kan vinner Bo med {-v} poäng.'
    return 'Om båda spelar så bra de kan blir det oavgjort.'


# Mycket enkla tillämpningar (användarönskemål 2026-11-23): vem som är MAX och MIN, och vad talen i löven betyder.
# neg: om talen kan vara negativa i sammanhanget. tolk: vad rotens värde betyder.
KONTEXTER = [
    dict(sit='En butik och en konkurrent sätter priser i tur och ordning.', max='butiken', min='konkurrenten',
         tal='butikens vinst i tusentals kronor, där ett negativt tal betyder förlust', neg=True,
         tolk=_vinst('Butiken', 'tusen kronor')),
    dict(sit='En säljare och en köpare förhandlar om priset på en begagnad bil.', max='säljaren', min='köparen',
         tal='slutpriset i tusentals kronor', neg=False,
         tolk=lambda v: f'Om båda förhandlar så bra de kan blir priset {v} tusen kronor.'),
    dict(sit='Två robotar tävlar om att samla batterier på en bana.', max='den blå roboten', min='den röda roboten',
         tal='hur många fler batterier den blå roboten får än den röda, där ett negativt tal betyder att den röda får flest',
         neg=True, tolk=_robotar),
    dict(sit='En vaktrobot väljer var den ska patrullera, och en inkräktare väljer var den ska försöka ta sig in i ett lager.',
         max='vaktroboten', min='inkräktaren', tal='hur säkert lagret är, där ett högre tal betyder säkrare', neg=False,
         tolk=lambda v: f'Vaktroboten kan se till att säkerheten blir {v}, hur inkräktaren än väljer.'),
    dict(sit='En drönare väljer flygväg med ett paket, och vinden kan ändra riktning på sämsta tänkbara sätt.',
         max='drönaren', min='vinden', tal='hur många minuter drönaren kan flyga vidare när paketet är levererat', neg=False, maxforst=True,
         tolk=lambda v: f'Drönaren kan räkna med {v} minuters flygtid kvar, även om vinden blir så dålig som möjligt.'),
    dict(sit='En sparare väljer mellan olika fonder och räknar med att börsen utvecklas så dåligt som möjligt.',
         max='spararen', min='börsen', tal='vinsten i hundratals kronor efter ett år, där ett negativt tal betyder förlust',
         neg=True, maxforst=True, tolk=_sparare),
    dict(sit='En schackdator spelar mot en människa.', max='datorn', min='människan',
         tal='datorns bedömning av slutläget, där ett högt tal är bra för datorn', neg=True,
         tolk=lambda v: f'Om båda spelar så bra de kan blir datorns bedömning av slutläget {T.fmt(v)}.'),
    dict(sit='I robotfotboll turas två robotar om att välja drag.', max='den gula roboten', min='den gröna roboten',
         tal='hur bra läget är för den gula roboten, där ett negativt tal betyder att den gröna har övertaget', neg=True,
         tolk=lambda v: f'Om båda robotarna väljer så bra de kan blir läget värt {T.fmt(v)} för den gula roboten.'),
    dict(sit='Två företag väljer i tur och ordning hur mycket de ska satsa på reklam.', max='företaget Alfa',
         min='företaget Beta', tal='Alfas vinst i miljoner kronor, där ett negativt tal betyder förlust', neg=True,
         tolk=_vinst('Alfa', 'miljoner kronor')),
    dict(sit='En lagerrobot planerar sin väg, och en annan robot kan ställa sig i vägen.', max='lagerroboten',
         min='den andra roboten', tal='hur många paket lagerroboten hinner leverera på en timme', neg=False,
         tolk=lambda v: f'Lagerroboten kan räkna med att hinna leverera {v} paket, även om den andra roboten ställer sig så illa som möjligt.'),
    dict(sit='En spelagent spelar luffarschack mot en människa.', max='spelagenten', min='människan',
         tal='hur bra slutläget är för spelagenten, där ett negativt tal betyder att människan har övertaget', neg=True,
         tolk=lambda v: f'Om båda spelar så bra de kan blir slutläget värt {T.fmt(v)} för spelagenten.'),
    dict(sit='Ada och Bo tar stickor från en hög i tur och ordning.', max='Ada', min='Bo',
         tal='Adas poäng när stickorna är slut, där ett negativt tal betyder att Bo vinner', neg=True, tolk=_stickor),
]


_SPEL = [
    'Två spelare turas om i ett enkelt brädspel. Talen i löven är MAX:s poäng när spelet är slut.',
    'En schackdator räknar några drag framåt. Talen i löven är datorns bedömning av slutlägena.',
    'I ett kortspel för två väljer spelarna kort i tur och ordning. Talen visar MAX:s poäng i slutläget.',
    'En spelagent i luffarschack bedömer slutlägena med tal, där högt är bra för MAX.',
    'Två elever spelar ett räknespel. Talen i löven är vad MAX vinner, och ett negativt tal betyder att MAX förlorar.',
    'En dator spelar fyra i rad mot en människa. Talen i löven är datorns bedömning av slutläget.',
    'I ett strategispel planerar en spelagent sina drag. Talen i löven är MAX:s poäng.',
    'Två robotar spelar ett spel där de turas om att flytta. Talen i löven är MAX:s poäng.',
    'En spelapp föreslår drag i ett pusselspel för två. Talen i löven är MAX:s poäng när spelet är slut.',
    'I ett brädspel utan tärning räknar datorn igenom alla drag. Högt tal är bra för MAX och lågt för MIN.',
    'En AI i ett datorspel väljer drag mot en mänsklig spelare. Talen i löven är AI:ns poäng i slutläget.',
    'Två spelare tar stickor i tur och ordning. Talen i löven är MAX:s poäng när stickorna är slut.',
]
SPEL = [dict(spel=t, neg=True, tolk=lambda v: f'Om båda väljer så bra de kan slutar spelet i ett läge som är värt {T.fmt(v)} för MAX.')
        for t in _SPEL]


def kontext_text(k, rm):
    if 'spel' in k:
        return f'{k["spel"]} {"MAX" if rm else "MIN"} väljer först.'
    forst = k['max'] if rm else k['min']
    return (f'{k["sit"]} {k["max"][:1].upper() + k["max"][1:]} är MAX och {k["min"]} är MIN. '
            f'Först väljer {forst}. Talen i löven är {k["tal"]}.')


# ---------------------------------------------------------------- figur

def figur(r, root_max, titel, varden=None, beskurna=(), markera=None, spacing=60):
    """Spelträd i samma stil som ai_figurer.game_tree. varden: nod -> text bredvid noden.
    beskurna: namn på barn (noder eller löv) vars gren beskärs. markera: (nod, text) som ringas in."""
    varden = varden or {}
    beskurna = set(beskurna)
    lov = T.leaves(r)
    W = max(420, len(lov) * spacing + 40)
    idx = [0]
    pos = {}

    def place(n, depth):
        y = 60 + depth * 88
        if 'leaf' in n:
            x = 20 + spacing / 2 + idx[0] * spacing + (W - 40 - len(lov) * spacing) / 2
            idx[0] += 1
        else:
            xs = [place(k, depth + 1) for k in n['kids']]
            x = sum(xs) / len(xs)
        pos[n['name']] = (x, y)
        return x
    place(r, 0)

    under = set()

    def markera_under(n, av):
        if av:
            under.add(n['name'])
        for k in n.get('kids', []):
            markera_under(k, av or k['name'] in beskurna)
    markera_under(r, False)

    out = []

    def linjer(n):
        x1, y1 = pos[n['name']]
        for k in n.get('kids', []):
            x2, y2 = pos[k['name']]
            if k['name'] in under:
                out.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" stroke="#d94343" stroke-width="1.8" stroke-dasharray="6 5"/>')
                if k['name'] in beskurna:  # kryss mitt på den beskurna grenen
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    out.append(f'<line x1="{mx - 7:.1f}" y1="{my - 7:.1f}" x2="{mx + 7:.1f}" y2="{my + 7:.1f}" stroke="#d94343" stroke-width="3"/>'
                               f'<line x1="{mx - 7:.1f}" y1="{my + 7:.1f}" x2="{mx + 7:.1f}" y2="{my - 7:.1f}" stroke="#d94343" stroke-width="3"/>')
            else:
                out.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" stroke="#64748b" stroke-width="1.8"/>')
            linjer(k)
    linjer(r)

    maxy = 0
    for n in _alla(r):
        x, y = pos[n['name']]
        nere = n['name'] in under
        if 'leaf' in n:
            fyll, farg = ('#f1f5f9', '#94a3b8') if nere else ('#fff', INK)
            out.append(f'<rect x="{x - 18:.1f}" y="{y - 16}" width="36" height="32" rx="3" fill="{fyll}" stroke="#64748b"/>'
                       f'<text x="{x:.1f}" y="{y + 7}" text-anchor="middle" font-size="18" fill="{farg}">{T.fmt(n["leaf"])}</text>'
                       f'<text x="{x:.1f}" y="{y + 34}" text-anchor="middle" font-size="12" fill="#475569">{n["name"]}</text>')
            maxy = max(maxy, y)
            continue
        mx = n['max']
        if mx:
            pts = f'{x:.1f},{y - 19} {x + 22:.1f},{y + 16} {x - 22:.1f},{y + 16}'
            fyll, kant = '#dbf5f1', '#14857f'
        else:
            pts = f'{x - 22:.1f},{y - 16} {x + 22:.1f},{y - 16} {x:.1f},{y + 19}'
            fyll, kant = '#fff0d9', '#b86b16'
        if nere:
            fyll, kant = '#f1f5f9', '#94a3b8'
        mark = markera and markera[0] == n['name']
        if mark:
            kant = '#7c3aed'
        out.append(f'<polygon points="{pts}" fill="{fyll}" stroke="{kant}" stroke-width="{4 if mark else 2.5}"/>')
        out.append(f'<text x="{x + 27:.1f}" y="{y + 6}" font-size="17" fill="#334155">{esc(n["name"])}</text>')
        if mark:  # α och β på två rader till vänster om noden, på vit bakgrund
            rader = markera[1]
            bredd = 8.5 * max(len(t) for t in rader) + 10
            x0 = x - 28 - bredd if x - 28 - bredd >= 4 else x + 46   # till höger om namnet om det inte får plats
            out.append(f'<rect x="{x0:.1f}" y="{y - 21}" width="{bredd:.1f}" height="40" rx="4" fill="#ffffff" fill-opacity="0.92" stroke="#7c3aed"/>')
            for k, t in enumerate(rader):
                out.append(f'<text x="{x0 + bredd - 5:.1f}" y="{y - 5 + 17 * k}" text-anchor="end" font-size="14" font-weight="bold" fill="#7c3aed">{esc(t)}</text>')
        elif n['name'] in varden:
            t = varden[n['name']]
            bredd = 8.5 * len(t) + 8
            out.append(f'<rect x="{x - 32 - bredd + 4:.1f}" y="{y - 9}" width="{bredd:.1f}" height="20" rx="3" fill="#ffffff" fill-opacity="0.9"/>'
                       f'<text x="{x - 28:.1f}" y="{y + 6}" text-anchor="end" font-size="15" font-weight="bold" fill="#14532d">{esc(t)}</text>')
    out.append('<polygon points="20,7 29,23 11,23" fill="#dbf5f1" stroke="#14857f"/><text x="38" y="22" font-size="14" fill="#334155">MAX</text>'
               '<polygon points="110,7 128,7 119,23" fill="#fff0d9" stroke="#b86b16"/><text x="137" y="22" font-size="14" fill="#334155">MIN</text>')
    H = maxy + 44
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H}" role="img" '
           f'aria-label="Spelträd. Uppåtriktad triangel är MAX, nedåtriktad är MIN." '
           f'style="width:100%;max-width:{W:.0f}px;min-width:{min(W, 420):.0f}px;height:auto"><title>{esc(titel)}</title>'
           + ''.join(out) + '</svg>')
    return f'<div style="overflow-x:auto">{svg}</div>'


def _alla(n):
    yield n
    for k in n.get('kids', []):
        yield from _alla(k)


def p(x):
    return f'<p>{x}</p>'


def djup(n, d=0):
    return d if 'leaf' in n else max(djup(k, d + 1) for k in n['kids'])


def titel(r, root_max):
    ro = 'MAX' if root_max else 'MIN'
    return f'Spelträd med {ro} i roten R och {len(T.leaves(r))} löv, L1–L{len(T.leaves(r))}.'


# ---------------------------------------------------------------- minimax

def minimax_info(r):
    info = {}

    def mm(n):
        if 'leaf' in n:
            return n['leaf']
        vals = [mm(k) for k in n['kids']]
        v = max(vals) if n['max'] else min(vals)
        info[n['name']] = (n['max'], [k['name'] for k in n['kids']], vals, v)
        return v
    return mm(r), info


def mm_rad(nm, info):
    mx, _, vals, v = info[nm]
    return f'{nm} = {"max" if mx else "min"}({", ".join(T.fmt(x) for x in vals)}) = {T.fmt(v)}.'


# ---------------------------------------------------------------- alfa–beta med spårning

def ab_spar(r):
    """Alfa–beta med vänster gren först. Returnerar värde och händelser:
    ('in', nod, α, β), ('lov', löv, värde, förälder), ('klar', nod, värde, exakt, förälder),
    ('ny', nod, 'α'|'β', värde), ('cut', nod, α, β, beskurna barn)."""
    ev = []

    def ab(n, a, b, foralder):
        if 'leaf' in n:
            ev.append(('lov', n['name'], n['leaf'], foralder))
            return n['leaf'], True
        ev.append(('in', n['name'], a, b))
        v = -INF if n['max'] else INF
        cut = False
        for i, k in enumerate(n['kids']):
            x, _ = ab(k, a, b, n['name'])
            if n['max']:
                v = max(v, x)
                if v > a:
                    a = v
                    ev.append(('ny', n['name'], 'α', a))
            else:
                v = min(v, x)
                if v < b:
                    b = v
                    ev.append(('ny', n['name'], 'β', b))
            if a >= b and i + 1 < len(n['kids']):
                ev.append(('cut', n['name'], a, b, [kk['name'] for kk in n['kids'][i + 1:]]))
                cut = True
                break
        ev.append(('klar', n['name'], v, not cut, foralder))
        return v, not cut

    v, _ = ab(r, -INF, INF, None)
    return v, ev


def f_ab(x):
    return '−∞' if x == -INF else '+∞' if x == INF else T.fmt(x)


def ab_kontroll(r):
    v, ev = ab_spar(r)
    v2, utv, cuts, notes = T.alphabeta(r)
    assert v == v2
    assert [e[1] for e in ev if e[0] == 'lov'] == utv
    assert [(e[1], e[2], e[3]) for e in ev if e[0] == 'cut'] == [(c[0], c[2], c[3]) for c in cuts]
    return v, ev, cuts, notes


def ab_varden(notes):
    """Text bredvid noderna i facitfiguren: exakt värde eller gräns."""
    out = {}
    for nm, no in notes.items():
        if no['kind'] == 'exakt':
            out[nm] = f'= {T.fmt(no["value"])}'
        else:
            out[nm] = ('≥ ' if no['max'] else '≤ ') + T.fmt(no['value'])
    return out


# ---------------------------------------------------------------- slumpträd

def sok(seed, bygg, ok, sedda):
    rng = random.Random(seed)
    for _ in range(20000):
        v, rm = bygg(rng)
        key = json.dumps([v, rm])
        if key in sedda:
            continue
        if ok(v, rm):
            sedda.add(key)
            return v, rm
    raise RuntimeError(f'inget träd för frö {seed}')


def varden(rng, n, lo, hi):
    return rng.sample(range(lo, max(hi, lo + n - 1) + 1), n)   # olika värden även i stora träd (förkastas sedan av villkoren)


def fyll(form, vals):
    it = iter(vals)

    def f(x):
        return [f(k) for k in x] if isinstance(x, list) else next(it)
    return f(form)


def antal_lov(form):
    return sum(antal_lov(k) for k in form) if isinstance(form, list) else 1


def form2(rng, barn, lov):
    return [[0] * rng.choice(lov) for _ in range(rng.choice(barn))]


def form3(rng, barn1, barn2, lov, lovchans=0.0):
    ut = []
    for _ in range(rng.choice(barn1)):
        k = []
        for _ in range(rng.choice(barn2)):
            k.append(0 if rng.random() < lovchans else [0] * rng.choice(lov))
        if all(not isinstance(x, list) for x in k):
            k[0] = [0] * rng.choice(lov)
        ut.append(k)
    return ut


def inte_trivial(v, rm):
    r = T.build(v, rm)
    rot, _ = minimax_info(r)
    lovv = _platt(v)
    return rot not in (max(lovv), min(lovv)) and len(lovv) == len(set(lovv))


def _platt(v):
    return [x for k in v for x in _platt(k)] if isinstance(v, list) else [v]


# ---------------------------------------------------------------- uppgifter

def bas(id_, omr, familj, tn, intro, fraga, s, ledtrad, svar, formaga, kg=None):
    """Fristående kort med en fråga. svar: dict med svarstyp, rättSvar, tolerans, svarFormat, ev. svarEtiketter."""
    niva = NIVA[tn]
    del_ = {'fraga': p(fraga), 's': s, 'ledtrad': p(ledtrad), 'alternativ': [], 'visaAlternativ': False,
            'traningsniva': tn, 'arbetsinsats': 1 if tn <= 2 else 2, 'niva': niva, 'poang': POANG[niva],
            'miniräknare': True, 'geogebra': False, 'självrättning': True, 'spel': True, 'svarEnhet': None,
            'etikett': 'a'}
    del_.update(svar)
    if kg:
        del_['kgInstruktion'] = kg
    u = {'id': id_, 'kap': 3, 'omr': omr, 'niva': niva, 'poang': POANG[niva], 'familj': familj, 'formaga': formaga,
         'traningsniva': tn, 'arbetsinsats': del_['arbetsinsats'], 'miniräknare': True, 'geogebra': False,
         'spel': True, 'självrättning': True, 'svarstyp': 'flera_delar',
         'rättSvar': [del_['rättSvar']], 'tolerans': [del_['tolerans']], 'svarFormat': [del_['svarFormat']],
         'svarEnhet': [del_['svarEnhet']], 'svarsstruktur': 'ordnad', 'svarEtiketter': ['a'],
         't': intro + p(fraga), 's': s, 'ledtrad': p(ledtrad), 'spelIntro': intro,
         'spelDelning': 'deluppgifter', 'spelDelar': [del_], 'visaSomDelkort': True}
    return u


def intro_text(k, r, rm, metod):
    m = 'minimax' if metod == 'mm' else 'alfa–beta-beskärning (vänster gren först)'
    return p(kontext_text(k, rm)) + figur(r, rm, titel(r, rm)) + p(f'Spelträdet söks igenom med {m}.')


NUM = lambda v: {'svarstyp': 'numeriskt', 'rättSvar': v, 'tolerans': 0, 'svarFormat': 'numeriskt'}  # noqa: E731
ROTFRAGA = ['Vilket värde får roten?', 'Bestäm rotens minimaxvärde.', 'Vilket värde får rotnoden R?',
            'Bestäm värdet i roten R.', 'Vilket minimaxvärde får roten när båda väljer så bra de kan?']


# ---------------------------------------------------------------- ledtrådar (2026-11-23, andra omgången)
# Ledtrådarna nämner uppgiftens egna löv och den väg sökningen tar, så att ingen ledtråd står ordagrant i flera
# uppgifter (steg 3 i språkomskrivningen: specifika ledtrådar). De ger första steget, inte svaret.

def _lista(namn):
    namn = list(namn)
    return namn[0] if len(namn) == 1 else ', '.join(namn[:-1]) + ' och ' + namn[-1]


def _lov(n):
    return _lista(T.fmt(k['leaf']) for k in n['kids'] if 'leaf' in k)


def _vem(ktx, nod):
    """', där väljer konkurrenten' i tillämpningar, annars tomt."""
    if 'spel' in ktx:
        return ''
    return f', där väljer {ktx["max"] if nod["max"] else ktx["min"]}'


def _typ(nod):
    return 'MAX' if nod['max'] else 'MIN'


def led_minimax(r, ktx, djupen):
    noder = {n['name']: n for n in _alla(r) if 'leaf' not in n}
    djupast = djupen[max(djupen)]
    forsta = noder[djupast[0]]
    ord_ = 'största' if forsta['max'] else 'minsta'
    ovriga = djupast[1:]
    if max(djupen) == 1:
        rest = f'Gör likadant för {_lista(ovriga)}, och välj sedan som roten.'
    elif len(ovriga) <= 3:
        rest = f'Gör likadant för {_lista(ovriga)} och arbeta sedan uppåt, nivå för nivå, mot roten.'
    else:
        rest = 'Gör likadant för de andra noderna på samma nivå och arbeta sedan uppåt, nivå för nivå, mot roten.'
    return (f'{forsta["name"]} är en {_typ(forsta)}-nod{_vem(ktx, forsta)}. Den har löven {_lov(forsta)} och får det '
            f'{ord_} av dem. {rest}')


def led_beskarning(r, ktx, tn):
    a, b = r['kids'][0], r['kids'][1]
    if tn == 3:
        forsta_b = next(k for k in b['kids'])
        return (f'{a["name"]} är en {_typ(a)}-nod med löven {_lov(a)}. Vilket värde får {a["name"]}, och vad är roten då '
                f'säker på? {b["name"]}:s första löv är {T.fmt(forsta_b["leaf"])}. Kan {b["name"]} fortfarande bli bättre '
                f'för roten än {a["name"]}?')
    vag = [a['name']]
    n = a
    while 'kids' in n and 'leaf' not in n['kids'][0]:
        n = n['kids'][0]
        vag.append(n['name'])
    return (f'Sökningen börjar i R med α = −∞ och β = +∞ och går ned genom {_lista(vag)}. {n["name"]} är en '
            f'{_typ(n)}-nod med löven {_lov(n)}. Skriv α och β vid varje nod sökningen går in i, och uppdatera dem när '
            'ett barn blir klart. Var blir α ≥ β innan alla barn är undersökta?')


def led_ab5(r, mal, foralder):
    nod = mal[1]
    noder = {n['name']: n for n in _alla(r)}
    if mal[0] == 'in':
        klara = []
        barn = nod
        while barn in foralder:
            f = noder[foralder[barn]]
            for k in f['kids']:
                if k['name'] == barn:
                    break
                klara.append(k['name'])
            barn = f['name']
        vag = [nod]
        while vag[-1] in foralder:
            vag.append(foralder[vag[-1]])
        forsta = noder[klara[0]]
        om_forsta = (f' {forsta["name"]} har löven {_lov(forsta)}.' if 'kids' in forsta and
                     all('leaf' in k for k in forsta['kids']) else '')
        return (f'Vägen ned till {nod} går genom {_lista(list(reversed(vag[1:])))}. När sökningen kommer fram är '
                f'{_lista(sorted(klara, key=lambda x: (x.startswith("L"), x)))} redan klara.{om_forsta} Vad gjorde de '
                'med α och β på vägen ned?')
    f = foralder[nod]
    barn = [f'{k["name"]} = {T.fmt(k["leaf"])}' if 'leaf' in k else k['name'] for k in noder[nod]['kids']]
    return (f'{nod} får α och β från {f} när sökningen går in i {nod}. Gå sedan igenom {nod}:s barn '
            f'{_lista(barn)} ett i taget och uppdatera {"α" if noder[nod]["max"] else "β"} när ett barn blir klart. '
            'När blir α ≥ β?')


def mm_uppgift(id_, ktx, qv, v, rm, tn):
    r = T.build(v, rm)
    rot, info = minimax_info(r)
    ro, bn = ('MAX', 'MIN') if rm else ('MIN', 'MAX')
    steg = []
    # nivå för nivå nedifrån: alla inre noder utom roten, grupperade efter djup
    djupen = {}

    def gaa(n, d):
        if 'leaf' in n:
            return
        djupen.setdefault(d, []).append(n['name'])
        for k in n['kids']:
            gaa(k, d + 1)
    gaa(r, 0)
    for d in sorted(djupen, reverse=True):
        if d == 0:
            continue
        mx = info[djupen[d][0]][0]
        typ, op = ('MAX', 'max') if mx else ('MIN', 'min')
        namn = ', '.join(djupen[d])
        steg.append(step(f'{typ}-noderna {namn}: värdet = {op}(barnens värden)', *[mm_rad(nm, info) for nm in djupen[d]]))
    op = 'max' if rm else 'min'
    barn = [k['name'] for k in r['kids']]
    steg.append(step(f'Roten är en {ro}-nod: R = {op}({", ".join(barn)})', mm_rad('R', info)))
    steg.append(step('Vad värdet betyder', ktx['tolk'](rot)))
    steg.append(step('Trädet med alla värden',
                     figur(r, rm, 'Spelträdet med minimaxvärdet vid varje inre nod.', varden={n: f'= {T.fmt(x[3])}' for n, x in info.items()})))
    s = facit(steg, f'{T.fmt(rot)}.')
    ledtrad = led_minimax(r, ktx, djupen)
    fraga = ROTFRAGA[qv % len(ROTFRAGA)]
    return bas(id_, 'minimax', 'Minimaxvärden och bästa drag', tn, intro_text(ktx, r, rm, 'mm'), fraga, s, ledtrad, NUM(rot), ['procedur'])


AB_REGEL = ('α är det bästa värde MAX redan är säker på, och β det bästa MIN redan är säker på. '
            'När α ≥ β i en nod kan resten av nodens barn hoppas över, eftersom de inte kan ändra rotens val.')
BESK_FRAGA = {3: ['Vilken gren beskärs? Ange de löv som aldrig utvärderas.', 'Vilka löv behöver aldrig utvärderas?',
                  'Vilka löv beskärs?', 'Vilka löv hoppar alfa–beta över?',
                  'Vilken gren behöver aldrig undersökas? Ange dess löv.'],
              4: ['Vilka grenar beskärs? Ange de löv som aldrig utvärderas.', 'Vilka löv behöver aldrig utvärderas?',
                  'Vilka löv beskärs med alfa–beta?', 'Vilka löv hoppar alfa–beta över?',
                  'Vilka grenar behöver aldrig undersökas? Ange deras löv.']}
KG_LOV = 'Skriv beteckningarna på löven, åtskilda med kommatecken.'


def besk_uppgift(id_, ktx, qv, v, rm, tn):
    r = T.build(v, rm)
    val_, ev, cuts, notes = ab_kontroll(r)
    pr = T.pruned_leaves(cuts)
    beskurna = [k['name'] for c in cuts for k in c[4]]
    steg = [step('Alfa–beta: sluta undersöka en nod när α ≥ β', AB_REGEL)]
    for k in r['kids']:
        if k['name'] in notes:
            rader = T.subtree_lines(k, notes)
        else:
            rader = [f'Grenen till {k["name"]} undersöks inte alls.']
        steg.append(step(f'Grenen till {k["name"]}', *rader))
    steg.append(step('Roten', T.node_line('R', notes['R']), ktx['tolk'](val_)))
    steg.append(step(f'Löv som aldrig utvärderas: {len(pr)} st', ', '.join(pr) + '.',
                     figur(r, rm, 'Spelträdet med värden och beskurna grenar.', varden=ab_varden(notes), beskurna=beskurna)))
    s = facit(steg, ', '.join(pr) + '.')
    ledtrad = led_beskarning(r, ktx, tn)
    fraga = BESK_FRAGA[tn][qv % len(BESK_FRAGA[tn])]
    svar = {'svarstyp': 'kort_text', 'rättSvar': ', '.join(pr), 'tolerans': None, 'svarFormat': 'namnmangd'}
    return bas(id_, 'alfa_beta', 'Rotvärde och beskurna löv', tn, intro_text(ktx, r, rm, 'ab'), fraga, s, ledtrad, svar,
               ['procedur'], kg=KG_LOV)


def ab_beskriv(e, maxnod):
    typ = e[0]
    if typ == 'in':
        ro = 'MAX' if maxnod[e[1]] else 'MIN'
        return f'Sökningen går in i {e[1]} ({ro}-nod) med α = {f_ab(e[2])} och β = {f_ab(e[3])}.'
    if typ == 'lov':
        return f'{e[1]} = {T.fmt(e[2])} utvärderas.'
    if typ == 'klar':
        return f'{e[1]} är klar med värdet {T.fmt(e[2])}.' if e[3] else \
            f'{e[1]} är klar och blir {"minst" if maxnod[e[1]] else "högst"} {T.fmt(e[2])}.'
    if typ == 'ny':
        return f'{e[1]} {"höjer α" if e[2] == "α" else "sänker β"} till {T.fmt(e[3])}.'
    if typ == 'cut':
        return (f'I {e[1]} är nu α = {f_ab(e[2])} ≥ β = {f_ab(e[3])}, så '
                f'{" och ".join(e[4])} beskärs.')


def ab5_uppgift(id_, ktx, qv, v, rm, mal):
    """mal = ('in', nod) eller ('cut', nod)."""
    r = T.build(v, rm)
    val_, ev, cuts, notes = ab_kontroll(r)
    maxnod = {n['name']: n['max'] for n in _alla(r) if 'leaf' not in n}
    foralder = {}
    for n in _alla(r):
        for k in n.get('kids', []):
            foralder[k['name']] = n['name']
    nod = mal[1]
    vag = [nod]
    while vag[-1] in foralder:
        vag.append(foralder[vag[-1]])
    vag = set(vag)
    # händelserna fram till frågans ögonblick
    for slut, e in enumerate(ev):
        if e[0] == mal[0] and e[1] == nod:
            break
    else:
        raise AssertionError(id_)
    a, b = ev[slut][2], ev[slut][3]
    assert abs(a) != INF and abs(b) != INF, id_
    # figurens läge: noder som är klara före ögonblicket och grenar som redan har beskurits (även den nya)
    klara = {}
    for e in ev[:slut]:
        if e[0] == 'klar':
            klara[e[1]] = f'= {T.fmt(e[2])}' if e[3] else ('≥ ' if maxnod[e[1]] else '≤ ') + T.fmt(e[2])
    beskurna = [k for e in ev[:slut + 1] if e[0] == 'cut' for k in e[4]]
    rader = []
    for e in ev[:slut + 1]:
        visa = (e[0] in ('in', 'ny', 'cut') and e[1] in vag) or \
               (e[0] in ('klar', 'lov') and e[-1] in vag)
        if visa:
            rader.append(ab_beskriv(e, maxnod))
    steg = [step('α och β förs nedåt i trädet',
                 'Varje nod får α och β från sin förälder. En MAX-nod höjer α när ett barn ger mer, och en MIN-nod sänker β '
                 'när ett barn ger mindre. Beskärning sker när α ≥ β.'),
            step(f'Sökningen fram till {nod}, gren för gren', *rader),
            step(f'Läget i trädet när {"beskärningen sker" if mal[0] == "cut" else "sökningen går in i " + nod}',
                 figur(r, rm, f'Spelträdet med noden {nod} markerad och värdena som är klara i det ögonblicket.',
                       varden=klara, beskurna=beskurna, markera=(nod, [f'α = {f_ab(a)}', f'β = {f_ab(b)}'])))]
    s = facit(steg, f'α = {f_ab(a)} och β = {f_ab(b)}.')
    if mal[0] == 'in':
        fraga = [f'Vilka värden har α och β när sökningen går in i noden {nod}?',
                 f'Sökningen kommer fram till noden {nod}. Vilka värden har α och β där innan något av {nod}:s barn har undersökts?'][qv % 2]
        ledtrad = led_ab5(r, mal, foralder)
    else:
        fraga = [f'I noden {nod} sker en beskärning. Vilka värden har α och β i {nod} precis när den sker?',
                 f'Alfa–beta beskär en del av trädet under noden {nod}. Vilka värden har α och β i {nod} när beskärningen sker?'][qv % 2]
        ledtrad = led_ab5(r, mal, foralder)
    svar = {'svarstyp': 'flera_delar', 'rättSvar': [a, b], 'tolerans': [0, 0], 'svarFormat': ['numeriskt', 'numeriskt'],
            'svarsstruktur': 'ordnad', 'svarEtiketter': ['α', 'β'], 'svarEnhet': [None, None]}
    u = bas(id_, 'alfa_beta', 'Rotvärde och beskurna löv', 5, intro_text(ktx, r, rm, 'ab'), fraga, s, ledtrad, svar,
            ['procedur', 'begrepp'])
    u['svarEnhet'] = [[None, None]]
    return u


# ---------------------------------------------------------------- urval av träd

def ren_text(html):
    import re
    t = re.sub(r'<svg\b[\s\S]*?</svg\s*>', ' figur ', html)
    t = re.sub(r'<[^>]+>', ' ', t).lower()
    return ' '.join(re.sub(r'[^a-zåäö0-9#]+', ' ', t).split())


FRAGOR = {1: len(ROTFRAGA), 2: len(ROTFRAGA), 3: 5, 4: 5, 5: 2}


def trad(niva, seed, rm, lo, hi, sedda, typ=None):
    """Slumpar ett träd för nivån. Nivå 5 ger också noden som frågan gäller."""
    if niva == 1:
        def b(rng):
            f = form2(rng, [2, 3], [2, 2, 3])
            return fyll(f, varden(rng, antal_lov(f), lo, min(hi, lo + 11))), rm

        def ok(v, rm):
            return 4 <= len(_platt(v)) <= 7 and inte_trivial(v, rm)
    elif niva == 2:
        bred = seed % 5 == 4

        def b(rng):
            f = form2(rng, [4], [3, 3, 4]) if bred else form3(rng, [2, 3], [2, 3], [2, 2, 3], lovchans=0.2 if rng.random() < 0.5 else 0)
            return fyll(f, varden(rng, antal_lov(f), lo, hi)), rm

        def ok(v, rm):
            n = len(_platt(v))
            return 8 <= n <= 14 and inte_trivial(v, rm) and (djup(T.build(v, rm)) == 3 or n >= 12)
    elif niva == 3:
        def b(rng):
            f = form2(rng, [2, 3, 3], [2, 3, 3])
            return fyll(f, varden(rng, antal_lov(f), max(lo, 1), max(hi, 15))), rm

        def ok(v, rm):
            if not 5 <= len(_platt(v)) <= 9:
                return False
            _, _, cuts, _ = T.alphabeta(T.build(v, rm))
            return len(cuts) == 1
    elif niva == 4:
        def b(rng):
            f = form3(rng, [2, 3], [2, 3], [2, 2, 3])
            return fyll(f, varden(rng, antal_lov(f), lo, hi)), rm

        def ok(v, rm):
            n = len(_platt(v))
            if not 8 <= n <= 14:
                return False
            r = T.build(v, rm)
            _, _, cuts, _ = T.alphabeta(r)
            pr = T.pruned_leaves(cuts)
            hel = any('leaf' not in k for c in cuts for k in c[4])
            djupt = any(c[0] != 'R' and c[0] not in [k['name'] for k in r['kids']] for c in cuts)
            return len(cuts) >= 2 and len(pr) >= 3 and (hel or djupt) and len(pr) < n - 3
    else:
        def b(rng):
            f = form3(rng, [2, 3], [2, 3], [2, 3])
            return fyll(f, varden(rng, antal_lov(f), lo, hi)), rm

        def ok(v, rm):
            return 8 <= len(_platt(v)) <= 13 and bool(kandidater(v, rm, typ))
    v, rm = sok(seed, b, ok, sedda)
    if niva == 5:
        return v, random.Random(seed).choice(kandidater(v, rm, typ))
    return v, None


def kandidater(v, rm, typ):
    r = T.build(v, rm)
    _, ev = ab_spar(r)
    djup2 = {kk['name'] for k in r['kids'] for kk in k.get('kids', []) if 'leaf' not in kk}
    return [e[1] for e in ev if e[0] == typ and e[1] in djup2 and abs(e[2]) != INF and abs(e[3]) != INF]


def gor(niva, id_, k, qv, v, rm, nod, typ):
    if niva <= 2:
        return mm_uppgift(id_, k, qv, v, rm, niva)
    if niva <= 4:
        return besk_uppgift(id_, k, qv, v, rm, niva)
    return ab5_uppgift(id_, k, qv, v, rm, (typ, nod))


def ren_text(html):
    import re
    t = re.sub(r'<svg\b[\s\S]*?</svg\s*>', ' figur ', html)
    t = re.sub(r'<[^>]+>', ' ', t).lower()
    return ' '.join(re.sub(r'[^a-zåäö0-9#]+', ' ', t).split())


GRUND = {1: 30, 2: 30, 3: 25, 4: 25, 5: 25}   # 3.81–3.215, spelsammanhang
TILLAMP = 8                                   # 3.216–3.255, åtta per nivå, bara tillämpningar
VARDEN = {1: (1, 12), 2: (-9, 15), 3: (1, 15), 4: (-9, 15), 5: (-9, 15)}


def alla():
    sedda, texter, ut = set(), set(), []
    nr = [81]

    def unik(i, kontexter, niva, v, rm, nod, typ):
        """Välj kontext och frågeformulering så att texten blir unik i banken (validatorns EXACT_TEXT_DUPLICATE)."""
        L, Q = len(kontexter), FRAGOR[niva]
        for steg_ in range(L * Q):
            k = kontexter[(i + steg_) % L]
            if min(_platt(v)) < 0 and not k['neg']:
                continue
            id_ = f'3.{nr[0]}'
            u = gor(niva, id_, k, (i + steg_ // L) % Q, v, rm, nod, typ)
            key = ren_text(u['t'])
            if key not in texter:
                texter.add(key)
                nr[0] += 1
                return u
        raise RuntimeError(f'ingen unik text för nivå {niva}')

    # Grunduppgifter: spelsammanhang, MAX i roten i två av tre träd
    for niva, antal in GRUND.items():
        for i in range(antal):
            rm = i % 3 != (2 if niva in (1, 3, 5) else 1)
            typ = ('cut' if i % 2 == 0 else 'in') if niva == 5 else None
            v, nod = trad(niva, niva * 10000 + i, rm, *VARDEN[niva], sedda, typ)
            ut.append(unik(i * 5 + niva, SPEL, niva, v, rm, nod, typ))
    assert nr[0] == 216
    # Tillämpningar: kontexten väljs först, och talen passar sammanhanget (negativa bara där de betyder något)
    for niva in range(1, 6):
        for i in range(TILLAMP):
            k = KONTEXTER[(i * 5 + niva * 3) % len(KONTEXTER)]
            rm = i % 3 != 2 or k.get('maxforst', False)   # vinden och börsen väljer aldrig först
            typ = ('cut' if i % 2 == 0 else 'in') if niva == 5 else None
            lo, hi = VARDEN[niva]
            if not k['neg']:
                lo, hi = 1, (12 if niva == 1 else 20)
            v, nod = trad(niva, 60000 + niva * 1000 + i, rm, lo, hi, sedda, typ)
            ut.append(unik(KONTEXTER.index(k), KONTEXTER, niva, v, rm, nod, typ))
    assert nr[0] == 256
    return ut


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = alla()
    finns = {u['id'] for u in bank}
    for u in nya:
        k = next((k for k, x in enumerate(bank) if x['id'] == u['id']), None)
        if k is None:
            bank.append(u)
        else:
            bank[k] = u
    nytt = sum(u['id'] not in finns for u in nya)
    print(f'{len(nya)} uppgifter ({nytt} nya), {len(bank)} i banken')
    for tn in range(1, 6):
        print(f'  nivå {tn}: {sum(u["traningsniva"] == tn for u in nya)}')
    if SKRIV:
        with open(BANK, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
        print('skrivet')
    else:
        json.dump(nya, open(os.environ.get('UT', os.devnull), 'w', encoding='utf-8'), ensure_ascii=False)
        print('torrkörning')


if __name__ == '__main__':
    main()
