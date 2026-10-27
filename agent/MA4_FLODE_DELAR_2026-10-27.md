# Ma4: flöde och medelvärde med deluppgifter

| Uppgift | Genomgång och ändring |
|---|---|
| 3.209 a | Integralen ger en ökning med \(180+120/\pi\) liter. De 120 liter som fanns från början läggs till, så slutvolymen är \(300+120/\pi\approx338,2\) liter. Huvudfacit och delkort visar beräkningen. Det självrättande målet lagras med full precision. |
| 3.209 b | En hel sinusperiod ger inget nettobidrag; \(360/20=18\) L/min. Både huvudfacit och delkort förklarar medelvärdet. |
| 3.225 a | Första halvperioden ger volymen \(180+144/\pi\approx225,8\) m³. Facit visar primitiv funktion och gränser. |
| 3.225 b | Medelvärdet är \(30+24/\pi\approx37,6\) m³/min, inte 30. Facit förklarar varför sinusbidraget är positivt under en halv period. |

De irrelevanta generella råden om vinklar och längdenheter är borttagna.
I 3.209 har formeln och dess intervall delats upp för mobilvisning, utan
att ändra uppgiften. 3.225 är avstängd från ordinarie träning i
Kunskapsgymmet. Nivåer och verktyg behålls: miniräknare och GeoGebra är
tillåtna. Tidigare jämförelser av samma feltyp finns i
`MA4_FLODESFACIT_2026-10-27.md`: 3.95, 3.105, 3.106, 3.470, 3.121 och 3.248.

Uppgiftslabbet visade båda uppgifterna i 2c. Kunskapsgymmet kontrollerade
46 svar och fyra vyer på mobil och dator för 3.209; enheter, korrekt
avrundning och felaktiga värden prövades. Enligt gällande fri avrundning
kan 300 och 340 godtas som avrundningar av cirka 338,197 till hundratal
respektive tiotal; detta är en följd av att frågan saknar precisionskrav.
320 och 340,0 underkänns. Mobilbilden för a granskades visuellt.
Bankkopior, syntax och diff kontrollerades. Svarsfallen finns i
konsumentens `tools/ma4-flode-delar-2026-10-27.cases.json`.

Författarkällorna `tools/ma4-flode-delar-2026-10-27.py` och
`tools/ma4-flode-delar-mobil-2026-10-27.py` förutsätter den dåtida
bankversionen. Inga rapportstatusar har ändrats i produktionsdatabasen.
