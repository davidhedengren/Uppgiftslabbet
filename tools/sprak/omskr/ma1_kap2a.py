# Ma1 kapitel 2, del A (funktionsbegreppet, definitionsmängd och värdemängd, representationer), omskrivet för hand
# 2026-11-17. "Funktionen är f(x) = …" heter nu "Funktionen f ges av f(x) = …", "en elev" har fått namn, "Välj ett
# alternativ." och "(Svara i …)" är borttagna. Delkorten börjar med samma inledning som huvudtexten.
FIG = '<span class="fig">[F1]</span>'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def en(s):
    return f'<div class="spel-en-del">{s}</div>'


I56 = p(r'Funktionen \(f\) ges av \(f(x)=x^2-2\).') + FIG
I61 = p(r'Funktionen \(f\) ges av \(f(x)=2x-1\). En del av grafen visas.') + FIG
I85 = None
I93 = p(r'Kostnaden för ett abonnemang är \(K(n)=59+12n\) kronor, där \(n\) är antalet extra användningar.')
I228 = p(r'Funktionen \(q\) ges av \(q(x)=-2x^2+5\). Leo skriver') + p(r'\[q(-3)=-2\cdot(-3)^2+5=23.\]')
I233 = p(r'Funktionen \(f\) ges av \(f(x)=4x-7\).') + FIG + p('Bestäm:')
I267 = p(r'Funktionen \(f\) ges av \(f(x)=5-3x\).')
I288 = p(r'Funktionen \(f\) ges av \(f(x)=x^2+2\).') + FIG
I297 = p(r'Funktionen \(f\) ges av \(f(x)=3x-1\). Grafen visar bara en del av funktionen.') + FIG
I305 = p(r'Funktionen \(f\) ges av \(f(x)=4x+1\).')
I445 = '<p>Ali påstår att tabellen visar ett linjärt samband.</p>[F1]'
KRAN1 = ('<p>En kran fyller en tank. Tanken är tom när kranen öppnas. Tabellen visar hur mycket vatten som finns i tanken '
         'vid olika tider. Kranen ger lika mycket vatten varje sekund.</p>[F1]')
KRAN2 = ('<p>En kran fyller en tank. Tabellen visar hur mycket vatten som finns i tanken vid olika tider. Kranen ger lika '
         'mycket vatten varje sekund.</p>[F1]')
PROP = 'Är volymen proportionell mot tiden? Motivera ditt svar.'
PROP_KG = 'Är volymen proportionell mot tiden, och varför?'


def kran(intro, liter):
    fr = f'Hur många minuter efter starten finns {liter} liter i tanken?'
    return {'t': intro + p(f'a) {PROP}') + p(f'b) {fr}'),
            'd': {'a': {'t': intro + p(PROP_KG)}, 'b': {'t': intro + p(fr)}}}


R = {
    # ---------------------------------------------------------------- funktionsbegreppet
    '2.15': {'t': p(r'Vad krävs för att ett samband mellan \(x\) och \(y\) ska beskriva \(y\) som en funktion av \(x\)?')},
    '2.56': {'t': I56 + p(r'a) Bestäm \(f(1)\) med grafen.<br>b) Bestäm \(f(4)\).<br>c) Lös \(f(x)=7\).'),
             'd': {'a': {'t': I56 + p(r'Bestäm \(f(1)\) med grafen.')}, 'b': {'t': I56 + p(r'Bestäm \(f(4)\).')},
                   'c': {'t': I56 + p(r'Lös \(f(x)=7\).')}}},
    '2.58': {'t': p(r'Funktionen \(f\) ges av \(f(x)=x^2-1\). Grafen visar bara \(-2\le x\le2\).') + FIG +
             p(r'a) Bestäm \(f(f(0))\).<br>b) Bestäm \(f(f(2))\).<br>c) Förklara varför formeln behövs i b).')},
    '2.61': {'t': I61 + p(r'a) Bestäm \(f(1)\) med hjälp av grafen.<br>b) Bestäm \(f(4)\).'),
             'd': {'a': {'t': I61 + p(r'Bestäm \(f(1)\) med hjälp av grafen.')}, 'b': {'t': I61 + p(r'Bestäm \(f(4)\).')}}},
    '2.89': {'t': p(r'Funktionen \(f\) ges av \(f(x)=4x-5\). Beräkna \(f(7)\).')},
    '2.90': {'t': p(r'För funktionen \(f\) gäller att \(f(x)=2x^2-3x\). Bestäm \(a\) så att') + p(r'\[f(a+1)-f(a)=11.\]')},
    '2.93': {'t': I93 + p(r'a) Beräkna \(K(8)\).<br>b) Vad betyder \(K(0)\) i den här situationen?'),
             'd': {'a': {'t': I93 + p(r'Beräkna \(K(8)\).')}, 'b': {'t': I93 + p(r'Vad betyder \(K(0)\) i den här situationen?')}}},
    '2.226': {'t': p(r'Funktionen \(f\) ges av \(f(x)=x^2+px+q\). För två olika tal \(a\) och \(b\) är \(f(a)=f(b)\).') +
              p(r'a) Visa att \(p=-(a+b)\).<br>b) Dessutom vet man att \(f(1)=f(5)\) och \(f(2)=7\). Beräkna \(f(-2)\).')},
    '2.227': {'t': p(r'Funktionen \(g\) ges av \(g(x)=2x^2+1\). Beräkna \(g(-3)\).')},
    '2.228': {'t': I228 + p(r'a) Förklara felet och beräkna rätt värde.<br>b) Visa algebraiskt att \(q(-x)=q(x)\) för alla \(x\).'),
              'd': {'a': {'t': I228 + p('Förklara felet och beräkna rätt värde.')},
                    'b': {'t': I228 + p(r'Visa algebraiskt att \(q(-x)=q(x)\) för alla \(x\).')}}},
    '2.233': {'t': I233 + p(r'a) \(f(0)\)<br>b) \(f(3)\)<br>c) \(f(-2)\)'),
              'd': {'a': {'t': I233 + en(r'\(f(0)\)')}, 'b': {'t': I233 + en(r'\(f(3)\)')}, 'c': {'t': I233 + en(r'\(f(-2)\)')}}},
    '2.235': {'t': p(r'Funktionen \(h\) ges av \(h(x)=\frac{x+5}{3}\). Beräkna \(h(4)\).')},
    '2.258': {'t': p(r'Funktionen \(f\) ges av \(f(x)=-3x+8\). Beräkna \(f(-4)\).')},
    '2.267': {'t': I267 + p(r'a) Beräkna \(f(-2)\).<br>b) Beräkna \(f(4)\).<br>c) Lös \(f(x)=2\).'),
              'd': {'a': {'t': I267 + en(r'Beräkna \(f(-2)\).')}, 'b': {'t': I267 + en(r'Beräkna \(f(4)\).')},
                    'c': {'t': I267 + en(r'Lös \(f(x)=2\).')}}},
    '2.272': {'t': p(r'Mira påstår: ”Om \(f(2)=6\) och \(f(4)=12\) måste \(f(x)=3x\).”',
                     'Har hon rätt? Om inte, ge ett exempel som visar det. Vilken extra information skulle göra slutsatsen '
                     'säker?')},
    '2.277': {'t': p(r'Funktionen \(f\) ges av \(f(x)=x^2+1\). Omar skriver att \(f(-3)=-8\).',
                     'Förklara felet och beräkna det rätta värdet.')},
    '2.281': {'t': p(r'För en funktion gäller att \(f(-2)=4\) och \(f(2)=4\).',
                     r'Linnea säger: ”Om \(f(a)=f(b)\) måste \(a=b\).” Har hon rätt? Motivera ditt svar med hjälp av '
                     'funktionsvärdena.')},
    '2.287': {'t': p(r'Punkten \((-1,3)\) ligger på grafen till \(y=f(x)\).', 'Vilket påstående måste då vara sant?')},
    '2.288': {'t': I288 + p(r'a) Beräkna \(f(4)\).<br>b) Lös \(f(x)=18\).'),
              'd': {'a': {'t': I288 + p(r'Beräkna \(f(4)\).')}, 'b': {'t': I288 + p(r'Lös \(f(x)=18\).')}}},
    '2.290': {'t': p(r'Funktionen \(f\) ges av \(f(x)=(x-1)^2+1\). Grafen visas nedan.') + FIG +
              p(r'Lös ekvationen \(f(2x-1)=f(x+2)\). Förklara varför två olika fall kan ge samma funktionsvärde.')},
    '2.297': {'t': I297 + p(r'a) Bestäm \(f(1)\) med hjälp av grafen.<br>b) Beräkna \(f(4)\).'),
              'd': {'a': {'t': I297 + p(r'Bestäm \(f(1)\) med hjälp av grafen.')}, 'b': {'t': I297 + p(r'Beräkna \(f(4)\).')}}},
    '2.300': {'t': p('Noah påstår att en funktion kan ha en definitionsmängd med 4 tal och en värdemängd med 5 tal.',
                     r'Är det möjligt? Om definitionsmängden innehåller \(n\) tal, hur många tal kan värdemängden som mest '
                     'innehålla?')},
    '2.302': {'t': p('Elsa säger: ”Alla formler är funktioner.” Ge ett enkelt exempel som visar att påståendet inte stämmer.')},
    '2.305': {'t': I305 + p(r'a) Förenkla \(f(x+2)\).<br>b) Wilma säger att \(f(x+2)=f(x)+2\). Förklara varför det inte '
                            'stämmer och skriv ett korrekt samband.'),
              'd': {'a': {'t': I305 + p(r'Förenkla \(f(x+2)\).')},
                    'b': {'t': I305 + p(r'Wilma säger att \(f(x+2)=f(x)+2\). Förklara varför det inte stämmer och skriv '
                                        'ett korrekt samband.')}}},
    '2.515': {'t': p(r'Vattennivån i en damm är \(h(t)=240-8t\) cm efter \(t\) dygn. Hur hög är nivån efter 12 dygn?')},
    '8.02': {'t': p(r'En tank innehåller \(V(t)=24+3t\) liter vatten efter \(t\) minuter. Hur mycket vatten finns i tanken '
                    'efter 6 minuter?') + FIG},
    # ---------------------------------------------------------------- definitionsmängd och värdemängd
    '2.22': {'t': p(r'Funktionen \(f\) är bara definierad för x-värdena i tabellen.') + '[F1]' +
             p('Ange definitionsmängden och värdemängden.'),
             'kg': 'Skriv varje mängd med klammerparenteser, till exempel {1, 2, 3}.'},
    '2.54': {'t': p(r'En triangel ska ha arean 30 m². Basen är \(b\) meter och höjden \(h\) meter.') +
             p(r'a) Skriv basen \(b\) som funktion av höjden \(h\).<br>b) Basen ska vara minst 2 m och höjden minst 1 m. '
               r'Vilken definitionsmängd har funktionen \(b(h)\)?'),
             'd': {'b': {'t': p(r'En triangel ska ha arean 30 m². Basen \(b\) beror på höjden \(h\) enligt') +
                              p(r'\[b(h)=\frac{60}{h}.\]') +
                              en(r'Basen ska vara minst 2 m och höjden minst 1 m. Vilken definitionsmängd har '
                                 r'funktionen \(b(h)\)?')}}},
    '2.77': {'t': p(r'En buss har 48 sittplatser. Biljettintäkten är \(I(n)=80n\) kronor när \(n\) passagerare åker.',
                    r'Ida anger definitionsmängden \(0\le n\le48\) och värdemängden \(0\le I(n)\le3840\). Förklara vad hon '
                    'har missat i båda svaren och ange mängderna exakt.')},
    '2.80': {'t': p(r'En fullsatt salong har 240 besökare. En vuxenbiljett kostar 90 kr och en barnbiljett 55 kr. Låt \(x\) '
                    'vara antalet vuxna.') +
             p(r'a) Skriv intäkten \(I(x)\).<br>b) Ange exakt definitionsmängd och värdemängd.<br>c) Ebba säger att alla '
               'intäkter mellan den minsta och den största är möjliga. Förklara varför hon har fel.')},
    '2.84': {'t': p(r'Funktionen \(f\) ges av \(f(x)=2x+3\) och har definitionsmängden \(\{0,1,2,3\}\).',
                    'Bestäm värdemängden.')},
    '2.313': {'t': p(r'Funktionen \(f(x)=10-3x\) används för \(0\le x\le3\). Elias säger att värdemängden är '
                     r'\(0\le f(x)\le 10\). Förklara felet och ange rätt värdemängd.')},
    '2.317': {'t': p(r'En behållare med 120 liter vatten töms med 8 liter per minut. Volymen efter \(t\) minuter är '
                     r'\(V(t)=120-8t\) liter. Vilket är det största värde på \(t\) som är rimligt?')},
    '2.318': {'t': p(r'En behållare med 210 liter vatten töms med 15 liter per minut. Volymen efter \(t\) minuter är '
                     r'\(V(t)=210-15t\) liter, från starten tills behållaren är tom. Ange en rimlig definitionsmängd.')},
    '2.319': {'t': p(r'En behållare med 96 liter vatten töms med 6 liter per minut. Volymen är \(V(t)=96-6t\) liter, där '
                     r'\(t\) är tiden i minuter efter att tömningen börjar. Modellen gäller tills behållaren är tom.',
                     'Vilket påstående beskriver definitionsmängden bäst?')},
    '2.509': {'t': p(r'Ett tåg kör med farten 120 km/h i högst 4 timmar. Sträckan i km efter \(t\) timmar är \(s(t)=120t\). '
                     'Vilket är det största värdet i värdemängden?')},
    '2.548': {'t': p(r'En rektangulär hage byggs mot en lång vägg med 60 m staket på de tre andra sidorna. De två sidor som går '
                     r'ut från väggen är \(x\) m långa.', r'Hagens area är \(A(x)=x(60-2x)\).',
                     'Bestäm funktionens definitionsmängd och värdemängd i det här sammanhanget. Använd en graf eller en '
                     'tabell.'),
              'kg': 'Skriv det största x som definitionsmängden närmar sig och sedan den största arean.'},
    # ---------------------------------------------------------------- representationer
    '2.67': {'t': p(r'Funktionen \(f\) ges av \(f(x)=2x-1\). Beräkna \(f(-1)\), \(f(0)\), \(f(2)\) och \(f(4)\).')},
    '2.74': {'t': p('Tabellen visar tre funktionsvärden.') + '[F1]' +
             p(r'Hugo säger att tabellen visar att \(f(x)=2x+1\) för alla \(x\). Visa att han inte kan vara säker genom att '
               r'hitta ett annat funktionsuttryck som ger samma tre värden som i tabellen, men inte samma värden för alla '
               r'\(x\).')},
    '2.331': {'t': p(r'Sambandet mellan \(x\) och \(y\) är \(y=12-2x\).',
                     r'Beskriv med ord startvärdet och hur \(y\) förändras när \(x\) ökar med 1.')},
    '2.337': {'t': p(r'Sambandet mellan \(x\) och \(y\) är \(y=-x+5\).', r'Vilka värden har \(y\) när \(x=0\), 1 och 2?')},
    '2.445': {'t': I445 + p('a) Har han rätt? Motivera ditt svar.<br>b) Bestäm en formel som passar tabellen.'),
              'd': {'a': {'t': I445 + p('Har han rätt? Motivera ditt svar.')},
                    'b': {'t': I445 + p('Bestäm en formel som passar tabellen.')}}},
    '6.31': {'t': p(r'Du ritar graferna till \(y=2x+1\) och \(y=7-x\) i GeoGebra. Vad kan du säga om grafernas '
                    'skärningspunkt?')},
    '6.75': {'t': p(r'Grafen visar \(f(x)=1000+2x\) i fönstret \(0\le x\le10\), \(0\le y\le2000\).') + FIG +
             p('Felix tycker att funktionen ser konstant ut. Förklara varför den gör det och föreslå ett bättre y-fönster '
               'om man vill se förändringen tydligt.')},
    '6.77': {'t': p('Tre modeller visas:', r'\(A(x)=100+15x\)<br>\(B(x)=100\cdot1{,}10^x\)<br>\(C(x)=130+8x\), \(x\ge0\).') +
             FIG + p(r'För vilka \(x\) har respektive modell störst värde?')},
    '6.81': {'t': p(r'Två modeller är \(L(x)=50+8x\) och \(E(x)=90\cdot1{,}04^x\).') + FIG +
             p(r'Ella använder först fönstret \(0\le x\le20\) och hittar en skärningspunkt. Hon drar slutsatsen att modellerna '
               r'bara är lika en gång. Undersök \(0\le x\le40\), bestäm alla skärningspunkter och förklara vad hon har '
               'missat.')},
    '2.549': {'t': p('Två taxibolag tar betalt enligt tabellerna. Priset är linjärt mot sträckan för båda bolagen.') +
              '[F1][F2]' + p('För vilken sträcka kostar bolagen lika mycket?'),
              'kg': 'Avrunda till en decimal.'},
    '2.550': kran(KRAN1, 180),
    '2.551': kran(KRAN1, 72),
    '2.552': kran(KRAN2, 60),
}
