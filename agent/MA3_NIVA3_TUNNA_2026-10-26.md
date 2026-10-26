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

## 2. Derivatan av aˣ: 6 kort, 2.1265–2.1270

De befintliga korten handlade mest om att derivera aˣ eller skriva om till basen e. De nya korten är tillämpningar:

| ID | Familj | Innehåll |
|---|---|---|
| 2.1265 | Derivera a^x | Befolkningens ökningstakt år 2030, 116 invånare per år |
| 2.1266 | Derivera a^x | När ett läkemedel minskar med 4 mg/h. Derivatan sätts till −4, och svaret är 3,6 h |
| 2.1267 | Derivera a^x | Tangenten till y = 2ˣ i x = 3: k ≈ 5,55 och m ≈ −8,64 |
| 2.1268 | Skriva a^x med basen e | Basen som ger lutningen 2 i x = 0 är a = e² |
| 2.1269 | Derivera a^x | Derivatan av 2⁻ˣ (flerval). De fel alternativen bygger på vanliga misstag |
| 2.1270 | Derivera a^x | Ökningstakten 477 kr/år jämförs med ökningen 487 kr under ett helt år |

Kontroller:

- I 2.1267 har m toleransen 0,011, så att −8,65 godtas. Det svaret får man om man räknar vidare med det avrundade k-värdet.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 6 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Alla Ma3-tester går igenom.
- Självrättningen testades med 15 svar, och alla gav väntat resultat.
