"""Explicitly authored solutions for all 26 Blandade kopplingar, 2026-11-04."""
from render import *
def step(title,tex='',why=''):
 return (title,(p(why) if why else '')+(m(tex) if tex else ''))
def sol(steps,answer):return (steps,answer)
def giv(text):return step('Givet och sökt',why=text)
def ohm(tex,why=''):return step(r'Ohms lag: \(U=RI\)',tex,why)
def par(tex,why=''):
 return step(r'Parallellkoppling: \(R_p=\frac{R_aR_b}{R_a+R_b}\)',tex,why)
def ser(tex,why=''):return step(r'Seriekoppling: \(R_{\mathrm{tot}}=R_a+R_b\)',tex,why)
def direct(title,tex,answer,why=''):return sol([step(title,tex,why)],answer)

setq('8.4',[
 giv('Sökt: effekten i R₃. R₁ ligger före förgreningen, medan R₂ och R₃ har samma spänning.'),
 par(r'R_p=\frac{200\cdot300}{200+300}=120\ \Omega'),
 ser(r'R_{\mathrm{tot}}=120+120=240\ \Omega','Ersätt parallellkopplingen med en resistor på 120 Ω.'),
 ohm(r'I=\frac{12}{240}=0{,}050\ \mathrm A','Detta är totalströmmen, inte strömmen genom R₃.'),
 ohm(r'U_p=0{,}050\cdot120=6{,}0\ \mathrm V','Spänningen över R₃ är lika stor som över hela parallellkopplingen.'),
 step(r'Effekt i R₃: \(P_3=\frac{U_p^2}{R_3}\)',r'P_3=\frac{6{,}0^2}{300}=0{,}12\ \mathrm W')],r'\(P_3=0{,}12\ \mathrm W\).')

a=sol([giv('Spänningen är 12 V. R₁ = 100 Ω och R₂ = 200 Ω. Sökt: totalströmmen i båda brytarlägena.'),
 ohm(r'I_{\mathrm{öppen}}=\frac{12}{100+200}=0{,}040\ \mathrm A','Med öppen brytare måste strömmen gå genom båda resistorerna i serie.'),
 ohm(r'I_{\mathrm{sluten}}=\frac{12}{100}=0{,}120\ \mathrm A','Med sluten brytare förbinder en ledning R₂:s båda ändar. R₂ får ingen spänning över sig och förbikopplas.')],r'Öppen brytare: \(0{,}040\ \mathrm A\). Sluten brytare: \(0{,}120\ \mathrm A\).')
b=sol([step(r'Elektrisk effekt: \(P=I^2R\)',why='Resistansen är oförändrad. När vi dividerar den nya effekten med den gamla förkortas R bort.'),step('Jämför strömmarnas kvadrater',r'\frac{P_{\mathrm{ny}}}{P_{\mathrm{gammal}}}=\left(\frac{0{,}120}{0{,}040}\right)^2=9')],'Effekten blir 9 gånger så stor.')
multi('8.18',[a,b])

a=sol([par(r'R_p=\frac{300\cdot600}{300+600}=200\ \Omega','De två resistorerna har samma spänning. Strömmen kan delas mellan dem, så ersättningsresistansen blir mindre än vardera resistansen.')],r'\(200\ \Omega\).')
b=sol([ser(r'R_{\mathrm{tot}}=150+200=350\ \Omega','Parallellkopplingens 200 Ω från a) ligger i serie med R₁.'),ohm(r'I=\frac{12}{350}\approx0{,}03429\ \mathrm A')],r'\(0{,}03429\ \mathrm A\).')
c=sol([ohm(r'U_p=\frac{12}{350}\cdot200\approx6{,}857\ \mathrm V','Använd totalströmmen från b) med full precision. Den går in i hela parallellkopplingen.')],r'\(6{,}857\ \mathrm V\).')
d=sol([ohm(r'I_2=\frac{(12/350)\cdot200}{300}\approx0{,}02286\ \mathrm A','R₂ har parallellkopplingens spänning från c). Behåll full precision i beräkningen.')],r'\(0{,}02286\ \mathrm A\).')
multi('8.43',[a,b,c,d],[a,sol([ohm(r'I=\frac{12}{350}\approx0{,}03429\ \mathrm A','Totalresistansen 350 Ω och spänningen 12 V är givna.')],b[1]),sol([ohm(r'U_p=0{,}03429\cdot200=6{,}858\ \mathrm V','Använd strömmen och resistansen som anges i detta kort.')],r'\(6{,}858\ \mathrm V\).'),sol([ohm(r'I=\frac{6{,}86}{300}\approx0{,}02287\ \mathrm A','Detta kort anger spänningen 6,86 V.')],r'\(0{,}02287\ \mathrm A\).')])

setq('8.52',[giv('Sökt: spänningen över R₃ = 250 Ω. Börja med grenen där R₂ och R₃ ligger i serie.'),
 ser(r'R_{23}=150+250=400\ \Omega'),par(r'R_p=\frac{400\cdot400}{400+400}=200\ \Omega','Seriekombinationen R₂ och R₃ ligger parallellt med R₄.'),
 ohm(r'I=\frac{12}{100+200}=0{,}040\ \mathrm A','Totalströmmen går genom R₁ och delar sig därefter.'),
 ohm(r'U_p=0{,}040\cdot200=8{,}0\ \mathrm V','Hela grenen med R₂ och R₃ har denna spänning.'),
 ohm(r'I_{23}=\frac{8{,}0}{400}=0{,}020\ \mathrm A','Samma grenström går genom R₂ och R₃.'),
 ohm(r'U_3=0{,}020\cdot250=5{,}0\ \mathrm V')],r'\(U_3=5{,}0\ \mathrm V\).')

a=sol([par(r'R_p=\frac{200\cdot300}{200+300}=120\ \Omega','R₂ och R₃ ligger mellan samma två förgreningspunkter.')],r'\(120\ \Omega\).')
b=sol([ser(r'R_{\mathrm{tot}}=100+120=220\ \Omega','R₁ ligger i serie med parallellkopplingens ersättningsresistans 120 Ω.')],r'\(220\ \Omega\).')
c=sol([ohm(r'I=\frac{12}{220}\approx0{,}05455\ \mathrm A','Hela kretsen har spänningen 12 V och resistansen 220 Ω.')],r'\(0{,}05455\ \mathrm A\).')
d=sol([ohm(r'U_p=\frac{12}{220}\cdot120\approx6{,}545\ \mathrm V','Totalströmmen från c) går in i parallellkopplingen. Behåll dess fulla precision.')],r'\(6{,}545\ \mathrm V\).')
multi('8.53',[a,b,c,d],[a,b,c,sol([ohm(r'U_p=0{,}05455\cdot120=6{,}546\ \mathrm V','Utgå från kortets givna ström 0,05455 A.')],r'\(6{,}546\ \mathrm V\).')])

a=sol([step('Laddningen bevaras i knutpunkten',why='Ingen laddning samlas i knutpunkten. Därför måste lika mycket laddning passera in som ut under samma tid.')],'Summan av strömmarna in är lika stor som summan av strömmarna ut.')
b=sol([step(r'Knutpunktslagen: \(I=I_1+I_2+I_3\)',r'I_2=450-180-120=150\ \mathrm{mA}','Dra de två kända utgående strömmarna från strömmen in. Alla värden är i mA.')],r'\(I_2=150\ \mathrm{mA}\).')
c=sol([step(r'Andel: \(\frac{\text{delen}}{\text{helheten}}\)',r'\frac{I_1}{I}=\frac{180}{450}=0{,}40','Grenströmmen jämförs med hela strömmen. 0,40 motsvarar 40 %.')],'40 %.')
d=sol([step(r'Ohms lag: \(I=\frac UR\)',why='Spänningen över varje kvarvarande gren och dess resistans är oförändrade. Då är också strömmen genom den grenen oförändrad.'),step(r'Ny totalström: \(I=I_1+I_3\)',r'I=180+120=300\ \mathrm{mA}','Den brutna grenen leder inte längre någon ström.')],'I₁ och I₃ är oförändrade. Totalströmmen minskar till 300 mA.')
dc=sol([step(r'Ohms lag: \(I=\frac UR\)',why='Varje kvarvarande resistor har samma spänning och resistans som tidigare. Därför ändras inte strömmen i den grenen.')],'Strömmarna i de kvarvarande grenarna är oförändrade.')
multi('8.54',[a,b,c,d],[a,b,c,dc])

a=sol([step(r'Samma spänning i parallell: \(U_1=U_2=U\)',why='Båda resistorerna är anslutna mellan samma två punkter på spänningskällan. Varje resistor får därför hela spänningen 6,0 V.')],r'\(U_1=6{,}0\ \mathrm V\) och \(U_2=6{,}0\ \mathrm V\).')
b=sol([ohm(r'I_1=\frac{6{,}0}{200}=0{,}030\ \mathrm A','Varje gren har spänningen 6,0 V, men grenarnas olika resistanser ger olika strömmar.'),ohm(r'I_2=\frac{6{,}0}{300}=0{,}020\ \mathrm A')],r'\(I_1=0{,}030\ \mathrm A\) och \(I_2=0{,}020\ \mathrm A\).')
c=sol([par(r'R_p=\frac{200\cdot300}{200+300}=120\ \Omega'),step('Rimlighetskontroll',why='120 Ω är mindre än både 200 Ω och 300 Ω, som det ska vara vid parallellkoppling.')],r'\(120\ \Omega\).')
multi('8.87',[a,b,c])

a=sol([giv('Spänningen är 12 V, R₁ = 40 Ω och R₂ = 60 Ω. Brytaren är öppen.'),ohm(r'I=\frac{12}{40+60}=0{,}120\ \mathrm A','Strömmen måste gå genom båda resistorerna i serie.')],r'\(0{,}120\ \mathrm A\).')
b=sol([ohm(r'U_1=0{,}120\cdot40=4{,}8\ \mathrm V','Samma ström 0,120 A går genom de två seriekopplade resistorerna.'),ohm(r'U_2=0{,}120\cdot60=7{,}2\ \mathrm V'),step('Kontrollera hela spänningen',r'4{,}8+7{,}2=12\ \mathrm V')],r'\(U_1=4{,}8\ \mathrm V\) och \(U_2=7{,}2\ \mathrm V\).')
c=sol([step('Sluten brytare förbikopplar R₂',why='Ledningen förbinder R₂:s båda ändar. Därmed är spänningen över R₂ noll och bara R₁ begränsar totalströmmen.'),ohm(r'I=\frac{12}{40}=0{,}300\ \mathrm A')],r'\(0{,}300\ \mathrm A\).')
d=sol([step(r'Elektrisk effekt: \(P=I^2R\)',why='Resistansen är oförändrad. Effektens ändringsfaktor är därför kvadraten på strömmens ändringsfaktor.'),step('Jämför den nya effekten med den gamla',r'\frac{P_{\mathrm{ny}}}{P_{\mathrm{gammal}}}=\left(\frac{0{,}300}{0{,}120}\right)^2=6{,}25')],'Effekten blir 6,25 gånger så stor.')
multi('8.90',[a,b,c,d])

a=sol([ser(r'R_{12}=100+200=300\ \Omega','Samma ström går genom R₁ och R₂ utan någon förgrening mellan dem.')],r'\(300\ \Omega\).')
b=sol([par(r'R_p=\frac{300\cdot300}{300+300}=150\ \Omega','De två grenarna har resistansen 300 Ω vardera. Två lika stora resistanser parallellt ger halva resistansen.')],r'\(150\ \Omega\).')
c=sol([ohm(r'I=\frac{9{,}0}{150}=0{,}060\ \mathrm A','Spänningen är 9,0 V och hela kretsens ersättningsresistans är 150 Ω.')],r'\(0{,}060\ \mathrm A\).')
multi('8.123',[a,b,c])

a=sol([step('Jämför spänningen över varje lampa',why='I parallellkopplingen B får varje lampa hela batteriets spänning. I seriekopplingen A delas spänningen lika mellan de tre likadana lamporna.'),step('Större spänning ger mer ljus från samma lampa',why='Varje lampa får större elektrisk effekt i parallellkopplingen och lyser därför starkare.')],'Varje lampa lyser starkare i krets B, parallellkopplingen.')
b=sol([step(r'Total elektrisk effekt: \(P=UI\)',why='I parallellkopplingen får varje lampa hela batteriets spänning och drar mer ström än en lampa i serien. Dessutom adderas de tre grenströmmarna. Totalströmmen och därmed batteriets effektuttag blir större.'),step(r'Drifttid vid given energi: \(t=\frac EP\)',why='När mer energi används varje sekund räcker samma mängd batterienergi kortare tid.')],'Parallellkopplingen tömmer batteriet snabbare.')
c=sol([step('Serie: en enda strömväg',why='När en lampa går sönder och bryter kretsen kan ingen ström gå genom någon av lamporna.'),step('Parallell: en egen strömväg för varje lampa',why='Ett avbrott i en gren bryter inte de andra grenarna. De andra lamporna fortsätter lysa.')],'I serie slocknar alla lampor. I parallellkoppling lyser de andra vidare.')
multi('8.126',[a,b,c])

a=sol([par(r'R_p=\frac{90\cdot90}{90+90}=45\ \Omega','Två lika resistorer parallellt ger halva resistansen.')],r'\(45\ \Omega\).')
b=sol([ser(r'R_{\mathrm{tot}}=90+45=135\ \Omega','Den ensamma resistorn ligger i serie med parallellkopplingen.')],r'\(135\ \Omega\).')
c=sol([ohm(r'I=\frac{9{,}0}{90+45}=\frac1{15}\ \mathrm A','Totalströmmen går genom den ensamma resistorn.'),ohm(r'U=\frac1{15}\cdot90=6{,}0\ \mathrm V')],r'\(6{,}0\ \mathrm V\).')
multi('8.127',[a,b,c])

setq('8.252',[giv('Sökt: spänningen över R₂ och R₃. R₁ ligger i serie med deras parallellkoppling.'),par(r'R_p=\frac{6\cdot12}{6+12}=4\ \Omega'),ohm(r'I=\frac{18}{4+4}=2{,}25\ \mathrm A','Serieresistanserna adderas innan totalströmmen beräknas.'),ohm(r'U_p=2{,}25\cdot4=9{,}0\ \mathrm V')],r'\(9{,}0\ \mathrm V\).')

a=sol([giv('R₁ = 120 Ω och I = 30 mA = 0,030 A. Sökt: spänningen över R₁.'),ohm(r'U_1=0{,}030\cdot120=3{,}6\ \mathrm V')],r'\(3{,}6\ \mathrm V\).')
b=sol([step(r'Spänningar i serie: \(U=U_1+U_2\)',r'U_2=9{,}0-3{,}6=5{,}4\ \mathrm V','Hela spänningen 9,0 V fördelas över de två resistorerna.')],r'\(5{,}4\ \mathrm V\).')
c=sol([giv('U₂ = 5,4 V och samma ström 30 mA = 0,030 A går genom R₂.'),ohm(r'R_2=\frac{5{,}4}{0{,}030}=180\ \Omega')],r'\(180\ \Omega\).')
dc=sol([ohm(r'R_{\mathrm{tot}}=\frac{9{,}0}{0{,}030}=300\ \Omega','Omvandla först 30 mA till 0,030 A. Använd hela kretsens spänning och ström.')],r'\(300\ \Omega\).')
d=sol(dc[0]+[step(r'Kontroll med \(R_2=R_{\mathrm{tot}}-R_1\)',r'R_2=300-120=180\ \Omega','Det stämmer med resultatet i c).')],dc[1])
multi('8.130',[a,b,c,d],[a,b,c,dc])

a=sol([par(r'R_p=\frac{100\cdot100}{100+100}=50\ \Omega','Två lika resistanser parallellt ger halva resistansen.')],r'\(50\ \Omega\).')
b=sol([ser(r'R_{\mathrm{tot}}=50+50=100\ \Omega','R₁ ligger i serie med parallellkopplingens ersättningsresistans.')],r'\(100\ \Omega\).')
c=sol([ohm(r'I=\frac{12}{100}=0{,}12\ \mathrm A','Totalströmmen från källan går genom R₁.'),ohm(r'U_1=0{,}12\cdot50=6{,}0\ \mathrm V')],r'\(6{,}0\ \mathrm V\).')
multi('8.133',[a,b,c],[a,b,sol([ohm(r'U=0{,}12\cdot50=6{,}0\ \mathrm V','Kortet anger redan strömmen genom resistorn och dess resistans.')],c[1])])

setq('8.253',[giv('Varje parallell resistor är 8,0 Ω och har spänningen 8,0 V. Sökt: källans spänning.'),ohm(r'I_2=I_3=\frac{8{,}0}{8{,}0}=1{,}0\ \mathrm A'),step(r'Knutpunktslagen: \(I=I_2+I_3\)',r'I=1{,}0+1{,}0=2{,}0\ \mathrm A','R₁ leder båda grenarnas sammanlagda ström.'),ohm(r'U_1=2{,}0\cdot5{,}0=10\ \mathrm V'),step(r'Spänningar i serie: \(U=U_1+U_p\)',r'U=10+8{,}0=18\ \mathrm V')],r'\(18\ \mathrm V\).')
setq('8.134',[giv('Amperemetern sitter i grenen med R₃ = 600 Ω och visar 8,0 mA = 0,0080 A. Sökt: batteriets spänning.'),ohm(r'U_p=0{,}0080\cdot600=4{,}8\ \mathrm V','R₂ och R₃ har samma spänning eftersom de är parallellkopplade.'),ohm(r'I_2=\frac{4{,}8}{300}=0{,}016\ \mathrm A'),step(r'Knutpunktslagen: \(I=I_2+I_3\)',r'I=0{,}016+0{,}0080=0{,}024\ \mathrm A','R₁ leder totalströmmen, inte bara amperemeterns ström.'),ohm(r'U_1=0{,}024\cdot150=3{,}6\ \mathrm V'),step(r'Spänningar i serie: \(U=U_1+U_p\)',r'U=3{,}6+4{,}8=8{,}4\ \mathrm V')],r'\(8{,}4\ \mathrm V\).')
setq('8.254',[giv('Sökt: parallellkopplingens spänning. Källspänningen 18 V delas mellan R₁ och parallellkopplingen.'),par(r'R_p=\frac{10\cdot10}{10+10}=5\ \Omega'),ohm(r'I=\frac{18}{6+5}=\frac{18}{11}\ \mathrm A','Behåll strömmen som bråk tills spänningen är beräknad.'),ohm(r'U_p=\frac{18}{11}\cdot5\approx8{,}1818\ \mathrm V')],r'\(8{,}1818\ \mathrm V\).')
setq('8.255',[giv('Sökt: totalströmmen från källan på 18 V.'),par(r'R_p=\frac{12\cdot12}{12+12}=6\ \Omega'),ser(r'R_{\mathrm{tot}}=7+6=13\ \Omega','R₁ ligger före förgreningen och är i serie med parallellkopplingen.'),ohm(r'I=\frac{18}{13}\approx1{,}3846\ \mathrm A')],r'\(1{,}3846\ \mathrm A\).')

a=sol([step(r'Utgångsläget: \(I=\frac UR\)',why='Spänningen är densamma som när endast en resistor R är inkopplad.'),step(r'Serieresistans: \(R_{\mathrm{tot}}=nR\)',r'I_{\mathrm{serie}}=\frac{U}{nR}=\frac{I}{n}','Alla n resistorer leder samma ström. Deras resistanser adderas.')],r'\(I/n\).')
b=sol([step(r'Ohms lag i varje gren: \(I=\frac UR\)',why='Varje resistor är ansluten till hela spänningen U. Varje gren leder därför strömmen I.'),step(r'Knutpunktslagen: \(I_{\mathrm{tot}}=I_1+\cdots+I_n\)',r'I_{\mathrm{parallell}}=nI','De n lika stora grenströmmarna adderas.')],r'\(nI\).')
multi('8.153',[a,b])
setq('8.154',[giv('Sökt: strömmen genom R₄ = 600 Ω. R₂, R₃ och R₄ är parallellkopplade och R₁ = 100 Ω ligger i serie med dem.'),step(r'Parallellkoppling: \(\frac1{R_p}=\frac1{R_2}+\frac1{R_3}+\frac1{R_4}\)',r'\begin{aligned}\frac1{R_p}&=\frac1{200}+\frac1{300}+\frac1{600}\\&=\frac1{100}\end{aligned}','Alltså är parallellkopplingens ersättningsresistans 100 Ω.'),ser(r'R_{\mathrm{tot}}=100+100=200\ \Omega'),ohm(r'I=\frac{12}{200}=0{,}060\ \mathrm A','Detta är strömmen genom R₁, som sedan delas upp i tre grenar.'),ohm(r'U_p=0{,}060\cdot100=6{,}0\ \mathrm V'),ohm(r'I_4=\frac{6{,}0}{600}=0{,}010\ \mathrm A','R₄ har samma spänning som de andra parallella resistorerna.')],r'\(I_4=0{,}010\ \mathrm A\), alltså 10 mA.')
setq('8.256',[giv('Sökt: strömmen genom R₂ = 6 Ω, inte totalströmmen. R₂ och R₃ = 8 Ω är parallellkopplade.'),par(r'R_p=\frac{6\cdot8}{6+8}=\frac{24}{7}\ \Omega'),ohm(r'I=\frac{18}{4+24/7}=\frac{63}{26}\ \mathrm A','Totalströmmen går genom R₁. Behåll exakta bråk i mellanleden.'),ohm(r'U_p=\frac{63}{26}\cdot\frac{24}{7}=\frac{108}{13}\ \mathrm V'),ohm(r'I_2=\frac{108/13}{6}=\frac{18}{13}\approx1{,}3846\ \mathrm A')],r'\(I_2\approx1{,}3846\ \mathrm A\).')
setq('8.370',[par(r'R_p=\frac{10\cdot10}{10+10}=5{,}0\ \Omega','De två resistorerna på 10 Ω är parallellkopplade.'),ser(r'R_{\mathrm{tot}}=5{,}0+4{,}7=9{,}7\ \Omega','Den återstående resistorn ligger i serie med parallellkopplingen.')],r'\(9{,}7\ \Omega\).')
setq('8.524',[giv('Strömmen är 0,30 A med öppen brytare och 0,60 A med sluten brytare. Källspänningen är oförändrad. Sökt: spänningen och R.'),ohm(r'U=0{,}30\cdot(10+30)=12\ \mathrm V','Med öppen brytare är grenen med R bruten. Bara 10 Ω och 30 Ω ligger i strömvägen.'),ohm(r'R_{\mathrm{tot}}=\frac{12}{0{,}60}=20\ \Omega','Med sluten brytare använder vi samma källspänning men den nya totalströmmen.'),ser(r'R_p=20-10=10\ \Omega','Dra bort serieresistorn för att få parallellkopplingens resistans.'),step(r'Parallellkoppling: \(\frac1{R_p}=\frac1{30}+\frac1R\)',r'\begin{aligned}\frac1R&=\frac1{10}-\frac1{30}\\&=\frac2{30}=\frac1{15}\\R&=15\ \Omega\end{aligned}')],r'Källspänningen är \(12\ \mathrm V\) och \(R=15\ \Omega\).')
setq('8.526',[giv('Alla tre resistanser är 1,0 kΩ = 1 000 Ω. Källan ger 6,0 V. Sökt: voltmeterns spänning och totalströmmen i mA.'),par(r'R_p=\frac{1000\cdot1000}{1000+1000}=500\ \Omega','Voltmetern leder ström och bildar en parallellkoppling med den nedre resistorn. Den kan därför inte behandlas som en ideal voltmeter.'),ser(r'R_{\mathrm{tot}}=1000+500=1500\ \Omega'),ohm(r'I=\frac{6{,}0}{1500}=0{,}004\ \mathrm A','Detta är strömmen från spänningskällan, alltså 4 mA.'),ohm(r'U_V=0{,}004\cdot500=2{,}0\ \mathrm V','Voltmetern visar spänningen över parallellkopplingen, inte över hela kretsen.'),step('Mätaren påverkar kretsen',why='Utan mätaren delas 6 V lika mellan de två resistorerna. Mätaren sänker den nedre delens resistans, så den uppmätta spänningen blir mindre än 3 V.')],r'Voltmetern visar \(2{,}0\ \mathrm V\). Strömmen från källan är \(4{,}0\ \mathrm{mA}\).')
setq('8.527',[giv('Värmaren är 4,0 Ω. Båda ledningarna är 0,40 Ω vardera. Sökt: minsta källspänningen för 25 W och andelen effekt i värmaren.'),step(r'Värmarens effekt: \(P_v=I^2R_v\)',r'I=\sqrt{\frac{25}{4{,}0}}=2{,}50\ \mathrm A','Beräkna först den minsta ström som ger den önskade effekten.'),step(r'Resistanser i serie: \(R_{\mathrm{tot}}=R_v+2R_l\)',r'R_{\mathrm{tot}}=4{,}0+2\cdot0{,}40=4{,}80\ \Omega','Strömmen går genom både framledningen och återledningen.'),ohm(r'U=2{,}50\cdot4{,}80=12{,}0\ \mathrm V'),step(r'Källans effekt: \(P_{\mathrm{tot}}=UI\)',r'P_{\mathrm{tot}}=12{,}0\cdot2{,}50=30{,}0\ \mathrm W'),step(r'Andel till värmaren: \(\eta=\frac{P_v}{P_{\mathrm{tot}}}\)',r'\eta=\frac{25}{30}\approx0{,}8333','Multiplicera andelen med 100 för procent. Resterande 5 W värmer ledningarna.')],r'Minst \(12{,}0\ \mathrm V\). Värmaren får \(83{,}3\,\%\) av källans effekt.')
setq('8.529',[giv('Källan ger 12 V. Ingen ström går mellan grenarnas mittpunkter. Sökt: R och totalströmmen.'),step('Mittpunkterna har samma potential',why='Nollströmmen innebär att ingen ström överförs mellan grenarna. Därför kan varje gren räknas som två serieresistorer. Spänningen från vardera mittpunkten till den gemensamma nedre punkten är lika stor.'),ohm(r'I_{\mathrm{vänster}}=\frac{12}{6+3}=\frac43\ \mathrm A'),ohm(r'U_{\mathrm{nedre}}=\frac43\cdot3=4\ \mathrm V','Den nedre resistorn i höger gren måste också ha spänningen 4 V.'),ohm(r'I_{\mathrm{höger}}=\frac44=1\ \mathrm A'),step(r'Spänningar i serie: \(U_R=U-U_{\mathrm{nedre}}\)',r'U_R=12-4=8\ \mathrm V'),ohm(r'R=\frac81=8\ \Omega'),step(r'Knutpunktslagen: \(I_{\mathrm{tot}}=I_{\mathrm{vänster}}+I_{\mathrm{höger}}\)',r'I_{\mathrm{tot}}=\frac43+1=\frac73\approx2{,}33\ \mathrm A')],r'\(R=8{,}00\ \Omega\) och totalströmmen är \(2{,}33\ \mathrm A\).')

# Explicitly reviewed hints: replace irrelevant generic Ohm prompts, never infer from text.
hints={
'8.18':['Följ strömvägen i vart och ett av brytarens lägen.','Vad händer med strömvägen när en ledning förbinder R₂:s båda ändar?','Hur beror effekten på strömmen när resistansen är oförändrad?'],
'8.43':['Börja med de två resistorerna mellan samma förgreningspunkter.','Hur kombineras två resistanser vid parallellkoppling?','Vilken ström ger den angivna spänningen över hela resistansen?','Vilket samband kopplar ihop grenens spänning, totalström och ersättningsresistans?','Vilken ström ger den angivna spänningen över resistorn?'],
'8.53':['Ersätt först parallellkopplingen med en enda resistans.','Hur kombineras de två parallella resistanserna?','Hur kombineras resistorn och den givna parallellresistansen när de ligger i serie?','Använd hela kretsens spänning och resistans.','Strömmen genom hela parallellkopplingen och dess resistans är givna.'],
'8.54':['Följ hur strömmen delas vid knutpunkten.','Vad skulle hända med laddningen i knutpunkten om olika mycket kom in och gick ut?','Jämför strömmen in med summan av de tre strömmarna ut.','Jämför grenströmmen med totalströmmen.','Vilka storheter bestämmer strömmen genom var och en av de kvarvarande resistorerna?'],
'8.87':['Jämför vilka två punkter de båda resistorerna är anslutna till.','Vilken spänning ligger mellan grenarnas gemensamma ändpunkter?','Använd spänningen och resistansen för varje gren separat.','Hur kombineras resistanser vid parallellkoppling?'],
'8.90':['Följ strömvägen med öppen respektive sluten brytare.','Vilka resistorer måste strömmen gå genom när brytaren är öppen?','Samma ström går genom båda resistorerna. Använd deras resistanser var för sig.','Vilken resistor förbikopplas av ledningen när brytaren sluts?','Hur beror effekten på strömmen när resistansen är oförändrad?'],
'8.123':['Förenkla först den gren som innehåller två resistorer.','Hur adderas resistanser i serie?','Två lika stora resistanser är parallellkopplade.','Använd hela kretsens givna resistans.'],
'8.127':['Förenkla parallellkopplingen innan du tar med den tredje resistorn.','Vad blir ersättningsresistansen för två lika resistorer parallellt?','Hur kombineras två resistanser som ligger i serie?','Beräkna strömmen genom hela kretsen. Vilken ström går genom den ensamma resistorn?'],
'8.130':['Samma ström går genom båda resistorerna. Fördela källans spänning mellan dem.','Omvandla milliampere till ampere innan du använder resistansen.','Hela spänningen är summan av spänningarna över resistorerna.','Använd resistorns spänning och ström, efter omvandling till ampere.','Använd hela kretsens spänning och ström.'],
'8.133':['Ersätt först de två parallella resistorerna.','Vad blir ersättningsresistansen för två lika resistorer parallellt?','Den ensamma resistorn ligger i serie med parallellkopplingen.','Strömmen och resistansen är givna. Vilket samband ger spänningen?']}
for id,hs in hints.items():
 q=byid[id];assert len(hs)==1+len(q.get('spelDelar',[]))
 for obj,h in zip([q]+q.get('spelDelar',[]),hs):obj['ledtrad']=p(h)
assert len(changes)==26
if __name__=='__main__':save();print('Revised',len(changes),'main tasks and',sum(len(byid[id].get('spelDelar',[])) for id in changes),'cards')
