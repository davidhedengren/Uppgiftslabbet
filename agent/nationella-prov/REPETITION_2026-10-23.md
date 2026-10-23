# Repetitionsområde – första omgången 2026-10-23

## Leverans och granskningens omfattning

80 självständiga uppgifter: 20 i vardera ma1, ma2, mato1 och mato2.
Området ”Repetera inför Nationella provet” ligger sist i båda apparna.
Ma5/matf1 är pausad enligt användarens svar. Inga gamla bankuppgifter ändras.

Detta är inte en komplett genomgång av alla frisläppta prov. VT22 har lästs
för uppgiftstyper och innehåll; nya frågor täcker ett urval och kompletterande
ämnesplansinnehåll. Ingen ett-till-ett-mappning till originalfrågor påstås.
Se [källor och kvarvarande arbete](README.md).

## Innehåll och nivå

| Bank | Nivå 1 | Nivå 2 | Nivå 3 | Nivå 4 | Nivå 5 | Antal per spår |
|---|---:|---:|---:|---:|---:|---|
| ma1 | 4 | 11 | 4 | 1 | 0 | 1a: 18, 1b: 18, 1c: 19 |
| ma2 | 6 | 8 | 4 | 1 | 1 | 2a: 14, 2b: 19, 2c: 20 |
| mato1 | 4 | 8 | 5 | 2 | 1 | 1b: 18, 1c: 18 |
| mato2 | 4 | 9 | 5 | 1 | 1 | 2c: 20 |

Nivåerna anger bankens träningssvårighet, inte originalprovens poäng eller
betygsgränser. Nivå 1 är direkt avläsning eller en grundläggande metod.
Nivå 2 har ett kort, välbekant beräkningsförlopp. Nivå 3 kombinerar samband.
Nivå 4–5 kräver eget modellbygge, falluppdelning eller flera algebraiska samband.

- Ma1: procent åt båda håll, förändringsfaktor, sannolikhet, modellval,
  kostnadssamband, index, geometri och ett symboliskt kantmönster.
- Ma2: ekvationer, andragradsmodeller, logaritmform, likformighet,
  statistik, normalfördelning, regression, felaktiga rötter och tangentvillkor.
- Mato1: derivata, primitiv funktion, tabell/diagram, extrema, areor,
  nettoförändring, optimering samt spårspecifik trigonometri och ekonomiska summor.
- Mato2: kedje-, produkt- och kvotregel, trigonometri, komplexa tal,
  integraler, täthetsfunktion, rotationsvolym och amplitudresonemang.

## Gy25-beslut

Skolverkets ämnesplaner, version 1 från 2025-07-01, finns i
`amnesplaner-gy25.json`. Metadata per ID finns i gransknings-JSON-filen.

- Ma1 #8.11 index ligger i 1b. #8.12 ramptrigonometri ligger i 1c och
  yrkesanknuten geometri 1a. #8.13 vektorer ligger i 1c.
- Ma2 #6.06 logaritmlag, #6.07–08 klassisk geometri, #6.15 mittpunkt
  och #6.17 regression ligger i 2b/c. #6.13 rotekvation ligger i 2c.
  #6.05 exponentialekvation är digital i alla tre spår; 2a behöver inte logaritmlagen.
- Mato1 #5.14–15 sinus-/cosinussats ligger i 1c. #5.16 geometrisk summa
  och #5.17 linjär optimering ligger i 1b.
- Mato2:s täthetsfunktion och rotationsvolym finns uttryckligen bland
  integralernas tillämpningar i aktuell ämnesplan.
- Inga originalfrågor utanför dagens innehåll har importerats. Detta är en
  granskning av de 80 egna frågorna, inte ett godkännande av hela VT22 eller arkivet.

## Verktyg och pedagogik

Miniräknare är tillåten när den inte ersätter den metod som prövas. Digitala
verktyg och miniräknare är båda tillåtna i ma2 #6.05, #6.09, #6.17 samt
mato1 #5.17. Standardavvikelsen beräknas som Sx med nämnaren n−1.

Symboliska derivator, faktoriseringar och primitiva funktioner prövar metoden;
CAS skulle ta bort den. De är därför inte digitala lösningsuppgifter. Räknare
är tillåten i flera tillämpningar även om en handlösning också är enkel.

Alla kort är självständiga, utan beroenden till tidigare delkort. Flera svar
har antingen namngivna ordnade fält eller mängdstruktur där ordningen saknar
betydelse. Formkrav, exempelvis en enda logaritm eller faktoriserad form,
är uttryckliga och testas. Vanliga avrundningar accepteras när inget exakt
svar efterfrågas. Slutsvar har enhet där den behövs.

25 egna SVG-figurer och ytterligare tabeller ingår. Ren algebra har inte fått
innehållslösa dekorationsbilder. Vid tvetydiga trianglar skulle en färdig figur
kunna avslöja det antal fall eleven ska hitta, så där används text.

## Rättat under förhandsgranskningen

Detta gäller nya, ännu inte publicerade uppgifter; inga gamla felrapporter avslutas.

- Ma2 #6.01 och #6.20, mato2 #6.07 och #6.17: rätt mängdmetadata för svar
  i valfri ordning. Även de ordnade ma2 #6.04/#6.15 testas med omkastade svar.
- Ma2 #6.09: kortare beräkningsrader i facit så Sx-uttrycket ryms på mobil.
- Ma2 #6.10: full numerisk referens till normalfördelningsandelen; både 68 %
  och 68,3 % accepteras utan att 65 % blir rätt.
- Ma1 #8.12: vinkeletiketten flyttad från triangelns sida in i vinkelområdet.
- Ma2 #6.15: vita bakgrunder bakom punktnamn hindrar rutnätet från att gå
  genom texten. Samma läsbarhet används i övriga punktdiagram.
- Ma2 #6.19: högra måttetiketten flyttad bort från rektangelkanten.
- Mato2 #6.02/#6.07: svarsenheten rad angiven i metadata för svarsrutorna.
  #6.02/#6.07 har numeriska referenser så avrundade radianvärden godtas när
  frågan inte kräver exakt svar; π och π rad ska också fortsatt godtas.

## Granskad – inget fel

Ingen befintlig felrapporterad uppgift bedöms i denna omgång. Det finns därför
ingen ny lista med avslutade rapporter av typen ”Granskad – inget fel”. Alla
nya ID:n nedan har granskats och behåller sina verifierade matematiska svar.

Kommentarsförslag för önskemålet:
”Ett nytt repetitionsområde finns sist i Ma1–Ma4, med egna varierade frågor,
figurer, lösningar och självrättning. Innehållet filtreras efter aktuellt spår.
Detta är första omgången; Ma5 väntar.”

## Kontroller

- Oberoende SymPy-beräkningar och bankkontrakt: fem testgrupper, alla 80 ID:n.
- Verklig självrättning i Kunskapsgymmet: 668 godkända kontroller, korrekta och felaktiga svar,
  alternativkombinationer, enheter, avrundning, symboliska uttryck och svarsfält.
- Alla 80 kort på 390 och 1280 px: KaTeX, sidbredd och matematikrader.
- Båda apparnas faktiska kurs-/spårurval: nio spår, rätt innehåll och sista område.
  Uppgiftslabbet visar även alternativ i uppgiftstexten inför utskrift.
- Alla 25 figurer visuellt granskade. Geometrigranskarens DOM-del och analys
  körda genom Playwright eftersom Chromium-kommandots dump-dom gav timeout.
  Slutresultat: 0 ERROR, 0 WARNING och 28 INFO.
  Bakgrundsrektanglarnas kontakt med viewBox-kanten är avsiktlig.
  Tre vinkelbågar har manuellt kontrollerats mot figurernas koordinater.
- Full bankvalidator: inga fynd på de nya ID:na. Befintlig baslinje är oförändrad:
  1 483 ERROR, 230 WARNING och 1 445 INFO. Hela banken är alltså inte felfri.
- Ursprungliga bankobjekt oförändrade av denna omgång. De fyra bankfilerna
  är byteidentiska mellan apparna och de nya kapitlens struktur är densamma.
  Kunskapsgymmets befintliga GRUPPMATO1-överskrivning är avsiktligt bevarad.
- Parallella ändringar integrerade före push: Uppgiftslabbet b52eed1,
  5a0a8b9, 33fc582 och Kunskapsgymmet f5d30f7, 3837df1, eaf38a3.
  De ändrar gamla Ma3-facit. Samtliga deras bankobjekt är bevarade oförändrade;
  nya uppgifter ligger efter dem. Enda manuella mergekonflikten var bankens
  cacheversion i Kunskapsgymmet, som fick en gemensam ny versionssträng.
  Spår-/visningskontroller kördes igen efter integrationen.

Tester:
`tools/np-repetition-2026-10-23.test.py` (SymPy),
`tools/np-repetition-2026-10-23.browser.cjs` i respektive repo (Playwright).
Webbläsartesterna använder lokala servrar och blockerar Supabase; inga elevdata
eller rapportstatusar skrivs. Författarskriptet ska inte köras ovanpå befintliga
ID:n. Framtida ändringar ska göras både där och i bankerna och verifieras igen.

## Alla granskade och tillagda ID:n

Tabellen är den fullständiga listan. Verktygsbeslut, svar och kommentarsförslag
per ID finns i [JSON-loggen](REPETITION_2026-10-23.json).

| Bank | ID | Nivå | Spår | Innehåll | Verktyg | Figur |
|---|---|---:|---|---|---|---|
| ma1 | 8.01 | 1 | 1a, 1b, 1c | Procent och modeller | Miniräknare | ingen |
| ma1 | 8.02 | 1 | 1a, 1b, 1c | Funktioner och grafer | Miniräknare | SVG |
| ma1 | 8.03 | 2 | 1a, 1b, 1c | Algebra och ekvationer | Utan verktyg | ingen |
| ma1 | 8.04 | 2 | 1a, 1b, 1c | Algebra och ekvationer | Miniräknare | ingen |
| ma1 | 8.05 | 1 | 1a, 1b, 1c | Funktioner och grafer | Miniräknare | SVG |
| ma1 | 8.06 | 2 | 1a, 1b, 1c | Procent och modeller | Miniräknare | ingen |
| ma1 | 8.07 | 2 | 1a, 1b, 1c | Procent och modeller | Miniräknare | ingen |
| ma1 | 8.08 | 3 | 1a, 1b, 1c | Sannolikhet och granskning | Miniräknare | ingen |
| ma1 | 8.09 | 2 | 1a, 1b, 1c | Sannolikhet och granskning | Miniräknare | SVG |
| ma1 | 8.10 | 1 | 1a, 1b, 1c | Funktioner och grafer | Miniräknare | ingen |
| ma1 | 8.11 | 2 | 1b | Begreppet index | Miniräknare | tabell |
| ma1 | 8.12 | 2 | 1a, 1c | Trigonometri i rätvinkliga trianglar; yrkesrelevant geometri för 1a | Miniräknare | SVG |
| ma1 | 8.13 | 2 | 1c | Addition och absolutbelopp av vektorer | Miniräknare | SVG |
| ma1 | 8.14 | 2 | 1a, 1b, 1c | Algebra och ekvationer | Miniräknare | ingen |
| ma1 | 8.15 | 3 | 1a, 1b, 1c | Funktioner och grafer | Miniräknare | tabell |
| ma1 | 8.16 | 2 | 1a, 1b, 1c | Procent och modeller | Miniräknare | ingen |
| ma1 | 8.17 | 2 | 1a, 1b, 1c | Sannolikhet och granskning | Miniräknare | ingen |
| ma1 | 8.18 | 3 | 1a, 1b, 1c | Algebra och ekvationer | Miniräknare | ingen |
| ma1 | 8.19 | 3 | 1a, 1b, 1c | Funktioner och grafer | Miniräknare | tabell |
| ma1 | 8.20 | 4 | 1a, 1b, 1c | Algebra och ekvationer | Utan verktyg | SVG |
| ma2 | 6.01 | 1 | 2a, 2b, 2c | Algebra och ekvationer | Utan verktyg | ingen |
| ma2 | 6.02 | 1 | 2a, 2b, 2c | Algebra och ekvationer | Utan verktyg | ingen |
| ma2 | 6.03 | 1 | 2a, 2b, 2c | Funktioner och modeller | Miniräknare | SVG |
| ma2 | 6.04 | 2 | 2a, 2b, 2c | Algebra och ekvationer | Miniräknare | ingen |
| ma2 | 6.05 | 2 | 2a, 2b, 2c | Digital lösning av exponentialekvation; 2b/c även logaritmer | GeoGebra + miniräknare | ingen |
| ma2 | 6.06 | 2 | 2b, 2c | Logaritmlagar | Utan verktyg | ingen |
| ma2 | 6.07 | 1 | 2b, 2c | Vinklar i likbent triangel | Miniräknare | SVG |
| ma2 | 6.08 | 2 | 2b, 2c | Likformighet | Miniräknare | SVG |
| ma2 | 6.09 | 2 | 2a, 2b, 2c | Digital beräkning av standardavvikelse Sx | GeoGebra + miniräknare | tabell |
| ma2 | 6.10 | 1 | 2a, 2b, 2c | Normalfördelning med given standardavvikelse | Miniräknare | SVG |
| ma2 | 6.11 | 1 | 2a, 2b, 2c | Kvartiler och spridningsmått | Miniräknare | SVG |
| ma2 | 6.12 | 3 | 2a, 2b, 2c | Funktioner och modeller | Miniräknare | SVG |
| ma2 | 6.13 | 3 | 2c | Rotekvationer och extralösningar | Utan verktyg | ingen |
| ma2 | 6.14 | 3 | 2a, 2b, 2c | Algebra och ekvationer | Utan verktyg | ingen |
| ma2 | 6.15 | 2 | 2b, 2c | Koordinatgeometri och mittpunkt | Miniräknare | SVG |
| ma2 | 6.16 | 3 | 2a, 2b, 2c | Funktioner och modeller | Miniräknare | ingen |
| ma2 | 6.17 | 2 | 2b, 2c | Digital linjär regression | GeoGebra + miniräknare | tabell |
| ma2 | 6.18 | 2 | 2a, 2b, 2c | Medelvärde och median | Miniräknare | tabell |
| ma2 | 6.19 | 4 | 2a, 2b, 2c | Geometri och samband | Miniräknare | SVG |
| ma2 | 6.20 | 5 | 2a, 2b, 2c | Funktioner och modeller | Utan verktyg | ingen |
| mato1 | 5.01 | 1 | 1b, 1c | Derivata och förändring | Utan verktyg | ingen |
| mato1 | 5.02 | 1 | 1b, 1c | Integraler och area | Utan verktyg | ingen |
| mato1 | 5.03 | 1 | 1b, 1c | Derivata och förändring | Miniräknare | tabell |
| mato1 | 5.04 | 1 | 1b, 1c | Derivata och förändring | Miniräknare | SVG |
| mato1 | 5.05 | 2 | 1b, 1c | Rationella uttryck | Utan verktyg | ingen |
| mato1 | 5.06 | 2 | 1b, 1c | Derivata och förändring | Utan verktyg | ingen |
| mato1 | 5.07 | 2 | 1b, 1c | Integraler och area | Miniräknare | SVG |
| mato1 | 5.08 | 2 | 1b, 1c | Integraler och area | Utan verktyg | ingen |
| mato1 | 5.09 | 2 | 1b, 1c | Derivata och förändring | Miniräknare | ingen |
| mato1 | 5.10 | 3 | 1b, 1c | Optimering och modeller | Miniräknare | SVG |
| mato1 | 5.11 | 2 | 1b, 1c | Integraler och area | Miniräknare | ingen |
| mato1 | 5.12 | 3 | 1b, 1c | Integraler och area | Miniräknare | SVG |
| mato1 | 5.13 | 3 | 1b, 1c | Integraler och area | Miniräknare | SVG |
| mato1 | 5.14 | 2 | 1c | Cosinussatsen | Miniräknare | SVG |
| mato1 | 5.15 | 4 | 1c | Sinussatsen och den tvetydiga situationen | Miniräknare | ingen |
| mato1 | 5.16 | 2 | 1b | Geometriska summor | Miniräknare | tabell |
| mato1 | 5.17 | 3 | 1b | Linjär optimering | GeoGebra + miniräknare | SVG |
| mato1 | 5.18 | 3 | 1b, 1c | Derivata och förändring | Utan verktyg | ingen |
| mato1 | 5.19 | 5 | 1b, 1c | Derivata och förändring | Miniräknare | SVG |
| mato1 | 5.20 | 4 | 1b, 1c | Derivata och förändring | Utan verktyg | ingen |
| mato2 | 6.01 | 1 | 2c | Derivata och funktioner | Utan verktyg | ingen |
| mato2 | 6.02 | 1 | 2c | Trigonometri och modeller | Utan verktyg | ingen |
| mato2 | 6.03 | 1 | 2c | Komplexa tal och algebra | Miniräknare | SVG |
| mato2 | 6.04 | 2 | 2c | Derivata och funktioner | Utan verktyg | ingen |
| mato2 | 6.05 | 2 | 2c | Derivata och funktioner | Utan verktyg | ingen |
| mato2 | 6.06 | 2 | 2c | Derivata och funktioner | Utan verktyg | ingen |
| mato2 | 6.07 | 2 | 2c | Trigonometri och modeller | Miniräknare | ingen |
| mato2 | 6.08 | 2 | 2c | Integraler och tillämpningar | Utan verktyg | ingen |
| mato2 | 6.09 | 3 | 2c | Integraler och tillämpningar | Miniräknare | SVG |
| mato2 | 6.10 | 3 | 2c | Integraler och tillämpningar | Miniräknare | ingen |
| mato2 | 6.11 | 2 | 2c | Komplexa tal och algebra | Miniräknare | ingen |
| mato2 | 6.12 | 3 | 2c | Komplexa tal och algebra | Utan verktyg | ingen |
| mato2 | 6.13 | 1 | 2c | Derivata och funktioner | Utan verktyg | ingen |
| mato2 | 6.14 | 2 | 2c | Trigonometri och modeller | Miniräknare | SVG |
| mato2 | 6.15 | 3 | 2c | Derivata och funktioner | Utan verktyg | ingen |
| mato2 | 6.16 | 2 | 2c | Derivata och funktioner | Miniräknare | ingen |
| mato2 | 6.17 | 2 | 2c | Komplexa tal och algebra | Utan verktyg | ingen |
| mato2 | 6.18 | 3 | 2c | Integraler och tillämpningar | Utan verktyg | ingen |
| mato2 | 6.19 | 4 | 2c | Integraler och tillämpningar | Utan verktyg | ingen |
| mato2 | 6.20 | 5 | 2c | Trigonometri och modeller | Utan verktyg | ingen |
