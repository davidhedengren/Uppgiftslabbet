"""AI-banken 2026-11-11, åttonde omgången: teorifrågor och beräkningar.

Användarens önskemål: fler uppgifter inom minimax samt oinformerad och
informerad sökning, gärna teorifrågor med flerval. 16 teoriuppgifter (flerval
där varje fel alternativ fångar en vanlig feltanke) och 12 beräkningsuppgifter.
Allt i Kunskapsgymmets format och nivåindelat enligt AI_NIVAINDELNING.md.

Teorifrågorna har en figur där den hjälper (Manhattanavstånd, spelträd).
Rena begreppsfrågor om datastrukturer och definitioner saknar figur, eftersom
en figur inte tillför något till själva frågan.

Kör efter bygg-ai-pafyllnad4-2026-11-11.py och före bygg-ai-nivaer-2026-11-11.py.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_spec = importlib.util.spec_from_file_location('ai_kg', os.path.join(HERE, 'bygg-ai-kunskapsgymmet-2026-11-11.py'))
K = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(K)
from ai_figurer import step, maze, search_tree, weighted_graph, game_tree, tab  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402

p, alt, num, val, kg_task, names, lista, pil = K.p, K.alt, K.num, K.val, K.kg_task, K.names, K.lista, K.pil
BANK = 'uppgifterai.js'
MARK = [('#fff3b0', 'Markerad ruta')]


def mc(fraga, rubrik, forklaring, alts, ledtrad, tn):
    """Teorifråga med ett rätt alternativ. alts: [(text, rätt, kommentar)]."""
    return val(fraga, [step(rubrik, forklaring)], [alt(t, r, k) for t, r, k in alts], ledtrad, tn)


def teori(id_, omr, familj, intro, parts, ledtrad, formaga=None):
    return kg_task(id_, omr, familj, intro, parts, ledtrad, formaga or ['begrepp'], 1)


# ======================================================================== oinformerad sökning

def t155():
    a = mc('Vilken datastruktur använder BFS för att hålla reda på rutorna som ska undersökas?',
           'BFS använder en FIFO-kö', 'Den ruta som lades in först tas ut först. Därför undersöks rutorna i ordning efter avstånd från start.',
           [('En FIFO-kö', True, 'Först in, först ut gör att BFS tar en nivå i taget.'),
            ('En stack', False, 'En stack tar ut den senast inlagda rutan. Det ger DFS.'),
            ('En prioritetskö sorterad efter h', False, 'Det är girig bäst först, en informerad sökning.'),
            ('Ingen datastruktur, BFS väljer slumpmässigt', False, 'BFS följer en fast ordning, inte slumpen.')],
           'Vilken nod tas ut först i BFS, den äldsta eller den senaste?', 1)
    b = mc('Varje steg kostar lika mycket. Vad gäller för vägen som BFS hittar?',
           'BFS hittar en kortaste väg', 'Eftersom BFS undersöker alla rutor på avstånd 1 före avstånd 2, och så vidare, nås målet första gången längs en väg med minst antal steg.',
           [('Den har minst antal steg', True, 'BFS når målet på det minsta avståndet först.'),
            ('Den är alltid den första vägen åt höger', False, 'Grannordningen avgör bara vilken av flera lika korta vägar som hittas.'),
            ('Den är billigast även när rutorna kostar olika mycket', False, 'BFS räknar steg, inte kostnader.'),
            ('Den är slumpmässig', False, 'BFS är helt bestämd av labyrinten och grannordningen.')],
           'BFS undersöker rutorna nivå för nivå.', 1)
    c = mc('I vilken ordning tar BFS ut rutorna ur kön?',
           'Efter avstånd från start', 'Alla rutor på avstånd 1 tas ut före rutorna på avstånd 2, och så vidare.',
           [('Efter avstånd från start', True, 'Det är just så BFS fungerar.'),
            ('Efter uppskattat avstånd till målet', False, 'Det beskriver girig bäst först, som använder h.'),
            ('Den senast inlagda rutan först', False, 'Det beskriver en stack och DFS.'),
            ('I bokstavsordning efter rutnamn', False, 'Rutnamnen avgör inte ordningen i BFS.')],
           'Tänk på hur kön växer nivå för nivå.', 1)
    return teori('1.55', 'bfs', 'BFS i teorin', p('Frågorna handlar om bredden först-sökning (BFS) i en labyrint.'), [a, b, c],
                 'BFS använder en FIFO-kö och undersöker rutorna nivå för nivå.')


def t156():
    a = mc('Vilken datastruktur passar för DFS?', 'DFS kan använda en stack',
           'Den senast hittade noden undersöks först, så sökningen går på djupet innan den backar.',
           [('En stack', True, 'Sist in, först ut gör att DFS fortsätter från den senast hittade noden.'),
            ('En FIFO-kö', False, 'En FIFO-kö ger BFS.'),
            ('En prioritetskö sorterad efter f', False, 'Det är A*, en informerad sökning.'),
            ('En tabell med alla avstånd', False, 'DFS behöver inga avstånd.')], 'Vilken nod fortsätter DFS från?', 1)
    b = mc('Hittar DFS alltid den kortaste vägen till målet?', 'DFS stoppar vid den första vägen den hittar',
           'DFS följer en väg så långt det går i första tillåtna riktningen. Den kan hitta målet via en lång omväg innan den har prövat en kortare väg.',
           [('Nej, DFS kan hitta en lång väg först', True, 'DFS stoppar vid första vägen den hittar, oavsett längd.'),
            ('Ja, alltid', False, 'Det gäller BFS när varje steg kostar lika, inte DFS.'),
            ('Ja, om labyrinten är liten', False, 'Även i små labyrinter kan DFS ta en omväg.'),
            ('Nej, DFS hittar aldrig målet', False, 'DFS hittar målet om det går att nå, men inte nödvändigtvis den kortaste vägen.')],
           'Vad gör DFS när den har hittat en väg till målet?', 1)
    c = mc('Vad gör DFS när den hamnar i en återvändsgränd?', 'DFS backar',
           'Den går tillbaka till den senaste ruta som fortfarande har en obesökt granne och fortsätter därifrån.',
           [('Backar till den senaste rutan som har en obesökt granne', True, 'Det är just att backa.'),
            ('Börjar om från start', False, 'DFS behåller vägen hittills och backar bara så långt som behövs.'),
            ('Stannar och meddelar att målet saknas', False, 'DFS slutar först när alla nåbara rutor är prövade.'),
            ('Hoppar till den ruta som ligger närmast målet', False, 'Det vore en informerad sökning. DFS vet inte var målet ligger.')],
           'Var finns det fortfarande en väg som inte är prövad?', 1)
    return teori('1.56', 'dfs', 'DFS i teorin', p('Frågorna handlar om djupet först-sökning (DFS).'), [a, b, c],
                 'DFS går så djupt som möjligt i en riktning och backar när det tar stopp.')


def t157():
    a = mc('Varför läggs en ruta som redan har upptäckts inte in i kön igen?', 'Annars undersöks samma ruta flera gånger',
           'I en labyrint med slingor kan samma ruta nås på flera sätt. Utan regeln kan sökningen gå runt i cirklar och göra onödigt arbete.',
           [('Annars kan samma ruta undersökas flera gånger och sökningen gå runt i cirklar', True, 'Regeln gör att varje ruta undersöks högst en gång.'),
            ('Annars hittar BFS en kortare väg', False, 'Vägen blir inte kortare av att rutor läggs in flera gånger.'),
            ('För att målet ska hittas före start', False, 'Start tas alltid ut först.'),
            ('Regeln gäller bara för DFS', False, 'Både BFS och DFS behöver den i labyrinter med slingor.')],
           'Vad händer i en labyrint där man kan gå runt i en ring?', 3)
    b = mc('Vad händer i BFS om målet inte går att nå?', 'Kön blir tom',
           'BFS tar ut alla rutor som går att nå från start. När kön är tom finns inget mer att undersöka, och sökningen slutar utan väg.',
           [('Kön blir tom och sökningen slutar utan att hitta någon väg', True, 'Alla nåbara rutor har undersökts.'),
            ('Sökningen fortsätter för alltid', False, 'Varje ruta läggs bara in en gång, så kön tar slut.'),
            ('BFS går igenom en vägg', False, 'BFS följer bara tillåtna steg.'),
            ('BFS returnerar vägen till den ruta som ligger närmast målet', False, 'BFS letar efter just målet, inte efter en ruta nära det.')],
           'Hur många gånger kan en ruta läggas in i kön?', 2)
    return teori('1.57', 'ko_sokning', 'Kön och upptäckta rutor', p('Frågorna handlar om hur kön används när en labyrint söks igenom med BFS.'), [a, b],
                 'Varje ruta läggs in i kön högst en gång.', ['begrepp', 'resonemang'])


def t158():
    a = mc('Vad betyder det att en sökning är oinformerad?', 'Ingen uppskattning av avståndet kvar',
           'En oinformerad sökning vet inte åt vilket håll målet ligger. Den följer bara en fast ordning, till exempel en kö eller en stack.',
           [('Den använder ingen uppskattning av hur långt det är kvar till målet', True, 'BFS och DFS vet inte var målet ligger.'),
            ('Den vet inte var start ligger', False, 'Alla sökningar börjar i start.'),
            ('Den väljer nästa ruta slumpmässigt', False, 'BFS och DFS följer en bestämd ordning.'),
            ('Den använder bara h', False, 'Att använda h är just det som gör en sökning informerad.')],
           'Vad vet BFS och DFS om var målet ligger?', 1)
    b = mc('Vilket par består av två oinformerade sökningar?', 'BFS och DFS',
           'Ingen av dem använder någon heuristik. A* och girig bäst först använder h och är informerade.',
           [('BFS och DFS', True, 'Båda följer en fast ordning utan att uppskatta avståndet till målet.'),
            ('A* och girig bäst först', False, 'Båda använder h och är informerade.'),
            ('BFS och A*', False, 'A* använder h och är informerad.'),
            ('Girig bäst först och DFS', False, 'Girig bäst först använder h och är informerad.')],
           'Vilka sökningar använder h?', 1)
    return teori('1.58', 'ko_sokning', 'Oinformerad sökning', p('Frågorna handlar om skillnaden mellan oinformerade och informerade sökningar.'), [a, b],
                 'En informerad sökning använder en heuristik h, en oinformerad gör det inte.')


def t159():
    a = mc('Vad händer om BFS:s FIFO-kö byts mot en stack?', 'Sökningen blir DFS',
           'Med en stack tas den senast inlagda rutan ut först. Sökningen fortsätter då från den senast hittade rutan och går på djupet.',
           [('Sökningen beter sig som DFS', True, 'Det är datastrukturen som skiljer BFS från DFS.'),
            ('Sökningen beter sig som A*', False, 'A* behöver en prioritetskö sorterad efter f.'),
            ('Ingenting ändras', False, 'Ordningen som rutorna tas ut i ändras helt.'),
            ('Sökningen hittar alltid kortare vägar', False, 'DFS kan tvärtom hitta längre vägar.')],
           'Vilken ruta tas ut först ur en stack?', 2)
    b = mc('Vilken nod tas ut ur en stack?', 'Den senast inlagda', 'En stack fungerar som en hög: det som lades dit sist ligger överst och tas först.',
           [('Den som lades in senast', True, 'Sist in, först ut.'), ('Den som lades in först', False, 'Det gäller en FIFO-kö.'),
            ('Den med lägst värde', False, 'Det gäller en prioritetskö.'), ('Den som ligger närmast målet', False, 'En stack vet inget om målet.')],
           'Tänk på en hög med tallrikar.', 1)
    return teori('1.59', 'ko_stack', 'Kö eller stack i sökningen', p('Frågorna handlar om vilken datastruktur en sökning använder.'), [a, b],
                 'BFS använder en FIFO-kö och DFS en stack.')


def t160():
    a = mc('Kan grannordningen, till exempel ↑ → ↓ ← eller ↓ → ↑ ←, ändra vilken väg DFS hittar?', 'DFS följer den första tillåtna riktningen',
           'DFS går till den första tillåtna grannen och följer den så långt det går. Med en annan ordning kan DFS välja en helt annan väg.',
           [('Ja, eftersom DFS följer den första tillåtna riktningen', True, 'Olika ordning kan ge olika vägar, även olika långa.'),
            ('Nej, DFS hittar alltid samma väg', False, 'Vägen beror på vilken riktning som prövas först.'),
            ('Bara om labyrinten saknar väggar', False, 'Även i labyrinter med väggar påverkar ordningen.'),
            ('Bara antalet besökta rutor ändras, aldrig vägen', False, 'Både vägen och antalet besök kan ändras.')],
           'Vilken granne går DFS till först?', 2)
    b = mc('Varje steg kostar lika mycket. Kan grannordningen ändra hur många steg vägen som BFS hittar har?', 'BFS hittar alltid en väg med minst antal steg',
           'BFS hittar alltid en väg med minst antal steg. Grannordningen kan bara avgöra vilken av flera lika korta vägar som returneras.',
           [('Nej, men den kan ändra vilken av flera lika korta vägar som hittas', True, 'Längden är alltid den kortaste möjliga.'),
            ('Ja, BFS kan hitta en längre väg med en annan ordning', False, 'BFS undersöker alla rutor på ett avstånd före nästa, så den kortaste vägen hittas alltid.'),
            ('Ja, men bara om målet ligger nära start', False, 'Avståndet till målet spelar ingen roll för den slutsatsen.'),
            ('Nej, och vägen blir alltid exakt densamma', False, 'Om flera vägar är lika korta kan ordningen avgöra vilken som hittas.')],
           'I vilken ordning tar BFS ut rutorna?', 3)
    return teori('1.60', 'dfs', 'Grannordningens betydelse', p('Frågorna handlar om vad grannordningen betyder för BFS och DFS.'), [a, b],
                 'Grannordningen avgör vilken granne som prövas först.', ['begrepp', 'resonemang'])


# ======================================================================== informerad sökning

def t267():
    a = mc('Vad betyder h i A*?', 'h är en uppskattning av kostnaden kvar', 'h uppskattar hur långt det är kvar från rutan till målet, till exempel med Manhattanavståndet.',
           [('En uppskattning av kostnaden kvar till målet', True, 'h kallas heuristik.'), ('Kostnaden från start till rutan', False, 'Det är g, kostnaden hittills, inte uppskattningen kvar.'),
            ('Summan av kostnaden hittills och kostnaden kvar', False, 'Det är f = g + h, inte h ensamt.'), ('Antalet rutor som har undersökts', False, 'Det är inget av värdena i A*.')],
           'h hjälper sökningen att gå mot målet.', 1)
    b = mc('Vad betyder g i A*?', 'g är kostnaden hittills', 'g är den kostnad det har kostat att ta sig från start till rutan längs den bästa vägen hittills.',
           [('Kostnaden från start till rutan längs vägen hittills', True, 'g räknas längs gångarna.'), ('En uppskattning av kostnaden kvar till målet', False, 'Det är h, uppskattningen av vägen som återstår.'),
            ('Avståndet fågelvägen till målet', False, 'Det liknar h, inte g.'), ('Antalet väggar runt rutan', False, 'Väggar påverkar g bara genom att vägen blir längre.')],
           'Vad har det kostat att komma till rutan?', 1)
    c = mc('Vad betyder f = g + h?', 'f uppskattar hela vägen via rutan', 'f är kostnaden hittills plus uppskattningen kvar, alltså en uppskattning av hela vägens kostnad om man går via rutan.',
           [('En uppskattning av hela vägens kostnad om man går via rutan', True, 'A* väljer rutan med lägst f.'),
            ('Den exakta kostnaden för den billigaste vägen', False, 'f bygger på h, som bara är en uppskattning.'),
            ('Kostnaden kvar till målet', False, 'Det är h. f innehåller också kostnaden hittills.'), ('Antalet steg från start', False, 'Det är g när varje steg kostar 1.')],
           'Lägg ihop vad som redan har kostat och vad som uppskattas återstå.', 1)
    return teori('2.67', 'astar_varden', 'g, h och f i ord', p('Frågorna handlar om de tre värden som A* använder för varje ruta.'), [a, b, c],
                 'g är kostnaden hittills, h uppskattningen kvar och f summan.')


def t268():
    rows2 = ['S....', '.###.', '.#G#.', '.....']
    s2, g2 = A.parse(rows2)
    R = (1, 0)
    assert A.manhattan(R, g2) == 3 and A.dist_all(rows2, g2)[R] == 5
    intro = (maze(rows2, s2, g2, {R: 'P'}, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd till målet).'))
    a = mc('Hur räknas Manhattanavståndet h från en ruta till målet?', 'Rader plus kolumner',
           'Man räknar hur många rader och hur många kolumner rutan ligger från målet och lägger ihop dem. Väggarna räknas inte.',
           [('Antalet rader plus antalet kolumner mellan rutan och målet', True, 'Det är avståndet om man går rakt, utan väggar och utan diagonaler.'),
            ('Fågelvägen, räknad med Pythagoras sats', False, 'Det är det euklidiska avståndet, inte Manhattanavståndet.'),
            ('Antalet steg längs gångarna runt väggarna', False, 'Det är det verkliga avståndet, som h bara uppskattar.'),
            ('Antalet väggar mellan rutan och målet', False, 'h räknar inte väggar alls.')], 'Tänk på kvarteren på Manhattan: man går längs gatorna.', 1)
    b = num('Bestäm h för P.', [step('h = radskillnad + kolumnskillnad', 'P ligger i B1 och målet i C3: 1 + 2 = 3.')], 3, 'Räkna rader och kolumner till målet.', 1)
    c = mc('Från P behövs 5 steg till målet. Varför är h mindre än det?', 'h räknar inte med väggarna',
           'Väggarna tvingar fram en omväg. h räknar som om vägen gick rakt, och blir därför mindre än det verkliga antalet steg.',
           [('h räknar inte med väggarna, och väggarna tvingar fram en omväg', True, 'h är en uppskattning som bortser från hinder.'),
            ('h räknar diagonala steg', False, 'Manhattanavståndet räknar bara rader och kolumner.'),
            ('h är felräknat', False, 'h är rätt räknat. Det är bara en uppskattning.'),
            ('Väggrutorna kostar mer än vanliga rutor', False, 'Man kan inte gå in i väggar alls.')], 'Vad finns mellan P och målet?', 3)
    return teori('2.68', 'astar_varden', 'Manhattanavståndet', intro, [a, b, c], 'h räknas rakt, utan väggar.', ['begrepp', 'procedur'])


def t269():
    a = mc('Vad jämför girig bäst först när den väljer nästa ruta?', 'Bara h', 'Girig bäst först väljer den ruta som verkar ligga närmast målet och bryr sig inte om vad vägen hittills har kostat.',
           [('Bara h', True, 'Den går mot målet så snabbt som möjligt.'), ('Bara g', False, 'Att välja efter bara kostnaden hittills är inte girig bäst först.'),
            ('f = g + h', False, 'Det är A*, som också räknar med kostnaden hittills.'), ('När rutan lades in', False, 'Det gäller BFS och DFS.')], 'Vad betyder ”girig” här?', 1)
    b = mc('Vad jämför A* när den väljer nästa ruta?', 'f = g + h', 'A* tar hänsyn både till vad vägen hittills har kostat och till uppskattningen kvar.',
           [('f = g + h', True, 'Därför hittar A* en billigaste väg när h aldrig överskattar.'), ('Bara h', False, 'Det är girig bäst först.'),
            ('Bara g', False, 'A* använder också h för att styra mot målet.'), ('Antalet grannar', False, 'Antalet grannar påverkar inte valet.')],
           'A* lägger ihop två värden.', 1)
    c = mc('Vilken av sökningarna kan lockas in på en dyr väg bara för att vägen verkar leda nära målet?', 'Girig bäst först',
           'Eftersom girig bäst först bara tittar på h ser den inte att till exempel is eller lera gör vägen dyr. A* räknar med g och undviker det.',
           [('Girig bäst först', True, 'Den ser bara h och missar kostnaden hittills.'), ('A*', False, 'A* räknar med g och märker när en väg blir dyr.'),
            ('Båda lika mycket', False, 'A* skyddas av att g ingår i f.'), ('Ingen av dem', False, 'Girig bäst först kan välja en dyr väg, se exemplen med is och lera.')],
           'Vilken av dem bryr sig inte om kostnaden hittills?', 3)
    return teori('2.69', 'astar_sokning', 'Girig bäst först eller A*', p('Frågorna jämför de två informerade sökningarna girig bäst först och A*.'), [a, b, c],
                 'Girig bäst först sorterar efter h, A* efter f = g + h.', ['begrepp', 'resonemang'])


def t270():
    a = mc('Vad gör en sökning informerad?', 'Den använder en heuristik', 'En informerad sökning använder en uppskattning h av hur långt det är kvar till målet för att välja ordning.',
           [('Den använder en uppskattning av avståndet kvar till målet', True, 'Uppskattningen kallas heuristik.'),
            ('Den undersöker alla rutor', False, 'Även oinformerade sökningar kan undersöka alla rutor.'),
            ('Den har en karta över hela labyrinten', False, 'Alla sökningarna här använder samma karta. Skillnaden är om h används.'),
            ('Den hittar alltid den kortaste vägen', False, 'Girig bäst först är informerad men hittar inte alltid den kortaste vägen.')], 'Vad är h?', 1)
    b = mc('Vilken av sökningarna är informerad?', 'A*', 'A* använder h. BFS och DFS gör det inte.',
           [('A*', True, 'A* använder f = g + h.'), ('BFS', False, 'BFS använder en FIFO-kö utan h.'),
            ('DFS', False, 'DFS använder en stack utan h.'), ('En sökning som tar rutorna i bokstavsordning', False, 'Bokstavsordning säger inget om var målet ligger.')],
           'Vilken sökning använder h?', 1)
    return teori('2.70', 'astar_sokning', 'Informerad sökning', p('Frågorna handlar om vad som skiljer informerade sökningar från oinformerade.'), [a, b],
                 'Informerade sökningar använder en heuristik.')


def t271():
    a = mc('Vad krävs av h för att A* säkert ska hitta den billigaste vägen?', 'h får aldrig överskatta',
           'Om h aldrig är större än den verkliga kostnaden kvar kan A* inte luras att tro att en bra väg är sämre än den är.',
           [('h får aldrig vara större än den verkliga kostnaden kvar', True, 'En sådan heuristik kallas tillåten eller optimistisk.'),
            ('h måste vara exakt lika med den verkliga kostnaden kvar', False, 'Det räcker att h inte överskattar. Exakta värden är sällan kända.'),
            ('h ska vara så stort som möjligt', False, 'Om h överskattar kan A* missa den billigaste vägen.'),
            ('h måste räkna med alla väggar', False, 'Manhattanavståndet bortser från väggar och fungerar ändå, eftersom det inte överskattar.')],
           'Vad kan hända om h säger att en väg är dyrare än den egentligen är?', 4)
    b = mc('Varje steg kostar minst 1. Kan Manhattanavståndet då överskatta kostnaden kvar?', 'Varje steg minskar h med högst 1',
           'Varje steg flyttar högst en rad eller en kolumn. För att komma fram behövs därför minst h steg, och de kostar minst h.',
           [('Nej, minst h steg behövs alltid för att nå målet', True, 'Väggar och terräng kan bara göra vägen längre eller dyrare.'),
            ('Ja, när det finns väggar', False, 'Väggar gör den verkliga vägen längre, så h blir för litet, inte för stort.'),
            ('Ja, när rutorna kostar mer än 1', False, 'Dyrare rutor ökar den verkliga kostnaden, så h underskattar ännu mer.'),
            ('Det beror på var start ligger', False, 'Slutsatsen gäller från varje ruta.')], 'Hur mycket kan ett steg minska radskillnaden plus kolumnskillnaden?', 4)
    return teori('2.71', 'astar_varden', 'När h är en bra heuristik', p('Frågorna handlar om vilka heuristiker A* kan använda och fortfarande hitta den billigaste vägen.'), [a, b],
                 'Jämför h med den verkliga kostnaden kvar.', ['begrepp', 'resonemang'])


def t272():
    a = mc('Vilken nod tar en prioritetskö ut?', 'Den med lägst värde', 'I en prioritetskö sorteras noderna efter ett värde, här så att lägst värde tas ut först.',
           [('Den med lägst värde', True, 'Värdet avgör, inte när noden lades in.'), ('Den som lades in först', False, 'Det gäller en FIFO-kö.'),
            ('Den som lades in senast', False, 'Det gäller en stack.'), ('En slumpmässig nod', False, 'En prioritetskö följer värdena.')], 'Vad betyder prioritet?', 1)
    b = mc('Varför använder A* en prioritetskö och inte en FIFO-kö?', 'A* ska alltid ta lägst f',
           'A* tar alltid ut den ruta i öppna listan som har lägst f, oavsett när rutan lades in. Det kräver en kö som sorterar efter värde.',
           [('A* ska alltid ta ut rutan med lägst f, oavsett när den lades in', True, 'En prioritetskö gör just det.'),
            ('En FIFO-kö är för långsam', False, 'Skälet är vilken ruta som tas ut, inte hastigheten.'),
            ('A* behöver ta ut den senast inlagda rutan', False, 'Det gör en stack, och det vore DFS.'),
            ('A* lägger aldrig in mer än en ruta', False, 'A* lägger in många rutor i öppna listan.')], 'Vilken ruta vill A* ta ut?', 2)
    return teori('2.72', 'prioritetsko', 'Prioritetskön i A*', p('Frågorna handlar om prioritetsköer och hur A* använder dem.'), [a, b],
                 'En prioritetskö sorterar efter värde.')


def t273():
    a = mc('Vad är skillnaden mellan den kortaste och den billigaste vägen?', 'Steg jämfört med kostnad',
           'Den kortaste vägen har minst antal steg. Den billigaste vägen har lägst summa av kostnaderna. När rutor eller kanter kostar olika mycket kan de vara olika vägar.',
           [('Den kortaste har minst antal steg, den billigaste lägst summa av kostnaderna', True, 'De sammanfaller bara när varje steg kostar lika.'),
            ('Det är alltid samma väg', False, 'Is, lera eller dyra kanter kan göra den kortaste vägen dyr.'),
            ('Den billigaste vägen har alltid flest steg', False, 'Den kan ha lika många steg som den kortaste.'),
            ('Den kortaste vägen går alltid genom färre väggar', False, 'Man går aldrig genom väggar.')], 'Vad räknas, antal steg eller kostnad?', 1)
    b = mc('Rutorna kostar olika mycket. Hittar BFS då den billigaste vägen?', 'Inte säkert', 'BFS räknar antal steg och bryr sig inte om vad rutorna kostar.',
           [('Inte säkert, eftersom BFS räknar steg och inte kostnader', True, 'BFS kan välja en kort men dyr väg.'),
            ('Ja, alltid', False, 'BFS ser inte kostnaderna.'), ('Ja, om man börjar i ett hörn', False, 'Startens läge ändrar inte vad BFS räknar.'),
            ('Nej, BFS hittar aldrig någon väg då', False, 'BFS hittar en väg, men den behöver inte vara billigast.')], 'Vad sorterar BFS efter?', 2)
    return teori('2.73', 'viktade_vagar', 'Kortast eller billigast', p('Frågorna handlar om vägar där rutor eller kanter kostar olika mycket.'), [a, b],
                 'Antalet steg och kostnaden är två olika mått.')


# ======================================================================== minimax

def tree_fig(vals, root_max, title, leaf_names=False):
    import ai_speltrad as T
    r = T.build(vals, root_max)
    return game_tree(T.to_figure(r), root_max, title, leaf_names=leaf_names)


def t343():
    fig = tree_fig([[3, 8], [5, 6]], True, 'Spelträd med MAX i roten och två MIN-noder.')
    a = mc('Vad försöker MAX göra?', 'MAX vill ha så högt värde som möjligt', 'Lövens tal beskriver hur bra slutläget är för MAX. MAX väljer därför draget med störst värde.',
           [('Välja det drag som ger störst värde', True, 'Uppåtriktad triangel betyder MAX.'), ('Välja det drag som ger minst värde', False, 'Det gör MIN, motspelaren.'),
            ('Välja ett drag slumpmässigt', False, 'Minimax väljer det bästa draget.'), ('Välja draget längst till vänster', False, 'Placeringen avgör inte.')], 'Vad betyder talen i löven för MAX?', 1)
    b = mc('Vad antar minimax om motspelaren MIN?', 'MIN spelar så bra som möjligt', 'Minimax räknar med att MIN alltid väljer det drag som är sämst för MAX.',
           [('Att MIN alltid väljer det drag som är sämst för MAX', True, 'Därför väljer MIN minsta värdet.'),
            ('Att MIN gör slumpmässiga drag', False, 'Då skulle man räkna med medelvärden, inte minimum.'),
            ('Att MIN hjälper MAX', False, 'MIN och MAX har motsatta mål.'), ('Att MIN alltid gör samma drag som MAX', False, 'MIN väljer efter sina egna möjligheter.')],
           'Vad vill MIN uppnå?', 1)
    c = mc('Vad beskriver talen i löven?', 'Hur bra slutläget är för MAX', 'Ett högt tal är bra för MAX och dåligt för MIN.',
           [('Hur bra slutläget är för MAX', True, 'Därför vill MAX ha höga och MIN låga tal.'), ('Hur många drag spelet har tagit', False, 'Talen är värden, inte antal drag.'),
            ('Sannolikheten att MIN vinner', False, 'I minimax är talen värden för MAX.'), ('Ordningen som löven undersöks i', False, 'Ordningen anges av placeringen, inte av talen.')],
           'Vem vill ha höga tal?', 1)
    return teori('3.43', 'minimax', 'Minimax i teorin', fig + p('Frågorna handlar om hur minimax fungerar.'), [a, b, c], 'MAX vill ha höga värden och MIN låga.')


def t344():
    a = mc('Vad motsvarar en nod i ett spelträd?', 'Ett läge i spelet', 'Varje nod är ett läge, till exempel hur brädet ser ut i luffarschack.',
           [('Ett läge i spelet', True, 'Roten är läget just nu.'), ('Ett drag', False, 'Ett drag är en kant mellan två lägen.'),
            ('En spelare', False, 'Spelarna turas om mellan nivåerna.'), ('Ett slutresultat', False, 'Bara löven är slutlägen.')], 'Vad ser man om man stannar spelet vid en nod?', 1)
    b = mc('Vad motsvarar en kant mellan två noder?', 'Ett drag', 'En kant går från ett läge till läget efter ett drag.',
           [('Ett drag', True, 'Kanterna från en nod är de möjliga dragen.'), ('Ett läge', False, 'Lägena är noderna.'),
            ('Ett värde', False, 'Värden finns i löven och räknas fram i noderna.'), ('En regel för spelet', False, 'Reglerna avgör vilka kanter som finns.')], 'Vad tar spelet från ett läge till nästa?', 1)
    c = mc('Varför kan en spelagent inte räkna igenom hela spelträdet i schack?', 'Trädet blir för stort',
           'Varje drag ger många nya möjliga lägen. Antalet lägen växer så snabbt att hela trädet inte går att räkna igenom.',
           [('Antalet lägen växer så snabbt att trädet blir för stort', True, 'Därför räknar man bara några drag framåt.'),
            ('Schack har för få drag', False, 'Det är tvärtom: schack har väldigt många möjliga drag.'),
            ('Minimax fungerar bara för två drag', False, 'Minimax fungerar på hur djupa träd som helst, men det tar tid.'),
            ('Datorer kan inte jämföra tal', False, 'Jämförelserna är enkla. Det är mängden lägen som är problemet.')], 'Hur många nya lägen ger varje drag?', 2)
    return teori('3.44', 'minimax', 'Spelagentens träd', p('Frågorna handlar om hur ett spel beskrivs som ett spelträd för en spelagent.'), [a, b, c],
                 'Noder är lägen och kanter är drag.')


def t345():
    a = mc('Rotens minimaxvärde är 5. MIN spelar inte alltid sitt bästa drag. Vad kan MAX räkna med?', 'Minst 5',
           'Minimax räknar med att MIN spelar så bra som möjligt. Om MIN gör ett sämre drag kan MAX bara vinna på det, så MAX får minst 5.',
           [('Minst 5', True, 'Ett misstag av MIN kan bara ge MAX mer.'), ('Exakt 5', False, 'MAX kan få mer om MIN gör ett misstag.'),
            ('Högst 5', False, 'Rotvärdet är det sämsta MAX kan få när MAX spelar rätt.'), ('Ingenting går att säga', False, 'Rotvärdet är en garanti för MAX.')],
           'Vad antar minimax om MIN?', 3)
    b = mc('Varför växlar man mellan max och min för varje nivå i trädet?', 'Spelarna turas om',
           'På varannan nivå är det MAX tur att välja och på varannan MIN:s.',
           [('Spelarna turas om att göra drag', True, 'Varje nivå är en spelares tur.'), ('För att värdena ska bli lagom stora', False, 'Växlingen speglar turordningen, inte talens storlek.'),
            ('För att roten alltid ska få värdet 0', False, 'Rotens värde beror på löven.'), ('Det är en regel som bara gäller schack', False, 'Det gäller alla tvåpersonsspel med turordning.')],
           'Vems tur är det på varje nivå?', 1)
    return teori('3.45', 'minimax', 'Rotvärdet som garanti', p('Frågorna handlar om vad rotens minimaxvärde betyder.'), [a, b],
                 'Minimax räknar med att motspelaren spelar så bra som möjligt.', ['begrepp', 'resonemang'])


def t346():
    vals = [[9, 1], [4, 6]]
    assert A.minimax(vals, True) == 4
    fig = tree_fig(vals, True, 'Spelträd med MAX i roten, MIN-noderna A och B och löven 9, 1, 4 och 6.')
    a = num('Vilket värde får roten?', [step('MIN väljer i A och B', 'A = min(9, 1) = 1. B = min(4, 6) = 4.'), step('MAX väljer i roten', 'R = max(1, 4) = 4.')], 4,
            'Bestäm A och B först.', 1)
    b = mc('Lövet 9 är det högsta. Varför väljer MAX inte draget mot A?', 'MIN svarar med 1',
           'Om MAX går till A väljer MIN lövet 1. Via B kan MIN som bäst ge 4. MAX väljer därför B.',
           [('MIN skulle svara med draget som ger 1', True, 'MAX måste räkna med MIN:s bästa svar, inte med det bästa lövet.'),
            ('Lövet 9 kan inte nås', False, 'Det kan nås, men bara om MIN gör ett misstag.'),
            ('MAX väljer alltid draget längst till höger', False, 'Placeringen avgör inte.'),
            ('9 är för stort för att räknas', False, 'Alla löv räknas. Det är MIN:s val som gör A dåligt för MAX.')],
           'Vad gör MIN om MAX går till A?', 3)
    return teori('3.46', 'minimax', 'Varför inte det högsta lövet?', fig + p('Spelträdet söks igenom med minimax.'), [a, b], 'MAX måste räkna med MIN:s bästa svar.', ['begrepp', 'resonemang'])


def t349():
    import ai_speltrad as T
    vals = [[[4, 8], [2, 6]], [[7, 1], [5, 3]]]
    assert A.minimax(vals, True) == 6
    fig = tree_fig(vals, True, 'Spelträd med MAX i roten, MIN-noderna A och B och MAX-noderna C, D, E och F. Löven heter L1–L8.', leaf_names=True)
    a = mc('Spelet har tre drag. MAX börjar, sedan MIN och sist MAX. Vilket slutläge (löv) når spelet när båda gör sina bästa drag?', 'Följ värdena från roten',
           'C = 8, D = 6, så A = min(8, 6) = 6. E = 7, F = 5, så B = 5. Roten väljer A (6), MIN i A väljer D och MAX i D väljer lövet 6 (L4).',
           [('L2', False, 'L2 = 8 är C:s värde, men MIN i A väljer D i stället för C.'), ('L4', True, 'Roten → A → D → lövet 6.'),
            ('L5', False, 'L5 = 7 ligger under B, men roten väljer A.'), ('L7', False, 'L7 = 5 ger B:s värde, men B är sämre för MAX än A.')],
           'Bestäm alla nodvärden först och följ sedan valen från roten.', 2)
    b = num('Vilket värde har slutläget som spelet når, alltså rotens värde?', [step('A och B', 'A = min(8, 6) = 6. B = min(7, 5) = 5.'), step('Roten', 'R = max(6, 5) = 6.')], 6, 'Arbeta från löven och uppåt.', 2)
    return kg_task('3.49', 'minimax', 'Vägen till lövet', fig + p('Spelträdet söks igenom med minimax.'), [a, b], 'Följ i varje nod det barn som ger nodens värde.', ['procedur'])


# ======================================================================== beräkningar i labyrinter och grafer

M161 = ['S...#.', '.##...', '...#..', '.#...G']
M162 = ['.S.#', '.#..', '...#', '#..G']
M163 = ['S..#..', '.#....', '.#.##.', '...#.G']
M274 = ['S....', '.##..', '...#.', '.#..G']
M275 = ['.....', '.S.#G', '.....']


def t164():
    kids = {'S': ['A', 'B'], 'A': ['C', 'D'], 'B': ['E'], 'C': ['F'], 'E': ['G']}
    q, out, par = ['S'], [], {}
    while q:
        n = q.pop(0)
        out.append(n)
        if n == 'G':
            break
        for k in kids.get(n, []):
            par[k] = n
            q.append(k)
    assert out == ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G'] and par['G'] == 'E'
    tree = dict(nodes={'S': (200, 35), 'A': (110, 110), 'B': (290, 110), 'C': (60, 185), 'D': (160, 185), 'E': (290, 185), 'F': (60, 260), 'G': (290, 260)},
                edges=[('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'G')], start='S', goals=['G'], width=380,
                title='Sökträd: S har barnen A och B, A har C och D, C har F, B har E och E har målet G.')
    intro = search_tree(**tree) + p('Trädet söks igenom med BFS (vänster gren först).')
    a = num('Hur många noder har tagits ut när målet tas ut, inklusive S och målet?',
            [step('Nivå för nivå', 'Nivå 0: S. Nivå 1: A, B. Nivå 2: C, D, E. Nivå 3: F, G.'), step('Räkna', 'F lades in före G och tas ut före. Totalt 8 noder.')], 8,
            'Ta alla noder på en nivå innan nästa nivå.', 2)
    b = val('Vilken nod lägger in målet G i kön?', [step('G är barn till E', 'När E tas ut läggs G in längst bak i kön.')],
            [alt('E', True, 'G är E:s barn och läggs in när E tas ut.'), alt('B', False, 'B lägger in E, som i sin tur lägger in G.'),
             alt('F', False, 'F är C:s barn och har inga egna barn.'), alt('S', False, 'S lägger bara in A och B.')], 'Vilken nod är G:s förälder?', 1)
    return kg_task('1.64', 'ko_sokning', 'Vem lägger in målet?', intro, [a, b], 'En nods barn läggs in i kön när noden tas ut.', ['procedur'])


def t275():
    s, g = A.parse(M275)
    nb = {A.cname(v): A.manhattan(v, g) for v in A.neigh(M275, s)}
    assert nb == {'A2': 4, 'B3': 2, 'C2': 4, 'B1': 4} and A.cname(A.greedy(M275)['order'][1]) == 'B3'
    intro = maze(M275, s, g) + p('Labyrinten söks igenom med girig bäst först (h = Manhattanavstånd).')
    a = num('Hur många grannar har start?', [step('Pröva fyra riktningar', 'A2 uppåt, B3 åt höger, C2 nedåt och B1 åt vänster. Ingen av dem är en vägg.')], 4,
            'Titta upp, höger, ned och vänster från start.', 1)
    b = val('Vilken granne tar girig bäst först ut efter start?',
            [step('h för grannarna', 'A2: 1 + 3 = 4. B3: 0 + 2 = 2. C2: 1 + 3 = 4. B1: 0 + 4 = 4.'), step('Lägst h', 'B3 har h = 2.')],
            [alt('A2', False, 'A2 ligger en rad upp och har h = 1 + 3 = 4.'), alt('B3', True, 'B3 ligger på samma rad som målet och har lägst h = 2.'),
             alt('C2', False, 'C2 ligger en rad ned och har h = 1 + 3 = 4.'), alt('B1', False, 'B1 ligger längst från målet bland grannarna, h = 4.')], 'Jämför h för de fyra grannarna.', 1)
    c = num('Vilket h-värde har den rutan?', [step('h = radskillnad + kolumnskillnad', 'B3 och målet B5: 0 + 2 = 2.')], 2, 'Rutan och målet ligger på samma rad.', 1)
    return kg_task('2.75', 'astar_sokning', 'Girig bäst först bland fyra grannar', intro, [a, b, c], 'Girig bäst först väljer lägst h.', ['procedur'], 1)


def t276():
    rows = ['S.....', '.##.#.', '......', '.#...G']
    s, g = A.parse(rows)
    marks = {(0, 5): 'P', (2, 3): 'Q', (3, 2): 'R'}
    hv = {k: A.manhattan(c, g) for c, k in marks.items()}
    assert hv == {'P': 3, 'Q': 3, 'R': 3}
    gv = {'P': 5, 'Q': 6, 'R': 4}
    f = {k: gv[k] + hv[k] for k in gv}
    assert f == {'P': 8, 'Q': 9, 'R': 7}
    intro = (maze(rows, s, g, marks, extra_legend=MARK) + p('Labyrinten söks igenom med A* (h = Manhattanavstånd). Rutorna P, Q och R ligger i öppna listan.') +
             tab(['Ruta', 'g'], [[k, str(v)] for k, v in gv.items()]))
    a = val('Vilken av rutorna tar A* ut först?',
            [step('Alla tre har h = 3', 'P i A6: 3 + 0. Q i C4: 1 + 2. R i D3: 0 + 3.'), step('f = g + h', 'P: 5 + 3 = 8. Q: 6 + 3 = 9. R: 4 + 3 = 7.')],
            [alt('P', False, 'P har f = 5 + 3 = 8, högre än R:s 7.'), alt('Q', False, 'Q har högst g och f = 9.'), alt('R', True, 'R har lägst g och därmed lägst f = 7, eftersom alla har samma h.')],
            'Räkna h för varje ruta. Vad händer när h är lika?', 2)
    b = num('Vilket f-värde har Q?', [step('f = g + h', 'Q: 6 + 3 = 9.')], 9, 'Lägg ihop g från tabellen och h från figuren.', 1)
    return kg_task('2.76', 'astar_sokning', 'Samma h, olika g', intro, [a, b], 'När h är lika avgör g vilken ruta som har lägst f.', ['procedur'])


G277 = dict(nodes={'S': (50, 150), 'A': (180, 50), 'B': (330, 50), 'M': (450, 150)},
            edges=[('S', 'M', 10), ('S', 'A', 2), ('A', 'B', 3), ('B', 'M', 2)])


def t277():
    r = A.ucs_graph(G277['edges'], 'S', 'M')
    assert r['cost'] == 7 and r['path'] == ['S', 'A', 'B', 'M']
    svg = weighted_graph(G277['nodes'], G277['edges'], 'S', 'M', 'Graf med en direkt kant S–M och en väg via A och B. Talet vid varje kant är kostnaden.', 500)
    intro = svg + p('Talet vid varje kant är kostnaden att gå längs den.')
    a = num('Vad kostar den direkta vägen S → M?', [step('En enda kant', 'Kanten S–M kostar 10.')], 10, 'Läs av talet på kanten.', 1)
    b = num('Vad kostar vägen S → A → B → M?', [step('Summera', '2 + 3 + 2 = 7.')], 7, 'Lägg ihop de tre kanterna.', 1)
    c = num('Hur mycket billigare är vägen via A och B än den direkta vägen?', [step('Jämför', '10 − 7 = 3.')], 3, 'Ta skillnaden mellan kostnaderna.', 2)
    return kg_task('2.77', 'viktade_vagar', 'Den direkta vägen och omvägen', intro, [a, b, c], 'Färre kanter betyder inte alltid lägre kostnad.', ['procedur'], 1)


def build_all():
    return [t155(), t156(), t157(), t158(), t159(), t160(),
            K.bfs_task('1.61', 'BFS i 4 × 6', M161, 8, ['avst3', 'k', 'steg'], 'Skriv upp kön efter varje uttag.', (1, 2, 2)),
            K.dfs_task('1.62', 'DFS från en ruta i övre raden', M162, 3, 'DFS fortsätter alltid från den senast besökta rutan.'),
            K.dfs_task('1.63', 'DFS och en kortare väg', M163, 8, 'DFS backar först när det tar stopp.'),
            t164(),
            t267(), t268(), t269(), t270(), t271(), t272(), t273(),
            K.astar_task('2.74', 'A* längs översta raden', M274, 6, 'Räkna f = g + h för grannarna till varje uttagen ruta.'),
            t275(), t276(), t277(),
            t343(), t344(), t345(), t346(),
            K.mm_kg('3.47', [[[3, -2], [4, 1]], [[-5, 6], [2, 0]], [[1, 7], [-3, 8]]], True, 'H', 'Tre nivåer med negativa tal: var noga med tecknen.', (2, 2, 2)),
            K.mm_kg('3.48', [[[5, 2], [1, 4]], [[3, 6], [7, 0]]], False, 'F', 'Roten är en MIN-nod.', (2, 2, 2)),
            t349()]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = build_all()
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    assert len({u['id'] for u in bank}) == len(bank)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya i denna omgång.')


if __name__ == '__main__':
    main()
