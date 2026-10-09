# Fysik 1: två manuella rundor genom vätsketryck

Alla 97 huvuduppgifter, lösningar och fristående delkort har lästs två gånger. Samtliga 97 huvuduppgifter har reviderats. Området omfattar 125 spelkort och 16 uppgifter med manuell rättning. Inga andra områden har ändrats i denna omgång. Exakt ändringslista finns i JSON-rapporten.

## Språk, pedagogik och nivå

- Frågorna skiljer tydligt mellan tryckökningen från ytan och det totala trycket. Varje separat kort har nödvändiga givna värden. Information som bara hör till en annan del har tagits bort.
- Facit visar relevanta enhetsomvandlingar, tryckbidrag från vätskelager, areor, volymer och krafter före slutsvaret. Numrerade lösningssteg används inte. Deluppgifterna har egna rader.
- 6.354 tränar omvandlingen från kPa till Pa. 6.355 jämför tryckökningen vid två djup utan sifferräkning. Dessa ersätter överlappande uppgiftstyper och ger större variation på nivå 1.
- Nivå 1 omfattar direkta samband med givna värden i rätt enheter och enkla jämförelser. Delkort bedöms separat. Exempelvis är 6.445 nivå 3 som heluppgift, medan dess självständiga kraftkort är nivå 2 och ger tryckskillnaden direkt.
- ”Hydrotermal öppning”, ”container” och svårtolkade formuleringar om blodtryck har ersatts med konkreta beskrivningar.

## Konkreta rättningar

- 6.442 visar korrekt avrundning: 101499,52 Pa blir 101000 Pa med tre värdesiffror. Avrundning görs från det oavrundade värdet.
- 6.443 ger 45,75 mm och avrundar till 45,8 mm. Fråga, svarsenhet och självrättning använder mm för kvicksilverpelarens höjd.
- 6.444:s fristående kort ger bara ett konsekvent hjärttryck, 104 mmHg, och räknar vidare från den oavrundade tryckberäkningen. Den motstridiga uppgiften 13,9 kPa har tagits bort.
- 6.445 frågar efter kraften mot ett litet, nästan plant område med given area. Beräkningen av en kraft på en hel cylindrisk mantelyta var missvisande. Delkortet använder sin givna tryckskillnad och får samma avrundade slutsvar som heluppgiften.
- 6.457:s första kort hänvisar inte längre till en träbit som saknas i kortet. De andra kortens lösningar visar tyngdkraft, undanträngd volym och vattenytans höjning.
- 6.460 och 6.462 visar differensen i cm innan den omvandlas till m. Tidigare gav subtraktionen i cm felaktigt sken av att direkt ge ett värde i meter.
- 6.52 och 6.452 använder fönstrets mittpunktsdjup och förklarar medeltrycket. 6.133 och 6.68 visar medeltryck och väggarea innan kraften beräknas.
- Manuella modelluppgifter om blodtryck, vattenledning och tryckmoment har fått sammanhängande, kortare facit med beräkningarna utskrivna.

## Verifiering

- 80 oberoende fysikmodeller kontrollerar samtliga 124 numeriska svarsfält samt facits efterfrågade avrundning.
- Kunskapsgymmets riktiga självrättning klarar 637 numeriska kontrollfall och flervalsfrågans tre alternativ. Kontrollen prövar både korrekta avrundningar, oavrundade värden och felaktiga svar.
- Samtliga frågor och lösningar i området har renderats med 1064 matematikuttryck, utan KaTeX-fel eller numrerade steg.
- Hela Fysik 1 har kontrollerats tekniskt: 4985 spelkort och 32800 rättningskontroller utan fel i kontrollfallen. Detta är ingen oberoende fysikgranskning av återstående områden.
- 162 tester i Uppgiftslabbet, 65 i Kunskapsgymmet och 47 SVG-tester har godkänts.
- Alla 25 figurer har granskats visuellt. Tio representativa kort har granskats på mobil; även datorlayouten har kontrollerats. Ingen displayformel i området är för bred i mobilkontrollen.
- Validatorn ger 0 ERROR, 8 WARNING och 699 INFO. Varningarna är kända dubbletter utanför området. Bankkopiorna är byteidentiska.

## Fortsatt arbete

Övriga kurser är fortsatt pausade. Återstående områden i Fysik 1 behöver fortsatta manuella rundor. Hela banken kan ännu inte beskrivas som fri från pedagogiska eller fysikaliska fel. Användarens nya uppdrag om adminbyte från lärarprofil till elevkonto hanteras separat i Kunskapsgymmet.
