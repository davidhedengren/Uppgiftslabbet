# Kursfilter, sökning och sortering av dokument

Datum: 2026-10-12. Gäller Uppgiftslabbet, Mina prov och övningsblad samt Gemensamma banken.

## Ändringar

- Kursväljaren visar kurser som faktiskt finns i aktuell dokumentlista. En kurs kan väljas med alla spår eller med ett specifikt spår, exempelvis Ma2c.
- Sortering: senast ändrad (standard), kurs A–Ö eller namn A–Ö. Svenska tecken och tal i namn sorteras naturligt, exempelvis Prov 2 före Prov 10. Prov och övningsblad behåller sina separata kolumner.
- Sökningen kombineras med kursfiltret. Alla sökord ska finnas i dokumentets namn, kurs/spår, områden eller ägarens/avsändarens namn. För Ma1/Ma2 fungerar även förkortningar som ma2c.
- Antal träffar visas, exempelvis ”Visar 2 av 5 dokument”. Tomma filterresultat har ett tydligt meddelande.
- Sökning fungerar även i delningsförfrågningar; kurs- och sorteringskontrollerna döljs där.
- Valen behålls när listan uppdateras i samma vy. När vyn öppnas på nytt återställs de. Efter accepterad delning öppnas den ofiltrerade Mina-vyn så det mottagna dokumentet inte göms av gamla filter.

## Beslut att bevara

Filtrera aldrig bort mottagna dokument utifrån ägarrollen (UI01). Personliga dokument och skolans bank använder sina egna RPC-listor. Filtrering/sortering ändrar endast presentationen, inte originaldata, medlemskap, behörigheter eller dokumentinnehåll. Kursvalet byggs före sökningen så en sökning inte tar bort valbara kurser.

## Verifiering

- 18 godkända tester: `node --test tools/delade-dokument.test.js tools/sparskydd.test.js`.
- `python tools/delade-dokument.browser.py`: verkliga kontroller med isolerade RPC-fixturer, kurs/spår + sökning, alla tre sorteringar, tomma resultat, uppdatering, mottagna dokument, acceptans/avböjning, återförsök vid fel, separation från skolbanken och riktig dokumentöppning.
- Mobil 390 px och dator 1280 px, kontroller inom skärmen, visuell kontroll av mobilvyn. Inga JavaScript-fel. Inga produktionsanrop till Supabase.
