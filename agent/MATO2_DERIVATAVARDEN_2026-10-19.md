# Mato2: derivatavärden och tangentlutning, 2026-10-19

Fortsatt manuell granskning utifrån FP64 och tidigare felloggar om precision,
formuleringar och generiska lösningsmallar. Sex uppgifter granskade och åtgärdade:
2.417, 2.418, 2.419, 2.423, 2.424, 2.425. Granskad – inget fel: inga i denna omgång.
Fem analoger följdes upp till det första fyndet om lösningar utan beräkning.

| ID | Åtgärd och föreslagen kommentar |
|---|---|
| 2.417 | Lösningen visar nu kedjeregeln och insättningen: 3 cos(0)=3. Svaret är oförändrat. |
| 2.418 | Exponenten visas korrekt. Lösningen visar 2e^(2x−1) och 2/e≈0,736. Exakt svar eller tre decimaler godtas. |
| 2.419 | Lösningen visar −2x sin(x²). Maskinfacit räknas från det faktiskt givna x=1,25331, inte det närliggande exakta värdet √(π/2). Svaret till tre decimaler är −2,507. |
| 2.423 | Frågan anger t=1. Lösningen visar s′(t)=3t²−12t+9 och lutningen 0. |
| 2.424 | Frågan anger x=1 och ln visas korrekt. Lösningen visar h′(x)=1/x+1 och lutningen 2. |
| 2.425 | Frågan anger r=3. Lösningen visar A′(r)=2πr och lutningen 6π≈18,85. Exakt svar eller två decimaler godtas. |

Alla sex är E, träningsnivå 2: derivering följd av insättning, snarare än ett
enda direkt grundsamband. E-poängen bevaras. Räknare tillåts, GeoGebra behövs
inte och skulle göra den prövade deriveringen åt eleven. De tre tangentuppgifterna
är procedur/begrepp, inte självständig problemlösning. Inga delkort finns.
Figurer bedömdes: här prövas algebraisk derivering av givna uttryck, inte
avläsning; ingen ny figur tillfördes. Inga ID:n eller övriga bankobjekt ändras.

## Användarbeslut under granskningen: ingen dold precision

När en numerisk fråga saknar precisionskrav godtar rättningen även facit korrekt
avrundat till elevens valda precision. Exempel: 3, 3,1, 3,14 och 3,1416 för π,
men inte 3,15. Exakta heltalsfacit, formkrav, uttryckliga avrundningskrav och
enhetsdimensioner behåller sin kontroll. Avrundning till noll godtas inte som
ersättning för ett litet icke-nollvärde. Detta är en kontroll av avrundningen,
inte en generell procentuell tolerans. Befintliga exakta/mer precisa svar
fortsätter genom den ordinarie rättningen. Regeln finns även i CLAUDE.md.

## Verifiering

- Oberoende centrala differenser kontrollerar alla sex derivatavärden.
- Faktiska elevkort och lärarvisningar kontrollerade vid 390 och 1280 px.
- Nya browserkontroller omfattar både rätta och felaktiga tal, precision,
  exakta svar, enheter, negativa tal och mycket små värden.
- Tidigare browserregression: 418 svarskontroller och 122 vyer passerar.
- Bankvalidator: 72 befintliga fynd före och efter, inga nya.
- Regressionstester för tidigare felloggar, exakta tal, polära svar,
  enhetsprefix, procent och decimalform passerar. Testernas funktionsladdare
  kompletterades med den nya hjälpfunktionen; inga tidigare assertions togs bort.

Före/efter per ändrat objekt sparas i motsvarande JSON. Rapporter i produktion
är inte avslutade och inga kommentarer har skickats till elever.
