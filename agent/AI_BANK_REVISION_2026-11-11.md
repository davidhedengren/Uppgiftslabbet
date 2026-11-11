# AI: korta frågor, SCEN-figurer och köuppgifter

Användarens uppföljning ersätter föregående layoutbeslut: minimera frågetext,
färgmarkera start/mål utan bokstäver, använd deluppgifter och SCEN:s trianglar.

## Ändrat

AI 1.01–1.02, 2.01–2.03, 3.01–3.03: korta a–d-frågor. Endast nödvändig
ordning, heuristik och viktinformation står kvar. Ingen förklaring om diagonaler,
upptäcktmarkering, köinläggning eller upprepning av synliga lövvärden.

Grön start (#22a05a), rött mål (#d94343), färgförklaring i varje labyrint;
inget S eller G i rutorna. Mörka rutlinjer bevaras. Spelträden har uppåtriktad
MAX-triangel, nedåtriktad MIN-triangel och namn utanför noderna. Referens:
SCEN:s `scripts/build-minimax-visuals.py`, funktionerna för v3-figurernas
trianglar och symbolförklaring. Färgerna är anpassade för vit pappersbakgrund.

Fem nya uppgifter: 1.03 FIFO/stack, 1.04 BFS-kö, 1.05 DFS-stack, 2.04
prioritetskö och 2.05 g/h/f samt val av nästa ruta. Inspirerade av uppladdade
övningsblad. Totalt 13 uppgifter och 39 deluppgifter.

Varje del har egen fråga, facit, ledtråd, nivå och verktygsmetadata.
`spelIntro` bär den gemensamma figuren och förutsättningarna. Ingen del
kräver ett osynligt tidigare svar. Uppgifterna är fortsatt manuellt bedömda
med `spel:false`; ingen konsumentsynkronisering eller automatisk rättning
har aktiverats. Miniräknare är tillåten, GeoGebra behövs inte. Huvudpoängen
är summan av delarnas poäng. Antalsfrågor har nivå 2 även inom svårare uppgifter.

## Kontroller

Oberoende simulering av BFS, DFS, A*, UCS, alfa–beta, FIFO/LIFO och
prioritetskö. Befintliga algoritmtester bevarade. Utökade kontroller av
samtliga delkort, färgförklaring och triangelrepresentation.
Bankvalidator: inga fynd i AI-banken. Browserprov: 13 kort, 39 facit och
10 figurer renderade. Mobilbredd och print-media provade. Enkla matematiska
regler skrivs med vanliga tecken i facit så att de även visas utan extern
matematikrenderare. De äldre bankerna är inte redigerade.

Ändrade filer: uppgifterai.js, strukturai.js, tools/ai-bank-2026-11-11.test.js
samt denna logg, beslutsregistret och GRANSKNINGSLOGG.md.
