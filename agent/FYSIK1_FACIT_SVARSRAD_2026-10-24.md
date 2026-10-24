# Fysik 1-facit: enhetlig form och svarsrad (från 2026-10-24)

Användaren bad att Fysik 1 ska få samma genomgång som Ma3-facit fick 2026-10-23
(`MA3_FACIT_SOM_MA2_2026-10-23.md`): facit ska likna Ma2, och banken ska förbättras
i flera rundor med push mellan varje.

## Skillnad mot Ma3: ingen numrerad steglista i fysik

Fysikfacit skrivs sedan granskningarna 2026-10-08–10 som sammanhängande stycken utan
numrerade steg (se `FYSIK1_KAPITEL3_MANUELL_GRANSKNING_2026-10-08.md`,
`ELEKTRICITET_FYSIK1_2026-10-09.md` och `CLAUDE.md`, avsnittet om förebilden Ma1 #1.116).
Testet `tools/fysik1-prosa.test.js` förbjuder `facit-steglista`. Den regeln gäller
fortfarande. "Likt Ma2" betyder därför för Fysik 1:

- stycken i `facit-forklaring`/`facit-stycke`, där varje stycke förklarar vad som görs
  och visar beräkningen;
- en egen svarsruta sist, `<p class="facit-svar"><strong>Svar:</strong> …</p>`, som i
  de redan granskade Fy1-facit (till exempel 2.232 och 3.271).

Kapitel 9 lämnas utanför svarsradsrundorna, eftersom en annan session arbetar där.

## Rundor

| Runda | Innehåll | Ändrade facit |
|---|---|---:|
| 1 | Numrerade steglistor från nivå 1-rundorna 2026-10-21/22 görs om till stycken | 60 |
| 2 | Lösa svarsstycken blir svarsrutor, och svarsrutor utan etikett normaliseras | 887 + 302 |
| 3 | Svarsruta i enkla numeriska facit och flervalsfacit som saknade svar | 696 |
| 4 | En svarsruta per del i flerdelsfacit som saknade svar | 504 (1 408 rutor) |

### Runda 1

Nivå 1-korten 3.600–3.619 (a-t-diagram), 4.800–4.836 (normalkraft och Newtons tredje
lag) och 9.431, 9.432 och 9.435 hade fått numrerade steglistor. Det bröt mot
fysikregeln, och `fysik1-prosa.test.js` fallerade. Varje steg blev ett stycke, och
texten är oförändrad. 26 facit som bara bestod av en formel fick en förklarande
första mening, till exempel "Hastighetsändringen är arean under a-t-grafen" (3.609) och
"Enligt Newtons tredje lag är kraft och motkraft lika stora" (4.826).

Kända fel före och efter rundan, inte orsakade av den: fem antalskontroller i
`fysik1-kapitel3.test.js` (områdenas antal har ändrats av en annan session) och
figurbreddstestet `svg-bredd-2026-10-21.test.js`.

### Runda 2

- 887 facit hade svaret i ett löst stycke, `<p><strong>Svar:</strong> X</p>` eller
  `<p><strong>Svar: X</strong> Y</p>`. De blev svarsrutor
  `<p class="facit-svar"><strong>Svar:</strong> X</p>`. I flerdelsuppgifter står en
  svarsruta efter varje del, som i de redan granskade Fy1-facit (till exempel 3.28).
- En kommentar efter det fetstilta svaret (47 fall, till exempel "Minustecknet betyder
  att impulsen är riktad åt vänster" i 5.32 c) flyttades till ett eget stycke direkt
  före svarsrutan.
- 302 facit hade svarsrutor utan fetstilt etikett: "Svar: X" (255) och "Svaret är X"
  (145). De fick samma form som övriga. Orden "Svaret är" ersattes av "Svar:".
- 2.62 ("Exempel på svar") och 3.172 (svar i hela meningar per del) lämnades.
- Kontroll: all text finns kvar i varje ändrat facit, bortsett från "Svaret är" → "Svar:",
  och inga andra fält ändrades.

Regressionstest: `tools/fysik1-facit-svarsrad-2026-10-24.test.js`.

### Runda 3

- 591 numeriska facit och 105 flervalsfacit i kapitel 2–8 saknade svar och fick en svarsruta.
- **Talet hämtas ur facit självt:** det sista visade värdet som stämmer med `rättSvar` inom
  toleransen, i samma skrivform (decimaler och tiopotens). Facit visar alltså samma
  avrundning i beräkningen och i svarsrutan. Enheten tas från `svarEnhet`. Grader skrivs
  48,6°, övriga enheter med mellanslag.
- Flervalsfacit får det rätta alternativets text.
- Facit som redan nämner "Svar" i löptext (till exempel 7.35 och 8.79) och facit vars
  yttersta element inte är `facit-v2` lämnades.
- Regressionstestet kontrollerar att talet i varje svarsruta stämmer med självrättningen.

### Runda 4

- 504 flerdelsfacit fick 1 408 svarsrutor, en efter varje del, som i de redan granskade
  Fy1-facit. Delarna hittas via `<p><strong>a)</strong></p>` eller `facit-del`, och antalet
  delar måste vara lika med antalet `rättSvar`. I `facit-del` står rutan sist i `facit-arbete`.
- Talet hämtas ur delens egen lösning med samma regel som i runda 3. Textsvar i `rättSvar`
  används som de står. Delar utan självrättat svar, eller där talet inte syns i delens
  lösning, fick ingen ruta (28 delar).
- Regressionstestet jämför varje dels tal med delens `rättSvar` och tolerans.

Kvar efter runda 4: cirka 90 flerdelsfacit (delarna kunde inte paras ihop säkert med
`rättSvar`) och cirka 325 resonemangsuppgifter utan svarsruta. De flesta resonemangsuppgifter
saknar ett kort entydigt svar och lämnas.
