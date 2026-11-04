"""Explicitly authored and manually checked speed solutions, 2026-11-04."""
from render import *
F=r'Medelfart: \(v_m=s_{\mathrm{tot}}/t_{\mathrm{tot}}\)'
H=r'Medelhastighet: \(\bar v=\Delta x/\Delta t\)'
T=r'Tid vid konstant fart: \(t=s/v\)'
S=r'Sträcka vid konstant fart: \(s=vt\)'
U=r'Fartenheter: \(1\ \mathrm{m/s}=3{,}6\ \mathrm{km/h}\)'
MIN=r'Tidsenheter: \(1\ \mathrm{min}=60\ \mathrm s\)'
HOUR=r'Tidsenheter: \(1\ \mathrm h=3600\ \mathrm s\)'
KM=r'Längdenheter: \(1\ \mathrm{km}=1000\ \mathrm m\)'
E=r'Eko: \(2d=vt\)'
def st(h,tex='',why=''):return (h,(p(why) if why else '')+(m(tex) if tex else ''))
def plan(steps,answer):return (steps,answer)
def a(tex):return inline(tex)+'.'
def single(id,steps,answer):setq(id,steps,answer)
def one(h,tex,answer,why=''):return ([st(h,tex,why)],a(answer))
def parts(id,ps):multi(id,ps)
parts('3.1',[
 one(MIN,r't=92\cdot60=5520\ \mathrm s',r'5520\ \mathrm s'),
 one(F,r'v_m=\frac{4{,}25\cdot10^7}{92\cdot60}\approx7699\ \mathrm{m/s}',r'7699\ \mathrm{m/s}','Använd banans hela omkrets och tiden för ett helt varv. Tiden måste vara i sekunder.'),
 one(U,r'v_m=\frac{4{,}25\cdot10^7}{92\cdot60}\cdot3{,}6\approx27717\ \mathrm{km/h}',r'27717\ \mathrm{km/h}','Multiplicera den oavrundade farten i m/s med 3,6. Avrunda först slutsvaret.')])
parts('3.2',[one(T,r't=380/9{,}5=40\ \mathrm s',r'40\ \mathrm s'),one(U,r'v=9{,}5\cdot3{,}6=34{,}2\ \mathrm{km/h}',r'34{,}2\ \mathrm{km/h}')])
parts('3.3',[
 one(HOUR,r't=2\cdot3600+5\cdot60=7500\ \mathrm s',r'7500\ \mathrm s'),
 one(F,r'v_m=\frac{42195}{7500}=5{,}626\ \mathrm{m/s}\approx5{,}63\ \mathrm{m/s}',r'5{,}63\ \mathrm{m/s}','42,195 km är 42 195 m och hela tiden är 7500 s.'),
 one(r'Tid per kilometer: \(t_{\mathrm{km}}=t_{\mathrm{tot}}/s_{\mathrm{tot,km}}\)',r't_{\mathrm{km}}=7500/42{,}195\approx177{,}75\ \mathrm s',r'178\ \mathrm s','Dela hela tiden med antalet kilometer. 178 s motsvarar 2 min 58 s.')])
parts('3.229',[
 plan([st(T,r't_1=\frac{s}{2v_1},\qquad t_2=\frac{s}{2v_2}','Låt hela sträckan vara s. Halvorna är lika långa, men tiderna är olika.'),st(F,r'V=\frac{s}{s/(2v_1)+s/(2v_2)}=\frac{2v_1v_2}{v_1+v_2}')],a(r'V=\frac{2v_1v_2}{v_1+v_2}')),
 plan([st(r'Lös ut den andra farten: \(V(v_1+v_2)=2v_1v_2\)',r'\begin{aligned}Vv_1+Vv_2&=2v_1v_2\\Vv_1&=(2v_1-V)v_2\\v_2&=\frac{Vv_1}{2v_1-V}\end{aligned}','Multiplicera med nämnaren, samla termerna med v₂ och dividera.')],a(r'v_2=\frac{Vv_1}{2v_1-V}')),
 plan([st(T,r't_1=\frac{s/2}{36}=\frac{s}{72}=t_{\mathrm{mål}}','Mät s i km och tiden i timmar. Redan första halvan tar hela tiden som målet 72 km/h tillåter.'),st('Även den andra halvan måste ta tid','', 'Varje ändlig positiv fart ger en positiv restid. Därför blir totaltiden större än den tillåtna.')],'Målet 72 km/h kan inte nås med någon ändlig fart på andra halvan.'),
 plan([st(r'Positiv och ändlig fart: \(v_2=Vv_1/(2v_1-V)\)',r'2v_1-V\gt0\quad\Rightarrow\quad v_1\gt\frac V2','Täljaren är positiv. Nämnaren måste därför vara positiv och får inte vara noll.')],a(r'v_1\gt V/2'))])
parts('3.8',[
 one(F,r'v_m=400/96\approx4{,}17\ \mathrm{m/s}',r'4{,}2\ \mathrm{m/s}','Hela vägsträckan räknas, även när löparen återvänder till starten.'),
 one(r'Förflyttning: \(\Delta\vec x=\vec x_{\mathrm{slut}}-\vec x_{\mathrm{start}}\)',r'\Delta\vec x=\vec0',r'0\ \mathrm m','Startpunkt och slutpunkt sammanfaller.'),
 plan([st(H,r'\bar{\vec v}=\frac{\Delta\vec x}{96}=\vec0\ \mathrm{m/s}','Medelhastighet beror på förflyttningen. Medelfart beror på hela vägsträckan, som här är 400 m.')],'Medelhastigheten är 0 m/s, trots att medelfarten inte är noll.')])
for id,d,v1,v2,ansv in [('3.9','2','12','28','16{,}8'),('3.178','30','60','90','72')]:
 single(id,[st(T,rf't_1=\frac{{{d}}}{{{v1}}}\ \mathrm h,\qquad t_2=\frac{{{d}}}{{{v2}}}\ \mathrm h','Beräkna tiden för varje lika lång delsträcka.'),st(F,rf'v_m=\frac{{2\cdot{d}}}{{{d}/{v1}+{d}/{v2}}}={ansv}\ \mathrm{{km/h}}','Den långsammare delen tar längre tid. Därför fungerar inte ett vanligt medelvärde av farterna.')],a(ansv+r'\ \mathrm{km/h}'))
parts('3.19',[
 one(r'Total tid: \(t=t_1+t_2+t_3+t_4\)',r'\begin{aligned}t&=11{,}2+10{,}4+10{,}8+10{,}6\\&=43{,}0\ \mathrm s\end{aligned}',r'43{,}0\ \mathrm s'),
 one(F,r'v_m=400/43\approx9{,}30\ \mathrm{m/s}',r'9{,}30\ \mathrm{m/s}','Hela stafetten är 400 m och den sammanlagda tiden är 43,0 s.'),
 plan([st(F,r'v_{\mathrm{störst}}=100/10{,}4\approx9{,}62\ \mathrm{m/s}','Alla springer 100 m. Kortast tid ger därför störst medelfart; löpare 2 har tiden 10,4 s.')],'Löpare 2: cirka 9,62 m/s.')])
parts('3.20',[
 one(E,r'd_1=340\cdot0{,}40/2=68\ \mathrm m',r'68\ \mathrm m','Ekot innebär att ljudet går både till väggen och tillbaka. Avståndet är halva ljudsträckan.'),
 one(E,r'd_2=340\cdot1{,}10/2=187\ \mathrm m',r'187\ \mathrm m','Även det andra ekot färdas tur och retur.'),
 one(r'Avstånd mellan väggarna: \(D=d_1+d_2\)',r'\begin{aligned}D&=340\cdot0{,}40/2+340\cdot1{,}10/2\\&=255\ \mathrm m\end{aligned}',r'255\ \mathrm m','Personen står mellan väggarna. Därför adderar vi avstånden till dem.')])
parts('3.21',[
 one(S,r's=1500\cdot0{,}80=1200\ \mathrm m',r'1200\ \mathrm m','Här efterfrågas hela ljudsträckan, både ned och upp.'),
 one(E,r'd=1500\cdot0{,}80/2=600\ \mathrm m',r'600\ \mathrm m','Ljudet går till bottnen och tillbaka, så djupet är halva ljudsträckan.'),
 one(E,r'd=1500\cdot0{,}20/2=150\ \mathrm m',r'150\ \mathrm m','Den nya ekotiden är också tiden för en resa tur och retur.')])
parts('3.49',[
 one(HOUR,r't=8\cdot30\cdot24\cdot3600=20736000\ \mathrm s',r'20736000\ \mathrm s','Använd uppgiftens modell med 30 dygn per månad.'),
 one(F,r'v_m=\frac{70000\cdot1000}{8\cdot30\cdot24\cdot3600}\approx3{,}38\ \mathrm{m/s}',r'3{,}38\ \mathrm{m/s}','Hela flyttningens tid, även pauserna, ska vara med i nämnaren.'),
 one(F,r'v_m=\frac{70000}{8\cdot30\cdot24}\approx12{,}2\ \mathrm{km/h}',r'12{,}2\ \mathrm{km/h}','Här använder vi km och timmar direkt. Resultatet beskriver hela flyttningen, inte bara tiden i luften.')])
parts('3.50',[
 one(r'Medströms: \(v_{\mathrm{strand}}=v_{\mathrm{vatten}}+u\)',r'v=1{,}8+0{,}7=2{,}5\ \mathrm{m/s}',r'2{,}5\ \mathrm{m/s}','Paddlingen och strömmen verkar åt samma håll.'),
 one(r'Motströms: \(v_{\mathrm{strand}}=v_{\mathrm{vatten}}-u\)',r'v=1{,}8-0{,}7=1{,}1\ \mathrm{m/s}',r'1{,}1\ \mathrm{m/s}\text{ mot strömmen}','Strömmen motverkar paddlingen men är långsammare än kanotisten.'),
 one(T,r't=\frac{500}{1{,}8+0{,}7}=200\ \mathrm s',r'200\ \mathrm s','Använd farten relativt stranden, eftersom sträckan mäts längs älven.'),
 one(T,r't=\frac{500}{1{,}8-0{,}7}\approx455\ \mathrm s',r'455\ \mathrm s','Farten relativt stranden är 1,1 m/s motströms.')])
parts('3.51',[
 plan([st(r'Vägsträcka: \(s=s_1+s_2\)',r's=32+14=46\ \mathrm m','Båda gångsträckorna räknas positivt.'),st(F,r'v_m=46/24\approx1{,}92\ \mathrm{m/s}')],a(r'1{,}92\ \mathrm{m/s}')),
 plan([st(r'Förflyttning med tecken: \(\Delta x=32-14\)',r'\Delta x=+18\ \mathrm m','Österut är positiv riktning. Sträckan västerut minskar förflyttningen.'),st(H,r'\bar v=18/24=+0{,}75\ \mathrm{m/s}')],a(r'+0{,}75\ \mathrm{m/s}\text{ (österut)}'))])
parts('3.53',[one(S,r's=11{,}5\cdot32=368\ \mathrm m',r'368\ \mathrm m'),one(F,r'v=470/32\approx14{,}7\ \mathrm{m/s}',r'14{,}7\ \mathrm{m/s}'),one(T,r't=820/15\approx54{,}7\ \mathrm s',r'54{,}7\ \mathrm s')])
parts('3.54',[one(U,tex,answer,why) for tex,answer,why in [
(r'1{,}5\cdot3{,}6=5{,}4\ \mathrm{km/h}',r'5{,}4\ \mathrm{km/h}','Från m/s till km/h multiplicerar vi med 3,6.'),
(r'54/3{,}6=15\ \mathrm{m/s}',r'15\ \mathrm{m/s}','Från km/h till m/s dividerar vi med 3,6.'),
(r'90\cdot3{,}6=324\ \mathrm{km/h}',r'324\ \mathrm{km/h}','Från m/s till km/h multiplicerar vi med 3,6.'),
(r'72/3{,}6=20\ \mathrm{m/s}',r'20\ \mathrm{m/s}','Från km/h till m/s dividerar vi med 3,6.')]])
parts('3.55',[
 one(r'Tidsprefix: \(1\ \mathrm{ms}=10^{-3}\ \mathrm s\)',r't=12\cdot10^{-3}=0{,}012\ \mathrm s',r'0{,}012\ \mathrm s'),
 one(S,r's=340\cdot0{,}012=4{,}08\ \mathrm m',r'4{,}08\ \mathrm m','12 ms är 0,012 s. Det här är ljudets hela sträcka tur och retur.'),
 one(E,r'd=340\cdot0{,}012/2=2{,}04\ \mathrm m',r'2{,}04\ \mathrm m','Avståndet till insekten är halva ljudets sträcka eftersom ekot ska tillbaka.')])
parts('3.234',[
 plan([st(r'Farter relativt byggnaden: \(v_\pm=v\pm u\)',r'v_+=2{,}00\ \mathrm{m/s},\quad v_-=0{,}40\ \mathrm{m/s}','Addera 1,20 och 0,80 åt ena hållet; subtrahera åt det andra.'),st(T,r'\begin{aligned}t_+&=90/2=45\ \mathrm s\\t_-&=90/0{,}40=225\ \mathrm s\end{aligned}'),st(r'Total tid: \(T=t_++t_-\)',r'T=45+225=270\ \mathrm s')],a(r'270\ \mathrm s')),
 plan([st(F,r'v_m=180/270\approx0{,}667\ \mathrm{m/s}','Totalsträckan är 2 · 90 = 180 m och totaltiden 270 s.'),st(H,r'\bar v=0/270=0\ \mathrm{m/s}','Personen kommer tillbaka till startpunkten. Därför är förflyttningen noll.')],'Medelfart cirka 0,667 m/s; medelhastighet 0 m/s.'),
 plan([st(T,r'T=\frac L{v+u}+\frac L{v-u}'),st(r'Gemensam nämnare: \((v+u)(v-u)=v^2-u^2\)',r'T=\frac{L(v-u)+L(v+u)}{v^2-u^2}=\frac{2Lv}{v^2-u^2}')],a(r'T=\frac{2Lv}{v^2-u^2}')),
 plan([st(T,r't_{\mathrm{tillbaka}}=\frac L{v-u}\to\infty','När u närmar sig v underifrån närmar sig farten tillbaka noll. En bestämd sträcka tar då allt längre tid.')],'Totaltiden växer utan gräns. Vid u = v kommer personen inte tillbaka.')])
parts('3.96',[
 one(r'Längdenhet: \(1\ \mathrm{cm}=0{,}01\ \mathrm m\)',r's=45/100=0{,}45\ \mathrm m',r'0{,}45\ \mathrm m'),
 one(MIN,r't=15\cdot60=900\ \mathrm s',r'900\ \mathrm s'),
 one(F,r'v_m=0{,}45/900=0{,}0005\ \mathrm{m/s}',r'0{,}0005\ \mathrm{m/s}','45 cm är 0,45 m och 15 minuter är 900 s.'),
 plan([st(F,r'v_m=0{,}45/(15\cdot60)=0{,}0005\ \mathrm{m/s}'),st(HOUR,r't=24\cdot3600=86400\ \mathrm s'),st(S,r's=0{,}0005\cdot86400=43{,}2\ \mathrm m','Uppgiften antar samma medelfart hela dygnet, utan uppehåll.')],a(r'43{,}2\ \mathrm m'))])
parts('3.97',[
 plan([st(T,r't_1=200/100=2\ \mathrm h','Välj till exempel hela sträckan 200 km. Valet påverkar inte vilken bil som vinner.'),st(r'Deltider adderas: \(t_2=100/80+100/120\)',r't_2=\frac54+\frac56=\frac{25}{12}\ \mathrm h\gt2\ \mathrm h')],'Bilen som håller 100 km/h kommer fram först.'),
 plan([st(F,r'v_{m,2}=\frac{200}{100/80+100/120}=96\ \mathrm{km/h}','Den långsammare halvan tar längre tid än den snabbare. Lika långa sträckor innebär inte lika långa tider.')],'Medelfarten är 96 km/h. Ett vanligt medelvärde av farterna fungerar bara när tiderna är lika.')])
parts('3.99',[
 plan([st(U,r'v=80/3{,}6\ \mathrm{m/s}'),st(T,r't=150/(80/3{,}6)=6{,}75\ \mathrm s')],a(r'6{,}75\ \mathrm s')),
 plan([st(U,r'v=80/3{,}6\ \mathrm{m/s}'),st(S,r's=(80/3{,}6)\cdot2{,}5\approx55{,}6\ \mathrm m','Behåll farten oavrundad.')],a(r'55{,}6\ \mathrm m'))])
parts('3.101',[
 plan([st(r'Banradie: \(r=R+h\)',r'r=6371+700=7071\ \mathrm{km}','Höjden mäts från jordytan men banradien från jordens centrum.'),st(r'Cirkelns omkrets: \(s=2\pi r\)',r's=2\pi\cdot7071\approx44428{,}4\ \mathrm{km}')],a(r'44400\ \mathrm{km}')),
 plan([st(T,r't=\frac{2\pi\cdot(6371+700)}{7{,}5}\ \mathrm s','Använd den oavrundade omkretsen. km delat med km/s ger sekunder.'),st(MIN,r't=\frac{2\pi\cdot7071}{7{,}5\cdot60}\approx98{,}7\ \mathrm{min}')],a(r'98{,}7\ \mathrm{min}'))])
# Short routines: each heading, calculation and explanation is chosen explicitly.
for id,h,tex,answer,why in [
('3.102',F,r'v_m=660/30=22\ \mathrm{m/s}',r'22\ \mathrm{m/s}','Dela hela sträckan med hela tiden.'),
('3.256',F,r'v_m=135/11\approx12{,}3\ \mathrm{m/s}',r'12{,}3\ \mathrm{m/s}','Sträckan är i meter och tiden i sekunder.'),
('3.257',S,r's=6{,}0\cdot15=90\ \mathrm m',r'90\ \mathrm m','Farten är konstant, så varje sekund tillkommer 6,0 m.'),
('3.258',T,r't=340/14\approx24{,}3\ \mathrm s',r'24{,}3\ \mathrm s','Dela sträckan med farten.'),
('3.259',U,r'v=10\cdot3{,}6=36\ \mathrm{km/h}',r'36\ \mathrm{km/h}','Multiplicera med 3,6 när m/s ska bli km/h.'),
('3.260',U,r'v=50/3{,}6\approx13{,}9\ \mathrm{m/s}',r'13{,}9\ \mathrm{m/s}','Dividera med 3,6 när km/h ska bli m/s.'),
('3.261',r'Förflyttning: \(\Delta x=x_{\mathrm{slut}}-x_{\mathrm{start}}\)',r'\Delta x=20-20=0\ \mathrm m',r'0\ \mathrm m','Personen kommer tillbaka till startpunkten. Gångsträckan är större, men den efterfrågas inte.'),
('2.340',T,r't=8{,}0/0{,}40=20\ \mathrm s',r'20\ \mathrm s','Nästa framkant måste färdas 8,0 m till sensorn. Paketlängden behövs inte eftersom avståndet gäller motsvarande kanter.'),
('2.343',F,r'v_m=(3{,}0+5{,}0)/0{,}50=16\ \mathrm{km/h}',r'16\ \mathrm{km/h}','Addera de två delsträckorna i figuren. Hela sträckan är 8,0 km.'),
('2.344',F,r'v=(16-0)/(4-0)=4\ \mathrm{m/s}',r'4\ \mathrm{m/s}','Positionen ökar med 4 m varje sekund. Farten är konstant.'),
('2.346',U,r'v=90/3{,}6=25\ \mathrm{m/s}',r'25\ \mathrm{m/s}','Mätaren visar 90 km/h. Dividera med 3,6 för m/s.'),
('2.348',T,r't=150/100=1{,}5\ \mathrm h',r'1{,}5\ \mathrm h','Skylten anger 150 km kvar. km delat med km/h ger timmar.'),
('2.349',H,r'\bar v=600/120=5{,}0\ \mathrm{m/s}',r'5{,}0\ \mathrm{m/s}\text{ österut}','Hunden rör sig rakt från A till B. Förflyttningen är 600 m österut.')]:single(id,*one(h,tex,answer,why))
single('3.262',[st(MIN,r't=2{,}5\cdot60=150\ \mathrm s'),st(F,r'v_m=650/150\approx4{,}3\ \mathrm{m/s}')],a(r'4{,}3\ \mathrm{m/s}'))
parts('3.103',[
 one(S,r's=340\cdot6{,}0=2040\ \mathrm m\approx2{,}0\ \mathrm{km}',r'2{,}0\ \mathrm{km}','Börja enligt frågan med att låta de 6,0 sekunderna vara ljudets restid.'),
 plan([st(T,r't_{\mathrm{ljus}}=\frac{2040}{3{,}00\cdot10^8}=6{,}8\cdot10^{-6}\ \mathrm s','Samma sträcka tar ljuset 6,8 mikrosekunder, jämfört med ljudets 6,0 sekunder.')],'Ljusets restid är så kort att den inte påverkar det avrundade avståndet.')])
parts('3.104',[
 plan([st(T,r't_1=s/v','Första bilen håller samma fart hela vägen.'),st(r'Deltider adderas: \(t_2=t_a+t_b\)',r'\begin{aligned}t_2&=\frac{s/2}{0{,}8v}+\frac{s/2}{1{,}2v}\\&=\frac sv\left(\frac58+\frac5{12}\right)\\&=\frac{25}{24}\frac sv\end{aligned}','Andra bilens farter är 0,8v respektive 1,2v. Varje delsträcka är s/2.')],a(r't_1=\frac sv,\quad t_2=\frac{25}{24}\frac sv')),
 plan([st(r'Jämför restiderna: \(t_2/t_1\)',r'\frac{t_2}{t_1}=\frac{25}{24}\gt1','Kvoten är oberoende av s och v. Båda är positiva, så andra bilens tid är alltid längre.')],'Den andra bilen kommer alltid sist. Restiden är cirka 4,2 % längre.')])
single('3.235',[st(r'Återstående andel: \(f=1-1/4-1/3\)',r'f=5/12','Låt hela sträckan vara S km och den sista farten v km/h.'),st(T,r'\frac S{75}=\frac{S/4}{50}+\frac{S/3}{80}+\frac{5S/12}{v}','Målfarten bestämmer hela tiden. Den ska vara summan av de tre deltiderna.'),st('Dividera med sträckan och isolera sista tiden',r'\begin{aligned}\frac5{12v}&=\frac1{75}-\frac1{200}-\frac1{240}\\&=\frac1{240}\\v&=\frac{5\cdot240}{12}=100\ \mathrm{km/h}\end{aligned}')],a(r'100\ \mathrm{km/h}'))
parts('3.125',[
 one(T,r't_+=850/(4{,}2+1{,}3)\approx155\ \mathrm s',r'155\ \mathrm s','Medströms är farten relativt stranden 5,5 m/s.'),
 one(T,r't_-=850/(4{,}2-1{,}3)\approx293\ \mathrm s',r'293\ \mathrm s','Motströms är farten relativt stranden 2,9 m/s.'),
 plan([st(r'Total tid med ström: \(T=t_++t_-\)',r'T=850/5{,}5+850/2{,}9\approx447{,}65\ \mathrm s','Använd oavrundade deltider.'),st(T,r'T_0=1700/4{,}2\approx404{,}76\ \mathrm s','Utan ström hålls farten 4,2 m/s på båda sträckorna.'),st('Jämför tiderna',r'T-T_0\approx42{,}89\ \mathrm s')],'Turen tar cirka 43 s längre med ström. Förlusten motströms är större än vinsten medströms.')])
parts('3.236',[
 plan([st(T,r't_{\mathrm{mål}}=180/100=1{,}8\ \mathrm h'),st(r'Återstående tid: \(t_2=t_{\mathrm{mål}}-t_1-t_{\mathrm{stopp}}\)',r't_2=1{,}8-90/90-12/60=0{,}6\ \mathrm h','Stoppet måste räknas med i hela resan.'),st(F,r'v_2=90/0{,}6=150\ \mathrm{km/h}')],a(r'150\ \mathrm{km/h}')),
 plan([st(r'Kortaste totaltid: \(T=t_1+t_{\mathrm{stopp}}+t_2\)',r'\begin{aligned}T&=90/90+12/60+90/120\\&=1{,}95\ \mathrm h\end{aligned}','Största tillåtna fart på sista delen ger kortast tid och därmed störst medelfart.'),st(F,r'v_m=180/1{,}95\approx92{,}3\ \mathrm{km/h}')],a(r'92{,}3\ \mathrm{km/h}'))])
single('3.126',[st(r'Tid i timmar: \(1\ \mathrm{min}=1/60\ \mathrm h\)',r't=2+50/60=17/6\ \mathrm h'),st(F,r'v_m=340/(17/6)=120\ \mathrm{km/h}')],a(r'120\ \mathrm{km/h}'))
parts('3.127',[
 plan([st(KM,r's=20200\cdot1000=20200000\ \mathrm m','Mottagaren ligger rakt under satelliten, så signalsträckan är den angivna höjden.'),st(T,r't=\frac{20200000}{3{,}00\cdot10^8}\approx0{,}067333\ \mathrm s'),st(r'Tidsprefix: \(1\ \mathrm s=1000\ \mathrm{ms}\)',r't\approx67{,}3\ \mathrm{ms}')],a(r'67{,}3\ \mathrm{ms}')),
 plan([st(r'Tidsprefix: \(1\ \mathrm{\mu s}=10^{-6}\ \mathrm s\)',r'\Delta t=1{,}0\cdot10^{-6}\ \mathrm s'),st(r'Avståndsfel: \(|\Delta s|=c|\Delta t|\)',r'|\Delta s|=3{,}00\cdot10^8\cdot10^{-6}=300\ \mathrm m','Det här är felets storlek för en enkel signalväg, inte ett eko.')],a(r'300\ \mathrm m'))])
parts('3.128',[
 one(F,r'v_m=200/19{,}8\approx10{,}1\ \mathrm{m/s}',r'10{,}1\ \mathrm{m/s}'),
 one(U,r'v_m=(200/19{,}8)\cdot3{,}6\approx36{,}4\ \mathrm{km/h}',r'36{,}4\ \mathrm{km/h}','Använd den oavrundade medelfarten vid enhetsbytet.'),
 plan([st(F,'','Medelfarten omfattar hela loppet, även accelerationen från vila. Under delar av loppet är farten lägre än 11,5 m/s.')],'Hon håller inte toppfarten hela tiden. Därför blir medelfarten lägre än 11,5 m/s.')])
parts('3.129',[
 one(KM,r's=(3{,}0+2{,}0)\cdot1000=5000\ \mathrm m',r'5000\ \mathrm m'),
 one(MIN,r't=(15+20)\cdot60=2100\ \mathrm s',r'2100\ \mathrm s'),
 one(F,r'v_m=\frac{(3+2)\cdot1000}{(15+20)\cdot60}\approx2{,}38\ \mathrm{m/s}',r'2{,}38\ \mathrm{m/s}','Använd hela sträckan och hela tiden. Ett vanligt medelvärde av etappernas farter ger inte rätt viktning.')])
single('3.130',[st(E,r's=2d=2\cdot85=170\ \mathrm m','Ljudet går till väggen och tillbaka.'),st(F,r'v=170/0{,}50=340\ \mathrm{m/s}')],a(r'340\ \mathrm{m/s}'))
parts('3.131',[
 one(T,r't=240/3{,}0=80\ \mathrm s',r'80\ \mathrm s','Strömmen är parallell med stranden. Den ändrar inte fartkomponenten mot andra stranden, som här är 3,0 m/s.'),
 plan([st(T,r't=240/3{,}0=80\ \mathrm s'),st(S,r's_{\mathrm{ned}}=1{,}2\cdot80=96\ \mathrm m','Strömmen för färjan nedströms under hela överresan.')],a(r'96\ \mathrm m')),
 plan([st(r'Uppströmskomponent: \(v\sin\alpha=u\)',r'3{,}0\sin\alpha=1{,}2','Vinkeln mäts från riktningen vinkelrätt mot stranden. Båtens uppströmskomponent ska ta ut strömmen.'),st('Lös ut vinkeln',r'\alpha=\arcsin(1{,}2/3{,}0)\approx23{,}6^\circ')],a(r'23{,}6^\circ\text{ uppströms}')),
 plan([st(r'Vinkelräta komponenter: \(v_\perp^2+u^2=v^2\)',r'v_\perp=\sqrt{3{,}0^2-1{,}2^2}\ \mathrm{m/s}','En del av farten genom vattnet används nu för att motverka strömmen.'),st(T,r't=\frac{240}{\sqrt{3{,}0^2-1{,}2^2}}\approx87{,}3\ \mathrm s')],a(r'87{,}3\ \mathrm s'))])
parts('3.237',[
 plan([st(F,r'\begin{aligned}v_A&=500{,}0/42{,}380\approx11{,}7980\ \mathrm{m/s}\\v_B&=500{,}0/42{,}410\approx11{,}7897\ \mathrm{m/s}\end{aligned}','Anta i denna del samma sträcka, 500,0 m. Behåll extra siffror eftersom skillnaden är liten.')],'A: cirka 11,7980 m/s. B: cirka 11,7897 m/s.'),
 plan([st(r'Tidsskillnad: \(\Delta t=t_B-t_A\)',r'\Delta t=42{,}410-42{,}380=0{,}030\ \mathrm s'),st(S,r'\Delta s=\frac{500{,}0}{42{,}380}\cdot0{,}030\approx0{,}354\ \mathrm m','Vid samma fart som A måste den extra tiden bero på extra sträcka.')],a(r'0{,}354\ \mathrm m\text{ längre}')),
 plan([st(S,r'\Delta s=\frac{500{,}0}{42{,}380}\cdot0{,}030\approx0{,}354\ \mathrm m'),st('Jämför med inmätningens gräns',r'0{,}354\ \mathrm m\gt0{,}20\ \mathrm m')],'Nej. Det skulle krävas cirka 0,354 m, mer än den tillåtna skillnaden 0,20 m.')])
parts('3.132',[
 one(S,r'\begin{aligned}s&=2{,}998\cdot10^8\cdot3{,}156\cdot10^7\\&\approx9{,}462\cdot10^{15}\ \mathrm m\end{aligned}',r'9{,}462\cdot10^{15}\ \mathrm m','Ett ljusår är den sträcka ljuset färdas på ett år. Tabellen ger ungefär 3,156 · 10⁷ s per år och c ≈ 2,998 · 10⁸ m/s.'),
 plan([st(T,r't=\frac{2{,}5\cdot10^{11}}{2{,}998\cdot10^8}\ \mathrm s'),st(MIN,r't=\frac{2{,}5\cdot10^{11}}{2{,}998\cdot10^8\cdot60}\approx13{,}9\ \mathrm{min}','Detta är tiden åt ett håll. Ett svar tillbaka tar ytterligare ungefär lika lång tid.')],a(r'13{,}9\ \mathrm{min}'))])
parts('3.133',[
 plan([st(F,r'\begin{aligned}v_1&=30/4{,}20\approx7{,}14\ \mathrm{m/s}\\v_2&=30/2{,}70\approx11{,}1\ \mathrm{m/s}\\v_3&=40/3{,}80\approx10{,}5\ \mathrm{m/s}\end{aligned}','Använd tiden för just respektive delsträcka. Den sista sträckan är 40 m, inte 30 m.')],'Cirka 7,14 m/s, 11,1 m/s och 10,5 m/s i ordning.'),
 plan([st(r'Total tid: \(T=t_1+t_2+t_3\)',r'T=4{,}20+2{,}70+3{,}80=10{,}70\ \mathrm s'),st(F,r'v_m=100/10{,}70\approx9{,}35\ \mathrm{m/s}')],a(r'9{,}35\ \mathrm{m/s}')),
 plan([st(F,r'30/2{,}70\gt40/3{,}80\gt30/4{,}20','Jämför delarnas medelfarter. På första delen ingår accelerationen från vila.')],'Snabbast mellan 30 och 60 m. Starten från vila gör första delens medelfart lägre.')])
parts('3.134',[
 one(F,r'v_m=210/7{,}0=30\ \mathrm{m/s}',r'30\ \mathrm{m/s}'),
 one(U,r'v_m=(210/7{,}0)\cdot3{,}6=108\ \mathrm{km/h}',r'108\ \mathrm{km/h}'),
 one(r'Fartkvot: \(v_{\mathrm{gepard}}/v_{\mathrm{bil}}\)',r'\frac{(210/7{,}0)\cdot3{,}6}{90}=1{,}2',r'1{,}2','Skriv båda farterna i samma enhet. Kvoten saknar enhet; gepardens medelfart är 20 % högre.')])
parts('3.238',[
 plan([st(r'Ljudets väg: \(ct=D+(D-ut)\)',r'2D=(c+u)t','Ljudet går D till väggen. När det når personen har personen gått ut närmare väggen, så retursträckan är D − ut.'),st('Lös ut startavståndet',r'D=\frac{(340+2{,}0)\cdot0{,}600}{2}=102{,}6\ \mathrm m')],a(r'102{,}6\ \mathrm m')),
 one(E,r'D_0=340\cdot0{,}600/2=102{,}0\ \mathrm m',r'102{,}0\ \mathrm m','Om personen felaktigt antas stå stilla blir retursträckan lika lång som utsträckan. Resultatet blir 0,6 m för litet.'),
 plan([st(r'Ljudets väg: \(ct=2D-ut\)',r'ct+ut=2D\quad\Rightarrow\quad D=\frac{(c+u)t}{2}'),st(r'Kontroll av modellen: \(D-ut=(c-u)t/2\)',r'D-ut\gt0','Villkoret u < c gör att personen inte har nått väggen när ekot hörs.')],a(r'D=\frac{(c+u)t}{2}'))])
single('3.179',[st(S,r's=4{,}2t+5{,}6t=9{,}8t','Låt varje tidsperiod vara t sekunder.'),st(F,r'v_m=9{,}8t/(2t)=4{,}9\ \mathrm{m/s}','Här är tiderna lika långa. Därför fungerar det vanliga medelvärdet av de två farterna.')],a(r'4{,}9\ \mathrm{m/s}'))
# Chapter 2's applied speed questions: explicit plans, not transformations of old prose.
parts('2.291',[
 plan([st(KM,r's=25\cdot1000=25000\ \mathrm m'),st(T,r't=25000/1{,}5\ \mathrm s'),st(HOUR,r't=25000/(1{,}5\cdot3600)\approx4{,}6\ \mathrm h')],a(r'4{,}6\ \mathrm h')),
 one(T,r't=25/18\approx1{,}4\ \mathrm h',r'1{,}4\ \mathrm h','km delat med km/h ger timmar.'),
 plan([st(T,r't=25/70\ \mathrm h'),st(r'Tidsenhet: \(1\ \mathrm h=60\ \mathrm{min}\)',r't=(25/70)\cdot60\approx21{,}4\ \mathrm{min}')],a(r'21{,}4\ \mathrm{min}')),
 one(T,r't=25/0{,}69\approx36{,}2\ \mathrm s',r'36{,}2\ \mathrm s','Farten är i km/s och sträckan i km. Därför blir tiden direkt i sekunder.')])
parts('2.292',[
 one(S,r's=340\cdot4{,}60=1564\ \mathrm m',r'1564\ \mathrm m','När ljusets restid försummas är fördröjningen ljudets restid.'),
 plan([st(r'SI-enheter: \(1\ \mathrm{km}=1000\ \mathrm m\), \(1\ \mathrm{ms}=10^{-3}\ \mathrm s\)',r's=18000\ \mathrm m,\quad t=0{,}00013\ \mathrm s'),st(F,r'v=18000/0{,}00013\approx1{,}38\cdot10^8\ \mathrm{m/s}')],a(r'1{,}4\cdot10^8\ \mathrm{m/s}')),
 one(E,r'd=340\cdot0{,}20/2=34\ \mathrm m',r'34\ \mathrm m','Ljudet går till bytet och tillbaka. Avståndet är därför halva ljudsträckan.'),
 plan([st(E,r's=2\cdot50=100\ \mathrm m','Ekot färdas både ned och upp.'),st(r'Tidsprefix: \(1\ \mathrm{ms}=10^{-3}\ \mathrm s\)',r't=0{,}0665\ \mathrm s'),st(F,r'v=100/0{,}0665\approx1504\ \mathrm{m/s}')],a(r'1504\ \mathrm{m/s}'))])
parts('2.293',[
 plan([st(r'Tidsenhet: \(1\ \mathrm{min}=1/60\ \mathrm h\)',r't=17/60\ \mathrm h','Från 11.34 till 11.51 går 17 minuter.'),st(S,r's=110\cdot17/60\approx31{,}2\ \mathrm{km}')],a(r'31{,}2\ \mathrm{km}')),
 one(T,r't=(42{,}5/110)\cdot60\approx23{,}2\ \mathrm{min}',r'23{,}2\ \mathrm{min}','Kvoten i km och km/h ger timmar. Multiplicera med 60 för minuter.')])
parts('2.294',[
 plan([st(U,r'v=145/3{,}6\ \mathrm{m/s}'),st(T,r't=15/(145/3{,}6)\approx0{,}37\ \mathrm s')],a(r'0{,}37\ \mathrm s')),
 plan([st(T,r't=25/(100/3{,}6)=0{,}90\ \mathrm s','Beräkna först bollens restid. Spelaren har samma tid på sig.'),st(F,r'v=7{,}32/0{,}90\approx8{,}1\ \mathrm{m/s}')],a(r'8{,}1\ \mathrm{m/s}')),
 plan([st(r'Relativ fart åt samma håll: \(v_{\mathrm{rel}}=v_g-v_z\)',r'v_{\mathrm{rel}}=28-16=12\ \mathrm{m/s}','Avståndet minskar med 12 m varje sekund.'),st(T,r't=35/12\approx2{,}9\ \mathrm s')],a(r'2{,}9\ \mathrm s')),
 plan([st(r'Längdprefix: \(1\ \mathrm{mm}=10^{-3}\ \mathrm m\)',r'v=0{,}0075\ \mathrm{m/s}'),st(T,r't=20/0{,}0075\ \mathrm s'),st(MIN,r't=20/(0{,}0075\cdot60)\approx44{,}4\ \mathrm{min}')],a(r'44\ \mathrm{min}'))])
parts('2.295',[
 one(T,r't_A=(10/18)\cdot60\approx33{,}3\ \mathrm{min}',r'33{,}3\ \mathrm{min}','Beräkna tiden i timmar och omvandla till minuter.'),
 plan([st(r'Stinas tid: \(t_S=t_A-\Delta t_{\mathrm{start}}-\Delta t_{\mathrm{mål}}\)',r't_S=10/18-5/60=17/36\ \mathrm h','Senare start och tidigare målgång gör körtiden 2 + 3 = 5 minuter kortare.'),st(F,r'v_S=10/(17/36)\approx21{,}2\ \mathrm{km/h}')],a(r'21{,}2\ \mathrm{km/h}'))])
single('2.296',[st(r'Cykeltid: \(t=t_{\mathrm{borta}}-t_{\mathrm{stopp}}\)',r't=(50-15)/60=35/60\ \mathrm h'),st(T,r'd/12+d/9=35/60','Låt d vara avståndet till affären i km. De båda cykeltiderna ska tillsammans bli 35 minuter.'),st('Lös ut avståndet',r'd=\frac{35/60}{1/12+1/9}=3{,}0\ \mathrm{km}')],a(r'3{,}0\ \mathrm{km}'))
parts('2.297',[
 plan([st(r'Fartskillnad: \(v_{\mathrm{rel}}=v_1-v_2\)',r'v_{\mathrm{rel}}=(106-98)/3{,}6\ \mathrm{m/s}','Bilarna kör åt samma håll.'),st(T,r't=186/(8/3{,}6)=83{,}7\ \mathrm s')],a(r'83{,}7\ \mathrm s')),
 plan([st(r'Mötestid: \(t=d/(v_I+v_G)\)',r't=27/(15+18)=27/33\ \mathrm h','Avståndet minskar med summan av farterna.'),st(S,r's_I=15\cdot27/33\approx12{,}3\ \mathrm{km}')],'Cirka 12,3 km från Ines startpunkt.'),
 plan([st(r'Mötesfart: \(v_{\mathrm{rel}}=v_1+v_2\)',r'v_{\mathrm{rel}}=(78+85)/3{,}6\ \mathrm{m/s}'),st(T,r't=186/(163/3{,}6)\approx4{,}1\ \mathrm s')],a(r'4{,}1\ \mathrm s'))])
single('2.298',[st(r'Antal hundrameterssträckor: \(N=s/100\)',r'N=42000/100=420','Anta samma medelfart under hela maratonloppet.'),st(r'Total tid: \(t=N\cdot24\)',r't=420\cdot24=10080\ \mathrm s'),st(HOUR,r't=10080/3600=2{,}8\ \mathrm h')],a(r'2{,}8\ \mathrm h'))
parts('2.299',[
 plan([st(S,r'\begin{aligned}s_1&=6{,}7\cdot15\cdot60=6030\ \mathrm m\\s_2&=8{,}2\cdot12\cdot60=5904\ \mathrm m\end{aligned}','Skriv båda tiderna i sekunder.'),st(r'Total sträcka: \(s=s_1+s_2\)',r's=6030+5904=11934\ \mathrm m')],a(r'11934\ \mathrm m')),
 plan([st(MIN,r't=35\cdot60=2100\ \mathrm s'),st(F,r'v_m=11934/2100\approx5{,}7\ \mathrm{m/s}')],a(r'5{,}7\ \mathrm{m/s}'))])
parts('2.300',[
 plan([st(T,r'\begin{aligned}t_F&=400/(12/3{,}6)=120\ \mathrm s\\t_R&=400/(15/3{,}6)=96\ \mathrm s\end{aligned}'),st(r'Startfördröjning: \(\Delta t=t_F-t_R\)',r'\Delta t=120-96=24\ \mathrm s','Rita har kortare löptid och måste därför börja senare.')],'Rita startar 24 s efter Frida.'),
 plan([st(T,r't=400/(15/3{,}6)=96\ \mathrm s','Vid samtidig start är tiden fram till mål Ritas löptid.'),st(S,r's_F=(12/3{,}6)\cdot96=320\ \mathrm m'),st(r'Försprång: \(d=400-s_F\)',r'd=400-320=80\ \mathrm m')],'Frida ska starta 80 m framför Rita.')])
# Graphical solutions for the seven non-linear speed equations. Coordinates are
# evaluated from the explicitly supplied time model, never from answer text.
def timegraph(fn,target,root,xmin,xmax,ymax,xticks,yticks,difference=False):
 def X(x):return 48+300*(x-xmin)/(xmax-xmin)
 def Y(y):return 205-165*y/ymax
 def fmt(x):return f'{x:g}'.replace('.',',')
 svg='<svg viewBox="0 0 400 270" style="max-width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tid som funktion av fart. Skärning vid '+fmt(root)+' kilometer per timme."><rect width="400" height="270" fill="white"/><g font-family="Arial,sans-serif" font-size="12" fill="#172a3a">'
 for x in xticks:svg+=f'<path d="M{X(x):.2f} 40V205" stroke="#dce3e9"/><text x="{X(x):.2f}" y="224" text-anchor="middle">{fmt(x)}</text>'
 for y in yticks:svg+=f'<path d="M48 {Y(y):.2f}H348" stroke="#dce3e9"/><text x="40" y="{Y(y)+4:.2f}" text-anchor="end">{fmt(y)}</text>'
 svg+='<path d="M48 38V205H350" fill="none" stroke="#172a3a" stroke-width="1.5"/><text x="48" y="20">Tid (h)</text><text x="348" y="243" text-anchor="end">Fart (km/h)</text>'
 pts=[]
 for j in range(401):
  x=xmin+(xmax-xmin)*j/400;y=fn(x)
  if 0<=y<=ymax:pts.append(f'{X(x):.2f},{Y(y):.2f}')
 svg+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="#176b99" stroke-width="2.2"/><path d="M48 {Y(target):.2f}H348" stroke="#b44b19" stroke-width="2"/><circle cx="{X(root):.2f}" cy="{Y(target):.2f}" r="4" fill="#172a3a"/><text x="{X(root)+7:.2f}" y="{Y(target)-8:.2f}">{fmt(root)}</text><text x="48" y="263" fill="#176b99">Blå: beräknad tid</text><text x="215" y="263" fill="#b44b19">Orange: given tid</text></g></svg>'
 if difference:svg=svg.replace('Tid (h)','Tidsskillnad (h)')
 return '<span class="fig">'+svg+'</span>'
def graphical(eq,fn,target,root,xmin,xmax,ymax,xticks,yticks,check,difference=False):
 return ('Lös ekvationen grafiskt',p('Rita vänsterledets tidsfunktion och den vågräta linjen '+inline('y='+('4/3' if target==4/3 else str(target).replace('.', '{,}')))+'. Skärningens x-värde ger farten i km/h. Använd bara det tillåtna intervallet för farten.')+m(eq)+timegraph(fn,target,root,xmin,xmax,ymax,xticks,yticks,difference)+m(check))
parts('2.301',[
 plan([st(T,r'd/72-d/80=2/60','Låt d vara sträckan i km. Tidsvinsten ska bli 2 minuter.'),st('Samla faktorn framför sträckan',r'\begin{aligned}d(1/72-1/80)&=1/30\\d/720&=1/30\\d&=24\ \mathrm{km}\end{aligned}')],a(r'24\ \mathrm{km}')),
 one(T,r'\Delta t=(80/90-80/95)\cdot60\approx2{,}8\ \mathrm{min}',r'2{,}8\ \mathrm{min}','Subtrahera den snabbare resans tid från den långsammare. Omvandla timmar till minuter.'),
 plan([st(T,r'\frac{240}{v}-\frac{240}{v+20}=1','Låt v > 0 vara det långsammare tågets fart i km/h. Skillnaden i restid är 1 h.'),graphical(r'y=240/x-240/(x+20)',lambda x:240/x-240/(x+20),1,60,20,120,5,[20,40,60,80,100,120],[0,1,2,3,4,5],r'240/60-240/80=4-3=1\ \mathrm h',difference=True)],a(r'60\ \mathrm{km/h}')),
 plan([st(S,r'5v=4(v+18)','Samma sträcka körs på 5 h respektive 4 h. Låt v vara den lägre farten i km/h.'),st('Lös ekvationen',r'5v=4v+72\quad\Rightarrow\quad v=72\ \mathrm{km/h}')],a(r'72\ \mathrm{km/h}'))])
single('2.302',[st(S,r'0{,}850t=1{,}25(t-5{,}00)','Låt t vara tiden efter första kulans start. Den andra kulan rullar bara under t − 5,00 s. Vid kollisionen är sträckorna lika.'),st('Lös ut tiden',r'\begin{aligned}0{,}400t&=6{,}25\\t&=15{,}625\ \mathrm s\end{aligned}'),st(S,r's=0{,}850\cdot15{,}625\approx13{,}3\ \mathrm m')],a(r'13{,}3\ \mathrm m'))
parts('2.303',[
 plan([st(T,r'\frac3{v-3}+\frac3{v+3}=\frac43','Låt v vara farten genom vattnet i km/h, med v > 3. Tiden 1 h 20 min är 4/3 h. Motströms är farten v − 3, medströms v + 3.'),graphical(r'y=3/(x-3)+3/(x+3)',lambda x:3/(x-3)+3/(x+3),4/3,6,3.2,12,4,[4,6,8,10,12],[0,1,2,3,4],r'\begin{aligned}3/(6-3)+3/(6+3)&=1+1/3\\&=4/3\ \mathrm h\end{aligned}')],a(r'6{,}0\ \mathrm{km/h}')),
 plan([st(T,r'\frac{750}{v-50}+\frac{750}{v+50}=8','Låt v > 50 vara planets fart genom luften i km/h. Markfarten minskar mot vinden och ökar med vinden.'),graphical(r'y=750/(x-50)+750/(x+50)',lambda x:750/(x-50)+750/(x+50),8,200,60,400,20,[100,200,300,400],[0,4,8,12,16,20],r'750/150+750/250=5+3=8\ \mathrm h')],a(r'200\ \mathrm{km/h}')),
 plan([st(T,r'\frac{30}{v+2}+\frac{30}{v-2}=8','Låt v > 2 vara farten genom vattnet i km/h. Addera de båda restiderna.'),graphical(r'y=30/(x+2)+30/(x-2)',lambda x:30/(x+2)+30/(x-2),8,8,2.5,16,20,[4,8,12,16],[0,4,8,12,16,20],r'30/10+30/6=3+5=8\ \mathrm h')],a(r'8{,}0\ \mathrm{km/h}'))])
single('2.304',[st(T,r't_{\mathrm{luft}}=5{,}00/340\ \mathrm s'),st(r'Järnets restid: \(t_j=t_{\mathrm{luft}}-\Delta t\)',r't_j=5{,}00/340-0{,}0137\ \mathrm s','Ljudet genom järnet kommer först. Dra därför bort 13,7 ms från luftens restid.'),st(F,r'v_j=\frac{5{,}00}{5{,}00/340-0{,}0137}\approx4971\ \mathrm{m/s}','Behåll oavrundade tider, eftersom differensen är liten.')],a(r'4{,}97\cdot10^3\ \mathrm{m/s}'))
parts('2.305',[
 plan([st(T,r'\frac d4+4=\frac{d+36}{6}','Låt d vara avståndet till bilen. Oskar behöver sin löptid plus 4 s. Björnen ska springa d + 36 m.'),st('Multiplicera med 12 och lös ekvationen',r'\begin{aligned}3d+48&=2d+72\\d&=24\ \mathrm m\end{aligned}'),st(T,r'24/4+4=10\ \mathrm s,\quad60/6=10\ \mathrm s','Kontroll: båda tiderna blir 10 s.')],a(r'24\ \mathrm m')),
 one(E,r'd=1500\cdot0{,}30/2=225\ \mathrm m',r'225\ \mathrm m','Ekot färdas till fiskstimmet och tillbaka.')])
parts('2.306',[
 one(r'Isärgående rörelse: \(t=d/(v_1+v_2)\)',r't=\frac{1{,}0}{2{,}4\cdot10^5+6{,}7\cdot10^6}\approx1{,}4\cdot10^{-7}\ \mathrm s',r'1{,}4\cdot10^{-7}\ \mathrm s','Åt motsatta håll ökar avståndet med summan av farterna.'),
 plan([st(S,r'38t=32(t+5/60)','Låt t vara Olles körtid i timmar. Kalle har kört fem minuter längre. Vid upphinnandet är sträckorna lika.'),st('Lös ut Olles tid',r'\begin{aligned}6t&=8/3\\t&=4/9\ \mathrm h\\t&=(4/9)\cdot60\approx26{,}7\ \mathrm{min}\end{aligned}')],'Cirka 26,7 min efter Olles start.'),
 plan([st(S,r'38t=32(t+5/60)\quad\Rightarrow\quad t=4/9\ \mathrm h','Återanvänd den oavrundade tiden efter Olles start.'),st(S,r's=38\cdot4/9\approx16{,}9\ \mathrm{km}')],a(r'16{,}9\ \mathrm{km}'))])
parts('2.307',[
 plan([st(S,r'4{,}2t+5(t-300)=3000','Låt t vara sekunder efter 10.00. B springer under t − 300 s. Åt motsatta håll adderas sträckorna.'),st('Lös ut tiden och omvandla till minuter',r'\begin{aligned}9{,}2t&=4500\\t&=4500/9{,}2\ \mathrm s\\t/60&\approx8{,}2\ \mathrm{min}\end{aligned}')],'Cirka 8,2 min efter 10.00.'),
 plan([st(S,r'4{,}2t-5(t-300)=1000','A:s sträcka är 1000 m längre än B:s. t mäts från 10.00 och ska vara minst 300 s.'),st('Lös ut tiden',r'\begin{aligned}1500-0{,}8t&=1000\\t&=625\ \mathrm s\\t/60&\approx10{,}4\ \mathrm{min}\end{aligned}')],'Cirka 10,4 min efter 10.00.'),
 plan([st(S,r'5(t-300)-4{,}2t=1000','Nu är B:s sträcka 1000 m längre än A:s. Samma tidsstart 10.00 används.'),st('Lös ut tiden',r'\begin{aligned}0{,}8t&=2500\\t&=3125\ \mathrm s\\t/60&\approx52{,}1\ \mathrm{min}\end{aligned}')],'Cirka 52,1 min efter 10.00.')])
parts('2.308',[
 one(T,r't=10{,}0/12+10{,}0/8{,}5\approx2{,}01\ \mathrm s',r'2{,}0\ \mathrm s','Pucken färdas 10 m åt varje håll. Addera tiderna, inte farterna.'),
 plan([st(r'Cirkelns omkrets: \(C=2\pi r\)',r'C=2\pi\cdot4200\ \mathrm m','Radien 4,20 km är 4200 m.'),st(r'Antal varv: \(N=ct/C\)',r'N=\frac{3{,}00\cdot10^8\cdot1{,}00}{2\pi\cdot4200}\approx11368')],'Cirka 11 400 varv.')])
single('2.309',[st(T,r't_A=360/85\ \mathrm h,\quad t_S=1+360/102\ \mathrm h','Räkna båda ankomsttiderna från 08.00. Sanna startar en timme senare.'),st(r'Väntetid: \(\Delta t=t_S-t_A\)',r'\begin{aligned}\Delta t&=(1+360/102-360/85)\cdot60\\&\approx17{,}65\ \mathrm{min}\end{aligned}')],a(r'18\ \mathrm{min}'))
parts('2.310',[
 plan([st(S,r'1{,}5v+\frac{70}{60}(v+12)=90','Låt v vara första båtens fart i km/h. Första båten kör i 90 min och andra i 70 min. Åt motsatta håll adderas sträckorna.'),st('Samla termerna och lös ut farten',r'\begin{aligned}\frac83v+14&=90\\v&=76\cdot\frac38=28{,}5\ \mathrm{km/h}\end{aligned}')],a(r'28{,}5\ \mathrm{km/h}')),
 plan([st(S,r'85t=95(t-1)','Låt t vara timmar efter Pelles start. Tove har kört en timme kortare. Vid upphinnandet är sträckorna lika.'),st('Lös ut tiden',r'10t=95\quad\Rightarrow\quad t=9{,}5\ \mathrm h')],'9,5 h efter Pelles start.'),
 one(T,r'\begin{aligned}t_{\mathrm{stopp}}&=(85/80-30/70-55/95)\cdot60\\&\approx3{,}3\ \mathrm{min}\end{aligned}',r'3{,}3\ \mathrm{min}','Wendys hela restid är också Alfs hela restid. Dra bort Alfs båda körtider för att få stoppet.')])
single('2.311',[st(r'Mötesfart: \(v_s+v_l=d/t\)',r'v_s+v_l=1000/0{,}00045','Avståndet är 1000 m och tiden 0,00045 s. Partiklarna rör sig mot varandra.'),st(r'Fartskillnad: \(v_s-v_l=1{,}2\cdot10^6\)',r'v_l=\frac{1000/0{,}00045-1{,}2\cdot10^6}{2}','Subtrahera skillnaden från summan. Då återstår två gånger den långsammare farten.'),st(S,r'\begin{aligned}s_l&=\frac{1000-1{,}2\cdot10^6\cdot0{,}00045}{2}\\&=230\ \mathrm m\end{aligned}')],'230 m från den långsammare partikelns start.')
parts('2.312',[
 one(E,r'L=343{,}0\cdot0{,}02332/2=3{,}99938\ \mathrm m',r'3{,}999\ \mathrm m','23,32 ms är 0,02332 s. Ljudet går rörets längd två gånger.'),
 one(E,r'v=\frac{2\cdot3{,}99938}{0{,}02993}\approx267\ \mathrm{m/s}',r'267\ \mathrm{m/s}','29,93 ms är 0,02993 s. Hela ljudsträckan är 2L.'),
 one(E,r't=\frac{2\cdot3{,}99938}{1304}\approx0{,}006134\ \mathrm s',r'0{,}006134\ \mathrm s','Tiden avser ljudets resa tur och retur.')])
single('2.313',[st(T,r'\begin{aligned}t_A&=1500/4{,}0+500/3{,}1\\t_B&=1200/3{,}6+800/3{,}9\end{aligned}','Hela banan är 2000 m. Återstående sträckor är 500 m för A och 800 m för B.'),st('Addera deltiderna och jämför',r't_A\approx536{,}29\ \mathrm s,\quad t_B\approx538{,}46\ \mathrm s'),st(r'Tidsvinst: \(\Delta t=t_B-t_A\)',r'\Delta t\approx2{,}17\ \mathrm s','Subtrahera med oavrundade tider. A har den kortare tiden.')],'Båt A vinner med cirka 2,2 s.')
parts('2.314',[
 one(T,r'\Delta t=(5/12-5/14{,}5)\cdot60\approx4{,}3\ \mathrm{min}',r'4{,}3\ \mathrm{min}','Bertil är snabbare. Subtrahera hans tid från Karls och omvandla timmar till minuter.'),
 plan([st(T,r't_K=8/14\ \mathrm h','När Karl går i mål har båda sprungit lika länge.'),st(S,r's_B=11\cdot8/14\ \mathrm{km}'),st(r'Återstående sträcka: \(s_{\mathrm{kvar}}=8-s_B\)',r's_{\mathrm{kvar}}=8-11\cdot8/14\approx1{,}7\ \mathrm{km}')],a(r'1{,}7\ \mathrm{km}'))])
parts('2.315',[
 plan([st(T,r'\frac{120}{v-10}-\frac{120}{v}=2','Låt v > 10 vara farten dit i km/h. Hemfärden går långsammare och tar två timmar längre.'),graphical(r'y=120/(x-10)-120/x',lambda x:120/(x-10)-120/x,2,30,12,60,8,[20,30,40,50,60],[0,2,4,6,8],r'120/20-120/30=6-4=2\ \mathrm h',difference=True)],a(r'30\ \mathrm{km/h}')),
 plan([st(T,r'\frac{150}{v}-\frac{150}{v+5}=1{,}5','Låt v > 0 vara ursprungsfarten i km/h. Den högre farten ger kortare restid.'),graphical(r'y=150/x-150/(x+5)',lambda x:150/x-150/(x+5),1.5,20,5,45,6,[10,20,30,40],[0,1.5,3,4.5,6],r'150/20-150/25=7{,}5-6=1{,}5\ \mathrm h',difference=True)],a(r'20\ \mathrm{km/h}')),
 plan([st(T,r'\frac{140}{v}-\frac{152}{v+20}=0{,}5','Låt v > 0 vara Haralds fart i km/h. Harald kör totalt 140 km och Lisa 152 km. Lisa kommer hem en halvtimme tidigare.'),graphical(r'y=140/x-152/(x+20)',lambda x:140/x-152/(x+20),.5,56,20,100,4,[20,40,56,80,100],[0,.5,1,2,3,4],r'140/56-152/76=2{,}5-2=0{,}5\ \mathrm h',difference=True)],a(r'56\ \mathrm{km/h}'))])
for id in ['2.301','2.303','2.315']:byid[id]['geogebra']=True
parts('2.316',[
 plan([st(S,r'1{,}5(v+10)+v=115','Låt v vara Öyvinds fart i km/h. Kristoffer kör 10 km/h snabbare. Sträckorna ska tillsammans bli 115 km.'),st('Lös ut den lägre farten',r'2{,}5v=100\quad\Rightarrow\quad v=40\ \mathrm{km/h}'),st(S,r's_K=1{,}5(40+10)=75\ \mathrm{km}')],'75 km från Kristoffers hem.'),
 plan([st(S,r'\frac{25}{60}v=\frac{15}{60}(v+5)','Låt v vara gångfarten i km/h. Båda färdsätten gäller samma sträcka. Skriv minuterna i timmar.'),st('Multiplicera med 60 och lös ut farten',r'\begin{aligned}25v&=15v+75\\10v&=75\\v&=7{,}5\ \mathrm{km/h}\end{aligned}')],a(r'7{,}5\ \mathrm{km/h}')),
 plan([st(S,r'2v+2{,}5\cdot1{,}75v=255','Låt v vara den lägre farten i km/h. Summan av delsträckorna är 255 km.'),st('Samla termerna med farten',r'6{,}375v=255\quad\Rightarrow\quad v=40\ \mathrm{km/h}')],a(r'40\ \mathrm{km/h}')),
 plan([st(T,r's/80+1=s/60','Låt s vara sträckan i km. Körtid plus stopp är hela tiden; medelfarten 60 km/h ger samma totaltid.'),st('Samla termerna med sträckan',r'\begin{aligned}1&=s(1/60-1/80)\\1&=s/240\\s&=240\ \mathrm{km}\end{aligned}')],a(r'240\ \mathrm{km}'))])
parts('2.317',[
 plan([st(r'Farter med och mot ström: \(v_\pm=v\pm u\)',r'v+u=s/8,\quad v-u=s/12','Låt sträckan vara s km, båtens fart genom vattnet v och strömmens fart u, båda i km/h.'),st('Addera för att få båtens egen fart',r'2v=s/8+s/12\quad\Rightarrow\quad v=5s/48'),st(T,r't=s/(5s/48)=48/5=9{,}6\ \mathrm h')],a(r'9{,}6\ \mathrm h')),
 plan([st(r'Farter med och mot ström: \(v_\pm=v\pm u\)',r'v+u=s/6,\quad v-u=s/8','Låt v vara laxens fart genom vattnet och u strömmens fart, i km/h. Sträckan s är densamma.'),st('Subtrahera för att få strömmens fart',r'\begin{aligned}2u&=s/6-s/8=s/24\\u&=s/48\end{aligned}'),st(T,r't=s/(s/48)=48\ \mathrm h','Ett drivande föremål rör sig med strömmens fart.')],a(r'48\ \mathrm h')),
 plan([st(r'Mötesfart: \(v_{\mathrm{rel}}=v_1+v_2\)',r'v_{\mathrm{rel}}=(72+32{,}4)/3{,}6=29\ \mathrm{m/s}'),st(S,r'L=29\cdot10=290\ \mathrm m','Hela tågets längd passerar en enda passagerare. Den egna tåglängden ska inte läggas till.')],a(r'290\ \mathrm m')),
 plan([st(F,r'v+u=42/1{,}40=30\ \mathrm{km/h}'),st(F,r'v-u=42/1{,}68=25\ \mathrm{km/h}'),st(r'Addera ekvationerna: \(2v=v_++v_-\)',r'v=(30+25)/2=27{,}5\ \mathrm{km/h}','Medelvärdet här ger farten genom vattnet, inte medelfarten för turen.')],a(r'27{,}5\ \mathrm{km/h}'))])
parts('2.318',[
 plan([st(r'Farter relativt marken: \(v_\pm=v\pm u\)',r'v_+=3{,}65\ \mathrm{m/s},\quad v_-=2{,}35\ \mathrm{m/s}'),st(T,r'L/3{,}65+L/2{,}35=300','Fem minuter är 300 s. Låt L vara rullgångens längd i meter.'),st('Lös ut längden',r'L=\frac{300}{1/3{,}65+1/2{,}35}\approx429\ \mathrm m')],a(r'429\ \mathrm m')),
 plan([st(r'Mötesfart: \(v_{\mathrm{rel}}=v_1+v_2\)',r'v_{\mathrm{rel}}=(90+36)/3{,}6=35\ \mathrm{m/s}'),st(T,r't=24{,}0/35\approx0{,}69\ \mathrm s','Lastbilens hela längd ska passera en enda punkt, bilrutan.')],a(r'0{,}69\ \mathrm s')),
 plan([st(r'Samma riktning: \(v_{\mathrm{rel}}=v_b-v_f\)',r'v_{\mathrm{rel}}=(72-54)/3{,}6=5\ \mathrm{m/s}'),st(S,r'L=5\cdot60=300\ \mathrm m','Båten vinner en fartygslängd på 60 s. Båtens egen längd försummas.')],a(r'300\ \mathrm m')),
 plan([st(r'Relativ sträcka: \(s=L_1+L_2\)',r's=200+800=1000\ \mathrm m','För att hela tåget ska passera måste dess front vinna båda tågens sammanlagda längd.'),st(r'Samma riktning: \(v_{\mathrm{rel}}=v_1-v_2\)',r'v_{\mathrm{rel}}=(72-27)/3{,}6=12{,}5\ \mathrm{m/s}'),st(T,r't=1000/12{,}5=80\ \mathrm s')],a(r'80\ \mathrm s'))])
parts('2.319',[
 plan([st(S,r'40(t+1/6)=60t','Låt t vara polisens körtid i timmar. Den första bilen har 10 min = 1/6 h i försprång.'),st('Lös ut polisens körtid',r'20t=40/6\quad\Rightarrow\quad t=1/3\ \mathrm h'),st(S,r's=60\cdot1/3=20\ \mathrm{km}')],a(r'20\ \mathrm{km}')),
 plan([st(r'Fartskillnad: \(v_{\mathrm{rel}}=v_m-v_b\)',r'v_{\mathrm{rel}}=700-90=610\ \mathrm{km/h}'),st(T,r't=(5{,}0/610)\cdot3600\approx29{,}5\ \mathrm s','Beräkna tiden i timmar och omvandla till sekunder.')],a(r'30\ \mathrm s'))])
single('2.320',[st(U,r'u=40/3{,}6\ \mathrm{m/s}'),st(S,r'\ell=1500\cdot5{,}0=7500\ \mathrm m','Bojen sänder med fem sekunders mellanrum. Två efterföljande pulser ligger därför 7500 m från varandra i vattnet.'),st(r'Mottagningsintervall: \(\Delta t=\ell/(c+u)\)',r'\Delta t=\frac{7500}{1500+40/3{,}6}\approx4{,}963\ \mathrm s','Ubåten kör mot den kommande pulsen. Därför möts de med summan av farterna.'),st(S,r's=\frac{40}{3{,}6}\cdot\frac{7500}{1500+40/3{,}6}\approx55{,}1\ \mathrm m','Använd det oavrundade mottagningsintervallet.')],a(r'55{,}1\ \mathrm m'))
single('2.335',[st(r'Vägsträcka vid rörelse åt ett håll: \(s=x_{\mathrm{slut}}-x_{\mathrm{start}}\)',r's=180-100=80\ \mathrm m','Startpositionen 100 m är inte en färdad sträcka.'),st(F,r'v_m=80/40=2\ \mathrm{m/s}')],a(r'2\ \mathrm{m/s}'))
single('2.336',[st(r'Total sträcka: \(s=s_1+s_2\)',r's=240+360=600\ \mathrm m'),st(r'Total tid inklusive paus: \(T=t_1+t_p+t_2\)',r'T=(3+1+4)\cdot60=480\ \mathrm s'),st(F,r'v_m=600/480=1{,}25\ \mathrm{m/s}')],a(r'1{,}25\ \mathrm{m/s}'))
single('2.337',[st(r'Förflyttning: \(\Delta x=x_{\mathrm{slut}}-x_{\mathrm{start}}\)',r'\Delta x=50-20=+30\ \mathrm m','Vändningen påverkar vägsträckan men inte skillnaden mellan start- och slutposition.'),st(H,r'\bar v=30/30=+1\ \mathrm{m/s}')],a(r'+1\ \mathrm{m/s}'))
single('2.338',[st(r'Total vägsträcka: \(s=s_{\mathrm{ut}}+s_{\mathrm{hem}}\)',r's=20+20=40\ \mathrm m','Avläs att roboten kör 20 m framåt, står stilla och kör 20 m tillbaka.'),st(F,r'v_m=40/25=1{,}6\ \mathrm{m/s}','Även de fem sekunderna stillastående ingår i hela tiden 25 s.')],a(r'1{,}6\ \mathrm{m/s}'))
single('2.339',[st(r'Delsträcka och deltid: \(\Delta s=s_2-s_1\), \(\Delta t=t_2-t_1\)',r'\begin{aligned}\Delta s&=100-40=60\ \mathrm m\\\Delta t&=12-6=6\ \mathrm s\end{aligned}'),st(F,r'v_m=60/6=10\ \mathrm{m/s}','Frågan gäller bara sträckan mellan markeringarna, inte loppet från start.')],a(r'10\ \mathrm{m/s}'))
single('2.341',[st(r'Frontens sträcka: \(s=L_{\mathrm{bro}}+L_{\mathrm{tåg}}\)',r's=180+120=300\ \mathrm m','När bakänden lämnar bron har fronten hunnit en tåglängd förbi brons slut.'),st(U,r'v=54/3{,}6=15\ \mathrm{m/s}'),st(T,r't=300/15=20\ \mathrm s')],a(r'20\ \mathrm s'))
single('2.342',[st(r'Flygtid: \(T=t_{\mathrm{max}}-t_{\mathrm{mätning}}\)',r'T=(10-1)\cdot60=540\ \mathrm s'),st(T,r'd/6+d/4=540','Låt d vara avståndet till mätplatsen. Ut- och hemresa tar olika lång tid.'),st('Lös ut avståndet',r'5d/12=540\quad\Rightarrow\quad d=1296\ \mathrm m'),st(r'Kontroll: \(t_{\mathrm{ut}}+t_{\mathrm{mätning}}+t_{\mathrm{hem}}\)',r'1296/6+60+1296/4=600\ \mathrm s')],a(r'1296\ \mathrm m'))
single('2.345',[st(F,r'v_m=400/80=5{,}0\ \mathrm{m/s}'),st(H,r'\bar v=0/80=0\ \mathrm{m/s}','Leo kommer tillbaka till startpunkten. Förflyttningen är noll, medan vägsträckan är 400 m.')],'Medelfarten är 5,0 m/s och medelhastigheten är 0 m/s.')
single('2.347',[st('Hastighetsmätaren visar farten just nu','','Mätaren visar momentanfarten: hur snabbt bilen kör i det ögonblicket. Den visar varken medelfarten för hela resan eller rörelsens riktning.')],'Bilens fart just i det ögonblicket.')
single('2.350',[st(r'Tidsenhet: \(1\ \mathrm h=60\ \mathrm{min}\)',r't=30/60=0{,}50\ \mathrm h','Från 10.15 till 10.45 går 30 minuter.'),st(F,r'v_m=30/0{,}50=60\ \mathrm{km/h}')],a(r'60\ \mathrm{km/h}'))
if __name__=='__main__':
 expected={q['id'] for q in bank if q.get('omr')=='medelhastighet'}
 assert set(changes)==expected,expected-set(changes)
 save()
 print('Authored',len(changes),'main solutions and',sum(len(byid[i].get('spelDelar',[])) for i in changes),'cards')
