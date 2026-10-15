# Ma2: funktioners lösningsgång · 2026-10-15

Fortsättning på FP52 och MA2_LOSNINGSGANG_2026-10-15. Användaren har bett om fortsatt granskning och vill ha resultatet direkt i chatten, med tydlig skillnad mellan ändrade och oförändrade uppgifter. Denna fil är endast internt granskningsspår.

## Omfattning

Samtliga 90 uppgifter i andragradsfunktion_graf, symmetrilinje_extrempunkt och andragradsfunktioner har lästs för att bedöma om facit förklarar lösningen. Huvudfacit och varje delkortsfacit kontrollerades separat. Korta, tillräckliga förklaringar behålls; detta är inte en fullständig omklassificering eller en ny revision av all självrättningsmetadata i de 90 uppgifterna.

## Åtgärdade — 24 uppgifter, 70 lösningsfält

46 delkortsfacit och 24 huvudfacit har kompletterats. Några kort innehöll bara slutsvar. Andra saknade eget s och fick hela huvudfacit, inklusive andra delars svar. För grafavläsning förklaras vilken axel/punkt eleven ska titta på; vid koordinater anges x först, sedan y. Symmetri, extremvärden, insättning och bestämning av faktorn a förklaras med relevanta mellanled.

| ID | Exakta ändringsvägar |
|---|---|
| 2.05 | spelDelar[2].s, s |
| 2.48 | spelDelar[0].s, s |
| 2.83 | spelDelar[0].s, s |
| 2.107 | spelDelar[0].s, s |
| 2.140 | spelDelar[0].s, spelDelar[1].s, s |
| 2.141 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, s |
| 2.144 | s |
| 2.146 | spelDelar[0].s, spelDelar[2].s, s |
| 2.148 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, s |
| 2.157 | spelDelar[0].s, spelDelar[1].s, s |
| 2.238 | s |
| 2.245 | spelDelar[0].s, s |
| 2.247 | spelDelar[0].s, spelDelar[1].s, s |
| 2.273 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, s |
| 2.297 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, s |
| 2.300 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, spelDelar[3].s, s |
| 2.305 | s |
| 2.308 | spelDelar[0].s, spelDelar[1].s, s |
| 2.310 | spelDelar[0].s, spelDelar[1].s, s |
| 2.311 | spelDelar[0].s, spelDelar[1].s, s |
| 2.313 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, spelDelar[3].s, s |
| 2.319 | spelDelar[0].s, spelDelar[1].s, s |
| 2.506 | spelDelar[0].s, spelDelar[1].s, s |
| 2.507 | spelDelar[0].s, spelDelar[1].s, spelDelar[2].s, s |

Särskilda innehållsbeslut:

- 2.141 c, 2.144 och 2.305 visar uttryckligen hur y-skärningen bestämmer a; den slutsatsen ska inte bara påstås. Exempelvis 2.305: f(0)=−8 ger −8=−8a, alltså a=1.
- 2.157/2.247/2.319 får oberoende lösningar även till extremvärdeskortet. Eleven ska inte behöva ha läst det andra kortets facit för att förstå var extrempunkten ligger.
- 2.238:s gamla lösning utgick från att punkten på symmetrilinjen var ett minimum innan a bestämts, trots att frågan inte angav detta. Nu bestäms a först; a=1 visar sedan att parabeln är uppåtvänd.
- 2.273/2.297/2.300/2.308/2.310/2.311/2.313/2.319/2.506/2.507 har egna lösningar per del. Totalt 27 tidigare saknade s-fält tillagda. Grafkortens symmetri kan förklaras med linjen genom extrempunkten utan att samtidigt lista en annan dels nollställen.
- Långa beräkningskedjor delas i korta, justerade rader. Inget generellt gränssnitt eller automatisk elevtext ändras.

Tidigare beslut är bevarade: 2.141 c:s uttrycksformat (2026-10-10), namngivna ordnade koordinater i 2.141/2.146 (2026-10-11) och 2.146 b:s x=1 som symmetrilinjeekvation (2026-10-08). Det tidigare b-kortets s i 2.146 är byteidentiskt; dess verifierade förklaring har inte skrivits över.

## Granskad — ingen motsvarande komplettering behövdes, 66 uppgifter

2.06, 2.08, 2.40, 2.45, 2.46, 2.74, 2.85, 2.86, 2.115, 2.137, 2.139, 2.142, 2.143, 2.145, 2.147, 2.161, 2.165, 2.239, 2.244, 2.258, 2.294, 2.295, 2.296, 2.298, 2.299, 2.301, 2.302, 2.303, 2.304, 2.306, 2.307, 2.309, 2.312, 2.314, 2.315, 2.316, 2.317, 2.318, 2.320, 2.321, 2.322, 2.323, 2.504, 2.505, 2.540, 2.547, 2.548, 2.564, 2.565, 2.566, 2.567, 2.568, 2.571, 2.612, 2.627, 2.628, 2.629, 2.631, 2.694, 2.723, 2.724, 2.734, 2.735, 2.740, 2.748, 2.759

Exempel: 2.06 förklarar avläsning vid x-axeln och mittpunkten mellan nollställena; 2.40 visar bestämning av a och insättning; 2.137 visar både faktorer och utveckling; 2.244 förklarar graf ovanför x-axeln; 2.548/2.565/2.612 visar medelvärdet av nollställena; 2.566 förklarar att kvadraten är minst 0. Korta rutinlösningar har därför inte förlängts bara för längdens skull.

## Matematik och verktyg

De 24 ändrade uppgifterna motsvarar 57 faktiska träningskort. Oberoende polynommodeller har använts för att räkna fram insättningar, nollställen, extrempunkter, tecken och intervall. För de 14 relevanta grafuppgifterna har även 2 896 koordinatpunkter från SVG-kurvorna jämförts med modellerna, efter kalibrering mot skalstreck/axlar (i 2.308 används den markerade punkten (0,5) för y-skalan). Avvikelsen ligger inom figurernas koordinatavrundning. Graferna har inte ändrats.

Verktyg kontrollerade på förälder och varje delkort. Symboliska småtalsuppgifter har miniräknare=false och geogebra=false: grundläggande insättning, kvadratkomplettering och exakt algebra är möjliga utan numeriska verktyg. Grafavläsningsuppgifter behåller miniräknare=true men behöver inte GeoGebra för att läsa den givna figuren. 2.238 behåller miniräknare=true, geogebra=false. Alla delkort ärver förälderns val, och GeoGebra ⇒ miniräknare-kontraktet är uppfyllt. Nivåer, poäng, frågor och all rättningsmetadata bevaras.

## Kontroller

- 379/379 befintliga tester i Uppgiftslabbet och 174/174 i Kunskapsgymmet passerar på den slutliga versionen. Den generella SVG-sviten kördes inte: inga figurer ändrades.
- Chromium i Kunskapsgymmets verkliga gränssnitt: 114 kortvisningar och 48 heluppgiftsvisningar på 390/1280 px, 140 rättningskontroller mot oberoende framräknade svar. Nollställen prövades i omvänd ordning; omvänd koordinatordning avvisades där den ska vara ordnad. Inga formelrenderingsfel eller lån av hela huvudfacit i de ändrade korten.
- Mobilkontrollen mäter även den faktiska formelbasens högra kant, eftersom en nästlad formel kan klippas utan att förälderns scrollWidth växer. För långa rader delades i mellanled och verifierades på nytt. Inga nya överflödande beräkningsrader i den slutliga kontrollen. Skärmbilder på mobil och dator granskade.
- Bankvalidator: 2 190 uppgifter. 257 fynd före, 230 efter. 27 saknade delkortsfacit åtgärdade, inga nya fynd. Övriga fynd ligger utanför detta avgränsade uppdrag.
- Strukturerad diff: exakt 24 objekt, endast s och spelDelar[i].s. JSON-loggen med samma namn innehåller fullständigt före/efter och korrekta fältvägar. Inga uppgifter, svar, figurer, nivåer, toleranser eller verktygsflaggor har ändrats.
- Bankfilerna jämfördes innan synkronisering och var identiska mot master-HEAD. Den godkända banken är åter byteidentisk i båda repona. Cacheversionerna uppdaterade i båda apparna.

## Kommentarsförslag

Inga nya enskilda felrapporter ingick i denna fortsättning. Gemensam kommentar för berörda uppgifter: ”Lösningen är kompletterad med förklaring och relevanta mellanled. Varje delkort visar nu sin egen lösning.”
