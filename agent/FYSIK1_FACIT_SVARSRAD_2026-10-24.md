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
