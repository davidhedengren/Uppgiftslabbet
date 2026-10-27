# Ma4: flöden och integraler

Sex uppgifter om volym och flöde har granskats: 3.95, 3.105, 3.106,
3.470, 3.121 och 3.248. Faciten visar hur flöde summeras till volym;
irrelevanta generella råd om vinklar och längdenheter har tagits bort.

| ID | Oberoende kontroll och ändring |
|---|---|
| 3.95 | Delareorna under grafen är 300, 400 och 100 liter: totalt 800 liter. Facit skiljer rektangel, trapets och rektangel. |
| 3.105 | Grafens delareor är 80, 120 och 60 liter: totalt 260 liter. Facit visar beräkningen för varje tidsintervall. |
| 3.106 | Nettoflödet är \(18+5t\) och \(V=50+18t+2,5t²\). Den positiva roten till \(V=300\) är cirka 7,028264 min. Rättningsmålet använder den beräknade roten i stället för 7,03; facit förklarar även varför volymen bara passerar 300 liter en gång. |
| 3.470 | Nettoflödet är \(6+2t\). Integralen under fem minuter ger 55 liter. |
| 3.121 | Grafens delareor är 90, 180 och 135 liter, totalt 405 liter. |
| 3.248 | \(V(t)=-10t+t²+(120/\pi)(1-\cos(\pi t/6))\). Kandidaternas nettovolymer och båda ändpunkterna jämförs; största värdet är cirka 52,63 m³ efter 6,237 timmar. Formler i fråga och facit har delats upp för mobilvisning. |

Graferna i 3.95, 3.105 och 3.121 har granskats visuellt och stämmer med
beräkningarna; inga figurer har ändrats. Nivåer och verktygsval är
oförändrade. Alla sex tillåter miniräknare; 3.470 har inte GeoGebra tillåtet
och övriga fem tillåter båda. 3.105 och 3.248 är manuellt bedömda.

Uppgiftslabbet visade sex uppgifter i 2c. Kunskapsgymmet kontrollerade 60
svarsförsök och tolv vyer på mobil och dator; korrekta avrundningar, svar med
enhet och rimliga felsvar ingick. En för bred fråga och formel i 3.248
delades därefter upp och kontrollerades igen på båda bredderna; mobilvyn
granskades visuellt. Bankkopior, syntax och diff har kontrollerats.
Författarkällorna `tools/ma4-flode-facit-2026-10-27.py` och
`tools/ma4-flode-mobil-2026-10-27.py` förutsätter den dåtida bankversionen.
Svarstester finns i konsumentens `tools/ma4-flode-2026-10-27.cases.json`.
Inga rapportstatusar har ändrats i produktionsdatabasen.
