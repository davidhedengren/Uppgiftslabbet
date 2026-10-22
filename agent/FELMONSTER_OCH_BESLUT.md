# Register över felmönster och tidigare beslut

Detta är ingången för framtida granskning. Läs den före bankändringar och sök
sedan upp uppgifts-ID:t i `agent/` och i testerna. Granskningsloggarna innehåller
matematisk kontroll, exakta ändringar, utfall och kommentarsförslag. Git visar
diffen och historiken. Registret är ett urval av återkommande mönster, inte en
förteckning över varje fel som någonsin rättats.

## Arbetsgång för nästa agent

1. Sök ID och feltyp, exempelvis `rg -n '1\.234|begreppssvar' agent tools`.
2. Läs aktuell uppgift, dess delkort och den tidigare motiveringen.
3. Lös matematiken självständigt och testa det faktiska elevflödet.
4. Undersök minst fem liknande uppgifter per feltyp när det finns relevanta fall.
5. Skriv en ny logg: granskade ID:n, ändrade ID:n, **Granskad – inget fel**,
   osäkra/ofullständiga kontroller och färdiga kommentarsförslag.
6. Lägg till nya felmönster eller uppdatera relevanta poster här. Länka testerna.

Ett tidigare beslut får ändras om det visar sig felaktigt, men det ska ske med
ny matematisk/pedagogisk motivering och verifiering. Befintliga mönster i banken
är inte facit. Ett test får inte tas bort eller försvagas för att dölja en återgång.

## FP-01: Frågan och rättningssvaret mäter olika saker

**Sök efter:** ”Vad betyder”, ”förklara”, ”ange skärningen”, flera namngivna storheter
med svar som bara består av ett belopp eller en punktsträng.

**Beslut:** antal svarsfält, etiketter, ordning och rättning ska motsvara frågan.
Begreppsfrågor får inte rättas genom att eleven måste gissa en exakt fras.
Använd granskade förklaringsalternativ eller manuell bedömning när det behövs.

**Exempel:** ma2 1.234 b frågade vad 45 betydde men lagrade ”45 kr”. Nu prövas
förståelsen av fast avgift genom förklaringsalternativ på spelkortet. 1.29 har
x/y-fält; 1.299 har fält för T-shirts och hoodies. 2.12 b frågar efter faktorn.

**Skydd:** Kunskapsgymmet `tools/modellgranskning-ma2-2026-10-09.browser.py`,
`tools/felrapporter-2026-10-09-2049.browser.py`.

**Underlag:** [modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md),
[rapporter 20:49](FELRAPPORTER_2026-10-09_2049.md).

## FP-02: Delkort saknar tidigare information eller visar andra delars facit

**Uppföljning 2026-10-14 13:25:** Mato1 #2.82 och tretton analoger visar
en funktion på varje kort. Där används singular och giltig HTML;
huvudbladets plural och matematik behålls. Ma2 #3.201 a får
egna x/y-etiketter, medan b-facit beräknar dubbla MB från sina synliga data
i stället för att börja med A:s osynliga koordinater. Se
[granskning 13:25](FELRAPPORTER_2026-10-14_1325.md).

**Sök efter:** `spelDelning`, saknat `spelDelar[i].s`, ”använd”, ”samma”, ”modellen”,
”mer än så”, facit som börjar med ett mellanresultat utan att det ges på kortet.

**Beslut:** varje kort ska innehålla sina givna värden, formel/figur, eget facit
och relevant ledtråd. Om ett tidigare resultat behövs för den avsedda nivån,
ge det direkt. Kalibrera kortets nivå efter den information som faktiskt visas.
Huvuduppgiftens och spelkortens delar ska ha entydig koppling till svaren.

**Tillägg 2026-10-11:** 3.311 hade sin vektorfigur i huvuduppgiften men inte i
c-kortet. Egna korttexter ersätter `spelIntro`; kontrollera därför den faktiskt
renderade frågan. Alla delar får riktningarna i egen SVG, medan c behåller
enbart sina behövliga tal 50 s och 0,9 m/s. ”Överfarten” ersätts med resan
till andra stranden, även i jämförelsen 3.131. Se
[rapporter 11:31](FELRAPPORTER_2026-10-11_1131.md) och
`tools/felrapporter-2026-10-11-1131.test.js`; konsumentens browsertest har samma datum.

**Exempel:** ma2 1.271 b får kilometerpriset och c hela taximodellen. 2.11 b får
förändringsfaktorn. 2.361, 2.363 och 2.365 har egna delfacit. 2.195 b får
kvadratkompletterad form i sitt kort och en förklaring till minsta värdet.

**Skydd:** `tools/delkort.test.js`, `tools/foljdgranskning-ma2-2026-10-09.browser.py`,
`tools/modellgranskning-ma2-2026-10-09.browser.py`,
`tools/kvadratkomplettering-2026-10-09.browser.py` (Kunskapsgymmet).

**Underlag:** [följdgranskning](FOLJDGRANSKNING_MA2_2026-10-09.md),
[modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md),
[kvadratkomplettering](KVADRATKOMPLETTERING_2026-10-09.md).

## FP-03: Algebraisk likhet räcker inte när en särskild form efterfrågas

**Sök efter:** ”faktorisera”, ”kvadratkomplettera”, ”förenkla”, ”decimalform”
kombinerat med generiskt `svarFormat:"uttryck"` eller saknat format.

**Beslut:** kontrollera både matematiskt värde och efterfrågad form. Generiska
likhetsgenvägar får inte godkänna ursprungsuttrycket i en omskrivningsuppgift.
Använd ett uttryckligt svarsformat; ändra inte vanlig uttrycksrättning globalt.

**Exempel:** ma2 2.19, 2.71, 2.88 a, 2.190, 2.194 och 2.195 a använder
`kvadratkompletterat`. `(x-3)^2+4` och `4+(3-x)^2` godtas; `x^2-6x+13` är
matematiskt lika men besvarar inte kvadratkompletteringsfrågan.

**Avgränsning:** den nya kontrollen gäller x-polynom på formen `A*(x+h)^2+k`,
med en uttrycklig kvadrat och x-koefficient ±1 inne i parentesen. Den ska inte
sättas på godtyckliga andra uppgiftstyper utan separat granskning och tester.

**Skydd:** `tools/kvadratkomplettering-2026-10-09.browser.py` i Kunskapsgymmet.
**Underlag:** [kvadratkomplettering](KVADRATKOMPLETTERING_2026-10-09.md).

## FP-04: Modellvillkor och svarsenheter saknas eller blandas ihop

**Sök efter:** olika storheter i samma ekvation, saknad `svarEnhet`, avrundat
facit med för snäv tolerans, rörelsemodeller utan nödvändigt fartvillkor.

**Beslut:** behåll bara villkor som behövs och skriv dem enkelt. Kontrollera
fråga, beräkning, visad enhet och accepterade elevsvar tillsammans.

**Exempel:** ma2 1.37 använder kg kryddblandning och kg salt, inte odefinierad
salthalt i liter. 1.326 anger lika paddlingsfart relativt vattnet. 1.325 får kg
i svarsfältet. Se också fysikrapporten om tre värdesiffror.

**Skydd:** `tools/modellgranskning-ma2-2026-10-09.browser.py`,
`tools/felrapport-6-422.browser.py` i Kunskapsgymmet.
**Underlag:** [modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md),
[fy1 6.422](FELRAPPORT_6_422_2026-10-09.md).

## FP-05: Nivå eller variation följer en mall i stället för elevens arbete

**Sök efter:** identiska grafsvar, nivå 1 med modellering och flera beroende steg,
eller delkort som är lika högt graderade trots givna mellanresultat.

**Beslut:** nivå 1 är de allra enklaste uppgifterna. Bedöm träningsnivå, E/C/A
samt arbetsinsats separat. Höj eller sänk individuellt. Variationsproblem kräver
inte att varje liknande uppgift ändras.

**Exempel:** ma2 1.296–1.302 ligger på nivå 2; grafuppgifter har varierade
skärningspunkter. 3.529 a ligger på 4 medan 3.523 sänktes till 2. Taxikorten
1.271 har nivåerna 3/2/1 efter vad som ges på varje kort.

**Skydd och underlag:** [rapporter 20:49](FELRAPPORTER_2026-10-09_2049.md),
[följdgranskning](FOLJDGRANSKNING_MA2_2026-10-09.md),
[modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md) och deras webbläsartester.

## FP-06: Facit räknar rätt men förklarar inte beräkningen

**Sök efter:** ”Lös systemet” följt av enbart svar, uppdelade meningar i flera
numrerade steg, långa formler som kräver sidscrollning, fel variabelnamn.

**Beslut:** visa den avgörande substitutionen/eliminationen och nödvändiga
mellanled i korta, begripliga rader. I fysik används inte numrerade steg enligt
användarens instruktion. Kontrollera facit på mobil och dator.

**Exempel:** ma2 1.296–1.302 hade ingen uträkning mellan system och svar.
1.223 fick en kortare elimination; 1.30:s förklaring jämförde felaktigt
”x-koefficienterna” trots att det var y-koefficienterna.

**Skydd och underlag:** [följdgranskning](FOLJDGRANSKNING_MA2_2026-10-09.md),
[modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md), motsvarande webbläsartester.

## Att hitta äldre historik

Övriga granskningar finns i `agent/FELRAPPORT*.md`, `agent/FYSIK*.md` och
andra ämnesspecifika loggar. Sök alltid även där. Detta register ersätter inte
historiken eller ämnesreglerna. Rapportstatus i appen är skild från Git-historik;
en push innebär inte att rapporter har markerats som avslutade.

## FP-07: Elektronöverskott, influens och Coulombs lag

**Sök efter:** ”hur många elektroner har avlägsnats” utan känt utgångsläge,
`rättSvar:null` på numeriska elektronfrågor, saknade elektron-enheter,
slutrader som bara anger elementarladdningen, långa enhetsomvandlingar,
A/C-märkta direkta halveringar och ord som ”repellerande” på enkla kort.

**Beslut:** skilj tidigare överföring från aktuellt elektronunderskott.
Visa tecken, nödvändiga enhetsomvandlingar och mellanled utan nummersteg.
En direkt halvering är normalt E/nivå 1; Q/e med enhetsomvandling normalt E/2.
Rutinuppgifter blir inte C bara för att de innehåller två kontakter.
Numeriska kort kräver inte manuell komplettering om ingen motivering efterfrågas.

**Influens:** omfördelning inom ett isolerat föremål ändrar inte nettoladdningen.
Håll isär laddningsförskjutning i papper och rörliga elektroner i metall.

**Tillägg 2026-10-11:** i 8.503 prövas också missuppfattningen att elektroner
sitter fast i metallkulan. Alternativet är felaktigt och får egen återkoppling:
en del av metallens elektroner kan röra sig genom metallen. Lägg inte samma
förklaring om fri elektronrörelse på pappers-/isolatoruppgifter.
Se [rapporter 11:31](FELRAPPORTER_2026-10-11_1131.md).
Vid jordning/separation ska ordningen framgå. Attraktion ensam bevisar inte
motsatt nettoladdning. Lika stora krafter tar bara ut varandra vid motsatt riktning.

8.73 kräver att elektroskopet är oladdat från början. Ange detta utgångsläge
utan att överförklara i frågan. Om ett korts facit avslöjar nästa svar kan
delarna förenas på spelkortet, samtidigt som lärarbladets delar bevaras.
Utelämnade spelkort kräver entydig bokstavsmappning till originalets metadata.
8.306–309 varierar Coulombgruppen med avstånd, Newtons tredje lag och
förändringsfaktorer i stället för fyra nästan identiska uträkningar.

8.71 b hade 0 i rättningsmetadata men ett felaktigt kortslutsvar 84,3 µN:
det senare gällde bara en granne. Visa kraftsumman, 0 N, och förklara
symmetrin. 8.68/74 visar att storlek och riktning måste prövas var för sig
när båda efterfrågas. 8.21:s lärar-d bevaras men utelämnas i spelet eftersom
c:s facit redan förklarar sambandet. Se
[Coulomb- och fältgranskning 2026-10-10](COULOMB_OCH_FALT_FYSIK1_2026-10-10.md).

**Enheter:** N/C och V/m är likvärdiga. Kunskapsgymmets dimensionsjämförelse
utvecklar C = A·s och V = J/C. Bevara prefix och avvisa fel dimension.
`tools/elektriska-enheter.test.js` och det faktiska elevflödet i
`tools/coulomb-falt-fy1-2026-10-10.browser.py` skyddar detta.
Ledtrådar om ΣF = ma ska inte återinföras i rena E = F/q- eller U = Ed-frågor.

**Miniräknare:** användarbeslut 2026-10-09: alltid tillåten i fysik, även på
begreppskort. Återställ inte `miniräknare:false` med hänvisning till låg nivå.

**Exempel och skydd:** [fullständig logg](LADDNING_FYSIK1_2026-10-09.md).
8.35 b saknade självrättning; 8.56 hade missvisande kortslutsvar;
8.182/8.315 låg för högt; 8.475 behöver mellanledet 3−(−2)=5 µC.
Kunskapsgymmets `tools/laddning-fy1-2026-10-09.browser.py` prövar berörda
kort, alternativ, korrekta avrundningar, felaktiga tecken och mobila facit.


## FP-08: Flera fysikstorheter på samma delkort

**Sök efter:** ”varje resistor”, ”båda polerna”, ”potentialerna” eller flera
namngivna effekter, där `rättSvar` är null, en ensam storhet eller kortets
slutrad bara innehåller det sista värdet. Sök även efter beroenden som
”den energin” eller ”samma punkt” utan egna data på spelkortet.

**Beslut:** ordnade storheter får delens `svarsstruktur: "ordnad"` och egna
`svarEtiketter`. Kunskapsgymmet bevarar dessa vid `expandGameTask`; rotmängder
utan uttrycklig ordning fortsätter vara mängder. Fria motiveringar måste
bedömas manuellt eller ersättas på spelkortet av genomtänkta alternativ med
förklaringar. Läraruppgiftens fria resonemang får finnas kvar.

**Exempel:** 8.49, 8.103, 8.117, 8.144, 8.149, 8.150, 8.40, 8.55,
8.131, 8.132 och 8.135. Se [granskningslogg](ELEKTRICITET_FYSIK1_2026-10-09.md).
Samma mönster är rättat i parallelluppgifterna 8.16, 8.19, 8.91, 8.136,
8.142 och 8.155. 8.141 visar att en storhet given bara i a måste flyttas till
gemensam information när även b/c behöver den. Facitets blockelement ska
vara syskon till delrubrikernas stycken, aldrig en div inuti ett p-element.
`tools/delkort.test.js` och `tools/elektricitet-fy1-svar.browser.py` i
Kunskapsgymmet skyddar fältordning, enheter och rättning. Fysikmodeller finns
i masterrepots `tools/fysik1-elektricitet.test.js`.

**Figurer:** kontrollera faktisk förbindelse till batteripolerna. En ledning
får varken sluta med ett glapp eller fortsätta genom batteriets två plattor.
8.49 visar varför polaritet också måste kontrolleras mot jordpunkt och facit.
Geometrikontroll räcker inte för elektrisk korrekthet.

## FP-09: Sant alternativ som inte definierar begreppet

En envalsfråga får inte använda ett också sant påstående som tydligt fel
utan att avgränsa vad frågan efterfrågar. I 5.364 var sammanlagd
rörelseenergi rätt definition av elastisk stöt, men rörelsemängdens
bevarande var också sant under det givna antagandet. Ersättningen skiljer
varje bolls rörelsemängd från deras summa. Fysikfacit om elastisk stöt
ska inte ändras. Se [rapport och sex jämförelser](FELRAPPORT_5364_2026-10-09.md).

## FP-10: Fält, kraft och vardagligt riktningstänkande

Ett spelkort ska fråga efter samma storhet som lärarfrågan. 8.106 frågade
fältstyrka i huvuduppgiften men kraft på en ny testladdning i spelkortet; de två
numeriska korten och N/C-enheterna är nu samstämmiga. Jämför med 8.65, 8.321,
8.326, 8.328 och 8.336. Kraftens storlek använder laddningens belopp; en
uttryckligen efterfrågad kraftkomponent behåller sitt tecken.

Kraftens riktning avgör inte ensam rörelsens riktning utan startvillkor.
8.11, 8.60 och 8.105 frågar därför kraftens riktning. En negativ laddning
påverkas motsatt fältet; en positiv i fältets riktning. 8.47 har däremot
uttryckliga horisontella och lodräta startvillkor, och dess avvikelse är
beräkningsbar. 8.69 skiljer svävande jämvikt från fallet när fältet stängs av.

Punktladdning: dubbelt avstånd ger en fjärdedel (8.59, 8.106, 8.115).
Parallella plattor vid oförändrad spänning: dubbelt avstånd ger hälften
(8.168). Återanvänd inte en generell avståndsledtråd mellan dessa modeller.

Rutinberäkning med omvandling är E/nivå 2; den blir inte C/A av stora
exponenter eller en kvadratrot. 8.337, 8.341, 8.343, 8.345 och 8.347 är
exempel. Givna vinkelräta fält som summeras med Pythagoras är också E/2 i
8.350, 8.353, 8.356 och 8.359. Sammanhängande strategi/härledning bedöms
separat, liksom nivån på ett fristående kort med givna mellanresultat.

Se [fullständig fältlogg](FALT_HELA_FYSIK1_2026-10-10.md),
`tools/fysik1-falt-hela.test.js` och Kunskapsgymmets
`tools/falt-hela-fy1-2026-10-10.browser.py`. Två värdesiffror godtas bland
annat för 8.47 c och 8.115 d. Geometrivarningar för minus inuti
laddningssymboler måste bedömas visuellt; en verklig text–fältlinjekollision
som 8.60:s laddningsetikett behöver däremot rättas.

## FP-11: Coulombkort med dold föregående beräkning eller ofullständigt slutsvar

Kontrollera om kortet använder en redan beräknad laddning, kraft eller
fältkomponent som inte visas. Ge mellanresultatet på just det kortet och
beräkna dess target och facit från det givna värdet, även när värdet är
avrundat. 8.58 c/d, 8.119 b, 8.121 c, 8.33 c, 8.160 c, 8.161 c,
8.479 b, 8.485 b, 8.486 b, 8.488 b och 8.493 b är jämförelser.
Lärarens huvuduppgift får behålla sin sammanhängande beräkning.

8.121 b frågar efter två krafter; 8.33/8.160 c efter storlek och riktning.
Alla efterfrågade svar ska ha egna namngivna ordnade fält. Storlek och
vinkel behöver olika enheter. Att bara lägga sista värdet i facitets
slutrad tappar en del av frågan. Jämför FP-08:s 8.49, 8.103, 8.117,
8.40 och 8.131. 8.488 a ska visa endast den större roten; nästa korts
mindre laddning får inte stå i a-facit.

Lika laddningsfördelning vid kontakt kräver likadana metallkulor; 8.119
saknade det villkoret. Nollpunktens svar måste ange vilken källaddning
avståndet räknas från. Nollpunktsalgebra kräver en förklaring av varför
de motriktade fälten sätts lika, följd av kvadratroten och lösningen.
32/34/314/320/484 i kapitel 8 visar modellen. Enkel symmetri är däremot
E/nivå 2 i 8.313, inte A.

SVG-avstånd för små laddade kulor ska gå mellan mittpunkterna. I 8.160
låg det gamla måttstrecket mellan cirkelkanterna; den nya figuren har
mått till mittpunkterna. Kontrollera att hjälplinjer slutar före kulorna
eller ligger bakom deras bakgrund, och att laddningsetiketter har plats
även nära lodräta linjer. 8.33, 8.160, 8.316, 8.317, 8.319 och 8.489
är visuellt granskade jämförelser.

Se [fullständig logg och återkopplingslista](COULOMB_RESTERANDE_FYSIK1_2026-10-10.md),
`tools/fysik1-coulomb-hela.test.js` och Kunskapsgymmets
`tools/coulomb-hela-fy1-2026-10-10.browser.py`. Granskningsstatus med
ID:n och loggproveniens finns i `agent/ELEKTRICITET_GRANSKNINGSSTATUS.json`.
Det registret säger uttryckligen att hela banken och hela andra manuella
rundan ännu inte är klara.

## FP-12 – resistansgeometri, fristående kort och temperaturändring

2026-10-10: 68 manuella kretsgranskningar finns i
[KRETSAR_FYSIK1_2026-10-10.md](KRETSAR_FYSIK1_2026-10-10.md).

Kvadrera hela radien efter omvandling till meter. Skriv exempelvis
`A=π(2,0·10⁻⁴)²`, aldrig `π·0,20·10^{-3\,2}`. 8.410, 8.412,
8.413, 8.425, 8.427, 8.428 och 8.436 hade den senare feltypen.
Det numeriska svaret kunde ändå vara rätt. Visa area och relevanta
mellanresultat i facit; dela långa ekvationskedjor över rader för mobil.

Ett fristående spelkort med givna avrundade mellanresultat ska använda
sina egna `rättSvar`, `tolerans`, `svarEnhet`, `svarFormat`,
`självrättning` och `manuellKomplettering`. Uttryckliga delvärden har
företräde i `expandGameTask`; när delvärden saknas används huvuduppgiftens
metadata och originaletikett som tidigare. Flerfältslayout bestäms efter
prioriteringen. Kontrolljämförelser: 8.8, 8.28, 8.61, 8.157, 8.424
 och 8.436. Ursprungligt lärarfacit får fortfarande använda full precision.

Förväxla inte en lampas märkström med strömmen när kabelresistans ingår
(8.84), och skriv inget maximivillkor om frågan egentligen söker exakt
önskad lampspänning (8.438). 3:1 innebär fyra delar, inte fem (8.416).
Kopparresistivitet behöver anges när den krävs; 8.196, 8.198 och 8.200
saknade den. Två av tre kloner blev inversa area-/längdfrågor.

`svarFormat:"temperaturandring"` är ett uttryckligt opt-in för en
**temperaturdifferens**. Samma tal i K och °C godtas, utan 273-offset.
Detta får inte användas för absolut temperatur. Jämför 8.440 med
8.439 och 8.441–8.444. Regressioner prövar både rätt tal i båda enheterna,
fel enhet, fel 273-omvandling och oförändrad absolut temperaturrättning.

Grafritning och fri linjeanpassning ska fortsatt kunna vara läraruppgifter
(8.81, 8.108). Metodjämförelsen i 8.158 c bevaras hos läraren men ska inte
bli ett andra spelkort som redan fått samma slutsvar från b.
Se `tools/fysik1-kretsar.test.js`, Kunskapsgymmets
`tools/temperaturandring.test.js`, `tools/delkort.test.js` och
`tools/kretsar-fy1-2026-10-10.browser.py`. Alla granskade ID:n och
återstående uppgifter registreras i `ELEKTRICITET_GRANSKNINGSSTATUS.json`.

## FP13 – efterfrågad storhet, fristående batterikort och omöjliga energimodeller (2026-10-10)

135 kopplingsuppgifter är genomlästa och omräknade, med ID-för-ID-kommentarer i [KOPPLINGAR_FYSIK1_2026-10-10.md](KOPPLINGAR_FYSIK1_2026-10-10.md) och maskinläsbart ändringsunderlag i motsvarande JSON. Se särskilt 8.39, 8.112, 8.97, 8.164, 8.99, 8.13 och 8.402: ett korrekt mellanled gör inte ett gammalt motstridigt slutsvar korrekt. Facit och rättning måste svara på den storhet frågan faktiskt efterfrågar. En fråga om kopplingstyp ska inte rättas som effekt i W.

Delkort med avrundade givna mellanvärden ska ha egna numeriska mål: exempelvis 8.43, 8.94, 8.162, 8.402, 8.403, 8.407 och 8.409. Föräldralösningen kan samtidigt använda full precision. Bevara denna avsiktliga skillnad och förklaring; återställ inte gamla föräldravärden i barnkort. Två efterfrågade strömmar/spänningar ska ha två namngivna fält och ordnad rättning: 8.18, 8.87, 8.90, 8.98, 8.162, 8.164. Numeriska kort ska inte blockeras av gammal manuellKomplettering, som i 8.154.

Ett värmeproblem behöver veta vart energin går, kort och tydligt: 8.451, 8.455, 8.457, 8.458, 8.459, 8.460 och 8.462. Temperaturökning, exempelvis 8.452b, använder temperaturandring så att samma tal i K och °C godtas utan 273-omvandling. Energi som fås tillbaka vid batteriurladdning är inte automatiskt all kemiskt lagrad energi. 8.98 använder för låg spänning för en extrapolering där förlusten överstiger tillförseln; detta granskas som orimlig modell, inte som ett möjligt driftfall. En säkrings märkström är inte en exakt utlösningstid (8.96). Högre inre resistans kan göra bilstart svårare, men utan startgräns kan man inte säkert säga att bilen inte startar (8.162).

Rutinuppgifter klassas efter fysikvalet, inte antalet multiplikationer eller ursprungliga A-markeringen: 8.202, 8.205, 8.203, 8.206, 8.235, 8.238, 8.241 och 8.447. Direkt formel nivå 1; vanliga omvandlingar/bekanta samband nivå 2. Fri grafritning 8.10 och generellt symboliskt resonemang 8.153 bevaras hos läraren. För optimering 8.13 behövs en verklig motivering till R = r; numeriskt optimalvärde ensamt ersätter inte lärarens resonemang.

Kretsfigurer har kontrollerad topologi och större Arial-etiketter med marginaler. Ändra inte polaritet, amperemeterns seriekoppling eller voltmeterns parallellkoppling när figurer förbättras. A/V ligger avsiktligt inne i instrumentcirklar. De äldre små/överlappande etiketterna i bland annat 8.52, 8.95, 8.123, 8.130, 8.134 och 8.154 ska inte återinföras.

## FP14 – nuklidantal, massjämförelse och energi per nukleon (2026-10-10)

Alla 78 nukliduppgifter är manuellt genomlästa. ID-för-ID-beslut och kommentar finns i [NUKLIDER_FYSIK1_2026-10-10.md](NUKLIDER_FYSIK1_2026-10-10.md) och motsvarande JSON. Aktuell kapitelstatus finns i KARNFYSIK_GRANSKNINGSSTATUS.json; övriga kärnfysikområden är ännu inte färdiggranskade.

Exakta partikelantal rättas med tolerans 0 (9.202, 9.203, 9.207, 9.214, 9.231, 9.241). Enkla subtraktioner och direkta energiomvandlingar är nivå 1, inte automatiskt C eller A (9.218, 9.220, 9.221, 9.224, 9.228, 9.230). Omvänd massdefekt med mycket små masskillnader behöver uttrycklig precision: 9.235 fem decimaler, 9.389a och 9.392 fyra, 9.397 tre. En tvåprocentstolerans på själva atommassan skulle gömma hela massdefekten och får inte ersätta dessa snäva toleranser.

Skilj kärnmassa från atommassa. Jämför med proton/neutron för kärnmassa; med väteatom/neutron för atommassa så att elektronbidragen balanserar (9.20, 9.31, 9.35, 9.61, 9.62, 9.68, 9.398). Insatta massor i facit ska behålla givna decimaler. Irrelevant elektronmassa ska inte läggas tillbaka i dessa kort. Facit visar masskillnad och energiomvandling före slutsvar.

Optin-formatet energi_per_nukleon godtar MeV och MeV/nukleon samt korrekt omräknade eV/keV/GeV/J. Det får inte godta energi per sekund eller fel dimension. Använd bara för energi per nukleon, inte total energi (9.219 och 9.223 söker nu total energi). Granskade analoger är 9.218, 9.220, 9.227, 9.230, 9.236, 9.394, 9.395. Regressioner: tools/fysik1-nuklider.test.js i master och tools/energi-per-nukleon.test.js samt tools/nuklider-fy1-2026-10-10.browser.py i konsumenten.

Alla efterfrågade antal/storheter får namngivna fält: 9.22, 9.34, 9.36, 9.61, 9.66. Kort med eget avrundat mellanvärde använder detta värde, medan lärarens sammanhängande lösning får räkna med full precision (9.19b, 9.31d, 9.32b, 9.66b/c, 9.393b, 9.394b, 9.395b). Lärarens fria motiveringar bevaras och rättas manuellt; de ska inte skapa beroende spelkort som redan fått sitt svar. Plusmärken i protoncirklarna i 9.36 är avsiktliga och korrekt placerade. Radien i 9.66 går från centrum till kanten.

## FP15 – radioaktivitet: sökt storhet, halveringsmodeller och inversa tidsenheter (2026-10-10)

Samtliga 101 uppgifter i aktivitet är manuellt granskade med ID-för-ID-beslut och kommentarsförslag i [AKTIVITET_FYSIK1_2026-10-10.md](AKTIVITET_FYSIK1_2026-10-10.md) och motsvarande JSON. Kärnfysikstatus omfattar nu 179 av 450 uppgifter, inte hela Fysik 1 eller dess andra granskningsvarv.

Ett gammalt slutsvar kan vara fel även när beräkningen före det är korrekt: 9.27a/b ska ge 4,5/2,25 µg, 9.43a betyder 15 sönderfall/s, 9.58b söker 60 minuter och inte 500 Bq, 9.80a söker två halveringstider och inte 2⁻², 9.81b/c och 9.82b hade motstridiga gamla slutsvar, 9.88b söker fyra halveringstider och inte 50 Bq. Varje kort ska använda egna givna mellanvärden (9.5c, 9.18c, 9.30b, 9.81b/c, 9.85b, 9.345c/d, 9.359b/c, 9.360b/c) och ha bara relevanta data.

Direkt halvering, igenkänd halvminskning och enkel division är nivå 1: 9.123, 9.134, 9.135, 9.136, 9.146. Vanliga enhetsomvandlingar och direkt användning av halveringsformel är nivå 2: 9.57, 9.139, 9.142, 9.143, 9.335, 9.338. Att lösa en exponentialekvation med logaritmer är nivå 3. Två olika isotopers ändrade kvot eller förorenat kol kräver egna modellval och ligger högre (9.151, 9.348, 9.352, 9.357, 9.427). Facit visar logaritmsteget innan tiden löses ut, utan numrerade steg.

Sönderfall minskar mängden ursprunglig radioaktiv isotop, inte nödvändigtvis hela provets massa (9.27). Trämassa är inte kolmassa: 9.426c måste ange 200 g kol för att kunna använda Bq per gram kol. Andelar i blandningar avser tydligt kolmassan eller antalet kärnor (9.151, 9.342, 9.357). En isotops egen aktivitet ska inte utan vidare kallas total aktivitet inklusive radioaktiva dotterämnen (9.5, 9.341, 9.355, 9.358, 9.359). Rymdkällan 9.360 söker värmeeffekt och använder given energi per sönderfall, inte en alfapartikels energi som om den säkert var all energi eller elektrisk effekt.

9.84:s skärning är cirka 15,6 dygn, inte 26, när X börjar på 600 Bq med T = 20 dygn och Y på 400 Bq med T = 80 dygn. Raka segment gav även fel skärning. 9.11, 9.37 och 9.84 har nu exponentiella SVG-kurvor med kontrollerade skalor och tydligt placerade axel-/kurvnamn. Avläsningstoleranser får inte bytas mot exakt algebraisk rättning. 9.346 anger att den extremt lilla aktiviteten är ett medelvärde från en matematisk modell, inte en bråkdel av en verklig kvarvarande kärna. 9.427:s antagna startkvot är en modell, inte en säker bestämning av solsystemets ålder.

Kunskapsgymmets enhetstolkning behandlar upphöjda exponenter och vanlig notation lika: år⁻¹, år^-1, 1/år samt s⁻¹, s^-1, 1/s. I ett svar som "0,12 1/s" tillhör ettan enheten; den får inte bli en extra decimal i talet. Kontrollerade analoger: 9.83a, 9.143, 9.335a, 9.85a, 9.81a och 9.345a. Se tools/fysik1-aktivitet.test.js, konsumentens tools/radioaktiva-enheter.test.js och tools/aktivitet-fy1-2026-10-10.browser.py. Tidigare kärn- och kretskontroller passerar också.

## FP16 – stråldoser: bestrålad vävnad, dosenheter och pedagogiska energiintermediater (2026-10-10)

Alla 77 uppgifter har granskats manuellt. ID, ändrade fält och kommentarsförslag finns i [STRALDOSER_FYSIK1_2026-10-10.md](STRALDOSER_FYSIK1_2026-10-10.md) och motsvarande JSON. Kapitelstatus är nu 256 av 450; hela Fysik 1 och andra granskningsvarvet är inte färdiga.

Ekvivalenta doser får summeras för samma vävnad, inte för olika organ och sedan kallas kroppens ekvivalenta dos (9.15, 9.89, 9.178, 9.186, 9.189). Lungdos får inte beräknas med helkroppsmassa: 9.367/9.384 anger nu den bestrålade vävnadens massa och en uttrycklig isotopmodell. Bara egna sönderfall ingår och konstant radonmängd anges. Energi per sönderfall kan vara ett givet medelvärde; hävda inte att beta alltid har en enda energi eller att en förenklad koboltmodell är hela sönderfallsschemat (9.368, 9.369, 9.373, 9.378, 9.386, 9.387).

Direkt dos-/energi-/tidssamband är nivå 1, inte automatiskt C eller A: 9.153, 9.154, 9.168, 9.170, 9.176, 9.179, 9.259. Omvända viktfaktorer, skärmningstid och genomsläppt procent ger variation (9.174, 9.176, 9.180, 9.182, 9.188, 9.194). 9.178 var identisk med 9.159 och använder nu två undersökningar i samma vävnad.

Visa energi per partikel, total energi och dos i rätt enheter innan ekvivalent dos: 9.365, 9.366, 9.368, 9.369, 9.371, 9.375, 9.378, 9.379, 9.387. Delkort med egna avrundade givna värden måste ha motsvarande eget mål (9.94, 9.97, 9.98, 9.373, 9.380, 9.385, 9.386); föräldern får använda full precision. 9.370 kräver summerat antal sönderfall när aktiviteten avtar, inte konstant startdosrat. 9.372 söker 25 µSv per undersökning; Sv och mSv ska fungera efter korrekt omräkning. Temperaturökning 9.363/9.365b använder temperaturandring utan 273-offset.

9.96 har en jämnt graderad avståndsskala; gamla bågar hade inte strålkällan som centrum. Bakgrundsrektangeln vid viewBox-kanten är avsiktlig. 9.378b och 9.381 har kortare formler för mobil. Skyddande tester: tools/fysik1-straldoser.test.js och konsumentens tools/straldoser-fy1-2026-10-10.browser.py.

## FP17 – halveringstjocklek, entydiga alternativ och fotonenergi (2026-10-10)

38 uppgifter manuellt granskade i [STRALNING_FYSIK1_2026-10-10.md](STRALNING_FYSIK1_2026-10-10.md) och motsvarande JSON. 9.13c söker cirka 7,97 cm och hade inget numeriskt rättningsmål; detta är nu självrättande. Halveringstjocklek ska finnas på varje eget kort. Facit visar antal skikt, kvarvarande andel och vid behov logaritmen (9.2, 9.13, 9.93, 9.184, 9.187, 9.190, 9.193, 9.284, 9.286). De tidigare nivå 4-klonerna är rutinfrågor på nivå 2 och söker nu olika storheter. 9.190 söker exakt fem plattor; tolerans 0 på antal.

9.256 hade synligt ljus som felalternativ till strålning som stoppas av papper. Papper kan även stoppa synligt ljus; alternativet är nu beta. Begränsa materialjämförelser till givna alternativ (9.282). En alfastrålare ska inte beskrivas som ovillkorligt ofarlig utanför kroppen (9.7, 9.283). En elektromagnetisk jämförelse av fotonernas kemiska verkan är inte ett påstående att radiovågor aldrig kan avge energi eller skada genom värme (9.313). Korrekt fotonmodell och prefix kontrolleras också i 9.310, 9.311, 9.323, 9.324, 9.325 och 9.327.

E=hf och E=hc/λ med rutinomvandlingar är nivå 2, inte automatiskt C/3. Använd full numerisk precision för rättningsmål men korta beräkningsrader i facit. 9.305/9.324 innehöll trasig text i matteblock; denna är borttagen. Långa halveringskedjor delas för mobil. SVG 9.7 har större etiketter utan betakrock och visar att gamma dämpas gradvis. Tester: tools/fysik1-stralning.test.js samt konsumentens tools/stralning-fy1-2026-10-10.browser.py.

## FP18 – medicinska kortmodeller och enkla partikelbegrepp (2026-10-10)

41 manuellt granskade uppgifter finns med ID, ändrade fält och kommentar i [PARTIKLAR_MEDICIN_FYSIK1_2026-10-10.md](PARTIKLAR_MEDICIN_FYSIK1_2026-10-10.md) och motsvarande JSON. Kapitelstatus: 335 av 450. Hela Fysik 1 och andra varvet pågår.

9.3 hade omkastade a/b i lärarfacit; aktivitet 50 MBq hör till a och tre halveringstider till b. Varje kort ska bara visa relevanta data (9.3, 9.12, 9.28, 9.56, 9.92, 9.329). Lärarens härledning i 9.28a är fortsatt manuell; spelet får formeln och rättar numeriskt. 9.28b använder kortets 7,27 dygn. Skilj patientens biologiska utsöndring från en modell med bara radioaktivt sönderfall (9.3, 9.28, 9.296, 9.302). 20 GBq i 9.56 är ett produktionsparti, inte en given patientdos. Undvik absolut måste produceras nära och bestämd tidpunkt när bestrålning slutar (9.56, 9.299).

Gammastrålning väljs för att en del kan registreras utanför kroppen, inte för att varje sönderfall ovillkorligt ger lägre dos (9.297). Doser adderas i all bestrålad vävnad; tre riktningar kan koncentrera hög sammanlagd dos i tumören (9.301 med ny SVG). 9.92 anger värmekapacitet och att energin blir värme; temperaturandring används för K och °C. 9.298 har korrekt summa 1022 keV och godtar normal avrundning.

Direkt partikelklassificering och kvarkladdning är nivå 1 (9.261–9.263, 9.268, 9.269, 9.273, 9.275, 9.279). Antikvarkars teckenbyte nivå 2. Omvänt kvarkantal 9.329 får två fristående kort på C/3 med exakt heltalsrättning; samma svar får inte godtas med decimalavvikelse. 9.326/9.328 visar att 1/r² förkortas bort och har delade beräkningsrader för mobil. Tester: tools/fysik1-partiklar-medicin.test.js och konsumentens tools/partiklar-medicin-fy1-2026-10-10.browser.py.

## FP19 – beta-/elektroninfångningsenergi och alla efterfrågade svar (2026-10-10)

Alla 23 uppgifter i sönderfall granskade manuellt; se [SONDERFALL_FYSIK1_2026-10-10.md](SONDERFALL_FYSIK1_2026-10-10.md) och motsvarande JSON. Kapitelstatus 358 av 450; hela banken och andra varvet pågår.

Med neutrala atommassor: beta-minus och elektroninfångning använder masskillnaden direkt, beta-plus drar bort två elektronmassor. Positronens massa och skillnaden i de neutrala atomernas elektronantal måste båda förklaras (9.26, 9.45, 9.72, KG-FY1-BP-04). Den sistnämnda frågan krävde förklaringen men facit hade tidigare bara beräkningen. 9.72b söker både beta-plus och elektroninfångning och får två namngivna svarsfält i den ordningen. Fri lärarmotivering får inte bli numeriskt självrättande. 9.8c använder sitt eget givna 2,62 MeV; föräldern använder full energi från massdefekten. Den givna massdefekten kopplas inte längre till ett ogrundat specifikt aluminium-26-sönderfall.

En ändring av atomnummer är nivå 1 (9.248, 9.314, 9.315, 9.317, 9.318, 9.319). Dotterkärnans neutronantal kräver också A−Z och är nivå 2 (9.316). Reaktionsformler och fria förklaringar kan behållas som läraruppgifter utan spelkort (9.74, 9.77, KG-FY1-BM-02/03/04, KG-FY1-BP-02/03). Ledtråden ska gälla aktuell betatyp, inte alfa, friktion eller ett allmänt stegupplägg.

Tester: tools/fysik1-sonderfall.test.js och konsumentens tools/sonderfall-fy1-2026-10-10.browser.py. Ett felaktigt escape i beta-kommandot fångades av både kontrollteckenregression och faktisk KaTeX-visning, och rättades före leverans.

## FP20 – fission: enheter, massprecision och självständiga energikedjor (2026-10-10)

Alla 26 uppgifter manuellt granskade: [FISSION_FYSIK1_2026-10-10.md](FISSION_FYSIK1_2026-10-10.md) och JSON med alla ID, ändrade fält och kommentarer. Kapitelstatus 384 av 450; hela banken och andra varvet pågår.

9.16b visade km fast rättningen väntade mil. 9.412 söker massflöde och rättas i kg/s. Skilj massan som klyvs från massan som omvandlas till energi (9.104, 9.199, 9.200, 9.407, 9.409). Behåll atommassornas decimaler fram till massdefekten; allmän procenttolerans får inte dölja det sökta resultatet (9.401–9.403). 9.402 får märkta fält för både neutronantal och energi; antalet är exakt. 9.403 visar 232,79 u och tolerans 0,005 u. Hela kollisioner/markytor avrundas uppåt och rättas exakt (9.404, 9.406b).

Fristående kort räknar med sina egna givna mellanvärden (9.9, 9.16, 9.42, 9.407, 9.408, 9.410, 9.411), inte förälderns osynliga fullprecision. Varje kort har bara nödvändiga data. El och värmeeffekt skiljs åt. Formelrader delas för mobil utan att nödvändiga beräkningar hoppas över. SVG 9.70:s axel anger bindningsenergi per nukleon, inte total energi. Tester: tools/fysik1-fission.test.js samt konsumentens tools/fission-fy1-2026-10-10.browser.py.

## FP21 – fusion: bränsleblandning, medelenergi och kortdata (2026-10-10)

Alla 19 uppgifter manuellt granskade: [FUSION_FYSIK1_2026-10-10.md](FUSION_FYSIK1_2026-10-10.md) och motsvarande JSON. Kapitelstatus 403 av 450.

Påstå inte att all fusion kräver över hundra miljoner kelvin: solens fusion sker vid lägre temperatur. 9.288 gäller hög temperatur i en D–T-reaktor och den ökade chansen att kärnorna kommer nära. 9.295 skiljer tillgången på deuterium i vatten från tritium som behöver framställas; ingen generell avfallsgaranti. 9.415 avser fria protoner, inte neutrala atomer i solens inre. Farten som motsvarar genomsnittlig rörelseenergi är inte medelfarten.

9.71 anger lika antal D och T och fullständig reaktion; ett kilo bränsle utan blandning är otydligt. Två märkta fält rättar massminskning och energi. Figurens nukleoner bevaras: två protoner och tre neutroner. Frigjord energi får inte jämställas med el utan verkningsgrad (9.416–9.418); massflöde anges i kg/s. Kort räknar med egna givna mellanvärden (9.46, 9.71, 9.415–9.420). Råa LaTeX-komman får inte ligga i vanlig text; procenttecken måste escape:as i matte.

Lösningar visar massor före/efter, massminskning, energi per reaktion, antal och förbrukad massa där sambanden behövs (9.53, 9.71, 9.414, 9.416–9.419). Undvik tidig massavrundning. 9.290 kräver sex decimaler och har toleransen 0,0000005 u. Tester: tools/fysik1-fusion.test.js och konsumentens tools/fusion-fy1-2026-10-10.browser.py.

## FP22 – kärnreaktioner: rekyl, precisa massor och alla sökta svar (2026-10-10)

Alla 47 uppgifter manuellt granskade: [KARNREAKTIONER_FYSIK1_2026-10-10.md](KARNREAKTIONER_FYSIK1_2026-10-10.md) och JSON med alla ID, bedömningar och kommentarer. Kapitel 9:s första manuella pass är klart: 450 av 450. Hela banken och andra varvet är inte slutmarkerade.

Atommassetolerans får inte dölja massdefekten: 9.10b rättas till sex decimaler med 0,0000005 u; 9.116/117 till fem decimaler med 0,000005 u. Liknande redan kontrollerat i 9.290 och 9.403. Neutron-/sönderfallsantal är exakta heltal (9.195, 9.196, 9.114, 9.73, KG-FY1-ALFA-04, 9.320–9.322). 9.100/101 får fulla mål 0,072 respektive 0,1035 TJ och given c.

Alfapartikelns energi är inte hela reaktionsenergin. Dotterkärnan får rekylenergi. 9.119:s uppmätta alfaenergier 4,785/4,602 MeV ger cirka 4,87 MeV totalenergi och 0,186 MeV gamma i den givna massmodellen. Gammaformeln ges där den behövs. 9.49/111 härleder lika stora motriktade rörelsemängder och Eₖ = p²/(2m), fördelar energin och räknar båda farterna i kg/J. Två efterfrågade svar får två märkta fält, fri lärarhärledning förblir manuell. Kontrollerade energikedjor: 9.10, 9.49, 9.69, 9.76, 9.109–9.111, 9.115, 9.118/119.

Eget avrundat mellanvärde styr kortets mål (9.10, 9.49, 9.69, 9.73, 9.110, 9.111, 9.119). Reaktionsformeluppgifter ska inte innehålla ovidkommande energiberäkning (9.105–9.108, 9.112/113). 9.108:s orealistiska B-8 till Li-4 genom direkt alfa ersatt av Po-216 till Pb-212. 9.78 anger sönderfallstyper och nödvändiga grundämnen. 9.51:s figur visar exakta ΔN/ΔZ, tabellen använder HTML för mobil läsbarhet. 9.119:s figur skiljer alfaenergi och energinivåer och är uttryckligen schematisk. Tester: tools/fysik1-karnreaktioner.test.js och konsumentens tools/karnreaktioner-fy1-2026-10-10.browser.py.

## FP23 – enheter: avrundningsintervall och bara kortets egna data (2026-10-10)

Alla 59 uppgifter i enheter är manuellt genomlästa igen. Se [ENHETER_FYSIK1_2026-10-10.md](ENHETER_FYSIK1_2026-10-10.md) och JSON med samtliga ID, bedömningar och kommentarer.

Exakt matchning av ett avrundat facittal avvisar korrekt extra precision. Använd halva avrundningssteget som tolerans när frågan anger en viss precision (2.11, 2.12, 2.29, 2.35, 2.59, 2.68, 2.214, 2.219, 2.221, 2.222). Nästa felaktiga avrundade svar ska avvisas; använd inte ett generellt procentintervall för dessa precisa frågor. Exakta prefixomvandlingar behåller sin rättning.

2.12b anger egna 19,8 bildpunkter/mm och rättar 50,5 µm; lärarens kedja rättar 50,6 µm från de fullständiga skärmdata. 2.11, 2.29, 2.35 och 2.36 visar bara relevanta givna data per kort. 2.66 ska inte kalla volt/ohm SI-grundenheter. 2.226/227 ger märkta fält för samtliga exponenter/faktor och förklarar jämförelsen med meter/sekundexponenter. Fri lärarjämförelse av bilarnas tillförda energi bevaras i 2.36; ovidkommande klimat/kostnadsförbehåll behövs inte.

Långa likhetskedjor delas för mobil med alla mellanled kvar (2.205, 2.210, 2.29, 2.218, 2.63, 2.219, 2.67, 2.72, 2.75, 2.76). Modellpelaren i 2.63 har begripligare språk men behåller massa ∝ längd³, maxkraft ∝ area och kvoten maxkraft/tyngd. Tester: tools/fysik1-enheter-avrundning.test.js och konsumentens tools/enheter-fy1-2026-10-10.browser.py. Helbankens tekniska kontroll finns nu i konsumentens tools/fysik1-hela-banken.browser.py; den ersätter inte manuell fysikgranskning.

## FP24 – funktionsvänsterled, relativa ordsvar och LaTeX i rätt-svar-raden (2026-10-10)

Nio rapporter och fem analoger per rapport är granskade: [FELRAPPORTER_2026-10-10_1542.md](FELRAPPORTER_2026-10-10_1542.md) och motsvarande JSON listar samtliga 54 ID, 12 åtgärdade och 42 utan fel samt kommentarsförslag. Detta avslutar inte hela bankens manuella andra varv.

Pröva faktiskt elevens naturliga svar i `checkAnswer`, inte bara bankens eget facit genom parsern. #5.564 b godtar redan 11 200 W/11,2 kW och #6.241 godtar 48,0 kg; toleransen ska inte vidgas utan belägg. #6.65 a hade rätt facit men frågan förtydligar nu att lufttrycket ingår. Granskade tryckanalogier omfattar #6.66–70 och #6.240/#6.242–245.

#2.378 använder fullprecisionsmålet lg(20/3)/lg(1,4), numeriskt format och tolerans 0,005. `5,64`, `x=5,64`, `x≈5,64` och logaritmuttrycket godtas, 5,65 avvisas. LaTeX `\approx` och `{,}` normaliseras även i facit. #2.137 b och #2.141 c får uttrycksformat så funktionsvänsterled godtas; a:s faktorisering jämför högerleden innan produktformen kontrolleras. Självständigt b-kort i #2.137 får faktorformen direkt och visar multiplikation/samling i facit. Analoger: #2.139/#2.141/#2.143–145 och #2.375/#2.377/#2.379/#2.381/#2.382.

#2.731:s matematik och rotparser var korrekta. Den oordnade svarsvägen visade däremot rå LaTeX efter ett felaktigt försök. Även denna väg måste använda `facitText`/`visatSvar` och `renderMath`; oordnade rötter får inte passera som dubblerade svar. Fem kontrollerade analoger: #2.32/#2.132/#2.193/#2.198/#2.242. Lägg inte nya specialskrivkrav i uppgiftstexten för att dölja ett presentationsfel.

`multipel` är ett uttryckligt format för storleksförhållanden (#6.553/#6.534/#6.552), där exempelvis "dubbelt" och "dubbelt så stort" betyder 2. Det ska inte aktiveras för antal, kraft, tryck eller andra mått med enheter. Ordigenkänningen är förankrad till hela svaret och avvisar negationer/motsägelser. Även #6.42/#6.94/#6.95 kontrollerade utan ändrat matematiskt svar.

Delmängdsfrågor på ingångsnivå ska tydliggöra att tomma och hela mängden ingår. #1.565–567 (matf1) får konkreta mängder, ledtråd om med/inte med och konsekvent nivå 2. Ändra inte till propera eller icke-tomma delmängder av misstag. Analoger #1.169/#1.614/#1.784 är räknade med sina villkor.

Regressioner: master `tools/felrapporter-2026-10-10.test.js`; konsument `tools/multipel.test.js` och `tools/felrapporter-2026-10-10.browser.py`. De faktiska fälten, ordningsoberoende rötter och LaTeX-korrigeringen kontrolleras utan XP/databasskrivningar. Ingen elevkontakt eller Supabase-statusändring ingår.

### Uppföljning: fy1 #5.385 (2026-10-10 16:56)

[Granskningslista och kommentarsförslag](FELRAPPORT_5_385_2026-10-10.md), med motsvarande JSON: #5.385 samt fem analoger #5.381/#5.382/#5.383/#5.384/#5.393 är granskade utan fel. Bollen vänder, så Δv är 50 − (−40) = 90 m/s och medelkraftens storlek 180 N. Behåll omvandlingarna 60 g → 0,060 kg och 30 ms → 0,030 s. Blanda inte ihop kraftens storlek med en tecknad komponent eller beräkna 50 − 40 vid riktningsbyte. Självrättningen godtar 180, 180 N, 180,0 N, 0,180 kN och 1.80e2 N; fel storlek/tecken avvisas. Inga innehålls- eller rättningsändringar behövs. Rörelsemängdstester 3/3 och faktiska svarsfält 26/26, 18 mobil-/datorvisningar utan KaTeX-fel; reproducerbar kontroll i konsumentens `tools/felrapport-5-385.browser.py`. Ingen elevinmatning finns i rapporten, så orsaken till den tidigare rapporteringen är okänd.

## FP25 – enhetssuffix får inte sluka prefix före numerisk rättning (2026-10-10)

[Felrapport #6.438 och fem analoger](FELRAPPORT_6_438_2026-10-10.md), med JSON som innehåller verifierade inmatningar. Facit ρgh = 1,20 · 9,82 · 35,0 = 412,44 Pa → 412 Pa var korrekt. Rättaren godkände felaktigt 412 kPa: målenheten Pa togs bort, sedan slängdes kvarvarande k bort i en genväg för tal utan enhet. Därmed blev ett tusen gånger för stort svar till det korrekta talet 412.

För format `numeriskt` med numeriskt facit och målenhet ska ett svar med känd utskriven enhet få en auktoritativ skal-/dimensionsjämförelse före borttagning av enhet. Korrekt omräkning till ett annat prefix måste fortfarande fungera. Undvik att denna väg kringgår representationkrav i exempelvis heltals- eller decimalformat, eller bestämmer numeriska värden av algebraiska facit genom att läsa första talet. Nakna talsvar och formatens övriga regler behålls.

Granskade/åtgärdade genom samma rättarfix: #6.438/#6.436/#6.437/#6.444/#6.445/#6.464. Alla sex har korrekta fysikfacit; inga bankobjekt ändras. Fem analoger lösta med egna givna data. #6.445 b använder kortets 17,2 kPa, inte förälderns fullprecisionsvärde. Tidigare rättare återskapar 15 prefixfel i dessa kort. Efter rättning: 68 verkliga fältkontroller och 30 mobil-/datorvisningar utan fel. Konsumenttester: `tools/numeriska-enhetsprefix.test.js` (Pa/N/J/W/C/m och fel dimension) och `tools/felrapport-6-438.browser.py`. Mastertester `tools/fysik1-vatsketryck.test.js` passerar. Elevens exakta inmatning är okänd; påstå inte att detta säkert orsakade rapporten.


## FP26 – fakultetssvar, formelbladets musdragning och tabellkonstanters precision (2026-10-11)

[Samtliga 14 granskade ID, åtgärder och kommentarer](FELRAPPORTER_2026-10-11_1009.md) och motsvarande JSON. Matf1 #1.510 ska godta 6! = 720: den rena talvägen måste tillåta ! och sedan använda den strikta numeriska parserns fakultet. Kvoter som 8!/5! och 9!/(2!*7!) ska jämföras numeriskt. Acceptera inte fel värde, variabler, ofullständig syntax, negativa/icke-heltalsfakulteter eller omtolka !! som upprepad vanlig fakultet. Fem analoger #1.509/#1.511–514 samt #1.528 är självständigt räknade. Uppgiftstexter och nivåer ändras inte för att dölja parserfelet. Skydd: konsumentens tools/exakta-talsvar.test.js och tools/felrapporter-2026-10-11.browser.py.

#1.528 rapporterar en gränssnittsfunktion, inte fel i facit 36. Alla fem riktiga PDF-formelblad har testats med musdragning i två riktningar, avslut, hjulrullning och zoom. Vänster musknapp får panorera vid zoom över 100 %. Rätta inte bankinnehåll på grund av ett allmänt gränssnittsönskemål.

FY1 #4.346: givet G = 6,674·10⁻¹¹ gav korrekt facit 118,6489 nN men för snävt tvådecimalskrav; G = 6,67·10⁻¹¹ gav 118,5778 nN. Kräv nu tre värdesiffror (119 nN) och lagra fullständigt numeriskt mål med halva avrundningsstegets tolerans. #4.9/#4.364/#4.367/#4.372 får rimligare precision med både tabellvärdena verifierade. #4.363/#4.375 avvisade inte dessa svar före ändring; den förstnämnda har ändå harmoniserad precision och fullständigt numeriskt mål. Blanda inte konstantskillnad med felaktiga kraftenheter, tecken eller fysikmodeller. #4.367:s typtext måste avse planetradie. #4.9:s egna delar ska bevara alla planetdata och fullständiga uträkningar; #4.372 visar insättning i densitetsformeln. Skydd: master tools/gravitationskonstant-precision.test.js och befintliga tools/fysik1-kapitel4.test.js samt konsumentens riktade webbläsartest.

## FP27 – statistikfigurer, lodräta tabeller och namngivna delkort (2026-10-11)

[Alla 40 granskade kontrollfall, åtgärder och kommentarsförslag](FELRAPPORTER_2026-10-11_1618.md) samt motsvarande JSON. Sju rapporter, minst fem analogier per bekräftat mönster. Detta är en riktad omgång; helbankens granskning slutmarkeras inte.

Normalfördelningens frågetecken får inte ha samma koordinater som μ+σ eller μ+2σ (#4.50/#4.196/#4.214). Kontrollera verklig textstorlek i mobilen. Breda datatabeller vänds med samtliga datapars koppling bevarad (#4.300 och nio analogier). Parvisa Alva/Bea-tider behåller loppordningen. Underliggande matematik ändras inte för att lösa ett layoutfel.

FP-02/FP-08 gäller även matematikkort: #4.95 c behöver sina egna 10 %-områden, #4.26 b sin egen andel, #4.72 b/#4.87 c intervallets beskrivning. Fristående namngivna storheter kräver delens egna `svarsstruktur:"ordnad"` och `svarEtiketter`; förälderns ordning räcker inte när `expandGameTask` skapar en mängd som standard. #2.711 och nio analogier rättade. Ändra inte denna standard generellt: rötter ska fortsatt vara oordnade. #2.407/#2.436 får lokala facit utan läckor.

#4.299:s bortstrukna sämsta tid ger σ = 0,554977… → 0,55 s. #4.302:s ”alltid minskar” gäller inte redan noll spridning. #4.300:s r = −0,985079881… rättas från full precision med 0,005; #4.95:s percentilgränser får 0,05 för en decimal. Fysik #5.99 a är rätt kurs och #6.300 har korrekt 7 856 Pa med angivet g/heltalskrav. Vid rapport utan elevinmatning ska okänd tidigare orsak redovisas; vidga inte toleransen utan belägg.

Skydd: master `tools/felrapporter-2026-10-11-1618.test.js`, konsument `tools/delkort.test.js` och `tools/felrapporter-2026-10-11-1618.browser.py`. Browserkontrollen måste verkligen ladda KaTeX innan rå LaTeX/överbredd bedöms.

## FP28 – precisionsvisning för heltal, modelldefinitioner och explicit Sx/σx (2026-10-11)

[Alla 20 granskade ID, 18 åtgärdade/förtydligade och 2 utan fel samt kommentarsförslag](FELRAPPORTER_2026-10-11_1749.md) och motsvarande JSON. Fyra rapporter, sex analoger för precisionsvisning och fem vardera för modelldefinitioner och standardavvikelse. 11 bankobjekt ändras; sju ytterligare fysikuppgifter får förbättrad kortfacitvisning genom samma kodfix. Detta är en riktad omgång.

Kortfacit måste tillämpa precision innan det returnerar heltal. Betydelsefulla nollor får inte försvinna genom Number(...). 30 N med tre värdesiffror visas som 30,0 N; 17 676 J visas som 1,77·10⁴ J. Kontrollera exponentbyte efter avrundning, exempelvis 999,9 → 1,00·10³. Självrättningen behåller fullprecisionsmål och accepterar både rätt avrundning och extra precision. #5.575 a:s fysik och #5.497 b:s fulla lösning var redan korrekta. Ingen elevinmatning fanns i rapporterna; beskriv det demonstrerade visningsfelet utan att påstå att det säkert orsakade elevens tidigare rapport.

Ett funktionstecken förklarar inte storheten: definiera x/t, T/P/D och enheter i frågan (#5.162/#5.92/#5.90/#5.121). #5.79/#5.91 hade redan definitioner. Behåll matematiknivån och låt svarsenheten följa den definierade storheten. Nödvändiga insättningar och mellanled ska finnas kvar när formelrader delas för mobil.

Att datamaterialet kommer från mätningar avgör inte ensamt om frågan söker Sx eller σx. σx beskriver spridningen i alla angivna värden; Sx används här för uppskattning från ett stickprov. Ange målet uttryckligen. #5.94:s temperaturstickprov använder n−1 och ger 0,32 °C. #5.71:s tidigare s-beteckningar stämde inte med division med n; nu ges konsekvent Sx, 0,71/1,41 °C. #5.66/#5.110/#4.299 beskriver uttryckligen σx i de visade värdena, utan förändrade rättningsmål. #5.66:s tabell vänds med dataparen bevarade.

**Precisering av FP27/#4.306:** golfstickprovet får nu Sx som uttrycklig huvudmetod: 3,15 slag och intervallet 275,44–281,73. Andelen är fortfarande 75 %. Den tidigare beskrivande σx-metoden var inte felräknad; uppgiftens statistiska mål preciseras nu. Återställ inte metoden utan att samtidigt ändra fråga, facit och regressionstest.

Skydd: master `tools/felrapporter-2026-10-11-1749.test.js`, konsument `tools/prov-talformat.test.js` och `tools/felrapporter-2026-10-11-1749.browser.py`. Browserkontrollen laddar riktig KaTeX och testar verkliga svarsfält, kortfacit, prefixenheter och mobilformler. Ingen Supabase-status eller elevkommentar ändras genom push.

## FP29 – genomgång av stickprov, urval och spridningsmått (2026-10-11)

[Alla 177 granskade uppgifter, 41 åtgärdade/förtydligade och 136 utan ändring, med kommentarsförslag](STICKPROV_STANDARDAVVIKELSE_2026-10-11.md) och motsvarande JSON. Samtliga sju banker söktes; alla 54 ursprungliga uttryckliga stickprovsträffar finns i listan. Hela ma1-områdena urvalsmetoder/signifikans och hela ma2-standardavvikelse ingår, med relaterade frågor. Detta slutmarkerar inte andra bankdelar.

**Precisering av FP28/#4.299:** tvådecimalsfrågan om σx hade toleranser som även godkände de andra Sx-värdena. Den nya självständiga beräkningen och verkliga fältkontrollen visar felet. Fullprecisionsmål och 0,005 används nu; 0,23/0,65 godkänns, 0,25/0,71 avvisas. #4.299 d:s σ = 0,55 s bevaras. Ange uttryckligen σx vid beskrivning av hela den givna värdelistan och Sx när stickprovet ska uppskatta populationens spridning. Mätvärden i sig kräver inte Sx. Givna normalfördelningsparametrar ska inte räknas om med n−1. Analoger #4.05/#4.10/#4.28/#4.46/#4.97/#4.157/#4.306/#5.66/#5.71/#5.94/#5.110.

Exakta procentandelar av personer måste ge hela personer. Ma1 #5.571:s tidigare 60 % av 32 och 45 % av 28 var omöjliga exakta antal. Nu används 62,5 % av 32, 50 % av 28 och 30 % av 20: 20 + 14 + 6 = 40 av 80, alltså 50,0 %. Förklara viktningen med personantal; ett ovägt procentmedelvärde 47,5 % är fel. Kontrollanalogier #5.11/#5.60/#5.99/#5.105/#6.93. Uppgiften kalibreras från A/nivå 4 till C/nivå 3.

Nämn målgruppen när urvalets representativitet bedöms (#5.182/#5.221/#5.526/#5.535). Att bjuda in alla garanterar inte att alla svarar; #5.102 a anger faktisk total svarstäckning. Bortfall är uteblivna svar, medan bortfallsfel kräver att bortfallet snedvrider resultatet. Självurval är en separat urvalsmekanism (#5.174/#5.180). Signifikans ger ingen sannolikhet för att en hypotes är sann och betyder inte stor eller praktiskt viktig skillnad (#5.91/#5.545). Stratifiering med ospecificerat antal per grupp lovar inte samma inklusionssannolikhet (#5.566). Minst fem analoger per mönster finns i granskningsloggen.

Förälderns ordning räcker inte efter delning: skrivarnas egna #4.241-kort får namngivna ordnade fält. Facit visar varför kvadratsummorna är 8 och 16, och del a slipper en formel som bara behövs i b. Ledtrådar ska inte avslöja andra delars svar (#5.97). Konkreta begreppsfrågor behöver egna förklaringar (#5.175/#5.179/#5.181/#5.183). Breda formler delas med mellanleden kvar (#4.283/#4.284). #4.302:s nollspridningsundantag och #4.306:s Sx-metod bevaras.

Skydd: master `tools/stickprov-standardavvikelse.test.js` med oberoende beräkningsmodeller och konsument `tools/stickprov-standardavvikelse.browser.py` med 50 oberoende svarskontroller, 149 facitbaserade parser-/fältkontrakt och 388 mobil-/datorvisningar. Ett facitbaserat kontrakt bevisar inte att facit är matematiskt rätt. Tidigare 16:18/17:49-regressioner körs också; inga Supabase-statusar eller elevkommentarer ändras.

## FP30 – mellanprecision och rätt avrundningsgranne vid exakt halvsteg (2026-10-11)

[Rapporterna 19:02: alla 43 granskade uppgifter/delkort, 33 åtgärdade och 10 utan fel, med kommentarer](FELRAPPORTER_2026-10-11_1902.md) och motsvarande JSON. Granskningen omfattar fyra rapporter, minst fem analoger per mönster och samtliga 16 identifierade exakta halvsteg med tre värdesiffror i kapitel 5–6. Andra delar av delvis granskade uppgifter slutmarkeras inte.

Fy1 #5.224: gamla 3,47 m var korrekt med det angivna 1,45 N. Elevens 3,48 m följer den oavrundade bromskraften från a. Föräldern använder nu samma F utan mellanavrundning; eget b-kort ger 1,4457 N och får eget fullprecisionsmål. Båda ger 3,48 m med två decimaler. Toleransen 0,005 vidgas inte. Detta preciserar energigranskningen 2026-10-09. Återställ inte andra kort till osynliga föräldravärden: #5.485/#5.508/#5.514/#5.537/#5.543 har sina uttryckliga givna scenarier, som räknas självständigt.

**Undantag till fullprecisionscentrum vid verifierat exakt halvsteg:** 4805 ± 5 N godkände både rätt avrundning 4810 och fel 4800. Rättningen centreras nu på den rätt avrundade grannen 4810, med samma tolerans 5. Fullvärdet 4805 godtas fortfarande och finns kvar i lösningen. Detta tillämpas endast på de 16 självständigt verifierade fallen i loggen; ingen generell procenttolerans införs. Båda grannavrundningarna och fullvärdet ska testas i verkliga fält. Negativa halvsteg avrundas bort från noll: −2,835 → −2,84. Binära talfel nära exakt decimalhalva får inte göra att kortfacit visar fel granne (#5.270/#5.381).

Halvsteg: #5.72 a/#5.270/#5.160 d/#5.370 a/#5.375/#5.381 a/#5.209 c/#5.578 a/#5.505 c/#5.509 b/#5.514 d/#6.457 b/#5.529 b/#5.533 a/#5.418 b/#5.440 c. De redan korrekta fysiklösningarna behåller sina fulla mellanvärden. Tidigare regressioner kontrollerar både oberoende fullvärde och uttryckligt avrundat rättningscentrum för berörda fält; alla andra exakta mål skyddas som tidigare.

Ma1 #0.992 anger nu en decimal och tom startpool: 3,125 h → 3,1 h, fullprecision godtas, 3,0/3,2 avvisas. #0.991 anger två decimaler. Grundläggande proportionalitetsrutiner #0.987–993 är E/nivå 2; #0.994:s två symboliska proportioner är C/nivå 3, inte A/5. Fy1 #6.105 behöver bara tryckökningen från vattenytan; fem djupanalogier är kontrollerade. #6.261:s subtraktion och formelinsättning är E/2. #5.55 a var redan korrekt och tydligt efter den tidigare granskningen: 25 g = 0,025 kg. Ingen elevinmatning finns i rapporten, så dess tidigare orsak är okänd.

Åtta breda mobilformler delas med alla nödvändiga mellanled kvar (#5.543 b/#6.264/#5.52 c/#5.474 c/#5.492 b/#5.494/#5.160 d och ma1 #0.987). Skydd: master `tools/felrapporter-2026-10-11-1902.test.js`, berörda äldre fysiktester och konsument `tools/felrapporter-2026-10-11-1902.browser.py`: 118 svarskontroller, 16 kortfacitvisningar och 118 mobil-/datorvisningar. Ingen Supabase-status eller elevkommentar ändras.

## FP31 – alternativa kelvinsvar ska följa rätt del även i heluppgiften (2026-10-11)

[Rapport 19:39: alla granskade ID, åtgärder och kommentarsförslag](FELRAPPORT_2026-10-11_1939.md) och motsvarande JSON. #6.21 a är korrekt: både 273 och 273,15 ger 170,5 bar och godkänns. Elevens exakta svar saknas, så den rapporterade underkänningen i a har inte återskapats.

När hela uppgiften rättades kunde b:s lokala svarindex läsa a:s `rättSvar273`. Det underkände giltiga alternativa svar i #6.21 b (13,7 %), #6.22 b (92,2 °C), #6.201 b (oavrundat 131,285714… °C) och #6.213 b (7,40 %). Fristående kort fungerade redan. `svarsPlan` måste bära alternativ per del och per svar; `checkAnswer` ska använda delens metadata. Ändra inte facit eller vidga toleransen för att dölja ett indexfel.

Följdgranskade heluppgifter #6.4/#6.54/#6.513 godkände redan kontrollfallen genom sin ordinarie tolerans. Enkla analoger #6.19/#6.20/#6.50/#6.84/#6.214/#6.221 är också kontrollerade med båda omvandlingarna. Uppgiftstexten får fortsatt inte föreskriva 273 eller 273,15; facit kan räkna med 273,15. En faktiskt given kelvintemperatur ska behållas.

Skydd: konsumentens `tools/delkort.test.js` och `tools/felrapport-2026-10-11-1939.browser.py` testar riktiga svarsfält, heluppgifter, oavrundade/avrundade värden, enheter och nästlade metadata. Mastertester och tidigare temperatur-/gaslagskontroller behålls. Inga bankobjekt ändras i denna runda.

## FP32 – x/X i numerisk grundpotensform och hela enhetsprefixet (2026-10-11)

[Rapport 21:46: alla sex granskade ID, åtgärder och kommentarsförslag](FELRAPPORT_2026-10-11_2146.md) samt motsvarande JSON. Fy1 #6.445 a har korrekt facit: 17 175,18 Pa → 17 200 Pa. Vanlig avrundning godkändes redan, men `1,72x10^4` underkändes. Elevens exakta inmatning saknas; påstå inte att den bekräftade parserbristen säkert orsakade just rapporten.

Bokstaven x/X får beteckna gånger endast mellan en numerisk koefficient och en tiopotens. Normalisera före både strikt talrättning och tal-/enhetsdelning: annars kan prefix försvinna när målenheten tas bort. Tal-/enhetsfunktionerna ska läsa hela exponenten även med +. Ändra inte generell symbolisk multiplikation, toleranser eller svarsenheter. Fel dimension, tusen gånger fel svar och ofullständig syntax ska fortfarande avvisas. Originalkedjan godkände redan *-skrivna positiva exponenter genom en annan rättningsväg; dess lägre parserbrist är inte samma sak som att alla sådana svar underkändes.

Fem analoger #6.436/#6.437/#6.438/#6.444/#6.464 är självständigt räknade. Alla sex fysikfacit är korrekta. Åtta jämförelsekorts breda formelrader delas med alla mellanled bevarade, även i huvudfacit. #6.445 b behåller sina egna 17,2 kPa och 0,94 cm²: 1,6168 N → 1,6 N. Det är fortfarande nivå 2, a nivå 1.

Skydd: konsumentens `tools/numeriska-enhetsprefix.test.js` och `tools/felrapport-6-445.browser.py` (202 fältkontroller, 30 mobil-/datorvisningar och kortfacit), samt master `tools/fysik1-vatsketryck.test.js`. Gamla tester och rättningsmål behålls. Ingen rapportstatus eller elevkommentar sparas genom en Git-push.

## FP33 – Ma1-enheter, räntekort, avgiftsordning och hela kronor (2026-10-12)

[Alla 42 granskade uppgifter, 34 åtgärdade/förtydligade, 8 utan ändring och kommentarer](FELRAPPORTER_2026-10-12_0958.md) samt motsvarande JSON. Åtta rapporter: sju åtgärdade; fy1 #6.470 c har korrekt facit och rättning, 687,4 N → 690 N. Elevens exakta inmatning saknas och den tidigare underkänningen kan inte återskapas. Riktad kontroll, inte en slutmarkering av hela banken. #3.86 avser endast avgiftsmodell/saldoformler, inte olikhetsparsern.

Saknad `svarEnhet` kan få den generella rättningen att godkänna samma tal med helt fel dimension (#7.01/#3.39 och analoger). Lägg rätt enhet och strikt numeriskt format på bankobjektet; ändra inte den generella rättaren för alla matematiska uttryck. Tal utan enhet och rätt utskriven enhet ska godtas. #7.03:s uttryckliga enhetsomvandlingar använder `decimalform` och målenheten; en likvärdig storhet i ursprungsenheten besvarar inte den begärda omvandlingen. Procentfrågor får %-metadata och uttrycklig procentsats/precision (#3.08/#3.126 och fem analoger). Befintlig regel för andel utan %-tecken bevaras, medan exempelvis 0,03 % inte är 3 %.

Fristående #3.40 c måste ange startbeloppet 12 000 kr. #3.28 c måste ange att 1 875 kr är priset med moms. Andra kort får sina egna jämförelsebelopp och precisionskrav (#3.25/#3.26/#3.38/#3.88). Behåll huvuduppgiftens sammanhang och undvik facitläckor mellan egna kort. Avgiftens tidpunkt påverkar modellen: #3.258/#3.256 drar årsavgiften efter räntan; #3.84 gjorde redan det. #3.86:s omedelbara startavgift ligger före alla ränteår och får inte flyttas till slutet.

#3.223 anger nu hela kronor: 7 772 kr och fullvärdet 7 772,43 kr godkänns. Analoger #3.203/#3.217/#3.518–520 använder fullprecisionsmål med 0,5 kr; angränsande felavrundade heltal avvisas. Två decimaler ger 0,005 och en decimal 0,05. Detta ändrar inte FP30:s särskilda beslut vid exakt halvsteg. #3.88:s gamla 1 kr-tolerans var för bred för två decimaler. Nivå kalibreras på kortet: direkta faktor/summakort nivå 1, #3.127:s rutiner E/2, sammansatta räntor #3.80/#3.82 nivå 3. Ändra inte nivå enbart på grund av ett enhetsfel.

Skydd: master `tools/felrapporter-2026-10-12-0958.test.js`, tidigare Arkimedes-/Ma1-provtester och konsument `tools/felrapporter-2026-10-12-0958.browser.py`: 399 verkliga svarskontroller, 12 heluppgifter och 124 mobil-/datorvisningar. #3.07/#3.88/#6.473 får radbrutna formler med alla mellanled kvar. Fysik #6.470 c:s rättningsmål, två värdesiffror och nivå 1 bevaras. Inga rapportstatusar eller elevkommentarer skrivs genom push.

## ST01 – separata geometriska områdeskort i ma2c (2026-10-12)

[Beslut, genomförande och tester](MA2C_GEOMETRI_OMRADEN_2026-10-12.md) samt JSON-lista över 118 berörda huvuduppgifts-ID:n. Ma2c ska ha separata kort för ”Randvinklar och medelpunktsvinklar” och ”Kordasatsen och bisektrissatsen”. Ma2b behåller ”Cirkelgeometri”. `GRUPPMA2` kan begränsa en grupp med `kurs:[...]`; `getCards()` måste välja en grupp för aktuellt spår och behålla vanlig gruppering när kurslistan saknas.

Behåll OMR-nycklarna `randvinkel_medelpunkt` och `kordasatsen_biskarningssatsen` trots den senare nyckelns gamla stavning. Alla bankobjekt och sparade resultat använder fortfarande samma nycklar. Ingen resultatmigrering behövs för en ändring av visningsgrupper. Befintliga genomgångar kopplas genom OMR. Detta beslut gäller indelningen, inte uppgifternas facit eller nivåer. Skydd i konsumenten: `tools/ma2c-geometri-omraden.test.js` och `tools/ma2c-geometri-omraden.browser.py`.

## UI01 – mottagna dokument ska visas i Mina prov (2026-10-12)

[Orsak, rättning och verifiering](DELADE_DOKUMENT_2026-10-12.md). Uppgiftslabbets `ul_mina`-lista får inte filtreras till `roll==='agare'` i Mina-vyn: det gömmer dokument som mottagaren redan har accepterat. Visa den befintliga RPC-listan och behåll ägarkontroller för rollberoende åtgärder. Personliga delningar och skolans gemensamma bank har separata listor. Efter lyckad acceptans ska Mina-vyn öppnas och uppdateras; avböjning stannar i förfrågningsvyn och fel återaktiverar knappen. Inga databasbehörigheter eller medlemskap ändras av denna rättning. Skydd: `tools/delade-dokument.test.js`, `tools/delade-dokument.browser.py` och befintliga `tools/sparskydd.test.js` i master.

## UI02 – kursfilter och sortering av prov/övningsblad (2026-10-12)

[Genomförande och verifiering](DOKUMENT_FILTER_SORTERING_2026-10-12.md). Mina-vyn och Gemensamma banken ska erbjuda kurs/spår-filter och sortering på datum, kurs eller namn. Sökning kombinerar flera ord över namn, kurs, områden och kollega. Bygg kursval från aktuell ofiltrerad lista, behåll UI01:s mottagna dokument och ändra aldrig källistan vid sortering. Uppdatering behåller val; ny öppning och lyckad acceptans återställer filter så delade dokument syns. Skydd: `tools/delade-dokument.test.js`, `tools/delade-dokument.browser.py` och `tools/sparskydd.test.js`.

## FYM01 – momentanhastighet, momentanacceleration och tangenter (2026-10-12)

[15 nya uppgifter, nivåmotivering, facitkontroll och kommentarer](FYSIK1_MOMENTAN_2026-10-12.md), med maskinläsbar JSON-lista. Fysik 1 #3.410–3.424 ligger i befintliga s-t-/v-t-områden. En färdig tangent ska finnas i spelbara diagram där eleven ska bestämma en momentan lutning. Uppgifter som kräver egen tangentritning (#3.421–3.424) har `spel:false` och manuell bedömning; ändra inte detta bara för att facit också innehåller ett numeriskt värde. Bankkopiorna ska ändå vara identiska.

Hastigheten fås från lägeskurvans tangent och accelerationen från hastighetskurvans tangent. Två avlästa tangentpunkter behöver inte ligga på själva kurvan. Skilj grafens höjd från lutningen, fart från tecknad hastighet och medelvärde från momentanvärde. Handritade tangenter ger rimliga uppskattningar och ska inte rättas med en snäv numerisk tolerans. Nivå 1 gäller enkla begrepp, avläsning/koordinatskillnader och enhetsomvandling är normalt nivå 2; fler rutinberäkningar gör inte automatiskt en uppgift till C.

I Uppgiftslabbet kräver `altVisas()` att huvudtexten uttryckligen efterfrågar alternativ, exempelvis ”Välj ett alternativ”, för att alternativen ska följa med i lärarvyn. Nya #3.415/#3.420 kontrolleras i båda apparna. Skydd: `tools/fysik1-momentan.test.js`, `tools/fysik1-momentan.browser.py` och den utökade fullständiga inventeringen i `tools/fysik1-kapitel3.test.js`. Miniräknare tillåts i samtliga fysikuppgifter.

## FYM02 – egna tangenter, rutnät och grafiska uppskattningar (2026-10-12)

[15 ytterligare uppgifter med granskning och kommentarer](FYSIK1_EGNA_TANGENTER_2026-10-12.md), även som JSON. #3.425–3.439 har tydliga rutnät men inga färdiga tangenter i frågorna. De ska behålla manuell bedömning och `spel:false`. Lösningsfigurerna har korrekta tangenter med två avläsningspunkter. Frågan får inte kräva den exakta modellens decimaler från en handritad tangent.

Kontrollera fysisk lutning med båda axlarnas skalor, särskilt ms/s, min/s och cm/m. Samma ritade vinkel behöver inte betyda samma hastighet. Noll hastighet innebär inte alltid vändning (#3.429), noll acceleration innebär inte stillastående (#3.433), och låg medelfart utesluter inte en hög momentanfart (#3.437). Två lika hastigheter bevisar inte ensamma nollacceleration vid intervallets mittpunkt (#3.439); formulera det som en uppskattning. Nivå 4–5 ska kräva mer tanke, inte bara fler likadana beräkningar. Skydd: `tools/fysik1-egna-tangenter.test.js` och `tools/fysik1-egna-tangenter.browser.py`.

## FP34 – standardkonstanter och formelval hör till elevens arbete (2026-10-12)

**Uppföljning 2026-10-14:** Fy1 #4.364 saknade en uttrycklig fråga redan i
precisionstexten från 11 oktober; borttagandet av formeluppmaningen gjorde
bristen ännu tydligare. Skriv ”Bestäm planetens massa” utan att återinföra
standardkonstanten eller färdig formel i frågan. Gamla maskinsvar/toleranser
behålls. Ledtrådar får inte hänvisa till en ”given formel” som inte längre visas.
Se [granskning 13:25](FELRAPPORTER_2026-10-14_1325.md).

[Helbankens avgränsade granskning, alla ID, åtgärder och kommentarer](FYSIK_FORMELSAMLING_2026-10-12.md), med maskinläsbar JSON-logg. Användarbeslut: ge inte g, G, Coulombs konstant, e, h, c eller andra standardkonstanter/omvandlingar i frågan. Skriv inte ”Använd F = ma” eller liknande färdiga formelledningar. Regeln gäller också `spelIntro` och delkortens `t`/`fraga`. Facit ska fortsatt förklara formelval och insättning. Ledtrådar bakom separat knapp ingår inte i frågetexten.

Behåll nödvändiga situations- och experimentdata, materialvärden, fjäderkonstanter, modellplaneters g, lokala jämförelsevärden, riktning och fysikaliska villkor. En formel som eleven ska kritisera eller härleda är själva uppgiften och ska inte raderas. Granska träffar i sammanhanget; radera inte efter en bred regex på ”konstant”, ”=” eller ”använd”. Nivåer höjs inte automatiskt för att eleven söker en formel.

Åtta fy1-uppgifter har särskilt beräknade `svarTabell` per fält. Samma enhet, format och tolerans används för varje mål; inga generella toleranser vidgas. Vid uppdelning följer varianten rätt etikett. Ett delkort med egna `rättSvar`/mellanresultat måste ange egna varianter. `svarsPlan` måste koppla heluppgiftens tabellvariant till aktuell del. FP26 kompletteras eftersom givet G tas bort: 4.74/4.740/4.742 måste godta de två vanliga G-värdenas avrundningar. Kontrollera också olika cal-/hk-omvandlingar och partikelkonstanter. Skydd: master `tools/fysik-formelsamling.test.js` och konsumentens `tools/tabellkonstanter.test.js`/`tools/fysik-formelsamling.browser.py`.

## FP35 – LaTeX-lg och korrekt avrundade sannolikheter (2026-10-13)

[19 rapporter, alla 107 granskade ID, ändrade fält och kommentarsförslag](FELRAPPORTER_2026-10-13.md), även i JSON. `latexToPlain` ska normalisera `\lg` precis som ln/log även när argumentet följer direkt: ma2 #2.219 och fem analoger. Ändra inte rätt facit för att kringgå parserfelet.

Vid sannolikhetsformatet godtas exakta uttryck och korrekt avrundade decimaler/procent med minst två värdesiffror. Ett symmetriskt halvt avrundningsintervall godkände tidigare båda grannvärdena vid exakt mittpunkt: 1/16 ska bli 0,063, inte 0,062. Jämför med det faktiskt avrundade målet och en relativ flyttalsmarginal; en absolut epsilon får inte godkänna noll för små sannolikheter. Bevara explicit tolerans. Numeriska decimalsträngar ska visas lika avrundat som numeriska facit; exakta bråk ska behålla bråkformen. Ändra inte alla exakta bråk till decimaltal. Rapporterna saknar elevens exakta inmatning, så ett bekräftat parserfynd bevisar inte alltid orsaken till just elevens historiska fel.

## FP36 – primtalsfaktorisering kräver primtal men potenser är valfria (2026-10-13)

Matf1 #2.79/#2.157/#2.209 använder `primtalsfaktorisering`. Upprepade faktorer, ändrad faktorordning och positiva heltalspotenser är likvärdiga. Enbart ursprungstalet eller sammansatta faktorer är fel form, även om uttryckets numeriska värde stämmer. Formatet ska fånga svaret före generell uttrycksekvivalens och läsa hela inmatningen. Noll/negativa exponenter, addition och division ska inte smita igenom. SGD/MGM behåller numeriskt svar: att en metod använder primtalsfaktorisering innebär inte att slutsvaret måste ha denna form. Kompletterar FP03, ingen tidigare rättning tas bort.

## FP37 – fasvinklar, namngivna fält och fullständiga delkort (2026-10-13)

Mato2 #1.131/#1.81/#1.149 anger grader och avrundning när fasvinkeln inte är en standardvinkel. Bestäm R och v i tydliga fält; kontrollera R cos v och R sin v mot originalkoefficienterna. Bevara exakta radianer när uppgiften uttryckligen tränar dem. Flytta inte slentrianmässigt alla vinkeluppgifter till grader. #1.81 ligger nu i asinx_bcosx och ska inte flyttas tillbaka till radianernas kurvområde enbart på grund av äldre metadata.

En del med `svarsstruktur:"ordnad"` måste rätta sina inre fält i ordning också i heluppgiften; parentens a/b-etiketter bestämmer inte automatiskt ordningen på en nästlad lösningsmängd. R/v och max/min är ordnade; två ekvationsrötter och asymptoter kan vara oordnade. Använd konsumentens etablerade `svarsstruktur:"mängd"` för fria rötter, inte den okända strängen ”oordnad”. Fragment som ”medellinje och” ska bli kompletta frågor i både huvudtext och kort. Varje delfacit ska förklara just den delen utan att blanda in andra svar.

## FP38 – verklig variation och balanserad repetition (2026-10-13)

Mato1 #1.99 hade korrekt facit men flera andra ID:n innehöll samma kontinuitetsproblem. ID-spärrar räcker inte mot innehållskopior. Fem funktioner har varierats med självständigt verifierade gränsvärden, inklusive faktor2 i nämnaren och tredjegrad (C/nivå3).

Urvalet ska använda hela `passHistory`, inte enbart de senaste60 `lastIds`. Så länge ett tillgängligt kort inte visats ska det prioriteras före repetition. När hela poolen visats väljs bland korten med minst antal visningar i passet; undvik också direkt återkomst om alternativ finns. Felsvarskön får fortfarande repetera av pedagogiska skäl. Bakåtträning ska fortsatt ge0XP och får inte logga nya resultat. Ändra inte facit eller alla nivåer för att dölja ett urvalsproblem. Historiska elevpass kan inte förklaras säkert utan deras faktiska urval och svar.

## FP39 – båda linjevillkoren och begripliga nybörjarbegrepp (2026-10-13)

Ma2 #1.54/#1.347 är korrekta: vinkelrätheten bestämmer lutningen och den angivna punkten bestämmer m=9 respektive−1. Godkänn inte godtyckligt m när punkten är ett villkor. Föreslå **Granskad – inget fel** även om texten förtydligas. Matf1 #1.164:s union36 var rätt; konferensens ”föredrag” i #1.77 var också korrekt och betyder presentation, inte företag.

Säkerhetsfaktor måste definieras i Ma1:s enkla tillämpningsuppgifter. Tillåten last beräknas med division, nödvändig kapacitet med multiplikation. ”Frakt295kr. Total?” blir hela meningar och en tydlig fråga om kostnaden inklusive frakt. En enkel introduktionsuppgift får vara nivå1, men en ledning som uttryckligen ger hela svaret ska tas bort.

Skydd för FP35–39: master `tools/felrapporter-2026-10-13.test.js`, konsument `tools/felrapporter-2026-10-13.test.js` och `tools/felrapporter-2026-10-13.browser.py`, samt tidigare delkort-, exakt-tal-, kelvin-/tabellvariant- och passhistoriktester. Inga rapportstatusar eller elevkommentarer sparas genom Git-pushen.

## FP40 – diskreta ordningsantal och hela fakultetskedjor (2026-10-13)

[Rapport09:32, samtliga sex granskade ID, före/efter och kommentarer](FELRAPPORT_2026-10-13_0932.md), även i JSON. Matf1 #1.136:s facit720 var korrekt. `720` och `6!` fungerade redan genom FP26, medan `6!=720` och `6! sätt` underkändes. Dessutom godtog en numerisk standardtolerans720,01, som inte är ett antal ordningar. Fem analoger #1.509/#1.510/#1.511/#1.70/#1.72 är självständigt räknade; deras korrekta likhetskedjor underkändes också före ändring. Elevens exakta svar saknas, så den reproducerade bristen bevisar inte den historiska inmatningen.

Använd `svarFormat:"antal_satt"` och `tolerans:0` för de granskade dimensionlösa heltalsantalen. Potens, produkt, fakultet, numeriskt svar och en fullständig likhetskedja med samma korrekta antal ska godtas. Varje led kontrolleras; kasta aldrig bara bort vänsterledet i `5!=720`. Valfri ”sätt”/”ordningar” godtas, även efter ett uttryck. Okända suffix, bråkiga antal, `!!`, öppna uttryck och variabler underkänns. Vanliga svarsetiketter får vara frivilliga, men funktionsnamn som `sin(0)` får inte behandlas som en etikett och dölja ett felaktigt led.

Detta format använder säkert representerbara icke-negativa heltal. Applicera inte slentrianmässigt på mätetal, sannolikheter, primtalsfaktorisering eller stora heltal utanför det säkra området. Bevara FP26:s generella fakultetsparser och alla fysiktoleranser. `svarEnhet` ska vara tomt för dessa antal; en teknisk SI-enhetsväg får inte blockera tidigare giltiga fakulteter i äldre öppna flikar. Kompatibilitet med gamla klienten och nya banken är verifierad för tal/fakultet i samtliga sex uppgifter. Nivåer/frågor bevaras. #1.136:s facit och ledtråd förklarar antalet val per plats.

Skydd: master `tools/felrapport-1-136.test.js`, konsument `tools/antal-satt.test.js` och `tools/antal-satt.browser.py`; tidigare `tools/exakta-talsvar.test.js` och FP35–39-testen kvarstår. Ingen rapportstatus eller elevkommentar sparas genom Git-pushen.

## MA2S01 – varierad avläsning och tolkning av statistik (2026-10-13)

[Alla 15 nya uppgifter, facitkontroller, nivåmotiveringar och önskemålskommentar](MA2_STATISTIK_DIAGRAM_2026-10-13.md), även som JSON. Ma2 #4.307–4.321 gäller 2a/2b/2c och ger 18 fristående spelkort. Åtta huvuduppgifter ligger i det nya området `tabeller_diagram`; övriga ligger i befintliga områden för lägesmått, percentiler och lådagram. Tidigare 2121 bankobjekt är oförändrade. Nivå 1 är ren avläsning, nivå 2 rutinmässig bearbetning och nivå 3 kritisk tolkning/modellbygge. #4.316 a är nivå 1 trots parentens nivå 2.

Variationen ska omfatta representation och tankeoperation, inte bara utbytta tal. Tabeller hålls lodräta enligt FP27. Varje delkort behåller egen tabell/figur och sammanhang. Delfaciten får inte avslöja andra delars svar. Behåll FP28–29 om ordning och stickprov; de nya uppgifterna ändrar inte standardavvikelsereglerna.

Skalorna måste kunna avläsas utan textkollisioner även på mobil. #4.308 behöver tillräcklig höjd mellan markeringarna. I #4.312 anges antalen inne i de staplade segmenten, eftersom exempelvis 24 annars inte går att avläsa exakt. Jämför andelar med varje klass eget antal; skillnad i procentenheter är inte relativ förändring i procent. #4.318:s brutna skala är avsiktlig och ska behållas som kritisk tolkningsuppgift, med korrekta avlästa värden.

Histogrammens hela minuter gör intervallen 0–4, 5–9 osv. entydiga. #4.321:s extremvärden 5 och 9 är uppnåeliga genom minsta/största heltalsvärde i varje intervall. Ta inte bort heltalsvillkoret utan att ompröva maxsvaret. Minsta/största medelvärde har namngivna ordnade fält enligt FP37. #4.315 avläser percentilen i en kumulativ kurva; inför inte en annan indexregel från en lista över enskilda observationer. #4.320 väger samman antal deltagare, inte ett oviktat medelvärde av två procentsatser.

Alternativfrågor ska säga ”Välj ett alternativ” så att Uppgiftslabbet tar med alternativen i lärarvy/export. En SVG-heuristik om vinkelbågar på cirkeldiagram är en INFO att granska; #4.313:s fyra sektorer är kontrollerade mot 25/40/20/15 procent och saknar ingen nödvändig vinkelmarkering. Skydd: `tools/ma2-statistik-diagram.test.js` och `tools/ma2-statistik-diagram.browser.py` testar självständiga beräkningar, faktisk SVG-geometri, verklig svarsinmatning, alternativ och mobil-/datorvyer i båda apparna. Ingen önskemålsstatus sparas genom Git-pushen.

## MA2S02 – flera läges- och spridningsmått från samma data (2026-10-13)

[30 nya uppgifter, alla deluppgifter, svar, nivåer och kontroller](MA2_STATISTIK_MATT_2026-10-13.md), även som JSON. #4.322–4.351 har alla tabell eller diagram och tre till fem delar. De ger 111 fristående kort och 141 svarsfält för Ma2a/b/c. Nio uppgifter har SVG-diagram och 21 har tabeller. Tidigare bankobjekt är oförändrade.

När medelvärdet behövs i standardavvikelsens beräkning kan båda måtten efterfrågas på samma delkort, i två namngivna ordnade fält. Då kan lösningen visa hela sambandet utan att hänvisa till en annan del. Andra mått får separata kort med fullständig tabell/figur. Två typvärden (#4.345/#4.347) använder däremot `svarsstruktur:"mängd"` på själva delen, så båda ordningarna godtas. Förväxla inte ett typvärde med dess frekvens eller tabellens största tal.

FP28–29 gäller fortsatt: beskrivande standardavvikelse för angivna värden använder σx; de uttryckliga stickproven #4.332/#4.335/#4.340/#4.343 använder Sx med n−1. Facit visar medelvärdet, kvadrerade avvikelser med frekvens, summan, nämnaren och kvadratroten. Fler standardberäkningar gör inte en uppgift till C. Fallet med bara lika värden (#4.344) får en kort begreppsförklaring på nivå 1: inga avvikelser, ingen spridning.

Rättningsmålen behåller full precision; två decimaler använder tolerans 0,005 och de exakta måtten tolerans 0. Alla nya tvådecimalsfall är kontrollerade mot båda grannhundradelarna. Binära representationseffekter får inte underkänna exempelvis 12,6 eller 0,6. Ingen generell tolerans ändras. #4.327:s procentfråga har uttryckligen en decimal och tolerans 0,05.

Kvartilfallen använder jämnt antal värden och medianerna i två lika stora halvor av den ordnade listan; lösningen visar hur. Förskjutning ändrar lägesmåtten men inte spridningen, fördubbling fördubblar standardavvikelsen och samma variationsbredd innebär inte samma standardavvikelse. Frekvenstabeller ska viktas med antalet observationer, inte med antalet rader. Skydd: `tools/ma2-statistik-matt.test.js`, data i `tools/fixtures/ma2-statistik-matt.json` och `tools/ma2-statistik-matt.browser.py`. Alla kort provas med riktiga rätta/felaktiga svar, omkastade fält och mobil-/datorvisning. Ingen rapportstatus eller kommentar sparas genom Git-pushen.

## MA2S03 – varierade kvartiler, percentiler och statistiskt resonemang (2026-10-13)

[Alla 35 granskade uppgifter, ändringar, nivåer och kommentarsförslag](MA2_STATISTIK_REFERENSER_2026-10-13.md), även som JSON. #4.352–4.375 är nya. #4.40/#4.48/#4.63/#4.71/#4.78/#4.92/#4.98/#4.171/#4.183/#4.202/#4.208 är varierade; gamla facit var inte generellt felräknade. Nio egna SVG-figurer, 60 spelbara kort och en manuell rituppgift ingår. Samtliga huvuduppgifter har tabell eller figur.

Nivå 1 ska vara enkel avläsning eller en direkt grundoperation. Sex analoga flerstegsrutiner #4.48/#4.63/#4.71/#4.92/#4.171/#4.183 höjs till nivå 2. Skapa variation med olika representationer och tankeoperationer: omvänd fråga, undre/övre svans, central andel, saknat värde, jämförelse, konstruktion och begränsningar i underlaget. Återinför inte identiska definitioner och procentmallar med enbart andra tal.

Percentilgränser ger ungefärliga andelar/antal, särskilt när observationer kan vara lika. #4.358:s ytterstreck är P10/P90, inte min/max. #4.363 skyddar mot obefogad linjär interpolation av andelar inom ett kvartilintervall. Vanliga lådagram bestämmer inte medelvärdet, men #4.360 gör det med fem observationer och uttrycklig kvartilkonvention. #4.361/#4.362 utelämnar mittvärdet vid udda antal. #4.362:s svar 4 och 5 är en oordnad mängd och båda ordningarna måste fungera.

#4.365/#4.366 anger intervallmittpunkter som modell för histogram. Medelvärde och standardavvikelse är uppskattningar: fullprecisionsmål och en decimal med tolerans 0,05. Värden inne i varje intervall är okända. Följ fortsatt FP28–29 om beskrivande σx respektive skattande Sx; mätningar i sig kräver inte n−1. Frekvensviktade summor ska framgå och medianer kan förklaras via kumulativa antal utan långa upprepade listor.

#4.359 kräver en ritad figur och ska därför förbli `spel:false`/manuell i Uppgiftslabbet tills ett riktigt ritverktyg kan bedöma svaret. Ingen osynlig deluppgift får behövas för de övriga korten. Flervalsfrågor måste få med alternativen även i lärarvy/export. #4.374 har tre rätta alternativ; delvis rätt och extra felval provas via verkliga alternativknappar.

Skydd: `tools/ma2-statistik-referenser.test.js` gör oberoende beräkningar, uttömmande kontroller och SVG-geometrikontroller. `tools/ma2-statistik-referenser.browser.py` provar 263 svarskombinationer och 190 mobil-/datorvyer, med Supabase/XP-skrivning blockerad. Data finns i `tools/fixtures/ma2-statistik-referenser.json`. Ingen rapportstatus eller elevkommentar sparas genom Git-pushen.

## FP41 – avrundningsledningar hör inte hemma i frågetexten (2026-10-13)

[Granskade ID:n, åtgärder och kommentarsförslag](MA1_AVRUNDNINGSLEDNINGAR_2026-10-13.md), även som JSON. Användarrapport Ma1 #0.189: behåll ”Avrunda 2,675 till två decimaler”, ta bort påminnelsen om hur femman avrundas. Samma redaktionella ändring görs i #0.193/#0.566/#0.587/#0.592. Bara `t` ändras; facit, separat ledtråd, nivå, svar och rättningsmetadata bevaras. #0.189 är fortsatt nivå 1 och har svaret 2,68.

Vanlig skolavrundning av positiva tal används fortsatt, även vid intervallgränser. Återinför inte regelpåminnelser i frågorna; förklaringar finns i facit. Efterfrågad precision ska stå kvar. #0.186/#0.203/#7.500 är granskade utan fel: avrundningsmetoderna finns där som innehåll att bedöma, inte som extra hjälptext. Ta inte bort deras alternativ. Ändra inte heller givna situationsvillkor om uppåt-/nedåtavrundning.

Kontroll: endast de fem `t`-fälten skiljer sig från föreversionen; 29 befintliga regressionstester, 12 verkliga svarsinmatningar och 24 elev-/lärarvyer passerar. Exakta decimalberäkningar verifierar 2,675→2,68 och manuella intervallfacit. Dubbelavrundningen i #0.592 kontrolleras också på 10 000 decimalvärden, utöver gränsargumentet. Ingen generell tolerans ändras och inga rapportstatusar sparas i appen.

## KG01 – fristående önskemål och allmänna appproblem (2026-10-13)

[Genomförande, tester, aktivering och kommentarsförslag](KUNSKAPSGYMMET_ONSKEMAL_2026-10-13.md). Funktionsönskemål inkom via matf1 #1.622; det är ingen matematisk felrapport. ”Skicka in önskemål” finns i Kunskapsgymmets kontomeny utan krav på aktuell uppgift. Alla inloggade användare kan skicka, även elever och vanliga lärare. Admin får en separat lista med status, valfri inlinekommentar, filtrering och kopierbar logg. Användaren kan läsa sina egna inskick och återkoppling.

Databasen använder `kg_private.onskemal` och serverbehöriga RPC:er. Behåll avgränsningen: endast admin får läsa/granska hela listan, användare får endast egna rader. Kontobyte rensar listor, utkast och modalvyer. Behåll dubblettskydd vid nätverksförsök och fungerande tom kommentar. Inga inskick ska kopplas till ett godtyckligt uppgifts-ID eller ge XP/felrapportsbonus. Visa bekräftelse bara efter ett lyckat serversvar.

Aktivering kräver `kunskapsgymmet/sql/2026-10-13-onskemal.sql` i Supabase. SQL är lokalt testad men inte körd i produktion av agenten. Skydd: konsumentens `tools/onskemal.test.js`, `tools/onskemal.integration.js` och `tools/onskemal.browser.py`. Ingen bankändring, rapportstatus eller elevkommentar har sparats genom arbetet.

## FP42 – begripliga bevisbegrepp, konstanta lösningar och mängdskiljetecken (2026-10-13)

[Fem rapporter, alla 27 granskade uppgifter och kommentarsförslag](FELRAPPORTER_2026-10-13_2127.md), även som JSON. Matf1 #4.326 frågar nu efter en konstant lösning; ytterligare sju frågor förtydligas. Matf1 #2.305/#2.541 använder indirekt bevis och facit förklarar kontraposition; fem analoga bevisfrågor följs upp. Kontraposition är en variant av indirekt bevis och ska inte felaktigt likställas med samma metod som motsägelsebevis. #2.305 hör till indirekta bevis, inte induktionsbevis. Matematiska slutsvar är oförändrade.

Fy1 #4.64:s a/b/c är självständiga fjäderfrågor utan en onödig hänvisning till tre andra fjädrar; egna förklaringar och enheter följer med. c ger 28/350=0,08 m och har nivå 1 som direkt beräkning. Bevara tidigare FP34: inga allmänna fysikkonstanter eller färdiga formelledningar återinförs i frågan.

Matf1 #1.478 och fem andra mängdfrågor får tolerant hantering av ett avslutande komma/semikolon i explicit mängdformat, t.ex. {3,4}, eller 3,4,. Rätt element krävs fortfarande; saknade/extra element avvisas. Avgränsa ändringen till mängd-/lösningsmängdsformatet och ändra inte generellt tal, koordinater eller numeriska toleranser. {3,4,} godtogs redan. Tre för långa mobilformler i #4.123/#2.144/#2.148 delas med alla mellanled kvar.

Skydd: master `tools/felrapporter-2026-10-13-2127.test.js` och konsument `tools/felrapporter-2026-10-13-2127.browser.py`; 30 riktade mastertester, 150 konsumenttester, 125 svarskombinationer och 128 vyer. Ingen rapportstatus eller elevkommentar har sparats genom Git-pushen.

## FYEL01 – varierad fördjupning om laddning och elektriska kretsar (2026-10-13)

[Alla tolv uppgifter, nivåmotiveringar, svar och kontroller](FYSIK1_ELEKTRICITET_FORDJUPNING_2026-10-13.md), även som JSON. #8.518–8.529 har egna SVG-figurer och är fristående kort. Fem är nivå 3, sex nivå 4 och en nivå 5. Ingen tidigare bankuppgift ändras i denna konstruktionsomgång. Miniräknare är alltid tillåten. Förmågor bedöms per uppgift, inte som samma generiska lista.

Användarens figurprincip är införd i båda CLAUDE.md: vid nya/omarbetade uppgifter ska man alltid sträva efter en figur om möjligt och kontrollera beteckningar, längder, vinklar, pilar, enheter och faktisk mobilvisning. Figurer ska följa med de kort som behöver dem.

Bevara fysikmodellerna: #8.519 har endast en fysisk nollkraftspunkt till vänster om den mindre laddningen; den algebraiska punkten mellan motsatta laddningar är ogiltig. #8.520:s två positiva kraftkomponenter följer rätt attraktion/repulsion. #8.521 skiljer på ordningen i jordningsförlopp; #8.522 skiljer på inducerad fördelning och bevarad nettoladdning efter isolering. #8.524 har konstant källspänning i båda brytarlägen. #8.525 skiljer ems från polspänning. #8.526:s givna voltmeterresistans måste räknas med. #8.527 är omvänd dimensionering från minsta värmareffekt och har två ledningsresistanser. #8.528 kräver sitt uttryckliga villkor om konstant lampresistans. #8.529 använder nollström och lika mittpunktspotential, inte en färdig bryggformel i frågan.

FP30 gäller #8.523:s exakta halvsteg: 9/16=0,5625 avrundas till 0,563. Rättningscentrum 0,563 och tolerans 0,0005 godtar fullvärdet men avvisar 0,562. Återställ inte ett symmetriskt fullprecisionscentrum i detta fall. FP34 gäller fortsatt: inga standardkonstanter/färdiga formler återinförs i frågorna. Skydd: master `tools/fysik1-elektricitet-fordjupning.test.js`, beräkningsdata i `tools/fixtures/fysik1-elektricitet-fordjupning.json` och `tools/fysik1-elektricitet-fordjupning.browser.py`. Ingen rapportstatus eller kommentar har sparats genom Git-pushen.

## FP43 – lösningsmängder, ∅ och varierad approximation (2026-10-14)

[Alla granskade ID:n, åtgärder, oförändrade uppgifter och kommentarer](FELRAPPORTER_2026-10-14_0756.md), även som JSON. Mato1 #1.451:s två rötter är en oordnad lösningsmängd; explicit `svarsstruktur:"mängd"` styr det. UI godtar hela numeriska lösningsmängden i ett fält eller ett tal per fält. Begränsa stöd till numeriska, enhetslösa mängder; ordnade koordinater och namngivna svar ska aldrig omtolkas. Samtliga rötter krävs och multiplicitet kontrolleras. ∅-knappen ska infoga i aktivt fält med bibehållet fokus/markering; tom mängd är inte samma sak som {0}.

Matf1 #1.20:s metodval får klickbara alternativ. Ange ”Välj ett alternativ” så att lärarvisning/export tar med alternativen. Facit ska nämna uttrycket, inte placeringen A, eftersom alternativen blandas. #1.21/24/25/26/27:s exakta antal skyddas med FP40:s `antal_satt`, tolerans 0. Generell numerisk mättolerans kunde felaktigt godta svar som var en enhet fel. Kombinationsval och fyra produktval i #1.21/25 är nivå 2.

#3.99:s 5,04 var rätt. Nya ID:n ensamt garanterar inte variation: #3.277/278/280/281 upprepade redan använda tal och funktioner. Dessa får andra förändringsriktningar, avtagande funktioner eller given tangent, och nivå 1 har nu givna värden. Sex nya #3.324–329 ger signal, temperatur, relativ areaökning, omvänd användning, kvadrattangent och en horisontell tangent med begränsad relativ noggrannhet. #3.26/116:s gamla klippta/schematiska figurer ersätts av matematiskt beräknade kurvor och tangenter. Bevara FP38:s balanserade urval. Snäva filter och avsiktlig felrepetition är inte samma fel som för tidig normal repetition.

Skydd: master `tools/felrapporter-2026-10-14.test.js`, konsument `tools/felrapporter-2026-10-14.browser.py`; tidigare FP38/40/42-tester kvarstår. Rapporterna #4.326, #2.305, #2.541, Fy1 #4.64 c och #1.478 är tidigare rättade och kontrollerade, inte nya facitändringar.

## FP44 – enhetlig Sx-standard efter extra kontroll (2026-10-14)

[Alla 207 granskade statistik-ID:n, de 42 anpassningarna och kommentarsförslag](STATISTIK_SX_2026-10-14.md), även som JSON. Användaren begär nu Sx genomgående i beräkningarna. Detta ersätter FP28–29 och MA2S02–03:s pedagogiska val av σx vid beskrivning av givna observationer. Det tidigare måttet var matematiskt korrekt men ska inte återinföras. Sx = √(kvadratsumma/(n−1)), med alla frekvenser som observationer. Givna normalfördelningsparametrar σ, summatecken och fysikens σ ändras inte.

42 Ma2-uppgifter anpassas i fråga, facit, delkort/ledtråd och relevanta maskinsvar/toleranser. 42 explicita datamodeller verifierar beräkningarna; tidigare korrekta Sx-uppgifter för temperatur, skruvar m.m. bevaras. #4.299:s simmarvärden blir Sx ≈ 0,25/0,71 s; Bea utan 32,0 s får ≈0,62 s och är fortfarande inte lika jämn som Alva. #4.344:s nollspridning förblir noll.

Ändra inte enbart nämnarsymbolen i specialproblem. #4.283:s två grupper har nu givna Sx-värden: deras inre kvadratsummor är 19·25 och 29·25. Lägg till skillnaderna från gemensamma medelvärdet 66: total kvadratsumma 2400, Sx = √(2400/49). #4.284:s oförändrade Sx kräver v = 50 ± √(72/7), cirka 46,79 och 53,21; de gamla 47/53 bevarar σx men inte Sx. Både exakta uttryck och angiven avrundning godtas.

Skydd: `tools/statistik-sx-2026-10-14.test.js`, `tools/fixtures/statistik-sx-2026-10-14.json` och konsument `tools/statistik-sx-2026-10-14.browser.py`. Befintliga stickprovs-, statistikmåtts-, referens- och 17:49-regressioner har nya oberoende Sx-mål; skydd för ordning, frekvenser, nollspridning, histogramuppskattningar och felavrundning behålls. Ett σx-värde kan avrundas till samma tal som Sx; avvisa det andra måttet när skillnaden faktiskt överstiger den angivna toleransen, inte när avrundade svar sammanfaller.

## FP45 – GeoGebra för statistik och verktyg per delkort (2026-10-14)

[Alla 45 berörda uppgifter, verktygsregler och licensbeslut](STATISTIK_GEOGEBRA_2026-10-14.md). Samtliga 42 datamodeller från FP44 samt #4.283/284/306 tillåter GeoGebra. Den inbyggda miniräknaren spärras för standardavvikelseberäkningar; övriga delar behåller sin tidigare miniräknare. `expandGameTask` ska beakta uttryckliga `geogebra`/`miniräknare` från varje del, även false. Ändra inte fysikens generella miniräknartillstånd.

Kunskapsgymmet visar en GeoGebra-länk till officiella Classic i ny flik, med noopener/noreferrer. Ingen app, kod, språkfil eller iframe bäddas in. Användaren bekräftade att tjänsten är kostnadsfri nu men överväger kommersiell uppskalning. GeoGebras officiella licens kräver särskilt avtal för kommersiell användning; extern länk är inte ett generellt undantag från deras användarvillkor vid framtida kommersiell användning. Aktivera inte en inbäddning utifrån enbart att webbplatsen är gratis.

Skydd: `tools/statistik-geogebra-2026-10-14.test.js`, dess fixture och konsument `tools/statistik-geogebra-2026-10-14.browser.py`. Facit, maskinsvar, toleranser och figurer är oförändrade från FP44. Hänvisningar till ”Sx på räknaren” uppdateras till GeoGebra.

## FP46 – verktyg efter uppgiftens syfte; GeoGebra ger alltid miniräknare (2026-10-14)

**Fullständig Ma1-runda 2026-10-15:** [3 968 huvuduppgifter och 954 delkort,
146 ändrade uppgifter](MA1_VERKTYG_2026-10-15.md); per-ID-beslut och
verktygstillstånd finns i motsvarande JSON. Vanlig insättning och n:te rötter
behöver normalt miniräknare men inte GeoGebra. Faktiska digitala
undersökningar måste däremot tillåtas. Blandade delar bedöms separat:
6.69 c ska fortsatt kontrolleras utan digitalt verktyg, medan a/b får båda.
Överslag som följs av ett efterfrågat faktiskt värde behöver räknare till
kontrollen; rena överslagsfrågor kan behålla spärren. Verktygsbedömningen
får ompröva en provförlagas delindelning: 0.1126 och 0.1130–1132 får räknare
enligt senaste policyn, med källa, frågor och svar bevarade. Skydd:
`tools/ma1-verktyg-2026-10-15.test.js` i båda repona och den uppdaterade
masterkontrollen `tools/ma1-prov-varianter.test.js`.

[Grundregler, bankinventering, alla granskade/åtgärdade ID:n och nästa granskningssteg](VERKTYGSPOLICY_2026-10-14.md), även som JSON. Senaste användarbeslutet ersätter FP45:s miniräknarspärr för statistik: GeoGebra tillåtet innebär alltid miniräknare tillåten. Fysikens generella miniräknartillstånd består. Sx-facit och den externa GeoGebra-knappen bevaras.

Alla uppgiftsanalyser, rättningar och konstruktioner ska kontrollera miniräknare och GeoGebra, också per delkort. Tillåt miniräknare för beräkningar som inte är snabb huvudräkning, inklusive stora produkter och numerisk trigonometri. Nekande ska motiveras av att verktyget tar bort det som prövas; huvudräkning och aritmetiska handalgoritmer är normalt inte målet. GeoGebra tillåts för digital grafundersökning, grafritning, statistik, regression och avancerade beräkningar där digitalt verktyg behövs. Läs hela frågan, inte bara nyckelordet: givna resultat från ett digitalt verktyg innebär inte att eleven själv behöver verktyget; ”utan digitalt verktyg” kan skydda metodförståelse.

Första rundan: metadata inventerade i alla 17 599 huvuduppgifter/sju banker. 63 uppgifter ändras: 45 statistikuppgifter får tillbaka miniräknare; 16 uttryckligen digitala undersökningar/integraler/regressions-/ekvationsberäkningar får GeoGebra; Ma2 #4.44/115 får miniräknare för procent × antal men behåller figuravläsning utan behov av GeoGebra. Åtta kandidater lämnas oförändrade efter verktygsbedömning. Mato1 #3.466 har olika metodvillkor i a/b och kvarstår för separat delbedömning. Ingen fullständig pedagogisk genomgång av hela banken påstås.

Skydd: validatorns ERROR `GEOGEBRA_REQUIRES_CALCULATOR` granskar parent och delkort med arv/explicit override. Konsumentens `raknareTillaten` tillåter alltid miniräknare med GeoGebra även med äldre cachemetadata. `tools/verktygspolicy-2026-10-14.test.js`, validatorregressionerna och konsumentens motsvarande test skyddar regeln; FP45:s tester har uppdaterats till det nya beslutet. Historiska granskningsloggar ska inte användas för att återinföra statistikspärren.

## KG02 – lärarstart, egna klasser och elevval (2026-10-14)

[Lärarflöde, behörigheter, datamodell, SQL-aktivering och verifiering](LARARKLASSER_2026-10-14.md). Lärarens startsida har **Skapa träningspass till eleverna** och **Mina klasser**. Undervisningsgrupper återanvänds som klasser, med klass-/elevstatistik och sökbar krysslista för elever på lärarens skola eller i egna grupper. Servern kontrollerar samma begränsning vid varje skrivning, inte bara i UI. Lärare får inte global adminstatistik.

Standardtillägg behåller andra undervisningsgrupper. En flytt måste ha en uttryckligt vald, behörig källklass, och alla valda elever måste finnas där. Validera hela mängden före första ändringen; behåll övriga grupper, träningshistorik och XP. Topplisteklass är en separat modell; befintlig trigger gäller nya gruppmedlemskap i kopplade klasser. Elevvalet informerar om detta. Val ska bevaras genom sökning och sparfel, och kontroller spärras under sparande.

Skydd: konsumentens `tools/larare-elevval.integration.js` (lokal PostgreSQL, rättigheter/atomisk flytt och verklig toppliste-trigger) och `tools/larare-elevval.browser.py` (roller, direkt start, klassskapande, statistik, val/flytt och mobil). `sql/2026-10-14-larare-elevval.sql` måste köras separat i Supabase; push aktiverar inte databasen.

## KG03 – undervisningsgrupper, klassimport och återkommande elevklassval (2026-10-14)

[Åtgärder, klassimportens omfattning, SQL och verifiering](GRUPPER_KLASSIMPORT_2026-10-14.md). Ersätter KG02:s benämning **Mina klasser** med **Mina grupper**. Klass och undervisningsgrupp är skilda: samma elev kan ha olika ämnesgrupper/lärare. Klassimport markerar nya, behöriga elever från en eller flera valda klasser och behåller övriga grupper; inget sparas före lärarens knapptryck. Klassalternativ byggs från den behöriga elevlistan, inte globala elevuppgifter.

Befintliga gruppmedlemmar ska vara ibockade, utan texten ”Redan i gruppen”. Befintliga kryss är låsta i tilläggsvyn; bara nya elever räknas/skickas. Klassimport återställer flyttläget så att en tidigare vald källa inte oavsiktligt används. Okopplade grupper bevarar elevens klass; en tidigare uttrycklig grupp–topplistekoppling har kvar sin dokumenterade trigger och ska inte skapas automatiskt.

Elever utan klass får den obligatoriska klassrutan vid varje inloggning/sidstart, oberoende av nyhetsflaggor. Verifiera rollen, undanta lärare/admin och bind väntande uppmaning till inloggat användar-ID. Klassvalet ska inte visa lärarklassen. Konsumentens klassintegration-/webbläsartester skyddar detta. Aktivera med `sql/2026-10-14-grupper-klassimport.sql`, även när föregående elevval-SQL har körts. Ingen ny SQL behövs för den befintliga klassvalsmodellens inloggningsruta.

## KG04 – separat undervisning/egen träning och samlad gruppvy (2026-10-14)

[Godkänd design, implementation, SQL och tester](LARARFLÖDE_IMPLEMENTATION_2026-10-14.md). Lärarens standardstart är **Min undervisning**; **Träna själv** öppnar ordinarie träning. Läget är kontobundet och återställs med historiken. Första besökets knappar ska vara **Skapa min första grupp** och **Träna själv**, utan den borttagna hjälpsentensen om att växla högst upp. Återinför inte KG02:s dubbla lärar- och träningsstart.

Gruppen samlar översikt, pass, elever, områdesstatistik och hopfällda inställningar. Kurs sparas via `sql/2026-10-14-gruppkurs.sql` och förväljs för pass/statistik; gammal SQL erbjuder bara namn tills kursstöd finns. Behåll tidigare grupp/klassmodeller och behörigheter; gör ingen massflytt av medlemskap. Pass dedupliceras på ID, skapande spärrar dubbelklick, sena svar får inte skriva över ett annat konto/formulär. Elev utan pass går direkt till egen kursväljare. Gruppöversiktens veckoaktivitet gäller alla kurser och måste vara tydligt märkt.

Skydd: konsumentens `tools/gruppkurs.integration.js`, `tools/larare-arbetsflode.browser.py` och uppdaterade `tools/larare-elevval.browser.py`, samt befintligt klassimporttest. Prototyp och produktionskod är olika saker: prototypens exempelsiffror får aldrig användas i den riktiga vyn. Pushmedgivande lämnades efter användarens prototypgranskning.

## KG05 – Dagens uppdrag som kompakt utfällbar rad (2026-10-14)

Användaren vill minska plottrighet och godkände en kompakt rad med pergamentikon, **Dagens uppdrag**, verkligt antal klara uppdrag och pil. Den tidigare stora, alltid synliga pergamentrullen ersätts i konsumentens `index.html` av native `details/summary`, hopfälld som standard. Innehållet rullas ut på klick och visar samma uppdrag, framsteg, XP och startknappar. Använd inte ett hårdkodat totalt antal; det kommer från dagens uppdragslista. Den lilla tränarvyns uppdragsindikator går också att klicka för att öppna hela uppdragslistan.

Visningsval sparas lokalt per konto (gäst separat) och används även vid kursbyte/omritning. Det ligger utanför träningsprofilen och får inte påverka XP, uppdragsräknare, synk eller SQL. Spara med det renderade kortets ägare så att ett sent toggle-event från en gammal vy inte ändrar nästa kontos val. Minnesreserv gäller om lokal lagring inte är tillgänglig. Respektera minskad rörelse och behåll tangentbordsåtkomst. Tränarens textbubbla får `max-width:100%` så att dess tillfälliga skrivanimationsbredd inte sticker ut när skärmen blir smalare.

Kontrollerat i riktiga appen med Chromium: 12 öppna/stängda lägen vid 320/390/1440 px i ljust/mörkt tema, höjd under 55 px hopfälld, mus/tangentbord, omritning, omladdning, kursbyte, korrekt räknare/startknapp, liten tränarvy, separata konton, minskad rörelse och oförändrad XP/uppdragsdata vid öppning/stängning. JavaScript-syntax och diffkontroll godkända. Engångsverifieringen ligger i molnmiljöns `/tmp/check-compact-quests.py`; inga nya bank-/belöningsregler eller testpaket införs för denna presentationsändring. Den tidigare versionens områdesverktygstips ger redan 328 px dokumentbredd vid 320 px fönster; jämförelsen verifierade att ändringen inte ökar den avvikelsen och att själva uppdragsraden/tränarkortet ryms.

## KG06 – pergament med egen scroll och veckobok; halv XP för äldre uppdrag (2026-10-14)

**Senare presentation samma dag:** Konsumentens `docs/UPPDRAGSBOK.md` beskriver
det aktuella lilla bokomslaget uppe till höger, dialogen och sidornas uppvikta
bläddringshörn. En räknare på omslaget visar dagens antal klara/antal uppdrag,
exempelvis 0/4. Den hämtar dagens verkliga lista för vald kurs, även om boken
visar en äldre dag. Kursgränsens `{tak:true}` får ingen falsk 0/4-indikator.
Ingen XP-, historik- eller SQL-regel ändras av räknaren. Kontrollerna i
`tools/uppdragsbok-vy.browser.js` omfattar nu riktig måluppdatering och båda
tränarkortens räknare.

[Implementation, slutligt XP-beslut, historikens gränser, SQL och verifiering](UPPDRAGSBOK_2026-10-14.md). Ersätter KG05:s stora utfällda höjd: öppning får inte öka tränarkortet. Pergament/rullar återinförs; dagbläddring visar senaste sju dagarna och äldre uppdrag kan slutföras. Skapa inte påhittad historik för tidigare osparade dagar.

Användarens senaste korrigering är **halva original-XP** för äldre uppdrag, inklusive hela-dagen-bonus: 25/50/50 XP, totalt 175 för en gammal fyrgrupp. Dagens 350 XP består. Historisk träning gäller vald dag/ägare/kurs och följer med återupptagning/fortsättning. Normalstart och noXp-repetition ska inte ge gamla bonusar. Kvitterade äldre uppdrag får inte betalas igen; gamla redan klara mål migreras som redan betalda.

Aktivera med konsumentens `sql/2026-10-14-uppdragsbok.sql`. Privat unik betalningsbok och serverns kontroll av kända, oförändrade uppdrag skyddar varje halvbelöning. Profilens revisions-/kredit-/bonusregler kvarstår. Inloggad klient väntar på `uppdragsbok:true` innan historisk träning tillåts, så nya XP inte skickas till äldre SQL. Lägg inte en generell extra XP-marginal i profilen eller topplistans spärr utan verifierade betalningar. Undvik tvetydiga SQL-variabelnamn (t.ex. `v_dag` mot kolumnen `dag`).

Skydd: konsumentens `tools/uppdragsbok.test.js`, `tools/uppdragsbok.integration.js` och `tools/uppdragsbok.browser.py`. Dessa ersätter inte tidigare passhistorik-, konto- eller adminskydd. Bankerna är oförändrade.

## FP47 – stora bokstäver i förenklade polynom och tydliga grupperingar (2026-10-14)

[Nio rapporter, följdgranskade ID:n och kommentarer](FELRAPPORTER_2026-10-14_1325.md).
Ma1 #1.09 a hade korrekt facit men dess särskilda `förenklat_polynom`-parser
avvisade `10X+3`. Den normaliserar nu bokstäver som övrig uttrycksrättning.
Detta gäller det avgränsade formatet, inte fysikens enheter eller allmän
symbolisk multiplikation. Kraven på samlade termer och förkortade bråk består:
`7X+5+3X-2`, `X+x` och `3X/9` ska fortfarande avvisas som ofärdiga svar.

De numeriska uttrycken #0.265/#0.266/#0.282 var matematiskt entydiga.
Explicit multiplikation och yttre hakparenteser gör dem lättare att läsa;
faciten visar den inre beräkningen först. Ändra inte värdena på grund av
typografiska synpunkter. Koordinatfält i ma2 #3.134/#3.341 får tydliga x/y-
etiketter och ordnad struktur. Mato2 #1.611:s ledtråd ska täcka alla tre
egenskaper, inte bara amplituden.

Skydd: master `tools/felrapporter-2026-10-14-1325.test.js`; konsument
`tools/brakuttryck.test.js` och `tools/felrapporter-2026-10-14-1325.browser.js`.
Matf1 #1.680 a har rätt facit 25/81; mato1 #2.250 har korrekt derivata och
testade ekvivalenta skrivsätt. Historiska underkännanden kan inte förklaras
säkert utan elevens faktiska inmatning. Lagra dem inte som bevisade facitfel.


## ST02 – lektionsområden och historiska uppdragskort (2026-10-14)

[Beslut och verifiering](LEKTIONSOMRADEN_MA2_2026-10-14.md). Ma2:s breda
GRUPPMA2-samlingskort är historiska; nya kort följer befintliga OMR-moment.
Konjugatregeln och kvadreringsreglerna är ett gemensamt område. I 2a samlas
andragradsfördjupning med tillämpningarna. ST01:s geometriavgränsning bevaras.
Gamla g:-nycklar måste fungera för sparade dagsuppdrag och arkiverade uppdrag
utan att återkomma i nya rekommendationer. Ändra inte OMR eller familjer för
en ren visningsuppdelning. Uppgiftslabbet ska behålla ordningen och filtrera
historiska/spårbegränsade grupper. Tester: lektionsomraden.test.js i båda
repona och lektionsomraden.browser.js i Kunskapsgymmet.

## FP48 – flerdelsformulering på fristående kort och avslöjande grafände (2026-10-14)

[Rapporter och jämförelser](FELRAPPORTER_2026-10-14_1634.md). Fy1 3.192,
3.197 och 3.386 visar hur pluralinledning, ”vart och ett av slutvärdena”
och byte från partikel till bil följer med trots att kortets siffror är
kompletta. Granska också referensord och vilket föremål en mening avser.
Fy1 3.143:s a–t-graf ska fortsätta streckad förbi 13 s; grafens slutpunkt
ska inte sammanfalla med det efterfrågade stoppet. Stopptiden beräknas från
arean, inte från accelerationens grafände. Tidigare numeriska rättningar
bevaras. Regression: tools/felrapporter-2026-10-14-1634.test.js i master och
motsvarande browser.js i Kunskapsgymmet.

## FP49 – modellbygge på delkort och rutinuppgifter felmärkta A (2026-10-14)

[Nivåbeslut och jämförelser](NIVAKALIBRERING_2026-10-14_1645.md), även som JSON.
Fy1 4.536 b och 4.533 är nivå 3 när retardationen ska härledas innan ett okänt
friktionstal bestäms. 4.669 b är nivå 4: tre krafter på B, rätt accelerationstecken;
att a-kortet är enklare ska inte styra b:s nivå. Givna mellanresultat ska fortfarande
vägas in. Ma2 3.487/488/489/491/492/497/498 har inte A-krav: poäng och E/C/A måste
ändras tillsammans med träningsnivån. Gör inte en rutinuppgift till A enbart
för att den har flera beräkningssteg. Ma2 3.531:s mått står vid AC i figuren.
Test: tools/nivakalibrering-2026-10-14-1645.browser.js i Kunskapsgymmet.

## KG07 – π och exakta uttryck utan algebrabibliotek (2026-10-14)

[Reproduktion, rättning och sex granskade uppgifter](FELRAPPORT_PI_2026-10-14_1905.md).
Mato2 #1.37 fick en textfallback när algebraisktLika avbröt vid saknat nerdamer.
Då godtogs pi/3 men inte π/3. Rena taluttryck ska normaliseras och jämföras
med den befintliga strikta talparsern även utan bibliotek; symboliska uttryck
behåller tidigare bibliotek/fallback. Ändra inte ett korrekt bankfacit för
att kringgå det. Testa själva π-knappen i rätt svarsfält och sätt biblioteket
uttryckligen undefined när frånvaro simuleras (delete kan misslyckas).
Tester: exakta-talsvar.test.js och pi-symbolrad-2026-10-14.browser.js i konsumenten.

## KG08 / FP50 – polär form, mobilinmatning och ordnade kvartilfält (2026-10-15)

[Rapporter, alla jämförelser och tester](FELRAPPORTER_2026-10-15_0945.md), även
som JSON med 16 ändrade bankposter. Mato2 4.117 b kräver stöd för både
trigonometrisk och Eulerform; det använda biblioteket gav fel tecken på
imaginärdelen vid en reproducerad negativ Eulerexponent. Formaten `polar` och
`polar_0_2pi` använder en avgränsad konstant komplexparser, oberoende av
biblioteket. Bevara positiva belopp och uttryckliga argumentintervall.
Mato2 4.09 c:s reella facit får inte ge numeriskt mobiltangentbord när ett
symboliskt svar begärs. Symbolraden ska finnas
även för manuella textområden. Ma2 4.296 b ska ha tydliga Q₁/Q₃-fält och
ritjämförelse först efter båda kvartilerna. Talet 8,5 i facit var korrekt.

Mato2 4.10:s cirkel måste vara ofylld även i spelIntro, vars SVG-attribut kan
ha annan ordning än i huvudtexten. Ändra semantiskt, inte bara genom en
ordningsberoende strängersättning. Små punktmarkörer behåller fyllning.
Fy1 3.298 visar båten som rektangel med pilarna fem respektive två rutor.
Tester: felrapporter-2026-10-15.test.js, polara-svar.test.js och motsvarande browserkontroll.


## FP51 – ofyllda cirkellinjer i samtliga banker (2026-10-15)

[Cirkelfigurer, inventering och exakt ändringslista](CIRKLAR_2026-10-15.md).
Följ upp KG08/FP50 även på enhetscirklar och liknande figurer. Ofylld
cirkellinje ska inte markera hela cirkelskivan. Äkta ytor får ha transparent
skuggning, medan små punktmarkörer, Venndiagram och fysiska föremål behåller
avsiktliga fyllningar. Kontrollera rekursivt huvudfråga, spelIntro, delkort
och facit, oberoende av SVG-attributens ordning. Tio ytterligare Mato2-poster
rättade; alla sju bankerna inventerade. Metadata, matematik och geometri
bevarade. Riktad SVG- och mobil/datorverifiering gav inga nya fynd.


## FP52 – lösningsgång försvinner på separata delkort (2026-10-15)

[Ma2 2.130 b och 80 jämförelser](MA2_LOSNINGSGANG_2026-10-15.md).
Ett fylligt huvudfacit garanterar inte ett pedagogiskt delkort: expandGameTask
väljer del.s före förälderns s. Ett explicit kortfacit med enbart rötter
ska kompletteras med metod och relevanta mellanled, inte bara få en
facit-stegvis-klass. Saknat del.s kan i stället visa hela huvudfacit och
avslöja andra delar (2.521). Varje kort ska ha sin egen fullständiga lösning.
Kontrollera s och samtliga spelDelar[i].s separat, inklusive faktisk
webbläsarvisning. 12 uppgifter rättade, 68 utan motsvarande brist;
matematiska svar och rättningsmetadata bevarade. 2.134 b:s missvisande
kommalista ersatt med entydiga separata rötter.


### FP52, fortsättning: andragradsfunktioner (2026-10-15)

[90 funktionsuppgifter granskade, 24 åtgärdade och 66 oförändrade](MA2_FUNKTIONSLOSNINGAR_2026-10-15.md).
27 saknade delkortsfacit ersatta med egna lösningar. Visa hur grafens
y-skärning bestämmer a (2.141 c/2.144/2.305), hur extremvärdet följer av
kvadraten och hur avläsning skiljer mellan x-koordinat, y-koordinat och
hela punkten. 2.238 ska bestämma tecknet på a innan punkten kallas minimum.
Bevara 2.146 b:s tidigare verifierade ekvationsformat och ordnade koordinater
i 2.141/2.146. Kontrollera formelns faktiska kanter på mobil; en klippt
KaTeX-bas behöver inte öka förälderns scrollWidth.


## ST03 – balanserade lektionsområden i Ma2c (2026-10-14)

[Beslut och verifiering](LEKTIONSOMRADEN_MA2C_2026-10-14.md). Användaren tyckte
att ST02 gav för många kort i 2c (57), att de gamla samlingskorten var för få
(22) och att en första version med 39 kort hade för få uppgifter per område.
Ma2c har nu 27 kort, ett per avsnitt i planeringen. Närliggande lektioner är
samlade, så de flesta kort har 55–130 träningskort och 4–8 delmoment.

Gruppernas inställningar:
- Nya grupper har `kurs:["2c"]`.
- `konjugat_kvadrering` gäller 2a/2b.
- 2c-gruppen `randvinkel_medelpunkt` är historisk.

ST01 i ny form: Randvinklar ligger med Yttervinkelsatsen, men aldrig i samma
kort som Kordasatsen. 2a/2b är oförändrade.

`hittaTraningskort()` måste hitta ensamma OMR-nycklar och grupper för andra
spår, så att äldre uppdrag fungerar. Ändra inte OMR eller familjer för
visningsgrupper.

Tester:
- lektionsomraden.test.js i båda repona,
- ma2c-geometri-omraden.test.js och lektionsomraden.browser.js i Kunskapsgymmet.

## FP53 – begärd uttrycksform, likhetstecken och namngivna delfält (2026-10-16)

[Alla 13 rapporter, 81 granskade uppgifter och kommentarsförslag](FELRAPPORTER_2026-10-16_0809.md),
även som JSON. 58 bankposter ändrade, 23 granskade utan motsvarande fel.

Ma2 2.241 ska uttryckligen begära **en enda logaritm**: ”förenkla” anger inte
varför 2lg3 skulle vara sämre än lg9. Formatet `en_logaritm` prövar både
ekvivalens och form, före generella numeriska genvägar. Bevara FP35:s
lg-/LaTeX-normalisering. I 2.572 och fem jämförelser används `faktoriserat`:
f(x)=, y= och enbart produkten godtas; utvecklat polynom ersätter inte den
begärda faktoriseringen. Rensa LaTeX-avgränsare **före** vänsterledet,
även när facit inte innehåller andra LaTeX-kommandon.

2.14 och fyra jämförelser får numeriska facit; = och ≈ får inte skilja
mellan rätt/fel på samma avrundade tal. Frågans precision styr toleransen.
3.202 a och andra koordinat-/storhetskort ska ha ordning och underetiketter
på delen själv, även när heluppgiften har a/b/c. Helvyn visar delens
fältetiketter. Neutrala ”Sidlängd”-fält passar oordnade sidlängder (2.73);
uttryckligt kortast→längst i 2.709 kräver däremot ordnad a-del.

Följ upp FP52 även när numerisk självrättning kompletteras med resonemang:
på ett fristående ordnat flersvarskort visar en ensam
`manuellKomplettering:true` hela kortfacit efter **första** rätta fältet.
Använd fältvis `[false, ..., true]` så att nästa tal inte avslöjas.
Verifierat i 3.412 c, 3.413 b, 3.515 b och 2.709 a.

Nivåbeslut: 2.32 är 5; 2.505 är 4. 2.620 c behålls på 5 men får given
linjeform och egen lösning. Omvandling av given standardavvikelse är
begreppsresonemang: 4.21/4.43/4.56 b är 4, enklare spridningsomvandlingar
är 3. Detta ändrar tidigare låg nivåbedömning, inte FP44:s korrekta
Sx-resultat. 2.484:s **reella** ska behållas. 4.107/4.226:s bokstäver
kopplas till kurvor med peklinjer, färg och linjetyp; deras tätheter har
samma totalarea. De tidigare korrekta svaren C respektive A bevaras.

Mät också `.katex-display .base` mot formelbehållaren: intern klippning
behöver inte öka sidans scrollWidth. 19 granskade lösningar fick kortare
rader efter en sådan reproduktion. Bevara den tidigare verifierade matematiken.

Tester: master `tools/felrapporter-2026-10-16.test.js`; konsument
`tools/felrapporter-2026-10-16.browser.py` (riktiga svarsfält och mobil/dator).

## FP54 – nästlade √-uttryck, exakt mobilsvar och rotmängder i Mato1 (2026-10-16)

[Rapporter kl. 19:19, 28 granskade ID:n och kommentarsförslag](FELRAPPORTER_2026-10-16_1919.md).
21 bankposter ändrade; ytterligare fyra rotuppgifter omfattas av parserfixen.
Tre jämförelser har inget motsvarande fel. JSON-loggen anger alla fält och verktyg.

Mato1 2.530:s två rötter ska vara en `mängd`, inte underförstått ordnade
`flera_delar`. Samma fel fanns i 2.531/2.416/2.576. Namngivna storheter
som x-värde/minimivärde i 2.826 behåller däremot ordning (FP53).
Tidsvariabeln måste stå i den självständiga frågan: minuter i 2.571/2.537,
timmar i 3.655, år i 2.321/3.656. 2.321 hade dessutom fel `rättSvar=6`:
ln(150/96)/0,08≈5,57859 ger **5,6 år** enligt frågans decimalprecision.

Ett numeriskt lagrat facit kan fortfarande tillåta ln2, √3 eller 11/3.
`sifferlage` ska därför få frågetexten, inte enbart facittypen. Exakt svar
kräver fullständigt mobiltangentbord. Bevara numerisk tolerans när både
exakt och avrundat svar tillåts. För tre decimaler används 0,0005 i de
granskade uppgifterna, så fel närliggande avrundning inte godtas. Enbart
exakt svar i 2.816 lagras däremot som ln2/ln3, inte avrundade rottal.

√x och √(x) fungerade redan i 2.212; det tidigare korrekta facit får inte
ändras därför att eleven skriver att roten ur generellt inte fungerar.
Den reproducerade bristen är √((x)): den gamla regexen tillät inga inre
parenteser. Normalisera √ framför en öppningsparentes till sqrt och låt
uttrycksparsern hantera den nästlade gruppen. Avvisa fortfarande ogiltig
syntax. Testa den **verkliga √-knappen**. Den rapporterade elevens exakta
historiska inmatning är okänd; ange denna begränsning i kommentaren.

Nivåer efter självständig analys: 2.530 C/3, 2.826 C/4; poäng uppdateras
tillsammans med nivå. 2.826/4.474 tillåter miniräknare eftersom frågan även
tillåter numeriska svar. Digital grafanalys i 2.321 kräver GeoGebra tillåtet.
De fem visuellt bekräftat klippta lösningarna får kortare rader, med
tidigare korrekt matematik och FP52:s förklaringar bevarade.

Tester: master `tools/felrapporter-2026-10-16-1919.test.js`; konsument
`tools/mato1-inmatning-2026-10-16.test.js` och
`tools/felrapporter-2026-10-16-1919.browser.py`.

## FP55 – uppgiftstrogna figurer, samtidig optimering och svarsprecision i Mato1 (2026-10-17)

[Rapporter kl. 19:17 och 71 manuellt granskade uppgifter](FELRAPPORTER_2026-10-17_1917.md).
62 bankposter ändras, med 47 omritade figurer. Av 27 rapporter ändras 26;
2.321 är redan rättad enligt FP54 och lämnas exakt oförändrad.

Återanvänd inte en generisk triangel eller tangentkurva till andra givna tal.
Konstruera figuren från sidlängder/vinklar respektive funktion och derivata.
Vinkeltext ska ligga inne vid rätt hörn; längder utanför rätt sida. Separera
figurens fyllningsopacitet från dess tydliga kontur. Studsbågar ska nå marken
mellan hoppen och följa den givna höjdkvoten. Kontrollera även färgen i den
riktiga appen: ärvd ljus currentColor på dess vita figuryta gör linjer osynliga.
De 47 nya figurerna har därför en egen mörk grundfärg.

4.257/4.260:s ursprungliga minimering är korrekt: alla olikheter gäller
samtidigt och origo bryter mot de positiva undre gränserna. Förtydliga
villkoren och skugga rätt område; ändra inte ≥ till > eller minimum till 0.
Minimivärdena är fortfarande 35,4 respektive 204. I 4.260 tillåts uttryckligen
bråkdelar av portioner, i enlighet med den ursprungliga kontinuerliga modellen.

2.317 hade däremot ett verkligt facitfel: frågan gäller x², men lösningen
använde x²+1. Tangenter genom (0, −4) ger a²=4 och tangentpunkterna
(−2, 4)/(2, 4). Digitalt ritande och tangentanalys i 2.316/2.317/2.318/2.349
ska tillåta GeoGebra och miniräknare. Generiska tidströskelledtrådar passar
inte parameterbeviset i 2.323.

En ensam svarsruta i 2.318 efterfrågar nu endast tangentekvationen, med
koefficienter till tre decimaler. 2.346 ska avrundas till 10,9; 10,8 är
avkortning och ska inte godkännas. Lagra fullprecisionsvärdet med tolerans
anpassad till den efterfrågade avrundningen, inte ett grovt mellanresultat.
Samma kontroll omfattar närliggande tids-, längd-, area- och vinkeluppgifter;
ange tidsenhet i den självständiga frågan och rätt enhet vid svarsfältet.

Fyra areaövningar får mellanvinklarna 50°/120°/40°/150° och 4.463 får 60°
för att minska upprepningen av 90°-fall. Fråga, figur, lösning, numeriskt mål,
miniräknare och nivå 2 samordnas; E-bedömning och poäng bevaras.
17 lösningar får kortare formelrader efter reproducerad intern KaTeX-klippning
på mobil, med matematik och pedagogiska förklaringar bevarade.

Tester: master `tools/felrapporter-2026-10-17.test.js`; konsument
`tools/felrapporter-2026-10-17.browser.cjs`. Webbläsaren provar riktiga
svarsfält och elev-/lärarvisning på mobil och dator, inklusive SVG-kontrast
och intern formelklippning. Tidigare FP53/FP54-regressioner ska fortsatt passera.

## FP56 – tre namngivna obekanta ska ha egna svarsfält (2026-10-18)

[Ma2 1.168 och 27 jämförelser](MA2_TRE_OBEKANTA_2026-10-18.md).
Tolv ekvationssystem hade ett uttrycksfält med facit som `(x,y,z)=(4,3,2)`.
Använd tre ordnade fält med etiketter x/y/z och exakt uttrycksrättning.
Eleven ska inte behöva gissa en sammansatt koordinatnotation. Facitens värden
är verifierade mot alla ekvationer och bevaras, även bråken i 1.65.
1.165/1.269 får också uttrycklig ordning för sina redan namngivna kategorier.
Nivå och verktygsval bevaras efter individuell kontroll.

Tester: master `tools/ma2-tre-obekanta-2026-10-18.test.js`; konsument
`tools/ma2-tre-obekanta-2026-10-18.browser.cjs` kontrollerar alla 14 kort
med korrekta och omkastade svar i riktig mobil-/datorvy (56 kontroller).

## FP57 – Mato1: fullständiga svar, definitionsvillkor och uppgiftstrogna figurer (2026-10-18)

[Mato1, första delomgången](MATO1_GRANSKNING_2026-10-18.md) ändrar 66 uppgifter.
Förkortning ger inte originaluttrycket ett värde i en förbjuden punkt (1.539).
När frågan begär både uttryck och definitionsvillkor ska båda få svarsfält
(1.43/48/53). En mängd förbjudna värden är oordnad även när huvudfältens
etiketter kräver ordning. Olikheter kräver hela lösningsmängden, inte en
trasig textrest (1.45). Kontinuitet behövs för slutsatsen att en värdemängd
fyller hela intervallet mellan minsta och största värdet (1.187).

Studsfigurer ska nå marken mellan varje båge och ha rätt höjdkvot.
En optimeringsfigur ska motsvara just frågans tillåtna område; en återanvänd
fyrhörning får inte illustrera en triangel eller en ren insättningsuppgift.
Öppna intervalls ändpunkter får inte behandlas som tillåtna extrempunkter.
Tids- och storhetsenheter måste finnas även när modellen ger ett rent tal.
Miniräknare tillåts när aritmetiken annars skymmer den avsedda metoden;
blandade delkort kan fortfarande ha skilda behörigheter (4.158 a/b).

Tester: `tools/mato1-granskning-2026-10-18.test.js` och konsumentens
`tools/mato1-granskning-2026-10-18.browser.cjs`. Hela banken är ännu inte
färdiggranskad; JSON-loggen skiljer lästa områden från ändrade uppgifter.

## FP58 – derivatafacit ska förklara regeln, inte bara återge svaret (2026-10-18)

[Mato1 derivata, delomgång 2](MATO1_DERIVATA_2026-10-18.md): 24 huvuduppgifter,
36 delkort med egna förklaringar. Ledtrådar om skalning av potensmodeller hör
inte hemma vid termvis derivering. Numeriska logaritmsvar kräver uttalad
precision, fullprecisionsmål och rätt tolerans. Avrundade mellanled får inte
skrivas som exakta likheter. En efterfrågad tolkning eller motivering måste
bedömas även om talet självrättas. Sekantpunkter måste ligga på den ritade
kurvan i samma koordinatsystem. 3.1079 varierar en exakt dubblett av 2.753.

Tester: `tools/mato1-derivata-2026-10-18.test.js` och konsumentens motsvarande
`.browser.cjs`. Tidigare korrekta svar och verktygsbeslut från FP54 bevaras.

## FP59 – enhet, precision och antal efterfrågade svar (2026-10-18)

[Fellogg 21:50](FELRAPPORTER_2026-10-18_2150.md): hastigheter behöver explicit
målenhet och precision. cm/min kan omvandlas till m/min; cm/s är något annat.
Exakta taluttryck och begärda närmevärden ska båda fungera. Två asymptoter
behöver två svarsfält även i fristående delkort. De Moivre-frågor anger
uttryckligen svarsform. Ma2 1.168 och 1.272 var redan korrekta i master.
Tester: `tools/felrapporter-2026-10-18-2150.test.js` och konsumentens browser-test.

## FP60 – grafavläsning ska bygga på elevens information (2026-10-18)

[Mato1 andraderivatan](MATO1_ANDRADERIVATA_2026-10-18.md): 37 uppgifter
granskade, 12 ändrade. Ett dolt funktionsuttryck får inte vara den enda
förklaringen till en grafavläsning. Ange konkreta intervall när frågan
efterfrågar dem, begränsa slutsatserna till synligt område och markera
avlästa gränser som ungefärliga. Ledtrådar ska stödja metoden utan att
avslöja antal eller färdig teckentabell. Dubbletten 3.241 varierar nu
resonemanget från maximum till minimum med positiv andraderivata.

Tester: `tools/mato1-andraderivata-2026-10-18.test.js` och konsumentens
motsvarande `.browser.cjs`. Numeriska svar och verktygsbeslut bevarade.

## FP61 – villkor för primitiva funktioner ska vara matematiskt möjliga (2026-10-19)

[Mato1 primitiva med villkor](MATO1_PRIMITIVA_VILLKOR_2026-10-19.md):
49 uppgifter i området och två följdfynd granskade, 19 ändrade. En kubik
på hela reella axeln har inget globalt minimum; 3.313 måste ange lokalt
minimum. Bilens avstånd från en linje kräver känd färdriktning, inte
bara fart och initialt avstånd (3.898/3.1014/3.1100).

Begärt exakt svar ska inte rättas med tolerans för avrundade decimaler
(3.1147). Begärda två decimaler använder fullprecisionsmål med halv
hundradels tolerans (3.1011). Integration med givet funktionsvärde behåller
uttrycksrättning: en felaktig integrationskonstant får inte godtas.
3.944 varierar framåträkning med bestämning av startvolymen.

Tester: `tools/mato1-primitiva-villkor-2026-10-19.test.js` och konsumentens
motsvarande `.browser.cjs`. Tidigare korrekta uttryck och verktygsval bevaras.

## FP62 – primitivkontrollen får inte tappa exponentialuttryckets variabel (2026-10-19)

[Mato1 primitiva, del 1](MATO1_PRIMITIVA_DEL1_2026-10-19.md): 25 uppgifter
granskade, 13 ändrade. Sex delkort får lösningar utöver slutsvaret.
Potensregel-ledtrådar ska inte användas för exponentialfunktioner.

Nerdamers simplify efter expand kunde felaktigt göra en x-beroende
exponentialdifferens konstant. Använd expand utan denna förenkling i
primitiv/primitiva. 3.16 b ska avvisa 3e^(2x)+K och godta 3e^(2x)/2+K.
Fri konstant krävs fortfarande när alla primitiva funktioner efterfrågas.
Kontrollera flera baser, negativa exponenter och blandade uttryck.

Skydd: konsumentens `tools/mato1-primitiva-del1-2026-10-19.browser.cjs`.

## FP63 – kontrolluppgifter ska ge en konkret fråga i träningskortet (2026-10-19)

[Fellogg 08:07](FELRAPPORTER_2026-10-19_0807.md): Mato2 4.179 a/b visade
redan det vänsterled som svarsrutan väntade sig. Läraruppgiftens kontroll av
likheten bevaras; träningskortet frågar efter utveckling av högerledet.
Använd förenklat_polynom så att den ursprungliga produkten inte kan kopieras
som ett godkänt svar. Lösning och ledtråd ska förklara multiplikationen.

Matematikens symbolrad kompletteras med i och e (rapport 4.144 a).
Testa klick i aktiv svarsruta och båda rotfälten, inte bara knappens HTML.
Bankens korrekta rotpar och tidigare polär-/π-rättning bevaras.

Skydd: konsumentens `tools/felrapporter-2026-10-19-0807.browser.cjs`.

## FP64 – radianenheter, uttalad precision och uppgiftsspecifik grafanalys (2026-10-19)

[Fellogg 20:44, 23 granskade uppgifter och alla kommentarsförslag](FELRAPPORTER_2026-10-19_2044.md).
Mato2 1.166:s matematiska facit π/6 var korrekt och vanliga π-skrivsätt
fungerade. Det reproducerade felet gällde utskriven radianenhet. Använd
`svarEnhet:"rad"` på rätt fält; normalisera radian/radianer till rad med
den befintliga enhetsrättningen. Ta inte bort enhetssuffix globalt och
godta inte grader, längdenheter eller rad/s i en radianomvandling.
Fem analoger rättas. Elevens historiska exakta inmatning är fortfarande okänd.

2.187:s precision är redan rättad i FP59 och ska bevaras. Sex jämförelser
får uttalad precision, fullprecisionsmål och relevanta enheter. Ett grovt
avrundat maskinfacit får inte underkänna mer noggranna eller exakta svar.
2.188 b ska själv härleda radiens ökning innan areans ökning beräknas.
2.237 får kortare formelrader efter reproducerad mobilklippning, med FP59:s
matematik och svarskontrakt bevarade.

2.420/421 frågar om x-koordinaten, inte en otydlig ”x-skärning”. Lösningen
ska använda f(x)=0 och rätt ekvation, inte asymptoternas generiska mall.
Rita grafer från faktiska funktioner. 2.407/408 förklarar sina egna
gränsbeteenden; orelaterad polynomdivision ska inte återinföras.
2.420/421 är E/nivå 2, 2.182 C/nivå 3. GeoGebra innebär fortsatt räknare;
1.27:s enkla exakta delar och numeriska d-del har olika verktygsbehov.

Skydd: master `tools/felrapporter-2026-10-19-2044.test.js`; konsumentens
motsvarande `.browser.cjs` provar faktiska svarsfält, π-knapp, mobil/dator
och båda apparnas figur- och formelvisning.

## FP65 – deriveringen måste visas; ingen dold avrundningsprecision (2026-10-19)

[Mato2 derivatavärden](MATO2_DERIVATAVARDEN_2026-10-19.md): sex granskade och
rättade uppgifter 2.417–419 och 2.423–425. En metodfras är inte en lösning:
visa den konkreta derivatan och insättningen. Beräkna med frågans verkliga
indata, inte ett tänkt exakt värde nära dess decimal. Skriv exponenter med
LaTeX-klamrar. Tangentfrågor ska namnge variabeln och dess värde.

Användarbeslut: utan angiven precision godtas korrekt avrundade numeriska
svar på elevens valda precision. Räkna avrundningen, vidga inte bara en
relativ tolerans. Bevara enhetskontroll, exakta heltal, formkrav och uttalad
precision. CLAUDE.md anger regeln. Noll ersätter inte ett litet icke-nollvärde.
Skydd: `tools/mato2-derivatavarden-2026-10-19.test.js` samt konsumentens
motsvarande `.browser.cjs` med positiva och negativa rättningsfall.

## FP66 – fristående förändringskort och facits egna avrundningar (2026-10-19)

[Mato2 hastigheter](MATO2_HASTIGHETER_2026-10-19.md): 2.125, 2.184 och 2.212
rättade; fem analoger kontrollerade utan ytterligare fel. Testa alltid det
avrundade svar som lösningen själv visar (28,1 s mot 28,125 s). Ett rent
numeriskt värde får inte kräva uttrycksformat när frågan inte begär exakt svar.

När b-kortet redan får volymökningen ska det inte också ärva a-kortets radie
och radiehastighet. Använd delens egen t och en figur med rätt radie. Bedöm
nivån för den faktiskt visade frågan. Härled mellanled i delens eget facit.
Dela upp enhetsmetadata per del; dA/ds har enheten längd, ds/dt längd/tid.
Kontrollera att radiepilar verkligen når kanten och etiketter inte ligger på
pil/ellips. Skydd: tools/mato2-hastigheter-2026-10-19.test.js samt konsumentens
motsvarande browserkontroll.

## FP67 – minimipunkt är ordnad, skärningsrötter är en mängd (2026-10-19)

[Mato2 extremvärden](MATO2_EXTREMVARDEN_2026-10-19.md): fem ändrade och en
oförändrad. 2.266:s minimipunkt använder märkta x/y-fält och ordnad struktur;
2.265/266/268:s skärningsrötter tillåter valfri ordning. Säg x-koordinater när
bara x söks. Lagra fullprecisionsvärden, även vid numerisk rotlösning, och
kontrollera originalekvationen. En stationär punkt behöver ett teckenargument
för att vara minimum. Visa metod för numeriska skärningar, inte bara svaren.

2.571/582 erbjuder decimalsvar och måste därför tillåta räknare. C/nivå 3
ersätter överdriven A/nivå 4. Grafer i lösningarna förklarar skärningar utan
att avslöja andra delars svar i frågan. Skydd: tools/mato2-extremvarden-2026-10-19.test.js
samt motsvarande browserkontroll i konsumentrepot.

## FP68 – numeriska extrempunkter ska inte lämnas utan självrättning (2026-10-19)

[Mato2 asymptoter](MATO2_ASYMPTOTER_2026-10-19.md): sex förbättrade uppgifter.
2.264/267 använder märkta ordnade fält för maximi- och minimipunktens x/y.
Lagra oavrundade koordinater; testa rotuttryck, tre decimaler och omkastade
punkter. Asymptotfält kan fråga efter a och g(x) i x=a och y=g(x), så eleven
inte måste gissa ett särskilt ekvationsformat. Förklara varför punkten är
maximum/minimum med teckenbyte. Fristående b-facit ska visa sin egen
funktionsomskrivning. Skiss/resonemang i 2.14/103 förblir lärarbedömt.
Ledtrådar om polynomdivision passar inte ln x eller produktregeln.
Skydd: tools/mato2-asymptoter-2026-10-19.test.js och konsumentens browserkontroll.

## FP69 – variation, sannolikhetsavrundning och energienheter (2026-10-20)

[Fellogg 07:03](FELRAPPORTER_2026-10-20_0703.md): sju rapporter åtgärdade
samt fem energianaloger. Variera faktiskt funktion/intervall när separata
ID:n visar samma matematiska fråga. Synka huvudtext, delkort, figur och mål.
3.116 a ger nu 26π/3; 3.77 använder en avtagande parabeltäthet.
3.450/508 normaliserar nya funktioner på intervall med undre gräns 1.

Energi från kW och timmar kräver kWh även i svarEnhet. Lagra full precision,
inte facits avrundade visning. Fri korrekt avrundning enligt FP65 gäller
också sannolikhetsformatet, inklusive andel/procent. Fel närliggande
avrundning och fel dimension ska avvisas. 3.132 a godtar 0,71 och 71 %.
Ma2 2.88 b har egen räknarspärr för att begreppet i den givna
kvadratkompletterade formen ska prövas. Kontrollera det faktiska kortet.

Skydd: master `tools/felrapporter-2026-10-20-0703.test.js` och konsumentens
motsvarande `.browser.cjs`.

## FP70 – en integral per delkort och synligt exaktkrav (2026-10-20)

[Fellogg 09:44](FELRAPPORTER_2026-10-20_0944.md): Matf1 3.322/323 ska tala
om en integral på varje fristående kort, även när hela läraruppgiften har
flera. Kontrollera både spelIntro och delens egen t, som ersätter introt.
3.322:s uttryckliga exaktkrav samordnas med uttrycksrättning utan gammal
numerisk tolerans: 1/3 ska fungera, 0,3333 ska underkännas.

Mato2 3.220 hade korrekt facit och redan ett exaktkrav. Flytta den viktiga
instruktionen före den stora figuren och ange exakt uttryck med π.
Behåll det korrekta värdet 128π/15. Fri avrundning utan precisionskrav
ska inte ta bort ett uttryckligt exaktkrav. Ersätt orelaterad malltext med
konkreta radier, tvärsnittsarea och integrationssteg.

Skydd: konsumentens `tools/felrapporter-2026-10-20-0944.browser.cjs`.

## FP71 – avrundat maskinfacit och klippt figurtext (2026-10-20)

[Fellogg 12:48](FELRAPPORTER_2026-10-20_1248.md): Matf1 3.44 lagrade 15,1
med tolerans 0,01 och underkände därför 15,08. Lagra 4,8π i full precision;
bevara FP65:s jämförelse på elevens valda precision. Samma fel rättas i
3.20 och 3.45. Ange rätt storhetsenhet i svarEnhet, inte bara i facit.

3.79:s etikett vid x=237 gick utanför SVG:ns högra kant. Flytta texten,
inte bara viewBox, och mät textens faktiska bounding box i appen.
Förtydliga om frågan söker negativ förändringshastighet eller positivt
minskningsbelopp; facit och rättningsmål måste följa samma tolkning.

Skydd: `tools/felrapporter-2026-10-20-1248.test.js` och konsumentens
motsvarande `.browser.cjs`, inklusive reproduktion från föregående bank.

## FP72 – primtecknet ska vara ett upphöjt matematiskt tecken (2026-10-20)

[Fellogg 13:05](FELRAPPORTER_2026-10-20_1305.md): Matf1 3.277 och sju
analoger använder f^{\prime} respektive A^{\prime} i stället för f\prime
på baslinjen. Kontrollera renderad KaTeX, inte bara att LaTeX saknar syntaxfel.
Endast formateringen ändras; tidigare matematik, variation och behörigheter
bevaras. Skydd: konsumentens `tools/felrapporter-2026-10-20-1305.browser.cjs`
samt befintliga `tools/felrapporter-2026-10-14.test.js` i master.


## FP73 – fria konstanter, enhetskontrakt och verklig variation i Matf1 (2026-10-21)

[23 rapporter, alla beslut och jämförelser](FELRAPPORTER_2026-10-21_0910.md),
med ändrade ID:n/fält i motsvarande JSON. Matf1 4.04/4.53/4.27 och 21
analoger använder `diffekv_losning`: samma affina lösningsfamilj, inte samma
namn eller ordning på två fria konstanter. C/D, A/B och C₁/C₂ stöds. Kontrollera
hela spannet i båda riktningar och den partikulära lösningen symboliskt;
fel exponent, beroende konstanter och fel partikulärterm får inte godtas.
4.102 är villkorsbestämd och ska fortsatt ha uttrycksformat med
e^(−2x)(2cos3x+4sin3x/3), aldrig två fria konstanter.

`diffekvation` används för 4.160/4.72/4.76/4.78 och jämför ekvationernas
residualer upp till en konstant icke-noll faktor. Flyttade termer godtas;
variabla faktorer kan lägga till lösningar och ska inte godtas. Den generella
uttrycksrättningen ändras inte. 3.03 och sex analoga obestämda integraler
använder `primitiva` och kräver en fri integrationskonstant oberoende av namn.

Användarbeslut: 4.106 och 4.386 behålls som markerad fördjupning i
Uppgiftslabbet men har spel:false och nivå 5. Återaktivera dem inte genom
heuristisk nivå- eller svarstypsrensning. 3.275 ger den primitiva funktionen
och standardgränsvärdet; inga sådana förkunskaper krävs längre i smyg.
4.134/4.172:s delkort är singular; 3.284 frågar konkret efter tangentens c.
3.60 har explicit konvergensval och 4.46 säger ja/nej. Mängdklamrar finns i
symbolraden och Venn-etiketter ligger inne i cirklarna.

Svarsenheter förtydligade i Matf1 och Mato2:s förändringshastigheter.
Fullprecisionsmål plus FP64:s precisionsjämförelse används i berörda
Matf1-kort utan angivet avrundningskrav. Återinför inte avrundade facitmål
eller breda toleranser. Explicit precision/exakthet i andra kort kvarstår.

FP38:s urvalsprincip kompletteras: karensen är nu ett helt varv av det
aktuella urvalet (fortsatt tak 250), så att kort inte blir färska för tidigt
mellan två pass. Felsvarskö och balanserad repetition när området är uttömt
bevaras. Nya 3.330–339 och 4.569–576 ger 16 spelbara kort i vardera av de två
rapporterade områdena. 3.212/3.227:s uppgift/facit är oförändrade och korrekta.
3.277 är oförändrad efter FP72.

Skydd: master tools/felrapporter-2026-10-21-0910.test.js; konsument
tools/passvariation-2026-10-21.test.js och
tools/felrapporter-2026-10-21-0910.browser.cjs. Tidigare tester kvarstår.

## FP74 – verifiera versalrapporter före extra normalisering (2026-10-21)

[Ma1 1.902 och fem jämförelser](FELRAPPORTER_2026-10-21_1113.md): 6X+4 godtas
redan som 6x+4 i förenklat_polynom. Samma gäller 1.11/18/26/27/70.
Ändra inte facit eller parser utifrån en kommentar om stort X utan att
reproducera felet. Testa faktisk inmatning och bevara kravet på förenklad form.
Elevens historiska fullständiga inmatning är okänd. Sex granskade, inga
innehållsändringar. Skydd: konsumentens tools/felrapporter-2026-10-21-1113.browser.cjs.

## FP75 – fysikens svarsinstruktioner, mätarscheman och beständiga enheter

2026-10-21: Se `GRANSKNING_2026-10-21_1300.md` och fullständig före/efter-lista
`FYSIK_SVARSINSTRUKTIONER_2026-10-21.json`. Svarsinstruktioner ska stå i
parentes efter frågan, även på egna delkort. Bevara fysikens nödvändiga
förutsättningar. Kopplingsfrågorna fy1 8.382/8.383 har nu schemaalternativ
A–C. Återställ inte till enbart textalternativ. Matf1 3.303/3.308 behöver
explicit mörka färger och vit bakgrund för kontrast även i mörkt läge.
Enhet ska synas ovanför svarsfältet, inte enbart i en platshållare som
försvinner när eleven skriver. Fullprecision i maskinfacit ska hållas skild
från det avrundade elevfacit. Regression: `tools/felrapporter-2026-10-21-1300.test.js`
och konsumentens motsvarande browsertest.

## FP76 – variation i densitet utan fler likadana insättningsuppgifter

2026-10-21: `FYSIK1_DENSITET_2026-10-21.md` dokumenterar nya fy1 2.327–2.334
och jämförelsegranskning av 2.284/285/287/190/194. Skilj på materialets densitet,
hela föremålets medeldensitet och uppmätt densitet vid luftbubblor. Mätglasets
nivåökning räknar undanträngd volym; vågens massa kan inkludera behållaren.
Lägg inte till rena talvarianter när området redan har många rutinuppgifter.
Samband mellan massa, hålrum, kompression och mätfel ger mer varierad träning.
Skydd: `tools/fysik1-densitet-2026-10-21.test.js` och motsvarande browsertest.

I samma omgång rättades fullprecision/tolerans i fy1 2.176–2.179, 2.190
och 2.194. 2.190 reproducerade underkännande av ett korrekt oavrundat
beräkningsuttryck. Behåll fullvärdet i maskinfacit och frågans noggrannhet
i toleransen; huvudfacit ska inte använda avrundade mellanled som exakta.

## FP77 – positionsändring, total sträcka och total tid

2026-10-21: `FYSIK1_MEDELHASTIGHET_2026-10-21.md` dokumenterar nya fy1
2.335–2.342 samt granskning av 3.102/126/259/260/262. En position skild från
noll är inte en färdad sträcka. Medelhastighet använder förflyttning;
medelfart använder hela tillryggalagda sträckan. Pauser ingår i hela tiden.
I 2.338 begärs en decimal uttryckligen för att särskilja korrekt svar 1,6
från 2 m/s, vilket annars både är en tillåten grov avrundning och resultatet
av att glömma pausen. Behåll fri avrundning i frågor utan precisionskrav.
Mätnoggrannhet hoppas över i denna utbyggnad enligt användarens beslut.
Skydd: `tools/fysik1-medelhastighet-2026-10-21.test.js` och konsumentens
motsvarande browsertest.

## FP78 – accelerationens tecken, graflutning och ikappkörning

2026-10-21: Nya fy1 3.440–3.448, med kontroll av 3.190/191/194/270/279,
dokumenteras i `FYSIK1_ACCELERATION_2026-10-21.md`. Positiv acceleration kan
minska farten när hastigheten är negativ. Högre hastighet i ett v-t-diagram
innebär inte större lutning. Vid ikappkörning ska positioner jämföras;
hastighetslikhet räcker inte. Ange vald positiv riktning när tecken behövs.
Förklara skillnaden mellan acceleration och retardationens storlek utan att
likställa negativa svar med fel när frågan faktiskt gäller acceleration.
Skydd: `tools/fysik1-acceleration-2026-10-21.test.js` och konsumentens
motsvarande browsertest.

## FP79 – position, sträcka och tangent i läge–tid-diagram

2026-10-21: Nya fy1 3.449–3.454 dokumenteras i
`FYSIK1_ST_DIAGRAM_2026-10-21.md`. Skilj position från körd sträcka.
Position noll betyder inte stillastående och negativ position betyder inte
negativ hastighet. Summera delsträckornas positiva längder vid vändning.
Momentanhastighet avläses från tangentens lutning, inte sekanten från start.
Utritad tangent och tydliga rutnät gör uppgiften självständig i Kunskapsgymmet.
Skydd: `tools/fysik1-st-diagram-2026-10-21.test.js` och motsvarande browsertest.

## FP80 – arean under accelerationsgrafen är en hastighetsändring

2026-10-21: Nya fy1 3.455–3.460 dokumenteras i
`FYSIK1_AT_DIAGRAM_2026-10-21.md`. Lägg till starthastigheten när arean
under a-t-grafen har beräknats. Noll acceleration betyder konstant hastighet,
inte nödvändigtvis vila. Riktningsbyte sker när hastigheten passerar noll.
Vid sträckberäkning i flera intervall ska föregående sluthastighet bli nästa
starthastighet; visa även delsträckorna i lösningen. Testa teckenfel och
förväxling mellan acceleration, hastighetsändring och sträcka.
Skydd: `tools/fysik1-at-diagram-2026-10-21.test.js` och motsvarande browsertest.

## FP81 – vektorskillnad och kompenserad ström

2026-10-21: Nya fy1 3.461–3.464 dokumenteras i
`FYSIK1_VEKTORER_2026-10-21.md`. Hastighetsändring är skillnaden mellan
hastighetsvektorer, inte alltid skillnaden mellan farter. Vid relativ rörelse
ska referensen anges tydligt: golv, band respektive vatten. En båts fart
relativt vattnet är inte farten tvärs över ån när strömmen kompenseras.
Visa riktningar med tydliga pilar och låt komponentförhållanden stämma i figuren.
Skydd: `tools/fysik1-vektorer-2026-10-21.test.js` och motsvarande browsertest.

## FP82 – mäta med multimeter

2026-10-21: Det nya området `multimeter` i kap 8 och fy1 8.530–8.549
dokumenteras i `FYSIK1_MULTIMETER_2026-10-21.md`. Mätaren följer Mollic MS8201:
COM alltid, µA mA V Ω Hz högst 400 mA och 10A för större strömmar, med områdena
4000 µA, 400 mA och 10 A. När frågan ber om den noggrannaste mätningen är det
minsta område som räcker rätt, och ett större område som fungerar är fel.
Vredet får inte visa svaret i uttags- eller lägesfrågor.
Amperemetern kopplas i serie och voltmetern parallellt. Resistans mäts utan
spänningskälla.
Skydd: `tools/fysik1-multimeter-2026-10-21.test.js`.

## FP83 – figurer utan bredd blir för stora

2026-10-21: Användaren påpekade att flera äldre figurer, till exempel fy1 8.383,
var väldigt stora. Orsaken var inbäddade SVG utan width-attribut och utan
width/max-width i style. De fyller hela uppgiftens bredd, cirka 880 px på dator,
och tre scheman i samma uppgift blev mycket höga.

Åtgärden är deterministisk. Varje sådan SVG fick
`style="width:100%;max-width:<viewBox-bredd>px"`, och inget annat ändrades.
Det gällde 59 figurer i 52 uppgifter i fy1 (bland annat 8.382, 8.383, 2.321–2.342,
3.440–3.452, 9.7, 9.96 och 9.301), 1 i matf1 (3.308) och 14 i mato2
(2.14, 2.125, 2.184 och 2.264–2.268).

fy2 2.12 och 2.13 hade en uttrycklig storlek på 380×801 respektive 380×886 px. De
krymptes till 260 px bredd, med höjden i samma proportion, så att skalan
fortfarande är läsbar.

Breda diagram med avsiktlig maxbredd på 640–700 px och rimlig höjd lämnades orörda.
Nya figurer ska alltid ha en bredd eller maxbredd.
Skydd: `tools/svg-bredd-2026-10-21.test.js`.

### FP82, fortsättning: begrepp och sladdfärg (2026-10-21)

Området Mäta med multimeter (8.530–8.565) har gemensamma regler. Alla uppgifter
utgår från samma strömtyp, så DC/AC, likström, likspänning, växelström och
växelspänning används inte i elevinnehållet eller i multimeterfiguren.
Sladdfärg får inte avgöra rätt eller fel; beskriv uttagen. Den gamla 8.541 om
växelspänning är ersatt av en uppgift om att byta från strömmätning till
spänningsmätning. Skydd: sista testet i `tools/fysik1-multimeter-2026-10-21.test.js`.

## FP84 – synlig alternativordning, metodledningar och kraftmodeller

2026-10-21 17:41: se `FELRAPPORTER_2026-10-21_1741.md` och JSON-listan
med samtliga granskade, ändrade och oförändrade ID:n samt kommentarsförslag.

- Skilj råbankens ordning från elevens visade ordning. Kunskapsgymmets
  `altOrdna` blandar redan klickbara alternativ och `altLista` håller ordningen
  stabil under kortet. Uppgiftslabbet använder grundordningen i export.
  Variera även denna vid konstruktion. Rätt/fel och kommentarer måste följa
  hela alternativobjektet. Ändra aldrig A/B-beteckningar i en figur enbart
  genom att flytta bokstäver i facit. Fy1 8.559 har nu även 4000 µA som val.
- Figurer ska visa uppgiftens situation, inte ge bort metoden. Matf1
  1.137/1.40/1.73 visar bokstäverna utan upprepningsantal. 1.152 visar
  likvärdiga platser utan fixerad person. Förklaringen hör hemma i facit.
- En negativ laddning ger inte ensam en kraftriktning; fältets riktning behövs.
  Fy2 3.346 visar fält nedåt och räknar med elektrisk kraft uppåt minus tyngd.
  Återinför inte den gamla modellen med outtalat försumbar tyngdkraft.
- Kopiera inte "bortse från tyngdkraften på elektroner och protoner" till en
  svävande oljedroppe. Fy2 3.353/3.354 behöver droppens tyngd i kraftbalansen.
  Ett fristående kort med ett nytt avrundat mellanresultat måste räknas från
  just detta värde (FP13), eller ges fullständiga ursprungsdata som nu i
  3.354 b. En bred tolerans får inte dölja två olika fysikaliska mål.
- Vanliga tabellkonstanter verifieras med separata beräknade `svarTabell`,
  inte generell extra tolerans (FP34/FP64). Både fullprecisionssvar och
  rimliga avrundningar testas genom den faktiska konsumenten.
- Matf1 4.30/4.153 följer tidigare avgränsning i FP73: extra fördjupning,
  nivå 5 och `spel:false`. Markera även närliggande resonansuppgifter tydligt.
  Ämnesplanen omfattar enklare linjära differentialekvationer av första och
  andra ordningen; kalla inte hela området högskoleinnehåll. Fysikens
  kondensatorfråga 3.121 har korrekt facit; avsaknad av uttryckligt omnämnande
  i ämnesplanen räcker inte för att massradera tillämpningsuppgifter.

Skydd: master `tools/felrapporter-2026-10-21-1741.test.js`, tidigare
multimetertester och konsumentens motsvarande `.browser.cjs`.

### FP82/FP84, fortsättning: rimliga felkopplingar (2026-10-21 18:13)

Alla 36 multimeterkort granskade; se
`MULTIMETER_INKOPPLING_2026-10-21_1813.md` och JSON-listan. Nya beslut:

- Frågan om **hur** mätaren ska kopplas ska inte redan säga att kretsen måste
  brytas. Blanda serie/parallellt och rätt/fel komponent eller gren i alternativen.
  Låt även rätt uttag och rätt område förekomma med fel inkoppling, exempelvis
  i 8.548/8.564. Felalternativ får inte alltid ha flera uppenbara fel samtidigt.
- Hela strömmen kan mätas efter att grenarna gått ihop, inte bara före
  förgreningen. 8.553 visar detta. En mätning över en annan parallellgren kan
  ge samma spänning och får inte automatiskt märkas fel.
- Variera själva schemat: lampornas placering, gemensamt motstånd före grenar,
  antal grenar och mätpunkt på återledningen. Flytta med etiketter, alternativ
  och facit. Ingen etikett ska ligga på en ledning. 8.543 behåller sitt innehåll.
- 8.554 har fyra bilder (A/V i serie/parallellt), med Bild B fortsatt rätt.
  Bildbokstaven ska följa bilden även när knappordningen blandas.
- 8.542/8.550 är nu nivå 2 efter omarbetning; 8.539 sänks till 2 och 8.548
  till 3. Flera raka val är inte automatiskt nivå 4.
- 10 A kan fungera för mindre strömmar med sämre upplösning; undvik absoluta
  påståenden att det endast går över 400 mA. OL på 4000 µA ger bara en undre
  gräns. 8.540 anger därför även ström under 100 mA när 400 mA ska väljas.

Skydd: `tools/multimeter-inkoppling-2026-10-21.test.js`, uppdaterade
`tools/fysik1-multimeter-2026-10-21.test.js` och konsumentens motsvarande
browsertest (alla kort och varje felalternativ på mobil/dator).

### FP82/FP84, fortsättning: ”det spelar ingen roll” och likvärdiga mätpunkter (2026-10-21 18:36)

Se `MULTIMETER_VARIATION_2026-10-21_1836.md` och JSON-listan med samtliga
18 manuellt granskade/konstruerade ID:n, ändringar och kommentarsförslag.

- I 8.542/8.545/8.552/8.553 finns det preciserade felalternativet ”Det spelar
  ingen roll: bryt vid P, Q eller R.” P/Q/R mäter inte alla samma ström i dessa
  förgrenade kretsar. Beskriv vad punkterna mäter; påstå inte att två
  parallellgrenars strömmar alltid måste vara olika.
- Använd inte formuleringen som ett automatiskt felalternativ. I nya 8.566
  är P/Q/R likvärdiga i en seriekrets. I 8.568 ger de tre angivna
  spänningsparen samma mätning över parallellgrenarna. ”Vilka punkter som
  helst” vore ett annat och felaktigt påstående.
- Åtta nya kort 8.566–8.573: serie med motor, motorgren, likvärdiga
  spänningspar, tre seriemotstånd, totalström före/efter grenar, fyra
  bildalternativ, öppen motorgren och två samtidiga mätare. Varje kort har
  egen figur, självständig text, förklarande facit och alternativa kopplingar.
- 8.570: P och S mäter totalström. 8.572: med öppen motorgren mäter P och Q
  lampström medan R ger noll. Bedöm aktuell topologi och brytarläge.
- 8.571: Bild C är rätt spänningsmätning över R2. Rätt knapp måste följa
  bilden när alternativordningen blandas. 8.573 kräver både amperemeter i
  serie och voltmeter över rätt del av kretsen.

Skydd: det utökade `tools/multimeter-inkoppling-2026-10-21.test.js` och
konsumentens motsvarande browsertest (44 kort, 334 svarskontroller, 88 vyer).

## FP85 – medicinska bilder, pulsantal och motsatta tidskrav

2026-10-21: åtta nya fy1 9.436–9.443 i `medicinska_metoder`, se
`FYSIK1_MEDICINSKA_METODER_2026-10-21.md` med fullständig ID-lista och
kommentarsförslag. 13 → 21 huvuduppgifter, figurer 1 → 9.

Skilj yttre röntgenkälla från spårämne i kroppen; minskad detektorsignal från
kvarvarande andel; absorberad energi från dos per kilogram; registrerade
pulser från aktivitet. Bakgrund dras från samma mättid. En lämplig
halveringstid måste kunna uppfylla både tidigt och sent aktivitetskrav.
Pröva båda, som i 9.443. 9.438 anger dosbidrag i tumören utan att påstå att
annan vävnad slipper strålning. Pulsantalet i 9.441 är diskret och exakt
beräknat från de givna värdena (`antal_satt`). Nivå 1 innehåller raka
avläsningar och ett direkt samband; de två tidskraven i 9.443 är nivå 3.

Skydd: `tools/fysik1-medicinska-metoder-2026-10-21.test.js`, utökat äldre
partiklar/medicin-test och konsumentens `fysik1-kompletteringar-2026-10-21.browser.cjs medicin`.

## FP86 – neutral är inte samma sak som elementär eller sin egen antipartikel

2026-10-21: Standardmodellen 16 → 24 uppgifter, 0 → 8 figurer.
Se `FYSIK1_STANDARDMODELLEN_2026-10-21.md` och JSON för alla 16 granskade,
7 reviderade och 8 nya ID:n samt kommentarsförslag.

Neutronen är neutral men består av kvarkar; antineutronen är också neutral
men består av antikvarkar. Summera varje laddning, inklusive avgivna
leptoner vid betaomvandling. Beta-plus med proton till neutron ska gälla
proton i en kärna, inte fri proton. Atommodellers markeringar måste skilja
elektron, proton, kärna och hel atom. Räkna inte elektroner som kvarkar.

Standardladdningarna hos u/d och deras antikvarkar hör till formelsamling
och facit, inte till frågetext. Ekvationen i ett facit måste ändå förklaras:
ange vad termerna står för (9.329), inte bara algebra utan fysikalisk koppling.
Skydd: `fysik1-standardmodellen-2026-10-21.test.js`, partiklar/medicin-testet
och konsumentens kompletteringsprov med argument `standard`.

## FP87 – rutinvariation är mer än nya tal eller nya maskinnamn

2026-10-21: användaren ber att lämna återstående kärn-/partikeldelar och
komplettera andra rutinområden med variation. Effekt 110 → 116 uppgifter,
2 → 8 figurer. Nya 5.623–5.628, se fullständig ID-/kommentarslista i
`FYSIK1_RUTINVARIATION_EFFEKT_2026-10-21.md` och JSON.

Variera representation (diagram, tabell, energiflöde, instrumentavläsning),
frågans riktning (effekt/kraft/energi) och faktisk tankegång, inte bara siffror.
Enkla nivåer får fortfarande ha figur. Fler textkloner behövs inte bara för
att en familj har många uppgifter. I facit: visa kJ→J och min→h när det behövs,
varje tidsdel och skillnaden mellan två mätarställningar.

Pilspetsen i en SVG avgör riktningen, inte banans start-/slutordning.
Vid positiv effekt från en vinsch längs rörelsen ska kraft och fart peka
åt samma håll (5.627). Kontrollera visuellt och håll regression för spetsen.
Skydd: effektvariationstestet, utökat äldre effekttest och konsumentens
kompletteringsprov med argument `effekt`.

## FP87 – rutinvariation är mer än nya tal eller nya maskinnamn

2026-10-21: användaren ber att lämna återstående kärn-/partikeldelar och
komplettera andra rutinområden med variation. Effekt 110 → 116 uppgifter,
2 → 8 figurer. Nya 5.623–5.628, se fullständig ID-/kommentarslista i
`FYSIK1_RUTINVARIATION_EFFEKT_2026-10-21.md` och JSON.

Variera representation (diagram, tabell, energiflöde, instrumentavläsning),
frågans riktning (effekt/kraft/energi) och faktisk tankegång, inte bara siffror.
Enkla nivåer får fortfarande ha figur. Fler textkloner behövs inte bara för
att en familj har många uppgifter. I facit: visa kJ→J och min→h när det behövs,
varje tidsdel och skillnaden mellan två mätarställningar.

Pilspetsen i en SVG avgör riktningen, inte banans start-/slutordning.
Vid positiv effekt från en vinsch längs rörelsen ska kraft och fart peka
åt samma håll (5.627). Kontrollera visuellt och håll regression för spetsen.
Skydd: effektvariationstestet, utökat äldre effekttest och konsumentens
kompletteringsprov med argument `effekt`.


### FP87, komplettering – ström, tabellintervall och korta signaler

Sex nya 8.574–8.579: ström 31 → 37 uppgifter, 4 → 10 figurer.
Se `FYSIK1_RUTINVARIATION_STROM_2026-10-21.md`/JSON för alla nya,
alla sex granskade jämförelse-ID:n och färdiga kommentarsförslag.

För sammanlagd laddning ska ett valt intervall använda skillnader i både
laddning och tid (8.575). Vid korta signaler kräver medelström hela
periodens tid, även den strömlösa delen (8.578). Vid förgrening måste
pilar och beräkning ha samma in-/utströmmar. Diagram för konstant ström
ska särskilja rak Q-t-linje från böjda eller knäckta grafer (8.579).
Axlar och skala måste räcka för den avläsning som efterfrågas.
Skydd: strömvariationstestet och konsumentens kompletteringsprov `strom`.

## FP84 – påfyllnad i Ma2 inom ämnesplanen

2026-10-21: Ma2 1.675–1.683 (grafisk lösning) och 4.384–4.395 (standardavvikelse)
dokumenteras i `MA2_PAFYLLNAD_2026-10-21.md`.

Innan en uppgift läggs till ska innehållet stämmas av mot Gy25-ämnesplanens
centrala innehåll för nivån, och nya uppgifter ska bara läggas i befintliga
områden. Tabeller och diagram som eget innehåll finns inte på nivå 2, så det
området byggs inte ut.

Standardavvikelse:

- Räkna aldrig Sx för hand. Datauppgifter har GeoGebra påslaget, och lösningen
  hänvisar till Sx i statistikverktyget, aldrig till SD(), som ger σ.
- Teori- och diagramuppgifter får sakna GeoGebra.
- Välj data så att antal-inom-intervall-svar inte hamnar nära en intervallgräns.

Skydd: `tools/ma2-pafyllnad-2026-10-21.test.js`.

### FP84, fortsättning: ombyggda upprepningar (2026-10-21)

Ma2 4.14, 4.65, 4.102, 4.114, 4.173, 4.174, 4.195, 4.201, 4.211, 4.212,
4.213, 4.235 och 4.236 är ombyggda på plats, med bevarade ID:n, `kurs` och
`familjTidigare`. De gamla versionerna finns i
`MA2_SX_OMBYGGDA_GAMLA_VERSIONER_2026-10-21.json`.

Bygg inte tillbaka fler omvandlingsuppgifter av typen "alla värden ökas med a".
Det finns tillräckligt med representanter för den typen.

En flervalsfråga om att välja det värde som ger störst eller minst Sx måste ha
en tydlig marginal mellan alternativen. Kontrollera alla alternativ numeriskt.

## FP85 – tangensgrafer och deriverbarhet med figurer

2026-10-21: Ma4 2.605–2.612 (tan_kurvan) och Ma3c 3.1157–3.1164 (deriverbarhet)
dokumenteras i `MA3_MA4_FIGURER_2026-10-21.md`.

Tangensgrafer:

- Bryt kurvan vid asymptoterna, aldrig med en lodrät förbindelselinje, och streckmarkera asymptoterna.
- Gradetiketter på x-axeln.

Deriverbarhet:

- Hopp ritas med ofylld och ifylld ändpunkt.
- Pröva både värde och lutning i skarven.
- Kontinuitet räcker inte för deriverbarhet (|x|), och en lodrät tangent ger ingen derivata (∛x).

13 äldre uppgifter i området deriverbarhet handlar om extrempunkter. Flytta dem
inte utan användarens beslut, eftersom elevresultaten följer området.

Skydd: `tools/ma3-ma4-figurer-2026-10-21.test.js`.

## FP88 – golvimpulsens nivå och elektriska punkters verkliga anslutning

2026-10-21, rapport 21:14: se `FELRAPPORTER_FY1_2026-10-21_2114.md`/JSON
för alla 12 granskade ID:n, två åtgärdade uppgifter, tio jämförelser utan fel
och färdiga kommentarsförslag.

5.386a behåller den fullständiga modellen (normalkraft och tyngdkraft), men
flyttas uttryckligen enligt användarens beslut till träningsnivå 5. B stannar
på 2. Ändra inte den tidigare riktiga golvimpulsen 9,00 Ns till nettoimpulsen
8,76 Ns utan att uttryckligen ändra modellen. Fristående b använder sina egna
9,00 Ns och ger 450 N. Kraftskiss och mellanled förklarar skillnaden; figurens
riktningar respektive skalning måste framgå. Befintliga tyngdkraftsregressioner
ska bevaras. Träningsnivå är separat från E/C/A-poäng.

8.150:s C var en lös punkt i figuren. Ny sluten krets förbinder B med C genom
ett motstånd och C med batteriets minuspol. Rita inte en ideal sladd mellan
punkter med olika givna potentialer. Att välja A som ny nollnivå ändrar
referensen i hela kretsen, inte ström eller spänningar. Varje elkort ska ha
figuren och egna namngivna, ordnade svarsfält vid flera potentialer.
Skydd: riktat rapporttest, äldre rörelsemängds-/elektricitetstest, konsumentens
delkortstest och webbläsartest med rapportens tidsstämpel 2114.


## FP89 – värmeöverföring genom flera representationer

2026-10-21: nya 7.225–7.230 kompletterar familjen Värmeledning och strålning
från 6 till 12. Se `FYSIK1_VARIATION_VARMEOVERFORING_2026-10-21.md`/JSON
för nya/granskade ID:n och kommentarsförslag. Inga äldre bankobjekt ändras.

Variera experiment, strömmande vatten, tomrum, avkylningsdiagram, reflekterad
energi och lika temperatur vid olika massa. I temperaturjämförelser ska
**ändringarna**, inte sluttemperaturerna, jämföras. Lika temperatur betyder
inte lika inre energi. Vakuum hindrar inte värmestrålning. Visa materialens
faktiska placering: stavar får inte se ut att gå genom kärlväggen.
Giltiga vardagsord som "dubbelt" ska godtas via `multipel` när en faktor söks.
Skydd: värmeöverföringstestet, äldre värmetestet och konsumentens
`fysik1-kompletteringar-2026-10-21.browser.cjs varme`.


## FP90 – variation i tyngdkraft utan att blanda kraft och hastighet

2026-10-21: nya 4.758–4.763 ger 25 spelbara tyngdkraftsfrågor (tidigare 19),
27 huvuduppgifter totalt och sju med figur. Fullständiga ID-/kommentarslistor
finns i `FYSIK1_VARIATION_TYNGDKRAFT_2026-10-21.md`/JSON. Listan över områden
under 25 är uppdaterad; samma spelräknemetod måste användas där.

Variera kraftbilder, diagram, mätningar och jämförelser. Gör inte bara fler
texter med given massa/g. Standardkonstanter hör till formelsamlingen, men
nödvändiga experimentvärden på modellplaneter får finnas i diagram.

Kraftpilar och hastighetspilar måste skiljas åt i frågan. Noll hastighet
innebär inte noll tyngdkraft. Större tyngdkraft på en större massa innebär
inte automatiskt större fallacceleration. När pilar kvantitativt jämför
krafter ska längdförhållandet stämma (4.762: 3:1).
Skydd: tyngdkraftsvariationstestet, utökat kapitel 4-test och konsumentens
`fysik1-kompletteringar-2026-10-21.browser.cjs tyngd`.

## FP91 – importerade kopplingsblad: lös om facit och namnge komponenterna

2026-10-22: användarens två blad med enkla kopplingar ger 24 importerade
frågor och 16 varianter, **8.580–8.619**. Se
[FYSIK1_ENKLA_KOPPLINGAR_2026-10-22.md](FYSIK1_ENKLA_KOPPLINGAR_2026-10-22.md)
och motsvarande JSON för alla ID:n, källmappning, rättningar och
kommentarsförslag. Inga äldre bankobjekt ändras.

- Originalfacit är inte en verifierad beräkning: I 3b ger 30,0 W, I 5a
  ger 13,38 mW och II 6a ger 7,5 Ω när lampan har effekten 10 W.
  Bevara dessa omräknade svar; återinför inte 30,3 W, 1,33 mW eller 22,5 Ω.
- ”En av komponenterna” med känd effekt/spänning kan ge olika svar beroende
  på vilken komponent som avses. Här får komponenten ett tydligt namn och
  det andra fallet en egen fråga (8.604–8.607). Byt aldrig plats på U₁/U₂
  när den kända resistansen byter komponent.
- En serieresistor använder samma ström som lampan men **sin egen**
  spänning/effekt. En lampas märkeffekt gäller när den får märkspänningen.
  Visa den kopplingen i lösningen utan att ge färdiga formler i frågan.
- Voltmetergrenen ansluts över rätt komponent(er). Totalamperemetern ska
  ligga före förgreningen; ledningen måste avbrytas vid mätarsymbolen.
  Ingen genomgående ledning får kortsluta mätare, resistor eller batteri.
- Använd två namngivna, ordnade fält när två komponentstorheter efterfrågas.
  Pröva även omkastade svar. Bevara tillräcklig precision i mellanled och
  följ den avrundning som faktiskt står i slutet av frågan.

Skydd: master `tools/fysik1-enkla-kopplingar-2026-10-22.test.js` med
oberoende svarsberäkningar och ström-/effektbalans; konsumentens likadaterade
`.browser.cjs` prövar samtliga 40 kort och enheter på mobil/dator.

## FP92 – delkortens nivå, sammanhang och enhetsvisning

2026-10-22 12:24: `FELRAPPORTER_2026-10-22_1224.md` innehåller samtliga tio
rapportbeslut, följdgranskningar och färdiga kommentarer. Ma2 4.117 får
sammanhängande text; fy1 5.117, 5.97, 5.382 och 9.415 får tydligare frågor.
9.415 gäller fortfarande protoner, inte neutrala atomer i solens inre.
5.123a är nivå 4, 5.225a och 5.396 nivå 5; jämförelsen 5.395b nivå 4.
Detta är träningsnivåer, inte automatisk omräkning av E/C/A-poäng.
5.95a:s decimalregel togs bort särskilt efter rapporten i remote 6d9dcb3.
Kortet får två rekommenderade värdesiffror med den nya ±2-regeln.
Oavrundat facit 9427,2 J bevaras; 9,4·10³ J är rätt avrundning.

Enhetsförhandsvisningen ska skilja tal från enhetsbråk, skriva enhetsbokstäver
upprätt och visa multiplikation i kg·m/s. Algebra får inte bli enheter (1,5x).
Skydd: master `tools/felrapporter-2026-10-22.test.js`, befintliga fysiktester
och konsumentens `tools/felrapporter-2026-10-22.browser.cjs`.

## FP93 – värdesiffror med ±2, uttryckliga precisionskrav går före

Användarbeslut 2026-10-22, förtydligat i chatten: behåll äldre uttryckliga
decimal-/värdesifferkrav. Utan sådant krav rekommenderas minsta relevanta
mätprecision och korrekt avrundade svar med ±2 värdesiffror godtas, minst en.
Godta inte felavrundade värden genom att bara öka toleransen.

Granskad metadata `svarVardesiffror` och oavrundat maskinfacit krävs. Den nya
kontrollen ligger före den generella rättningen, även för enhetsalternativ
och separata delkort. Nya regeln får inte kringgås av en äldre bred tolerans.
Exakta antal, konstanter, figursiffror och andra delars uppgifter får inte
automatiskt styra precisionen. Skilj dessutom subtraktion av nära massor från
vanlig multiplikation av mätvärden. Heltalsnollor är tvetydiga; grundpotensform
och decimalnollor ger entydig precision.

Första införandet omfattar elva kort: fy1 2.2ab, 5.95a, 9.415ab samt fy2 1.2,
1.3ab, 1.4ab, 1.6. Övriga äldre fysikkort är **inte** färdigkalibrerade.
Alla beslut, ändrade mål och begränsningar finns i samma rapport som FP92.
Skydd: `tools/fysik-vardesiffror-2026-10-22.test.js` i Kunskapsgymmet,
masterrapportens test samt gemensamt browserprov. Äldre matematikrättning
och fysikkort med uttrycklig precision ska vara oförändrade.

Uppföljning 2026-10-22: se `FYSIK1_DENSITET_2026-10-22.md`. Fem äldre
avrundade maskinfacit rättas (2.18, 2.27, 2.274, 2.52, 2.54), med
bevarade uttryckliga precisionskrav. Ytterligare fem kort kalibreras för
±2: 2.26acd och 2.38ab. Skilj ren enhetsomvandling från mätberäkning.
Skydd: `tools/fysik1-densitet-2026-10-22.test.js` och konsumentens
likadaterade browserprov. Fyra jämförelseuppgifter lämnas oförändrade.

## Ma3-påfyllnad 2026-10-22 – grundbegrepp med flera representationer

Se `MA3_PAFYLLNAD_2026-10-22.md`: 1.862–1.873 och 2.1144–2.1149.
Skyddas av `tools/ma3-tangenter-2026-10-22.test.js`,
`tools/ma3-definition-2026-10-22.test.js`, `tools/ma3-polynom-2026-10-22.test.js`
och motsvarande browserprov i konsumenten.

- En tangent kan korsa kurvan: x³/4 har vågrät tangent i origo (1.865).
- Negativt h är tillåtet; h är en förändring, inte en x-koordinat.
- En differenskvot kan vara odefinierad vid h=0 men ha ett gränsvärde (2.1149).
- Ändligt många tabellvärden ger en uppskattning, inte ett bevis för derivatan.
- Gradtal bedöms efter förenkling; π är en tillåten polynomkoefficient.
- Konstanttermen är värdet vid x=0, även när den läses ur en tabell eller graf.
- Nya kort har miniräknare men behöver inte GeoGebra. Flera tankeled ligger
  på nivå 2 eller 3 även om slutberäkningen är enkel. De nya uppgifterna
  ersätter inga tidigare ID:n eller redaktionella beslut.

### Ma3-logaritmer: fortsättning 2026-10-22

Se `MA3_LOGARITMER_2026-10-22.md`, nya 2.1150–2.1157 och granskade
2.124, 2.129, 2.134, 2.413, 2.414, 2.816. I ln x=3 finns ingen exponentialterm
att först isolera; ledtråden ska koppla ln till potenser med basen e.
De fem förbättrade äldre faciten behåller rätt svar och visar sina egna
algebraiska övergångar. 2.816 behålls. När en enda logaritm uttryckligen
efterfrågas används `en_logaritm`, även för ln. Se FP53. Skydd:
`tools/ma3-logaritmer-2026-10-22.test.js` och konsumentens browserprov.

### Ma3-faktorisering: fortsättning 2026-10-22

Se `MA3_FAKTORISERING_2026-10-22.md`, nya 1.874–1.879. Areabilder ska
stämma med det algebraiska uttrycket och ha läsbara längdmarkeringar.
Faktorform kräver `faktoriserat`: omordnade faktorer och likvärdiga
teckenbyten godtas, medan en utvecklad summa inte uppfyller ett uttryckligt
krav på faktorform. Skydd: `tools/ma3-faktorisering-2026-10-22.test.js`
och konsumentens motsvarande browserprov. Äldre uppgifter är oförändrade.

### Rationella uttryck och svarsetiketter före förenklade polynom, 2026-10-22

Se `MA3_RATIONELLA_2026-10-22.md`: nya Mato1 1.880–1.887 samt fem
Ma1-jämförelser (1.08, 1.11, 1.18, 1.26, 1.67). `förenklat_polynom`
använder nu befintliga `hogerled` före sin strikta formkontroll, så att
y=3x och f(x)=3x godtas liksom 3x. Detta tar inte bort kravet på ett
färdigförenklat svar. Samlade termer, reducerade bråk och rätt variabel
krävs fortfarande. Skydd: konsumentens `tools/brakuttryck.test.js` och
`tools/ma3-rationella-2026-10-22.browser.cjs`, mastertest med samma datum.
