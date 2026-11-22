"""Fy1/Fy2: förbehållet ”Bortse från …” sist, efter frågan (språkgranskning 2026-11-22).

Lärarens prov ställer frågan och lägger förbehållet sist: ”Hur lång tid tar fallet? Bortse från luftmotstånd.”
Gäller uppgifter med en enda fråga (inga delfrågor eller delkort), där förbehållet står före frågan. Meningen
flyttas oförändrad till slutet av frågans stycke. Ingen text tas bort eller skrivs om.

  python tools/sprak/omskr/fy1_bortse_sist.py <bank> [--visa] [--skriv]
"""
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import bankobjekt as B  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
FIL = {'fy1': 'uppgifter.js', 'fy2': 'uppgifter2.js'}
FORBEHALL = re.compile(r' ?(Bortse (?:även )?från [^.<]{1,120}\.)(?= |<|$)')


def flytta(t):
    if re.search(r'<ol|<li|\b[a-d]\)', t):
        return None
    fb = FORBEHALL.findall(t)
    if len(fb) != 1:
        return None
    mening = fb[0]
    # sista frågan i texten (utanför svg)
    utan_svg = re.sub(r'<svg[\s\S]*?</svg>', lambda m: '§' * len(m.group(0)), t)
    fragor = [m.end() for m in re.finditer(r'\?(?=\s*(?:</p>|$))', utan_svg)]
    if not fragor:
        return None
    slut = fragor[-1]
    pos = utan_svg.index(mening)
    if pos > slut:
        return None   # står redan efter frågan
    # Inga andra meningar efter frågan i samma stycke
    ny = t[:slut] + ' ' + mening + t[slut:]
    ny = ny[:pos] + ny[pos:].replace((' ' if t[pos - 1:pos] == ' ' else '') + mening, '', 1) if False else None
    tt = t.replace((' ' + mening) if (' ' + mening) in t else mening, '', 1)
    utan = re.sub(r'<svg[\s\S]*?</svg>', lambda m: '§' * len(m.group(0)), tt)
    fr = [m.end() for m in re.finditer(r'\?(?=\s*(?:</p>|$))', utan)]
    s = fr[-1]
    ny = tt[:s] + ' ' + mening + tt[s:]
    ny = re.sub(r'<p>\s*</p>', '', ny).replace('<p> ', '<p>')
    return ny


def main():
    bank_namn = sys.argv[1]
    fil = os.path.join(ROOT, FIL[bank_namn])
    src, bank = B.las(fil)
    nya = {}
    for q in bank:
        if q.get('spelDelar') or q.get('spelIntro'):
            continue
        ny = flytta(q['t'])
        if ny and ny != q['t']:
            k = json.loads(json.dumps(q))
            k['t'] = ny
            nya[q['id']] = k
            if '--visa' in sys.argv:
                txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg[\s\S]*?</svg>', ' [F] ', ny))).strip()
                print(q['id'], '|', txt[-230:])
    print(bank_namn, len(nya), 'uppgifter')
    if '--skriv' in sys.argv and nya:
        # Byt bara strängliteralen för t inom varje objekt, så att filens format i övrigt behålls.
        delar, pos = [], 0
        gamla = {q['id']: q for q in bank}
        for start, slut, obj in B.spann(src):
            uid = str(obj.get('id'))
            if uid not in nya:
                continue
            bit = src[start:slut]
            lit_g = json.dumps(gamla[uid]['t'], ensure_ascii=False)
            assert bit.count(lit_g) >= 1, uid
            bit = bit.replace(lit_g, json.dumps(nya[uid]['t'], ensure_ascii=False))
            delar += [src[pos:start], bit]
            pos = slut
        delar.append(src[pos:])
        ny_src = ''.join(delar)
        nb = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        for q, r in zip(nb, bank):
            if q != r:
                assert q['id'] in nya and {k for k in q if q[k] != r.get(k)} == {'t'}, q['id']
        B.skriv(fil, ny_src)


if __name__ == '__main__':
    main()
