# Kunskapsgymmet – önskemål utanför uppgifter

Datum: 2026-10-13. Funktionsönskemål inkom via matf1 #1.622: eleven vill kunna skicka önskemål och rapportera allmänna problem utan att öppna en uppgift. Användaren godkänner en funktion liknande Uppgiftslabbets ”Skicka in önskemål”.

## Genomförd ändring

Alla inloggade användare får **Skicka in önskemål** och **Mina önskemål** i kontomenyn. Formuläret finns även på kursvalssidan och kräver inte ett uppgifts-ID eller vald kurs. Tre kategorier: fler uppgifter, förslag på förbättring och problem med appen. Fler uppgifter kräver kurs, område och träningsnivå; förslag/problem kan skickas utan kurs. Beskrivning krävs. Formuläret har tydlig bekräftelse först efter lyckat serversvar, behåller texten vid fel och kan användas med tangentbord.

Admin får **Inskickade önskemål** i menyn och fliken **Önskemål** i adminvyn. Listan filtreras på Öppen, Pågår, Åtgärdad, Avslutad eller Alla. Status och valfri kommentar sparas direkt i kortet. Kommentarer får vara tomma. Utkast till kommentarer överlever byte av filter. Loggen kan kopieras; om urklipp inte är tillgängligt laddas en textfil ned. En användare ser status och eventuell sparad kommentar under Mina önskemål.

Backend lagrar inskick separat från uppgiftsfel, profil och XP. `kg_private.onskemal` saknar direkt läs-/skrivbehörighet för elever/lärare. SECURITY DEFINER-funktioner använder tom search_path, `auth.uid()` och befintlig `kg_ar_admin()` för behörighet. Användare får endast sina egna inskick. Admin får hela listan och kan granska. Loggfunktionerna visar högst de senaste 1000 inskicken. Idempotent request-ID motverkar dubbla inskick efter nätverksfel; max 20 nya inskick per timme och användare begränsar oavsiktlig upprepning. Kontobyte rensar önskemålsdata, utkast, formulär och adminmodaler direkt.

## Aktivering i Supabase

**SQL har inte körts i produktionsdatabasen.** Molnsessionen har ingen ansluten databasadministration. Kör hela `kunskapsgymmet/sql/2026-10-13-onskemal.sql` i Kunskapsgymmets Supabase SQL Editor. Filen kräver befintlig `auth.users` och `public.kg_ar_admin()`, körs i en transaktion och kan köras igen. Den avslutar med schema-refresh för PostgREST.

Frontend kan pushas separat men inskick kan inte sparas före aktiveringen. Ett saknat backend ger ett felmeddelande, aldrig en falsk bekräftelse. Efter installationen: skicka ett test från ett elevkonto utan vald kurs, kontrollera adminlistan och spara status utan kommentar samt med kommentar. Detta kräver de faktiska kontona och har inte genomförts i produktion.

## Kontroller

- **150 Node-tester passerar**, inklusive sex nya tester för utloggning, kontobyte före anrop, svar från gammalt konto, sparfel, adminavgränsning och loggtext.
- **39 lokala PostgreSQL-kontroller** med PGlite. Riktiga roller `anon`/`authenticated` används. Elev och vanlig lärare nekas global läsning/granskning och direkt tabellåtkomst. Egna listor, null/tom/blank kommentar, textgränser, ogiltiga värden, rate limit och dubblettskydd kontrolleras. Migrationen körs tre gånger och bevarar data.
- **Webbläsarprov med lokala RPC-svar:** konto-/kursval utan uppgift, tomt inskick, fler uppgifter med nivå 1, allmänt problem utan kurs, serverfel, nytt försök, Mina önskemål, inlinegranskning, tom kommentar, sparad återkoppling, utkast, filtrering, urklipp och kontobyte.
- **Åtta layoutkontroller**: formulär i ljust/mörkt tema vid 360/390/1280 pixlar och adminlista vid 390/1280. Inga upptäckta JavaScript-fel eller överflöden i de ändrade vyerna. Skärmbilder granskade visuellt.
- Syntax och diffkontroll passerar. Browserprovet blockerar andra Supabase-anrop; inga produktionskonton, elevresultat, kommentarer eller önskemål har skrivits av testen.

Reproduktion i konsumenten:

```bash
node --test tools/*.test.js
node tools/onskemal.integration.js /sökväg/till/@electric-sql/pglite
python tools/onskemal.browser.py
```

Browserprovet kräver Playwright, Chromium och lokal server på port 8083.

## Rapportlista och kommentarsförslag

**Granskad rapport:** matf1 #1.622, funktionsönskemålet om fristående inskick. Rapporten gäller appen; matematik, facit och nivå på #1.622 har inte granskats i denna omgång.

**Åtgärd:** frontend, databasfunktioner, migration och tester är färdiga. Aktivering i produktions-Supabase återstår. Inga uppgiftsbanker har ändrats.

**Granskad – inget fel, uppgifter:** tom lista; ingen uppgift har genomgått en sakgranskning här.

**Kommentar efter aktivering:** ”Nu kan du välja Skicka in önskemål i kontomenyn, även utan att öppna en uppgift. Där kan du lämna förslag eller beskriva problem med appen. Under Mina önskemål kan du följa status och läsa eventuell återkoppling.”

Ingen rapportstatus har ändrats och ingen kommentar har skickats i appen.

## Beständiga filer

Konsument: `index.html`, `onskemal.js`, `sql/2026-10-13-onskemal.sql`, `tools/onskemal.test.js`, `tools/onskemal.integration.js`, `tools/onskemal.browser.py`. Master: denna logg och registerpost KG01. Utgångspunkt: Uppgiftslabbet fa44447, Kunskapsgymmet f8ca529. Befintlig ospårad `tools/__pycache__/` lämnas utanför commit. Ingen banksynkronisering behövs.
