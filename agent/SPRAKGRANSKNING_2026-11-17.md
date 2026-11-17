# Språkgranskning: AI-känsla i uppgiftstexterna (2026-11-17)

Användaren tycker att många uppgifter låter AI-genererade och vill att språket känns autentiskt. Det här är en
analys. Ingen bank är ändrad ännu.

## Metod

1. **Lärarkorpus:** text ur 375 egna Word-filer (prov, extrauppgifter, diagnoser och repetition) i OneDrive
   `Fysik\` och `Matematik\`, från 2012–2025. Förlagsmaterial, arkiv, lösningsförslag, AI-gjorda övningsprov
   och filer skapade efter 2026-09-01 är uteslutna. Korpusen har cirka 177 000 ord. Formler (OMML) följer inte
   med, så jämförelsen gäller den löpande texten.
2. **Banktext:** uppgiftstexten `t` i de sju bankerna, 21 985 uppgifter och cirka 497 000 ord. HTML, SVG och
   tabeller är borttagna och formler ersatta med X.
3. **Jämförelse:** ord, ordpar och tretal som är mycket vanligare i bankerna än i korpusen
   (log-kvot med minst 25 träffar), meningsstarter och 45 riktade mönster räknade per 10 000 ord.
   Därefter lästes slumpvisa exempel i sitt sammanhang för varje mönster.

Skript: scratchpad `sprak/korpus.py`, `jamfor.py`, `monster.py`, `perbank.py` och `visa.py`. De flyttas till
`tools/` när omskrivningen börjar.

## Huvudfynd

Det som får texten att låta maskinskriven är inte enstaka ord. Det är **stapling**: korta påståendemeningar
som ger förbehåll, modellantaganden och svarsinstruktioner, en i taget, före eller efter själva frågan. Lärarens
uppgifter berättar en situation och ställer en fråga. Förbehåll kommer sist och är få, oftast bara ”Bortse
från luftmotstånd.”

| Mönster | Bank /10 000 ord | Lärare /10 000 ord | Kommentar |
|---|---:|---:|---|
| ”(Svara i …)” | 37,4 | 0,1 | 1 860 st, varav 953 i Fy1. Läraren skriver ”Svara i …” utan parentes och bara när det behövs (timmar och minuter, ppm, enklaste form). |
| ”Välj ett alternativ” | 12,2 | 0 | 605 st i alla banker. Läraren skriver ”Välj rätt alternativ” eller ”Ringa in” några gånger. |
| ”Markera det korrekta alternativet” | 3,0 | 0 | 149 st, bara i Fy1. |
| ”Bortse från …” | 15,8 | 2,2 | 786 st, varav 655 i Fy1. Ofta flera i rad och ofta före frågan. |
| ”andra krafters impuls under den korta stöten” | 2,5 | 0 | 72 st i Fy1. Det strider redan mot CLAUDE.md (”modelljargong”). |
| ”Höger/uppåt räknas som positiv(a) riktning(ar)”, ”med tecken” | 6,2 | 0 | Cirka 250 st i Fy1. |
| ”en kloss/vagn/puck **på** 2,0 kg” | 19,6 | 2,7 | 691 uppgifter i Fy1. Läraren skriver ”med massan 2,0 kg” eller ”som väger 2,0 kg”. |
| ”vågrät/lodrät” | 24,1 | 0,7 | Läraren skriver ”horisontell/vertikal” (8,1 mot 2,0). |
| ”från vila” | 6,9 | 0,6 | Läraren skriver ”från stillastående”, ”släpps” eller ”startar”. |
| ”Räkna med …”, ”Endast … verkar”, ”Inga andra krafter …” | – | ≈0 | Cirka 200 meningar som ger modellantaganden i stället för att beskriva situationen. |
| Formel eller konstant före frågan (”Stefan–Boltzmanns lag: … Nettoeffekt: …”) | 2,1 | 0,6 | 81 uppgifter i Fy2. Det bryter också mot konstantregeln (σ står i frågan). |
| ”En elev säger/påstår/skriver …” | 3,3 | 0,1 | 162 st. Läraren använder namn: ”Kalle påstår …”, ”Har hon rätt?” |
| ”Funktionen är \(f(x)=…\).” | 69/100 000 | 1,7/100 000 | Läraren skriver ”För funktionen f gäller att …” eller ”Funktionen f ges av …”. |
| ”digitalt verktyg” | 2,3 | 0,1 | Läraren skriver ”räknare”, ”grafritande räknare” eller ”GeoGebra”. |
| ”Du kan svara med exakt bråk, decimaltal eller procent.” | – | 0 | 98 st i Ma5. Det är en rättningsinstruktion. |
| ”Skriv svaret som ett vanligt tal, inte i tiopotensform.” | – | 0 | 83 st i Ma1. Det är en rättningsinstruktion. |
| ”Miniräknare får användas. Behåll oavrundade värden i mellanleden.” | – | 0 | Cirka 40 st. Det är metainstruktioner. |
| ”Fördjupning utanför ordinarie Ma5-träning.” | – | 0 | 7 st. Det är internt utvecklarspråk i elevtext. |
| ”Bestäm” | 196 | 84 | Bestäm används 2,3 gånger så ofta. ”Beräkna” används hälften så ofta (26 mot 48). |
| ”Hur stor är” | 25/10 000 | 10/10 000 | Används 2,6 gånger så ofta. |
| ”Motivera” | 7,1 | 15,8 | Läraren skriver oftare ”Motivera ditt svar.” |
| ”enligt figuren”, ”se figur” | 0,8 | 8,3 | Banken skriver nästan alltid ”Figuren visar …”. |
| ”sammanlagd(a/t)” | 7,6 | 1,4 | Läraren skriver ”totalt”, ”tillsammans” eller ”hela”. |
| ”Anta att” / ”Antag att” | 3,9 / 0 | 1,2 / 2,3 | Läraren skriver oftast ”Antag att”. |

Lärarens egna drag som nästan saknas i banken:

- namngivna personer (Helmut, Lena, Märta, Kalle, Tarzan);
- verkliga platser och märken (Burj Khalifa, Audi och Volvo, Sputnik);
- ”Motivera ditt svar.”;
- ”Beräkna …”;
- ”enligt figuren” och ”se figur”;
- frågor med om-sats, som ”Om släden dras … 15 m, hur stort arbete har pojken då utfört?”;
- en enda avslutande förenkling.

## Var problemen finns

Tabellen anger antal uppgifter där mönstret förekommer minst en gång.

| | Fy1 | Fy2 | Ma1 | Ma2 | Ma3c | Ma4 | Ma5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Välj ett alternativ | 129 | 46 | 100 | 139 | 112 | 40 | 39 |
| (Svara i …) | 953 | 182 | 197 | 203 | 47 | 37 | 3 |
| ”på 2 kg” | 691 | 23 | 3 | 2 | 0 | 0 | 1 |
| vågrät/lodrät | 603 | 100 | 17 | 32 | 13 | 58 | 8 |
| Bortse från | 655 | 83 | 11 | 2 | 1 | 0 | 1 |
| positiv riktning | 151 | 2 | 0 | 0 | 0 | 0 | 3 |
| formel före frågan | 0 | 81 | 10 | 4 | 2 | 0 | 0 |
| En elev säger … | 44 | 0 | 72 | 24 | 16 | 3 | 3 |
| modelleras/förenklad modell | 54 | 3 | 41 | 70 | 91 | 72 | 15 |

**Fysik 1 är klart värst**, och sedan kommer Fysik 2. Matematikbankerna låter mer som läroboken, men har egna
drag: ”Funktionen är …”, telegramstil som ”Material kostar 160 kr/m². Kostnad för 14,5 m²?”,
”modelleras av”, ”digitalt verktyg”, ”En elev säger” och rättningsinstruktioner.

## Exempel: före och efter (förslag, inte införda)

| ID | Nu | Förslag |
|---|---|---|
| Fy1 5.449 | En isbit på 5,00 kg träffar en stillastående isbit på 5,00 kg med 12,0 m/s och fastnar. De glider sedan uppför en friktionsfri backe. Bortse från andra krafters impuls under den korta stöten. Bortse även från luftmotstånd. Hur stor höjd når de över backens början? | En isbit med massan 5,00 kg glider med farten 12,0 m/s och krockar med en likadan isbit som ligger stilla. Isbitarna fastnar i varandra och glider sedan uppför en backe. Hur högt upp kommer de? Bortse från friktion och luftmotstånd. |
| Fy1 5.178 | Två vagnar fastnar vid en stöt. Vagn 1 på 1,2 kg har hastigheten +4,0 m/s och vagn 2 på 0,80 kg har hastigheten −1,0 m/s. Höger är positiv riktning. Bortse från andra krafters impuls under den korta stöten. Bestäm deras gemensamma sluthastighet med tecken. | En vagn med massan 1,2 kg rullar åt höger med farten 4,0 m/s. Den krockar med en vagn med massan 0,80 kg som rullar åt vänster med farten 1,0 m/s. Vagnarna fastnar i varandra. Vilken hastighet får de efter krocken? (Kunskapsgymmet: tecken och riktning i delkortet.) |
| Fy1 6.367 | … Vätskan kan inte pressas ihop. Bortse från friktion, läckage och kolvarnas massa. Räkna med samma tryckökning under båda kolvarna. Den stora kolven ska bära en bil med massan 1200 kg utan acceleration. Hur stor kraft behövs på den lilla kolven? | En hydraulisk domkraft har en liten kolv med diametern 2,0 cm och en stor kolv med diametern 12 cm. Hur stor kraft måste man trycka med på den lilla kolven för att lyfta en bil som väger 1 200 kg? |
| Fy1 8.346 | Ett elektriskt fält är riktat åt höger och har styrkan 1200 N/C. En dammpartikel i en luftrenare har laddningen −3,0 µC. Vilken elektrisk kraft verkar på laddningen? (Svara i N med höger som positiv riktning.) | I en luftrenare finns ett elektriskt fält med fältstyrkan 1 200 N/C riktat åt höger. En dammpartikel har laddningen −3,0 µC. Hur stor kraft verkar på dammpartikeln, och åt vilket håll? |
| Fy2 4.468 | Stefan–Boltzmanns lag: \(M=e\sigma T^4\) där \(\sigma=5{,}67\cdot10^{-8}\) … Nettoeffekt: … Värmekameror mäter skillnader i utstrålad effekt. Med hur många procent ökar … | En värmekamera mäter hur mycket värmestrålning en kropp sänder ut. Med hur många procent ökar den utstrålade effekten från huden om hudtemperaturen stiger från 33,0 °C till 34,0 °C? |
| Ma1 7.20 | Material kostar 160 kr/m². Kostnad för 14,5 m²? | Ett golv ska läggas med en matta som kostar 160 kr/m². Golvet är 14,5 m². Vad kostar mattan? |
| Ma1 0.550 | Omvandla 235000 cm³ till m³. Skriv svaret som ett vanligt tal, inte i tiopotensform. | Hur många m³ är 235 000 cm³? (Rättningen godtar båda skrivsätten.) |
| Ma2 2.1232 | En elev skriver \(x^2-10x+7=(x-5)^2+7.\) Vad är felet? (Välj ett alternativ.) | Axel kvadratkompletterar och skriver \(x^2-10x+7=(x-5)^2+7\). Vad har blivit fel? |
| Ma5 1.377 | En kod byggs i tre steg. I första steget finns 3 val, i andra 4 val och i tredje 2 val. Valen kan kombineras fritt. Hur många olika koder kan skapas? | Till frukost kan man välja mellan 3 sorters bröd, 4 sorters pålägg och 2 sorters dryck. Hur många olika frukostar kan man sätta ihop? |
| Ma5 1.79 | Fyra sensorer ska väljas ur en uppsättning med 12 olika sensorer. Ordningen spelar ingen roll. Hur många urval finns? | En klass med 12 elever ska välja fyra representanter till elevrådet. På hur många sätt kan det ske? |
| Ma5 1.105 | Fem kort dras slumpmässigt ur en vanlig kortlek med 52 kort. Bestäm sannolikheten att exakt två av korten är hjärter. Du kan svara med exakt bråk, decimaltal eller procent. | Du drar fem kort ur en vanlig kortlek. Hur stor är sannolikheten att exakt två av dem är hjärter? |
| Ma3c 2.795 | … Miniräknare får användas. Behåll oavrundade värden i mellanleden. a) … | Metainstruktionerna tas bort, eftersom verktygsflaggan redan styr räknaren. |

## Det som gör omskrivningen svår

Många av de AI-lika meningarna finns där av ett skäl: **självrättningen i Kunskapsgymmet**. Tecken och positiv
riktning, svarsenhet, ”vanligt tal” och ”Välj ett alternativ” finns för att maskinen ska kunna rätta. AI-banken
löste samma sak 2026-11-11: `t` skrivs för papper och rättningsinstruktionerna ligger i `spelDelar`. För de sju
stora bankerna kräver det ett beslut, eftersom uppgifter utan `spelDelar` visar `t` direkt i Kunskapsgymmet.

Det finns också gamla regler som drev fram mönstren och som måste vägas mot det nya målet:

- CLAUDE.md: ”säg uttryckligen vad som ska skrivas (’Svara i m/s’)”.
- Regeln om svarsinstruktioner i parentes.
- ”Behåll nödvändig positiv riktning.”

## Förslag till arbetssätt

1. Ta en bank och ett område i taget, med Fy1 rörelsemängd och stötar först, eftersom stöt-jargongen är tätast
   där. Varje uppgift skrivs om för hand, inte med sök och ersätt, enligt reglerna i stilguiden nedan.
   Matematiken, svaren och ID:na ändras inte.
2. Rättningsinstruktioner flyttas från `t` till delkorten där det går. Annars skrivs de naturligt, som ”Svara i
   timmar och minuter”.
3. Ett regressionstest ser till att de förbjudna fraserna inte kommer tillbaka.
4. Ingen massändring görs utan läsning, eftersom heuristiska fynd inte får massändras.

## Stilguide (förslag, utgår från lärarens prov)

- Beskriv situationen i en eller två meningar med en verklig sak, gärna ett namn eller en plats. Ställ sedan en
  direkt fråga: ”Hur stor …?”, ”Beräkna …”, ”Vilken …?”
- Använd högst ett förbehåll, och sätt det sist: ”Bortse från luftmotstånd.” Ta inte med förbehåll som inte
  ändrar svaret.
- Skriv ”med massan 2,0 kg” eller ”som väger 2,0 kg”, inte ”på 2,0 kg”. Skriv ”horisontell/vertikal”,
  ”stillastående” och ”Antag att”.
- Riktning beskrivs i ord (”åt höger”, ”mot väggen”). Tecken och positiv riktning hör hemma i facit eller i
  rättningsinstruktionen.
- Inga formler eller konstanter i frågan. Eleven har formelsamlingen.
- Matematik: ”För funktionen f gäller att f(x) = …”, ”Funktionen f ges av …” och ”Beräkna …”. Använd hellre
  namn än ”En elev”, och skriv ”Motivera ditt svar.”
- Flerval: ställ frågan (”Vilket alternativ stämmer?”) eller ingenting. Skriv inte ”Välj ett alternativ.” eller
  ”Markera det korrekta alternativet.”
- Skriv aldrig metainstruktioner som ”Miniräknare får användas”, ”Behåll oavrundade värden” eller ”Fördjupning
  utanför …”.
