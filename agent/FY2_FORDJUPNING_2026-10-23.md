# Fy2: förståelse och kombinerade samband, 2026-10-23

Sex nya, individuellt konstruerade uppgifter: **3.532–3.537**. Inga äldre
uppgifter har ändrats i denna omgång. Alla sex är detaljgranskade: modell,
facit, självrättning, språk, nivå, verktyg och egen SVG-figur. Det är inte
ytterligare en fullständig revision av elektromagnetismkapitlet.

| ID | Nivå | Innehåll och nivåmotivering | Kontrollerat svar / kommentarsförslag |
| --- | --- | --- | --- |
| 3.532 | 5 / A | Hängande vikt driver stavgenerator. Två kraftbalanser, gemensam acceleration, induktion och Ohms lag. Eleven behöver själv välja system och hålla isär kropparnas krafter. | 0,190029… Ω. ”Ny fördjupningsuppgift: koppla Newtons lag för två kroppar till induktion och bestäm kretsens resistans.” |
| 3.533 | 5 / A | Två fria stavar med olika farter. Här måste eleven upptäcka att rörelsemängden bevaras medan rörelseenergi blir värme. | 0,60 J; gemensam fart 3,0 m/s. ”Ny fördjupningsuppgift om induktion, rörelsemängd och energiomvandling.” |
| 3.534 | 4 / C | Jonens massa bestäms genom accelerationsspänning och halvcirkelbana. Kombinera elektrisk energi och centripetalkraft; avståndet är diameter, laddningen 2e. | 39,881… u ≈ 40 u. ”Ny uppgift som kombinerar elektrisk energi och cirkelrörelse.” |
| 3.535 | 4 / C | Generator, transformator och resistiva kablar. Toppspänning måste skiljas från effektivvärde, och kabel- samt generatorförluster räknas med. Flera samband men etablerade modeller ger C. | 141,113… W ≈ 140 W. ”Ny uppgift om hela energikedjan från mekaniskt arbete till ett värmeelement.” |
| 3.536 | 4 / C | En externt driven stav laddar ett batteri. Eleven måste först avgöra energins och strömmens riktning och därefter skilja lagrad energi från värme. | 75 %. ”Ny uppgift om när inducerad spänning laddar ett batteri i stället för att batteriet driver rörelsen.” |
| 3.537 | 5 / A | Slingans area växer medan fältet minskar. Flödet är produkten av två tidsberoende storheter. Andragradsfunktionens maximum ger strömriktningens byte. | 1,0 s. ”Ny fördjupningsuppgift där algebra och magnetiskt flöde måste kombineras.” |

## Pedagogiska och fysiska beslut

- Nivån beror på modellval och samband, inte bara antalet räkneoperationer.
- Varje fråga är ett fristående kort med alla nödvändiga data. Faciten visar
  avgörande mellanled i sammanhängande resonemang, utan numrerade steg.
- Alla sex har miniräknare. Ingen kräver GeoGebra. I 3.537 räcker en
  andragradsfunktions symmetri/kvadratkomplettering; derivata är inget krav.
- Inga standardkonstanter eller färdiga lösningsformler ges i frågorna.
  Mätuppgifter lagrar oavrundade svar och tillåter normal tvåsiffrig precision.
  Enhet står i parentes efter frågan och visas även vid svarsfältet.
- 3.532: magnetisk bromskraft är inte mg; både vikten och staven accelererar.
- 3.533: lika stora motriktade krafter följer av samma ström, stavlängd och
  homogena B. Farterna utjämnas asymptotiskt. Slutströmmen är noll och
  minskad rörelseenergi blir värme; uppgiften kräver ingen differentialekvation.
- 3.534: positiv jon, hastighet uppåt och B ut ur bilden ger böjning åt höger.
  Halvcirkeln och detektoravståndet är geometriskt samstämmiga.
- 3.535: sinusformen motiverar toppvärde/√2. Båda kablarna ligger i serie
  med lasten. Transformatorn är ideal; 80 % gäller generatorn.
- 3.536: pluspol på övre skenan, B inåt, rörelse åt höger. Stavens emk 8 V
  överstiger batteriets 6 V: 1 A laddar batteriet. Effektbalans 8 = 6 + 2 W.
- 3.537: flödet är 0,018−0,002(t−1)² Wb under det angivna intervallet.
  Noll inducerad spänning vid maximum, sedan motsatt riktning. Vanlig
  resistiv slinga används, utan behandling av självinduktiva fördröjningar.

## Granskningsutfall

**Samtliga granskade:** 3.532, 3.533, 3.534, 3.535, 3.536, 3.537.

**Åtgärdade äldre fel:** inga; detta är konstruktion av nytt innehåll.

**Granskad – inget fel efter konstruktionskontrollen:** samtliga sex ovan.
Kommentarsförslag finns per ID i tabellen. Inga externa felrapporter stängs.

Under konstruktionen korrigerades två långa mobilrader i 3.532:s facit,
flyttades fältmarkörer från etiketter och förtydligades generatorns
verkningsgrad i figuren. Nya regressionstester skyddar fysiken och visningen.

## Verifiering

- `tools/fy2-fordjupning-2026-10-23.test.js`: sju godkända testgrupper.
  Oberoende kraft-, energi- och kretsberäkningar; dessutom numerisk simulering
  av de två fria stavarna som verifierar slutlig fart och värme.
- Konsumentens `tools/fy2-fordjupning-2026-10-23.browser.cjs`: 48 godkända
  rättningskontroller, 12 elevvyer och 12 lärarvyer (390/1280 px).
  Korrekt avrundade och mer noggranna svar, decimalpunkt/komma och enhet
  godtas; fel svar avvisas. Inga renderings-, JavaScript- eller klippningsfel.
- Full validator före/efter: ERROR 1485/1485, WARNING 230/230, INFO
  1446/1446. Inga nya fynd; äldre fynd är utanför denna leverans.
- Samtliga sex figurer visuellt granskade. En hastighetsetikett flyttades
  från den streckade slingkanten efter SVG-kontrollen. Chromium-CLI fick
  timeout; samma DOM- och geometriregler kördes med Playwright i stället.
  Slutresultat: 6 figurer, 0 ERROR, 0 WARNING, 7 INFO (bakgrundskanter
  och jonens halvcirkelbana, som är manuellt och geometriskt verifierad).
- Gemensam bank synkas från master, cacheversion höjs i båda apparna.
  Befintliga orelaterade Fy1-utkast i `uppgifter.js` ingår inte.
