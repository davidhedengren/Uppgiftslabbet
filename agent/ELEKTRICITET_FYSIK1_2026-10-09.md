# Fysik 1 – elektricitet, manuell runda 2026-10-09

Denna logg omfattar 152 granskade uppgifter: alla 30 i ström, alla 60 i potential, alla 23 i seriekoppling, alla 26 i parallellkoppling, 8.73 om influens, nio Coulombuppgifter (8.302–310) och tre nya uppgifter. Kapitel 8 innehåller nu 517 uppgifter. Återstående 365 uppgifter är **inte** markerade som färdiggranskade. Hela Fysik 1 omfattar 3738 uppgifter. Tidigare laddningsgranskning finns i `LADDNING_FYSIK1_2026-10-09.md`.

## Resultat och beslut

134 befintliga uppgifter ändrade; 15 granskade utan ändring; 3 nya. Ändring kan avse pedagogik, nivå, figur eller svarskort även när fysiksvaret redan var korrekt.

- 8.78, 8.79, 8.197 och 8.199 hade felaktiga rättningsvärden. De räknas nu från givna data.
- 8.49 hade batteriets polaritet felritad. Ledningsglapp i 8.140 och åtta seriefigurer repareras. I 8.244/246/248 gick en ledning genom batteriet; den delas vid polerna.
- Namngivna numeriska resultat ska rättas i bestämd ordning. Delkort får `svarsstruktur: "ordnad"` och egna `svarEtiketter`. Övriga rotmängder fortsätter godta valfri ordning.
- Fullständiga slutsvar, enheter och mellanled ersätter slutrader som bara gav det sista av flera värden. Följdkort får egna nödvändiga givna värden.
- Rutinmässig serieberäkning blir nivå 1–2. Mätarbelastning och kombinerad förändring av lampkrets ligger på nivå 3. Avancerade Kirchhoffsystem och fria resonemang bevaras.
- Batteriets Ah-märkning beskriver kapacitet, inte nettoladdning. Ny 8.517 tränar detta med figur. 8.515–516 tränar energi och oförändrad potential från en SVG-graf.
- Långa likhetskedjor bryts på flera rader. Ingen numrerad steglista införs. Äldre CSS-klass `facit-stegvis` är inte obligatorisk; regressionstesten kräver fortsatt `facit-v2`, inga nummersteg och kvarvarande delbokstäver.

## Följduppgifter för samma felmönster

| Felmönster | Minst fem jämförelser |
|---|---|
| Ofullständiga slutsvar/fält | 8.49, 8.103, 8.117, 8.149, 8.150, 8.40, 8.55, 8.131, 8.132, 8.135, 8.138 |
| Delkort saknar tidigare resultat | 8.116, 8.165, 8.31, 8.50, 8.118, 8.145, 8.167, 8.89, 8.135 |
| Onödigt hög nivå | 8.197, 8.199, 8.273, 8.284, 8.285, 8.146, 8.151, 8.392, 8.396 |
| Batterifigur/anslutning | 8.49, 8.103, 8.116, 8.117, 8.147, 8.140, 8.244, 8.246, 8.248, 8.40, 8.62, 8.64, 8.85, 8.89 |
| Mobilens långa formelkedjor | 8.257, 8.259, 8.280, 8.284, 8.286, 8.287, 8.290, 8.292, 8.293, 8.393, 8.468, 8.469 |

## Kontroller

- 112 tester för Fysik 1 och bankvalidatorn i masterrepo samt samtliga 96 tester i Kunskapsgymmet passerar.
- 47 praktiska numeriska UI-försök, inklusive korrekta avrundningar, fel tecken och fel ordning; 47 alternativförsök passerar.
- 201 kort i fyra vyer (390 och 1174 px, ljust och mörkt): 804 visningar utan sidöverflöde, breda facitformler eller KaTeX-fel. 340 tekniska svarskontrakt passerar.
- Kortkontrakt prövar lagrade svar och tydligt felaktiga värden. Dessa är teknisk kontroll, inte ersättning för oberoende fysikgranskning.
- 66 SVG-figurer körda i geometrikontroll. Tre varningar gäller A inuti amperemetersymbolen; visuell kontroll visar att cirkelns vita bakgrund döljer ledningen bakom. Åtta INFO gäller avsiktlig bakgrund vid figurkanten, 8.244–251. Verkliga kollisioner i 8.249–251 har åtgärdats och omkontrollerats.
- Bankvalidator: 0 fel, samma 8 varningar som före rundan; de ligger utanför ändringarna. Validatorn accepterar nu uttryckligt bokstavsmappade delmängder av spelkort, med regression som fortsatt varnar för felaktig eller tvetydig mappning.
- 271 kort från samtliga 152 granskade uppgifter kontrolleras i fyra vyer (1084 visningar), inklusive 502 svarskontrakt: inga fel. Läraruppgifternas sammansatta facit har också fått giltig HTML-blockstruktur.
- Rapportstatus i Supabase ändras inte av Git-push. Kommentarerna nedan är förslag för rapporthanteringen.

## Fortsatt manuell runda: parallellkoppling och begreppsvariation

- Alla 26 parallelluppgifter är granskade. 8.16/19/91/136/142/155 får kompletta, namngivna svar och egna rättningsfält. 8.17:s tidigare saknade enheter rättas. Korrekt fri motivering behåller manuell komplettering, men rena talfrågor rättas automatiskt.
- 8.141 anger strömmen i gemensam information; den fanns förut bara i a trots att b/c behövde den. 8.42 b får eget värde och mellanled. 8.51 d godtar 160 Ω, 8.250/251 godtar 2,1/1,8 A.
- Parallellfigurerna 8.16/19/41/42/51/91/137/141/155 får hela batterianslutningar. 8.245/247/249/250/251 får avbrott mellan batteriplattorna. Maskerna i 8.103/136 förkortas så att de inte döljer anslutningen till plattorna.
- 8.73 saknade elektroskopets utgångsladdning. Det anges nu att det är oladdat med slutna blad. En ny SVG visar negativ stav, metallkula och blad utan att avslöja laddningarna i facit. Spelkort a förenar orsak och laddning; b utelämnas där eftersom a:s facit annars avslöjar svaret. Lärarbladets a/b/c och samtliga tre facit bevaras. Spelkort c har egen nödvändig bakgrund och rätt metadata från originalets c-index.
- Coulombgruppen 8.302–310 får enkla formuleringar och nödvändiga omvandlingar. 8.304 godtar 0,22 N, 8.306 godtar 27,5 cm och 0,275 m men avvisar 27,5 m. Nivå 1 tränar direkta begrepp och förändringsfaktorer; rutinberäkningar med enhetsomvandling ligger på nivå 2.
- Fyra nästan likadana Coulombberäkningar ersätts av olika uppgiftstyper på samma ID: 8.306 avstånd ur kraft, 8.307 Newtons tredje lag, 8.308 jämförelse av uppmätta krafter vid dubbelt avstånd, 8.309 två laddningsförändringar som tar ut varandra. Fyra tydliga SVG-figurer tillkommer. Utgångsläget i figuren anges där storheter sedan ändras.
- För fem eller fler jämförelser används grupperna 8.16/19/91/136/142/155 (namngivna svar), 8.51/137/139/141/142/155 (enheter och egen information), 8.245/247/249/250/251 (batterianslutningar) och 8.302/304/305/306/308/310 (Coulombberäkning och avrundning). Influens jämförs med tidigare dokumenterad laddningsrunda, särskilt 8.503–507; det räknas inte som en ny fullständig granskning av dessa ID:n i denna logg.


## Alla granskade uppgifter

| ID | Status | Kontroll/resultat och förslag till kommentar |
|---|---|---|
| 8.103 | Åtgärdad | Åtgärdad: del b:s slutsvar saknade R₁:s spänning. Namngivna fält för 4 och 8 V, rätt enheter, självständiga delkort och nivå 1–2. Andra figurkontrollen: batteriets vita täckruta krymps till avståndet mellan polerna så att ingen liten ledningslucka döljs. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.110 | Åtgärdad | 42 C, cirka 2,62·10²⁰ elektroner; mellanled och korrekta ledtrådar. |
| 8.116 | Åtgärdad | Åtgärdad: batteripolaritet och ström 0.03 A är rätt. Spänningskortet får strömmen angiven och nivå 1, utan behov av svaret från föregående kort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.117 | Åtgärdad | Åtgärdad: tre efterfrågade effekter får tre märkta svarsfält och fullständig energibalans. Strömmen finns uttryckligen på effektkortet. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.118 | Åtgärdad | Åtgärdad: alla beräkningar är rätt, men slutsvar a saknade I₁ och slutsvar b var bara I₃. Kompletta slutsvar och givna strömmar på kontrollkortet. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.12 | Åtgärdad | Åtgärdad: energin 2,0 GJ var rätt. Delkort b anger egen energi och facit använder ett konkret 1 kW-exempel. Molnhöjd och modell ges i c. Fria förklaringar markeras som manuell komplettering, så numerisk träff inte godkänner resonemang automatiskt. Långa beräkningskedjor radbryts för mobilvisning. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.124 | Åtgärdad | Åtgärdad: begreppskortet får självrättande alternativ. 300 Ω och 0,030 A är korrekta. Varje självständigt kort är enkelt nog för nivå 1. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. |
| 8.125 | Åtgärdad | Åtgärdad: korrekt ersättningsresistans 115 Ω saknade rättning. Alla tre kort får rättning och nivå 1–2; begreppskortet kontrollerar att strömmen är lika. |
| 8.128 | Åtgärdad | Åtgärdad: lika spänningsdelning kräver likadana lampor, vilket nu anges. Konstant resistans behövs för modellen vid kortslutning. 11,5 V och cirka 176 Ω får rättning; förklaringskortets slutsvar besvarar frågan. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.129 | Åtgärdad | Åtgärdad nivå: härledningen är rätt och bevaras som fri läraruppgift. Samma spänning, strömsumma och Ohms lag räcker; nivå 3/C är rimligare än 5/A. |
| 8.131 | Åtgärdad | Åtgärdad: facit skrev felaktigt 5/10 = 50 %. Nu visas 0,50 och omvandling till procent. Alla tre delspänningar och procent får rättning och egna data; nivå 1–2. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.132 | Åtgärdad | Åtgärdad: båda delspänningar 4,5 och 7,5 V får märkta fält och komplett slutsvar. Kontrollkortet är självständigt med egna spänningar och förklarade alternativ. Nivå 1–2. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.135 | Åtgärdad | Åtgärdad: effektkortet saknade den okända resistorns värde och slutsvaret innehöll bara en effekt. Eget värde, två märkta fält och korrekt fullständigt facit. Nivå 2. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.136 | Åtgärdad | Åtgärdad: lampornas effekt anges vid 12 V. Båda spänningarna, strömmarna och resistanserna får märkta svarsfält. Egen beräkning per kort utan tidigare delresultat. Nivå 1–2. Andra figurkontrollen: batteriets vita täckruta krymps till avståndet mellan polerna så att ingen liten ledningslucka döljs. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.137 | Åtgärdad | Åtgärdad: sista resistanssvaret saknade rättning. Varje följdkort visar egen beräkning av tidigare ström/resistans. Rätt resultat 30 mA, 15 mA, 800 Ω och 266,7 Ω; nivå 2. Fri kontroll i d bevaras. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.138 | Åtgärdad | Åtgärdad: båda delspänningarna får rättning och fullständigt slutsvar. Strömmen ges på spänningskortet. Enkla kort nivå 1–2, inte C/3. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.139 | Åtgärdad | Åtgärdad: strömsvaret är konsekvent i mA även i facit. Härledning av resistans på eget kort och enkel förklaring utan HTML-entiteter i matematik. Nivå 2, fri motivering endast i c. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.140 | Åtgärdad | 24,3 mA och 3,65 V korrekta. a självrättas; b får egen given ström och c namnger R₁ och har alternativ. Inga onödiga manuella kompletteringar. Figurens nedre batteriledning ansluts hela vägen till batteripolen. |
| 8.141 | Åtgärdad | Åtgärdad: strömmen fanns bara i a, men behövdes även i b/c. Den läggs i gemensamt underlag. Två spänningar bevaras i uttrycklig ordning med märkta fält. Nivå 1 för given U/I, 2 för spänningsfall, 3 för okänt parallellvärde. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.142 | Åtgärdad | Åtgärdad: parallellvärden räknade från 12 V och [100, 150] Ω. Alla efterfrågade grenstorheter har fullständiga slutsvar, märkta fält och enheter. Varje del visar egen beräkning; nivå 1–2. Fria motiveringar/två metoder kräver manuell komplettering där de efterfrågas. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.143 | Åtgärdad | Åtgärdad: rätt enheter för energi och fart. Sista delen frågar tydligt efter fartkvoten och rättar den, inte bara protonens fart. Eget energiunderlag på fartkortet. Nivå 1, 2 respektive 3. Självrättningen godtar även den korrekta avrundningen 43. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.144 | Åtgärdad | Åtgärdad: även strömriktningen kontrolleras. Ny jordpunkt ger två ordnade svarsfält för A och B. Facit visar hur båda potentialerna ändras. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.145 | Åtgärdad | Åtgärdad: strömmarna och laddningseffekten 0,160 W är rätt. Facit visar insättning och lösning av systemet samt alla tre strömmar. Effektkortet anger sin ström. Långa beräkningskedjor radbryts för mobilvisning. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.146 | Åtgärdad | Åtgärdad: rutinberäkningar låg felaktigt på nivå 5. Nivå 1–2, tre självrättande kort med tydliga enheter och egna givna värden. Energi, fart och procent jämförs i korta facit. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.147 | Åtgärdad | Åtgärdad: ström och riktning är rätt. Numerisk rättning kontrollerar storleken; manuell komplettering krävs uttryckligen för riktningen, så 20 mA inte ensam räcker för hela svaret. |
| 8.148 | Åtgärdad | Åtgärdad: del c får numerisk rättning med korrekt negativ potential. Varje kort visar egen beräkning av ström och spänningsfall. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.149 | Åtgärdad | Åtgärdad: båda spänningarna och båda polpotentialerna får ordnade, namngivna numeriska fält. Negativ potential för minuspolen förklaras utan hänvisning till föregående kort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.150 | Åtgärdad | Åtgärdad: strömriktningen ingår i rättningen och omjordningen får tre märkta fält. Nivå 1 för enkla potentialskillnader, nivå 2 för övriga kort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.151 | Åtgärdad | Åtgärdad: begreppskort har förklarade svarsalternativ. Läraruppgiften ber fortfarande om potentialvandringen; spelkortet rättar strömmen och visar hela ekvationen. Två delspänningar får egna fält. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.152 | Åtgärdad | Åtgärdad: energisvaren var rätt. Antaganden för halvvägsarbete anges i frågan, positiv laddning finns på eget kort och vägoberoendet avgränsas till det stillastående fältet. Nivå 2 i stället för 5. Fri motivering bevaras som läraruppgift. Långa beräkningskedjor radbryts för mobilvisning. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.155 | Åtgärdad | Åtgärdad: parallellvärden räknade från 6 V och [100, 200, 200] Ω. Alla efterfrågade grenstorheter har fullständiga slutsvar, märkta fält och enheter. Varje del visar egen beräkning; nivå 1–2. Fria motiveringar/två metoder kräver manuell komplettering där de efterfrågas. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.16 | Åtgärdad | Åtgärdad: parallellvärden räknade från 5 V och [100, 1000] Ω. Alla efterfrågade grenstorheter har fullständiga slutsvar, märkta fält och enheter. Varje del visar egen beräkning; nivå 1–2. Fria motiveringar/två metoder kräver manuell komplettering där de efterfrågas. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.165 | Åtgärdad | Åtgärdad: batteripolaritet och ström 0.03 A är rätt. Spänningskortet får strömmen angiven och nivå 1, utan behov av svaret från föregående kort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.166 | Åtgärdad | Åtgärdad: 4 och 8 V är rätt, men frågan saknade svarens ordning och del b:s slutsvar gav bara 8 V. Båda anges med placering. Enkel begreppsuppgift nivå 1–2; fri förklaring bevaras. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.167 | Åtgärdad | Åtgärdad: beräkningarna är rätt. Facit visar ekvationslösning, alla strömmar och korrekt jämförelse utan HTML-kod i matematiken. Följdkorten innehåller egen ström respektive nodspänning. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.17 | Åtgärdad | Åtgärdad enheter och nivå: 60 mA före, 120 Ω och 100 mA efter, fortfarande 60 mA genom första resistorn. Tidigare saknades samtliga svarsenheter. En fri motivering i d ska kontrolleras manuellt; övriga kort rättas direkt. |
| 8.19 | Åtgärdad | Åtgärdad: parallellvärden räknade från 6 V och [200, 300] Ω. Alla efterfrågade grenstorheter har fullständiga slutsvar, märkta fält och enheter. Varje del visar egen beräkning; nivå 1–2. Fria motiveringar/två metoder kräver manuell komplettering där de efterfrågas. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.191 | Åtgärdad | 2,3 A ska också godtas när båda givna värdena har två värdesiffror. Toleras nu tillsammans med 2,34 A. |
| 8.197 | Åtgärdad | Direkt Q=It ger 135 C; E/nivå 1 i stället för C/3, relevanta avrundningar godtas. |
| 8.199 | Åtgärdad | Direkt Q=It ger 126 C; E/nivå 1 i stället för C/3, relevanta avrundningar godtas. |
| 8.20 | Åtgärdad | Åtgärdad nivå och facit: 150 Ω, 7,5 V och 250 Ω är rätt. Nivå 1–2 i stället för 3, och R₂-kortet visar hur dess spänning beräknas. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.244 | Åtgärdad | Åtgärdad figur: resistansberäkningen och nivå 1 är rätt, men en ledning var ritad genom batterisymbolen och kortslöt den. Ledningen delas vid de två batteripolerna. Facit förklarar konkret varför resistanserna adderas. |
| 8.245 | Åtgärdad | Åtgärdad pedagogik: rätt ersättningsresistans 3.4285714285714284 Ω. Facit visar insatta resistansvärden och hur svaret fås, i stället för en allmän instruktion utan beräkning. Nivå 2 behålls. Ledningen genom batterisymbolen delas så att batteriet inte ritas kortslutet. |
| 8.246 | Åtgärdad | Åtgärdad figur: resistansberäkningen och nivå 1 är rätt, men en ledning var ritad genom batterisymbolen och kortslöt den. Ledningen delas vid de två batteripolerna. Facit förklarar konkret varför resistanserna adderas. |
| 8.247 | Åtgärdad | Åtgärdad pedagogik: rätt ersättningsresistans 5.454545454545454 Ω. Facit visar insatta resistansvärden och hur svaret fås, i stället för en allmän instruktion utan beräkning. Nivå 2 behålls. Ledningen genom batterisymbolen delas så att batteriet inte ritas kortslutet. |
| 8.248 | Åtgärdad | Åtgärdad figur: resistansberäkningen och nivå 1 är rätt, men en ledning var ritad genom batterisymbolen och kortslöt den. Ledningen delas vid de två batteripolerna. Facit förklarar konkret varför resistanserna adderas. |
| 8.249 | Åtgärdad | Åtgärdad nivå och facit: totalström 12/8 + 12/12 = 2.5 A är rätt. Grenströmmar gör metoden tydligare; två rutinberäkningar på nivå 2, inte C/3. Ledningen genom batterisymbolen delas så att batteriet inte ritas kortslutet. Spänningsetiketten flyttas bort från batteripolerna efter geometrikontroll. |
| 8.250 | Åtgärdad | Åtgärdad nivå och facit: totalström 12/10 + 12/14 = 2.057142857142857 A är rätt. Grenströmmar gör metoden tydligare; två rutinberäkningar på nivå 2, inte C/3. Ledningen genom batterisymbolen delas så att batteriet inte ritas kortslutet. Spänningsetiketten flyttas bort från batteripolerna efter geometrikontroll. |
| 8.251 | Åtgärdad | Åtgärdad nivå och facit: totalström 12/12 + 12/16 = 1.75 A är rätt. Grenströmmar gör metoden tydligare; två rutinberäkningar på nivå 2, inte C/3. Ledningen genom batterisymbolen delas så att batteriet inte ritas kortslutet. Spänningsetiketten flyttas bort från batteripolerna efter geometrikontroll. |
| 8.257 | Åtgärdad | Kontrollerat värde 11.5 µJ. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Tolerans korrigerad så rätt svar med två värdesiffror godtas. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.258 | Åtgärdad | Kontrollerat värde 10.8571 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.259 | Åtgärdad | Kontrollerat värde 4.75 µC. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.26 | Åtgärdad | 18 mC / 4,0 s = 4,5 mA. E/2, enhet och tolerans är korrekta. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.260 | Åtgärdad | Begrepp kontrollerat: volt = J/C, positiv/negativ laddning ger rätt tecken på energiändringen, och dubblerad laddning ger dubblerad energiändring. |
| 8.261 | Åtgärdad | Kontrollerat värde 15.5 J. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Tolerans korrigerad så rätt svar med två värdesiffror godtas. |
| 8.262 | Granskad – inget fel | Kontrollerat värde 7.5 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.263 | Åtgärdad | Begrepp kontrollerat: volt = J/C, positiv/negativ laddning ger rätt tecken på energiändringen, och dubblerad laddning ger dubblerad energiändring. |
| 8.264 | Åtgärdad | Begrepp kontrollerat: volt = J/C, positiv/negativ laddning ger rätt tecken på energiändringen, och dubblerad laddning ger dubblerad energiändring. |
| 8.265 | Åtgärdad | Begrepp kontrollerat: volt = J/C, positiv/negativ laddning ger rätt tecken på energiändringen, och dubblerad laddning ger dubblerad energiändring. |
| 8.266 | Åtgärdad | Kontrollerat värde 7.42857 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.267 | Åtgärdad | Kontrollerat värde 10.8 J. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Tolerans korrigerad så rätt svar med två värdesiffror godtas. |
| 8.268 | Åtgärdad | Kontrollerat värde 4.28571 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.269 | Åtgärdad | Kontrollerat värde 0.06 J. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.270 | Åtgärdad | Begrepp kontrollerat: volt = J/C, positiv/negativ laddning ger rätt tecken på energiändringen, och dubblerad laddning ger dubblerad energiändring. |
| 8.271 | Åtgärdad | Begrepp kontrollerat: volt = J/C, positiv/negativ laddning ger rätt tecken på energiändringen, och dubblerad laddning ger dubblerad energiändring. |
| 8.272 | Åtgärdad | Kontrollerat värde 1666.67 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Tolerans korrigerad så rätt svar med två värdesiffror godtas. |
| 8.273 | Åtgärdad | Kontrollerat värde 250 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.274 | Åtgärdad | Kontrollerat värde 1000 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.275 | Åtgärdad | Kontrollerat värde 350 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.276 | Åtgärdad | Kontrollerat värde 0.48 mJ. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Start- och slutpotential ger ett entydigt tecken. |
| 8.277 | Åtgärdad | Kontrollerat värde 200 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.278 | Åtgärdad | Kontrollerat värde 3.5 keV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.279 | Åtgärdad | Kontrollerat värde 300 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.280 | Åtgärdad | Kontrollerat värde 2.25 µJ. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.281 | Åtgärdad | Kontrollerat värde 400 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.282 | Åtgärdad | Kontrollerat värde 2000 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.283 | Åtgärdad | Kontrollerat värde 180 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.284 | Åtgärdad | Kontrollerat värde -400 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.285 | Åtgärdad | Kontrollerat värde 5 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Visar båda spänningsfallen i facit. |
| 8.286 | Åtgärdad | Kontrollerat värde -0.0005 J. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.287 | Åtgärdad | Kontrollerat värde -300 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.288 | Åtgärdad | Kontrollerat värde 8 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.289 | Åtgärdad | Kontrollerat värde -0.0004 J. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.290 | Åtgärdad | Kontrollerat värde -450 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.291 | Åtgärdad | Kontrollerat värde 4 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. En del av en krets beskrivs, inte en hel sluten slinga som skulle återvända till 0 V. |
| 8.292 | Åtgärdad | Kontrollerat värde -0.0007 J. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.293 | Åtgärdad | Kontrollerat värde -350 eV. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.294 | Åtgärdad | Kontrollerat värde 89900 V. Direkt energisamband/definition eller givna potentialsteg bedöms efter faktiskt arbete; enheter och tecken verifierade. |
| 8.302 | Åtgärdad | Åtgärdad: kraften räknad med uttrycklig k = 8,99·10⁹. Facit visar laddningsomvandling, produkt och beräkning utan långa likhetskedjor. Rutinberäkning på nivå 2. |
| 8.303 | Åtgärdad | Åtgärdad nivå och språk: dubbelt avstånd ger en fjärdedel så stor kraft. Enkel förändringsfråga nivå 1 och förklaring utan ordet proportionell. |
| 8.304 | Åtgärdad | Åtgärdad: kraften räknad med uttrycklig k = 8,99·10⁹. Facit visar laddningsomvandling, produkt och beräkning utan långa likhetskedjor. Rutinberäkning på nivå 2. |
| 8.305 | Åtgärdad | Åtgärdad: kraften räknad med uttrycklig k = 8,99·10⁹. Facit visar laddningsomvandling, produkt och beräkning utan långa likhetskedjor. Rutinberäkning på nivå 2. |
| 8.306 | Åtgärdad | Reviderad variation: tidigare nästan samma kraftberäkning som 8.305/307/308/309. Nu söks avståndet från en given kraft. Figuren märker avståndet r i stället för att visa svaret. Korrekt modell ger 27,5034 cm och godtar även 28 cm. Ny SVG skiljer tydligt på utgångsläget och den sökta storheten; ingen onödig avståndsuppgift på Newton-kortet. |
| 8.307 | Åtgärdad | Reviderad variation: tränar lika stora krafter trots olika laddningar, i stället för ännu en identisk insättning. Nivå 1 och korrekt kraft 0,599 N på båda kulorna, motsatt riktning. Ny SVG skiljer tydligt på utgångsläget och den sökta storheten; ingen onödig avståndsuppgift på Newton-kortet. |
| 8.308 | Åtgärdad | Reviderad variation: utgår från en uppmätt kraft och dubblerar avståndet, nivå 1. Figuren beskriver utgångsläget. 0,1275 N och den korrekta avrundningen 0,13 N godtas. Ny SVG skiljer tydligt på utgångsläget och den sökta storheten; ingen onödig avståndsuppgift på Newton-kortet. |
| 8.309 | Åtgärdad | Reviderad variation: ett begreppskort prövar två samtidiga laddningsändringar, med förklarade alternativ. Ersätter en orimligt laddad dammpartikel och ännu en likadan kraftberäkning. Nivå 2. Ny SVG skiljer tydligt på utgångsläget och den sökta storheten; ingen onödig avståndsuppgift på Newton-kortet. |
| 8.31 | Åtgärdad | Åtgärdad: alla tre strömmar var rätt. Facit visar hur ekvationssystemet löses och ger fullständiga slutsvar. Följdkort får egna strömvärden. Läraruppgift med fri energikontroll bevaras. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.310 | Åtgärdad | Åtgärdad: kraften räknad med uttrycklig k = 8,99·10⁹. Facit visar laddningsomvandling, produkt och beräkning utan långa likhetskedjor. Rutinberäkning på nivå 2. |
| 8.361 | Granskad – inget fel | Granskad – inget fel: samma ström går genom serieresistorerna. De kan ha olika resistans, spänning och effekt. Precis ett alternativ är rätt och nivå 1 passar. |
| 8.362 | Åtgärdad | Åtgärdad språkförenkling: Alla parallellgrenar har samma spänning, medan ström, resistans och effekt kan skilja sig. Precis ett korrekt alternativ. Onödigt antagande om batteriets inre resistans tas bort: samma två anslutningspunkter räcker. |
| 8.363 | Granskad – inget fel | Granskad – inget fel: 4,7 + 6,8 = 11,5 Ω. Direkt enkel beräkning på nivå 1. Fråga och facit stämmer. |
| 8.364 | Granskad – inget fel | Granskad – inget fel: Två lika 15 Ω-grenar ger 7,5 Ω. Fråga, facit och nivå stämmer. |
| 8.365 | Granskad – inget fel | Granskad – inget fel: 9/2 = 4,5 V. Direkt enkel beräkning på nivå 1. Fråga och facit stämmer. |
| 8.366 | Granskad – inget fel | Granskad – inget fel: Strömmen är 12/8,2 = 1,4634 A i den givna grenen. Fråga, facit och nivå stämmer. |
| 8.367 | Granskad – inget fel | Granskad – inget fel: Grenströmmarna summeras: 2,0 + 1,5 = 3,5 A. Fråga, facit och nivå stämmer. |
| 8.368 | Granskad – inget fel | Granskad – inget fel: Lika grenar delar 3,4 A lika: 1,7 A. Fråga, facit och nivå stämmer. |
| 8.369 | Granskad – inget fel | Granskad – inget fel: 15 − 6,8 = 8,2 Ω. Direkt enkel beräkning på nivå 1. Fråga och facit stämmer. |
| 8.377 | Granskad – inget fel | 0,50 A · 60 s = 30 C. Direkt Q=It, E/1. |
| 8.378 | Granskad – inget fel | 2,1 mC / 0,75 ms = 2,8 A. Medelström behövs för den korta gnistan. E/2. |
| 8.379 | Åtgärdad | 360 s är korrekt. Trasig LaTeX med ”u r” ersatt; direkt beräkning är nivå 1. |
| 8.380 | Granskad – inget fel | 250 mA = 0,250 A och 2,0 min = 120 s ger 30 C. E/2. |
| 8.381 | Åtgärdad | 25 s är korrekt. Enhetsomvandling och division är E/nivå 2, inte C. |
| 8.382 | Granskad – inget fel | Amperemeter kopplas i serie med lampan. Alternativ och E/1 stämmer. |
| 8.383 | Granskad – inget fel | Voltmetern ansluts mellan motståndets ändar, parallellt. Alternativ och E/1 stämmer. |
| 8.384 | Åtgärdad | Sluten krets krävs; grundbegrepp nivå 1. |
| 8.385 | Åtgärdad | Strömmen är lika stor före och efter lampan; energi omvandlas men laddning förbrukas inte. Grundbegrepp nivå 1. |
| 8.386 | Åtgärdad | Elektroner går motsatt den konventionella strömriktningen; grundbegrepp E/nivå 1, inte C/3. |
| 8.392 | Åtgärdad | Åtgärdad nivå: mätaren belastar spänningsdelaren, vilket är mer än enkel Ohms lag men inte nivå 5. Rätt resultat 10 · 1,5/3,5 = 4,2857 V. Nivå 3/C. |
| 8.393 | Åtgärdad | 0,49 mm/s är korrekt. Givet samband ger E/nivå 2. Påståendet att elektroner börjar röra sig samtidigt överallt ersatt med att fältet sprids snabbt, med ändlig hastighet. |
| 8.395 | Granskad – inget fel | Granskad – inget fel: Alla fyra uppgivna resistanser stämmer: 22/3, (44·22)/(44+22), 11+22 och 3·22. Att hitta alla kopplingar motiverar nivå 4; fri svarsmängd ska inte kräva en viss ordning. Fråga, facit och nivå stämmer. |
| 8.396 | Åtgärdad | Åtgärdad pedagogik och nivå: rätt effekt 5,09695 W behålls. Facit använder oavrundad lampspänning och visar nödvändiga beräkningar. Kombinerad modelluppgift nivå 3, inte 5. |
| 8.397 | Åtgärdad | 0,571 A och 4,8 % är korrekta. Nödvändiga mellanled och procentjämförelsen visas. C/nivå 3 i stället för A/4. |
| 8.40 | Åtgärdad | Åtgärdad: två effekter 0,088 och 0,132 W får två namngivna numeriska fält. Heluppgiften nivå 2; delarna är redan självständiga med fullständiga facit. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. |
| 8.41 | Åtgärdad | Granskad – inget fel: R₂ och R₃ ger 80 Ω, totalt 180 Ω, I = 0,100 A och 8 V över parallelldelen. Effekterna är 1,00, 0,64 och 0,16 W. R₁ ger mest effekt. Blandad strategisk koppling på nivå 3 och fri läraruppgift passar. Figurens två batteriledningar förlängs fram till polerna. |
| 8.42 | Åtgärdad | Åtgärdad: effektkortet får det okända R₃-värdet som eget givet värde och visar hur parallelldelens spänning fås. 600 Ω och 0,1067 W är rätt. Strategidelen behåller nivå 3. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.464 | Åtgärdad | Elektroner per sekund, Q=It och jonström kontrollerade. Facit förklarar centrala mellanled; första svarsfältet får korrekt antal per sekund som enhet. |
| 8.465 | Åtgärdad | 324000 C, 3,75 A och 0,04375 A korrekta. Kapacitet är levererad laddning, inte batteriets nettoladdning. Omvandlingar och medelström förklarade. |
| 8.466 | Åtgärdad | 12500 A är korrekt; två värdesiffror 13000 A accepteras redan. Facit visar tidsomvandlingen och vad medelström betyder. |
| 8.467 | Åtgärdad | 13 % kvar innebär 87 % överförd laddning. 0,013 A är korrekt. Mellanled och enkelt språk; E/nivå 2. |
| 8.468 | Åtgärdad | 0,0026 A åt höger är korrekt. Förklarar varför motsatt laddning och motsatt rörelse ger ström åt samma håll; båda bidrag visas. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.469 | Åtgärdad | 0,0080 A är korrekt. Svårare ord ersatt med jonens laddning; båda strömbidrag förklaras. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.470 | Åtgärdad | Protonantal och temperaturhöjning kontrollerade. a befrias från oanvända värmedata; b har eget protonantal och tydliga energi- och temperaturberäkningar. E/2 med givna mellanvärden. Långa beräkningskedjor radbryts för mobilvisning. |
| 8.471 | Åtgärdad | 7,3·10⁻⁵ A är korrekt. Visar omkrets, varvtid och passerad laddning. C/nivå 3 snarare än A/4. |
| 8.49 | Åtgärdad | Åtgärdad: batteriets polaritet i figuren var omvänd. Båda delspänningarna och potentialerna får namngivna svarsfält, kompletta facit och självständiga kort. Nivå 2 för heluppgiften. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.50 | Åtgärdad | Åtgärdad: ekvationer och strömmar är korrekta, men del a hade slutsvaret 0 och del b bara en av tre strömmar. Slutsvaren rättas. Tolkningskortet anger strömmarna självt. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.51 | Åtgärdad | Åtgärdad: parallellvärden räknade från 4.7 V och [470, 470] Ω. Alla efterfrågade grenstorheter har fullständiga slutsvar, märkta fält och enheter. Varje del visar egen beräkning; nivå 1–2. Fria motiveringar/två metoder kräver manuell komplettering där de efterfrågas. Figurens två batteriledningar förlängs fram till polerna. Tre parallella 470 Ω-resistorer godtar även avrundningen 160 Ω. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.515 | Ny uppgift | Ny varierad uppgift med SVG: arbete ur potentialgraf. Nivå 2. |
| 8.516 | Ny uppgift | Ny varierad uppgift med SVG: samma potential längs en väg. Nivå 1. |
| 8.517 | Ny uppgift | Ny varierad uppgift med SVG: batterikapacitet är inte nettoladdning. Nivå 1. |
| 8.55 | Åtgärdad | Åtgärdad: båda delspänningarna får rättning och fullständigt slutsvar. Strömmen ges på spänningskortet. Enkla kort nivå 1–2, inte C/3. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.62 | Åtgärdad | Åtgärdad: korrekta resultat 450 Ω, 20 mA, 3 V och 30 mA. Nivå 1–2 och varje kort räknar sin egen resistans. Enhetsomvandlingen till mA visas korrekt även i delens facit. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.64 | Åtgärdad | Åtgärdad nivå och rättningsmetadata: 300 Ω och 0,48 W är korrekta. Fri motivering till amperemeterns placering bevaras; bara den delen kräver manuell komplettering. Nivå 1–2. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. |
| 8.7 | Åtgärdad | Åtgärdad: R₂ = 300 Ω var korrekt, men en rent numerisk uppgift saknade självrättning. Den får numeriskt fält och en relevant ledtråd. |
| 8.73 | Åtgärdad | Åtgärdad: oladdat utgångsläge anges och en tydlig elektroskopfigur läggs till. Flyttad till laddning/influens och nivå 1–2. Läraruppgiftens tre delar bevaras; a+b kombineras till ett självrättande begreppskort så att dess facit inte avslöjar ett separat b-kort. C-kortet har eget underlag och förklarade alternativ. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.78 | Åtgärdad | 15,75 C, cirka 9,83·10¹⁹ elektroner; felaktiga slutrader 12 C och 7,49·10¹⁹ ersatta. |
| 8.79 | Åtgärdad | Delfacitets felaktiga 1,667 h och 9,0 kC ersatta med 1,47 h och 7,92 kC. a självrättas nu utan manuell komplettering. |
| 8.83 | Åtgärdad | 144 C, cirka 8,99·10²⁰ elektroner; mellanled och korrekta ledtrådar. |
| 8.85 | Åtgärdad | Åtgärdad: resultaten var rätt, men c:s slutsvar saknade R₁ och följdkorten krävde R₂ från b. Båda spänningarna och eget R₂-värde anges. Fri motivering behålls som läraruppgift. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.86 | Åtgärdad | Kopplingar och motiveringar korrekta. E/1 för koppling, E/2 för mätarens påverkan. Ledtrådar ger stöd utan att avslöja hela svaret; fri förklaring behålls utanför spelet. |
| 8.88 | Åtgärdad | Åtgärdad: numeriska kort får självrättning och märkta fält. Grenströmmarna beräknas i facit, inte bara anges. Den fria kontrollen i c kräver manuell komplettering. Rätt fysik och nivå 1–2. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.89 | Åtgärdad | Åtgärdad: alla energier och effekter är rätt. Följdkort får egna givna värden och nödvändiga mellanled; fråga d ber tydligt om energimängd i J, inte en andel. Nivå 1–2. Figurens ledningar ansluts till båda batteripolerna; de tidigare glappen tas bort. Facitets delrubriker och lösningar har också giltig HTML-struktur. |
| 8.91 | Åtgärdad | Åtgärdad: parallellvärden räknade från 9 V och [300, 600] Ω. Alla efterfrågade grenstorheter har fullständiga slutsvar, märkta fält och enheter. Varje del visar egen beräkning; nivå 1–2. Fria motiveringar/två metoder kräver manuell komplettering där de efterfrågas. Figurens två batteriledningar förlängs fram till polerna. Facitets delrubriker och lösningar har också giltig HTML-struktur. |

## Åtgärdad

8.103, 8.110, 8.116, 8.117, 8.118, 8.12, 8.124, 8.125, 8.128, 8.129, 8.131, 8.132, 8.135, 8.136, 8.137, 8.138, 8.139, 8.140, 8.141, 8.142, 8.143, 8.144, 8.145, 8.146, 8.147, 8.148, 8.149, 8.150, 8.151, 8.152, 8.155, 8.16, 8.165, 8.166, 8.167, 8.17, 8.19, 8.191, 8.197, 8.199, 8.20, 8.244, 8.245, 8.246, 8.247, 8.248, 8.249, 8.250, 8.251, 8.257, 8.258, 8.259, 8.26, 8.260, 8.261, 8.263, 8.264, 8.265, 8.266, 8.267, 8.268, 8.269, 8.270, 8.271, 8.272, 8.273, 8.274, 8.275, 8.276, 8.277, 8.278, 8.279, 8.280, 8.281, 8.282, 8.283, 8.284, 8.285, 8.286, 8.287, 8.288, 8.289, 8.290, 8.291, 8.292, 8.293, 8.294, 8.302, 8.303, 8.304, 8.305, 8.306, 8.307, 8.308, 8.309, 8.31, 8.310, 8.362, 8.379, 8.381, 8.384, 8.385, 8.386, 8.392, 8.393, 8.396, 8.397, 8.40, 8.41, 8.42, 8.464, 8.465, 8.466, 8.467, 8.468, 8.469, 8.470, 8.471, 8.49, 8.50, 8.51, 8.55, 8.62, 8.64, 8.7, 8.73, 8.78, 8.79, 8.83, 8.85, 8.86, 8.88, 8.89, 8.91.

## Granskad – inget fel

8.262, 8.361, 8.363, 8.364, 8.365, 8.366, 8.367, 8.368, 8.369, 8.377, 8.378, 8.380, 8.382, 8.383, 8.395.

## Ny uppgift

8.515, 8.516, 8.517.

## Återstår

365 av kapitlets 517 uppgifter återstår i denna manuella runda. Alla deras ID:n finns i JSON-loggens `remainingIds`. Återstående Coulombuppgifter, elektriskt fält och blandade kretsar är inte markerade färdiga. Tidigare laddningsgranskning ersätter inte den planerade andra kontrollen av hela banken.
