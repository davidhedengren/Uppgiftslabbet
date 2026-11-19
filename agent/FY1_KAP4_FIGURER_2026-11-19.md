# Fy1 kapitel 4: fler figurer, 19 november 2026

## Uppdrag

Fortsättning på kapitel 2 och 3 (`FY1_KAP2_FIGURER_2026-11-18.md`, `FY1_KAP3_FIGURER_2026-11-19.md`). Användaren:
”fortsätt”. Samma önskemål: fler figurer, snygga och med färg, inte generiska och inte där de inte tillför något.

Kapitel 4 hade 995 uppgifter, och 574 saknade figur:

| Område | Utan figur före | Läge |
|---|---:|---|
| newton3 | 42 | 7 figurer tillagda 2026-11-19 |
| normalkraft | 41 | 8 figurer tillagda 2026-11-19 |
| newton2 | 124 | ej påbörjat |
| lutande_plan | 79 | ej påbörjat |
| friktion | 70 | ej påbörjat |
| gravitation | 45 | 7 figurer tillagda 2026-11-19 |
| kraftvektorer | 41 | ej påbörjat |
| fjadrar | 33 | 5 figurer tillagda 2026-11-19 |
| tyngdkraft | 31 | 3 figurer tillagda 2026-11-19 |
| blandat_kraft | 28 | ej påbörjat |
| moment | 22 | 8 figurer tillagda 2026-11-19 |
| newton1 | 18 | 8 figurer tillagda 2026-11-19 |

## Regler

Samma som i kapitel 2 och 3 (vit bakgrund, fasta färger, okända storheter med ?, inget ”positiv riktning”, figuren i
frågan, i `spelIntro` och på delkort med samma data). Särskilt för kapitel 4: **figuren visar föremålen och de krafter
som är givna i texten, men inte de krafter som söks** (normalkraft, kraft mellan föremål, spännkraft), och ingen färdig
kraftfigur där eleven ska rita den själv.

## Urval i newton3 och normalkraft

Newtons tredje lag är mest korta begreppsfrågor (4.455–4.461, 4.819–4.836), där en figur med kraftpar skulle visa
svaret. Figur lades till där två föremål påverkar varandra: skridskoåkare (4.463), astronaut och verktygslåda (4.464),
vagnar med fjäder (4.465), lådor i kontakt (4.496), lok med två vagnar (4.501), två pulkor (4.896) och krock mellan
lastbil och personbil (4.894).

I normalkraft lades figur till där situationen är mer än ”en låda på ett golv”: träningsvikt som dras uppåt (4.477),
staplade böcker (4.478), låda som dras och trycks snett (4.502), våg och dynamometer (4.207, bara delkort a), person
på våg i hiss (4.217), två vikter i hiss (4.646), fisk i lina under brygga (4.642) och bok som trycks mot vägg (4.816).
Enkla frågor om en låda på golvet (4.475, 4.479, 4.801–4.818) och flera liknande hissuppgifter fick ingen figur, för
att undvika generiska kopior.

## Urval i gravitation och tyngdkraft

Gravitation: figur där geometrin är det svåra, alltså avstånd från centrum och höjd över ytan. Det gäller satellit 400 km
över jordytan (4.74, delkort b och c, eftersom a har en egen kortare text), sond på höjden R (4.354), nollpunkten mellan
två planeter (4.379), sten mellan två massor (4.753), bollar som nuddar varandra (4.738), jordens radie vid pol och
ekvator (4.739, med överdriven tillplattning) och två fartyg (4.188). I 4.379 är punkten P **inte** skalenligt placerad,
eftersom läget är svaret. Formelövningar med g = GM/R² och procentjämförelser fick ingen figur.

Tyngdkraft: mest enstegsberäkningar med m och g, utan figur. Figur lades till där mätinstrumentet är poängen:
kraftmätare på en planet (4.474), fjädervåg och balansvåg på månen (4.498) och kraftmätare på jorden och månen (4.887).

## Urval i newton1, moment och fjädrar

Newtons första lag (jämvikt): snören och vajrar med vinklar (4.91, 4.97, 4.313, 4.500), trissor (4.671 och 4.672,
bara delkort b och c, eftersom a har en egen kortare text, samt 4.674) och tvättlinan med nedhänget h (4.172). Inga
krafter som söks är utritade. 4.171 ber eleven frilägga och rita krafterna och fick ingen figur.

Kraftmoment: balk med led och lina (4.451), skottkärra (4.75), stång med tre krafter kring O (4.301), gungbräda (4.505),
hängande plattform med målare (4.508, bara delkort a), stege mot vägg (4.510), stång med snöre i 30° (4.511) och
underarm med bok (4.514). Enstegsuppgifter med M = Fl (4.127) och tyngdpunktsfrågor utan geometri fick ingen figur.

Fjädrar: två fjädrar i serie med vikt (4.181), stång i två fjädrar (4.272, med vikten på okänd plats), serie- och
parallellkoppling (4.308), fjäder som dras från väggen (4.329) och obelastad och belastad längd (4.327). Enstegsuppgifter
med F = kx (4.323–4.328, 4.332–4.340) fick ingen figur.

## Kontroll

- Byggskript: `tools/bygg-fy1-kap4-figurer-2026-11-19.py`. Regressionstest: `tools/fysik1-kap4-figurer-2026-11-19.test.js`.
- Figurerna är granskade som bilder och med `tools/granska-svg.js`. Inga krockar eller klippta etiketter återstår.
- Hela testsviten ger samma resultat som före ändringen.
- **Kunskapsgymmet är inte synkat i denna session.**
