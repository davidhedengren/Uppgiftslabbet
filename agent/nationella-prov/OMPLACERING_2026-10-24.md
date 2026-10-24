# Omplacering av 80 uppgifter – 2026-10-24

Användaren ersätter gårdagens beslut: repetitionsområdet är för litet och ska
bort. Samtliga 80 uppgifter placeras i befintliga ämnesområden och delmoment.
Detta är en omplacering, inte en ny uppgiftsomgång eller en innehållsrättning.

## Ändrat

- `kap`, `omr` och `familj` på de 80 ID:na i tabellen nedan.
- `omrTidigare` och `familjTidigare` används av Kunskapsgymmets befintliga
  migrering. Historikposternas ID, tidpunkt och rätt/fel-resultat bevaras;
  områdes- och familjenamn följer nuvarande bank. Befintliga högre kunskapsvärden
  skrivs inte ned. En gammal områdespoäng sprids inte automatiskt till varje
  nytt område: den befintliga tröskeln för områdesmigrering gäller fortsatt.
- De fyra extra kapitlen tas bort ur strukturerna i båda apparna. Därmed finns
  varken kapitlet eller knappen ”Repetera inför Nationella provet” kvar.
  Den särskilda informationsraden i respektive index.html tas också bort.
- Författarskript och tester använder placeringskartan, inte det borttagna området.
- Bankversionerna höjs så att apparna hämtar aktuella filer.

## Bevarat

ID:n behålls av hänsyn till elevhistorik, sparade dokument och felrapporter.
ID-prefixet anger därför inte längre aktuellt kapitel för dessa 80 uppgifter;
`kap` och `omr` är den aktuella placeringen. Inga dubletter läggs till.
Frågor, facit, figurer, ledtrådar, rättningsmetadata, nivåer, poäng, spår och
verktyg är identiska med före flytten. Detta skyddas med en SHA-256 per objekt
på alla fält utom de fem uttryckligen ändrade placeringsfälten.

Alla destinationer och familjer fanns redan före ändringen. Ma5 är orört.
Fysikutkastet i `uppgifter.js`, prototyper och lokala cachefiler ingår inte.
Parallell påfyllnad av Ma3 har hämtats och bevarats före redigering.

## Kontroll

- Fem grupper med oberoende matematikkontroller: godkända för alla 80.
- Regressionstester för bankvalidator och parallella Ma3-facit: godkända.
- Uppgiftslabbets nio spår: samtliga uppgifter nås i sina ordinarie områden.
- Kunskapsgymmet: 688 rättningskontroller, 160 kortvisningar (mobil/dator),
  nio spår och historikmigrering för alla 80. Inga fel eller webbläsarundantag.
- Bankvalidator: inga fynd på de 80 omplacerade uppgifterna. Befintlig baslinje
  är oförändrad: 1 483 ERROR, 230 WARNING och 1 445 INFO i hela banken.

Den befintliga matematiska kontrollen för alla 80 uppgifter körs igen.
Placering, befintliga familjer, oförändrat innehåll, unika ID:n och synk mellan
apparna kontrolleras maskinellt. Webbläsartester kontrollerar alla nio spår,
att varje uppgift går att välja inom sitt vanliga område och att inget
repetitionskort visas. Kunskapsgymmets historikmigrering kontrolleras även
vid upprepad körning. Självrättning och visning kontrolleras av det befintliga
80-uppgiftstestet. Inga Supabase-data eller rapportstatusar ändras.

## Rapportutfall och kommentar

Åtgärdat: placeringsönskemålet för samtliga 80 ID:n nedan.
Felrapporter granskade: inga. ”Granskad – inget fel”: inga rapporter i denna omgång.
Kommentarsförslag: ”Uppgifterna finns nu i sina vanliga ämnesområden. Det separata
repetitionsområdet är borttaget. Alla uppgifter och deras ID:n är kvar.”

## Alla granskade och omplacerade uppgifter

| Kurs | ID | Kapitel | Område | Delmoment |
|---|---|---:|---|---|
| ma1 | 8.01 | 3 | Procentuella förändringar och jämförelser | Procentuell ökning och minskning |
| ma1 | 8.02 | 2 | Skrivsättet f(x) och funktionsvärden | Funktionsvärden från formel |
| ma1 | 8.03 | 1 | Skriva och förenkla uttryck | Uttryck med parenteser |
| ma1 | 8.04 | 1 | Problemlösning med ekvationer | Ställa upp och lösa ekvationer |
| ma1 | 8.05 | 2 | Skrivsättet f(x) och funktionsvärden | f(x) i grafer |
| ma1 | 8.06 | 3 | Förändringar i flera steg | Upprepad procentuell förändring |
| ma1 | 8.07 | 3 | Förändringsfaktor | Räkna med förändringsfaktor |
| ma1 | 8.08 | 5 | Komplementhändelser | Sannolikheten för minst en händelse |
| ma1 | 8.09 | 5 | Beroende händelser | Dragning utan återläggning |
| ma1 | 8.10 | 2 | Linjära funktioner | Linjära funktioner i vardagliga sammanhang |
| ma1 | 8.11 | 3 | Index | Procentuell förändring av index |
| ma1 | 8.12 | 4 | Trigonometri i tillämpningar | Sträckor i tillämpningar |
| ma1 | 8.13 | 4 | Vektorers absolutbelopp | Längd i tillämpningar och resonemang |
| ma1 | 8.14 | 1 | Linjära olikheter | Olikheter i vardagsproblem |
| ma1 | 8.15 | 2 | Bestämma en linjär funktion | Linjär funktion från tabell |
| ma1 | 8.16 | 3 | Förändringar i flera steg | Total förändring i flera steg |
| ma1 | 8.17 | 5 | Korrelation och kausalitet | Kausalitet och bakomliggande variabler |
| ma1 | 8.18 | 0 | Proportionalitet | Proportionalitet i problemlösning |
| ma1 | 8.19 | 2 | Matematiska modeller | Jämföra linjär och exponentiell tillväxt |
| ma1 | 8.20 | 1 | Mönster och generella samband | Figurmönster i bilder |
| ma2 | 6.01 | 2 | Enkla andragradsekvationer | Ekvationer av typen x² = a |
| ma2 | 6.02 | 1 | Faktorisering | Faktorisera i flera steg |
| ma2 | 6.03 | 2 | Andragradsfunktionens graf | Avläsa egenskaper ur grafen |
| ma2 | 6.04 | 1 | Tillämpningar och problemlösning med ekvationssystem | Ställa upp ekvationssystem |
| ma2 | 6.05 | 2 | Exponentialekvationer | Tillämpade exponentialekvationer |
| ma2 | 6.06 | 2 | Logaritmlagarna | Förenkla med logaritmlagarna |
| ma2 | 6.07 | 3 | Geometriska begrepp och definitioner | Geometriska grundbegrepp |
| ma2 | 6.08 | 3 | Likformighet | Indirekt mätning |
| ma2 | 6.09 | 4 | Standardavvikelse | Beräkna och tolka standardavvikelse |
| ma2 | 6.10 | 4 | Normalfördelning | Andel i ett intervall |
| ma2 | 6.11 | 4 | Lådagram | Avläsa lådagram |
| ma2 | 6.12 | 2 | Problemlösning med andragradsfunktioner | Optimering |
| ma2 | 6.13 | 2 | Rotekvationer | Falska rötter och kontroll |
| ma2 | 6.14 | 2 | Andragradsekvationer – fördjupning | Parametrar och villkor på rötterna |
| ma2 | 6.15 | 3 | Avståndsformeln och mittpunktsformeln | Mittpunktsformeln |
| ma2 | 6.16 | 2 | Andragradsfunktioner | Bestämma andragradsfunktion från nollställen |
| ma2 | 6.17 | 4 | Linjär regression | Bestämma och använda regressionsmodellen |
| ma2 | 6.18 | 4 | Medelvärde, median och typvärde | Förändring av lägesmått |
| ma2 | 6.19 | 2 | Tillämpningar och problemlösning med andragradsekvationer | Andragradsekvationer i geometri |
| ma2 | 6.20 | 2 | Andragradsekvationer – fördjupning | Antal lösningar och tillämpningar med grafer |
| mato1 | 5.01 | 2 | Deriveringsregler | Derivera polynom |
| mato1 | 5.02 | 3 | Från derivata till funktion | Bestämma primitiva funktioner |
| mato1 | 5.03 | 2 | Ändringskvoter och derivata | Förändring ur grafer, tabeller och sammanhang |
| mato1 | 5.04 | 2 | Begreppet derivata | Derivata som tangentens lutning |
| mato1 | 5.05 | 1 | Förkorta rationella uttryck | Förkorta rationella uttryck |
| mato1 | 5.06 | 3 | Extrempunkter och terrasspunkter | Bestämma extrempunkter |
| mato1 | 5.07 | 3 | Integralberäkning med primitiv funktion | Area med integraler |
| mato1 | 5.08 | 3 | Primitiva funktioner med villkor | Primitiv funktion genom en given punkt |
| mato1 | 5.09 | 2 | Exponentialfunktioner – tillämpningar och problemlösning | Derivata i exponentialmodeller |
| mato1 | 5.10 | 3 | Extremvärdesproblem med modellering | Stängsel och inhägnader |
| mato1 | 5.11 | 3 | Primitiva funktioner med villkor | Återskapa funktion från derivata |
| mato1 | 5.12 | 3 | Integraler – tillämpningar och problemlösning | Ackumulerad mängd från förändringshastighet |
| mato1 | 5.13 | 3 | Integral och area | Integral som area under en graf |
| mato1 | 5.14 | 4 | Cosinussatsen | Använda cosinussatsen |
| mato1 | 5.15 | 4 | När ger sinussatsen två fall? | Antal möjliga trianglar |
| mato1 | 5.16 | 4 | Geometriska summor | Geometriska summor i tillämpningar |
| mato1 | 5.17 | 4 | Linjär optimering | Grafisk optimering |
| mato1 | 5.18 | 2 | Mer om derivatan av polynomfunktioner | Parameterproblem med derivata |
| mato1 | 5.19 | 2 | Tangenter och derivata | Fördjupade tangentproblem |
| mato1 | 5.20 | 3 | Extrempunkter och terrasspunkter | Extrempunkter med parameter |
| mato2 | 6.01 | 2 | Derivatan av sammansatta funktioner | Kedjeregeln för trigonometriska och exponentiella funktioner |
| mato2 | 6.02 | 2 | Trigonometriska kurvor i radianer | Amplitud, period och medellinje för trigonometriska funktioner |
| mato2 | 6.03 | 5 | Konjugat, absolutbelopp och de fyra räknesätten | Konjugat och absolutbelopp av komplexa tal |
| mato2 | 6.04 | 3 | Derivatan av en produkt | Derivering med produktregeln |
| mato2 | 6.05 | 3 | Derivatan av en kvot | Derivering med kvotregeln |
| mato2 | 6.06 | 3 | Exponential- och logaritmfunktioner | Kedjeregeln med logaritmfunktioner |
| mato2 | 6.07 | 2 | Trigonometriska kurvor i radianer | Trigonometriska ekvationer i radianer |
| mato2 | 6.08 | 4 | Integraler och primitiva funktioner | Bestämda integraler med trigonometriska funktioner |
| mato2 | 6.09 | 4 | Skivmetoden | Rotationsvolymer |
| mato2 | 6.10 | 4 | Sannolikhetsfördelning | Normalisera täthetsfunktion och bestäm parameter |
| mato2 | 6.11 | 5 | Konjugat, absolutbelopp och de fyra räknesätten | Division av komplexa tal |
| mato2 | 6.12 | 5 | Faktorsatsen | Faktorsatsen och faktorisering |
| mato2 | 6.13 | 3 | Kurvor och asymptoter | Asymptoter för rationella funktioner |
| mato2 | 6.14 | 2 | Tillämpningar och problemlösning – trigonometri och grafer | Tolka och bestämma trigonometriska modeller |
| mato2 | 6.15 | 3 | Grafer och derivator | Extrempunkter, terrasspunkter och inflexion |
| mato2 | 6.16 | 2 | Derivatan av sammansatta funktioner | Derivering med kedjeregeln |
| mato2 | 6.17 | 5 | Andragradsekvationer | Andragradsekvationer med komplexa lösningar |
| mato2 | 6.18 | 4 | Integraler och areor | Parameterproblem med area och integral |
| mato2 | 6.19 | 4 | Integraler och primitiva funktioner | Bestämda integraler med trigonometriska funktioner |
| mato2 | 6.20 | 2 | Kurvan y = a sin x + b cos x | Skriva om kombinationer av sinus och cosinus |
