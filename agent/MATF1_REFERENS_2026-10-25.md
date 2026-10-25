# Matematik fördjupning: egna uppgifter efter lärarens exempel – 2026-10-25

18 nya uppgifter: 7 kombinatorik/fakulteter, 6 kongruens och 5 partiell integration. Samtliga har öppna svar, individuella lösningar med mellanled och markerat slutsvar samt en egen ledtråd. Inga gamla bankuppgifter ändras. Användarens bilder är referens för innehåll och nivå; uppgifterna är egna varianter med andra uttryck, sammanhang eller frågeidéer.

## Nivåer och variation

Nivå 1/2/3/4/5: **2/5/6/4/1**. Ren resttolkning är nivå 1. Val av grupp och enkel partiell integration är nivå 2. Omvända frågor och samband får nivå 3. Urval med villkor, fakultetssumma och två integrationsomgångar är nivå 4. Den cirkulära integralen #3.356 kräver att eleven löser ett samband där samma integral återkommer och ligger på nivå 5.

Vi har inte kopierat betygsetiketterna från skärmbilderna automatiskt. #1.804 är en direkt fakultetsförkortning (nivå 2), medan #1.806 kräver förkortning av två termer och faktorisering (nivå 4). Mängdträning ingår, men kombineras med omvänd permutation, teckenkontroll, intervallvillkor, två potensperioder och en area.

Fakultetsalgebra efterfrågar ett uttryck utan fakultetstecken eller en saknad faktor. Därmed prövas samma samband utan att självrättningen måste gissa om godtyckliga symboliska fakultetsuttryck är identiska. Ekvivalenta utvecklade/faktoriserade polynom godkänns. Antalsfrågorna godtar både heltalet och korrekta numeriska fakultetsuttryck.

## Verktyg och figurer

Miniräknare tillåts på 15 uppgifter. Undantagen #1.804–1.806 prövar uttrycklig symbolisk fakultetsalgebra med små koefficienter. GeoGebra behövs inte för dessa uppgifter. Integralerna anger uttryckligen partiell integration: CAS skulle ta bort den metod som ska tränas, vilket motiverar undantaget enligt verktygspolicyn. Vanlig miniräknare är tillåten även där.

Fyra egna SVG: böcker (#1.803), urna och sorterade val (#1.807), 24-timmarsklocka (#2.723), integralarea (#3.357). Övriga frågor är ren algebra eller korta talvillkor där en bild inte tillför information. Figurerna är visuellt granskade; SVG-kontrollen har inga varningar, bara information om avsiktliga bakgrundsrektanglar. Integralfiguren följer y=x cos x med de korrekta nollställena 0 och π/2.

## Hittad rättningsbrist och åtgärd

`7*32!/(2!*30!)` gav ett flyttal strax under 3472 och underkändes trots korrekt heltalsresultat. `antal_satt` räknar nu uttryck med heltal, de fyra räknesätten, heltalspotenser och fakulteter som exakta bråk med BigInt. Det är **inte** en utökad numerisk tolerans. Varje led i en likhetskedja ska fortfarande vara korrekt. Bråkexponenter och andra numeriska funktioner använder den tidigare strikta parsern. Fysikens och övriga numeriska format ändras inte.

Parsern är avgränsad: säkert representerbart icke-negativt slutsvar, fakultet högst 170, längd- och storleksgränser, ingen eval. Felaktiga fakulteter, dubbel fakultet, division med noll, öppna uttryck, fel svar och nästan-heltal ska fortsatt underkännas. Fem äldre uppgifter har provats i faktiska svarsfält:

| ID | Status | Kommentarförslag |
| --- | --- | --- |
| #1.21 | Åtgärdad i självrättningen | Rätt facit 33 649 är oförändrat. Även den exakta kvoten 23!/(5!·18!) godkänns utan flyttalsfel. |
| #1.27 | Åtgärdad i självrättningen | Rätt facit 2 598 960 är oförändrat. Även 52!/(5!·47!) godkänns säkert. |
| #1.509 | Granskad – inget fel | 5! och 120 godkänns fortfarande. |
| #1.510 | Granskad – inget fel | 6! och 720 godkänns fortfarande; tidigare rättning bevaras. |
| #1.136 | Granskad – inget fel | 6! och 720 godkänns fortfarande; likhetskedjor kontrolleras led för led. |

Inga rapportstatusar har ändrats i Supabase.

## Verifiering

- `tools/matf1-referens-2026-10-25.test.py`: oberoende SymPy-derivering av bankens faktiska integralsvar, symbolisk fakultetsförenkling, fullständig uppräkning av bokordningar/urnurval, modulär exponentiering, unik intervallösning och metadata.
- 256 kontroller i verkliga svarsfält för 18 nya och 5 äldre uppgifter, inklusive faktorisering, fria konstanter, fakultetskvoter, feltecken och saknade konstanter. Allt godkänt.
- 46 elevvyer och 46 lärarvyer vid 390/1280 px: godkända. Flera för långa integralrader delades innan leverans. Fritextfälten testas som textarea, inte som påhittade numeriska fält.
- Bankvalidator: inga fynd på de 18 nya uppgifterna. Detta är inte en ny full manuell granskning av äldre Matf1.
- Tidigare tester `antal-satt`, `exakta-talsvar`, `felrapport-1-136` och `felrapporter-2026-10-14` passerar. Nya regressionsfall omfattar minst fem stora fakultetskvoter och fall som måste underkännas.
- De 1 685 äldre bankobjekten är oförändrade. Master och konsument synkroniseras byte för byte.

## Alla nya uppgifter och kommentarförslag

| ID | Nivå | Innehåll/kommentar |
| --- | --- | --- |
| #1.802 | 2 | Tillagd och granskad: Välja sju ledamöter utan roller: 120 grupper. |
| #1.803 | 3 | Tillagd och granskad: Två bestämda böcker intill varandra: 2·6! = 1 440 ordningar. |
| #1.804 | 2 | Tillagd och granskad: Fakultetskvot till polynom: (n+1)(n+2). |
| #1.805 | 3 | Tillagd och granskad: Gemensam faktor i fakultetsdifferens: faktorn n−2. |
| #1.806 | 4 | Tillagd och granskad: Summa av fakultetskvoter: (n+1)(n+3). |
| #1.807 | 4 | Tillagd och granskad: Fyra lappar med 8 som näst minsta tal: 7·C(32,2) = 3 472. |
| #1.808 | 2 | Tillagd och granskad: Omvänd permutation: n! = 120 ger n = 5. |
| #2.720 | 1 | Tillagd och granskad: Tolka resten: 47 modulo 6 ger 5. |
| #2.721 | 2 | Tillagd och granskad: Två kongruenser i ett intervall: enda lösningen är 32. |
| #2.722 | 1 | Tillagd och granskad: Kongruent med noll: minsta tillägg till 79 är 12. |
| #2.723 | 3 | Tillagd och granskad: Klocka och stor exponent: efter 7¹²³ timmar är timtalet 0. |
| #2.724 | 3 | Tillagd och granskad: Period sex för potensrester: resten av 14³⁷ modulo 9 är 5. |
| #2.725 | 4 | Tillagd och granskad: Två olika potensperioder och addition: sista siffran är 2. |
| #3.353 | 2 | Tillagd och granskad: Linjärt polynom gånger eˣ: en partiell integration. |
| #3.354 | 3 | Tillagd och granskad: x³ ln x: logaritmen deriveras, polynomet integreras. |
| #3.355 | 4 | Tillagd och granskad: x² cos(2x): två partiella integrationer och teckenkontroll. |
| #3.356 | 5 | Tillagd och granskad: e²ˣ sin x: två integraler kopplas ihop till en ekvation. |
| #3.357 | 3 | Tillagd och granskad: Exakt skuggad area: π/2−1. |
