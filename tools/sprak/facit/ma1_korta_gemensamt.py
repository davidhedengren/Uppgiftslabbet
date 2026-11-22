# Gemensamma rubriker och hjälpfunktioner för korta Ma1-facit (2026-11-22). Läses in av ma1_korta_*.py med exec.
GEMN = 'Skriv bråken med gemensam nämnare och räkna med täljarna'
BMULT = r"Multiplicera bråk: \(\frac ab\cdot\frac cd=\frac{a\cdot c}{b\cdot d}\)"
BDIV = r"Dividera med ett bråk: multiplicera med det inverterade bråket, \(\frac ab\div\frac cd=\frac ab\cdot\frac dc\)"
FORL = 'Förläng eller förkorta: multiplicera eller dividera täljare och nämnare med samma tal'
BRAKAV = r"Del av ett tal: \(\frac ab\) av \(x\) är \(\frac ab\cdot x\)"
DEC2BR = 'Skriv decimaltalet som tiondelar, hundradelar eller tusendelar och förkorta'
POS = 'Positionssystemet: ental, tiondelar (0,1), hundradelar (0,01), tusendelar (0,001)'
JMF = 'Jämför siffra för siffra från vänster; fyll på med nollor så att talen har lika många decimaler'
TIOP = 'Multiplikation med 10, 100, 1 000 flyttar kommat lika många steg åt höger'
GRUND = r"Grundpotensform: \(a\cdot10^n\) med \(1\le a<10\)"
TILLDEC = r"Från grundpotensform: \(10^n\) flyttar kommat \(n\) steg (åt höger om \(n>0\), åt vänster om \(n<0\))"
PREFIX = 'Prefix: kilo = 1 000, mega = 1 000 000, milli = 0,001'
AVR = 'Avrundning: titta på första siffran som tas bort; 5 eller mer avrundar uppåt, annars nedåt'
OVER = 'Överslag: avrunda talen så att räkningen går att göra i huvudet'
ANDEL = r"Andel: \(\frac{\text{delen}}{\text{det hela}}\)"
PROCAV = r"Procent av ett tal: \(\text{andel i decimalform}\cdot\text{det hela}\)"
FORH = 'Förenkla ett förhållande: dela båda talen med samma tal'
FORHDEL = r"Förhållandet \(a:b\): helheten består av \(a+b\) lika stora delar"
PROP = r"Proportionalitet: \(y=kx\), där \(k=\frac yx\) är samma för alla par"
PER1 = 'Räkna först ut värdet för en enhet'
SKALA = r"Skala \(1:n\): verkligheten är \(n\) gånger större än bilden"
ENHET = 'Enhetsbyte: 1 km = 1 000 m, 1 kg = 1 000 g, 1 h = 60 min, 1 l = 1 000 ml, 1 m³ = 1 000 l'


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


def enkla_delar(rubrik, *d):
    """Delkort med ett steg vardera och samma rubrik: d = (etikett, matte, text, svar)."""
    return delar(*[(et, [(rubrik, m, t)] if t else [(rubrik, m)], s) for et, m, t, s in d])
