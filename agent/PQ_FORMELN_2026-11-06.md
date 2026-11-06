# pq-formeln i alla facit (användarbeslut 2026-11-06)

Läraren: ”Vi använder PQ-formeln i alla kurser, inte ABC, ändra det i alla facit.”

## Regel

- Andragradsekvationer löses med pq-formeln, \(x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}\). Visa först divisionen till normalformen \(x^2+px+q=0\).
- abc-formeln \(\frac{-b\pm\sqrt{b^2-4ac}}{2a}\) används aldrig, inte heller med insatta tal.
- Formeln kallas ”pq-formeln”, inte ”lösningsformeln” eller ”andragradsformeln”.
- I Fy1 är grafisk lösning fortfarande huvudmetoden (FACITMALL 4), med ”Alternativ: pq-formeln”.
- Regeln står i `agent/FACITMALL.md` (avsnitt 3 och 4) och i `CLAUDE.md`.

## Sökning

- `tools/pq-formeln-2026-11-06.test.js` söker i alla sju banker efter:
  - en rot i en bråktäljare, \(\frac{\ldots\pm\sqrt{\ldots}}{\ldots}\), som inte är pq-formens \(-\frac p2\pm\sqrt{\ldots}\);
  - \(b^2-4ac\);
  - orden ”lösningsformeln” och ”andragradsformeln”.
- Träffar som var andra uttryck har lämnats, till exempel:
  - tidlösa formeln \(s=\frac{v^2-v_0^2}{2a}\);
  - Pythagoras sats;
  - exakta trigonometriska värden \(\frac{\sqrt6+\sqrt2}{4}\);
  - \(x=\frac{d}{1+\sqrt{M_2/M_1}}\).

## Ändrade facit

Skript: `tools/pq-formeln-2026-11-06.py`. Varje ny uträkning ger samma rötter som tidigare (kontrollerat numeriskt). Inga `rättSvar` är ändrade.

| Bank | Uppgifter | Ändring |
|---|---|---|
| Fy1 (`uppgifter.js`) | 3.30, 3.123, 3.383, 3.388, 3.389, 3.391, 3.400, 3.404 (konstacc) | ”Alternativ: lösningsformeln” med abc-uttryck blir ”Alternativ: pq-formeln”, med division till normalform. |
| Fy1 | 8.488 (coulomb) | \(\frac{25\pm\sqrt{25^2-4\cdot150}}2\) blir \(12{,}5\pm\sqrt{12{,}5^2-150}\). |
| Fy1 | 5.582, 5.585 (effekt), 5.172 (blandat_energi) | De nya faciten fick pq-formeln som alternativ redan vid omskrivningen samma dag. |
| Fy1 | 14 rubriker i konstacc med mera, till exempel 3.74, 3.118, 3.177, 3.188, 3.360, 3.448, samt 3.189 | De använde redan pq-formen. Namnet ”lösningsformeln” blir ”pq-formeln”. |
| Fy2 (`uppgifter2.js`) | 1.25, 1.113, 1.115, 1.123 (kast) | abc-uttryck med \(4\cdot4{,}91\) eller \(2\cdot9{,}82\) blir normalform och pq-formeln. |
| Ma2 | 2.29, 2.32, 2.70 | ”Lös med andragradsformeln” blir division till normalform och pq-formeln. |
| Ma3c (`uppgiftermato1.js`) | 1.204, 3.48, 3.68, 3.294, 2.16 | Rötter som tidigare angavs i abc-form visas nu med pq-formeln. |
| Ma3c | 1.58, 1.146, 1.153, 1.206, 1.207 | ”lösningsformeln för andragradsekvationer” blir ”pq-formeln”. |
| Ma4 (`uppgiftermato2.js`) | 2.268, 3.79, 4.78, 4.124, 4.402, samt ledtråden i 3.466 | Samma som ovan. I 3.466 står bara ”pq-formeln”. |
| Ma3c, omgång 2 | 1.248, 2.369 | ”Kontroll med andragradsformeln” blir pq-formeln, och 2.369 visar division med 3. |
| Ma4, omgång 2 | 2.01, 2.39, 2.226, 4.25, 4.74, 4.143, 4.144, 4.145, 3.224 | abc-diskriminanten, ”uttrycket under rottecknet i andragradsformeln”, \((2a)^2-4\cdot3\cdot3\), blir pq-formelns rotuttryck efter division till normalform, till exempel \(\frac{a^2}9-1\le0\). Komplexa rötter: \((6\pm\sqrt{-16})/2\) blir \(3\pm\sqrt{9-13}\). |
| Ma5 (`uppgiftermatf1.js`) | 2.152, 2.602 | Samma som ovan. |
| Kunskapsgymmet | `typuppgifter-mato2.js`, genomgången ”Lös en polynomekvation med komplexa rötter” | ”Använd pq-formeln eller lösningsformeln” med abc-uttryck blir pq-formeln: \(x=2\pm\sqrt{4-13}=2\pm3i\). |

Kontroller:

- Alla ändrade facit är renderade i 380 px bredd utan KaTeX-fel.
- Långa pq-kedjor i Fy2 1.113, 1.115, 1.123 och Ma5 2.602 är uppdelade på flera rader.
- Fy2 1.25 har kvar en för bred rad som inte rör pq-formeln, och den var bred redan innan.
- `node --check` gick igenom för alla banker.
- `tools/pq-formeln-2026-11-06.test.js` går igenom.

## Inte ändrat

- Ma2:s kortnamn i `strukturma2.js` heter fortfarande ”Lösningsformel för andragradsekvationer” och ”Kvadratkomplettering och lösningsformeln”, eftersom de syns som kortnamn i Kunskapsgymmet. Uppgifterna i korten använder redan pq-formeln. Fråga till läraren: ska korten byta namn till ”pq-formeln”?
- Ma5 4.595 och 4.626 använder ordet ”lösningsformeln” om differentialekvationer, inte om andragradsekvationer.
