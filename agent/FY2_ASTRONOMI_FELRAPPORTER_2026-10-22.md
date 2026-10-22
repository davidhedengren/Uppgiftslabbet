# Fysik 2 – rapporter 2026-10-22 22:30

Alla fem rapporterade huvuduppgifter samt fem liknande uppgifter är
granskade. Tio huvuduppgifter och deras totalt 20 spelkort har reviderats.
Inga ID:n har tagits bort. Detta är en riktad granskning av dessa tio,
inte en genomgång av hela astronomikapitlet.

## Rapporterna: åtgärd och kommentar att använda i appen

| Uppgift | Åtgärd | Föreslagen kommentar |
|---|---|---|
| 5.42 f | Nivå 5 på det fristående kortet. Full lösning från parallax och magnitud till intensitet, öppningsarea, mottagen effekt och fotonenergi. | Åtgärdad: facit visar nu hela beräkningen. Någon särskild ”enfärgsformel” behövs inte: mottagen effekt delas med energin per foton. Uppgiften ligger på nivå 5. |
| 5.35 b | Nivå 5. Facit visar först hur radie och temperatur ger effektkvoterna. Tydliga fält för stjärna A och B, nu med självrättning. | Åtgärdad: nivån är höjd till 5 och de saknade mellanberäkningarna finns med. Svara för A och B i de namngivna fälten. |
| 5.41 | Kvantitativ magnitudomräkning ersatt av en begreppsfråga med figur och fyra alternativ. Nivå 1. | Omgjord: uppgiften prövar nu vilken stjärna som strålar ut störst effekt utifrån absolut magnitud. Ingen magnitudformel behövs. |
| 5.48 | Omgjord till begreppsfråga om skenbar ljusstyrka kontra utstrålad effekt. Magnitudskala i egen SVG. Nivå 2. | Omgjord: jämför hur ljusa stjärnorna ser ut och vad man behöver veta för att jämföra deras utstrålade effekt. Ingen magnitudberäkning behövs. |
| 5.30 b | ”Bolometrisk” ersatt med att magnituden gäller all strålning. Nivå 5 på b, nivå 4 på a. Komplett beräkning i båda delkorten. | Åtgärdad: språket är förenklat, b ligger på nivå 5 och facit visar både effektkvoten och omräkningen till watt. Svaret 1,77·10²⁸ W var korrekt. |

Rapporterna om att beräkningar inte ingår i lärarens bok hanteras i
5.41 och 5.48 genom att ändra just dessa uppgifter till begreppsträning.
Detta är **inte** ett beslut att magnitudberäkningar saknas i alla
gymnasieböcker eller måste tas bort ur hela Fysik 2. Ingen sådan
generell kursavgränsning har verifierats här.

## Alla fem liknande uppgifter

Samma fem används för att följa upp språk, nivå, beräkningskedjor och
fristående facit. De har granskats individuellt, inte ändrats utifrån
en automatisk svårighetsregel.

| ID | Granskning och åtgärd | Föreslagen kommentar |
|---|---|---|
| 5.31 | Bolometrisk-jargong borttagen. Nivå 4 i stället för gammal E. Facit förklarar effektkvoten och magnitudskillnaden. | Språk och nivå justerade. Facit +11,6 är korrekt. |
| 5.32 | a nivå 3, b nivå 5. b-kortets facit visar nu även beräkningen från radie och temperatur. | Lösningen är kompletterad: effekten blir cirka 216 gånger solens och magnituden cirka −1,10. |
| 5.33 | Nivå 5. Lösningen visar först effektkvoten och sedan hur radien löses ut. | Mellanleden är förtydligade. Radien 3,44 solradier är korrekt. |
| 5.34 | Nivå 5. Lösningen visar effektkvoten och hur temperaturen beräknas. | Mellanleden är förtydligade. Temperaturen är cirka 5951 K. |
| 5.39 | a nivå 3, b nivå 5. Även fristående b-facit börjar med radie/temperatur. | Lösningen är kompletterad. Effekten är 6,88 gånger solens och magnituden +2,65. |

**Granskad – inget fel i tidigare numeriskt facit:** 5.30, 5.31, 5.32,
5.33, 5.34, 5.35, 5.39 och 5.42. De är ändå åtgärdade enligt tabellerna
ovan. I 5.41 var den tidigare kvoten cirka 34 korrekt och i 5.48 cirka
24, men de två gamla beräkningsfrågorna ersätts nu av begreppsfrågor.
Ingen rapport har stängts och inga kommentarer har skickats till elever.

## Pedagogik och bevarade beslut

- `FYSIK_FORMELSAMLING_2026-10-12.md` läst. Solens magnitud +4,74 och
  övriga nödvändiga modellvärden bevaras; det kommer inga nya uppmaningar
  att använda givna standardkonstanter eller färdiga formler i frågorna.
- Att magnituderna avser total strålning måste stå kvar för att kopplingen
  till total utstrålad effekt ska vara fysikaliskt riktig. Det uttrycks med
  vanliga ord i stället för ”bolometrisk”.
- 5.42 f behåller den uttryckliga förenklingen att alla fotoner räknas som
  632 nm. Det tidigare antalet är korrekt i denna modell. Lösningen gör
  inte anspråk på att beräkna ett verkligt bredbandigt stjärnspektrum.
- 5.42 a och c är direkta beräkningar och får nivå 2 även om de tillhör en
  svår heluppgift. b får nivå 4, d–f nivå 5. Varje del har egen ledtråd.
- Alla tio huvuduppgifter och deras delkort har miniräknare. Inget kort
  behöver digital grafanalys, avancerad integration eller liknande;
  GeoGebra är av. Nivån bedöms separat från hjälpmedlen.
- Rättningsmålen för de bevarade beräkningarna är oförändrade. 5.35 har
  fått fullprecisionsmål från en oberoende modell; A och B är ordnade
  svar med egna etiketter. Inga förväxlingsbara anonyma koordinatfält.
- För 5.30 a och 5.42 d efterfrågas nu en faktor. Svaret kräver därför
  inte ett svårt tangentbordstecken för solen som enhet.

## Verifiering

- `tools/fy2-astronomi-2026-10-22.test.js`: fyra grupper med självständig
  omräkning av magnituder, effekter, radier, temperaturer och fotonantal.
- `tools/fysik-formelsamling.test.js`: tre grupper godkända. Den tidigare
  rensningen av standardkonstanter och formeluppmaningar är skyddad.
- Konsumentens `tools/fy2-astronomi-2026-10-22.browser.cjs`: 174 kontroller
  i verkliga svarsfält, inklusive exakta/avrundade svar, felsvar, omkastade
  A/B-värden och samtliga valkombinationer i båda begreppsfrågorna.
- 40 elevvyer och 20 lärarvyer på 390/1280 px. Mobilöverflöde i två
  formler rättades med radbrytningar; slutkontrollen har inga överflöden
  eller KaTeX-/JavaScript-fel.
- Tre SVG-figurer granskas visuellt och geometriskt. Parallaxvinkeln
  ligger vid stjärnan, den räta vinkeln vid solen. Skalan i 5.48 visar
  −1,46 och +1,98 på rätt platser.
- Full bankvalidator: ERROR minskar 1539 → 1519 genom tio kompletterade
  verktygspar; WARNING 230 och INFO 1446 oförändrade. Inga nya fynd.
