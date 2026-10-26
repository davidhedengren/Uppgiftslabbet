"""Individuellt skrivna facit för första ordningens differentialekvationer."""
import json,math,importlib.util
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fields',ROOT/'tools/revidera-ma3-facitstruktur-2026-10-25.py');fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)
D={};PARTS={}
def solution(steps,answer):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+escape(h)+'</p>'+b+'</li>' for h,b in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def add(id,hint,steps,answer,**meta):D[id]=dict(s=solution(steps,answer),ledtrad='<p>'+hint+'</p>',**meta)
add('4.48',r'Vad blir exponentialfaktorn när x=0?',[
 ('Använd startvärdet i den givna familjen',r'\[5=Ce^{2\cdot0}=C\]'),
 ('Sätt tillbaka C i funktionsuttrycket',r'\[y=5e^{2x}\]<p>Vid x=0 blir värdet 5, som villkoret kräver.</p>')],r'\(y=5e^{2x}\).',traningsniva=1)
add('4.03',r'Vilken exponentialfunktion får faktorn 3 när den deriveras?',[
 ('Känn igen exponentialekvationen',r'<p>I y′=ky är k=3. Lösningarna har därför formen</p>\[y=Ce^{3x}\]'),
 ('Kontrollera att alla C fungerar',r'\[y^{\prime}=3Ce^{3x}=3y\]<p>C är en valfri reell konstant, även 0.</p>')],r'\(y=Ce^{3x}\), där C är valfri.',svarFormat='diffekv_losning')
add('4.358',r'Samla y och dy på ena sidan och x och dx på den andra. Kontrollera även lösningen som kan förloras när du dividerar med y.',[
 ('Separera när y inte är noll',r'\[\frac{dy}{y}=3x\,dx\]'),
 ('Integrera båda leden',r'\[\ln|y|=\frac32x^2+K\]'),
 ('Skriv exponentialformen och ta med nollösningen',r'<p>Exponentiering ger |y|=\(e^K e^{3x^2/2}\). Tecknet på y och den positiva faktorn eᴷ samlas i en konstant C.</p>\[y=Ce^{3x^2/2}\]<p>Separationen uteslöt y=0. Direkt insättning visar att även den är en lösning, så C får också vara 0.</p>'),
 ('Kontrollera med kedjeregeln',r'\[y^{\prime}=Ce^{3x^2/2}\cdot3x=3xy\]')],r'\(y=Ce^{3x^2/2}\), där C är valfri reell konstant.',svarFormat='diffekv_losning',niva='C',poang='0/2/0',traningsniva=3)
add('4.50',r'Lös först exponentialekvationen. Vid x=0 blir exponentialfaktorn 1.',[
 ('Använd koefficienten −0,5 i exponenten',r'\[y=Ce^{-0{,}5x}\]'),
 ('Välj C med startvärdet 12',r'\[12=Ce^0=C\]'),
 ('Kontrollera funktionen',r'<p>För y=12e⁻⁰˒⁵ˣ är y(0)=12 och y′=−6e⁻⁰˒⁵ˣ=−0,5y.</p>')],r'\(y=12e^{-0{,}5x}\).')
add('4.67',r'Jämför med y′=ky. Vilket tecken ska exponentens koefficient ha?',[
 ('Använd koefficienten −4',r'\[y=Ce^{-4x}\]'),
 ('Kontrollera genom derivering',r'\[y^{\prime}=-4Ce^{-4x}=-4y\]<p>Det gäller för alla reella C, även 0. Om C är negativ närmar sig funktionen noll underifrån.</p>')],r'\(y=Ce^{-4x}\), där C är valfri.',svarFormat='diffekv_losning')
add('4.68',r'Koefficienten i differentialekvationen bestämmer exponenten. Startvärdet bestämmer faktorn framför.',[
 ('Skriv lösningsfamiljen för k=0,3',r'\[y=Ce^{0{,}3x}\]'),
 ('Använd y(0)=7',r'\[7=Ce^0=C\]'),
 ('Kontrollera derivatan och startvärdet',r'\[y^{\prime}=2{,}1e^{0{,}3x}=0{,}3y\]\[y(0)=7\]')],r'\(y=7e^{0{,}3x}\).')
add('4.69',r'Använd först startvärdet för att bestämma faktorn framför exponentialfunktionen. Det andra värdet ger en ekvation för k.',[
 ('Låt startvärdet bestämma C',r'\[y=Ce^{kx},\qquad y(0)=C=12\]'),
 ('Använd värdet vid x=5',r'\[18=12e^{5k}\]\[e^{5k}=\frac{18}{12}=1{,}5\]'),
 ('Logaritmera och dividera med 5',r'\[5k=\ln1{,}5\]\[k=\frac{\ln1{,}5}{5}\approx0{,}081093\]<p>k är positivt, vilket stämmer med att y ökar från 12 till 18.</p>')],r'\(k=\ln(1{,}5)/5\approx0{,}0811\).',rättSvar=math.log(1.5)/5,tolerans=0,niva='E',poang='3/0/0',traningsniva=2)
add('4.120',r'Sätt in den givna punkten och dividera bort exponentialfaktorn.',[
 ('Sätt in x=1 och y=10',r'\[10=Ce^{2\cdot1}=Ce^2\]'),
 ('Dividera båda leden med e²',r'\[C=\frac{10}{e^2}\approx1{,}35335\]<p>Insättning ger (10/e²)·e²=10.</p>')],r'\(C=10/e^2\approx1{,}35\).',rättSvar=10/math.e**2,svarstyp='numeriskt',svarFormat='numeriskt',tolerans=0,traningsniva=2)
add('4.396',r'Använd startvärdet för att bestämma exponentialfunktionens faktor innan du sätter in x=1.',[
 ('Lös y′=y och välj C',r'\[y=Ce^x,\qquad 2=Ce^0=C\]'),
 ('Beräkna värdet efter ett x-steg',r'\[y(1)=2e^1=2e\approx5{,}43656\]')],r'\(y(1)=2e\approx5{,}44\).',tolerans=0)
add('4.399',r'Börja med punkten där x=0. Använd sedan den andra punkten för att bestämma exponentens koefficient.',[
 ('Bestäm C från y(0)=6',r'\[6=Ce^0=C\]'),
 ('Bestäm k från y(1)=12',r'\[12=6e^k\]\[e^k=2\quad\Rightarrow\quad k=\ln2\]'),
 ('Kontrollera båda punkterna',r'\[y(0)=6,\qquad y(1)=6e^{\ln2}=12\]')],r'\(C=6\) och \(k=\ln2\approx0{,}6931\).',spel=True,självrättning=[True,True],svarstyp='flera_delar',rättSvar=[6,math.log(2)],tolerans=[0,0],svarFormat=['numeriskt','numeriskt'],svarsstruktur='ordnad',svarEtiketter=['C','k'],niva='E',poang='2/0/0',traningsniva=2)
add('4.124',r'Vilken exponentialfunktion har derivatan två gånger funktionen? Använd sedan startvärdet.',[
 ('Skriv familjen för y′=2y',r'\[y=Ce^{2x}\]'),
 ('Använd startvärdet 3',r'\[3=Ce^0=C\]'),
 ('Kontrollera den valda lösningen',r'\[y^{\prime}=6e^{2x}=2y,\qquad y(0)=3\]')],r'\(y=3e^{2x}\).',traningsniva=2)
add('4.125',r'Lösningen är exponentiell. Startvärdet ger faktorn framför exponentialuttrycket.',[
 ('Skriv familjen med negativ exponent',r'\[y=Ce^{-0{,}5x}\]'),
 ('Välj C så att y(0)=8',r'\[8=Ce^0=C\]'),
 ('Kontrollera koefficienten efter derivering',r'\[y^{\prime}=-4e^{-0{,}5x}=-0{,}5y\]')],r'\(y=8e^{-0{,}5x}\).',traningsniva=2)
add('4.515',r'Uttryck den kvarvarande andelen med en exponentialfunktion. Använd halveringstiden för att bestämma k innan du löser ut åldern.',[
 ('Beskriv den kvarvarande andelen',r'\[y=y_0e^{-kt},\qquad \frac{y}{y_0}=e^{-kt}\]'),
 ('Bestäm k från en halvering',r'\[e^{-5730k}=\frac12\]\[-5730k=\ln(1/2)=-\ln2\]\[k=\frac{\ln2}{5730}\]'),
 ('Lös för tiden när 30 procent återstår',r'\[e^{-kt}=0{,}30\]\[t=\frac{-\ln0{,}30}{k}\]\[=5730\frac{\ln(1/0{,}30)}{\ln2}\]\[\approx9952{,}81\text{ år}\]'),
 ('Avrunda till tiotal och kontrollera storleken',r'<p>Det blir 9 950 år. Eftersom 30 % ligger mellan 50 % och 25 % ska åldern ligga mellan en och två halveringstider, alltså mellan 5 730 och 11 460 år.</p>')],r'Cirka 9 950 år.',niva='C',poang='0/3/0',traningsniva=3,svarFormat='numeriskt',tolerans=5)
add('4.516',r'Bestäm faktorn framför exponentialfunktionen med startvärdet. Sätt sedan in x=4 utan att avrunda i förväg.',[
 ('Lös ekvationen och använd y(0)=50',r'\[y=Ce^{-0{,}3x},\qquad C=50\]'),
 ('Beräkna det efterfrågade värdet',r'\[y(4)=50e^{-0{,}3\cdot4}\]\[=50e^{-1{,}2}\approx15{,}05971\]')],r'\(y(4)\approx15{,}06\).',niva='E',poang='2/0/0',traningsniva=2,svarFormat='numeriskt',tolerans=.005)
add('4.520',r'Fördubblingen ger ett samband för k. Behåll det exakta värdet när du räknar ut den längre tiden.',[
 ('Använd en fördubbling på 20 minuter',r'\[y=y_0e^{kt}\]\[2y_0=y_0e^{20k}\]\[20k=\ln2\quad\Rightarrow\quad k=\frac{\ln2}{20}\]\[k\approx0{,}0347\text{ min}^{-1}\]'),
 ('Lös för tillväxtfaktorn 1 000',r'\[e^{kt}=1000\]\[t=\frac{\ln1000}{\ln2/20}\]\[\approx199{,}3157\text{ min}\]'),
 ('Kontrollera med antalet fördubblingar',r'<p>Tio fördubblingar ger faktorn 2¹⁰=1 024 på 200 minuter. Svaret ska därför ligga strax under 200 minuter.</p>')],r'\(k\approx0{,}0347\) per minut och tiden är cirka 199,3 minuter.',niva='C',poang='0/3/0',traningsniva=3,svarFormat=['numeriskt','numeriskt'],tolerans=[.00005,.05],svarEnhet=['min^-1','min'])
add('4.556',r'Låt tiden noll vara när Bertil börjar elda. Den andra temperaturmätningen bestämmer k.',[
 ('Använd den angivna temperaturmodellen',r'\[y=Ce^{kt},\qquad C=y(0)=14\]'),
 ('Bestäm k från mätningen efter två timmar',r'\[17=14e^{2k}\]\[2k=\ln(17/14)\]\[k=\frac{\ln(17/14)}2\]'),
 ('Lös för tiden då temperaturen är 20 °C',r'\[20=14e^{kt}\]\[t=\frac{\ln(20/14)}{\ln(17/14)/2}\]\[\approx3{,}6741\text{ h}\]<p>Detta är tiden från det att eldningen började, inte ytterligare tid efter mätningen.</p>')],r'Cirka 3,7 timmar efter att eldningen började.',rättSvar=2*math.log(20/14)/math.log(17/14),tolerans=.05,niva='C',poang='0/3/0',traningsniva=3)
add('4.557',r'Vid exponentiell tillväxt ger lika långa tidsintervall samma förändringsfaktor. Hur många åttatimmarsperioder ryms i ett dygn?',[
 ('Beräkna förändringsfaktorn på åtta timmar',r'\[\frac{500}{200}=2{,}5\]'),
 ('Använd samma faktor under tre perioder',r'\[24/8=3\]\[N(24)=200\cdot2{,}5^3=3125\]<p>Efter 8, 16 och 24 timmar ger modellen 500, 1 250 respektive 3 125 bakterier.</p>')],r'3 125 bakterier enligt modellen.',tolerans=0)
add('4.559',r'Beräkna först tidsintervallet mellan inventeringarna. Jämför sedan antalet par med startvärdet.',[
 ('Räkna tiden från 1960',r'\[2008-1960=48\text{ år}\]\[N=20e^{kt}\]'),
 ('Använd ökningen till 4 000 par',r'\[4000=20e^{48k}\]\[e^{48k}=200\]'),
 ('Logaritmera och dividera med 48',r'\[k=\frac{\ln200}{48}\approx0{,}1103816\]')],r'\(k\approx0{,}110\) per år.',rättSvar=math.log(200)/48,tolerans=.0005,svarEnhet='år^-1')
add('4.560',r'Använd en exponentialfunktion med negativ exponent. Starttrycket kan förkortas när du använder halveringen.',[
 ('Skriv trycket som funktion av höjden',r'\[p=p_0e^{-kx}\]'),
 ('Använd att trycket halveras på 5,50 km',r'\[p_0/2=p_0e^{-5{,}50k}\]\[1/2=e^{-5{,}50k}\]'),
 ('Logaritmera och lös ut k',r'\[-\ln2=-5{,}50k\]\[k=\frac{\ln2}{5{,}50}\approx0{,}1260268\]')],r'\(k\approx0{,}126\ \text{km}^{-1}\).',rättSvar=math.log(2)/5.5,tolerans=.0005,svarEnhet='km^-1')
# Manuella delfacit: inget kort visar andra delens slutsvar.
a=solution([('Använd proportionaliteten i tillväxten',r'\[N^{\prime}=0{,}05N\]\[N=Ce^{0{,}05t}\]'),('Bestäm C från startantalet',r'\[1500=Ce^0=C\]')],r'\(N(t)=1500e^{0{,}05t}\).')
b=solution([('Använd modellen vid t=7',r'\[N(7)=1500e^{0{,}05\cdot7}\]\[=1500e^{0{,}35}\approx2128{,}60\]'),('Avrunda till närmaste hundratal',r'<p>2 128,60 ligger närmare 2 100 än 2 200.</p>')],r'Cirka 2 100 bakterier.')
D['4.554']=dict(s='<h4>a)</h4>'+a+'<h4>b)</h4>'+b,ledtrad='<p>Använd proportionaliteten för att skriva differentialekvationen. Startantalet bestämmer konstanten.</p>',traningsniva=2,rättSvar=['1500*e^(0.05t)',1500*math.exp(.35)],tolerans=[None,50])
PARTS['4.554']=[dict(s=a,ledtrad='<p>Vilken typ av funktion har en derivata som är proportionell mot funktionen själv?</p>',traningsniva=2),dict(s=b,ledtrad='<p>Sätt in tiden i modellen och avrunda först på slutet.</p>',traningsniva=2)]
a=solution([('Välj faktorn med startantalet 14',r'\[N=Ce^{0{,}05t},\qquad C=14\]'),('Beräkna antalet efter sju år',r'\[N(7)=14e^{0{,}35}\approx19{,}87\]')],r'Cirka 20 lodjur.')
b=solution([('Använd båda inventeringarna',r'\[N=14e^{kt}\]\[122=14e^{7k}\]'),('Förkorta startantalet och logaritmera',r'\[e^{7k}=122/14\]\[7k=\ln(122/14)\]\[k=\frac{\ln(122/14)}7\approx0{,}30928\]')],r'\(k\approx0{,}31\) per år.')
D['4.558']=dict(s='<h4>a)</h4>'+a+'<h4>b)</h4>'+b,ledtrad='<p>Startantalet bestämmer faktorn framför exponentialfunktionen. I den andra delen behöver du också bestämma k.</p>',rättSvar=[14*math.exp(.35),math.log(122/14)/7],tolerans=[.5,.005])
PARTS['4.558']=[dict(s=a,ledtrad='<p>Bestäm funktionen med det givna k-värdet och startantalet. Sätt sedan in sju år.</p>',traningsniva=2),dict(s=b,ledtrad='<p>Jämför det nya antalet med startantalet. Logaritmera för att lösa ut k.</p>')]
add('4.362',r'Bestäm först den konstanta lösningen. Vilken differentialekvation gäller för avvikelsen från detta värde?',[
 ('Hitta den konstanta lösningen',r'\[0=5-2y\quad\Rightarrow\quad y=\frac52\]'),
 ('Beskriv avvikelsen från 5/2',r'<p>Sätt u=y−5/2. Då är u′=y′ och</p>\[u^{\prime}=5-2(u+5/2)=-2u\]\[u=Ce^{-2x}\]'),
 ('Återgå till y',r'\[y=\frac52+Ce^{-2x}\]<p>C får väljas fritt. C=0 ger den konstanta lösningen.</p>')],r'\(y=5/2+Ce^{-2x}\).',svarFormat='diffekv_losning')
add('4.09',r'Lös först den homogena ekvationen. Pröva sedan en linjär funktion för den del som orsakas av x-termen.',[
 ('Lös ekvationen utan x-termen',r'\[y_h^{\prime}=3y_h\quad\Rightarrow\quad y_h=Ce^{3x}\]'),
 ('Sätt in en linjär partikulärlösning',r'\[y_p=ax+b,\qquad y_p^{\prime}=a\]\[a=3(ax+b)-x\]\[a=(3a-1)x+3b\]'),
 ('Jämför x-termer och konstanter',r'\[3a-1=0\quad\Rightarrow\quad a=\frac13\]\[a=3b\quad\Rightarrow\quad b=\frac19\]'),
 ('Addera de två delarna',r'\[y=Ce^{3x}+\frac{x}{3}+\frac19\]<p>Kontroll: y′=3Ce³ˣ+1/3, vilket också fås av 3y−x.</p>')],r'\(y=Ce^{3x}+x/3+1/9\).',svarFormat='diffekv_losning')
add('4.21',r'Använd högerledets exponentialform för partikulärlösningen, men låt koefficienten vara okänd tills du satt in den.',[
 ('Lös den homogena ekvationen',r'\[y_h^{\prime}-2y_h=0\quad\Rightarrow\quad y_h=Ce^{2x}\]'),
 ('Pröva yₚ=Ae³ˣ och derivera',r'\[y_p^{\prime}=3Ae^{3x}\]\[y_p^{\prime}-2y_p=(3A-2A)e^{3x}\]'),
 ('Bestäm A från högerledet',r'\[Ae^{3x}=e^{3x}\quad\Rightarrow\quad A=1\]'),
 ('Addera homogen och partikulär lösning',r'\[y=Ce^{2x}+e^{3x}\]')],r'\(y=Ce^{2x}+e^{3x}\).',svarFormat='diffekv_losning')
add('4.51',r'En konstant funktion kan ge högerledet 6. Lägg till den homogena lösningen för att få alla lösningar.',[
 ('Lös den homogena ekvationen y′+2y=0',r'\[y_h=Ce^{-2x}\]'),
 ('Bestäm den konstanta partikulärlösningen',r'\[y_p=A,\qquad y_p^{\prime}=0\]\[2A=6\quad\Rightarrow\quad A=3\]'),
 ('Addera och kontrollera',r'\[y=Ce^{-2x}+3\]\[y^{\prime}+2y\]\[=-2Ce^{-2x}+2(Ce^{-2x}+3)\]\[=6\]')],r'\(y=Ce^{-2x}+3\).',svarFormat='diffekv_losning')
add('4.71',r'Bestäm den konstanta lösningen och den homogena delen. Startvärdet väljer sedan en enda funktion.',[
 ('Lös y′+2y=10 utan startvillkor',r'<p>Den konstanta lösningen uppfyller 2A=10, alltså A=5. Den homogena delen är Ce⁻²ˣ.</p>\[y=5+Ce^{-2x}\]'),
 ('Använd y(0)=1',r'\[1=5+C\quad\Rightarrow\quad C=-4\]'),
 ('Kontrollera villkoret',r'\[y(0)=5-4=1\]')],r'\(y=5-4e^{-2x}\).')
add('4.94',r'Börja med den konstanta lösningen. Det är avvikelsen från den som följer en homogen exponentialekvation.',[
 ('Bestäm jämviktsvärdet',r'\[0=8-2A\quad\Rightarrow\quad A=4\]'),
 ('Lös för avvikelsen från 4',r'<p>Om u=y−4 blir u′=−2u. Därför är u=Ce⁻²ˣ.</p>\[y=4+Ce^{-2x}\]'),
 ('Kontrollera att högerledet ger derivatan',r'\[8-2(4+Ce^{-2x})\]\[=-2Ce^{-2x}=y^{\prime}\]')],r'\(y=4+Ce^{-2x}\).',svarFormat='diffekv_losning')
add('4.95',r'Hitta först den konstanta lösningen. Startvärdet bestämmer sedan avvikelsen från den.',[
 ('Bestäm jämvikten och lösningsfamiljen',r'\[0=6-3A\quad\Rightarrow\quad A=2\]<p>Avvikelsen från 2 följer u′=−3u.</p>\[y=2+Ce^{-3x}\]'),
 ('Välj konstanten med y(0)=5',r'\[5=2+C\quad\Rightarrow\quad C=3\]'),
 ('Kontrollera startvärdet och riktningen',r'<p>y(0)=2+3=5. Lösningen minskar mot 2, som stämmer med att y′ är negativt när y är större än 2.</p>')],r'\(y=2+3e^{-3x}\).')
add('4.142',r'Pröva en konstant partikulärlösning. Var noga med minustecknet framför 2y.',[
 ('Lös y′−2y=0',r'\[y_h=Ce^{2x}\]'),
 ('Sätt in en konstant för den andra delen',r'\[y_p=A\quad\Rightarrow\quad -2A=8\]\[A=-4\]'),
 ('Sätt ihop lösningen och kontrollera',r'\[y=Ce^{2x}-4\]\[y^{\prime}-2y\]\[=2Ce^{2x}-2(Ce^{2x}-4)=8\]')],r'\(y=Ce^{2x}-4\).',svarFormat='diffekv_losning')
add('4.143',r'Vilket konstant värde gör högerledet noll? Beskriv sedan avvikelsen från det värdet.',[
 ('Bestäm jämviktsvärdet',r'\[0=0{,}5A-3\quad\Rightarrow\quad A=6\]'),
 ('Lös ekvationen för avvikelsen',r'<p>Med u=y−6 får vi u′=0,5u. Därför är u=Ce⁰˒⁵ˣ.</p>\[y=6+Ce^{0{,}5x}\]'),
 ('Tolka den positiva exponenten',r'<p>Om C inte är noll växer avståndet från jämvikten när x ökar. Bara C=0 ger en konstant funktion.</p>')],r'\(y=Ce^{0{,}5x}+6\).',svarFormat='diffekv_losning')
add('4.145',r'Pröva en linjär partikulärlösning och jämför x-termerna respektive konstanterna efter insättning.',[
 ('Lös den homogena delen',r'\[y_h^{\prime}=2y_h\quad\Rightarrow\quad y_h=Ce^{2x}\]'),
 ('Sätt in yₚ=ax+b',r'\[a=2(ax+b)+4x-1\]\[a=(2a+4)x+2b-1\]'),
 ('Bestäm a och b var för sig',r'\[2a+4=0\quad\Rightarrow\quad a=-2\]\[-2=2b-1\quad\Rightarrow\quad b=-\frac12\]'),
 ('Addera homogen och partikulär lösning',r'\[y=Ce^{2x}-2x-\frac12\]')],r'\(y=Ce^{2x}-2x-1/2\).',svarFormat='diffekv_losning')
add('4.397',r'Avvikelsen från jämviktsvärdet följer en homogen ekvation. Använd startvärdet innan du beräknar y(2).',[
 ('Lös för avvikelsen från 6',r'\[y=6+Ce^{-3x}\]'),
 ('Bestäm C från y(0)=10',r'\[10=6+C\quad\Rightarrow\quad C=4\]'),
 ('Beräkna y(2) utan mellanavrundning',r'\[y(2)=6+4e^{-6}\approx6{,}009915\]<p>Värdet är lite större än 6, eftersom kurvan närmar sig jämvikten ovanifrån.</p>')],r'\(y(2)=6+4e^{-6}\approx6{,}01\).',tolerans=0,niva='E',poang='3/0/0',traningsniva=2)
add('4.107',r'Bestäm den konstanta lösningen till ekvationen. Startvärdet anger hur långt från den lösningen kurvan börjar.',[
 ('Bestäm lösningsfamiljen',r'<p>Den konstanta lösningen är 4. Den homogena ekvationen y′+y=0 ger Ce⁻ˣ.</p>\[y=4+Ce^{-x}\]'),
 ('Använd startvärdet 10',r'\[10=4+C\quad\Rightarrow\quad C=6\]'),
 ('Kontrollera båda kraven',r'<p>y(0)=10 och y′+y=−6e⁻ˣ+4+6e⁻ˣ=4.</p>')],r'\(y=4+6e^{-x}\).')
add('4.126',r'Sök först en konstant lösning. Lägg därefter till den homogena delen och använd startvärdet.',[
 ('Bestäm konstant och homogen lösning',r'\[0=A+4\quad\Rightarrow\quad A=-4\]\[y=Ce^x-4\]'),
 ('Använd y(0)=2',r'\[2=C-4\quad\Rightarrow\quad C=6\]'),
 ('Kontrollera startvärdet och ekvationen',r'<p>y(0)=6−4=2 och y′=6eˣ=y+4.</p>')],r'\(y=6e^x-4\).')
add('4.168',r'Utgå från den konstanta lösningen. Startvärdet bestämmer hur stor exponentialdelen är.',[
 ('Skriv familjen kring jämvikten 3',r'<p>y′=0 ger y=3. Avvikelsen från 3 följer u′=−u.</p>\[y=3+Ce^{-x}\]'),
 ('Använd startvärdet 5',r'\[5=3+C\quad\Rightarrow\quad C=2\]'),
 ('Kontrollera att kurvan minskar mot 3',r'\[y^{\prime}=-2e^{-x}=3-y\]<p>Startvärdet är 3+2=5.</p>')],r'\(y=3+2e^{-x}\).')
add('4.517',r'Använd temperaturskillnaden mot rummet. Bestäm k från mätningen efter fem minuter och behåll dess exakta uttryck.',[
 ('Använd startskillnaden mot rummet',r'\[T=20+Ce^{-kt}\]\[90=20+C\quad\Rightarrow\quad C=70\]'),
 ('Bestäm k med femminutersmätningen',r'\[70=20+70e^{-5k}\]\[e^{-5k}=50/70=5/7\]\[k=\frac{\ln(7/5)}5\]'),
 ('Lös för tiden till 40 °C',r'\[40=20+70e^{-kt}\]\[e^{-kt}=2/7\]\[t=\frac{\ln(7/2)}{\ln(7/5)/5}\]\[\approx18{,}6161\text{ min}\]'),
 ('Tolka tiden',r'<p>Tiden räknas från att koppen ställs i rummet. Avsvalningen går långsammare när temperaturskillnaden blir mindre.</p>')],r'Cirka 18,6 minuter.',niva='C',poang='0/3/0',traningsniva=3,svarFormat='numeriskt',tolerans=.05)
add('4.521',r'Vilken saltmängd ger lika stort inflöde och utflöde av salt? Använd därefter startvärdet för lösningen.',[
 ('Bestäm mängden som nås i längden',r'\[0=1-0{,}05y\quad\Rightarrow\quad y=20\text{ kg}\]<p>Vid 20 kg är koncentrationen 20/100=0,2 kg/l, samma som i inflödet.</p>'),
 ('Välj lösningen som börjar med rent vatten',r'\[y=20+Ce^{-0{,}05t}\]\[0=20+C\quad\Rightarrow\quad C=-20\]\[y=20(1-e^{-0{,}05t})\]'),
 ('Lös för tiden till 15 kg',r'\[15=20(1-e^{-0{,}05t})\]\[e^{-0{,}05t}=1/4\]\[t=\frac{\ln4}{0{,}05}\approx27{,}7259\text{ min}\]')],r'20 kg i längden; 15 kg efter cirka 27,7 minuter.',niva='C',poang='0/3/0',traningsniva=3,svarFormat=['numeriskt','numeriskt'],tolerans=[0,.05],svarEnhet=['kg','min'])
add('4.591',r'Vilken derivata har en lösning där y inte ändras?',[
 ('Sätt derivatan till noll för y=c',r'\[0+2c=6\]\[c=3\]'),
 ('Jämför med nivån som kurvorna närmar sig',r'<p>De ritade kurvorna närmar sig y=3. Det stämmer med det beräknade jämviktsvärdet.</p>')],r'\(c=3\).')
add('4.592',r'Behåll parentesen när du subtraherar hela ax+b. Jämför sedan koefficienterna.',[
 ('Derivera och sätt in den givna ansatsen',r'\[y_p^{\prime}=a\]\[a-(ax+b)=2x\]\[-ax+(a-b)=2x\]'),
 ('Jämför x-termer och konstanttermer',r'\[-a=2\quad\Rightarrow\quad a=-2\]\[a-b=0\quad\Rightarrow\quad b=-2\]'),
 ('Kontrollera partikulärlösningen',r'\[-2-(-2x-2)=2x\]')],r'\(a=-2\) och \(b=-2\).',traningsniva=2,poang='2/0/0')
add('4.593',r'Derivera den givna exponentialansatsen. Jämför sedan faktorerna framför samma exponentialfunktion.',[
 ('Derivera ansatsen med kedjeregeln',r'\[y_p^{\prime}=2Ae^{2x}\]'),
 ('Sätt in och jämför med högerledet',r'\[2Ae^{2x}+Ae^{2x}=6e^{2x}\]\[3A=6\quad\Rightarrow\quad A=2\]')],r'\(A=2\).')
add('4.594',r'Vad händer med v′ när hastigheten närmar sig ett konstant värde?',[
 ('Sätt förändringen av hastigheten till noll',r'\[0=9{,}8-0{,}5v\]'),
 ('Lös ut gränshastigheten',r'\[0{,}5v=9{,}8\]\[v=\frac{9{,}8}{0{,}5}=19{,}6\text{ m/s}\]'),
 ('Kontrollera mot grafen',r'<p>Kurvan planar ut strax under 20 m/s. Under 19,6 m/s är v′ positivt, och över denna hastighet är v′ negativt.</p>')],r'19,6 m/s.')
add('4.595',r'Kontrollera både startpunkten och nivån som kurvan närmar sig.',[
 ('Använd startvärdet för att utesluta B',r'<p>Kurvan ska gå genom (0,4). B börjar i (0,0) och kan inte stämma.</p>'),
 ('Bestäm jämviktsnivån',r'\[0=2-y\quad\Rightarrow\quad y=2\]<p>A närmar sig 2, medan C närmar sig 0.</p>'),
 ('Kontrollera kurva A med lösningsformeln',r'\[y=2+Ce^{-x},\qquad 4=2+C\]\[y=2+2e^{-x}\]<p>Derivatan är −2e⁻ˣ, vilket också är 2−y.</p>')],r'Kurva A.')
add('4.596',r'Bestäm först lösningen med det givna startvärdet. Använd sedan det sökta funktionsvärdet för att få en exponentialekvation.',[
 ('Bestäm familjen och använd y(0)=0',r'\[y=3+Ce^{-x}\]\[0=3+C\quad\Rightarrow\quad C=-3\]'),
 ('Sätt y=2 och isolera exponentialtermen',r'\[2=3-3e^{-x}\]\[3e^{-x}=1\quad\Rightarrow\quad e^{-x}=1/3\]'),
 ('Logaritmera för att få x',r'\[-x=\ln(1/3)=-\ln3\]\[x=\ln3\approx1{,}098612\]')],r'\(x\approx1{,}10\).',rättSvar=math.log(3),traningsniva=2,poang='3/0/0')
add('4.597',r'Tangenten ger derivatan i origo. Jämviktsnivån ger ett annat villkor där derivatan är noll.',[
 ('Läs tangentens lutning vid origo',r'\[y^{\prime}(0)=\frac{2-0}{1-0}=2\]'),
 ('Använd y(0)=0 för att bestämma b',r'\[2=a\cdot0+b\quad\Rightarrow\quad b=2\]'),
 ('Använd jämviktsnivån för att bestämma a',r'\[0=4a+2\]\[a=-\frac24=-0{,}5\]'),
 ('Kontrollera riktningen mot jämvikten',r'<p>y′=−0,5y+2 är positivt under y=4 och noll vid y=4. Det stämmer med den växande kurvan som planar ut.</p>')],r'\(a=-0{,}5\) och \(b=2\).',traningsniva=3)
# Även nyare kort granskas: bevara tillräckliga facit; förbättra bara konkreta luckor.
add('4.606',r'Jämför derivatan med hela den givna funktionen. Vilken faktor skiljer dem åt?',[
 ('Derivera exponentialfunktionen',r'\[y^{\prime}=4\cdot0{,}3e^{0{,}3x}\]'),
 ('Jämför med ky',r'\[y^{\prime}=0{,}3(4e^{0{,}3x})=0{,}3y\]')],r'\(k=0{,}3\).')
add('4.611',r'Använd den exponentiella minskningen och jämför mängden efter två timmar med startmängden.',[
 ('Skriv mängden som funktion av tiden',r'\[y=y_0e^{-0{,}25t}\]'),
 ('Beräkna andelen efter två timmar',r'\[\frac{y(2)}{y_0}=e^{-0{,}5}\approx0{,}606531\]'),
 ('Omvandla andelen till procent',r'\[100e^{-0{,}5}\approx60{,}6531\ \%\]')],r'Cirka 60,7 %. ',rättSvar=100*math.exp(-.5))
add('4.614',r'Använd punkten vid x=2 för att bestämma faktorn framför exponentialfunktionen.',[
 ('Skriv lösningsfamiljen för y′=0,5y',r'\[y=Ce^{0{,}5x}\]'),
 ('Använd funktionsvärdet vid x=2',r'\[10=Ce^{0{,}5\cdot2}=Ce\]\[C=10/e\]'),
 ('Beräkna y(0)',r'\[y(0)=Ce^0=C\]\[=10/e\approx3{,}67879\]')],r'\(y(0)\approx3{,}68\).',rättSvar=10/math.e)
add('4.615',r'Jämför mängden vid tiden t med startmängden. Vid halvering är kvoten en halv.',[
 ('Skriv lösningen och halveringsvillkoret',r'\[y=y_0e^{-0{,}1t}\]\[\frac{y_0}{2}=y_0e^{-0{,}1t}\]'),
 ('Förkorta startmängden och logaritmera',r'\[\frac12=e^{-0{,}1t}\]\[-\ln2=-0{,}1t\]'),
 ('Beräkna halveringstiden',r'\[t=\frac{\ln2}{0{,}1}\approx6{,}93147\text{ dygn}\]')],r'Cirka 6,9 dygn.',rättSvar=math.log(2)/.1)
add('4.622',r'Kan startvärdet också vara en konstant lösning till ekvationen?',[
 ('Pröva en konstant lösning med startvärdet',r'<p>För y=5 är y′=0.</p>\[y^{\prime}+2y=0+2\cdot5=10\]'),
 ('Kontrollera startvillkoret',r'<p>Funktionen är 5 även vid x=0. Båda kraven uppfylls: lösningen startar i jämviktsläget och stannar där.</p>')],r'\(y=5\).')
add('4.623',r'Bestäm först jämvikten. Startvärdet visar hur stor avvikelsen från jämvikten är.',[
 ('Hitta jämvikten och lösningsfamiljen',r'\[0=4-A\quad\Rightarrow\quad A=4\]\[y=4+Ce^{-x}\]'),
 ('Använd att kurvan börjar i origo',r'\[0=4+C\quad\Rightarrow\quad C=-4\]'),
 ('Kontrollera startvärdet',r'\[y(0)=4-4=0\]')],r'\(y=4-4e^{-x}\).')
add('4.628',r'Bestäm först den konstanta lösningen. Startvillkoret bestämmer exponentialdelen innan du sätter in x=1.',[
 ('Lös y′+2y=6 utan startvillkor',r'<p>Den konstanta delen uppfyller 2A=6 och är 3. Den homogena delen är Ce⁻²ˣ.</p>\[y=3+Ce^{-2x}\]'),
 ('Använd att y(0)=0',r'\[0=3+C\quad\Rightarrow\quad C=-3\]'),
 ('Beräkna y(1)',r'\[y(1)=3-3e^{-2}\approx2{,}593994\]')],r'\(y(1)\approx2{,}59\).',rättSvar=3-3*math.exp(-2))

# Inga pedagogiska ändringar behövdes efter läsning av dessa kort.
UNCHANGED={'4.605','4.607','4.608','4.609','4.610','4.612','4.613','4.616','4.617','4.618','4.619','4.620','4.621','4.624','4.625','4.626','4.627'}
def install():
 p=ROOT/'uppgiftermatf1.js';raw=p.read_text();dec=json.JSONDecoder();i=raw.index('[')+1;edits=[];seen=[]
 while True:
  while raw[i].isspace() or raw[i]==',':i+=1
  if raw[i]==']':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if q['omr'] in ['homogena_forsta','inhomogena_forsta']:
   seen.append(id);assert id in D or id in UNCHANGED,id
   q.update(D.get(id,{}))
   if id in PARTS:
    for part,updates in zip(q['spelDelar'],PARTS[id]):part.update(updates)
   if id=='4.554':
    part=q['spelDelar'][1]
    new=r'Modellen är \(N(t)=1500e^{0{,}05t}\). Hur många bakterier finns efter 7,0 minuter? Avrunda till hundratal.'
    part['t']=part['t'].replace(part['fraga'],new);part['fraga']=new
   if id=='4.521':q['t']=q['t'].replace('Svara i minuter med en decimal.','Ange saltmängden i kg och tiden i minuter med en decimal.')
   if id in ['4.69','4.399','4.559','4.560']:
    # Frågan/ursprunglig metadata avgör om svaret är exakt eller numeriskt.
    pass
   if q!=old:
    out=fields.replace_fields(raw[i:i+n],q)
    for k,v in q.items():
     if k not in old:out=out.rstrip()[:-1]+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  }'
    edits.append((i,i+n,out))
  i+=n
 assert set(seen)==set(D)|UNCHANGED and len(seen)==68
 for a,b,s in reversed(edits):raw=raw[:a]+s+raw[b:]
 p.write_text(raw);print('68 granskade,',len(edits),'ändrade.')
if __name__=='__main__':install()
