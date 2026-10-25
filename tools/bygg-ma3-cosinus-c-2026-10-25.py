"""Arton individuellt skrivna C-uppgifter; gemensam kod sköter endast format/figurer."""
import importlib.util,json,math
from pathlib import Path
def module(name,file):
 sp=importlib.util.spec_from_file_location(name,Path(__file__).with_name(file));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
h=module('h','bygg-ma3-kontinuitet-2026-10-24.py');g=module('g','ma3-trig-c-figurer-2026-10-25.py')
p,eq=h.p,h.eq;s,c,acos=g.sin,g.cos,g.acos
TASKS=[];REVIEW={};CASES={}
def add(n,text,answer,steps,hint,why,fig,unit='cm',integer=False):
 final=f'{answer:.0f}' if integer else f'{answer:.2f}'.replace('.',',')
 final+=((' '+unit) if unit else '')+'.'
 q=h.make('4.'+str(n),'cosinussatsen','Cosinussatsen – samband och problemlösning',3,p(text),answer,steps,final,hint,fig=fig,unit=unit or None,skills=['procedur','problemlösning']);q.update(kap=4,kurs=['1c'],miniräknare=True,poang='0/2/0',tolerans=0 if integer else .005)
 TASKS.append(q);REVIEW[q['id']]={'status':'Ny, granskad – inget fel.','C-motivering':why,'kommentar':final};CASES['mato1:'+q['id']]=[[str(answer),f'{answer:.0f}' if integer else f'{answer:.2f}',(f'{answer:.0f}' if integer else f'{answer:.2f}')+' '+unit],[str(round(answer,2)+1)]]
def tri(a,b,cc,sides,angles,title,**kwargs):
 A=acos((b*b+cc*cc-a*a)/(2*b*cc));B=acos((a*a+cc*cc-b*b)/(2*a*cc));return g.triangle(A,B,a,title,sides,angles,**kwargs)
def line(P,Q,color='#096c9a',dash=False):return f'<path d="M{P[0]} {P[1]}L{Q[0]} {Q[1]}" fill="none" stroke="{color}" stroke-width="2.5"'+(' stroke-dasharray="6 5"' if dash else '')+'/>'
def poly(points):return '<polygon points="'+' '.join(f'{x:.5f},{y:.5f}' for x,y in points)+'" fill="#edf6fb" stroke="#096c9a" stroke-width="2.5"/>'

add(549,'Två sidor i en triangel är x cm och (x+3) cm. Vinkeln mellan dem är 60° och den tredje sidan är 7 cm. Bestäm x. Svara med ett heltal.',5,
 [p('Cosinussatsen ger en ekvation för x.')+eq(r'\begin{aligned}49={}&x^2+(x+3)^2\\&-2x(x+3)\cos60^\circ\end{aligned}'),p('Använd cos60° = 1/2 och utveckla parenteserna.')+eq(r'x^2+3x-40=0'),p('Faktorisera: (x+8)(x−5) = 0. Roten −8 ger negativa längder, så x = 5. Sidorna blir 5, 8 och 7 cm.')], 'Skriv cosinussatsen med den kända sidan ensam i vänsterledet.', 'Algebraisk rutin: bygger och löser en andragradsekvation med geometriskt rotvillkor.', tri(7,5,8,{'a':'7 cm','b':'x','c':'x + 3'},{0:'60°'},'Triangel med två sidlängder som beror på x.'),unit='',integer=True)

x=14/math.sqrt(7)
add(550,'Två sidor i en triangel är x cm och 2x cm. Vinkeln mellan dem är 120° och den motstående sidan är 14 cm. Bestäm x. Svara med två decimaler.',x,
 [p('Sätt in de två siduttrycken och den trubbiga vinkeln i cosinussatsen.')+eq(r'14^2=x^2+(2x)^2-4x^2\cos120^\circ'),p('Eftersom cos120° = −1/2 blir högerledet 7x². Därför är x² = 28. Endast den positiva roten kan vara en längd.')], 'Var noggrann med minustecknet när cosinus är negativt.', 'Tränar parameteruttryck, trubbig vinkel och val av positiv rot.',tri(14,x,2*x,{'a':'14 cm','b':'x','c':'2x'},{0:'120°'},'Triangel med en trubbig vinkel.'),unit='')

add(551,'En triangel har sidorna 5 cm, 7 cm och 8 cm. Bestäm arean. Svara i cm² med två decimaler.',10*math.sqrt(3),
 [p('Bestäm vinkeln A mellan sidorna 5 och 7 cm.')+eq(r'\cos A=\frac{5^2+7^2-8^2}{2\cdot5\cdot7}=\frac17'),p('A är ungefär 81,79°. Använd sedan areasatsen med samma två sidor.')+eq(r'K=\frac{5\cdot7\sin A}{2}'),p('Beräkna med oavrundad vinkel för att undvika avrundningsfel.')], 'En vinkel behövs innan du kan använda areasatsen.', 'Kombinerar cosinussatsen och areasatsen och kopplar rätt vinkel till rätt sidor.',tri(8,5,7,{'a':'8 cm','b':'5 cm','c':'7 cm'}, {},'Triangel med tre kända sidor.'),unit='cm²')

add(552,'I triangeln är AB = 14 cm, AC = 10 cm och BC = 12 cm. M är mittpunkten på AB. Bestäm CM. Svara i cm med två decimaler.',math.sqrt(73),
 [p('I hela triangeln ger cosinussatsen vinkeln vid A.')+eq(r'\cos A=\frac{14^2+10^2-12^2}{2\cdot14\cdot10}=\frac{19}{35}'),p('AM är 7 cm. Använd samma vinkel i den mindre triangeln ACM.')+eq(r'\begin{aligned}CM^2&=10^2+7^2-140\cdot\frac{19}{35}\\&=73\end{aligned}'),p('Ta den positiva kvadratroten.')], 'Bestäm en vinkel som är gemensam för ABC och ACM.', 'Använder cosinussatsen i två sammanhängande trianglar och utnyttjar mittpunkten.',tri(12,10,14,{'a':'12 cm','b':'10 cm','c':'14 cm'}, {},'Triangel med median CM.',median=True))

b=math.sqrt(37)
add(553,'En vandrare går 3 km från A till B. Vid B svänger hon 60° från sin tidigare färdriktning och går ytterligare 4 km till C. Hur långt är det fågelvägen från A till C? Svara i km med två decimaler.',b,
 [p('Svängen mäts från den fortsatta färdriktningen. Triangelns inre vinkel B är därför 180°−60° = 120°.'),p('Cosinussatsen ger det raka avståndet.')+eq(r'\begin{aligned}AC^2&=3^2+4^2-24\cos120^\circ\\&=37\end{aligned}'),p('Avståndet är den positiva roten ur 37.')], 'Skilj svängens vinkel från den inre vinkeln i triangeln.', 'Översätter en riktning i verkligheten till rätt triangelvinkel.',tri(4,b,3,{'a':'4 km','c':'3 km'}, {},'En vandring med en markerad sväng.',externalB='60°'),unit='km')

ans=math.sqrt(52-48*c(75))
add(554,'Två båtar lämnar samma brygga samtidigt. De håller 12 km/h respektive 18 km/h och kör rakt fram. Vinkeln mellan deras färdriktningar är 75°. Hur långt är det mellan båtarna efter 20 minuter? Svara i km med två decimaler.',ans,
 [p('20 minuter är 1/3 timme. Båtarna hinner därför 4 km respektive 6 km.'),p('Använd dessa sträckor och vinkeln mellan dem.')+eq(r'd^2=4^2+6^2-2\cdot4\cdot6\cos75^\circ'),p('Ta den positiva roten. Hastigheterna får inte sättas in som om de vore sidlängder.')], 'Bestäm först hur långt varje båt har hunnit.', 'Kombinerar hastighet och tid med avstånd i två olika riktningar.',tri(ans,4,6,{'b':'12 km/h','c':'18 km/h'},{0:'75°'},'Båtar färdas från A mot B och C.'),unit='km')

ans=7.2*math.sqrt(1-(45/144)**2)
add(555,'Två vajrar går från punkter A och B på plan mark till toppen C på en mast. AB = 10 m, AC = 8 m och BC = 9 m. Hur hög är masten? Svara i m med två decimaler.',ans,
 [p('Bestäm vinkeln C mellan vajrarna.')+eq(r'\cos C=\frac{8^2+9^2-10^2}{2\cdot8\cdot9}=\frac{45}{144}'),p('Triangelns area kan skrivas på två sätt.')+eq(r'\frac{8\cdot9\sin C}{2}=\frac{10h}{2}'),p('Därför är h = 7,2 sin C. Använd oavrundad vinkel.')], 'Triangelns area kopplar ihop vajrarna med den lodräta höjden.', 'Kombinerar vinkelbestämning med två uttryck för samma area.',tri(9,8,10,{'a':'9 m','b':'8 m','c':'10 m'}, {},'Två vajrar till en mast med höjdfot H.',altitude=True),unit='m')

add(556,'En triangel har sidorna 6 cm, 8 cm och 11 cm. Den kortaste sidan ska förlängas tills vinkeln mittemot 11 cm blir rät. De andra två sidorna behåller sina längder. Hur mycket ska den kortaste sidan förlängas? Svara i cm med två decimaler.',math.sqrt(57)-6,
 [p('När vinkeln blir 90° är cosinusledet noll. Om den nya längden är x blir cosinussatsen')+eq(r'11^2=x^2+8^2'),p('Därför är x = √57 ≈ 7,55 cm. Frågan gäller ökningen, så dra bort den ursprungliga längden 6 cm.')], 'Bestäm först den nya längden och sedan skillnaden mot den gamla.', 'Kopplar cosinussatsen till rät vinkel och skiljer ny längd från förändring.',tri(11,6,8,{'a':'11 cm','b':'6 cm','c':'8 cm'}, {},'Triangeln före förlängningen.'))

# Två trianglar på var sin sida om samma diagonal, i gemensam skala.
d=math.sqrt(52);bx=(36+52-64)/(2*d);by=math.sqrt(36-bx*bx);dx=(25+52-49)/(2*d);dy=-math.sqrt(25-dx*dx)
sc=28;f=lambda x,y:(155+sc*x,220-sc*y)
A=f(0,0);B=f(bx,by);C=f(d,0);D=f(dx,dy)
body=poly([A,B,C,D])+line(A,C,'#a15320',True)
for P,label,ox,oy in [(A,'A',-22,0),(B,'B',0,-23),(C,'C',23,0),(D,'D',0,24)]:body+=g.txt(P[0]+ox,P[1]+oy,label)
for P,Q,label in [(A,B,'6 cm'),(B,C,'8 cm'),(C,D,'7 cm'),(D,A,'5 cm')]:
 dx=Q[0]-P[0];dy=Q[1]-P[1];l=math.hypot(dx,dy);body+=g.txt((P[0]+Q[0])/2+dy/l*36,(P[1]+Q[1])/2-dx/l*36,label)
body+=g.arc(B,A,C,'60°')
add(557,'I fyrhörningen ABCD är AB = 6 cm, BC = 8 cm, CD = 7 cm och DA = 5 cm. Vinkeln B är 60°. Bestäm vinkeln D. Svara i grader med två decimaler.',acos(22/70),
 [p('Diagonalen AC kan beräknas i triangeln ABC.')+eq(r'\begin{aligned}AC^2&=6^2+8^2-96\cos60^\circ\\&=52\end{aligned}'),p('Samma diagonal ingår i triangeln ADC. Där ger cosinussatsen')+eq(r'\cos D=\frac{5^2+7^2-52}{2\cdot5\cdot7}=\frac{22}{70}'),p('Ta invers cosinus för att få D.')], 'Diagonalen är länken mellan de två trianglarna.', 'För över en beräknad längd från en triangel till en annan.',g.svg('Fyrhörning med gemensam diagonal AC.',body,410),unit='°')

add(558,'Två sidor i en triangel är x cm och 2x cm. Vinkeln mellan dem är 60° och arean är 6√3 cm². Bestäm den tredje sidan. Svara i cm med ett heltal.',6,
 [p('Areasatsen bestämmer först x².')+eq(r'6\sqrt3=\frac{x\cdot2x\sin60^\circ}{2}=\frac{x^2\sqrt3}{2}'),p('Alltså är x² = 12. Cosinussatsen ger den tredje sidan a.')+eq(r'\begin{aligned}a^2&=x^2+4x^2-4x^2\cos60^\circ\\&=3x^2\end{aligned}'),p('Därför är a² = 36 och a = 6 cm.')], 'Du behöver inte beräkna x som decimaltal: x² räcker i båda satserna.', 'Kombinerar area med cosinussats och återanvänder ett exakt mellanresultat.',tri(6,math.sqrt(12),2*math.sqrt(12),{'a':'a','b':'x','c':'2x'},{0:'60°'},'Triangel med givet sidförhållande och area.'),integer=True)

BD=70/11;ans=math.sqrt(100+BD*BD-20*BD*19/35)
add(559,'Triangeln har AB = 10 cm, AC = 12 cm och BC = 14 cm. AD delar vinkeln A i två lika stora delar. D ligger på BC. Bestäm AD. Svara i cm med två decimaler.',ans,
 [p('Bisektrissatsen ger BD/DC = 10/12. Eftersom hela BC är 14 cm blir BD = 14·10/22 = 70/11 cm.'),p('Bestäm cos B i hela triangeln.')+eq(r'\cos B=\frac{10^2+14^2-12^2}{2\cdot10\cdot14}=\frac{19}{35}'),p('Använd sedan cosinussatsen i triangeln ABD.')+eq(r'\begin{aligned}AD^2={}&10^2+\left(\frac{70}{11}\right)^2\\&-2\cdot10\cdot\frac{70}{11}\cdot\frac{19}{35}\end{aligned}'),p('Ta den positiva roten utan att mellanavrunda BD.')], 'Bisektrissatsen delar den motstående sidan i ett känt förhållande.', 'Kombinerar bisektrissats med cosinussats i två trianglar.',tri(14,12,10,{'a':'14 cm','b':'12 cm','c':'10 cm'}, {},'Triangel med vinkelbisektris AD.',bisector=0))

opp=math.sqrt(74-70*c(100))
add(560,'Två sidor i en triangel är 5 cm och 7 cm. Den tredje sidan ska vara längre än 9 cm. Vilken är den minsta hela grad som vinkeln mellan 5 cm och 7 cm kan ha? Svara i grader med ett heltal.',96,
 [p('Börja med gränsfallet där den tredje sidan är exakt 9 cm.')+eq(r'\cos v=\frac{5^2+7^2-9^2}{2\cdot5\cdot7}=-0{,}1'),p('Gränsvinkeln är ungefär 95,74°. Mellan 0° och 180° växer den motstående sidan när vinkeln växer.'),p('Vinkeln måste därför vara större än 95,74°. Den minsta hela graden är 96°.')], 'Beräkna gränsvinkeln och avgör sedan på vilken sida om den svaret ska ligga.', 'Översätter ett längdvillkor till vinkelgräns och väljer rätt heltal.',tri(opp,5,7,{'a':'längre än 9 cm','b':'5 cm','c':'7 cm'},{0:'v'},'Exempel på triangel med en sida längre än nio centimeter.'),unit='°',integer=True)

add(561,'En triangels sidor är x cm, (x+1) cm och (x+2) cm. Den största vinkeln är 120°. Bestäm x. Svara med två decimaler.',1.5,
 [p('Största vinkeln ligger mittemot längsta sidan, x+2. Cosinussatsen ger')+eq(r'\begin{gathered}(x+2)^2=x^2+(x+1)^2\\{}-2x(x+1)\cos120^\circ\end{gathered}'),p('Med cos120° = −1/2 förenklas ekvationen till')+eq(r'2x^2-x-3=0'),p('Faktorisering ger (2x−3)(x+1) = 0. Roten x = −1 kan inte vara en längd. Med x = 1,5 blir sidorna 1,5; 2,5 och 3,5 cm, vilket är en möjlig triangel.')], 'Börja med att koppla den största vinkeln till rätt motstående sida.', 'Väljer motstående sida, löser en andragradsekvation och kontrollerar geometriska villkor.',tri(3.5,1.5,2.5,{'a':'x + 2','b':'x','c':'x + 1'},{0:'120°'},'Triangel med tre siduttryck.'),unit='')

O=(260,205);scale=22;A=(106,205);C=(414,205);B=(315,205-scale*5*s(60));D=(205,205+scale*5*s(60))
body=poly([A,B,C,D])+line(A,C,'#a15320',True)+line(B,D,'#a15320',True)+g.arc(O,C,B,'60°')
for P,label,ox,oy in [(A,'A',-22,0),(B,'B',0,-23),(C,'C',23,0),(D,'D',0,23)]:body+=g.txt(P[0]+ox,P[1]+oy,label)
body+=g.txt(260,370,'AC = 14 cm    BD = 10 cm')+g.txt(231,224,'O',16)
add(562,'En parallellograms diagonaler är 14 cm och 10 cm. Den spetsiga vinkeln mellan diagonalerna är 60°. Bestäm parallellogrammens längsta sida. Svara i cm med två decimaler.',math.sqrt(109),
 [p('Diagonalerna halverar varandra, så delarna från O är 7 cm och 5 cm.'),p('Den längsta sidan ligger mittemot den trubbiga vinkeln 120°, inte mot 60°. Cosinussatsen ger')+eq(r'\begin{aligned}a^2&=7^2+5^2-70\cos120^\circ\\&=109\end{aligned}'),p('Ta den positiva roten.')], 'Dela figuren vid diagonalernas skärningspunkt och jämför de två vinklarna.', 'Utnyttjar en parallellograms egenskaper och väljer rätt av två möjliga vinklar.',g.svg('Parallellogram med två diagonaler och vinkel vid O.',body,410))

O=(260,195);R=130;P=[(O[0]+R*s(i*72),O[1]-R*c(i*72)) for i in range(5)];body=f'<circle cx="260" cy="195" r="130" fill="none" stroke="#9aabba" stroke-width="1.5"/>'+poly(P)+line(O,P[0],'#a15320')+line(O,P[1],'#a15320')+g.arc(O,P[0],P[1],'v')+g.txt(242,214,'O')+g.txt(228,135,'6 cm',17)
add(563,'En regelbunden femhörning är inskriven i en cirkel med radien 6 cm. Bestäm femhörningens omkrets. Svara i cm med två decimaler.',60*s(36),
 [p('De fem lika stora medelpunktsvinklarna är 360°/5 = 72°.'),p('Två radier och en sida bildar en triangel. Cosinussatsen ger sidlängden a.')+eq(r'a^2=6^2+6^2-2\cdot6\cdot6\cos72^\circ'),p('Alla fem sidor är lika långa. Beräkna 5a med oavrundad sidlängd.')], 'Dela femhörningen i fem likadana trianglar med spets i cirkelns centrum.', 'Kombinerar regelbunden månghörning, medelpunktsvinkel och cosinussats.',g.svg('Regelbunden femhörning i en cirkel med två radier markerade.',body,390))

O=(260,195);H=(260+72*s(70),195-72*c(70));M=(260+108*s(120),195-108*c(120));body='<circle cx="260" cy="195" r="135" fill="#edf6fb" stroke="#096c9a" stroke-width="2"/>'
for i in range(12):
 u=(260+121*s(i*30),195-121*c(i*30));v=(260+128*s(i*30),195-128*c(i*30));body+=line(u,v,'#647587')
for X,Y,T in [(260,35,'12'),(414,195,'3'),(260,350,'6'),(106,195,'9')]:body+=g.txt(X,Y,T)
body+=line(O,H)+line(O,M,'#a15320')+line(H,M,'#677e93',True)+g.arc(O,H,M,'v')+g.txt(299,155,'8 cm',17)+g.txt(294,249,'12 cm',17)
add(564,'En klockas timvisare är 8 cm lång och minutvisaren är 12 cm. Klockan visar 2:20. Hur långt är det mellan visarnas spetsar? Svara i cm med två decimaler.',math.sqrt(208-192*c(50)),
 [p('Minutvisaren har vridits 20·6° = 120° från klockan 12. Timvisaren har vridits 2·30° + 20·0,5° = 70°.'),p('Vinkeln mellan visarna är alltså 50°. Cosinussatsen ger')+eq(r'd^2=8^2+12^2-2\cdot8\cdot12\cos50^\circ'),p('Ta den positiva roten. Timvisaren står en bit efter 2, inte exakt på 2.')], 'Timvisaren rör sig också under de 20 minuterna.', 'Bestämmer två vinkellägen och kombinerar dem med en avståndsberäkning.',g.svg('Klocka med timvisare och minutvisare vid 2:20.',body,390))

O=(260,285);F=(380,285);U=(342.5,285-165*s(60));V=(177.5,285-165*s(120))
body=line(O,F)+line(O,U,'#096c9a')+line(O,V,'#a15320')+line(F,U,'#61778c',True)+line(F,V,'#a15320',True)
body+=g.arc(O,F,U,'60°')+g.txt(314,316,'8 cm')+g.txt(333,215,'11 cm',17)+g.txt(170,220,'11 cm',17)+g.txt(356,118,'Läge 1',17)+g.txt(158,118,'Läge 2',17)+g.txt(260,355,'Vinkeln öppnas från 60° till 120°',16)
ans=100*(math.sqrt(273)/math.sqrt(97)-1)
add(565,'Två stänger, 8 cm och 11 cm långa, sitter ihop i ena änden. Vinkeln mellan dem ökas från 60° till 120°. Med hur många procent ökar avståndet mellan de fria ändarna? Svara i procent med två decimaler.',ans,
 [p('Beräkna avståndet i varje läge med cosinussatsen.')+eq(r'\begin{aligned}d_1^2&=8^2+11^2-176\cos60^\circ\\&=97\end{aligned}')+eq(r'\begin{aligned}d_2^2&=8^2+11^2-176\cos120^\circ\\&=273\end{aligned}'),p('Jämför längderna, inte deras kvadrater. Procentökningen är')+eq(r'\frac{\sqrt{273}-\sqrt{97}}{\sqrt{97}}\cdot100\,\%')], 'Den ursprungliga längden ska stå i nämnaren när procentökningen beräknas.', 'Kombinerar två geometriska beräkningar med relativ förändring.',g.svg('Två lägen för en rörlig stång.',body,390),unit='%')

add(566,'I triangeln är AB = 7 cm, AC = 10 cm och BC = 15 cm. Höjden från C träffar linjen genom A och B i H, utanför sidan AB. Hur långt är det från A till H? Svara i cm med två decimaler.',38/7,
 [p('Vinkeln A är trubbig. Cosinussatsen ger')+eq(r'\cos A=\frac{7^2+10^2-15^2}{2\cdot7\cdot10}=-\frac{19}{35}'),p('I den räta triangeln ACH är vinkeln vid A i stället 180°−A. Därför gäller')+eq(r'\begin{aligned}AH&=10\cos(180^\circ-A)\\&=-10\cos A\end{aligned}'),p('Insättning ger AH = 38/7 cm. Avståndet är positivt trots att cos A är negativt.')], 'H ligger på andra sidan A än B. Rita därför baslinjens förlängning.', 'Tolkar negativ cosinus som en projektion utanför sidan och bestämmer ett positivt avstånd.',tri(15,10,7,{'a':'15 cm','b':'10 cm','c':'7 cm'}, {},'Trubbig triangel med höjdfoten utanför basen.',altitude=True))

if __name__=='__main__':
 h.install(TASKS)
 (h.ROOT/'agent/MA3_COSINUS_C_2026-10-25.json').write_text(json.dumps(REVIEW,ensure_ascii=False,indent=2)+'\n')
 (h.ROOT/'tools/ma3-cosinus-c-2026-10-25.cases.json').write_text(json.dumps(CASES,ensure_ascii=False,indent=2)+'\n')
