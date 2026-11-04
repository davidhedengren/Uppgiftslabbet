"""Individually authored solutions for all 68 measurement/uncertainty tasks."""
from render import *
# Single calculations: each tuple has the actual rule, substitution, and interpretation.
rows={
'2.230':(r'Tre värdesiffror: \(7{,}8463\to7{,}85\)',r'7{,}8463\approx7{,}85',r'7{,}85','Behåll 7, 8 och 4. Nästa siffra är 6, så fyran höjs till fem.'),
'2.231':(r'Tre värdesiffror: \(0{,}07586\to0{,}0759\)',r'0{,}07586\approx0{,}0759',r'0{,}0759','Börja räkna vid 7; nollorna före den är inte värdesiffror. Behåll 7, 5 och 8. Nästa siffra 6 höjer åttan till nio.'),
'2.232':(r'Längd från två lägen: \(L=x_2-x_1\)',r'L=7{,}8-1{,}2=6{,}6\ \mathrm{cm}',r'6{,}6\ \mathrm{cm}','Vänstra änden ligger vid 1,2 cm och högra vid 7,8 cm. Höger ändläge ensamt är inte föremålets längd.'),
'2.234':(r'Displayens sista plats: \(10^{-2}\ \mathrm g\)',r'10^{-2}\ \mathrm g=0{,}01\ \mathrm g',r'0{,}01\ \mathrm g','Vågen visar hundradels gram. Det är upplösningen, inte ett löfte om att varje mätning är korrekt inom 0,01 g.'),
'2.236':(r'Övre avrundningsgräns: \(x+\frac{h}{2}\)',r'12{,}4+\frac{0{,}1}{2}=12{,}45\ \mathrm{cm}',r'12{,}45\ \mathrm{cm}','Avrundningssteget h är 0,1 cm. Gränsen ingår inte: exakt 12,45 cm avrundas uppåt till 12,5 cm. Det finns därför inget största tal i intervallet.'),
'2.237':(r'Undre avrundningsgräns: \(x-\frac{h}{2}\)',r'12{,}4-\frac{0{,}1}{2}=12{,}35\ \mathrm{cm}',r'12{,}35\ \mathrm{cm}','Avrundningssteget h är 0,1 cm. Exakt 12,35 avrundas uppåt till 12,4, så denna gräns ingår.'),
'2.238':(r'Absolut osäkerhet i \(F\pm\Delta F\)',r'\Delta F=0{,}3\ \mathrm N',r'0{,}3\ \mathrm N','Talet efter ± är osäkerheten. Den har samma enhet som kraften; 18,2 N är mätvärdet.'),
'2.239':(r'Relativ osäkerhet: \(u=\Delta m/m\)',r'u=\frac{0{,}5}{45{,}0}\approx0{,}0111\approx1{,}1\,\%',r'1{,}1\,\%','Den absoluta osäkerheten är 0,5 g och mätvärdet 45,0 g. Enheterna tar ut varandra. Multiplicera kvoten med 100 för att få procent.'),
'2.240':(r'Medelvärde: \(\bar x=(x_1+x_2+x_3)/3\)',r'\bar x=\frac{5{,}12+5{,}15+5{,}14}{3}\ \mathrm{cm}\approx5{,}14\ \mathrm{cm}',r'5{,}14\ \mathrm{cm}','Summera de tre mätningarna och dela med antalet, tre.'),
'2.241':(r'Variationsbredd: \(R=t_{\max}-t_{\min}\)',r'R=2{,}17-2{,}11=0{,}06\ \mathrm s',r'0{,}06\ \mathrm s','Det största värdet är 2,17 s och det minsta 2,11 s. Övriga värden påverkar inte variationsbredden.'),
'2.242':(r'Angiven uppskattningsregel: \(\Delta t=R/2\)',r'\Delta t=\frac{0{,}06}{2}=0{,}03\ \mathrm s',r'0{,}03\ \mathrm s','Frågan anger att osäkerheten ska uppskattas som halva variationsbredden. Det är en uppskattningsmetod, inte en garanti för alla tänkbara mätfel.'),
'2.243':(r'Period: \(T=t/N\)',r'T=\frac{14{,}8\ \mathrm s}{10}=1{,}48\ \mathrm s',r'1{,}48\ \mathrm s','Perioden är tiden för en svängning. Totaltiden avser tio svängningar.'),
'2.245':(r'Korrigering av nollfel: \(m=m_{\text{visad}}-f\)',r'm=72{,}40-0{,}20=72{,}20\ \mathrm{kg}',r'72{,}20\ \mathrm{kg}','Vågen visar för mycket. Därför dras det kända felet bort.'),
'2.246':(r'Relativt fel: \(f=|U-U_{\text{ref}}|/U_{\text{ref}}\)',r'f=\frac{|11{,}7-12{,}0|}{12{,}0}=0{,}025=2{,}5\,\%',r'2{,}5\,\%','Skillnadens storlek är 0,3 V. Frågan jämför med referensvärdet 12,0 V, inte med instrumentets visning.'),
'2.248':(r'Rektangelns area: \(A=lb\)',r'A=2{,}4\cdot3{,}15=7{,}56\ \mathrm{m^2}\approx7{,}6\ \mathrm{m^2}',r'7{,}6\ \mathrm{m^2}','Längden 2,4 m har två värdesiffror. Med den vanliga tumregeln för multiplikation redovisas därför arean med två värdesiffror; behåll fler siffror i mellanräkningen.'),
'2.249':(r'Densitet: \(\rho=m/V\)',r'\rho=\frac{15{,}0\ \mathrm g}{2{,}0\ \mathrm{cm^3}}=7{,}5\ \mathrm{g/cm^3}',r'7{,}5\ \mathrm{g/cm^3}','Volymen har två värdesiffror, så två är en lämplig precision i slutsvaret.'),
'2.250':(r'Summa: \(L=L_1+L_2\)',r'L=12{,}3+0{,}56=12{,}86\ \mathrm{cm}\approx12{,}9\ \mathrm{cm}',r'12{,}9\ \mathrm{cm}','Vid addition utgår avrundningen från den grövsta decimalplatsen. Den första längden är angiven till tiondels centimeter, så slutsvaret redovisas på samma decimalplats.'),
'2.251':(r'Avstånd: \(d=x_2-x_1\)',r'd=8{,}62-1{,}4=7{,}22\ \mathrm m\approx7{,}2\ \mathrm m',r'7{,}2\ \mathrm m','Läget 1,4 m är angivet till tiondels meter. Vid subtraktion redovisas slutsvaret på den grövsta decimalplatsen.'),
'2.252':(r'Periodens osäkerhet: \(\Delta T=\Delta t/N\)',r'\Delta T=\frac{0{,}2}{20}=0{,}010\ \mathrm s',r'0{,}010\ \mathrm s','Antalet svängningar är exakt. När totaltiden delas med 20 delas även intervallets bredd, och därmed den absoluta osäkerheten, med 20.'),
'2.254':(r'Största rektangelarea: \(A_{\max}=l_{\max}b_{\max}\)',r'\begin{aligned}A_{\max}&=(12{,}0+0{,}1)(8{,}0+0{,}1)\\&=98{,}01\ \mathrm{cm^2}\end{aligned}',r'98{,}01\ \mathrm{cm^2}','Båda längderna är positiva. Arean blir störst när både längd och bredd är störst: 12,1 cm respektive 8,1 cm.'),
'2.257':(r'Halva variationsbredden: \(\Delta a=(a_{\max}-a_{\min})/2\)',r'\Delta a=\frac{9{,}84-9{,}77}{2}=0{,}035\ \mathrm{m/s^2}',r'0{,}035\ \mathrm{m/s^2}','Största värdet är 9,84 och minsta 9,77 m/s². Använd frågans uppskattningsregel och behåll svaret utan ytterligare avrundning.'),
'2.259':(r'Jämför skalstegen: \(k=h_{\text{linjal}}/h_{\text{skjutmått}}\)',r'k=\frac{1\ \mathrm{mm}}{0{,}05\ \mathrm{mm}}=20',r'20','Skjutmåttets minsta steg är en tjugondel av linjalens. Det är stegen, inte den uppmätta längden 30 mm, som ska jämföras.'),
'2.262':(r'Korrigera systematiskt fel: \(m=m_{\text{visad}}-f\)',r'm=124{,}8-0{,}5=124{,}3\ \mathrm g',r'124{,}3\ \mathrm g','Det kända felet på +0,5 g försvinner inte när fler vägningar medelvärdesbildas. Slumpmässiga avvikelser kan däremot delvis ta ut varandra.'),
'2.267':(r'Tidlösa formeln från vila: \(a=v^2/(2s)\)',r'a=\frac{12{,}0^2}{2\cdot25}=2{,}88\ \mathrm{m/s^2}\approx2{,}9\ \mathrm{m/s^2}',r'2{,}9\ \mathrm{m/s^2}','Vi använder frågans givna samband. Sträckan har två värdesiffror och farten tre; två värdesiffror är en lämplig precision i slutsvaret.'),
'2.269':(r'Diameter från täta varv: \(d=L/N\)',r'd=\frac{12{,}6}{40}=0{,}315\ \mathrm{mm}',r'0{,}315\ \mathrm{mm}','De 40 täta varven upptar 40 diametrar. Enligt den givna osäkerheten blir diameterns osäkerhet 0,1/40 = 0,0025 mm.'),
'2.351':(r'Längd från nollan: \(L=x_{\text{höger}}\)',r'L=7{,}0+4\cdot0{,}1=7{,}4\ \mathrm{cm}',r'7{,}4\ \mathrm{cm}','Linjalen har millimeterstreck. Höger ändpunkt ligger fyra sådana steg efter 7 cm, och vänster ändpunkt ligger vid noll.'),
'2.352':(r'Längd mellan ändpunkter: \(L=x_2-x_1\)',r'L=8{,}5-2{,}0=6{,}5\ \mathrm{cm}',r'6{,}5\ \mathrm{cm}','Läs av båda ändarna. Pinnen börjar vid 2,0 cm, så 8,5 cm är ett läge, inte pinnens längd.'),
'2.354':(r'Medelvärde: \(\bar t=(t_1+\cdots+t_5)/5\)',r'\bar t=\frac{2{,}3+2{,}4+2{,}5+2{,}6+2{,}7}{5}=\frac{12{,}5}{5}=2{,}5\ \mathrm s',r'2{,}5\ \mathrm s','Diagrammets fem mätvärden väger lika mycket. Summera dem och dela med fem.'),
'2.356':(r'Relativ osäkerhet: \(u=\Delta m/m\)',r'u=\frac{0{,}5}{50{,}0}=0{,}01=1\,\%',r'1\,\%','Osäkerheten 0,5 g jämförs med mätvärdet 50,0 g. Kvoten 0,01 motsvarar en procent.'),
'2.357':(r'Undre gräns: \(T_{\min}=T-\Delta T\)',r'T_{\min}=21{,}5-0{,}5=21{,}0\ ^\circ\mathrm C',r'21{,}0\ ^\circ\mathrm C','Mätintervallet sträcker sig 0,5 °C åt båda håll från 21,5 °C.')}
for id,args in rows.items():setq(id,*conv(*args))
# Repair sentence fragments left by earlier removal of rounding instructions.
byid['2.250']['t']=byid['2.250']['t'].replace('Beräkna summan, eftersom 12,3 cm är angivet.','Beräkna summan av längderna.')
byid['2.251']['t']=byid['2.251']['t'].replace('Bestäm avståndet mellan dem, eftersom 1,4 m är angivet.','Bestäm avståndet mellan lägena.')
# Pure concepts legitimately use named concept headings, not artificial formulas.
concepts={
'2.228':('Värdesiffror och inledande nollor','Nollorna före 4 anger bara decimalens läge. Siffrorna 4 och 5 räknas, och den sista nollan anger också precision.','Tre värdesiffror: 4, 5 och den sista nollan.'),
'2.229':('Värdesiffror i ett decimaltal','I 120,0 är även båda nollorna betydelsefulla. Decimaltecknet visar att talet anges till tiondelar.','Fyra värdesiffror.'),
'2.247':('Nollor mellan och efter värdesiffror','I 3,0400 räknas nollan mellan 3 och 4. Även de två sista nollorna efter decimaltecknet räknas.','Fem värdesiffror.'),
'2.233':('Avläsning av menisken','Varje litet skalsteg är 2 ml. Vätskeytans lägsta punkt ligger ett skalsteg över 40 ml. Läs av den punkten, inte vätskans kanter mot glaset.','42 ml.'),
'2.235':('Avläsning mellan hela grader','De långa markeringarna anger hela grader. Den korta markeringen mellan 21 och 22 är 21,5 °C, och dit når vätskepelaren.','21,5 °C.'),
'2.353':('Systematiskt nollfel','Vågen visar 0,3 kg för mycket även utan belastning. Alla vägningar förskjuts åt samma håll. Felet försvinner inte genom att mäta flera gånger; vågen behöver nollställas.','Ett systematiskt fel.'),
'2.355':('Avvikande mätvärde','Fem tider ligger mellan 3,1 och 3,3 s. Tiden 4,0 s ligger tydligt utanför denna samling. Kontrollera anteckningen och tidtagningen eller gör om mätningen; kasta inte bort värdet enbart för att det avviker.','Mätvärdet 4,0 s bör kontrolleras.'),
'2.358':('Parallaxfel vid sned avläsning','Ögat ska ligga i höjd med vätskeytans lägsta punkt, som i position B. Från A eller C ser ytan ut att hamna mot ett annat skalstreck, trots att volymen inte ändras.','Position B.')}
for id,(h,b,a) in concepts.items():setq(id,[(h,p(b))],a)
setq('2.244',[(r'Skalsteg: \(h=L/N\)',p('Båda skalorna täcker 10 cm. Skala A har 10 lika stora steg och skala B 50.')+m(r'h_A=\frac{10}{10}=1\ \mathrm{cm}')+m(r'h_B=\frac{10}{50}=0{,}2\ \mathrm{cm}')),
('Upplösning skiljer sig från kalibrering',p('B:s minsta steg är fem gånger mindre. Den kan visa mindre längdskillnader, men det säger inte i sig att skalan är korrekt kalibrerad.'))],'Skala B har bäst upplösning: 0,2 cm per steg.')
setq('2.265',[(r'Jämför variation och visningssteg: \(0{,}06/0{,}01\)',m(r'\frac{0{,}06}{0{,}01}=6')+p('Variationens storlek är sex gånger det minsta visningssteget. Att visa fler decimaler tar inte bort variationen mellan mätningarna.'))],'Av de två angivna faktorerna begränsar variationen noggrannheten mest.')
setq('2.266',[(r'Variationsbredd: \(R=t_{\max}-t_{\min}\)',m(r'R_A=2{,}02-2{,}00=0{,}02\ \mathrm s')+m(r'R_B=2{,}08-1{,}94=0{,}14\ \mathrm s')),
('Precision beskriver hur tätt mätningarna ligger',p('Grupp A har mindre spridning och högre precision. Det visar inte vilken grupp som ligger närmast det sanna värdet, eftersom ett systematiskt fel kan finnas.'))],'Grupp A har högst precision.')
setq('2.260',[(r'Relativ osäkerhet: \(u=\Delta t/t\)',p('Låt perioden vara T. Den absoluta osäkerheten Δt för hela tidtagningen är lika stor i båda fallen.')+m(r'u_1=\frac{\Delta t}{T}')+m(r'u_{20}=\frac{\Delta t}{20T}=\frac{u_1}{20}'))],'Den relativa osäkerheten blir en tjugondel, alltså 20 gånger mindre.')
setq('2.261',[(r'Osäkerhetsintervall: \([g-\Delta g,\ g+\Delta g]\)',m(r'g_{\min}=9{,}72-0{,}08=9{,}64\ \mathrm{m/s^2}')+m(r'g_{\max}=9{,}72+0{,}08=9{,}80\ \mathrm{m/s^2}')),
('Jämför referensen med intervallet',p('Referensvärdet 9,82 m/s² är större än den övre gränsen 9,80 m/s².'))],'Nej. Referensvärdet ligger utanför det angivna intervallet.')
# Explicit worst-case constructions and approximations.
setq('2.253',[(r'Buntens tjocklek: \(L=N\,d\)',p('Varje ark är 0,10 mm tjockt. N ark ger därför L = 0,10N mm. Den absoluta osäkerheten är alltid 0,10 mm.')),
(r'Krav på relativ osäkerhet: \(\Delta L/L\le0{,}010\)',m(r'\frac{0{,}10}{0{,}10N}\le0{,}010')+m(r'\frac1N\le0{,}010\ \Rightarrow\ N\ge100')),
('Kontroll av minsta antal',p('100 ark ger tjockleken 10 mm. Osäkerheten 0,10/10 = 0,010 är exakt 1,0 %, vilket tillåts eftersom kravet är högst 1,0 %.'))],'Minst 100 ark.')
setq('2.273',[(r'Totaltid för N svängningar: \(t=NT\)',m(r't=1{,}50N\ \mathrm s')),
(r'Krav på relativ osäkerhet: \(\Delta t/t<0{,}005\)',m(r'\frac{0{,}30}{1{,}50N}<0{,}005')+m(r'0{,}30<0{,}0075N\ \Rightarrow\ N>40')),
('Välj första heltalet som uppfyller kravet',p('40 perioder ger exakt 0,5 %, men frågan kräver mindre än 0,5 %. Nästa heltal är 41.'))],'Minst 41 svängningar.')
setq('2.268',[(r'Största fart: \(v_{\max}=s_{\max}/t_{\min}\)',p('En större sträcka ökar kvoten, medan en kortare tid också ökar den. Måtten får variera oberoende.')+m(r's_{\max}=100{,}0+0{,}5=100{,}5\ \mathrm m')+m(r't_{\min}=12{,}0-0{,}2=11{,}8\ \mathrm s')),
('Sätt in intervallets yttervärden',m(r'v_{\max}=\frac{100{,}5}{11{,}8}\ \mathrm{m/s}\approx8{,}52\ \mathrm{m/s}'))],'Ungefär 8,52 m/s.')
for id,u0,u100,reading,answer in [('2.258','0{,}8','100{,}6','50{,}7','50{,}0'),('2.272','2{,}4','98{,}8','47{,}7','47{,}0')]:
 setq(id,[(r'Linjära skalor: \(T=\frac{u-u_0}{u_{100}-u_0}\cdot100\ ^\circ\mathrm C\)',p('u är avläsningen och T den verkliga temperaturen. Dra bort avläsningen vid 0 °C och jämför med hela visningsintervallet som motsvarar 100 °C.')),
 ('Sätt in de två kalibreringspunkterna',m(rf'T=\frac{{{reading}-{u0}}}{{{u100}-{u0}}}\cdot100\ ^\circ\mathrm C\approx{answer}\ ^\circ\mathrm C'))],inline(answer+r'\ ^\circ\mathrm C')+'.')
setq('2.255',[(r'Cylindervolym: \(V=\pi r^2h\)',p('Radien förekommer två gånger i produkten, höjden en gång. Använd den uppskattningsregel som frågan anger.')),
(r'Relativ volymosäkerhet: \(\Delta V/V\approx2\Delta r/r+\Delta h/h\)',m(r'\frac{\Delta V}{V}\approx2\cdot\frac{0{,}02}{2{,}50}+\frac{0{,}1}{10{,}0}')+m(r'\frac{\Delta V}{V}\approx0{,}016+0{,}010=0{,}026=2{,}6\,\%'))],'Ungefär 2,6 %.')
setq('2.256',[(r'Densitetens mittvärde: \(\rho=m/V\)',m(r'\rho=\frac{85{,}0}{10{,}0}=8{,}50\ \mathrm{g/cm^3}')),
(r'Relativ osäkerhet enligt frågan: \(u\approx\Delta m/m+\Delta V/V\)',m(r'u\approx\frac{0{,}1}{85{,}0}+\frac{0{,}2}{10{,}0}\approx0{,}02118')),
(r'Absolut osäkerhet: \(\Delta\rho\approx u\rho\)',p('Kvoten u saknar enhet. Multiplicera med densiteten för att få osäkerheten i g/cm³.')+m(r'\Delta\rho\approx\left(\frac{0{,}1}{85{,}0}+\frac{0{,}2}{10{,}0}\right)8{,}50')+m(r'\Delta\rho\approx0{,}18\ \mathrm{g/cm^3}'))],'Ungefär 0,18 g/cm³.')
setq('2.263',[(r'Cirkelns area: \(A=\pi r^2\)',m(r'A=\pi\cdot5{,}00^2\approx78{,}54\ \mathrm{cm^2}')),
(r'Relativ osäkerhet: \(u\approx2\Delta r/r\)',m(r'u\approx\frac{2\cdot0{,}05}{5{,}00}=0{,}020')),
(r'Absolut osäkerhet: \(\Delta A\approx uA\)',m(r'\Delta A\approx0{,}020\cdot\pi\cdot5{,}00^2\approx1{,}57\ \mathrm{cm^2}'))],'Ungefär 1,57 cm².')
setq('2.264',[(r'Rätblockets volym: \(V=lbh\)',m(r'V=20{,}0\cdot10{,}0\cdot5{,}0=1000\ \mathrm{cm^3}')),
(r'Relativ osäkerhet enligt frågan: \(u\approx\Delta l/l+\Delta b/b+\Delta h/h\)',m(r'u\approx\frac{0{,}1}{20{,}0}+\frac{0{,}1}{10{,}0}+\frac{0{,}1}{5{,}0}=0{,}035')),
(r'Absolut osäkerhet: \(\Delta V\approx uV\)',m(r'\Delta V\approx0{,}035\cdot1000=35\ \mathrm{cm^3}'))],'Ungefär 35 cm³.')
multi('2.3',[
conv(r'Relativ tidsosäkerhet: \(u=\Delta t/t\)',r'u=\frac{0{,}20}{1{,}4}\approx0{,}143\approx14\,\%',r'14\,\%','Vid en svängning är mättiden 1,4 s och den absoluta osäkerheten 0,20 s.'),
([(r'Period från 20 svängningar: \(T=t_{20}/20\)',m(r'T=28/20=1{,}4\ \mathrm s')+m(r'\Delta T=0{,}20/20=0{,}010\ \mathrm s')),
(r'Relativ osäkerhet: \(u=\Delta T/T\)',m(r'u=\frac{0{,}010}{1{,}4}=\frac{0{,}20}{28}\approx0{,}00714\approx0{,}71\,\%'))],'Ungefär 0,71 %.'),
([(r'Samma absoluta tidtagningsfel: \(u=\Delta t/t\)',p('När hela mättiden blir 20 gånger längre men start- och stoppfelet är oförändrat blir kvoten en tjugondel. Felet fördelas över fler svängningar.'))],'Att mäta 20 svängningar ger mycket mindre relativ osäkerhet i perioden.')])
multi('2.4',[
([(r'Densitet: \(\rho=m/V\)',p('Kvoten blir större när massan ökar och när volymen minskar. Välj därför största tillåtna massa och minsta tillåtna volym.')+m(r'm_{\max}=285+10=295\ \mathrm g')+m(r'V_{\min}=175-15=160\ \mathrm{cm^3}'))],'Största massan 295 g och minsta volymen 160 cm³ ger högsta densiteten.'),
([(r'Högsta densitet: \(\rho_{\max}=m_{\max}/V_{\min}\)',m(r'\rho_{\max}=\frac{295}{160}\approx1{,}84\ \mathrm{g/cm^3}')),
(r'Lägsta densitet: \(\rho_{\min}=m_{\min}/V_{\max}\)',p('För lägsta kvoten används tvärtom minsta massa, 285 − 10 = 275 g, och största volym, 175 + 15 = 190 cm³.')+m(r'\rho_{\min}=\frac{275}{190}\approx1{,}45\ \mathrm{g/cm^3}'))],'Maximalt ungefär 1,84 g/cm³ och minimalt ungefär 1,45 g/cm³.')])
multi('2.13',[
([(r'Konstant fart: \(s=vt\)',p('Alla möjliga farter och tider är positiva. Den största sträckan fås därför när båda storheterna har sina största värden.')+m(r's_{\max}=(v+\Delta v)(t+\Delta t)'))],r'\(s_{\max}=(v+\Delta v)(t+\Delta t)\).'),
([(r'Kortaste sträckan: \(s_{\min}=(v-\Delta v)(t-\Delta t)\)',p('Den kortaste sträckan fås med minsta fart och minsta tid.')),
('Utveckla båda produkterna',m(r's_{\max}=vt+v\Delta t+t\Delta v+\Delta v\Delta t')+m(r's_{\min}=vt-v\Delta t-t\Delta v+\Delta v\Delta t')),
('Subtrahera och samla lika termer',p('Termerna vt och ΔvΔt tar ut varandra. De båda återstående termerna får vardera faktorn två.')+m(r's_{\max}-s_{\min}=2v\Delta t+2t\Delta v'))],r'Intervallets bredd är \(2v\Delta t+2t\Delta v\).'),
conv(r'Intervallets bredd: \(B=2v\Delta t+2t\Delta v\)',r'\begin{aligned}B&=2\cdot6{,}0\cdot10\\&\quad+2\cdot300\cdot0{,}2\\&=240\ \mathrm m\end{aligned}',r'240\ \mathrm m','Vi söker hela intervallets bredd, inte en osäkerhet åt bara ena hållet.')])
multi('2.14',[
([(r'Halva avrundningssteget: \(h/2=1/2\ \mathrm{km}\)',m(r'd_{\min}=24-0{,}5=23{,}5\ \mathrm{km}')+m(r'd_{\text{övre}}=24+0{,}5=24{,}5\ \mathrm{km}')),
('Undre gränsen ingår, övre gränsen ingår inte',p('23,5 avrundas uppåt till 24. Men 24,5 avrundas uppåt till 25 och ska därför inte ingå.'))],r'\(23{,}5\le d<24{,}5\) km.'),
([(r'Halva avrundningssteget: \(h/2=0{,}1/2\ \mathrm{km}\)',m(r'd_{\min}=24{,}0-0{,}05=23{,}95\ \mathrm{km}')+m(r'd_{\text{övre}}=24{,}0+0{,}05=24{,}05\ \mathrm{km}')+p('Samma regel för halva steg gäller.'))],r'\(23{,}95\le d<24{,}05\) km.'),
([(r'Intervallbredd: \(B=d_{\text{övre}}-d_{\min}\)',m(r'B_1=24{,}5-23{,}5=1\ \mathrm{km}')+m(r'B_2=24{,}05-23{,}95=0{,}10\ \mathrm{km}')+m(r'B_2/B_1=0{,}10'))],'Bredden minskar till en tiondel: från 1 km till 0,10 km.')])
setq('2.15',[(r'Ett arks relativa osäkerhet: \(u_1=\Delta t/t\)',m(r'u_1=\frac{0{,}02}{0{,}10}=0{,}20=20\,\%')),
(r'Tjocklek per ark i bunten: \(t=L/N\)',m(r't=52/500=0{,}104\ \mathrm{mm}')+m(r'\Delta t=1/500=0{,}002\ \mathrm{mm}')),
(r'Buntmetodens relativa osäkerhet: \(u_2=\Delta t/t\)',m(r'u_2=\frac{0{,}002}{0{,}104}=\frac1{52}\approx1{,}9\,\%')),
('Jämför metoder under samma antaganden',p('Buntmetoden har lägre relativ osäkerhet. Slutsatsen förutsätter, som frågan anger, att arken är lika tjocka och ligger tätt utan att pressas samman. Luft eller hoppressning kan annars ge ett extra systematiskt fel.'))],'Buntmetoden: ungefär 1,9 % jämfört med 20 % för ett enda ark.')
multi('2.16',[([('Värdesiffror',p(expl))],ans) for expl,ans in [
('25 innehåller två betydelsefulla siffror, 2 och 5.','2 värdesiffror.'),
('I 25,0 anger även sista nollan precision.','3 värdesiffror.'),
('I 0,04 anger nollorna bara decimalens läge; endast 4 räknas.','1 värdesiffra.'),
('I 0,040 räknas 4 och den sista nollan.','2 värdesiffror.'),
('I grundpotensformen räknas siffrorna i 3,00. Tiopotensen ändrar inte antalet.','3 värdesiffror.'),
('I 3,000 är alla tre avslutande nollor angiven precision.','4 värdesiffror.')]])
multi('2.28',[
conv(r'Densitet: \(\rho=m/V\)',r'\rho=\frac{580}{480}\approx1{,}208\ \mathrm{g/cm^3}',r'1{,}208\ \mathrm{g/cm^3}','Mittmassan 0,58 kg = 580 g och mittvolymen 480 ml = 480 cm³. Använd mittvärdena, inte intervallets gränser.'),
([(r'Lägsta densitet: \(\rho_{\min}=m_{\min}/V_{\max}\)',p('Minsta massan är 580 − 10 = 570 g. Största volymen är 480 + 20 = 500 cm³. En liten täljare och stor nämnare ger minsta kvoten.')+m(r'\rho_{\min}=\frac{570}{500}=1{,}140\ \mathrm{g/cm^3}'))],'1,140 g/cm³.'),
([(r'Högsta densitet: \(\rho_{\max}=m_{\max}/V_{\min}\)',p('Största massan är 580 + 10 = 590 g. Minsta volymen är 480 − 20 = 460 cm³.')+m(r'\rho_{\max}=\frac{590}{460}\approx1{,}283\ \mathrm{g/cm^3}'))],'Ungefär 1,283 g/cm³.')])
multi('2.30',[
([(r'Medelvärde: \(\bar t=\sum t_i/N\)',p('Båda eleverna har fem värden. Summera respektive serie och dividera med fem.')+m(r'\begin{aligned}S_A&=1{,}42+1{,}41+1{,}43\\&\quad+1{,}42+1{,}42\\&=7{,}10\ \mathrm s\end{aligned}')+m(r'\bar t_A=7{,}10/5=1{,}420\ \mathrm s')+m(r'\begin{aligned}S_B&=1{,}38+1{,}47+1{,}35\\&\quad+1{,}50+1{,}40\\&=7{,}10\ \mathrm s\end{aligned}')+m(r'\bar t_B=7{,}10/5=1{,}420\ \mathrm s'))],'Båda medelvärdena är 1,42 s.'),
([(r'Variationsbredd: \(R=t_{\max}-t_{\min}\)',m(r'R_A=1{,}43-1{,}41=0{,}02\ \mathrm s')+m(r'R_B=1{,}50-1{,}35=0{,}15\ \mathrm s')+p('A:s mätningar ligger tätare samlade.'))],'Elev A har högre precision.'),
([('Precision och riktighet är olika',p('Liten spridning visar hög precision. Alla mätningar kan ändå ha förskjutits av samma systematiska fel. Utan en oberoende referens vet vi inte hur nära det sanna värdet de ligger.'))],'Nej. Hög precision garanterar inte att mätvärdena ligger nära det sanna värdet.')])
multi('2.44',[
([('Värdesiffror i längden',p('Alla tre siffror i 12,4 är betydelsefulla: 1, 2 och 4.'))],'3 värdesiffror.'),
([('Värdesiffror i bredden',p('I 3,0 anger nollan precisionen och räknas tillsammans med 3.'))],'2 värdesiffror.'),
([(r'Area: \(A=lb\)',m(r'A=12{,}4\cdot3{,}0=37{,}2\ \mathrm{cm^2}')),
('Avrunda enligt frågans regel',p('Bredden har färst värdesiffror, två. Behåll därför 3 och 7. Nästa siffra är 2, så talet avrundas till 37.'))],'37 cm².')])
plans=[]
for C,h,result,why in [('1{,}45','12{,}0','2{,}01','Använd måttens mittvärden: C = 1,45 m och h = 12,0 m.'),('1{,}43','11{,}7','1{,}90','Volymen ökar med både omkrets och längd. Välj därför båda minsta måtten: C = 1,45 − 0,02 = 1,43 m och h = 12,0 − 0,3 = 11,7 m.'),('1{,}47','12{,}3','2{,}12','För högsta volym väljs båda största måtten: C = 1,45 + 0,02 = 1,47 m och h = 12,0 + 0,3 = 12,3 m.')]:
 plans.append(([(r'Omkrets: \(C=2\pi r\Rightarrow r=C/(2\pi)\)',p(why)),
 (r'Cylindervolym: \(V=\pi r^2h\)',m(r'V=\pi\left(\frac{C}{2\pi}\right)^2h=\frac{C^2h}{4\pi}')),
 ('Sätt in de valda måtten',m(rf'V=\frac{{{C}^2\cdot{h}}}{{4\pi}}\ \mathrm{{m^3}}\approx{result}\ \mathrm{{m^3}}'))],inline(result+r'\ \mathrm{m^3}')+'.'))
multi('2.45',plans)
# Linear regression: independently calculated, with a diagram of all five measurements.
xs=[10,20,35,50,65];ys=[90,174,300,426,550]
k=(sum(x*y for x,y in zip(xs,ys))-sum(xs)*sum(ys)/5)/(sum(x*x for x in xs)-sum(xs)**2/5)
b=sum(ys)/5-k*sum(xs)/5
assert abs(k-8.37055837563)<1e-8 and abs(b-6.65989847716)<1e-8
px=lambda x:55+350*x/70;py=lambda y:290-240*y/600
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 345" width="450" height="345" style="max-width:100%;height:auto;display:block" role="img" aria-label="Massa mot volym. Fem mätpunkter och anpassad linje med lutningen 8,37 gram per centiliter."><title>Linjär anpassning av massa mot volym</title><rect width="450" height="345" rx="10" fill="white"/>'
for x in range(0,71,10):svg+=f'<line x1="{px(x)}" x2="{px(x)}" y1="50" y2="290" stroke="#dde5ed"/><text x="{px(x)}" y="310" text-anchor="middle" font-size="18" fill="#172438">{x}</text>'
for y in range(0,601,100):svg+=f'<line x1="55" x2="405" y1="{py(y)}" y2="{py(y)}" stroke="#dde5ed"/><text x="46" y="{py(y)+4}" text-anchor="end" font-size="18" fill="#172438">{y}</text>'
svg+='<path d="M55 45V290H415" fill="none" stroke="#172438" stroke-width="2"/><text x="55" y="26" font-size="20" fill="#172438">m (g)</text><text x="405" y="333" text-anchor="end" font-size="20" fill="#172438">V (cl)</text>'
svg+=f'<line x1="{px(0)}" y1="{py(b)}" x2="{px(70)}" y2="{py(k*70+b)}" stroke="#176c87" stroke-width="2.5"/>'
for x,y in zip(xs,ys):svg+=f'<circle cx="{px(x)}" cy="{py(y)}" r="4.5" fill="#ac371c"/>'
svg+='<text x="110" y="70" font-size="18" fill="#176c87" stroke="white" stroke-width="4" paint-order="stroke">m ≈ 8,37V + 6,66</text></svg>'
multi('2.46',[
([(r'Linjär modell: \(m=kV+b\)',p('Sätt volym V i cl på x-axeln och massa m i g på y-axeln. Lägg in de fem punkterna i ett digitalt verktyg och anpassa en rät linje med linjär regression.')),
 ('Läs av den anpassade linjens lutning',m(r'm\approx8{,}3706V+6{,}6599')+svg+p('Koefficienten framför V är lutningen. En ökning av volymen med 1 cl ger ungefär 8,37 g större massa.'))],'Lutningen är ungefär 8,37 g/cl.'),
([(r'Densitet som lutning: \(\rho=\Delta m/\Delta V\)',p('Linjens lutning beskriver hur mycket vätskans massa ökar per tillagd volym. En cl är 10 cm³.')+m(r'\rho=\frac{8{,}3706\ \mathrm g}{10\ \mathrm{cm^3}}\approx0{,}837\ \mathrm{g/cm^3}'))],'Ungefär 0,837 g/cm³ (cirka 0,84 g/cm³).'),
([(r'Skärning med massaaxeln: \(m(0)=b\)',p('Modellen ger ungefär 6,66 g även vid noll vätskevolym. Det kan bero på att behållarens massa inte tarerats bort eller på ett nollfel i vågen. Skärningen ensam avgör inte orsaken.'))],'Exempelvis en behållare som inte tarerats bort, eller ett nollfel.')])
byid['2.46']['geogebra']=True
multi('2.47',[
([(r'Cylindervolym: \(V=\pi r^2h\)',p('Sätt u = Δr/r och w = Δh/h. Vid de största tillåtna måtten blir r + Δr = r(1 + u) och h + Δh = h(1 + w).')),
(r'Volymkvot: \(V_{\max}/V=(1+u)^2(1+w)\)',m(r'\begin{aligned}&(1+u)^2(1+w)\\&=1+2u+w\\&\quad+u^2+2uw+u^2w\end{aligned}')),
('Försumma produkter av små relativa osäkerheter',p('Termerna u², uw och u²w är mycket mindre än u och w när båda osäkerheterna är små. Efter att mittvärdet 1 dragits bort återstår första ordningens bidrag. Samma resonemang vid de minsta måtten ger motsatt tecken.')+m(r'\frac{\Delta V}{V}\approx2u+w=2\frac{\Delta r}{r}+\frac{\Delta h}{h}'))],r'\(\Delta V/V\approx2\Delta r/r+\Delta h/h\).'),
([(r'Radien i kvadrat: \(V=\pi r^2h\)',p('Radien förekommer två gånger i produkten, höjden en gång. Samma lilla relativa ändring i radien påverkar därför volymen ungefär dubbelt så mycket som motsvarande ändring i höjden.'))],'Radieosäkerheten får faktorn 2 eftersom radien är kvadrerad.'),
([(r'Omkrets och radie: \(C=2\pi r\)',p('En konstant faktor ändrar inte den relativa osäkerheten. Därför är Δr/r = ΔC/C = 1,4 %.')),
(r'Volymens relativa osäkerhet: \(u_V\approx2u_r+u_h\)',m(r'u_V\approx2\cdot1{,}4\,\%+2{,}5\,\%=5{,}3\,\%'))],'Ungefär 5,3 %.')])
multi('2.48',[
([('Systematiskt respektive slumpmässigt fel',p('Första vågen visar alltid 0,3 kg för mycket, alltså ett systematiskt fel. Den andra visar ibland för mycket och ibland för lite kring rätt värde, alltså slumpmässiga fel.'))],'Första vågen: systematiskt fel. Andra vågen: slumpmässiga fel.'),
([(r'Medelvärde: \(\bar m=(m_1+\cdots+m_{10})/10\)',p('Oberoende slumpmässiga avvikelser tar delvis ut varandra när man bildar medelvärdet. En konstant förskjutning på +0,3 kg finns däremot i varje värde och därför också i medelvärdet. Slumpfelet blir inte säkert noll efter tio mätningar.'))],'Den slumpmässiga osäkerheten i medelvärdet brukar minska. Det systematiska felet blir kvar.'),
([('Kalibrering mot en känd massa',p('Väg en oberoende känd massa. Om vågen visar 0,3 kg för mycket, nollställ eller kalibrera den. Om det inte går kan det kända felet dras bort från varje avläsning.'))],'Kontrollera med en känd massa och kalibrera vågen eller korrigera dess avläsningar.')])
setq('2.270',[(r'Rörelseenergi: \(E=mv^2/2\)',p('Sätt u = Δm/m och w = Δv/v. För största tillåtna massa och fart gäller följande kvot.')+m(r'\frac{E_{\max}}E=(1+u)(1+w)^2')),
('Utveckla och behåll första ordningens bidrag',m(r'\begin{aligned}&(1+u)(1+w)^2\\&=1+u+2w\\&\quad+w^2+2uw+uw^2\end{aligned}')+p('När de relativa osäkerheterna är små kan w², uw och uw² försummas. Vid de minsta värdena fås motsvarande minskning.')),
(r'Relativ energi-osäkerhet: \(\Delta E/E\approx\Delta m/m+2\Delta v/v\)',m(r'\frac{\Delta E}{E}\approx\frac{0{,}002}{0{,}450}+2\frac{0{,}3}{12{,}0}')+m(r'\frac{\Delta E}{E}\approx0{,}05444\approx5{,}4\,\%')),
(r'Mittvärde och absolut osäkerhet: \(\Delta E\approx u_EE\)',m(r'E=\frac{0{,}450\cdot12{,}0^2}{2}=32{,}4\ \mathrm J')+m(r'\Delta E\approx0{,}05444\cdot32{,}4\approx1{,}76\ \mathrm J')+p('Fartens bidrag är 5 %, medan massans är ungefär 0,44 %. Fartmätningen dominerar alltså osäkerheten.'))],r'\(\Delta E/E\approx\Delta m/m+2\Delta v/v\). Osäkerheten är cirka 5,4 % eller 1,8 J; resultatet kan skrivas \((32{,}4\pm1{,}8)\) J.')
setq('2.271',[(r'Cirkelarea med diameter: \(A=\pi d^2/4\)',p('Låt u = Δd/d. För största diametern blir förhållandet mellan största area och mittvärdets area:')+m(r'\frac{A_{\max}}A=(1+u)^2=1+2u+u^2')),
(r'Liten relativ osäkerhet: \(\Delta A/A\approx2\Delta d/d\)',p('u² är mycket mindre än 2u och kan försummas i uppskattningen.')+m(r'\frac{\Delta A}{A}\approx\frac{2\cdot0{,}5}{120{,}0}\approx0{,}00833\approx0{,}83\,\%')),
('Jämför de två metoderna',p('0,83 % är mindre än rutpappersmetodens 3 %. Även om kvadrattermen behålls blir slutsatsen densamma.'))],'Metod A ger lägst relativ osäkerhet, ungefär 0,83 %.')
multi('2.49',[
([(r'Avdunstad massa: \(m_{\text{avd}}=m_0-m_1\)',m(r'm_{\text{avd}}=312-309=3\ \mathrm g')),
(r'Största osäkerhet i differensen: \(\delta m_{\text{avd}}=\delta m_0+\delta m_1\)',p('Felen kan enligt frågan variera oberoende. Den största differensen fås om startvärdet är 1 g för högt och slutvärdet 1 g för lågt. De absoluta osäkerheterna adderas.')+m(r'\delta m_{\text{avd}}=1+1=2\ \mathrm g'))],r'\((3\pm2)\) g.'),
([(r'Relativ osäkerhet: \(u=\delta m/m\)',p('Jämför en startvägning med den beräknade masskillnaden.')+m(r'u_{\text{vägning}}=\frac1{312}\approx0{,}00321\approx0{,}32\,\%')+m(r'u_{\text{skillnad}}=\frac23\approx0{,}667\approx67\,\%')+p('Slutvägningen ger nästan samma relativa osäkerhet som startvägningen. Den lilla skillnaden är däremot mycket osäker.'))],'Ungefär 0,32 % i en vägning och 67 % i skillnaden.'),
([(r'Minska kvoten \(u=\delta m_{\text{avd}}/m_{\text{avd}}\)',p('Mät under längre tid så att mer vatten hinner avdunsta. Då blir masskillnaden större medan vågens absoluta avläsningsosäkerhet är ungefär densamma. En våg med mindre osäkerhet är ett annat sätt.')),
('Skilj oberoende fel från ett gemensamt nollfel',p('Om samma konstanta nollfel fanns vid båda vägningarna skulle just den delen ta ut sig i subtraktionen. Här ska vi däremot, enligt frågan, räkna med oberoende möjliga fel.'))],'Längre mättid, eller en våg med mindre osäkerhet, minskar den relativa osäkerheten.')])
if __name__=='__main__':
    targets={q['id'] for q in bank if q['omr']=='matnogg'}
    assert set(changes)==targets,(targets-set(changes),set(changes)-targets)
    assert len(targets)==68
    save()
    print('68 huvudfacit och 9 delfacit omskrivna.')
