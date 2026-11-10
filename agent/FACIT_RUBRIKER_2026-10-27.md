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

## Klara områden i Ma4 (uppgiftermato2.js)

Ma4-sessionen fyller i den här tabellen. Svaren kontrolleras automatiskt mot `rättSvar`, även numeriskt (till exempel `-\tfrac{\sqrt3}{2}` mot `-sqrt(3)/2`).

| Område | Uppgifter | Fel och övriga ändringar |
|---|---|---|
| enhetscirkeln_trianglar | 42 nya facit (1.429 hade redan rubriker, 1.04 är inte spelbar) | Inga räknefel. Alla svar är omräknade, även 1.672 (åttahörningens area \(2\sqrt2\)), 1.679 och 1.680. 1.410 har nu kommentarer på de tre felaktiga alternativen. |
| enhetscirkeln_formler | 34 nya facit (4 är inte spelbara) | Inga räknefel. Alla svar är omräknade. 1.675 (två delfrågor utan delkort) har nu ett facit med a) och b) enligt facitmallen. |
| dubbla_vinkeln | 34 nya facit (14 är inte spelbara) | Inga räknefel. Alla svar är omräknade. 1.214 och 1.220 är samma uppgift; facit är skrivna på olika sätt. 1.250 löses med en 3–4–5-triangel i stället för tangensformeln för sin 2x, som inte står i formelbladet. |
| additionsformler | 28 nya facit (4 är inte spelbara) | Inga räknefel. Alla svar är omräknade. Dubbletter i området: 1.29 och 1.38 samt 1.41 och 1.145 är samma uppgifter (inte borttagna); facit delar upp vinklarna på olika sätt. |
| trig_identiteter | 25 nya facit (1.705 hade redan rubriker, 3 är inte spelbara) | Inga räknefel. Alla svar är omräknade. 1.141 (två delsvar utan delkort) har båda svaren i svarsraden. |
| trig_ekv_formler | 36 nya facit (1.201, 1.240, 1.290 och 1.704 hade redan rubriker, 2 är inte spelbara) | Inga räknefel. Alla vinklar är omräknade och kontrollerade mot `rättSvar`. Andragradsekvationer i \(u=\sin x\) eller \(u=\cos x\) löses med pq-formeln på normalform; ekvationer med en gemensam faktor löses med utbrytning och nollproduktmetoden, med en rubrik om varför man inte delar med faktorn. Allmänna lösningar anger att \(n\in\mathbb Z\). |

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

## Klara områden i Ma3 (uppgiftermato1.js)

Ma3-sessionen fyller i den här tabellen. Hjälpskripten (facitlib.py med svarskontroll, även för delar som bara finns i huvudfacit, och kontroll av att varje felaktigt flervalsalternativ har kommentar) ligger i sessionens scratchpad.

| Område | Uppgifter | Fel och övriga ändringar |
|---|---|---|
| funktioner | 27 nya facit (17 hade redan rubriker) | Inga räknefel. Alla svar och figuravläsningar (1.07, 1.27, 1.32) är omräknade. 1.32 c finns bara i huvudfacit och har nu ett eget delfacit där. 1.453 har kommentarer på de tre felaktiga alternativen. Nya specifika ledtrådar i 1.72, 1.77 och 1.221. |
