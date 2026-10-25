# Facitgranskning av dagens 489 nya kort, 2026-10-25

Läraren frågade om facit, ledtrådar och svar alltid görs noggrant och bad sedan om en granskning av alla nya uppgifter. Kravet står nu i `CLAUDE.md` (”Facit, ledtråd och svar ska alltid granskas noggrant”) och i `INNEHALLSREGLER.md` 3.6. Läraren har bekräftat att rubrikerna ska skrivas för varje uppgift: ”det är exakt så jag vill ha det”.

## Omfattning

| Bank | Kort | Område och ID |
|---|---|---|
| Ma1 | 99 | Digital ekvationslösning 2.632–2.645, oberoende händelser 5.641–5.664, statistik och intervall 5.665–5.684 och 1.1551–1.1556, nivå 3 omgång B 0.1261–0.1265, 1.1557–1.1566, 4.820–4.823 och 7.781–7.796 |
| Ma2 | 259 | Omgång 4, 7 och 9: 1.1090–1.1228. Omgång 6 och 7: 2.1097–2.1216 |
| Fy1 | 102 | 9.524–9.575, 3.733–3.745, 4.885–4.896, 8.636–8.660 |
| Fy2 | 29 | 5.464–5.486, 3.538–3.543 |

## Fynd och åtgärder

1. **Matematikfacit utan förklarande rubriker (304 kort).**
   - Läget före ändringen:
     - 259 Ma2-kort och 45 Ma1-kort hade bara räknerader.
     - 54 Ma1-kort hade sina rubriker som egna punkter, skilda från beräkningen.
   - Åtgärd: alla 358 matematikfacit har nu formen från 1.116. Varje steg har en `facit-rubrik` och beräkningen står i samma steg.
     - Rubrikerna är skrivna för hand för varje uppgift, till exempel ”\(x^2\) finns i båda leden och tar ut varandra”, ”Gången finns på båda sidor, så båda måtten växer med 2x” och ”Modellen gäller bara tills bilen stannar”.
     - 23 för allmänna rubriker, som ”Skriv ekvationen” och ”Tolka resultatet”, skärptes, till exempel till ”Sätt in \(k=-2\) och \(m=8\)”.
   - Steg som saknades lades till:
     - kontroller i 1.1093, 1.1097 och 1.1103;
     - omräkning från förändringsfaktor till procent i 2.1113 och 2.1177.
   - Facit till 2.1191 skrevs om till en tabell.
2. **Råa `<` och `>` i formler (58 ställen, 39 strängar).**
   - När `<` står före en bokstav, som i `-3<x<6` eller `…<Q(11)` i 2.1190, tolkar webbläsaren det som en html-tagg och texten försvinner.
   - Alla har bytts mot `\lt` och `\gt` (regel 3.8). Svarsfälten (`rättSvar`) är orörda.
3. **Långa räkneled på mobil.** 115 formelblock var bredare än 300 px.
   - De har brutits på flera rader med `gathered`, som i 1.116: påståenden på var sin rad, brytning före ⇒ och sedan vid = eller ≈.
   - Sex långa massdefektsummor i Fy1 kap 9 bröts för hand, så att massan före och massan efter står på var sin rad.
   - Nu är alla 862 block högst 300 px breda, mätt med KaTeX.
4. **Fysikfacit.**
   - Alla har en sammanhängande lösning med modell i ord, samband, beräkning med enheter och en svarsrad.
   - En inledande modellmening lades till i åtta facit där modellen saknades: 9.544, 9.546, 9.549, 3.538, 5.465, 5.471, 5.482 och 5.486.
5. **Ledtrådar.**
   - De korta ledtrådarna lästes igenom. De flesta pekar på nästa steg och passar nivån.
   - Fyra ändrades: 1.1121 och 2.1102 gav nästan bort svaret, och 2.1110 och 2.1191 var för allmänna.
6. **Flerval.** Alla felaktiga alternativ har en kommentar, och inga ändringar behövdes.

## Kontroll

`tools/facitgranskning-2026-10-25.test.js` låser kraven för alla 489 kort:

- rubrik i varje matematiksteg och inga generiska rubriker;
- metodtext i fysikfacit;
- svarsrad, kommenterade felalternativ och ledtråd;
- inga råa `<` eller `>` i formler.

Omgångarnas egna tester passerar, och facit och `rättSvar` är oförändrade i sak. Ett urval från alla banker renderades och lästes igenom.
