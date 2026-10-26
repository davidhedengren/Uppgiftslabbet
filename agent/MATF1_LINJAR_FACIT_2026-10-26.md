# Matf1: linjär approximation – manuell områdesgranskning 2026-10-26

**39 huvuduppgifter / 48 träningskort granskade. Alla 39 har förbättrats. Granskad – inget fel: inga.** Matematiska metoder och slutsatser stämde i de äldre faciten, men flera saknade mellanled eller hade olämpliga rättningskontrakt. Detta är ett helt område, inte en färdig manuell helbanksgranskning.

## Fynd, jämförelser och beslut

- Alla huvudfacit och samtliga 14 delkort i 3.312/313/314/316/317 har manuellt författade, uppgiftsspecifika rubriker, beräkningsled, slutsvar och ledtrådar. Irrelevanta mallråd i bland annat 3.18/43/99 är ersatta. Jämförelser av samma mönster omfattar hela området, särskilt 3.07/26/41/42/63/65.
- Rättningen ska använda **tangentens approximation**, inte den ursprungliga funktionens exakta värde. Snäva numeriska bastoleranser ersätter ospecificerade/breda toleranser. Konsumentens befintliga regel för fri avrundning används fortfarande när frågan inte anger precision. Kontrollerade jämförelser: 3.18/26/42/279/315/326/328. 3.315 får inte godkänna den icke-linjära ekvationens rot i stället för den linjära ekvationens lösning.
- 3.07, 3.42, 3.313b, 3.316a/b och 3.317b lagrar oavrundade referenser. 3.192/196 visar nu fyra decimaler som frågan kräver, och toleransen är en halv enhet i sista decimalen. Rätt grannavrundning och fel grannavrundning är testade. 3.286b ska vara 100, inte 95.
- 3.78 använder uttrycksformat eftersom tangentfunktionen efterfrågas; 1, L(x)=1, f(x)=1 och y=1 godtas. 3.283 kräver inte bråkform och använder numeriskt format med fullvärdet 1/6; även korrekta decimalavrundningar godtas. Befintlig policy för procentandel utan procenttecken bevaras: 0,04 kan motsvara 4 %, medan 0,04 % inte är 4 %. Ingen generell rättningsregel är ändrad.
- 3.316b är fristående med 18,93 °C och 1,01 °C/h givna. Facitet använder dessa värden. Huvudfacitet beräknar i stället T(6) ur modellen och använder oavrundad derivata. Båda ger 19,2 °C. Enheterna °C/h och °C är separata. Även 3.324/325/326 får uttrycklig enhetsmetadata (V/°C/%).
- Nivåbedömning: 3.08 blir C/nivå 4 (approximation plus motiverad felbedömning); 3.286 blir C/nivå 3 (felmodellen h² är given). 3.312a blir nivå 2 eftersom derivata, funktionsvärde och linje kräver flera led. Fristående 3.316b blir E/nivå 2 med givna värden. Övriga nivåer behålls efter kontroll; enkla kort med given lutning, exempelvis 3.118/119/120/277/278, är fortfarande nivå 1.
- Miniräknare tillåts nu i 3.07/42/192/196 för mer besvärliga divisioner. 3.316/317 har redan räknare. Övriga kort använder enkla exakta tangentvärden; i 3.08/313/314 är beräkning utan räknare ett uttryckligt metodsyfte. GeoGebra är avstängt: eleverna ska använda tangentmetoden, inte ersätta den med digital funktionsvärdering. Detta beslut gäller detta område och är inte en generell regel för derivatauppgifter.
- 3.43 bedöms fortfarande manuellt; 3.08 har automatisk taldel och manuell motivering. Ingen påhittad automatisk resonemangsbedömning har införts.
- Alla 12 befintliga SVG-figurer är visuellt kontrollerade: kurvor, tangenter, tangentpunkter, tabellvärden, texter och kvadratens ändrade sida stämmer. Figurerna är oförändrade. Uppgifternas variation från granskningen 2026-10-14 är bevarad. Formelrader har delats manuellt där de blev för breda på mobil.

## Alla granskade uppgifter och föreslagna kommentarer

Alla nedan är **åtgärdade**; det betyder även pedagogiska förbättringar, inte att alla hade felaktiga numeriska svar. Statusar och kommentarer finns i repot. Inga elevrapporter har avslutats i Supabase och inga kommentarer har skickats.

| ID / delar | Status | Kommentar att använda |
|---|---|---|
| #3.07 | Åtgärdad | Facit visar tangentpunkt, lutning och insättning. Rättningen använder 91/30 utan mellanavrundning och godtar rimligt avrundade svar. Miniräknare tillåts. |
| #3.08 | Åtgärdad | Facit förklarar varför logaritmens avtagande lutning ger en för stor approximation. Nivå 4. Talet 0,04 självrättas; motiveringen bedöms fortfarande manuellt. |
| #3.18 | Åtgärdad | Facit visar den negativa ändringen −0,2 och hela beräkningen till 3,975. Korrekt avrundning 3,98 godtas, men 3,97 gör det inte. |
| #3.26 | Åtgärdad | Facit visar varför lutningen är 1/8 och hur den ger 4,0375. Formlerna ryms på mobil. Figuren är kontrollerad. |
| #3.41 | Åtgärdad | Facit visar derivatans minustecken och hur ökningen i x sänker tangentens värde till 0,49. |
| #3.192 | Åtgärdad | Facit svarar nu med de fyra decimaler som efterfrågas: 7,0286. Rättningen skiljer korrekt avrundning från grannvärdet 7,0285. Miniräknare tillåts. |
| #3.42 | Åtgärdad | Facit visar kubikrotens derivata och värdet 271/90. Rättningen utgår från full precision; exempelvis 3,01 och 3,01111 godtas. Miniräknare tillåts. |
| #3.43 | Åtgärdad | Den irrelevanta ledtråden är ersatt. Lösningen förklarar att kvadratrotens avtagande lutning gör tangentens uppskattning för stor. Fortsatt manuell bedömning. |
| #3.63 | Åtgärdad | Facit visar varför sin 0 = 0 och cos 0 = 1 ger tangentlinjen y = x. Vinkeln räknas i radianer. |
| #3.64 | Åtgärdad | Facit visar att både startvärdet och lutningen är 1, innan 0,03 sätts in. |
| #3.65 | Åtgärdad | Facit skiljer konstruktionen av tangentlinjen x−1 från beräkningen av uppskattningen 0,08. Båda svarsfälten är kontrollerade. |
| #3.78 | Åtgärdad | Rättningsformatet är anpassat till att en funktion efterfrågas. Både 1, L(x)=1 och y=1 godtas. Facit förklarar den vågräta tangenten. |
| #3.196 | Åtgärdad | Facit svarar nu med fyra decimaler: 7,0143. Rättningen utgår från det oavrundade tangentvärdet och avvisar 7,0142. Miniräknare tillåts. |
| #3.99 | Åtgärdad | Irrelevanta råd om potens- och logaritmlagar är borttagna. Facit visar derivatan 1/10 och höjdändringen 0,04. |
| #3.116 | Åtgärdad | Facit visar tangentlinjen och insättningen av 1,05. Grafens logaritm, tangent och tangentpunkt stämmer. |
| #3.118 | Åtgärdad | Facit använder den givna lutningen och visar båda beräkningsleden till 2,025. Nivå 1 behålls. |
| #3.119 | Åtgärdad | Facit visar ändringen 0,03 och använder den givna lutningen. Nivå 1 behålls. |
| #3.120 | Åtgärdad | Facit skiljer höjdändringen 0,05 från startvärdet 1, som ska adderas. Nivå 1 behålls. |
| #3.277 | Åtgärdad | Facit visar 0,6/12 = 0,05 och därefter 6,05. Den givna lutningen gör uppgiften lämplig för nivå 1. Tabellen är kontrollerad. |
| #3.278 | Åtgärdad | Facit förklarar varför negativ ändring gånger negativ lutning ger ökning. Svaret är 12,3. Tabellen är kontrollerad. |
| #3.279 | Åtgärdad | Facit visar hur kubikrotens derivata ger 1/12 vid 8, och därmed uppskattningen 2,025. |
| #3.280 | Åtgärdad | Facit använder den redan givna linjen och förklarar minustecknet i −0,03. Grafen är kontrollerad. |
| #3.281 | Åtgärdad | Ledtråden och facitet klargör att x är positivt 0,04 medan minustecknet redan finns i funktionen. Svaret 0,96 och grafen stämmer. |
| #3.282 | Åtgärdad | Facit visar derivatan −1/x² och hur tangentens värde blir 0,98. |
| #3.283 | Åtgärdad | Frågan kräver inte bråkform. Rättningen godtar nu både 1/6 och korrekt avrundade decimaler, exempelvis 0,17 och 0,1667. |
| #3.284 | Åtgärdad | Facit visar hur tangentpunkten (1,0) sätts in i y=x+c och ger c=−1. |
| #3.286 | Åtgärdad | Facit visar båda avstånden och kvadraten av deras kvot. Nivå 3 eftersom felmodellen är given. För grov tolerans på svaret 100 är borttagen. |
| #3.312 a, b, c, d | Åtgärdad | Alla fyra delar har egna facit med funktionsvärde, derivata och tangentekvation. Del a är nivå 2. Ekvivalenta tangentuttryck godtas. |
| #3.313 a, b | Åtgärdad | Båda delkort visar val av tangentpunkt och hela beräkningen. Del b rättas mot 49/24 och avrundas till 2,042. |
| #3.314 a, b, c, d | Åtgärdad | Alla fyra delkort visar hur exponent och ändring identifieras, inklusive negativa tecken och kubikrotens exponent. |
| #3.315 | Åtgärdad | Facit skiljer den linjära ekvationen från den ursprungliga. Svaret är 1,125; det icke-linjära närmevärdet 1,127 godtas inte som lösning till den nya ekvationen. |
| #3.316 a, b | Åtgärdad | Facit visar kedjeregel, radianer, enheter och tidsomvandling. Del b har egna givna temperatur- och lutningsvärden och är nivå 2. Huvudfacitet räknar från modellen utan mellanavrundning. |
| #3.317 a, b | Åtgärdad | Facit visar tangentens konstruktion och båda temperaturerna före beräkningen av relativt fel. Referensvärdet behåller full precision; svaret avrundas till 0,8 %. |
| #3.324 | Åtgärdad | Facit visar ändring i mm, ökning i V och den uppskattade signalen 7,3 V. Svarsfältet har rätt enhet. |
| #3.325 | Åtgärdad | Facit visar tidsändringen och temperatursänkningen till 49 °C. Svarsfältet har rätt enhet. |
| #3.326 | Åtgärdad | Facit visar areans derivata, uppskattad areaökning och omvandling till procent. Svaret är 4 %, inte den exakta areaökningen 4,04 %. Figuren har kontrollerats. |
| #3.327 | Åtgärdad | Facit visar hur höjdändringen divideras med lutningen innan 4 adderas. Svaret är x≈4,3. Tabellen har kontrollerats. |
| #3.328 | Åtgärdad | Facit visar att ändringen är −0,05 och ger tangentvärdet 3,8. Figuren och tangentpunkten är kontrollerade. |
| #3.329 | Åtgärdad | Facit förklarar varför en vågrät tangent ger 0 även om funktionens värde är 0,008. Alla fyra alternativ har nu egna kommentarer. Figuren är kontrollerad. |

## Verifiering

- Oberoende symbolisk/numerisk kontroll av tangentvärden, ekvationer, konkavitet, relativa fel, enheter och referensprecision för alla 39 huvuduppgifter / 48 kort: godkänd.
- **570 rättningskontroller** i Chromium på mobil och dator: 560 genom vanliga svarsfält/flervalsknappar och 10 av automatdelen i blandat bedömda 3.08. Rätt svar, ekvivalenta uttryck, rätt/fel grannavrundning, enheter och fel metods svar ingår. Samtliga passerade. Manuell motivering har inte räknats som automatisk bedömning.
- **96 elevvyer och 106 lärarvyer** renderade på 390 och 1280 pixlars bredd, utan LaTeX-fel eller för breda formelrader. Alla 12 SVG-figurer samt utvalda komplexa mobilfacit visuellt inspekterade.
- Befintlig regression från 2026-10-14: 6 tester godkända, inklusive tio varierade approximationer. Föregående områdes 44 integrationskontroller är fortsatt godkända.
- Matf1:s bankvalidator: **0 ERROR, 8 WARNING, 67 INFO**, oförändrat mot föregående runda. Dessa äldre varningar gäller andra granskningspunkter; inga nya validatorfynd skapades. En helbankskörning visar dessutom 1479 befintliga ERROR utanför denna Matf1-runda (1477 verktygsmetadata i Fy2, två områdesreferenser i Mato2); de är inte manuellt lösta eller verifierade av denna runda.
- Semantisk diff: exakt de 39 redovisade huvuduppgifterna ändrade; inga ID:n tillagda/borttagna. Installationsskriptet är idempotent. Bankfilerna i master och konsument är byteidentiska. Git diff --check passerade.

Skydd: `tools/matf1-linjar-facit-2026-10-26.test.py` och det manuellt författade `tools/revidera-matf1-linjar-facit-2026-10-26.py`. Konsumenten har `tools/matf1-linjar-facit-2026-10-26.cases.json`, som körs med `tools/ma3-facitstruktur-2026-10-25.browser.cjs`, `REVIEW_COURSE=matf1` och ID-listan i granskningsloggen. Browserharnessen stöder nu flerdelade specialfall och blandad bedömning; dess tvådecimalsprov använder avrundning som inte rundar 2,025 nedåt på grund av binär representation. Ingen generell produktionsrättare ändrad.

Ändrade produktionsfiler: `uppgiftermatf1.js` i båda repona och cacheversion i respektive `index.html`. Övriga filer är granskningslogg, inventering och tester. Andra checkouters pågående arbete är lämnat orört. Inga ändringar av produktionsdata eller rapportstatusar.

Parallell Ma3/Ma4-leverans integrerad före push (master 85fd9cd, konsument a92c58a). Enda konflikten var konsumentens cacheversion, som nu omfattar båda rundorna. Båda bankflyttarna och fem nya Ma3-kort bevarades. Efter rebase passerade tangenttestet, regressionssviten från 2026-10-14, Ma3/Ma4-flyttens test och bankjämförelsen. Inventeringen är uppdaterad till 21475 huvuduppgifter.
