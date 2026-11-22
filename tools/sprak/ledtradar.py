"""Byt ledtrådar för hand (2026-11-22).

Användning: python tools/sprak/ledtradar.py <bank> <skript.py> [--skriv]
Skriptet definierar L = {id: ledtråd} för huvuduppgiften, eller L = {id: {'': huvudledtråd, 'a': delkortets ledtråd, …}}.
Text utan <p> slås in i <p>…</p>. Delkortens ledtrådar byts bara inne i det delkortets objekt, så att samma
gamla text i huvuduppgiften eller ett annat delkort inte påverkas. Formatet i bankfilen bevaras.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprakverktyg import Bank, lit


def html(t):
    return t if t.lstrip().startswith('<') else f'<p>{t}</p>'


def delkort_spann(txt):
    """Spann (start, slut) för varje delkort i spelDelar, i ordning."""
    m = re.search(r'"spelDelar"\s*:\s*\[', txt)
    if not m:
        return []
    dec, i, ut = json.JSONDecoder(), m.end(), []
    while True:
        while txt[i] in ' \t\r\n,':
            i += 1
        if txt[i] == ']':
            return ut
        _, slut = dec.raw_decode(txt, i)
        ut.append((i, slut))
        i = slut


def byt_i(txt, start, slut, gammal, ny, id_, var):
    rx = re.compile(r'("ledtrad"\s*:\s*)' + re.escape(lit(gammal)))
    del_ = txt[start:slut]
    hits = list(rx.finditer(del_))
    if not hits:
        raise ValueError(f'{id_} {var}: ledtråden hittades inte')
    m = hits[0]
    del_ = del_[:m.start()] + m.group(1) + lit(ny) + del_[m.end():]
    return txt[:start] + del_ + txt[slut:]


def main():
    kod, skript = sys.argv[1], sys.argv[2]
    ns = {}
    exec(open(skript, encoding='utf-8').read(), ns)
    L = ns['L']
    b = Bank(kod)
    n = 0
    for id_, v in L.items():
        if isinstance(v, str):
            v = {'': v}
        u = b.obj(id_)
        txt = b.byte.get(id_, b.text(id_))
        for et, ny in v.items():
            ny = html(ny)
            spann = delkort_spann(txt)
            if et == '':
                gammal = u.get('ledtrad')
                if gammal is None:
                    raise ValueError(f'{id_}: saknar ledtråd')
                # huvudledtråden ligger utanför spelDelar
                if spann:
                    s0, s1 = spann[0][0], spann[-1][1]
                    fore = txt[:s0]
                    if re.search(r'"ledtrad"\s*:\s*' + re.escape(lit(gammal)), fore):
                        txt = byt_i(txt, 0, s0, gammal, ny, id_, 'huvud')
                    else:
                        txt = byt_i(txt, s1, len(txt), gammal, ny, id_, 'huvud')
                else:
                    txt = byt_i(txt, 0, len(txt), gammal, ny, id_, 'huvud')
            else:
                delar = u.get('spelDelar') or []
                idx = next((i for i, d in enumerate(delar) if d.get('etikett') == et), None)
                if idx is None:
                    raise ValueError(f'{id_}: delkort {et} finns inte')
                gammal = delar[idx].get('ledtrad')
                s, e = spann[idx]
                txt = byt_i(txt, s, e, gammal, ny, id_, et)
            n += 1
        json.loads(txt)
        b.byte[id_] = txt
    print(n, 'ledtrådar i', len(L), 'uppgifter')
    if '--skriv' in sys.argv:
        print(b.spara(), 'objekt skrivna')


main()
