# Ma3b/3c – primitiva funktioner med villkor, 2026-10-22

Sex nya uppgifter, 3.1195–3.1200: två på nivå 1, en på nivå 2 och tre
på nivå 3. Fyra SVG-figurer och en tabell. Området växer från 49 till
55 huvuduppgifter. Spelbara huvuduppgifter med uttrycklig nivå 1 ökar
från två till fyra och med nivå 3 från en till fyra.

De tidigare 49 uppgifternas frågor inventerades för att undvika en ny
serie av samma ”integrera och sätt in x=0”. Deras facit har inte fått
en fullständig ny granskning och inga äldre uppgifter ändras här.

## Alla granskade uppgifter och kommentarsförslag

| ID | Nivå | Innehåll och verifierat svar / kommentar |
|---|---|---|
| 3.1195 | 1 | Välj grafen bland tre primitiva funktioner till 2x. F(0)=2 väljer kurva B. |
| 3.1196 | 1 | Konstant derivata 2: från F(3)=10 följer F(4)=12. Derivatagrafen visar det aktuella intervallet. |
| 3.1197 | 2 | Felsökning med negativt punktvillkor: F′=3x² och F(−1)=4 ger F=x³+5, inte x³+3. |
| 3.1198 | 3 | Okänd parameter och två punkter: F′=ax+2, F(1)=2, F(3)=14 ger a=2, C=−1 och F=x²+2x−1. |
| 3.1199 | 3 | Integralen av den sökta funktionen bestämmer konstanten: F′=2x och integral 0–2 av F=14/3 ger F=x²+1. |
| 3.1200 | 3 | Avgör om informationen räcker: F′=2x och F(2)−F(0)=4 bestämmer inte F(0). Alla F=x²+C fungerar. |

Alla sex: **nya, granskade – inget fel** efter konstruktionskontrollen.
Åtgärdade äldre uppgifter: inga. Kommentarerna ovan kan användas för
dokumentation; inga meddelanden eller rapportstatusar skickas till appen.

## Nivå och presentation

- Nivå 1 är en direkt grafavläsning respektive ändring med konstant lutning.
  Nivå 2 kräver att en primitiv funktion tas fram och ett negativt x-värde
  sätts in rätt. Nivå 3 kräver parameterbestämning, användning av ett annat
  slags villkor eller resonemang om varför ett villkor inte ger ny information.
- Alla sex har miniräknare. Inga avancerade integraler eller digitala
  grafanalyser behövs. GeoGebra skulle utföra det som ska prövas i de
  algebraiska uppgifterna och är därför av.
- 3.1198 visar bara de givna punkterna. En färdig kurva skulle avslöja
  konstanttermen. 3.1199 har ingen figur av den okända funktionen av samma
  skäl. 3.1200 samlar de två villkoren i en kompakt tabell.
- Inga nya konkurrerande delmomentsnamn: fyra kort använder befintliga
  ”Primitiv funktion genom en given punkt” och två ”Återskapa funktion från derivata”.
- Facit har korta förklaringar och de avgörande algebraiska mellanleden.
  Alla uppgifter är fristående. Uttryckssvar godtas både med och utan F(x)=.

## Verifiering

- `tools/ma3-primitiva-villkor-2026-10-22.test.js`: tre grupper med
  oberoende beräkningar, numerisk kontroll av derivator, punktvillkor,
  integralvillkor och faktiska koordinater i grafalternativen.
- Konsumentens motsvarande browserprov: 84 kontroller av rätt/fel svar,
  alternativa uttryck och samtliga icke-tomma valkombinationer i de två
  flervalsfrågorna.
- 12 elevvyer och 12 lärarvyer på 390/1280 px. Inga överflöden,
  JavaScript-/KaTeX-fel eller klippta figuretiketter. Alla fyra figurer
  samt nivå 3-faciten visuellt granskade.
- SVG-validator: noll ERROR/WARNING. Fyra INFO gäller den avsiktligt
  heltäckande vita bakgrunden.
- Full bankvalidator före/efter: 1519 ERROR, 230 WARNING och 1446 INFO.
  Inga nya fynd; de äldre fynden utanför denna omgång kvarstår.
- Endast sex nya objekt i banken. Båda kopiorna synkas och båda apparnas
  cacheversioner uppdateras. Pausade fysikutkast ingår inte.
