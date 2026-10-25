# Ma3: derivatabegreppet på nivå 3 – omgång 4

18 nya självständiga C-uppgifter #2.1241–2.1258. Området går från 2 till
20 spelbara nivå 3-kort i både 1b och 1c. Inga äldre uppgifter ändras.

## Samtliga granskade uppgifter

Status för alla nedan: **ny, granskad – inget fel efter konstruktionskontroll**.
Sista kolumnen ger ett kort kommentarsförslag.

| ID | C-motivering | Kommentar / verifierat svar |
|---|---|---|
| 2.1241 | Kombinerar tangentlutning, två enhetsskalor, kort tidsintervall och relativ förändring. | Cirka 3,85 %. |
| 2.1242 | Tolkar symmetrisk kvot och omvandlar en absolut förändringshastighet till en relativ. | Cirka 9,33 % per år. |
| 2.1243 | Kombinerar medelvärde över ett intervall med lokal förändringshastighet och väljer rätt rot. | \(\sqrt7\) s. |
| 2.1244 | Återskapar en lokal lutning från två punktvärden och en annan lutning. | f′(0) = −1. |
| 2.1245 | Kombinerar motriktade flöden med gränser för en förändringshastighet över ett intervall. | Minst 60 liter, högst 80 liter. |
| 2.1246 | Kombinerar två derivator innan en lokal förändring uppskattas. | Cirka 105 kr. |
| 2.1247 | Skiljer marginalkostnad från genomsnittskostnad och hanterar båda axlarnas enhetsskalor. | Cirka 58,86 kr per stol. |
| 2.1248 | Avslöjar ett felaktigt derivataargument med symmetrisk kvot i en kontinuerlig hörnpunkt. | f′(2) finns inte; vänster och höger lutning skiljer sig. |
| 2.1249 | Bedömer riktningen på felet när en lokal linjär modell används baklänges för att hitta en tidpunkt. | Tangenten ger en för tidig tidpunkt, eftersom kurvan då fortfarande ligger över 25 °C. |
| 2.1250 | Skiljer mötestid från hastighet och använder relativ rörelse. | 8 m/s. |
| 2.1251 | Analyserar ett approximationsfel och skiljer tangentens förändring från den exakta. | 20 kr mindre. |
| 2.1252 | Tolkar derivatan geometriskt och omvandlar liter per centimeter till area. | 1000 cm². |
| 2.1253 | Kombinerar kontinuitet med lika lutning vid en skarv. | a = 2 och b = −1. |
| 2.1254 | Skiljer absolut och relativ tillväxt och kopplar derivata till en exponentialekvation. | Efter cirka 11,16 timmar. |
| 2.1255 | Resonerar om vad lika ändpunktshöjd och deriverbarhet garanterar, utan att anta en viss funktionsform. | Det finns minst ett x mellan 0 och 4 där f′(x) = 0. |
| 2.1256 | Översätter en grafisk derivata per kilometer till en förändring över tid med hjälp av hastigheten. | Cirka 1,8 liter. |
| 2.1257 | Kombinerar lokal approximation med både tidsomvandling och en temperaturtransformation. | Cirka 101,3 °F. |
| 2.1258 | Prövar skillnaden mellan ett nödvändigt extremvillkor och ett tillräckligt teckenbyte. | Punkten är inget extremställe; funktionen växer på båda sidor. |

## Variation och nivå

Tillskottet breddar den befintliga dominansen av ”derivera och sätt in en
tid”. Det innehåller tankar, befolkning, kostnad/vinst, relativ rörelse,
bränsleförbrukning, en okänd andragradsfunktion, skarvar, avsvalning och
begreppsliga motexempel. Inga frågor har skapats genom enbart talbyte.

C-motivet är att flera samband måste skiljas åt eller kombineras:
absolut/relativ förändring, medel/momentan hastighet, läge/hastighet,
nettoflöde, marginal/genomsnitt, kontinuitet/deriverbarhet samt stationär
punkt/extrempunkt. Några kort är lättare C-ingångar; de numeriskt tyngre
är fortfarande byggda av gymnasiekursens standardmetoder.

Sju egna SVG-grafer. Alla kurvkoordinater kommer från funktioner, och
utritade tangenter har rätt lutning och kontakt. Två punktmarkeringar
på en tangent får inte förväxlas med punkter på kurvan: de är orange.
En kollision mellan 0 och 1 på volymaxeln i #2.1252 togs bort före
publicering. #2.1250 visar två rörelser, inte en tangent; färgförklaringen
anger uttryckligen cyklist A och B.

Miniräknare tillåts utom i de tre begreppsfrågorna #2.1248, #2.1255 och
#2.1258. Ingen kräver digital grafanalys eller GeoGebra. Numeriska
uppskattningar med bestämd precision anger den uttryckligen. Namngivna
minimi-/maximivolymer och a/b har märkta fält. Flervalsfrågornas rätta
alternativ är fördelade på A, B, C och D i källdata; appens blandning
respekteras också av testet.

## Verifiering

- 318 kontroller i riktiga svarsfält, 36 elevvyer och 36 lärarvyer på
  390/1280 px. Båda spåren kontrollerade. Inga rättningsfel; en lång
  ny lösningsrad i #2.1251 delades före slutkontroll.
- `ma3-derivatabegrepp-c-2026-10-25.test.js`: oberoende beräkningar av
  svar, enheter, modellfel, parametrar och motexempel. Testet kontrollerar
  även figurernas faktiska kurv- och linjekoordinater.
- Full mato1-validator: 0 ERROR, 50 WARNING, 179 INFO, oförändrat.
  Inga nya fynd. Äldre bankobjekt bevarade.
- Alla sju figurer visuellt granskade. SVG-validatorns geometriska
  kontroll via Playwright efter etikettjusteringen: 0 ERROR, 0 WARNING.
  Sju INFO gäller bara bakgrundsrektanglar vid viewBox-kanten.
- Master/konsument ska ha identiska bankfiler och uppdaterade cacheversioner.

Åtgärdade äldre uppgifter: inga. Rapportstatus och elevkommentarer i
databasen är oförändrade. Konstruktionsfynd i nya uppgifter är korrigerade
innan publicering och är inte elevrapporter.
