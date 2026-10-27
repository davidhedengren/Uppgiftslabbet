# Facit med förklarande rubrik i varje steg (från 2026-10-27)

Användarbeslut 2026-10-27: alla mattefacit ska ha en rubrik som förklarar steget. Det ska vara mycket pedagogiskt och enkelt för eleverna. Alla facit som inte uppfyller det ska ändras, och fler fel ska letas upp under arbetet.

## Omfattning vid start

Inventeringen gjordes med `facitinventering.js` (scratchpad). Den räknar spelbara uppgifter vars facit, eller något delkortsfacit, saknar rubriker:

| Bank | Uppgifter att göra | Spelbara uppgifter totalt |
|---|---|---|
| Ma1 | 4 045 | 4 418 |
| Ma2 | 2 358 | 3 121 |
| Ma3 | 2 281 | 2 597 |
| Ma4 | 1 966 | 2 047 |
| Ma5 | 1 284 | 1 628 |

Ma5 och Ma2 kap 3 granskas samtidigt i andra sessioner (MATF1_*_FACIT, MA2_KAP3_REVISION).

## Arbetssätt per område

1. Exportera området (`exportera_omr.js`) och läs varje uppgift.
2. Räkna om svaret och notera fel.
3. Skriv facit för hand: en rubrik som säger vad som händer i steget, beräkningen i samma steg och en svarsrad. Rubrikerna skrivs för just den uppgiften och genereras aldrig automatiskt.
4. Kontrollera automatiskt att svarsraden stämmer med `rättSvar` och att varje steg har en rubrik.
5. Rendera och läs ett urval, radbryt långa rader för mobil, lägg till området i `tools/facit-rubriker-2026-10-27.test.js` och kör hela sviten.
6. Committa, pusha och synka till Kunskapsgymmet.

## Klara områden

| Bank | Område | Uppgifter | Fel hittade |
|---|---|---|---|
| Ma1 | tal_rakneordning | 84 nya facit (3 hade redan rubriker) | Inga räknefel. Alla 87 svar är omräknade, även kombinatorikuppgifterna 0.170, 0.173, 0.859, 0.862, 0.1045 och 0.1065. |
| Ma1 | negativa_tal | 94 nya facit (3 hade redan rubriker) | Inga räknefel. Alla 97 svar är omräknade. Kommentarer har lagts till för felaktiga alternativ i 11 flervalskort. 0.134: den allmänna rubriken ”Kontrollera” har bytts mot en specifik. Miniräknarbesluten för 0.866 och 0.1067 i MA1_VERKTYG_2026-10-15 gäller fortfarande. 0.1082–0.1084 har nu riktiga minustecken i frågan. |
