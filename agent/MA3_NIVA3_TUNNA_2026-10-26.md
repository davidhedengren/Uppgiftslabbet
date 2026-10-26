# Ma3: nivå 3 i tunna områden (2026-10-26)

Inventering i Kunskapsgymmet (spelbara kort på nivå 3, Ma3c):

| Område | Nivå 3 | Totalt |
|---|---|---|
| trig_ekvationer | 2 | 23 |
| derivata_a_x | 3 | 31 |
| trig_ratvinkliga | 3 | 31 |
| sinussatsen_tva_fall | 3 | 16 |
| deriveringsregler | 3 | 52 |
| rationella_uttryck | 4 | 31 |
| forkorta_rationella | 4 | 44 |
| problemlosning_derivata | 4 | 26 |
| primitiva_villkor | 4 | 52 |
| integral_area | 4 | 69 |
| areasatsen | 4 | 33 |
| enhetscirkeln | 4 | 65 |

En annan session fyllde 2026-10-25 flera Ma3-områden med C-kort: derivatagraf, cosinus- och sinussatsen, funktioner, derivatans begrepp, primitiva funktioner, potensderivata och logaritmer. De områdena väntar därför.

Regressionstest: `tools/ma3-niva3-tunna-2026-10-26.test.js`.

## 1. Deriveringsregler: 6 kort, 2.1259–2.1264

| ID | Familj | Innehåll |
|---|---|---|
| 2.1259 | Beräkna derivatans värde | För vilka x är f′(x) = 9? Derivatan ger en andragradsekvation |
| 2.1260 | Derivera polynom | \((x^2+4)/\sqrt x\) skrivs om till potenser innan deriveringen |
| 2.1261 | Beräkna derivatans värde | Punkten där tangenten är parallell med y = 2x + 5 |
| 2.1262 | Beräkna derivatans värde | Volymen i en tank: ändringshastigheten och när ökningen upphör |
| 2.1263 | Beräkna derivatans värde | Vilken funktion har f′(2) = 0 (flerval) |
| 2.1264 | Derivera polynom | En kvot förenklas innan deriveringen |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom. Inga räkneled behövde radbrytas.
- 2.1260 fick ”Svara exakt.”. Annars godtogs 3 för 2,75.
- Validatorn ger 224 fynd både före och efter ändringen.
- Alla Ma3-tester går igenom.
- Självrättningen testades med 16 svar, och alla gav väntat resultat.
