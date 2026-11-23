# AI-banken: spelträd på nivå 1–5 och enkla tillämpningar, 23 november 2026

## Uppdrag

Användaren 2026-11-23: ”Jag vill att banken ska ha massor av uppgifter med olika träd i olika storlekar, där de på
nivå 1 bara ska bestämma rotnodens värde, nivå 2 samma sak fast större träd, nivå 3 ska man kunna bestämma vilken gren
som beskärs, nivå 4 samma sak när det är fler grenar och lite större träd, nivå 5 ska man kunna bestämma olika noders
alfa- och betavärden.” Därefter: ”lägga in mycket enkla kontexter i uppgifterna, t.ex. någon ekonomisk eller en
robotisk tillämpning … så man kan förstå att dessa abstrakta värden kan tillämpas” och ”inte bara ersätta, utan kanske
skapa några fler bara med tillämpningar”.

## Resultat: 175 nya uppgifter (3.81–3.255)

| Träningsnivå | Nivå | Område | Uppgift | Grund (spel) | Tillämpning |
|---|---|---|---|---|---|
| 1 | E | Minimax | Rotens värde, två nivåer, 4–7 löv | 3.81–3.110 (30) | 3.216–3.223 (8) |
| 2 | E | Minimax | Rotens värde, tre nivåer, ojämna eller breda träd, 8–14 löv, negativa tal | 3.111–3.140 (30) | 3.224–3.231 (8) |
| 3 | C | Alfa–beta | Vilken gren beskärs (exakt en beskärning), två nivåer, 5–9 löv | 3.141–3.165 (25) | 3.232–3.239 (8) |
| 4 | A | Alfa–beta | Vilka grenar beskärs (minst två beskärningar, djupt eller ett helt delträd), 8–14 löv | 3.166–3.190 (25) | 3.240–3.247 (8) |
| 5 | A | Alfa–beta | α och β i en nod: när sökningen går in i noden eller när den beskär | 3.191–3.215 (25) | 3.248–3.255 (8) |

- Varje uppgift är ett fristående kort med en fråga (`visaSomDelkort`). På papper står frågan utan a).
- Familjer: nivå 1–2 ”Minimaxvärden och bästa drag”, nivå 3–5 ”Rotvärde och beskurna löv”.
- Nivå 3 är C (träningsnivå 3) enligt användarens trappa, fast äldre alfa–beta-uppgifter är A. Undantaget står i
  `bygg-ai-nivaer-2026-11-11.py` (nivån sätts i byggskriptet för 3.81–3.255) och i `ai-nivaer-2026-11-11.test.js`.
- Träden slumpas med fasta frön. Villkor: olika lövvärden, inget träd två gånger, rotens värde är varken största eller
  minsta lövet (nivå 1–2), rätt antal beskärningar och ändliga α och β (nivå 5).
- Svar: tal (nivå 1–2), lövnamn i valfri ordning med `namnmangd` och `kgInstruktion` ”Skriv beteckningarna på löven,
  åtskilda med kommatecken.” (nivå 3–4), två tal med etiketterna α och β (nivå 5).

## Sammanhang

- Grunduppgifterna har spelsammanhang (brädspel, schackdator, stickspel …) och ”MAX väljer först.”/”MIN väljer först.”.
- Tillämpningarna säger vem som är MAX och MIN, vem som väljer först och vad talen betyder: butik och konkurrent (vinst i
  tusentals kronor), säljare och köpare (pris), två robotar som samlar batterier, vaktrobot och inkräktare (säkerhet),
  drönare och vind (minuter flygtid kvar), sparare och börs (vinst i hundratals kronor), schackdator, robotfotboll, två
  företag och reklam, lagerrobot och annan robot (paket per timme), spelagent i luffarschack, Ada och Bo med stickor.
- Negativa tal används bara där de betyder något (förlust, övertag). Vind och börs väljer aldrig först.
- Facit på nivå 1–4 har ett steg om vad rotens värde betyder, t.ex. ”Butiken kan räkna med en vinst på 5 tusen kronor om
  båda väljer så bra de kan.”

## Facit och ledtrådar

- FACITMALL: regeln står i rubriken (”MIN-noderna A, B, C: värdet = min(barnens värden)”, ”Alfa–beta: sluta undersöka en
  nod när α ≥ β”, ”α och β förs nedåt i trädet”), beräkningen nod för nod och svarsraden.
- Facit har trädet med värden vid noderna (”= 5”, ”≤ 3”), beskurna grenar streckade i rött med kryss och grå löv. På
  nivå 5 visar figuren läget i ögonblicket: klara noder, redan beskurna grenar och den efterfrågade noden lila med α och β.
- Nivå 5 spåras med en egen alfa–beta-funktion som jämförs med `ai_speltrad.alphabeta`.
- Ledtrådarna nämner uppgiftens noder (”Bestäm A helt. Vad är roten då säker på? …”).

## Verktyg och kontroll

- Byggskript: `tools/bygg-ai-speltrad-nivaer-2026-11-23.py [--skriv]`. Placering i
  `bygg-ai-omgruppering-2026-11-11.py` (körs efteråt och sorterar banken), nivåregel i `bygg-ai-nivaer-2026-11-11.py`.
- Texterna är unika (validatorns EXACT_TEXT_DUPLICATE): kontext och frågeformulering väljs så att ingen text upprepas.
- Test: `tools/ai-speltrad-nivaer-2026-11-23.test.js` läser träden ur figurerna och räknar om minimax, beskurna löv och
  α/β oberoende. Alla `tools/ai-*.test.js` går igenom. Validatorn: samma fynd i AI-banken som före ändringen.
- Kunskapsgymmet lokalt: 3.216 (tal), 3.141 (”L5, L4” rätt, ”L4” fel) och 3.191 (α och β) rättas rätt.
- Inga etiketter eller rutor utanför figurernas viewBox (kontrollerat för alla 175).
