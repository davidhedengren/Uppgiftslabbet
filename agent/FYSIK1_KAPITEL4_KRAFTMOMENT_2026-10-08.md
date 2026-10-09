# Fysik 1: kraftmoment, 2026-10-08

## Omfattning

Samtliga 72 huvuduppgifter och 105 elevkort i kapitel 4, området `moment`, har lästs manuellt två gånger. Frågor, lösningsförslag och ledtrådar har jämförts. 69 huvuduppgifter, som motsvarar 102 kort, är ändrade. ID:n är bevarade. JSON-rapporten anger ändrade fält per ID.

Rapporten gäller detta område. Hela Fysik 1-banken är fortfarande under granskning. Nästa område är blandade kraftuppgifter, därefter senare kapitel och en andra genomgång av hela banken.

## Revidering

Numeriska lösningar visar val av vridpunkt, momentarmar, insatta värden och den uträkning som ger svaret. Lösningarna skiljer kraftbalans från momentbalans och förklarar när tyngdaccelerationen eller en gemensam längdenhet kan förkortas bort. Inga numrerade lösningssteg har införts. Uppgifter med flera frågor har separata rader för delarna.

- **4.291 b:** det fristående stegkortet beräknar nu höjden med Pythagoras sats innan momentbalansen används. En höjd från ett tidigare kort behövs inte.
- **4.11, 4.51, 4.61, 4.130, 4.245 och 4.249:** enklare kort har kortare egna texter utan data för andra deluppgifter. Egna ledtrådar och lösningar passar den fristående frågan.
- **4.508 b:** kortet ger den högra stödkraften 393 N och beräknar den vänstra från kortets egna uppgifter. Skillnaden mellan detta och huvuduppgiftens oavrundade högra kraft är kontrollerad mot rättningens tolerans.
- **4.509:** avståndet 172 cm avser uttryckligen avståndet mellan vågarna. Personens längd används inte som ett oklart mått på momentarmen.
- **4.510–4.513:** jämnt fördelad massa, målarens tyngdpunkt, däckens kontaktpunkter och förutsättningarna för tippning är uttryckliga.
- **4.127:** fyra varianter tränar moment, kraft, momentarm och en fördubbling, i stället för nästan identiska insättningar. Formlerna ges på nivå 1.
- **4.507:** den tidigare upprepningen av linjalens okända massa har ändrats till okänt överhäng. Enhet och rättningsvärde följer den nya frågan.
- **4.515:** en ny geometriskt korrekt figur visar hjulet, kantens höjd, radien och krafterna. Facit beräknar båda momentarmarna och förklarar varför hörnet blir vridpunkt vid lyftgränsen.

Önskad avrundning står i numeriska frågor. Rättningen använder oavrundade beräknade värden med tolerans för tre värdesiffror. Lösningar använder ungefär lika med för avrundade resultat.

## Nivå

Nivå 1 omfattar en enda direkt beräkning med en given formel eller ett enkelt begreppsval. En momentbalans, en enkel enhetsomvandling eller kraftbalans ligger vanligen på nivå 2. Egen bestämning av tyngdpunkt, flera moment eller kombinationen av kraftbalans och momentbalans ligger högre. Träningsnivå och betygsnivå har bedömts separat.

| Träningsnivå | Före | Efter |
| --- | ---: | ---: |
| 1 | 8 | 13 |
| 2 | 24 | 41 |
| 3 | 56 | 39 |
| 4 | 13 | 11 |
| 5 | 4 | 1 |

## Verifiering

- `tools/fysik1-moment.test.js`: 43 numeriska huvuduppgifter med 76 svar räknas från manuellt avlästa givna värden. Alla 76 numeriska slutsvar i lösningsförslagen jämförs med dessa beräkningar. Kortets egna avrundade stödkraft kontrolleras separat.
- Kunskapsgymmets faktiska rättning i Chromium: 77 oberoende beräknade numeriska svar godkända; dessutom godkänns rätt alternativ B och avvisas A i 4.310.
- Hela Fysik 1-banken: 4 977 kort och 32 822 kontroller av rätta svar, format, enheter och felaktiga svar, utan fel i kontrollen.
- Full formelrendering i båda repona: 23 833 formelförekomster per repo, inga renderingsfel eller presentationsfynd.
- Alla 53 figurförekomster i huvuduppgifternas frågor och facit har granskats visuellt. Separata kortfigurer med egna uppgifter har också granskats. Tyngdpunkten i 4.255, proportionerna i 4.304 och marginalen under kraftetiketterna i 4.220 har rättats. Figurerna i 4.76 visar enbart kortets eget fall; ändrade mått och okända massor visas på respektive kort i 4.51, 4.245 och 4.251.
- 122 vanliga tester och 47 SVG-tester i Uppgiftslabbet samt 65 tester i Kunskapsgymmet: godkända.
- Samtliga 105 elevkort och 72 läraruppgifter har kontrollerats för för breda displayformler vid 390 pixels bredd med appens verkliga text- och facitklasser. Breda beräkningar har fått radbrytningar eller beräknade mellanvärden. Inga displayformler kräver sidscrollning i kontrollen. Utvalda fristående kort har också granskats visuellt på mobil och dator, utan horisontellt överflöde.
- Bankvalidator: 0 ERROR, 8 WARNING, 693 INFO. Varningsantalet är oförändrat.
- Bankfilerna är identiska byte för byte. Inga uppgifter utanför området har ändrats i denna leverans.

Kontrollerna kompletterar den manuella analysen och bevisar inte att hela banken saknar pedagogiska fel.
