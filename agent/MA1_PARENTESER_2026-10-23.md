# Ma1: mängdträning med parenteser på nivå 3–5

Användaren önskade betydligt fler svårare uppgifter i **ekv_parenteser**.
Området hade 49 huvuduppgifter: 25 på nivå 1, 15 på nivå 2, sex på nivå 3,
två på nivå 4 och en på nivå 5. Efter denna omgång finns **64**:
25 / 15 / 12 / 8 / 4 på nivå 1–5. Alla nya kort gäller 1a, 1b och 1c.

Samtliga äldre texter i området lästes för variationsjämförelse. Särskilt
1.43, 1.116, 1.1114, 1.1115, 1.1116, 1.1124, 1.1193 och 1.1198 gav
jämförelsepunkter för nivå och metod. Det är inte en ny fullständig
facitgranskning av dessa äldre kort; inga av dem ändras.

## Alla nya och detaljgranskade uppgifter

| ID | Nivå | Innehåll | Facit | Föreslagen kommentar |
| --- | --- | --- | --- | --- |
| 1.1386 | 3/C | Tre parenteser, x i båda leden | x=9 | Ny rutinuppgift med flera parenteser och negativa faktorer. |
| 1.1387 | 3/C | Minus framför inre parentes | x=13 | Ny träning på att förenkla inifrån och hålla reda på tecken. |
| 1.1388 | 3/C | Tre olika nämnare | x=−13 | Ny uppgift där hela täljarna måste följa med när nämnarna tas bort. |
| 1.1389 | 3/C | Decimala faktorer | x=7,25 | Ny rutinuppgift med decimaltal; korrekt avrundade svar godtas också. |
| 1.1390 | 3/C | Parenteser inne i parenteser | x=0,8 | Ny uppgift där minustecknet påverkar två termer. |
| 1.1391 | 3/C | Bråk och fristående konstantterm | x=−4 | Ny uppgift där även konstanttermen måste multipliceras när nämnarna tas bort. |
| 1.1392 | 4/C | Två nästlade parentesuttryck | x=−5 | Ny svårare rutinuppgift med negativa faktorer på flera nivåer. |
| 1.1393 | 4/C | Parenteser i två bråktäljare | x=4 | Ny uppgift som kombinerar täljarförenkling och ekvationslösning. |
| 1.1394 | 4/C | Subtrahera en hel parentesprodukt | x=5,5 | Ny träning på att byta alla tecken efter utveckling av den andra produkten. |
| 1.1395 | 4/C | Flera nämnare och dubbla minus | x=35/18 | Ny uppgift med exakt bråksvar; ekvivalenta bråk godtas. |
| 1.1396 | 4/C | Förlängd rektangel, skillnad mellan areor | x=6 cm | Ny figuruppgift som kan lösas med två areauttryck eller remsans bredd. |
| 1.1397 | 4/C | Återskapa k ur en felaktig elevlösning | x=10 | Ny felanalys: k=18 hittas först, sedan löses originalekvationen. |
| 1.1398 | 5/A | Två konstanter, likhet för alla x | b=2 (a=5) | Ny parameteruppgift där både koefficient och konstantterm måste stämma. |
| 1.1399 | 5/A | Två ekvationer med samma lösning | a=4/13 | Ny kombinationsuppgift: uttryck a ur den första och sätt in i den andra. |
| 1.1400 | 5/A | Ändra en konstant så att x minskar med 1 | 8/3 ersätter 5 | Ny uppgift om hur en konstant styr lösningen, efter förenkling av nästlade bråk. |

Tio direkta ekvationer ger mängdträning. Övriga fem ger modellering,
felanalys och parameterresonemang. Nivå 5 grundas på att eleven behöver
kombinera villkor eller resonera om hur en lösning förändras; stora tal
ensamma motiverar inte nivån. Inga andragradsmetoder behövs: kvadrattermerna
i 1.1394/1.1396 försvinner och 1.1399 kan lösas genom enkel insättning utan
att en allmän metod för ekvationssystem förutsätts.

Vanlig miniräknare tillåts i alla 15. GeoGebra behövs inte och skulle
ersätta det symboliska arbete som tränas. Tre uppgifter begär exakt svar
och använder `bråk`: 1.1395, 1.1399, 1.1400. Övriga följer befintligt beslut
om godtagbara avrundningar utan dolt precisionskrav; exempelvis godtas både
7,25 och 7,3 i 1.1389, medan 7,2 är fel avrundat. Prefix som x=, a= och b=
fungerar i de faktiska svarsfälten. För 1.1396 godtas 6 och 6 cm men inte 6 m.

1.1396 har en egen SVG med korrekt placerade mått. Vid facits x=6 är
ursprungsrektangeln 5×8 och den tillagda remsan 7×8; figuren har motsvarande
proportioner. Övriga 14 är symbolisk mängdträning eller algebraisk felanalys.
En extra bild skulle inte ge användbar information och har därför utelämnats.

## Utfall och skydd mot återkommande fel

**Alla granskade:** de 15 nya ID:n som listas i tabellen.
**Åtgärdade äldre uppgifter:** inga.
**Konstruktionsjusteringar:** långa rader i 1.1392, 1.1398 och 1.1400
delades för mobilvisning. Samma överflödeskontroll gjordes för alla 15;
bland jämförelserna 1.1386, 1.1388, 1.1393, 1.1395, 1.1396 och 1.1399
fanns inga överflöden. Figurens två måttlinjer i 1.1396 är separata SVG-paths,
så att geometrikontrollen inte misstolkar mellanrummet som en sammanhängande linje.
**Granskad – inget fel efter slutkontroll:** alla 15. Kommentarsförslag finns
per ID ovan. Inga felrapporter markeras avslutade i tjänsten.

## Verifiering

- Fyra nya testgrupper: metadata, tio oberoende ekvationsmodeller,
  area/felanalys och parameterfallen. Alla godkända.
- Sex tidigare testgrupper för Ma1-ekvationer och parentesuttryck fortsatt godkända.
- 144 riktiga svarskontroller, 30 elevvyer och 30 lärarvyer vid 390/1280 px.
  Inga JavaScript-, KaTeX- eller överflödesfel i slutkontrollen.
- Full validator: ERROR 1485 → 1485, WARNING 230 → 230, INFO 1444 → 1445.
  Det nya INFO-fyndet jämför 1.1394 med äldre 1.1116. Båda har produkter
  med kvadrattermer som försvinner. Här tillkommer minus framför en hel
  utvecklad produkt; detta är en avsiktlig, avgränsad rutinvariation i den
  efterfrågade mängdträningen, inte en serie med enbart utbytta tal.
- Areabilden kontrollerad visuellt på mobil och med SVG-validatorns regler.
- Bankkopiorna är identiska; inga äldre Ma1-objekt ändrade.

Skydd: `tools/ma1-parenteser-2026-10-23.test.js` och Kunskapsgymmets
`tools/ma1-parenteser-2026-10-23.browser.cjs`.
