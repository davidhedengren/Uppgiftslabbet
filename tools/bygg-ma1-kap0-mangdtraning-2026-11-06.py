"""Ma1 kapitel 0: mängdträning (2026-11-06).

Användaren (lärare): "Det är viktigt med mängdträning i kapitel 0. Inte konstigt formulerade, men vanliga
beräkningar som de kan träna på. Ibland bara en uppgift, ibland a) b) osv med varierande antal deluppgifter,
och gärna då a) enklast, b) lite svårare och c) svårast." (felrapport 0.02 samma dag.)

Talen är valda för hand per uppgift. Svaren räknas exakt (Fraction/Decimal) och facit byggs steg för steg ur
uttryckets struktur: varje rubrik namnger regeln och visar just den uppgiftens tal, t.ex.
"Multiplikation före subtraktion: 3·(−5) = −15". Varje del har en egen träningsnivå (stigande svårighet).
Logg: agent/MA1_KAP0_MANGDTRANING_2026-11-06.md

  python tools/bygg-ma1-kap0-mangdtraning-2026-11-06.py [--skriv]
"""
import ast
import json
import re
import sys
from decimal import Decimal
from fractions import Fraction
from math import gcd
from pathlib import Path

BANK = Path(__file__).resolve().parent.parent / 'uppgifterma1.js'
START_ID = 1302


# ------------------------------------------------------------------ tal och LaTeX
def sv_tal(x):
    """Tal i svensk form för text (decimalkomma, typografiskt minus)."""
    if isinstance(x, Fraction):
        if x.denominator == 1:
            x = x.numerator
        else:
            return ('−' if x < 0 else '') + f'{abs(x.numerator)}/{x.denominator}'
    if isinstance(x, Decimal):
        s = format(x.normalize(), 'f')
    else:
        s = str(x)
    if '.' in s:
        s = s.rstrip('0').rstrip('.') if 'e' not in s else s
    return grupp(s, ' ').replace('-', '−').replace('.', ',')


def grupp(s, mellan):
    """Mellanrum mellan tusentalen när heltalsdelen har minst fem siffror (som i banken: 15 501)."""
    hel, punkt, dec = s.partition('.')
    tecken = '-' if hel.startswith('-') else ''
    hel = hel.lstrip('-')
    if len(hel) > 4:
        g = []
        while hel:
            g.insert(0, hel[-3:]); hel = hel[:-3]
        hel = mellan.join(g)
    return tecken + hel + punkt + dec


def tex_tal(x, frac_ok=True):
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return tex_tal(x.numerator)
        tecken = '-' if x < 0 else ''
        return f'{tecken}\\frac{{{abs(x.numerator)}}}{{{x.denominator}}}'
    if isinstance(x, Decimal):
        s = format(x.normalize(), 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return grupp(s, '\\ ').replace('.', '{,}')
    return grupp(str(x), '\\ ')


def neg(x):
    return x < 0


def svar_rs(x):
    """rättSvar och svarFormat för ett exakt värde."""
    if isinstance(x, Fraction) and x.denominator != 1:
        return f'{x.numerator}/{x.denominator}', 'bråk'
    if isinstance(x, Fraction):
        x = x.numerator
    if isinstance(x, Decimal):
        if x == x.to_integral_value():
            return int(x), 'numeriskt'
        return float(x), 'numeriskt'
    return int(x), 'numeriskt'


# ------------------------------------------------------------------ uttrycksträd (ast) med steg
PREC = {ast.USub: 2.5, ast.Add: 1, ast.Sub: 1, ast.Mult: 2, ast.Div: 2, ast.Pow: 3}
OPTEX = {ast.Add: '+', ast.Sub: '-', ast.Mult: '\\cdot ', ast.Div: '\\div ', ast.Pow: '^'}
OPNAMN = {ast.Add: 'addition', ast.Sub: 'subtraktion', ast.Mult: 'multiplikation', ast.Div: 'division', ast.Pow: 'potens'}


class Tal:
    def __init__(self, v):
        self.v = v


def bygg(node, bratal):
    """ast → träd av Tal och ('op', vänster, höger). F(a,b) är ett bråk, D('1.5') ett decimaltal."""
    if isinstance(node, ast.Expression):
        return bygg(node.body, bratal)
    if isinstance(node, ast.Constant):
        return Tal(Fraction(node.value) if not bratal == 'dec' else Decimal(str(node.value)))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = bygg(node.operand, bratal)
        if isinstance(inner, Tal):
            return Tal(-inner.v)
        return (ast.USub, None, inner)   # t.ex. -6**2 = -(6**2)
    if isinstance(node, ast.Call) and node.func.id == 'F':
        return Tal(Fraction(node.args[0].value, node.args[1].value) * (-1 if False else 1))
    if isinstance(node, ast.Call) and node.func.id == 'D':
        return Tal(Decimal(node.args[0].value))
    if isinstance(node, ast.BinOp):
        return (type(node.op), bygg(node.left, bratal), bygg(node.right, bratal))
    raise ValueError(ast.dump(node))


def tex(tr, sida=None, foralder=None):
    """LaTeX med nödvändiga parenteser. sida: 'v'/'h' i förhållande till föräldern."""
    if isinstance(tr, Tal):
        t = tex_tal(tr.v)
        if neg(tr.v) and foralder is not None and not (foralder is not ast.Pow and FORSTA.get(id(tr))):
            return f'({t})'
        return t
    op, v, h = tr
    if op is ast.USub:
        return '-' + tex(h, 'h', ast.USub)
    if op is ast.Div and BRAKSTRECK[0]:
        s = f'\\dfrac{{{tex(v)}}}{{{tex(h)}}}'
    else:
        s = f'{tex(v, "v", op)}{OPTEX[op]}{tex(h, "h", op)}'
    if foralder is not None:
        pf, p = PREC[foralder], PREC[op]
        if p < pf or (p == pf and sida == 'h' and foralder in (ast.Sub, ast.Div)) or foralder is ast.Pow:
            s = f'({s})'
    return s


FORSTA = {}
BRAKSTRECK = [False]


def markera_forsta(tr):
    """Det tal som står först i hela uttrycket skrivs utan parentes även om det är negativt."""
    FORSTA.clear()
    x = tr
    while not isinstance(x, Tal):
        x = x[2] if x[0] is ast.USub else x[1]
    FORSTA[id(x)] = True


def varde(tr):
    if isinstance(tr, Tal):
        return tr.v
    op, v, h = tr
    if op is ast.USub: return -varde(h)
    a, b = varde(v), varde(h)
    if op is ast.Add: return a + b
    if op is ast.Sub: return a - b
    if op is ast.Mult: return a * b
    if op is ast.Div:
        if isinstance(a, Decimal): return a / b
        return Fraction(a) / Fraction(b)
    if op is ast.Pow: return a ** int(b)


def parentes(op, foralder, sida):
    """Skrivs deluttrycket med operationen op inom parentes under föräldern?"""
    if foralder is None or op is ast.USub:
        return False
    pf, p = PREC[foralder], PREC[op]
    return p < pf or (p == pf and sida == 'h' and foralder in (ast.Sub, ast.Div)) or (foralder is ast.Pow and sida == 'v')


def nasta(tr, foralder=None, sida=None, ip=False):
    """Hittar nästa nod att räkna: innersta parentes, potens, multiplikation/division från vänster, sedan +/- från vänster.
    Returnerar (nod, förälderns op, sida, ligger i en parentes)."""
    if isinstance(tr, Tal):
        return None
    op, v, h = tr
    # barn som inte är tal räknas först (parenteser och högre prioritet ligger djupare i trädet)
    for barn, s in ((v, 'v'), (h, 'h')):
        if barn is not None and not isinstance(barn, Tal):
            return nasta(barn, op, s, ip or parentes(barn[0], op, s))
    return (tr, foralder, sida, ip)


def ersatt(tr, mal, ny):
    if tr is mal:
        return ny
    if isinstance(tr, Tal) or tr is None:
        return tr
    op, v, h = tr
    v, h = ersatt(v, mal, ny), ersatt(h, mal, ny)
    if op is ast.USub and isinstance(h, Tal):
        return Tal(-h.v)
    return (op, v, h)


def stegtext(nod, foralder, sida, ip=False):
    """Rubrik för ett räknesteg: regeln i ord och just den här uppgiftens tal."""
    op, v, h = nod
    a, b = varde(v), varde(h)
    r = varde(nod)
    T = lambda x: tex_tal(x)
    P = lambda x: f'({T(x)})' if x < 0 else T(x)
    kalk = f'\\({T(a)}{OPTEX[op]}{P(b)}={T(r)}\\)'
    teckenregel = ''
    if op in (ast.Mult, ast.Div) and (a < 0 or b < 0):
        teckenregel = ' (samma tecken ger plus)' if (a < 0) == (b < 0) else ' (olika tecken ger minus)'
    hel_parentes = parentes(op, foralder, sida)
    if op is ast.Pow and foralder is ast.USub:
        return f'Potensen först, minustecknet står utanför: \\(-{T(a)}^{{{T(b)}}}=-({T(a)}^{{{T(b)}}})=-{T(r)}\\)', r
    if op is ast.Pow:
        upprepad = '\\cdot '.join([P(a)] * int(b))
        regel, kalk = 'potensen först', f'\\({P(a)}^{{{T(b)}}}={upprepad}={T(r)}\\)'
    elif hel_parentes:
        return f'Parentesen först: {kalk}{teckenregel}', r
    elif op in (ast.Mult, ast.Div) and foralder in (ast.Add, ast.Sub):
        regel = f'{"multiplikation" if op is ast.Mult else "division"} före {"addition" if foralder is ast.Add else "subtraktion"}'
    elif op in (ast.Mult, ast.Div) and foralder in (ast.Mult, ast.Div) and foralder is not op and sida == 'v':
        regel = 'division och multiplikation från vänster'
    elif op in (ast.Mult, ast.Div):
        regel = 'multiplicera' if op is ast.Mult else 'dividera'
    elif op is ast.Sub and b < 0:
        regel, kalk = 'minus ett negativt tal blir plus', f'\\({T(a)}-{P(b)}={T(a)}+{T(-b)}={T(r)}\\)'
    elif op is ast.Add and b < 0:
        regel, kalk = 'plus ett negativt tal blir minus', f'\\({T(a)}+{P(b)}={T(a)}-{T(-b)}={T(r)}\\)'
    elif foralder in (ast.Add, ast.Sub) and sida == 'v':
        regel = 'addition och subtraktion från vänster'
    else:
        regel = 'addera' if op is ast.Add else 'subtrahera'
    if ip:
        return f'I parentesen, {regel}: {kalk}{teckenregel}', r
    return f'{regel[0].upper()}{regel[1:]}: {kalk}{teckenregel}', r


def finns(tr, villkor):
    if tr is None or isinstance(tr, Tal):
        return False
    return villkor(tr) or finns(tr[1], villkor) or finns(tr[2], villkor)


def ledtrad_uttryck(tr):
    """Ledtråd som pekar på det första tankesteget i just detta uttryck, utan att avslöja svaret."""
    T = tex_tal
    nod, f, s, ip = nasta(tr)
    op = nod[0]
    if finns(tr, lambda n: n[0] is ast.USub):
        return 'Står minustecknet innanför eller utanför potensen? Potensen räknas före minustecknet.'
    if op is ast.Pow and varde(nod[1]) < 0 and not ip:
        bas = varde(nod[1])
        return f'Parentesen visar att hela \\({T(bas)}\\) ska upphöjas. Skriv potensen som en multiplikation och håll koll på tecknet.'
    if ip:
        if parentes(op, f, s):
            return 'Börja med det som står inom parentes.'
        return 'Börja inuti parentesen. Vilken räkneoperation ska göras först där?'
    if op is ast.Pow:
        bas, ex = T(varde(nod[1])), int(varde(nod[2]))
        return f'Räkna ut potensen först: \\({bas}^{{{ex}}}={"\\cdot ".join([bas] * ex)}\\).'
    rot = tr[0]
    if rot in (ast.Add, ast.Sub) and finns(tr, lambda n: n[0] in (ast.Mult, ast.Div)):
        forsta = op if op in (ast.Mult, ast.Div) else ast.Mult
        plus = f if f in (ast.Add, ast.Sub) else rot
        return f'Vilken räkneoperation ska göras först: {OPNAMN[forsta]} eller {OPNAMN[plus]}?'
    if not finns(tr, lambda n: n[0] in (ast.Add, ast.Sub)):
        neg = any(x.v < 0 for x in alla_tal(tr))
        n = len(alla_tal(tr))
        if neg and n > 2:
            return 'Räkna två tal i taget från vänster. Samma tecken ger plus och olika tecken ger minus.'
        if neg:
            return 'Räkna först utan tecken. Samma tecken ger plus och olika tecken ger minus.'
        if finns(tr, lambda n: n[0] is ast.Div) and finns(tr, lambda n: n[0] is ast.Mult):
            return 'Division och multiplikation har samma prioritet. Räkna från vänster till höger.'
        if finns(tr, lambda n: n[0] is ast.Div):
            return 'När det bara är divisioner räknar du från vänster till höger.'
        return 'Räkna från vänster till höger.'
    if finns(tr, lambda n: n[0] is ast.Sub and isinstance(n[2], Tal) and n[2].v < 0):
        return 'Att subtrahera ett negativt tal är samma sak som att addera motsvarande positiva tal.'
    if finns(tr, lambda n: n[0] is ast.Add and isinstance(n[2], Tal) and n[2].v < 0):
        return 'Att addera ett negativt tal är samma sak som att subtrahera motsvarande positiva tal.'
    if len(alla_tal(tr)) == 2:
        a, b = varde(tr[1]), varde(tr[2])
        hoger = (op is ast.Add) == (b > 0)
        return f'Börja på \\({T(a)}\\) på tallinjen och gå {T(abs(b))} steg åt {"höger" if hoger else "vänster"}.'
    return 'Räkna från vänster till höger, ett steg i taget.'


# ------------------------------------------------------------------ HTML
def li(rub, *h):
    return f'<li><p class="facit-rubrik">{rub}</p>{"".join(h)}</li>'


def mat(x):
    return f'<div class="facit-matte">\\[{x}\\]</div>'


def lista(steg, svar):
    return (f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{"".join(steg)}</ol>'
            f'<p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def svarstext(x, enhet=''):
    if isinstance(x, Fraction) and x.denominator != 1:
        return f'\\({tex_tal(x)}\\)' + (f' {enhet}' if enhet else '')
    return sv_tal(x) + (f' {enhet}' if enhet else '')


# ------------------------------------------------------------------ deltyper
def del_uttryck(uttr, bratal='frac', ledtrad=None):
    """Ett räkneuttryck: facit med ett steg per operation i rätt ordning."""
    BRAKSTRECK[0] = False
    tr = bygg(ast.parse(uttr, mode='eval'), bratal)
    markera_forsta(tr)
    fraga = tex(tr)
    steg, nu = [], tr
    while not isinstance(nu, Tal):
        nod, f, s, ip = nasta(nu)
        rub, r = stegtext(nod, f, s, ip)
        nu = ersatt(nu, nod, Tal(r))
        markera_forsta(nu)
        steg.append(li(rub, mat(tex(nu))) if not isinstance(nu, Tal) else li(rub))
    svar = varde(tr)
    if ledtrad is None:
        ledtrad = ledtrad_uttryck(tr)
    return dict(fraga=f'\\({fraga}\\)', steg=steg, svar=svar, ledtrad=f'<p>{ledtrad}</p>')


def alla_tal(tr):
    if isinstance(tr, Tal):
        return [tr]
    return alla_tal(tr[1]) + alla_tal(tr[2])


def del_brak(a, op, b):
    """Bråkräkning: a och b är Fraction (eller heltal). op i + - * /."""
    a, b = Fraction(a), Fraction(b)
    T = tex_tal
    P = lambda x: f'\\left({T(x)}\\right)' if x < 0 else T(x)
    fr = lambda t, n: ('-' if t < 0 else '') + f'\\frac{{{abs(t)}}}{{{n}}}'   # oförkortat bråk
    fraga = f'{T(a)}{ {"+": "+", "-": "-", "*": "\\cdot ", "/": "\\div "}[op]}{P(b)}'
    steg = []
    if op in '+-':
        n = a.denominator * b.denominator // gcd(a.denominator, b.denominator)
        ta, tb = a.numerator * (n // a.denominator), b.numerator * (n // b.denominator)
        if a.denominator != b.denominator:
            rader = []
            for x, tx in ((a, ta), (b, tb)):
                if x.denominator == n:
                    continue
                k = n // x.denominator
                if x.denominator == 1:
                    rader.append(f'{T(x)}={fr(tx, n)}')
                else:
                    rader.append(f'{T(x)}={"-" if x < 0 else ""}\\frac{{{abs(x.numerator)}\\cdot {k}}}{{{x.denominator}\\cdot {k}}}={fr(tx, n)}')
            heltal = [T(x) for x in (a, b) if x.denominator == 1]
            rub = (f'Skriv \\({heltal[0]}\\) som ett bråk med nämnaren {n}' if heltal
                   else f'Förläng till den gemensamma nämnaren {n}')
            steg.append(li(rub, *[mat(rad) for rad in rader]))   # en rad per bråk, annars för brett på mobil
        t = ta + tb if op == '+' else ta - tb
        tbt = f'({tb})' if tb < 0 else str(tb)
        steg.append(li(f'{"Addera" if op == "+" else "Subtrahera"} täljarna och behåll nämnaren {n}',
                       mat(f'\\frac{{{ta}{op}{tbt}}}{{{n}}}={fr(t, n)}')))
        r = a + b if op == '+' else a - b
        k = gcd(abs(t), n)
        if k > 1:
            steg.append(li(f'Förkorta med {k}', mat(f'{fr(t, n)}={T(r)}')))
        if a.denominator == b.denominator:
            led = 'Nämnarna är redan lika. Vad händer med täljarna?'
        elif 1 in (a.denominator, b.denominator):
            hel = a if a.denominator == 1 else b
            ovr = b if hel is a else a
            led = f'Skriv \\({T(hel)}\\) som ett bråk med nämnaren {ovr.denominator}.'
        else:
            led = f'Vilken är den minsta nämnare som både {a.denominator} och {b.denominator} går jämnt upp i?'
    elif op == '*':
        tn, nn = a.numerator * b.numerator, a.denominator * b.denominator
        bt = b.numerator if b.numerator >= 0 else f'({b.numerator})'
        if 1 in (a.denominator, b.denominator):
            hel = a if a.denominator == 1 else b
            rub = f'Heltalet {T(hel)} multipliceras bara med täljaren'
        else:
            rub = f'Multiplicera täljarna ({sv_tal(a.numerator)} och {sv_tal(b.numerator)}) och nämnarna ({a.denominator} och {b.denominator})'
        steg.append(li(rub, mat(f'\\frac{{{a.numerator}\\cdot {bt}}}{{{a.denominator}\\cdot {b.denominator}}}={fr(tn, nn)}'
                                if 1 not in (a.denominator, b.denominator)
                                else f'\\frac{{{a.numerator}\\cdot {bt}}}{{{max(a.denominator, b.denominator)}}}={fr(tn, nn)}')))
        r = a * b
        k = gcd(abs(tn), nn)
        if k > 1:
            steg.append(li(f'Förkorta med {k}', mat(f'{fr(tn, nn)}={T(r)}')))
        led = ('Multiplicera bara täljaren med heltalet. Förkorta sedan om det går.' if 1 in (a.denominator, b.denominator)
               else 'Multiplicera täljarna för sig och nämnarna för sig. Förkorta sedan om det går.')
    else:
        inv = 1 / b
        r = a / b
        steg.append(li(f'Att dela med \\({T(b)}\\) är samma sak som att multiplicera med \\({T(inv)}\\)',
                       mat(f'{T(a)}\\div {P(b)}={T(a)}\\cdot {P(inv)}')))
        tn, nn = a.numerator * inv.numerator, a.denominator * inv.denominator
        if a.denominator == 1 and inv.denominator == 1:
            steg.append(li(f'Multiplicera: \\({T(a)}\\cdot {T(inv)}={T(r)}\\)'))
        else:
            it = inv.numerator if inv.numerator >= 0 else f'({inv.numerator})'
            steg.append(li(f'Multiplicera täljarna ({sv_tal(a.numerator)} och {sv_tal(inv.numerator)}) och nämnarna ({a.denominator} och {inv.denominator})',
                           mat(f'\\frac{{{a.numerator}\\cdot {it}}}{{{a.denominator}\\cdot {inv.denominator}}}={fr(tn, nn)}')))
            k = gcd(abs(tn), nn)
            if k > 1:
                steg.append(li(f'Förkorta med {k}', mat(f'{fr(tn, nn)}={T(r)}')))
        led = f'Byt division med \\({T(b)}\\) mot multiplikation med det inverterade talet. Vad blir det inverterade talet?'
    return dict(fraga=f'\\({fraga}\\)', steg=steg, svar=r, ledtrad=f'<p>{led}</p>')


def del_decimal(a, op, b):
    """Decimaltal utan räknare. a, b som strängar."""
    A, Bv = Decimal(a), Decimal(b)
    T = tex_tal
    steg = []
    if op in '+-':
        r = A + Bv if op == '+' else A - Bv
        dec = max(-A.as_tuple().exponent, -Bv.as_tuple().exponent, 0)
        q = Decimal(1).scaleb(-dec)
        if max(-A.as_tuple().exponent, 0) != max(-Bv.as_tuple().exponent, 0):
            steg.append(li(f'Fyll på med nollor så att båda talen har {dec} {"decimal" if dec == 1 else "decimaler"}', mat(f'{format(A.quantize(q), "f").replace(".", "{,}")}{op}{format(Bv.quantize(q), "f").replace(".", "{,}")}')))
        steg.append(li(f'{"Addera" if op == "+" else "Subtrahera"} \\({T(A)}\\) och \\({T(Bv)}\\) med decimaltecknen under varandra', mat(f'{T(A)}{op}{T(Bv)}={T(r)}')))
        fraga = f'{T(A)}{op}{T(Bv)}'
        led = 'Ställ upp talen så att decimaltecknen hamnar under varandra.'
    elif op == '*':
        r = A * Bv
        da, db = max(0, -A.as_tuple().exponent), max(0, -Bv.as_tuple().exponent)
        ia, ib = int(A.scaleb(da)), int(Bv.scaleb(db))
        if Bv in (Decimal(10), Decimal(100), Decimal(1000)):
            n = len(str(int(Bv))) - 1
            steg.append(li(f'Gånger {int(Bv)}: flytta decimaltecknet {n} steg åt höger', mat(f'{T(A)}\\cdot {T(Bv)}={T(r)}')))
            led = f'Åt vilket håll flyttas decimaltecknet när du multiplicerar med {int(Bv)}?'
        else:
            steg.append(li(f'Räkna först utan decimaltecken: \\({ia}\\cdot {ib}\\)',mat(f'{ia}\\cdot {ib}={ia * ib}')))
            ord_ = 'decimal' if da + db == 1 else 'decimaler'
            full = format((A * Bv).quantize(Decimal(1).scaleb(-(da + db))), 'f').replace('.', '{,}')
            visning = f'{full}={T(r)}' if full != T(r) else T(r)
            steg.append(li(f'Faktorerna har tillsammans {da + db} {ord_}, så svaret får {da + db} {ord_}', mat(f'{T(A)}\\cdot {T(Bv)}={visning}')))
            led = 'Räkna som om det inte fanns några decimaltecken. Hur många decimaler har faktorerna tillsammans?'
        fraga = f'{T(A)}\\cdot {T(Bv)}'
    else:
        r = A / Bv
        if Bv in (Decimal(10), Decimal(100), Decimal(1000)):
            n = len(str(int(Bv))) - 1
            steg.append(li(f'Delat med {int(Bv)}: flytta decimaltecknet {n} steg åt vänster', mat(f'{T(A)}\\div {T(Bv)}={T(r)}')))
            led = f'Åt vilket håll flyttas decimaltecknet när du dividerar med {int(Bv)}?'
        elif Bv == Bv.to_integral_value():
            steg.append(li(f'Dela \\({T(A)}\\) med {T(Bv)} som vanligt och behåll decimaltecknet på samma plats', mat(f'{T(A)}\\div {T(Bv)}={T(r)}')))
            led = f'Dela som om det vore heltal. Var hamnar decimaltecknet?'
        else:
            k = max(0, -Bv.as_tuple().exponent)
            f = Decimal(10) ** k
            steg.append(li(f'Förläng med {int(f)} så att nämnaren blir ett heltal', mat(f'\\frac{{{T(A)}}}{{{T(Bv)}}}=\\frac{{{T(A * f)}}}{{{T(Bv * f)}}}')))
            steg.append(li(f'Nu delar vi med heltalet {T(Bv * f)}', mat(f'{T(A * f)}\\div {T(Bv * f)}={T(r)}')))
            led = f'Multiplicera båda talen med {int(f)}. Då ändras inte kvoten, men du delar med ett heltal.'
        fraga = f'{T(A)}\\div {T(Bv)}'
    return dict(fraga=f'\\({fraga}\\)', steg=steg, svar=r.normalize(), ledtrad=f'<p>{led}</p>')


ENH = {  # enhet -> (storhet, värde i basenhet)
    'm': ('l', '1'), 'dm': ('l', '0.1'), 'cm': ('l', '0.01'), 'mm': ('l', '0.001'), 'km': ('l', '1000'),
    'g': ('m', '1'), 'kg': ('m', '1000'), 'mg': ('m', '0.001'), 'ton': ('m', '1000000'), 'hg': ('m', '100'),
    'l': ('v', '1'), 'dl': ('v', '0.1'), 'cl': ('v', '0.01'), 'ml': ('v', '0.001'),
    'dm³': ('v', '1'), 'cm³': ('v', '0.001'), 'm³': ('v', '1000'),
    'm²': ('a', '1'), 'dm²': ('a', '0.01'), 'cm²': ('a', '0.0001'), 'km²': ('a', '1000000'), 'mm²': ('a', '0.000001'),
    'h': ('t', '3600'), 'min': ('t', '60'), 's': ('t', '1'),
}


def dec(x):
    """Fraction med nämnare 1, 2, 5, 10 … → Decimal exakt."""
    return (Decimal(x.numerator) / Decimal(x.denominator)).normalize()


def del_enhet(tal, fran, till):
    A = Decimal(tal)
    (sf, vf), (st, vt) = ENH[fran], ENH[till]
    assert sf == st
    faktor = Fraction(vf) / Fraction(vt)
    r = (A * dec(faktor)).normalize()
    T = tex_tal
    stor, liten, k = (fran, till, faktor) if faktor >= 1 else (till, fran, 1 / faktor)
    rel = f'1\\ \\text{{{stor}}}={T(dec(k))}\\ \\text{{{liten}}}'
    steg = []
    exp = stor[-1] if stor[-1] in '²³' and liten[-1] == stor[-1] else ''
    if exp:
        lin = Fraction(ENH[stor[:-1]][1]) / Fraction(ENH[liten[:-1]][1])
        ggr = '\\cdot '.join([T(dec(lin))] * (2 if exp == '²' else 3))
        steg.append(li(f'1 {stor[:-1]} = {sv_tal(dec(lin))} {liten[:-1]}, så 1 {stor} = {" · ".join([sv_tal(dec(lin))] * (2 if exp == "²" else 3))} {liten}',
                       mat(f'1\\ \\text{{{stor}}}={T(dec(k))}\\ \\text{{{liten}}}')))
    if faktor == 1:
        steg.append(li(f'1 {fran} = 1 {till}, så talet blir detsamma', mat(f'{T(A)}\\ \\text{{{fran}}}={T(r)}\\ \\text{{{till}}}')))
        led = f'Hur stor är 1 {fran} jämfört med 1 {till}?'
    elif faktor > 1:
        steg.append(li(f'1 {fran} = {sv_tal(dec(k))} {till}, så multiplicera med {sv_tal(dec(k))}',
                       *([] if exp else [mat(rel)]), mat(f'{T(A)}\\cdot {T(dec(k))}={T(r)}')))
        led = f'Hur många {till} går det på 1 {fran}? Ska talet bli större eller mindre?'
    else:
        steg.append(li(f'1 {till} = {sv_tal(dec(k))} {fran}, så dividera med {sv_tal(dec(k))}',
                       *([] if exp else [mat(rel)]), mat(f'{T(A)}\\div {T(dec(k))}={T(r)}')))
        led = f'Hur många {fran} går det på 1 {till}? Ska talet bli större eller mindre?'
    return dict(fraga=f'\\({T(A)}\\ \\text{{{fran}}}\\)', steg=steg, svar=r, ledtrad=f'<p>{led}</p>', enhet=till,
                fragetext=f'Skriv \\({T(A)}\\ \\text{{{fran}}}\\) i {till}.')


def del_procent(typ, a, b):
    T = tex_tal
    if typ == 'av':          # a % av b
        p, h = Decimal(a), Decimal(b)
        andel = (p / 100).normalize()
        r = (andel * h).normalize()
        steg = [li(f'{sv_tal(p)} % = {sv_tal(andel)} i decimalform', mat(f'{T(p)}\\,\\%=\\frac{{{T(p)}}}{{100}}={T(andel)}')),
                li(f'{sv_tal(p)} % av {sv_tal(h)} är {sv_tal(andel)} gånger {sv_tal(h)}', mat(f'{T(andel)}\\cdot {T(h)}={T(r)}'))]
        return dict(fraga=f'{sv_tal(p)} % av {sv_tal(h)}', steg=steg, svar=r, ledtrad=f'<p>Skriv {sv_tal(p)} % i decimalform och multiplicera.</p>',
                    fragetext=f'Beräkna \\({T(p)}\\,\\%\\) av \\({T(h)}\\).')
    if typ == 'andel':       # a av b i procent
        del_, h = Decimal(a), Decimal(b)
        q = (del_ / h)
        r = (q * 100).normalize()
        steg = [li(f'Dela delen {sv_tal(del_)} med det hela {sv_tal(h)}', mat(f'\\frac{{{T(del_)}}}{{{T(h)}}}={T(q.normalize())}')),
                li('Skriv andelen i procent: gånger 100', mat(f'{T(q.normalize())}=\\ {T(r)}\\,\\%'))]
        return dict(fraga=f'{sv_tal(del_)} av {sv_tal(h)}', steg=steg, svar=r, enhet='%',
                    ledtrad=f'<p>Dela delen med det hela och skriv svaret i procent.</p>',
                    fragetext=f'Hur många procent är \\({T(del_)}\\) av \\({T(h)}\\)?')
    if typ == 'tillprocent':  # decimalform -> procent
        d = Decimal(a); r = (d * 100).normalize()
        steg = [li('Procent betyder hundradelar: multiplicera med 100', mat(f'{T(d)}={T(r)}\\,\\%'))]
        return dict(fraga=f'{sv_tal(d)}', steg=steg, svar=r, enhet='%', ledtrad='<p>Hur många hundradelar är talet?</p>',
                    fragetext=f'Skriv \\({T(d)}\\) i procent.')
    if typ == 'tilldecimal':  # procent -> decimalform
        p = Decimal(a); r = (p / 100).normalize()
        steg = [li('Procent betyder hundradelar: dividera med 100', mat(f'{T(p)}\\,\\%=\\frac{{{T(p)}}}{{100}}={T(r)}'))]
        return dict(fraga=f'{sv_tal(p)} %', steg=steg, svar=r, ledtrad='<p>Procent betyder hundradelar.</p>',
                    fragetext=f'Skriv \\({T(p)}\\,\\%\\) i decimalform.')
    raise ValueError(typ)


from decimal import ROUND_HALF_UP

PLATS = {'heltal': 0, 'en decimal': 1, 'två decimaler': 2, 'tre decimaler': 3,
         'tiotal': -1, 'hundratal': -2, 'tusental': -3}
PLATSNAMN = {0: 'entalssiffran', 1: 'tiondelssiffran', 2: 'hundradelssiffran', 3: 'tusendelssiffran',
             -1: 'tiotalssiffran', -2: 'hundratalssiffran', -3: 'tusentalssiffran'}
NASTA_NAMN = {0: 'tiondelssiffran', 1: 'hundradelssiffran', 2: 'tusendelssiffran', 3: 'tiotusendelssiffran',
              -1: 'entalssiffran', -2: 'tiotalssiffran', -3: 'hundratalssiffran'}


def tusental(x):
    """tex_tal grupperar redan tusentalen (som i banken: 12 849)."""
    return tex_tal(x)


def del_avrunda(tal, till):
    A = Decimal(tal)
    k = PLATS[till]
    q = Decimal(1).scaleb(-k)
    r = A.quantize(q, rounding=ROUND_HALF_UP) if k >= 0 else (A / q).quantize(Decimal(1), rounding=ROUND_HALF_UP) * q
    r = Decimal(r).normalize() if k < 0 else r
    nasta = int(str(abs(A).scaleb(k + 1).to_integral_value(rounding='ROUND_DOWN'))[-1])
    upp = nasta >= 5
    T = tusental
    rt = format(r, 'f').replace('.', '{,}') if k > 0 else T(r)   # 4,00 och 10,0 behåller sina decimaler
    steg = [li(f'Siffran efter {PLATSNAMN[k]} är {nasta}. '
               + (f'Den är 5 eller större, så avrunda uppåt' if upp else f'Den är mindre än 5, så avrunda nedåt'),
               mat(f'{T(A)}\\approx {rt}'))]
    ord_ = {'heltal': 'till heltal', 'tiotal': 'till närmaste tiotal', 'hundratal': 'till närmaste hundratal',
            'tusental': 'till närmaste tusental'}.get(till, f'till {till}')
    led = f'Titta på {NASTA_NAMN[k]}. Är den 5 eller större?'
    svar = r if k >= 0 else Decimal(int(r))
    return dict(fraga=f'\\({T(A)}\\)', steg=steg, svar=svar, ledtrad=f'<p>{led}</p>',
                fragetext=f'Avrunda \\({T(A)}\\) {ord_}.', svartex=rt)


def del_forkorta(t, n):
    g = gcd(t, n)
    r = Fraction(t, n)
    steg = [li(f'Den största gemensamma faktorn till {t} och {n} är {g}',
               mat(f'{t}={g}\\cdot {t // g}\\qquad {n}={g}\\cdot {n // g}')),
            li(f'Dividera täljare och nämnare med {g}', mat(f'\\frac{{{t}}}{{{n}}}=\\frac{{{t}/{g}}}{{{n}/{g}}}={tex_tal(r)}'))]
    led = f'Vilket är det största tal som både {t} och {n} är delbara med?'
    return dict(fraga=f'\\(\\frac{{{t}}}{{{n}}}\\)', steg=steg, svar=r, ledtrad=f'<p>{led}</p>', svarform='forkortat_brak',
                fragetext=f'Förkorta \\(\\frac{{{t}}}{{{n}}}\\) så långt som möjligt.')


PREFIX = {'k': 3, 'h': 2, 'd': -1, 'c': -2, 'm': -3, 'µ': -6, 'M': 6, 'G': 9, 'n': -9}


def del_tiopotens(typ, a, b=None):
    T = tex_tal
    if typ == 'grundpotens':   # skriv a i grundpotensform
        A = Decimal(a)
        e = A.adjusted()
        m = (A.scaleb(-e)).normalize()
        steg = [li(f'Flytta decimaltecknet {abs(e)} steg så att det står en siffra före det', mat(f'{T(A)}={T(m)}\\cdot 10^{{{e}}}'))]
        return dict(fraga=f'\\({T(A)}\\)', steg=steg, svar=A.normalize(), svarform='grundpotensform', svartex=f'{T(m)}\\cdot 10^{{{e}}}',
                    ledtrad='<p>Talet framför tiopotensen ska vara minst 1 och mindre än 10.</p>',
                    fragetext=f'Skriv \\({T(A)}\\) i grundpotensform.')
    if typ == 'decimal':       # a·10^b i decimalform
        A = Decimal(a); e = int(b)
        r = A.scaleb(e).normalize()
        riktning = 'höger' if e > 0 else 'vänster'
        steg = [li(f'Gånger \\(10^{{{e}}}\\): flytta decimaltecknet {abs(e)} steg åt {riktning}', mat(f'{T(A)}\\cdot 10^{{{e}}}={T(r)}'))]
        return dict(fraga=f'\\({T(A)}\\cdot 10^{{{e}}}\\)', steg=steg, svar=r,
                    ledtrad=f'<p>Exponenten {sv_tal(e)} visar hur många steg och åt vilket håll decimaltecknet flyttas.</p>',
                    fragetext=f'Skriv \\({T(A)}\\cdot 10^{{{e}}}\\) i decimalform.')
    if typ == 'prefix':        # a med prefix -> basenhet b
        tal, pre, bas = a
        A = Decimal(tal); e = PREFIX[pre]
        r = A.scaleb(e).normalize()
        steg = [li(f'{pre} betyder \\(10^{{{e}}}\\)', mat(f'{T(A)}\\ \\text{{{pre}{bas}}}={T(A)}\\cdot 10^{{{e}}}\\ \\text{{{bas}}}')),
                li(f'Flytta decimaltecknet {abs(e)} steg åt {"höger" if e > 0 else "vänster"}', mat(f'{T(A)}\\cdot 10^{{{e}}}={T(r)}'))]
        return dict(fraga=f'\\({T(A)}\\ \\text{{{pre}{bas}}}\\)', steg=steg, svar=r, enhet=bas,
                    ledtrad=f'<p>Vilken tiopotens står prefixet {pre} för?</p>',
                    fragetext=f'Skriv \\({T(A)}\\ \\text{{{pre}{bas}}}\\) i {bas}.')
    raise ValueError(typ)


# ------------------------------------------------------------------ uppgifterna (talen valda för hand)
E = lambda u, L, br='frac': ('uttr', u, L, br)
U = []   # (omr, familj, instruktion, [del], ...)


def uppg(omr, familj, instr, delar):
    U.append((omr, familj, instr, delar))


# Negativa tal: addition och subtraktion (1–4 delar, stigande svårighet)
NA = 'Addition och subtraktion med negativa tal'
uppg('negativa_tal', NA, 'Beräkna.', [E('-6+4', 1), E('3-9', 1), E('-5-8+2', 2), E('-12-(-7)+4', 3)])
uppg('negativa_tal', NA, 'Beräkna.', [E('-7+10', 1), E('-4-6', 1)])
uppg('negativa_tal', NA, 'Beräkna.', [E('-15+(-6)', 2)])
uppg('negativa_tal', NA, 'Beräkna.', [E('8-13', 1), E('-9+(-4)', 2), E('6-(-11)', 2)])
uppg('negativa_tal', NA, 'Beräkna.', [E('-3-(-8)', 2)])
uppg('negativa_tal', NA, 'Beräkna.', [E('-20+35', 1), E('14-30', 1), E('-25-(-40)', 2), E('-18+(-7)-(-30)', 3)])
uppg('negativa_tal', NA, 'Beräkna.', [E('-11+4-9', 2), E('7-(-3)-15', 3)])
uppg('negativa_tal', NA, 'Beräkna.', [E('-100+45', 1), E('-60-(-25)', 2), E('-38+(-17)+50', 3)])
# Negativa tal: multiplikation och division
NM = 'Beräkna med negativa tal'
uppg('negativa_tal', NM, 'Beräkna.', [E('-4*6', 1), E('-7*(-3)', 2), E('-36/(-4)', 2), E('-2*(-5)*(-3)', 3)])
uppg('negativa_tal', NM, 'Beräkna.', [E('-48/6', 2)])
uppg('negativa_tal', NM, 'Beräkna.', [E('5*(-8)', 1), E('-63/(-9)', 2)])
uppg('negativa_tal', NM, 'Beräkna.', [E('-9*(-9)', 2), E('-72/8', 2), E('-4*(-2)*(-5)*(-1)', 3)])
uppg('negativa_tal', NM, 'Beräkna.', [E('(-6)**2', 2), E('-6**2', 3)])
uppg('negativa_tal', NM, 'Beräkna.', [E('-3*4+10', 2), E('-20/(-5)-7', 2), E('6-4*(-3)', 3), E('-2*(-3)**2+12/(-4)', 4)])
uppg('negativa_tal', NM, 'Beräkna.', [E('(-2)**3', 3)])
uppg('negativa_tal', NM, 'Beräkna.', [E('-5*(-4)-30', 2), E('(-8+2)*(-3)', 3), E('-24/(3-9)', 3)])
# Räkneordning
PR = 'Prioriteringsregler'
uppg('tal_rakneordning', PR, 'Beräkna.', [E('4+3*5', 1), E('20-12/4', 1), E('(4+3)*5', 2), E('18/(2+4)-1', 3)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('7+2*8-5', 2)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('30-4*6', 1), E('(30-4)*6', 2)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('2**3+4', 1), E('3*2**2', 2), E('(5-2)**2*4', 3)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('48/6*2', 2), E('48/(6*2)', 2), E('100-48/6*2', 3)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('9+16/4-3*2', 2)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('5*(12-7)+3', 2), E('(15+9)/(10-4)', 2), E('2*(3+4*5)', 3), E('(2+3)**2-4*(6-1)', 4)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('72/6/3', 2), E('72/(6/3)', 3)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('8+4*3-6/2', 2), E('(8+4)*(3-6/2)', 3)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('7*8-6*9', 2)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('4*10-3*2', 1), E('4*(10-3*2)', 2), E('(4*10-3)*2', 2)])
uppg('tal_rakneordning', PR, 'Beräkna.', [E('3+(12-2**3)*5', 3)])
# Bråk: addition och subtraktion
BR = 'Räkna med bråk'
F = Fraction
B = lambda a, op, b, L: ('brak', a, op, b, L)
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(1, 5), '+', F(2, 5), 1), B(F(1, 2), '+', F(1, 4), 2), B(F(2, 3), '+', F(3, 4), 2), B(F(5, 6), '-', F(3, 8), 3)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(7, 9), '-', F(4, 9), 1), B(F(3, 4), '-', F(1, 6), 2)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(2, 5), '+', F(1, 3), 2)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(3, 10), '+', F(1, 10), 1), B(F(5, 12), '+', F(1, 4), 2), B(F(1, 6), '-', F(3, 4), 3)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(7, 8), '-', F(1, 2), 2)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(1, 3), '+', F(1, 6), 2), B(F(4, 5), '-', F(3, 10), 2), B(F(-2, 3), '+', F(1, 4), 3), B(F(-5, 6), '-', F(1, 4), 3)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(2, '-', F(3, 4), 2), B(F(3, 2), '+', F(5, 6), 3)])
# Bråk: multiplikation och division
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(2, 3), '*', F(4, 5), 1), B(F(3, 4), '*', F(2, 9), 2), B(6, '*', F(5, 8), 2), B(F(-5, 6), '*', F(9, 10), 3)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(1, 2), '/', F(1, 4), 2), B(F(2, 3), '/', F(4, 9), 3)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(3, 5), '/', 3, 2)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(4, 7), '*', F(7, 8), 2), B(F(5, 6), '/', F(10, 9), 3), B(F(-3, 4), '/', F(9, 16), 4)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(3, 8), '*', 4, 1), B(5, '/', F(1, 3), 2)])
uppg('brakrakning', BR, 'Beräkna. Ange svaret i enklaste form.', [B(F(9, 10), '*', F(5, 6), 2)])
# Decimaltal
DE = 'Räkna med decimaltal'
Dd = lambda a, op, b, L: ('dec', a, op, b, L)
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('3.4', '+', '2.5', 1), Dd('7.2', '-', '4.8', 1), Dd('12.6', '+', '3.75', 2), Dd('10', '-', '3.46', 3)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('0.45', '*', '100', 1), Dd('62.5', '/', '1000', 2)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('2.4', '*', '3', 1), Dd('1.5', '*', '0.4', 2), Dd('0.3', '*', '0.07', 3)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('8.4', '/', '4', 1), Dd('4.8', '/', '0.6', 2), Dd('0.36', '/', '0.04', 3)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('5.06', '-', '2.8', 2)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('3.2', '*', '1.5', 2)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('0.7', '+', '0.65', 1), Dd('6', '-', '0.25', 2), Dd('2.5', '*', '2.5', 3), Dd('1.2', '/', '0.03', 4)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('0.08', '*', '1000', 1), Dd('4.5', '/', '100', 1), Dd('7', '/', '0.5', 2)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('9.6', '/', '0.8', 3)])
uppg('decimaltal_positionssystem', DE, 'Beräkna utan räknare.', [Dd('14.3', '-', '9.75', 2), Dd('0.6', '*', '0.6', 2)])
# Enhetsbyten
EN = 'Längd, massa och tid'
En = lambda t, f, ti, L: ('enh', t, f, ti, L)
uppg('enhetsbyten', EN, 'Gör om till den angivna enheten.', [En('3.5', 'km', 'm', 1), En('250', 'cm', 'm', 1), En('0.8', 'kg', 'g', 2), En('45', 'mm', 'dm', 3)])
uppg('enhetsbyten', EN, 'Gör om till den angivna enheten.', [En('1500', 'g', 'kg', 1), En('2.3', 'ton', 'kg', 2)])
uppg('enhetsbyten', EN, 'Gör om till den angivna enheten.', [En('3', 'h', 'min', 1), En('150', 'min', 'h', 2), En('0.75', 'h', 'min', 2)])
uppg('enhetsbyten', EN, 'Gör om till den angivna enheten.', [En('720', 'mg', 'g', 2)])
uppg('enhetsbyten', EN, 'Gör om till den angivna enheten.', [En('4.2', 'dl', 'l', 1), En('350', 'ml', 'dl', 2), En('0.6', 'l', 'cl', 2), En('2.5', 'dm³', 'l', 2)])
uppg('enhetsbyten', EN, 'Gör om till den angivna enheten.', [En('7', 'dm', 'cm', 1), En('0.04', 'km', 'm', 2)])
EA = 'Area- och volymenheter'
uppg('enhetsbyten', EA, 'Gör om till den angivna enheten.', [En('3', 'm²', 'dm²', 2), En('450', 'cm²', 'dm²', 3), En('2', 'm²', 'cm²', 3)])
uppg('enhetsbyten', EA, 'Gör om till den angivna enheten.', [En('5', 'dm³', 'cm³', 2), En('0.4', 'm³', 'l', 3)])
uppg('enhetsbyten', EA, 'Gör om till den angivna enheten.', [En('25000', 'cm²', 'm²', 3)])
uppg('enhetsbyten', EA, 'Gör om till den angivna enheten.', [En('1.2', 'l', 'cm³', 2), En('800', 'cm³', 'dm³', 2), En('3', 'm³', 'dm³', 3), En('0.05', 'km²', 'm²', 4)])
# Procent
PK = 'Beräkningar när procentsatsen är känd'
Pc = lambda typ, a, b, L: ('proc', typ, a, b, L)
uppg('andelar', PK, None, [Pc('av', '10', '80', 1), Pc('av', '25', '60', 1), Pc('av', '15', '120', 2), Pc('av', '4', '350', 3)])
uppg('andelar', PK, None, [Pc('av', '50', '46', 1), Pc('av', '75', '200', 2)])
uppg('andelar', PK, None, [Pc('av', '30', '250', 2)])
uppg('andelar', PK, None, [Pc('av', '1', '900', 2), Pc('av', '12.5', '80', 3), Pc('av', '120', '45', 3)])
uppg('andelar', PK, None, [Pc('av', '20', '35', 2)])
PO = 'Jämföra och omvandla andelar'
uppg('andelar', PO, None, [Pc('tillprocent', '0.35', None, 1), Pc('tilldecimal', '8', None, 2), Pc('tillprocent', '1.2', None, 3)])
uppg('andelar', PO, None, [Pc('tilldecimal', '42', None, 1), Pc('tillprocent', '0.075', None, 2)])
PA = 'Andel i procent'
uppg('andelar', PA, None, [Pc('andel', '6', '24', 1), Pc('andel', '18', '40', 2), Pc('andel', '7', '35', 2), Pc('andel', '45', '36', 3)])
uppg('andelar', PA, None, [Pc('andel', '9', '150', 2)])
uppg('andelar', PA, None, [Pc('andel', '4', '5', 1), Pc('andel', '13', '20', 2)])
# Förkorta bråk
FB = 'Bråkform, blandad form och decimalform'
Fk = lambda t, n, L: ('fkt', t, n, L)
uppg('brakform', FB, None, [Fk(6, 8, 1), Fk(12, 18, 2), Fk(40, 64, 2), Fk(84, 120, 3)])
uppg('brakform', FB, None, [Fk(30, 42, 2)])
uppg('brakform', FB, None, [Fk(9, 12, 1), Fk(35, 49, 2), Fk(72, 90, 3)])
uppg('brakform', FB, None, [Fk(15, 25, 1), Fk(56, 64, 2)])
# Avrundning
AV = 'Avrunda till angiven noggrannhet'
Av = lambda t, till, L: ('avr', t, till, L)
uppg('avrundning', AV, None, [Av('4.62', 'heltal', 1), Av('7.348', 'en decimal', 1), Av('0.0657', 'två decimaler', 2), Av('3.996', 'två decimaler', 3)])
uppg('avrundning', AV, None, [Av('2348', 'hundratal', 1), Av('15501', 'tusental', 2)])
uppg('avrundning', AV, None, [Av('9.95', 'en decimal', 2), Av('199.7', 'tiotal', 2), Av('0.12049', 'tre decimaler', 3)])
uppg('avrundning', AV, None, [Av('64.55', 'heltal', 1)])
# Prefix och tiopotenser
PF = 'Omvandla med prefix'
Tp = lambda typ, a, b, L: ('tio', typ, a, b, L)
uppg('prefix', PF, None, [Tp('prefix', ('4', 'k', 'm'), None, 1), Tp('prefix', ('350', 'm', 'g'), None, 2), Tp('prefix', ('2.5', 'M', 'W'), None, 2), Tp('prefix', ('80', 'µ', 's'), None, 3)])
uppg('prefix', PF, None, [Tp('prefix', ('12', 'c', 'm'), None, 1), Tp('prefix', ('0.6', 'k', 'g'), None, 2)])
uppg('prefix', PF, None, [Tp('prefix', ('1.5', 'G', 'W'), None, 3)])
GP = 'Grundpotensform och decimalform'
uppg('tiopotenser_prefix', GP, None, [Tp('decimal', '3', 4, 1), Tp('decimal', '5.2', 3, 2), Tp('decimal', '7', -2, 2), Tp('decimal', '4.05', -3, 3)])
uppg('tiopotenser_prefix', GP, None, [Tp('decimal', '6.1', 5, 2), Tp('decimal', '8', -4, 3)])
SG = 'Skriva tal i grundpotensform'
uppg('tiopotenser_prefix', SG, None, [Tp('grundpotens', '5000', None, 1), Tp('grundpotens', '340000', None, 2), Tp('grundpotens', '0.007', None, 2), Tp('grundpotens', '0.000062', None, 3)])
uppg('tiopotenser_prefix', SG, None, [Tp('grundpotens', '72000', None, 2)])


# ------------------------------------------------------------------ bygg JSON
def bygg_del(d):
    typ = d[0]
    if typ == 'uttr':
        _, u, L, br = d
        x = del_uttryck(u, br)
    elif typ == 'brak':
        _, a, op, b, L = d
        x = del_brak(a, op, b)
    elif typ == 'dec':
        _, a, op, b, L = d
        x = del_decimal(a, op, b)
    elif typ == 'enh':
        _, t, f, ti, L = d
        x = del_enhet(t, f, ti)
    elif typ == 'proc':
        _, ty, a, b, L = d
        x = del_procent(ty, a, b)
    elif typ == 'tio':
        _, ty, a, b, L = d
        x = del_tiopotens(ty, a, b)
    elif typ == 'avr':
        _, a, b, L = d
        x = del_avrunda(a, b)
    elif typ == 'fkt':
        _, a, b, L = d
        x = del_forkorta(a, b)
    x['L'] = L
    x['typ'] = typ
    return x


def huvudledtrad(dd):
    """Huvudkortets ledtråd: delarnas egna ledtrådar, en gång var."""
    texter = [x['ledtrad'][3:-4] for x in dd]
    if len(set(texter)) == 1:
        return f'<p>{texter[0]}</p>'
    return ''.join(f'<p><strong>{"abcd"[i]})</strong> {t}</p>' for i, t in enumerate(texter))


# ------------------------------------------------------------------ felrapport 2026-11-06 08:31 (0.02, 0.125, 0.62)
# Textersättningar i JSON-form (citattecken och backslash är redan escapade som i filen).
RATTELSER = {
    # "strikt mellan" är okänt för eleverna: frågetext → fetstilt mellan, facit/ledtråd → mellan
    '0.125': [('ligger strikt mellan', 'ligger <strong>mellan</strong>'),
              ('”Strikt mellan” betyder att ändpunkterna inte räknas', '”Mellan” betyder att ändpunkterna inte räknas')],
    '0.76': [('ger ett tal strikt mellan vilka', 'ger ett tal <strong>mellan</strong> vilka'),
             ('ligger talet strikt mellan a och b', 'ligger talet mellan a och b')],
    '0.591': [('ligger alltså strikt mellan', 'ligger alltså mellan')],
    '1.449': [('bara tal strikt mellan 3 och 5', 'bara tal mellan 3 och 5')],
    '0.1134': [('Andra tal strikt mellan gränserna', 'Andra tal mellan gränserna')],
    '0.1135': [('Andra tal strikt mellan gränserna', 'Andra tal mellan gränserna')],
    # övriga "strikt" i Ma1-banken skrivs med vardagliga ord
    '0.112': [('ger först ett strikt större tal?', 'ger först ett större tal?')],
    '0.118': [('Räkna bara siffror som ger strikt mindre.', 'Räkna bara siffror som ger ett mindre tal.')],
    '0.558': [('För positiva k växer k³ strikt, så', 'För positiva k blir k³ större när k blir större, så')],
    '1.118': [('−2 utesluts av det strikta tecknet och 7 är för stort.',
               '−2 utesluts eftersom tecknet vid −2 är &lt; och inte ≤, och 7 är för stort.')],
    '1.121': [('eftersom tecknet där är strikt mindre än.', 'eftersom tecknet där är &lt; och inte ≤.')],
    '1.226': [('Det strikta villkoret gäller vid 2 och likhet tillåts vid 7:', '2 ingår inte men 7 ingår:')],
    '2.214': [('ligger strikt i första kvadranten.', 'ligger i första kvadranten och inte på någon av axlarna.'),
              ('“Strikt i första kvadranten” betyder att', '“I första kvadranten och inte på axlarna” betyder att')],
    '3.02': [('är strikt växande. Lika potensvärden', 'blir alltid större när u blir större. Lika potensvärden')],
    '7.138': [('För en strikt värsta-fall-garanti återstår därför', 'För att summan garanterat ska hålla även i värsta fall återstår därför')],
    # 0.62: elevens räkning ska visa −7·(−5), inte en parentes runt −4−3
    '0.62': [('och skriver \\\\((-4-3)\\\\cdot(-5)=35\\\\)', 'och skriver \\\\(-7\\\\cdot(-5)=35\\\\)')],
}

# 0.02: deluppgifter med stigande svårighet (a enklast, d svårast) i stället för tre likvärdiga
DEL_0_02 = [E('-8+5', 1), E('6-14+9', 2), E('-3-7+12', 2), E('-5-(-9)+(-6)', 3)]


def objekt_span(src, uid):
    m = re.search(r'\{\s*"id":\s*"' + re.escape(uid) + r'"', src)
    assert m, uid
    obj, slut = json.JSONDecoder().raw_decode(src, m.start())
    return m.start(), slut, obj


def som_json(u, nl):
    return '\n'.join(('  ' + rad) if i else rad for i, rad in enumerate(json.dumps(u, ensure_ascii=False, indent=2).split('\n'))).replace('\n', nl)


def bygg_flerdelad(dd, instr):
    etik = 'abcd'
    rs, fm = zip(*[svar_rs(x['svar']) for x in dd])
    t = (f'<p>{instr}</p><div class="deluppgifter" style="display:grid;gap:0.85rem;margin:0.8rem 0;">'
         + ''.join(f'<div>{etik[i]}) {x["fraga"]}</div>' for i, x in enumerate(dd)) + '</div>')
    s_ = '<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<p><strong>{etik[i]})</strong></p>' + lista(x['steg'], f'\\({tex_tal(x["svar"])}\\)') for i, x in enumerate(dd)) + '</div>'
    spel = [dict(etikett=etik[i], t=f'<p>{instr}</p><div class="spel-en-del">{x["fraga"]}</div>', s=lista(x['steg'], f'\\({tex_tal(x["svar"])}\\)'),
                 ledtrad=x['ledtrad'], niva='E', poang='1/0/0', traningsniva=x['L']) for i, x in enumerate(dd)]
    return dict(t=t, s=s_, rättSvar=list(rs), svarFormat=list(fm), spelDelar=spel, poang=f'{len(dd)}/0/0',
                ledtrad=huvudledtrad(dd), traningsniva=max(x['L'] for x in dd))


def rattelser(src):
    nl = '\r\n' if '\r\n' in src else '\n'
    for uid, par in RATTELSER.items():
        a, b, _ = objekt_span(src, uid)
        bit = src[a:b]
        for gammal, ny in par:
            if gammal not in bit and ny in bit:   # redan rättad
                continue
            assert bit.count(gammal) == 1, (uid, gammal, bit.count(gammal))
            bit = bit.replace(gammal, ny)
        src = src[:a] + bit + src[b:]
    a, b, u = objekt_span(src, '0.02')
    if u.get('rättSvar') == [-14, 1, 2]:          # bara en gång
        u.update(bygg_flerdelad([bygg_del(d) for d in DEL_0_02], 'Beräkna.'))
        src = src[:a] + som_json(u, nl) + src[b:]
    return src


def main():
    src = open(BANK, encoding='utf-8', newline='').read()
    src = rattelser(src)
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    finns = {u['id'] for u in data}
    nya = []
    nr = START_ID
    for omr, familj, instr, delar in U:
        uid = f'0.{nr}'; nr += 1
        assert uid not in finns or '--skriv' not in sys.argv, uid   # torrkörning går även efter skrivning
        dd = [bygg_del(d) for d in delar]
        n = len(dd)
        enh = [x.get('enhet', '') for x in dd]
        rs, fm = zip(*[svar_rs(x['svar']) for x in dd])
        fm = [(x['svarform'] if x.get('svarform')
               else 'decimalform' if x['typ'] in ('dec', 'enh', 'proc', 'tio', 'avr') and f == 'numeriskt' else f) for x, f in zip(dd, fm)]
        rs = [(float(x['svar']) if x.get('svarform') == 'grundpotensform' else r) for x, r in zip(dd, rs)]
        def svar_html(x):
            if x.get('svartex'):
                return f'\\({x["svartex"]}\\)'
            v = x['svar']
            s = f'\\({tex_tal(v)}\\)'
            return s + (f' {x["enhet"]}' if x.get('enhet') else '')
        if n == 1:
            x = dd[0]
            text = x.get('fragetext') or f'{instr[:-1] if instr.endswith(".") else instr} {x["fraga"]}.'
            if instr and instr.startswith('Beräkna. Ange'):
                text = f'Beräkna {x["fraga"]}. Ange svaret i enklaste form.'
            elif instr and instr.startswith('Beräkna utan'):
                text = f'Beräkna {x["fraga"]} utan räknare.'
            elif instr and instr.startswith('Gör om'):
                text = x['fragetext']
            elif instr == 'Beräkna.':
                text = f'Beräkna {x["fraga"]}.'
            t = f'<p>{text}</p>'
            s = lista(x['steg'], svar_html(x))
            uppgift = dict(svarstyp='numeriskt', rättSvar=rs[0], tolerans=1e-9, svarFormat=fm[0], ledtrad=x['ledtrad'],
                           traningsniva=x['L'], arbetsinsats=1)
            if fm[0] in ('bråk', 'forkortat_brak'):
                uppgift['svarstyp'] = 'bråk'
            if enh[0]:
                uppgift['svarEnhet'] = enh[0]
        else:
            etik = 'abcd'
            delrader = []
            for i, x in enumerate(dd):
                q = x.get('fragetext') if instr is None or instr.startswith('Gör om') else x['fraga']
                delrader.append(f'<div>{etik[i]}) {q}</div>')
            inl = f'<p>{instr}</p>' if instr else ''
            t = (inl + '<div class="deluppgifter" style="display:grid;gap:0.85rem;margin:0.8rem 0;">' + ''.join(delrader) + '</div>')
            s = '<div class="facit-v2 facit-stegvis">' + ''.join(
                f'<p><strong>{etik[i]})</strong></p>' + lista(x['steg'], svar_html(x)) for i, x in enumerate(dd)) + '</div>'
            spel = []
            for i, x in enumerate(dd):
                q = x.get('fragetext') if instr is None or instr.startswith('Gör om') else x['fraga']
                st = f'<p>{instr}</p><div class="spel-en-del">{q}</div>' if instr and not instr.startswith('Gör om') else f'<div class="spel-en-del">{q}</div>'
                if instr and instr.startswith('Gör om'):
                    st = f'<p>{x["fragetext"]}</p>'
                elif instr is None:
                    st = f'<p>{x["fragetext"]}</p>'
                spel.append(dict(etikett=etik[i], t=st, s=lista(x['steg'], svar_html(x)), ledtrad=x['ledtrad'],
                                 niva='E', poang='1/0/0', traningsniva=x['L']))
            uppgift = dict(svarstyp='flera_delar', svarsstruktur='ordnad', rättSvar=list(rs), tolerans=1e-9, svarFormat=list(fm),
                           spelDelning='deluppgifter', spelDelar=spel,
                           ledtrad=huvudledtrad(dd),
                           traningsniva=max(x['L'] for x in dd), arbetsinsats=2)
            if any(enh):
                uppgift['svarEnhet'] = [e or None for e in enh]
        bas = dict(id=uid, kap=0, omr=omr, kurs=['1a', '1b', '1c'], niva='E', poang=f'{n}/0/0', t=t, s=s, familj=familj,
                   geogebra=False, miniräknare=False, självrättning=True, formaga=['procedur'], spel=True)
        bas.update(uppgift)
        nya.append(bas)
    # Lägg till efter sista kapitel 0-uppgiften i filen.
    sista = max((u for u in data if str(u.get('kap')) == '0'), key=lambda u: src.index('"' + u['id'] + '"'))
    m = re.search(r'\{\s*"id":\s*"' + re.escape(sista['id']) + r'"', src)
    _, slut = json.JSONDecoder().raw_decode(src, m.start())
    nl = '\r\n' if '\r\n' in src else '\n'
    tillagg = ''.join(',' + nl + '  ' + som_json(u, nl) for u in nya)
    ny_src = src[:slut] + tillagg + src[slut:]
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    print(len(nya), 'nya uppgifter,', sum(len(u.get('spelDelar') or [0]) for u in nya), 'delar')
    from collections import Counter
    print('delar per uppgift', sorted(Counter(len(u.get('spelDelar') or [1]) for u in nya).items()))
    print('per område', sorted(Counter(u['omr'] for u in nya).items()))
    if '--visa' in sys.argv:
        for u in nya:
            print(u['id'], u['omr'], json.dumps(u['rättSvar'], ensure_ascii=False), re.sub('<[^>]+>', ' ', u['t'])[:160])
    if '--skriv' in sys.argv:
        open(BANK, 'w', encoding='utf-8', newline='').write(ny_src)
        print('skrivet')
    return nya


if __name__ == '__main__':
    main()
