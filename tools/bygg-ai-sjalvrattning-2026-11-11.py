"""AI-banken 2026-11-11: de 95 manuella uppgifterna blir självrättande i Kunskapsgymmet.

Användarbeslut 2026-11-11: uppgifterna ska kunna tränas i Kunskapsgymmet, men de ska
fortfarande gå att använda på övningsblad och prov i Uppgiftslabbet utan att se
anpassade för automaträttning ut. Därför ändras ALDRIG uppgiftens text `t`, facit `s`
eller den gemensamma inledningen `spelIntro`; Uppgiftslabbet visar bara `t` och `s`.

Det som ändras finns bara i delkorten (`spelDelar`), som bara Kunskapsgymmet visar:
- `rättSvar`, `svarstyp`, `svarFormat`, `tolerans`, `svarEnhet`, `självrättning`, `spel`;
- en kort svarsinstruktion i parentes efter frågan, när svaret är en lista av namn,
  till exempel ”(Skriv rutorna i ordning, åtskilda med kommatecken.)”;
- namngivna svarsfält (`svarEtiketter`) när frågan efterfrågar flera värden,
  till exempel g, h och f;
- `visaSomDelkort: true` på uppgifter med ett enda delkort (2.06, 2.07, 2.08, 2.11),
  så att Kunskapsgymmet visar delkortet och inte huvudtexten;
- tre nya flervalsfrågor där frågan var en fri förklaring eller en olikhet
  (2.03c, 1.07d, 3.07c). Facit för delkortet behålls.

Svaren är hämtade ur delkortens facit, som de tidigare testerna räknar om med egna
simuleringar. tools/ai-sjalvrattning-2026-11-11.test.js kontrollerar att varje svar
stämmer med facit och räknar dessutom om köer, stackar, minimax och alfa–beta.

Format i Kunskapsgymmet: `namnordning` (ordnad lista av namn eller tal) och
`namnmangd` (oordnad). Facit "tom" betyder en tom lista. Flera godtagbara facit
skiljs med |.

Körs före bygg-ai-nivaer-2026-11-11.py. Idempotent.
"""
import json
import re

BANK = 'uppgifterai.js'

# Svarsinstruktioner (bara i Kunskapsgymmets delkort)
RO = 'Skriv rutorna i ordning, åtskilda med kommatecken.'
RV = 'Skriv rutorna längs vägen, från start till mål.'
NO = 'Skriv noderna i ordning, åtskilda med kommatecken.'
NV = 'Skriv noderna längs vägen, från start till mål.'
NT = 'Svara med noderna i den ordning de tas ut.'
RT = 'Svara med rutorna i den ordning de tas ut.'
LB = 'Skriv beteckningarna på löven, åtskilda med kommatecken.'
NN = 'Svara med nodens namn.'
RN = 'Svara med rutans namn.'
RM = 'Skriv rutorna, åtskilda med kommatecken.'
NM = 'Skriv noderna, åtskilda med kommatecken.'
SV = 'Skriv nodernas namn längs vägen och avsluta med lövets beteckning.'


def T(n):
    return ('tal', n)


def O(v, suf=None):
    return ('ord', v, suf)


def M(v, suf=None):
    return ('mangd', v, suf)


def F(fields, suf=None):
    """Flera svarsfält: (etikett, värde, typ) där typ är 'tal', 'ord' eller 'mangd'."""
    return ('falt', fields, suf)


def NA(alts):
    return ('nyalt', alts)


def a(txt, ratt, kommentar):
    return {'txt': txt, 'ratt': ratt, 'kommentar': kommentar}


SPEC = {
    # 1.01–1.31: köer, stackar, BFS och DFS
    '1.01a': O('A1, A2, B1, B2, C2, C3, D2, C4, D1, B4, D4, A4, D5', RO),
    '1.01b': O('A1, A2, B2, C2, C3, C4, D4, D5', RV), '1.01c': T(7), '1.01d': T(13),
    '1.02a': O('A1, A2, B2, C2, C3, C4, B4, A4, A5, D4, D5', RO),
    '1.02b': O('A1, A2, B2, C2, C3, C4, D4, D5', RV), '1.02c': T(7), '1.02d': T(11),
    '1.03a': O('A, B, C, D, E', NO), '1.03b': O('C, D, B, E, A', NO),
    '1.04a': O('S, A, B, C, D, E, F, G', NT), '1.04b': M('tom', NM),
    '1.05a': O('S, A, C, D, B, E, G', NT), '1.05b': M('F', NM),
    '1.06a': O('C1, B1, C2, B2, C3, A2, B3, A3, A4', RO), '1.06b': O('C1, B1, B2, A2, A3, A4', RV),
    '1.07a': O('E1, D1, C1, B1, A1, A2, B2, C2, C3, C4, C5, B5, A5, A6', RO),
    '1.07b': O('E1, D1, C1, B1, A1, A2, B2, C2, C3, C4, C5, B5, A5, A6', RV),
    '1.07d': NA([
        a('Ja, DFS hittar alltid den kortaste vägen.', False,
          'DFS följer en gren så långt det går och kan därför hitta en lång väg först.'),
        a('Nej, det finns en väg med 9 steg.', True,
          'BFS hittar vägen E1 → D1 → C1 → C2 → C3 → C4 → C5 → B5 → A5 → A6, som har 9 steg.'),
        a('Ja, det finns ingen annan väg till målet.', False,
          'Det finns en kortare väg: från C1 går den direkt åt höger i stället för upp till A1.'),
        a('Nej, det finns en väg med 11 steg.', False,
          'En väg med 11 steg är också kortare, men den kortaste vägen har 9 steg.'),
    ]),
    '1.08b': T(11),
    '1.09a': F([('Uttag', 'A, B, C, D', 'ord'), ('Väg', 'A, B, D', 'ord')], NO),
    '1.10b': O('P, R, S'),
    '1.11a': O('B, Y, X', NO), '1.11b': O('H', NN),
    '1.12b': O('A, B, C, D', NO),
    '1.13a': O('A1, A2, B1, A3, C1, B3, C2, C3', RT), '1.13b': O('A1, A2, A3, B3, C3', RV),
    '1.14b': O('B, C, D, E, F', 'Svara med noderna i den ordning de tas ut efter dem som redan står i tabellen.'),
    '1.14c': T(2),
    '1.15a': M('C3, D2', RM), '1.15b': T(6),
    '1.16a': O('A1, A2, A3, A4, B4, C4', RV), '1.16b': T(10),
    '1.17a': O('A1, A2, B2, C2, C3, C4, B4, A4, D4', RO),
    '1.17b': O('A1, A2, B2, C2, C3, C4, D4', RV), '1.17c': M('B4, A4', RM),
    '1.18a': F([('Väg', 'A1, A2, A3, A4, B4, B3, C3, D3, D4', 'ord'), ('Steg', 8, 'tal')], RV),
    '1.18b': F([('Väg', 'A1, B1, C1, D1, D2, D3, D4', 'ord'), ('Steg', 6, 'tal')], RV),
    '1.19b': O('C5', RN), '1.19c': T(6),
    '1.21a': F([('FIFO-kö', 'R, S, T', 'ord'), ('Stack', 'P, R, T', 'ord')],
               'Svara med kön och stacken efter sista steget, skrivna som i tabellen.'),
    '1.21b': F([('FIFO-kö', 'P, Q', 'ord'), ('Stack', 'Q, S', 'ord')], 'Skriv noderna i den ordning de tas ut.'),
    '1.22b': O('A, B, C, D, E, F', 'Svara med noderna i den ordning de tas ut, från och med A.'),
    '1.22c': T(6),
    '1.23a': O('S, A, B, C, G', NT),
    '1.24a': O('A1, A2, B1, B2, C1, C2', RO), '1.24b': T(8), '1.24c': T(18),
    '1.25a': O('B3, C4, C2'), '1.25c': T(4),
    '1.26a': O('S, A, C, E, F, D, B, G', NO), '1.26b': O('S, A, B, C, D, G', NO),
    '1.27b': O('A1, A2, B2, C2, C3', RV),
    '1.28a': O('A, C, F', 'Svara med stacken efter sista steget, med den översta noden längst till höger.'),
    '1.28b': O('B, E, D', NO),
    '1.29a': O('S, A, D, B, E, F, C, G', NT), '1.29b': T(8),
    '1.30a': O('A1, A2, B1, A3, C1, B3, C2, B4, C3, D2, B5, A5, C5, D5', RO),
    '1.30b': F([('Väg', 'A1, A2, A3, B3, B4, B5, C5, D5', 'ord'), ('Steg', 7, 'tal')], RV),
    '1.31a': O('A1, A2, B2, B3, C3, C4, C5, B5, A5, A4, D5', RO),
    '1.31b': F([('Väg', 'A1, A2, B2, B3, C3, C4, C5, D5', 'ord'), ('Steg', 7, 'tal')], RV),
    # 2.01–2.34: prioritetsköer, g/h/f, A* och viktade vägar
    '2.01a': F([('g', 2, 'tal'), ('h', 5, 'tal'), ('f', 7, 'tal')]),
    '2.01b': F([('g', 4, 'tal'), ('h', 3, 'tal'), ('f', 7, 'tal')]),
    '2.01c': F([('g', 5, 'tal'), ('h', 4, 'tal'), ('f', 9, 'tal')]),
    '2.02a': O('A1, A2, B2, C2, C3, C4, D4, D5', RO),
    '2.02b': O('A1, A2, B2, C2, C3, C4, D4, D5', RV), '2.02c': T(7), '2.02d': T(8),
    '2.03a': F([('Väg', 'A1, A2, A3, A4', 'ord'), ('Kostnad', 11, 'tal')], RV),
    '2.03b': F([('Väg', 'A1, B1, C1, C2, C3, C4, B4, A4', 'ord'), ('Kostnad', 7, 'tal')], RV),
    '2.03c': NA([
        a('Girig bäst först jämför bara h och ser inte vad vägen hittills har kostat. A* räknar med båda.', True,
          'Med f = g + h får den dyra vägen genom femmorna högre f, så A* väljer den billigare vägen runt väggarna.'),
        a('A* hittar alltid vägen med minst antal steg.', False,
          'A*:s väg har fler steg här. Den är billigare, inte kortare.'),
        a('Girig bäst först räknar med kostnaden hittills men inte med h.', False,
          'Det är tvärtom: girig bäst först använder bara h, uppskattningen av avståndet kvar.'),
        a('Algoritmerna väljer slumpmässigt bland grannarna.', False,
          'Båda följer fasta regler. De väljer olika för att de jämför olika värden.'),
    ]),
    '2.04a': O('B, D, A, F, E, C', NO), '2.04b': M('E, C', NM),
    '2.05a': F([('P', 8, 'tal'), ('Q', 7, 'tal'), ('R', 8, 'tal')]),
    '2.05b': O('P', RN), '2.05c': O('Q', RN),
    '2.07a': T(14),
    '2.10b': F([('Is', 19, 'tal'), ('Backe', 16, 'tal'), ('Vanlig väg', 10, 'tal')]),
    '2.12a': O('L, N, K, M', NO),
    '2.13c': O('D', NN),
    '2.14a': F([('P', 11, 'tal'), ('Q', 8, 'tal'), ('R', 9, 'tal'), ('T', 9, 'tal')]),
    '2.15a': F([('P', 5, 'tal'), ('Q', 3, 'tal'), ('R', 2, 'tal')]),
    '2.16a': F([('h', 2, 'tal'), ('f', 4, 'tal')]), '2.16b': T(8),
    '2.17a': F([('g för C1', 1, 'tal'), ('h för C1', 6, 'tal'), ('f för C1', 7, 'tal'),
                ('g för D2', 1, 'tal'), ('h för D2', 6, 'tal'), ('f för D2', 7, 'tal')]),
    '2.17c': O('D1, C1, C2, B2, A2, A3, C3, C4, B4, B5, A5', RO), '2.17d': M('B2, A2, A3', RM),
    '2.18a': F([('K', 10, 'tal'), ('L', 9, 'tal'), ('M', 11, 'tal'), ('N', 9, 'tal')]),
    '2.18c': O('P', RN),
    '2.19a': T(18), '2.19b': O('A1, A2, A3, A4, A5, B5, C5, D5', RO),
    '2.20a': T(8), '2.20b': O('S, A, B, C, M', NV),
    '2.21a': F([('Noder', 'S, A, B, D, M', 'ord'), ('f', '5, 5, 6, 6, 6', 'ord')],
               'Svara med noderna i den ordning de tas ut och deras f-värden i samma ordning.'),
    '2.21b': F([('Väg', 'S, A, B, D, M', 'ord'), ('Kostnad', 6, 'tal')], NV),
    '2.22a': T(10), '2.22b': T(14),
    '2.23a': O('P, S, M, K', NO), '2.23b': O('M', NN),
    '2.25a': T(4),
    '2.26b': T(4),
    '2.27a': F([('C1', 10, 'tal'), ('D2', 7, 'tal')]),
    '2.27b': F([('Girig bäst först', 'C1', 'ord'), ('A*', 'D2', 'ord')], 'Svara med rutornas namn.'),
    '2.27c': F([('Girig bäst först', 13, 'tal'), ('A*', 7, 'tal')]),
    '2.28a': O('A1, A2, A3, A4, B4, C4', RO), '2.28b': M('B1, B3', RM),
    '2.29a': T(6), '2.29b': O('A1, B1, C1, C2, D2, D3, D4', RV),
    '2.30a': F([('Väg', 'S, A, M', 'ord'), ('Kostnad', 11, 'tal')], NV),
    '2.30b': O('S, A, B, C, M', NO),
    '2.31a': O('B, D, E', NO), '2.31b': M('A, C', NM),
    '2.32a': F([('P', '3, 4, 7', 'ord'), ('Q', '3, 4, 7', 'ord'), ('R', '8, 1, 9', 'ord')],
               'Skriv g, h och f i den ordningen, åtskilda med kommatecken.'),
    '2.33a': O('A2, A3, A4, B3, C3, C4', RO), '2.33b': O('A4', RN),
    '2.34a': T(9), '2.34b': F([('Kostnad', 8, 'tal'), ('Steg', 8, 'tal')]),
    # 3.01–3.30: minimax och alfa–beta
    '3.01a': F([('A', 2, 'tal'), ('B', 4, 'tal'), ('C', 1, 'tal')]), '3.01b': T(4), '3.01c': O('B', NN),
    '3.02a': F([('C', 5, 'tal'), ('D', 9, 'tal'), ('E', 4, 'tal'), ('F', 8, 'tal'), ('A', 5, 'tal'), ('B', 4, 'tal')]),
    '3.02b': T(5), '3.02c': O('A', NN),
    '3.03a': O('3, 5, 6, 2, 4', 'Skriv lövens värden i den ordning de utvärderas.'),
    '3.03b': M('9, 7, 8', 'Skriv värdena på de löv som aldrig utvärderas.'),
    '3.03c': T(5), '3.03d': T(5),
    '3.04a': T(3), '3.04b': M('L7, L8', LB),
    '3.04c': F([('Nod', 'D', 'ord'), ('α', 3, 'tal'), ('β', 0, 'tal')], 'Ange noden där beskärningen sker och α och β där.'),
    '3.05a': T(6), '3.05b': M('L8, L12, L13, L14, L15, L16', LB),
    '3.05c': F([('Nod 1', 'G', 'ord'), ('α 1', 8, 'tal'), ('β 1', 6, 'tal'),
                ('Nod 2', 'K', 'ord'), ('α 2', 18, 'tal'), ('β 2', 6, 'tal'),
                ('Nod 3', 'H', 'ord'), ('α 3', 11, 'tal'), ('β 3', 6, 'tal')],
               'Ta beskärningarna i den ordning de sker: nod, α och β för var och en.'),
    '3.06a': T(5), '3.06b': T(5),
    '3.07a': T(4), '3.07b': T(7),
    '3.07c': NA([
        a('x ≥ 5', True, 'B = min(x, 7) blir större än A = 4 precis när x är 5 eller mer.'),
        a('x ≥ 4', False, 'Med x = 4 blir B = 4, alltså lika med A och inte större.'),
        a('x ≥ 7', False, 'Även x = 5 och x = 6 räcker. Då blir B = 5 eller 6, som är större än 4.'),
        a('x ≤ 4', False, 'Då blir B högst 4, och det är inte större än A.'),
    ]),
    '3.08a': F([('C', 4, 'tal'), ('D', 3, 'tal'), ('E', 2, 'tal')]),
    '3.08b': F([('A', 1, 'tal'), ('B', 2, 'tal'), ('R', 2, 'tal')]),
    '3.09a': T(5), '3.09b': M('L5, L6, L9', LB),
    '3.10a': T(6), '3.10c': T(3),
    '3.11a': F([('Värde', 5, 'tal'), ('Drag', 'B', 'ord')], 'Svara med rotens värde och namnet på noden den väljer.'),
    '3.11c': T(7),
    '3.12a': F([('A', 4, 'tal'), ('B', 5, 'tal')]),
    '3.12b': O('R, B, E, L6|R, B, E, 5', SV),
    '3.13a': T(5), '3.13b': M('L4, L5', LB), '3.13c': T(5),
    '3.14a': T(3),
    '3.15a': T(3), '3.15b': M('L4', LB), '3.15c': O('A', NN),
    '3.16a': T(7), '3.16b': M('L6', LB), '3.16c': T(5),
    '3.17a': T(6), '3.17b': M('L4, L5', LB), '3.17c': T(6),
    '3.18a': T(4), '3.18b': M('L7', LB), '3.18c': T(4),
    '3.19a': T(6), '3.19b': M('L5, L6, L9', LB), '3.19c': O('B', NN),
    '3.20a': T(5), '3.20b': M('L5, L6, L8, L9', LB), '3.20c': T(4),
    '3.21a': T(7), '3.21b': M('L4, L7, L8', LB),
    '3.22a': T(-1), '3.22b': M('L4, L7, L8', LB), '3.22c': F([('α', -1, 'tal'), ('β', -2, 'tal')]),
    '3.23a': T(6), '3.23b': M('L4, L7, L8, L12', LB),
    '3.23c': F([('Exakt värde', 'A, C', 'mangd'), ('Bara en gräns', 'B', 'mangd')], 'Skriv nodernas namn.'),
    '3.24a': T(10), '3.24b': M('L4, L9, L10, L11, L12', LB),
    '3.24c': F([('Nod 1', 'D', 'ord'), ('α 1', 10, 'tal'), ('β 1', 5, 'tal'),
                ('Nod 2', 'B', 'ord'), ('α 2', 11, 'tal'), ('β 2', 10, 'tal')],
               'Ta beskärningarna i den ordning de sker: nod, α och β för var och en.'),
    '3.25a': T(4), '3.25b': M('L8, L9, L10, L13, L14', LB), '3.25c': T(4),
    '3.26a': T(3), '3.26b': M('L4, L7, L8, L9', LB), '3.26c': T(3),
    '3.27a': F([('A', 9, 'tal'), ('B', 6, 'tal'), ('C', 8, 'tal')]),
    '3.27b': F([('Värde', 6, 'tal'), ('Drag', 'B', 'ord')], 'Svara med rotens värde och namnet på noden den väljer.'),
    '3.28a': F([('C', 3, 'tal'), ('D', 5, 'tal'), ('E', 6, 'tal'), ('F', 2, 'tal')]),
    '3.28b': F([('A', 3, 'tal'), ('B', 2, 'tal')]),
    '3.28c': O('R, A, C, L1|R, A, C, 3', SV),
    '3.29a': F([('D', 2, 'tal'), ('E', 3, 'tal'), ('F', 1, 'tal'), ('G', 4, 'tal'), ('H', 3, 'tal'), ('I', 5, 'tal')]),
    '3.29b': F([('A', 3, 'tal'), ('B', 4, 'tal'), ('C', 5, 'tal')]),
    '3.29c': F([('Värde', 3, 'tal'), ('Drag', 'A', 'ord')], 'Svara med rotens värde och namnet på noden den väljer.'),
    '3.30a': F([('C', 7, 'tal'), ('D', 5, 'tal'), ('E', 8, 'tal')]),
    '3.30b': F([('A', 4, 'tal'), ('B', 5, 'tal')]),
    '3.30c': O('R, B, D, L5|R, B, D, 5', SV),
}

# De 95 uppgifter som var manuella före 2026-11-11.
GAMLA = re.compile(r'^(1\.(0\d|1\d|2\d|3[01])|2\.(0\d|1\d|2\d|3[0-4])|3\.(0\d|1\d|2\d|30))$')

FORMAT = {'tal': 'numeriskt', 'ord': 'namnordning', 'mangd': 'namnmangd'}


def lagg_till_instruktion(fraga, suf):
    """Svarsinstruktionen i parentes efter frågan (efter första stycket)."""
    if not suf:
        return fraga
    tillagg = f' ({suf})'
    if tillagg in fraga:
        return fraga
    i = fraga.index('</p>')
    return fraga[:i] + tillagg + fraga[i:]


def falt_varde(kind, v):
    return v if kind == 'tal' else str(v)


def konvertera(d, spec):
    """Sätter delkortets rättningsfält. Returnerar (rättSvar, tolerans, svarFormat)."""
    d['självrättning'] = True
    d['spel'] = True
    kind = spec[0]
    if kind == 'tal':
        d.update(svarstyp='numeriskt', rättSvar=spec[1], tolerans=0, svarFormat='numeriskt', svarEnhet=None)
    elif kind in ('ord', 'mangd'):
        d['fraga'] = lagg_till_instruktion(d['fraga'], spec[2])
        d.update(svarstyp='kort_text', rättSvar=spec[1], tolerans=None, svarFormat=FORMAT[kind], svarEnhet=None)
    elif kind == 'falt':
        fields = spec[1]
        d['fraga'] = lagg_till_instruktion(d['fraga'], spec[2])
        d.update(svarstyp='flera_delar',
                 rättSvar=[falt_varde(k, v) for _, v, k in fields],
                 tolerans=[0 if k == 'tal' else None for _, _, k in fields],
                 svarFormat=[FORMAT[k] for _, _, k in fields],
                 svarEnhet=[None] * len(fields),
                 svarEtiketter=[e for e, _, _ in fields],
                 svarsstruktur='ordnad')
    elif kind in ('alt', 'nyalt'):
        if kind == 'nyalt':
            d['alternativ'] = spec[1]
            d['visaAlternativ'] = True
            if 'Välj ett alternativ.' not in d['fraga']:
                i = d['fraga'].index('</p>')
                d['fraga'] = d['fraga'][:i] + ' Välj ett alternativ.' + d['fraga'][i:]
        ratt = [x['txt'] for x in d['alternativ'] if x['ratt']]
        assert ratt, d['fraga']
        d.update(svarstyp='alternativ', rättSvar=ratt[0] if len(ratt) == 1 else ratt,
                 tolerans=None, svarFormat=None, svarEnhet=None)
    else:
        raise ValueError(kind)
    return d['rättSvar'], d['tolerans'], d['svarFormat']


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    used, n = set(), 0
    for u in bank:
        delar = u['spelDelar']
        keys = [u['id'] + d['etikett'] for d in delar]
        if not GAMLA.match(u['id']):
            continue
        n += 1
        fore = (u['t'], u['s'], u['spelIntro'])
        svar, tol, fmt = [], [], []
        for d, k in zip(delar, keys):
            spec = SPEC.get(k)
            if spec is None:
                assert d.get('alternativ'), k + ': saknar specifikation'
                spec = ('alt',)
            else:
                used.add(k)
            r, t_, f_ = konvertera(d, spec)
            svar.append(r)
            tol.append(t_)
            fmt.append(f_)
        u.update(spel=True, självrättning=True, svarstyp='flera_delar', rättSvar=svar, tolerans=tol,
                 svarFormat=fmt, svarEnhet=[None] * len(delar), svarsstruktur='ordnad',
                 svarEtiketter=[d['etikett'] for d in delar])
        if len(delar) == 1:
            # Kunskapsgymmet visar annars hela uppgiften, med t och dess A/B-lista, i
            # stället för delkortet med knappar. Påverkar inte Uppgiftslabbet.
            u['visaSomDelkort'] = True
        assert (u['t'], u['s'], u['spelIntro']) == fore, u['id']
    assert used == set(SPEC), sorted(set(SPEC) - used)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    manuella = [u['id'] for u in bank if u.get('spel') is False]
    assert n == 95, n
    print(f'{n} uppgifter självrättande, {len(SPEC)} delkort med egen specifikation, kvar manuella: {manuella}')


if __name__ == '__main__':
    main()
