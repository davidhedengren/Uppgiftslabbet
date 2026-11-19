# Matte, 2026-11-19: figuren stod mitt i en mening ("Bestäm tangenten till grafen för [figur] f(x)=… i punkten där x=2.").
# Figuren flyttas till direkt efter den mening den bröt. Körs direkt: python tools/sprak/omskr/matte_figur_sist.py <bank> [--skriv]
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FIGRX = re.compile(r'<(div|span) class="fig[^"]*">.*?</\1>', re.S)
PRX = re.compile(r'<p>((?:(?!</?p>).)*)</p>', re.S)


def slut(txt):
    t = re.sub(r'<[^>]+>', '', txt)
    t = re.sub(r'\\[\])]', '', t).strip()
    return bool(re.search(r'[.?!:]$', t))


def flytta(html):
    """Returnerar ny html eller None om inget behöver flyttas."""
    for m in PRX.finditer(html):
        rest = html[m.end():]
        f = re.match(r'\s*', rest)
        fm = FIGRX.match(rest, f.end())
        if not fm or slut(m.group(1)):
            continue
        fig = fm.group(0)
        efter = re.match(r'\s*<p>\s*(?:\\\[.*?\\\]\s*</p>\s*<p>\s*)?[a-zåäö](?!\))', rest[fm.end():], re.S)
        if not efter:  # bara när texten efter figuren fortsätter meningen (liten bokstav)
            continue
        utan = html[:m.end()] + rest[:f.end()] + rest[fm.end():]
        # första stycke efter brottet som avslutar meningen
        for p in PRX.finditer(utan, m.end()):
            if slut(p.group(1)):
                return utan[:p.end()] + fig + utan[p.end():]
        return None
    return None


def main():
    kod, skriv = sys.argv[1], '--skriv' in sys.argv
    b = Bank(kod)
    n = 0
    for u in b.arr:
        par = []
        for t in [u.get('t')] + [d.get('t') for d in u.get('spelDelar') or []]:
            if not t:
                continue
            ny = flytta(t)
            if ny and (t, ny) not in par:
                par.append((t, ny))
        if par:
            b.ersatt(u['id'], par)
            n += 1
            vis = FIGRX.sub('[F]', par[0][1])
            print(u['id'], re.sub(r'\s+', ' ', vis)[:220])
    print(n, 'uppgifter')
    if skriv:
        print(b.spara(), 'objekt skrivna')


main()
