"""Skriv facit enligt FACITMALL för hand (2026-11-22).

Användning: python tools/sprak/facitsteg.py <bank> <skript.py> [--skriv]
Skriptet definierar F = {id: FACIT} eller F = {id: {'': FACIT, 'a': FACIT, …}} där
FACIT = (steg, svar) och steg = [(rubrik, matte), …], [(rubrik, matte, text), …] eller [(rubrik, matte, text, html), …].
- rubrik: specifik rubrik för steget (facit-rubrik), gärna med formeln utskriven
- matte: LaTeX utan \\[ \\] (blir en facit-matte), eller None
- text: valfri förklarande mening (blir <p>) före matematiken; FIG(id, n) ger figur nr n ur uppgiftens nuvarande facit
- svar: svarsraden efter ”Svar:” (HTML/LaTeX med \\( \\))
Delkortens facit byts bara inne i det delkortets objekt. Formatet i bankfilen bevaras.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprakverktyg import Bank, lit


def html(facit):
    steg, svar = facit
    li = []
    for s in steg:
        rubrik, matte = s[0], s[1]
        text = s[2] if len(s) > 2 else None
        delar = [f'<p class="facit-rubrik">{rubrik}</p>']
        if text:
            delar.append(f'<p>{text}</p>')
        if matte:
            delar.append(f'<div class="facit-matte">\\[{matte}\\]</div>')
        if len(s) > 3 and s[3]:
            delar.append(s[3])  # färdig HTML, till exempel en figur från FIG()
        li.append('<li>' + ''.join(delar) + '</li>')
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(li) +
            f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def delkort_spann(txt):
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


def byt(txt, start, slut, gammal, ny, id_, var):
    rx = re.compile(r'("s"\s*:\s*)' + re.escape(lit(gammal)))
    del_ = txt[start:slut]
    m = rx.search(del_)
    if not m:
        raise ValueError(f'{id_} {var}: facit hittades inte')
    del_ = del_[:m.start()] + m.group(1) + lit(ny) + del_[m.end():]
    return txt[:start] + del_ + txt[slut:]


def main():
    kod, skript = sys.argv[1], sys.argv[2]
    b = Bank(kod)

    def FIG(id_, n=0):
        # Återanvänd figur nr n (span.fig eller div.fig med svg) ur uppgiftens nuvarande facit
        m = list(re.finditer(r'<(span|div) class="fig[^"]*">\s*<svg[\s\S]*?</svg>\s*</\1>', b.obj(id_)['s']))
        return m[n].group(0)
    ns = {'FIG': FIG}
    exec(open(skript, encoding='utf-8').read(), ns)
    F = ns['F']
    n = 0
    for id_, v in F.items():
        if isinstance(v, tuple):
            v = {'': v}
        u = b.obj(id_)
        txt = b.byte.get(id_, b.text(id_))
        for et, facit in v.items():
            ny = html(facit)
            spann = delkort_spann(txt)
            if et == '':
                gammal = u['s']
                if spann:
                    s0, s1 = spann[0][0], spann[-1][1]
                    if re.search(r'"s"\s*:\s*' + re.escape(lit(gammal)), txt[:s0]):
                        txt = byt(txt, 0, s0, gammal, ny, id_, 'huvud')
                    else:
                        txt = byt(txt, s1, len(txt), gammal, ny, id_, 'huvud')
                else:
                    txt = byt(txt, 0, len(txt), gammal, ny, id_, 'huvud')
            else:
                delar = u.get('spelDelar') or []
                idx = next((i for i, d in enumerate(delar) if d.get('etikett') == et), None)
                if idx is None:
                    raise ValueError(f'{id_}: delkort {et} finns inte')
                s, e = spann[idx]
                txt = byt(txt, s, e, delar[idx]['s'], ny, id_, et)
            n += 1
        json.loads(txt)
        b.byte[id_] = txt
    print(n, 'facit i', len(F), 'uppgifter')
    if '--skriv' in sys.argv:
        print(b.spara(), 'objekt skrivna')


main()
