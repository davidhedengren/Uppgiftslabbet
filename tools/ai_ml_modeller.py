"""AI-banken 2026-11-12, kapitel 4 del 2: regression, kNN och k-means, neurala nätverk.

Används av bygg-ai-maskininlarning-2026-11-12.py (listan NYA). Alla svar räknas fram här med
exakta bråk och kontrolleras oberoende i tools/ai-maskininlarning-2026-11-12.test.js.
"""
from fractions import Fraction as Fr

from ai_ml import p, f, exakt, num, dec, fv, namn, falt, uppgift, diagram, neuron_svg, natverk_svg, d2, step, tab  # noqa: F401

NYA = []


def ny(fn):
    NYA.append(fn)
    return fn


def mse(pts, k, m):
    res = [Fr(y) - (Fr(k) * x + Fr(m)) for x, y in pts]
    return res, sum(r * r for r in res) / len(res)


# ======================================================================== regression: linjär regression

@ny
def t440():
    pts = [(2, 5), (4, 9), (6, 10), (8, 15)]
    k, m = Fr(3, 2), 2
    res, e = mse(pts, k, m)
    assert [float(r) for r in res] == [0, 1, -1, 1] and e == Fr(3, 4)
    intro = (diagram([(x, y, 'A', '') for x, y in pts], 'Punktdiagram med fyra dagar och regressionslinjen y = 1,5x + 2.', 9, 16,
                     'soltimmar', 'sålda glassar (tiotal)', linjer=[(k, m, '')], ystep=2)
             + p('En kiosk vill förutsäga hur många glassar den säljer utifrån antalet soltimmar. Fyra dagar är markerade: '
                 '(2, 5), (4, 9), (6, 10) och (8, 15). En AI har anpassat linjen y = 1,5x + 2, där x är antalet soltimmar och y antalet glassar i tiotal.'))
    a = num('Hur många glassar (i tiotal) förutsäger modellen en dag med 4 soltimmar?', [step('Sätt in x = 4 i y = 1,5x + 2', '1,5 · 4 + 2 = 6 + 2 = 8.')], 8,
            'Sätt in x = 4 i linjens ekvation.', 1)
    b = num('Den dagen såldes 9 tiotal glassar. Hur stort är modellens fel den dagen, alltså verkligt värde minus förutsagt värde?',
            [step('Fel = verkligt − förutsagt', '9 − 8 = 1.')], 1, 'Jämför det verkliga värdet med modellens förutsägelse.', 1)
    c = dec('Räkna ut felet för varje dag, kvadrera felen och ta medelvärdet. Hur stort blir det? Talet kallas medelkvadratfel.',
            [step('Förutsägelser med y = 1,5x + 2', 'x = 2: 5. x = 4: 8. x = 6: 11. x = 8: 14.'),
             step('Fel = verkligt − förutsagt', '5 − 5 = 0, 9 − 8 = 1, 10 − 11 = −1 och 15 − 14 = 1.'),
             step('Medelkvadratfel = medelvärdet av felen i kvadrat', '(0² + 1² + (−1)² + 1²) / 4 = 3/4 = 0,75.')], e,
            'Räkna felet för varje dag, kvadrera och ta medelvärdet.', 3)
    return uppgift('4.40', 'regression', 'Linjär regression', intro, [a, b, c], 'Förutsägelse: sätt in x. Fel: verkligt minus förutsagt.', ['procedur'])


@ny
def t441():
    intro = p('En AI ska förutsäga priset på en lägenhet utifrån ytan. Den använder modellen pris = k · yta + m, där priset är i tusental kronor '
              'och ytan i kvadratmeter. Modellen har tränats på lägenheter mellan 20 och 120 m² och fått k = 40 och m = 600.')
    a = num('Vilket pris (i tusental kronor) förutsäger modellen för en lägenhet på 65 m²?', [step('pris = k · yta + m', '40 · 65 + 600 = 2 600 + 600 = 3 200.')], 3200,
            'Sätt in ytan i formeln.', 1)
    b = fv('Vad betyder k = 40 i modellen?', 'Lutningen', 'För varje extra kvadratmeter ökar det förutsagda priset med 40 tusen kronor.',
           [('Priset ökar med 40 tusen kronor för varje extra kvadratmeter', True, 'k är linjens lutning.'),
            ('Alla lägenheter kostar 40 tusen kronor', False, 'Priset beror på ytan.'),
            ('Lägenheten är 40 m²', False, 'k är inte en yta utan en ökning per kvadratmeter.'),
            ('Priset när ytan är 0', False, 'Det är m, där linjen skär y-axeln.')],
           'Hur mycket ändras priset när ytan ökar med 1?', 1)
    c = fv('Någon använder modellen för en villa på 400 m². Vad är rimligt att säga om förutsägelsen?', 'Långt utanför mätvärdena',
           'Modellen har bara sett lägenheter mellan 20 och 120 m². Det linjära sambandet behöver inte gälla för så stora bostäder.',
           [('Den är osäker, eftersom 400 m² ligger långt utanför de data modellen tränats på', True, 'Modellen vet inget om så stora bostäder.'),
            ('Den är säker, eftersom en linje gäller för alla x', False, 'Ett samband som gäller inom ett intervall behöver inte gälla långt utanför det.'),
            ('Modellen kan inte räkna ut något alls', False, 'Den kan räkna ut ett tal, men talet är osäkert.'),
            ('Priset blir alltid för lågt', False, 'Man vet inte om det blir för högt eller för lågt.')],
           'Har modellen sett några bostäder i den storleken?', 3, oppen=True)
    return uppgift('4.41', 'regression', 'Linjär regression', intro, [a, b, c], 'k är lutningen, m är värdet när x = 0.', ['procedur', 'begrepp'])


@ny
def t442():
    intro = (diagram([(1, 33, 'A', ''), (3, 44, 'A', ''), (5, 48, 'A', ''), (8, 58, 'A', '')], 'Punktdiagram med studietid och provpoäng och linjen y = 4x + 30.',
                     10, 80, 'timmar', 'poäng', linjer=[(4, 30, '')], ystep=10)
             + p('En AI har studerat elevers studietid och provresultat. Den har anpassat modellen poäng = 4 · timmar + 30.'))
    a = num('Hur många poäng förutsäger modellen för en elev som pluggar 6 timmar?', [step('Sätt in 6 timmar', '4 · 6 + 30 = 24 + 30 = 54.')], 54,
            'Sätt in antalet timmar i formeln.', 1)
    b = num('En elev pluggade 8 timmar och fick 58 poäng. Hur stort är modellens fel för eleven, alltså verkligt värde minus förutsagt värde?',
            [step('Modellens förutsägelse', '4 · 8 + 30 = 62.'), step('Fel = verkligt − förutsagt', '58 − 62 = −4.')], -4,
            'Räkna först ut vad modellen förutsäger för 8 timmar.', 2)
    c = fv('Vad betyder talet 30 i modellen?', 'Värdet när x = 0', 'Med 0 timmars plugg förutsäger modellen 30 poäng.',
           [('Modellen förutsäger 30 poäng för en elev som inte pluggar alls', True, '30 är värdet när timmar = 0.'),
            ('Varje timme ger 30 poäng till', False, 'Varje timme ger 4 poäng till, det är lutningen.'),
            ('Provet har 30 frågor', False, 'Modellen säger inget om antalet frågor.'),
            ('Ingen elev får under 30 poäng', False, 'Verkliga elever kan få färre poäng än modellen förutsäger.')],
           'Vad blir poängen om timmar = 0?', 1)
    return uppgift('4.42', 'regression', 'Linjär regression', intro, [a, b, c], 'Fel = verkligt − förutsagt. Felet kan vara negativt.', ['procedur', 'begrepp'])


@ny
def t443():
    intro = (diagram([(1, 185, 'A', ''), (3, 135, 'A', ''), (5, 95, 'A', ''), (7, 65, 'A', '')], 'Punktdiagram med bilars ålder och värde och linjen y = −20x + 200.',
                     10, 200, 'ålder (år)', 'värde (tkr)', linjer=[(-20, 200, '')], ystep=50)
             + p('En bilhandlare använder modellen värde = −20 · ålder + 200 för en viss bilmodell. Värdet är i tusental kronor och åldern i år. '
                 'Modellen bygger på bilar som är 1 till 7 år gamla.'))
    a = num('Vilket värde (i tusental kronor) förutsäger modellen för en bil som är 4 år?', [step('Sätt in ålder = 4', '−20 · 4 + 200 = −80 + 200 = 120.')], 120,
            'Sätt in åldern i formeln.', 1)
    b = fv('Vad betyder talet −20 i modellen?', 'Negativ lutning', 'Värdet minskar med 20 tusen kronor för varje år bilen blir äldre.',
           [('Bilen tappar 20 tusen kronor i värde för varje år', True, 'Negativ lutning betyder att y minskar när x ökar.'),
            ('Bilen kostar 20 tusen kronor', False, 'En ny bil är värd 200 tusen kronor enligt modellen.'),
            ('Bilen ökar 20 tusen kronor i värde varje år', False, 'Minustecknet betyder att värdet minskar.'),
            ('Bilen är 20 år gammal', False, '−20 är en ändring per år, inte en ålder.')],
           'Vad händer med värdet när åldern ökar med 1?', 1)
    c = num('Vid vilken ålder förutsäger modellen att bilen är värd 0 kr?', [step('Sätt värdet till 0', '−20 · ålder + 200 = 0.'), step('Lös ut åldern', '20 · ålder = 200, så ålder = 10.')],
            10, 'Lös ekvationen −20 · ålder + 200 = 0.', 2)
    d = fv('Är det rimligt att en 10 år gammal bil är värd 0 kr?', 'Utanför de data modellen bygger på',
           'Modellen bygger på bilar som är 1–7 år. Gamla bilar har oftast kvar ett visst värde, så sambandet slutar troligen vara linjärt.',
           [('Nej, modellen bygger bara på bilar upp till 7 år, och värdet sjunker troligen långsammare för äldre bilar', True,
             'En modell ska inte användas långt utanför de data den bygger på.'),
            ('Ja, modellen räknar alltid rätt', False, 'Modellen är en förenkling som bara gäller inom ett visst intervall.'),
            ('Ja, alla bilar är värdelösa efter 10 år', False, 'Många tio år gamla bilar säljs för pengar.'),
            ('Nej, eftersom lutningen borde vara positiv', False, 'Bilar tappar i värde, så en negativ lutning är rimlig.')],
           'Vilka åldrar fanns i datan?', 3, oppen=True)
    return uppgift('4.43', 'regression', 'Linjär regression', intro, [a, b, c, d], 'En negativ lutning betyder att y minskar när x ökar.', ['procedur', 'resonemang'])


@ny
def t444():
    intro = p('En AI har lärt sig hur fort batteriet i en mobil laddas ur när man spelar ett visst spel. Modellen är batteri = 100 − 8 · t, '
              'där batteriet är i procent och t är tiden i timmar.')
    a = num('Hur många procent förutsäger modellen att det finns kvar efter 5 timmar?', [step('Sätt in t = 5', '100 − 8 · 5 = 100 − 40 = 60.')], 60, 'Sätt in t = 5.', 1)
    b = num('Efter hur många timmar förutsäger modellen att batteriet är nere på 20 %?', [step('Sätt batteriet till 20', '100 − 8t = 20.'), step('Lös ut t', '8t = 80, så t = 10.')],
            10, 'Lös ekvationen 100 − 8t = 20.', 2)
    c = dec('Efter hur många timmar förutsäger modellen att batteriet är helt tomt?', [step('Sätt batteriet till 0', '100 − 8t = 0.'), step('Lös ut t', '8t = 100, så t = 12,5.')],
            Fr(25, 2), 'Lös ekvationen 100 − 8t = 0.', 2)
    d = fv('Modellen ger −20 % efter 15 timmar. Vad visar det?', 'Modellen gäller bara i ett visst intervall',
           'Ett batteri kan inte ha mindre än 0 %. Den linjära modellen gäller bara så länge batteriet laddas ur, alltså mellan 0 och 12,5 timmar.',
           [('Modellen gäller bara mellan 0 och 12,5 timmar, eftersom batteriet inte kan bli negativt', True, 'Utanför det intervallet säger modellen inget vettigt.'),
            ('Batteriet har lånat ström av telefonen', False, 'Ett batteri kan inte ha negativ laddning.'),
            ('Modellen har räknat fel', False, 'Räkningen stämmer, men modellen används utanför sitt intervall.'),
            ('Mobilen laddas upp igen', False, 'Modellen beskriver bara urladdning.')],
           'Kan ett batteri ha mindre än 0 %?', 3, oppen=True)
    return uppgift('4.44', 'regression', 'Linjär regression', intro, [a, b, c, d], 'Sätt in värden eller lös ekvationen för t.', ['procedur', 'resonemang'])


@ny
def t445():
    pts = [(1, 2), (2, 4), (3, 5), (4, 9)]
    _, ea = mse(pts, 2, 0)
    _, eb = mse(pts, 1, 2)
    assert ea == Fr(1, 2) and eb == Fr(5, 2)
    intro = (diagram([(x, y, 'A', '') for x, y in pts], 'Punktdiagram med fyra mätningar och två linjer, A: y = 2x och B: y = x + 2.', 5, 10,
                     'veckor', 'höjd (dm)', linjer=[(2, 0, 'A'), (1, 2, 'B')])
             + p('En odlare mäter hur höga solrosorna är. Mätningarna är (1, 2), (2, 4), (3, 5) och (4, 9), där x är antalet veckor och y höjden i dm. '
                 'Två AI-modeller föreslår var sin linje: A: y = 2x och B: y = x + 2.'))
    a = dec('Bestäm medelkvadratfelet för linje A, alltså medelvärdet av felen i kvadrat.',
            [step('Förutsägelser med y = 2x', '2, 4, 6 och 8.'), step('Fel = verkligt − förutsagt', '0, 0, −1 och 1.'),
             step('Medelkvadratfel = medelvärdet av felen i kvadrat', '(0 + 0 + 1 + 1) / 4 = 0,5.')], ea, 'Räkna felet för varje punkt, kvadrera och ta medelvärdet.', 2)
    b = dec('Bestäm medelkvadratfelet för linje B.',
            [step('Förutsägelser med y = x + 2', '3, 4, 5 och 6.'), step('Fel = verkligt − förutsagt', '−1, 0, 0 och 3.'),
             step('Medelkvadratfel = medelvärdet av felen i kvadrat', '(1 + 0 + 0 + 9) / 4 = 2,5.')], eb, 'Gör på samma sätt som för A.', 2)
    c = fv('Vilken linje passar bäst till mätningarna?', 'Lägst medelkvadratfel', 'A har medelkvadratfelet 0,5 och B har 2,5. Ett lägre medelkvadratfel betyder att linjen ligger närmare punkterna.',
           [('Linje A, eftersom den har lägre medelkvadratfel', True, 'Linjär regression väljer just den linje som har lägst medelkvadratfel.'),
            ('Linje B, eftersom den går genom två punkter exakt', False, 'B missar den sista punkten med 3, och det väger tungt i kvadrat.'),
            ('Linje B, eftersom den har högre medelkvadratfel', False, 'Ett högre medelkvadratfel betyder att linjen ligger längre från punkterna.'),
            ('De passar lika bra', False, 'Medelkvadratfelen skiljer sig mycket, 0,5 mot 2,5.')],
           'Är ett högt eller lågt medelkvadratfel bra?', 2)
    return uppgift('4.45', 'regression', 'Linjär regression', intro, [a, b, c], 'Den bästa linjen har lägst medelkvadratfel.', ['procedur'])


@ny
def t446():
    rows = [(0, 50), (5, 42), (10, 27)]
    res = [y - (50 - 2 * x) for x, y in rows]
    assert res == [0, 2, -3]
    intro = (tab(['Utetemperatur (°C)', 'Verklig förbrukning (kWh)'], [[str(x), str(y)] for x, y in rows])
             + p('En AI förutsäger hur mycket el ett hus använder för uppvärmning under ett dygn. Den använder modellen förbrukning = 50 − 2 · temperatur.'))
    a = num('Hur stort är modellens fel den dag då det var 10 °C ute, alltså verklig förbrukning minus förutsagd?', [step('Modellens förutsägelse', '50 − 2 · 10 = 30.'), step('Fel = verkligt − förutsagt', '27 − 30 = −3.')],
            -3, 'Räkna först ut vad modellen förutsäger vid 10 °C.', 2)
    b = num('Bestäm summan av felen i kvadrat för de tre dagarna.',
            [step('Förutsägelser', '0 °C: 50. 5 °C: 40. 10 °C: 30.'), step('Fel = verkligt − förutsagt', '0, 2 och −3.'),
             step('Kvadrera och summera', '0² + 2² + (−3)² = 0 + 4 + 9 = 13.')], 13, 'Räkna felet för varje dag och kvadrera det.', 2)
    c = fv('Varför kvadreras felen innan de läggs ihop?', 'Positiva och negativa fel ska inte ta ut varandra',
           'Utan kvadrering blir 2 + (−3) = −1, som om felen nästan försvann. Kvadraterna är alltid positiva, och stora fel väger tyngre.',
           [('Så att positiva och negativa fel inte tar ut varandra, och så att stora fel väger tyngre', True, 'Därför används medelkvadratfel.'),
            ('För att talen ska bli större och lättare att läsa', False, 'Syftet är inte att få stora tal.'),
            ('För att felen alltid är negativa', False, 'Felen kan vara både positiva och negativa.'),
            ('För att det är så man räknar ut lutningen', False, 'Lutningen räknas inte ut genom att kvadrera felen.')],
           'Vad händer om man bara lägger ihop 0, 2 och −3?', 3, oppen=True)
    return uppgift('4.46', 'regression', 'Linjär regression', intro, [a, b, c], 'Fel = verkligt − förutsagt.', ['procedur', 'resonemang'])


@ny
def t447():
    intro = p('Frågorna handlar om vad linjär regression kan och inte kan visa.')
    a = fv('En AI hittar ett tydligt samband: dagar då många glassar säljs drunknar också fler människor. Vilken slutsats är rimlig?', 'Samband är inte orsak',
           'Båda beror på en tredje sak: varmt väder. Då äter fler glass och fler badar. Glass orsakar inte drunkning.',
           [('Båda beror troligen på något annat, till exempel varmt väder', True, 'Ett samband i data visar inte vad som orsakar vad.'),
            ('Glass gör att människor drunknar', False, 'Ett samband betyder inte att det ena orsakar det andra.'),
            ('Man bör förbjuda glass vid stränder', False, 'Det bygger på en felaktig slutsats om orsak.'),
            ('Sambandet måste vara ett räknefel', False, 'Sambandet finns, men det har en annan förklaring.')],
           'Finns det något som får båda att öka samtidigt?', 3, oppen=True)
    b = fv('Vad gör linjär regression när den tränas?', 'Väljer linjen med minst fel', 'Algoritmen väljer k och m så att medelkvadratfelet blir så litet som möjligt.',
           [('Den väljer k och m så att medelkvadratfelet blir så litet som möjligt', True, 'Då ligger linjen så nära punkterna som möjligt.'),
            ('Den drar en linje genom de två första punkterna', False, 'Alla punkter används, inte bara två.'),
            ('Den väljer en linje som går genom alla punkter', False, 'Oftast finns ingen rak linje som går genom alla punkter.'),
            ('Den gissar en linje slumpmässigt', False, 'Linjen väljs så att felet blir minst.')],
           'Vad är det som ska bli så litet som möjligt?', 1)
    c = fv('Vilken data passar sämst för en linjär modell?', 'Ett samband som böjer sig',
           'En rak linje kan inte följa ett samband som först ökar och sedan minskar. Modellen blir då underanpassad.',
           [('Temperaturen under ett dygn, som stiger till eftermiddagen och sjunker på kvällen', True, 'Sambandet böjer sig, så en rak linje passar dåligt.'),
            ('Priset på bananer, som ökar lika mycket för varje kilo', False, 'Det är ett linjärt samband.'),
            ('Sträckan en bil kör i jämn fart', False, 'Sträckan ökar lika mycket varje minut, alltså linjärt.'),
            ('Kostnaden för bussbiljetter, som är lika för alla resor', False, 'Kostnaden växer lika mycket per resa.')],
           'Vilket samband kan inte beskrivas med en rak linje?', 2)
    return uppgift('4.47', 'regression', 'Linjär regression', intro, [a, b, c], 'Regression hittar samband, inte orsaker.', ['begrepp', 'resonemang'])


# ======================================================================== regression: gradientnedstigning

GD = p('Modellen tränas med gradientnedstigning. Vikten w uppdateras med regeln w<sub>ny</sub> = w − α · lutning. α (alfa) kallas '
       'inlärningstakten och bestämmer hur långa stegen blir. Lutningen visar hur felet ändras: är den positiv blir felet större om w ökar.')


@ny
def t448():
    w1 = Fr(3) - Fr(1, 10) * 4
    assert w1 == Fr(13, 5)
    a = dec('Just nu är w = 3, lutningen är 4 och α = 0,1. Vilket värde får w efter ett steg?',
            [step('Uppdateringsregeln: w<sub>ny</sub> = w − α · lutning', '3 − 0,1 · 4 = 3 − 0,4 = 2,6.')], w1, 'Multiplicera α med lutningen och dra av från w.', 2)
    b = fv('Varför dras α · lutning bort från w, i stället för att läggas till?', 'Gå nedför', 'Lutningen pekar åt det håll där felet ökar. Genom att gå åt motsatt håll minskar felet.',
           [('Lutningen pekar åt det håll där felet ökar, så man går åt andra hållet', True, 'Därför heter det gradientnedstigning.'),
            ('För att w alltid ska bli mindre', False, 'Om lutningen är negativ blir w större.'),
            ('Det spelar ingen roll om man lägger till eller drar av', False, 'Lägger man till ökar felet.'),
            ('För att α alltid är negativt', False, 'α är ett litet positivt tal.')],
           'Vad händer med felet om man går i lutningens riktning?', 3, oppen=True)
    c = fv('Vad kan hända om inlärningstakten α är alldeles för stor?', 'För långa steg', 'Stegen blir så långa att man hoppar förbi minimum, och felet kan öka i stället för att minska.',
           [('Stegen hoppar förbi minimum, så felet kan öka i stället för att minska', True, 'Därför väljer man ett lagom α.'),
            ('Träningen går långsammare', False, 'Det händer om α är för litet.'),
            ('Modellen blir alltid bättre ju större α är', False, 'För stora steg kan göra att träningen aldrig hittar minimum.'),
            ('Ingenting, α påverkar inte träningen', False, 'α bestämmer hur långa stegen är.')],
           'Tänk dig att du går nedför en backe med jättekliv.', 3, oppen=True)
    return uppgift('4.48', 'regression', 'Gradientnedstigning', GD, [a, b, c], 'w<sub>ny</sub> = w − α · lutning.', ['procedur', 'resonemang'])


@ny
def t449():
    w, vals = Fr(0), []
    for _ in range(2):
        w = w - Fr(1, 4) * 2 * (w - 5)
        vals.append(w)
    assert vals == [Fr(5, 2), Fr(15, 4)]
    intro = p('Felet för en modell är E(w) = (w − 5)², och lutningen är 2(w − 5). Gradientnedstigning startar i w = 0 med inlärningstakten α = 0,25 '
              'och regeln w<sub>ny</sub> = w − α · lutning.')
    a = dec('Vilket värde har w efter första steget?', [step('Lutningen 2(w − 5) i w = 0', '2(0 − 5) = −10.'), step('w<sub>ny</sub> = w − α · lutning', '0 − 0,25 · (−10) = 2,5.')],
            vals[0], 'Räkna först ut lutningen i w = 0.', 2)
    b = dec('Vilket värde har w efter andra steget?', [step('Lutningen 2(w − 5) i w = 2,5', '2(2,5 − 5) = −5.'), step('w<sub>ny</sub> = w − α · lutning', '2,5 − 0,25 · (−5) = 3,75.')],
            vals[1], 'Upprepa med det nya w.', 3)
    c = fv('Mot vilket värde närmar sig w om man fortsätter?', 'Minimum av felet', 'E(w) = (w − 5)² är minst när w = 5. Varje steg tar w halvvägs dit.',
           [('5', True, 'Där är felet 0 och lutningen 0, så stegen blir allt kortare.'), ('0', False, 'w rör sig bort från 0, mot minimum.'),
            ('Det växer utan gräns', False, 'Stegen blir kortare ju närmare 5 man kommer.'), ('2,5', False, '2,5 är bara värdet efter första steget.')],
           'Var är felet minst?', 2)
    return uppgift('4.49', 'regression', 'Gradientnedstigning', intro, [a, b, c], 'Lutningen blir mindre nära minimum, så stegen blir kortare.', ['procedur'])


@ny
def t450():
    lut = 2 * (1 - 4)
    w1 = 1 - Fr(1, 2) * lut
    assert lut == -6 and w1 == 4
    intro = p('Felet för en modell är E(w) = (w − 4)², och lutningen är 2(w − 4). Just nu är w = 1. Inlärningstakten är α = 0,5 och regeln är '
              'w<sub>ny</sub> = w − α · lutning.')
    a = num('Vad är lutningen i w = 1?', [step('Lutningen 2(w − 4)', '2(1 − 4) = 2 · (−3) = −6.')], lut, 'Sätt in w = 1 i 2(w − 4).', 1)
    b = num('Vilket värde får w efter ett steg?', [step('w<sub>ny</sub> = w − α · lutning', '1 − 0,5 · (−6) = 1 + 3 = 4.')], int(w1),
            'Minus en negativ lutning gör att w ökar.', 2)
    c = fv('Vad händer i nästa steg?', 'Lutningen är 0 i minimum', 'I w = 4 är lutningen 2(4 − 4) = 0. Steget blir 0, så w står kvar.',
           [('w står kvar på 4, eftersom lutningen där är 0', True, 'w = 4 är minimum av felet.'),
            ('w fortsätter att öka med 3', False, 'Stegets längd beror på lutningen, som nu är 0.'),
            ('w går tillbaka till 1', False, 'Det finns inget som drar tillbaka w.'),
            ('w blir negativt', False, 'Med lutningen 0 ändras inte w.')],
           'Räkna lutningen i w = 4.', 2)
    return uppgift('4.50', 'regression', 'Gradientnedstigning', intro, [a, b, c], 'En negativ lutning gör att w ökar.', ['procedur'])


@ny
def t451():
    w1 = 4 - Fr(3, 2) * 2 * (4 - 2)
    assert w1 == -2 and abs(w1 - 2) > abs(4 - 2)
    intro = p('Felet för en modell är E(w) = (w − 2)², och felet är minst när w = 2. Lutningen är 2(w − 2). Gradientnedstigning startar i w = 4 med en '
              'stor inlärningstakt, α = 1,5, och regeln w<sub>ny</sub> = w − α · lutning.')
    a = num('Vilket värde har w efter första steget?', [step('Lutningen 2(w − 2) i w = 4', '2(4 − 2) = 4.'), step('w<sub>ny</sub> = w − α · lutning', '4 − 1,5 · 4 = 4 − 6 = −2.')],
            -2, 'Räkna först ut lutningen i w = 4.', 2)
    c = fv('Före steget låg w 2 från minimum. Var ligger w efter steget?', 'Steget gick för långt',
           'w = −2 ligger 4 från minimum w = 2. Steget var så långt att w hoppade förbi minimum och hamnade längre bort än förut.',
           [('Längre från minimum, eftersom steget hoppade förbi', True, 'Inlärningstakten α är för stor.'),
            ('Närmare minimum', False, 'Avståndet ökade från 2 till 4.'),
            ('Precis i minimum', False, 'Minimum är w = 2, inte w = −2.'),
            ('På samma avstånd som förut', False, 'Avståndet ökade från 2 till 4.')],
           'Jämför avståndet från 4 till 2 med avståndet från −2 till 2.', 3)
    return uppgift('4.51', 'regression', 'Gradientnedstigning', intro, [a, c], 'För stort α kan få w att hoppa förbi minimum.', ['procedur', 'resonemang'])


@ny
def t452():
    intro = (tab(['Epok', '1', '2', '3', '4'], [['α = 0,001', '10', '9,9', '9,8', '9,7'], ['α = 0,1', '10', '4', '1,6', '0,6'], ['α = 2', '10', '30', '95', '280']])
             + p('Samma modell tränas med tre olika inlärningstakter. Tabellen visar felet efter varje epok (varv genom träningsdatan).'))
    a = fv('Vilken inlärningstakt är för liten?', 'Felet minskar mycket långsamt', 'Med α = 0,001 minskar felet bara med 0,1 per epok. Träningen skulle ta mycket lång tid.',
           [('α = 0,001', True, 'Små steg gör att det går långsamt.'), ('α = 0,1', False, 'Där minskar felet snabbt.'),
            ('α = 2', False, 'Där ökar felet, så α är för stort.'), ('Ingen av dem', False, 'α = 0,001 ger mycket långsam träning.')],
           'Vilken rad ändras nästan inte alls?', 2)
    b = fv('Vilken inlärningstakt är för stor?', 'Felet ökar', 'Med α = 2 ökar felet för varje epok. Stegen är så långa att minimum hoppas över.',
           [('α = 2', True, 'Felet går från 10 till 280.'), ('α = 0,1', False, 'Där minskar felet.'), ('α = 0,001', False, 'Där minskar felet, om än långsamt.'),
            ('Alla, eftersom felet inte blir 0', False, 'Felet behöver inte bli 0 efter fyra epoker.')],
           'Vilken rad växer?', 2)
    c = fv('Vilken inlärningstakt bör väljas?', 'Snabbt och stabilt', 'α = 0,1 ger ett fel som minskar snabbt och hela tiden.',
           [('α = 0,1', True, 'Felet går från 10 till 0,6 på fyra epoker.'), ('α = 2', False, 'Felet växer, träningen fungerar inte.'),
            ('α = 0,001', False, 'Den fungerar men är alldeles för långsam.'), ('Den största, eftersom den lär sig mest', False, 'Den största ger växande fel.')],
           'Vilken rad minskar snabbt utan att öka?', 1)
    return uppgift('4.52', 'regression', 'Gradientnedstigning', intro, [a, b, c], 'Jämför hur felet ändras i varje rad.', ['begrepp', 'resonemang'])


@ny
def t453():
    w1 = Fr(5) - Fr(1, 2) * Fr(4, 5)
    assert w1 == Fr(23, 5)
    a = dec('Just nu är w = 5, lutningen är 0,8 och α = 0,5. Vilket värde får w efter ett steg?',
            [step('Uppdateringsregeln: w<sub>ny</sub> = w − α · lutning', '5 − 0,5 · 0,8 = 5 − 0,4 = 4,6.')], w1, 'Räkna α · lutning först.', 1)
    b = fv('Efter många steg är lutningen 0. Vad betyder det?', 'Felet ändras inte där', 'Lutningen 0 betyder att felet varken ökar eller minskar om w ändras lite. Man har nått ett minimum.',
           [('Felet är som minst där, så w ändras inte längre', True, 'Steget α · 0 är 0.'),
            ('Felet är 0', False, 'Felet kan vara större än 0 även i minimum.'),
            ('Inlärningstakten har blivit 0', False, 'α är densamma, det är lutningen som är 0.'),
            ('Modellen har slutat fungera', False, 'Det betyder tvärtom att träningen har hittat ett minimum.')],
           'Vad blir α · lutning om lutningen är 0?', 2)
    c = fv('Felet har flera dalar, och gradientnedstigning stannar i en dal som inte är den djupaste. Vad kallas det?', 'Lokalt minimum',
           'Gradientnedstigning går alltid nedför från där den startar. Den kan fastna i en grund dal, ett lokalt minimum, utan att hitta den djupaste.',
           [('Ett lokalt minimum', True, 'Lutningen är 0 där, så stegen slutar, fast felet kunde vara lägre någon annanstans.'),
            ('Ett globalt minimum', False, 'Det globala minimum är den djupaste dalen.'),
            ('Överanpassning', False, 'Överanpassning handlar om skillnaden mellan träning och test.'),
            ('Ett för litet α', False, 'Även med lagom α kan man fastna i en grund dal.')],
           'Ser algoritmen hela landskapet eller bara lutningen där den står?', 3, oppen=True)
    return uppgift('4.53', 'regression', 'Gradientnedstigning', GD, [a, b, c], 'Lutningen 0 betyder att stegen slutar.', ['procedur', 'begrepp'])


@ny
def t454():
    E = lambda w: (w - 6) ** 2  # noqa: E731
    w1 = 10 - Fr(1, 4) * 2 * (10 - 6)
    w2 = w1 - Fr(1, 4) * 2 * (w1 - 6)
    assert (E(10), w1, E(w1), w2) == (16, 8, 4, 7)
    intro = p('En modell har felet E(w) = (w − 6)², med lutningen 2(w − 6). Gradientnedstigning startar i w = 10 med α = 0,25 och regeln '
              'w<sub>ny</sub> = w − α · lutning.')
    a = num('Hur stort är felet i startpunkten w = 10?', [step('Felet E(w) = (w − 6)²', '(10 − 6)² = 4² = 16.')], 16, 'Sätt in w = 10 i E(w).', 1)
    b = num('Vilket värde har w efter första steget?', [step('Lutningen 2(w − 6) i w = 10', '2 · 4 = 8.'), step('w<sub>ny</sub> = w − α · lutning', '10 − 0,25 · 8 = 8.')],
            int(w1), 'Räkna lutningen i w = 10 först.', 2)
    c = num('Hur stort är felet efter första steget?', [step('Felet E(w) = (w − 6)² i det nya w', '(8 − 6)² = 4.')], int(E(w1)), 'Sätt in det nya w i E(w).', 1)
    d = num('Vilket värde har w efter andra steget?', [step('Lutningen 2(w − 6) i w = 8', '2 · 2 = 4.'), step('w<sub>ny</sub> = w − α · lutning', '8 − 0,25 · 4 = 7.')],
            int(w2), 'Upprepa med w = 8.', 2)
    return uppgift('4.54', 'regression', 'Gradientnedstigning', intro, [a, b, c, d], 'Varje steg halverar här avståndet till w = 6.', ['procedur'])


@ny
def t455():
    w1 = Fr(-2) - Fr(1, 5) * (-3)
    assert w1 == Fr(-7, 5)
    a = fv('I vilken ordning sker ett steg när en modell tränas med gradientnedstigning?', 'Förutsäg, mät felet, räkna lutningen, uppdatera',
           'Modellen förutsäger först, sedan jämförs förutsägelsen med facit. Lutningen av felet visar hur vikten ska ändras, och sist uppdateras vikten.',
           [('Förutsäga, räkna ut felet, räkna ut lutningen, uppdatera vikten', True, 'Sedan upprepas samma steg många gånger.'),
            ('Uppdatera vikten, förutsäga, räkna ut felet', False, 'Man vet inte hur vikten ska ändras innan felet är känt.'),
            ('Räkna ut lutningen, förutsäga, uppdatera vikten', False, 'Lutningen är lutningen av felet, så felet måste räknas ut först.'),
            ('Räkna ut felet, förutsäga, uppdatera vikten', False, 'Felet kan inte räknas ut innan modellen har förutsagt.')],
           'Vad behövs för att kunna räkna ut felet?', 2)
    b = dec('Just nu är w = −2, lutningen är −3 och α = 0,2. Vilket värde får w efter ett steg?',
            [step('Uppdateringsregeln: w<sub>ny</sub> = w − α · lutning', '−2 − 0,2 · (−3) = −2 + 0,6 = −1,4.')], w1, 'Minus gånger minus blir plus.', 2)
    c = fv('Vad visar lutningen av felet?', 'Hur felet ändras när w ändras', 'Lutningen visar hur snabbt felet ökar eller minskar när w ändras lite, och åt vilket håll.',
           [('Hur mycket och åt vilket håll felet ändras när w ändras lite', True, 'Därför kan den användas för att välja riktning.'),
            ('Hur stort felet är', False, 'Felet kan vara stort fast lutningen är 0.'),
            ('Hur många steg som är kvar', False, 'Lutningen säger inget om antalet steg.'),
            ('Hur bra modellen är på testdata', False, 'Lutningen räknas på träningsfelet.')],
           'Tänk på lutningen i en backe.', 1)
    return uppgift('4.55', 'regression', 'Gradientnedstigning', GD, [a, b, c], 'w<sub>ny</sub> = w − α · lutning.', ['procedur', 'begrepp'])


# ======================================================================== knn_kmeans: kNN

def ordning(pts, q):
    d = {e: d2((x, y), q) for x, y, _, e in pts}
    return d, sorted(d, key=lambda e: (d[e], e))


def klass_k(pts, q, k):
    d, o = ordning(pts, q)
    assert d[o[k - 1]] < d[o[k]], (q, k)
    kl = {e: c for _, _, c, e in pts}
    rost = [kl[e] for e in o[:k]]
    vinn = max(set(rost), key=rost.count)
    assert rost.count(vinn) * 2 > k
    return vinn, o[:k], d


def avst_steg(pts, q, urval):
    d, _ = ordning(pts, q)
    pos = {e: (x, y) for x, y, _, e in pts}
    return '. '.join(f'{e}: ({pos[e][0]} − {q[0]})² + ({pos[e][1]} − {q[1]})² = {d[e]}'.replace('− -', '+ ') for e in urval) + '.'


def knn_fig(pts, q, titel, xmax, ymax, xl, yl, a_namn, b_namn):
    return diagram(pts + [(q[0], q[1], '?', 'Ny')], titel, xmax, ymax, xl, yl,
                   legend=f'Blå cirklar: {a_namn}. Orange kvadrater: {b_namn}. Vit ring: den nya punkten.')


KNN_INTRO = 'AI:n använder k närmaste grannar (kNN). Avståndet i kvadrat mellan två punkter är (Δx)² + (Δy)², och den nya punkten får den klass som flest av de k närmaste grannarna har.'


def klass_fv(pts, q, k, namn_, fraga, extra_fel=None, tn=2):
    vinn, nara, d = klass_k(pts, q, k)
    kl = {e: c for _, _, c, e in pts}
    andra = 'B' if vinn == 'A' else 'A'
    nara_txt = ', '.join(f'{e} ({namn_[kl[e]].lower()}, {d[e]})' for e in nara)
    alts = [(namn_[vinn], True, f'{sum(kl[e] == vinn for e in nara)} av de {k} närmaste är {namn_[vinn].lower()}.'),
            (namn_[andra], False, f'Bara {sum(kl[e] == andra for e in nara)} av de {k} närmaste är {namn_[andra].lower()}.' if k > 1 else
             f'Den närmaste grannen, {nara[0]}, är {namn_[vinn].lower()}.'),
            ('Det blir oavgjort', False, 'Med ett udda k och två klasser kan det inte bli oavgjort.'),
            (extra_fel or 'Det går inte att avgöra utan fler punkter', False, 'De givna punkterna räcker för att avgöra klassen.')]
    return fv(fraga, f'De {k} närmaste grannarna' if k > 1 else 'Den närmaste grannen', f'Avstånd i kvadrat: {nara_txt}.', alts,
              'Jämför avstånden i kvadrat och räkna klasserna bland de närmaste.', tn)


@ny
def t460():
    pts = [(1, 2, 'A', 'P1'), (2, 4, 'A', 'P2'), (3, 1, 'A', 'P3'), (6, 6, 'B', 'P4'), (7, 4, 'B', 'P5'), (5, 7, 'B', 'P6'), (4, 5, 'B', 'P7')]
    q = (3, 4)
    namn_ = {'A': 'Äpple', 'B': 'Päron'}
    _, nara, d = klass_k(pts, q, 3)
    assert nara == ['P2', 'P7', 'P1'] and d['P7'] == 2
    intro = (knn_fig(pts, q, 'Punktdiagram med sju frukter och en ny frukt i (3, 4).', 8, 8, 'vikt', 'sötma', 'äpple', 'päron')
             + p('En AI sorterar frukt utifrån vikt och sötma, båda i en skala 0–8. Sju frukter är redan klassade. En ny frukt har vikt 3 och sötma 4. ' + KNN_INTRO))
    a = num('Beräkna avståndet i kvadrat från den nya frukten till P7 (4, 5).', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(4 − 3)² + (5 − 4)² = 1 + 1 = 2.')], 2,
            'Räkna skillnaden i x och i y, kvadrera och lägg ihop.', 1)
    b = namn('Vilka tre frukter ligger närmast den nya frukten?',
             [step('Avstånd i kvadrat till de närmaste', avst_steg(pts, q, ['P2', 'P7', 'P1', 'P3'])), step('De tre minsta', 'P2 (1), P7 (2) och P1 (8).')],
             nara, 'Jämför avstånden i kvadrat, då slipper du räkna med rötter.', 2)
    c = klass_fv(pts, q, 3, namn_, 'Vad klassas den nya frukten som med k = 3?')
    return uppgift('4.60', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c], 'Hitta de k närmaste och låt dem rösta.', ['procedur'])


@ny
def t461():
    pts = [(1, 1, 'A', 'P1'), (4, 5, 'B', 'P2'), (6, 1, 'A', 'P3'), (5, 3, 'B', 'P4'), (7, 5, 'B', 'P5')]
    q = (5, 1)
    namn_ = {'A': 'Stannar kvar', 'B': 'Slutar'}
    d, _ = ordning(pts, q)
    assert d['P2'] == 17
    intro = (knn_fig(pts, q, 'Punktdiagram med fem kunder och en ny kund i (5, 1).', 8, 6, 'köp per månad', 'snittbelopp (hundratal kr)', 'stannar kvar', 'slutar')
             + p('Ett företag vill förutsäga vilka kunder som tänker sluta. Fem kunder är markerade. En ny kund ligger i punkten (5, 1). ' + KNN_INTRO))
    a = num('Beräkna avståndet i kvadrat från den nya kunden till P2 (4, 5).', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(4 − 5)² + (5 − 1)² = 1 + 16 = 17.')], 17,
            'Kvadrera skillnaden i x och i y och lägg ihop.', 1)
    b = klass_fv(pts, q, 1, namn_, 'Vad blir klassen för den nya kunden med k = 1?')
    c = klass_fv(pts, q, 3, namn_, 'Vad blir klassen för den nya kunden med k = 3?', tn=3)
    return uppgift('4.61', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c], 'Jämför avstånden i kvadrat.', ['procedur'])


@ny
def t462():
    intro = p('Frågorna handlar om hur valet av k påverkar k närmaste grannar (kNN).')
    a = fv('Vad händer med kNN om k = 1?', 'Bara den allra närmaste räknas', 'Klassen avgörs av en enda granne. En enda konstig punkt kan då ge fel klass.',
           [('Den nya punkten får samma klass som den allra närmaste grannen', True, 'Det gör metoden känslig för enstaka avvikande punkter.'),
            ('Den nya punkten får den vanligaste klassen i hela datan', False, 'Det händer om k är lika med antalet punkter.'),
            ('kNN fungerar inte med k = 1', False, 'Det fungerar, men blir känsligt för brus.'), ('Alla punkter röstar lika', False, 'Bara en punkt röstar.')],
           'Hur många grannar röstar?', 1)
    b = fv('Varför väljer man ofta ett udda k när det finns två klasser?', 'Undvika oavgjort', 'Med ett udda antal röster kan det inte bli lika mellan två klasser.',
           [('Då kan det inte bli oavgjort mellan de två klasserna', True, 'Till exempel 2 mot 1 eller 3 mot 2.'),
            ('Udda tal ger alltid rätt svar', False, 'Ett udda k undviker bara oavgjort, det garanterar inte rätt svar.'),
            ('Datorn räknar snabbare med udda tal', False, 'Det har inget med beräkningshastighet att göra.'),
            ('Jämna k är inte tillåtna', False, 'Jämna k är tillåtna, men kan ge oavgjort.')],
           'Vad kan hända med fyra grannar och två klasser?', 1)
    c = fv('Vad händer om k är lika stort som antalet punkter i datan?', 'Alla röstar', 'Alla nya punkter får då den klass som är vanligast i hela datan, oavsett var de ligger.',
           [('Alla nya punkter får samma klass, den vanligaste i datan', True, 'Var punkten ligger spelar ingen roll längre.'),
            ('Klassificeringen blir perfekt', False, 'Den blir tvärtom dålig, alla får samma svar.'),
            ('Bara de närmaste punkterna röstar', False, 'Alla punkter röstar när k är lika med antalet punkter.'),
            ('Det blir alltid oavgjort', False, 'Det blir den vanligaste klassen.')],
           'Hur många av punkterna är med och röstar?', 3, oppen=True)
    return uppgift('4.62', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c], 'Litet k är känsligt för brus, stort k suddar ut gränserna.', ['begrepp', 'resonemang'])


@ny
def t463():
    pts = [(6, 1, 'A', 'P1'), (8, 2, 'A', 'P2'), (7, 4, 'A', 'P3'), (5, 2, 'A', 'P4'), (1, 6, 'B', 'P5'), (2, 8, 'B', 'P6'), (3, 5, 'B', 'P7'), (1, 3, 'B', 'P8')]
    q = (4, 4)
    namn_ = {'A': 'Action', 'B': 'Romantik'}
    assert klass_k(pts, q, 1)[0] == 'B' and klass_k(pts, q, 3)[0] == 'A'
    d, _ = ordning(pts, q)
    intro = (knn_fig(pts, q, 'Punktdiagram med åtta filmer och en ny film i (4, 4).', 9, 9, 'biljakter', 'kärleksscener', 'action', 'romantik')
             + p('En streamingtjänst klassar filmer efter antalet biljakter och kärleksscener. Åtta filmer är redan klassade. En ny film har 4 biljakter '
                 'och 4 kärleksscener. ' + KNN_INTRO))
    a = num('Beräkna avståndet i kvadrat från den nya filmen till P4 (5, 2).', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(5 − 4)² + (2 − 4)² = 1 + 4 = 5.')], d['P4'],
            'Kvadrera skillnaden i x och i y och lägg ihop.', 1)
    b = klass_fv(pts, q, 1, namn_, 'Vad klassas den nya filmen som med k = 1?')
    c = klass_fv(pts, q, 3, namn_, 'Vad klassas den nya filmen som med k = 3?', tn=3)
    return uppgift('4.63', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c], 'Svaret kan bli olika för olika k.', ['procedur'])


@ny
def t464():
    pts = [(2, 6, 'A', 'P1'), (3, 7, 'A', 'P2'), (4, 6, 'A', 'P3'), (3, 5, 'A', 'P4'), (5, 4, 'B', 'P5'), (6, 3, 'B', 'P6'), (7, 2, 'B', 'P7'), (6, 1, 'B', 'P8')]
    q = (4, 4)
    namn_ = {'A': 'Ätlig', 'B': 'Giftig'}
    v1, n1, d = klass_k(pts, q, 1)
    v3, n3, _ = klass_k(pts, q, 3)
    assert v1 == 'B' and v3 == 'A' and n3 == ['P5', 'P4', 'P3']
    intro = (knn_fig(pts, q, 'Punktdiagram med åtta svampar och en ny svamp i (4, 4).', 8, 8, 'hattbredd (cm)', 'fotlängd (cm)', 'ätlig', 'giftig')
             + p('En svampapp jämför hattbredd och fotlängd med åtta svampar som redan är artbestämda. En ny svamp har hattbredd 4 cm och fotlängd 4 cm. ' + KNN_INTRO))
    a = namn('Vilka tre svampar ligger närmast den nya svampen?',
             [step('Avstånd i kvadrat till de närmaste', avst_steg(pts, q, ['P5', 'P4', 'P3', 'P6'])), step('De tre minsta', 'P5 (1), P4 (2) och P3 (4).')],
             n3, 'Jämför avstånden i kvadrat.', 2)
    b = klass_fv(pts, q, 3, namn_, 'Vad klassas den nya svampen som med k = 3?')
    c = fv('Med k = 3 blir svaret ätlig, men den allra närmaste svampen är giftig. Vad bör appen göra?', 'Visa osäkerheten',
           'Grannarna är oense, och ett fel kan vara livsfarligt. Appen bör tala om att den är osäker och inte säga att svampen är ätlig.',
           [('Varna för att den är osäker och inte säga att svampen är ätlig', True, 'När ett falskt ”ätlig” kan vara farligt ska appen vara försiktig.'),
            ('Säga ätlig, eftersom majoriteten bestämmer', False, 'Majoriteten är bara 2 mot 1, och ett fel kan vara livsfarligt.'),
            ('Byta till k = 1 så att svaret blir giftig', False, 'Att välja k efter önskat svar är inte en bra metod.'),
            ('Gissa slumpmässigt', False, 'En gissning hjälper inte användaren.')],
           'Hur allvarligt är det om appen säger ätlig om en giftig svamp?', 3, oppen=True)
    return uppgift('4.64', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c], 'Tänk på vad ett fel skulle innebära.', ['procedur', 'resonemang'])


@ny
def t465():
    pts = [(2, 2, 'A', 'P1'), (3, 1, 'A', 'P2'), (2, 4, 'A', 'P3'), (4, 3, 'A', 'P4'), (7, 8, 'B', 'P5'), (8, 6, 'B', 'P6'), (6, 7, 'B', 'P7'), (9, 9, 'B', 'P8')]
    q = (5, 4)
    namn_ = {'A': 'Lugn', 'B': 'Energisk'}
    v3, n3, d = klass_k(pts, q, 3)
    assert n3 == ['P4', 'P3', 'P7'] and v3 == 'A' and d['P7'] == 10
    intro = (knn_fig(pts, q, 'Punktdiagram med åtta låtar och en ny låt i (5, 4).', 10, 10, 'tempo', 'ljudstyrka', 'lugn', 'energisk')
             + p('En musikapp sorterar låtar efter tempo och ljudstyrka, båda i en skala 0–10. Åtta låtar är redan sorterade som lugna eller energiska. '
                 'En ny låt har tempo 5 och ljudstyrka 4. ' + KNN_INTRO))
    a = num('Beräkna avståndet i kvadrat från den nya låten till P7 (6, 7).', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(6 − 5)² + (7 − 4)² = 1 + 9 = 10.')], 10,
            'Kvadrera skillnaden i x och i y och lägg ihop.', 1)
    b = namn('Vilka tre låtar ligger närmast den nya låten?',
             [step('Avstånd i kvadrat till de närmaste', avst_steg(pts, q, ['P4', 'P3', 'P7', 'P1'])), step('De tre minsta', 'P4 (2), P3 (9) och P7 (10).')],
             n3, 'Räkna avståndet i kvadrat till punkterna nära den nya låten.', 2)
    c = klass_fv(pts, q, 3, namn_, 'Vad klassas den nya låten som med k = 3?')
    e = num('Man kan också mäta med Manhattanavstånd, |Δx| + |Δy|, som i A*. Vilket Manhattanavstånd har den nya låten till P7?',
            [step('Manhattanavstånd: |Δx| + |Δy|', '|6 − 5| + |7 − 4| = 1 + 3 = 4.')], 4, 'Lägg ihop skillnaderna i x och y utan att kvadrera.', 1)
    return uppgift('4.65', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c, e], 'Jämför avstånden i kvadrat.', ['procedur'])


@ny
def t466():
    pts = [(1, 0, 'A', 'P1'), (0, 1, 'A', 'P2'), (2, 1, 'A', 'P3'), (1, 2, 'A', 'P4'), (6, 5, 'B', 'P5'), (5, 7, 'B', 'P6'), (7, 6, 'B', 'P7'), (4, 4, 'B', 'P8')]
    q = (5, 4)
    namn_ = {'A': 'Inte spam', 'B': 'Spam'}
    v3, n3, d = klass_k(pts, q, 3)
    assert n3 == ['P8', 'P5', 'P7'] and v3 == 'B' and d['P4'] == 20
    intro = (knn_fig(pts, q, 'Punktdiagram med åtta mejl och ett nytt mejl i (5, 4).', 8, 8, 'länkar', 'utropstecken', 'inte spam', 'spam')
             + p('Ett e-postprogram jämför antalet länkar och utropstecken i ett nytt mejl med åtta mejl som redan är sorterade. '
                 'Det nya mejlet har 5 länkar och 4 utropstecken. ' + KNN_INTRO))
    a = num('Beräkna avståndet i kvadrat från det nya mejlet till P4 (1, 2).', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(1 − 5)² + (2 − 4)² = 16 + 4 = 20.')], 20,
            'Kvadrera skillnaden i x och i y och lägg ihop.', 1)
    b = namn('Vilka tre mejl ligger närmast det nya mejlet?',
             [step('Avstånd i kvadrat till de närmaste', avst_steg(pts, q, ['P8', 'P5', 'P7', 'P6'])), step('De tre minsta', 'P8 (1), P5 (2) och P7 (8).')],
             n3, 'Börja med punkterna som ligger nära (5, 4) i diagrammet.', 2)
    c = klass_fv(pts, q, 3, namn_, 'Vad klassas det nya mejlet som med k = 3?')
    return uppgift('4.66', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c], 'De närmaste grannarna röstar om klassen.', ['procedur'])


@ny
def t467():
    intro = (tab(['Frukt', 'Vikt (g)', 'Längd (cm)'], [['Ny frukt', '150', '6'], ['A', '152', '9'], ['B', '160', '6']])
             + p('En AI jämför frukter med kNN. Varje frukt beskrivs med vikt i gram och längd i centimeter, och avståndet i kvadrat är (Δvikt)² + (Δlängd)².'))
    a = num('Beräkna avståndet i kvadrat mellan den nya frukten och frukt A.', [step('Avstånd i kvadrat: (Δvikt)² + (Δlängd)²', '(152 − 150)² + (9 − 6)² = 4 + 9 = 13.')], 13,
            'Kvadrera skillnaden i vikt och i längd och lägg ihop.', 1)
    b = num('Beräkna avståndet i kvadrat mellan den nya frukten och frukt B.', [step('Avstånd i kvadrat: (Δvikt)² + (Δlängd)²', '(160 − 150)² + (6 − 6)² = 100 + 0 = 100.')], 100,
            'Samma sak för frukt B.', 1)
    c = fv('Längden skiljer 3 cm för A, vilket är mycket för en frukt, men A räknas ändå som närmast. Varför?', 'Gram är stora tal',
           'Vikten mäts i gram och varierar med tiotals enheter, längden i cm varierar bara några enheter. Vikten får därför nästan all betydelse för avståndet.',
           [('Vikten mäts med större tal och styr därför nästan hela avståndet', True, 'En skillnad på 10 g väger lika mycket som 10 cm.'),
            ('Längden spelar aldrig någon roll för frukter', False, 'Längden kan vara viktig, men den drunknar här i vikten.'),
            ('Avståndet är fel uträknat', False, 'Uträkningen stämmer, problemet är skalan.'),
            ('A och B är lika långt bort', False, '13 och 100 är olika avstånd.')],
           'Jämför storleken på skillnaderna i gram och i cm.', 3)
    e = fv('Vad gör man för att vikt och längd ska få lika stor betydelse?', 'Räkna om till samma skala',
           'Man räknar om båda, till exempel så att de går från 0 till 1. Då väger en stor skillnad i längd lika mycket som en stor skillnad i vikt.',
           [('Räknar om vikt och längd så att båda får tal av ungefär samma storlek', True, 'Då styr inte vikten hela avståndet.'),
            ('Tar bort längden', False, 'Då försvinner information.'),
            ('Väljer ett större k', False, 'Det ändrar inte vilka punkter som räknas som nära.'),
            ('Mäter vikten i milligram', False, 'Då blir talen ännu större och vikten styr ännu mer.')],
           'Hur kan man göra så att talen blir lika stora?', 3, oppen=True)
    return uppgift('4.67', 'knn_kmeans', 'Klassificera med kNN', intro, [a, b, c, e], 'Egenskaper som mäts med stora tal styr avståndet.', ['procedur', 'resonemang'])


# ======================================================================== knn_kmeans: k-means

KM = 'Algoritmen k-means gör så här: varje punkt tillhör det närmaste centrumet, och sedan flyttas varje centrum till medelvärdet av sina punkter.'


def tilldela(punkter, centra):
    return {k: min(centra, key=lambda c: (d2(v, centra[c]), c)) for k, v in punkter.items()}


def medel(pts):
    return tuple(Fr(sum(x[i] for x in pts), len(pts)) for i in range(2))


@ny
def t468():
    punkter = {'P1': (1, 1), 'P2': (2, 1), 'P3': (1, 3), 'P4': (6, 5), 'P5': (7, 6), 'P6': (8, 4)}
    centra = {'C1': (2, 2), 'C2': (6, 6)}
    till = tilldela(punkter, centra)
    g2 = [punkter[k] for k in punkter if till[k] == 'C2']
    assert [k for k in punkter if till[k] == 'C1'] == ['P1', 'P2', 'P3'] and medel(g2) == (7, 5)
    intro = (diagram([(x, y, 'C', k) for k, (x, y) in punkter.items()], 'Sex användare och två klustercentrum, C1 i (2, 2) och C2 i (6, 6).', 9, 7, 'pop', 'rock',
                     centra=[(2, 2, 'C1'), (6, 6, 'C2')], legend='Gröna trianglar: användare. Kryss: klustercentrum.')
             + p('En musiktjänst grupperar sex användare efter hur många timmar pop och rock de lyssnar på per vecka. Den använder k-means med k = 2. '
                 'Klustercentrum C1 ligger i (2, 2) och C2 i (6, 6). ' + KM))
    a = namn('Vilka användare tillhör C1?',
             [step('Jämför avståndet till C1 och C2', 'P1, P2 och P3 ligger nära (2, 2). P4, P5 och P6 ligger nära (6, 6).')],
             ['P1', 'P2', 'P3'], 'Jämför avståndet till de två centrumen för varje punkt.', 2, suf='Skriv punkternas namn, åtskilda med kommatecken.')
    b = falt('Var hamnar C2 när det flyttas till medelvärdet av sina punkter?',
             [step('Punkterna i C2', 'P4 (6, 5), P5 (7, 6) och P6 (8, 4).'), step('Medelvärdet av x och av y', 'x = (6 + 7 + 8) / 3 = 7. y = (5 + 6 + 4) / 3 = 5.')],
             'C2 = (7, 5).', 'Ta medelvärdet av x-koordinaterna och av y-koordinaterna.', 2, ['x', 'y'], [7, 5])
    c = fv('Vad är typiskt för k-means?', 'Oövervakad gruppering', 'k-means hittar grupper utan etiketter, men man måste själv välja hur många grupper (k) det ska bli.',
           [('Den grupperar data utan etiketter, men man väljer själv antalet kluster k', True, 'Det är oövervakad inlärning.'),
            ('Den behöver veta vilken grupp varje punkt hör till från början', False, 'Det vore övervakad inlärning.'),
            ('Den hittar alltid rätt antal grupper själv', False, 'Antalet kluster k väljs i förväg.'),
            ('Den förutsäger ett tal, som regression', False, 'k-means delar in i grupper.')],
           'Behöver k-means några rätta svar?', 1)
    return uppgift('4.68', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, c], 'Tilldela till närmaste centrum, flytta centrum till medelvärdet.', ['procedur', 'begrepp'])


@ny
def t469():
    vals = [2, 3, 4, 10, 11, 15]
    g0 = [v for v in vals if abs(v - 3) < abs(v - 12)]
    g1 = [v for v in vals if v not in g0]
    assert g0 == [2, 3, 4] and Fr(sum(g1), 3) == 12
    intro = p('En webbutik grupperar sex kunder efter hur många minuter de stannar på sidan: 2, 3, 4, 10, 11 och 15 minuter. '
              'Den använder k-means med k = 2 och startcentrum 3 och 12. ' + KM)
    a = num('Hur många kunder hamnar i klustret med centrum 3?', [step('Närmaste centrum för varje kund', '2, 3 och 4 ligger närmast 3. 10, 11 och 15 ligger närmast 12.')], 3,
            'Jämför avståndet till 3 och till 12 för varje kund.', 1)
    b = num('Vilket blir det nya centrumet för det andra klustret?', [step('Medelvärdet av klustrets punkter', '(10 + 11 + 15) / 3 = 36 / 3 = 12.')], 12,
            'Ta medelvärdet av kunderna i klustret.', 2)
    c = fv('Centrumen ändras inte när de räknas om. Vad betyder det?', 'Algoritmen är klar', 'När centrumen står still byter ingen punkt kluster i nästa varv. Då stannar k-means.',
           [('Algoritmen är klar, eftersom ingen punkt kommer att byta kluster', True, 'Då har k-means hittat en stabil gruppering.'),
            ('Algoritmen har gjort fel', False, 'Att centrumen står still är just målet.'),
            ('Man måste byta k', False, 'k väljs i förväg och behöver inte ändras.'),
            ('Alla punkter tillhör samma kluster', False, 'Det finns fortfarande två kluster med tre punkter i varje.')],
           'Vad händer i nästa varv om centrumen inte flyttas?', 3, oppen=True)
    return uppgift('4.69', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, c], 'Tilldela, räkna om medelvärdet, upprepa tills inget ändras.', ['procedur', 'begrepp'])


@ny
def t470():
    punkter = {'P1': (1, 2), 'P2': (3, 1), 'P3': (2, 3), 'P4': (7, 8), 'P5': (8, 8), 'P6': (9, 5)}
    centra = {'C1': (3, 3), 'C2': (8, 6)}
    till = tilldela(punkter, centra)
    g1 = [punkter[k] for k in punkter if till[k] == 'C1']
    g2 = [punkter[k] for k in punkter if till[k] == 'C2']
    assert [k for k in punkter if till[k] == 'C2'] == ['P4', 'P5', 'P6'] and medel(g1) == (2, 2) and medel(g2) == (8, 7)
    intro = (diagram([(x, y, 'C', k) for k, (x, y) in punkter.items()], 'Sex elever och två klustercentrum, C1 i (3, 3) och C2 i (8, 6).', 10, 9, 'läsning', 'räkning',
                     centra=[(3, 3, 'C1', 'nh'), (8, 6, 'C2')], legend='Gröna trianglar: elever. Kryss: klustercentrum.')
             + p('En läxhjälpstjänst vill dela in sex elever i två grupper efter hur många timmar per vecka de lägger på läsning och räkning. '
                 'Den använder k-means med k = 2 och startcentrum C1 (3, 3) och C2 (8, 6). ' + KM))
    a = namn('Vilka elever tillhör C2?',
             [step('Avstånd i kvadrat till C1 och C2', 'P4: 41 och 5. P5: 50 och 4. P6: 40 och 2. P1, P2 och P3 ligger närmare C1.')],
             ['P4', 'P5', 'P6'], 'Jämför avståndet till de två centrumen för varje elev.', 2)
    b = falt('Var hamnar C1 när det flyttas till medelvärdet av sina punkter?',
             [step('Punkterna i C1', 'P1 (1, 2), P2 (3, 1) och P3 (2, 3).'), step('Medelvärdet av x och av y', 'x = (1 + 3 + 2) / 3 = 2. y = (2 + 1 + 3) / 3 = 2.')],
             'C1 = (2, 2).', 'Ta medelvärdet av x och av y för punkterna i C1.', 2, ['x', 'y'], [2, 2])
    c = falt('Var hamnar C2?', [step('Punkterna i C2', 'P4 (7, 8), P5 (8, 8) och P6 (9, 5).'), step('Medelvärdet av x och av y', 'x = (7 + 8 + 9) / 3 = 8. y = (8 + 8 + 5) / 3 = 7.')],
             'C2 = (8, 7).', 'Ta medelvärdet av x och av y för punkterna i C2.', 2, ['x', 'y'], [8, 7])
    return uppgift('4.70', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, c], 'Centrum = medelvärdet av klustrets punkter.', ['procedur'])


@ny
def t471():
    hus = [1, 2, 3, 8, 9, 13, 14, 15]
    c = [2, 9, 14]
    grp = {ci: [h for h in hus if min(c, key=lambda x: abs(h - x)) == ci] for ci in c}
    assert grp == {2: [1, 2, 3], 9: [8, 9], 14: [13, 14, 15]}
    intro = p('Ett företag ska bygga tre utlämningsställen för paket längs en lång landsväg. Åtta hus ligger vid kilometer 1, 2, 3, 8, 9, 13, 14 och 15. '
              'Företaget använder k-means med k = 3 och startcentrum vid kilometer 2, 9 och 14. ' + KM)
    a = num('Hur många hus hamnar i klustret med centrum vid kilometer 9?', [step('Närmaste centrum för varje hus', '8 och 9 ligger närmast 9. 1–3 ligger närmast 2 och 13–15 närmast 14.')], 2,
            'Jämför avståndet från varje hus till de tre centrumen.', 1)
    b = dec('Vid vilken kilometer hamnar centrumet när det flyttas till medelvärdet av sina hus?', [step('Medelvärdet av husen 8 och 9', '(8 + 9) / 2 = 8,5.')], Fr(17, 2),
            'Ta medelvärdet av husen i klustret.', 2)
    e = fv('Varför passar k-means för att placera utlämningsställena?', 'Kort väg för alla', 'k-means placerar varje centrum mitt bland sina punkter, så att avstånden från husen till närmaste ställe blir små.',
           [('Varje ställe hamnar mitt bland husen som ligger närmast det', True, 'Då blir avståndet till närmaste utlämningsställe kort för alla hus.'),
            ('k-means bestämmer själv hur många ställen som behövs', False, 'Antalet, k = 3, väljs i förväg.'),
            ('k-means placerar ställena så långt från varandra som möjligt', False, 'Målet är att vara nära husen, inte långt från varandra.'),
            ('k-means använder husens adresser som etiketter', False, 'k-means använder inga etiketter.')],
           'Vad händer med avstånden när ett centrum flyttas till medelvärdet?', 3, oppen=True)
    return uppgift('4.71', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, e], 'Varje centrum flyttas till mitten av sina punkter.', ['procedur', 'begrepp'])


@ny
def t472():
    vals = [1, 2, 6, 7, 8, 12]
    c = [Fr(1), Fr(2)]
    hist = []
    for _ in range(3):
        g = [[v for v in vals if abs(v - c[0]) <= abs(v - c[1])], [v for v in vals if abs(v - c[0]) > abs(v - c[1])]]
        c = [Fr(sum(x), len(x)) for x in g]
        hist.append((g, c))
    assert hist[0][0] == [[1], [2, 6, 7, 8, 12]] and hist[0][1] == [1, 7]
    assert hist[1][0] == [[1, 2], [6, 7, 8, 12]] and hist[1][1] == [Fr(3, 2), Fr(33, 4)] and hist[2][0] == hist[1][0]
    intro = p('Sex sensorer i en fabrik mäter temperaturen 1, 2, 6, 7, 8 och 12 grader över det normala. En AI grupperar mätningarna med k-means, k = 2, '
              'och startcentrum C1 = 1 och C2 = 2. ' + KM)
    a = num('Hur många mätningar tillhör C2 efter den första tilldelningen?', [step('Närmaste centrum', '1 ligger närmast C1. 2, 6, 7, 8 och 12 ligger närmast C2.')], 5,
            'Jämför avståndet till 1 och till 2 för varje mätning.', 1)
    b = num('Vilket värde får C2 när det flyttas till medelvärdet av sina mätningar?', [step('Medelvärdet av klustrets mätningar', '(2 + 6 + 7 + 8 + 12) / 5 = 35 / 5 = 7.')], 7,
            'Ta medelvärdet av de fem mätningarna.', 2)
    e = fv('Nu är C1 = 1 och C2 = 7. Vilken mätning byter kluster i nästa tilldelning?', 'Mätningen 2 ligger nu närmare C1',
           'Avståndet från 2 till C1 = 1 är 1, och till C2 = 7 är det 5. Mätningen 2 byter därför till C1.',
           [('Mätningen 2', True, 'Den ligger 1 från C1 och 5 från C2.'), ('Mätningen 6', False, '6 ligger 5 från C1 och 1 från C2, så den stannar i C2.'),
            ('Mätningen 12', False, '12 ligger närmare C2.'), ('Ingen mätning byter kluster', False, 'Mätningen 2 ligger nu närmare C1.')],
           'Räkna avståndet till 1 och till 7 för mätningarna nära mitten.', 3)
    g = dec('Vilket värde får C1 efter den andra flytten?', [step('Punkterna i C1', '1 och 2.'), step('Medelvärdet', '(1 + 2) / 2 = 1,5.')], Fr(3, 2),
            'Vilka mätningar tillhör C1 nu?', 3)
    return uppgift('4.72', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, e, g], 'Tilldela och flytta om och om igen tills inget ändras.', ['procedur'])


@ny
def t473():
    intro = p('Frågorna handlar om vad k betyder i k-means och i kNN.')
    a = fv('Vad betyder k i k-means?', 'Antalet grupper', 'k är antalet kluster, alltså hur många grupper datan ska delas in i. Man väljer k innan algoritmen startar.',
           [('Antalet kluster, alltså grupper', True, 'Med k = 3 delas datan in i tre grupper.'),
            ('Antalet punkter i varje grupp', False, 'Grupperna kan bli olika stora.'),
            ('Antalet varv som algoritmen kör', False, 'Algoritmen kör tills inget ändras.'),
            ('Antalet grannar som röstar', False, 'Det gäller k i kNN.')],
           'Hur många centrum finns det?', 1)
    b = fv('Vad är skillnaden mellan kNN och k-means?', 'Klassificering eller gruppering',
           'kNN klassar en ny punkt med hjälp av grannar som redan har en klass. k-means delar in punkter utan klasser i k grupper.',
           [('kNN klassar med hjälp av grannar som har en klass, k-means delar in data utan klasser i grupper', True, 'k betyder antal grannar i kNN och antal grupper i k-means.'),
            ('De är samma algoritm med olika namn', False, 'De löser olika problem.'),
            ('k-means behöver färdiga klasser, kNN behöver inga', False, 'Det är tvärtom: kNN behöver färdiga klasser.'),
            ('Båda förutsäger tal, som regression', False, 'kNN ger en klass och k-means en grupp.')],
           'Vilken av metoderna behöver punkter som redan har en klass?', 2)
    c = fv('Vad händer om man kör k-means med k = 1?', 'En enda grupp', 'Alla punkter hamnar i samma kluster, och centrumet hamnar i medelvärdet av alla punkter.',
           [('Alla punkter hamnar i samma grupp, med centrum i medelvärdet av alla punkter', True, 'Det finns bara ett centrum att vara närmast.'),
            ('Varje punkt blir en egen grupp', False, 'Det händer om k är lika med antalet punkter.'),
            ('Algoritmen fungerar inte', False, 'Den fungerar, men resultatet blir inte intressant.'),
            ('Punkterna delas i två lika stora grupper', False, 'Med k = 1 finns bara en grupp.')],
           'Hur många centrum finns det med k = 1?', 3)
    return uppgift('4.73', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, c], 'k i k-means är antalet grupper.', ['begrepp'])


@ny
def t474():
    punkter = {'P1': (2, 1), 'P2': (4, 3), 'P3': (3, 5), 'P4': (8, 6), 'P5': (9, 8), 'P6': (10, 7)}
    centra = {'C1': (1, 1), 'C2': (8, 8)}
    till = tilldela(punkter, centra)
    g1 = [punkter[k] for k in punkter if till[k] == 'C1']
    assert [k for k in punkter if till[k] == 'C1'] == ['P1', 'P2', 'P3'] and medel(g1) == (3, 3)
    assert d2(punkter['P3'], centra['C1']) == 20 and d2(punkter['P3'], centra['C2']) == 34
    intro = (diagram([(x, y, 'C', k) for k, (x, y) in punkter.items()], 'Sex bostadsområden och två startcentrum, C1 i (1, 1) och C2 i (8, 8).', 11, 9, 'x (km)', 'y (km)',
                     centra=[(1, 1, 'C1'), (8, 8, 'C2')], legend='Gröna trianglar: bostadsområden. Kryss: klustercentrum.')
             + p('En kommun ska bygga två laddstationer för elbilar. Sex bostadsområden är markerade på en karta. Kommunen använder k-means med k = 2 och '
                 'startcentrum C1 (1, 1) och C2 (8, 8). ' + KM))
    a = num('Beräkna avståndet i kvadrat från P3 (3, 5) till C1.', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(3 − 1)² + (5 − 1)² = 4 + 16 = 20.')], 20,
            'Kvadrera skillnaden i x och i y och lägg ihop.', 1)
    b = num('Beräkna avståndet i kvadrat från P3 till C2.', [step('Avstånd i kvadrat: (Δx)² + (Δy)²', '(3 − 8)² + (5 − 8)² = 25 + 9 = 34.')], 34,
            'Samma sak för C2. Vilket centrum ligger närmast?', 1)
    c = falt('P1, P2 och P3 tillhör C1. Var hamnar C1 när det flyttas till medelvärdet?',
             [step('Medelvärdet av x och av y', 'x = (2 + 4 + 3) / 3 = 3. y = (1 + 3 + 5) / 3 = 3.')], 'C1 = (3, 3).',
             'Ta medelvärdet av x och av y för de tre punkterna.', 2, ['x', 'y'], [3, 3])
    return uppgift('4.74', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, c], 'Närmaste centrum först, sedan medelvärdet.', ['procedur'])


@ny
def t475():
    vals = [2, 4, 9, 11]

    def summa(c):
        return sum(min((v - x) ** 2 for x in c) for v in vals)
    assert summa([3, 10]) == 4 and summa([5, 11]) == 14
    intro = p('Fyra kunder har handlat för 2, 4, 9 och 11 hundralappar. Två olika grupperingar ska jämföras med summan av alla avstånd i kvadrat '
              'från varje kund till det närmaste centrumet. Gruppering A har centrum 3 och 10. Gruppering B har centrum 5 och 11.')
    a = num('Bestäm summan av avstånden i kvadrat för gruppering A.', [step('Avstånd till närmaste centrum (3 eller 10)', '2: 1, 4: 1, 9: 1 och 11: 1.'),
                                                                      step('Kvadrera och summera', '1² + 1² + 1² + 1² = 4.')], 4, 'Ta varje kunds avstånd till närmaste centrum.', 2)
    b = num('Bestäm summan av avstånden i kvadrat för gruppering B.', [step('Avstånd till närmaste centrum (5 eller 11)', '2: 3, 4: 1, 9: 2 och 11: 0.'),
                                                                      step('Kvadrera och summera', '9 + 1 + 4 + 0 = 14.')], 14, 'Kunden 9 ligger närmare 11 än 5.', 2)
    c = fv('Vilken gruppering är bäst enligt k-means?', 'Minst summa', 'Gruppering A har summan 4 och B har 14. k-means försöker göra summan så liten som möjligt.',
           [('Gruppering A', True, 'Summan 4 är mindre än 14.'), ('Gruppering B', False, 'B har större summa, 14.'),
            ('De är lika bra', False, 'Summorna skiljer sig, 4 och 14.'), ('Gruppering B, eftersom ett centrum ligger exakt på en kund', False, 'Det som räknas är summan för alla kunder.')],
           'Är en liten eller stor summa bäst?', 2)
    return uppgift('4.75', 'knn_kmeans', 'Klustring med k-means', intro, [a, b, c], 'k-means vill ha så liten summa av avstånd i kvadrat som möjligt.', ['procedur'])


# ======================================================================== neurala: fördjupning (enkla neuroner)
# Användarbeslut 2026-11-12: neurala nätverk är ett fördjupningsavsnitt i AI1 med enkla uppgifter om
# viktad summa, bias och enkla aktiveringsfunktioner (stegfunktion och ReLU). Mest heltal.

def steg(z):
    return 1 if z >= 0 else 0


def relu(z):
    return z if z > 0 else 0


NEURON = ('En artificiell neuron multiplicerar varje indata med sin vikt och lägger ihop produkterna. Det kallas den viktade summan. '
          'Sedan läggs bias b till: z = w₁x₁ + w₂x₂ + b.')
STEG = ' Stegfunktionen skickar ut 1 om z ≥ 0 och annars 0.'
RELU = ' ReLU skickar ut z om z är positivt och annars 0.'
FAM1, FAM2 = 'Viktad summa och bias', 'Aktiveringsfunktioner'


def zz(w, x, b):
    return sum(Fr(wi) * Fr(xi) for wi, xi in zip(w, x)) + Fr(b)


def ws_txt(w, x):
    return ' + '.join(f'{f(wi)} · {f(xi)}' for wi, xi in zip(w, x)).replace('+ −', '− ').replace('+ -', '− ')


@ny
def t480():
    w, x, b = (2, -3), (1, 0), -1
    assert zz(w, x, 0) == 2 and zz(w, x, b) == 1
    intro = (neuron_svg([1, 0], w, b, 'En neuron med indata x₁ = 1 och x₂ = 0, vikterna 2 och −3 och bias −1.', akt=None)
             + p('En app avgör om det är cykelväder. x₁ = 1 om solen skiner och x₂ = 1 om det regnar, annars 0. I dag skiner solen och det regnar inte. '
                 'Neuronen har vikterna w₁ = 2 och w₂ = −3 och bias b = −1. ' + NEURON))
    a = num('Beräkna den viktade summan w₁x₁ + w₂x₂.', [step('Viktad summa: w₁x₁ + w₂x₂', '2 · 1 + (−3) · 0 = 2 + 0 = 2.')], 2,
            'Multiplicera varje indata med sin vikt och lägg ihop.', 1)
    bb = num('Lägg till bias. Vad blir z?', [step('z = viktad summa + b', '2 + (−1) = 1.')], 1, 'Bias är −1.', 1)
    c = fv('Vad är bias?', 'Ett tal som alltid läggs till', 'Bias läggs till den viktade summan, oavsett vad indata är. Den flyttar z uppåt eller nedåt.',
           [('Ett tal som läggs till den viktade summan, oavsett vad indata är', True, 'Här är bias −1, så z blir 1 mindre än den viktade summan.'),
            ('Vikten för det viktigaste indatat', False, 'Bias hör inte till något indata, den läggs alltid till.'),
            ('Ett indata som är 0 eller 1', False, 'Bias är inget indata, den är en del av neuronen.'),
            ('Svaret som neuronen skickar ut', False, 'Utdata räknas ut från z, och bias är bara en del av z.')],
           'Står bias bredvid något indata i figuren?', 1)
    return uppgift('4.80', 'neurala', FAM1, intro, [a, bb, c], 'Viktad summa först, sedan bias.', ['procedur', 'begrepp'])


@ny
def t481():
    w, b = (1, 2), -5
    assert zz(w, (3, 2), 0) == 7 and zz(w, (3, 2), b) == 2 and zz(w, (1, 1), b) == -2
    intro = (neuron_svg([None, None], w, b, 'En neuron med två indata, vikterna 1 och 2 och bias −5.', akt=None)
             + p('Ett spamfilter använder en neuron. x₁ är antalet länkar i mejlet och x₂ antalet gånger ordet ”gratis” står i mejlet. '
                 'Vikterna är w₁ = 1 och w₂ = 2 och bias är b = −5. ' + NEURON))
    a = num('Ett mejl har 3 länkar och 2 ”gratis”. Beräkna den viktade summan.', [step('Viktad summa: w₁x₁ + w₂x₂', '1 · 3 + 2 · 2 = 3 + 4 = 7.')], 7,
            'Sätt in x₁ = 3 och x₂ = 2.', 1)
    bb = num('Vad blir z för samma mejl?', [step('z = viktad summa + b', '7 + (−5) = 2.')], 2, 'Lägg till bias.', 1)
    c = num('Ett annat mejl har 1 länk och 1 ”gratis”. Beräkna z.', [step('z = w₁x₁ + w₂x₂ + b', '1 · 1 + 2 · 1 + (−5) = 1 + 2 − 5 = −2.')], -2,
            'Räkna på samma sätt med x₁ = 1 och x₂ = 1.', 2)
    return uppgift('4.81', 'neurala', FAM1, intro, [a, bb, c], 'z = w₁x₁ + w₂x₂ + b.', ['procedur'])


@ny
def t482():
    w, x, b = (1, 3), (4, 2), -6
    assert w[1] * x[1] == 6 and zz(w, x, b) == 4
    intro = (neuron_svg([4, 2], w, b, 'En neuron med indata 4 och 2, vikterna 1 och 3 och bias −6.', akt=None)
             + p('En filmtjänst använder en neuron för att avgöra om den ska föreslå en film för dig. x₁ är ditt betyg på actionfilmer (4) och x₂ '
                 'ditt betyg på komedier (2). Vikterna är w₁ = 1 och w₂ = 3 och bias är b = −6. ' + NEURON))
    a = num('Hur mycket bidrar komedibetyget till den viktade summan, alltså w₂x₂?', [step('Bidrag från x₂: w₂x₂', '3 · 2 = 6.')], 6,
            'Multiplicera komedibetyget med dess vikt.', 1)
    bb = num('Beräkna z.', [step('z = w₁x₁ + w₂x₂ + b', '1 · 4 + 3 · 2 + (−6) = 4 + 6 − 6 = 4.')], 4, 'Lägg ihop båda bidragen och bias.', 1)
    c = fv('Vilket betyg påverkar z mest om det ökar med 1?', 'Störst vikt', 'Om komedibetyget ökar med 1 ökar z med 3. Om actionbetyget ökar med 1 ökar z bara med 1.',
           [('Komedibetyget, eftersom det har störst vikt', True, 'Vikten 3 är större än vikten 1.'),
            ('Actionbetyget, eftersom det är högst', False, 'Betyget är högre, men en ökning med 1 ger bara 1 · 1 = 1.'),
            ('Båda påverkar lika mycket', False, 'Vikterna är olika, 1 och 3.'),
            ('Bias, eftersom den är störst', False, 'Bias ändras inte när betygen ändras.')],
           'Vad händer med z om x₁ ökar med 1? Om x₂ ökar med 1?', 2)
    return uppgift('4.82', 'neurala', FAM1, intro, [a, bb, c], 'Varje indata bidrar med vikt gånger värde.', ['procedur', 'begrepp'])


@ny
def t483():
    w, b = (4, -5, -2), -1
    assert zz(w, (1, 0, 1), b) == 1 and zz(w, (1, 1, 1), b) == -4
    intro = (neuron_svg([None, None, None], w, b, 'En neuron med tre indata, vikterna 4, −5 och −2 och bias −1.', akt=None)
             + p('En robotdammsugare bestämmer om den ska städa. x₁ = 1 om golvet är smutsigt, x₂ = 1 om batteriet är nästan slut och x₃ = 1 om någon är hemma, '
                 'annars 0. Vikterna är 4, −5 och −2 och bias är −1. Ju större z är, desto mer vill roboten städa. ' + NEURON))
    a = num('Golvet är smutsigt, batteriet är fullt och någon är hemma. Beräkna z.', [step('Indata (x₁, x₂, x₃) = (1, 0, 1)', 'z = 4 · 1 + (−5) · 0 + (−2) · 1 + (−1) = 4 − 2 − 1 = 1.')], 1,
            'Sätt in 1, 0 och 1 och glöm inte bias.', 2)
    bb = num('Nu är batteriet också nästan slut. Beräkna z.', [step('Indata (x₁, x₂, x₃) = (1, 1, 1)', 'z = 4 − 5 − 2 − 1 = −4.')], -4,
             'Nu är alla tre indata 1.', 2)
    c = fv('Vad betyder det att batteriet har vikten −5?', 'Negativ vikt drar ner z', 'När batteriet är nästan slut minskar z med 5. Roboten vill då mycket mindre städa.',
           [('Ett nästan tomt batteri gör att roboten hellre låter bli att städa', True, 'En negativ vikt drar ner z.'),
            ('Roboten städar mer när batteriet är svagt', False, 'Den negativa vikten gör tvärtom.'),
            ('Batteriet laddas ur fem gånger snabbare', False, 'Vikten säger inget om hur batteriet laddas ur.'),
            ('En negativ vikt påverkar inte z', False, 'z ändrades från 1 till −4 när batteriet blev svagt.')],
           'Vad hände med z mellan de två situationerna?', 2)
    return uppgift('4.83', 'neurala', FAM1, intro, [a, bb, c], 'Positiva vikter drar upp z, negativa drar ner.', ['procedur', 'begrepp'])


@ny
def t484():
    w, b = (Fr(1, 2), -1), 1
    minst = next(n for n in range(20) if zz(w, (n, 3), b) >= 0)
    assert zz(w, (6, 3), b) == 1 and minst == 4
    intro = (neuron_svg([None, None], [0.5, -1], b, 'En neuron med två indata, vikterna 0,5 och −1 och bias 1.', akt=None)
             + p('Skolbiblioteket använder en neuron för att avgöra om en bok ska köpas in. x₁ är antalet elever som har önskat boken och x₂ är priset i hundralappar. '
                 'Vikterna är w₁ = 0,5 och w₂ = −1 och bias är b = 1. Boken köps in om z är minst 0. ' + NEURON))
    a = num('Sex elever har önskat en bok som kostar 3 hundralappar. Hur mycket bidrar önskningarna till den viktade summan, alltså w₁x₁?',
            [step('Bidrag från x₁: w₁x₁', '0,5 · 6 = 3.')], 3, 'Multiplicera antalet önskningar med 0,5.', 1)
    bb = num('Beräkna z för boken.', [step('z = w₁x₁ + w₂x₂ + b', '0,5 · 6 + (−1) · 3 + 1 = 3 − 3 + 1 = 1.')], 1, 'Lägg ihop båda bidragen och bias.', 1)
    c = num('En annan bok kostar också 3 hundralappar. Hur många elever måste minst ha önskat den för att z ska bli minst 0?',
            [step('z med priset 3', 'z = 0,5 · x₁ − 3 + 1 = 0,5 · x₁ − 2.'), step('När blir z minst 0?', '0,5 · x₁ − 2 ≥ 0 när x₁ ≥ 4. Kontroll: 4 önskningar ger z = 0.')],
            minst, 'Pröva till exempel med 3, 4 och 5 önskningar.', 3)
    return uppgift('4.84', 'neurala', FAM1, intro, [a, bb, c], 'z = w₁x₁ + w₂x₂ + b.', ['procedur'])


@ny
def t485():
    w, x = (2, 3), (1, 1)
    assert zz(w, x, -6) == -1 and zz(w, x, -4) == 1
    intro = (neuron_svg([1, 1], w, -6, 'En neuron med indata 1 och 1, vikterna 2 och 3 och bias −6.', akt=None)
             + p('En neuron har vikterna w₁ = 2 och w₂ = 3 och bias b = −6. Indata är x₁ = 1 och x₂ = 1. ' + NEURON))
    a = num('Beräkna z.', [step('z = w₁x₁ + w₂x₂ + b', '2 · 1 + 3 · 1 + (−6) = 5 − 6 = −1.')], -1, 'Viktad summa först, sedan bias.', 1)
    bb = num('Under träningen ändras bias till −4. Beräkna z igen.', [step('Samma viktade summa, nytt bias', '5 + (−4) = 1.')], 1, 'Bara bias har ändrats.', 1)
    c = fv('Bias ökade med 2. Hur ändrades z?', 'z ändras lika mycket som bias', 'Bias läggs till direkt, så z ökar med lika mycket som bias, från −1 till 1.',
           [('z ökade med 2', True, 'z gick från −1 till 1.'), ('z ökade med 4', False, 'z gick från −1 till 1, det är en ökning med 2.'),
            ('z minskade med 2', False, 'Ett större bias gör z större.'), ('z ändrades inte', False, 'z gick från −1 till 1.')],
           'Jämför de två z-värdena.', 2)
    return uppgift('4.85', 'neurala', FAM1, intro, [a, bb, c], 'Bias läggs till den viktade summan.', ['procedur', 'begrepp'])


@ny
def t486():
    w, x = (2, 1), (3, 4)
    vs = zz(w, x, 0)
    assert vs == 10 and 7 - vs == -3
    intro = (neuron_svg([3, 4], w, '?', 'En neuron med indata 3 och 4, vikterna 2 och 1 och okänt bias.', akt=None)
             + p('En neuron har indata x₁ = 3 och x₂ = 4 och vikterna w₁ = 2 och w₂ = 1. Bias är okänt, men neuronen räknar ut z = 7. ' + NEURON))
    a = num('Beräkna den viktade summan.', [step('Viktad summa: w₁x₁ + w₂x₂', '2 · 3 + 1 · 4 = 6 + 4 = 10.')], 10, 'Multiplicera och lägg ihop.', 1)
    bb = num('Vilket värde har bias b?', [step('z = viktad summa + b', '7 = 10 + b.'), step('Lös ut b', 'b = 7 − 10 = −3.')], -3,
             'Vilket tal ska läggas till 10 för att få 7?', 3)
    c = num('Vad skulle z bli om bias i stället var 0?', [step('z = viktad summa + 0', '10 + 0 = 10.')], 10, 'Då är z bara den viktade summan.', 1)
    return uppgift('4.86', 'neurala', FAM1, intro, [a, bb, c], 'z = viktad summa + bias.', ['procedur'])


@ny
def t487():
    w, b = (2, 3, -4), -2
    assert zz(w, (1, 1, 0), b) == 3 and zz(w, (1, 0, 1), b) == -4
    intro = (neuron_svg([None, None, None], w, b, 'En neuron med tre indata, vikterna 2, 3 och −4 och bias −2.', akt=None)
             + p('En neuron ska avgöra om ett djur på en bild är en katt. x₁ = 1 om djuret har spetsiga öron, x₂ = 1 om det har långa morrhår och x₃ = 1 om det skäller, '
                 'annars 0. Vikterna är 2, 3 och −4 och bias är −2. Ju större z är, desto mer liknar djuret en katt. ' + NEURON))
    a = num('Djuret har spetsiga öron och långa morrhår och skäller inte. Beräkna z.', [step('Indata (x₁, x₂, x₃) = (1, 1, 0)', 'z = 2 + 3 + 0 − 2 = 3.')], 3,
            'Sätt in 1, 1 och 0.', 1)
    bb = num('Ett annat djur har spetsiga öron men inga långa morrhår, och det skäller. Beräkna z.', [step('Indata (x₁, x₂, x₃) = (1, 0, 1)', 'z = 2 + 0 − 4 − 2 = −4.')], -4,
             'Sätt in 1, 0 och 1.', 2)
    c = fv('Vilket indata talar mest emot att djuret är en katt?', 'Den negativa vikten', 'Att djuret skäller har vikten −4. Den drar ner z mest.',
           [('Att djuret skäller', True, 'Vikten −4 drar ner z med 4.'), ('Att djuret har spetsiga öron', False, 'Vikten 2 drar upp z.'),
            ('Att djuret har långa morrhår', False, 'Vikten 3 drar upp z mest av alla.'), ('Bias', False, 'Bias är inget indata, den gäller alla djur.')],
           'Vilken vikt är negativ?', 2)
    return uppgift('4.87', 'neurala', FAM1, intro, [a, bb, c], 'Positiva vikter talar för katt, negativa emot.', ['procedur', 'begrepp'])


@ny
def t488():
    intro = (tab(['z', '3', '−2', '0'], [['Utdata', '?', '?', '?']])
             + p('En neuron använder en aktiveringsfunktion för att bestämma vad den skickar ut. ' + STEG[1:]))
    a = num('Vad skickar stegfunktionen ut när z = 3?', [step('Stegfunktionen: 1 om z ≥ 0, annars 0', '3 ≥ 0, så utdata är 1.')], 1, 'Är z minst 0?', 1)
    bb = num('Vad skickar stegfunktionen ut när z = −2?', [step('Stegfunktionen: 1 om z ≥ 0, annars 0', '−2 är mindre än 0, så utdata är 0.')], 0, 'Är z minst 0?', 1)
    c = num('Vad skickar stegfunktionen ut när z = 0?', [step('Stegfunktionen: 1 om z ≥ 0, annars 0', '0 ≥ 0 stämmer, så utdata är 1.')], 1,
            'Läs regeln noga: står det z > 0 eller z ≥ 0?', 2)
    d = fv('Vad är ett neuralt nätverk?', 'Många neuroner i lager', 'Ett neuralt nätverk består av många neuroner i lager. Det som ett lager skickar ut blir indata till nästa lager.',
           [('Många neuroner i lager, där utdata från ett lager blir indata till nästa', True, 'Varje neuron räknar på samma sätt som här.'),
            ('En kopia av en människohjärna', False, 'Nätverket är inspirerat av hjärnan, men det är bara räkningar med tal.'),
            ('En enda neuron med många vikter', False, 'En enda neuron är inget nätverk.'),
            ('Ett nätverk av datorer som är kopplade till internet', False, 'Det handlar om neuroner i ett program, inte om datorer i ett nätverk.')],
           'Vad händer med det en neuron skickar ut?', 1)
    return uppgift('4.88', 'neurala', FAM2, intro, [a, bb, c, d], 'Stegfunktionen ger 1 om z ≥ 0, annars 0.', ['procedur', 'begrepp'])


@ny
def t489():
    intro = (tab(['z', '5', '−3', '0,5'], [['Utdata', '?', '?', '?']])
             + p('En annan vanlig aktiveringsfunktion är ReLU.' + RELU))
    a = num('Vad skickar ReLU ut när z = 5?', [step('ReLU: z om z är positivt, annars 0', '5 är positivt, så utdata är 5.')], 5, 'Är z positivt?', 1)
    bb = num('Vad skickar ReLU ut när z = −3?', [step('ReLU: z om z är positivt, annars 0', '−3 är negativt, så utdata är 0.')], 0, 'Är z positivt?', 1)
    c = dec('Vad skickar ReLU ut när z = 0,5?', [step('ReLU: z om z är positivt, annars 0', '0,5 är positivt, så utdata är 0,5.')], Fr(1, 2), 'ReLU släpper igenom positiva tal.', 1)
    d = fv('z = 5 skickas in i både stegfunktionen och ReLU. Vad blir skillnaden?', 'ReLU behåller storleken',
           'Stegfunktionen skickar ut 1, eftersom 5 ≥ 0. ReLU skickar ut hela talet 5.',
           [('Stegfunktionen ger 1 och ReLU ger 5', True, 'ReLU visar också hur stort z är.'), ('Båda ger 1', False, 'ReLU ger z när z är positivt, alltså 5.'),
            ('Båda ger 5', False, 'Stegfunktionen ger bara 0 eller 1.'), ('Stegfunktionen ger 5 och ReLU ger 1', False, 'Det är tvärtom: ReLU ger 5.')],
           'Vilka värden kan stegfunktionen skicka ut?', 2)
    return uppgift('4.89', 'neurala', FAM2, intro, [a, bb, c, d], 'ReLU: positiva z släpps igenom, annars 0.', ['procedur', 'begrepp'])


@ny
def t490():
    w, b = (2, 2), -1
    assert [steg(zz(w, x, b)) for x in [(0, 0), (0, 1), (1, 0), (1, 1)]] == [0, 1, 1, 1]
    intro = (neuron_svg([None, None], w, b, 'En neuron med två indata, vikterna 2 och 2, bias −1 och en stegfunktion.')
             + p('Indata är 0 eller 1. Neuronen har vikterna w₁ = 2 och w₂ = 2 och bias b = −1. ' + NEURON + STEG))
    a = num('Beräkna z när x₁ = 1 och x₂ = 0.', [step('z = w₁x₁ + w₂x₂ + b', '2 · 1 + 2 · 0 + (−1) = 1.')], 1, 'Sätt in indata och lägg till bias.', 1)
    bb = num('Vad skickar neuronen ut när x₁ = 1 och x₂ = 0?', [step('Stegfunktionen', 'z = 1 ≥ 0, så utdata är 1.')], 1, 'Använd z från förra frågan.', 1)
    c = num('Vad skickar neuronen ut när båda indata är 0?', [step('Beräkna z', '2 · 0 + 2 · 0 + (−1) = −1.'), step('Stegfunktionen', 'z = −1 < 0, så utdata är 0.')], 0,
            'Bara bias finns kvar i z.', 2)
    d = fv('Neuronen prövas med alla fyra kombinationer av 0 och 1. Vilken regel följer den?', 'ELLER',
           'Bara (0, 0) ger z < 0. Om minst ett indata är 1 blir z minst 1, och neuronen skickar ut 1.',
           [('Den skickar ut 1 om minst ett indata är 1 (ELLER)', True, '(0, 0) → 0, (0, 1) → 1, (1, 0) → 1, (1, 1) → 1.'),
            ('Den skickar ut 1 bara om båda indata är 1 (OCH)', False, '(1, 0) ger z = 1 och utdata 1.'),
            ('Den skickar alltid ut 1', False, '(0, 0) ger z = −1 och utdata 0.'), ('Den skickar alltid ut 0', False, '(1, 0) ger utdata 1.')],
           'Räkna z för alla fyra kombinationerna.', 3)
    return uppgift('4.90', 'neurala', FAM2, intro, [a, bb, c, d], 'Räkna z först, sedan stegfunktionen.', ['procedur'])


@ny
def t491():
    w, b = (2, 2), -3
    assert [steg(zz(w, x, b)) for x in [(0, 0), (0, 1), (1, 0), (1, 1)]] == [0, 0, 0, 1]
    intro = (neuron_svg([None, None], w, b, 'En neuron med två indata, vikterna 2 och 2, bias −3 och en stegfunktion.')
             + p('En dörr öppnas bara om man både visar ett passerkort (x₁ = 1) och slår rätt kod (x₂ = 1). Neuronen har vikterna 2 och 2 och bias −3. '
                 'Utdata 1 betyder att dörren öppnas. ' + NEURON + STEG))
    a = num('Beräkna z när båda indata är 1.', [step('z = w₁x₁ + w₂x₂ + b', '2 + 2 − 3 = 1.')], 1, 'Sätt in x₁ = 1 och x₂ = 1.', 1)
    bb = num('Någon visar passerkortet men slår fel kod. Vad skickar neuronen ut?', [step('Beräkna z', '2 · 1 + 2 · 0 − 3 = −1.'), step('Stegfunktionen', 'z = −1 < 0, så utdata är 0. Dörren förblir stängd.')],
             0, 'Här är x₁ = 1 och x₂ = 0.', 2)
    c = fv('Varför fungerar neuronen som det ska för dörren?', 'Bara båda tillsammans räcker', 'Ett indata ensamt ger z = 2 − 3 = −1, alltså 0. Båda ger z = 1, alltså 1. Det är regeln OCH.',
           [('Bara när båda indata är 1 blir z minst 0', True, 'Ett ensamt indata räcker inte för att komma över −3.'),
            ('Det räcker med ett av indata', False, 'Ett indata ger z = −1, och då skickas 0 ut.'),
            ('Bias är positivt', False, 'Bias är −3, alltså negativt.'),
            ('Vikterna är olika stora', False, 'Båda vikterna är 2.')],
           'Pröva med bara ett indata lika med 1.', 3)
    return uppgift('4.91', 'neurala', FAM2, intro, [a, bb, c], 'Ett negativt bias gör att det krävs mer för att få utdata 1.', ['procedur', 'resonemang'])


@ny
def t492():
    w, b = (2, -1), 1
    assert zz(w, (3, 2), b) == 5 and relu(zz(w, (1, 4), b)) == 0
    intro = (neuron_svg([None, None], w, b, 'En neuron med två indata, vikterna 2 och −1, bias 1 och aktiveringsfunktionen ReLU.', akt='ReLU')
             + p('En neuron har vikterna w₁ = 2 och w₂ = −1 och bias b = 1. Den använder ReLU. ' + NEURON + RELU))
    a = num('Beräkna z när x₁ = 3 och x₂ = 2.', [step('z = w₁x₁ + w₂x₂ + b', '2 · 3 + (−1) · 2 + 1 = 6 − 2 + 1 = 5.')], 5, 'Multiplicera, lägg ihop och lägg till bias.', 1)
    bb = num('Vad skickar neuronen ut när x₁ = 3 och x₂ = 2?', [step('ReLU', 'z = 5 är positivt, så utdata är 5.')], 5, 'Använd z från förra frågan.', 1)
    c = num('Vad skickar neuronen ut när x₁ = 1 och x₂ = 4?', [step('Beräkna z', '2 · 1 + (−1) · 4 + 1 = 2 − 4 + 1 = −1.'), step('ReLU', 'z = −1 är negativt, så utdata är 0.')], 0,
            'Räkna z först. Vad gör ReLU med negativa tal?', 2)
    return uppgift('4.92', 'neurala', FAM2, intro, [a, bb, c], 'Räkna z, använd sedan ReLU.', ['procedur'])


@ny
def t493():
    w, b = (1, 3), -2
    assert [steg(zz(w, x, b)) for x in [(1, 0), (0, 1), (1, 1)]] == [0, 1, 1] and zz(w, (1, 0), b) == -1
    intro = (neuron_svg([None, None], w, b, 'En neuron med två indata, vikterna 1 och 3, bias −2 och en stegfunktion.')
             + p('En app säger ”ta med paraply” när neuronen skickar ut 1. x₁ = 1 om det är molnigt och x₂ = 1 om väderprognosen säger regn, annars 0. '
                 'Vikterna är w₁ = 1 och w₂ = 3 och bias är b = −2. ' + NEURON + STEG))
    a = num('Det är molnigt men prognosen säger inte regn. Beräkna z.', [step('Indata (x₁, x₂) = (1, 0)', 'z = 1 · 1 + 3 · 0 + (−2) = −1.')], -1, 'Sätt in x₁ = 1 och x₂ = 0.', 1)
    bb = num('Vad skickar neuronen ut i den situationen?', [step('Stegfunktionen', 'z = −1 < 0, så utdata är 0. Appen säger inget om paraply.')], 0, 'Är z minst 0?', 1)
    c = num('Det är inte molnigt, men prognosen säger regn. Vad skickar neuronen ut?', [step('Beräkna z', '1 · 0 + 3 · 1 + (−2) = 1.'), step('Stegfunktionen', 'z = 1 ≥ 0, så utdata är 1.')],
            1, 'Räkna z med x₁ = 0 och x₂ = 1.', 2)
    d = fv('Vilket indata räcker ensamt för att appen ska säga ”ta med paraply”?', 'Den stora vikten', 'Regn i prognosen ger 3 − 2 = 1 ≥ 0. Moln ensamt ger 1 − 2 = −1 < 0.',
           [('Att prognosen säger regn', True, 'Vikten 3 räcker för att komma över bias −2.'), ('Att det är molnigt', False, 'Moln ensamt ger z = −1, och då blir utdata 0.'),
            ('Båda räcker ensamma', False, 'Moln ensamt räcker inte.'), ('Inget av dem räcker ensamt', False, 'Regn i prognosen räcker, z blir 1.')],
           'Jämför z för (1, 0) och (0, 1).', 3)
    return uppgift('4.93', 'neurala', FAM2, intro, [a, bb, c, d], 'En stor vikt kan ensam få z över 0.', ['procedur', 'resonemang'])


@ny
def t494():
    w = (2, 2)
    ut = lambda b: [steg(zz(w, x, b)) for x in [(0, 0), (0, 1), (1, 0), (1, 1)]]  # noqa: E731
    assert ut(-3) == [0, 0, 0, 1] and ut(-1) == [0, 1, 1, 1] and ut(-5) == [0, 0, 0, 0] and ut(1) == [1, 1, 1, 1]
    intro = (neuron_svg([None, None], w, '?', 'En neuron med två indata, vikterna 2 och 2, okänt bias och en stegfunktion.')
             + p('En neuron har vikterna w₁ = 2 och w₂ = 2. Indata är 0 eller 1. Man vill välja bias b så att neuronen gör olika saker. ' + NEURON + STEG))
    a = num('Beräkna den viktade summan när båda indata är 1.', [step('Viktad summa: w₁x₁ + w₂x₂', '2 · 1 + 2 · 1 = 4.')], 4, 'Multiplicera och lägg ihop.', 1)
    bb = fv('Vilket bias gör att neuronen bara skickar ut 1 när båda indata är 1?', 'Pröva varje bias',
            'Med b = −3 ger båda indata z = 4 − 3 = 1 ≥ 0, men ett indata ger z = 2 − 3 = −1 < 0.',
            [('b = −3', True, 'Bara (1, 1) ger z ≥ 0.'), ('b = −1', False, 'Då ger även ett ensamt indata z = 1, och utdata 1.'),
             ('b = −5', False, 'Då blir z negativt även när båda är 1, så utdata är alltid 0.'), ('b = 1', False, 'Då blir z positivt även när båda är 0.')],
            'Räkna z för (1, 1) och för (1, 0) med varje bias.', 3)
    c = fv('Vilket bias gör att neuronen skickar ut 1 även när båda indata är 0?', 'z = b när båda är 0', 'När båda indata är 0 är z = b. Då måste b vara minst 0.',
           [('b = 1', True, 'z = 1 ≥ 0 när båda är 0.'), ('b = −1', False, 'Då är z = −1 när båda är 0.'),
            ('b = −3', False, 'Då är z = −3 när båda är 0.'), ('b = −5', False, 'Då är z = −5 när båda är 0.')],
           'Vad blir z när båda indata är 0?', 2)
    return uppgift('4.94', 'neurala', FAM2, intro, [a, bb, c], 'När båda indata är 0 är z lika med bias.', ['procedur', 'resonemang'])


@ny
def t495():
    x = 2
    h = relu(2 * x - 1)
    y = relu(3 * h - 2)
    assert (h, y) == (3, 7)
    intro = (natverk_svg([1, 1, 1], 'Ett nätverk med indata x, en neuron h i ett dolt lager och en utneuron.', ['Indata', 'Dolt lager', 'Utdata'], noder=[['x'], ['h'], ['ut']])
             + p('Ett litet nätverk har två neuroner efter varandra. Båda använder ReLU.' + RELU)
             + p('Den första neuronen räknar h = ReLU(2x − 1). Den andra tar h som indata och räknar ut = ReLU(3h − 2). Indata är x = 2.'))
    a = num('Beräkna h.', [step('h = ReLU(2x − 1)', '2 · 2 − 1 = 3. Talet är positivt, så h = 3.')], h, 'Sätt in x = 2.', 2)
    bb = num('Beräkna nätverkets utdata.', [step('ut = ReLU(3h − 2)', '3 · 3 − 2 = 7. Talet är positivt, så utdata är 7.')], y, 'Använd h från förra frågan som indata.', 2)
    c = fv('Vad är det som ändras när ett neuralt nätverk tränas?', 'Vikter och bias', 'Under träningen ändras vikterna och bias lite i taget, så att nätverket gör färre fel.',
           [('Vikterna och bias', True, 'Här är det talen 2, −1, 3 och −2.'), ('Indata', False, 'Indata kommer från omvärlden, till exempel en bild.'),
            ('Aktiveringsfunktionen byts ut varje gång', False, 'ReLU är densamma, det är talen som ändras.'),
            ('Antalet neuroner växer av sig självt', False, 'Antalet neuroner bestäms av den som bygger nätverket.')],
           'Vilka tal i formlerna skulle man kunna justera?', 1)
    return uppgift('4.95', 'neurala', FAM2, intro, [a, bb, c], 'Utdata från den första neuronen blir indata till den andra.', ['procedur', 'begrepp'])
