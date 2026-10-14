# Verktygspolicy och första bankrundan 2026-10-14

Senaste användarbeslutet är infört i båda reponas AGENTS.md/CLAUDE.md, arbetsinstruktionen, de pedagogiska grundreglerna och granskningschecklistan. Verktyg ska kontrolleras vid varje konstruktion, analys, rättning och revidering. Detta ersätter FP45:s statistikspärr.

## Regler

- Miniräknare för beräkningar som inte görs snabbt och enkelt i huvudet: stora produkter, divisioner, potenser, rötter, logaritmer och numerisk trigonometri. Den får gärna användas när den inte tar bort det som faktiskt prövas. Gymnasiematematik testar normalt inte huvudräkning eller aritmetiska handalgoritmer.
- GeoGebra när digitala funktioner behövs: grafanalys/ritning/undersökning, statistik, regression och mer avancerad numerisk eller symbolisk beräkning. En enkel redan given figur eller ett redan givet digitalt resultat kräver inte automatiskt verktyget.
- **GeoGebra tillåtet innebär alltid tillåten miniräknare.** Samma regel gäller per delkort, också med äldre cachemetadata i appen. Fysik får fortsatt alltid ha miniräknare.
- Motivera begränsningar med uppgiftens pedagogiska mål. Uppgifter med olika verktygskrav i delarna ska bedömas per del.

## Omfattning och kvarstående arbete

Alla 17 599 huvuduppgifter i sju banker inventerade strukturellt. GeoGebra/miniräknare-regeln är nu uppfylld i samtliga parent- och delmetadata. **Detta är inte en fullständig pedagogisk genomgång av verktygsbehovet i alla 17 599 uppgifter.** Beräkningssvårighet och metodmål måste bedömas manuellt i efterföljande rundor.

Första avgränsade omgången omfattar 72 verktygsbedömningar: 63 åtgärdade, åtta utan verktygsfel och en kvarstående blandad uppgift. 45 statistikuppgifter får åter miniräknare. 16 frågor som redan efterfrågar digitala undersökningar/beräkningar får GeoGebra-taggen. Två normalfördelningsuppgifter får miniräknare utan GeoGebra för att antalsberäkningen inte ska bli ett huvudräkningstest.

Facit, maskinsvar, toleranser, svarsformat/-enheter, nivåer och figurer bevaras. Bara #4.44/115:s texter ändras: hänvisning till given figur ersätter förbudet mot digitalt verktyg. Ingen numerisk facitrevidering görs i denna omgång.

## Metadatainventering

| Bank | Huvuduppgifter | GeoGebra före/efter | Motstridiga parent/delmetadata före/efter |
|---|---|---|---|
| uppgifter.js | 3780 | 2/2 | 0/0 |
| uppgifter2.js | 1412 | 0/0 | 0/0 |
| uppgifterma1.js | 3968 | 63/63 | 0/0 |
| uppgifterma2.js | 2190 | 172/177 | 90/0 |
| uppgiftermato1.js | 2727 | 61/70 | 0/0 |
| uppgiftermato2.js | 1975 | 566/567 | 0/0 |
| uppgiftermatf1.js | 1547 | 13/14 | 0/0 |

## Kontroller

- 51 relevanta mastertester och 152 konsumenttester godkända. Reglerna kontrolleras i alla banker, och de specifika metodundantagen skyddas.
- Full validator har fått ERROR GEOGEBRA_REQUIRES_CALCULATOR för parent och ärvda/egna delkortstillstånd. Säkra kontraktsfel skiljs från heuristiska granskningskandidater.
- Full validator körd på sju banker: inga nya fynd. Tidigare fynd i andra delar kvarstår. Alla bankkopior är identiska mellan master och konsument.
- 294 riktiga kortvisningar: båda verktygen tillgängliga på statistikdelarna och de 16 digitala frågorna, på mobil/dator. Tidigare spärrad öppen miniräknare förblir nu tillåten på Sx-kort. Extern GeoGebra-knapp, fokus, popup utan opener och oförändrad Sx-rättning verifierade.
- Facit, svar, toleranser, format, nivåer och figurer jämförda mot före-versionerna; inga ändringar.

## Alla granskade, åtgärdade, utan fel och kvarstående

| Bank | ID | Utfall | Bedömning | Kommentarsförslag |
|---|---|---|---|---|
| uppgifterma2.js | 1.342 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 2.757 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.05 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.10 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.28 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.46 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.97 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.157 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.287 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.292 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.241 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.283 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.284 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.299 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.302 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.306 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 5.66 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 5.71 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 5.94 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 5.110 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 5.181 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.328 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.329 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.330 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.331 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.332 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.333 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.334 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.335 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.336 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.337 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.338 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.339 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.340 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.341 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.342 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.343 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.344 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.345 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.346 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.347 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.348 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.349 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.350 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.351 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.364 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.365 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.366 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.371 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.373 | Åtgärdad – verktygsbehörigheter | GeoGebra innebär alltid tillåten miniräknare enligt nya användarbeslutet. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.462 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.467 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.532 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.534 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.583 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.588 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.589 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.590 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato1.js | 3.592 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermato2.js | 2.573 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgiftermatf1.js | 3.287 | Åtgärdad – verktygsbehörigheter | Frågan efterfrågar digital undersökning, numerisk integral, regression eller ekvationslösning. | Verktygstaggarna är uppdaterade: GeoGebra och miniräknare är nu båda tillåtna. |
| uppgifterma2.js | 4.44 | Åtgärdad – verktygsbehörigheter | Normalfördelningsfiguren prövar avläsning av andel; miniräknare tillåts för andel × 800/500. GeoGebra behövs inte när figuren är given. | Verktygstaggarna är uppdaterade: Miniräknare är tillåten för antalsberäkningen; figuren används för att tolka andelen. |
| uppgifterma2.js | 4.115 | Åtgärdad – verktygsbehörigheter | Normalfördelningsfiguren prövar avläsning av andel; miniräknare tillåts för andel × 800/500. GeoGebra behövs inte när figuren är given. | Verktygstaggarna är uppdaterade: Miniräknare är tillåten för antalsberäkningen; figuren används för att tolka andelen. |
| uppgifterma1.js | 3.118 | Granskad – inget fel i verktygsvalet | Potensjämförelse med motivering utan digitala verktyg. Logaritmberäkning skulle ersätta den metod som prövas. | Granskad – inget fel: Potensjämförelse med motivering utan digitala verktyg. Logaritmberäkning skulle ersätta den metod som prövas. |
| uppgifterma1.js | 3.177 | Granskad – inget fel i verktygsvalet | Olikheten ska visas utan digitala verktyg genom potensregler; en numerisk kvot ersätter inte beviset. | Granskad – inget fel: Olikheten ska visas utan digitala verktyg genom potensregler; en numerisk kvot ersätter inte beviset. |
| uppgifterma2.js | 2.55 | Granskad – inget fel i verktygsvalet | En enkel exponentialekvation ska lösas med potensregler utan digitalt verktyg. | Granskad – inget fel: En enkel exponentialekvation ska lösas med potensregler utan digitalt verktyg. |
| uppgifterma2.js | 2.69 | Granskad – inget fel i verktygsvalet | Två modeller är redan givna. Miniräknare tillåts för residualer; eleven behöver inte göra regressionen på nytt. | Granskad – inget fel: Två modeller är redan givna. Miniräknare tillåts för residualer; eleven behöver inte göra regressionen på nytt. |
| uppgifterma2.js | 4.290 | Granskad – inget fel i verktygsvalet | Regressionslinjen är redan given. Miniräknare är tillåten; det saknade värdet bestäms algebraiskt utan att återköra regression. | Granskad – inget fel: Regressionslinjen är redan given. Miniräknare är tillåten; det saknade värdet bestäms algebraiskt utan att återköra regression. |
| uppgiftermato1.js | 3.586 | Granskad – inget fel i verktygsvalet | Integralen ska tolkas som en halvcirkels area utan digitalt verktyg. Numerisk integration skulle ersätta just den tolkningen. | Granskad – inget fel: Integralen ska tolkas som en halvcirkels area utan digitalt verktyg. Numerisk integration skulle ersätta just den tolkningen. |
| uppgiftermatf1.js | 3.53 | Granskad – inget fel i verktygsvalet | Integralvärdet är redan givet. Uppgiften prövar geometrisk betydelse, inte numerisk integration. Miniräknare är tillåten. | Granskad – inget fel: Integralvärdet är redan givet. Uppgiften prövar geometrisk betydelse, inte numerisk integration. Miniräknare är tillåten. |
| uppgiftermatf1.js | 4.87 | Granskad – inget fel i verktygsvalet | Lösningsförslaget är redan givet. Kontroll genom derivata och insättning är målet, inte digital lösning av differentialekvationen. Miniräknare är tillåten. | Granskad – inget fel: Lösningsförslaget är redan givet. Kontroll genom derivata och insättning är målet, inte digital lösning av differentialekvationen. Miniräknare är tillåten. |
| uppgiftermato1.js | 3.466 | Granskad – kvarstående delbedömning | a frågar vad man kan avgöra utan digitalt verktyg; b ber om ett numeriskt integralvärde. Hela uppgiften är inte fristående delkort. Kontrollera metodvillkor och verktygsbehörighet per del i den fortsatta genomgången. Ingen ny GeoGebra-tagg sätts slentrianmässigt. | Delarnas verktygsbehov behöver granskas var för sig. Uppgiften är ännu inte färdigreviderad. |

## Fortsatt grundlig verktygsgenomgång

Gå kurs- och kapitelvis genom matematikbankerna. Börja med numerisk trigonometri, exponential-/logaritmberäkningar, större produkter/bråk, grafundersökning/regression och integraler/derivator. Bedöm också självbärande delkort, inte bara parentens text. Markera varje uppgift färdig först efter att beräkningsbehovet och det prövade innehållet har vägts mot verktygens funktioner. Ta #3.466:s blandade metodvillkor tidigt. Inventering och nyckelord är underlag, aldrig automatisk fullständig pedagogisk granskning.

Kommentarerna är förslag till rapportvyn. Git-push ändrar inte rapportstatus eller elevkommentarer i Supabase.
