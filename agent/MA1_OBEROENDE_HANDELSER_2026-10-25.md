# Ma1 oberoende händelser: nivå 1–3, 2026-10-25

Läraren bad om en omgång för `oberoende_handelser` (Ma1 kap 5). Området hade 38 kort: ungefär 28 på nivå 1–2 och 5 på nivå 3.

## Nya kort (24, 5.641–5.664): 8 på nivå 1, 9 på nivå 2 och 7 på nivå 3

| Nivå | Innehåll |
|---|---|
| 1 | P(båda) ur ett träddiagram, två larm, två udda tärningar, känna igen oberoende händelser (flerval), gissa en kod med tre siffror, fyra kronor i rad, fylla i en saknad gren i ett träddiagram, lyckohjul två gånger |
| 2 | Minst en etta eller tvåa på två tärningar, exakt en träff på två skott, exakt en fungerande komponent ur träddiagram, minst en pojke bland tre barn, summa 11 ur tärningstabell, minst ett av tre larm, felet att addera sannolikheter (flerval), okänd gren ur produkten längs vägen, tre syskon födda på en lördag |
| 3 | Serie- och parallellkoppling, exakt två av tre, P(B) och P(A eller B), antal kast för minst en sexa, antal skott för minst en träff, pröva om två händelser är oberoende (flerval), bäst av tre matcher |

- Fem figurer: fyra stående träddiagram med raka, färgade grenar (två av dem med en gren att fylla i) och en tärningstabell med alla 36 summor.
- Svarsformerna varierar: bråk, sannolikhet (decimal eller procent), heltal, två delsvar och flerval.
- Miniräknare är tillåten där decimalräkningen blir tung.
- Rätt alternativ står aldrig först.

## Kontroll

- Inget nytt kort har samma facit som ett annat kort i området.
- Validatorn för Ma1 visade först en exakt textdubblett. Kortet ”minst en sexa på två kast” fanns redan i komplementhändelse (5.454). Det byttes mot ”minst en etta eller tvåa”, och därefter ger validatorn inga nya fynd (201 före och efter).
- SVG-granskaren ger 0 fynd för de 5 figurerna.
- `tools/ma1-oberoende-handelser-2026-10-25.test.js` ger 2/2 pass och räknar om varje facit.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 30 svar. Testet täckte bland annat:
  - bråk, decimaler och procent;
  - delsvar i rätt ordning.
- 0,4 godkänns för 0,42, eftersom frågan inte anger någon precision (avrundningsregeln). Det är avsett.
- Hela testsviten ger samma 11 fel som tidigare.
