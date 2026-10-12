# Fysik 1 – 15 ytterligare uppgifter med egen tangentritning

2026-10-12. **3.425–3.439**, kapitel 3 Rörelse. Alla är nykonstruerade och granskade. Inga befintliga uppgifter ändras. Uppgifterna visas endast i Uppgiftslabbet och bedöms manuellt, även när facit har ett numeriskt svar. `spel:false`, `självrättning:false`, `rättSvar:null`, `manuellKomplettering:true`. Den gemensamma bankfilen synkas ändå byteidentiskt till Kunskapsgymmet.

## Pedagogiska beslut

- Alla frågor har tydliga huvudrutor och finare hjälprutor, axelrubriker och enheter. Ingen uppgiftsfigur har en dragen tangent. Lösningsfigurerna visar exempel på tangenter och två användbara avläsningspunkter.
- Fem uppgifter är nivå 2, sex nivå 3, två nivå 4 och två nivå 5. Nivå 2 tränar grundläggande tangentritning; nivå 3 jämför rörelser eller tolkar tecken och olika skalor. Nivå 4 kopplar lutning till kraft eller söker en gränstidpunkt. Nivå 5 prövar påståenden och uppskattar acceleration från lägesdata. E/C/A bedöms separat från träningsnivån.
- Varierade situationer: hiss, båt, skateboard, sprint, robot, cykel, bollkast, motorcykel, bollstöt, inbromsning, hastighetsgräns, drönare och fjädervagn. Variation i frågans tankeuppgift, kurvform, riktning och axelenheter.
- Miniräknare tillåts. Ingen symbolisk derivering krävs. Beräkningsmodeller i testerna är författarunderlag, inte extra data i elevfrågan. Facit visar nödvändiga beräkningar och förklarar resultatet utan numrerade steg. Deluppgifter har egna stycken.
- Avläsningar och slutsvar är uppskattningar: handritade tangenter kan ge något olika värden. I 3.439 är medelaccelerationen över det korta intervallet en uppskattning vid mittpunkten, inte ett allmänt bevis för exakt nollacceleration.

## Granskade uppgifter och förslag på kommentarer

| ID | Innehåll | Nivå | Kontrollerat svar | Förslag på kommentar |
|---|---|---:|---|---|
| 3.425 | egen tangent till hissens höjdkurva | 2 | v ≈ 2,5 m/s uppåt | Läs två punkter på tangenten och beräkna höjdskillnaden per sekund. |
| 3.426 | negativ momentanhastighet när en båt närmar sig bryggan | 2 | v ≈ −4 m/s; fart ≈ 4 m/s | Hastighetens tecken visar riktningen; farten saknar tecken. |
| 3.427 | jämföra hastighet före och vid en vändning på skateboard | 2 | v(2) ≈ 2 m/s, v(6) = 0; stilla bara i vändögonblicket | En vågrät tangent vid en tidpunkt betyder inte stillastående under ett helt intervall. |
| 3.428 | momentanhastighet jämförd med medelhastighet under ett sprintlopp | 3 | v(4) ≈ 6 m/s; medelhastighet 2 m/s; kvot 3 | Räkna bort startläget när du beräknar förflyttningen. |
| 3.429 | noll hastighet utan riktningsbyte för en programmerad robot | 3 | v(3) = 0; ingen vändning | Noll hastighet innebär inte alltid ett riktningsbyte. |
| 3.430 | en motorbåt ökar farten allt långsammare | 3 | a(2) ≈ 1,5 m/s²; a(6) ≈ 0,5 m/s²; kvot 3 | Farten kan fortsätta öka även när accelerationen blir mindre. |
| 3.431 | momentanacceleration när en cykel rullar och bromsas av motstånd | 2 | a(4) ≈ −0,75 m/s² | Tangentens punkt vid 0 s är inte den verkliga starthastigheten. |
| 3.432 | jämföra fart och hastighet uppåt och nedåt för en kastad boll | 3 | v(0,5) ≈ +4,9 m/s; v(1,5) ≈ −4,9 m/s; samma fart | Lika stor fart kan ha motsatta hastighetstecken. |
| 3.433 | hitta nollacceleration utan att förväxla den med stopp | 2 | a = 0 vid cirka 4 s; v ≈ 8 m/s | Noll acceleration betyder inte noll hastighet. |
| 3.434 | jämföra två båtar: snabbast är inte samma som störst acceleration | 3 | B snabbast: 11 mot 6 m/s. A accelererar mer: 2 mot 0,5 m/s² | Grafens höjd visar hastigheten, dess lutning visar accelerationen. |
| 3.435 | kort bollstöt: tangent, millisekunder och kraft | 4 | a ≈ −625 m/s²; kraft cirka 125 N bort från väggen | Omvandla millisekunder till sekunder före lutningsberäkningen. |
| 3.436 | bestäm när en gräns för bromsacceleration överskrids | 4 | Gränsen överskrids efter cirka 6,3 s till 10 s | Sök en tangent med lutningen −2,5 m/s² och jämför lutningarna runt den. |
| 3.437 | hastighetsgräns: granska ett påstående med tangenter och uppskatta tiden över gränsen | 5 | Cirka 34 km/h vid 5,5 s; över gränsen sista cirka 1 s | Låg medelfart utesluter inte att hastighetsgränsen överskrids. |
| 3.438 | två drönare med olika tids- och höjdskalor | 3 | A: 4 m/s; B: 120 m/min = 2 m/s; A dubbelt så snabb | Jämför lutningar efter enhetsomvandling, inte bara vinklarna på papperet. |
| 3.439 | uppskatta acceleration ur två tangenter till en svängande vagns lägeskurva | 5 | Båda v ≈ −2,9 cm/s; uppskattad acceleration vid 4 s ≈ 0 cm/s² | Två hastigheter ger en uppskattning av accelerationen; lägeskurvans branthet visar fart. |

**Åtgärdade befintliga uppgifter:** inga. **Granskad – inget fel, befintliga felrapporter:** inga. Detta är nyproduktion, inte handläggning av rapporter. Inga elevkommentarer eller rapportstatusar har skickats. Alla 15 nya uppgifter listas ovan och maskinläsbart i JSON-filen med samma namn.

## Kontroller

- `node --test tools/fysik1-egna-tangenter.test.js tools/fysik1-momentan.test.js tools/fysik1-kapitel3.test.js`: 13 godkända testfall. Kurvornas 301 koordinater, kontaktpunkter och lösningstangenternas lutningar kontrolleras mot oberoende fysikmodeller. Särskilda kontroller för millisekunder, kraft, hastighetsgräns, minutaxel och acceleration ur två hastigheter.
- `python tools/fysik1-egna-tangenter.browser.py --master-port 8085 --student-port 8083`: 30 kortvisningar vid 390/1280 px. Alla facit öppnas. Inga JavaScript-/KaTeX-fel, överlappande SVG-etiketter eller överflöde i frågorna. Alla 15 utesluts ur Kunskapsgymmets verkliga `availableTasks()`.
- 38 SVG: 16 uppgiftsfigurer och 22 lösningsfigurer, även visuellt granskade. `tools/granska-svg.js`: 0 ERROR, 0 WARNING, 38 INFO. INFO gäller den avsiktliga vita bakgrundsrektangeln vid viewBox-kanten. Som vid föregående genomgång körs validatorns mät-HTML via lokal Playwright-adapter eftersom Chromium-CLI inte kunde öppna lokala file-URL:er; analysen är oförändrad.
- Hela Fysik 1-bankens validator har samma resultat som före tillägget: 0 ERROR, 8 WARNING, 833 INFO. Inga nya fynd. Befintliga varningar ligger utanför denna nyproduktion.
- Alla 3 753 tidigare bankobjekt är oförändrade. Exakt 15 tillägg ger 3 768 objekt. Bankkopiorna är byteidentiska. Konsumentens `BANK_VERSION` är `2026-10-12-fy1-egna-tangenter`.

Produktionsändringar: master `uppgifter.js`, konsumentens synkade bank och cacheversion i `index.html`. Inga databasändringar behövs.
