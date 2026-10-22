# Fy2 interferens – 2026-10-22

Läraren bad om tre saker:

- fler uppgifter i interferens;
- en kontroll av facit;
- att självrättade kort görs om till automatiskt rättade.

Läraren ville särskilt ha uppgifter där Pythagoras sats och vägskillnaden används för att bestämma till exempel nästa maximum, och med snygga bilder. Två typexempel visades för nivå 2 och uppåt. I båda står högtalarna H₁ och H₂ lodrätt till vänster. En person går från mittpunktsnormalen och stannar vid det n:te ljudminimumet rakt framför en av högtalarna, och uppgiften är att bestämma frekvensen.

## Facit

Alla 52 befintliga kort är omräknade och facit stämde, bland annat 2.149, 2.150, 2.171 och 2.356–2.359.

## Självrättade kort som nu rättas automatiskt (30 st)

| Svarsform | Kort |
|---|---|
| Flerval | 2.90, 2.116, 2.117, 2.118, 2.121, 2.151, 2.152, 2.156, 2.164, 2.165, 2.166 |
| Tal med enhet | 2.78, 2.95, 2.122, 2.148, 2.150, 2.155, 2.158, 2.167, 2.168 |
| Mängd av frekvenser | 2.159, 2.161 |
| Tal och ord | 2.124, 2.154, 2.157, 2.160, 2.162, 2.163, 2.169, 2.175 |

- **Svarsinstruktioner:** frågorna fick en instruktion i parentes, till exempel ”(Svara med maximum eller minimum.)”. Det gäller även delkorten.
- **2.148:** frågan lyder nu ”den näst längsta och den tredje längsta våglängden”, så att svaret blir entydigt.
- **2.157 a:** svaren är ordnade med etiketter.
- **Träningsnivå:** fem kort saknade nivå och fick en: 2.85 (3), 2.149 (4), 2.153 (2), 2.170 (4) och 2.171 (4).

## Nya kort 2.600–2.627 (28 st)

| Nivå | Antal | Exempel |
|---|---|---|
| 1 | 10 | Pythagoras för datorhögtalare, vågbassäng och radiomast; vägskillnad i våglängder; maximum eller minimum (vågbassäng, FM-radio, felkopplad högtalare); vägskillnad i första minimum och på tredje nodlinjen; λ ur första minimum |
| 2 | 7 | lärarens typ: frekvens ur första minimum rakt framför H₂ eller H₁; koordinater i vågbassäng; radiomottagning längs en väg; museigång rakt framför H₁; flytta en högtalare från maximum till minimum; λ ur tredje minimum |
| 3 | 7 | andra minimum med mått i cm; antal maximum längs en väg; antal minimum som passeras; vågfart ur andra nodlinjen; motfas; två minimum passeras; vilket minimum i ordningen |
| 4 | 4 | sista maximum längs vägen (144 m); nästa maximum med GeoGebra; frekvenser som ger minimum (mängd); avstånd till det yttersta minimumet |

### Figurer

- **Lärarens stil:** högtalarna står lodrätt till vänster. De streckade ljudvägarna har färg och mittpunktsnormalen är streckad. En gångpil går från mittpunktsnormalen till P. Måtten är skalenliga och etiketterna har vit bakgrund.
- **Vågbassäng:** vågfronter, nodlinjer ritade som hyperbler och koordinatrutnät.
- **Radiomaster:** en väg som går vinkelrätt mot AB.

### Svar och rättning

- **Ljudets fart anges inte i frågan**, som i lärarens exempel, eftersom den räknas som en standardkonstant. Facit använder 340 m/s.
- **Svar som beror på ljudfarten** rättas med 2 % tolerans i stället för värdesiffror, så att även 343 m/s godtas.
- **Övriga beräkningssvar** har `svarVardesiffror` 2.

## Kunskapsgymmet

`TEXT_ORDKLASSER` godtar nu fler ord som betyder maximum eller minimum, till exempel förstärkning, förstärks, konstruktiv (interferens), interferensmaximum, försvagas, släckning, utsläckning, tyst och destruktiv (interferens). Klasserna motfas och i fas är nya. Inledningar som ”de är” och ”det blir ett” tas nu bort i två varv. Testet är `tools/text-interferens.test.js`.

## Verifiering

- **Validator:** inga nya fynd. Antalet fynd minskade med 30, eftersom inga kort i området är självrättade längre.
- **SVG-granskningen:** 0 fynd för 2.600–2.627. Vågcirklarna ritas som bågar inne i bassängen, eftersom granskaren inte förstår clipPath.
- **Test:** `tools/fy2-interferens-2026-10-22.test.js` räknar om facit för både omgjorda och nya kort. Det kontrollerar också att inga kort är självrättade, att alla har träningsnivå, att svarsinstruktionen finns och att ljudfarten inte står i frågan.
- **Rättningen i Kunskapsgymmet** är prövad med 65 svar i webbläsaren. Alla bedömdes rätt.
- **Hela sviten:** bara de kända felen kvarstår (fysik 1 kapitel 3, fy1-prosa, svg-bredd 2026-10-21 och felrapporter 2026-10-16), och de finns även utan dessa ändringar.

**Lärdom:** kör aldrig `git checkout <bankfil>` för att börja om. Det raderade arbetet i banken, men alla steg var skriptade och kunde köras om.
