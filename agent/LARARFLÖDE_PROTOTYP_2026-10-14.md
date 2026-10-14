# Prototyp för undervisning och egen träning – 2026-10-14

Användaren begärde först en prototyp att granska före push. Efter ändringen med ”Träna själv” bredvid ”Skapa min första grupp” godkände användaren push 2026-10-14. Denna fil beskriver den fristående prototypen; se [produktionsimplementationen](LARARFLÖDE_IMPLEMENTATION_2026-10-14.md) för aktuellt läge.

Fristående, klickbar prototyp: konsument `prototyper/larare-elev.html`. Se `prototyper/README.md` för flöden, avgränsning och verifiering.

Visar:
- Lärarens tydligt separata lägen **Min undervisning** och **Träna själv**.
- Undervisningsgrupp med kurs, gemensam översikt, träningspass, elever och statistik.
- Förstagångsflöde grupp → kurs → elevimport → träningspass.
- Elev med tilldelade pass respektive utan pass; egen träning alltid direkt tillgänglig.
- Klass och grupp som separata begrepp; exempelimport bevarar klass/andra medlemskap.
- Befintliga medlemmar ibockade, sökning med bibehållna val och deduplicering av pass/mottagare.

Fyra exempelroller kan väljas i en prototypmeny. Alla personer/resultat är exempeldata. Exempeluppgifter går att besvara, men hela banken och produktionsstatistiken är inte inkopplade. När prototypen togs fram var `index.html`, SQL och uppgiftsbanker oförändrade. Kollegainbjudan/arkivering och fullständig backend återstår till godkänd implementation; den tidigare valfria grupp–topplistekopplingen är inte borttagen från produktionen av denna prototyp.

Kontrollerat med Chromium: 12 startlayouter, separata lärarlägen/egen träning, kurstillhörighet, skapande och import, befintliga medlemskap, unika mottagare/pass, elevens start med/utan pass och smala grupp-/modalvyer. Inga externa nätverksanrop. Testfil: konsument `tools/larare-arbetsflode-prototyp.browser.py`.

Godkännande mottaget: ”kanon, pusha”. Den tidigare pushspärren är därmed hävd. Produktionen använder riktiga grupper och pass; den fristående prototypen behålls som designreferens.
