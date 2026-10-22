# Fysik 1: manuell kontroll av 14 densitetsuppgifter

De första 14 numeriska huvuduppgifterna i områdets källordning har granskats:
32 fristående träningskort. Detta är inte hela densitetsbanken.

| ID | Beslut |
|---|---|
| 2.2 | Oförändrad. Kubvolymer, densitet och uppskalad massa stämmer. Precisionen verifierad. |
| 2.8 | Oförändrad. Anpassad linje ger 8,5 g/cm³. Figur och avläsning fungerar. |
| 2.17 | Volymkort utan irrelevant massa, även i figuren. Egna ledtrådar och tydligare lösningar. |
| 2.18 | Fullvärde 300/(200/8,96+100/7,14), tolerans 0,005. Två decimaler bevaras. Svarsenhet och mobilformel förbättrade. |
| 2.26 | Volymkort utan massa; massomvandling utan sidlängd. Egna ledtrådar. Två rekommenderade värdesiffror i a/c/d; b är ren enhetsomvandling. |
| 2.27 | Fullvärden för folietjocklek och lagerantal, tolerans 0,5. Tre värdesiffror bevaras. Atomlagrets tjocklek tas bort ur a. B får hela lösningen. |
| 2.31 | Oförändrad. Graf, fyra svar och avläsningstoleranser stämmer. |
| 2.38 | Två rekommenderade värdesiffror från volymen 0,25 m³. Fulla mål 1967,5 kg och 1,9675 ton bevaras. Förklarande lösningar. |
| 2.39 | Oförändrad. Linjen ger 40 g respektive 2 g/cm³. |
| 2.42 | a–c blir nivå 1: ett direkt densitetssamband med miniräknare. d behåller nivå 2 med två enhetsomvandlingar. Egna ledtrådar. |
| 2.274 | Fullvärde 4π/3·(2,70·8+7,80·19), tolerans 0,05. En decimal bevaras. Ny genomskärning och förklaring av kärna/skal. |
| 2.52 | Fullvärden för volym/radier; toleranser 5/0,005/0,005. Tre värdesiffror bevaras. C är ett eget 30 kg-sammanhang. Fullständiga lösningar. |
| 2.53 | Svarsenhet och lösning förtydligas. Skiljer volymandelar från massandelar. 8210 kg/m³ oförändrat. |
| 2.54 | Fullvärden 450/8,96 och 8,96·27; toleranser 0,05/0,5. Tre värdesiffror bevaras. Förklaringar och egna ledtrådar. |

Samma feltyp följs upp i fem uppgifter: 2.18, 2.27, 2.274, 2.52, 2.54 hade
avrundade maskinfacit med noll tolerans. Nu godtas efterfrågat avrundat
slutsvar och korrekt beräkningsvärde enligt befintlig precisionsrättning.
Felaktiga angränsande avrundningar testas. Inga uttryckliga krav tas bort.

Alla 32 kort tillåter miniräknare; GeoGebra behövs inte. Färdiga grafer läses
av, inte anpassas digitalt. E/C/A-poäng behålls. 2.42abc kräver ett direkt
grundsamband och flyttas därför till nivå 1; övriga träningsnivåer behålls.
Geometrikorten behåller figurerna; 2.274 får en genomskärning. Rena
enhetsomvandlingar och massa/volymkvoter behöver ingen dekorativ bild.

±2-regeln införs på ytterligare fem manuellt kalibrerade kort: 2.26acd,
2.38ab. Diagramavläsning och enhetsomvandling får inte automatiskt samma
regel. Tvetydiga heltalsnollor i andra äldre data får ingen gissad precision.
Hela fysikbanken är ännu inte färdigkalibrerad.

Verifiering: 10 riktade mastertester, inklusive kapitel 2:s oberoende
beräkningar. 236 svarsfältskontroller och 64 kortvisningar på 390/1280 px.
Mobilkontrollen hittade en överlång formel i 2.18; den rättades och testades
igen (8 svar, 2 visningar). Inga JavaScript- eller KaTeX-fel. Bankvalidatorn:
840 fynd före/efter, inga nya. De åtta befintliga varningarna ligger kvar.
SVG-kontrollen använder validatorns egna funktioner i Playwright eftersom
Chrome-CLI inte fungerar i molnet. Befintliga sneda måttlinjer i 2.17/2.26
ger samma varning före/efter; bilderna är visuellt granskade. Ny figur i
2.274 kontrolleras separat och etiketten placeras fri från cirkellinjerna.

Inga rapportstatusar eller kommentarer ändras i produktion. Master synkas
identiskt till Kunskapsgymmet och båda bankversionerna höjs.
