# AI 1 · Felrapporter den 27 november

| Rapport | Ändring |
|---|---|
| 2.128 c | Formelblad på ett A4 med matematiskt satta formler och en klassificeringsmatris för TP, FP, TN och FN. LaTeX-källan ligger bredvid PDF-filen. |
| 2.127 a | Alla 30 övningar 2.123–2.152 har egna situationer. Frågorna om g, h och f varierar mellan att följa en väg, tolka en uppskattning och prioritera en ruta. Återkommande texter om BFS, DFS, spelträd och maskininlärning har också bearbetats. |
| 2.126 b | Samtliga 34 kartor med viktad terräng har minst träningsnivå 3 på varje delkort. Huvudnivå och E/C/A-poäng beräknas från delkorten. |
| 2.93 a | 185 kartor har fått avgränsade gångar. I 64 värdeuppgifter har sammanlagt 238 tidigare vita rutor blivit hela väggar. 1.105 och 1.106 använder öppet rutnät för resonemanget om R · C. |
| 2.92 a | Notisen om Manhattanavstånd ligger efter frågan på 373 delkort och en gång sist på vart och ett av 125 arbetsblad. 2.106 jämför tre olika heuristiker och behöver sina individuella definitioner. |
| 1.98 b | Den överflödiga meningen om barn och datastrukturer är borttagen även från den gemensamma inledningen. |

## Verifiering

Banken behåller alla ID:n och självrättningssvar. För nya hela väggar kontrolleras nåbarhet och kortaste vägkostnader till refererade rutor från både start och mål. Befintliga vägar i facit skyddas. Kartor med uttags- och köfrågor har samma förbindelser mellan rutornas mittpunkter. Testet för labyrinterna läser kartans rutor och jämför med delsvaren.

Samtliga huvuduppgifter och delkort har jämförts med sina tidigare verktygsval. De viktade kartorna tillåter miniräknare för kostnadsberäkningen och har GeoGebra avstängt. Regeln GeoGebra ⇒ miniräknare är uppfylld i hela AI-banken.

Slutredigeringen ingår i det befintliga sista byggsteget för nivåer. Upprepad körning ger en byteidentisk bank. Formelbladet byggs med pdfLaTeX via det befintliga Python-kommandot.

## Uppföljning · Hela rutor och sammanhängande gångar

Alla 187 kartor använder nu en kvadratisk platta per position och en mörk bakgrund, enligt rutprincipen i [AI-aktiviteters labyrintsimulering](https://github.com/davidhedengren/AI-aktiviteter/blob/main/sokalgoritmer-labyrinter/index.html). Bankens grön/röda start- och målmarkörer, rad- och kolumnnamn och terrängkostnader finns kvar.

13 kartor hade rutor utanför startens sammanhängande område. I 2.175 öppnar A2 passagen till övre högra gången. I 2.25 och 2.152 ansluts de avskilda lerrutorna. Överflödiga avskilda gångar har blivit väggar. I 1.08 prövas nu hur BFS stannar vid ett nåbart mål. Där räknas rutterna, uttagsordningen och lösningen med två korrekta alternativ om. Övriga facit och verktygsval behålls.

Regressionstestet söker från start i den publicerade SVG-figurens fyra grannriktningar och kräver att alla öppna plattor nås, även på det öppna rutnätet. Samma figur ska finnas på papper och elevkort.

## Uppföljning · Vad visar sökningen på kartan?

Varje labyrint har en följdfråga om en egenskap som går att undersöka på just den ritade kartan. Kartan används både på elevkort och arbetsblad. Facit visar uträkningen. På jämförelsekartorna kan eleven också följa vägarna bredvid varandra.

54 kartor har fått ny geometri. Varje sådan karta har högst två ställen där fyra gångrutor bildar en öppen kvadrat. I 1.83–1.90 skiljer eleverna på arbetet fram till målet och antalet steg i vägen som algoritmen hittar. I 1.89 besöker DFS 16 rutor och hittar en väg på 14 steg. BFS tar ut 19 rutor och hittar en väg på 10 steg. I 1.84 undersöker BFS färre rutor än DFS.

I 2.123–2.152 visas skillnaden mellan gångavstånd, terrängkostnad och uppskattat avstånd. På alla elva viktade kartor i serien hittar A* en längre väg med lägre totalkostnad än girig bäst först. I 2.126 skiljs vägarna åt vid D2. De har 11 respektive 13 steg och kostar 14 respektive 13. I 2.173–2.188 är de markerade kandidaterna en verklig ögonblicksbild ur girig bäst först. På åtta av kartorna får eleven byta urvalsregel i just det läget och se att A* väljer en annan kandidat.

De 54 ritningarna och markeringarna finns i `tools/ai-labyrintval.json`. JS-testerna tolkar publicerade SVG-rutor och kontrollerar vägkostnaderna, när kandidaterna ligger öppna och de nya självrättningssvaren. Samtliga 187 kartor kontrolleras för nåbarhet.
