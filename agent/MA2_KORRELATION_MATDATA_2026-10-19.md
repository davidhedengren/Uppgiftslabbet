# Ma2: korrelation i mätdata med GeoGebra – 2026-10-19

Önskemålet kom från Linnea Lundkvist, Erik Dahlbergsgymnasiet, 2026-10-15: ”Korrelation – fler uppgifter på A-nivå”. Hon vill ha uppgifter som liknar statistisk mätdata, där eleverna använder GeoGebra för att bestämma till exempel r eller jämföra två undersökningar.

**8 nya uppgifter, #4.376–4.383**, har lagts till för Ma2b och Ma2c. Området är `korrelation_koefficient`, som bara finns i 2b/2c. Uppgifterna ligger i ett nytt delmoment, **Korrelation i mätdata med digitala verktyg**, och ger **23 fristående kort** i Kunskapsgymmet. Huvudnivåerna är 7 A och 1 C. Delmomentet har 8 huvuduppgifter, vilket uppfyller minimikravet på 8.

## Uppgifterna

| ID | Sammanhang | Idé | Nivå (kort: nivå/träningsnivå) | Kontrollerat svar |
|---|---|---|---|---|
| #4.376 | Studietid och provpoäng i två klasser | Jämföra två undersökningar; sammanslagning ger negativt r | A (a–c E/2, d A/4) | 0,97; 0,87; −0,25; förklaring |
| #4.377 | Fart och bromssträcka | Högt r trots krökt samband; r mot \(v^2\) | A (a E/2, b C/3, c A/4) | 0,98; 1,00; bedömning |
| #4.378 | Längd och armspann, tio elever | Hitta ett troligt felinmatat värde och hantera det | A (a E/2, b C/3, c E/2, d A/4) | 0,82; elev 7; 0,99; hantering |
| #4.379 | Utetemperatur och elförbrukning per månad | Begränsat intervall (maj–sep) försvagar r | A (a–b E/2, c A/4) | −0,98; −0,64; förklaring |
| #4.380 | Två odlingsförsök | Nästan samma r men olika mönster; när passar en linjär modell? | A (a–b E/2, c A/4) | 0,90; 0,89; försök 1 |
| #4.381 | Solros, suddat mätvärde | Vilka heltal ger r ≥ 0,95? Både för små och för stora värden sänker r | A/5, ett kort | 12 cm och 18 cm |
| #4.382 | Elsparkcyklar och hemleveranser | Gemensam trend över tid, inte orsak | C (a E/2, b C/3) | 0,96; nej |
| #4.383 | Två termometrar i samma vattenbad | r ≈ 1 betyder inte överensstämmelse | A (a–b E/2, c A/4) | 1,00; 2,0 °C; nej |

### Matematisk kontroll och nivåmotivering

Alla r-värden är beräknade med Pearsons formel ur de tabeller som visas (numpy och Node-testet oberoende av varandra). Inget tvådecimalsfacit ligger närmare än 0,0012 en avrundningsgräns, så GeoGebra ger samma avrundning som facit. Mätvärdet för 110 km/h i #4.377 justerades vid kontrollen, eftersom r först låg 0,0008 från gränsen 0,985.

- **#4.376:** \(r_A\approx0{,}973\), \(r_B\approx0{,}871\). Alla 16 punkterna ger \(r\approx-0{,}251\). B studerade 8–17 h men skrev ett svårare prov (4–18 p), A studerade 2–9 h (14–35 p). Nivå: eleven ska förklara varför sammanslagna grupper kan byta tecken på r, vilket är A.
- **#4.377:** \(r(v,s)\approx0{,}983\), \(r(v^2,s)\approx0{,}9994\), \(s\approx0{,}0054v^2\). Ökningen per 10 km/h är 4–5 m vid låga farter och 10–13 m vid höga. Nivå: ny variabel \(v^2\) (C). Att värdera att ett högt r inte räcker för en linjär modell är A.
- **#4.378:** Alla tio ger 0,817. Utan elev 7 (177 cm, 157 cm) blir det 0,990. Nivå: att identifiera avvikelsen ur ett eget punktdiagram är C. Att värdera rättning, kontrollmätning eller borttagning är A.
- **#4.379:** Hela året ger −0,983. Maj–sep ger −0,641. Nivå: begränsat variationsintervall och andra påverkande faktorer, alltså resonemang på A-nivå.
- **#4.380:** 0,897 respektive 0,893. Försök 2 planar ut efter cirka 5 kg. Nivå: r avslöjar inte formen, så eleven måste värdera modellval utifrån diagrammet.
- **#4.381:** \(r\ge0{,}95\) gäller för \(11{,}32\le y\le18{,}42\), alltså heltalen 12–18. Kontroll: 11 ger 0,939, 12 ger 0,968, 18 ger 0,955 och 19 ger 0,943. Nivå: eleven måste själv välja undersökningsstrategi (glidare eller systematisk prövning) och upptäcka att r har ett maximum. Det är problemlösning, A/5.
- **#4.382:** r ≈ 0,964. Nivå: korrelation kontra orsak med en gemensam trend är C, eftersom resonemanget är välbekant från #4.180.
- **#4.383:** r ≈ 0,9996. Skillnaderna B − A summeras till 16,0, så medelvärdet är 2,0 °C. Nivå: att skilja mellan starkt linjärt samband och lika värden är begreppsligt A.

## Verktyg

Alla huvuduppgifter och kort har `geogebra:true` och `miniräknare:true`. Undantag: inga. Varje r-kort kräver statistikfunktion, och Kunskapsgymmets miniräknare saknar sådan. Resonemangskorten ger de r-värden som behövs, men eleven uppmanas i ledtråden att rita punkterna i GeoGebra. Därför har även de GeoGebra. Ledtrådarna hänvisar till regressionsanalys med två variabler i kalkylbladet, inte till ett kommandonamn, eftersom det svenska namnet på korrelationskommandot inte kunde bekräftas.

## Figurer

Varje uppgift har punktdiagram i facit: 9 unika figurer, och totalt 19 i huvudfacit och kortfacit. Figurerna ligger **inte** i uppgiftstexten. Önskemålet gäller just att eleven själv matar in data och ritar i GeoGebra, och en färdig figur skulle ge bort den delen (till exempel elev 7 i #4.378 eller kurvformen i #4.377/#4.380). Figurerna har vit bakgrund, mörka skalor, olika färg och form för grupper (cirkel/kvadrat), streckad referenslinje där det behövs och etiketter som inte överlappar.

## Svar och kort

Numeriska r-svar har tolerans 0,005 runt exakt r, så tvådecimalssvar, fler decimaler, decimalpunkt, minustecken och ”r=0,97” godtas. #4.383b har tolerans 0,05 och enheten °C. #4.381 har två ordnade, namngivna fält (Minsta höjd/Största höjd) i cm med tolerans 0.

Resonemangsdelarna är öppna frågor i Uppgiftslabbet. Som kort i Kunskapsgymmet är de flervalsfrågor med fyra alternativ och exakt ett rätt, enligt mönstret i #1.234. Varje resonemangskort anger själv de r-värden det bygger på, så korten är självbärande. Delfacit innehåller bara den egna delen.

## Verifiering

- Nytt test `tools/ma2-korrelation-matdata.test.js`, 5 tester. Det läser tabellerna ur `spelIntro` och räknar om varje r. Testet kontrollerar också metadata och arraylängder, avrundningsmarginaler, givna värden i resonemangskort, intervallet 12–18 och att figurpunkterna ligger inom ramen.
- Master: 82 tester i ma2-, statistik-, deluppgifts- och validatortesterna passerar. Kunskapsgymmet: 178 tester passerar.
- Bankvalidator Ma2: 4 ERROR, 131 WARNING och 96 INFO före och efter, alltså inga fynd på de nya ID:na. De 4 ERROR är de kända på #2.636/#2.637.
- Rättning i Kunskapsgymmets egen kod: alla 23 kort via `expandGameTask` och `delSvarRatt`. Rätt tvådecimalssvar godkänns och fel med 0,03 underkänns. ”2,0 °C”, ”12 cm”, ”r=0,97” och ”−0,251” godkänns, medan ”2,1” och ”11” underkänns. Alla alternativkort har exakt ett rätt alternativ.
- Kortvisning på 375 px: alla 23 kort med visat facit har inga KaTeX-fel, ingen horisontell överbredd och fungerande GeoGebra-knapp. Korten syns i spår 2b och 2c (23 vardera) men inte i 2a.
- SVG: alla 19 figurer kontrollerade i webbläsaren med `getBBox`. Ingen text hamnar utanför och inga etiketter överlappar punkter eller andra texter. Figurerna är också granskade visuellt. `tools/granska-svg.js` kunde inte köras klart på `Hedav`, eftersom Chrome-anropet fick timeout (`spawnSync … ETIMEDOUT`). Det beror på miljön, inte på figurerna.
- Strukturerad jämförelse: de 2190 tidigare Ma2-objekten är oförändrade, och banken har nu 2198 objekt med unika ID:n. Bankkopiorna är byteidentiska. I Kunskapsgymmet ändras bara `BANK_VERSION` till `2026-10-19-ma2-korrelation-matdata`.

## Observation utanför uppdraget

#4.300a ber eleven bestämma r med två decimaler men har `geogebra:false` på både uppgift och delkort. Kunskapsgymmets miniräknare saknar statistikfunktion, så kortet bör sannolikt få GeoGebra. Ledtråden nämner LinReg på räknaren. Detta är **inte ändrat**, eftersom bankgranskningen är pausad.

## Kommentarsförslag till önskemålet

> 8 nya uppgifter (#4.376–4.383) med mätdata för Ma2b/2c finns i ett nytt delmoment, Korrelation i mätdata med digitala verktyg. Eleverna bestämmer r i GeoGebra och jämför undersökningar: två klasser, två odlingsförsök, hela året och bara sommaren. De hittar också ett felinmatat värde, ser varför ett högt r inte räcker för en linjär modell och skiljer samband från orsak och från överensstämmelse. Sju är A-uppgifter. Punktdiagram finns i facit.
