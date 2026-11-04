# Fy1 medelhastighet: facitgranskning 2026-11-04

## Omfattning

Alla **92 huvuduppgifter och 125 explicita delkort** i området är manuellt genomgångna och omskrivna enligt FACITMALL.md. Detta omfattar både äldre 3.x-ID och senare 2.x-ID i samma område. Lösningarna har handskrivna formelrubriker, nummersteg, beräkningsled och separata svarsrutor. Huvuduppgiftens faktiska delindelning kontrolleras även när träningskort saknas.

Alla 92 räknas som åtgärdade på grund av den pedagogiska och strukturella förbättringen. **Granskad – inget fel: inga i denna omgång.** De numeriska rättningsnycklarna behövde inte ändras. Inga kommentarer eller rapportstatusar har skickats till Supabase.

## Fynd och beslut

- 3.1–3.3, 3.19–3.21, 3.49–3.55 och övriga delkort saknade ofta egna avslutande svar. Nu är varje delfacit fullständigt.
- 3.8, 3.51, 3.234, 2.337, 2.345 och 2.349 skiljer vägsträcka från förflyttning, och fart från riktad hastighet.
- 3.9, 3.97, 3.104, 3.178, 3.179, 3.229 och 3.235 förklarar skillnaden mellan lika långa sträckor och lika långa tidsperioder. Del a i 3.97 jämför nu båda bilarna innan vinnaren anges.
- 3.125 besvarar var och en av de tre delarna. 3.131 förklarar vinkel och komponenter. 3.237 visar varför små tidsskillnader kräver oavrundade mellanled. 3.238 härleder ekots olika ut- och retursträckor.
- Avrundade värden markeras med ≈, inte =. Bland annat 3.8, 3.97, 3.104, 3.128, 3.133 och 3.237 behövde denna formella korrigering. Oavrundade uttryck används i fortsatta uträkningar.
- 2.301 c, 2.303 a–c och 2.315 a–c får **sju egna grafiska lösningar**. Modellen ställs upp, tillåten fart anges, skärningen visas och resultatet kontrolleras i ursprungsekvationen. Graferna skiljer total tid från tidsskillnad.
- 2.298 får en fullständig förklaring i stället för bara en beräkningsrad. 2.307/310 anger tidsstart; 2.317/318 skiljer passage förbi en punkt från passage förbi ett helt föremål. 2.320 skiljer sändningsintervall från mottagningsintervall.

Varje återkommande feltyp har följts upp i minst fem analoger. Uppgifter om eko, relativ fart, enhetsbyte, delsträckor och totaltid är genomgångna som separata grupper. Frågor, givna data, ledtrådar, nivåer, rättningsnycklar, toleranser och precisionsmetadata är bevarade.

## Verktyg och verifiering

- Miniräknare tillåts i alla 92 uppgifter; inga delkort förbjuder den. GeoGebra är nu tillåtet i 2.301, 2.303 och 2.315. Övriga tillstånd är bevarade.
- **Alla numeriska huvudnycklar** kontrolleras från uppgiftens givna data i det nya testet `tools/fysik1-medelhastighet-facit-2026-11-04.test.js`, inklusive grafuppgifternas lösningar och ursprungsekvationer. Konceptuppgifter granskas manuellt.
- Äldre områdestester från 2026-10-21/24 samt kapitel 2/3:s numeriska tester passerar. Prosatestet anpassas till det nya användarbeslutet; kontrollen av delbokstäver finns kvar med den nya markeringen.
- Samtliga **217 huvud-/delfacit** renderade i Chromium/KaTeX med båda apparnas CSS vid **390 px**: inga KaTeX-fel eller överskjutande formelrader/svarsrutor efter radbrytning.
- **22 befintliga frågefigurer och sju nya lösningsgrafer** visuellt granskade. Utvalda fullständiga facit och delkort har lästs i mobilvisningen.
- Strukturerad jämförelse: endast 92 huvudfacit, 125 delfacit och tre GeoGebra-flaggor ändras. Authoringskriptet är idempotent.

## Alla granskade, åtgärdade och kommentarsförslag

[Maskinläsbar lista](FY1_MEDELHASTIGHET_FACIT_2026-11-04.json).

| ID | Status | Föreslagen kommentar |
|---|---|---|
| 3.1 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.2 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.3 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.229 | Åtgärdad | Facit härleder medelfarten för lika långa delsträckor och förklarar varför målfarten kräver ett strikt villkor. |
| 3.8 | Åtgärdad | Medelfart, förflyttning och medelhastighet har egna förklaringar och slutsvar. |
| 3.9 | Åtgärdad | Facit visar varför lika långa delsträckor kräver att restiderna räknas först. |
| 3.19 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.20 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.21 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.49 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.50 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.51 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.53 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.54 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.55 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.234 | Åtgärdad | Facit skiljer farten relativt rullgången från farten relativt byggnaden och förklarar gränsfallet. |
| 3.96 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.97 | Åtgärdad | Båda bilarnas tider jämförs redan i del a. Del b förklarar varför medelfarten blir 96 km/h. |
| 3.99 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.101 | Åtgärdad | Banradien skiljs från höjden över jordytan, och oavrundad omkrets används i tiden. |
| 3.102 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.103 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.104 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.235 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.125 | Åtgärdad | Facit har ett separat svar på varje del och jämför turens totala tid med och utan ström. |
| 3.236 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.126 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.127 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.128 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.129 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.130 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.131 | Åtgärdad | Facit förklarar fartkomponenterna, var vinkeln mäts och varför tiden blir längre när färjan styr uppströms. |
| 3.237 | Åtgärdad | Facit behåller extra siffror för den lilla tidsskillnaden och visar varför 0,20 m inte räcker som förklaring. |
| 3.132 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.133 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.134 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.178 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.238 | Åtgärdad | Facit visar hur personens rörelse förkortar ekots retursträcka och ger rätt startavstånd. |
| 3.179 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.256 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.257 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.258 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.259 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.260 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.261 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 3.262 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.291 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.292 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.293 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.294 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.295 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.296 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.297 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.298 | Åtgärdad | Det tidigare mycket korta facit visar nu antalet hundrameterssträckor och omvandlingen till timmar. |
| 2.299 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.300 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.301 | Åtgärdad | Ekvationerna förklaras stegvis. Del c har en grafisk lösning med kontroll och GeoGebra är tillåtet. |
| 2.302 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.303 | Åtgärdad | Alla tre ekvationer löses grafiskt med egna diagram, tillåtna fartintervall och kontroll. GeoGebra är tillåtet. |
| 2.304 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.305 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.306 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.307 | Åtgärdad | Varje del anger att tiden räknas från 10.00 och visar hur den fördröjda starten används. |
| 2.308 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.309 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.310 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.311 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.312 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.313 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.314 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.315 | Åtgärdad | Alla tre fartproblem har grafiska lösningar, fysisk tolkning och kontroll i ursprungsekvationen. GeoGebra är tillåtet. |
| 2.316 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.317 | Åtgärdad | Facit skiljer båtens fart genom vattnet från turens medelfart och förklarar när farter adderas. |
| 2.318 | Åtgärdad | Facit visar varför både tåglängderna behövs vid en fullständig omkörning. |
| 2.319 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.320 | Åtgärdad | Facit förklarar avståndet mellan pulserna och varför en mötande ubåt tar emot dem tätare. |
| 2.335 | Åtgärdad | Facit skiljer startposition från tillryggalagd sträcka. |
| 2.336 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.337 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.338 | Åtgärdad | Facit visar att båda färdsträckorna och hela tiden inklusive pausen ska räknas. |
| 2.339 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.340 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.341 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.342 | Åtgärdad | Facit visar tidsbudgeten, de olika restiderna och en kontroll av hela flygtiden. |
| 2.343 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.344 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.345 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.346 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.347 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.348 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.349 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
| 2.350 | Åtgärdad | Facit visar relevanta formler, enhetsbyten och beräkningssteg samt ett tydligt slutsvar för varje del. |
