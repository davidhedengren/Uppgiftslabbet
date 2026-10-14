# Godkänt lärar- och elevflöde – 2026-10-14

Användaren granskade den klickbara prototypen, bad att hjälpsentensen om att växla högst upp skulle tas bort och att **Träna själv** skulle ligga bredvid **Skapa min första grupp**. Därefter gavs uttryckligt pushmedgivande: ”kanon, pusha”.

## Ändrat i Kunskapsgymmet

- Lärarens standardstart är **Min undervisning**. **Träna själv** öppnar den riktiga kursväljaren och den befintliga träningen. Läget är kontobundet i flikens sessionslagring, med minnesreserv om lagringen är blockerad. Bakåt/framåt återställer läget. XP visas i egen träning; resultat och träningsprofil ändras inte av lägesväxlingen.
- Första besöket visar **Välkommen till din undervisning**, med de två önskade knapparna bredvid varandra. Gruppformuläret öppnas först när det behövs. Det borttagna hjälputtrycket ska inte återinföras.
- Mina grupper visar riktiga grupper. Varje grupp har **Översikt**, **Träningspass**, **Elever** och **Gruppens statistik per område**. Gruppinställningar är hopfällda. Kod och elevimport går att nå direkt.
- Översikten visar elevantal, aktiva elever och antal uppgifter under senaste veckan, samt gruppens aktiva pass. Aktivitetssiffrorna gäller alla elevens kurser och märks uttryckligen så; statistik per område låter läraren välja kurs. Ett misslyckat anrop visas som okänt/fel med nytt försök, aldrig som noll elever/pass.
- Gruppens passlista filtrerar de befintliga, behöriga passen till vald grupp. Samma pass finns fortfarande som ett enda objekt när det delas med flera grupper. Klick på översiktskort öppnar rätt pass/resultat. Den samlade passfliken finns kvar för lärarens samtliga pass.
- En grupp kan få en kurs som sparas i databasen. Den förväljs i passformuläret och områdesstatistiken. Äldre grupper utan kurs fortsätter fungera och kan få kurs via gruppinställningarna. Ett kursbyte ändrar inte tidigare pass eller elevresultat.
- Sparandet av träningspass spärrar dubbelklick och kontroller under anropet. Fel låter läraren försöka igen med samma val. Ett sent svar får inte skriva i ett annat konto eller ett nytt formulär.
- Inloggade elever har en kort start med sina tilldelade pass överst och egen kursväljare direkt under. Utan pass visas kursval utan blockerande tomt passflöde. Listan dedupliceras på pass-ID och sena svar från tidigare konto kastas. Publika totalsiffror finns på den utloggade startsidan.
- Grupp-/pass-/kursdata och importer fortsätter använda den befintliga behörighetsmodellen. Ingen global adminstatistik läses av lärarvyn. Ingen ny parallell grupp-, klass- eller resultatmodell införs.

## Databas och aktivering

Konsumentens **`sql/2026-10-14-gruppkurs.sql`** körs separat i Supabase SQL Editor. Push kör inte migrationen. Kräver de befintliga grupp-/skol-/klassmigrationerna 2026-10-03–06. Scriptet kan köras flera gånger och lägger till:

- `kg_grupp.kurs`, initialt null för äldre grupper.
- `kg_lar_grupp_skapa_kurs(p_namn,p_kurs)`: validerar kurs och anropar den befintliga gruppskapandefunktionen med dess namn-/roll-/frekvenskontroller. Grupp och kurs sparas i samma transaktion.
- `kg_lar_grupp_kurs(p_grupp,p_kurs)`: endast aktiv lärare med tillgång till gruppen kan ändra/tömma kurs.
- `kg_lar_grupper()` returnerar kurs och `kursstod:true`, med samma medlems- och behörighetsfilter som tidigare.

Klienten fungerar utan den nya SQL-filen: gruppskapande med namn och övriga flöden finns kvar, men kursvalet erbjuds först när servern uttryckligen anger stöd. Den låtsas inte spara kurs i lokal lagring. Klassimport kräver fortsatt `sql/2026-10-14-grupper-klassimport.sql` från KG03.

**Klass och grupp:** ingen automatisk klasskoppling införs. En gammal, uttrycklig koppling till topplisteklass behåller sin befintliga trigger. Importvyn informerar fortfarande om den effekten. Elevens klass och övriga gruppmedlemskap får inte massändras i samband med designbytet. Prototypens fristående modell ska inte användas som en datamigration.

Ingen produktions-Supabase har ändrats eller verifierats från molnmiljön. Lokal PostgreSQL och webbläsare använder enbart fixture-konton. Bankfiler är oförändrade. Arkivering/automatisk synk av klassmedlemmar och nya statistikmått ingår inte; befintlig kollegainbjudan, explicit klassimport, namnbyte och borttagning återanvänds.

## Verifiering

Konsument:

- `tools/gruppkurs.integration.js`: 38 kontroller i PGlite med den faktiska migrationen och den ursprungliga gruppskapandefunktionen. Anonym/elev/annan lärare nekas; delad lärare tillåts, avaktiverad lärare nekas. Kursvalidering, tom kurs, atomiskt skapande, upprepad migration och bibehållen klass/medlemskap kontrolleras. RPC-grants kontrolleras.
- `tools/larare-elevval.integration.js`: 39 kontroller, fortsatt skydd för skolgränser, import, idempotens, atomisk flytt och tidigare klass-trigger.
- `tools/larare-elevval.browser.py`: riktiga appen, tio lärarlayouter i ljust/mörkt tema, egen träning, skapande, statistik, tangentbordsval, bibehållna kryss/sparfel, klassimport/flytt samt återkommande elevklassval. Tidigare hemknappsförväntningar har ersatts av de godkända lägena, övriga funktionskontroller består.
- `tools/larare-arbetsflode.browser.py`: riktiga `index.html`, lägesväxling utan profiländring, webbläsarhistorik, verklig kursöppning, kurs/defaults/sparfel, gruppfiltrerade pass och resultat, dubbla spartryck, första besöket, äldre SQL, unik elevpasslista, tom elevstart, sen kontorespons och tolv responsiva layouter. Figurer/skärmbilder kontrolleras lokalt på mobil och dator.
- Prototypens befintliga browser-test behålls som designreferens.
- Regressioner: `admin-elevroll.test.js`, `admin-online.test.js`, `admin-statistik.test.js`, `prov-talformat.test.js`, `verktygspolicy-2026-10-14.test.js`. Sammanlagt 29 godkända tester.
- JavaScript-syntax och `git diff --check`.

PGlite körs med paketet i `/tmp/kg-admin-stat-tests/node_modules/@electric-sql/pglite` som testscriptets argument. Browser-testerna använder lokal webbserver på port 8083 och Chromium, utan produktionsanrop.
