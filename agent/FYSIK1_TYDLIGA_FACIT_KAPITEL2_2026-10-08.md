# Fysik 1: tydliga uppgifter och facit, första omgången

Användarens prioritering 2026-10-08: pausa Fysik 2, mato2 och övriga uppdrag. Börja den manuella fysikgranskningen i kapitel 2, rätta 3.172 direkt, ta bort numrerade lösningssteg och visa de beräkningar som slutsvaren bygger på.

## Utfört

- 3.172 har separata stycken för a) och b). Facit visar båda reaktionssträckorna, bromssträckan, båda stoppsträckorna, avståndet som återstår för bromsning och farten vid hindret. Beräkningarna har kontrollerats oberoende. Lösningen är vanlig förklarande text med beräkningar och slutsvar.
- Den genererade stegnumreringen har tagits bort i hela Fysik 1: 3715 huvuduppgifter och deras delkort. Vid denna presentationsändring kontrollerades att exakt text, formler och SVG bevarades, bortsett från de genererade siffermarkörerna. Delbokstäver och deras ordning finns kvar. Övriga bankers presentation har inte ändrats.
- Kapitel 2:s 365 huvuduppgifter har lästs med sina facit: enheter, densitet, mätning och medelfart. Konkreta redaktionella ändringar finns i JSON-rapporten. Automatisk presentation skiljs där från innehållsändringar. Frågor och separata Kunskapsgymmet-kort har reviderats där de behöver egna förutsättningar, bättre språk, rätt enheter eller tydlig avrundning.
- Felaktigt formaterade enheter, särskilt g/cm³, har rättats. Formatteringsverktyget har en spärr mot att göra enheterna till lösa variabler. Det verifierade motsvarande felet i 6.64 har också rättats.
- Facit för rörelseproblemen 2.291–2.320 har utvecklats individuellt: varför farter adderas/subtraheras, vilket tidsintervall som avses, omvandlingar, ekvationer och relevanta mellanled. Bland annat har 2.307b förtydligats till tiden efter B:s start, 2.315a anger 120 km åt varje håll och 2.320 avser mottagna pulser. 3.234 hade motstridiga referenssystem i texten; gångfarten anges nu relativt rullgången.
- Avrundade svar och toleranser har anpassats i berörda uppgifter. Några exakta beräkningar hade toleranser som även accepterade felaktiga närliggande värden; dessa har rättats efter individuell bedömning.
- Nivåerna har justerats bland annat för enkla densitetsresonemang, beräkning av en kubs sida och flytkraftsproblem. De självständiga delkorten har bedömts separat. Varje område i kapitel 2 har fortfarande enkla nivå 1-uppgifter.
- Felrapporterna 5.142, 5.160a och 5.209b är rättade; se den separata felrapportloggen.
- Ett fel i Kunskapsgymmets symboliska rättning av vetenskaplig notation har rättats. Exempelvis ska 2e27 tolkas som ett tal, inte som 2 gånger Eulers tal plus 27. Bankkontrollen hittade tidigare felaktiga godkännanden av stora, felaktiga tal.

## Verifiering

- Oberoende numeriska beräkningar av 185 svar i 133 kapitel 2-uppgifter, med givna data transkriberade separat från lösnings-HTML. Därtill riktade tester av bland annat stoppsträckor, upphinnande, strömfart och ljudpulser.
- Alla 4977 aktiva Fysik 1-kort körda genom Kunskapsgymmets faktiska rättningsfunktioner: 13966 kontroller, inga fel i dessa kontroller. De täcker facitsvar, enheter och avvisning av avvikande tal; riktade kompletteringar täcker relevanta avrundningar och tidsintervall.
- Alla 3715 huvuduppgifter och deras texter, facit, ledtrådar och delkort har renderats med KaTeX i båda apparna. Inga formelfel hittades. Även manuella läraruppgifter som 3.172 ingår.
- 3.172 har inspekterats visuellt med appens CSS i 1174 px och 390 px bredd: deluppgifterna ligger på egna rader och ingen stegnumrering eller sidövergripande horisontell överströmning finns.
- 140 mastertester godkända, inklusive 47 figurtester. 64 konsumenttester godkända.
- Fysik 1-validator: 0 ERROR, 8 WARNING och 655 INFO. De osäkra befintliga fynden redovisas som granskningspunkter, inte som bevisade fel.
- Samtliga ursprungliga SVG i huvuduppgifterna är identiska med utgångsläget. Inga figurer har ritats om i denna omgång.

## Fortsatt manuell granskning

Kapitel 3–9 återstår för motsvarande innehållsgranskning. Att deras facit har fått en ny presentation och passerat tekniska kontroller innebär inte att alla deras formuleringar och pedagogiska mellanled är färdiggranskade. Den här omgången ska inte beskrivas som att hela banken är felfri.

Reproducerbara kontroller: `tools/fysik1-kapitel2.test.js`, `tools/fysik1-prosa.test.js`, `tools/fysik-felrapporter-2026-10-08.test.js`, formatterarens regressionstester och `tools/fysik1-prosa.browser.py`. Browserkontrollen körs mot startade lokala appar; portarna kan anges med `--teacher-port` och `--student-port`.
