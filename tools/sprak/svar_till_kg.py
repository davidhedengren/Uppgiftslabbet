"""Meningar om hur svaret ska skrivas flyttas från uppgiftstexten till `kgInstruktion` (användarbeslut 2026-11-23).

Användaren: ”Sådana kommentarer om hur svaret ska vara behövs inte i uppgiftslabbet, det är bara i kunskapsgymmet
det behövs ibland.” Uppgiftslabbet visar `t` på papper. Kunskapsgymmet lägger `kgInstruktion` sist i texten
(`kgInstruktionerIn`) innan uppgiften visas och rättas, så rättningen ser samma ord som förut (till exempel
”exakt”, ”avrunda”, ”decimal” i `fysikVardesiffror` och `friAvrundningRatt`).

Flyttas: ”Avrunda till …”, ”Avrunda vid behov till …”, ”Svara exakt.”, ”Svara med två decimaler.”, ”Svara i
bråkform.”, ”Svara med olikhetstecken.”, ”Svara på formen …”, ”Ange svaret i enklaste form.”, ”Skriv svaret …” och
liknande, när de står som egna meningar.

Undantag:
- Områden där avrundning eller skrivsätt är själva uppgiften (`UNDANTAG_OMR`).
- Om texten efter flytten saknar fråga eller uppmaning lämnas fältet orört.

Var meningen hamnar:
- Huvudtexten → uppgiftens `kgInstruktion`. Står meningen i en deluppgift i en lista (<li>) får den deluppgiftens
  bokstav: ”b) Avrunda till en decimal.”
- Ett delkorts `t`/`fraga` → delkortets `kgInstruktion`.
- `spelIntro` → varje delkorts `kgInstruktion` (och uppgiftens).

Bara strängliteralerna byts och `kgInstruktion` läggs till eller förlängs, så filernas format behålls.

  python tools/sprak/svar_till_kg.py <bank> [--visa N] [--skriv]
"""
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FIL = {'fy1': 'uppgifter.js', 'fy2': 'uppgifter2.js', 'ma1': 'uppgifterma1.js', 'ma2': 'uppgifterma2.js',
       'mato1': 'uppgiftermato1.js', 'mato2': 'uppgiftermato2.js', 'matf1': 'uppgiftermatf1.js'}
UNDANTAG_OMR = {'avrundning', 'overslag_grunder', 'decimaltal_positionssystem', 'tiopotenser_prefix', 'prefix',
                'enhetsbyten', 'matnogg', 'enheter', 'brakform', 'matning_enheter'}
MENING = (r'(?:Avrunda (?:svaret |svaren |vid behov |sedan )?(?:till|med|på)\b[^.<?]{0,90}'
          r'|Svara (?:exakt|med (?:en|ett|två|tre|fyra|\d+) (?:decimal|decimaler|värdesiffr|exakt|heltal|ord|bråk)'
          r'|med olikhetstecken|i (?:enklaste form|bråkform|decimalform|grundpotensform|procent|exakt form|hela)'
          r'|på formen)[^.<?]{0,110}'
          r'|Ange (?:svaret(?! både| också)|ett exakt värde)[^.<?]{0,90}|Skriv svaret[^.<?]{0,90})\.')
# (?<=<p>) tillagt 2026-11-23: en instruktion i ett eget stycke efter en figur (”…</span><p>Avrunda till en
# decimal.</p>”) missades, eftersom den varken stod först i texten eller efter en annan mening.
SV = re.compile(r'(?:(?<=^)|(?<=[.?!] )|(?<=[.?!])|(?<=<p>))\s?(' + MENING + r')')
UPPMANING = re.compile(r'\?|\b(?:Bestäm|Beräkna|Lös|Ange|Skriv|Förenkla|Visa|Rita|Faktorisera|Utveckla|Derivera|'
                       r'Undersök|Hur|Vilk|Vad|Teckna|Ställ|Räkna|Bryt|Kontrollera|Jämför|Förklara|Motivera|Skissa|'
                       r'Uppskatta|Avgör|Tolka|Pröva|Konstruera|Markera|Gör|Använd|Välj|Omvandla|Multiplicera|'
                       r'Dividera|Sätt|Integrera|Ta fram|Beskriv|Ge|Är|Finns|Kan|Stämmer|Ordna|Para|Sortera|'
                       r'Formulera|Lista|Läs|Uttryck|Fyll|Uppskatta|Bevisa|Härled)\b')
BOK = 'abcdefghij'


def plain(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg[\s\S]*?</svg>', ' ', h or ''))).strip()


def flytta(t, med_bokstav=True):
    """Returnerar (ny text, [meningar för kgInstruktion]) eller (None, []) om inget ska ändras."""
    if not isinstance(t, str) or not t:
        return None, []
    delar = re.split(r'(<svg[\s\S]*?</svg>)', t)
    ut = []
    funna = []
    li_index = 0
    for i, d in enumerate(delar):
        if i % 2:
            ut.append(d)
            continue
        # Dela upp i listpunkter så att bokstaven kan anges
        bitar = re.split(r'(<li\b[^>]*>|</li>)', d)
        inne = False
        for j, b in enumerate(bitar):
            if re.match(r'<li\b', b):
                inne = True
                ut.append(b)
                continue
            if b == '</li>':
                inne = False
                li_index += 1
                ut.append(b)
                continue
            def ers(m):
                s = m.group(1)
                funna.append((BOK[li_index] + ') ' if inne and med_bokstav and li_index < len(BOK) else '') + s)
                return ''
            ny = SV.sub(ers, b)
            ut.append(ny)
    if not funna:
        return None, []
    ny = ''.join(ut)
    ny = re.sub(r'<p>\s*</p>', '', ny)
    ny = re.sub(r'<li>\s*</li>', '<li></li>', ny)
    ny = ny.replace(' </p>', '</p>').replace(' </li>', '</li>').replace('<p> ', '<p>')
    if not UPPMANING.search(plain(ny)) or '<li></li>' in ny:
        return None, []
    return ny, funna


def ny_kg(gammal, tillagg):
    delar = [gammal.strip()] if gammal and gammal.strip() else []
    for s in tillagg:
        if s not in ' '.join(delar):
            delar.append(s)
    return ' '.join(delar)


def main():
    namn = sys.argv[1]
    fil = os.path.join(ROOT, FIL[namn])
    src = open(fil, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    nya = {}
    for q in bank:
        if q.get('omr') in UNDANTAG_OMR:
            continue
        k = json.loads(json.dumps(q))
        kg_main = []
        nt, f = flytta(k.get('t'))
        if nt is not None:
            k['t'] = nt
            kg_main += f
        delkort_extra = []
        if isinstance(k.get('spelIntro'), str):
            ni, fi = flytta(k['spelIntro'], med_bokstav=False)
            if ni is not None:
                k['spelIntro'] = ni
                delkort_extra = fi
                kg_main = [s for s in fi if s not in kg_main] + kg_main
        for d in k.get('spelDelar') or []:
            tillagg = list(delkort_extra)
            for falt in ('t', 'fraga'):
                nd, fd = flytta(d.get(falt), med_bokstav=False)
                if nd is not None:
                    d[falt] = nd
                    tillagg += [s for s in fd if s not in tillagg]
            if tillagg:
                d['kgInstruktion'] = ny_kg(d.get('kgInstruktion'), tillagg)
        if kg_main:
            k['kgInstruktion'] = ny_kg(k.get('kgInstruktion'), kg_main)
        if k != q:
            nya[q['id']] = (q, k)
    print(namn, len(nya), 'uppgifter')
    if '--visa' in sys.argv:
        n = int(sys.argv[sys.argv.index('--visa') + 1])
        for uid, (q, k) in list(nya.items())[:n]:
            print(' ', uid, '|', plain(k['t'])[-120:], '|| KG:', k.get('kgInstruktion'))
    if '--skriv' in sys.argv and nya:
        skriv(fil, src, bank, nya)


def lit(v):
    return json.dumps(v, ensure_ascii=False)


def skriv(fil, src, bank, nya):
    delar, pos = [], 0
    for start, slut, obj in spann(src):
        uid = str(obj.get('id'))
        if uid not in nya:
            continue
        q, k = nya[uid]
        bit = src[start:slut]
        kompakt = '\n' not in bit
        # Dela objektet i: före spelDelar, varje delkort, efter spelDelar.
        m = re.search(r'"spelDelar":\s*\[', bit)
        if m:
            dec = json.JSONDecoder()
            j = m.end()
            kort = []
            while True:
                while bit[j] in ' \n\r\t,':
                    j += 1
                if bit[j] == ']':
                    break
                _, e = dec.raw_decode(bit, j)
                kort.append((j, e))
                j = e
            fore, efter = bit[:m.end()], bit[j:]
            mellan = [bit[kort[i][1]:kort[i + 1][0]] for i in range(len(kort) - 1)]
            dbits = [bit[x:y] for x, y in kort]
        else:
            fore, efter, mellan, dbits = bit, '', [], []
        for idx, (dg, dn) in enumerate(zip(q.get('spelDelar') or [], k.get('spelDelar') or [])):
            if dg == dn:
                continue
            db = dbits[idx]
            for falt in ('t', 'fraga'):
                if dg.get(falt) != dn.get(falt):
                    a2, b2 = lit(dg[falt]), lit(dn[falt])
                    assert db.count(a2) == 1, (uid, idx, falt)
                    db = db.replace(a2, b2)
            if dg.get('kgInstruktion') != dn.get('kgInstruktion'):
                if 'kgInstruktion' in dg:
                    mm = re.search(r'"kgInstruktion": ?' + re.escape(lit(dg['kgInstruktion'])), db)
                    assert mm, (uid, idx, 'dkg')
                    db = db[:mm.start()] + db[mm.start():mm.end()].replace(lit(dg['kgInstruktion']), lit(dn['kgInstruktion'])) + db[mm.end():]
                else:
                    ankare = lit(dn['t']) if isinstance(dn.get('t'), str) else lit(dn['fraga'])
                    db = _lagg_till(db, ankare, dn['kgInstruktion'], kompakt)
            dbits[idx] = db
        huvud = [fore, efter]
        for falt in ('t', 'spelIntro'):
            if q.get(falt) != k.get(falt):
                a2, b2 = lit(q[falt]), lit(k[falt])
                hit = [i for i, h in enumerate(huvud) if a2 in h]
                assert hit, (uid, falt)
                huvud[hit[0]] = huvud[hit[0]].replace(a2, b2, 1)
        if q.get('kgInstruktion') != k.get('kgInstruktion'):
            if 'kgInstruktion' in q:
                a2 = lit(q['kgInstruktion'])
                for i, h in enumerate(huvud):
                    mm = re.search(r'"kgInstruktion": ?' + re.escape(a2), h)
                    if mm:
                        huvud[i] = h[:mm.start()] + h[mm.start():mm.end()].replace(a2, lit(k['kgInstruktion'])) + h[mm.end():]
                        break
                else:
                    raise AssertionError((uid, 'kg'))
            else:
                i = 0 if lit(k['t']) in huvud[0] else 1
                huvud[i] = _lagg_till(huvud[i], lit(k['t']), k['kgInstruktion'], kompakt)
        mitt = ''
        for i, db in enumerate(dbits):
            mitt += db + (mellan[i] if i < len(mellan) else '')
        bit = huvud[0] + mitt + huvud[1]
        delar += [src[pos:start], bit]
        pos = slut
    delar.append(src[pos:])
    ny_src = ''.join(delar)
    nb = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    for q, r in zip(nb, bank):
        uid = q['id']
        if uid in nya:
            assert q == nya[uid][1], uid
        else:
            assert q == r, uid
    with open(fil, 'w', encoding='utf-8', newline='') as fh:
        fh.write(ny_src)


def spann(src):
    """(start, slut, objekt) för varje uppgift, där start är objektets egen '{' (även när flera står på en rad)."""
    dec = json.JSONDecoder()
    i = src.index('[') + 1
    while True:
        while src[i] in ' \n\r\t,':
            i += 1
        if src[i] == ']':
            return
        obj, slut = dec.raw_decode(src, i)
        yield i, slut, obj
        i = slut


def _lagg_till(bit, ankare_lit, kg, kompakt):
    i = bit.index(ankare_lit) + len(ankare_lit)
    if kompakt:
        return bit[:i] + ',"kgInstruktion":' + lit(kg) + bit[i:]
    rad_start = bit.rfind('\n', 0, bit.index(ankare_lit)) + 1
    ind = re.match(r'\s*', bit[rad_start:]).group(0)
    sep = ': ' if '": "' in bit[rad_start:i] or '": ' in bit[rad_start:i] else ':'
    return bit[:i] + ',\n' + ind + '"kgInstruktion"' + sep + lit(kg) + bit[i:]


if __name__ == '__main__':
    main()
