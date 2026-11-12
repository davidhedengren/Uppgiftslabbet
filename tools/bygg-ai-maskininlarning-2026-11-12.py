"""AI-banken 2026-11-12: kapitel 4 Maskininlärning (lärarens planering AI1 TE24 2026/2027).

Användaren: fyll banken i kursens övriga områden, anpassat till gymnasiet och AI1. Flerval där de
felaktiga alternativen är vanliga missförstånd, numeriska uppgifter med verkliga beräkningar och
gärna många klassificeringsmatriser.

Fem kort med två delmoment var och minst åtta uppgifter per delmoment:
- ml_grunder 4.01–4.16: typer av inlärning; träning, test och överanpassning.
- klassmatris 4.20–4.39: beräkna utvärderingsmått; tolka klassificeringsmatrisen.
- regression 4.40–4.55: linjär regression; gradientnedstigning (ai_ml_modeller.py).
- knn_kmeans 4.60–4.75: klassificera med kNN; klustring med k-means (ai_ml_modeller.py).
- neurala 4.80–4.95: fördjupning med enkla neuroner: viktad summa och bias; aktiveringsfunktioner (ai_ml_modeller.py).

Talen är valda så att svaren blir exakta decimaltal (F1 avrundas med angiven precision).
Instruktionen ”Svara i decimalform.” visas bara i Kunskapsgymmet. Förklaringsfrågor är öppna på
papper och flerval i Kunskapsgymmet. Nivån för kapitel 4 sätts här (traningsniva 1–2 = E, 3 = C,
5 = A) och behålls av nivåskriptet. Svaren räknas om oberoende i
tools/ai-maskininlarning-2026-11-12.test.js. Kör efter bygg-ai-tillampningar-2026-11-12.py och före
omgrupperingen.
"""
import json
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ai_ml import p, f, exakt, num, dec, fv, falt, uppgift, matris, matris_n, step, tab  # noqa: E402
import ai_ml_modeller  # noqa: E402

BANK = 'uppgifterai.js'
NYA = []


def ny(fn):
    NYA.append(fn)
    return fn


# ======================================================================== ml_grunder: typer av inlärning

TYP = {'klass': 'Övervakad inlärning (klassificering)', 'regr': 'Övervakad inlärning (regression)',
       'oov': 'Oövervakad inlärning', 'rl': 'Förstärkningsinlärning'}
RUBRIK = {'klass': 'Märkta exempel där svaret är en kategori', 'regr': 'Märkta exempel där svaret är ett tal',
          'oov': 'Inga givna svar, algoritmen hittar grupper själv', 'rl': 'En agent provar handlingar och får belöning'}
KOMM = {
    ('klass', 'regr'): 'Svaret som ska förutsägas är ett tal, inte en kategori.',
    ('klass', 'oov'): 'Det finns inga givna kategorier att lära sig av.',
    ('klass', 'rl'): 'Ingen har märkt exempel med rätt svar. Agenten lär sig av belöningar.',
    ('regr', 'klass'): 'Svaret är en kategori, inte ett tal, så det är klassificering.',
    ('regr', 'oov'): 'Det finns inga kända svar att lära sig av, varken tal eller kategorier.',
    ('regr', 'rl'): 'Agenten lär sig av belöningar för sina handlingar, inte av kända tal.',
    ('oov', 'klass'): 'Exemplen har kända svar (etiketter), så inlärningen är övervakad.',
    ('oov', 'regr'): 'Exemplen har kända tal som svar, så inlärningen är övervakad.',
    ('oov', 'rl'): 'Agenten handlar i en miljö och får belöning. Det är inte gruppering av data.',
    ('rl', 'klass'): 'Ingen agent provar handlingar för att få belöning. Modellen lär sig av märkta exempel.',
    ('rl', 'regr'): 'Ingen agent får belöning. Modellen lär sig av exempel med kända tal.',
    ('rl', 'oov'): 'Det finns ingen belöning, bara data som ska delas in i grupper.',
}
SCEN = [
    ('Ett e-postprogram tränas på 50 000 mejl som användare har märkt som ”spam” eller ”inte spam”.', 'klass',
     'Varje mejl har en etikett med rätt kategori.'),
    ('En mäklarfirma tränar en modell på 3 000 sålda bostäder med yta, läge och slutpris för att kunna förutsäga priset på nya bostäder.', 'regr',
     'Priset är ett tal, och de sålda bostäderna har kända priser.'),
    ('En robotdammsugare får pluspoäng när den suger upp damm och minuspoäng när den krockar. Efter många körningar har den lärt sig städa effektivt.', 'rl',
     'Roboten provar handlingar och lär sig av poängen den får.'),
    ('En nyhetssajt låter en algoritm dela in 10 000 artiklar i grupper med liknande innehåll, utan att någon har bestämt vilka ämnen som finns.', 'oov',
     'Ingen artikel har en given etikett. Grupperna hittas i datan.'),
    ('Ett sjukhus tränar en AI på röntgenbilder där läkare har markerat om det finns en tumör eller inte.', 'klass',
     'Bilderna är märkta av läkare med kategorin tumör eller inte tumör.'),
    ('En AI lär sig spela ett datorspel genom att spela tusentals gånger. Den får poäng när den vinner och förlorar poäng när den förlorar.', 'rl',
     'AI:n lär sig av belöningen, vinst eller förlust, efter sina drag.'),
    ('En väderapp tränas på tio års mätningar för att förutsäga hur många millimeter regn som faller i morgon.', 'regr',
     'Regnmängden är ett tal, och de gamla mätningarna har kända värden.'),
    ('En bank letar efter ovanliga kortköp genom att se vilka köp som skiljer sig mycket från alla andra, utan att ha exempel på bedrägerier.', 'oov',
     'Det finns inga märkta exempel. Algoritmen hittar avvikande köp själv.'),
    ('En app känner igen vilken växtart en blomma tillhör. Den är tränad på 200 000 foton som botaniker har artbestämt.', 'klass',
     'Fotona har etiketter, och svaret är en art, alltså en kategori.'),
    ('Ett trafikljus styrs av en AI som får belöning när köerna blir korta och straff när bilar får vänta länge.', 'rl',
     'Trafikljuset provar olika sätt att växla och lär sig av belöningen.'),
    ('En streamingtjänst grupperar låtar som låter lika, utan att ha några färdiga genrer att utgå från.', 'oov',
     'Låtarna har inga givna grupper. Algoritmen hittar likheterna själv.'),
    ('En kollektivtrafikapp tränas på gamla resor för att förutsäga hur många minuter en bussresa tar.', 'regr',
     'Restiden är ett tal, och de gamla resorna har kända restider.'),
    ('Elever har sorterat 5 000 kommentarer på sociala medier som ”vänlig” eller ”elak”. En modell tränas på dem för att flagga elaka kommentarer.', 'klass',
     'Kommentarerna har en etikett, vänlig eller elak.'),
    ('En robothund lär sig gå. Den får belöning för varje meter den tar sig framåt utan att ramla.', 'rl',
     'Robothunden lär sig genom att prova rörelser och få belöning.'),
    ('En klädbutik låter en algoritm dela in kunderna i grupper efter vad de köper, för att kunna skicka olika erbjudanden.', 'oov',
     'Kunderna har inga givna grupper. Algoritmen hittar grupperna i köpdatan.'),
    ('En energiförening tränar en modell på gamla mätningar för att förutsäga hur många kilowattimmar en solpanel producerar i morgon.', 'regr',
     'Elproduktionen är ett tal, och de gamla mätningarna har kända värden.'),
]

EXTRA = [
    lambda: fv('Vad är det som gör maskininlärning annorlunda än vanlig programmering?', 'Modellen lär sig ur data',
               'I vanlig programmering skriver människan reglerna. I maskininlärning hittar algoritmen mönstren i exempeldata.',
               [('Modellen hittar själv mönster i data i stället för att få alla regler av en programmerare', True, 'Reglerna lärs in ur exemplen.'),
                ('Datorn tänker och förstår som en människa', False, 'Modellen hittar statistiska mönster, den förstår inte som en människa.'),
                ('Maskininlärning kräver ingen data', False, 'Det är tvärtom, maskininlärning bygger på data.'),
                ('Maskininlärning gör aldrig fel', False, 'Modeller gör fel, därför mäter man till exempel träffsäkerhet.')],
               'Vem bestämmer reglerna i de två fallen?', 1),
    lambda: fv('Vad är träningsdata?', 'Exemplen som modellen lär sig av',
               'Träningsdata är de exempel som modellen får se när den tränas, till exempel tusentals bilder med rätt svar.',
               [('Exemplen som modellen lär sig av', True, 'Ju fler och mer varierade exempel, desto bättre brukar modellen bli.'),
                ('Den data som modellen ska användas på i framtiden', False, 'Det är nya fall som modellen inte har sett.'),
                ('Programkoden för modellen', False, 'Koden är instruktioner, inte exempel att lära sig av.'),
                ('Svaren som modellen skriver ut', False, 'Det är modellens svar, inte det den lär sig av.')],
               'Vad behöver modellen för att kunna lära sig?', 1),
    lambda: fv('Vad är skillnaden mellan klassificering och regression?', 'Kategori eller tal',
               'Klassificering ger en kategori, till exempel spam. Regression ger ett tal, till exempel ett pris.',
               [('Klassificering förutsäger en kategori, regression ett tal', True, 'Till exempel ”spam” jämfört med ”3,2 miljoner kr”.'),
                ('Klassificering är oövervakad, regression övervakad', False, 'Båda är normalt övervakad inlärning.'),
                ('Regression används bara för bilder', False, 'Regression används för att förutsäga tal, till exempel temperatur.'),
                ('Det är två namn på samma sak', False, 'De förutsäger olika slags svar.')],
               'Vilken sorts svar ger modellen?', 1),
    lambda: fv('Vad är en etikett i träningsdatan för övervakad inlärning?', 'Det rätta svaret',
               'Etiketten är det rätta svaret för ett exempel, till exempel ”katt” på en bild av en katt.',
               [('Det rätta svaret som hör till varje exempel', True, 'Modellen jämför sina gissningar med etiketterna.'),
                ('Filnamnet på bilden', False, 'Filnamnet säger inget om vad bilden föreställer.'),
                ('En egenskap hos bilden, till exempel hur stor den är', False, 'Egenskaper beskriver exemplet. Etiketten är det rätta svaret.'),
                ('Modellens gissning', False, 'Gissningen kommer från modellen. Etiketten är det rätta svaret.')],
               'Vad jämför modellen sina gissningar med?', 1),
    lambda: fv('Vilket av exemplen är inte maskininlärning?', 'Fasta regler som någon har skrivit',
               'En miniräknare följer regler som programmeraren har skrivit. Den lär sig ingenting av data.',
               [('En miniräknare som räknar ut 12 · 34', True, 'Den följer fasta regler och lär sig inget av exempel.'),
                ('Ett spamfilter som blir bättre när användare markerar skräppost', False, 'Filtret lär sig av märkta exempel.'),
                ('En app som känner igen ansikten efter träning på foton', False, 'Appen har lärt sig av tusentals exempel.'),
                ('En tjänst som föreslår filmer utifrån vad liknande användare har sett', False, 'Förslagen bygger på mönster i data.')],
               'Lär sig programmet något av exempel?', 1),
    lambda: fv('Hälften av etiketterna i en träningsdata är fel, eftersom de som märkte bilderna slarvade. Vad händer troligen?', 'Skräp in, skräp ut',
               'Modellen lär sig de mönster som finns i datan, även felen. Dålig data ger en dålig modell.',
               [('Modellen lär sig felen och blir dålig', True, 'Modellen kan inte veta vilka etiketter som är fel.'),
                ('Modellen rättar själv de felaktiga etiketterna', False, 'Modellen litar på etiketterna, den vet inte vilka som är fel.'),
                ('Det spelar ingen roll om det finns tillräckligt med bilder', False, 'Fler bilder med fel etiketter hjälper inte.'),
                ('Modellen blir bättre eftersom den får mer variation', False, 'Fel etiketter är inte variation, de är fel svar.')],
               'Kan modellen veta vilka etiketter som är fel?', 3, oppen=True),
    lambda: fv('Varför behöver en modell för bildigenkänning ofta mycket träningsdata?', 'Många varianter att lära sig',
               'Samma sak kan se olika ut beroende på ljus, vinkel och bakgrund. Modellen behöver många exempel för att hitta det gemensamma.',
               [('Samma sak kan se ut på många olika sätt, och modellen behöver se många varianter', True, 'Då lär den sig det som är gemensamt.'),
                ('Datorn har dåligt minne och glömmer gamla bilder', False, 'Det handlar inte om minne utan om variation.'),
                ('Mer data gör alltid modellen perfekt', False, 'Mer data hjälper, men ingen modell blir perfekt.'),
                ('Det behövs inte, en bild per sak räcker', False, 'En enda bild visar inte hur saken ser ut i andra situationer.')],
               'Hur många olika sätt kan en hund se ut på ett foto?', 3, oppen=True),
    lambda: fv('Vad betyder det att träna en modell?', 'Justera modellen efter exemplen',
               'Under träningen justeras modellens inre värden, till exempel vikter, så att den gör så få fel som möjligt på träningsexemplen.',
               [('Modellens inre värden justeras så att den gör så få fel som möjligt på exemplen', True, 'Det är det som sker i träningen.'),
                ('En människa skriver in alla svar i modellen', False, 'Modellen hittar mönstren själv ur exemplen.'),
                ('Modellen kopierar träningsdatan och slår upp svaret', False, 'En bra modell ska klara även nya exempel.'),
                ('Datorn laddar ner en färdig modell från internet', False, 'Det är inte träning.')],
               'Vad ändras i modellen när den tränas?', 1),
]


def typ_del(text, typ, varfor):
    alts = [(TYP[t], t == typ, varfor if t == typ else KOMM[(t, typ)]) for t in TYP]
    return fv(text + ' Vilken sorts inlärning är det?', RUBRIK[typ], varfor, alts,
              'Finns det kända svar? Är svaret en kategori eller ett tal? Finns det belöningar?', 1)


for _i in range(8):
    def _t(i=_i):
        s1, s2 = SCEN[2 * i], SCEN[2 * i + 1]
        a, b = typ_del(*s1), typ_del(*s2)
        c = EXTRA[i]()
        intro = p('Frågorna handlar om olika sorters maskininlärning: övervakad inlärning (klassificering eller regression), '
                  'oövervakad inlärning och förstärkningsinlärning.')
        return uppgift(f'4.0{i + 1}', 'ml_grunder', 'Typer av inlärning', intro, [a, b, c],
                       'Fråga dig om det finns kända svar och vilken sorts svar som ska förutsägas.', ['begrepp'])
    ny(_t)


# ======================================================================== ml_grunder: träning, test och överanpassning

def split_task(id_, intro_txt, n, pt, pv, c):
    tr = n * pt // 100
    va = n * pv // 100
    te = n - tr - va
    parts = [num('Hur många exempel används för att träna modellen?', [step(f'{pt} % av {f(n)}', f'{f(pt / 100)} · {f(n)} = {f(tr)}.')], tr,
                 f'Räkna {pt} % av {f(n)}.', 1)]
    if pv:
        parts.append(num('Hur många exempel används för att testa modellen?',
                         [step(f'Validering: {pv} % av {f(n)}', f'{f(pv / 100)} · {f(n)} = {f(va)}.'),
                          step('Testdatan är det som blir kvar', f'{f(n)} − {f(tr)} − {f(va)} = {f(te)}.')], te,
                         'Räkna först ut hur många som används till validering.', 2))
    else:
        parts.append(num('Hur många exempel används för att testa modellen?', [step('Testdatan är det som blir kvar', f'{f(n)} − {f(tr)} = {f(te)}.')], te,
                         'Det som inte används till träning används till test.', 1))
    parts.append(c)
    return uppgift(id_, 'ml_grunder', 'Träning, test och överanpassning', p(intro_txt), parts,
                   'Träningsdata och testdata ska vara olika exempel.', ['procedur', 'begrepp'])


@ny
def t409():
    return split_task('4.09', 'En skola vill förutsäga vilka elever som riskerar att inte klara en kurs. Den har data om 500 tidigare elever. '
                      '80 % används för att träna modellen och resten för att testa den.', 500, 80, 0,
                      fv('Varför testar man modellen på elever som den inte har tränat på?', 'Testet ska visa hur modellen klarar nya fall',
                         'På träningsdatan kan modellen ha lärt sig exemplen utantill. Testdatan visar hur den klarar nya elever.',
                         [('För att se hur bra modellen är på nya fall som den inte har sett', True, 'Det är just nya elever modellen ska användas på.'),
                          ('För att träningen ska gå snabbare', False, 'Testdatan påverkar inte hur snabbt träningen går.'),
                          ('För att få mer data att träna på', False, 'Testdatan används inte till träning.'),
                          ('Det spelar ingen roll vilken data man testar på', False, 'Testar man på träningsdata kan resultatet bli för bra för att vara sant.')],
                         'Vad händer om modellen bara har lärt sig träningsexemplen utantill?', 3, oppen=True))


@ny
def t410():
    intro = (tab(['Modell', 'Rätt på träningsdata', 'Rätt på testdata'], [['A', '99 %', '62 %'], ['B', '86 %', '84 %'], ['C', '58 %', '57 %']])
             + p('Tre modeller har tränats för att känna igen trafikskyltar. Tabellen visar hur stor andel av bilderna de klassar rätt.'))
    a = fv('Vilken modell är överanpassad?', 'Stor skillnad mellan träning och test',
           'Modell A är nästan perfekt på träningsdatan men mycket sämre på nya bilder. Den har lärt sig träningsbilderna utantill.',
           [('Modell A', True, '99 % på träning men bara 62 % på test.'), ('Modell B', False, 'B är nästan lika bra på test som på träning.'),
            ('Modell C', False, 'C är dålig på båda. Den är underanpassad, inte överanpassad.'), ('Ingen av dem', False, 'A visar tydliga tecken på överanpassning.')],
           'Jämför resultatet på träningsdata och testdata.', 2)
    b = fv('Vilken modell bör användas i en riktig bil?', 'Bäst på nya bilder', 'Det är testresultatet som visar hur modellen fungerar på nya skyltar.',
           [('Modell B', True, 'B har bäst resultat på testdatan, 84 %.'), ('Modell A', False, 'A har bäst träningsresultat, men bara 62 % på nya bilder.'),
            ('Modell C', False, 'C klarar bara 57 % av testbilderna.'), ('Det går inte att avgöra', False, 'Testresultaten visar tydligt att B är bäst på nya bilder.')],
           'Vilket resultat visar hur modellen klarar nya bilder?', 2)
    c = fv('Vad kan man göra för att minska överanpassning?', 'Fler och mer varierade exempel', 'Med fler och mer varierade exempel blir det svårare att lära sig utantill.',
           [('Träna på fler och mer varierade exempel', True, 'Då måste modellen hitta allmänna mönster.'),
            ('Testa på träningsdatan i stället', False, 'Det döljer bara problemet.'),
            ('Träna längre på samma data', False, 'Det brukar göra överanpassningen värre.'),
            ('Göra modellen ännu mer komplex', False, 'En mer komplex modell kan lättare lära sig exemplen utantill.')],
           'Vad gör det svårare att lära sig exemplen utantill?', 3, oppen=True)
    return uppgift('4.10', 'ml_grunder', 'Träning, test och överanpassning', intro, [a, b, c], 'Överanpassning: bra på träning, dålig på test.', ['begrepp', 'resonemang'])


@ny
def t411():
    return split_task('4.11', 'En app ska känna igen svampar från foton. Utvecklarna har 1 200 foton. 75 % används för att träna modellen och resten för att testa den.',
                      1200, 75, 0,
                      fv('Några foton råkar finnas både i träningsdatan och i testdatan. Vad blir följden?', 'Testet blir för lätt',
                         'Modellen har redan sett de fotona. Testresultatet blir då bättre än modellen egentligen är på nya svampar.',
                         [('Testresultatet blir bättre än modellen egentligen är', True, 'Modellen kan ha lärt sig just de fotona utantill.'),
                          ('Testresultatet blir sämre än modellen egentligen är', False, 'Kända foton är lättare, inte svårare.'),
                          ('Det påverkar inte testresultatet', False, 'Testet ska bara innehålla foton modellen aldrig sett.'),
                          ('Modellen slutar fungera', False, 'Modellen fungerar, men testet ger en felaktig bild av hur bra den är.')],
                         'Är det svårt att känna igen ett foto man redan har sett?', 3, oppen=True))


@ny
def t412():
    return split_task('4.12', 'En modell ska avgöra om recensioner av restauranger är positiva eller negativa. Det finns 2 500 recensioner. '
                      '70 % används för att träna modellen och resten för att testa den. Recensionerna lottas till träning och test.', 2500, 70, 0,
                      fv('Varför lottar man vilka recensioner som hamnar i testdatan, i stället för att ta de sista 750?', 'Testdatan ska likna träningsdatan',
                         'De sista recensionerna kan vara speciella, till exempel alla från samma restaurang eller samma månad. Med lottning blir båda delarna lika varandra.',
                         [('Så att testdatan liknar träningsdatan och testet ger en rättvis bild', True, 'Annars kan testdatan vara helt annorlunda än det modellen tränat på.'),
                          ('För att modellen ska tränas snabbare', False, 'Lottningen påverkar inte hur snabbt träningen går.'),
                          ('För att få fler recensioner', False, 'Antalet recensioner är detsamma.'),
                          ('Det spelar ingen roll hur man delar upp', False, 'En skev uppdelning kan ge ett missvisande testresultat.')],
                         'Tänk om de sista 750 recensionerna alla kommer från samma restaurang.', 3, oppen=True))


@ny
def t413():
    intro = p('En röstassistent tränas på 800 inspelningar av människor som säger kommandon. 640 av inspelningarna kommer från vuxna män.')
    a = dec('Hur stor andel av inspelningarna kommer från vuxna män?', [step('Andel = delen / det hela', '640 / 800 = 0,8.')], Fr(640, 800),
            'Dela antalet inspelningar med vuxna män med antalet inspelningar.', 1)
    b = fv('Vad händer troligen när ett barn pratar med röstassistenten?', 'Barnröster liknar inte träningsdatan',
           'Modellen har nästan bara hört vuxna män. Barnröster är ljusare och kan därför tolkas fel oftare.',
           [('Den gör fler fel, eftersom barnröster nästan inte fanns i träningsdatan', True, 'Modellen fungerar bäst på data som liknar träningsdatan.'),
            ('Den fungerar lika bra för alla', False, 'Den har lärt sig mönster från vuxna mansröster.'),
            ('Den fungerar bättre, eftersom barn pratar tydligt', False, 'Det avgörande är vad modellen har tränats på.'),
            ('Den lär sig barnrösten direkt', False, 'En färdigtränad modell lär sig inte av sig själv under användningen.')],
           'Vilka röster har modellen tränats på?', 3, oppen=True)
    c = fv('Vad är bästa sättet att få röstassistenten att fungera för fler?', 'Mer varierad träningsdata',
           'Träningsdatan bör innehålla röster av alla åldrar, kön och dialekter som assistenten ska användas av.',
           [('Träna på inspelningar från personer i alla åldrar, av alla kön och med olika dialekter', True, 'Då liknar träningsdatan verkligheten.'),
            ('Träna längre på samma inspelningar', False, 'Samma data ger samma brister.'),
            ('Be barn att prata med mörkare röst', False, 'Tekniken ska anpassas till användarna, inte tvärtom.'),
            ('Ta bort inspelningarna med vuxna män', False, 'Då blir datan bara skev åt ett annat håll.')],
           'Vad saknas i datan?', 2)
    return uppgift('4.13', 'ml_grunder', 'Träning, test och överanpassning', intro, [a, b, c], 'Träningsdatan ska likna de fall modellen möter.', ['procedur', 'resonemang'])


@ny
def t414():
    intro = (tab(['Modell', 'Medelfel på träningsdata', 'Medelfel på testdata'], [['A', '20 000 kr', '180 000 kr'], ['B', '60 000 kr', '70 000 kr'],
                                                                                    ['C', '150 000 kr', '160 000 kr']])
             + p('Tre modeller förutsäger priset på begagnade bilar. Tabellen visar hur mycket fel de i genomsnitt gissar. Ett lägre fel är bättre.'))
    a = fv('Vilken modell är överanpassad?', 'Litet fel på träning, stort på test', 'A gissar nästan rätt på träningsbilarna men mycket fel på nya bilar.',
           [('Modell A', True, 'Felet ökar från 20 000 kr till 180 000 kr på nya bilar.'), ('Modell B', False, 'B är nästan lika bra på nya bilar.'),
            ('Modell C', False, 'C har stort fel på båda. Den är underanpassad.'), ('Ingen av dem', False, 'A visar tydliga tecken på överanpassning.')],
           'Här är ett lågt tal bra. Jämför träning och test.', 2)
    b = fv('Vilken modell är underanpassad?', 'Stort fel överallt', 'C gör stora fel både på träningsdata och testdata. Den har inte ens lärt sig träningsexemplen.',
           [('Modell C', True, 'Den är för enkel för att fånga sambandet.'), ('Modell A', False, 'A har lärt sig träningsdatan för bra, det är överanpassning.'),
            ('Modell B', False, 'B har lagom fel på båda.'), ('Ingen av dem', False, 'C har stort fel redan på träningsdatan.')],
           'Vilken modell klarar inte ens träningsdatan?', 2)
    c = num('Hur många tusen kronor större är felet på testdatan än på träningsdatan för modell B?', [step('Testfel minus träningsfel', '70 000 − 60 000 = 10 000 kr, alltså 10 tusen kronor.')],
            10, 'Dra träningsfelet från testfelet.', 1)
    return uppgift('4.14', 'ml_grunder', 'Träning, test och överanpassning', intro, [a, b, c], 'Lågt fel är bra här. Jämför träning och test.', ['begrepp', 'resonemang'])


@ny
def t415():
    djup = [1, 2, 3, 4, 5, 6]
    tr = [70, 80, 88, 94, 98, 100]
    te = [68, 78, 85, 84, 80, 76]
    bast = djup[te.index(max(te))]
    assert bast == 3
    intro = (tab(['Trädets djup', '1', '2', '3', '4', '5', '6'], [['Rätt på träningsdata (%)'] + [str(x) for x in tr], ['Rätt på testdata (%)'] + [str(x) for x in te]])
             + p('Ett beslutsträd ska förutsäga om en kund kommer att köpa en vara. Ju djupare trädet är, desto fler frågor kan det ställa. '
                 'Tabellen visar resultatet för olika djup.'))
    a = num('Vilket djup ger bäst resultat på testdatan?', [step('Största värdet på raden för testdata', 'Testresultaten är 68, 78, 85, 84, 80 och 76 %. Störst är 85 % vid djup 3.')],
            bast, 'Titta bara på raden för testdata.', 1)
    b = num('Hur många procentenheter skiljer det mellan träning och test vid djup 6?', [step('Träning minus test', '100 − 76 = 24 procentenheter.')], 24,
            'Ta resultatet på träningsdata minus resultatet på testdata.', 1)
    c = fv('Varför blir testresultatet sämre när trädet blir djupare än 3?', 'Trädet lär sig träningsdatan utantill',
           'Ett mycket djupt träd kan ställa så många frågor att det passar varje träningsexempel, även slumpmässiga detaljer. Det är överanpassning.',
           [('Trädet börjar lära sig detaljer som bara gäller träningsdatan', True, 'Det är överanpassning: 100 % på träning men sämre på test.'),
            ('Ett djupare träd är alltid sämre', False, 'Djup 2 och 3 är bättre än djup 1.'),
            ('Testdatan blir svårare när trädet växer', False, 'Testdatan är densamma hela tiden.'),
            ('Trädet glömmer det det lärde sig först', False, 'Träningsresultatet fortsätter att öka.')],
           'Vad händer med resultatet på träningsdatan samtidigt?', 3, oppen=True)
    return uppgift('4.15', 'ml_grunder', 'Träning, test och överanpassning', intro, [a, b, c], 'Det bästa djupet ger bäst resultat på testdatan.', ['procedur', 'resonemang'])


@ny
def t416():
    intro = p('Frågorna handlar om överanpassning och underanpassning.')
    a = fv('En modell får 100 % rätt på träningsdatan. Vad kan man säga om den?', 'Testdatan avgör',
           'Det kan betyda att modellen är bra, men också att den har lärt sig träningsexemplen utantill. Först testdatan visar vilket.',
           [('Det går inte att veta hur bra den är förrän den har testats på ny data', True, 'Modellen kan vara överanpassad.'),
            ('Den är perfekt och kommer aldrig att göra fel', False, 'Nya exempel kan se annorlunda ut än träningsexemplen.'),
            ('Den är säkert överanpassad', False, 'Det är möjligt, men inte säkert. Testet visar det.'),
            ('Den har tränats för kort tid', False, 'Kort träning ger snarare sämre resultat på träningsdatan.')],
           'Vad visar resultatet på träningsdatan, och vad visar det inte?', 3, oppen=True)
    b = fv('Vad betyder det att en modell är underanpassad?', 'För enkel modell', 'Modellen är för enkel för att fånga sambandet och gör många fel, även på träningsdatan.',
           [('Den är för enkel och gör många fel redan på träningsdatan', True, 'Till exempel en rak linje för ett samband som böjer sig.'),
            ('Den är bra på träningsdatan men dålig på ny data', False, 'Det är överanpassning.'),
            ('Den har för lite testdata', False, 'Underanpassning handlar om modellen, inte om testdatan.'),
            ('Den är perfekt anpassad', False, 'Underanpassad betyder att den inte har lärt sig tillräckligt.')],
           'Hur går det för modellen på träningsdatan?', 1)
    c = fv('En lärare ger exakt samma frågor på provet som på övningsbladet. En elev har lärt sig svaren utantill och får alla rätt. Vilket begrepp liknar det?',
           'Utantillinlärning är överanpassning', 'Eleven har lärt sig exemplen, inte metoden. Med nya frågor hade det gått sämre, precis som för en överanpassad modell.',
           [('Överanpassning', True, 'Bra på kända exempel, osäker på nya.'), ('Underanpassning', False, 'Eleven klarar ju de kända frågorna perfekt.'),
            ('Oövervakad inlärning', False, 'Eleven har facit att lära sig av.'), ('Förstärkningsinlärning', False, 'Det handlar inte om belöning för handlingar.')],
           'Skulle eleven klara nya frågor av samma slag?', 2)
    return uppgift('4.16', 'ml_grunder', 'Träning, test och överanpassning', intro, [a, b, c], 'Överanpassad: lär sig exemplen utantill. Underanpassad: för enkel.', ['begrepp'])


# ======================================================================== klassmatris: beräkna utvärderingsmått

def matt(tp, fn, fp, tn):
    return {'acc': Fr(tp + tn, tp + fn + fp + tn), 'prec': Fr(tp, tp + fp), 'rec': Fr(tp, tp + fn)}


TOLKNING = {
    'cancer': lambda m, tp, fn, fp, tn: fv(
        'Vilket mått är viktigast att få högt när AI:n letar efter cancer?', 'Missade sjuka är farligast',
        'En missad cancer (falskt negativ) kan vara livsfarlig. Ett falskt larm leder till en extra undersökning.',
        [('Recall, så att så få sjuka som möjligt missas', True, f'Recall är {f(exakt(m["rec"]))}: {fn} av {tp + fn} sjuka missas.'),
         ('Precision, så att så få friska som möjligt får larm', False, 'Ett falskt larm är jobbigt, men en missad cancer är farligare.'),
         ('Träffsäkerheten, eftersom den räknar med alla patienter', False, 'De flesta är friska, så träffsäkerheten kan bli hög även om sjuka missas.'),
         ('Alla mått är lika viktiga här', False, 'Felen har olika följder, så måtten väger olika tungt.')],
        'Vilket fel är farligast: att missa en sjuk eller att larma för en frisk?', 3, oppen=True),
    'bedrageri': lambda m, tp, fn, fp, tn: fv(
        f'Träffsäkerheten är {f(exakt(m["acc"]))}. Varför betyder det inte att modellen är bra?', 'Nästan alla köp är äkta',
        f'En modell som alltid säger ”äkta” får {f(fp + tn)} av {f(tp + fn + fp + tn)} rätt utan att hitta ett enda bedrägeri.',
        [('Nästan alla köp är äkta, så hög träffsäkerhet kan nås utan att hitta bedrägerierna', True,
          f'Recall är bara {f(exakt(m["rec"]))}: {fn} av {tp + fn} bedrägerier missas.'),
         ('Träffsäkerheten räknas fel när det finns många fall', False, 'Beräkningen är rätt. Problemet är att klasserna är ojämnt fördelade.'),
         ('Modellen är bra, talet är nära 1', False, 'Den missar ändå mer än hälften av bedrägerierna.'),
         ('Träffsäkerheten säger bara något om falska larm', False, 'Den räknar med alla fall, men domineras av de många äkta köpen.')],
        'Hur många rätt skulle en modell få om den alltid sa ”äkta”?', 3, oppen=True),
    'mobil': lambda m, tp, fn, fp, tn: fv(
        'Vilket fel är allvarligast för en mobil som låses upp med ansiktet?', 'En främling som kommer in',
        'Ett falskt positivt betyder att någon annan låser upp mobilen. Ett falskt negativt betyder bara att ägaren får försöka igen.',
        [('Falskt positivt: någon annan låser upp mobilen', True, 'Det är ett säkerhetsproblem. Därför vill man ha mycket hög precision.'),
         ('Falskt negativt: ägaren känns inte igen', False, 'Det är irriterande, men ägaren kan använda en kod i stället.'),
         ('Sant negativt: någon annan nekas', False, 'Det är ett rätt beslut, inget fel.'),
         ('Alla fel är lika allvarliga', False, 'Att släppa in en främling är värre än att neka ägaren en gång.')],
        'Vad händer vid varje sorts fel?', 3, oppen=True),
    'fusk': lambda m, tp, fn, fp, tn: fv(
        f'Precisionen är {f(exakt(m["prec"]))}. Vad betyder det för eleverna?', 'Hälften av de utpekade är oskyldiga',
        f'Av de {tp + fp} inlämningar AI:n pekade ut var bara {tp} fusk. {fp} elever skulle anklagas felaktigt.',
        [('Hälften av de utpekade eleverna har inte fuskat', True, 'Därför måste en lärare granska varje fall. AI:n kan inte döma själv.'),
         ('AI:n hittar hälften av allt fusk', False, f'Det beskriver recall, som här är {f(exakt(m["rec"]))}.'),
         ('Hälften av alla inlämningar är fusk', False, f'Bara {tp + fn} av {tp + fn + fp + tn} inlämningar var fusk.'),
         ('AI:n gör aldrig fel på elever som inte fuskat', False, f'{fp} elever som inte fuskat pekades ut.')],
        'Räknar precisionen på alla inlämningar eller bara på de utpekade?', 3, oppen=True),
    'rost': lambda m, tp, fn, fp, tn: fv(
        'Ibland vaknar röstassistenten fast ingen har sagt ”Hej Nova”. Vilken sorts fel är det?', 'Falskt positivt',
        'Assistenten svarar ”ordet sades” fast det inte sades. Det är ett falskt positivt.',
        [('Falskt positivt', True, f'Det hände {fp} gånger i testet.'), ('Falskt negativt', False, 'Ett falskt negativt är när någon säger orden men assistenten inte vaknar.'),
         ('Sant positivt', False, 'Ett sant positivt är när orden sades och assistenten vaknade.'),
         ('Sant negativt', False, 'Ett sant negativt är när orden inte sades och assistenten sov vidare.')],
        'Vad svarar assistenten, och vad var sant?', 2),
    'ogras': lambda m, tp, fn, fp, tn: fv(
        'Om roboten sprutar på en nyttig planta skadas den. Vilket mått visar hur stor andel av de besprutade plantorna som verkligen var ogräs?', 'Precision',
        'Roboten sprutar på allt den förutsäger är ogräs. Precisionen är andelen av dem som verkligen var ogräs.',
        [('Precision', True, f'Precisionen är {f(exakt(m["prec"]))}.'), ('Recall', False, 'Recall visar hur stor andel av allt ogräs som besprutades.'),
         ('Träffsäkerhet', False, 'Träffsäkerheten räknar med alla plantor, även de som inte besprutades.'),
         ('Antalet sant negativa', False, 'Sant negativa är nyttiga plantor som roboten lät vara.')],
        'Vilken kolumn i matrisen beskriver de besprutade plantorna?', 2),
}

MATRISER = [
    ('4.20', 'Ett spamfilter har testats på 100 e-postmeddelanden.', 'spam', 'inte spam', 36, 4, 4, 56, ['fel', 'acc', 'prec', 'rec'], None),
    ('4.21', 'En AI som granskar röntgenbilder har testats på 200 patienter för att hitta lungcancer.', 'cancer', 'frisk', 18, 2, 30, 150,
     ['pos', 'acc', 'rec', 'prec'], 'cancer'),
    ('4.22', 'En app som känner igen djur på bilder har testats på 100 bilder av katter och hundar.', 'katt', 'hund', 45, 5, 15, 35,
     ['acc', 'prec', 'rec', 'fn'], None),
    ('4.23', 'En bank använder AI för att hitta bedrägliga kortköp. Den har testats på 1 000 köp.', 'bedrägeri', 'äkta', 8, 12, 2, 978,
     ['acc', 'rec', 'prec'], 'bedrageri'),
    ('4.24', 'En mobil låses upp med ansiktsigenkänning. Den har testats med 200 försök.', 'ägaren', 'någon annan', 95, 5, 5, 95,
     ['fp', 'acc', 'prec'], 'mobil'),
    ('4.25', 'En självkörande bil ska upptäcka fotgängare. Systemet har testats på 250 bilder från bilens kamera.', 'fotgängare', 'ingen fotgängare',
     72, 8, 18, 152, ['fn', 'acc', 'rec', 'prec'], None),
    ('4.26', 'En AI sorterar burkar och flaskor vid en pantstation. Den har testats på 400 föremål.', 'burk', 'flaska', 192, 8, 48, 152,
     ['fn', 'acc', 'prec', 'rec'], None),
    ('4.27', 'En skola testar en AI som ska upptäcka fusk i inlämningar. Den har testats på 50 inlämningar.', 'fusk', 'inte fusk', 4, 1, 4, 41,
     ['fp', 'prec', 'rec'], 'fusk'),
    ('4.28', 'En röstassistent ska vakna när någon säger ”Hej Nova”. Den har testats med 200 korta ljudklipp.', 'orden sades', 'orden sades inte',
     48, 2, 12, 138, ['pos', 'acc', 'prec', 'rec'], 'rost'),
    ('4.29', 'En ogräsrobot ska bara spruta på ogräs. Den har testats på 200 plantor i ett grönsaksland.', 'ogräs', 'nyttig planta', 70, 30, 10, 90,
     ['acc', 'rec', 'prec'], 'ogras'),
]


def matris_task(id_, sammanhang, pos, neg, tp, fn, fp, tn, fragor, tolkning):
    m = matt(tp, fn, fp, tn)
    n = tp + fn + fp + tn
    intro = (matris(pos, neg, tp, fn, fp, tn) + p(sammanhang + ' Klassificeringsmatrisen visar resultatet. Raderna är den verkliga klassen '
                                                  f'och kolumnerna det modellen förutsade. Positiv klass är {pos}.'))
    parts = []
    for fr in fragor:
        if fr == 'fel':
            parts.append(num('Hur många fall klassade modellen fel?', [step('Felen ligger utanför diagonalen: FP + FN', f'{fp} + {fn} = {fp + fn}.')], fp + fn,
                             'Rätt klassade fall ligger på diagonalen. Var ligger felen?', 1))
        elif fr == 'pos':
            parts.append(num(f'Hur många av fallen var verkligen {pos}?', [step('Raden för den positiva klassen: TP + FN', f'{tp} + {fn} = {tp + fn}.')], tp + fn,
                             f'Lägg ihop raden ”Verkligt: {pos}”.', 1))
        elif fr == 'fp':
            parts.append(num(f'Hur många fall klassades som {pos} fast de egentligen var {neg}?',
                             [step('Falskt positiva (FP)', f'Raden ”Verkligt: {neg}” och kolumnen ”Förutsagt: {pos}”: {fp}.')], fp, 'Leta upp rätt rad och kolumn.', 1))
        elif fr == 'fn':
            parts.append(num(f'Hur många fall av {pos} missade modellen?',
                             [step('Falskt negativa (FN)', f'Raden ”Verkligt: {pos}” och kolumnen ”Förutsagt: {neg}”: {fn}.')], fn,
                             f'Leta efter fall som verkligen var {pos} men fick fel klass.', 1))
        elif fr == 'acc':
            parts.append(dec('Bestäm träffsäkerheten (accuracy), alltså andelen av alla fall som modellen klassar rätt.',
                             [step('Träffsäkerhet = (TP + TN) / alla', f'({tp} + {tn}) / {f(n)} = {f(tp + tn)}/{f(n)} = {f(exakt(m["acc"]))}.')],
                             m['acc'], 'Rätt klassade fall finns på diagonalen.', 2))
        elif fr == 'prec':
            parts.append(dec(f'Bestäm precisionen, alltså andelen av fallen som modellen kallade {pos} som verkligen var {pos}.',
                             [step('Precision = TP / (TP + FP)', f'{tp} / ({tp} + {fp}) = {tp}/{tp + fp} = {f(exakt(m["prec"]))}.')],
                             m['prec'], f'Använd kolumnen ”Förutsagt: {pos}”.', 2))
        elif fr == 'rec':
            parts.append(dec(f'Bestäm recall (täckningen), alltså andelen av alla verkliga fall av {pos} som modellen hittade.',
                             [step('Recall = TP / (TP + FN)', f'{tp} / ({tp} + {fn}) = {tp}/{tp + fn} = {f(exakt(m["rec"]))}.')],
                             m['rec'], f'Använd raden ”Verkligt: {pos}”.', 2))
        elif fr == 'f1':
            pr, rc = m['prec'], m['rec']
            f1 = 2 * pr * rc / (pr + rc)
            parts.append(dec('Bestäm F1-värdet. Avrunda till två decimaler.',
                             [step('Precision = TP / (TP + FP) och recall = TP / (TP + FN)',
                                   f'Precision = {tp}/{tp + fp} = {f(exakt(pr))}. Recall = {tp}/{tp + fn} = {f(exakt(rc))}.'),
                              step('F1 = 2 · P · R / (P + R)', f'2 · {f(exakt(pr))} · {f(exakt(rc))} / ({f(exakt(pr))} + {f(exakt(rc))}) ≈ {f(round(float(f1), 2))}.')],
                             round(float(f1), 2), 'Räkna först ut precision och recall.', 3, tol=0.005))
    if tolkning:
        parts.append(TOLKNING[tolkning](m, tp, fn, fp, tn))
    return uppgift(id_, 'klassmatris', 'Beräkna utvärderingsmått', intro, parts, 'Leta först upp TP, FN, FP och TN i matrisen.', ['procedur', 'resonemang'])


for _m in MATRISER:
    ny(lambda m=_m: matris_task(*m))


# ======================================================================== klassmatris: tolka

@ny
def t430():
    intro = (tab(['', 'Förutsagt: sjuk', 'Förutsagt: frisk'], [['<strong>Verkligt: sjuk</strong>', 'sant positiv (TP)', 'falskt negativ (FN)'],
                                                               ['<strong>Verkligt: frisk</strong>', 'falskt positiv (FP)', 'sant negativ (TN)']])
             + p('En klassificeringsmatris har fyra rutor. Här gäller den ett test för en sjukdom, där positiv betyder sjuk.'))
    a = fv('En sjuk person får beskedet att den är frisk. Vilken ruta hamnar personen i?', 'Testet har fel och svarar negativt',
           '”Falskt” betyder att testet har fel. ”Negativt” betyder att testet svarar frisk.',
           [('Falskt negativ (FN)', True, 'Testet missar en sjuk person.'), ('Falskt positiv (FP)', False, 'FP är en frisk person som testet säger är sjuk.'),
            ('Sant negativ (TN)', False, 'TN är en frisk person som testet säger är frisk.'), ('Sant positiv (TP)', False, 'TP är en sjuk person som testet säger är sjuk.')],
           '”Falskt” eller ”sant” säger om testet har rätt. ”Positivt” eller ”negativt” säger vad testet svarar.', 1)
    b = fv('Var i matrisen finns alla fall som testet klassade rätt?', 'Diagonalen', 'TP och TN ligger på diagonalen från övre vänstra till nedre högra hörnet.',
           [('På diagonalen: TP och TN', True, 'Där stämmer verklig och förutsagd klass.'), ('I den översta raden', False, 'Översta raden är alla sjuka, både rätt och fel klassade.'),
            ('I den vänstra kolumnen', False, 'Vänstra kolumnen är alla som fick beskedet sjuk, både rätt och fel.'), ('I rutorna FP och FN', False, 'Det är just felen.')],
           'Var stämmer den verkliga klassen med den förutsagda?', 1)
    c = fv('Testet ändras så att det säger ”sjuk” mycket oftare än förut. Vad händer troligen?', 'Fler sjuka hittas, men fler falska larm',
           'Fler sjuka hittas, så recall ökar. Men fler friska får också larm, så precisionen brukar minska.',
           [('Recall ökar, men precisionen brukar minska', True, 'Det är en avvägning mellan att hitta alla och att undvika falska larm.'),
            ('Både precision och recall ökar', False, 'Fler larm ger fler falska positiva, så precisionen brukar sjunka.'),
            ('Precisionen ökar, men recall minskar', False, 'Det är tvärtom: fler larm ger högre recall.'), ('Ingenting ändras', False, 'Fler larm ändrar både FN och FP.')],
           'Vad händer med antalet FN och FP när testet larmar oftare?', 3, oppen=True)
    return uppgift('4.30', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Sant/falskt: har testet rätt? Positivt/negativt: vad svarar testet?',
                   ['begrepp', 'resonemang'])


@ny
def t431():
    intro = (matris('bedrägeri', 'äkta', 0, 20, 0, 980) + p('En lat modell säger alltid ”äkta” om alla 1 000 kortköp, varav 20 egentligen är bedrägerier.'))
    a = dec('Bestäm träffsäkerheten för den lata modellen.', [step('Träffsäkerhet = (TP + TN) / alla', '(0 + 980) / 1 000 = 0,98.')], Fr(98, 100),
            'Räkna de rätt klassade fallen på diagonalen.', 1)
    b = num('Hur stor är recall för den lata modellen?', [step('Recall = TP / (TP + FN)', '0 / (0 + 20) = 0. Den hittar inget bedrägeri.')], 0,
            'Hur många bedrägerier hittar den?', 2)
    c = fv('Vad visar exemplet?', 'Träffsäkerheten räcker inte när en klass är ovanlig',
           'När en klass är mycket vanligare kan en modell få hög träffsäkerhet utan att vara till någon nytta.',
           [('Hög träffsäkerhet kan vara missvisande när en klass är mycket vanligare än den andra', True, 'Därför används också precision och recall.'),
            ('Modellen är bra eftersom träffsäkerheten är 0,98', False, 'Den hittar inte ett enda bedrägeri.'),
            ('Recall är alltid lika med träffsäkerheten', False, 'Här är träffsäkerheten 0,98 men recall 0.'),
            ('Man ska alltid välja den modell som har högst träffsäkerhet', False, 'Den lata modellen har hög träffsäkerhet men är oanvändbar.')],
           'Är modellen användbar för banken?', 3, oppen=True)
    return uppgift('4.31', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Jämför träffsäkerhet och recall.', ['procedur', 'resonemang'])


@ny
def t432():
    intro = (p('Två modeller ska hitta en ovanlig sjukdom. Båda har testats på samma 1 000 personer, varav 50 är sjuka.')
             + tab(['Modell', 'TP', 'FN', 'FP', 'TN'], [['A', '45', '5', '95', '855'], ['B', '30', '20', '10', '940']]))
    a = dec('Bestäm recall för modell A.', [step('Recall = TP / (TP + FN)', '45 / (45 + 5) = 45/50 = 0,9.')], Fr(45, 50), 'Hur stor andel av de 50 sjuka hittar A?', 2)
    b = dec('Bestäm precisionen för modell B.', [step('Precision = TP / (TP + FP)', '30 / (30 + 10) = 30/40 = 0,75.')], Fr(30, 40), 'Hur stor andel av B:s larm gäller sjuka?', 2)
    c = fv('Sjukdomen är farlig men går att bota om den upptäcks. Ett larm leder till ett enkelt blodprov. Vilken modell bör användas?',
           'Hitta så många sjuka som möjligt', 'A hittar 45 av 50 sjuka (recall 0,9), B bara 30 (recall 0,6). Ett falskt larm kostar bara ett blodprov.',
           [('Modell A, eftersom den missar färre sjuka', True, 'Recall är viktigast när en missad sjuk är farlig och ett falskt larm är billigt.'),
            ('Modell B, eftersom den har högre precision', False, 'B missar 20 sjuka, vilket är värre än några extra blodprov.'),
            ('Modell B, eftersom den har högre träffsäkerhet', False, 'Träffsäkerheten domineras av de 950 friska.'),
            ('Det spelar ingen roll', False, 'A hittar 15 fler sjuka än B.')],
           'Vilket fel är värst: en missad sjuk eller ett onödigt blodprov?', 3)
    return uppgift('4.32', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Välj mått efter vilket fel som är värst.', ['procedur', 'resonemang'])


@ny
def t433():
    intro = p('Frågorna handlar om utvärderingsmåtten precision och recall.')
    a = fv('Ett spamfilter har hög precision men låg recall. Vad märker användaren?', 'Få fel i skräpposten, men mycket spam kommer igenom',
           'Hög precision: det som hamnar i skräpposten är nästan alltid spam. Låg recall: mycket spam hamnar ändå i inkorgen.',
           [('Mycket spam kommer in i inkorgen, men nästan inga riktiga mejl hamnar i skräpposten', True, 'Filtret är försiktigt.'),
            ('Många riktiga mejl hamnar i skräpposten', False, 'Det vore låg precision.'),
            ('Filtret stoppar allt spam', False, 'Det vore hög recall.'),
            ('Ingenting, precision och recall betyder samma sak', False, 'Precision gäller det som stoppas, recall allt spam som finns.')],
           'Vad mäter precision och vad mäter recall?', 3)
    b = fv('Vad räknar precisionen på?', 'Det modellen kallade positivt', 'Precision = TP / (TP + FP): av alla positiva förutsägelser, hur stor andel var rätt.',
           [('Alla fall som modellen förutsade som positiva', True, 'Precisionen säger hur ofta ett larm stämmer.'),
            ('Alla fall som verkligen är positiva', False, 'Det är vad recall räknar på.'), ('Alla fall i testet', False, 'Det är vad träffsäkerheten räknar på.'),
            ('Bara de fall som modellen klassade fel', False, 'Precisionen räknar på både rätt och fel bland de positiva förutsägelserna.')],
           'Vilken kolumn i matrisen används?', 1)
    c = fv('En modell har precisionen 0,8 och recall 0,8. Vad måste då gälla för antalen i matrisen?', 'Samma täljare, samma nämnare',
           'Precision = TP / (TP + FP) och recall = TP / (TP + FN) har samma täljare. Är de lika stora måste nämnarna vara lika, alltså FP = FN.',
           [('Antalet falskt positiva är lika med antalet falskt negativa', True, 'TP + FP = TP + FN ger FP = FN.'),
            ('TP är lika med TN', False, 'TN finns inte med i någon av formlerna.'),
            ('Träffsäkerheten är också 0,8', False, 'Träffsäkerheten beror på TN, som inte syns i precision och recall.'),
            ('Det finns inga fel alls', False, 'Med 0,8 finns det fel, men lika många av varje sort.')],
           'Skriv upp formlerna för precision och recall och jämför dem.', 5)
    return uppgift('4.33', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Precision: kolumnen förutsagt positiv. Recall: raden verkligt positiv.',
                   ['begrepp', 'resonemang'])


@ny
def t434():
    tp, fn, fp, tn = 36, 4, 9, 151
    intro = p('Ett snabbtest för halsfluss prövas på 200 patienter. 40 av dem har halsfluss. Testet ger positivt svar för 36 av dem som har halsfluss '
              'och för 9 av dem som inte har det.')
    a = falt('Fyll i klassificeringsmatrisen. Positiv klass är halsfluss.',
             [step('Sant positiva och falskt negativa bland de 40 sjuka', 'TP = 36. FN = 40 − 36 = 4.'),
              step('Falskt positiva och sant negativa bland de 160 friska', 'FP = 9. TN = 160 − 9 = 151.')],
             'TP = 36, FN = 4, FP = 9, TN = 151.', 'Hur många är friska? Dela upp de sjuka och de friska var för sig.', 2, ['TP', 'FN', 'FP', 'TN'], [tp, fn, fp, tn])
    b = dec('Bestäm testets recall.', [step('Recall = TP / (TP + FN)', '36 / 40 = 0,9.')], Fr(36, 40), 'Hur stor andel av de sjuka får positivt svar?', 2)
    c = dec('Bestäm testets precision.', [step('Precision = TP / (TP + FP)', '36 / (36 + 9) = 36/45 = 0,8.')], Fr(36, 45), 'Hur stor andel av de positiva svaren är rätt?', 2)
    return uppgift('4.34', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Dela först upp patienterna i sjuka och friska.', ['procedur'])


@ny
def t435():
    intro = p('Vilket fel som är värst beror på vad modellen används till. Frågorna handlar om tre olika AI-system.')
    a = fv('En brandvarnare med AI avgör om det brinner (positiv) eller inte. Vilket fel är allvarligast?', 'Missad brand',
           'Ett falskt negativt betyder att det brinner utan att varnaren larmar. Ett falskt larm är bara irriterande.',
           [('Falskt negativt: det brinner men varnaren larmar inte', True, 'Det kan kosta liv.'),
            ('Falskt positivt: varnaren larmar fast det inte brinner', False, 'Det är jobbigt men ofarligt.'),
            ('Sant positivt', False, 'Det är ett rätt larm, inget fel.'), ('Båda felen är lika allvarliga', False, 'En missad brand är mycket värre än ett falskt larm.')],
           'Vad händer i värsta fall vid varje fel?', 2)
    b = fv('Ett spamfilter avgör om ett mejl är spam (positiv) eller inte. Vilket fel är oftast allvarligast för användaren?', 'Viktigt mejl i skräpposten',
           'Ett falskt positivt betyder att ett viktigt mejl, kanske en kallelse till en anställningsintervju, hamnar i skräpposten.',
           [('Falskt positivt: ett riktigt mejl hamnar i skräpposten', True, 'Då kan man missa något viktigt.'),
            ('Falskt negativt: ett spammejl kommer in i inkorgen', False, 'Det är irriterande, men lätt att ta bort.'),
            ('Sant negativt', False, 'Ett riktigt mejl i inkorgen är rätt.'), ('Inget av felen spelar roll', False, 'Ett missat viktigt mejl kan få stora följder.')],
           'Vad är värst: att se ett spammejl eller att missa ett viktigt mejl?', 2)
    c = fv('En svampapp avgör om en svamp är ätlig (positiv) eller inte. Vilket fel är allvarligast?', 'Giftig svamp som kallas ätlig',
           'Ett falskt positivt betyder att en giftig svamp kallas ätlig. Det kan vara livsfarligt.',
           [('Falskt positivt: en giftig svamp kallas ätlig', True, 'Därför ska appen ha mycket hög precision, och man ska aldrig lita på den ensam.'),
            ('Falskt negativt: en ätlig svamp kallas giftig', False, 'Då slänger man bara en god svamp.'),
            ('Sant negativt', False, 'En giftig svamp som kallas giftig är rätt.'), ('Båda är lika farliga', False, 'Att äta en giftig svamp är mycket värre.')],
           'Här är ”positiv” att svampen är ätlig. Vad händer vid varje fel?', 3)
    return uppgift('4.35', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Fundera på vad som händer i verkligheten vid varje sorts fel.', ['resonemang'])


@ny
def t436():
    tp, fn, fp = 40, 10, 40
    tn = 200 - tp - fn - fp
    assert Fr(tp, tp + fn) == Fr(4, 5) and Fr(tp, tp + fp) == Fr(1, 2)
    intro = p('En modell för att hitta diabetes har testats på 200 personer, varav 50 har diabetes. Modellen har recall 0,8 och precision 0,5.')
    a = num('Hur många av de 50 med diabetes hittar modellen (TP)?', [step('Recall = TP / (TP + FN)', 'TP = 0,8 · 50 = 40.')], tp, 'Recall är andelen av de sjuka som hittas.', 2)
    b = num('Hur många falskt positiva (FP) har modellen?',
            [step('Precision = TP / (TP + FP)', '0,5 = 40 / (40 + FP), så 40 + FP = 80.'), step('Lös ut FP', 'FP = 80 − 40 = 40.')], fp,
            'Hälften av alla positiva svar är rätt. Hur många positiva svar ger modellen totalt?', 3)
    c = dec('Bestäm modellens träffsäkerhet.',
            [step('Fyll i resten av matrisen', f'FN = 50 − 40 = 10. TN = 150 − 40 = {tn}.'),
             step('Träffsäkerhet = (TP + TN) / alla', f'(40 + {tn}) / 200 = {40 + tn}/200 = {f(exakt(Fr(tp + tn, 200)))}.')],
            Fr(tp + tn, 200), 'Räkna ut FN och TN först.', 3)
    return uppgift('4.36', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Använd formlerna baklänges.', ['procedur'])


@ny
def t437():
    kl = ['äpple', 'päron', 'banan']
    M = [[18, 2, 0], [3, 16, 1], [0, 0, 20]]
    n = sum(map(sum, M))
    diag = sum(M[i][i] for i in range(3))
    assert n == 60 and diag == 54
    intro = (matris_n(kl, M) + p('En AI i en fruktdisk känner igen tre sorters frukt. Den har testats på 60 frukter. '
                                 'Raderna är den verkliga frukten och kolumnerna det AI:n gissade.'))
    a = num('Hur många päron gissades vara äpplen?', [step('Raden för verkligt päron och kolumnen för förutsagt äpple', 'Där står 3.')], 3, 'Leta upp raden för päron.', 1)
    b = dec('Bestäm träffsäkerheten.', [step('Träffsäkerhet = rätt klassade / alla', f'Diagonalen: 18 + 16 + 20 = {diag}. {diag} / 60 = 0,9.')], Fr(diag, n),
            'De rätt klassade ligger på diagonalen.', 2)
    c = dec('Bestäm recall för päron, alltså andelen av alla päron som AI:n kände igen.', [step('Recall = rätt päron / alla päron', '16 / (3 + 16 + 1) = 16/20 = 0,8.')],
            Fr(16, 20), 'Använd hela raden för päron.', 3)
    d = fv('Vilka två frukter blandar AI:n oftast ihop?', 'Störst tal utanför diagonalen', 'Äpple och päron förväxlas 2 + 3 = 5 gånger. Banan förväxlas bara en gång.',
           [('Äpple och päron', True, 'De liknar varandra i form och färg.'), ('Päron och banan', False, 'Ett päron gissades vara banan en gång, mer än så är det inte.'),
            ('Äpple och banan', False, 'De förväxlas aldrig i testet.'), ('Ingen förväxlas', False, 'Det finns 6 fel utanför diagonalen.')],
           'Titta på talen utanför diagonalen.', 2)
    return uppgift('4.37', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c, d], 'Diagonalen är rätt, resten är förväxlingar.', ['procedur'])


@ny
def t438():
    intro = (p('Ett spamfilter kan ställas in på två sätt. Båda inställningarna har testats på samma 200 mejl, varav 50 är spam.')
             + tab(['Inställning', 'TP', 'FN', 'FP', 'TN'], [['Försiktig', '36', '14', '4', '146'], ['Hård', '48', '2', '12', '138']]))
    a = dec('Bestäm recall för den försiktiga inställningen.', [step('Recall = TP / (TP + FN)', '36 / 50 = 0,72.')], Fr(36, 50), 'Hur stor andel av spammet stoppas?', 2)
    b = dec('Bestäm recall för den hårda inställningen.', [step('Recall = TP / (TP + FN)', '48 / 50 = 0,96.')], Fr(48, 50), 'Samma formel, andra raden.', 2)
    c = dec('Bestäm precisionen för den hårda inställningen.', [step('Precision = TP / (TP + FP)', '48 / (48 + 12) = 48/60 = 0,8.')], Fr(48, 60),
            'Hur stor andel av det som stoppas är spam?', 2)
    d = fv('En skola får viktiga mejl från vårdnadshavare som inte får hamna i skräpposten. Vilken inställning bör skolan välja?', 'Få falskt positiva',
           'Den försiktiga inställningen stoppar bara 4 riktiga mejl, mot 12 för den hårda. Skolan får i stället lite mer spam.',
           [('Den försiktiga, eftersom färre riktiga mejl hamnar i skräpposten', True, '4 falskt positiva jämfört med 12.'),
            ('Den hårda, eftersom den stoppar mer spam', False, 'Den stoppar mer spam men också tre gånger så många riktiga mejl.'),
            ('Den hårda, eftersom den har högre recall', False, 'Hög recall är bra, men här är falskt positiva det värsta felet.'),
            ('Det spelar ingen roll', False, 'Inställningarna gör olika slags fel.')],
           'Vilken ruta i matrisen motsvarar ett viktigt mejl i skräpposten?', 3)
    return uppgift('4.38', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c, d], 'En hårdare inställning ger högre recall men oftast lägre precision.',
                   ['procedur', 'resonemang'])


@ny
def t439():
    intro = (p('Två AI-system ska upptäcka brand i ett lager. De har testats i 1 000 situationer, varav 10 var bränder.')
             + tab(['System', 'TP', 'FN', 'FP', 'TN'], [['A', '10', '0', '20', '970'], ['B', '0', '10', '10', '980']]))
    a = dec('Bestäm träffsäkerheten för system A.', [step('Träffsäkerhet = (TP + TN) / alla', '(10 + 970) / 1 000 = 0,98.')], Fr(98, 100), 'Rätt klassade är TP och TN.', 2)
    b = dec('Bestäm träffsäkerheten för system B.', [step('Träffsäkerhet = (TP + TN) / alla', '(0 + 980) / 1 000 = 0,98.')], Fr(98, 100), 'Samma formel för B.', 2)
    c = fv('Vilket system bör lagret välja?', 'Samma träffsäkerhet, olika fel',
           'A hittar alla 10 bränder men larmar falskt 20 gånger. B hittar inte en enda brand.',
           [('System A, eftersom det hittar alla bränder', True, 'Falska larm är bättre än missade bränder.'),
            ('System B, eftersom det har färre falska larm', False, 'B missar alla bränder, det är oanvändbart.'),
            ('Det spelar ingen roll, de är lika bra', False, 'De har samma träffsäkerhet men gör helt olika fel.'),
            ('System B, eftersom det har fler sant negativa', False, 'Det beror bara på att B aldrig larmar.')],
           'Jämför FN för de två systemen.', 3, oppen=True)
    return uppgift('4.39', 'klassmatris', 'Tolka klassificeringsmatrisen', intro, [a, b, c], 'Samma träffsäkerhet kan dölja helt olika fel.', ['procedur', 'resonemang'])


NYA += ai_ml_modeller.NYA


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    ids = set()
    for fn in NYA:
        u = fn()
        assert u['id'] not in ids, u['id']
        ids.add(u['id'])
        old = next((k for k, x in enumerate(bank) if x['id'] == u['id']), None)
        if old is None:
            bank.append(u)
        else:
            bank[old] = u
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(NYA)} uppgifter i maskininlärning inlagda, {len(bank)} i banken')


if __name__ == '__main__':
    main()
