import importlib.util,json,math
from pathlib import Path
def module(name,file):
 sp=importlib.util.spec_from_file_location(name,Path(__file__).with_name(file));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
h=module('h','bygg-ma3-kontinuitet-2026-10-24.py');g=module('g','ma3-trig-c-figurer-2026-10-25.py')
p,m,eq,table=h.p,h.m,h.eq,h.table
sin,cos,asin=g.sin,g.cos,g.asin
TASKS=[];REVIEW={};CASES={}
def add(n,t,ans,steps,final,hint,why,fig='',unit='cm',labels=None,tol=.005,old=False,options=None):
 q=h.make('4.'+str(n),'sinussatsen','Sinussatsen – samband och problemlösning',3,t,ans,steps,final,hint,fig=fig,labels=labels,options=options,unit=None if labels or options else unit,skills=['procedur','problemlösning']);q.update(kap=4,kurs=['1c'],poang='0/2/0',miniräknare=True)
 if not options:q['tolerans']=[tol]*len(ans) if labels else tol
 if labels:q['svarsstruktur']='mängd'
 TASKS.append(q);REVIEW[q['id']]={'status':'Åtgärdad: tidigare manuellt C-resonemang blir självrättande.' if old else 'Ny, granskad – inget fel.','C-motivering':why,'kommentar':final}
 if not options and not labels:
  decimals=1 if tol==.05 else 2;CASES['mato1:'+q['id']]=[[f'{ans:.{decimals}f}',f'{ans:.{decimals}f} '+unit],[str(round(ans,decimals)+1)]]
 return q
def tri(A,B,a,sides,angles,title,**kw):return g.triangle(A,B,a,title,sides,angles,**kw)

add(52,p('Kan en triangel ha A = 42°, a = 12 cm och b = 20 cm, där a och b ligger mittemot A respektive B? Välj rätt svar med motivering.'),None,
 [p('Sinussatsen skulle kräva')+eq(r'\sin B=\frac{20\sin42^\circ}{12}\approx1{,}12'),p('Sinus till en vinkel kan inte vara större än 1. Ingen triangel uppfyller därför villkoren.')],'Nej, villkoren skulle kräva sin B > 1.','Kontrollera vilket värde sinussatsen ger för sin B.', 'Kontrollerar att givna data beskriver en möjlig triangel.',fig=table(['Givet','Värde'],[['A','42°'],['a, mot A','12 cm'],['b, mot B','20 cm']]),old=True,options=[('Ja, eftersom alla längder är positiva.',False),('Ja, och B är 90°.',False),('Nej, villkoren skulle kräva sin B > 1.',True),('Nej, eftersom b alltid måste vara kortare än a.',False)])

c=80;A=40;B=65;C=75;a=c*sin(A)/sin(C);b=c*sin(B)/sin(C)
add(532,p('En stig går från A till B via C. AB = 80 m, A = 40° och B = 65°. Hur mycket längre är vägen A–C–B än den raka sträckan AB? Svara i m med två decimaler.'),a+b-c,
 [p('Toppvinkeln är 180°−40°−65° = 75°. Använd AB som känd sida i sinussatsen.')+eq(r'AC=\frac{80\sin65^\circ}{\sin75^\circ}')+eq(r'BC=\frac{80\sin40^\circ}{\sin75^\circ}'),p('Lägg ihop de två stigdelarna och dra bort 80 m. Behåll extra decimaler tills du avrundar.')],f'{a+b-c:.2f} m.'.replace('.',',',1),'Båda delarna av omvägen behöver beräknas.', 'Kombinerar två sidberäkningar och tolkar skillnaden mellan två färdvägar.',fig=tri(A,B,a,{'c':'80 m'},{0:'40°',1:'65°'},'Triangel för en omväg via C.'),unit='m')

A=55;B=75;C=50;c=60;a=c*sin(A)/sin(C);b=c*sin(B)/sin(C);area=.5*a*b*sin(C)
add(533,p('Ett triangelformat markområde har AB = 60 m, A = 55° och B = 75°. Bestäm områdets area. Svara i m² med två decimaler.'),area,
 [p('Vinkeln C är 50°. Sinussatsen ger sidan AC.')+eq(r'AC=\frac{60\sin75^\circ}{\sin50^\circ}'),p('AB och AC omger vinkeln A. Triangelns area blir därför')+eq(r'K=\frac{60\cdot AC\cdot\sin55^\circ}{2}')],f'{area:.2f} m².'.replace('.',',',1),'Bestäm en sida som kan kombineras med AB i areasatsen.', 'Kombinerar sinussatsen med area och väljer en vinkel mellan rätt två sidor.',fig=tri(A,B,a,{'c':'60 m'},{0:'55°',1:'75°'},'Triangelformat markområde.'),unit='m²')

A=35;B=65;a=20*sin(A)/(sin(A)+sin(B))
add(534,p('I triangeln är A = 35° och B = 65°. Sidorna a och b, mittemot dessa vinklar, är tillsammans 20 cm. Bestäm a. Svara i cm med två decimaler.'),a,
 [p('Sinussatsen ger b = a·sin65°/sin35°. Använd summan a+b = 20.')+eq(r'a\left(1+\frac{\sin65^\circ}{\sin35^\circ}\right)=20'),p('Dividera med parentesen för att få a. Båda sidlängderna blir positiva.')],f'{a:.2f} cm.'.replace('.',',',1),'Skriv den ena sidan som en multipel av den andra.', 'Bestämmer en okänd skala ur ett sidförhållande och en summa.',fig=tri(A,B,a,{'a':'a','b':'b'},{0:'35°',1:'65°'},'Två sidor med given summa.'))

A=45;B=60;C=75;P=36;scale=P/(sin(A)+sin(B)+sin(C));a=scale*sin(A);ans=scale*sin(C)
add(535,p('En triangel har vinklarna 45°, 60° och 75° och omkretsen 36 cm. Hur lång är dess längsta sida? Svara i cm med två decimaler.'),ans,
 [p('Den längsta sidan ligger mittemot 75°. Sidorna är proportionella mot sinus till sina motstående vinklar.'),p('Sätt sidorna till k sin45°, k sin60° och k sin75°. Då gäller')+eq(r'k=\frac{36}{\sin45^\circ+\sin60^\circ+\sin75^\circ}'),p('Den längsta sidan är k sin75°. I beräkningen behålls k utan mellanavrundning.')],f'{ans:.2f} cm.'.replace('.',',',1),'Omkretsen bestämmer den gemensamma skalan i sinussatsen.', 'Kopplar tre sidförhållanden till omkrets och väljer rätt efterfrågad sida.',fig=tri(A,B,a,{}, {0:'45°',1:'60°',2:'75°'},'Triangel med given omkrets.'))

A=30;a=8;b=12;B=asin(b*sin(A)/a)
add(536,p('En triangel har A = 30°, a = 8 cm och b = 12 cm. Sidorna a och b ligger mittemot A respektive B. Bestäm alla möjliga värden på B. Svara i grader med en decimal. Figuren visar en möjlig form.'),[B,180-B],
 [p('Sinussatsen ger')+eq(r'\sin B=\frac{12\sin30^\circ}{8}=0{,}75'),p('Det ger B ≈ 48,6° eller 180°−48,6° ≈ 131,4°. Båda fungerar: med A = 30° blir vinkelsumman mindre än 180° i båda fallen.')],'B ≈ 48,6° eller 131,4°.','En sinus kan motsvara både en spetsig och en trubbig vinkel.', 'Kontrollerar båda sinuslösningarna mot triangelns vinkelsumma.',fig=tri(A,B,a,{'a':'8 cm','b':'12 cm'},{0:'30°'},'En möjlig form; även en annan triangel kan uppfylla uppgiften.'),labels=['Ett B-värde (°)','Det andra B-värdet (°)'],tol=.05)

A=40;b=10;a=b*sin(A)/sin(60);ans=b*sin(A)
add(537,p('Vinkeln A är 40° och den motstående sidan a är okänd. Sidan b, mittemot B, är 10 cm. Vilket är det minsta värde a kan ha för att en triangel ska vara möjlig? Svara i cm med två decimaler. Figuren är ett exempel, inte gränsfallet.'),ans,
 [p('Sinussatsen kräver sin B = 10 sin40°/a. Detta värde får vara högst 1.'),p('Därför måste a ≥ 10 sin40°. Gränsen är möjlig: B = 90° ger då C = 50°, så triangeln är inte hopfallen.')],f'{ans:.2f} cm.'.replace('.',',',1),'Hur stort kan sin B som mest vara?', 'Översätter sinusgränsen till ett möjligt längdintervall och verifierar gränsfallet.',fig=tri(A,60,a,{'a':'a','b':'10 cm'},{0:'40°'},'Exempel på triangel med A=40 grader och b=10 cm.'))

A=30;a=7;b=10;B=asin(b*sin(A)/a);C=180-A-B;c=a*sin(C)/sin(A);ans=.5*b*c*sin(A)
add(538,p('I en triangel är A = 30°, a = 7 cm och b = 10 cm. Det finns två möjliga trianglar. Bestäm den största möjliga arean. Svara i cm² med två decimaler. Figuren visar en av formerna.'),ans,
 [p('Sinussatsen ger sin B = 10 sin30°/7 = 5/7. Därför är B ungefär 45,58° eller 134,42°.'),p('De två C-vinklarna blir ungefär 104,42° och 15,58°. Beräkna sidan c för båda med c = 7 sin C/sin30°.'),p('Det större c-värdet ger den större arean, eftersom b och A är samma.')+eq(r'K_{\max}=\frac{10\cdot c_{\max}\cdot\sin30^\circ}{2}')],f'{ans:.2f} cm².'.replace('.',',',1),'Jämför de två möjliga trianglarna innan du väljer area.', 'Kombinerar tvetydigt sinusfall med en jämförelse av areor.',fig=tri(A,B,a,{'a':'7 cm','b':'10 cm'},{0:'30°'},'En av två möjliga trianglar.'),unit='cm²')

A=40;B=70;C=70;P=40;k=P/(sin(A)+sin(B)+sin(C));a=k*sin(A);b=k*sin(B);ans=.5*b*b*sin(A)
add(539,p('En likbent triangel har toppvinkeln A = 40° och omkretsen 40 cm. Bestäm dess area. Svara i cm² med två decimaler.'),ans,
 [p('Basvinklarna är (180°−40°)/2 = 70°. Om de lika sidorna är x ger sinussatsen basen a = x sin40°/sin70°.'),p('Omkretsvillkoret ger')+eq(r'x\left(2+\frac{\sin40^\circ}{\sin70^\circ}\right)=40'),p('Bestäm x och använd vinkeln mellan de lika sidorna.')+eq(r'K=\frac{x^2\sin40^\circ}{2}')],f'{ans:.2f} cm².'.replace('.',',',1),'Använd symmetrin för att få de två andra vinklarna.', 'Bestämmer sidlängder från omkrets innan arean kan beräknas.',fig=tri(A,B,a,{'b':'x','c':'x'},{0:'40°'},'Likbent triangel med två lika sidor.'),unit='cm²')

A=40;B=115;C=25;c=30;a=c*sin(A)/sin(C);b=c*sin(B)/sin(C);ans=b*sin(A)
add(540,p('A och B ligger på plan mark, 30 m från varandra. B ligger mellan A och huset. Vinkeln upp till takpunkten C är 40° från A och 65° från B. Hur högt över marken ligger C? Svara i m med två decimaler.'),ans,
 [p('Triangelns vinkel vid B är 180°−65° = 115°. Därför är vinkeln C 25°.'),p('Sinussatsen ger avståndet AC.')+eq(r'AC=\frac{30\sin115^\circ}{\sin25^\circ}'),p('Höjden är den lodräta delen av AC.')+eq(r'CH=AC\sin40^\circ')],f'{ans:.2f} m.'.replace('.',',',1),'Den uppmätta vinkeln vid B är en yttervinkel till triangeln ABC.', 'Skiljer observationsvinkel från triangelvinkel och kombinerar avstånd med höjd.',fig=tri(A,B,a,{'c':'30 m'},{0:'40°'},'Två observationspunkter och höjden till C.',altitude=True,externalB='65°'),unit='m')

A=60;B=80;C=40;c=10;a=c*sin(A)/sin(C);b=c*sin(B)/sin(C);ans=b*sin(A)/sin(100)
add(541,p('I triangeln är AB = 10 cm, A = 60° och B = 80°. CD delar vinkeln C i två lika stora delar, och D ligger på AB. Bestäm CD. Svara i cm med två decimaler.'),ans,
 [p('Först är C = 40°. Sinussatsen i hela triangeln ger AC = 10 sin80°/sin40°.'),p('I triangeln ACD är vinkeln vid C 20°, så vinkeln vid D är 100°.'),p('Använd sinussatsen i den mindre triangeln.')+eq(r'CD=\frac{AC\sin60^\circ}{\sin100^\circ}')],f'{ans:.2f} cm.'.replace('.',',',1),'Arbeta först i ABC och sedan i ACD.', 'Använder sinussatsen i två sammanhängande trianglar och utnyttjar en vinkelbisektris.',fig=tri(A,B,a,{'c':'10 cm'},{0:'60°',1:'80°'},'Triangel med bisektris CD.',bisector=2))

A=30;a=10;ans=a/sin(A)
add(542,p('I en triangel är A = 30° och a = 10 cm. Sidan b ligger mittemot B. Hur lång kan b som mest vara? Svara i cm med två decimaler. Figuren visar ett exempel.'),ans,
 [p('Sinussatsen ger b = 10 sin B/sin30° = 20 sin B.'),p('Sin B är som störst 1, vid B = 90°. Då blir C = 60°, vilket är en möjlig triangel. Största b är alltså 20 cm.')],'20,00 cm.','Vilken möjlig B-vinkel gör sin B störst?', 'Optimerar en sidlängd med sinus begränsning och kontrollerar vinkelsumman.',fig=tri(A,60,a,{'a':'10 cm','b':'b'},{0:'30°'},'En möjlig triangel, inte den med störst b.'))

A=35;a=10;b=14;B=180-asin(b*sin(A)/a);C=180-A-B;ans=a*sin(C)/sin(A)
add(543,p('Triangeln har A = 35°, a = 10 cm och b = 14 cm. Vinkeln B är trubbig. Bestäm sidan c mittemot C. Svara i cm med två decimaler.'),ans,
 [p('Sinussatsen ger sin B = 14 sin35°/10. Räknarens spetsiga vinkel ska ersättas med dess supplementvinkel eftersom B är trubbig.'),p('Beräkna sedan C = 180°−A−B och använd sinussatsen igen.')+eq(r'c=\frac{10\sin C}{\sin35^\circ}'),p('Behåll de oavrundade vinklarna tills sidan är beräknad.')],f'{ans:.2f} cm.'.replace('.',',',1),'Villkoret ”trubbig” avgör vilken sinuslösning som ska användas.', 'Väljer rätt vinkelgren före en ny sidberäkning.',fig=tri(A,B,a,{'a':'10 cm','b':'14 cm','c':'c'},{0:'35°'},'Triangel med trubbig vinkel B.'))

A=50;B=asin(sin(A)/2);C=180-A-B;a=10
add(544,p('I en triangel är A = 50° och sidan a dubbelt så lång som sidan b. Bestäm vinkeln C. Svara i grader med en decimal.'),C,
 [p('Sinussatsen ger sin B/sin50° = b/a = 1/2. Därför är den spetsiga B-vinkeln ungefär 22,5°.'),p('Den andra sinuslösningen skulle vara ungefär 157,5°. Tillsammans med A = 50° blir det mer än 180°, så den går inte.'),p('Den återstående vinkeln är C = 180°−50°−B.')],f'{C:.1f}°.'.replace('.',',',1),'Använd sidförhållandet; en bestämd längd behövs inte.', 'Översätter ett längdförhållande till en vinkel och utesluter den omöjliga grenen.',fig=tri(A,B,a,{'a':'2b','b':'b'},{0:'50°'},'Triangel med sidförhållandet två till ett.'),unit='°',tol=.05)

A=50;B=60;C=70;c=50;a=c*sin(A)/sin(C);ans=c*sin(30)/sin(100)
add(545,p('I triangeln är AB = 50 cm, A = 50° och B = 60°. BD delar vinkeln B i två lika stora delar. D ligger på AC. Bestäm AD. Svara i cm med två decimaler.'),ans,
 [p('I den mindre triangeln ABD är vinkeln vid B 30°. Vinkeln vid D är därför 180°−50°−30° = 100°.'),p('AB ligger mittemot 100° och AD mittemot 30°. Sinussatsen ger')+eq(r'AD=\frac{50\sin30^\circ}{\sin100^\circ}')],f'{ans:.2f} cm.'.replace('.',',',1),'Välj triangeln som innehåller den efterfrågade delen AD.', 'Väljer en deltriangel och använder halverad vinkel i rätt motstående par.',fig=tri(A,B,a,{'c':'50 cm'},{0:'50°'},'Triangel med vinkelbisektris BD.',bisector=1))

A=50;a=10;b=13;B=asin(b*sin(A)/a)
add(546,p('I en triangel är A = 50°, a = 10 cm och b = 13 cm. Hur många olika trianglar uppfyller villkoren och har B &gt; 90°? Svara med ett heltal. Figuren visar en möjlig form.'),1,
 [p('Sinussatsen ger sin B = 13 sin50°/10 ≈ 0,99586. Det finns en spetsig och en trubbig lösning.'),p('Den trubbiga är ungefär 95,2°. Med A = 50° återstår en positiv C-vinkel, ungefär 34,8°. Den trubbiga lösningen är alltså tillåten.'),p('Endast en av de två möjliga trianglarna har B > 90°.')],'1 triangel.','Kontrollera både om sinuslösningen är trubbig och om vinkelsumman tillåter den.', 'Räknar de trianglar som uppfyller ett extra villkor, inte bara antalet sinuslösningar.',fig=tri(A,B,a,{'a':'10 cm','b':'13 cm'},{0:'50°'},'En möjlig form; uppgiften gäller alla trianglar som uppfyller villkoren.'),unit='')
TASKS[-1]['svarEnhet']='';TASKS[-1]['tolerans']=0

A=30;B=80;x=2*sin(B)/(1-sin(B));a=x+2
add(547,p('I triangeln är A = 30° och B = 80°. Sidan a är (x+2) cm och sidan b är 2x cm. Bestäm x. Svara med två decimaler.'),x,
 [p('Sinussatsen ger ett samband mellan de två uttrycken.')+eq(r'\frac{x+2}{\sin30^\circ}=\frac{2x}{\sin80^\circ}'),p('Eftersom sin30° = 1/2 får vi (x+2)sin80° = x.'),p('Samla x-termerna och lös ut x.')+eq(r'x=\frac{2\sin80^\circ}{1-\sin80^\circ}')],f'x ≈ {x:.2f}.'.replace('.',',',1),'Behandla x som en obekant även när trigonometriska tal ingår.', 'Algebraisk mängdträning med en parameter i båda sidlängderna.',fig=tri(A,B,a,{'a':'x + 2','b':'2x'},{0:'30°',1:'80°'},'Två sidlängder uttryckta med samma parameter.'),unit='')
TASKS[-1]['svarEnhet']=''

A=35;B=70;C=75;K=60;a=math.sqrt(2*K*sin(A)/(sin(B)*sin(C)))
add(548,p('En triangel har A = 35°, B = 70° och arean 60 cm². Bestäm sidan a mittemot A. Svara i cm med två decimaler.'),a,
 [p('Vinkeln C är 75°. Sinussatsen uttrycker de två övriga sidorna med a.')+eq(r'b=\frac{a\sin70^\circ}{\sin35^\circ},\quad c=\frac{a\sin75^\circ}{\sin35^\circ}'),p('Sätt in dem i areasatsen K = bc sin A/2 och förenkla.')+eq(r'60=\frac{a^2\sin70^\circ\sin75^\circ}{2\sin35^\circ}'),p('Lös ut a² och ta den positiva roten eftersom a är en längd.')],f'{a:.2f} cm.'.replace('.',',',1),'Använd vinklarna för att uttrycka alla längder med samma skala.', 'Återskapar en längd från area och vinklar genom två satser och en kvadratrot.',fig=tri(A,B,a,{'a':'a'},{0:'35°',1:'70°'},'Triangel med given area och två vinklar.'))

if __name__=='__main__':
 path=h.ROOT/'uppgiftermato1.js';raw=path.read_text();q=TASKS[0];pos=raw.index('"id": "4.52"');start=raw.rfind('{',0,pos);old,n=json.JSONDecoder().raw_decode(raw[start:]);old.update(q);path.write_text(raw[:start]+json.dumps(old,ensure_ascii=False,indent=2)+raw[start+n:]);h.install(TASKS[1:])
 (h.ROOT/'agent/MA3_SINUS_C_2026-10-25.json').write_text(json.dumps(REVIEW,ensure_ascii=False,indent=2)+'\n');(h.ROOT/'tools/ma3-sinus-c-2026-10-25.cases.json').write_text(json.dumps(CASES,ensure_ascii=False,indent=2)+'\n')
