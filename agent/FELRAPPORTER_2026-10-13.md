# Felrapporter 2026-10-13 08:46

19 rapporter kontrollerade. 15 föreslås avslutas som **Åtgärdad**, 4 som **Granskad – inget fel**. Totalt 107 uppgifter följdgranskade och 66 bankobjekt ändrade. Självrättning och passurval har också ändrats i Kunskapsgymmet. Detta är en riktad granskning, inte en slutmarkering av hela matematikbanken.

Inga Supabase-statusar eller kommentarer har sparats. Tabellen innehåller förslag att använda vid manuell avslutning. När elevens exakta inmatning saknas går det inte att fastställa orsaken till den historiska underkänningen. Kända parserfel och avrundningsfall har reproducerats separat.

## Rapporter och kommentarer

| Kurs | Uppgift | Föreslagen status | Kommentar |
|---|---|---|---|
| matf1 | #1.15 a) | Åtgärdad | Frågan skiljer nu tydligt mellan talet 2 och mängden {2}. Lösningen förklarar varför påståendet är falskt. |
| matf1 | #1.347 | Åtgärdad | Frågan och ledtråden är förtydligade. De som väljer båda räknas en gång: 36 + 31 − 8 = 59. |
| matf1 | #1.164 a) | Granskad – inget fel | Facit 36 är korrekt: 18 + 7 + 11. De 4 utanför cirklarna ingår inte i unionen. Frågan och förklaringen har förtydligats. |
| mato2 | #1.149 | Åtgärdad | Alternativen visar nu vinkeln i grader med en decimal. Rätt alternativ är fortfarande B. |
| mato2 | #1.131 b) | Åtgärdad | Det står nu att v ska anges i grader med en decimal. R och v har egna svarsfält: R = 13, v ≈ −67,4°. |
| mato2 | #1.59 b) | Åtgärdad | Det överblivna ordet är borttaget. Frågan är nu: Bestäm en ekvation för funktionens medellinje. Svaret är y = 2. |
| matf1 | #1.727 a) | Åtgärdad | Facit visas nu avrundat. Korrekt avrundade svar med minst två värdesiffror godtas, exempelvis 0,16 eller 15,5 %. Det tidigare sannolikhetsvärdet var korrekt. |
| matf1 | #1.77 | Granskad – inget fel | Föredrag betyder en presentation och var korrekt i konferenssituationen. Texten använder nu presentationer. AB räknas som ett block, så antalet är 5! = 120. |
| matf1 | #1.625 | Åtgärdad | Miniräknare är nu tillåten. Varje bokstavsplats har 6 val, så antalet koder är 6⁴ = 1 296. |
| mato1 | #1.99 | Åtgärdad | Flera likadana kontinuitetsuppgifter har varierats, och urvalet undviker återkomst tills alternativen har använts. När urvalet är slut fördelas repetitionerna jämnt. Extra repetition av felsvar är avsiktlig. |
| mato1 | #4.495 | Åtgärdad | Ledningen som gav hela svaret har tagits bort. Uppgiften är kvar som en enkel introduktion på nivå 1. |
| ma2 | #2.219 | Åtgärdad | Självrättningen är korrigerad. Både lg8 och lg(8) godkänns nu. |
| ma2 | #1.54 | Granskad – inget fel | Lutningen −2 gör linjen vinkelrät, men den ska också gå genom (4, 1). Insättning ger 1 = −8 + m, alltså m = 9. Båda villkoren är nu tydligare i frågan. |
| ma2 | #1.347 | Granskad – inget fel | Lutningen 3 gör linjen vinkelrät, men linjen ska också gå genom (2, 5). Därför är 5 = 6 + m och m = −1. Båda villkoren är nu tydligare i frågan. |
| matf1 | #1.548 | Åtgärdad | Frågan anger nu noggrannheten för avrundade svar. 1/16, 0,0625, 0,063 och 6,25 % godkänns. 0,06 har bara en värdesiffra. Det tidigare exakta facit var korrekt. |
| ma2 | #2.57 | Åtgärdad | Båda lösningarna skrivs nu i separata svarsfält. Du kan skriva 2 och −3 i valfri ordning. |
| ma1 | #7.490 | Åtgärdad | Frågan förklarar nu vad säkerhetsfaktorn betyder. Med faktorn 2 får kranen lyfta halva kapaciteten, alltså 2,5 ton. |
| ma1 | #7.163 | Åtgärdad | Texten är omskriven till hela meningar och anger att kostnaden ska inkludera frakt. Svaret är 1 051 kr. |
| matf1 | #2.79 | Åtgärdad | Potenser är valfria. Både 2³·3²·5 och 2·2·2·3·3·5 godkänns. Svaret måste bestå av primtalsfaktorer; enbart 360 är ingen faktorisering. |

## Analys och beslut

- Ma2 #2.219: båda LaTeX-listorna saknade `lg`. `lg8`, `lg(8)` och `lg 8` godkänns, `lg9` underkänns. Inga logaritmfacit ändrade.
- Sannolikhet: det tidigare intervalltestet kring ett halvt avrundningssteg godtog även fel grannsvar. För 1/16 godtas 0,063 men inte 0,062; för 5/16 godtas 0,313 men inte 0,312. Relativ numerisk tolerans och exakta uttryck behålls, explicit tolerans vidgas inte. Decimalsträngar visas med samma avrundning som tal. #1.727 använder full beräkningsprecision; dess a-kort visar bara stående skott.
- Primtalsfaktorisering: potenser var redan valfria, men generell uttryckslikhet godkände även 360 och 4·9·10. Det nya formatet kräver en produkt av primtal med valfria positiva heltalspotenser. Mängd-/SGD-/MGM-svar får inte detta format bara för att metoden använder primtal.
- Mato2 #1.131/#1.81: R och v har separata etiketter, vinkelenhet grader, intervall −90° < v < 90°, R exakt och v med en decimal. Fullprecision svarsvärden och halvt decimalsteg som tolerans. Namngivna nästlade fält rättas i ordning även i heluppgift. #1.81 hör nu till området asinx_bcosx, inte radianernas kurvområde. #1.149 har avrundade grader i alternativen; B är fortfarande rätt.
- Mato2 #1.59 och fem analoger: hela frågemeningar på varje kort, rätt radianenhet där den behövs, facit utan generiska irrelevanta inledningar eller andra delars svar. Max/min har tydliga etiketter; asymptoternas ordning är fri.
- Mato1 #1.99: 4 är fortfarande korrekt. Samma algebraiska problem fanns under olika ID:n. Fem varianter har fått andra faktoriseringsvägar och svar. Efter att alla tillgängliga kort visats väljer urvalet bland dem som visats minst, baserat på hela passhistoriken. Felsvarskön får fortfarande ge avsiktlig repetition. Bakåtträning och XP-spärr ändras inte. Utan passhistorik kan vi inte säkert fastställa elevens ursprungliga upprepningskedja.
- Vinkelräta linjer: m-värdet är fritt endast om inget punktvillkor eller motsvarande krav finns. I båda rapporterna bestämmer den angivna punkten m. De korrekta facitvärdena bevaras.
- Nivå: den nästlade mängden #1.15 och primtalsfaktoriseringen av 360 #2.79 är nivå 2, inte de allra enklaste nivå 1. Tredjegradsfaktoriseringen i #3.799 är C/nivå 3. Övriga rapportuppgifter behåller nivån; enkel cosinusintroduktion #4.495 är kvar på E/1 sedan facitledningen tagits bort.
- Ma1: säkerhetsfaktorn definieras i fem nybörjaruppgifter. Frågor om kostnad har hela meningar, rätt moms-/fraktordning och kr som svarsenhet.

## Jämförelser per feltyp

**element_och_mangd (matf1)**: #1.476, #1.477, #1.474, #1.475, #1.481, #1.02. Enda uppgiften med en mängd som element. Jämförd med sex medlemskaps- och uppräkningsuppgifter. Fem ledtrådar hänvisade felaktigt till mängdoperationer och har anpassats.

**Venn_union (matf1)**: #1.308, #1.309, #1.318, #1.319, #1.310, #1.320. 36+31−8=59. Venn-diagrammets områden ger union36, exakt-en29, utanför4. Två ledtrådar om mängdbyggare ersatta med dubbelräkning.

**blockordning (matf1)**: #1.72, #1.74, #1.76, #1.138, #1.195. Föredrag var ett korrekt ord för konferenspresentationer. AB-block ger5!=120; med fri intern ordning måste man också multiplicera med2.

**potens_och_raknare (matf1)**: #1.24, #1.501, #1.576, #1.580, #1.582. 6^4=1296. Fem jämförbara större potensberäkningar får också räknare. Dubbelt villkor om upprepade siffror i1.580 borttaget.

**sannolikhet_avrundning (matf1)**: #1.549, #1.550, #1.551, #1.552, #1.553, #1.554, #1.725, #1.726, #1.719, #1.720, #1.728. Kortare korrekt avrundade svar godkändes redan. Numeric-strängar visades med onödiga decimaler; halvstegsavrundningen godtog fel grannsvar. Minst två värdesiffror klargörs, exakt bråk/potens bevaras.

**primtalsprodukt (matf1)**: #2.157, #2.209, #2.649, #2.650, #2.80, #2.158, #2.210. Endast två andra direkta primtalsfaktoriseringar finns. Fem SGD/MGM-jämförelser behåller numeriskt svar eftersom de efterfrågar ett tal. Upprepade primtal är tillåtna, sammansatta faktorer och talet utan faktorisering underkänns.

**fasvinkel (mato2)**: #1.81, #1.178, #1.119, #1.148, #1.669, #1.670, #2.564. R=hypot(a,b), v=atan2(b,a) i grader. Vinklarna anges ungefärligt när de inte är standardvinklar; två namngivna fält. Övriga fem exempel har korrekt amplitud/extremvärde/angiven vinkelenhet.

**fullstandiga_delkort (mato2)**: #1.01, #1.17, #1.72, #1.93, #1.56. Fragment som medellinje och ersätts av fullständiga meningar. Delens facit renodlas. I1.72 var flera delsvar blandade i huvudfacit; ordnade max/min-fält förtydligas.

**kontinuitet_variation (mato1)**: #1.518, #3.57, #3.799, #1.523, #3.812. Identisk matematisk kärna under flera ID:n. Fem funktioner varierade, inklusive linjär faktor, andragrad, tredjegrad och faktor2 i nämnaren. Urvalet balanserar antal visningar över hela passhistoriken när poolen är slut.

**facitledning (mato1)**: #4.31, #4.36, #4.41, #4.46, #4.409. cos0=1-ledningen avslöjade hela svaret. Borttagen; nivå1 behålls. Jämförelserna kräver fortfarande att hitta hela lösningsmängden.

**lg_LaTeX (ma2)**: #2.217, #2.241, #2.26, #2.109, #2.250. LaTeX-normalisering saknade lg. Båda regexlistorna kompletterade, korrekt elevsvar accepteras utan att facitvärden ändras.

**vinkelrat_och_punkt (ma2)**: #1.317, #1.329, #1.17, #1.348, #1.82. Facit9 respektive−1 är rätt när linjen också passerar punkten. Endast lutningsuppgiften1.317 saknar punktvillkor och kräver inget m.

**tva_rotter (ma2)**: #2.01, #2.81, #2.128, #2.129, #2.49. Två separata rutfält och uttryckligt valfri ordning för sex ekvationer. Varje rot substituerad i originalekvationen.

**sakerhetsfaktor (ma1)**: #7.488, #7.491, #7.493, #7.499, #7.525, #7.536. Definition behövs på nivå1. Division när tillåten last söks, multiplikation när kapaciteten ska dimensioneras. De två senare hade redan tydlig definition.

**hela_meningar_kostnad (ma1)**: #7.162, #7.165, #7.167, #7.168, #7.169. Fullständiga meningar, definierad frakt/momsordning och svarsenhet. 18*42+295=1051kr; momsexempel180*24*.88*1.25=4752kr.

## Alla granskade uppgifter

**matf1**: #1.02, #1.15, #1.24, #1.72, #1.74, #1.76, #1.77, #1.138, #1.164, #1.195, #1.308, #1.309, #1.310, #1.318, #1.319, #1.320, #1.347, #1.474, #1.475, #1.476, #1.477, #1.481, #1.501, #1.548, #1.549, #1.550, #1.551, #1.552, #1.553, #1.554, #1.576, #1.580, #1.582, #1.625, #1.719, #1.720, #1.725, #1.726, #1.727, #1.728, #2.79, #2.80, #2.157, #2.158, #2.209, #2.210, #2.649, #2.650.

**mato2**: #1.01, #1.17, #1.56, #1.59, #1.72, #1.81, #1.93, #1.119, #1.131, #1.148, #1.149, #1.178, #1.669, #1.670, #2.564.

**mato1**: #1.99, #1.518, #1.523, #3.57, #3.799, #3.812, #4.31, #4.36, #4.41, #4.46, #4.409, #4.495.

**ma2**: #1.17, #1.54, #1.82, #1.317, #1.329, #1.347, #1.348, #2.01, #2.26, #2.49, #2.57, #2.81, #2.109, #2.128, #2.129, #2.217, #2.219, #2.241, #2.250.

**ma1**: #7.162, #7.163, #7.165, #7.167, #7.168, #7.169, #7.488, #7.490, #7.491, #7.493, #7.499, #7.525, #7.536.

## Åtgärdad – samtliga granskade ID

**matf1**: #1.15, #1.24, #1.308, #1.318, #1.347, #1.474, #1.475, #1.476, #1.477, #1.481, #1.501, #1.548, #1.549, #1.550, #1.551, #1.552, #1.553, #1.554, #1.576, #1.580, #1.582, #1.625, #1.719, #1.720, #1.725, #1.726, #1.727, #1.728, #2.79, #2.157, #2.209.

**mato2**: #1.01, #1.17, #1.56, #1.59, #1.72, #1.81, #1.93, #1.131, #1.149.

**mato1**: #1.99, #1.518, #1.523, #3.57, #3.799, #3.812, #4.495.

**ma2**: #2.01, #2.49, #2.57, #2.81, #2.128, #2.129, #2.219.

**ma1**: #7.162, #7.163, #7.165, #7.167, #7.168, #7.488, #7.490, #7.491, #7.493, #7.499.

## Granskad – inget fel – samtliga granskade ID

**matf1**: #1.02, #1.72, #1.74, #1.76, #1.77, #1.138, #1.164, #1.195, #1.309, #1.310, #1.319, #1.320, #2.80, #2.158, #2.210, #2.649, #2.650.

**mato2**: #1.119, #1.148, #1.178, #1.669, #1.670, #2.564.

**mato1**: #4.31, #4.36, #4.41, #4.46, #4.409.

**ma2**: #1.17, #1.54, #1.82, #1.317, #1.329, #1.347, #1.348, #2.26, #2.109, #2.217, #2.241, #2.250.

**ma1**: #7.169, #7.525, #7.536.

Fyra rapporterade uppgifter i listan ”inget fel” har ändå fått pedagogiska förtydliganden: matf1 #1.164/#1.77 och ma2 #1.54/#1.347. Deras ursprungliga facit var rätt. I övriga jämförelseuppgifter utan ändring gäller kommentarsförslaget: ”Granskad – inget fel: uppgiftens villkor, facit och svarsform är kontrollerade.”

## Ändrade bankobjekt och fält

| Kurs | ID | Fält |
|---|---|---|
| ma1 | #7.162 | `t`, `rättSvar`, `tolerans`, `svarEnhet`, `svarFormat` |
| ma1 | #7.163 | `t`, `svarEnhet`, `svarFormat` |
| ma1 | #7.165 | `t`, `svarEnhet`, `svarFormat` |
| ma1 | #7.167 | `t`, `svarEnhet`, `svarFormat` |
| ma1 | #7.168 | `t`, `svarEnhet`, `svarFormat` |
| ma1 | #7.488 | `t` |
| ma1 | #7.490 | `t` |
| ma1 | #7.491 | `t` |
| ma1 | #7.493 | `t` |
| ma1 | #7.499 | `t` |
| ma2 | #1.54 | `t`, `s` |
| ma2 | #2.01 | `t`, `svarstyp`, `rättSvar`, `tolerans`, `svarFormat`, `svarsstruktur`, `svarEtiketter` |
| ma2 | #2.49 | `t`, `svarstyp`, `svarEtiketter` |
| ma2 | #2.57 | `t`, `svarstyp`, `rättSvar`, `tolerans`, `svarFormat`, `svarsstruktur`, `svarEtiketter` |
| ma2 | #2.81 | `t`, `svarstyp`, `rättSvar`, `tolerans`, `svarFormat`, `svarsstruktur`, `svarEtiketter` |
| ma2 | #2.128 | `t`, `svarstyp`, `rättSvar`, `tolerans`, `svarFormat`, `svarsstruktur`, `svarEtiketter` |
| ma2 | #2.129 | `t`, `svarstyp`, `rättSvar`, `tolerans`, `svarFormat`, `svarsstruktur`, `svarEtiketter` |
| ma2 | #1.347 | `t`, `s` |
| matf1 | #1.308 | `ledtrad` |
| matf1 | #1.318 | `ledtrad` |
| matf1 | #1.15 | `t`, `s`, `spelDelar`, `ledtrad`, `traningsniva` |
| matf1 | #1.347 | `t`, `s`, `ledtrad` |
| matf1 | #1.164 | `t`, `s`, `spelDelar` |
| matf1 | #1.24 | `miniräknare` |
| matf1 | #1.77 | `t`, `s`, `ledtrad` |
| matf1 | #2.79 | `t`, `svarstyp`, `svarFormat`, `traningsniva` |
| matf1 | #2.157 | `t`, `svarFormat` |
| matf1 | #2.209 | `t`, `svarFormat` |
| matf1 | #1.474 | `ledtrad` |
| matf1 | #1.475 | `ledtrad` |
| matf1 | #1.476 | `ledtrad` |
| matf1 | #1.477 | `ledtrad` |
| matf1 | #1.481 | `ledtrad` |
| matf1 | #1.501 | `miniräknare` |
| matf1 | #1.548 | `t` |
| matf1 | #1.549 | `t` |
| matf1 | #1.550 | `t` |
| matf1 | #1.551 | `t` |
| matf1 | #1.552 | `t` |
| matf1 | #1.553 | `t` |
| matf1 | #1.554 | `t` |
| matf1 | #1.719 | `t`, `spelIntro`, `spelDelar` |
| matf1 | #1.720 | `t`, `spelIntro`, `spelDelar` |
| matf1 | #1.725 | `t`, `spelIntro`, `spelDelar` |
| matf1 | #1.726 | `t`, `spelIntro`, `spelDelar` |
| matf1 | #1.727 | `t`, `rättSvar`, `spelIntro`, `spelDelar` |
| matf1 | #1.728 | `t`, `spelIntro`, `spelDelar` |
| matf1 | #1.576 | `miniräknare` |
| matf1 | #1.580 | `t`, `miniräknare` |
| matf1 | #1.582 | `miniräknare` |
| matf1 | #1.625 | `miniräknare` |
| mato1 | #3.57 | `t`, `s`, `rättSvar`, `ledtrad` |
| mato1 | #1.518 | `t`, `s`, `rättSvar`, `ledtrad` |
| mato1 | #1.523 | `t`, `s`, `rättSvar`, `ledtrad` |
| mato1 | #3.799 | `niva`, `poang`, `t`, `s`, `rättSvar`, `ledtrad`, `traningsniva`, `arbetsinsats` |
| mato1 | #3.812 | `t`, `s`, `rättSvar`, `ledtrad` |
| mato1 | #4.495 | `t` |
| mato2 | #1.01 | `t`, `s`, `spelDelar`, `ledtrad`, `spelIntro` |
| mato2 | #1.17 | `t`, `s`, `spelDelar`, `ledtrad`, `spelIntro` |
| mato2 | #1.56 | `t`, `s`, `ledtrad`, `spelIntro`, `spelDelar` |
| mato2 | #1.59 | `t`, `s`, `spelDelar`, `spelIntro` |
| mato2 | #1.72 | `t`, `s`, `ledtrad`, `spelIntro`, `spelDelar` |
| mato2 | #1.81 | `omr`, `poang`, `t`, `s`, `rättSvar`, `tolerans`, `svarFormat`, `spelDelar`, `familjNyckel`, `spelIntro`, `omrTidigare`, `svarEnhet` |
| mato2 | #1.93 | `t`, `s`, `ledtrad`, `spelIntro`, `spelDelar` |
| mato2 | #1.131 | `t`, `s`, `rättSvar`, `tolerans`, `svarFormat`, `spelDelar`, `spelIntro`, `svarEnhet` |
| mato2 | #1.149 | `t`, `s` |

## Verifiering och leverans

- Master: 355 unika regressionstester täckta. Fullkörningens 310 godkända och 43 miljöfel kompletterades med samtliga 47 SVG-tester godkända i Chromium och den slutliga 12-testers matematikkörningen (två tester tillkom efter fullkörningen). SVG-verktygets standardväg pekar på Windows-Chrome; molnmiljön blockerar också file-URL:er. En tillfällig Playwright-adapter med samma installerade Chromium läste test-HTML direkt. Inga tester eller produktionsregler ändrades för att få grön körning.
- Kunskapsgymmet: samtliga 140 regressionstester godkända, inklusive delkort, rättning, enheter, alternativa tabellkonstanter, temperatur och bakåtknappens XP-spärr.
- Webbläsare: 144 rätt/fel-svarskombinationer i riktiga fält, 96 helkort/delkort och 10 mobil-/datorvisningar. Inga JavaScript-fel eller KaTeX-fel i de kontrollerade visningarna. Slutlig riktad kontroll av Mato2 verifierar att √2 förblir exakt i snabbfacit, medan v visas avrundat; felaktigt avrundad amplitud 1,4142 godtas inte.
- Syntax: fem bankfiler och Kunskapsgymmets två inline-skript kontrollerade. ID-ordning och bankstorlek bevarade, orelaterade objekt oförändrade. Endast dokumenterade fält ändras. Kopiorna i båda repona är byteidentiska.
- Validator: inga nytillkomna ERROR. Befintliga fel ligger utanför de aktuella rapporterna: Ma2 #2.636/#2.637 saknar svarstyp och rättSvar (fyra fynd), Mato2 #2.586/#2.587 ligger i okända kapitel-/områdespar (två fynd). Ma1, Matf1 och Mato1 har inga ERROR. Befintliga WARNING/INFO redovisas i JSON och är inte automatiskt korrigerade.
- Ingen inloggning eller databasändring användes i browserkontrollen. Kundens kommentarer och rapportstatus måste fortfarande sparas av admin. Maskinläsbar lista: [FELRAPPORTER_2026-10-13.json](FELRAPPORTER_2026-10-13.json).

Ändrade filer: fem bankfiler i båda repona; master `agent/FELMONSTER_OCH_BESLUT.md`, denna MD/JSON och `tools/felrapporter-2026-10-13.test.js`; konsument `index.html`, motsvarande enhetstest och browsertest. Befintlig `tools/__pycache__/` i konsumenten lämnas utanför leveransen.

Git: båda repona jämfördes med origin/main före ändring och före leverans. Ingen samtidig remoteändring fanns. Godkänd leverans går till origin/main utan force push.
