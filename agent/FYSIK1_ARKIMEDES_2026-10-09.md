# Fysik 1: två manuella rundor genom Arkimedes princip

Alla 134 huvuduppgifter, facit, ledtrådar och fristående delkort har granskats två gånger. Området omfattar 179 spelkort och 20 uppgifter med manuell rättning. 131 huvuduppgifter har ändrats; exakt ändringslista finns i JSON-rapporten. Endast området arkimedes har ändrats, även där uppgifter ligger i kapitel 4.

## Språk, nivå och lösningar

- 6.73 använder ”en kloss med raka, lodräta sidor” och förklarar att klossen har samma material rakt igenom. Heluppgiften och densitetskortet ligger på nivå 3. Höjdfrågan ligger på nivå 1 och procentfrågan på nivå 2.
- Krångliga sammansättningar och överflödiga villkor har förenklats. Varje fristående kort har de mått, krafter, densiteter och konstanter som behövs. Exempel är 6.46, 6.72, 6.113, 6.119, 6.476 och 6.512.
- Facit förklarar kraftbalansen och visar relevanta volymer, massor, lyftkrafter och tyngdkrafter innan slutsvaret. Inga numrerade lösningssteg har lagts tillbaka. Uppgiftens a), b) och c) har egna rader.
- Nivå 1 innehåller direkta samband och enkla jämförelser av två krafter. Enhetsomvandlingar och densitetsförhållanden ligger oftast på nivå 2. Flera sammanlänkade beräkningar och härledningar ligger högre. Delkorten har bedömts separat.
- 6.360 tränar varför lyftkraften inte ändras när en helt nedsänkt sten flyttas djupare i vatten med oförändrad densitet. 6.361 tränar kraftens både storlek och riktning. Detta ökar variationen bland de enkla korten.

## Fysik och självrättning

- 6.118 avrundar 0,2455 N till 0,246 N. 6.119 visar korrekta avläsningar i mN och beräknar först den undanträngda volymen.
- 6.470 visar hela kraftbalansen under vatten. Två värdesiffror ger 390 N och 690 N för statyn. Självrättningen accepterar också de oavrundade svaren 392,8 N och 687,4 N.
- 6.310 godtar det avrundade slutsvaret 19,6 N som facit visar, liksom 19,64 N. Toleransen följer nu den efterfrågade precisionen.
- 6.476 och 6.512 använder tillräckligt precisa givna mellanvärden på fristående kort. Kortens beräkningar ger samma avrundade slutsvar som heluppgiften.
- 6.498 har rimligare värden för flytvästen. 6.501 visar korrekt acceleration. 6.502 anger sin förenklade modell och frågar tydligt efter bollens mittpunkt.
- 6.507 beskriver en liten kula där de givna värdena inte passar en luftbubbla. 6.510 handlar om att hålla en guldtacka stilla helt under vatten, utan en okänd kontaktkraft från botten. 6.511 skiljer höljets massa från gasens massa.
- Luftens lyftkraft förklaras med undanträngd luft, och kvicksilvrets med undanträngt kvicksilver. Beräkningar och förklaringar använder samma medium.

## Verifiering

- 111 oberoende fysikmodeller kontrollerar 176 svarsfält och facits slutsvar. Givna mellanvärden på separata kort har också beräknats oberoende.
- Kunskapsgymmets riktiga rättning klarar 891 numeriska kontrollfall, 12 riktningskontroller och flervalsfrågans tre alternativ. Avrundade och oavrundade korrekta svar godtas; prövade felaktiga svar underkänns.
- Hela Fysik 1 har kontrollerats tekniskt: 4984 spelkort, 32800 svarskontroller, inga rättnings- eller KaTeX-fel i kontrollfallen. Detta är inte en oberoende fysikberäkning av återstående områden.
- 156 tester i Uppgiftslabbet, 65 i Kunskapsgymmet och 47 SVG-tester har godkänts. Efter sista presentationens ändringar har områdets riktade tester och rendering körts igen.
- Alla 47 SVG-figurer har granskats visuellt. 6.74 visar nu flottens ovansida vid vattenytan i maxlastläget. Tio representativa kort har granskats på mobil och dator. Mobilkontrollen av områdets displayformler hittar inga för breda formler.
- Validator: 0 ERROR, 8 WARNING och 699 INFO. Varningarna gäller kända dubbletter utanför området. Bankkopiorna är byteidentiska.
- En extra kontroll av den tidigare gaslagsrundans avrundade slutsvar hittade inga avvikelser från uttryckligen efterfrågad precision.

## Fortsatt arbete

Granskningen fortsätter med vätsketryck och återstående områden i Fysik 1. Denna rapport är inget påstående om att hela banken är fri från pedagogiska eller fysikaliska fel. Övriga kurser är fortsatt pausade.
