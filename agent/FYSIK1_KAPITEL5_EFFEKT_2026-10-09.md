# Fysik 1: effekt – manuell granskning 2026-10-09

Samtliga 110 huvuduppgifter, deras lösningar, ledtrådar och 175 fristående elevkort är manuellt genomlästa. En andra genomläsning gjordes efter revideringen. 20 huvuduppgifter rättas manuellt. 104 huvuduppgifter har ändrats. Ingen uppgift utanför effektområdet ingår i denna leverans.

## Pedagogik och självständiga kort

Frågorna skiljer medeleffekt från effekt i ett ögonblick och nyttig mekanisk effekt från tillförd elektrisk eller kemisk effekt. Facit visar nödvändiga omvandlingar, mellanberäkningar och varför rätt samband används. Deluppgifter har egna rader. Lösningarna använder inga numrerade steg.

- **5.30, 5.42 och 5.152:** varje kort har egna relevanta givna värden; lösningen använder samma underlag. Medeleffekt anges där kortet bara ger arbete och tid.
- **5.22, 5.43, 5.54 och 5.148:** enhetsomvandlingarna från W till kW/MW och från J till MJ visas. Farten räknas ut före effekten vid de olika tidpunkterna.
- **5.140 och 5.272:** hela steg respektive hela kg last avrundas nedåt med en förklaring. Oavrundade energier och effekter används fram till slutsvaret.
- **5.554 och 5.555:** tids- och fartomvandlingarna visas och mellanresultaten behåller sin precision.
- **5.556 b:** energin räcker till tre hela datorer. 3,75 är inte ett möjligt datorantal och godkänns inte.
- **5.557 c:** inköpen gäller hela lampor. Det behövs 14 glödlampor; besparingen är 582,60 kr, eller 583 kr med tre värdesiffror.
- **5.558 c och 5.564 a:** de två rörelseenergierna respektive både läges- och rörelseenergi beräknas innan medeleffekten.
- **5.560:** konstant positiv effekt gäller från en angiven positiv startfart. Modellen kräver inte obegränsad kraft från vila.
- **5.565 b:** den tidigare saknade slutfarten står nu på kortet. Båda energiökningarna visas.
- **5.570 c:** en upprepad uppförsberäkning har ersatts av bromsning nedför. Lösningen förklarar negativt bromsarbete och den efterfrågade positiva effekten som tas från rörelsen.
- **5.563 b, 5.567 b och 5.574 b:** ett nytt, uttryckligt motståndsvärde eller modellvärde ges för det separata fallet. Kortet förutsätter inte ett avrundat svar från föregående del.
- **5.576 och 5.577:** vågrät väg ger kortare texter och tydligare samband mellan effekt, drivkraft och acceleration.
- **5.591 och 5.593:** minsta antal verk avrundas uppåt och största antal lyft nedåt; gränserna kontrolleras i rättningen.
- **5.598 a:** huvuduppgiften anger nu både verkningsgrad och dragkraft, som tidigare bara stod på elevkortet.
- **5.599:** felaktiga mellanresultat i lösningen har rättats. Oavrundad kraft ger 13 705,04… W och slutsvaret 13,7 kW.

## Variation och nivå

Nivå 1 gäller de enklaste direkta insättningarna med given formel. Omvandlingar och enkel omformning ligger vanligen på nivå 2. Flera energier eller kraftbalanser ligger högre. Rutinberäkningar med flera samband har sänkts från A till C där de inte kräver självständig analys. Symboliska generaliseringar och bedömning av otillräckligt underlag ligger kvar högre. Träningsnivå och betygsnivå bedöms separat.

| Elevkortens träningsnivå | Före | Efter |
| --- | ---: | ---: |
| 1 | 18 | 19 |
| 2 | 69 | 70 |
| 3 | 66 | 66 |
| 4 | 15 | 20 |
| 5 | 7 | 0 |

## Verifiering

- `tools/fysik1-effekt.test.js`: alla 90 numeriska huvuduppgifter och deras 175 svar räknas självständigt från manuellt avlästa givna värden. Alla numeriska slutsvar i lösningarna jämförs med dessa beräkningar.
- Kunskapsgymmets faktiska rättning i Chromium: 187 kontroller, inklusive avrundning, heltalsgränser, decimalform, enheter och fel tecken. Inga fel.
- Hela Fysik 1: 4977 kort och 32 822 rättningskontroller, inga fel i kontrollen.
- Full formelrendering i båda repona: 23 800 respektive 23 801 formler, inga renderingsfel eller presentationsfynd.
- Områdets två huvudfigurer granskade visuellt. Alla 175 elevkort och 110 läraruppgifter kontrollerade vid 390 pixels bredd. Inga återstående för breda displayformler. Utvalda kort granskade visuellt på mobil och dator.
- 131 vanliga tester och 47 SVG-tester i Uppgiftslabbet; 65 tester i Kunskapsgymmet: godkända. SVG-kontrollen körs med miljöns Chromium via `CHROME_PATH`.
- Fysik 1-validator: 0 ERROR, 8 WARNING, 730 INFO, oförändrat varningsantal.
- Bankfilerna är identiska byte för byte.

Kontrollerna kompletterar den manuella analysen. Hela Fysik 1-banken är ännu inte färdiggranskad; automatiska kontroller kan inte garantera felfri pedagogik.
