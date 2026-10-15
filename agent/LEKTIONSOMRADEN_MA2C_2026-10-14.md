# Balanserade lektionsområden i Matematik 2c – 2026-10-14 (ST03)

## Användarens önskemål

”Det blev väldigt många delområden … ungefär ett område per avsnitt i
planeringen och sedan delmoment som går att punktträna inne i dem. Nu är det
lite för många områden och förut var det lite för få.”

Före ST02 hade 2c 22 kort (för få). Efter ST02 hade 2c 57 kort (för många).
De flesta av de 57 korten hade bara två delmoment.

## Underlag

Planeringarna som användes:

- `Matematik 1c/Planeringar/Planering Ma1c vt26.doc`, v. 9–23. Den täcker Ma2c kap 1 och kap 2.1–2.2.
- `Matematik 2c/Planeringar/Planering Ma2c-3c 2627.doc`, höstdelen. Den täcker kap 2.2–4.
- `Planering Ma2c-Ma3c 2324/2425` användes för att kontrollera att kap 3–4 har samma avsnittsindelning.

Planeringen har ungefär 45 lektionsrader (”Avsnitt”) med bankinnehåll.

## Princip

Ett kort motsvarar ett avsnitt i planeringen, men det ska också ha tillräckligt
många uppgifter. Användaren tyckte att den första versionen med 39 kort gav för
få uppgifter per område: "slå ihop några fler".

I den andra versionen samlas därför närliggande lektioner:

- metoder för samma ekvationstyp,
- lektioner som står på samma rad i planeringen (till exempel Pythagoras + Likformighet),
- numrerade avsnitt i planeringen (2.4 Exponential- och potensekvationer, 4.2 Normalfördelning).

De flesta kort har nu 55–130 träningskort och 4–8 delmoment.

ST01 i ny form: Randvinklar ligger tillsammans med Yttervinkelsatsen, men
aldrig i samma kort som Kordasatsen/bisektrissatsen. Användarens beslut från
2026-10-12 gällde att de två cirkelområdena inte skulle slås ihop.

Resultat för 2c: 57 → 27 kort.

| Kapitel | Kort |
|---|---|
| 1 (4) | Räta linjen · Lösa linjära ekvationssystem (grafiskt, substitution, addition) · Fler ekvationssystem och tillämpningar (tre obekanta, specialfall, tillämpningar) · Uttryck med parenteser och faktorisering |
| 2 (11) | Enkla andragradsekvationer och nollproduktmetoden · Kvadratkomplettering och lösningsformeln · Fördjupning, tillämpningar och rotekvationer · Funktioner – repetition · Andragradsfunktionens graf · Största och minsta värde och från graf till formel · Problemlösning med andragradsfunktioner · Potenser och exponentialfunktioner · Logaritmer · Exponentialekvationer och potensekvationer · Regressionsanalys |
| 3 (7) | Bevis och logik · Yttervinkelsatsen och randvinklar · Pythagoras sats och likformighet · Topptriangelsatsen, transversalsatsen och likformighetsbevis · Kordasatsen och bisektrissatsen · Koordinatgeometri · Problemlösning |
| 4 (5) | Medelvärde, median och typvärde (inkl. tabeller och diagram) · Kvartiler, percentiler och lådagram · Standardavvikelse · Korrelation och linjär regression · Normalfördelning |

Regressionsanalys har bara 15 träningskort, men den står ensam som avsnitt 2.5
och har lämnats orörd. Problemlösning i kap 3 saknar delmoment med minst 5 kort.

## Genomförande

Ändringen gäller bara visningsgrupper.

- Nya grupper i `GRUPPMA2` har `kurs:["2c"]`.
- `konjugat_kvadrering` gäller nu `kurs:["2a","2b"]`, eftersom de reglerna ingår i Uttryck med parenteser och faktorisering i 2c.
- 2c-gruppen `randvinkel_medelpunkt` är `historisk:true` och finns kvar för sparade uppdrag.
- 2a och 2b är oförändrade.

Inga bankobjekt, OMR-nycklar, familjer, ID:n, facit eller nivåer har ändrats.
Genomgångarna följer OMR och hamnar därför automatiskt på rätt kort.

Kunskapsgymmets `hittaTraningskort()` hittar nu även:

- en ensam OMR-nyckel, så att äldre uppdrag som pekar på ett tidigare eget kort fungerar,
- en grupp som numera bara gäller andra spår, till exempel `g:konjugat_kvadrering` i 2c.

Sparade områdesvärden lagras per OMR och behöver ingen migrering.

## Verifiering

- Kunskapsgymmet: 176/176 Node-tester godkända (efter sammanslagning med origin 2026-10-15).
- Uppgiftslabbet: 383/383 Node-tester godkända, utom SVG-sviten (inga figurer har ändrats).
- Lokal webbläsare, 2c:
  - Alla 27 kort har en uppgiftspool, startar med rätt urval och har rätt genomgångar.
  - Varje OMR visas exakt en gång.
  - Äldre nycklar fungerar: `substitutionsmetoden`, `g:konjugat_kvadrering`, `g:randvinkel_medelpunkt` och `g:ekvationssystem`.
  - Familjepass fungerar och punktträningsdialogen visar alla delmoment.
  - Inga konsolfel.
- `ma2c-geometri-omraden.test.js` (ST01) är anpassad till det nya kortnamnet.
- `tools/lektionsomraden.browser.js` är anpassad men kräver Linux-Chromium. Den har inte körts på Hedav.
