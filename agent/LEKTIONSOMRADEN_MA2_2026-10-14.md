# Lektionsområden i Matematik 2 – 2026-10-14

## Underlag och avgränsning

Användarens mål: ungefär ett områdeskort per lektion. Punktträning ska välja
uppgiftsvarianter inom momentet. Konjugatregeln och kvadreringsreglerna får vara
ett gemensamt område.

Windows-planeringarna är inte åtkomliga i molnmiljön. Ingen aktuell planering
har lästs. Denna första ändring utgår från befintliga OMR-moment, som enligt
CLAUDE.md indelades efter planeringarna 2026-10-01, samt det nya användarexemplet.
Exakt lektionsordning och omfattning behöver jämföras med uppladdade planeringar.

## Genomförd ändring

Ma2 hade kvar bred GRUPPMA2-gruppering trots den tidigare momentindelningen.
De breda samlingskorten visas nu som sina befintliga, mindre moment: bland annat
substitution, addition, nollproduktmetoden, kvadratkomplettering, pq-formeln,
logaritmbegreppet, logaritmlagarna, kvartiler, lådagram och standardavvikelse.
Konjugatregeln och kvadreringsreglerna samlas i ett område med fyra familjer.
I 2a samlas de två fördjupningskorten om andragradsekvationer med tillämpningar.
ST01:s separata geometrikort i 2c och samlade Cirkelgeometri i 2b bevaras.

| Spår | Kort före | Kort efter | Tillgängliga träningskort |
|---|---:|---:|---:|
| 2a | 15 | 40 | 1502 |
| 2b | 22 | 55 | 2239 |
| 2c | 22 | 57 | 2234 |

Uppgiftslabbet visar samma struktur och behåller områdenas ordning i menyn.
Spårbegränsade grupper visas bara i rätt spår, så geometrin dubbleras inte.

## Sparade resultat och uppdrag

Inga bankobjekt ändras: ID, omr, familj, facit, rättSvar, nivåer och
verktygstillstånd är oförändrade. Detta är ingen ny matematisk granskning.
Områdesresultaten var redan sparade per OMR, så ingen profilskrivande migrering
behövs. Genomgångarna är kopplade till OMR och deras kopplingar bevaras.

Gamla grupper markeras historisk:true. De deltar inte i nya områdeskort eller
rekommendationer. hittaTraningskort kan däremot återfinna dem för sparade
uppdrag, inklusive nivåpass och familjepass. Dagens och äldre uppdragsräkning
använder samma urval; uppdragens mål, befintliga framsteg och XP-regler ändras inte.
Kunskapsgymmets BANK_VERSION höjs. Strukturfilerna är identiska mellan repona.

## Verifiering

- Kunskapsgymmet: 167/167 Node-tester godkända.
- Uppgiftslabbet: 373/373 tester utanför SVG-sviten godkända. SVG-sviten ingår
  inte i denna slutkontroll; ett tidigare försök med hela sviten avslutades
  utan slutrapport och räknas inte som godkänt. Inga figurer har ändrats.
- Riktig Chromium: alla 152 områdeskort i de tre spåren har en uppgiftspool
  och kan startas. Varje OMR visas exakt en gång. Områdespass blandar inte
  in uppgifter från andra moment. Kopplade genomgångar följer rätt områden.
- Sparade områdesvärden, familjevärden, historik och XP är oförändrade vid
  navigering och passstart. Gamla grupp-, familje- och nivåpass fungerar.
- Dagens och gårdagens uppdrag räknar rätt delområden; fel svar och andra
  områden räknas inte. Uppdrags-XP betalas bara en gång.
- Mobil 390 px och dator 1280 px kontrollerade. Ingen JavaScript-runtimeexception.
- Syntaxkontroll av inline-JavaScript och git diff --check godkända.

Tester: Kunskapsgymmet/tools/lektionsomraden.test.js,
Kunskapsgymmet/tools/lektionsomraden.browser.js och
Uppgiftslabbet/tools/lektionsomraden.test.js. Den befintliga uppdragsbokssviten
laddar även den nya uppslagsfunktionen; dess tidigare kontrollvillkor behålls.

## Områden i 2c

- Kapitel 1: **Räta linjens ekvation** – 25 träningskort; 2 val i punktträningen.
- Kapitel 1: **Räta linjer: formel, tabell och graf** – 20 träningskort; 2 val i punktträningen.
- Kapitel 1: **Bestämma linjära funktioner** – 19 träningskort; 2 val i punktträningen.
- Kapitel 1: **Linjära ekvationssystem** – 19 träningskort; 2 val i punktträningen.
- Kapitel 1: **Grafisk lösning av ekvationssystem** – 11 träningskort; 0 val i punktträningen.
- Kapitel 1: **Substitutionsmetoden** – 25 träningskort; 2 val i punktträningen.
- Kapitel 1: **Additionsmetoden** – 23 träningskort; 2 val i punktträningen.
- Kapitel 1: **Ekvationssystem med tre obekanta** – 27 träningskort; 2 val i punktträningen.
- Kapitel 1: **Ekvationssystem med ingen eller oändligt många lösningar** – 23 träningskort; 2 val i punktträningen.
- Kapitel 1: **Tillämpningar och problemlösning med ekvationssystem** – 31 träningskort; 3 val i punktträningen.
- Kapitel 1: **Multiplikation av parentesuttryck** – 23 träningskort; 2 val i punktträningen.
- Kapitel 1: **Konjugatregeln och kvadreringsreglerna** – 47 träningskort; 4 val i punktträningen.
- Kapitel 1: **Faktorisering** – 24 träningskort; 2 val i punktträningen.
- Kapitel 2: **Enkla andragradsekvationer** – 37 träningskort; 2 val i punktträningen.
- Kapitel 2: **Nollproduktmetoden** – 37 träningskort; 2 val i punktträningen.
- Kapitel 2: **Kvadratkomplettering** – 25 träningskort; 2 val i punktträningen.
- Kapitel 2: **Lösningsformel för andragradsekvationer** – 32 träningskort; 2 val i punktträningen.
- Kapitel 2: **Andragradsekvationer – fördjupning** – 15 träningskort; 2 val i punktträningen.
- Kapitel 2: **Samband mellan rötter och koefficienter** – 17 träningskort; 2 val i punktträningen.
- Kapitel 2: **Tillämpningar och problemlösning med andragradsekvationer** – 30 träningskort; 2 val i punktträningen.
- Kapitel 2: **Rotekvationer** – 25 träningskort; 2 val i punktträningen.
- Kapitel 2: **Funktioner och funktionsskrivsätt – repetition** – 129 träningskort; 4 val i punktträningen.
- Kapitel 2: **Andragradsfunktioner** – 40 träningskort; 3 val i punktträningen.
- Kapitel 2: **Andragradsfunktionens graf** – 52 träningskort; 2 val i punktträningen.
- Kapitel 2: **Största och minsta värde** – 27 träningskort; 2 val i punktträningen.
- Kapitel 2: **Från graf till formel** – 28 träningskort; 2 val i punktträningen.
- Kapitel 2: **Problemlösning med andragradsfunktioner** – 39 träningskort; 3 val i punktträningen.
- Kapitel 2: **Potenser och potensregler** – 40 träningskort; 3 val i punktträningen.
- Kapitel 2: **Exponentialfunktioner** – 40 träningskort; 3 val i punktträningen.
- Kapitel 2: **Exponentialfunktioners grafer** – 28 träningskort; 2 val i punktträningen.
- Kapitel 2: **Logaritmbegreppet** – 36 träningskort; 2 val i punktträningen.
- Kapitel 2: **Logaritmlagarna** – 46 träningskort; 3 val i punktträningen.
- Kapitel 2: **Exponentialekvationer** – 47 träningskort; 3 val i punktträningen.
- Kapitel 2: **Potensekvationer** – 20 träningskort; 2 val i punktträningen.
- Kapitel 2: **Jämföra exponential- och potensekvationer** – 21 träningskort; 2 val i punktträningen.
- Kapitel 2: **Regressionsanalys** – 15 träningskort; 2 val i punktträningen.
- Kapitel 3: **Geometriska begrepp och definitioner** – 36 träningskort; 2 val i punktträningen.
- Kapitel 3: **Sats och bevis, implikation och ekvivalens** – 59 träningskort; 3 val i punktträningen.
- Kapitel 3: **Yttervinkelsatsen** – 43 träningskort; 2 val i punktträningen.
- Kapitel 3: **Randvinklar och medelpunktsvinklar** – 76 träningskort; 4 val i punktträningen.
- Kapitel 3: **Pythagoras sats** – 50 träningskort; 3 val i punktträningen.
- Kapitel 3: **Likformighet** – 63 träningskort; 3 val i punktträningen.
- Kapitel 3: **Topptriangelsatsen och transversalsatsen** – 49 träningskort; 2 val i punktträningen.
- Kapitel 3: **Bevis med likformighet** – 39 träningskort; 2 val i punktträningen.
- Kapitel 3: **Kordasatsen och bisektrissatsen** – 54 träningskort; 4 val i punktträningen.
- Kapitel 3: **Avståndsformeln och mittpunktsformeln** – 39 träningskort; 2 val i punktträningen.
- Kapitel 3: **Koordinatgeometri – problemlösning** – 39 träningskort; 2 val i punktträningen.
- Kapitel 3: **Problemlösning** – 30 träningskort; 0 val i punktträningen.
- Kapitel 4: **Tabeller och diagram** – 9 träningskort; 0 val i punktträningen.
- Kapitel 4: **Medelvärde, median och typvärde** – 75 träningskort; 3 val i punktträningen.
- Kapitel 4: **Kvartiler och percentiler** – 43 träningskort; 2 val i punktträningen.
- Kapitel 4: **Lådagram** – 64 träningskort; 2 val i punktträningen.
- Kapitel 4: **Standardavvikelse** – 154 träningskort; 2 val i punktträningen.
- Kapitel 4: **Korrelation och korrelationskoefficient** – 31 träningskort; 2 val i punktträningen.
- Kapitel 4: **Linjär regression** – 27 träningskort; 2 val i punktträningen.
- Kapitel 4: **Normalfördelning** – 70 träningskort; 2 val i punktträningen.
- Kapitel 4: **Normalfördelning med digitala verktyg** – 41 träningskort; 2 val i punktträningen.

## Kvarstående innehållsluckor

Omstruktureringen skapar inga nya genomgångar. Befintliga luckor finns bland
annat för Från graf till formel i 2a/2b, Yttervinkelsatsen i 2a samt Tabeller
och diagram. Programspecifika tillämpningar saknar avsiktligt genomgångar
enligt tidigare avgränsning. Geometri – problemlösning har många små familjer
som ännu inte når punktträningens femkortströskel. Dessa behöver redaktionell
uppföljning, inte automatisk massflytt eller sänkt synlighetströskel.
