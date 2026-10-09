# Följdgranskning av Ma2, 2026-10-09

## Omfattning

26 uppgifter är granskade: **1.26, 1.27, 1.30, 1.59, 1.92, 1.206, 1.224,
1.228, 1.231, 1.296, 1.297, 1.298, 1.300, 1.301, 1.302, 1.305, 2.11,
2.248, 2.361, 2.363, 2.365, 3.523, 3.524, 3.525, 3.526 och 3.528**.

22 uppgifter har förbättrats. Fyra är **Granskad – inget fel**: 1.305, 3.524,
3.525 och 3.528. Inga slutsvar ändras matematiskt; ändringarna gäller begriplighet,
svarsformat, självständiga delkort, facit, ledtrådar och nivåer.

Granskningen gäller dessa uppgifter, inte hela Ma2-banken. Alla rapportstatusar
och kommentarer i detta dokument är förslag; inga rapporter har avslutats i databasen.

## Minst fem jämförelser för varje ursprungsfel

| Ursprung i loggen 20:49 | Sökt feltyp | Jämförelseuppgifter |
|---|---|---|
| 1.29 | Oklart hur ett systems lösning ska matas in | 1.26, 1.27, 1.59, 1.92, 1.206 (5) |
| 1.299 | Otydliga namn/ordning i svarsfält och för låg nivå för modellering | 1.296, 1.297, 1.298, 1.300, 1.301, 1.302 (6) |
| 1.303 | Grafisk lösning: variation, avläsning och rättningsformat | 1.206, 1.224, 1.228, 1.231, 1.305 (5) |
| 2.12 b | Förändringsfaktor/startvärde: tydlig fråga, svarstyp och självständiga kort | 2.11, 2.248, 2.361, 2.363, 2.365 (5) |
| 3.529 a | Bisektrissatsen: nivå, kombination av samband och facit | 3.523, 3.524, 3.525, 3.526, 3.528 (5) |

1.206 hör till två relevanta jämförelsegrupper. 1.30 togs dessutom med efter
att en sökning i ekvationssystemens lösningar visade ett felaktigt variabelnamn.

Nya feltyper följdes upp i samma manuella kontroll:

- **Facit hoppar över själva lösningen:** jämfördes i samtliga sex textuppgifter
  1.296–1.298 och 1.300–1.302. Alla sex saknade beräkningen mellan system och svar.
- **Delkort saknar egen förklaring eller kräver ett tidigare resultat:** alla fem
  exponentialuppgifter i tabellen kontrollerades. 2.361, 2.363 och 2.365 återanvände
  hela facit på delkorten. 2.11 b krävde att eleven räknade fram faktorn igen.
  2.248 hade egna facit, men de var enbart korta svar utan förklaring.
- **Felaktig variabel i lösningsförklaring (1.30):** substitutions-/eliminationsleden
  jämfördes med 1.26, 1.27, 1.59, 1.92 och 1.296. Inget ytterligare sådant variabelfel
  hittades; däremot behövde 1.26 och 1.296 tydligare mellanled.
- **Generisk GeoGebra-instruktion passar inte den givna figuren:** alla fem
  grafuppgifter kontrollerades. 1.206, 1.224 och 1.231 bad eleven mata in ekvationer
  som inte var givna. 1.228 bad eleven zooma fram en skärningspunkt trots att
  linjerna var parallella. 1.305 hade redan en relevant förklaring.

Likhet med ett fel användes alltså som sökväg, inte som bevis för att en uppgift
måste ändras. Instruktionen om minst fem jämförelser är nu sparad i
`agent/PEDAGOGISKA_REGLER.md`.

## Alla åtgärdade uppgifter och förslag på kommentar

Alla ID:n nedan tillhör **ma2**. Träningsnivå och E/C/A har bedömts separat.

| Uppgift/del | Bekräftat problem och ändring | Föreslagen kommentar |
|---|---|---|
| 1.26 | Punktsträng ersätts med x/y-fält. Facit visar substitution och insättning. Nivå 2 behålls. | Nu finns separata fält för x och y. Lösningen visar hur substitutionen ger y=3 och sedan x=3. |
| 1.27 | x/y-fält, uppdelad uträkning och ledtråd som passar direkt addition. Nivå 2 behålls. | Addera ekvationerna så försvinner y-termerna: x=2 och y=−1. Svaren har nu tydliga fält. |
| 1.30 | Facit skrev x-koefficienter när 2a=6 faktiskt jämför y-koefficienter. Numeriskt a-svar och relevant ledtråd. Nivå 3 behålls. | Förklaringen är rättad: det är y-koefficienterna som jämförs. Svaret a=3 var redan korrekt. |
| 1.59 | Separata x/y-fält. Nivå 2 behålls. | Skriv x=4 och y=2 i varsitt fält. Vanliga tal räcker. |
| 1.92 | Separata x/y-fält. Nivå 2 behålls. | Skriv x=4 och y=3 i varsitt fält. Vanliga tal räcker. |
| 1.206 | x/y-fält och uppgiftsspecifikt facit. Tar bort olämplig GeoGebra-instruktion. Nivå 1 behålls. | Läs av skärningspunkten: x=1, y=2. Facit utgår nu från den visade grafen. |
| 1.224 | Samma rättning som 1.206. Nivå 1 behålls. | Grafens lösning är x=2, y=3. Nu finns tydliga svarsfält och en direkt förklaring. |
| 1.228 | Tar bort motsägande instruktion om att zooma fram en skärning. Ledtråden ger inte längre hela svaret. Nivå 2 och manuell bedömning behålls. | Linjerna har samma lutning och olika skärningar med y-axeln. Systemet saknar därför lösning. |
| 1.231 | x/y-fält och relevant grafavläsning i facit. Nivå 1 behålls. | Grafens lösning är x=4, y=3. GeoGebra-instruktionen är ersatt med en förklaring som passar figuren. |
| 1.296 | Språkfel, anonyma svarsfält och saknad uträkning rättas. Nivå 1→2. | Fälten anger vuxenbiljetter respektive barnbiljetter. Facit visar hur man får 5 och 13. |
| 1.297 | Samma feltyp; tydlig formulering om köp av pennor. Nivå 1→2. | Texten och svarsfälten är förtydligade. Beräkningen ger 12 svarta och 12 blå pennor. |
| 1.298 | Samma feltyp; naturlig text om en fruktkorg. Nivå 1→2. | Texten och lösningen är förtydligade. Det är 15 äpplen och 15 päron. |
| 1.300 | ”25 museum” ersätts med 25 biljetter. Namngivna svar och visad elimination. Nivå 1→2. | Det är biljetter som säljs. Nu framgår både frågan och beräkningen: 15 vuxenbiljetter och 10 ungdomsbiljetter. |
| 1.301 | ”20 café” och böjningsfel ersätts med konkret försäljning. Nivå 1→2. | Uppgiften handlar nu tydligt om 12 smörgåsar och 8 glas juice, med rätt märkta svarsfält och visad beräkning. |
| 1.302 | Namngivna fält för fordon, relevant ledtråd och fullständig uträkning. Nivå 1→2. | Svarsfälten skiljer på bilar och motorcyklar. Facit visar varför det är 15 bilar och 7 motorcyklar. |
| 2.11 b | Fristående b-kort får den redan beräknade faktorn 1,2 och egen ledtråd. Numeriska format för a/b. | Du behöver inte lösa en tidigare del först. B-kortet anger faktorn 1,2, så nästa värde är 288·1,2=345,6. |
| 2.248 a–c | Samma tydliga faktorfråga i huvudtext och c-kort. Alla tre delfacit får korta förklaringar. | Frågan anger vilken faktor som efterfrågas. Facit förklarar nu svaren 1, 8 och 2. |
| 2.361 a–b | Egna lösningar och ledtrådar för respektive del; hela facit visas inte längre. | Varje kort visar nu bara sin egen lösning. Startvärdet är 2 och den växande grafen har förändringsfaktor större än 1. |
| 2.363 a–c | Formeln följer med varje delkort; egna lösningar/ledtrådar. Huvudfacit svarar 0,5 på faktorfrågan. | Funktionen finns nu på varje kort. Facit skiljer tydligt på startvärdet 3, faktorn 0,5 och att funktionen är avtagande. |
| 2.365 a–b | Huvudfrågan preciseras till y-koordinat. Egna facit. B-kortet får a=2 i funktionen och blir E/nivå 2; a-kortet ligger kvar på C/nivå 3. Poängfördelningen anpassas. | B-kortet kan lösas självständigt och frågar tydligt efter y-koordinaten 6. A-kortets facit avslöjar inte längre b-svaret. |
| 3.523 | C/nivå 3→E/nivå 2: direkt användning av förhållandet 2:1 och totalsidan 15. | Nivån är sänkt till 2. Bisektrissatsen ger tre lika delar, så BD=2·5=10 cm. |
| 3.526 | Överlång lösningsrad ersätts med förklarad uppställning och korta mellanled. Nivå 3 behålls. | Facit visar nu hur ekvationen ger DC=3 cm, BD=5 cm och hela BC=8 cm. |

## Granskad – inget fel

| Uppgift | Kontroll och bedömning | Föreslagen kommentar |
|---|---|---|
| 1.305 | SVG-linjerna möts vid (2,2). x/y-fält, facit och nivå 1 stämmer. Svaret bidrar redan till variationen. | Granskad – inget fel: båda koordinaterna är 2 och svarsfälten fungerar. |
| 3.524 | Pythagoras ger BC=50. Bisektrissatsen ger BD=(3/7)·50=150/7≈21,4 m. 21,4 m godkänns. Kombinationen motiverar nivå 3. | Granskad – inget fel: 21,4 m är rätt och godkänns med en decimal. |
| 3.525 | DC=10−6=4, så BD/DC=6/4=9/6=AB/AC. Svaret är ja. Faktisk svarsknapp kontrollerad: ett ja kräver därefter egen bedömning av motiveringen, inte omedelbart färdigt försök. Nivå 3 behålls. | Granskad – inget fel: förhållandena är lika, så AD är bisektris. Ja-svaret kontrolleras och motiveringen jämförs sedan med facit. |
| 3.528 | BC=12 och AB+AC=24. Förhållandet AB:AC=5:7 ger 10 m respektive 14 m. Ordningen i svarsfälten och nivå 4 är rimliga. | Granskad – inget fel: AB=10 m och AC=14 m. Både omkretsen 36 m och förhållandet 5:7 stämmer. |

## Verifiering och avgränsning

- `tools/foljdgranskning-ma2-2026-10-09.browser.py` i Kunskapsgymmet:
  41 försök via den riktiga svarsknappen; korrekta, omkastade och felaktiga tal.
  29 ytterligare rättningskontroller med decimaler, bråk och enheter.
- Fem oberoende geometrikontroller av grafiska system, inklusive parallella
  linjer utan lösning. De gamla SVG-figurerna har inte ändrats.
- 132 kortvisningar (33 kort × två skärmbredder × två teman): inga KaTeX-fel,
  för breda facitformler eller sidöverbredd. Figurer och utvalda lösningar har
  även granskats visuellt, särskilt på mobil.
- Efter sista metadataändringen för 2.365 körs de 41+29 rättningskontrollerna
  igen och de berörda korten 2.365 samt manuella motiveringen i 3.525 visas på
  nytt i båda teman och skärmbredder (12 visningar).
- 29 befintliga delkortstester passerar.
- Validator för ma2: 4 ERROR, 166 WARNING, 95 INFO (före: 4/173/95).
  De fyra kända kontraktsfelen gäller andra uppgifter. Ingen fullständig
  felfrihetsförklaring för banken görs.
- Strukturerad diff: 22 ändrade objekt, oförändrade 2121 uppgifts-ID:n och
  samma antal uppgifter. Bankkopiorna jämförs före och efter synkronisering.
- Ändrade filer: `uppgifterma2.js` i båda repona, denna logg och
  `agent/PEDAGOGISKA_REGLER.md` i master, samt bankversionen i `index.html`
  och webbläsarkontrollen i Kunskapsgymmet. Övriga banker är oförändrade.

Svarsformat-/etikettändringar gäller 1.26, 1.27, 1.30, 1.59, 1.92, 1.206,
1.224, 1.231, 1.296–1.298, 1.300–1.302, 2.11 och 2.248. Delkortsändringar
är avgränsade till 2.11, 2.248, 2.361, 2.363 och 2.365. Nivåändringarna
redovisas individuellt i tabellen; övriga nivåer behålls.
