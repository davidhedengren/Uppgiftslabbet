# Fysik 1: arbete – manuell granskning 2026-10-09

Samtliga 108 huvuduppgifter, deras frågor, lösningar, ledtrådar och fristående kort är manuellt genomlästa. En andra genomläsning gjordes efter revideringen. Området har 152 självrättande kort och 23 manuella uppgifter. 104 huvuduppgifter har ändrats. Ingen uppgift utanför området ingår i denna leverans.

## Pedagogik och tydlighet

Frågorna anger vilken krafts arbete eller vilken energi som efterfrågas. Negativt arbete skiljs från ett positivt mått på energiförlust. Facit visar relevanta omvandlingar, höjdskillnader, kraftbalanser och energier innan slutsvaret beräknas. Deluppgifter står på egna rader. Lösningarna använder inga numrerade steg.

- **5.4 c:** eget fullständigt underlag för det lodräta skottet. Det vågräta diagrammet visas bara för det vågräta fallet.
- **5.11:** kulans höjd över mynningen skiljs från höjden över startläget. Fjäderenergin och höjdskillnaden beräknas uttryckligen.
- **5.53 b, 5.57 b och 5.535 b:** korten ger eller räknar fram den energi som behövs. Lösningarna förutsätter inga osynliga tidigare svar. Ändringen i fjäderenergi beräknas från båda energierna.
- **5.209 b:** 433 J godkänns enligt frågans tre värdesiffror. Rättningen använder det oavrundade värdet med rätt avrundningstolerans.
- **5.498 c:** minsta antal hela lyft kräver avrundning uppåt. Svaret är 26 047, och 26 046 avvisas. Energin per lyft beräknas först.
- **5.499:** negativ starthöjd och höjdskillnaden från dal till topp skrivs tydligt.
- **5.501:** energiförändringarna för hiss och motvikt visas var för sig före motorarbetet. Start och slut i vila anges.
- **5.520:** ett tidigare saknat lösningsförslag på del a är tillagt. Fristående kort innehåller endast relevanta givna värden.
- **5.527 a:** ledtrådens felaktiga höjdskillnad är borttagen; facit visar 1,90 − 0,82 = 1,08 m.
- **5.207:** kraftpilen har ändrats så att vinkeln i figuren stämmer med uppgiftens värden.

## Variation och nivå

Flera nästan identiska beräkningar har fått en annan relevant frågetyp: 5.521 omfattar extra gångsträcka, 5.525 c och 5.526 a negativt arbete under sänkning, och 5.527 c minskad lägesenergi när en stapel plockas isär. Frågor, enheter, maskinsvar, lösningar och ledtrådar följer ändringen.

Nivå 1 omfattar de enklaste direkta insättningarna, med given formel och utan dolda kombinationer. Enhetsomvandlingar, enkel kraftbalans och omformning ligger vanligen på nivå 2. Flera samband, ändrad normalkraft och tyngdpunktsgeometri ligger högre. Betygsnivå och träningsnivå bedöms separat.

| Träningsnivå | Före | Efter |
| --- | ---: | ---: |
| 1 | 33 | 32 |
| 2 | 76 | 93 |
| 3 | 40 | 27 |
| 4 | 3 | 0 |
| 5 | 0 | 0 |

## Verifiering

- `tools/fysik1-arbete.test.js`: alla 84 numeriska huvuduppgifter och deras 151 svar räknas självständigt från manuellt avlästa givna värden. Samtliga numeriska slutsvar i lösningarna kontrolleras mot dessa beräkningar.
- Kunskapsgymmets faktiska rättning i Chromium: 160 oberoende kontroller, inklusive enhetsbyte, rätt avrundning, fel tecken och gränser för minsta heltalsantal. Inga fel.
- Hela Fysik 1: 4 977 kort, 32 822 kontroller, inga rättnings- eller formelrenderingsfel i kontrollen.
- Full formelrendering i båda repona: inga renderingsfel eller presentationsfynd.
- Alla 39 figurförekomster i huvuduppgifterna granskade visuellt. Ändringen i 5.207 och den återställda vågräta figuren i 5.4 har granskats efter ändringen.
- Samtliga 152 elevkort och 108 läraruppgifter kontrollerade vid 390 pixels bredd. För långa formler har delats på läsbara rader; inga återstående för breda displayformler. Utvalda kort och figurer granskade visuellt på mobil och dator.
- 128 vanliga tester och 47 SVG-tester i Uppgiftslabbet; 65 tester i Kunskapsgymmet: godkända. SVG-kontrollen körs med miljöns Chromium via `CHROME_PATH`.
- Fysik 1-validator: 0 ERROR, 8 WARNING, 730 INFO. Varningsantalet är oförändrat.
- Bankfilerna är identiska byte för byte.

Kontrollerna kompletterar den manuella analysen. De innebär inte att hela Fysik 1-banken är färdiggranskad eller fri från pedagogiska fel.
