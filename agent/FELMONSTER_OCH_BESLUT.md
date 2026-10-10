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

**Sök efter:** `spelDelning`, saknat `spelDelar[i].s`, ”använd”, ”samma”, ”modellen”,
”mer än så”, facit som börjar med ett mellanresultat utan att det ges på kortet.

**Beslut:** varje kort ska innehålla sina givna värden, formel/figur, eget facit
och relevant ledtråd. Om ett tidigare resultat behövs för den avsedda nivån,
ge det direkt. Kalibrera kortets nivå efter den information som faktiskt visas.
Huvuduppgiftens och spelkortens delar ska ha entydig koppling till svaren.

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
