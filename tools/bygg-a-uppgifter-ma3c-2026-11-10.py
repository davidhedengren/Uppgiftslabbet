"""Ma3c (mato1): sju välkonstruerade A-uppgifter på träningsnivå 4–5 i centrala områden, 10 november 2026.

Varje uppgift är handskriven: egen situation, egna rubriker i facit enligt agent/FACITMALL.md, figur där den hjälper,
och delar i stigande svårighet. Alla svar kontrolleras med sympy. Se agent/A_UPPGIFTER_2026-11-10.md.

  python tools/bygg-a-uppgifter-ma3c-2026-11-10.py [--skriv] [--varianter fil.json]
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import m, mt, al, p, li, del_, Plot, svg, tt, linje, polygon, cirkel, BLA, ORA, GRON, GRA, INK, ROD  # noqa: E402

_s = importlib.util.spec_from_file_location('k1', Path(__file__).with_name('bygg-ma3c-kap1-mangdtraning-2026-11-06.py'))
k1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(k1)
sp, x = k1.sp, k1.x
BANK = 'uppgiftermato1.js'
VARIANTER = {}
PQ = r'pq-formeln: \(x=-\tfrac p2\pm\sqrt{\left(\tfrac p2\right)^2-q}\)'


# ================================================================ A1: gemensam tangent (tangenter)
def a1(uid):
    f1, f2 = x**2, -x**2 + 4 * x - 4
    a = sp.symbols('a')
    # Tangenten i (a, a²) är y = 2ax − a². Den tangerar f2 i x = 2 − a om punkten (2 − a, −a²) ligger på linjen.
    los = sp.solve(sp.Eq(-a**2, 2 * a * (2 - a) - a**2), a)
    assert sorted(los) == [0, 2]
    linje_ = 4 * x - 4
    assert sp.diff(f1, x).subs(x, 2) == 4 and f1.subs(x, 2) == linje_.subs(x, 2)
    assert sp.diff(f2, x).subs(x, 0) == 4 and f2.subs(x, 0) == linje_.subs(x, 0)
    assert sp.discriminant(f2 - linje_, x) == 0 and sp.discriminant(f1 - linje_, x) == 0

    def fig(med_tangent):
        P = Plot(-3, 5, -7.5, 10, W=420, H=340).axlar(xt=range(-2, 5), yt=range(-6, 10, 2))
        P.kurva(lambda v: v * v, color=BLA).kurva(lambda v: -(v - 2) ** 2, color=ORA)
        P.text(-1.9, 8.6, 'y = x²', BLA, 15, 'start', True).text(2, -6.6, 'y = −x² + 4x − 4', ORA, 15, 'middle', True)
        if med_tangent:
            P.kurva(lambda v: 4 * v - 4, color=GRON, w=2.2)
            P.punkt(2, 4, '(2, 4)', -10, -6, GRON, 'end').punkt(0, -4, '(0, −4)', 10, 6, GRON, 'start')
            P.text(3.55, 8.0, 'y = 4x − 4', GRON, 15, 'start', True)
            return P.svg('Parablerna y = x² och y = −x² + 4x − 4 med den gemensamma tangenten y = 4x − 4, som tangerar dem i (2, 4) och (0, −4).')
        return P.svg('Parabeln y = x² öppnar sig uppåt med vertex i origo. Parabeln y = −x² + 4x − 4 öppnar sig nedåt med vertex i (2, 0). Båda tangerar x-axeln.')

    intro = (p(r'Kurvorna \(y=x^2\) och \(y=-x^2+4x-4\) har två gemensamma tangenter, alltså räta linjer som tangerar båda '
               r'kurvorna. Den ena är \(x\)-axeln.') + fig(False))
    steg = [
        li(r'Tangenten till \(y=x^2\) i punkten \((a,\,a^2)\): lutningen är \(y^{\prime}=2a\)',
           p('Enpunktsformeln ger tangentens ekvation uttryckt i tangeringspunktens x-koordinat a.'),
           al(r'y-a^2=2a(x-a)', r'y=2ax-a^2')),
        li(r'Samma lutning i den andra kurvans tangeringspunkt: \(y^{\prime}=-2x+4\)',
           p(r'Kalla tangeringspunktens x-koordinat på den andra kurvan för \(b\). Lutningarna ska vara lika.'),
           al(r'-2b+4=2a', r'b=2-a')),
        li(r'Tangeringspunkten på den andra kurvan uttryckt i \(a\)',
           p(r'Den andra kurvan kan skrivas \(y=-(x-2)^2\). Med \(x=b=2-a\) blir \(y=-(2-a-2)^2=-a^2\).'),
           mt(r'\text{Punkten är }(2-a,\,-a^2)')),
        li('Punkten ska ligga på tangenten', p(r'Sätt in \(x=2-a\) och \(y=-a^2\) i \(y=2ax-a^2\).'),
           al(r'-a^2=2a(2-a)-a^2', r'0=2a(2-a)', r'a=0\ \text{eller}\ a=2')),
        li(r'\(a=0\) ger x-axeln och \(a=2\) ger den andra tangenten',
           al(r'a=0:\quad y=0', r'a=2:\quad y=2\cdot2\cdot x-2^2=4x-4')),
        li('Kontroll i figuren', p(r'Linjen \(y=4x-4\) tangerar \(y=x^2\) i \((2,\,4)\) och den andra kurvan i \((0,\,-4)\).'), fig(True)),
    ]
    d = del_(r'Bestäm ekvationen för den andra gemensamma tangenten.', steg, m('y=4x-4'),
             '', 'y=4x-4', 'A', 5, (0, 1, 2), fmt='uttryck', ai=3,
             ratt_txt=['y=4x-4', '4x-4', 'y = 4x − 4', '-4+4x'], fel=['y=0', '4x+4', 'y=4x', 'y=-4x-4'])
    return H.bygg(uid, 2, 'tangenter', 'Fördjupade tangentproblem', intro, [d], ('problemlösning', 'begrepp'), False, False,
                  r'Kalla tangeringspunkten på \(y=x^2\) för \((a,\,a^2)\) och skriv tangentens ekvation uttryckt i \(a\). '
                  'Vilka två villkor måste gälla i tangeringspunkten på den andra kurvan?', VARIANTER, kurs=['1b', '1c'])


# ================================================================ A2: kurva och tangent avgränsar ett område (integral)
def a2(uid):
    f, tang = x**3, 3 * x - 2
    assert sp.diff(f, x).subs(x, 1) == 3 and tang.subs(x, 1) == 1
    assert sp.factor(f - tang) == (x - 1)**2 * (x + 2)
    area = sp.integrate(f - tang, (x, -2, 1))
    assert area == sp.Rational(27, 4) and (f - tang).subs(x, 0) > 0
    F = x**4 / 4 - 3 * x**2 / 2 + 2 * x
    assert F.subs(x, 1) == sp.Rational(3, 4) and F.subs(x, -2) == -6

    def fig(siffror):
        P = Plot(-3, 2.4, -11.5, 7, W=400, H=340)
        P.axlar(xt=range(-2, 3) if siffror else (), yt=range(-10, 7, 2) if siffror else (), rut=siffror, siffror=siffror)
        P.fyll(lambda v: v**3, lambda v: 3 * v - 2, -2, 1, BLA, 0.22)
        P.kurva(lambda v: v**3, color=BLA).kurva(lambda v: 3 * v - 2, color=ORA, w=2.2)
        P.punkt(1, 1, '(1, 1)', -9, -9, INK, 'end').punkt(-2, -8, '(−2, −8)' if siffror else '', 10, 14, INK, 'start')
        P.text(1.72, 6.0, 'y = x³', BLA, 15, 'end', True).text(1.2, -3.4, 'tangent', ORA, 15, 'start', True)
        return P.svg('Kurvan y = x³ och dess tangent i punkten (1, 1). Tangenten skär kurvan en gång till, till vänster om y-axeln. '
                     'Området mellan kurvan och tangenten är skuggat.' + (' Den andra skärningspunkten är (−2, −8).' if siffror else ''))

    intro = (p(r'Figuren visar kurvan \(y=x^3\) och kurvans tangent i punkten \((1,\,1)\). Tangenten skär kurvan i ytterligare '
               'en punkt. Kurvan och tangenten begränsar tillsammans det skuggade området.') + fig(False))
    steg_a = [
        li(r'Derivatan ger tangentens lutning: \(y^{\prime}=3x^2\)', mt(r'k=3\cdot1^2=3')),
        li(r'Enpunktsformeln: \(y-y_1=k(x-x_1)\) med punkten \((1,\,1)\)', al(r'y-1=3(x-1)', r'y=3x-2')),
    ]
    steg_b = [
        li('I en skärningspunkt har kurvan och tangenten samma y-värde', al(r'x^3=3x-2', r'x^3-3x+2=0')),
        li(r'\(x=1\) är en dubbelrot eftersom linjen tangerar kurvan där',
           p(r'Polynomet har därför faktorn \((x-1)^2=x^2-2x+1\). Den tredje faktorn har formen \((x+c)\).'),
           mt(r'x^3-3x+2=(x^2-2x+1)(x+c)')),
        li(r'Konstanttermerna ger \(c\)', p(r'Vänsterledets konstantterm är 2 och högerledets är \(1\cdot c\), så \(c=2\). Kontroll:'),
           al(r'(x^2-2x+1)(x+2)', r'=x^3+2x^2-2x^2-4x+x+2', r'=x^3-3x+2')),
        li(r'Nollproduktmetoden: \((x-1)^2(x+2)=0\)', p(r'Lösningarna är \(x=1\), som är tangeringspunkten, och \(x=-2\).')),
    ]
    steg_c = [
        li(r'Kurvan ligger över tangenten mellan \(x=-2\) och \(x=1\)',
           p(r'Pröva med \(x=0\): kurvan ger \(0^3=0\) och tangenten ger \(3\cdot0-2=-2\).'), fig(True)),
        li(r'Area mellan två grafer: \(A=\displaystyle\int_a^b(\text{övre}-\text{undre})\,dx\)',
           al(r'A=\int_{-2}^{1}\left(x^3-(3x-2)\right)dx', r'\phantom{A}=\int_{-2}^{1}(x^3-3x+2)\,dx')),
        li(r'Primitiv funktion: \(F(x)=\dfrac{x^4}{4}-\dfrac{3x^2}{2}+2x\)',
           al(r'F(1)=\tfrac14-\tfrac32+2=\tfrac34', r'F(-2)=\tfrac{16}{4}-\tfrac{12}{2}-4=-6')),
        li(r'Integralens värde: \(F(1)-F(-2)\)', mt(r'A=\tfrac34-(-6)=\tfrac{27}{4}=6{,}75')),
    ]
    delar = [
        del_('Bestäm tangentens ekvation.', steg_a, m('y=3x-2'), 'Tangentens lutning är derivatans värde i tangeringspunkten.',
             'y=3x-2', 'C', 3, (0, 1, 0), fmt='uttryck', ratt_txt=['y=3x-2', '3x-2'], fel=['y=3x', '3x+2', 'y=x^3']),
        del_(r'Bestäm \(x\)-koordinaten för den andra skärningspunkten mellan tangenten och kurvan.', steg_b, m('x=-2'),
             r'Ekvationen blir av tredje graden. Vilken lösning känner du redan till, och varför är den en dubbelrot?',
             -2, 'C', 4, (0, 1, 0),
             kortfraga=r'Tangenten har ekvationen \(y=3x-2\). Bestäm \(x\)-koordinaten för den andra skärningspunkten mellan tangenten och kurvan.',
             ratt_txt=['-2', 'x=-2', '−2'], fel=['2', '1', '-1']),
        del_('Beräkna det skuggade områdets area.', steg_c, r'\(\tfrac{27}{4}=6{,}75\) areaenheter',
             'Avgör vilken graf som ligger överst mellan skärningspunkterna och integrera skillnaden.',
             6.75, 'A', 5, (0, 0, 1), ai=3,
             kortfraga=r'Tangenten har ekvationen \(y=3x-2\) och skär kurvan även där \(x=-2\). Beräkna det skuggade områdets area.',
             ratt_txt=['27/4', '6,75', '6.75'], fel=['6', '7,75', '27/2', '-6,75']),
    ]
    return H.bygg(uid, 3, 'integralberakning', 'Area mellan två grafer', intro, delar, ('problemlösning', 'procedur'), False, False,
                  'Börja med tangentens lutning i punkten (1, 1).', VARIANTER, kurs=['1b', '1c'])


# ================================================================ A3: extrempunkter med parameter
def a3(uid):
    a = sp.symbols('a')
    f = x**3 + a * x**2 - 9 * x
    assert sp.solve(sp.diff(f, x).subs(x, -1), a) == [-3]
    g = f.subs(a, -3)
    assert sorted(sp.solve(sp.diff(g, x), x)) == [-1, 3] and g.subs(x, -1) == 5 and g.subs(x, 3) == -27
    assert sp.diff(g, x, 2).subs(x, -1) < 0 < sp.diff(g, x, 2).subs(x, 3)
    antal = len([k for k in range(-60, 60) if len(sp.real_roots(g - k)) == 3 and len(set(sp.real_roots(g - k))) == 3])
    assert antal == 31 == 4 - (-26) + 1
    gf = lambda v: v**3 - 3 * v**2 - 9 * v

    def fig():
        P = Plot(-3.6, 5.6, -36, 14, W=420, H=340).axlar(xt=range(-3, 6), yt=range(-30, 11, 10))
        P.fyll(lambda v: 5, lambda v: -27, -3.6, 5.6, GRON, 0.10)
        P.streck(-3.6, 5, 5.6, 5, GRON).streck(-3.6, -27, 5.6, -27, GRON)
        P.kurva(gf, color=BLA)
        P.punkt(-1, 5, '(−1, 5)', -10, -9, ORA, 'end').punkt(3, -27, '(3, −27)', 0, 22, ORA, 'middle')
        P.streck(-3.6, -11, 5.6, -11, GRON, 2, None).text(2.6, -8.2, 'y = k', GRON, 15, 'middle', True)
        for r in sp.real_roots(g + 11):
            P.punkt(float(r), -11, '', color=GRON)
        return P.svg('Grafen till f(x) = x³ − 3x² − 9x med maximipunkten (−1, 5) och minimipunkten (3, −27). '
                     'En vågrät linje y = k mellan −27 och 5 skär grafen i tre punkter.')

    intro = p(r'Funktionen \(f(x)=x^3+ax^2-9x\), där \(a\) är en konstant, har en lokal maximipunkt där \(x=-1\).')
    steg_a = [
        li(r'I en lokal extrempunkt är derivatan noll: \(f^{\prime}(x)=3x^2+2ax-9\)', p(r'Villkoret är \(f^{\prime}(-1)=0\).'),
           al(r'3\cdot(-1)^2+2a\cdot(-1)-9=0', r'3-2a-9=0', r'a=-3')),
        li(r'Kontroll med andraderivatan: \(f^{\prime\prime}(x)=6x+2a=6x-6\)',
           p(r'\(f^{\prime\prime}(-1)=-12&lt;0\), så punkten är en maximipunkt.')),
    ]
    der = li(r'Derivatans nollställen: \(f^{\prime}(x)=3x^2-6x-9\)', p(r'Med \(a=-3\) är \(f(x)=x^3-3x^2-9x\). Dividera \(f^{\prime}(x)=0\) med 3.'),
             mt(r'x^2-2x-3=0'))
    pq = li(PQ + r' med \(p=-2\) och \(q=-3\)', al(r'x=1\pm\sqrt{1+3}=1\pm2', r'x=-1\ \text{eller}\ x=3'))
    steg_b = [der, pq,
              li(r'Andraderivatan avgör typen: \(f^{\prime\prime}(x)=6x-6\)', p(r'\(f^{\prime\prime}(3)=12&gt;0\), så \(x=3\) ger en minimipunkt.')),
              li(r'Minimivärdet är \(f(3)\)', al(r'f(3)=3^3-3\cdot3^2-9\cdot3', r'\phantom{f(3)}=27-27-27=-27'))]
    steg_c = [der, pq,
              li('Funktionens lokala extremvärden',
                 al(r'f(-1)=-1-3+9=5', r'f(3)=27-27-27=-27'), p('Maximivärdet är 5 och minimivärdet är −27.')),
              li(r'Linjen \(y=k\) ska skära grafen i tre punkter',
                 p(r'Grafen växer fram till maximipunkten, avtar till minimipunkten och växer sedan igen. En vågrät linje skär den '
                   r'därför tre gånger precis när den ligger mellan extremvärdena: \(-27&lt;k&lt;5\). För \(k=5\) och \(k=-27\) '
                   'tangerar linjen grafen, och då finns bara två olika lösningar.'), fig()),
              li(r'Räkna heltalen från \(-26\) till \(4\)', mt(r'4-(-26)+1=31'))]
    delar = [
        del_(r'Bestäm \(a\).', steg_a, m('a=-3'), r'Vad vet du om \(f^{\prime}(x)\) i en extrempunkt?', -3, 'C', 3, (0, 1, 0),
             ratt_txt=['-3', 'a=-3'], fel=['3', '-6']),
        del_('Bestäm funktionens lokala minimivärde.', steg_b, m('-27'),
             r'Bestäm först för vilka \(x\) derivatan är noll. Minimivärdet är funktionens värde där, inte \(x\)-värdet.',
             -27, 'C', 4, (0, 1, 0), kortfraga=r'Det gäller att \(a=-3\). Bestäm funktionens lokala minimivärde.',
             ratt_txt=['-27', '−27'], fel=['3', '27', '5']),
        del_(r'För hur många heltal \(k\) har ekvationen \(f(x)=k\) tre olika reella lösningar?', steg_c, '31 heltal',
             r'Skissa grafen med dess maximi- och minimipunkt. Hur ska en vågrät linje \(y=k\) ligga för att skära grafen tre gånger?',
             31, 'A', 5, (0, 0, 1), ai=3,
             kortfraga=r'Det gäller att \(a=-3\). För hur många heltal \(k\) har ekvationen \(f(x)=k\) tre olika reella lösningar?',
             ratt_txt=['31'], fel=['32', '30', '33', '3']),
    ]
    return H.bygg(uid, 3, 'extrempunkter', 'Extrempunkter med parameter', intro, delar, ('problemlösning', 'begrepp'), False, False,
                  r'I en lokal extrempunkt är \(f^{\prime}(x)=0\).', VARIANTER, kurs=['1b', '1c'])


# ================================================================ A4: areasatsen med två fall
def a4(uid):
    sinA = sp.Rational(2 * 14, 7 * 5)
    assert sinA == sp.Rational(4, 5)
    A1 = math.degrees(math.asin(0.8))
    A2 = 180 - A1
    bc1, bc2 = math.sqrt(74 - 70 * 0.6), math.sqrt(74 + 70 * 0.6)
    assert abs(A1 - 53.1301) < 1e-4 and abs(bc1**2 - 32) < 1e-9 and abs(bc2**2 - 116) < 1e-9
    for v, bc in ((A1, bc1), (A2, bc2)):  # båda trianglarna har arean 14 och uppfyller cosinussatsen
        assert abs(0.5 * 7 * 5 * math.sin(math.radians(v)) - 14) < 1e-9
        assert abs(bc**2 - (49 + 25 - 70 * math.cos(math.radians(v)))) < 1e-9

    def fig():
        s, b = 22, []
        for ax, cx, namn in ((24, 24 + 3 * s, 'spetsig vinkel A'), (286, 286 - 3 * s, 'trubbig vinkel A')):
            A, B, C = (ax, 150), (ax + 7 * s, 150), (cx, 150 - 4 * s)
            b.append(polygon([A, B, C], LJUS_BLA, INK))
            b.append(tt(A[0] - 2, A[1] + 20, 'A', 16, bold=True) + tt(B[0] + 2, B[1] + 20, 'B', 16, bold=True) + tt(C[0], C[1] - 9, 'C', 16, bold=True))
            b.append(tt((A[0] + B[0]) / 2, 172, '7,0 cm', 14))
            mx, my = (A[0] + C[0]) / 2, (A[1] + C[1]) / 2
            b.append(tt(mx - (14 if cx > ax else 26), my - 4, '5,0 cm', 14, 'end'))
            b.append(tt(ax + 3.5 * s, 196, namn, 13, fill=GRA))
        return svg(464, 208, ''.join(b), 'Två trianglar ABC med AB = 7,0 cm och AC = 5,0 cm. I den vänstra är vinkeln A spetsig, '
                                          'i den högra är vinkeln A trubbig. Båda har arean 14 cm².')

    intro = (p(r'I triangeln \(ABC\) är \(AB=7{,}0\) cm och \(AC=5{,}0\) cm. Triangelns area är 14 cm². '
               'Det finns två olika trianglar som uppfyller villkoren.') + fig())
    sinsteg = [li(r'Areasatsen: \(T=\dfrac{b\,c\,\sin A}{2}\)', p('Sidorna 7,0 cm och 5,0 cm är de som bildar vinkeln A.'),
                  mt(r'14=\frac{7{,}0\cdot5{,}0\cdot\sin A}{2}')),
               li(r'Lös ut \(\sin A\)', mt(r'\sin A=\frac{2\cdot14}{7{,}0\cdot5{,}0}=0{,}8'))]
    steg_a = sinsteg + [
        li(r'Två vinklar har samma sinusvärde: \(\sin v=\sin(180^\circ-v)\)',
           al(r'A_1=\sin^{-1}(0{,}8)\approx53{,}1^\circ', r'A_2=180^\circ-53{,}1^\circ=126{,}9^\circ'),
           p('Båda vinklarna är mindre än 180° och kan därför vara en vinkel i en triangel.'))]
    steg_b = sinsteg + [
        li(r'De två möjliga vinklarna: \(\sin v=\sin(180^\circ-v)\)', mt(r'A\approx53{,}13^\circ\ \text{eller}\ A\approx126{,}87^\circ')),
        li(r'Cosinussatsen: \(a^2=b^2+c^2-2bc\cos A\)',
           al(r'BC^2=5{,}0^2+7{,}0^2', r'\qquad-2\cdot5{,}0\cdot7{,}0\cdot\cos A', r'BC^2=74-70\cos A')),
        li(r'Spetsig vinkel: \(\cos53{,}13^\circ=0{,}6\)', al(r'BC^2=74-70\cdot0{,}6=32', r'BC=\sqrt{32}\approx5{,}7\ \text{cm}')),
        li(r'Trubbig vinkel: \(\cos126{,}87^\circ=-0{,}6\)', al(r'BC^2=74+70\cdot0{,}6=116', r'BC=\sqrt{116}\approx10{,}8\ \text{cm}'))]
    delar = [
        del_(r'Bestäm de två möjliga storlekarna på vinkeln \(A\). (Svara i grader med en decimal.)', steg_a,
             r'\(A\approx53{,}1^\circ\) eller \(A\approx126{,}9^\circ\)',
             'Använd areasatsen för att bestämma sin A. Hur många vinklar mellan 0° och 180° har det sinusvärdet?',
             [round(A1, 4), round(A2, 4)], 'C', 4, (0, 1, 0), tol=0.05, enhet='°'),
        del_(r'Bestäm de två möjliga längderna på sidan \(BC\). (Svara i cm med en decimal.)', steg_b,
             r'\(BC\approx5{,}7\) cm eller \(BC\approx10{,}8\) cm',
             'Bestäm först de två möjliga vinklarna A med areasatsen. Använd sedan cosinussatsen för varje vinkel.',
             [round(bc1, 4), round(bc2, 4)], 'A', 5, (0, 0, 2), tol=0.05, enhet='cm', ai=3),
    ]
    return H.bygg(uid, 4, 'areasatsen', 'Areasatsen i sammansatta figurer och omvända problem', intro, delar,
                  ('problemlösning', 'begrepp'), True, False,
                  'Areasatsen ger sin A. Tänk på att två olika vinklar i en triangel kan ha samma sinusvärde.', VARIANTER, kurs=['1c'])


LJUS_BLA = '#edf4f8'


# ================================================================ A5: polynom med parameter (polynomekvationer)
def a5(uid):
    a, c = sp.symbols('a c')
    pol = x**3 + a * x**2 - 4 * x - 12
    assert sp.solve(pol.subs(x, 2), a) == [3]
    pol = pol.subs(a, 3)
    assert sp.factor(pol) == (x - 2) * (x + 2) * (x + 3) and sp.expand((x - 2) * (x**2 + 5 * x + 6)) == pol
    # p(x) = c(x − 2)  ⇔  (x − 2)(x² + 5x + 6 − c) = 0. Dubbelrot i andragradsfaktorn när (5/2)² − (6 − c) = 0.
    cv = sp.solve(sp.Rational(25, 4) - (6 - c), c)[0]
    assert cv == sp.Rational(-1, 4)
    rot = sp.roots(sp.expand(pol - cv * (x - 2)), x)
    assert rot == {2: 1, sp.Rational(-5, 2): 2}
    intro = p(r'Polynomet \(p(x)=x^3+ax^2-4x-12\), där \(a\) är en konstant, har nollstället \(x=2\).')
    steg_a = [li(r'Ett nollställe uppfyller \(p(2)=0\)', al(r'2^3+a\cdot2^2-4\cdot2-12=0', r'8+4a-8-12=0', r'4a=12', r'a=3'))]
    steg_b = [
        li(r'Faktorsatsen: nollstället \(x=2\) ger faktorn \((x-2)\)',
           p(r'Med \(a=3\) är \(p(x)=x^3+3x^2-4x-12\). Den andra faktorn är av andra graden.'), mt(r'p(x)=(x-2)(x^2+kx+m)')),
        li('Jämför koefficienter', p('Utveckla högerledet och jämför med polynomet.'),
           al(r'(x-2)(x^2+kx+m)', r'=x^3+(k-2)x^2', r'\quad+(m-2k)x-2m'),
           p(r'Konstanttermen ger \(-2m=-12\), alltså \(m=6\). \(x^2\)-termen ger \(k-2=3\), alltså \(k=5\). '
             r'Kontroll med \(x\)-termen: \(m-2k=6-10=-4\).')),
        li(PQ + r' på \(x^2+5x+6=0\)', al(r'x=-\tfrac52\pm\sqrt{\tfrac{25}{4}-6}=-2{,}5\pm0{,}5', r'x=-3\ \text{eller}\ x=-2')),
        li('Grafisk kontroll: grafen skär x-axeln i nollställena',
           p(r'Grafen till \(y=x^2+5x+6\) skär x-axeln i \(x=-3\) och \(x=-2\).'),
           k1.graf(x**2 + 5 * x + 6, [-3, -2], 'Grafen till y = x² + 5x + 6 skär x-axeln vid x = −3 och x = −2.')),
    ]
    steg_c = [
        li(r'Samla allt i vänsterledet och bryt ut \((x-2)\)',
           al(r'(x-2)(x^2+5x+6)=c(x-2)', r'(x-2)(x^2+5x+6)-c(x-2)=0', r'(x-2)(x^2+5x+6-c)=0')),
        li('Dubbelroten ska komma från andragradsfaktorn',
           p(r'\(x=2\) är alltid en lösning. Den sökta dubbelroten är därför en dubbelrot till \(x^2+5x+(6-c)=0\).')),
        li(r'pq-formeln ger en dubbelrot när \(\left(\tfrac p2\right)^2-q=0\)', p(r'Här är \(p=5\) och \(q=6-c\).'),
           al(r'\left(\tfrac52\right)^2-(6-c)=0', r'6{,}25-6+c=0', r'c=-0{,}25')),
        li(r'Kontroll: \(x^2+5x+6{,}25=(x+2{,}5)^2\)', p(r'Dubbelroten är \(x=-2{,}5\), som inte är lika med 2.')),
    ]
    delar = [
        del_(r'Bestäm \(a\).', steg_a, m('a=3'), 'Vad blir polynomets värde när man sätter in ett nollställe?', 3, 'C', 3, (0, 1, 0),
             ratt_txt=['3', 'a=3'], fel=['-3', '5']),
        del_('Bestäm polynomets övriga nollställen.', steg_b, r'\(x=-3\) och \(x=-2\)',
             'Ett känt nollställe ger en faktor. Bestäm den andra faktorn, som är av andra graden.', [-3, -2], 'C', 4, (0, 1, 0),
             kortfraga=r'Det gäller att \(a=3\). Bestäm polynomets övriga nollställen.'),
        del_(r'För vilket värde på konstanten \(c\) har ekvationen \(p(x)=c(x-2)\) en dubbelrot som inte är \(x=2\)?', steg_c,
             r'\(c=-\tfrac14\)',
             r'Båda leden innehåller faktorn \((x-2)\). Vad måste gälla för den faktor som blir kvar?', -0.25, 'A', 5, (0, 0, 1), ai=3,
             kortfraga=(r'Det gäller att \(a=3\), så \(p(x)=(x-2)(x^2+5x+6)\). För vilket värde på konstanten \(c\) har ekvationen '
                        r'\(p(x)=c(x-2)\) en dubbelrot som inte är \(x=2\)?'),
             ratt_txt=['-0,25', '-1/4', 'c=-1/4', '−0,25'], fel=['0,25', '-0,5', '20', '6']),
    ]
    return H.bygg(uid, 1, 'polynomekvationer', 'Parameter och antal lösningar', intro, delar, ('problemlösning', 'procedur'),
                  False, False, r'Ett nollställe ger \(p(2)=0\) och faktorn \((x-2)\).', VARIANTER, kurs=['1b', '1c'])


# ================================================================ A6: vinst och skatt (derivata i modeller)
def a6(uid):
    t = sp.symbols('t')
    V = x * (130 - sp.Rational(1, 2) * x) - (400 + 10 * x + sp.Rational(1, 10) * x**2)
    assert sp.expand(V) == -sp.Rational(3, 5) * x**2 + 120 * x - 400
    assert sp.solve(sp.diff(V, x), x) == [100] and V.subs(x, 100) == 5600
    xt = sp.solve(sp.diff(V - t * x, x), x)[0]
    S = sp.simplify(t * xt)
    assert sp.solve(sp.diff(S, t), t) == [60] and S.subs(t, 60) == 3000 and xt.subs(t, 60) == 50
    def fig():
        P = Plot(0, 130, 0, 3600, W=420, H=300, ml=58).axlar(xt=range(0, 121, 20), yt=range(0, 3601, 1000), xlabel='t (kr)', ylabel='S (kr)')
        P.kurva(lambda u: u * (120 - u) / 1.2, 0, 120, color=BLA)
        P.streck(60, 0, 60, 3000).streck(0, 3000, 60, 3000).punkt(60, 3000, '(60, 3 000)', 10, -8, ORA, 'start')
        P.text(104, 1500, 'S(t)', BLA, 15, 'start', True)
        return P.svg('Statens skatteintäkt S som funktion av skatten t kronor per enhet. Grafen är en parabel som börjar i noll, '
                     'har sitt största värde 3 000 kr vid t = 60 kr och är noll igen vid t = 120 kr.')

    intro = p(r'Ett företag säljer \(x\) enheter av en vara per vecka, där \(0\le x\le200\). Priset per enhet är '
              r'\(p(x)=130-0{,}5x\) kr och kostnaden för att tillverka \(x\) enheter är \(K(x)=400+10x+0{,}1x^2\) kr.')
    vinst = li(r'Vinst = intäkt − kostnad: \(V(x)=x\cdot p(x)-K(x)\)',
               al(r'V(x)=x(130-0{,}5x)', r'\qquad-(400+10x+0{,}1x^2)', r'V(x)=-0{,}6x^2+120x-400'))
    steg_a = [vinst,
              li(r'Derivatan är noll i en extrempunkt: \(V^{\prime}(x)=-1{,}2x+120\)', al(r'-1{,}2x+120=0', r'x=100')),
              li(r'Maximum eftersom \(V^{\prime\prime}(x)=-1{,}2&lt;0\)', p(r'\(x=100\) ligger dessutom i intervallet \(0\le x\le200\).')),
              li(r'Största vinsten är \(V(100)\)', al(r'V(100)=-0{,}6\cdot100^2', r'\qquad+120\cdot100-400', r'V(100)=5\,600'))]
    steg_b = [vinst,
              li(r'Skatten \(t\cdot x\) dras från vinsten', mt(r'V_t(x)=-0{,}6x^2+(120-t)x-400')),
              li(r'Företaget väljer det \(x\) där \(V_t^{\prime}(x)=0\)', al(r'-1{,}2x+120-t=0', r'x=\frac{120-t}{1{,}2}')),
              li(r'Statens skatteintäkt: \(S(t)=t\cdot x\)', mt(r'S(t)=\frac{t(120-t)}{1{,}2}=\frac{120t-t^2}{1{,}2}')),
              li(r'Största intäkten: \(S^{\prime}(t)=\dfrac{120-2t}{1{,}2}=0\)', mt(r't=60'),
                 p(r'Det är ett maximum eftersom \(S^{\prime\prime}(t)=-\tfrac{2}{1{,}2}&lt;0\). Grafen visar samma sak.'), fig()),
              li('Kontroll', p(r'Med \(t=60\) säljer företaget \(x=\tfrac{120-60}{1{,}2}=50\) enheter, och staten får '
                               r'\(60\cdot50=3\,000\) kr per vecka. En högre skatt ger så få sålda enheter att intäkten minskar.'))]
    delar = [
        del_('Hur stor är den största möjliga vinsten per vecka?', steg_a, '5 600 kr',
             'Vinsten är intäkten minus kostnaden. Intäkten är antalet enheter gånger priset per enhet.', 5600, 'C', 4, (0, 2, 0),
             enhet='kr', ratt_txt=['5600', '5 600 kr', '5600 kr'], fel=['100', '5000', '12000']),
        del_(r'Staten inför en skatt på \(t\) kr per såld enhet, som företaget betalar. Företaget väljer då det antal enheter som ger '
             r'störst vinst efter skatt. Vilket värde på \(t\) ger staten störst skatteintäkt?', steg_b, r'\(t=60\) kr per enhet',
             r'Bestäm först hur många enheter företaget väljer att sälja, uttryckt i \(t\). Statens intäkt är \(t\) gånger det antalet.',
             60, 'A', 5, (0, 0, 2), enhet='kr', ai=3, ratt_txt=['60', '60 kr', 't=60'], fel=['50', '120', '30', '100']),
    ]
    return H.bygg(uid, 3, 'problemlosning_derivata', 'Tolka derivata i modeller', intro, delar, ('problemlösning', 'modellering'),
                  True, False, 'Ställ upp vinsten som en funktion av x: intäkt minus kostnad.', VARIANTER, kurs=['1b', '1c'])


# ================================================================ A7: parallellogrammens diagonaler (cosinussatsen)
def a7(uid):
    cosA = sp.Rational(64 + 25 - 121, 80)
    assert cosA == sp.Rational(-2, 5)
    A = math.degrees(math.acos(-0.4))
    AC = math.sqrt(89 - 80 * 0.4)
    assert abs(AC**2 - 57) < 1e-9 and abs(A - 113.5782) < 1e-4 and 121 + 57 == 2 * (64 + 25)

    def fig():
        s = 30
        Ax, Ay = 112, 180
        dx, dy = 5 * s * math.cos(math.radians(A)), 5 * s * math.sin(math.radians(A))
        Pa, Pb = (Ax, Ay), (Ax + 8 * s, Ay)
        Pd, Pc = (Ax + dx, Ay - dy), (Ax + 8 * s + dx, Ay - dy)
        b = polygon([Pa, Pb, Pc, Pd], LJUS_BLA, INK)
        b += linje(*Pb, *Pd, ORA, 2.4) + linje(*Pa, *Pc, GRA, 2, '6 5')
        b += tt(Pa[0] - 4, Pa[1] + 20, 'A', 16, bold=True) + tt(Pb[0] + 6, Pb[1] + 20, 'B', 16, bold=True)
        b += tt(Pc[0] + 8, Pc[1] - 6, 'C', 16, bold=True) + tt(Pd[0] - 8, Pd[1] - 6, 'D', 16, bold=True)
        b += tt((Pa[0] + Pb[0]) / 2, Ay + 21, '8,0 cm', 14) + tt((Pa[0] + Pd[0]) / 2 - 10, (Pa[1] + Pd[1]) / 2 + 4, '5,0 cm', 14, 'end')
        b += tt(Pd[0] + 0.30 * (Pb[0] - Pd[0]) + 8, Pd[1] + 0.30 * (Pb[1] - Pd[1]) - 9, '11 cm', 14, 'start', ORA, True, True)
        return svg(392, 214, b, 'Parallellogrammen ABCD med AB = 8,0 cm och AD = 5,0 cm. Diagonalen BD är 11 cm och är utritad. '
                                'Diagonalen AC är streckad. Vinkeln A är trubbig.')

    intro = p(r'I parallellogrammen \(ABCD\) är sidan \(AB=8{,}0\) cm och sidan \(AD=5{,}0\) cm. Diagonalen \(BD\) är 11 cm.') + fig()
    cos_a = li(r'Cosinussatsen i triangeln \(ABD\): \(a^2=b^2+c^2-2bc\cos A\)',
               p('Triangeln ABD har sidorna 8,0 cm, 5,0 cm och 11 cm, där 11 cm står mot vinkeln A.'),
               al(r'11^2=8{,}0^2+5{,}0^2', r'\qquad-2\cdot8{,}0\cdot5{,}0\cdot\cos A'))
    los_a = li(r'Lös ut \(\cos A\)', mt(r'\cos A=\frac{64+25-121}{80}=-0{,}4'))
    steg_a = [cos_a, los_a, li('Vinkeln är trubbig eftersom cosinusvärdet är negativt', mt(r'A=\cos^{-1}(-0{,}4)\approx113{,}6^\circ'))]
    steg_b = [cos_a, los_a,
              li(r'Närliggande vinklar i en parallellogram har summan 180°: \(\cos(180^\circ-A)=-\cos A\)', mt(r'\cos B=0{,}4')),
              li(r'Cosinussatsen i triangeln \(ABC\), där \(BC=AD=5{,}0\) cm',
                 al(r'AC^2=8{,}0^2+5{,}0^2-2\cdot8{,}0\cdot5{,}0\cdot0{,}4', r'AC^2=89-32=57', r'AC=\sqrt{57}\approx7{,}55\ \text{cm}'))]
    steg_c = [
        li(r'Cosinussatsen för båda diagonalerna: \(d^2=a^2+b^2-2ab\cos v\)',
           p(r'Kalla vinkeln mellan sidorna för \(v\). Den ena diagonalen står mot \(v\), den andra mot \(180^\circ-v\).'),
           al(r'd_1^2=a^2+b^2-2ab\cos v', r'd_2^2=a^2+b^2-2ab\cos(180^\circ-v)')),
        li(r'Använd \(\cos(180^\circ-v)=-\cos v\)', mt(r'd_2^2=a^2+b^2+2ab\cos v')),
        li('Addera de två sambanden', p(r'Termerna med \(\cos v\) tar ut varandra.'), mt(r'd_1^2+d_2^2=2a^2+2b^2=2\,(a^2+b^2)')),
        li('Kontroll med uppgiftens parallellogram', mt(r'11^2+57=178=2\cdot(8{,}0^2+5{,}0^2)')),
    ]
    delar = [
        del_(r'Bestäm vinkeln \(A\). (Svara i grader med en decimal.)', steg_a, r'\(A\approx113{,}6^\circ\)',
             'Diagonalen BD delar parallellogrammen i två trianglar. I triangeln ABD är alla tre sidor kända.',
             round(A, 4), 'C', 3, (0, 1, 0), tol=0.05, enhet='°', ratt_txt=['113,6', '113,58', '113,6°'], fel=['66,4', '113,5', '113']),
        del_(r'Bestäm längden av diagonalen \(AC\). (Svara i cm med två decimaler.)', steg_b, r'\(AC=\sqrt{57}\approx7{,}55\) cm',
             'Vilken vinkel står mot diagonalen AC i triangeln ABC? Hur hänger den ihop med vinkeln A?',
             round(AC, 5), 'C', 4, (0, 1, 0), tol=0.005, enhet='cm', ratt_txt=['7,55', '7,550', '7,55 cm'], fel=['7,5', '7,6', '11']),
        del_(r'För varje parallellogram med sidorna \(a\) och \(b\) och diagonalerna \(d_1\) och \(d_2\) gäller '
             r'\(d_1^2+d_2^2=k\,(a^2+b^2)\) för ett bestämt tal \(k\). Bestäm \(k\).', steg_c, m('k=2'),
             'Skriv cosinussatsen för var och en av diagonalerna. De två vinklarna har summan 180°.', 2, 'A', 5, (0, 0, 1), ai=3,
             ratt_txt=['2', 'k=2'], fel=['1', '4', '0,5']),
    ]
    return H.bygg(uid, 4, 'cosinussatsen', 'Cosinussatsen – samband och problemlösning', intro, delar,
                  ('problemlösning', 'resonemang'), True, False,
                  'Diagonalen BD delar parallellogrammen i två trianglar där alla sidor är kända.', VARIANTER, kurs=['1c'])


UPPGIFTER = [(2, a1), (3, a2), (3, a3), (4, a4), (1, a5), (3, a6), (4, a7)]


def main():
    src, bank = H.las(BANK)
    nasta = {}
    nya = []
    for kap, funk in UPPGIFTER:
        nasta.setdefault(kap, H.nasta_id(bank, kap))
        nya.append(funk(f'{kap}.{nasta[kap]}'))
        nasta[kap] += 1
    assert not {q['id'] for q in bank} & {q['id'] for q in nya}
    for q in nya:  # område och delmoment ska redan finnas i banken
        assert any(b['omr'] == q['omr'] and q['familj'] in ([b['familj']] if isinstance(b['familj'], str) else b['familj'])
                   for b in bank), (q['id'], q['omr'], q['familj'])
    print('uppgifter', len(nya), 'kort', sum(len(q.get('spelDelar') or [1]) for q in nya), [q['id'] for q in nya])
    if '--varianter' in sys.argv:
        Path(sys.argv[sys.argv.index('--varianter') + 1]).write_text(json.dumps(VARIANTER, ensure_ascii=False, indent=1), encoding='utf-8')
    if '--skriv' in sys.argv:
        H.lagg_till(BANK, src, nya)


if __name__ == '__main__':
    main()
