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
