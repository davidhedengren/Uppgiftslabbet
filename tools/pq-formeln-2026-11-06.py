"""pq-formeln i stället för abc-formeln i alla facit (användarbeslut 2026-11-06).

Läraren: "Vi använder PQ-formeln i alla kurser, inte ABC, ändra det i alla facit".
Varje ändring är handskriven: ekvationen divideras till normalformen x² + px + q = 0 och pq-formeln visas.
Rötterna är desamma som tidigare (kontrollerade numeriskt). "Lösningsformeln" byter namn till "pq-formeln" där
pq-formen redan användes. Logg: agent/PQ_FORMELN_2026-11-06.md

  python tools/pq-formeln-2026-11-06.py [--skriv]             (omgång 1)
  python tools/pq-formeln-2026-11-06.py --omgang2 [--skriv]   (abc-diskriminanten och (b ± √D)/2)
"""
import io, json, os, sys

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PQ = r"\(x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}\)"
ALT_GAMMAL = '<p class="facit-rubrik">Alternativ: lösningsformeln</p>'
ALT_NY = '<p class="facit-rubrik">Alternativ: pq-formeln ' + PQ + '</p>'

# (bank, id eller None för hela filen, före, efter)
BYTEN = [
    # ---------- Fysik 1, konstacc ----------
    ("uppgifter.js", "3.30", ALT_GAMMAL + r'<div class="facit-matte">\[\begin{aligned}t&=\frac{-8{,}0+\sqrt{8{,}0^2+4\cdot4{,}91\cdot22}}{9{,}82}\\&\approx1{,}453\ \mathrm s\end{aligned}\]</div>',
     ALT_NY + r'<p>Dividera med 4,91 så att ekvationen får normalformen.</p><div class="facit-matte">\[\begin{aligned}&4{,}91t^2+8{,}0t-22=0\\&\Leftrightarrow\ t^2+1{,}629t-4{,}481=0\\&\Rightarrow\ t=-0{,}815+\sqrt{0{,}815^2+4{,}481}\\&\approx1{,}453\ \mathrm s\end{aligned}\]</div>'),
    ("uppgifter.js", "3.123", ALT_GAMMAL + r'<div class="facit-matte">\[\begin{aligned}&t=\frac{25\pm\sqrt{25^2-4\cdot4{,}91\cdot20}}{9{,}82}\\',
     ALT_NY + r'<p>Dividera med 4,91 så att ekvationen får normalformen.</p><div class="facit-matte">\[\begin{aligned}&4{,}91t^2-25t+20=0\\&\Leftrightarrow\ t^2-5{,}092t+4{,}073=0\\&\Rightarrow\ t=2{,}546\pm\sqrt{2{,}546^2-4{,}073}\\'),
    ("uppgifter.js", "3.383", ALT_GAMMAL + r'<div class="facit-matte">\[t=\frac{-23+\sqrt{23^2+8\cdot59{,}5}}{4}\approx2{,}18\ \mathrm s\]</div>',
     ALT_NY + r'<p>Dividera med 2 så att ekvationen får normalformen.</p><div class="facit-matte">\[\begin{aligned}&2t^2+23t-59{,}5=0\\&\Leftrightarrow\ t^2+11{,}5t-29{,}75=0\\&\Rightarrow\ t=-5{,}75+\sqrt{5{,}75^2+29{,}75}\\&\approx2{,}18\ \mathrm s\end{aligned}\]</div>'),
    ("uppgifter.js", "3.388", ALT_GAMMAL + r'<div class="facit-matte">\[\begin{aligned}t&=\frac{\begin{gathered}-12{,}91+\\\sqrt{12{,}91^2+4\cdot0{,}2314\cdot85}\end{gathered}}{2\cdot0{,}2314}\\&\approx5{,}95\ \mathrm s\end{aligned}\]</div>',
     ALT_NY + r'<p>Dividera med 0,2314 så att ekvationen får normalformen.</p><div class="facit-matte">\[\begin{aligned}&0{,}2314t^2+12{,}91t-85=0\\&\Leftrightarrow\ t^2+55{,}79t-367{,}3=0\\&\Rightarrow\ t=-27{,}90+\sqrt{27{,}90^2+367{,}3}\\&\approx5{,}95\ \mathrm s\end{aligned}\]</div>'),
    ("uppgifter.js", "3.389", r'<p>Alternativt med lösningsformeln: \(0{,}375t^2+9{,}0t-250=0\) ger \(t\approx16{,}47\) s.</p>',
     r'<p>Alternativt med pq-formeln: \(0{,}375t^2+9{,}0t-250=0\Leftrightarrow t^2+24t-666{,}7=0\) ger \(t=-12+\sqrt{144+666{,}7}\approx16{,}47\) s.</p>'),
    ("uppgifter.js", "3.389", r'<p>Lösningsformeln ger samma rot:', r'<p>pq-formeln ger samma rot:'),
    ("uppgifter.js", "3.389", ALT_GAMMAL + r'<div class="facit-matte">\[\begin{aligned}t&=\frac{31-\sqrt{31^2-4\cdot216}}{2}\\&=\frac{31-\sqrt{97}}{2}\\&\approx10{,}58\ \mathrm s\end{aligned}\]</div>',
     ALT_NY + r'<div class="facit-matte">\[\begin{aligned}&t^2-31t+216=0\\&\Rightarrow\ t=15{,}5-\sqrt{15{,}5^2-216}\\&=15{,}5-\sqrt{24{,}25}\\&\approx10{,}58\ \mathrm s\end{aligned}\]</div>'),
    ("uppgifter.js", "3.391", r'Alternativt med lösningsformeln: \(\tau=\dfrac{18-\sqrt{52}}{4}\approx2{,}70\) s.',
     r'Alternativt med pq-formeln: \(\tau^2-9\tau+17=0\) ger \(\tau=4{,}5-\sqrt{4{,}5^2-17}\approx2{,}70\) s.'),
    ("uppgifter.js", "3.400", ALT_GAMMAL + r'<div class="facit-matte">\[\begin{aligned}t&=\frac{35+\sqrt{35^2+4\cdot4{,}91\cdot7{,}0}}{9{,}82}\\&\approx7{,}32\ \mathrm s\end{aligned}\]</div>',
     ALT_NY + r'<p>Dividera med 4,91 så att ekvationen får normalformen.</p><div class="facit-matte">\[\begin{aligned}&4{,}91t^2-35t-7{,}0=0\\&\Leftrightarrow\ t^2-7{,}128t-1{,}426=0\\&\Rightarrow\ t=3{,}564+\sqrt{3{,}564^2+1{,}426}\\&\approx7{,}32\ \mathrm s\end{aligned}\]</div>'),
    ("uppgifter.js", "3.404", ALT_GAMMAL + r'<div class="facit-matte">\[\begin{aligned}t&=\frac{24+\sqrt{24^2+4\cdot4{,}91\cdot2{,}50}}{9{,}82}\\&\approx4{,}99\ \mathrm s\end{aligned}\]</div>',
     ALT_NY + r'<p>Dividera med 4,91 så att ekvationen får normalformen.</p><div class="facit-matte">\[\begin{aligned}&4{,}91t^2-24t-2{,}50=0\\&\Leftrightarrow\ t^2-4{,}888t-0{,}5092=0\\&\Rightarrow\ t=2{,}444+\sqrt{2{,}444^2+0{,}5092}\\&\approx4{,}99\ \mathrm s\end{aligned}\]</div>'),
    # Fysik 1, coulomb
    ("uppgifter.js", "8.488", r'\[x\approx\frac{25\pm\sqrt{25^2-4\cdot150}}2\]', r'\[x\approx12{,}5\pm\sqrt{12{,}5^2-150}=12{,}5\pm2{,}5\]'),
    ("uppgifter.js", "8.488", r'\[x\approx\frac{25+\sqrt{25^2-4\cdot150}}2\]', r'\[x\approx12{,}5+\sqrt{12{,}5^2-150}=15\]'),
    # Fysik 1: där pq-formen redan användes byter "lösningsformeln" namn
    ("uppgifter.js", None, ALT_GAMMAL, ALT_NY),
    ("uppgifter.js", None, "Lösningsformeln (pq-formeln)", "pq-formeln"),
    # ---------- Fysik 2, kast ----------
    ("uppgifter2.js", "1.25", r'\[t=\frac{11{,}5+\sqrt{11{,}5^2+4\cdot4{,}91\cdot28}}{2\cdot4{,}91}=3{,}831\ \mathrm s\]',
     r'\[t^2-2{,}342t-5{,}703=0\]\[t=1{,}171+\sqrt{1{,}171^2+5{,}703}=3{,}831\ \mathrm s\]'),
    ("uppgifter2.js", "1.113", r'\iff t=\dfrac{20{,}0+\sqrt{20{,}0^2+2\cdot9{,}82\cdot50{,}0}}{9{,}82}',
     r'\iff t^2-4{,}073t-10{,}18=0\iff t=2{,}037+\sqrt{2{,}037^2+10{,}18}'),
    ("uppgifter2.js", "1.115", r'\iff t=\dfrac{-8{,}0+\sqrt{8{,}0^2+2\cdot9{,}82\cdot30{,}0}}{9{,}82}',
     r'\iff t^2+1{,}629t-6{,}110=0\iff t=-0{,}815+\sqrt{0{,}815^2+6{,}110}'),
    ("uppgifter2.js", "1.123", r'\iff t=\dfrac{2{,}50+\sqrt{2{,}50^2+2\cdot9{,}82\cdot3{,}00}}{9{,}82}',
     r'\iff t^2-0{,}5092t-0{,}6110=0\iff t=0{,}2546+\sqrt{0{,}2546^2+0{,}6110}'),
    # ---------- Ma2 ----------
    ("uppgifterma2.js", "2.32", r'<p>Lös med andragradsformeln:</p><p>\[a=\frac{9\pm\sqrt{945}}{16}.\]</p>',
     r'<p>Dividera med 8 och lös med pq-formeln:</p><p>\[a^2-\frac98a-\frac{27}8=0\]</p><p>\[a=\frac9{16}\pm\sqrt{\frac{81}{256}+\frac{864}{256}}=\frac{9\pm\sqrt{945}}{16}.\]</p>'),
    ("uppgifterma2.js", "2.29", r'<p>Den lösning som uppfyller \(a\ge0\) är \(a=\frac{1+\sqrt{65}}8\).</p>',
     r'<p>Dividera med 4 och använd pq-formeln: \(a^2-\frac14a-1=0\Rightarrow a=\frac18\pm\sqrt{\frac1{64}+1}=\frac{1\pm\sqrt{65}}8\).</p></li><li><p>Den lösning som uppfyller \(a\ge0\) är \(a=\frac{1+\sqrt{65}}8\).</p>'),
    ("uppgifterma2.js", "2.70", r'<li><div class="facit-matte">\[x=\frac{3\pm\sqrt{33}}2\].</div></li>',
     r'<li><p>pq-formeln:</p><div class="facit-matte">\[x=\frac32\pm\sqrt{\frac94+6}=\frac{3\pm\sqrt{33}}2\].</div></li>'),
    # ---------- Ma3c (mato1) ----------
    ("uppgiftermato1.js", "1.204", r'<p>Rötterna är</p><p>\[x=\frac{-1\pm\sqrt5}{2}.\]</p>',
     r'<p>pq-formeln ger rötterna</p><p>\[x=-\frac12\pm\sqrt{\frac14+1}=\frac{-1\pm\sqrt5}{2}.\]</p>'),
    ("uppgiftermato1.js", "3.48", r'<p>så</p><p>\[x_1=', r'<p>så pq-formeln ger \(x=-\frac12\pm\sqrt{\frac14+4}\), alltså</p><p>\[x_1='),
    ("uppgiftermato1.js", "3.68", r'<p>ger</p><div class="facit-matte">\[x=(8\pm\sqrt{10})/3\].</div>',
     r'<p>Dividera med 3 och använd pq-formeln:</p><div class="facit-matte">\[x=\frac83\pm\sqrt{\frac{64}9-6}=\frac{8\pm\sqrt{10}}3\].</div>'),
    ("uppgiftermato1.js", "3.294", r'<p>Nollställena är</p><p>\[t=\frac{5\pm\sqrt7}{3}',
     r'<p>Dividera med −3 och använd pq-formeln: \(t^2-\frac{10}3t+2=0\). Nollställena är</p><p>\[t=\frac53\pm\sqrt{\frac{25}9-2}=\frac{5\pm\sqrt7}{3}'),
    ("uppgiftermato1.js", "2.16", r'<p>Lös med lösningsformeln för andragradsekvationer eller kvadratkomplettering:</p></li><li><p>\[t=\frac{1\pm \sqrt{21}}{2}.\]</p>',
     r'<p>Lös med pq-formeln:</p></li><li><p>\[t=\frac12\pm\sqrt{\frac14+5}=\frac{1\pm \sqrt{21}}{2}.\]</p>'),
    ("uppgiftermato1.js", None, "lösningsformeln för andragradsekvationer", "pq-formeln"),
    ("uppgiftermato1.js", None, "Lösningsformeln för andragradsekvationer", "pq-formeln"),
    # ---------- Ma4 (mato2) ----------
    ("uppgiftermato2.js", "2.268", r'<p>Det ger x=2 samt</p>\[x=\frac{4\pm\sqrt7}{3}.\]',
     r'<p>Det ger x=2 samt, med pq-formeln efter division med 3,</p>\[x=\frac43\pm\sqrt{\frac{16}9-1}=\frac{4\pm\sqrt7}{3}.\]'),
    ("uppgiftermato2.js", "3.79", r'<p>Den lösning som ligger i intervallet är</p></li><li><p>\[b=\frac{9-\sqrt{21}}{2}.\]',
     r'<p>pq-formeln ger \(b=\frac92\pm\sqrt{\frac{81}4-15}=\frac{9\pm\sqrt{21}}2\). Den lösning som ligger i intervallet är</p></li><li><p>\[b=\frac{9-\sqrt{21}}{2}.\]'),
    ("uppgiftermato2.js", "4.78", r'<p>pq-/kvadratisk formel ger</p></li><li><p>\[x=\frac{6\pm\sqrt{96}}{10}=\frac{3\pm2\sqrt6}{5}.\]',
     r'<p>Dividera med 5 och använd pq-formeln: \(x^2-\frac65x-\frac35=0\).</p></li><li><p>\[x=\frac35\pm\sqrt{\frac9{25}+\frac{15}{25}}=\frac{3\pm\sqrt{24}}5=\frac{3\pm2\sqrt6}{5}.\]'),
    ("uppgiftermato2.js", "4.124", r'<p>\[2x^2-2x-9=0.\]</p></li><li><p>\[x=\frac{1\pm\sqrt{19}}2.\]</p>',
     r'<p>\[2x^2-2x-9=0.\]</p></li><li><p>Dividera med 2 och använd pq-formeln:</p><p>\[x=\frac12\pm\sqrt{\frac14+\frac92}=\frac{1\pm\sqrt{19}}2.\]</p>'),
    ("uppgiftermato2.js", "4.402", r'\[x=\frac{4\pm\sqrt{16-52}}2=2\pm3i\]', r'\[x^2-4x+13=0\Rightarrow x=2\pm\sqrt{4-13}=2\pm\sqrt{-9}=2\pm3i\]'),
    ("uppgiftermato2.js", "3.466", "Kan uttrycket faktoriseras, eller passar pq-formeln eller lösningsformeln bättre?", "Kan uttrycket faktoriseras, eller passar pq-formeln bättre?"),
    # ---------- Ma5 (matf1) ----------
    ("uppgiftermatf1.js", "2.152", r'<p>Lösningarna är</p></li><li><p>\[b=\frac{-4\pm\sqrt{16+468}}{2}=\frac{-4\pm22}{2},\]</p>',
     r'<p>pq-formeln ger</p></li><li><p>\[b=-2\pm\sqrt{4+117}=-2\pm11,\]</p>'),
    ("uppgiftermatf1.js", "2.602", r'n=\dfrac{-9+\sqrt{81+1\,600}}{2}=16', r'n=-4{,}5+\sqrt{20{,}25+400}=-4{,}5+20{,}5=16'),
]


# Omgång 2: abc-diskriminanten ("uttrycket under rottecknet i andragradsformeln") och formen (b ± √D)/2
BYTEN2 = [
    ("uppgiftermato1.js", "1.248", r'Kontroll med andragradsformeln: uttrycket under rottecknet blir noll när \(k^2-36=0\)',
     r'Kontroll med pq-formeln, \(x=-\frac k2\pm\sqrt{\frac{k^2}4-9}\): uttrycket under rottecknet blir noll när \(\frac{k^2}4-9=0\), det vill säga \(k^2=36\)'),
    ("uppgiftermato1.js", "2.369", r'Kritiska punkter är \(x=(4\pm\sqrt{13})/3\)',
     r'Dividera med 3 och använd pq-formeln: \(x=\frac43\pm\sqrt{\frac{16}9-\frac13}\). Kritiska punkter är \(x=(4\pm\sqrt{13})/3\)'),
    ("uppgiftermato2.js", "2.01", '<li><p>Uttrycket under rottecknet i andragradsformeln är</p></li><li><p>\\[\n\\Delta=(2a)^2-4\\cdot3\\cdot3\n=4a^2-36.\n\\]</p></li><li><p>Villkoret blir</p></li><li><p>\\[\n\\Delta\\le0\n\\Rightarrow\n4a^2\\le36\n\\Rightarrow\na^2\\le9.\n\\]</p></li>',
     r'<li><p>Dividera med 3 och använd pq-formeln: \(x^2+\frac{2a}3x+1=0\Rightarrow x=-\frac a3\pm\sqrt{\frac{a^2}9-1}\).</p></li><li><p>Uttrycket under rottecknet får inte vara positivt:</p></li><li><p>\[\frac{a^2}9-1\le0\Rightarrow a^2\le9.\]</p></li>'),
    ("uppgiftermato2.js", "2.39", r'<li><p>Uttrycket under rottecknet i andragradsformeln ska därför vara \(\le0\):</p></li><li><p>\[(2a)^2-4\cdot3\cdot3\le0\Rightarrow4a^2-36\le0\Rightarrow a^2\le9.\]</p></li>',
     r'<li><p>Dividera med 3 och använd pq-formeln: \(x=-\frac a3\pm\sqrt{\frac{a^2}9-1}\). Uttrycket under rottecknet ska därför vara \(\le0\):</p></li><li><p>\[\frac{a^2}9-1\le0\Rightarrow a^2\le9.\]</p></li>'),
    ("uppgiftermato2.js", "2.226", r'<li><p>För att sakna två olika reella nollställen ska uttrycket under rottecknet i andragradsformeln vara \(\le0\):</p></li><li><p>\[(2a)^2-36\le0\Rightarrow a^2\le9.\]</p></li>',
     r'<li><p>Dividera med 3 och använd pq-formeln: \(x=-\frac a3\pm\sqrt{\frac{a^2}9-1}\). För att sakna två olika reella nollställen ska uttrycket under rottecknet vara \(\le0\):</p></li><li><p>\[\frac{a^2}9-1\le0\Rightarrow a^2\le9.\]</p></li>'),
    ("uppgiftermato2.js", "4.25", r'<li><p>Det händer när uttrycket under rottecknet i andragradsformeln är noll:</p></li><li><p>\[a^2-4=0\Rightarrow a=\pm2.\]</p></li>',
     r'<li><p>pq-formeln ger \(w=-\frac a2\pm\sqrt{\frac{a^2}4-1}\). Dubbelrot fås när uttrycket under rottecknet är noll:</p></li><li><p>\[\frac{a^2}4-1=0\Rightarrow a=\pm2.\]</p></li>'),
    ("uppgiftermato2.js", "4.74", r'<p>Uttrycket under rottecknet i andragradsformeln är</p><div class="facit-matte">\[36-52=-16\].</div></div></li><li><p>Därför</p></li><li><p>\[x=\frac{-6\pm4i}{2}=\boxed{-3\pm2i}.\]</p></li>',
     r'<p>pq-formeln med \(p=6\) och \(q=13\):</p><div class="facit-matte">\[x=-3\pm\sqrt{9-13}=-3\pm\sqrt{-4}\].</div></div></li><li><p>Därför</p></li><li><p>\[x=\boxed{-3\pm2i}.\]</p></li>'),
    ("uppgiftermato2.js", "4.143", r'När uttrycket under rottecknet i andragradsformeln är negativ, skriv \(\sqrt{-k}=i\sqrt{k}\) och fortsätt med den vanliga andragradsformeln.',
     r'När uttrycket under rottecknet i pq-formeln är negativt, skriv \(\sqrt{-k}=i\sqrt{k}\) och räkna vidare som vanligt.'),
    ("uppgiftermato2.js", "4.143", r'<p>Uttrycket under rottecknet i andragradsformeln är</p><div class="facit-matte">\[16-52=-36\].</div></div></li><li><p>Därför</p></li><li><p>\[x=\frac{4\pm6i}{2}=2\pm3i.\]</p></li>',
     r'<p>pq-formeln med \(p=-4\) och \(q=13\):</p><div class="facit-matte">\[x=2\pm\sqrt{4-13}=2\pm\sqrt{-9}\].</div></div></li><li><p>Därför</p></li><li><p>\[x=2\pm3i.\]</p></li>'),
    ("uppgiftermato2.js", "4.144", "Använd andragradsformeln som vanligt.", "Använd pq-formeln som vanligt."),
    ("uppgiftermato2.js", "4.144", r'z=(6\pm\sqrt{-16})/2=\boxed{3\pm2i}', r'z=3\pm\sqrt{9-13}=3\pm\sqrt{-4}=\boxed{3\pm2i}'),
    ("uppgiftermato2.js", "4.144", r'z=(-4\pm\sqrt{-16})/2=\boxed{-2\pm2i}', r'z=-2\pm\sqrt{4-8}=-2\pm\sqrt{-4}=\boxed{-2\pm2i}'),
    ("uppgiftermato2.js", "4.145", r'x=(4\pm\sqrt{-36})/2=\boxed{2\pm3i}', r'x=2\pm\sqrt{4-13}=2\pm\sqrt{-9}=\boxed{2\pm3i}'),
    ("uppgiftermato2.js", "4.145", r'x=(-6\pm\sqrt{-64})/2=\boxed{-3\pm4i}', r'x=-3\pm\sqrt{9-25}=-3\pm\sqrt{-16}=\boxed{-3\pm4i}'),
    ("uppgiftermato2.js", "3.224", r'så \(x=(-1\pm\sqrt{17})/2\)', r'så pq-formeln ger \(x=-\frac12\pm\sqrt{\frac14+4}=(-1\pm\sqrt{17})/2\)'),
]


def esc(t):
    return json.dumps(t, ensure_ascii=False)[1:-1]


def spann(src):
    dec, ut, i = json.JSONDecoder(), {}, src.index('[') + 1
    while True:
        while src[i] in ' \t\r\n,':
            i += 1
        if src[i] == ']':
            return ut
        obj, slut = dec.raw_decode(src, i)
        ut[obj['id']] = (i, slut)
        i = slut


def main():
    banker = {}
    for bank, id_, fore, efter in (BYTEN2 if '--omgang2' in sys.argv else BYTEN):
        if bank not in banker:
            banker[bank] = io.open(os.path.join(ROT, bank), encoding='utf-8', newline='').read()
        src = banker[bank]
        f, e = esc(fore), esc(efter)
        if id_ is None:
            n = src.count(f)
            print(f'{bank} hela filen: {n} × {fore[:50]!r}')
            src = src.replace(f, e)
        else:
            s, slut = spann(src)[id_]
            del_ = src[s:slut]
            n = del_.count(f)
            assert n >= 1, (bank, id_, fore[:80])
            src = src[:s] + del_.replace(f, e) + src[slut:]
            print(f'{bank} {id_}: {n} ersättning(ar)')
        json.loads(src[src.index('['):src.rindex(']') + 1])
        banker[bank] = src
    if '--skriv' in sys.argv:
        for bank, src in banker.items():
            io.open(os.path.join(ROT, bank), 'w', encoding='utf-8', newline='').write(src)
        print('skrivet')


if __name__ == '__main__':
    main()
