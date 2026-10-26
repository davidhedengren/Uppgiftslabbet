# Ma2 kap 1–2: nivå 3 i tunna områden (2026-10-26)

Inventering i Kunskapsgymmet (spelbara kort på nivå 3, Ma2c): grafisk_losning_ekvationssystem 6, losningsformel_andragrad 6, linjara_representationer 7, exponentialgraf 7, kvadratkomplettering 7. Kap 3–4 fylls av en annan session.

Regressionstest: `tools/ma2-niva3-tunna-2026-10-26.test.js`. Det har ett block per område och räknar om svaren.

## 1. Grafisk lösning av ekvationssystem: 6 kort, 1.1229–1.1234

| ID | Innehåll |
|---|---|
| 1.1229 | Ekvationerna läses av ur grafen, och skärningspunkten (2,4; 3,8) ligger mellan rutpunkterna (figur) |
| 1.1230 | Oändligt många lösningar ger både a och b |
| 1.1231 | Två vattentankar: ett ekvationssystem ställs upp ur texten och grafen (figur) |
| 1.1232 | Skärningspunkten ligger på x-axeln, och m ska bestämmas |
| 1.1233 | Nästan parallella linjer: skärningspunkten (20, 11) ligger utanför figuren (figur) |
| 1.1234 | Parametern c avgör antalet lösningar (flerval) |

Kontroller:

- Facit följer 1.116. Varje steg har en rubrik som är skriven för just den uppgiften. Facit och ledtråd renderades och lästes igenom.
- 1 räkneled radbröts.
- I figurerna ligger axlarna i kanten, så att talen på axlarna inte krockar med linjerna. Etikettrektanglarna är lika stora som texten. SVG-granskaren ger 0 fynd.
- Validatorn ger 219 fynd både före och efter ändringen.
- Självrättningen testades med 17 svar i Kunskapsgymmet, och alla gav väntat resultat. ”2” godtas inte för 2,4, eftersom frågan säger ”exakt”.

## 2. Lösningsformeln: 6 kort, 2.1217–2.1222

De befintliga nivå 3-korten var nästan bara av typen ”lös ax² + bx + c = 0”. De nya korten:

| ID | Innehåll |
|---|---|
| 2.1217 | Rektangelns sidor ur arean. Den negativa roten förkastas (figur) |
| 2.1218 | \((x-1)(x-3)=4\): produkten är inte noll, och svaret är exakt \(2\pm\sqrt5\) |
| 2.1219 | Exakt en lösning: rotuttrycket ska vara 0, vilket ger c = 9 och x = −3 |
| 2.1220 | En lösning är känd: b = 5, och den andra lösningen är −7 |
| 2.1221 | Hitta felet: pq-formeln används utan att ekvationen först delas med 2 (flerval) |
| 2.1222 | \(3x^2=2(x+4)\) med bråk i pq-formeln, som ger 2 och −4/3 |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 2.1220 ändrades från \(x^2+bx-10\) till \(x^2+bx-14\). Facit [3, −5] krockade med 2.1015.
- 1 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 218 fynd både före och efter ändringen.
- Självrättningen testades med 14 svar, och alla gav väntat resultat.
  - Både 2+sqrt(5) och 2+√5 godtas.
  - Närmevärdena 4,24 och −1,33 underkänns, eftersom frågan säger ”exakt”.
