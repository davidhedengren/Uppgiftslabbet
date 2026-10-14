# Lärarstart och Mina klasser – 2026-10-14

Användaren prioriterade detta före fortsatt verktygsgenomgång. Ingen uppgift eller bankmetadata ändras i denna leverans.

## Åtgärdat

- Kunskapsgymmets startsida visar ett lärarkort ovanför användar-/uppgiftsantalet: **Skapa träningspass till eleverna** öppnar skapandet direkt; **Mina klasser** öppnar klasslistan. Visas för registrerade/godkända lärare och uppdateras även när rollen hämtas efter sidrendering. Elever och utloggade får inte kortet.
- Klasslistan har ett namnfält och **Skapa klass**. Dubbelklick skapar inte flera klasser medan anropet pågår. Befintliga undervisningsgrupper återanvänds; ingen data migreras eller slås ihop.
- I klassen finns **Lägg till / flytta elever**, med sökbar namnlista, kryssrutor, antal valda och markering för befintliga medlemmar. Val finns kvar när listan filtreras och efter sparfel. Kontroller spärras under sparandet.
- Standard är att lägga till elever och behålla andra grupper. **Flytta från [klass]** tar bara bort det valda källmedlemskapet och lägger till målet. Alla valda måste tillhöra källklassen; inga delvisa flyttar görs. Andra lärares grupper tas inte bort.
- Klassens statistik visas i elevlistans nyckeltal, på elevnivå och i den tydligt namngivna fliken **Klassens statistik per område**. Globala adminvyer får inga nya lärarbehörigheter.

## Behörighet och datamodell

`kg_grupp` är lärarens undervisningsklass/grupp. Eleven kan ingå i flera ämnesgrupper. `kg_klass` är separat topplisteklass, med ett medlemskap per elev. Dessa får inte sammanblandas vid en senare revidering.

Nya RPC:er `kg_lar_elevlista` och `kg_lar_elever_lagg_till` kontrollerar inloggning, lärarroll och tillgång till målgrupp. Vid flytt kontrolleras även källgruppen. Elevval begränsas till elever med samma registrerade skola som läraren eller elever som redan är med i lärarens egna grupper. Lärare/admin räknas inte som valbara elever. Elevlistan lämnar endast namn, ID, egna gruppnamn och medlemsmarkering, utan e-post eller global aktivitetsstatistik.

Elever som saknar skoluppgift och inte finns i lärarens grupper använder fortsatt klasskod/länk. Läraren kan ändra sin skolprofil från elevvalsvyn. Skolans namn räcker inte för att visa elever vid klienten; servern gör samma kontroll vid varje skrivning. Ett ogiltigt elevval stoppar hela operationen. Källmedlemskap låses under en flytt; mängden avdupliceras och begränsas till högst 500 val per anrop.

Befintlig grupp–klass-trigger gäller även lärartillagda elever: om målgruppen är kopplad till en topplisteklass flyttas eleven dit vid nytt gruppmedlemskap. Detta förklaras i elevvalsvyn. Övriga undervisningsgrupper lämnas kvar. Ingen historisk träningsdata eller XP ändras.

## Aktivering

Kör hela **Kunskapsgymmet `sql/2026-10-14-larare-elevval.sql`** i Supabase SQL Editor efter de befintliga lärargrupps-/skolmigrationerna från 2026-10-03–06. Filen är idempotent. Git-push kör inte SQL. Ingen produktionsdatabas har ändrats i molnmiljön.

## Kontrollerat utan ändring

Befintliga klass-/elevstatistik-RPC:er, träningspassens skapande och utdelning, kod/länkanslutning, kollegadelning, topplisteklassmodellen och adminstatistik återanvänds. Verktygspolicyn och alla bankfiler bevaras.

## Verifiering

- `kunskapsgymmet/tools/larare-elevval.integration.js`: 32 kontroller i lokal PostgreSQL/PGlite, migration körd två gånger. Nekar anonym, elev och annan lärare; annan skola, lärarkonto, obehörig källa och ofullständiga flyttval. Kontrollerar atomiskt avslag, dubbla ID:n, idempotent tillägg, bibehållna andra grupper och den verkliga befintliga toppliste-triggern. Kontrollerar RPC-privilegier och avstängd fixture-lärarprofil.
- `kunskapsgymmet/tools/larare-elevval.browser.py`: verklig Chromium med lokala RPC-fixtures, 10 startsideslayouter i ljust/mörkt läge (320–1280 px), knappar ovanför statistiken, direkt träningspassformulär, klassskapande, klassstatistik, sökning, bibehållna val, sparfel/nytt försök, tillägg/flytt, tangentbordsval och tre elevlistelayouter utan horisontellt överflöde. Elev/utloggad ser inga lärarknappar; senare rollhämtning visar dem. Ingen global adminstatistik efterfrågas.
- Befintliga regressioner för adminroll, onlinenärvaro, adminstatistik, träningspassens talformat och verktygspolicy körda.
- JavaScript-syntax och `git diff --check`.

Testerna använder lokala konton och svar. Ingen aktiverad produktionsmigration eller verkligt skolregister har kunnat verifieras här.

Kommentar till önskemålet: ”Lärare har nu knappar för träningspass och Mina klasser på startsidan. I klasserna går det att välja elever från skolans elevlista, flytta dem mellan egna klasser och följa klassens statistik.”
