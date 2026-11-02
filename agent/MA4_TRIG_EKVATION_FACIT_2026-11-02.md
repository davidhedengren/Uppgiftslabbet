# Ma4: trigonometriska ekvationer och delfacit, 2 november 2026

## Ändrade uppgifter

- **1.16 a–d, 1.68 a–d och 1.69 a–d:** lösningarna förklarar nu grundvinklar och perioder. Varje del anger att \(n\) är ett heltal; det saknades tidigare i flera delfacit.
- **1.132 a–c:** lösningarna förklarar referensvinkel och vilka kvadranter som ger rätt tecken inom intervallet. Lärarfacit har delats upp tydligt.
- **1.299 a–d:** facit visar först isoleringen av den trigonometriska funktionen och därefter hur vinklarna väljs. I d förklaras varför både \(+1/2\) och \(-1/2\) behövs.

Sammanlagt **19 delfacit** och fem helfacit har förbättrats. Uppgifter, svar, rättningsmetadata, nivåer och verktygstaggar är oförändrade. Ekvationernas vinklar och perioder har kontrollerats matematiskt.

## Liknande granskade uppgifter

- **1.09 a/b:** granskade – inget motsvarande fel i de granskade delarna; referensvinkel och kvadranter förklaras.
- **1.22 a/b och 1.65 a/b:** granskade – svaren i de granskade delarna stämmer, men motiveringarna är korta och kan förbättras.
- **1.68 och 1.69 a–d:** samma brist med \(n\) upptäcktes och åtgärdades i denna omgång.

## Tester och rapportkommentar

Banktester kontrollerar parametrarnas heltalsvillkor och vinkelsvaren genom insättning. I Kunskapsgymmet visas samtliga 19 delfacit på mobil och dator. De sju lösningsmängderna i 1.132 och 1.299 rättas också i omvänd ordning; de tre automatiskt rättade periodiska svaren i 1.16 provas separat. Delfacit med manuell självbedömning testas för visning, inte som automatiskt rättade. I Uppgiftslabbet öppnas samtliga fem helfacit och KaTeX-visningen kontrolleras. Mobilvisningen av en dellösning har granskats visuellt. Även föregående trigonometriomgångs webbläsartest körs som regression. Hela testsviter körs före push.

Förslag till rapportkommentar: ”Tack! Lösningen visar nu hur referensvinkeln och tecknet används och anger vad parametern \(n\) betyder.” Ingen rapportstatus eller kommentar har sparats i appen.

Testutfall: de riktade bank- och webbläsartesterna passerade. Hela sviten gav 1 068 godkända och 43 tidigare kända SVG-miljöfel i Uppgiftslabbet samt 304 godkända och 10 tidigare kända fel i Kunskapsgymmet. Vid en snabb inmatning i flera rutor kunde appens fördröjda autofokus flytta fokus tillbaka till den första rutan och sammanfoga två svar. Det är ett separat UI-problem som behöver åtgärdas; rättningstestet inväntar därför att den första fokusflyttningen är klar.
