# GeoGebra i statistikuppgifter 2026-10-14

45 läraruppgifter granskade och uppdaterade. Tio tillät redan GeoGebra, men alla 45 har nu konsekvent verktygspolicy och rätt metadata för varje delkort. Samtliga nya Sx-värden från FP44 bevaras.

## Vad eleven kan använda

Hela läraruppgiften tillåter GeoGebra. Kort där eleven beräknar Sx tillåter GeoGebra och spärrar Kunskapsgymmets vanliga miniräknare, som saknar statistikfunktion. Övriga delar behåller sin tidigare miniräknare. Delkortens uttryckliga verktygsmetadata har företräde framför förälderns; detta gällde tidigare inte geogebra/miniräknare och är nu korrigerat. Fysikens regel om alltid tillåten miniräknare ändras inte.

En GeoGebra-knapp i verktygsraden öppnar https://www.geogebra.org/classic?lang=sv i en ny flik, med noopener/noreferrer. Den pågående uppgiften ligger kvar. Ingen GeoGebra-app, iframe eller programkod bäddas in. Frågor och ledtrådar hänvisar nu till GeoGebra i stället för miniräknaren där det behövs.

## Licens och användarens beslut

Officiella källor kontrollerade 2026-10-14:

- [GeoGebra License och License FAQ](https://www.geogebra.org/license). Icke-kommersiell undervisning är tillåten enligt deras icke-kommersiella licens. ”Any use of GeoGebra for a commercial purpose is subject to and requires a special license.” Kommersiellt syfte avgörs av användningen, inte bara av om tjänsten är gratis.
- [GeoGebra Apps Embedding](https://geogebra.github.io/docs/reference/en/GeoGebra_Apps_Embedding/). Teknisk inbäddning är officiellt stödd. Det tekniska stödet upphäver inte licensvillkoren.

Användaren svarade att Kunskapsgymmet är kostnadsfritt nu men kan skalas upp senare. Därför väljs extern länk nu. För framtida kommersiell inbäddning behöver ett avtal med GeoGebra vara klart. Länken är inte en utfästelse om att alla framtida kommersiella användningar är licensfria. Ingen kontakt har skickats till GeoGebra.

## Kontrollresultat

- 51 relevanta mastertester och 150 konsumenttester godkända.
- 260 verkliga kortvisningar på 390 och 1280 px. Varje kort har rätt verktygsknapp och tillstånd.
- Extern länk, ny flik utan window.opener, bibehållen uppgift, spärrad redan öppen miniräknare på Sx-kort och fortsatt korrekt rättning av 3,8 i #4.28 verifierade.
- Ett explicit false på ett delkort överstyr true hos föräldern; arv utan explicit värde fungerar.
- Inga JavaScript-/KaTeX-fel eller sidöverflöden. Mobilverktygsraden kontrollerad visuellt.
- Full bankvalidator: Ma2 260→260 fynd, inga nya. Facit, maskinsvar, toleranser, svarsenheter, nivåer och figurer bevaras.
- Bankkopiorna var identiska före och efter synk. Inga Supabase-statusar, elevkommentarer eller XP ändras av dessa kontroller.

## Alla granskade och åtgärdade uppgifter

| Kurs | ID | Utfall | Standardavvikelsedelar med GeoGebra | Kommentarsförslag |
|---|---|---|---|---|
| ma2 | 4.05 | Åtgärdad – verktyg | b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.10 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.28 | Åtgärdad – verktyg | b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.46 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.97 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.157 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.241 | Åtgärdad – verktyg | b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.283 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.284 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.299 | Åtgärdad – verktyg | b, c, d | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.302 | Åtgärdad – verktyg | a, b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.306 | Åtgärdad – verktyg | a | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.328 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.329 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.330 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.331 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.332 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.333 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.334 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.335 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.336 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.337 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.338 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.339 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.340 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.341 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.342 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.343 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.344 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.345 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.346 | Åtgärdad – verktyg | a, b, c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.347 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.348 | Åtgärdad – verktyg | a, b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.349 | Åtgärdad – verktyg | a, b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.350 | Åtgärdad – verktyg | a, b, c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.351 | Åtgärdad – verktyg | a | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.364 | Åtgärdad – verktyg | c | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.365 | Åtgärdad – verktyg | a | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.366 | Åtgärdad – verktyg | a | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.371 | Åtgärdad – verktyg | a, b | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 4.373 | Åtgärdad – verktyg | a | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 5.66 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 5.71 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 5.94 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |
| ma2 | 5.110 | Åtgärdad – verktyg | Hela uppgiften | GeoGebra är nu tillåtet och kan öppnas från uppgiften. Standardavvikelseberäkningen använder Sx i GeoGebra; facit och självrättning är oförändrade. |

Alla 45 får ändringar; ingen av dessa lämnas i kategorin granskad – inget fel. Ingen rapportstatus eller elevkommentar har skickats till Supabase.
