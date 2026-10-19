# Mato2: extremvärden och skärningar, 2026-10-19

Sex uppgifter granskade: **2.265, 2.266, 2.268, 2.571, 2.582, 2.487**.
Fem åtgärdade; en granskad utan fel. Tidigare FP64/65 följs, och varje ny
ändring har före/efter i motsvarande JSON. Inga ID:n ändras.

## Åtgärder och kommentarsförslag

| ID | Kommentar |
|---|---|
| 2.265 | Åtgärdad: lösningen förklarar asymptoten, varför derivatans tecken ger ett minimum och hur skärningarna hittas. c frågar uttryckligen efter x-koordinater, som får anges i valfri ordning. Fullprecisionsfacit ersätter avrundade lagrade värden. |
| 2.266 | Åtgärdad: minimipunkten besvaras i två tydligt märkta fält, x och y. Exakta värden och tre decimaler godtas. Lösningen förklarar minimum och båda skärningarna. |
| 2.268 | Åtgärdad: lösningen motiverar minimum och visar hur ekvationen faktoriseras till tre lösningar. Rötterna kan anges i valfri ordning. Fullprecisionsvärden används vid rättningen. |
| 2.571 | Åtgärdad: miniräknare tillåts eftersom decimalsvar uttryckligen erbjuds. Tre decimaler rättas mot fullprecisionsfacit med halv tusendels tolerans. Uppgiften bedöms som C/nivå 3. |
| 2.582 | Åtgärdad: miniräknare tillåts för decimalsvaret. Exakta svar fungerar fortsatt. Precisionen följer frågan. Uppgiften bedöms som C/nivå 3. |

## Granskad – inget fel

**2.487:** Granskad – inget fel: e^(−x²)≤1 för alla reella x, med likhet
bara vid x=0. Både facit och teckenresonemanget är korrekta. x=0 godtas och
x=1 underkänns. Nivå 2 och verktygsval utan räknare/GeoGebra bevaras: ingen
krävande numerisk beräkning behövs.

## Matematisk och pedagogisk kontroll

- 2.265: f′(x)=(x−3)/(x−1)². På x>1 avtar funktionen till x=3 och växer
  sedan. Minsta värdet är 1+ln2. Ekvationen f(x)=2 har rötterna 2 och
  cirka 5,922, numeriskt lösta med bisektion och kontrollerade i originalet.
- 2.266: f′(x)=−e^(−x)+0,5 byter från minus till plus vid ln2.
  Minimipunkten är (ln2,(1+ln2)/2). f(x)=1 har rötterna 0 och cirka
  1,594. b behåller E/nivå 2 för digital ekvationslösning; a är C/nivå 3
  för derivata, exponentialekvation och funktionsvärde. Huvudnivå C/3,
  poäng 1/2/0. Det ordnade koordinatparet får aldrig rättas som en mängd.
- 2.268: f′(x)=3−4/(x−1)³. På högra grenen ligger minimum vid
  x=1+∛(4/3), med värdet 5+(9/2)∛(4/3). f(x)=10 ger
  (x−2)(3x²−8x+3)=0, alltså x=2 och (4±√7)/3. Alla rötter kontrollerade
  i originalfunktionen; x=1 är inte en lösning. C/nivå 3 bevaras med
  GeoGebra som möjlig metod.
- 2.571: f′(x)=ln x+1, teckenbyte vid 1/e, minsta värde −1/e.
- 2.582: f′(x)=e^x(x−1)/x², teckenbyte vid 1, minsta värde e.
  Dessa två är vanliga sammansatta extremvärdesproblem, inte A-problem.
  C/nivå 3 och 0/2/0 är rimligare. GeoGebra är fortsatt avstängt eftersom
  algebraisk analys prövas; räknare är tillåten för numeriska värden.

2.265/266/268 behåller GeoGebra och räknare, inklusive delkorten: digital
skärningsanalys är en avsedda metoderna. Generiska avrundningsmallar och
ledtrådar om orelaterad polynomdivision tas bort. Delarna får egna ledtrådar.
Inga tidigare delresultat behövs för att förstå ett separat kort.

Tre nya SVG-grafer ligger i lösningarna till skärningsdelarna, så att de
förklarar utan att ge bort andra delars svar i uppgiftstexten. Graferna är
ritade från originalfunktionerna och visar rätt vågräta linjer. 2.571/582
behåller sina algebraiska lösningar utan figur; graf i frågan skulle ge
extrempunktens läge som prövas.

## Verifiering

- 64 faktiska svarskontroller och 38 elev-/lärarvyer vid 390/1280 px passerar.
  Exakta uttryck, decimaler, felaktiga närliggande avrundningar, omvänd
  rotordning och felaktigt omkastade koordinater ingår.
- Inga JavaScriptfel, KaTeXfel eller klippta formler.
- Alla tre grafer granskade visuellt; SVG-analys av båda kopiorna ger inga
  fynd. Y-axeln i 2.268 glesades ut efter att etikettkollision upptäckts.
- Nytt regressionstest kontrollerar originalekvationernas residualer och
  derivatans tecken. Fem relevanta tidigare testfiler passerar också.
- Bankvalidator: 72 befintliga fynd före/efter, inga nya.

Inga produktionsrapporter avslutade och inga kommentarer skickade till elever.
