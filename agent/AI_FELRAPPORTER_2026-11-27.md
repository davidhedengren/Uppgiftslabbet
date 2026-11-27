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
