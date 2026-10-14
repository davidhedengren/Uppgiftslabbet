# Nivårapporter 2026-10-14 16:44–16:45

## Rapporterade uppgifter

| Kurs/ID | Beslut | Kommentar till rapportören |
|---|---|---|
| Fy1 4.536 b | Träningsnivå 2 → 3, E → C, 1 C-poäng. a behåller E/nivå 2. Hela uppgiften C, 1 E + 1 C. | Tack! Det fristående b-kortet kräver både bromsrörelse och friktionsmodell och ligger nu på nivå 3. |
| Fy1 4.669 b | Träningsnivå 3 → 4. C och poäng behålls. a/c:s nivåer ändras inte. Parentens träningsnivå blir 4. | Tack! Del b ligger nu på nivå 4 eftersom eleven måste hålla isär tre krafter och riktningen i det kopplade systemet. |
| Ma2 3.489, 2b/2c | A/nivå 4 → C/nivå 3; poäng 0/1/2 → 0/2/0. | Tack! Detta är en likformighetsuppgift med en andragradsekvation, inte A. Den är omklassificerad till C. |
| Ma2 3.498 a–b, 2b/2c | A/nivå 4 → C/nivå 3; poäng 0/1/2 → 1/2/0. | Tack! Den givna likformighetsmodellen kräver inte A-resonemang. Uppgiften ligger nu på C, med E-poäng för den första proportionen. |
| Ma2 3.531, 2b/2c | AC:s 6 cm står nu nära själva AC-sidan inne i figuren, inte som en rad under cirkeln. E/nivå 2 och poäng behålls. | Tack! Måttet 6 cm är flyttat till sidan AC i figuren. |

De tidigare rapporterna om 3.192, 3.197, 3.143 och 3.386 är redan åtgärdade
av föregående commit och har inte ändrats i denna omgång.

## Självständig bedömning

4.536 b är fristående: a:s retardation är inte given. Eleven måste först
bestämma b = 4²/(2·15) och därefter beskriva bromskraften med Newtons andra lag
och μmg, inklusive att massan förkortas bort. Detta modellbyte motiverar nivå 3;
höjningen beror inte enbart på antalet aritmetiska steg. μ ≈ 0,054311.

4.669 b anger accelerationen 4,22 m/s² men kräver en egen kraftmodell för B:
mg och den undre snörkraften verkar nedåt, den övre snörkraften uppåt.
B följer C nedåt, vilket ger 1·g + 50,4 − S = 1·4,22 och S = 56 N.
Given acceleration gör det onödigt att lösa hela två-/trekroppssystemet igen.
Nivå 4 är därför rimlig; nivå 5 skulle överskatta just detta delkort.

3.489: x/(x+5)=4/x ger x²−4x−20=0, alltså x=2+2√6≈6,90 cm.
Likformighet och pq-formeln behöver kombineras, men inget generellt eller
ovanligt bevis krävs. Det är C/nivå 3.

3.498: a ger H=1,8·6,4/2,4=4,8 m. I b är avståndet 6 m och
s/(6+s)=1,8/4,8, vilket ger s=3,6 m. Den första delen är rutinmässig och
får E-poäng; den andra kräver att samma modell används med ett nytt okänt.
Två sammanhängande beräkningar gör inte uppgiften till A.

3.531: diameter 10 cm och AC 6 cm ger rät vinkel vid C och BC=√(100−36)=8 cm.
Figurens AC/diameter-förhållande är 0,6 och BC/diameter-förhållandet 0,8.
Sidorna, vinklarna och måtten har inte ändrats, bara måttetikettens placering.

## Ytterligare bekräftade nivåfel

| ID | Ändring | Motivering och oberoende svar |
|---|---|---|
| Fy1 4.533 | E/2 → C/3, 2 C-poäng | Samma inverse modell som 4.536 b: bromsrörelsen ska ge ett okänt friktionstal. μ=20²/(2·112·9,82)≈0,181844. |
| Ma2 3.487 | A/5 → C/3, 2 C-poäng | VV-likformighet ger AB²=AD·AC=36, AB=6. Ett geometriskt samband ska identifieras, men inget A-bevis krävs. |
| Ma2 3.488 | A/5 → C/3, 2 C-poäng | Areaskala 1/2 ger längdskala 1/√2, CD=12/√2≈8,49 cm. |
| Ma2 3.491 | A/5 → C/4, 3 C-poäng | Ytterbisektrisser ger BPC=(B+C)/2=(180−40)/2=70°. Beviset kräver en generell koppling men är en kort vinkelsummekedja, inte A/5. |
| Ma2 3.492 | A/4 → C/3, 2 C-poäng | Pythagoras ger (4+y²)+(16+y²)=36, y=±2√2. Den vanliga andragradsekvationen motiverar inte A. |
| Ma2 3.497 | A/5 → C/4, 2 C-poäng | Likformiga trianglars höjder har förhållandet 3:1, summan är 8. Höjden mot AB är 6 och arean 36 cm². Modelleringen är mer krävande än direkt proportion men inte A/5. |

Detta är begränsad omklassificering efter rapporterna, inte en ersättning med
nykonstruerade A-uppgifter. Texternas innehåll, numeriska facit, toleranser och
uppgifts-ID bevaras. Lägre poäng/nivå ska motsvara den befintliga uppgiften.

## Jämförelser och kvarstående bedömningar

Minst fem jämförelser per feltyp har lästs. Alla huvudtexter, berörda delkort,
facit och verktygstillstånd kontrollerades. Följande ändras inte:

- Fy1 4.530 a–b: given retardation ger direkt kraft och μ=b/g; mindre modellbygge än 4.536 b.
- Fy1 4.531 och 4.532: givet μ gör rörelsemodellen direktare; E/nivå 2 behålls.
- Fy1 4.534 a–b: dragkraft, friktion, nettokraft och rörelse; C/nivå 3 behålls.
- Fy1 4.537 a–c: bromsmodell och km/h-omvandling; träningsnivå 3 behålls.
- Fy1 4.662 a–b, 4.663, 4.664 och 4.668: kopplade kroppar med lutning,
  friktion, okänd massa eller flera rörelsefaser; nivå 4 är motiverad.
- Fy1 4.665 a–d: kopplingskrafter med givet R ger enklare delsystem än tre
  hängande vikter utan figur; nivåerna ändras inte.
- Fy1 4.670: kopplad rörelse, snörets slack, stopp vid golvet och fortsatt
  kast kräver flera modeller och ett geometriskt villkor; nivå 5 behålls.
- Ma2 3.499: vinkelsökning med flera likbenta deltrianglar kräver egen
  geometrisk kedja (basvinklar 36°, toppvinkel 108°); A/nivå 5 behålls.
- Ma2 3.490: vinkelsumman ska gälla alla tillåtna femuddiga stjärnor;
  generellt resonemang motiverar fortsatt A/nivå 5.
- Ma2 3.500: cirkelfyrhörning och vinkelsummor; C/nivå 3 behålls.
- Ma2 3.532, 3.533, 3.534, 3.535 och 3.536: jämförda figurer och
  måttetiketter har rätt sida/referens; ingen motsvarande etikettflytt behövs.

Alla lästa ID: Fy1 4.530–4.534, 4.536–4.537, 4.662–4.665, 4.668–4.670;
Ma2 3.487–3.492, 3.497–3.500, 3.531–3.536. Totalt 30 huvuduppgifter.
De elva ändrade huvudposterna finns med komplett före/efter-data i JSON-loggen.

## Verktyg

Fysikens huvuduppgifter och delkort tillåter miniräknare. GeoGebra behövs inte
för dessa kraftberäkningar. Samtliga ändrade algebra-/likformighetsuppgifter
tillåter miniräknare för rötter och avrundning; digital grafanalys behövs inte.
3.531 behåller miniräknare:false: 10²−6²=64 och √64=8 är enkel exakt
8–6–10-aritmetik, medan den geometriska satsen är huvudmomentet. Inga
verktygstillstånd ändras i denna omgång.

## Kontroller

- Uppgiftslabbet: 376/376 tester utanför den allmänna SVG-sviten godkända,
  inklusive 17 riktade tester med oberoende kraft- och geometriberäkningar.
- Kunskapsgymmet: 167/167 Node-tester godkända.
- Browser: 60 rättningskontroller med riktiga svarsfält. Rätta numeriska/exakta
  svar godtas och fel svar underkänns; verkligt expanderade kort ger avsedda
  träningsnivåer, inklusive 4.536 b=3 och 4.669 b=4.
- Alla berörda kort renderade på mobil och dator: inga KaTeX-fel eller rå kod,
  korrekt antal svarsfält, inga JavaScript-runtimefel.
- SVG-granskning av 3.531 före/efter ger inga fynd; figuren även visuellt granskad.
- Inga matematiska svar eller toleranser ändrade. De tidigare bankversionerna
  var identiska mellan repona; ändrade bankfiler synkas och kontrolleras igen.
