"""20 nya problem med potensderivata; mängdträning och samband kompletterar varandra."""
import importlib.util,json,math,re
from pathlib import Path
sp=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p,m,eq,graph,table,svg,text=h.p,h.m,h.eq,h.graph,h.table,h.svg,h.text
TASKS=[];REVIEW={};CASES={}
def line_legend(fig,kind):
 matches=list(re.finditer(r'<polyline[^>]+/>',fig));last=matches[-1]
 fig=fig[:last.start()]+last.group().replace('#096c9a','#a15320')+fig[last.end():]
 return fig.replace('0 0 500 320','0 0 500 355').replace('height="320"','height="355"').replace('</svg>',text(250,340,'Blå: funktion. Orange: '+kind+'.',16)+'</svg>')

def add(n,t,ans,steps,final,hint,why,fig='',labels=None,options=None,unit=None,fmt='uttryck',calc=True):
 q=h.make('2.'+str(n),'derivata_potens','Potensderivata – samband och parametrar',3,t,ans,steps,final,hint,fig=fig,labels=labels,options=options,unit=unit,skills=['begrepp','problemlösning']);q.update(kap=2,poang='0/2/0',miniräknare=calc)
 if not options:q.update(svarFormat=[fmt]*len(ans) if labels else fmt,svarstyp='flera_delar' if labels else ('uttryck' if fmt=='uttryck' else 'numeriskt'),tolerans=[None]*len(ans) if labels else (None if fmt=='uttryck' else 1e-9))
 TASKS.append(q);REVIEW[q['id']]={'C-motivering':why,'figur':'Relevant figur/tabell.' if fig else 'Algebraiska samband är innehållet; ingen extra illustration behövs.','verktyg':'Miniräknare tillåten, GeoGebra behövs inte.' if calc else 'Symbolisk jämförelse prövas utan räknare.','kommentar':final}

add(1221,p('Funktionen är '+m('f(x)=ax^n')+' för x &gt; 0. Tabellen anger både ett funktionsvärde och en derivata. Bestäm a och n.'),[6,1.5],
 [p('Vid x = 1 är 1ⁿ = 1, så f(1) = a = 6.'),p('Potensregeln ger f′(x) = an xⁿ⁻¹. Använd nu derivatans värde.')+eq(r'6n=9\Rightarrow n=\frac32')],'a = 6 och n = 1,5.','Funktionsvärdet och derivatan ger två olika villkor.','Bestämmer både koefficient och exponent från två slags information.',fig=table(['Villkor','Värde'],[ [m('f(1)'),'6'],[m("f'(1)"),'9']]),labels=['a','n'])

add(1222,p('Funktionen är '+m('f(x)=x^n')+', där n &gt; 0. Tangentens lutning vid x = 8 är 16 gånger lutningen vid x = 2. Bestäm n.'),3,
 [p('Derivatan är n xⁿ⁻¹. Jämför de två lutningarna genom att bilda en kvot.')+eq(r'\frac{n\cdot8^{n-1}}{n\cdot2^{n-1}}=16'),p('n är positivt och kan förkortas bort.')+eq(r'4^{n-1}=16=4^2'),p('Därför är n−1 = 2 och n = 3.')],'n = 3.','Uttryck båda lutningarna med potensregeln och jämför dem.','Resonerar om hur derivatan skalar när x ändras, inte bara ett derivatavärde.')

add(1223,p('Funktionen '+m(r'f(x)=a\sqrt{x}+\frac b x')+' går genom (1, 6) och har en vågrät tangent där. Bestäm a och b.'),[4,2],
 [p('Punkten ger a+b = 6. En vågrät tangent betyder f′(1) = 0.'),p('Skriv termerna som potenser och derivera.')+eq(r"f'(x)=\frac a{2\sqrt{x}}-\frac b{x^2}"),p('Vid x = 1 får vi a/2−b = 0. Alltså är b = a/2 och 3a/2 = 6.')],'a = 4 och b = 2.','Översätt punkt och vågrät tangent till var sitt villkor.', 'Kombinerar funktionens höjd och lutning med bråk- och negativa exponenter.',labels=['a','b'])

add(1224,p('Funktionen är '+m(r'f(x)=x^2+\frac kx')+' för x &gt; 0. Bestäm k så att grafen har en vågrät tangent vid x = 2.'),16,
 [p('En vågrät tangent betyder att derivatan är noll. Kvottermen skrivs kx⁻¹.')+eq(r"f'(x)=2x-kx^{-2}"),p('Sätt in x = 2 och lös villkoret.')+eq(r'4-\frac k4=0\Rightarrow k=16')],'k = 16.','Vad måste derivatan vara när tangenten är vågrät?','Översätter ett geometriskt krav till en parameter i en negativ potens.')

add(1225,p('För vilket positivt x-värde är grafens tangent vågrät?')+eq(r'f(x)=x\sqrt{x}-12\sqrt{x}'),4,
 [p('Skriv x√x som x³ᐟ² och derivera.')+eq(r"f'(x)=\frac32\sqrt{x}-\frac6{\sqrt{x}}"),p('Sätt derivatan till noll. Eftersom x > 0 får vi multiplicera med 2√x.')+eq(r'3x-12=0\Rightarrow x=4')],'x = 4.','Skriv båda termerna som potenser innan du deriverar.','Behöver välja en omskrivning och lösa ett villkor som innehåller både rot och invers rot.')

add(1226,p('Funktionen är '+m(r'f(x)=\dfrac{x^3+4x}{\sqrt{x}}')+' för x &gt; 0. Vilket påstående med motivering är korrekt?'),None,
 [p('Dela upp kvoten och använd potenslagarna.')+eq(r'f(x)=x^{5/2}+4x^{1/2}'),p('Derivera.')+eq(r"f'(x)=\frac52x^{3/2}+2x^{-1/2}"),p('Båda termerna är positiva när x > 0. Funktionen är därför växande på hela sin definitionsmängd.')],'Funktionen växer eftersom båda termerna i derivatan är positiva.','En kvot kan ibland skrivas som en summa av potenser.', 'Väljer en algebraisk strategi och drar en slutsats om hela grafen.',calc=False,options=[('Funktionen avtar eftersom x finns i nämnaren.',False),('Funktionen har ett minimum eftersom derivatan byter tecken.',False),('Funktionen växer eftersom båda termerna i derivatan är positiva.',True),('Funktionen är konstant eftersom alla termer innehåller x.',False)])

fig=graph('Rotkurva och tangent i en okänd punkt. Tangenten skär x-axeln vid −9.',(-12,16),(-1,5),[[(i/10,math.sqrt(i/10)) for i in range(161)],[(-12,-.5),(16,25/6)]],[-9,0],[0],dots=[(9,3,True)],xlabel='x',ylabel='y')
# Rita de verkliga axlarna, inte grafens nedre/vänstra ram.
fig=fig.replace('M65 45V250H445','M223.571 45V250 M65 216.667H445')
fig=line_legend(fig,'tangent')
add(1227,p('En tangent till '+m(r'y=\sqrt{x}')+' skär x-axeln vid −9. Bestäm tangentpunktens x-koordinat exakt. Figuren visar situationen.'),9,
 [p('Kalla tangentpunktens x-koordinat a. Punkten är (a, √a), och derivatan ger lutningen 1/(2√a).'),p('Samma lutning fås från tangentens två punkter (−9, 0) och (a, √a).')+eq(r'\frac{\sqrt a}{a+9}=\frac1{2\sqrt a}'),p('Multiplicera med 2√a(a+9).')+eq(r'2a=a+9\Rightarrow a=9')],'x = 9.','Beskriv tangentens lutning både med derivatan och med två punkter.', 'Kombinerar potensderivata och koordinatgeometri med okänd tangentpunkt.',fig=fig)

fig=graph('Kurva a/x² och linjen y=−3x+9 som tangerar den. Skalan medger ingen säker exakt tangentpunkt.',(0,5),(0,10),[[(i/50,12/(i/50)**2) for i in range(55,251)],[(0,9),(3,0)]],[0,3],[0,9])
fig=line_legend(fig,'tangent')
add(1228,p('Linjen '+m('y=-3x+9')+' tangerar grafen till '+m(r'f(x)=a/x^2')+' i en punkt med positiv x-koordinat. Bestäm a exakt.'),12,
 [p('Om tangentpunkten har x-koordinaten u måste både höjden och lutningen stämma.')+eq(r'\frac a{u^2}=-3u+9')+eq(r'-\frac{2a}{u^3}=-3'),p('Lutningsvillkoret ger a = 3u³/2. Sätt in det i höjdvillkoret.')+eq(r'\frac32u=-3u+9\Rightarrow u=2'),p('Då är a = 3·2³/2 = 12.')],'a = 12.','En tangent har både samma höjd och samma lutning som kurvan i tangentpunkten.', 'Två tangensvillkor måste kombineras och den okända punkten bestämmas.',fig=fig)

add(1229,p('Funktionen är '+m('f(x)=x^n')+', där n är ett heltal och n ≥ 2. Det gäller att '+m("f''(1)=20")+'. Bestäm n.'),5,
 [p('Derivera två gånger.')+eq(r"f''(x)=n(n-1)x^{n-2}"),p('Vid x = 1 blir villkoret n(n−1) = 20.')+eq(r'n^2-n-20=0')+eq(r'(n-5)(n+4)=0'),p('Rötterna är 5 och −4. Villkoret n ≥ 2 gör att endast 5 är tillåtet.')],'n = 5.','Hur ser koefficienten ut efter två deriveringar?', 'Kopplar okänd exponent till andraderivata och väljer rätt rot med hjälp av villkoret.')

add(1230,p('En elev deriverar '+m(r'f(x)=1/\sqrt{x}')+' och får felaktigt '+m(r'-1/(2\sqrt{x})')+'. Vid x = 1 råkar elevens värde bli rätt. Hur många gånger så stort som den riktiga derivatans belopp blir elevens belopp vid x = 4?'),4,
 [p('Skriv f(x) = x⁻¹ᐟ². Exponenten ska minska med 1 vid derivering.')+eq(r"f'(x)=-\frac12x^{-3/2}"),p('Vid x = 4 är den riktiga derivatan −1/16. Elevens uttryck ger −1/4.'),p('Jämför beloppen.')+eq(r'\frac{1/4}{1/16}=4')],'4 gånger.','Kontrollera exponenten efter deriveringen; ett enda provvärde räcker inte.', 'Analyserar varför ett fel kan döljas vid ett provvärde och mäter felet vid ett annat.')

add(1231,p('En vagns läge ges av '+m('s(t)=20-80/t')+' för t ≥ 4, där s mäts i meter och t i sekunder. Vilken hastighet har vagnen när dess läge är 10 m? Svara i m/s med två decimaler.'),1.25,
 [p('Bestäm först när vagnen är vid 10 m.')+eq(r'20-\frac{80}{t}=10\Rightarrow t=8'),p('Hastigheten är lägets derivata. Skriv −80/t som −80t⁻¹.')+eq(r"s'(t)=80t^{-2}"),p('Beräkna hastigheten vid t = 8.')+eq(r"s'(8)=\frac{80}{64}=1{,}25")],'1,25 m/s.','Den sökta tidpunkten ges av läget, men hastigheten fås från derivatan.', 'Skiljer läge och hastighet och kopplar ihop dem genom en okänd tidpunkt.',fig=table(['Storhet','Enhet'],[['s(t): läge','m'],['t: tid','s']]),fmt='numeriskt',unit='m/s')
TASKS[-1]['tolerans']=.005

fig=graph('Rotkurva med en sekant genom (1,1) och (9,3).',(0,10),(0,4),[[(i/20,math.sqrt(i/20)) for i in range(201)],[(1,1),(9,3)]],[0,1,4,9],[0,1,2,3,4],dots=[(1,1,True),(9,3,True)])
fig=line_legend(fig,'sekant')
add(1232,p('Funktionen är '+m(r'f(x)=\sqrt{x}')+'. Vid vilket x-värde har tangenten samma lutning som sekanten genom (1, 1) och (9, 3)? Svara exakt.'),4,
 [p('Sekantens lutning är förändringskvoten.')+eq(r'k=\frac{3-1}{9-1}=\frac14'),p('Sätt derivatan lika med sekantens lutning.')+eq(r'\frac1{2\sqrt{x}}=\frac14'),p('Då är √x = 2 och x = 4.')],'x = 4.','Jämför en medellutning med den lokala lutningen.', 'Översätter mellan sekant, tangent och en ekvation med bråkexponent.',fig=fig)

add(1233,p('Efterfrågan beskrivs av '+m('D(p)=120000p^{-1{,}5}')+', där p är priset i kronor. Använd tangenten vid p = 100 för att uppskatta hur många procent efterfrågan minskar när priset höjs från 100 till 105 kr. Svara med en decimal.'),7.5,
 [p('Beräkna efterfrågan och lutningen vid det gamla priset.')+eq(r'D(100)=120')+eq(r"D'(p)=-180000p^{-2{,}5}") +eq(r"D'(100)=-1{,}8"),p('Tangenten uppskattar ändringen vid en höjning med 5 kr till −1,8·5 = −9.'),p('Minskningen jämförs med efterfrågan före höjningen.')+eq(r'\frac9{120}\cdot100=7{,}5\,\%')],'7,5 %.','Tangentens lutning uppskattar ändringen i antal per krona, inte procent direkt.', 'Kopplar negativ bråkexponent till lokal linjär uppskattning och relativ förändring.',fmt='numeriskt',unit='%')
TASKS[-1]['tolerans']=.05

add(1234,p('Två funktioner är '+m(r'f(x)=\sqrt{x}-2/x')+' och '+m(r'g(x)=\sqrt{x}+3/x')+' för x &gt; 0. Kan deras tangenter vara parallella vid samma x-värde? Välj rätt svar med motivering.'),None,
 [p('Parallella tangenter måste ha lika derivator.')+eq(r"f'(x)=\frac1{2\sqrt{x}}+\frac2{x^2}")+eq(r"g'(x)=\frac1{2\sqrt{x}}-\frac3{x^2}"),p('Skillnaden är 5/x², som är positiv för alla tillåtna x. Derivatorna kan därför aldrig vara lika.')],'Nej, f′(x)−g′(x) är alltid positiv.','Jämför derivatornas skillnad i stället för att försöka gissa ett x-värde.', 'Avgör ett existenspåstående genom att jämföra två derivator symboliskt.',calc=False,options=[('Ja, eftersom båda innehåller √x.',False),('Ja, vid x = 1 eftersom x² = 1.',False),('Nej, eftersom graferna har olika höjd.',False),('Nej, f′(x)−g′(x) är alltid positiv.',True)])

add(1235,p('Funktionen är '+m(r'f(x)=a/x^2+b/x')+'. Tangentens lutning är −7 vid x = 1 och −1,25 vid x = 2. Bestäm a och b.'),[2,3],
 [p('Derivera de två negativa potenserna.')+eq(r"f'(x)=-2ax^{-3}-bx^{-2}"),p('De två lutningarna ger')+eq(r'-2a-b=-7')+eq(r'-a/4-b/4=-1{,}25'),p('Den andra ekvationen ger a+b = 5. Den första ger 2a+b = 7. Subtraktion ger a = 2 och sedan b = 3.')],'a = 2 och b = 3.','Samma derivata ska uppfylla båda lutningsvillkoren.', 'Ställer upp och löser ett ekvationssystem från två lokala lutningar.',labels=['a','b'])

add(1236,p('Bestäm det minsta värdet av '+m(r'f(x)=x^2-4\sqrt{x}')+' för x &gt; 0. Svara exakt.'),-3,
 [p('Derivera och samla uttrycket över en positiv nämnare.')+eq(r"f'(x)=2x-\frac2{\sqrt{x}}")+eq(r'=\frac{2(x\sqrt{x}-1)}{\sqrt{x}}'),p('Derivatan är noll vid x = 1. För 0 < x < 1 är den negativ, och för x > 1 är den positiv. Funktionen avtar alltså fram till 1 och växer därefter.'),p('Beräkna funktionens värde, inte bara x-koordinaten.')+eq(r'f(1)=1-4=-3')],'Det minsta värdet är −3.','Efter att du hittat en stationär punkt behöver du kontrollera tecknet och beräkna funktionsvärdet.', 'Kombinerar rotderivata, stationärt villkor, teckenstudium och efterfrågat funktionsvärde.')

add(1237,p('Funktionen är '+m(r'f(x)=\dfrac{x^2-1}{x^{3/2}}')+' för x &gt; 0. Vilken beskrivning av derivatan f′ är korrekt? Välj ett alternativ.'),None,
 [p('Skriv om funktionen som två potenser.')+eq(r'f(x)=x^{1/2}-x^{-3/2}'),p('Derivatan är positiv eftersom båda termerna är positiva.')+eq(r"f'(x)=\frac12x^{-1/2}+\frac32x^{-5/2}"),p('När x ökar minskar båda termerna, eftersom exponenterna är negativa. Därför är f′ positiv och avtagande.')],'f′ är positiv och avtagande.','Undersök både tecknet på termerna i derivatan och vad som händer när x ökar.', 'Skiljer funktionens förändring från derivatans förändring efter en nödvändig omskrivning.',calc=False,options=[('f′ är negativ och avtagande.',False),('f′ är positiv och växande.',False),('f′ är positiv och avtagande.',True),('f′ byter tecken vid x = 1.',False)])

add(1238,p('Funktionen är '+m(r'f(x)=\sqrt{x}+c/\sqrt{x}')+' för x &gt; 0, där c &gt; 0. Funktionens minsta värde är 4. Bestäm c.'),4,
 [p('Derivera och samla termerna.')+eq(r"f'(x)=\frac{x-c}{2x^{3/2}}"),p('Nämnaren är positiv. Derivatan byter tecken från minus till plus vid x = c, så minimivärdet är f(c) = 2√c.'),p('Använd det givna minimivärdet.')+eq(r'2\sqrt c=4\Rightarrow c=4')],'c = 4.','Minimipunktens x-värde är inte samma sak som funktionens minsta värde.', 'Bestämmer en parameter genom både derivatans tecken och extremvärdets höjd.')

add(1239,p('Funktionerna är '+m('f(x)=x^3')+' och '+m('g(x)=-3/x')+', där x ≠ 0. Vid vilka x-värden är deras tangenter parallella med varandra? Jämför tangenter vid samma x-värde och ange alla svar exakt.'),[-1,1],
 [p('Parallella tangenter har lika lutning.')+eq(r"f'(x)=3x^2,\qquad g'(x)=3x^{-2}"),p('Sätt derivatorna lika och multiplicera med x², som inte är noll.')+eq(r'3x^2=3/x^2\Rightarrow x^4=1'),p('Båda reella lösningarna −1 och 1 är tillåtna. I båda fallen är lutningen 3.')],'x = −1 eller x = 1.','Olika höjd hindrar inte två tangenter från att vara parallella.', 'Jämför positiva och negativa potenser och hittar hela lösningsmängden.',labels=['En lösning','Den andra lösningen'])
TASKS[-1]['svarsstruktur']='mängd'

body='<polygon points="80,250 400,250 80,40" fill="#e7f3fa"/><path d="M65 250H455 M80 265V25" stroke="#344c60" stroke-width="2" fill="none"/><path d="M80 40L400 250" stroke="#a15320" stroke-width="3"/>'
body+='<polyline points="'+' '.join(f'{80+160*i/100:.3f},{250-105/(i/100):.3f}' for i in range(50,231))+'" fill="none" stroke="#096c9a" stroke-width="3.5"/>'
body+='<circle cx="240" cy="145" r="5" fill="#096c9a"/>'+text(240,184,'P',18)+text(80,285,'0',17)+text(450,275,'x',18)+text(60,28,'y',18)+text(250,310,'Orange: tangent. Skuggat: triangel.',16)
fig=svg('En tangent till y=1/x i första kvadranten bildar en triangel med koordinataxlarna.',body,335)
add(1240,p('En tangent till '+m('f(x)=1/x')+' dras i en punkt P med positiv x-koordinat. Tangenten och koordinataxlarna bildar en triangel. Bestäm triangelns area exakt.'),2,
 [p('Kalla tangentpunktens x-koordinat a. Punkten är (a, 1/a) och tangentens lutning är −1/a².')+eq(r'y-1/a=-(x-a)/a^2'),p('Tangentens ekvation kan därför skrivas')+eq(r'y=-x/a^2+2/a'),p('Skärningarna med axlarna ger basen 2a och höjden 2/a. Arean blir')+eq(r'A=\frac{2a\cdot(2/a)}2=2'),p('Parametern försvinner: arean är samma för varje positivt a.')],'2 areaenheter.','Uttryck tangentens båda axelskärningar med hjälp av samma okända tangentpunkt.', 'Kombinerar generell potensderivata, tangentekvation och triangelarea; parametern elimineras.',fig=fig)

for n,valid,invalid in [(1222,['3','n=3'],['2','4']),(1224,['16'],['4','8']),(1225,['4'],['2','16']),(1227,['9'],['-9','3']),(1228,['12'],['2','3']),(1229,['5'],['-4','20']),(1230,['4'],['0.25','16']),(1231,['1,25','1.25 m/s'],['8','10','1.24']),(1232,['4'],['5','2']),(1233,['7,5','7.5 %'],['9','7.1']),(1236,['-3'],['1','3']),(1238,['4'],['2','16']),(1240,['2'],['1','4'])]:CASES['mato1:2.'+str(n)]=[valid,invalid]
if __name__=='__main__':
 path=h.ROOT/'uppgiftermato1.js';raw=path.read_text();pos=raw.index('"id": "2.217"');start=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[start:]);q.update(traningsniva=2,niva='E',poang='2/0/0');path.write_text(raw[:start]+json.dumps(q,ensure_ascii=False,indent=2)+raw[start+n:])
 h.install(TASKS)
 (h.ROOT/'agent/MA3_POTENS_C_2026-10-25.json').write_text(json.dumps(REVIEW,ensure_ascii=False,indent=2)+'\n')
 (h.ROOT/'tools/ma3-potens-c-2026-10-25.cases.json').write_text(json.dumps(CASES,ensure_ascii=False,indent=2)+'\n')
