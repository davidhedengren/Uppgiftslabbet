# AI-banken: kapitel 4 Maskininlärning (2026-11-12)

Användaren delade lärarens planering (Artificiell intelligens 1, TE24 2026/2027) och bad om uppgifter i kursens
övriga områden, anpassade till gymnasiet och AI1. Önskemålen var flerval med vanliga missförstånd som felaktiga
alternativ, numeriska uppgifter och många klassificeringsmatriser, både med teori och med beräkningar.

Det här är första steget: maskininlärning, alltså planeringens veckor 2–12 och aktiviteten
”klassificeringsmatriser”. Grunderna (AI, data, agenter och beslutsträd), förstärkningsinlärning,
språkteknologi och etik/lagstiftning återstår.

## Struktur

Kapitel 4 ”Maskininlärning” har fem kort. Varje kort har två delmoment med minst åtta uppgifter per delmoment.

| Kort (`omr`) | Delmoment | Uppgifter | Delkort E / C / A | Nivå 1 |
|---|---|---|---|---|
| Grunder i maskininlärning (`ml_grunder`) | Typer av inlärning; Träning, test och överanpassning | 4.01–4.16 | 39 / 9 / 0 | 33 |
| Klassificeringsmatris och utvärdering (`klassmatris`) | Beräkna utvärderingsmått; Tolka klassificeringsmatrisen | 4.20–4.39 | 59 / 14 / 1 | 13 |
| Linjär regression och gradientnedstigning (`regression`) | Linjär regression; Gradientnedstigning | 4.40–4.55 | 39 / 11 / 0 | 16 |
| kNN och k-means (`knn_kmeans`) | Klassificera med kNN; Klustring med k-means | 4.60–4.75 | 40 / 11 / 0 | 17 |
| Fördjupning: neurala nätverk (`neurala`) | Viktad summa och bias; Aktiveringsfunktioner | 4.80–4.95 | 46 / 6 / 0 | 29 |

Totalt 84 uppgifter och 275 delkort. Ungefär hälften av delkorten är flerval och hälften har numeriska svar
eller namnlistor.

## Innehåll (efter förenklingen samma dag)

- **Klassificeringsmatriser (4.20–4.29):** tio verkliga sammanhang, bland annat spamfilter, cancerscreening,
  bedrägerier, ansiktsupplåsning, fotgängare, pantstation, fuskdetektor, röstassistent och ogräsrobot.
  Uppgifterna frågar efter träffsäkerhet, precision, recall och antal fel av olika slag. I de flesta
  finns också en tolkningsfråga: vilket mått som är viktigast, varför hög träffsäkerhet kan vilseleda,
  vilket fel som är värst och vad precisionen betyder för de utpekade.
- **Tolkning (4.30–4.39):** rutornas namn, en lat modell som alltid säger ”äkta”, val mellan två modeller,
  att bygga en matris ur en text, precision och recall baklänges, en 3 × 3-matris, inställningar av ett spamfilter
  och två system med samma träffsäkerhet. 4.33c (A) visar att lika precision och recall ger FP = FN.
- **Regression:** förutsägelse, modellens fel (verkligt − förutsagt, även negativt), medelkvadratfel med förklaring,
  tolkning av k och m, att en modell bara gäller där den har data, samband och orsak, och valet mellan två linjer.
  Gradientnedstigning: enstaka steg, negativ lutning, minimum, för stort α, lokalt minimum och träningsloopen.
- **kNN och k-means:** avstånd i kvadrat, de tre närmaste, majoritetsröst med k = 1 och k = 3 (som ger olika
  svar i 4.63 och 4.64), Manhattanavstånd, att räkna om egenskaper till samma skala, tilldelning, nya centrum,
  två varv där en punkt byter kluster, vad k betyder och summan av avstånd i kvadrat.
- **Fördjupning: neurala nätverk:** viktad summa, bias, negativa vikter, att hitta bias, stegfunktion och ReLU,
  OCH/ELLER, att välja bias, två neuroner efter varandra och vad som ändras vid träning.

Begreppen interpolation och extrapolation används inte (användarbeslut 2026-10-22). I stället står till exempel
”långt utanför de data modellen tränats på”.

## Papper och Kunskapsgymmet

- Decimalsvar är exakta, med högst tre decimaler. Instruktionen ”(Svara i decimalform.)” finns bara i Kunskapsgymmets delkort.
- Förklaringsfrågor (”Varför …”, ”Vad visar exemplet?”) är öppna på papper och flerval i Kunskapsgymmet, på
  samma sätt som i tillämpningsuppgifterna.
- Figurerna är nya och finns i `tools/ai_ml.py`: punktdiagram med regressionslinjer eller klustercentrum,
  en neuron med vikter, bias och aktiveringsfunktion, och helt kopplade nätverk. Matriserna är tabeller,
  och 3 × 3-matrisen har korta rubriker så att den ryms i mobilbredd.

## Nivåer

Nivån sätts i byggskriptet och följer AI_NIVAINDELNING.md: träningsnivå 1–2 är E, 3 är C och 5 är A.
Nivåskriptet behåller nivån för kapitel 4 och senare (`u['kap'] >= 4`). E-uppgifter är ett steg med en
given formel. C-uppgifter är flerstegsberäkningar, val av mått eller modell utifrån följderna och
förklaringar. A-uppgifter generaliserar.

## Ändrade tester

Testerna motiverar ändringarna i kommentarer.

- `ai-sjalvrattning`: decimalsvar är tillåtna i kapitel 4.
- `ai-nivaer`: α får förekomma i kapitel 4, eftersom det där är inlärningstakten.
- `ai-pafyllnad7`: KAPNAMNAI har fyra kapitel.
- Webbläsartestet i Kunskapsgymmet: antalet områden räknas ur strukturen, och decimalsvar kontrolleras med
  decimalkomma och med fel hundradel.

## Kontroller

- `tools/ai-maskininlarning-2026-11-12.test.js` räknar om alla svar oberoende av byggskriptet. Det gäller
  matriser lästa ur tabellerna, egen kNN-sortering, k-means, gradientnedstigning (även konvergens för α)
  och neuroner. Testet kontrollerar också strukturen, nivåerna och pappersversionen.
- Hela byggkedjan ger samma fil två gånger i rad och samma fil som stegvis körning. Validatorn hittar bara
  de två godkända fynden. Alla 18 AI-tester går igenom.
- Kunskapsgymmet: 1 150 delkort och 3 645 rättningskontroller utan fel, varav 67 decimalsvar.
  Alla 48 figurer och tabeller samt ett urval av kort med ledtråd och facit (4.22d, 4.37a, 4.40c, 4.45a,
  4.51d, 4.60b, 4.70b, 4.80a och 4.87e) har granskats i 390 px. Efter granskningen flyttades viktetiketterna
  i neuronfiguren bort från linjerna, centrumetiketten i 4.70 flyttades och 3 × 3-matrisen fick kortare rubriker.

Efter första versionen hade banken 1 150 delkort (860 E, 221 C och 69 A).

## Förenkling efter användarens synpunkt (2026-11-12, samma dag)

Användaren: ”nu är det mycket begrepp som eleverna inte kan i AI1. T.ex. residual. Gör Neurala nätverk som ett
fördjupningsavsnitt och ha enkla uppgifter om viktad summa, bias och enkla aktiveringsfunktioner (som ger enkla
beräkningar). Håll uppgifterna ganska lätta, tänk på att det är AI1.” Ändringarna gjordes innan något hade pushats,
så ID:n och innehåll kunde ändras utan att elevresultat påverkas.

- **Begrepp som tagits bort eller förklaras i vardagliga ord:**
  - ”Residual” heter nu ”modellens fel (verkligt − förutsagt)”.
  - ”MSE” heter ”medelkvadratfel, alltså medelvärdet av felen i kvadrat”.
  - F1-värdet är borta. 4.22d och 4.26a frågar i stället hur många fall modellen missade.
  - Valideringsdata är borta. 4.12 frågar i stället varför man lottar vilka exempel som blir testdata.
  - ”Särdrag” är bortbytt. 4.02c handlar nu om vad träningsdata är, och i 4.04c och 4.67 står ”egenskaper”.
  - ”Derivata” är borta. Lutningen förklaras med hur felet ändras.
- **Svåra A-delar borttagna:** 4.51d (0 < α < 1, och 4.51 har nu bara ett steg), 4.73c (summan kan aldrig öka;
  4.73 frågar nu vad k betyder) och XOR-nätverket. Kvar på A-nivå är bara 4.33c.
- **Neurala nätverk** är nu kortet ”Fördjupning: neurala nätverk” med delmomenten ”Viktad summa och bias” och
  ”Aktiveringsfunktioner” (stegfunktion och ReLU). Alla 16 uppgifter är nya och nästan alla räknar med heltal.
  Sammanhangen är cykelväder, spamfilter, filmförslag, robotdammsugare, bokinköp, kattigenkänning, passerdörr och
  paraplyapp. Epoker, dolda lager, bakåtpropagering och djupinlärning ingår inte längre. Neuronfigurerna utan
  aktiveringsfunktion slutar i z.
- **Kontroller:**
  - Testet har ett nytt deltest som förbjuder de borttagna begreppen i kapitel 4.
  - Neuronuppgifterna räknas om oberoende, och en kontroll säger att neurala nätverk saknar A-nivå.
  - Kedjan är stabil.
  - Kunskapsgymmet: 1 143 delkort och 3 589 kontroller utan fel.
  - Alla figurer och neuronuppgifternas facit har lästs igenom.

Efter förenklingen har banken 394 uppgifter och 1 143 delkort, varav 861 E, 216 C och 66 A.
