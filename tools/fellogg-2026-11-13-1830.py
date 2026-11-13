"""Avgränsade rättningar, räknade från givna data. Bevara övriga bankobjekt."""
from pathlib import Path
import math,re,bankpatch,runpy,json
ROOT=Path(__file__).resolve().parent.parent
m=lambda x:'<div class="facit-matte">\\['+x+'\\]</div>'
def st(h,b):return '<li><p class="facit-rubrik">'+h+'</p>'+b+'</li>'
def sol(ss,ans):return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(ss)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+ans+'</p></div>'
def join(ss):return '<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+chr(97+i)+')</span><div class="facit-arbete">'+s+'</div></div>' for i,s in enumerate(ss))+'</div>'

def fish(q):
 q['t']='<p>Du står i vatten och tittar på en fisk. Dina ögon är 0,52 m över vattenytan och fisken är 0,65 m under den. Siktlinjen i luften bildar 45° med vattenytan. Vattnets brytningsindex är 1,33.</p><p>Bestäm det vågräta avståndet mellan fisken och lodlinjen genom dina ögon, markerat x i figuren. Svara i meter.</p>'+fishfig()
 q['s']=sol([st(r'Vinklarna i Snells lag mäts från normalen',r'<p>Normalen är vinkelrät mot vattenytan. Strålen bildar 45° med ytan, så vinkeln i luften är också \(90^\circ-45^\circ=45^\circ\) från normalen.</p>'),st(r'Snells lag: \(n_l\sin\alpha_l=n_v\sin\alpha_v\)',r'<p>Ljuset går från fisken till ögat. Samma brytningslag kan användas när strålen följs baklänges. För luft används \(n_l\approx1{,}00\).</p>'+m(r'\begin{aligned}\sin\alpha_v&=\frac{1{,}00\sin45^\circ}{1{,}33}\\\alpha_v&\approx32{,}12^\circ\end{aligned}')),st(r'Två rätvinkliga trianglar: \(x=h\tan\alpha\)',r'<p>I luften blir det vågräta avståndet från ögats lodlinje till brytningspunkten:</p>'+m(r'x_l=0{,}52\tan45^\circ=0{,}52\ \mathrm m')+r'<p>I vattnet blir avståndet från brytningspunkten till fisken:</p>'+m(r'x_v=0{,}65\tan32{,}12^\circ\approx0{,}408\ \mathrm m')),st(r'Avståndet från personen: \(x=x_l+x_v\)',m(r'x=0{,}52+0{,}408\approx0{,}93\ \mathrm m')+'<p>Båda delsträckorna ska räknas med. Avståndet avser alltså inte någon vattenkant.</p>')],'Fisken är cirka 0,93 m bort i vågrät led, räknat från lodlinjen genom dina ögon.')
 q['ledtrad']='<p>Avståndet består av två vågräta delsträckor: en fram till brytningspunkten och en därifrån till fisken. Snells lag använder vinklar från normalen.</p>'

def fishfig():
 return '''<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" role="img" aria-label="Ögat ligger över vattenytan. Strålen bryts mot normalen i vattnet och går till fisken. Avståndet x mäts vågrätt från ögats lodlinje till fiskens lodlinje." style="width:100%;max-width:500px;height:auto"><rect width="500" height="400" fill="white"/><rect x="25" y="180" width="450" height="165" fill="#e6f4fa"/><path d="M25 180H475" stroke="#45677d" stroke-width="2"/><g stroke="#8595a4" stroke-width="1.4" stroke-dasharray="5 4"><line x1="110" y1="60" x2="110" y2="350"/><line x1="324.16" y1="330" x2="324.16" y2="350"/><line x1="230" y1="145" x2="230" y2="338"/></g><g stroke="#b43d28" stroke-width="3"><line x1="110" y1="60" x2="230" y2="180"/><line x1="230" y1="180" x2="324.16" y2="330"/></g><circle cx="110" cy="60" r="5" fill="#172d42"/><ellipse cx="324.16" cy="330" rx="13" ry="7" fill="#2a5d9e"/><path d="M337 330L348 321L348 338Z" fill="#2a5d9e"/><line x1="110" y1="60" x2="165" y2="60" stroke="#273e53" stroke-width="1.5"/><path d="M142 60A32 32 0 0 1 132.63 82.63" fill="none" stroke="#273e53" stroke-width="1.5"/><g fill="none" stroke="#273e53" stroke-width="1.5"><path d="M65 60V180 M59 60H71 M59 180H71"/><path d="M425 180V330 M419 180H431 M419 330H431"/><path d="M110 365H324.16 M110 359V371 M324.16 359V371"/></g><g font-family="Arial,sans-serif" fill="#172d42" font-size="18"><text x="89" y="40">Öga</text><text x="157" y="91">45°</text><text x="240" y="152">Normal</text><text x="365" y="169">Vattenyta</text><text x="32" y="126" transform="rotate(-90 32 126)" text-anchor="middle">0,52 m</text><text x="453" y="255" transform="rotate(-90 453 255)" text-anchor="middle">0,65 m</text><text x="217" y="389" text-anchor="middle">x</text><text x="345" y="316">Fisk</text></g></svg></span>'''

def nickel(q):
 q['t']=q['t'].replace('Anta att all effekt strålas ut och att tråden är en svart kropp. Beräkna smältpunkten.','Omgivningen har temperaturen 20 °C. Anta att tråden är en svart kropp och att all tillförd elektrisk effekt avges som nettostrålning till omgivningen. Bortse från trådens ändytor. Beräkna smältpunkten i °C.')
 q['rättSvar']=(56.5*12/(5.67e-8*math.pi*.000445*.955)+293.15**4)**.25-273.15
 q['s']=sol([st(r'Elektrisk effekt: \(P=UI\)',m(r'P=56{,}5\cdot12{,}0=678\ \mathrm W')),st(r'Trådens mantelarea: \(A=\pi dl\)',r'<p>Trådens längd är 0,955 m och diametern 0,000445 m. Ändytorna försummas enligt frågan.</p>'+m(r'\begin{aligned}A&=\pi\cdot0{,}000445\cdot0{,}955\\&\approx1{,}335\cdot10^{-3}\ \mathrm{m^2}\end{aligned}')),st(r'Nettostrålning: \(P=\sigma A(T^4-T_0^4)\)',r'<p>Tråden både strålar ut och tar emot energi. Omgivningens temperatur är given: \(T_0=20+273{,}15=293{,}15\) K. För den svarta kroppen är emissionstalet 1. Lös ut trådens temperatur i kelvin:</p>'+m(r'T^4=\frac{P}{\sigma A}+T_0^4')+m(r'\begin{aligned}T^4&=\frac{678}{5{,}67\cdot10^{-8}A}\\&\quad+293{,}15^4\\T&\approx1730{,}31\ \mathrm K\end{aligned}')),st(r'Kelvin till Celsius: \(t=T-273{,}15\)',m(r'\begin{aligned}t&\approx1730{,}31-273{,}15\\&=1457{,}16\ {}^\circ\mathrm C\end{aligned}')+'<p>Om inkommande strålning försummas blir svaret cirka 1456,80 °C. Skillnaden är bara 0,36 °C, men omgivningens temperatur ska inte behöva gissas.</p>')],r'Smältpunkten blir cirka \(1457\ {}^\circ\mathrm C\) enligt modellen.')
 q['ledtrad']='<p>Börja med den elektriska effekten och trådens mantelarea. I jämvikt motsvarar effekten nettot av utgående och inkommande strålning. Temperaturerna i strålningslagen ska anges i kelvin.</p>'

def machines(q):
 q['s']=sol([st(r'Ljudnivå till intensitet: \(L=10\lg(I/I_0)\)',r'<p>Decibel är en logaritmisk skala. Vi räknar först med ljudintensitet i W/m², som kan adderas. Här är lg tiologaritmen och \(I_0=10^{-12}\) W/m² är hörtröskeln. Sambandet kan skrivas \(I=I_0\cdot10^{L/10}\).</p>'+m(r'\begin{aligned}I_1&=10^{-12}\cdot10^{82/10}\\&\approx1{,}585\cdot10^{-4}\ \mathrm{W/m^2}\end{aligned}')),st(r'Fyra gånger längre avstånd: \(I\propto1/r^2\)',r'<p>Ljudet sprids över en klotyta. När avståndet ökar från 3,0 till 12 m blir intensiteten 16 gånger mindre, eftersom \((12/3)^2=16\).</p>'+m(r'\begin{aligned}I_2&=I_1\left(\frac{3{,}0}{12}\right)^2\\&\approx9{,}906\cdot10^{-6}\ \mathrm{W/m^2}\end{aligned}')),st(r'Fyra oberoende maskiner: \(I_3=4I_2\)',r'<p>Det är intensiteterna som adderas. Vi ska alltså inte multiplicera 82 dB med fyra.</p>'+m(r'I_3\approx3{,}962\cdot10^{-5}\ \mathrm{W/m^2}')),st(r'Skärmen släpper igenom 12 %: \(I_4=0{,}12I_3\)',m(r'I_4\approx4{,}755\cdot10^{-6}\ \mathrm{W/m^2}')),st(r'Tillbaka till decibel: \(L=10\lg(I_4/I_0)\)',m(r'\begin{aligned}L&=10\lg\left(\frac{4{,}755\cdot10^{-6}}{10^{-12}}\right)\\&\approx66{,}8\ \mathrm{dB}\end{aligned}')+'<p>Mellanresultaten ovan visas avrundade. Behåll fler siffror på räknaren tills slutsvaret beräknas.</p>')],'Ljudnivån på arbetsplatsen är cirka 67 dB (66,8 dB med en decimal).')
 q['ledtrad']='<p>Omvandla först 82 dB till intensitet. Hur påverkar sedan avståndet, de fyra maskinerna och skärmen denna intensitet? Omvandla till dB sist.</p>'

def sounds(q):
 id=q['id']
 if id=='2.99':q['s']=sol([st(r'Oberoende ljudkällor: \(I_{tot}=I_1+I_2\)',r'<p>Varje maskin ger samma intensitet I. Tillsammans ger de 2I. Decibeltalen 70 och 70 kan däremot inte adderas.</p>'),st(r'Nivåändring: \(\Delta L=10\lg(I_{tot}/I)\)',r'<p>lg är tiologaritmen. Intensitetskvoten är 2:</p>'+m(r'\Delta L=10\lg2\approx3{,}01\ \mathrm{dB}')),st(r'Lägg till nivåökningen: \(L_{tot}=70+\Delta L\)',m(r'L_{tot}\approx70+3{,}01=73{,}0\ \mathrm{dB}'))],'Den totala ljudnivån är ungefär 73 dB.')
 if id=='2.101':q['s']=sol([st(r'Klotytans area: \(A=4\pi r^2\)',r'<p>Avståndet blir \(8,0/2,0=4\) gånger större. Samma ljudeffekt fördelas då över \(4^2=16\) gånger så stor yta. Intensiteten blir därför 1/16 av den tidigare.</p>'),st(r'Nivåändring: \(\Delta L=10\lg(I_2/I_1)\)',r'<p>lg är tiologaritmen. Sätt in intensitetskvoten 1/16:</p>'+m(r'\Delta L=10\lg(1/16)\approx-12{,}04\ \mathrm{dB}')),st(r'Ljudnivån på 8,0 m: \(L_2=L_1+\Delta L\)',m(r'L_2\approx84-12{,}04=71{,}96\ \mathrm{dB}'))],'Ljudnivån är cirka 72 dB på 8,0 m avstånd.')
 if id=='2.103':q['s']=sol([st(r'Decibeldefinitionen: \(L=10\lg(I/I_0)\)',r'<p>lg är tiologaritmen och hörtröskeln \(I_0=10^{-12}\) W/m². Dela ljudnivån med 10. Använd sedan att \(10^{\lg x}=x\):</p>'+m(r'\begin{aligned}78/10&=\lg(I/I_0)\\I/I_0&=10^{7{,}8}\\I&=10^{-12}\cdot10^{7{,}8}\\&\approx6{,}31\cdot10^{-5}\ \mathrm{W/m^2}\end{aligned}')),st(r'Effekt genom en klotyta: \(P=I\cdot4\pi r^2\)',r'<p>Intensiteten är effekt per kvadratmeter. På 6,0 m avstånd sprids ljudeffekten över klotytan \(4\pi\cdot6,0^2\).</p>'+m(r'\begin{aligned}P&=6{,}31\cdot10^{-5}\cdot4\pi\cdot6{,}0^2\\&\approx0{,}0285\ \mathrm W\end{aligned}'))],r'Intensiteten är cirka \(6{,}3\cdot10^{-5}\) W/m² och ljudeffekten cirka 0,029 W.')
 if id=='2.105':q['s']=sol([st(r'Nivåskillnaden: \(\Delta L=10\lg(I_1/I_2)\)',r'<p>Skillnaden 86−80=6 dB ger intensitetskvoten. lg är tiologaritmen. Dela med 10 och använd en tiopotens:</p>'+m(r'\begin{aligned}6/10&=\lg(I_1/I_2)\\I_1/I_2&=10^{0{,}6}\approx3{,}981\end{aligned}')),st(r'Intensiteten avtar som \(I\propto1/r^2\)',r'<p>Den bortre punkten ligger på avståndet \(r+5,0\). Den har lägre intensitet. Intensitetskvoten ger avståndskvoten:</p>'+m(r'\begin{aligned}\left(\frac{r+5{,}0}{r}\right)^2&\approx3{,}981\\\frac{r+5{,}0}{r}&\approx1{,}9953\\5{,}0&\approx0{,}9953r\\r&\approx5{,}024\ \mathrm m\end{aligned}')),st(r'86 dB till intensitet: \(I_1=I_0\cdot10^{L_1/10}\)',r'<p>Hörtröskeln är \(I_0=10^{-12}\) W/m².</p>'+m(r'I_1\approx3{,}981\cdot10^{-4}\ \mathrm{W/m^2}')),st(r'Akustisk effekt: \(P=4\pi r^2I_1\)',m(r'\begin{aligned}P&\approx4\pi\cdot5{,}024^2\\&\quad\cdot3{,}981\cdot10^{-4}\\&\approx0{,}126\ \mathrm W\end{aligned}'))],'Närmaste mätpunkten är cirka 5,0 m från källan. Ljudeffekten är cirka 0,13 W.')
 if id=='2.172':
  a=sol([st(r'Intensitet på 4,0 m: \(I=P/(4\pi r^2)\)',r'<p>Effekten 0,80 W sprids jämnt över en klotyta. Intensiteten är effekten per kvadratmeter:</p>'+m(r'\begin{aligned}I&=\frac{0{,}80}{4\pi\cdot4{,}0^2}\\&\approx3{,}979\cdot10^{-3}\ \mathrm{W/m^2}\end{aligned}')),st(r'Ljudnivå: \(L=10\lg(I/I_0)\)',r'<p>lg är tiologaritmen. Jämför intensiteten med hörtröskeln \(I_0=10^{-12}\) W/m².</p>'+m(r'\begin{aligned}L&=10\lg\left(\frac{3{,}979\cdot10^{-3}}{10^{-12}}\right)\\&\approx96{,}0\ \mathrm{dB}\end{aligned}'))],'Ljudnivån är cirka 96 dB.')
  b=sol([st(r'70 dB till intensitet: \(L=10\lg(I/I_0)\)',r'<p>Dela med 10 och använd tiopotensen för att få bort lg. Hörtröskeln är \(I_0=10^{-12}\) W/m².</p>'+m(r'\begin{aligned}7&=\lg(I/I_0)\\I/I_0&=10^7\\I&=10^{-12}\cdot10^7\\&=10^{-5}\ \mathrm{W/m^2}\end{aligned}')),st(r'Lös ut avståndet ur \(I=P/(4\pi r^2)\)',r'<p>Multiplicera med r², dividera med I och dra kvadratroten. Använd den givna ljudeffekten 0,80 W.</p>'+m(r'\begin{aligned}r&=\sqrt{\frac{P}{4\pi I}}\\&=\sqrt{\frac{0{,}80}{4\pi\cdot10^{-5}}}\\&\approx79{,}8\ \mathrm m\end{aligned}'))],'Ljudnivån är 70 dB på cirka 80 m avstånd.')
  q['s']=join([a,b]);q['spelDelar'][0]['s']=a;q['spelDelar'][1]['s']=b

def lamp(q):
 sentence=' Anta att hela lampans elektriska effekt blir värmestrålning från glödtrådens mantelyta. Bortse från inkommande strålning från omgivningen.'
 if sentence not in q['t']:q['t']=q['t'].replace('Beräkna trådens temperatur.',sentence+' Beräkna trådens temperatur.')
 q['s']=sol([st(r'Mantelarea: \(A=\pi dl\)',r'<p>Diametern är 0,00020 m och längden 0,030 m.</p>'+m(r'A=\pi\cdot0{,}00020\cdot0{,}030')),st(r'Strålningseffekt: \(P=e\sigma AT^4\)',r'<p>Enligt frågan är effekten 60 W och emissionstalet 0,60. Inkommande strålning försummas; därför används inte någon okänd omgivningstemperatur.</p>'+m(r'\begin{aligned}T^4&=\frac{60}{0{,}60\sigma A}\\T&\approx3110\ \mathrm K\end{aligned}')),st(r'Kelvin till Celsius: \(t=T-273{,}15\)',m(r't\approx3110-273{,}15\approx2837\ {}^\circ\mathrm C'))],'Glödtrådens temperatur är cirka 2800 °C (ungefär 2837 °C före avrundning).')

def pipes(q):
 # Måtten ligger redan längs piporna, men textens typsnitt överlappar måttlinjen.
 for obj in [q,*q.get('spelDelar',[])]:
  if 't' not in obj:continue
  t=obj['t']
  for old,new in [('143.00','156.00'),('298.00','311.00'),('453.00','466.00')]:
   t=t.replace('x="'+old+'" y="137.50"','x="'+new+'" y="137.50"').replace('rotate(-90 '+old+' 137.50)','rotate(-90 '+new+' 137.50)')
  t=re.sub(r'font-size="15"([^>]*rotate\(-90 [^>]+)',r'font-size="17"\1',t)
  obj['t']=t
 # Måttlinjerna är redan rättade i remote 37bd17b. Förbättra den kvarvarande kompakta lösningen.
 a=sol([st(r'Vågformeln: \(f=v/\lambda\)',r'<p>En öppen ände ger en buk i luftpartiklarnas rörelse, en stängd ände ger en nod. Avläs hur stor del av en våglängd som ryms i varje pipa.</p>'),st(r'Pipa A: \(L=\lambda_A/2\)',r'<p>A har en buk i varje ände och en nod i mitten: en halv våglängd ryms i 0,80 m.</p>'+m(r'\begin{aligned}\lambda_A&=2\cdot0{,}80=1{,}60\ \mathrm m\\f_A&=340/1{,}60=212{,}5\ \mathrm{Hz}\end{aligned}')),st(r'Pipa B: \(L=3\lambda_B/4\)',r'<p>Från noden längst ned till buken överst ryms tre fjärdedels våglängd i 0,60 m.</p>'+m(r'\begin{aligned}\lambda_B&=4\cdot0{,}60/3=0{,}80\ \mathrm m\\f_B&=340/0{,}80=425\ \mathrm{Hz}\end{aligned}')),st(r'Pipa C: \(L=\lambda_C/4\)',r'<p>C har en nod nedtill och en buk upptill: en fjärdedels våglängd ryms i 0,45 m.</p>'+m(r'\begin{aligned}\lambda_C&=4\cdot0{,}45=1{,}80\ \mathrm m\\f_C&=340/1{,}80\approx188{,}9\ \mathrm{Hz}\end{aligned}'))],'A: cirka 213 Hz. B: 425 Hz. C: cirka 189 Hz.')
 b=sol([st(r'Beräkna frekvenserna med \(f=v/\lambda\)',r'<p>Mönstren i figuren ger \(\lambda_A=2\cdot0,80=1,60\) m, \(\lambda_B=4\cdot0,60/3=0,80\) m och \(\lambda_C=4\cdot0,45=1,80\) m.</p>'+m(r'\begin{aligned}f_A&=212{,}5\ \mathrm{Hz}\\f_B&=425\ \mathrm{Hz}\\f_C&\approx188{,}9\ \mathrm{Hz}\end{aligned}')),st(r'Jämför skillnaderna: \(\Delta f=|f_i-f_j|\)',m(r'\begin{aligned}|f_A-f_C|&\approx23{,}6\ \mathrm{Hz}\\|f_B-f_A|&=212{,}5\ \mathrm{Hz}\\|f_B-f_C|&\approx236{,}1\ \mathrm{Hz}\end{aligned}'))],'A och C ligger närmast varandra, med cirka 24 Hz skillnad.')
 q['s']=join([a,b]);q['spelDelar'][0]['s']=a;q['spelDelar'][1]['s']=b

def organ(q):
 a=sol([st(r'Öppen pipas grundton: \(L=\lambda/2\)',r'<p>Grundtonens halva våglängd ryms i pipan. Använd \(v=f\lambda\), alltså \(L=v/(2f)\).</p>'+m(r'\begin{aligned}L&=\frac{340}{2\cdot262}\\&\approx0{,}649\ \mathrm m\end{aligned}'))],'Pipan är cirka 0,649 m lång.')
 b=sol([st(r'Oförändrad längd: \(\lambda_{öppen}=2L\), \(\lambda_{täppt}=4L\)',r'<p>När ena änden täpps till fördubblas grundtonens våglängd. Eftersom ljudhastigheten är densamma halveras frekvensen.</p>'+m(r'f_1=262/2=131\ \mathrm{Hz}')),st(r'Halvöppen pipa: \(f_n=nf_1\) för udda n',r'<p>Efter grundtonen kommer resonanserna med tre respektive fem fjärdedels våglängder längs pipan:</p>'+m(r'\begin{aligned}f_3&=3\cdot131=393\ \mathrm{Hz}\\f_5&=5\cdot131=655\ \mathrm{Hz}\end{aligned}'))],'Grundtonen är 131 Hz. Nästa två resonanser är 393 Hz och 655 Hz.')
 c=sol([st(r'Jämför grundtonerna: \(131\lt262\)',r'<p>Den halvöppna pipan ger den lägsta tonen: 131 Hz.</p>'),st(r'Öppen pipa: \(f_n=n\cdot262=2n\cdot131\)',r'<p>Frekvenserna 262, 524, 786, … Hz är jämna multiplar av 131 Hz, eftersom n är ett positivt heltal.</p>'),st(r'Halvöppen pipa: \(f_n=n\cdot131\) för udda n',r'<p>Frekvenserna 131, 393, 655, … Hz är udda multiplar av 131 Hz. Ett heltal kan inte vara både jämnt och udda. Därför kan piporna inte ge exakt samma frekvens i dessa modeller.</p>')],'Den täppta pipan ger lägst grundton, 131 Hz. Ingen frekvens är gemensam för modellerna.')
 q['s']=join([a,b,c])
 for p,ss in zip(q['spelDelar'],[a,b,c]):p['s']=ss
 # Den tidigare A-klassningen stämmer inte med direkta grundtonsberäkningar.
 q.update(niva='C',poang='(3/1/0)',traningsniva=3)
 for p,grade,points,level in zip(q['spelDelar'],['E','E','C'],['(1/0/0)','(2/0/0)','(0/1/0)'],[2,2,3]):p.update(niva=grade,poang=points,traningsniva=level)

def apply():
 edits={'4.403':fish,'4.456':nickel,'2.104':machines,'4.454':lamp,'2.135':pipes,'2.179':organ}
 edits.update({id:sounds for id in ['2.99','2.101','2.103','2.105','2.172']})
 def pulse(q):
  # Linjär superposition på samma homogena lina kräver samma utbredningsfart.
  q['t']=q['t'].replace('går 0,40 m/s åt höger','går 0,30 m/s åt höger').replace('går 0,20 m/s åt vänster','går 0,30 m/s åt vänster')
  q['s']=q['s'].replace(r'0{,}40\cdot2{,}0=0{,}80',r'0{,}30\cdot2{,}0=0{,}60').replace(r'0{,}20\cdot2{,}0=0{,}40',r'0{,}30\cdot2{,}0=0{,}60').replace(r'0{,}80+0{,}40=1{,}20',r'0{,}60+0{,}60=1{,}20')
  q['t']=q['t'].replace('viewBox="0.000 5.288 308.000 135.000" width="620" height="272"','viewBox="0 0 308 143" width="620" height="288"')
  q['s']=q['s'].replace('<text x="197.3" y="81.5"','<text x="225" y="81.5"')
 edits['2.69']=pulse
 # Fysikens generella miniräknartillstånd gäller även manuella läraruppgifter.
 for id in list(edits)+['2.179','2.69']:
  f=edits.get(id,lambda q:None)
  def with_tools(q,f=f):
   f(q);q['miniräknare']=True;q['geogebra']=False
  edits[id]=with_tools
 bankpatch.andra(ROOT/'uppgifter2.js',edits)
 # Samma bekräftade mobilbreddsfel i de sex jämförda kraftkedjorna.
 def vector_mobile(q):
  for obj in [q,*q.get('spelDelar',[])]:
   ss=obj.get('s','')
   ss=re.sub(r'(?<!&)\\quad\((\d+)\\ \\text\{',lambda m:r'\\&\quad('+m[1]+r'\ \text{',ss)
   ss=re.sub(r'(?<!&)\\quad\(\\text\{ingen komposant\}\)',lambda m:r'\\&\quad(\text{ingen komposant})',ss)
   ss=re.sub(r'F_R=(\\sqrt\{[^<>\n]+?\})=(\\sqrt\{[^<>\n]+?\})\\approx([^<>\n]+?)\\ \\mathrm N',lambda m:r'\begin{aligned}F_R&='+m[1]+r'\\&='+m[2]+r'\\&\approx'+m[3]+r'\ \mathrm N\end{aligned}',ss)
   if 's' in obj:obj['s']=ss
 h=runpy.run_path(str(ROOT/'tools/felrapporter-2026-11-09.py'));b=h['read']('uppgifter.js');old={q['id']:json.loads(json.dumps(q)) for q in b}
 for q in b:
  if q['id'] in ['4.933','4.938','4.939','4.940','4.947','4.948']:vector_mobile(q)
 h['save']('uppgifter.js',b,old)
if __name__=='__main__':apply()
