# Heluppgifter: delfacit och motivering 2026-11-02

Granskningen söker svarsläckage också i uppgifter som inte är uppdelade i `spelDelar`, men har flera svarsfält och en manuell kontroll. Kandidaterna hittades i alla sju banker och lästes tillsammans med uppgift, svarsstruktur, facit och rättningsväg. Denna avgränsade sökning är inte en garanti att alla andra typer av läckage är hittade.

## Ändrade uppgifter

- **Ma1 2.201:** separata facit för linjär respektive exponentiell tabell och för modellen. Skillnaderna är 10, kvoterna 3 och modellen är \(y=5\cdot3^x\). Det första facitet avslöjar inte tabell b och det andra skriver inte ut modellen i c.
- **Ma1 4.22:** separata motiveringar för vektorsummans och differensens längd. Båda är 13 enligt Pythagoras; detta naturliga samband går inte att dölja utan att undanhålla svaret på a.
- **Matf1 4.138:** separata lösningar för jämvikter, lösningen som närmar sig 2 underifrån respektive ovanifrån. Gränsvärdet 2 förekommer naturligt i båda senare delarna, men inte den andra delens riktning.

Huvudlösning, frågetext, metadata och svarsnycklar har behållits. När en heluppgift med flera ordnade svar saknar separat delfacit visar appen inte längre hela lösningen som ersättning. Det är ett skydd mot läckage, inte en fullgod lösning: sådana uppgifter ska få egna delfacit när de upptäcks.

## Ytterligare fem granskade uppgifter och kontroll av rättning

- **Ma1 2.62, 2.232, 2.248 och Ma3 3.1149:** svaren är oordnade och fylls i tillsammans. Inget facit visades före något av dessa svar, men rättningen hoppade över den manuella komplettering som uppgifterna anger. Appen begär nu bedömning av motiveringen först när alla svar är korrekta. Vid fel svar rättas uppgiften som tidigare. Att eleven själv bedömer sin motivering innebär inte att systemet automatiskt kan verifiera den fria texten.
- **Ma1 2.79:** granskad – inget sådant fel. Uppgiften är manuell i sin helhet och visar lösningen för hela svaret, inte mellan separata automatiskt rättade svar.

Kontrollen av motiveringen behålls vid bläddring tillbaka och framåt i passet; en återupptagen fråga börjar om i stället för att ge poäng för osparade svar. Administratörsbläddring och nya frågor rensar tillståndet. Upprepade klick på kontrollera ger inte poäng i förtid. En nekad motivering markerar också svarsraderna som fel.

## Kommentarsförslag

Ingen enskild rapport har markerats eller kommenterats i appen. För en rapport om för tidigt visat facit: ”Tack! Uppgiften har fått separata lösningar för delarna, så att senare svar inte visas när du kontrollerar en tidigare del.” För rapporter om de två uppgifterna med naturligt återkommande svar behöver kommentaren även förklara att samma värde följer av matematiken.

## Kontroll

- Tre riktade banktester verifierar mellanled och separation.
- Webbläsartest på mobil och dator testar de tre uppgifterna, fyra uppgifter med oordnade svar och motivering, alternativa svar och ordning, felaktigt svar, avvisad motivering, flera klick samt navigering tillbaka och framåt under pågående kontroll.
- Tidigare riktade webbläsartester för delkort, kedjor, hela bankernas kedjetexter samt passflöde körs som regression. Kompletta `tools/*.test.js` körs i båda repon; se resultat i leveransen, inklusive kända miljöberoende och tidigare fel.
- Utfallet: båda riktade webbläsartesterna för kedjor och delkort, passflödestestet samt genomgången av 8 659 delkort i 3 144 kedjor passerade. Dessa kontroller jämför visning och data, inte den matematiska kvaliteten i varje uppgift.
- Hela testsviten: Uppgiftslabbet 1 061 godkända och 43 kända fel i SVG-verktygets webbläsarmiljö; Kunskapsgymmet 304 godkända och 10 tidigare identifierade fel. Samma misslyckanden fanns före denna omgång.
