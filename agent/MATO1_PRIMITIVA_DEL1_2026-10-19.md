# Mato1: primitiva funktioner, del 1 – 2026-10-19

De första 25 av områdets 78 huvuduppgifter har lästs individuellt. 13 ändras och 12 lämnas oförändrade. Återstående 53 i området är inte färdiggranskade i denna omgång.

## Ändringar
- **3.04**: Sex delkort med bara slutsvar får egna förklaringar; huvudfacit synkas. Exponentialdelen får korrekt ledtråd.
- **3.10**: Sex delkort med bara slutsvar får egna förklaringar; huvudfacit synkas. Exponentialdelen får korrekt ledtråd.
- **3.16**: Exponentialdelens ledtråd pekade felaktigt på potensregeln. Tidigare fullständiga lösningar bevaras.
- **3.40**: Flera termvisa operationer bedöms som E/nivå 2, inte områdets allra enklaste nivå 1.
- **3.58**: Påståendet kräver samma intervall. Ledtråden ska gälla derivatan av skillnaden, inte potensintegrering.
- **3.64**: Ledtråden avslöjade hela resonemanget; ersatt med en fråga om tangentens lutning.
- **3.76**: Flera termvisa operationer bedöms som E/nivå 2, inte områdets allra enklaste nivå 1.
- **3.82**: Förtydligat intervallvillkor vid x=0 och förklarat potensregeln med negativ exponent.
- **3.130**: Visar den nödvändiga utvecklingen före termvis integrering.
- **3.134**: Potens med bråkexponent får mellanled och kontroll i stället för bara svar.
- **3.138**: Potens med bråkexponent får mellanled och kontroll i stället för bara svar.
- **3.142**: Förtydligat intervallvillkor vid x=0 och förklarat potensregeln med negativ exponent.
- **3.146**: Blandat polynom/exponentialuttryck behöver två olika integrationsregler.

## Utan ändring
2.529, 3.46, 3.52, 3.70, 3.94, 3.100, 3.106, 3.112, 3.118, 3.122, 3.126, 3.150.

## Självrättning
Ett verkligt konsumentfel reproducerades: 3e^(2x)+K godkändes mot 3e^(2x)/2+C i 3.16 b. Nerdamers simplify efter expand tappade x-beroendet i differensen. Både primitiva och primitiv använder nu enbart expand vid konstantkontrollen. Fel koefficient ska underkännas; fri konstant kan fortsatt heta K, stå först eller vara linjärt omskriven. Villkorsbestämda funktioners uttrycksrättning ändras inte. Sex olika exponentialuttryck provas med båda formaten och rätt/fel koefficient, utöver kortens riktiga inmatning.

## Matematik och pedagogik
Samtliga 25 frågors facit kontrollerade genom derivering, inklusive 3.70:s tangentfall x=−1/5 och C=1/3 respektive 109/3. Inga slutsvar ändras. 3.58 behöver ett gemensamt intervall; separata intervall kan ha olika konstanter. 3.82 och 3.142 preciserar att intervallet inte innehåller 0. 3.16:s tidigare lösningar bevaras.

Miniräknare är fortsatt tillåten för alla 25; GeoGebra är avstängd eftersom symbolisk integration och begreppsresonemang prövas. Delkort är kontrollerade i konsumenten. 3.40/3.76 flyttas till nivå 2 för flera termvisa operationer; E/poäng bevaras. Inga figurer behövs för dessa algebraiska metodsteg. Variation finns mellan potens, exponential, rot, parameter, tangent och resonemang; inga nya talbyteskloner skapas.

## Verifiering
428 mastertester och 178 konsumenttester passerar. Inga nya validatorfynd. Browser-testet provar riktiga svar och renderar 62 kortvyer på mobil/dator, inklusive intern formelklippning. Den separata SVG-CLI-suiten är undantagen på grund av tidigare miljötimeout; inga figurer har ändrats. Master/konsument jämförda före synk. Inga rapportstatusar ändrade.
