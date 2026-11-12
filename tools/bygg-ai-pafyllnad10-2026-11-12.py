"""AI-banken 2026-11-12, omgång 10: alfa–beta på C-nivå och BFS på A-nivå.

Efter granskningen 2026-11-12 var alfa–beta på C-nivå och BFS på A-nivå de svagaste delarna
för prov. Användaren: ”fyll på där”.

- Alfa–beta, C (beskärning med stöd enligt AI_NIVAINDELNING.md: givna mellanvärden, ett
  beslut i taget):
  - 3.73–3.75: tre barn under roten. Behöver B:s andra löv undersökas? Behöver C:s andra löv
    undersökas? Svaren varierar mellan ja och nej.
  - 3.76–3.77: träd med 12 löv. A:s värde och rotvärdet (C enligt regeln om minst 12 löv) och
    hur många av B:s löv som behöver undersökas när A är känd.
  - 3.78: ordningen mellan B:s löv och hur många som behöver undersökas.
- BFS, A (generalisera och värdera):
  - 1.104: BFS hittar färst steg men inte nödvändigtvis den billigaste vägen.
  - 1.105: antal uttag i ett öppet rutnät med start och mål i motsatta hörn (R · C).
  - 1.106: antal rutor på avstånd k från ett hörn i ett öppet rutnät (k + 1).

Svaren kontrolleras oberoende i tools/ai-pafyllnad10-2026-11-12.test.js.
Kör efter bygg-ai-pafyllnad9-2026-11-12.py.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _load(name, fil):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fil))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = _load('ai_kg', 'bygg-ai-kunskapsgymmet-2026-11-11.py')
P6 = _load('ai_p6', 'bygg-ai-pafyllnad6-2026-11-11.py')
P7 = _load('ai_p7', 'bygg-ai-pafyllnad7-2026-11-11.py')
from ai_figurer import step, maze  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, num, val, lista, pil, names = K.p, K.alt, K.num, K.val, K.lista, K.pil, K.names
uppgift = P7.uppgift
BANK = 'uppgifterai.js'


def janej(ja, kommentar_ja, kommentar_nej):
    return [alt('Ja', ja, kommentar_ja), alt('Nej', not ja, kommentar_nej)]


# ======================================================================== alfa–beta med stöd, tre barn

TRE = [
    ('3.73', [[4, 7], [2, 9], [6, 5]], True, 'Två spelare turas om i ett enkelt brädspel. Talen i löven är MAX:s poäng.'),
    ('3.74', [[3, 8], [5, 6], [2, 9]], True, 'En spelagent i ett kortspel har räknat fram talen i löven.'),
    ('3.75', [[6, 2], [8, 1], [4, 5]], False, 'I ett strategispel är talen i löven MAX:s poäng, och MIN börjar.'),
]


def tre_barn(id_, vals, root_max, sammanhang):
    r = T.build(vals, root_max)
    v, ev, cuts, notes = T.alphabeta(r)
    beskurna = T.pruned_leaves(cuts)
    ro, bn = ('MAX', 'MIN') if root_max else ('MIN', 'MAX')
    bast = max if root_max else min
    va = T.minimax(r['kids'][0])
    b1, c1 = vals[1][0], vals[2][0]
    # B: MIN-nod (rot MAX) blir högst b1; MAX-nod (rot MIN) blir minst b1.
    b_kap = b1 <= va if root_max else b1 >= va
    assert b_kap == ('L4' in beskurna)
    vb = T.minimax(r['kids'][1])
    hittills = va if b_kap else bast(va, vb)
    c_kap = c1 <= hittills if root_max else c1 >= hittills
    assert c_kap == ('L6' in beskurna)
    gr, sämre = ('högst', 'mindre') if root_max else ('minst', 'större')
    intro = (P6.fig(vals, root_max, f'Spelträd med {ro} i roten och {bn}-noderna A, B och C. Löven heter L1–L6.')
             + p(sammanhang) + P6.AB)
    op = 'min' if root_max else 'max'
    a = num('Vilket värde får A?', [step(f'A är en {bn}-nod', f'A = {op}({vals[0][0]}, {vals[0][1]}) = {va}.')], va,
            f'Väljer {bn} största eller minsta värdet?', 1)
    b = val(f'A har värdet {va}. B:s första löv är L3 = {b1}. Behöver lövet L4 undersökas?',
            [step(f'B är en {bn}-nod: B blir {gr} {b1}', f'{bn} väljer {b1} eller något {sämre}.'),
             step(f'Jämför med A = {va}', (f'B kan inte bli bättre för {ro} än A, så L4 behövs inte.' if b_kap else
                                           f'B kan fortfarande bli bättre för {ro} än A, så L4 måste undersökas.'))],
            janej(not b_kap,
                  f'B kan fortfarande bli bättre för {ro} än A = {va}, beroende på L4.' if not b_kap else
                  f'B blir {gr} {b1}, och det kan aldrig slå A = {va} för {ro}.',
                  f'B blir {gr} {b1}, så B kan inte bli bättre för {ro} än A = {va}.' if b_kap else
                  f'{b1} är bättre för {ro} än A = {va}, så B kan fortfarande vinna. L4 behövs.'),
            f'Vad är det bästa B kan ge {ro}, och är det bättre än A?', 3)
    b_info = 'B beskärs efter L3 och ger inget bättre än A' if b_kap else f'B får värdet {vb}'
    c = val(f'{b_info}. Sökningen kommer till C och utvärderar L5 = {c1}. Behöver lövet L6 undersökas?',
            [step(f'Det bästa {ro} har hittills', f'Bästa av A och B för {ro}: {hittills}.'),
             step(f'C blir {gr} {c1}', (f'C kan inte bli bättre än {hittills}, så L6 behövs inte.' if c_kap else
                                       f'C kan fortfarande bli bättre än {hittills}, så L6 måste undersökas.'))],
            janej(not c_kap,
                  f'C kan bli bättre för {ro} än {hittills}, beroende på L6.' if not c_kap else
                  f'C blir {gr} {c1}, och det slår inte {hittills} för {ro}.',
                  f'C blir {gr} {c1}, och {ro} har redan {hittills}.' if c_kap else
                  f'{c1} är bättre för {ro} än {hittills}, så C kan fortfarande vinna.'),
            f'Jämför det bästa C kan ge med det bästa {ro} redan har.', 3)
    d = num('Vilket värde får roten?',
            [step('Barnens värden med minimax', ', '.join(f'{k["name"]} = {T.minimax(k)}' for k in r['kids']) + '.'),
             step(f'{ro} i roten', f'Roten får {v}.')], v, f'{ro} väljer det {"största" if root_max else "minsta"} värdet.', 1)
    return uppgift(id_, 'alfa_beta', 'Beskärningens idé', intro, [a, b, c, d],
                   'En nod kan hoppas över när den inte kan bli bättre än det bästa roten redan har.', ['procedur', 'resonemang'])


# ======================================================================== tolv löv

TOLV = [
    ('3.76', [[5, 8, 6, 9], [7, 3, 8, 4], [9, 6, 7, 10]], True, 'En dator spelar fyra i rad och har räknat fram talen i löven.'),
    ('3.77', [[2, 6, 4, 3], [5, 1, 9, 2], [4, 8, 3, 7]], False, 'I ett spel för två robotar är talen i löven MAX:s poäng, och MIN börjar.'),
]


def tolv_lov(id_, vals, root_max, sammanhang):
    r = T.build(vals, root_max)
    v, ev, cuts, notes = T.alphabeta(r)
    assert len(T.leaves(r)) == 12
    ro, bn = ('MAX', 'MIN') if root_max else ('MIN', 'MAX')
    va = T.minimax(r['kids'][0])
    blov = [f'L{i}' for i in range(5, 9)]
    b_und = [x for x in ev if x in blov]
    # Oberoende kontroll: B:s löv undersöks tills ett blir minst lika bra för roten som A.
    n = next((i + 1 for i, x in enumerate(vals[1]) if (x <= va if root_max else x >= va)), 4)
    assert n == len(b_und)
    gr = 'högst' if root_max else 'minst'
    op = 'min' if root_max else 'max'
    intro = (P6.fig(vals, root_max, f'Spelträd med {ro} i roten, {bn}-noderna A, B och C och tolv löv, L1–L12.', spacing=50)
             + p(sammanhang) + P6.AB)
    a = num('Vilket värde får A?', [step(f'A är en {bn}-nod', f'A = {op}({", ".join(map(str, vals[0]))}) = {va}.')], va,
            f'{bn} väljer det {"minsta" if root_max else "största"} av A:s fyra löv.', 3)
    stegen = []
    for i, x in enumerate(vals[1][:n]):
        stegen.append(f'L{5 + i} = {x}' + (f': B blir {gr} {x}, inte bättre för {ro} än A = {va}. Resten hoppas över.' if i == n - 1 and n < 4 else '.'))
    b = num(f'A har värdet {va}. Hur många av B:s fyra löv behöver undersökas?',
            [step('Undersök B:s löv från vänster', ' '.join(stegen)), step(f'{n} av B:s 4 löv undersöks', f'De övriga {4 - n} hoppas över.')], n,
            f'Sluta när B inte längre kan bli bättre för {ro} än A.', 3)
    barn = [T.minimax(k) for k in r['kids']]
    c = num('Vilket värde får roten?',
            [step('Barnens värden med minimax', ', '.join(f'{k["name"]} = {x}' for k, x in zip(r['kids'], barn)) + '.'),
             step(f'{ro} i roten', f'Roten får {v}. Alfa–beta ger samma värde som minimax.')], v,
            'Bestäm varje barns värde och välj sedan som roten.', 3)
    return uppgift(id_, 'alfa_beta', 'Rotvärde och beskurna löv', intro, [a, b, c],
                   'Undersök barnen från vänster och jämför med det bästa roten redan har.', ['procedur'])


def t378():
    vals_bild = [[6, 5], [9, 7, 4, 8]]
    vals_bra = [[6, 5], [4, 9, 7, 8]]
    va = 5
    n_bild = next(i + 1 for i, x in enumerate(vals_bild[1]) if x <= va)
    n_bra = next(i + 1 for i, x in enumerate(vals_bra[1]) if x <= va)
    for vals, n in ((vals_bild, n_bild), (vals_bra, n_bra)):
        v, ev, cuts, _ = T.alphabeta(T.build(vals, True))
        assert len([x for x in ev if x in ('L3', 'L4', 'L5', 'L6')]) == n
    assert (n_bild, n_bra) == (3, 1)
    intro = (P6.fig(vals_bild, True, 'Spelträd med MAX i roten och MIN-noderna A och B. A har två löv, B har fyra. Löven heter L1–L6.')
             + p('I ett spel för två är talen i löven MAX:s poäng.') + P6.AB)
    a = num('A får värdet 5. Hur många av B:s fyra löv behöver undersökas i ordningen i bilden?',
            [step('B:s löv från vänster', 'L3 = 9 och L4 = 7 är större än 5. L5 = 4: nu blir B högst 4, sämre än A.'),
             step('Tre löv undersöks, L6 hoppas över', 'Efter L5 kan B inte längre slå A.')], n_bild, 'Sluta när B blir högst lika med A.', 3)
    b = num('Samma fyra löv under B undersöks i stället i ordningen 4, 9, 7, 8. Hur många behöver undersökas nu?',
            [step('Första lövet räcker', 'Med 4 först blir B högst 4 direkt, sämre än A = 5. Resten hoppas över.')], n_bra,
            'Vad händer om det lägsta värdet kommer först?', 3)
    c = val('Vilken ordning ger flest beskurna löv i en MIN-nod som ligger under en MAX-rot?',
            [step('MIN vill ha låga värden', 'Ett lågt värde tidigt visar direkt att noden inte kan slå det roten redan har.')],
            [alt('De lägsta värdena undersöks först', True, 'Då syns det tidigt att MIN-noden blir låg, och resten kan hoppas över.'),
             alt('De högsta värdena undersöks först', False, 'Höga värden säger inget om att MIN-noden blir låg, så inget kan hoppas över.'),
             alt('Ordningen spelar ingen roll', False, 'I bilden behövdes tre löv, med 4 först bara ett.'),
             alt('Löven längst till höger undersöks först', False, 'Placeringen spelar ingen roll i sig, bara vilka värden som kommer tidigt.')],
            'Jämför svaren i a och b.', 3)
    return uppgift('3.78', 'alfa_beta', 'Beskärningens idé', intro, [a, b, c], 'Ordningen avgör hur tidigt en gren kan avbrytas.',
                   ['procedur', 'resonemang'])


# ======================================================================== BFS på A-nivå

M1104 = ['S3..', '.3#.', '...G']


def t1104():
    s, g = A.parse(M1104)
    bv = A.bfs(M1104)['path']
    bk = A.path_cost(M1104, bv)
    kost, billig = A.ucs_grid(M1104)
    assert len(bv) - 1 == 5 and bk > kost
    intro = (maze(M1104, s, g) + p('Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←). Att gå in i en lerruta (3) kostar 3 och att '
                                     'gå in i en vit ruta eller målet kostar 1. BFS bryr sig inte om kostnaden, bara om antalet steg.'))
    a = num('Vad kostar vägen som BFS hittar?',
            [step('BFS-vägen', pil(names(bv)) + '.'),
             step(f'BFS-vägen kostar {bk}', ' + '.join(str(A.cost(M1104, c)) for c in bv[1:]) + f' = {bk}.')], bk,
            'Hitta vägen BFS returnerar och lägg ihop kostnaden för rutorna.', 2)
    b = num('Vad kostar den billigaste vägen?',
            [step('En väg runt leran', pil(names(billig)) + '.'), step(f'Den billigaste vägen kostar {kost}', 'Den har lika många steg men går inte genom någon lerruta.')], kost,
            'Finns det en väg utan lerrutor?', 2)
    c = val('Vilket påstående om BFS stämmer i alla labyrinter, inte bara den här?',
            [step('BFS räknar steg', 'BFS hittar alltid en väg med färst steg, men tittar inte på vad rutorna kostar.'),
             step('Färst steg är inte alltid billigast', 'När alla steg kostar lika mycket är BFS-vägen också billigast. Annars kan en annan väg vara billigare.')],
            [alt('BFS hittar en väg med färst steg, men den behöver inte vara billigast när rutorna kostar olika', True,
                 f'Här kostar BFS-vägen {bk}, men den billigaste vägen bara {kost}.'),
             alt('BFS hittar alltid den billigaste vägen', False, f'Här är BFS-vägen dyrare: {bk} mot {kost}.'),
             alt('BFS hittar aldrig den billigaste vägen', False, 'När alla rutor kostar 1 är BFS-vägen också billigast.'),
             alt('BFS hittar alltid en väg som undviker terräng', False, 'BFS ser inte terrängen. Den går gärna genom lera om vägen blir kortare.')],
            'Vad är det BFS räknar, och vad räknar den inte?', 4)
    return uppgift('1.104', 'bfs', 'BFS i labyrinter', intro, [a, b, c], 'BFS hittar färst steg, inte lägst kostnad.', ['procedur', 'resonemang'])


def oppet(R, C):
    rows = [['.'] * C for _ in range(R)]
    rows[0][0], rows[R - 1][C - 1] = 'S', 'G'
    return [''.join(r) for r in rows]


def t1105():
    n34, n56 = len(A.bfs(oppet(3, 4))['order']), len(A.bfs(oppet(5, 6))['order'])
    assert (n34, n56) == (12, 30)
    for R in range(2, 7):
        for C in range(2, 7):
            assert len(A.bfs(oppet(R, C))['order']) == R * C
    M = oppet(3, 4)
    s, g = A.parse(M)
    intro = maze(M, s, g) + p('Rutnätet saknar väggar. Start ligger i ett hörn och målet i det motsatta hörnet. '
                              'Rutnätet söks igenom med BFS (ordning ↑ → ↓ ←).')
    a = num('Hur många rutor tar BFS ut, inklusive start och mål, i rutnätet i bilden?',
            [step('Målet ligger längst bort', 'Målet är den enda rutan på avstånd 5 från start. Alla rutor på avstånd 0–4 tas ut först.'),
             step(f'Alla 3 · 4 = {n34} rutor tas ut', 'Målet tas ut sist.')], n34, 'Vilka rutor ligger närmare start än målet?', 3)
    b = num('Ett likadant rutnät har 5 rader och 6 kolumner. Hur många rutor tar BFS ut där?',
            [step('Samma resonemang', 'Målet är ensamt längst bort, så alla andra rutor tas ut före målet.'),
             step(f'Alla 5 · 6 = {n56} rutor tas ut', 'Målet tas ut sist.')], n56, 'Gäller samma resonemang som i bilden?', 3)
    c = val('Vilken formel ger antalet rutor som BFS tar ut i ett öppet rutnät med R rader och C kolumner, när start och mål ligger i motsatta hörn?',
            [step('Målet ligger ensamt längst bort, på avståndet R + C − 2', 'Alla andra rutor ligger närmare start och tas ut före målet.'),
             step('Därför tas alla R · C rutor ut', 'Det stämmer med 12 i bilden och 30 i b.')],
            [alt('R · C', True, 'Alla rutor tas ut, eftersom målet ligger ensamt längst bort.'),
             alt('R + C − 2', False, 'Det är antalet steg i den kortaste vägen, inte antalet uttag.'),
             alt('R + C − 1', False, 'Det är antalet rutor på en kortaste väg. BFS tar ut många fler.'),
             alt('(R − 1) · (C − 1)', False, 'Pröva med bilden: 2 · 3 = 6, men BFS tar ut 12 rutor.')],
            'Kontrollera din formel mot svaren i a och b.', 4)
    return uppgift('1.105', 'bfs', 'BFS i labyrinter', intro, [a, b, c], 'BFS tar ut alla rutor som ligger närmare start än målet.',
                   ['procedur', 'resonemang'])


def t1106():
    M = oppet(6, 6)
    s, _ = A.parse(M)
    d = A.dist_all(M, s)
    antal = {k: sum(1 for v in d.values() if v == k) for k in range(11)}
    assert antal[3] == 4 and antal[5] == 6 and all(antal[k] == k + 1 for k in range(6))
    intro = maze(M, s, (5, 5)) + p('Rutnätet har 6 rader och 6 kolumner och saknar väggar. BFS startar i det övre vänstra hörnet '
                                   'och tar ut rutorna i ordning efter avstånd från start.')
    a = num('Hur många rutor ligger exakt 3 steg från start?',
            [step('Rutorna på avstånd 3 ligger på en diagonal', 'A4, B3, C2 och D1.'), step('4 rutor ligger 3 steg från start', 'En ruta i varje rad A–D.')], antal[3],
            'Ett steg nedåt eller åt höger ökar avståndet med 1.', 3)
    b = num('Hur många rutor ligger exakt 5 steg från start?',
            [step('Rutorna på avstånd 5 ligger på en diagonal', 'A6, B5, C4, D3, E2 och F1.'), step('6 rutor ligger 5 steg från start', 'En ruta i varje rad A–F.')], antal[5],
            'Rutorna på samma avstånd ligger på en diagonal.', 3)
    c = val('Hur många rutor ligger på avståndet k från hörnet, så länge k är högst 5?',
            [step('Avstånd k är en diagonal', 'Rutorna på avstånd k är de där radnumret och kolumnnumret har samma summa.'),
             step('Mönstret är k + 1', 'Avstånd 0: 1 ruta, avstånd 1: 2, avstånd 3: 4 och avstånd 5: 6.')],
            [alt('k + 1', True, 'Diagonalen på avstånd k har k + 1 rutor så länge den får plats i rutnätet.'),
             alt('2k', False, 'Pröva med k = 3: 2 · 3 = 6, men det finns bara 4 rutor på avstånd 3.'),
             alt('k', False, 'Pröva med k = 0: start ligger på avstånd 0, och det är 1 ruta.'),
             alt('k²', False, 'Antalet växer med en ruta per steg, inte i kvadrat.')],
            'Kontrollera din formel mot svaren i a och b.', 4)
    return uppgift('1.106', 'bfs', 'BFS i labyrinter', intro, [a, b, c], 'Rutorna på samma avstånd ligger på en diagonal.',
                   ['procedur', 'resonemang'])


NYA = [lambda x=x: tre_barn(*x) for x in TRE] + [lambda x=x: tolv_lov(*x) for x in TOLV] + [t378, t1104, t1105, t1106]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    for f in NYA:
        u = f()
        for d in u['spelDelar']:
            for x in d.get('alternativ', []):
                assert len(x['kommentar']) > 15, (u['id'], x)
        old = next((k for k, x in enumerate(bank) if x['id'] == u['id']), None)
        if old is None:
            bank.append(u)
        else:
            bank[old] = u
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(NYA)} uppgifter inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
