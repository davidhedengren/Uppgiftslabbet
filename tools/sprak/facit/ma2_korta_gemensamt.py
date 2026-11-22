# Gemensamma rubriker och hjälpfunktioner för korta Ma2-facit (2026-11-22). Läses in av ma2_korta_*.py med exec.
KONJ = r"Konjugatregeln: \((a+b)(a-b)=a^2-b^2\)"
KV1 = r"Första kvadreringsregeln: \((a+b)^2=a^2+2ab+b^2\)"
KV2 = r"Andra kvadreringsregeln: \((a-b)^2=a^2-2ab+b^2\)"
MULT = 'Multiplicera varje term i den första parentesen med varje term i den andra'
BRYT = 'Bryt ut den största gemensamma faktorn'
KLUT = r"Riktningskoefficienten: \(k=\frac{y_2-y_1}{x_2-x_1}\)"
MSATT = r"Sätt in en punkt i \(y=kx+m\) och lös ut \(m\)"
RAT = r"Räta linjens ekvation: \(y=kx+m\)"
LG = r"Tiologaritmen: \(\lg a=b\) betyder \(10^b=a\)"
LGP = r"Produktlagen: \(\lg a+\lg b=\lg(ab)\)"
LGK = r"Kvotlagen: \(\lg a-\lg b=\lg\frac ab\)"
LGPOT = r"Potenslagen för logaritmer: \(n\lg a=\lg a^n\)"
LGINV = r"\(10^x\) och \(\lg x\) tar ut varandra: \(10^{\lg a}=a\) och \(\lg10^b=b\)"
POTM = r"Potenslagen: \(a^m\cdot a^n=a^{m+n}\)"
POTD = r"Potenslagen: \(\frac{a^m}{a^n}=a^{m-n}\)"
POTP = r"Potenslagen: \(\left(a^m\right)^n=a^{m\cdot n}\)"
POTPROD = r"Potenslagen: \((ab)^n=a^nb^n\)"
KVROT = r"Kvadratrotsmetoden: \(x^2=a\) ger \(x=\pm\sqrt a\)"
KUBROT = r"Ta kubikroten ur båda leden: \(x^3=a\) ger \(x=\sqrt[3]a\)"
PQ = r"pq-formeln: \(x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}\)"
KK = r"Kvadratkomplettering: \(x^2+bx+c=\left(x+\frac b2\right)^2-\left(\frac b2\right)^2+c\)"
NOLL = 'Nollproduktmetoden: en produkt är 0 när någon av faktorerna är 0'
SYM = 'Symmetrilinjen ligger mitt emellan nollställena'
SAMBAS = 'Skriv båda leden som potenser med samma bas och jämför exponenterna'
FUNK = 'Sätt in x-värdet i funktionsuttrycket'


def ett(rubrik, matte, svar, text=None):
    return ([(rubrik, matte, text)] if text else [(rubrik, matte)], svar)


def mc(rubrik, text, svar):
    return ([(rubrik, None, text)], svar)


def delar(*d):
    """d = (etikett, steg, svar). Huvudfacit: alla steg, rubriken på delens första steg får etiketten."""
    huvud, svar, ut = [], [], {}
    for et, steg, s in d:
        ut[et] = (steg, s)
        huvud.append((f'{et}) ' + steg[0][0],) + tuple(steg[0][1:]))
        huvud.extend(steg[1:])
        svar.append(f'{et}) {s}')
    ut[''] = (huvud, ' '.join(svar))
    return ut


def lika(a, b):
    """Svarsrad för två lösningar."""
    return rf"\(x={a}\) eller \(x={b}\)"


def kvrot(ekv, steg2, a, b, forsta=None):
    """Ekvation av typen (x+c)^2 = d: ev. dela först, sedan ± roten."""
    s = []
    if forsta:
        s.append(forsta)
    s.append((KVROT, ekv))
    s.append(('Lös de två ekvationerna', steg2))
    return (s, lika(a, b))
