"""Manuellt skrivna facitplaner: tre kretsanalyser och absorberad dos."""
from render import byid,m,p,inline,solution,multi,save

def step(rule,calc='',why=''):return(rule,(p(why) if why else '')+(m(calc) if calc else ''))
def put(id,steps,answer,hint):
 q=byid[id];q['s']=solution(steps,answer);q['ledtrad']=p(hint)
D=r'Absorberad dos: \(D=\dfrac{E}{m}\)'
ENERGY=r'Lös ut energin: \(E=Dm\)'
MILLI=r'Omvandling: \(1\,\mathrm{Gy}=1000\,\mathrm{mGy}\)'
PHOTO=r'Partikelantal: \(N=\dfrac{E}{E_p}\)'
EV=r'Elektronvolt till joule: \(1\,\mathrm{eV}=1{,}602\cdot10^{-19}\,\mathrm J\)'

put('8.614',[
 step(r'Parallellresistans: \(R_p=\dfrac{R_2R_3}{R_2+R_3}\)',r'R_p=\frac{300\cdot600}{300+600}\,\Omega=200\,\Omega','R₂ och R₃ sitter mellan samma två förgreningspunkter.'),
 step(r'Serieresistans: \(R_{\mathrm{tot}}=R_1+R_p\)',r'R_{\mathrm{tot}}=100+200=300\,\Omega'),
 step(r'Totalström med Ohms lag: \(I=U/R_{\mathrm{tot}}\)',r'I=\frac{12\,\mathrm V}{300\,\Omega}=0{,}040\,\mathrm A'),
 step(r'Spänning över parallellgrenen: \(U_2=IR_p\)',r'U_2=0{,}040\cdot200\,\mathrm V=8{,}0\,\mathrm V','Hela totalströmmen går in i parallellkopplingen. Båda parallella resistorerna har samma spänning.')], '8,0 V över R₂.', 'Vilka resistorer sitter mellan samma två punkter? Bestäm deras gemensamma ersättningsresistans först.')
put('8.615',[
 step(r'Resistans i övre grenen: \(R_{12}=R_1+R_2\)',r'R_{12}=100+200=300\,\Omega','R₁ och R₂ är i serie. Den nedre grenen består av R₃ = 600 Ω.'),
 step(r'Grenströmmar med Ohms lag: \(I=U/R\)',r'\begin{aligned}I_{12}&=\frac{9{,}0}{300}\,\mathrm A=0{,}030\,\mathrm A\\I_3&=\frac{9{,}0}{600}\,\mathrm A=0{,}015\,\mathrm A\end{aligned}','Båda hela grenarna ligger över spänningskällan och har därför spänningen 9,0 V.'),
 step(r'Strömmen före förgreningen: \(I=I_{12}+I_3\)',r'I=0{,}030+0{,}015=0{,}045\,\mathrm A=45\,\mathrm{mA}')], '45 mA lämnar spänningskällan.', 'Bestäm strömmen i varje hel gren. Hur hänger grenströmmarna ihop med strömmen från källan?')
put('8.619',[
 step(r'Parallellresistans: \(R_p=\dfrac{R_2R_3}{R_2+R_3}\)',r'R_p=\frac{30\cdot60}{30+60}\,\Omega=20\,\Omega'),
 step(r'Totalresistans: \(R_{\mathrm{tot}}=R_1+R_p\)',r'R_{\mathrm{tot}}=20+20=40\,\Omega'),
 step(r'Ström genom R₁: \(I=U/R_{\mathrm{tot}}\)',r'I=\frac{12\,\mathrm V}{40\,\Omega}=0{,}30\,\mathrm A','R₁ ligger före förgreningen. Där går hela kretsens ström.'),
 step(r'Effekt i just R₁: \(P_1=I^2R_1\)',r'P_1=(0{,}30)^2\cdot20\,\mathrm W=1{,}8\,\mathrm W','Använd R₁ här, inte kretsens totala resistans.')], '1,8 W utvecklas i R₁.', 'Hitta kretsens totalström. Den går genom R₁ innan den delar upp sig.')

put('9.152',[
 step(D,r'D=\frac{0{,}03\,\mathrm J}{60\,\mathrm{kg}}=0{,}0005\,\mathrm{Gy}','Dela den absorberade energin med den massa som tar upp energin.'),
 step(MILLI,r'D=0{,}0005\cdot1000\,\mathrm{mGy}=0{,}5\,\mathrm{mGy}')], '0,5 mGy.', 'Börja med energin per kilogram. Omvandla sedan från Gy till mGy.')
put('9.153',[
 step(r'Dosens enhet: \(1\,\mathrm{mGy}=1\,\mathrm{mJ/kg}\)',r'D=3{,}5\,\mathrm{mJ/kg}','Dosen anger hur mycket energi varje kilogram tar upp.'),
 step(ENERGY,r'E=3{,}5\,\mathrm{mJ/kg}\cdot2{,}4\,\mathrm{kg}=8{,}4\,\mathrm{mJ}')], '8,4 mJ absorberas.', 'Du känner energin per kilogram och antalet kilogram. Hur får du hela energin?')
put('9.154',[
 step(D,r'D=1{,}8\,\mathrm{mGy}=1{,}8\,\mathrm{mJ/kg}','Både energin och dosen har prefixet milli. De kan användas direkt tillsammans.'),
 step(r'Lös ut massan: \(m=E/D\)',r'm=\frac{4{,}5\,\mathrm{mJ}}{1{,}8\,\mathrm{mJ/kg}}=2{,}5\,\mathrm{kg}')], '2,5 kg.', 'Hur många kilogram kan ta upp den totala energin när du känner energin per kilogram?')
put('9.155',[
 step(D,'','Absorberad dos beskriver absorberad energi per kilogram. Den säger inte hur många kärnor som sönderfaller.'),
 step(r'Enhetssamband: \(1\,\mathrm{Gy}=1\,\mathrm{J/kg}\)','','Enheten kallas gray och förkortas Gy.')], 'gray (Gy).', 'Utgå från vilken enhet energi per kilogram har och vad den dosenheten heter.')
put('9.156',[
 step(r'Definitionen av gray: \(1\,\mathrm{Gy}=1\,\mathrm{J/kg}\)','','En absorberad dos på 1 Gy betyder att varje kilogram i medeltal har tagit upp 1 J strålningsenergi. Det är energi per massa, inte energi per sekund.')], inline(r'1\,\mathrm{J/kg}')+'.', 'Vilka två storheter jämförs när man anger absorberad dos?')
put('9.157',[
 step(MILLI,'','Milli betyder en tusendel. Det går därför tusen milligray på en gray.'),
 step('Skriv samma dos i milligray',r'D=0{,}0065\cdot1000\,\mathrm{mGy}=6{,}5\,\mathrm{mGy}')], '6,5 mGy.', 'När du använder en mindre enhet behövs ett större antal. Vad betyder prefixet milli?')
put('9.158',[
 step(r'Milligray till gray: \(1\,\mathrm{mGy}=10^{-3}\,\mathrm{Gy}\)','','Milli betyder en tusendel.'),
 step('Skriv samma dos i gray',r'D=6\cdot10^{-3}\,\mathrm{Gy}=0{,}006\,\mathrm{Gy}')], '0,006 Gy.', 'När du går från mGy till den större enheten Gy ska talvärdet bli mindre.')
put('9.167',[
 step(r'Aktivitetens enhet: \(1\,\mathrm{Bq}=1\,\mathrm{s^{-1}}\)','','Becquerel anger antalet kärnsönderfall per sekund i en strålkälla.'),
 step(r'Dosens enhet: \(1\,\mathrm{Gy}=1\,\mathrm{J/kg}\)','','Gray anger absorberad energi per kilogram i det som träffas av strålningen. Samma aktivitet behöver inte ge samma dos: bland annat partikelenergi och absorberad andel spelar roll.')], 'Bq mäter sönderfall per sekund; Gy mäter absorberad energi per kilogram.', 'Handlar storheten om strålkällans sönderfall eller om energin som tas upp i kroppen?')
put('9.168',[
 step(r'Dosens enhet: \(1\,\mathrm{mGy}=1\,\mathrm{mJ/kg}\)',r'D=1{,}5\,\mathrm{mJ/kg}'),
 step(ENERGY,r'E=1{,}5\,\mathrm{mJ/kg}\cdot4{,}2\,\mathrm{kg}=6{,}3\,\mathrm{mJ}','Multiplicera energin per kilogram med vävnadens massa.')], '6,3 mJ absorberas.', 'Dosen anger energin per kilogram. Använd vävnadens massa för att få totalenergin.')
put('9.173',[
 step(D,r'D=\frac{0{,}012\,\mathrm J}{60\,\mathrm{kg}}=0{,}0002\,\mathrm{Gy}'),
 step(MILLI,r'D=0{,}0002\cdot1000\,\mathrm{mGy}=0{,}2\,\mathrm{mGy}')], '0,2 mGy.', 'Beräkna dosen i J/kg innan du omvandlar till milligray.')
put('9.362',[
 step(ENERGY,r'E=0{,}25\,\mathrm{J/kg}\cdot75{,}0\,\mathrm{kg}=18{,}75\,\mathrm J','En dos på 0,25 Gy betyder 0,25 J per kilogram.')], '18,75 J, ungefär 19 J.', 'Dosen är energi per kilogram. Hur får du energin för hela kroppen?')
put('9.363',[
 step(r'Värmeenergi: \(E=mc\Delta T\)','','All den absorberade energin blir värme enligt uppgiften.'),
 step(r'Kombinera med \(D=E/m\)',r'D=\frac{mc\Delta T}{m}=c\Delta T','Massan förkortas bort. Dosen anger redan energi per kilogram.'),
 step(r'Lös ut temperaturökningen: \(\Delta T=D/c\)',r'\Delta T=\frac{2{,}00}{4180}\,\mathrm K\approx4{,}78\cdot10^{-4}\,\mathrm K')], inline(r'4{,}78\cdot10^{-4}\,\mathrm K')+' (cirka 0,000478 K).', 'Kombinera sambandet för uppvärmning med dosens definition. Behöver du känna massan?')

# Huvuduppgift och fristående kort har ibland olika givna mellanvärden.
a44=([step('Omvandla den absorberade energin',r'E=3{,}0\,\mathrm{mJ}=3{,}0\cdot10^{-3}\,\mathrm J'),step(D,r'D=\frac{3{,}0\cdot10^{-3}}{60}\,\mathrm{Gy}=5{,}0\cdot10^{-5}\,\mathrm{Gy}'),step(r'Mikrogray: \(1\,\mathrm{Gy}=10^6\,\mathrm{\mu Gy}\)',r'D=5{,}0\cdot10^{-5}\cdot10^6\,\mathrm{\mu Gy}=50\,\mathrm{\mu Gy}')], '50 µGy.')
b44=([step(r'Ekvivalent dos: \(H=w_R D\)',r'H=1\cdot50\,\mathrm{\mu Sv}=50\,\mathrm{\mu Sv}','Gamma har här viktfaktorn 1. Den ekvivalenta dosen får samma talvärde som den absorberade, men enheten är Sv, inte Gy.')], '50 µSv.')
multi('9.44',[a44,b44]);byid['9.44']['ledtrad']=p('Börja med absorberad energi per kilogram. Skilj sedan mellan absorberad och viktad dos.')
byid['9.44']['spelDelar'][0]['ledtrad']=p('Omvandla millijoule till joule innan du beräknar energin per kilogram.')
byid['9.44']['spelDelar'][1]['ledtrad']=p('Hur påverkar strålningens viktfaktor sambandet mellan absorberad och ekvivalent dos?')
a97=([step(D,r'D=\frac{0{,}25\,\mathrm J}{70\,\mathrm{kg}}\approx0{,}00357\,\mathrm{Gy}')], 'Cirka 0,00357 Gy.')
b97=([step(MILLI,r'D=\frac{0{,}25}{70}\cdot1000\,\mathrm{mGy}\approx3{,}57\,\mathrm{mGy}','Behåll den oavrundade kvoten från a) till slutet.')], 'Cirka 3,57 mGy.')
card97=([step(MILLI,r'D=0{,}00357\cdot1000\,\mathrm{mGy}=3{,}57\,\mathrm{mGy}')], '3,57 mGy.')
multi('9.97',[a97,b97],[a97,card97]);byid['9.97']['ledtrad']=p('Beräkna först energin per kilogram. Byt därefter enhet till milligray.')
byid['9.97']['spelDelar'][0]['ledtrad']=p('Hur mycket absorberad energi motsvarar ett kilogram av kroppen?')
byid['9.97']['spelDelar'][1]['ledtrad']=p('Milligray är en mindre enhet än gray. Ska talvärdet då öka eller minska?')

# Fotoner och strålningsenergi: undvik avrundade mellanresultat i nästa steg.
a365=([step(ENERGY,r'E=2000\,\mathrm{J/kg}\cdot0{,}30\,\mathrm{kg}=600\,\mathrm J'),step(EV,r'E_p=100\cdot10^3\cdot1{,}602\cdot10^{-19}\,\mathrm J=1{,}602\cdot10^{-14}\,\mathrm J'),step(PHOTO,r'N=\frac{600}{1{,}602\cdot10^{-14}}\approx3{,}75\cdot10^{16}')], 'Cirka '+inline(r'3{,}75\cdot10^{16}')+' fotoner.')
b365=([step(r'Värmeenergi och dos: \(E=mc\Delta T\), \(D=E/m\)',r'D=c\Delta T','Dos är energi per kilogram. Därför behövs inte massan för att bestämma temperaturökningen.'),step(r'Temperaturökning: \(\Delta T=D/c\)',r'\Delta T=\frac{2000}{4180}\,\mathrm K\approx0{,}478\,\mathrm K')], 'Cirka 0,478 K (lika stor temperaturökning i °C).')
multi('9.365',[a365,b365]);byid['9.365']['spelDelar'][1]['ledtrad']=p('Skriv energin för uppvärmning och dosens definition. Vilken storhet kan förkortas bort?')
put('9.368',[
 step('Tid i sekunder och aktivitet i Bq',r'\begin{aligned}t&=24\cdot60\cdot60\,\mathrm s=86400\,\mathrm s\\A&=57{,}4\cdot10^3\,\mathrm{s^{-1}}\end{aligned}'),
 step(r'Absorberade fotoner: \(N=0{,}5At\)',r'N=0{,}5\cdot57400\cdot86400=2{,}47968\cdot10^9','Aktiviteten är konstant enligt modellen. Varje sönderfall ger en foton och hälften absorberas.'),
 step(EV,r'E_p=122\cdot10^3\cdot1{,}602\cdot10^{-19}\,\mathrm J=1{,}95444\cdot10^{-14}\,\mathrm J'),
 step(r'Absorberad energi: \(E=NE_p\)',r'\begin{aligned}E&=(2{,}47968\cdot10^9)\\&\quad\cdot(1{,}95444\cdot10^{-14})\,\mathrm J\\&=4{,}8463857792\cdot10^{-5}\,\mathrm J\end{aligned}'),
 step(D,r'\begin{aligned}D&=\frac{4{,}8463857792\cdot10^{-5}}{65}\,\mathrm{Gy}\\&\approx7{,}46\cdot10^{-7}\,\mathrm{Gy}\end{aligned}')], 'Cirka '+inline(r'7{,}46\cdot10^{-7}\,\mathrm{Gy}')+' (0,746 µGy).', 'Räkna först hur många fotoner som absorberas under ett dygn. Vilken energi tar de tillsammans med sig?')
put('9.369',[
 step('Omvandla kilogray till gray',r'D=4{,}5\,\mathrm{kGy}=4500\,\mathrm{Gy}'),
 step(ENERGY,r'E=4500\,\mathrm{J/kg}\cdot5{,}0\,\mathrm{kg}=22500\,\mathrm J'),
 step(EV,r'E_p=1{,}6\cdot10^6\cdot1{,}602\cdot10^{-19}\,\mathrm J=2{,}5632\cdot10^{-13}\,\mathrm J'),
 step(PHOTO,r'N=\frac{22500}{2{,}5632\cdot10^{-13}}\approx8{,}78\cdot10^{16}')], 'Cirka '+inline(r'8{,}78\cdot10^{16}')+' betapartiklar.', 'Bestäm hela den absorberade energin. Jämför den med energin från en enda partikel.')

a373=([
 step(r'Sönderfallskonstant: \(\lambda=\ln 2/T_{1/2}\)',r'\begin{aligned}\lambda&=\frac{\ln2}{14{,}3\cdot86400}\,\mathrm{s^{-1}}\\&\approx5{,}61\cdot10^{-7}\,\mathrm{s^{-1}}\end{aligned}','Aktiviteten är given per sekund, så halveringstiden behöver uttryckas i sekunder.'),
 step(r'Startantal från aktiviteten: \(A_0=\lambda N_0\)',r'\begin{aligned}N_0&=\frac{1{,}31\cdot10^6}{\ln2/(14{,}3\cdot86400)}\\&\approx2{,}34\cdot10^{12}\end{aligned}'),
 step(r'Sönderfallna kärnor: \(\Delta N=N_0-N(t)\)',r'\begin{aligned}\Delta N&=N_0\left(1-2^{-10/14{,}3}\right)\\&\approx8{,}97\cdot10^{11}\end{aligned}','Antalet kvarvarande kärnor minskar under tiden. Använd startantalet utan mellanavrundning. Ett sönderfall ger en betapartikel; startaktiviteten gånger tiden skulle överskatta antalet.')], 'Cirka '+inline(r'8{,}97\cdot10^{11}')+' betapartiklar.')
b373=([step(EV,r'E_p=700\cdot10^3\cdot1{,}602\cdot10^{-19}\,\mathrm J=1{,}1214\cdot10^{-13}\,\mathrm J'),step(r'Sammanlagd energi: \(E=\Delta N E_p\)',r'\begin{aligned}E&\approx(8{,}969600427\cdot10^{11})\\&\quad\cdot(1{,}1214\cdot10^{-13})\,\mathrm J\\&\approx0{,}100585\,\mathrm J\end{aligned}','Använd det oavrundade antalet från a). Här visas extra siffror för att göra mellanledet tydligt.')], 'Cirka 0,101 J.')
c373=([step('Omvandla vävnadens massa',r'm=100\,\mathrm g=0{,}100\,\mathrm{kg}'),step(D,r'D\approx\frac{0{,}100585}{0{,}100}\,\mathrm{Gy}\approx1{,}01\,\mathrm{Gy}','All avgiven energi absorberas enligt uppgiften. Använd energin från b) utan mellanavrundning.')], 'Cirka 1,01 Gy.')
b373card=([step(EV,r'E_p=700\cdot10^3\cdot1{,}602\cdot10^{-19}\,\mathrm J=1{,}1214\cdot10^{-13}\,\mathrm J'),step(r'Sammanlagd energi: \(E=NE_p\)',r'E=8{,}97\cdot10^{11}\cdot1{,}1214\cdot10^{-13}\,\mathrm J=0{,}10058958\,\mathrm J')], 'Cirka 0,101 J.')
c373card=([step('Omvandla vävnadens massa',r'm=100\,\mathrm g=0{,}100\,\mathrm{kg}'),step(D,r'D=\frac{0{,}101\,\mathrm J}{0{,}100\,\mathrm{kg}}=1{,}01\,\mathrm{Gy}')], '1,01 Gy.')
multi('9.373',[a373,b373,c373],[a373,b373card,c373card]);byid['9.373']['ledtrad']=p('Aktiviteten avtar under tiden. Jämför antalet kärnor från början med antalet som finns kvar efter 10 dygn.')
byid['9.373']['spelDelar'][0]['ledtrad']=byid['9.373']['ledtrad']
byid['9.373']['spelDelar'][1]['ledtrad']=p('Uttryck energin per partikel i joule och multiplicera med antalet partiklar.')
byid['9.373']['spelDelar'][2]['ledtrad']=p('Dosen anger energi per kilogram, så börja med att uttrycka massan i kilogram.')
a380=([step(D,r'D=\frac{1{,}7\,\mathrm J}{0{,}12\,\mathrm{kg}}\approx14{,}2\,\mathrm{Gy}')], 'Cirka 14,2 Gy.')
b380=([step(ENERGY,r'E_2=\frac{1{,}7}{0{,}12}\cdot0{,}15\,\mathrm J=2{,}125\,\mathrm J','Samma dos betyder samma energi per kilogram. Använd den oavrundade dosen från a).')], '2,125 J (cirka 2,13 J).')
b380card=([step(ENERGY,r'E=14\,\mathrm{J/kg}\cdot0{,}15\,\mathrm{kg}=2{,}1\,\mathrm J','Kortet anger dosen 14 Gy. Använd detta givna värde.')], '2,1 J.')
multi('9.380',[a380,b380],[a380,b380card]);byid['9.380']['ledtrad']=p('Samma dos betyder samma energi per kilogram, även om massorna skiljer sig.')
byid['9.380']['spelDelar'][0]['ledtrad']=p('Jämför den absorberade energin med tumörens massa.')
byid['9.380']['spelDelar'][1]['ledtrad']=p('Dosen anger energin per kilogram. Hur mycket energi tar hela tumören upp?')
put('9.383',[
 step(r'Tre energibidrag: \(E=ml_s+mc\Delta T+ml_v\)','','Först smälter isen vid 0 °C. Sedan värms vattnet till 100 °C. Till sist förångas vattnet vid 100 °C. Temperaturen ändras inte under själva fasövergångarna.'),
 step(r'Energi per kilogram: \(D=E/m=l_s+c\Delta T+l_v\)',r'\begin{aligned}D&=334+4{,}18\cdot100+2260\\&=3012\,\mathrm{kJ/kg}\end{aligned}','Massan förkortas bort i alla tre bidragen.'),
 step(r'Dos i gray: \(1\,\mathrm{Gy}=1\,\mathrm{J/kg}\)',r'D=3012\cdot1000\,\mathrm{J/kg}=3{,}012\cdot10^6\,\mathrm{Gy}')], inline(r'3{,}012\cdot10^6\,\mathrm{Gy}')+' (ungefär 3,0 MGy).', 'Vilka tre steg krävs för att gå från is till vattenånga? Summera deras energibehov per kilogram.')
# Fem närliggande instrumentuppgifter: matematiken stämmer men facitmallen saknades.
put('8.608',[
 step(r'Grenströmmar med Ohms lag: \(I=U/R\)',r'\begin{aligned}I_1&=\frac{12}{60}\,\mathrm A=0{,}20\,\mathrm A\\I_2&=\frac{12}{120}\,\mathrm A=0{,}10\,\mathrm A\end{aligned}','Resistorerna är parallellkopplade. Båda har 12 V över sig.'),
 step(r'Totalström: \(I=I_1+I_2\)',r'I=0{,}20+0{,}10=0{,}30\,\mathrm A=300\,\mathrm{mA}','Amperemetern sitter där hela strömmen passerar, innan den delas mellan grenarna.')], 'Amperemetern visar 300 mA.', 'Har resistorerna samma ström eller samma spänning? Vilken ström passerar amperemetern?')
put('8.609',[
 step(r'Lampans ström från \(P=UI\)',r'I_L=\frac{P}{U}=\frac{1{,}8}{6{,}0}\,\mathrm A=0{,}30\,\mathrm A','Lampan och resistorn är parallellkopplade. Båda har spänningen 6,0 V.'),
 step(r'Resistorns ström: \(I_R=U/R\)',r'I_R=\frac{6{,}0\,\mathrm V}{60\,\Omega}=0{,}10\,\mathrm A'),
 step(r'Totalström: \(I=I_L+I_R\)',r'I=0{,}30+0{,}10=0{,}40\,\mathrm A','Amperemetern mäter strömmen genom båda grenarna tillsammans.')], 'Amperemetern visar 0,40 A.', 'Använd lampans effekt för dess ström och resistansen för den andra grenens ström.')
put('8.611',[
 step(r'Ström genom R₂: \(I=U_2/R_2\)',r'I=\frac{4{,}4\,\mathrm V}{220\,\Omega}=0{,}020\,\mathrm A','Voltmetern är kopplad över R₂. Seriekopplingen innebär att samma ström går genom R₁.'),
 step(r'Källans spänning: \(U=I(R_1+R_2)\)',r'U=0{,}020\cdot(330+220)\,\mathrm V=11\,\mathrm V','Källans spänning fördelas över båda resistorerna, medan mätaren bara visar en av delspänningarna.')], 'Spänningskällan ger 11 V.', 'Vilken resistor ligger voltmetern över? Börja med strömmen genom den resistorn.')
put('8.612',[
 step(r'Serieresistans: \(R_{\mathrm{tot}}=R_1+R_2+R_3\)',r'R_{\mathrm{tot}}=100+200+300=600\,\Omega'),
 step(r'Kretsens ström: \(I=U/R_{\mathrm{tot}}\)',r'I=\frac{12\,\mathrm V}{600\,\Omega}=0{,}020\,\mathrm A'),
 step(r'Mätspänning: \(U_V=I(R_2+R_3)\)',r'U_V=0{,}020\cdot(200+300)\,\mathrm V=10\,\mathrm V','Följ voltmeterns ledningar: de ansluter på var sin sida om R₂ och R₃ tillsammans.')], 'Voltmetern visar 10 V.', 'Följ voltmeterns båda ledningar och se vilka resistorer som ligger mellan anslutningarna.')
put('8.613',[
 step(r'Parallellresistans: \(\dfrac1{R_e}=\dfrac1{R_1}+\dfrac1{R_2}+\dfrac1{R_3}\)',r'\frac1{R_e}=\frac1{120}+\frac1{240}+\frac1{80}=\frac1{40}\quad\Rightarrow\quad R_e=40\,\Omega','Alla tre resistorerna sitter mellan samma två punkter.'),
 step(r'Källans spänning: \(U=IR_e\)',r'U=0{,}30\,\mathrm A\cdot40\,\Omega=12\,\mathrm V','Amperemetern visar totalströmmen. Använd därför hela kopplingens ersättningsresistans.')], 'Spänningskällan ger 12 V.', 'Amperemetern visar hela kretsens ström. Vilken resistans ska paras ihop med den strömmen?')
save()
