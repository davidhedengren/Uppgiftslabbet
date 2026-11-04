"""Individually authored facit for 48 ems tasks. No inferred prose/heading rewrites."""
from render import *
from ems_figures import graph
def st(h,tex='',why=''):return h,(p(why) if why else '')+(m(tex) if tex else '')
def sol(steps,answer):return steps,answer
def giv(t):return st('Givet och sökt',why=t)
def ohm(tex,why=''):return st(r'Ohms lag: \(U=RI\)',tex,why)
def inner(tex='',why=''):return st(r'Inre spänningsfall: \(U_r=rI\)',tex,why)
def pole(tex='',why=''):return st(r'Polspänning: \(U=\mathcal E-rI\)',tex,why)
def total(tex,why=''):return st(r'Ström i hela kretsen: \(I=\mathcal E/(R+r)\)',tex,why or 'Den inre och den yttre resistansen ligger i serie.')
def power(tex='',why=''):return st(r'Effekt i en resistor: \(P=I^2R\)',tex,why)
def hints(id,main,*cards):
 q=byid[id];q['ledtrad']=p(main)
 if cards:
  assert len(cards)==len(q.get('spelDelar',[])),id
  for d,h in zip(q['spelDelar'],cards):d['ledtrad']=p(h)

multi('8.2',[sol([st('Batteriet bidrar också med resistans',why='Ett verkligt batteri kan beskrivas med ems och en inre resistans r. Den ligger i samma strömväg som den yttre resistorn.'),total(r'I=\frac{9{,}0}{0{,}10+r}', 'När r är positiv är nämnaren större än 0,10 Ω. Strömmen blir därför mindre än 90 A.')],'Batteriets inre resistans begränsar också strömmen.')])
setq('8.207',[inner(r'U_r=0{,}2\cdot0{,}5=0{,}10\ \mathrm V'),pole(r'U=1{,}5-0{,}10=1{,}4\ \mathrm V','Batteriet levererar ström, så det inre spänningsfallet dras från ems.')],r'\(1{,}4\ \mathrm V\).')
setq('8.208',[inner(r'U_r=0{,}80\cdot0{,}25=0{,}20\ \mathrm V','Använd Ohms lag för just batteriets inre resistans.')],r'\(0{,}20\ \mathrm V\).')
setq('8.209',[pole(r'U_r=\mathcal E-U=4{,}5-4{,}2=0{,}30\ \mathrm V'),inner(r'r=\frac{0{,}30}{1}=0{,}30\ \Omega','Dividera det inre spänningsfallet med strömmen.')],r'\(0{,}30\ \Omega\).')
setq('8.210',[pole(r'U_r=\mathcal E-U=6{,}0-5{,}4=0{,}60\ \mathrm V'),inner(r'I=\frac{0{,}60}{0{,}30}=2{,}0\ \mathrm A')],r'\(2{,}0\ \mathrm A\).')
setq('8.211',[pole(r'I\approx0\quad\Rightarrow\quad rI\approx0','Utan belastning går i praktiken ingen ström. Då är också det inre spänningsfallet nära noll.')],'Polspänningen är ungefär lika med ems.')

# The first graph deliberately stops before the short-circuit intercept and does not label the answers to b/c.
a=sol([st('Placera mätpunkterna i ett koordinatsystem',why='Sätt strömmen I i ampere på x-axeln och polspänningen U i volt på y-axeln. Lägg in tabellens fyra punkter.'),st(r'Linjär anpassning: \(U=kI+m\)',why='Anpassa en rät linje, till exempel med GeoGebras linjära regression. Punkterna ligger på samma räta linje.'),('Rita den anpassade linjen',graph('line'))],'Se grafen: den anpassade linjen går genom alla fyra mätpunkterna.')
b=sol([st(r'Linjelutning: \(k=\Delta U/\Delta I\)',r'k=\frac{0{,}92-1{,}42}{1{,}50-0{,}25}=-0{,}40\ \mathrm{V/A}','Använd två punkter på den anpassade linjen.'),pole(r'r=-k=0{,}40\ \Omega','Modellens lutning är −r. Resistansen är alltså positiv även om lutningen är negativ.'),st(r'Skärning med U-axeln: \(\mathcal E=U+rI\)',r'\mathcal E=1{,}42+0{,}40\cdot0{,}25=1{,}52\ \mathrm V')],r'Ems är \(1{,}52\ \mathrm V\) och inre resistans \(0{,}40\ \Omega\).')
c=sol([pole(r'0=1{,}52-0{,}40I_k','Vid kortslutning är spänningen över den yttre kretsen noll.'),('Läs av skärningen med I-axeln',p('Förläng modellens linje till U = 0. Skärningen visar modellens kortslutningsström.')+graph('short')),st(r'Kontroll: \(I_k=\mathcal E/r\)',r'I_k=\frac{1{,}52}{0{,}40}=3{,}8\ \mathrm A')],r'Modellens kortslutningsström är \(3{,}8\ \mathrm A\).')
multi('8.10',[a,b,c])
hints('8.10','Vad betyder linjens lutning och skärningen med spänningsaxeln i batterimodellen?','Sätt ström på x-axeln och spänning på y-axeln. Vilken linje passar punkterna?','Jämför tecknet framför I i linjens ekvation med batterimodellen.','Vilken polspänning har en ideal kortslutning?')
setq('8.212',[pole(why='När batteriet levererar ström är rI positivt. Det inre spänningsfallet dras från ems för att få spänningen mellan batteriets poler.')],'Polspänningen är lägre än ems.')

# Optimize graphically; do not disclose the numerical maximum power before part b.
a=sol([total(r'I=\frac{1{,}5}{R+0{,}60}'),power(r'P_R(R)=\frac{1{,}5^2R}{(R+0{,}60)^2}','Det är effekten i den yttre resistorn som ska maximeras. Sätt in kretsens ström i I²R.'),('Hitta maximum grafiskt',p('Rita funktionen för R ≥ 0, till exempel i GeoGebra. Högsta punkten ligger vid R = 0,60 Ω.')+graph('power')),st('Alternativ: jämför med en övre gräns',r'\begin{aligned}(R-r)^2&\ge0\\(R+r)^2&\ge4Rr\\P_R&\le\frac{\mathcal E^2}{4r}\end{aligned}','Likhet nås när R = r. Eftersom effekten aldrig kan bli större är detta ett maximum, inte bara ett värde större än några testvärden.')],r'Störst effekt fås när \(R=0{,}60\ \Omega\).')
b=sol([total(r'I=\frac{1{,}5}{0{,}60+0{,}60}=1{,}25\ \mathrm A'),power(r'P_R=1{,}25^2\cdot0{,}60=0{,}9375\ \mathrm W','Beräkna effekten i den yttre resistorn, inte i hela kretsen.')],r'\(0{,}9375\ \mathrm W\).')
multi('8.13',[a,b])
byid['8.13']['geogebra']=True
# Explicit per-card tool overrides are added after the token-preserving bank patch.

setq('8.213',[st(r'Kortslutningsström: \(I_k=\mathcal E/r\)',r'I_k=\frac{9{,}0}{1{,}4}\approx6{,}4\ \mathrm A','Vid kortslutning är den yttre resistansen noll i modellen. Den inre resistansen begränsar fortfarande strömmen.')],r'\(6{,}4\ \mathrm A\) enligt modellen.')
setq('8.216',[inner(r'U_r=0{,}50\cdot1=0{,}50\ \mathrm V'),pole(r'U=3{,}0-0{,}50=2{,}5\ \mathrm V')],r'\(2{,}5\ \mathrm V\).')
setq('8.217',[st(r'Ems: \(\mathcal E=U+U_r\)',r'\mathcal E=1{,}2+0{,}3=1{,}5\ \mathrm V','När batteriet levererar ström är ems summan av polspänningen och det inre spänningsfallet.')],r'\(1{,}5\ \mathrm V\).')
a=sol([inner(r'U_r=0{,}50\cdot1{,}2=0{,}60\ \mathrm V')],r'\(0{,}60\ \mathrm V\).')
b=sol([st(r'Polspänning: \(U=\mathcal E-U_r\)',r'U=9{,}0-0{,}60=8{,}4\ \mathrm V')],r'\(8{,}4\ \mathrm V\).')
c=sol([ohm(r'R=\frac{8{,}4}{1{,}2}=7{,}0\ \Omega','Polspänningen ligger över den yttre resistorn.')],r'\(7{,}0\ \Omega\).')
d=sol([pole(r'U=9{,}0-r\cdot0=9{,}0\ \mathrm V','Utan ström är det inre spänningsfallet noll oavsett r.')],r'\(9{,}0\ \mathrm V\).')
multi('8.44',[a,b,c,d])
# Card c describes an isolated resistor, not a battery. Its own data suffice.
byid['8.44']['spelDelar'][2]['s']=solution([ohm(r'R=\frac{8{,}4}{1{,}2}=7{,}0\ \Omega','Spänningen över resistorn och strömmen genom den är givna.')],c[1])
setq('8.218',[inner(why='I batterimodellen finns en resistans inne i batteriet. När ström går blir det ett spänningsfall rI där. En del av energin omvandlas samtidigt till värme inne i batteriet.')],'Att en del av spänningen kan falla inne i batteriet när ström går.')
setq('8.219',[inner(r'I=\frac{U_r}{r}=\frac{0{,}84}{0{,}35}=2{,}4\ \mathrm A')],r'\(2{,}4\ \mathrm A\).')
setq('8.220',[pole(r'U_r=\mathcal E-U=6{,}0-5{,}6=0{,}40\ \mathrm V'),inner(r'I=\frac{0{,}40}{0{,}20}=2{,}0\ \mathrm A')],r'\(2{,}0\ \mathrm A\).')
setq('8.221',[inner(why='När I ökar och r är oförändrad ökar spänningsfallet rI.'),pole(why='Ems är oförändrad. Ett större tal dras då från samma ems.')],'Polspänningen minskar.')
setq('8.223',[st(r'Serieresistans: \(R_{\mathrm{tot}}=R+r\)',r'R_{\mathrm{tot}}=5{,}0+0{,}50=5{,}50\ \Omega'),total(r'I=\frac{12}{5{,}50}\approx2{,}182\ \mathrm A')],r'\(2{,}182\ \mathrm A\).')
a=sol([pole(r'U=1{,}5-0{,}250\cdot2{,}0=1{,}0\ \mathrm V'),ohm(r'R=\frac{1{,}0}{2{,}0}=0{,}50\ \Omega','Den yttre resistorn har polspänningen, inte hela ems, över sig.')],r'\(0{,}50\ \Omega\).')
b=sol([st(r'Kortslutningsström: \(I_k=\mathcal E/r\)',r'I_k=\frac{1{,}5}{0{,}250}=6{,}0\ \mathrm A','Yttre resistansen är noll vid kortslutning i modellen.')],r'\(6{,}0\ \mathrm A\).')
multi('8.66',[a,b])
setq('8.225',[st(r'Ohms lag för hela kretsen: \(R+r=\mathcal E/I\)',r'R+r=\frac{12}{1{,}50}=8{,}0\ \Omega'),st('Dra bort den inre resistansen',r'R=8{,}0-0{,}70=7{,}30\ \Omega')],r'\(7{,}30\ \Omega\).')
setq('8.227',[st(r'Serieresistans: \(R_{\mathrm{tot}}=R+r\)',r'R_{\mathrm{tot}}=4{,}0+0{,}50=4{,}50\ \Omega'),total(r'I=\frac{12}{4{,}50}\approx2{,}667\ \mathrm A')],r'\(2{,}667\ \mathrm A\).')
a=sol([st(r'Kortslutningsström: \(I_k=\mathcal E/r\)',r'I_k=\frac{1{,}5}{0{,}30}=5{,}0\ \mathrm A','Den yttre resistansen är noll i modellen.')],r'\(5{,}0\ \mathrm A\).')
b=sol([total(r'I=\frac{1{,}5}{2{,}7+0{,}30}=0{,}50\ \mathrm A')],r'\(0{,}50\ \mathrm A\).')
c=sol([pole(r'U=1{,}5-0{,}30\cdot0{,}50=1{,}35\ \mathrm V')],r'\(1{,}35\ \mathrm V\).')
d=sol([st(r'Värmeeffekt inne i batteriet: \(P_r=I^2r\)',why='Kortslutningen ger stor ström genom den inre resistansen. Eftersom strömmen kvadreras i effektsambandet kan värmeeffekten bli stor.')],'Den stora strömmen utvecklar värme i batteriets inre resistans.')
multi('8.93',[a,b,c,d])
hints('8.93','Vilken resistans finns kvar i modellen vid kortslutning?','Den yttre resistansen är noll, men den inre finns kvar.','Vilka två resistanser ligger i samma strömväg?','Vilket spänningsfall ska dras från ems?','Hur beror värmeeffekten i en resistans på strömmen?')
setq('8.229',[total(r'I=\frac{12}{6{,}0+0{,}70}\approx1{,}791\ \mathrm A'),ohm(r'U=6{,}0\cdot\frac{12}{6{,}0+0{,}70}\approx10{,}7\ \mathrm V','Polspänningen är spänningen över den yttre resistorn. Behåll hela strömvärdet i beräkningen.')],r'\(10{,}7\ \mathrm V\).')
a=sol([total(r'I=\frac{1{,}5}{1{,}2+0{,}40}=0{,}9375\ \mathrm A')],r'\(0{,}9375\ \mathrm A\).')
b=sol([ohm(r'U_R=0{,}9375\cdot1{,}2=1{,}125\ \mathrm V','Använd strömmen från a).')],r'\(1{,}125\ \mathrm V\).')
c=sol([st('Samma anslutningspunkter ger samma spänning',why='Resistorn är direkt ansluten mellan batteriets två poler. Både polspänningen och resistorns spänning är skillnaden i potential mellan dessa två punkter.')],'Spänningen över resistorn är lika stor som batteriets polspänning.')
multi('8.95',[a,b,c],[a,sol([ohm(r'U_R=0{,}938\cdot1{,}2=1{,}1256\ \mathrm V','Kortet anger strömmen 0,938 A.')],r'\(1{,}1256\ \mathrm V\).'),c])
setq('8.231',[total(r'I=\frac{12}{8{,}0+0{,}50}\approx1{,}412\ \mathrm A'),power(r'P_R=\left(\frac{12}{8{,}0+0{,}50}\right)^2\cdot8{,}0\approx15{,}9\ \mathrm W','Använd bara den yttre resistansen i dess effektberäkning. Strömmen beräknas däremot från båda resistanserna.')],r'\(15{,}9\ \mathrm W\).')
setq('8.233',[total(r'I=\frac{12}{5{,}0+0{,}70}\approx2{,}105\ \mathrm A'),inner(r'U_r=0{,}70\cdot\frac{12}{5{,}0+0{,}70}\approx1{,}47\ \mathrm V','Använd den inre resistansen för spänningsfallet inne i batteriet.')],r'\(1{,}47\ \mathrm V\).')
setq('8.235',[st(r'Kortslutning: \(r=\mathcal E/I_k\)',r'r=\frac{9{,}0}{4{,}0}=2{,}25\ \Omega','Vid kortslutning är yttre resistansen noll. Hela ems motsvarar då spänningsfallet i den inre resistansen.')],r'\(2{,}25\ \Omega\).')
setq('8.236',[pole(r'U_r=12-10{,}8=1{,}2\ \mathrm V'),inner(r'I=\frac{1{,}2}{1{,}2}=1{,}0\ \mathrm A'),ohm(r'R=\frac{10{,}8}{1{,}0}=10{,}8\ \Omega','Det är polspänningen som ligger över den yttre resistorn.')],r'\(10{,}8\ \Omega\).')
a=sol([st(r'Batterier i serie: \(\mathcal E_s=3\mathcal E,\ r_s=3r\)',r'\begin{aligned}\mathcal E_s&=3\cdot1{,}5=4{,}5\ \mathrm V\\r_s&=3\cdot0{,}40=1{,}2\ \Omega\end{aligned}'),total(r'I_s=\frac{4{,}5}{6{,}0+1{,}2}=0{,}625\ \mathrm A')],r'\(0{,}625\ \mathrm A\).')
b=sol([st(r'Lika batterier parallellt: \(r_p=r/3\)',r'r_p=\frac{0{,}40}{3}\ \Omega','Ems är fortfarande 1,5 V. De tre identiska batterierna delar strömmen lika.'),total(r'I_p=\frac{1{,}5}{6{,}0+0{,}40/3}\approx0{,}245\ \mathrm A','Använd den gemensamma inre resistansen tillsammans med den yttre resistorn.')],r'\(0{,}245\ \mathrm A\).')
c=sol([power(why='Samma yttre resistans används i båda fallen. Därför ger den större strömmen också större effekt. 0,625 A är större än 0,245 A.')],'Seriekopplingen ger störst effekt i den yttre resistorn.')
multi('8.99',[a,b,c])
setq('8.238',[st(r'Kortslutning: \(r=\mathcal E/I_k\)',r'r=\frac{9{,}0}{7{,}0}\approx1{,}286\ \Omega','Hela ems ligger över den inre resistansen i kortslutningsmodellen.')],r'\(1{,}286\ \Omega\).')
a=sol([total(r'\begin{aligned}I_{20}&=\frac{12{,}6}{0{,}020+0{,}012}=393{,}75\ \mathrm A\\I_{-20}&=\frac{12{,}6}{0{,}020+0{,}030}=252\ \mathrm A\end{aligned}','Startmotorns resistans är densamma, men batteriets inre resistans är större i kyla.')],r'Vid 20 °C: \(393{,}75\ \mathrm A\). Vid −20 °C: \(252\ \mathrm A\).')
b=sol([ohm(r'\begin{aligned}U_{20}&=393{,}75\cdot0{,}020=7{,}875\ \mathrm V\\U_{-20}&=252\cdot0{,}020=5{,}04\ \mathrm V\end{aligned}','Använd strömmarna från a) och startmotorns resistans.')],r'Vid 20 °C: \(7{,}875\ \mathrm V\). Vid −20 °C: \(5{,}04\ \mathrm V\).')
c=sol([total(r'I=\frac{\mathcal E}{R+r}','När den inre resistansen ökar blir totalströmmen mindre om övriga värden är desamma.'),power(why='Startmotorns resistans är oförändrad. Mindre ström ger mindre effekt i motorn. Därför kan starten bli svårare; utan en startgräns går det inte att säga säkert att bilen inte startar.')],'Startmotorn får mindre ström och mindre effekt i kyla.')
cb=sol([ohm(r'\begin{aligned}U_{20}&=394\cdot0{,}020=7{,}88\ \mathrm V\\U_{-20}&=252\cdot0{,}020=5{,}04\ \mathrm V\end{aligned}','Kortet anger strömmarna 394 A och 252 A. Använd dessa värden.')],r'Vid 20 °C: \(7{,}88\ \mathrm V\). Vid −20 °C: \(5{,}04\ \mathrm V\).')
multi('8.162',[a,b,c],[a,cb,c])
setq('8.239',[pole(why='Ems är samma i båda mätningarna. När strömmen ökar kommer hela minskningen i polspänning från det ökade inre spänningsfallet.'),st(r'Inre resistans: \(r=(U_1-U_2)/(I_2-I_1)\)',r'r=\frac{11{,}6-10{,}8}{3{,}5-1{,}5}=\frac{0{,}80}{2{,}0}=0{,}40\ \Omega')],r'\(0{,}40\ \Omega\).')
a=sol([pole(why='Ems är oförändrad. Spänningens minskning är r gånger strömmens ökning.'),st(r'Inre resistans: \(r=(U_1-U_2)/(I_2-I_1)\)',r'r=\frac{1{,}45-1{,}30}{0{,}90-0{,}30}=\frac{0{,}15}{0{,}60}=0{,}25\ \Omega')],r'\(0{,}25\ \Omega\).')
b=sol([st(r'Ems: \(\mathcal E=U+rI\)',r'\mathcal E=1{,}45+0{,}25\cdot0{,}30=1{,}525\ \mathrm V','Lägg tillbaka det inre spänningsfallet till polspänningen.')],r'\(1{,}525\ \mathrm V\).')
c=sol([pole(r'U=1{,}525-0{,}25\cdot1{,}5=1{,}150\ \mathrm V')],r'\(1{,}150\ \mathrm V\).')
multi('8.163',[a,b,c])
setq('8.241',[st(r'Kortslutning: \(r=\mathcal E/I_k\)',r'r=\frac{9{,}0}{6{,}0}=1{,}5\ \Omega','Vid kortslutning begränsas strömmen av batteriets inre resistans.')],r'\(1{,}5\ \Omega\).')
a=sol([total(r'I=\frac{4{,}5}{12+1{,}2}=\frac{15}{44}\ \mathrm A'),ohm(r'U=12\cdot\frac{15}{44}\approx4{,}09\ \mathrm V'),power(r'P=\left(\frac{15}{44}\right)^2\cdot12\approx1{,}39\ \mathrm W')],r'Lampans spänning är \(4{,}09\ \mathrm V\) och effekt \(1{,}39\ \mathrm W\).')
b=sol([st(r'Identiska parallella lampor: \(R_{\rm ers}=R/n\)',r'R_2=6\ \Omega,\qquad R_3=4\ \Omega'),total(r'\begin{aligned}I_2&=\frac{4{,}5}{6+1{,}2}=0{,}625\ \mathrm A\\I_3&=\frac{4{,}5}{4+1{,}2}=\frac{45}{52}\ \mathrm A\end{aligned}'),ohm(r'\begin{aligned}U_2&=6\cdot0{,}625=3{,}75\ \mathrm V\\U_3&=4\cdot\frac{45}{52}\approx3{,}46\ \mathrm V\end{aligned}','Spänningen över parallellkopplingen är också spänningen över varje lampa.')],r'Två lampor: \(3{,}75\ \mathrm V\) per lampa. Tre lampor: \(3{,}46\ \mathrm V\) per lampa.')
c=sol([total(r'I=\frac{\mathcal E}{R_{\rm ers}+r}','Fler parallella lampor ger mindre ersättningsresistans och större totalström.'),pole(why='Större totalström ger större spänningsfall inuti batteriet. Spänningen över varje lampa sjunker.'),st(r'Lampans effekt: \(P=U^2/R\)',why='Varje lamps resistans är oförändrad. Lägre spänning ger därför lägre effekt i varje lampa.')],'Varje lampa får lägre spänning och effekt när fler lampor parallellkopplas.')
multi('8.164',[a,b,c])
a=sol([total(r'I=\frac{6{,}0}{71+0{,}90}\ \mathrm A'),ohm(r'U=71\cdot\frac{6{,}0}{71{,}9}\approx5{,}92\ \mathrm V')],r'\(5{,}92\ \mathrm V\).')
b=sol([total(r'I=\frac{6{,}0}{710+0{,}90}\ \mathrm A'),ohm(r'U=710\cdot\frac{6{,}0}{710{,}9}\approx5{,}99\ \mathrm V','Den större resistansen ger mindre ström och därmed mindre inre spänningsfall.')],r'\(5{,}99\ \mathrm V\).')
multi('8.398',[a,b])
setq('8.399',[st(r'Ems i serie: \(\mathcal E_{\rm tot}=4\mathcal E\)',r'\mathcal E_{\rm tot}=4\cdot1{,}5=6{,}0\ \mathrm V'),st(r'Total resistans: \(R_{\rm tot}=\mathcal E_{\rm tot}/I\)',r'R_{\rm tot}=\frac{6{,}0}{0{,}45}\ \Omega'),st(r'Fyra lika inre resistanser: \(r=(R_{\rm tot}-R)/4\)',r'r=\frac{6{,}0/0{,}45-12}{4}\approx0{,}33\ \Omega','Dra bort den yttre resistansen innan du delar på de fyra cellerna.')],r'Varje cell har inre resistansen \(0{,}33\ \Omega\).')
setq('8.400',[pole(r'U_r=12-8{,}8=3{,}2\ \mathrm V'),inner(r'r=\frac{3{,}2}{45}\approx0{,}071\ \Omega')],r'\(0{,}071\ \Omega\).')
setq('8.401',[ohm(r'U=10\cdot0{,}55=5{,}5\ \mathrm V','Båda parallellkopplade batterierna har samma polspänning som resistorn.'),st(r'Lika batterier delar strömmen: \(I_{\rm cell}=I_{\rm tot}/2\)',r'I_{\rm cell}=0{,}55/2=0{,}275\ \mathrm A'),inner(r'r=\frac{6{,}0-5{,}5}{0{,}275}\approx1{,}82\ \Omega','Använd strömmen genom ett batteri. Parallellkopplingen dubblerar inte ems.')],r'Varje batteri har inre resistansen \(1{,}82\ \Omega\).')
a=sol([power(r'I=\sqrt{\frac{P}{R}}=\sqrt{\frac{7{,}2}{0{,}32}}\approx4{,}74\ \mathrm A','Strömmens storlek är den positiva roten.')],r'\(4{,}74\ \mathrm A\).')
b=sol([ohm(r'U=0{,}32\sqrt{\frac{7{,}2}{0{,}32}}\approx1{,}52\ \mathrm V','Använd strömmen från a) utan mellanavrundning.')],r'\(1{,}52\ \mathrm V\).')
c=sol([pole(why='Ems fördelas på yttre och inre spänningsfall.'),st(r'Inre resistans: \(r=\mathcal E/I-R\)',r'r=\frac{2{,}0}{\sqrt{7{,}2/0{,}32}}-0{,}32\approx0{,}102\ \Omega','Använd den oavrundade strömmen från a).')],r'\(0{,}102\ \Omega\).')
d=sol([st(r'Två lika parallella resistorer: \(R_{\rm ers}=R/2\)',r'R_{\rm ers}=0{,}32/2=0{,}16\ \Omega'),total(r'I_{\rm ny}=\frac{2{,}0}{0{,}16+r}\approx7{,}64\ \mathrm A','Använd den oavrundade inre resistansen från c). Strömmen ändras när belastningen ändras.'),power(r'P_{\rm tot}=I_{\rm ny}^2\cdot0{,}16\approx9{,}35\ \mathrm W','Ersättningsresistorn tar emot samma totala effekt som de två yttre resistorerna tillsammans.')],r'Resistorernas sammanlagda effekt är \(9{,}35\ \mathrm W\).')
cb=sol([ohm(r'U=4{,}74\cdot0{,}32=1{,}5168\ \mathrm V','Använd strömmen 4,74 A som är given på kortet.')],r'\(1{,}52\ \mathrm V\).')
cc=sol([pole(r'U_r=2{,}0-1{,}52=0{,}48\ \mathrm V'),inner(r'r=\frac{0{,}48}{4{,}74}\approx0{,}101\ \Omega')],r'\(0{,}101\ \Omega\).')
cd=sol([st(r'Två lika parallella resistorer: \(R_{\rm ers}=R/2\)',r'R_{\rm ers}=0{,}16\ \Omega'),total(r'I=\frac{2{,}0}{0{,}16+0{,}10}=\frac{100}{13}\ \mathrm A','Kortet anger den inre resistansen 0,10 Ω.'),power(r'P_{\rm tot}=\left(\frac{100}{13}\right)^2\cdot0{,}16\approx9{,}47\ \mathrm W')],r'Resistorernas sammanlagda effekt är \(9{,}47\ \mathrm W\).')
multi('8.402',[a,b,c,d],[a,cb,cc,cd])
a=sol([st(r'Effekt och resistans: \(P=U^2/R\)',r'R=\frac{11{,}6^2}{20}=6{,}728\ \Omega')],r'\(6{,}728\ \Omega\).')
b=sol([st(r'Effekt: \(P=UI\)',r'I=\frac{20}{11{,}6}=\frac{50}{29}\ \mathrm A'),inner(r'r=\frac{15-11{,}6}{50/29}=1{,}972\ \Omega','Spänningsskillnaden mellan ems och polspänning ligger över den inre resistansen.')],r'\(1{,}972\ \Omega\).')
c=sol([st(r'Inre effekt: \(P_r=U_rI\)',r'P_r=(15-11{,}6)\cdot\frac{50}{29}\approx5{,}86\ \mathrm W','Använd den oavrundade strömmen från b).')],r'\(5{,}86\ \mathrm W\).')
cb=sol([inner(r'r=\frac{15-11{,}6}{1{,}72}\approx1{,}98\ \Omega','Använd kortets givna ström 1,72 A och det inre spänningsfallet.')],r'\(1{,}98\ \Omega\).')
cc=sol([st(r'Inre effekt: \(P_r=U_rI\)',r'P_r=(15-11{,}6)\cdot1{,}72=5{,}848\ \mathrm W')],r'\(5{,}85\ \mathrm W\).')
multi('8.403',[a,b,c],[a,cb,cc])
setq('8.404',[st(r'Total resistans: \(R+r=\mathcal E/I\)',r'r=\frac{12}{0{,}50}-21=3{,}0\ \Omega'),power(r'P_r=0{,}50^2\cdot3{,}0=0{,}75\ \mathrm W','Här används den inre resistansen eftersom det är batteriets värmeeffekt som efterfrågas.')],r'\(0{,}75\ \mathrm W\).')
a=sol([st(r'Seriekoppling: ems och inre resistans adderas',r'\begin{aligned}\mathcal E_{\rm tot}&=3{,}0\ \mathrm V\\r_{\rm tot}&=0{,}410\ \Omega\end{aligned}'),st(r'Yttre resistans: \(R=\mathcal E_{\rm tot}/I-r_{\rm tot}\)',r'R=\frac{3{,}0}{0{,}60}-0{,}410=4{,}59\ \Omega')],r'\(4{,}59\ \Omega\).')
b=sol([power(r'P_r=0{,}60^2\cdot0{,}410=0{,}1476\ \mathrm W','De inre resistanserna har summan 0,410 Ω.'),st(r'Total tillförd effekt: \(P_{\rm tot}=\mathcal E_{\rm tot}I\)',r'P_{\rm tot}=3{,}0\cdot0{,}60=1{,}8\ \mathrm W'),st(r'Andel inre förlust: \(P_r/P_{\rm tot}\)',r'\frac{0{,}1476}{1{,}8}=0{,}082=8{,}2\,\%')],r'\(8{,}2\,\%\) omvandlas till värme i batterierna.')
multi('8.405',[a,b])
a=sol([total(r'I=\frac{12{,}6}{5{,}0+0{,}080}\ \mathrm A'),ohm(r'U=5{,}0\cdot\frac{12{,}6}{5{,}08}\approx12{,}40\ \mathrm V')],r'\(12{,}40\ \mathrm V\).')
b=sol([st(r'Ström i förgreningen: \(I_{\rm tot}=I_{\rm lampor}+I_{\rm motor}\)',r'I_{\rm tot}=\frac{U}{5{,}0}+35','Lampornas ström beror på den nya polspänningen. Strömmen från a) kan därför inte återanvändas.'),pole(r'U=12{,}6-0{,}080\left(\frac U5+35\right)'),st('Samla termer med U',r'\begin{aligned}U&=9{,}8-0{,}016U\\1{,}016U&=9{,}8\\U&\approx9{,}65\ \mathrm V\end{aligned}')],r'\(9{,}65\ \mathrm V\).')
multi('8.406',[a,b])
a=sol([total(r'\begin{aligned}I_0&=\frac{6{,}0}{5{,}0+1{,}2}\\I_1&=\frac{6{,}0}{10+1{,}2}\end{aligned}','Den yttre resistansen dubbleras, men den inre resistansen är oförändrad.'),st(r'Förhållandet: \(I_1/I_0\)',r'\frac{I_1}{I_0}=\frac{6{,}2}{11{,}2}\approx0{,}554')],r'Den nya strömmen är \(0{,}554\) gånger den ursprungliga.')
b=sol([total(r'\begin{aligned}I_0&=\frac{6{,}0}{5{,}0+1{,}2}\\I_2&=\frac{6{,}0}{2{,}5+1{,}2}\end{aligned}','Den yttre resistansen halveras. Ta fortfarande med batteriets inre resistans.'),st(r'Förhållandet: \(I_2/I_0\)',r'\frac{I_2}{I_0}=\frac{6{,}2}{3{,}7}\approx1{,}68')],r'Den nya strömmen är \(1{,}68\) gånger den ursprungliga.')
ca=sol([total(r'I_1=\frac{6{,}0}{10+1{,}2}\ \mathrm A'),st(r'Förhållandet: \(I_1/I_0\)',r'\frac{I_1}{I_0}=\frac{6{,}0/11{,}2}{0{,}968}\approx0{,}553','Kortet anger den ursprungliga strömmen 0,968 A.')],r'Den nya strömmen är \(0{,}553\) gånger den ursprungliga.')
cb=sol([total(r'I_2=\frac{6{,}0}{2{,}5+1{,}2}\ \mathrm A'),st(r'Förhållandet: \(I_2/I_0\)',r'\frac{I_2}{I_0}=\frac{6{,}0/3{,}7}{0{,}968}\approx1{,}68','Kortet anger den ursprungliga strömmen 0,968 A.')],r'Den nya strömmen är \(1{,}68\) gånger den ursprungliga.')
multi('8.407',[a,b],[ca,cb])
setq('8.408',[st(r'Seriekoppling: ems och resistans adderas',r'\begin{aligned}\mathcal E_{\rm tot}&=2\cdot1{,}5=3{,}0\ \mathrm V\\r_{\rm tot}&=2\cdot0{,}20=0{,}40\ \Omega\end{aligned}'),total(r'I=\frac{3{,}0}{3{,}6+0{,}40}=0{,}75\ \mathrm A'),power(r'P_R=0{,}75^2\cdot3{,}6=2{,}025\ \mathrm W')],r'Cirka \(2{,}0\ \mathrm W\).')
a=sol([pole(r'\mathcal E=9{,}0\ \mathrm V','Utan belastning går i praktiken ingen ström. Den uppmätta spänningen är då ems.'),inner(r'I=\frac{9{,}0-7{,}6}{2{,}0}=0{,}70\ \mathrm A'),ohm(r'R=\frac{7{,}6}{0{,}70}=\frac{76}{7}\ \Omega\approx10{,}9\ \Omega')],r'\(10{,}9\ \Omega\).')
b=sol([st(r'Parallellresistans: \(R_{\rm ers}=30R/(30+R)\)',r'R_{\rm ers}=\frac{30\cdot(76/7)}{30+76/7}\approx7{,}972\ \Omega','Använd den oavrundade resistansen från a).'),st(r'Polspänning: \(U=\mathcal E R_{\rm ers}/(R_{\rm ers}+r)\)',r'U=\frac{9{,}0R_{\rm ers}}{R_{\rm ers}+2{,}0}\approx7{,}19\ \mathrm V','Sambandet fås genom att först beräkna totalströmmen och sedan använda Ohms lag för den yttre kretsen. Behåll full precision i mellanleden.')],r'\(7{,}19\ \mathrm V\).')
cb=sol([st(r'Parallellresistans: \(R_{\rm ers}=R_1R_2/(R_1+R_2)\)',r'R_{\rm ers}=\frac{10{,}9\cdot30}{10{,}9+30}\approx7{,}995\ \Omega','Använd kortets givna resistans 10,9 Ω.'),st(r'Polspänning: \(U=\mathcal E R_{\rm ers}/(R_{\rm ers}+r)\)',r'U=\frac{9{,}0R_{\rm ers}}{R_{\rm ers}+2{,}0}\approx7{,}20\ \mathrm V','Behåll full precision i ersättningsresistansen.')],r'\(7{,}20\ \mathrm V\).')
multi('8.409',[a,b],[a,cb])
multi('8.525',[sol([ohm(r'\begin{aligned}I_A&=10/5=2\ \mathrm A\\I_B&=9/3=3\ \mathrm A\end{aligned}','Det är två olika belastningar av samma batteri.'),st(r'Ems: \(\mathcal E=U+rI\)',r'\begin{aligned}\mathcal E&=10+2r\\\mathcal E&=9+3r\end{aligned}','Batteriets ems och inre resistans är desamma i båda försöken.'),st('Sätt uttrycken för ems lika',r'\begin{aligned}10+2r&=9+3r\\r&=1\ \Omega\end{aligned}'),st(r'Sätt tillbaka i \(\mathcal E=U+rI\)',r'\mathcal E=10+2\cdot1=12\ \mathrm V'),st('Kontrollera det andra försöket',r'12-1\cdot3=9\ \mathrm V','Även den andra uppmätta polspänningen stämmer.')],r'Ems är \(12\ \mathrm V\) och inre resistans \(1\ \Omega\).')])

# These hints are authored for the card's own givens; fix exponent notation inside TeX.
byid['8.225']['svarEnhet']='Ω'
# The two requested quantities belong to one question, not an artificial part a).
q=byid['8.525'];q['s']=q['s'].replace('<div class="facit-del"><span class="facit-mark">a)</span><div class="facit-arbete">','').removesuffix('</div></div></div>')+'</div>'
for id in changes:
 q=byid[id]
 for item in [q]+q.get('spelDelar',[]):
  if item.get('ledtrad'):item['ledtrad']=item['ledtrad'].replace('I²','I^2')
hints('8.407','Jämför den nya och den ursprungliga strömmen. Glöm inte den inre resistansen.','Beräkna strömmen med den nya totalresistansen. Dividera sedan med den givna ursprungliga strömmen.','Även när den yttre resistansen halveras finns den inre resistansen kvar. Jämför strömmarna.')
expected={q['id'] for q in bank if q.get('familj')=='Ems, polspänning och inre resistans'}
assert set(changes)==expected,(set(changes)^expected)
assert len(changes)==48
save()
# Add explicit card overrides only to the reviewed optimization task.
s=BANK.read_text();start=s.index('  {\n    "id": "8.13",')+2
q,end=json.JSONDecoder().raw_decode(s[start:])
q['spelDelar'][0]['geogebra']=True
q['spelDelar'][1]['geogebra']=False
replacement=json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ')
BANK.write_text(s[:start]+replacement+s[start+end:])
print(f'Updated {len(changes)} tasks and {sum(len(byid[id].get("spelDelar",[])) for id in changes)} cards')
