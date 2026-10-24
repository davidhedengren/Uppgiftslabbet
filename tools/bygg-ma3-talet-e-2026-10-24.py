"""Åtta handskrivna uppgifter med talet e, grafer och modeller."""
import importlib.util,json,math,re
from pathlib import Path
sp=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p,m,eq,sol,graph,table,text=h.p,h.m,h.eq,h.sol,h.graph,h.table,h.text
TASKS=[]
def tangent_legend(fig):
 segments=list(re.finditer(r'<polyline[^>]+/>',fig));last=segments[-1]
 fig=fig[:last.start()]+last.group().replace('#096c9a','#b35316')+fig[last.end():]
 return fig.replace('0 0 500 320','0 0 500 360').replace('height="320"','height="360"').replace('</svg>',text(250,340,'Orange linje: tangent.',17)+'</svg>')
def add(n,level,*args,expression=False,**kw):
 q=h.make('2.'+str(n),'talet_e','Talet e i grafer och modeller',level,*args,**kw);q['kap']=2
 if n==1199:q['tolerans']=0.0005
 if expression:q.update(svarstyp='uttryck',svarFormat='uttryck',tolerans=None)
 TASKS.append(q)

fig=graph('Grafen till e upphöjt till x med tangent i (0,1). Tangenten går även genom (1,2).',(-1,2),(0,4),[[(i/100,math.exp(i/100)) for i in range(-100,139)],[(-1,0),(2,3)]],[-1,0,1,2],[0,1,2,3,4],dots=[(0,1,True),(1,2,True)])
fig=tangent_legend(fig)
add(1193,1,p('Figuren visar '+m('f(x)=e^x')+' och tangenten vid x = 0. De markerade punkterna (0, 1) och (1, 2) ligger på tangenten. Bestäm '+m(r"f'(0)")+'.'),1,[p('Derivatan är tangentens lutning. När x ökar från 0 till 1 ökar y från 1 till 2.')+eq(r"f'(0)=\frac{2-1}{1-0}=1")],'1.','Använd de två punkterna på tangenten.',fig=fig)
add(1194,1,p('Grafen till '+m('g(x)=e^x+7')+' är grafen till '+m('e^x')+' flyttad 7 enheter uppåt. Bestäm '+m(r"g'(x)")+'.'),'e^x',[p('Derivatan av eˣ är eˣ. Konstanten 7 har derivatan 0. En förflyttning uppåt ändrar inte lutningen.')],m(r"g'(x)=e^x")+'.','Vad händer med lutningen om hela grafen flyttas uppåt?',expression=True)
add(1195,2,p('En växts massa beskrivs av '+m('M(t)=Ce^{kt}')+', där M mäts i gram och t i dygn. Tabellen gäller vid samma tidpunkt. Bestäm k.'),.15,[p('Derivering ger M′(t) = kCeᵏᵗ = kM(t). Använd båda tabellvärdena vid den aktuella tidpunkten.')+eq(r'12=k\cdot80\quad\Rightarrow\quad k=0{,}15')],'k = 0,15.','Jämför uttrycket för massan med uttrycket för dess förändring.',fig=table(['Storhet','Värde'],[['Massa','80 g'],['Massökning per dygn','12 g/dygn']]))
fig=graph('En dryck svalnar från 80 grader och närmar sig rumstemperaturen 20 grader.',(0,30),(0,100),[[(i/5,20+60*math.exp(-.1*i/5)) for i in range(151)]],[0,10,20,30],[0,20,40,60,80,100],xlabel='Tid t (min)',ylabel='Temperatur (°C)')
add(1196,3,p('En drycks temperatur är '+m('T(t)=20+60e^{-0{,}1t}')+' °C efter t minuter. Hur snabbt sjunker temperaturen när drycken är 40 °C? (Svara med ett positivt tal i °C/min.)'),2,[p('När T = 40 är den exponentiella delen 40−20 = 20.')+eq(r'60e^{-0{,}1t}=20'),p('Derivera modellen.')+eq(r"T'(t)=-0{,}1\cdot60e^{-0{,}1t}"),p('Vid den aktuella tidpunkten är derivatan −0,1·20 = −2 °C/min. Temperaturen sjunker alltså med 2 °C per minut.')],'2 °C/min.','Jämför derivatan med temperaturens skillnad från 20 °C.',fig=fig,unit='°C/min')
fig=graph('Grafen till Ae upphöjt till kx och tangenten vid x=0. Tangenten går genom (0,3) och (1,9).',(-1,1),(0,12),[[(i/100,3*math.exp(2*i/100)) for i in range(-100,70)],[(-.5,0),(1,9)]],[-1,0,1],[0,3,6,9,12],dots=[(0,3,True),(1,9,True)])
fig=tangent_legend(fig)
add(1197,3,p('Grafen visar '+m('f(x)=Ae^{kx}')+' och tangenten vid x = 0. Tangenten går genom de markerade punkterna (0, 3) och (1, 9). Bestäm A och k.'),[3,2],[p('f(0) = A eftersom e⁰ = 1. Grafen går genom (0, 3), så A = 3.'),p('Tangentens lutning är (9−3)/(1−0) = 6. Derivatan vid 0 är Ak.')+eq(r'3k=6\quad\Rightarrow\quad k=2')],'A = 3 och k = 2.','Använd tangentens punkt och lutning var för sig.',fig=fig,labels=['A','k'])
add(1198,3,p('Funktionerna är '+m('f(x)=e^{2x}')+' och '+m('g(x)=4e^x')+'. Vid vilket x-värde har deras grafer samma lutning? Svara exakt.'),'ln(2)',[p('Samma lutning betyder att derivatorna är lika.')+eq(r'2e^{2x}=4e^x'),p('Dividera med 2eˣ, som alltid är positivt.')+eq(r'e^x=2\quad\Rightarrow\quad x=\ln2')],m(r'x=\ln2')+'.','Det är derivatorna som ska vara lika, inte funktionsvärdena.',expression=True)
add(1199,2,p('En modell är '+m('N(t)=500e^{kt}')+', där t mäts i år. Antalet ökar med 10 % på ett år. Bestäm k. (Svara med tre decimaler.)'),math.log(1.1),[p('Efter ett år ska modellen ge 500·1,10 = 550.')+eq(r'500e^k=550\quad\Rightarrow\quad e^k=1{,}10'),p('Ta naturliga logaritmen.')+eq(r'k=\ln(1{,}10)\approx0{,}095')],'k ≈ 0,095.','Vilken förändringsfaktor motsvarar ett års ökning?',fig=table(['Tid (år)','Antal enligt modellen'],[['0','500'],['1','550']]))
add(1200,4,p('Funktionen är '+m('f(x)=e^{kx}+ax')+', där k &gt; 0. Det gäller att '+m(r"f'(0)=0")+' och '+m(r"f''(0)=9")+'. Bestäm k och a.'),[3,-3],[p('Derivera en och två gånger.')+eq(r"f'(x)=ke^{kx}+a")+eq(r"f''(x)=k^2e^{kx}"),p('Vid x = 0 ger den andra derivatan k² = 9. Villkoret k > 0 ger k = 3.'),p('Den första derivatan ger k+a = 0, så a = −3.')],'k = 3 och a = −3.','Börja med villkoret på andraderivatan.',labels=['k','a'])

NOTE_IDS=['2.06','2.07','2.11','2.15','2.19']
def revise(q):
 if q['id']=='2.06':
  q['s']=sol([p('Derivatan är '+m(r"f'(x)=3x^2-6")+'. Vid x = 2 är lutningen 3·4−6 = 6.'),p('Beräkna punktens y-koordinat.')+eq('f(2)=8-12+4=0'),p('Tangenten går genom (2, 0) och har lutningen 6.')+eq('y=6(x-2)=6x-12')],m('y=6x-12')+'.')
 if q['id']=='2.07':
  q['s']=sol([p('Parallella linjer har samma lutning. Den sökta tangentens lutning är därför 4. Derivatan är '+m(r"f'(x)=2x-2")+'.')+eq(r'2x-2=4\quad\Rightarrow\quad x=3'),p('Beräkna punktens y-koordinat.')+eq('f(3)=9-6+5=8'),p('Tangenten går genom (3, 8) och har lutningen 4.')+eq('y-8=4(x-3)')],m('y=4x-4')+'.')
 if q['id'] in ['3.896','3.917']:
  rate,n,value=(40,10,150) if q['id']=='3.896' else (60,15,400)
  q['s']=sol([p('Derivera och sätt derivatan lika med noll.')+eq("V'(x)=-4x+"+str(rate)+'=0')+p('Det ger x = '+str(n)+'. Parabeln är nedåtvänd, så där finns dess största värde.'),p('Beräkna vinsten vid detta antal varor.')+eq('V('+str(n)+')=-2\\cdot'+str(n)+'^2+'+str(rate)+'\\cdot'+str(n)+'-50')+eq('='+str(value))],str(value)+' kr.')
 if q['id'] in NOTE_IDS:
  q['s']=re.sub(r'<ol class="facit-steglista" role="list"><li><p class="facit-not">Vid olikheter ska tecknet vändas när du multiplicerar eller dividerar med ett negativt tal\.</p></li></ol>','',q['s'])
 if q['id']=='2.20':
  intro=p('Funktionen är '+m('f(x)=3e^{0{,}5x}')+'.')
  a=p('Bestäm '+m(r"f'(x)")+'.');b=p('Bestäm tangentens ekvation vid x = 0.')
  sa=sol([p('Derivatan av '+m('e^{0{,}5x}')+' innehåller faktorn 0,5 från exponenten.')+eq(r"f'(x)=3\cdot0{,}5e^{0{,}5x}")],m(r"f'(x)=1{,}5e^{0{,}5x}")+'.')
  sb=sol([p('Vid x = 0 är f(0) = 3. Derivatan är '+m(r"f'(x)=1{,}5e^{0{,}5x}")+', så tangentens lutning är f′(0) = 1,5.'),p('Linjen har lutningen 1,5 och skär y-axeln i 3.')],m('y=1{,}5x+3')+'.')
  q.update(t=intro+p('a) '+a[3:-4])+p('b) '+b[3:-4]),s=p('<strong>a)</strong>')+sa+p('<strong>b)</strong>')+sb,traningsniva=2,arbetsinsats=2,poang='2/0/0',miniräknare=True,geogebra=False,spel=True,självrättning=True,svarstyp='flera_delar',svarFormat=['uttryck','uttryck'],rättSvar=['1.5*e^(0.5*x)','1.5*x+3'],tolerans=[None,None],svarsstruktur='ordnad',spelDelning='deluppgifter',spelDelar=[dict(etikett='a',t=intro+a,s=sa,traningsniva=2,arbetsinsats=1,poang='1/0/0'),dict(etikett='b',t=intro+b,s=sb,traningsniva=2,arbetsinsats=2,poang='1/0/0')])
 if q['id']=='2.427':q['ledtrad']=p('En vågrät tangent har lutningen 0. Vilken ekvation får du om derivatan ska vara noll?')
 if q['id']=='2.771':
  q.update(t=p('Funktionen är '+m('f(x)=4e^{0{,}5x}+7')+'. Vilket samband gäller för derivatan? (Välj ett alternativ.)'),s=sol([p('Konstanten 7 försvinner vid derivering.')+eq(r"f'(x)=2e^{0{,}5x}"),p('Den exponentiella delen av f är f(x)−7. Därför är derivatan halva denna del.')],m(r"f'(x)=0{,}5(f(x)-7)")+'.'),ledtrad=p('Jämför derivatan med den del av f som innehåller e.'),svarstyp='alternativ',svarFormat='text',rättSvar=None,tolerans=None,formaga=['begrepp','resonemang'],alternativ=[dict(txt=m(v),ratt=i==2) for i,v in enumerate([r"f'(x)=0{,}5f(x)",r"f'(x)=0{,}5f(x)+7",r"f'(x)=0{,}5(f(x)-7)",r"f'(x)=f(x)-7"])])

if __name__=='__main__':
 path=h.ROOT/'uppgiftermato1.js';raw=path.read_text();bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);assert not {q['id'] for q in bank}&{q['id'] for q in TASKS}
 for q in bank:
  before=json.dumps(q);revise(q)
  if before==json.dumps(q):continue
  pos=raw.index('"id": "'+q['id']+'"');beg=raw.rfind('{',0,pos);_,n=json.JSONDecoder().raw_decode(raw[beg:]);raw=raw[:beg]+json.dumps(q,ensure_ascii=False,indent=2)+raw[beg+n:];print('Ändrad',q['id'])
 end=raw.rindex(']');path.write_text(raw[:end].rstrip()+','+json.dumps(TASKS,ensure_ascii=False,indent=2)[1:-1]+'\n'+raw[end:])
