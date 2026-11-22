# Ma4 radianbegreppet och cirkelsektorn: facit enligt FACITMALL (2026-11-22).
TILL_RAD = r"Från grader till radianer: multiplicera med \(\frac{\pi}{180^\circ}\)"
TILL_GR = r"Från radianer till grader: multiplicera med \(\frac{180^\circ}{\pi}\)"
BAGE = r"Båglängden: \(b=rv\), med v i radianer"
SEKT = r"Sektorns area: \(A=\frac{r^2v}{2}\), med v i radianer"


def grad_rad(g, rad, mellan=None):
    m = mellan or rf"\frac{{{g}}}{{180}}\pi"
    return ([(TILL_RAD, rf"{g}^\circ\cdot\frac{{\pi}}{{180^\circ}}={m}={rad}")], rf"\({rad}\)")


def rad_grad(rad, g):
    return ([(TILL_GR, rf"{rad}\cdot\frac{{180^\circ}}{{\pi}}={g}^\circ")], rf"\({g}^\circ\)")


F = {
    '1.46': {
        '': ([('Ett helt varv är \\(2\\pi\\) rad', None, 'Andelen av ett varv gånger \\(2\\pi\\) ger vinkeln i radianer.'),
              ('a) Ett halvt varv', r"\frac12\cdot2\pi=\pi"),
              ('b) Tre fjärdedels varv', r"\frac34\cdot2\pi=\frac{3\pi}{2}"),
              ('c) 2,5 varv', r"2{,}5\cdot2\pi=5\pi")],
             r"a) \(\pi\) rad b) \(\frac{3\pi}{2}\) rad c) \(5\pi\) rad"),
        'a': ([('Ett helt varv är \\(2\\pi\\) rad', r"\frac12\cdot2\pi=\pi")], r"\(\pi\) rad"),
        'b': ([('Ett helt varv är \\(2\\pi\\) rad', r"\frac34\cdot2\pi=\frac{3\pi}{2}")], r"\(\frac{3\pi}{2}\) rad"),
        'c': ([('Ett helt varv är \\(2\\pi\\) rad', r"2{,}5\cdot2\pi=5\pi")], r"\(5\pi\) rad"),
    },
    '1.451': grad_rad(150, r"\frac{5\pi}{6}"),
    '1.452': ([(BAGE, r"v=\frac br"), ('Sätt in båglängden och radien', r"v=\frac{6{,}3}{4{,}5}=1{,}4")], "1,4 rad"),
    '1.83': {
        '': ([(BAGE, r"v=\frac br=\frac{4\pi}{8}=\frac{\pi}{2}"), (TILL_GR, r"\frac{\pi}{2}\cdot\frac{180^\circ}{\pi}=90^\circ")],
             r"a) \(\frac{\pi}{2}\) rad b) \(90^\circ\)"),
        'a': ([(BAGE, r"v=\frac br=\frac{4\pi}{8}=\frac{\pi}{2}")], r"\(\frac{\pi}{2}\) rad"),
        'b': ([(TILL_GR, r"\frac{\pi}{2}\cdot\frac{180^\circ}{\pi}=90^\circ")], r"\(90^\circ\)"),
    },
    '1.454': ([(BAGE, r"r=\frac bv"), ('Sätt in båglängden och vinkeln', r"r=\frac{7{,}2}{1{,}2}=6{,}0")], "6,0 cm"),
    '1.457': rad_grad(r"\frac{3\pi}{4}", 135),
    '1.458': grad_rad(75, r"\frac{5\pi}{12}"),
    '1.461': ([('Ett varv är \\(2\\pi\\) rad', None, 'Antalet varv är vinkeln delad med \\(2\\pi\\).'),
               ('Dela vinkeln med ett helt varv', r"\frac{5\pi}{2\pi}=2{,}5")], "2,5 varv"),
    '1.462': ([(BAGE, r"b=0{,}35\cdot8{,}0=2{,}8")], "2,8 m"),
    '1.463': ([(SEKT, r"A=\frac{6^2\cdot\frac{5\pi}{6}}{2}=\frac{36\cdot5\pi}{12}=15\pi")], r"\(15\pi\) cm²"),
    '1.259': grad_rad(15, r"\frac{\pi}{12}"),
    '1.465': ([(BAGE, r"r=\frac bv"), ('Sätt in båglängden och vinkeln', r"r=\frac{14}{2{,}0}=7{,}0")], "7,0 cm"),
    '1.260': grad_rad(75, r"\frac{5\pi}{12}"),
    '1.466': ([(SEKT, r"18=\frac{6{,}0^2\cdot v}{2}=18v"), ('Lös ut vinkeln', r"v=1{,}0")], "1,0 rad"),
    '1.261': grad_rad(210, r"\frac{7\pi}{6}"),
    '1.262': grad_rad(330, r"\frac{11\pi}{6}"),
    '1.263': {
        '': ([(BAGE, r"v=\frac br=\frac{6\pi}{9}=\frac{2\pi}{3}"), (TILL_GR, r"\frac{2\pi}{3}\cdot\frac{180^\circ}{\pi}=120^\circ")],
             r"a) \(\frac{2\pi}{3}\) rad b) \(120^\circ\)"),
        'a': ([(BAGE, r"v=\frac br=\frac{6\pi}{9}=\frac{2\pi}{3}")], r"\(\frac{2\pi}{3}\) rad"),
        'b': ([(TILL_GR, r"\frac{2\pi}{3}\cdot\frac{180^\circ}{\pi}=120^\circ")], r"\(120^\circ\)"),
    },
    '1.469': ([(SEKT, r"80=\frac{10^2\cdot v}{2}=50v"), ('Lös ut vinkeln', r"v=\frac{80}{50}=1{,}6")], "1,6 rad"),
    '1.280': rad_grad(r"\frac{5\pi}{12}", 75),
    '1.471': ([(BAGE, r"b=0{,}45\cdot\frac{2\pi}{3}=0{,}30\pi")], r"\(0{,}30\pi\) m"),
    '1.592': ([('Ett halvt varv är \\(\\pi\\) rad', r"180^\circ=\pi\text{ rad}")], r"\(\pi\)"),
    '1.593': rad_grad(r"\frac{\pi}{2}", 90),
    '1.594': grad_rad(45, r"\frac{\pi}{4}"),
    '1.595': ([('Ett helt varv är \\(2\\pi\\) rad', r"2\pi\text{ rad}=360^\circ")], r"\(360^\circ\)"),
    '1.596': ([(BAGE, r"b=5\cdot2=10")], "10 cm"),
    '1.597': rad_grad(r"\frac{3\pi}{4}", 135),
    '1.598': ([(SEKT, r"A=\frac{4^2\cdot1}{2}=8")], "8 cm²"),
}
