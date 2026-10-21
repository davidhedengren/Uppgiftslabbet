# Fysik 1: komplettering av medicinska metoder, 2026-10-21

## Lucka och resultat

Området hade 13 huvuduppgifter och bara en figur. Många frågor var textuppgifter om framåträkning med halveringstid. Åtta olika figuruppgifter kompletterar bildtolkning, diagram, omvänd planering, bakgrund, dosjämförelse och två samtidiga tidskrav. Nu finns **21 uppgifter och 9 med figur**. Mätnoggrannhet ingår inte i denna utbyggnad.

## Alla nya uppgifter

| ID | Bedömning och korrekt svar |
|---|---|
| 9.436 | Bild B: strålkällan finns i patienten, till skillnad från den yttre röntgenkällan. Nivå 1. |
| 9.437 | Minskning från 800 till 300 fotoner: (800−300)/800 = 62,5 %. Nivå 2. |
| 9.438 | Fyra dosbidrag à 0,8 Gy ger 3,2 Gy i tumören. Nivå 1. |
| 9.439 | Aktivitetsgrafens 160 MBq blir 80 MBq efter 3 h. Nivå 1. |
| 9.440 | 180 MBq ska återstå efter två halveringar: startaktivitet 720 MBq. Nivå 2. |
| 9.441 | 180 uppmätta pulser minus 60 bakgrundspulser under samma tid ger 120. Diskret antal, inte aktivitet. Nivå 1. |
| 9.442 | A får 0,20 Gy och B 0,10 Gy vid samma absorberade 2 mJ. Nivå 2. |
| 9.443 | B ger 50 % efter 2 h och cirka 0,0244 % efter 24 h och klarar båda kraven. A minskar för snabbt, C för långsamt. Nivå 3. |

Varje nytt kort har egen SVG, självständig text, relevant ledtråd, kort förklarande lösning och kontrollerade metadata. Miniräknare tillåts alltid; GeoGebra behövs inte. Svarsinstruktioner står i parentes efter frågan. Inga standardkonstanter ges i frågorna. Fyra nivå 1, tre nivå 2 och en nivå 3.

## Alla granskade befintliga uppgifter – Granskad – inget fel

Följande är manuellt jämförda för innehåll/beräkning, inte ny fullständig webbläsartestning av varje äldre delkort. Deras tidigare regressionstester är bevarade. Minst fem relevanta jämförelser finns bland 9.3/9.12/9.56/9.92/9.296/9.297/9.301.

| ID | Färdigt kommentarsförslag |
|---|---|
| 9.3 | Granskad – inget fel: Tre halveringstider ger 50 MBq; behandlingsfrågans fria förklaring bevarad. |
| 9.12 | Granskad – inget fel: Maxenergi 60 keV och kortaste våglängd cirka 2,07·10⁻¹¹ m. |
| 9.28 | Granskad – inget fel: Effektiv halveringstid 80/11 dygn; kortets eget 7,27 används i den separata b-beräkningen. |
| 9.56 | Granskad – inget fel: 210 minuter ger cirka 5,325 GBq från 20 GBq vid T=110 min. |
| 9.92 | Granskad – inget fel: 0,30 J och cirka 4,78·10⁻⁴ K per behandling; strålverkan ska inte likställas med uppvärmning. |
| 9.296 | Granskad – inget fel: Fyra halveringar ger 50 MBq. |
| 9.297 | Granskad – inget fel: Gammastrålning som lämnar kroppen kan registreras utifrån. |
| 9.298 | Granskad – inget fel: Två fotoner à 511 keV ger 1022 keV. |
| 9.299 | Granskad – inget fel: Kortare halveringstid ger snabbare avtagande aktivitet vid samma startaktivitet. |
| 9.300 | Granskad – inget fel: Tre halveringar ger 12,5 % kvar. |
| 9.301 | Granskad – inget fel: Flera dosbidrag möts i tumören medan frisk vävnad på vägen får färre bidrag. |
| 9.302 | Granskad – inget fel: 500·2^(−20/8) ≈ 88,388 MBq. |
| 9.303 | Granskad – inget fel: Vanlig röntgen använder elektromagnetisk röntgenstrålning. |

**Åtgärdade befintliga uppgifter:** inga; samtliga äldre bankobjekt är identiska med versionen före omgången. **Nya felrapporter:** inga. **Kvar att utreda:** inga inom denna avgränsning.

## Viktiga kontroller

- Dosbidragen gäller uttryckligen tumören. Figuren i 9.438 gör inget påstående att frisk vävnad inte får dos.
- I 9.437 är procentminskningen jämförd med ursprungsvärdet 800. 37,5 % är kvarvarande andel, inte minskningen.
- 9.440 räknas bakåt från slutaktivitet. 9.443 prövar båda tidskraven, inte bara kortast eller längst halveringstid.
- 9.441 jämför samma mättid, drar bort bakgrunden och blandar inte detektorns registrerade pulsantal med sönderfallsaktivitet. `antal_satt` används för det diskreta antalet 120; exakta uttryck fungerar.
- Standardkonstanter och fysikformler hör till facit. De medicinska modellerna ger nödvändiga material-/tidsdata och kräver inte annan klinisk information.

## Tester och visning

- 86 svarskontroller och 16 kortvyer vid 390/1280 px. Korrekt procent/andel, Gy/mGy, h/min, MBq/GBq och heltalsuttryck prövade. Fel metod, enhet och felalternativ avvisas.
- Alla åtta figurer visuellt granskade. Inga klippta SVG-texter, KaTeX-fel, JavaScript-fel eller sidöverflöden.
- Riktat test `tools/fysik1-medicinska-metoder-2026-10-21.test.js`, befintligt `fysik1-partiklar-medicin.test.js` och testet för tunna områden passerar.
- Före denna ändring saknade det äldre testets fullständighetslista tre redan tillagda uppgifter: 9.431/9.432/9.435. Listan har kompletterats med oberoende formler med G=6,674·10⁻¹¹. Deras facit är korrekta; inga bankändringar eller borttagna testkrav. Denna extra kontroll gäller de tre talvärdena, inte en ny full innehållsgranskning av hela kraftområdet.
- Full bankvalidator före/efter: {'ERROR': 1577, 'WARNING': 227, 'INFO': 1452} → {'ERROR': 1577, 'WARNING': 227, 'INFO': 1452}. Inga nya fynd; äldre kvarvarande fynd i banken ligger utanför uppdraget.
- Master är Uppgiftslabbet. `uppgifter.js` jämförs före identisk synk, och cacheversioner uppdateras i båda repona.
- Orelaterade prototyper och Python-cache lämnas orörda. Ingen rapportstatus eller elevkommentar sparas i produktionsdatabasen.
