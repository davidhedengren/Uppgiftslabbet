"""AI-banken 2026-11-11, tionde omgången: de minsta delmomenten i informerad sökning.

Efter omgrupperingen hade ”Heuristiken h” 6 uppgifter och de två delmomenten om
prioritetsköer 7 var. Tio nya uppgifter (2.78–2.87), med olika sammanhang: karta med
fågelvägen, labyrint, robot utan karta, läxlista, spelserver (högst värde först), öppna
listan och små grafer där girig bäst först och A* väljer olika.

Alla svar räknas fram här (A* och girig bäst först med tools/ai_sokalgoritmer.py) och
kontrolleras oberoende i tools/ai-pafyllnad8-2026-11-11.test.js. Uppgiftstexten `t` är
skriven för papper, och alternativ är aldrig ett ensamt nodnamn (”Noden B”).

Kör efter bygg-ai-pafyllnad7-2026-11-11.py och före bygg-ai-omgruppering-2026-11-11.py.
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
P7 = _load('ai_p7', 'bygg-ai-pafyllnad7-2026-11-11.py')
from ai_figurer import step, maze, weighted_graph, tab  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402

p, alt, num, val, lista, pil = K.p, K.alt, K.num, K.val, K.lista, K.pil
lst, uppgift = P7.lst, P7.uppgift
BANK = 'uppgifterai.js'
MARK = [('#fff3b0', 'Markerad ruta')]
H_FAM, UT_FAM, AS_FAM = 'Heuristiken h', 'Uttag ur en prioritetskö', 'Prioritetskön i girig bäst först och A*'
NO = 'Skriv noderna i ordning, åtskilda med kommatecken.'


def prio(ops, hogst=False):
    """ops: (namn, värde) läggs in, None tar ut. Lika värden: bokstavsordning."""
    q, out = [], []
    for op in ops:
        if op:
            q.append(op)
        else:
            q.sort(key=lambda x: ((-x[1]) if hogst else x[1], x[0]))
            out.append(q.pop(0))
    return out, q


# ======================================================================== Heuristiken h

G278 = [('S', 'A', 4), ('S', 'B', 3), ('A', 'M', 5), ('B', 'C', 4), ('C', 'M', 3), ('A', 'C', 2)]
H278 = {'S': 7, 'A': 4, 'B': 6, 'C': 3, 'M': 0}
P278 = {'S': (50, 140), 'A': (190, 55), 'B': (170, 225), 'C': (320, 190), 'M': (440, 80)}


def t278():
    verklig = {n: A.astar_graph(G278, {k: 0 for k in H278}, n, 'M')['cost'] for n in H278}
    assert verklig == {'S': 9, 'A': 5, 'B': 7, 'C': 3, 'M': 0}
    assert all(H278[n] <= verklig[n] for n in H278)
    intro = (weighted_graph(P278, G278, 'S', 'M', 'Karta med orterna S, A, B, C och M. Vägar med längd: S–A 4, S–B 3, A–M 5, '
                            'B–C 4, C–M 3 och A–C 2. Fågelvägen till M: S 7, A 4, B 6, C 3.', 490, h=H278)
             + p('Kartan visar vägar mellan orter, med vägens längd i mil. Talet h vid varje ort är fågelvägen därifrån '
                 'till målet M. En sökning använder fågelvägen som heuristik.'))
    a = val('Vilken av grannarna till S ligger närmast M enligt h?',
            [step('S:s grannar', 'S har vägar till A och B. A har h = 4 och B har h = 6.')],
            [alt('Orten A', True, 'A har lägre h än B, 4 mot 6.'), alt('Orten B', False, 'B har h = 6, högre än A:s 4.'),
             alt('Orten C', False, 'C har lägst h, men C är inte granne med S.'), alt('Orten M', False, 'M är målet och inte granne med S.')],
            'Jämför h för de orter som S har en väg till.', 1)
    b = num('Den kortaste vägen från A till M är 5 mil. Hur många mil kortare än den vägen är fågelvägen från A?',
            [step('Jämför', f'Fågelvägen h = 4 och vägen 5. Skillnaden är 5 − 4 = 1.')], 1,
            'Läs av h vid A.', 1)
    c = val('Vad beskriver talet h vid orten A?',
            [step('h är en uppskattning', 'h säger ungefär hur långt det är kvar från A till M. Den räknar inte med hur vägarna går.')],
            [alt('En uppskattning av hur långt det är kvar från A till M', True, 'Fågelvägen är en uppskattning av avståndet kvar.'),
             alt('Hur långt det är från S till A', False, 'Sträckan från start hittills är g, inte h.'),
             alt('Den exakta längden på vägen från A till M', False, 'Vägen från A till M är 5 mil, men h = 4.'),
             alt('Antalet vägar som går från A', False, 'h handlar om avståndet till målet, inte om antalet vägar.')],
            'Vad mäter fågelvägen?', 1)
    return uppgift('2.78', 'astar_varden', H_FAM, intro, [a, b, c], 'h uppskattar hur långt det är kvar till målet.', ['begrepp', 'procedur'])


M279 = ['S.....', '.#.##.', '...G..', '.##...', '......']


def t279():
    s, g = A.parse(M279)
    P = (4, 0)
    ett = [c for c in A.neigh(M279, g)]
    assert A.manhattan(P, g) == 5 and len(ett) == 3
    intro = maze(M279, s, g, {P: 'P'}, extra_legend=MARK) + p('Labyrinten ska sökas igenom med A*, där h är Manhattanavståndet till målet.')
    a = num('Bestäm h för den markerade rutan P.',
            [step('Rader och kolumner till målet', 'P ligger i E1 och målet i C4: 2 rader och 3 kolumner.'),
             step('Summa', 'h = 2 + 3 = 5.')], 5, 'Räkna rader och kolumner mellan P och målet. Väggar räknas inte.', 1)
    b = num('Vilket värde har h i själva målrutan?',
            [step('Inget avstånd kvar', 'I målet är både rad- och kolumnskillnaden 0, så h = 0.')], 0,
            'Hur långt är det kvar när man redan står i målet?', 1)
    c = num('Hur många öppna rutor (inte väggar) har h = 1?',
            [step('h = 1 betyder ett steg från målet', 'Det är rutorna direkt ovanför, under, till vänster och till höger om målet.'),
             step('Väggen ovanför målet räknas inte', 'B4 är en vägg. Kvar blir C3, C5 och D4, alltså 3 rutor.')], 3,
            'Vilka rutor ligger direkt intill målet? Är någon av dem en vägg?', 2)
    return uppgift('2.79', 'astar_varden', H_FAM, intro, [a, b, c], 'h är radskillnad plus kolumnskillnad till målet.', ['procedur'])


def t280():
    def h(r, k, mr=5, mk=9):
        return abs(r - mr) + abs(k - mk)
    assert h(1, 2) == 11 and h(2, 2) == 10
    intro = p('En robot rör sig i ett lager som är indelat i rutor. Raderna heter A–H och kolumnerna 1–10. '
              'Roboten står i ruta B2 och ska till ruta F9. Den kan bara gå upp, ned, åt vänster eller åt höger, '
              'och den använder Manhattanavståndet som h.')
    a = num('Vilket h har roboten i B2?',
            [step('Rader', 'Från B till F är det 4 rader.'), step('Kolumner', 'Från 2 till 9 är det 7 kolumner.'),
             step('Summa', 'h = 4 + 7 = 11.')], 11, 'Räkna raderna och kolumnerna för sig och lägg ihop.', 1)
    b = num('Roboten går ett steg nedåt till C2. Vilket h har den nu?',
            [step('En rad närmare', 'Från C till F är det 3 rader, och kolumnerna är oförändrade, 7.'),
             step('Summa', 'h = 3 + 7 = 10.')], 10, 'Kommer roboten närmare målet med en rad eller en kolumn?', 1)
    c = val('Roboten tar ett steg i någon riktning. Hur mycket kan h ändras?',
            [step('Ett steg ändrar en rad eller en kolumn', 'Antingen rad- eller kolumnskillnaden ändras med 1. Därför ändras h med exakt 1.')],
            [alt('Med exakt 1, uppåt eller nedåt', True, 'Varje steg flyttar roboten en rad eller en kolumn.'),
             alt('Med 0, 1 eller 2', False, 'Roboten kan inte gå snett, så h ändras aldrig med 0 eller 2.'),
             alt('h kan bara minska', False, 'Om roboten går bort från målet ökar h.'),
             alt('Med hur mycket som helst', False, 'Ett enda steg kan bara ändra h med 1.')],
            'Vad händer med rad- och kolumnskillnaden när roboten tar ett steg?', 2)
    return uppgift('2.80', 'astar_varden', H_FAM, intro, [a, b, c], 'Manhattanavståndet räknar rader plus kolumner.', ['procedur', 'begrepp'])


def t281():
    intro = p('Frågorna handlar om heuristiker. En heuristik h är en tumregel som uppskattar hur långt det är kvar till målet.')
    a = val('Vilket är ett exempel på en heuristik när man letar efter vägen till en plats?',
            [step('En uppskattning av avståndet kvar', 'Fågelvägen säger ungefär hur långt det är kvar, utan att räkna med vägarna.')],
            [alt('Fågelvägen till platsen', True, 'Fågelvägen är en snabb uppskattning av avståndet kvar.'),
             alt('Hur långt man redan har gått', False, 'Det är kostnaden hittills, g, inte en uppskattning av det som är kvar.'),
             alt('Att välja riktning genom att singla slant', False, 'Slumpen säger ingenting om var målet ligger.'),
             alt('Hur många gator det finns i hela staden', False, 'Det säger ingenting om avståndet till just den platsen.')],
            'Vilket alternativ säger något om hur långt det är kvar?', 1)
    b = val('En robot går rakt mot målet i en labyrint utan väggar. Vad händer med Manhattanavståndet h för varje steg?',
            [step('Varje steg närmar sig målet', 'Ett steg mot målet minskar rad- eller kolumnskillnaden med 1, så h minskar med 1.')],
            [alt('h minskar med 1', True, 'Varje steg mot målet tar bort en rad eller en kolumn.'),
             alt('h ökar med 1', False, 'h ökar bara när roboten går bort från målet.'),
             alt('h är oförändrat', False, 'h beror på var roboten står, så det ändras när den flyttar sig.'),
             alt('h halveras', False, 'Manhattanavståndet ändras med ett steg i taget, inte med hälften.')],
            'Vad mäter h, och hur ändras det när roboten närmar sig målet?', 1)
    c = val('Varför kallas h en uppskattning och inte den verkliga kostnaden kvar?',
            [step('Väggar och omvägar räknas inte', 'Manhattanavståndet räknar som om vägen vore fri. Den verkliga vägen kan vara längre.')],
            [alt('Den räknar inte med väggar och omvägar', True, 'Därför kan den verkliga vägen vara längre än h.'),
             alt('Den räknas ut slumpmässigt', False, 'h räknas ut med en bestämd regel, till exempel rader plus kolumner.'),
             alt('Den ändras aldrig under sökningen', False, 'h är olika för olika rutor.'),
             alt('Den är alltid större än den verkliga kostnaden', False, 'Manhattanavståndet är tvärtom aldrig större än den verkliga vägen.')],
            'Vad tar Manhattanavståndet inte hänsyn till?', 2)
    return uppgift('2.81', 'astar_varden', H_FAM, intro, [a, b, c], 'En heuristik är en snabb uppskattning, inte ett exakt svar.', ['begrepp'])


# ======================================================================== Uttag ur en prioritetskö

def t282():
    ops = [('E', 3), ('F', 1), ('H', 5), None, ('M', 2), None, None]
    out, kvar = prio(ops)
    assert [n for n, _ in out] == ['F', 'M', 'E'] and kvar == [('H', 5)]
    intro = (p('Lisa skriver upp sina läxor i en lista där talet är antalet dagar kvar till inlämning. '
               'Hon gör alltid den läxa som har minst antal dagar kvar först, som en prioritetskö.')
             + tab(['Läxa', 'Dagar kvar'], [['E (engelska)', '3'], ['F (fysik)', '1'], ['H (historia)', '5']])
             + p('Hon gör en läxa. Sedan får hon M (matte) med 2 dagar kvar. Därefter gör hon två läxor till.'))
    a = lst('I vilken ordning gör Lisa de tre läxorna?',
            [step('Första läxan', 'F har minst antal dagar kvar, 1.'),
             step('M läggs till', 'Kvar är E (3), H (5) och M (2). M har minst och görs näst.'),
             step('Tredje läxan', 'Av E (3) och H (5) har E minst.')],
            [n for n, _ in out], 'Välj alltid läxan med minst antal dagar kvar bland dem som finns i listan just då.', 1,
            'Skriv läxornas bokstäver i ordning, åtskilda med kommatecken.')
    b = val('Vilken läxa är kvar när hon har gjort tre läxor?',
            [step('Den med flest dagar kvar', 'H har 5 dagar kvar och har aldrig minst värde vid något uttag.')],
            [alt('Historia', True, 'H har flest dagar kvar och väljs aldrig.'), alt('Engelska', False, 'Engelska görs som tredje läxa.'),
             alt('Matte', False, 'Matte har 2 dagar kvar och görs som andra läxa.'), alt('Fysik', False, 'Fysik har minst dagar kvar och görs först.')],
            'Vilken läxa har aldrig minst antal dagar kvar?', 1)
    return uppgift('2.82', 'prioritetsko', UT_FAM, intro, [a, b], 'Prioritetskön tar alltid ut den med lägst värde.', ['procedur'])


def t283():
    ops = [('A', 7), ('B', 12), ('C', 9), None, ('D', 15), ('E', 8), None, None]
    out, kvar = prio(ops, hogst=True)
    assert [n for n, _ in out] == ['B', 'D', 'C'] and sorted(kvar) == [('A', 7), ('E', 8)]
    intro = (p('En spelserver släpper in spelare från en kö där den med högst ranking släpps in först. '
               'Talet inom parentes är spelarens ranking.')
             + p('Lägg in A(7), B(12) och C(9) → släpp in en spelare → lägg in D(15) och E(8) → släpp in två spelare.'))
    a = lst('I vilken ordning släpps spelarna in?',
            [step('Första', 'Av A(7), B(12) och C(9) har B högst ranking.'),
             step('D och E läggs in', 'Kön är A(7), C(9), D(15) och E(8). D har högst och släpps in, sedan C.')],
            [n for n, _ in out], 'Här tas högst värde ut först, inte lägst.', 1, 'Skriv spelarnas bokstäver i ordning, åtskilda med kommatecken.')
    b = num('Vilken är den högsta rankingen bland spelarna som är kvar i kön?',
            [step('Kvar i kön', 'A(7) och E(8). Högst är 8.')], 8, 'Vilka spelare har inte släppts in?', 1)
    c = val('Hur skiljer sig den här kön från prioritetskön i A*?',
            [step('Olika ordning', 'A* tar ut noden med lägst f. Servern tar ut spelaren med högst ranking.')],
            [alt('A* tar ut lägst värde först, servern högst', True, 'Båda är prioritetsköer, men med omvänd ordning.'),
             alt('A* tar ut den som lades in först', False, 'Det beskriver en FIFO-kö, inte A*.'),
             alt('Det finns ingen skillnad', False, 'A* väljer lägst f, medan servern väljer högst ranking.'),
             alt('A* tar ut den som lades in sist', False, 'Det beskriver en stack, inte A*.')],
            'Vilken nod väljer A* ur öppna listan?', 2)
    return uppgift('2.83', 'prioritetsko', UT_FAM, intro, [a, b, c], 'En prioritetskö kan sortera efter lägst eller högst värde.',
                   ['procedur', 'begrepp'])


def t284():
    start = [('K', 5), ('L', 3), ('N', 8), ('P', 3)]
    out, _ = prio(start + [None, None, None])
    assert [n for n, _ in out] == ['L', 'P', 'K']
    out2, _ = prio(start + [None, None, ('R', 4), None])
    assert out2[-1] == ('R', 4)
    intro = (p('Tabellen visar vilka noder som ligger i en prioritetskö just nu. Noden med lägst värde tas ut först, '
               'och vid lika värde tas den nod ut som kommer först i bokstavsordning.')
             + tab(['Nod', 'Värde'], [['K', '5'], ['L', '3'], ['N', '8'], ['P', '3']]))
    a = lst('Tre noder tas ut. I vilken ordning tas de ut?',
            [step('Lika värden först', 'L och P har båda värdet 3. L kommer före P i bokstavsordning.'),
             step('Tredje uttaget', 'Kvar är K (5) och N (8). K har lägst värde.')],
            ['L', 'P', 'K'], 'Vilka noder har lägst värde? Vilken av dem kommer först i bokstavsordning?', 1, NO)
    b = val('Börja om från tabellen. Två noder tas ut, och sedan läggs R(4) in. Vilken nod tas ut vid nästa uttag?',
            [step('Efter två uttag', 'L och P har tagits ut. Kvar är K (5) och N (8).'),
             step('R läggs in', 'R har värdet 4, lägre än K:s 5. R tas ut.')],
            [alt('Noden R', True, 'R(4) har lägst värde bland R, K och N.'),
             alt('Noden K', False, 'K har värdet 5, högre än R:s 4.'),
             alt('Noden N', False, 'N har det högsta värdet, 8.'),
             alt('Noden P', False, 'P togs redan ut vid det andra uttaget.')],
            'En nod som läggs in sent kan ändå tas ut direkt om den har lägst värde.', 2)
    return uppgift('2.84', 'prioritetsko', UT_FAM, intro, [a, b], 'Lägst värde först, och vid lika värde bokstavsordning.', ['procedur'])


# ======================================================================== Prioritetskön i girig bäst först och A*

def t285():
    rad = {'A': (2, 6), 'B': (5, 3), 'C': (1, 5), 'D': (4, 4)}
    girig = min(rad, key=lambda n: (rad[n][1], n))
    astar = min(rad, key=lambda n: (sum(rad[n]), rad[n][1], n))
    assert girig == 'B' and astar == 'C' and sum(rad['B']) == 8
    intro = (p('Under en sökning ligger fyra noder i öppna listan. Tabellen visar kostnaden hittills g och uppskattningen h av '
               'kostnaden kvar till målet.')
             + tab(['Nod', 'g', 'h'], [[n, str(gv), str(hv)] for n, (gv, hv) in rad.items()]))
    a = val('Vilken nod tar girig bäst först ut?',
            [step('Girig bäst först jämför bara h', 'Lägst h har B, med h = 3.')],
            [alt('Noden B', True, 'B har lägst h, 3.'), alt('Noden C', False, 'C har lägst f, men girig bäst först tittar bara på h.'),
             alt('Noden A', False, 'A har h = 6, högre än B.'), alt('Noden D', False, 'D har h = 4, högre än B.')],
            'Vilket värde använder girig bäst först?', 1)
    b = num('Vilket f-värde har noden B?', [step('f = g + h', 'f = 5 + 3 = 8.')], 8, 'Lägg ihop g och h.', 1)
    c = val('Vilken nod tar A* ut?',
            [step('f för alla noder', 'A: 2 + 6 = 8. B: 5 + 3 = 8. C: 1 + 5 = 6. D: 4 + 4 = 8.'), step('Lägst f', 'C har lägst f, 6.')],
            [alt('Noden C', True, 'C har lägst f = 6.'), alt('Noden B', False, 'B har lägst h men f = 8.'),
             alt('Noden A', False, 'A har f = 8, högre än C:s 6.'), alt('Noden D', False, 'D har f = 8, högre än C:s 6.')],
            'Räkna f = g + h för varje nod.', 2)
    return uppgift('2.85', 'prioritetsko', AS_FAM, intro, [a, b, c], 'Girig bäst först sorterar efter h, A* efter f = g + h.', ['procedur'])


G286 = [('S', 'A', 2), ('S', 'B', 4), ('A', 'C', 5), ('B', 'C', 1), ('C', 'M', 2)]
H286 = {'S': 6, 'A': 6, 'B': 3, 'C': 2, 'M': 0}
P286 = {'S': (50, 130), 'A': (190, 50), 'B': (190, 210), 'C': (330, 130), 'M': (450, 130)}


def t286():
    r = A.astar_graph(G286, H286, 'S', 'M')
    ordning = [n for n, *_ in r['order']]
    assert ordning == ['S', 'B', 'C', 'M'] and r['cost'] == 7
    intro = (weighted_graph(P286, G286, 'S', 'M', 'Graf med noderna S, A, B, C och målet M. Kanter: S–A 2, S–B 4, A–C 5, B–C 1 och '
                            'C–M 2. h: S 6, A 6, B 3, C 2, M 0.', 500, h=H286)
             + p('Grafen söks igenom med A*. Talet vid varje kant är kostnaden, och h vid varje nod uppskattar kostnaden kvar till M. '
                 'Öppna listan är en prioritetskö där lägst f = g + h tas ut först.'))
    a = num('S tas ut och A och B läggs in. Vilket f får A?',
            [step('g för A', 'Kanten S–A kostar 2, så g = 2.'), step('f = g + h', 'f = 2 + 6 = 8.')], 8,
            'g är kostnaden från S till A.', 1)
    b = val('Vilken nod tas ut efter S?',
            [step('f för A och B', 'A: 2 + 6 = 8. B: 4 + 3 = 7.'), step('Lägst f', 'B har lägst f och tas ut.')],
            [alt('Noden B', True, 'B har f = 7, lägre än A:s 8.'), alt('Noden A', False, 'A har lägre g, men högre f: 8 mot 7.'),
             alt('Noden C', False, 'C har inte lagts in än. Den nås först från A eller B.'), alt('Noden M', False, 'M är inte granne med S.')],
            'Jämför f = g + h, inte bara g.', 2)
    c = lst('I vilken ordning tas noderna ut ur prioritetskön, fram till och med M?',
            [step('Från B', 'B lägger in C med g = 4 + 1 = 5 och f = 7.'),
             step('C före A', 'C har f = 7 och A f = 8. C tas ut och lägger in M med g = 7 och f = 7.'),
             step('M tas ut', 'M har f = 7, lägre än A:s 8.')],
            ordning, 'Räkna f för varje ny nod som läggs in och välj lägst f.', 2, NO)
    return uppgift('2.86', 'prioritetsko', AS_FAM, intro, [a, b, c], 'A* tar alltid ut noden med lägst f ur prioritetskön.', ['procedur'])


G287 = [('S', 'A', 2), ('S', 'B', 1), ('A', 'M', 6), ('B', 'C', 2), ('C', 'M', 2)]
H287 = {'S': 4, 'A': 1, 'B': 3, 'C': 2, 'M': 0}
P287 = {'S': (50, 140), 'A': (220, 50), 'B': (150, 220), 'C': (320, 220), 'M': (450, 120)}


def t287():
    gr = A.greedy_graph(G287, H287, 'S', 'M')
    ast = A.astar_graph(G287, H287, 'S', 'M')
    assert gr['order'][1] == 'A' and gr['cost'] == 8
    assert [n for n, *_ in ast['order']] == ['S', 'A', 'B', 'C', 'M'] and ast['cost'] == 5
    intro = (weighted_graph(P287, G287, 'S', 'M', 'Graf med noderna S, A, B, C och målet M. Kanter: S–A 2, S–B 1, A–M 6, B–C 2 och '
                            'C–M 2. h: S 4, A 1, B 3, C 2, M 0.', 500, h=H287)
             + p('Grafen söks igenom en gång med girig bäst först och en gång med A*. Båda använder en prioritetskö: girig bäst först '
                 'sorterar efter h och A* efter f = g + h.'))
    a = val('Vilken nod tar girig bäst först ut efter S?',
            [step('S:s grannar', 'A har h = 1 och B har h = 3. Girig bäst först väljer lägst h.')],
            [alt('Noden A', True, 'A har lägst h, 1.'), alt('Noden B', False, 'B har h = 3, högre än A.'),
             alt('Noden M', False, 'M är inte granne med S.'), alt('Noden C', False, 'C har inte lagts in än.')],
            'Jämför bara h.', 1)
    b = num('Vad kostar vägen som girig bäst först hittar?',
            [step('Vägen', 'Från A läggs M in, och M har h = 0. Vägen blir S → A → M.'), step('Kostnad', '2 + 6 = 8.')], 8,
            'Följ den väg som girig bäst först tar och lägg ihop kanternas kostnader.', 2)
    c = lst('I vilken ordning tar A* ut noderna, fram till och med M?',
            [step('S tas ut, och A har lägst f', 'A får f = 2 + 1 = 3 och B f = 1 + 3 = 4. A tas ut och lägger in M med f = 8 + 0 = 8.'),
             step('Via B och C får M ett lägre f', 'B (f = 4) tas ut och lägger in C med f = 3 + 2 = 5. C tas ut och hittar en billigare väg till M: g = 5, f = 5.'),
             step('M tas ut med f = 5', 'M har nu lägst f i kön, och sökningen stoppar.')],
            [n for n, *_ in ast['order']], 'M ligger i kön med f = 8 men får ett bättre värde senare.', 3, NO)
    d = num('Vad kostar vägen som A* hittar?',
            [step('Vägen', 'S → B → C → M.'), step('Kostnad', '1 + 2 + 2 = 5.')], 5, 'Vilken väg till M ger g = 5?', 2)
    return uppgift('2.87', 'prioritetsko', AS_FAM, intro, [a, b, c, d], 'Girig bäst först väljer lägst h, A* lägst f.',
                   ['procedur', 'resonemang'])


NYA = [t278, t279, t280, t281, t282, t283, t284, t285, t286, t287]


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
    print(f'{len(NYA)} uppgifter (2.78–2.87) inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
