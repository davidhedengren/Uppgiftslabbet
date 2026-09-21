# Kvalitetskontroll

Detta är minimikrav för ändringar i uppgiftsbanker, validatorer och synkroniserade konsumentkopior. Anpassa kontrollernas omfattning efter ändringen, men hoppa inte över en relevant kontroll utan att rapportera varför.

## 1. Före redigering

- [ ] Läs `agent/ARBETSINSTRUKTION.md` och relevanta kompletterande regler.
- [ ] Kontrollera repo, branch, upstream, remote och `git status`.
- [ ] Kör `git fetch` och jämför lokal branch med upstream.
- [ ] Identifiera och skydda befintliga lokala ändringar.
- [ ] Avgränsa exakt vilka filer, uppgifter och fält som får ändras.
- [ ] Verifiera om arbetet berör Uppgiftslabbet, Kunskapsgymmet eller båda.

## 2. Matematisk och pedagogisk kontroll

För varje ändrad uppgift:

- [ ] Lös eller verifiera matematiken självständigt.
- [ ] Kontrollera definitionsmängd, extralösningar och samtliga giltiga lösningar.
- [ ] Kontrollera om svaret är ordnat eller oordnat.
- [ ] Bedöm förmåga självständigt.
- [ ] Bedöm nivå självständigt.
- [ ] Bedöm självrättningsbarhet självständigt.
- [ ] Kontrollera att svarsformat, etiketter, tolerans, enheter och alternativa representationer motsvarar matematiken.
- [ ] Kontrollera att uppgiftstext, facit och maskinellt rätt svar är förenliga.
- [ ] Bevara ID om uppgiftens identitet inte faktiskt har ändrats.

## 3. Teknisk kontraktskontroll

- [ ] Kontrollera syntax och datatyper för ändrad metadata.
- [ ] Kontrollera arraylängder och inbördes relationer mellan flerdelssvar, toleranser, format, etiketter och självrättningsflaggor.
- [ ] Kontrollera ordning och struktur för svar med flera delar.
- [ ] Verifiera nya eller känsliga format mot Kunskapsgymmets faktiska renderings- och rättningskod.
- [ ] Kontrollera både hur många svarsfält som visas och hur de rättas.
- [ ] Om konsumenten har en begränsning: dokumentera den; förvräng inte uppgiften utan beslut.

## 4. Tester

Kör efter behov:

- syntaxkontroll för berörda JavaScript-filer och verktyg,
- projektets relevanta enhets- eller kontraktstester,
- validatorn för berörd bank,
- full validator när bankmetadata eller generella regler ändras,
- riktad kontroll av det ändrade uppgifts-ID:t,
- renderings- eller konsumenttest i Kunskapsgymmet,
- matematisk numerisk kontroll när den tillför verifieringsvärde.

Vid ändring efter merge eller rebase ska relevanta tester köras om på det integrerade resultatet.

Ett redan känt validatorfynd får ligga kvar endast om det ligger utanför uppdraget och resultatet rapporteras tydligt. Nya fynd som skapats av ändringen ska utredas före leverans.

## 5. Diff- och omfattningskontroll

- [ ] Kör `git diff --check`.
- [ ] Granska full diff för varje ändrad fil.
- [ ] Kontrollera ändrade filers antal och namn.
- [ ] För uppgiftsbanker: jämför objekten strukturerat och lista exakt vilka ID:n som ändrats.
- [ ] Kontrollera att icke berörda uppgifter är oförändrade.
- [ ] Kontrollera att tillfälliga och ospårade filer inte ingår i leveransen.
- [ ] Kontrollera att ingen formattering eller massändring skymmer den avsedda korrigeringen.

## 6. Validatorpolicy

Validatorn ska primärt kontrollera strukturella och körbara kontrakt. Resultat ska skilja mellan säkra fel och osäkra observationer.

- **ERROR**: ett verifierbart kontraktsbrott eller en otvetydig inkonsistens.
- **WARNING**: ett sannolikt problem som kräver mänsklig eller fördjupad granskning.
- **INFO**: en observation, möjlig likhet eller redaktionell granskningspunkt.

Heuristiska fynd får inte uppgraderas till säkra fel utan tillräcklig grund och får inte användas för automatisk masskorrigering.

## 7. Git- och leveranskontroll

Före commit:

- [ ] Tester är godkända eller kända avvikelser är uttryckligen redovisade.
- [ ] Endast avsedda filer är stagade.
- [ ] Commit-meddelandet beskriver ändringen kort och korrekt.

Precis före push:

- [ ] Kör `git fetch` igen.
- [ ] Kontrollera om upstream förändrats.
- [ ] Integrera samtidiga ändringar utan att skriva över någon version blint.
- [ ] Kör relevanta tester igen efter integration.
- [ ] Använd inte force push.

Efter push:

- [ ] Läs tillbaka remote-referensen.
- [ ] Verifiera att lokal och remote branch pekar på avsedd commit.

## 8. Rapportering

Slutrapporten ska ange:

- exakt vilka filer som ändrades,
- exakt vilka uppgifts-ID:n och fält som ändrades,
- vilka filer eller lokala ändringar som uttryckligen lämnades orörda,
- matematisk verifiering i relevant omfattning,
- utförda tester och faktiska resultat,
- validatorns sammanfattning,
- renderings-/konsumentverifiering när relevant,
- Git-status samt om commit och push utfördes,
- kvarstående risker, konflikter eller beslut som krävs.
