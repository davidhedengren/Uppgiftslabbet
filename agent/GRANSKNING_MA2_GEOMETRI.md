# Granskning av Matematik 2c: geometri

Granskad 2026-10-08. Omfattning: samtliga 529 uppgifter i kapitel 3 som är märkta med kurs 2c, inklusive huvudfacit, svarsvärden, nivåer och delkort. Uppgiftslabbet är master; uppgifterma2.js har synkroniserats byte för byte till kunskapsgymmet. Uppgifter som även är märkta 2a/2b får samma korrigeringar där.

## Viktiga rättelser

- 3.99, 3.162 och 3.164: ursprungliga areor översteg den maximala möjliga triangelarean med givna sidor. Givna areor är nu 12, 8 respektive 6; motsvarande stora areor är 108, 50 respektive 37,5. Siddata och träningsidé är bevarade.
- 3.427: två uttryckligen rätvinkliga trianglar med lika area ger ett giltigt motexempel. Olika hypotenusor visar att de inte är kongruenta; olika valda baser ensamt räckte inte.
- Åtta facit hade bråknämnare där en bokstav hamnade utanför nämnaren. Huvudfacit och delkort är rättade.
- Fyra delkort i 3.03/3.05 saknade egna lösningar. De har nu avgränsade facit. Del b i 3.145, 3.177, 3.181 och 3.417 innehåller sitt nödvändiga mellanresultat.
- 3.512: självrättning kräver det efterfrågade heltalssvaret 213 kr. Mindre formuleringar i 3.85, 3.137 och 3.503 är rättade.

## Nivåer och figurer

Nivå 1 reserveras för de allra enklaste uppgifterna: ett direkt samband och enkel beräkning. Nivå 2 kräver något mer, till exempel att först bestämma en skala, sätta upp en proportion eller kombinera vinkelregler. Regeln finns i PEDAGOGISKA_REGLER.md och INNEHALLSREGLER.md. Varje delkort bedöms utifrån sin egen fråga.

49 huvudnivåer och ytterligare fyra delkortsnivåer har justerats individuellt. 31 nya SVG-figurer visar främst likformighet och bevis; lika vinkelpar i VV-bevis markeras med α och β. Sju befintliga figurer följer nu även med till delkorten.

| Träningsnivå | Före | Efter |
|---|---:|---:|
| 1 | 164 | 133 |
| 2 | 150 | 182 |
| 3 | 120 | 122 |
| 4 | 48 | 48 |
| 5 | 47 | 44 |

## Verifiering och begränsningar

- 34 tester passerar: bankkontroll, matematiska regressioner och Kunskapsgymmets faktiska expandGameTask-funktion för delkort.
- JavaScript-syntax kontrollerad; uppgifts-ID:n, antal och innehåll utanför den valda geometrin är oförändrade. Bankkontrollen ger inga fel i de 529 uppgifterna och inga nya anmärkningar.
- Chromium har mätt de 335 SVG-figurer som kontrollverktyget hittar i kapitlet. De 31 nya figurerna har inga fynd. Exempel har även granskats visuellt på stor och smal skärm.
- Äldre figurer har sammanlagt 543 varningar och 79 informationsfynd i den automatiska SVG-kontrollen, exempelvis text nära linjer. Dessa är inte samtliga manuellt åtgärdade; kontrollfynd är inte i sig belägg för felaktigt facit.
- Båda apparna laddar alla 529 uppgifter utan JavaScript- eller KaTeX-fel. Chromium kan inte slå upp externa CDN-domäner direkt i denna container; testharnessen hämtar de riktiga KaTeX-filerna via plattformens HTTPS-proxy. Google Fonts ersätts bara i testet med tom CSS. Inloggning är inte provad.
- SVG-verktygets fulla svit hade 46 godkända tester och ett befintligt skört indexantagande om fysikbanken (584 i stället för aktuella 582). Testet kontrollerar nu det verkliga källindexet; denna kontroll passerar vid separat körning efter rättelsen. Fysikbanken är oförändrad.
- Befintliga dubblettanmärkningar är kvar. Ingen uppgift har raderats eller fått nytt ID. Geometriändringarna levereras i en separat commit efter användarens godkännande.

## Ändringar per uppgift

| ID | Ändrade fält | Motivering |
|---|---|---|
| 3.03 | spelDelar | Kompletterat saknade delkortsfacit utan att avslöja den andra delens svar. |
| 3.05 | s, spelDelar | Kompletterat saknade delkortsfacit utan att avslöja den andra delens svar. |
| 3.08 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.17 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.22 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.26 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.35 | t, traningsniva | Träningsnivå 1 → 2: längdskalan måste först bestämmas och sedan användas. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.43 | spelDelar | Del b sänks till nivå 1: längdskalan är redan given på kortet. |
| 3.44 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.48 | t, traningsniva | Träningsnivå 1 → 2: multiplikation med två decimaltal är inte en av de enklaste introduktionsuppgifterna. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.60 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.62 | traningsniva | Träningsnivå 1 → 2: Pythagoras med större kvadrater kräver mer beräkning än de enklaste fallen. |
| 3.65 | traningsniva | Träningsnivå 1 → 2: eleven måste koppla omkretsernas förhållande till längdskalan. |
| 3.77 | t, traningsniva | Träningsnivå 1 → 2: multiplikation med två decimaltal är inte en av de enklaste introduktionsuppgifterna. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.79 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.81 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.85 | s | Beviset omfattar även origo, där avståndet är noll. |
| 3.97 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.98 | traningsniva | Träningsnivå 1 → 2: hela sidan måste bestämmas före likformighetsberäkningen. |
| 3.99 | rättSvar, s, spelDelar, t | Omöjlig given area 18 ersatt med 12; omräknad stor area 108, även i maskinfacit. |
| 3.101 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.102 | t, traningsniva | Träningsnivå 1 → 2: hela sidan måste bestämmas före likformighetsberäkningen. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.110 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.115 | traningsniva | Träningsnivå 1 → 2: eleven måste koppla omkretsernas förhållande till längdskalan. |
| 3.129 | traningsniva | Träningsnivå 1 → 2: Pythagoras med större kvadrater kräver mer beräkning än de enklaste fallen. |
| 3.131 | t, traningsniva | Träningsnivå 1 → 2: hela sidan måste bestämmas före likformighetsberäkningen. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.132 | spelIntro | Befintlig figur följer nu även med till Kunskapsgymmets delkort. |
| 3.137 | rättSvar, s | Facit hänvisar inte längre till tre mätningar när frågan bara anger två. |
| 3.145 | spelDelar, spelIntro | Del b får nödvändigt mellanresultat i frågan och kan lösas självständigt. Befintlig figur följer nu även med till Kunskapsgymmets delkort. |
| 3.148 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.150 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. Lika vinkelpar markeras med α och β som stöd för VV-beviset. |
| 3.151 | spelDelar, spelIntro | Del a höjs till nivå 2: tre sidkvoter måste jämföras. Befintlig figur följer nu även med till Kunskapsgymmets delkort. |
| 3.153 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. Lika vinkelpar markeras med α och β som stöd för VV-beviset. |
| 3.158 | niva, poang, traningsniva | Träningsnivå 3 → 2: kalibrerad mot den faktiska lösningen och jämförbara uppgifter. |
| 3.162 | rättSvar, s, t | Omöjlig given area 24 ersatt med 8; omräknad stor area 50, även i maskinfacit. |
| 3.163 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.164 | rättSvar, s, t | Omöjlig given area 20 ersatt med 6; omräknad stor area 37.5, även i maskinfacit. |
| 3.165 | t, traningsniva | Träningsnivå 1 → 2: hela sidan måste bestämmas före likformighetsberäkningen. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.167 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.170 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.175 | spelDelar, spelIntro, t | Del a höjs till nivå 2: två mittpunktsberäkningar med negativa koordinater. Befintlig figur följer nu även med till Kunskapsgymmets delkort. Koordinatfiguren har fått en tillgänglig beskrivning. |
| 3.176 | spelIntro | Befintlig figur följer nu även med till Kunskapsgymmets delkort. |
| 3.177 | spelDelar, spelIntro | Del b får nödvändigt mellanresultat i frågan och kan lösas självständigt. Befintlig figur följer nu även med till Kunskapsgymmets delkort. |
| 3.181 | spelDelar, spelIntro | Del b får nödvändigt mellanresultat i frågan och kan lösas självständigt. Befintlig figur följer nu även med till Kunskapsgymmets delkort. |
| 3.185 | t, traningsniva | Träningsnivå 1 → 2: hela sidan måste bestämmas före likformighetsberäkningen. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.186 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.205 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.220 | traningsniva | Träningsnivå 1 → 2: flera vinkelberäkningar eller likbenthet kombineras. |
| 3.221 | traningsniva | Träningsnivå 1 → 2: flera vinkelberäkningar eller likbenthet kombineras. |
| 3.222 | traningsniva | Träningsnivå 1 → 2: flera vinkelberäkningar eller likbenthet kombineras. |
| 3.223 | traningsniva | Träningsnivå 1 → 2: flera vinkelberäkningar eller likbenthet kombineras. |
| 3.227 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.239 | niva, poang, traningsniva | Träningsnivå 5 → 3: kalibrerad mot den faktiska lösningen och jämförbara uppgifter. |
| 3.240 | traningsniva | Träningsnivå 1 → 2: Pythagoras med större kvadrater kräver mer beräkning än de enklaste fallen. |
| 3.241 | traningsniva | Träningsnivå 1 → 2: Pythagoras måste ställas om för en okänd katet. |
| 3.242 | traningsniva | Träningsnivå 1 → 2: Pythagoras med större kvadrater kräver mer beräkning än de enklaste fallen. |
| 3.260 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.261 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.262 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.264 | traningsniva | Träningsnivå 1 → 2: koordinatskillnader ska först beräknas och sedan sättas in i avståndsformeln. |
| 3.267 | traningsniva | Träningsnivå 1 → 2: koordinatskillnader ska först beräknas och sedan sättas in i avståndsformeln. |
| 3.285 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.288 | traningsniva | Träningsnivå 1 → 2: både sidlängder och area ska räknas fram ur koordinater. |
| 3.297 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.298 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.311 | t, traningsniva | Träningsnivå 1 → 2: längdskalan måste först bestämmas och sedan användas. Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.313 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.315 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.319 | traningsniva | Träningsnivå 1 → 2: både sidlängder och area ska räknas fram ur koordinater. |
| 3.322 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.337 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.338 | t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. |
| 3.340 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.342 | traningsniva | Träningsnivå 1 → 2: koordinatskillnader ska först beräknas och sedan sättas in i avståndsformeln. |
| 3.349 | traningsniva | Träningsnivå 1 → 2: situationen ska först modelleras som en rätvinklig triangel. |
| 3.352 | traningsniva | Träningsnivå 1 → 2: flera vinkelberäkningar eller likbenthet kombineras. |
| 3.502 | niva, poang, traningsniva | Träningsnivå 5 → 3: kalibrerad mot den faktiska lösningen och jämförbara uppgifter. |
| 3.363 | traningsniva | Träningsnivå 1 → 2: två olika vinkelregler kombineras i samma uppgift. |
| 3.366 | traningsniva | Träningsnivå 1 → 2: två olika vinkelregler kombineras i samma uppgift. |
| 3.369 | traningsniva | Träningsnivå 1 → 2: två olika vinkelregler kombineras i samma uppgift. |
| 3.372 | traningsniva | Träningsnivå 1 → 2: två olika vinkelregler kombineras i samma uppgift. |
| 3.383 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.384 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.387 | traningsniva | Träningsnivå 2 → 1: ett direkt vinkel- eller längdsamband räcker. |
| 3.395 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.396 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.397 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.398 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.404 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.406 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.409 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.410 | s, spelDelar | Rättat felplacerade nämnarklamrar i proportioner, även i delkortens facit. |
| 3.417 | spelDelar | Del b får given randvinkel och nivå 1, i stället för att kräva hela del a igen. |
| 3.500 | niva, poang, traningsniva | Träningsnivå 5 → 3: kalibrerad mot den faktiska lösningen och jämförbara uppgifter. |
| 3.427 | s, spelDelar, t | Tillagt märkt SVG-figur; gemensam information följer även med till delkort. Specificerat rätvinkliga trianglar och bevisat motexemplet med olika hypotenusor. |
| 3.519 | traningsniva | Träningsnivå 1 → 2: satsen måste omsättas i en proportion eller ekvation som sedan löses. |
| 3.503 | s, t | Korrigerat vilka ytor som ger den kortaste vägen; sträckan genom luften ingår inte i frågans färdväg. |
| 3.512 | rättSvar, tolerans | Maskinsvaret är 213 kr, samma heltalsavrundning som frågan och facit. |
