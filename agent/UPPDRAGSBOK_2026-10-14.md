# Uppdragsbok och begränsad pergamenthöjd – 2026-10-14

Användaren korrigerade KG05: en utfälld uppdragslista får **inte öka tränarkortets höjd**, och pergamentutseendet ska finnas kvar. Därefter begärdes en boksymbol med bläddring genom veckan och möjlighet att slutföra gårdagens uppdrag. Det slutliga XP-beslutet är **halva original-XP för äldre uppdrag**; detta ersätter både det först föreslagna noll-XP-valet och felskrivningen om hela XP. Dagens uppdrag behåller full belöning.

## Gränssnitt

Kunskapsgymmets `index.html` visar hopfällt pergament med boksymbol, rubrik, faktiskt antal klara uppdrag och pil. Papprets guldton och rullar följer temat. Utfälld lista har egen vertikal scroll och tangentbordsåtkomst. På datorn begränsas den av höjden bredvid tränarens text och knappar; `ResizeObserver` följer även skrivanimation och skärmändringar. På mobil öppnas den som en liten överliggande rulle, högst 190 px, så tränarkortet och områdena inte flyttas. Rullen ligger över efterföljande fokus-/områdestext så länkarna kan klickas. Minskad rörelse respekteras och gamla höjdobservatörer kopplas bort vid omritning.

Dagpilar bläddrar genom **de senaste sju kalenderdagarna**. Inga framtida uppdrag visas. Man kan gå direkt tillbaka till idag. Datumknapparna ligger kvar i scrollens överkant. Kontobundet öppningsval från KG05 bevaras; dagval är separat lokal vydata per konto/kurs.

## Historik och träning

`profile.uppdragsVecka` sparar riktiga uppsättningar per dag/kurs. Den tidigare uppsättningen räddas innan den ersätts vid datumbyte, och dagens post återkopplas till `profile.uppdrag` efter JSON-inläsning. Äldre dagar än veckofönstret rensas. Uppdrag från dagar som aldrig sparats fabriceras inte: tomma dagar märks tydligt. Historiken byggs framåt från uppdateringen; den tidigare profilens senaste dag kan räddas, men en hel gammal vecka kan inte återskapas om den redan skrivits över.

Historiska uppdrag startar träning utifrån typ/område/nivå/familj, utan `eval` av sparad kod. Alla oavslutade uppdrag har en startknapp. Äldre felreparation kräver att fel finns att repetera; borttagna områden ger besked utan att lämna ett gammalt passval kvar. Vald dag/ägare/kurs följer med träningspasset, återupptagning och ”fortsätt pass”. Ett nytt normalt pass rensar valet. Bara **den aktivt valda äldre dagen** får historisk progress; normal träning ska inte automatiskt klara en hel veckas gamla uppdrag. Tidigare frågor med `noXp` ger ingen ny progress/belöning. Dagens normala uppdrag kan samtidigt räknas enligt sina tidigare villkor.

## Halva XP, en gång

- Vanligt äldre uppdrag: **25 XP**.
- Äldre huvuduppdrag: **50 XP**.
- Alla äldre uppdrag i en kurs/dag klara: **50 XP** extra.
- En full gammal fyrgrupp ger totalt **175 XP**. Dagens motsvarighet ger fortsatt 350 XP.

`betald` per uppdrag och `bonusBetald` per kurs/dag hindrar lokal dubbelbelöning. Redan klara äldre uppdrag markeras som betalda vid migration från det tidigare profilformatet; de får inte betalas igen. `profile.uppdragRetroXp` bokför sammanlagda historiska XP separat. De befintliga räknarna för dagens uppdrag/uppdragsmedaljer ökas inte av äldre uppdrag; deras tidigare serverregler består. Vanliga uppgiftssvar ger XP enligt ordinarie regler.

## Supabase: separat aktivering

Kör konsumentens **`sql/2026-10-14-uppdragsbok.sql`** i Supabase SQL Editor. Kräver befintlig profilmigration och uppdrags-/topplistemedalj-/fyra-uppdrag-migrationerna 2026-10-01. Scriptet kan köras igen utan att betalningar raderas. Git-push kör inte SQL. Ingen produktionsdatabas har lästs eller ändrats i denna molnomgång.

Migrationen behåller profilerpc:ns revisioner, radlås, konfliktåterhämtning, kreditgräns, minskningskontroller samt felrapports- och passbonus. Den lägger till:

- Privat betalningsbok med unik nyckel **konto + datum + kurs + uppdragsindex**; index 4 reserveras för hela-dagen-bonus. Ingen direkt åtkomst för elever/anon.
- Privat verifierare för sparade äldre uppsättningar. Äldre datum/kurs måste redan finnas i serverns profil eller dess tidigare aktuella uppsättning. Antal och definitioner är oföränderliga. Progress får inte öka mer än nya rätta svar, och ny betalning kräver nya rätta svar. Betald/klar status får inte backas för att återkräva belöning.
- Exakt kontroll att det extra XP-fältets ökning motsvarar de halvbelöningar som faktiskt kan bokföras. Profil, XP, betalningsposter och publicering sker i samma transaktion.
- Betalningsverifieringen skyddar mot påhittade gamla dagar, ändrade mål, dubbelbelöning och extra XP utan rätta svar. Den verifierar inte själva matte-/fysiksvaret på servern; klienten självrättar som tidigare.
- Profilens läs-/sparsvaret anger `uppdragsbok:true`. Inloggad klient aktiverar historisk träning först när den flaggan mottagits, så den inte skickar nya XP till äldre SQL. Innan aktivering går boken att läsa och dagens uppdrag fungerar. Lokal gästträning kan använda bokfunktionen direkt.
- Topplistans automatiska spärr lägger till **bara verifierade, bokförda äldre belöningar från idag** i dagens XP-marginal. Den allmänna marginalen höjs inte för alla konton.

SQL-variabler får inte ha samma obestämda namn som tabellkolumner. Den verifierade funktionen använder exempelvis `v_dag`, inte `dag`, vid jämförelse med `l.dag`; det hindrar ett nytt 42702-fel. Blanda inte in generell extra XP i `profile_error` utan motsvarande serverkontroll av faktisk betalning.

## Verifiering

Konsument:

- `tools/uppdragsbok.test.js`: fem tester för datumbyte/arkiv, redan betalda mål, halva XP exakt en gång, konton/kurs/datum/noXp/aktiveringsgräns, nivå/familj/ledtråd/reparation och serier.
- `tools/uppdragsbok.integration.js`: 42 kontroller med lokal PGlite och verkliga nya profil-/betalningsfunktioner. Profilarkivering, halvbelöning, fem unika betalningar, samma/stale revision, falska mål/XP/kurser, borttagna betalningsflaggor, gamla datum, rätta-svar-krav, gamla redan klara uppdrag, dagens fulla bonus och tak, spärr med/utan verifierad historisk XP, upprepad migration och grants/anonspärr.
- `tools/uppdragsbok.browser.py`: verkliga appen med lokala fixture-profiler, tolv kombinationer av tema/bredd/öppen/stängd, **oförändrad tränarkortshöjd**, egen scroll, pergament, klick/tangentbord, datumgränser och tom historik, historiskt träningspass, fortsatt/återupptaget pass, halv XP en gång, normalt nytt pass, SQL-flagga och omladdad historik/öppningspreferens.
- Tidigare admin-, statistik-, svarsformat-, verktygs- och passhistorikskydd behålls. JavaScript-syntax och diffkontroll.

Ingen uppgiftsbank är ändrad. Skärmbilder från lokal verifiering finns under `/tmp/quest-book-*.png`, utan produktionsdata.
