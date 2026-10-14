# Mina grupper, klassimport och klassval – 2026-10-14

Fortsättning och ändring av användarbeslutet i `LARARKLASSER_2026-10-14.md`/KG02. Undervisningsgrupper ska heta **Mina grupper**, inte Mina klasser. En elev har en klass, men kan ha flera undervisningsgrupper och olika lärare per ämne. Ingen bank eller verktygsmetadata ändras.

## Åtgärder

- Startsidan, lärarfliken, skapandeformuläret, träningspassets gruppval och statistiken använder gruppnamn. Gruppen kan exempelvis heta ”Matematik NA26a + NA26b”. Befintliga grupp-ID:n och medlemskap behålls.
- Elevlistan har **Välj elever från en klass**. Klassval markerar alla tillgängliga elever i klassen som inte redan ingår i gruppen. Fler klassval lägger till fler markeringar, utan att kasta tidigare val. Läraren kan justera enskilda kryss och klicka **Lägg till valda elever**. Ingen skrivning sker vid enbart klassval.
- Befintliga medlemmar visas **ibockade**, utan texten ”Redan i gruppen”. Deras kryss är låsta: importvyn lägger till nya elever och ska inte oavsiktligt ta bort befintliga medlemskap. Borttagning finns i den befintliga elevvyn. Räknaren visar **nya elever valda**, och bara nya ID:n skickas vid sparandet.
- Klassimport väljer tilläggsläget och nollställer ett tidigare flyttval. Övriga undervisningsgrupper bevaras. En vanlig, okopplad grupp påverkar inte elevens klass. Den befintliga uttryckliga kopplingen ”Klass på topplistan” behåller sin tidigare triggerfunktion; om läraren har valt en sådan koppling flyttas nya gruppmedlemmar även till den topplisteklassen. Detta visas i elevvalsvyn. Ingen koppling skapas automatiskt av importen.
- Elever utan klass får den obligatoriska klassrutan vid varje inloggning/sidstart, även om nyhetsrutan redan är läst. Den saknar stängknapp och stängs efter lyckat klassval/klassskapande. Lärarprofil/godkänd roll verifieras före uppmaningen; lärare/admin undantas. Väntande uppmaningar är bundna till användar-ID och väntar tills annan onboarding är klar. Lärarklassen filtreras bort från elevens obligatoriska klasslista.

## Klassimportens omfattning

Den nya rosterfunktionen returnerar varje tillgänglig elevs aktuella `kg_klass` från `klassmedlem`. Klassalternativen byggs från samma behörighetsbegränsade elevlista, aldrig en global elevförteckning. En lärare kan välja elever från sin registrerade skola eller egna befintliga grupper. Elever utan skoluppgift som inte redan ingår i egna grupper går fortsatt med via gruppkod/länk. Klassimport kopierar de registrerade elever som är tillgängliga vid importtillfället; framtida klassmedlemmar läggs inte automatiskt till.

## SQL som behöver köras

**Kunskapsgymmet `sql/2026-10-14-grupper-klassimport.sql`** innehåller hela tidigare elevval-migrationen plus klassuppgift/kapacitetsflagga i svaret. Kör hela denna fil, även om `2026-10-14-larare-elevval.sql` redan är körd. Den är idempotent och kräver de befintliga grupp-/skolmigrationerna från 2026-10-03–06. Den äldre filen bevaras för historiken; använd den nya för aktivering.

Om nya SQL-filen ännu inte körts fungerar befintligt elevval fortsatt. Klassimporten visas inaktiverad med information om aktivering. Klassrutan vid inloggning använder befintliga klass-RPC:er och behöver ingen ny migrationsfunktion.

## Verifiering

- **39 PostgreSQL/PGlite-kontroller** i `kunskapsgymmet/tools/larare-elevval.integration.js`: uppgradering från tidigare migration, nya migrationen två gånger, skol-/gruppbehörighet, klassmetadata utan andra skolors elevuppgifter, tillägg till okopplad grupp med bibehållen klass/källgrupp, atomiska avslag, flytt, dubbla ID:n och befintlig uttrycklig toppliste-trigger.
- `kunskapsgymmet/tools/larare-elevval.browser.py`: 10 startsideslayouter (ljus/mörk, 320–1280 px), tre rosterlayouter, gruppnamn/skapande/statistik, ibockade befintliga medlemmar, två klassval, upprepat klassval utan dubletter, justerat urval, klassimport som nollställer flyttläge och skickar enbart nya elever. Kontrollerar obligatorisk klassruta trots redan läst nyhet, sparat klassval som stoppar uppmaningen, ny uppmaning vid senare inloggning utan klass, Escape utan stängning och undantag för registrerad/godkänd lärare och utloggad.
- Tidigare regressioner för adminroller, närvaro/statistik, träningspassens talformat och verktygspolicy samt syntax/diffkontroll.

Ingen produktions-SQL eller elevförflyttning har utförts i molnmiljön. Push aktiverar inte Supabase-migrationen.

Kommentar till önskemålet: ”Vyn heter nu Mina grupper. Välj en eller flera klasser för att markera eleverna och lägg till dem i en undervisningsgrupp. Befintliga medlemmar är ibockade. Elever utan klass uppmanas att välja vid varje inloggning.”
