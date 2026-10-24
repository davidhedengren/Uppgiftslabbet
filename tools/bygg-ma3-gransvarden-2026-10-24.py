"""Handskrivna gränsvärden; rättar fem felaktiga facit och kalibrerar tio äldre frågor."""
import importlib.util,json,math
from pathlib import Path
spec=importlib.util.spec_from_file_location('helpers',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
p,m,eq,graph,table,text,svg=h.p,h.m,h.eq,h.graph,h.table,h.text,h.svg
TASKS=[]
def add(n,level,*args,**kw):TASKS.append(h.make('1.'+str(n),'gransvarde','Gränsvärden när x växer obegränsat och i modeller' if n in [942,943,947] else 'Gränsvärden med parameter' if n==948 else 'Beräkna gränsvärden',level,*args,**kw))
add(941,1,p('Figuren visar funktionen f. Bestäm gränsvärdet när x närmar sig 1 från vänster: '+m(r'\lim_{x\to1^-}f(x)')+'.'),2,[p('Från vänster följer vi den nedre delen av grafen. Där närmar sig funktionsvärdet 2. Den fyllda punkten på höjden 4 anger f(1), inte vänstergränsvärdet.')],'2.','Vilken del av grafen hör till x-värden mindre än 1?',fig=graph('Funktionen går mot 2 från vänster vid x=1, men har värdet 4 där.',(0,3),(0,5),[[(0,1),(1,2)],[(1,4),(3,4)]],[0,1,2,3],[0,1,2,3,4,5],dots=[(1,2,False),(1,4,True)]))
points=[(i/10,12*(1-math.exp(-0.4*i/10))) for i in range(101)]
fig=graph('Spänningen stiger från noll och närmar sig den streckade nivån 12 volt.',(0,10),(0,14),[points],[0,2,4,6,8,10],[0,4,8,12],xlabel='Tid t (s)',ylabel='Spänning U (V)')
fig=fig.replace('</svg>','<path d="M65 78.571H435" stroke="#b25c17" stroke-width="2" stroke-dasharray="7 5"/>'+text(330,28,'Gränsnivå',16)+'</svg>')
add(942,1,p('Spänningen närmar sig den streckade nivån när tiden ökar. Vilket värde har '+m(r'\lim_{t\to\infty}U(t)')+'? (Svara i V.)'),12,[p('Den streckade nivån ligger vid 12 V. Det är det värde spänningen närmar sig när tiden blir mycket stor.')],'12 V.','Läs av höjden på den streckade nivån.',fig=fig,unit='V')
add(943,2,p('Funktionen är '+m(r'f(x)=\dfrac{2x+1}{x+2}')+'. Tabellen visar avrundade värden. Bestäm '+m(r'\lim_{x\to\infty}f(x)')+' med hjälp av uttrycket.'),2,[p('Skriv om täljaren som 2(x+2)−3.')+eq(r'f(x)=2-\frac3{x+2}'),p('När x växer obegränsat går bråket mot 0. Funktionen närmar sig alltså 2.')],'2.','Jämför täljaren med två gånger nämnaren.',fig=table(['x','f(x), avrundat'],[['10','1,750'],['100','1,971'],['1000','1,997']]))
fig=graph('Graferna till f och g har hål vid (1,3) respektive (1,-2).',(0,2),(-4,5),[[(0,2),(2,4)],[(0,-1),(2,-3)]],[0,1,2],[-4,-2,0,2,3,4],dots=[(1,3,False),(1,-2,False)])
fig=fig.replace('</svg>',text(390,57,'f',20)+text(460,233,'g',20)+'</svg>')
add(944,2,p('Graferna visar funktionerna f och g nära x = 1. Bestäm')+eq(r'\lim_{x\to1}\bigl(2f(x)-g(x)\bigr)'),8,[p('Av graferna ser vi att f(x) närmar sig 3 och g(x) närmar sig −2. Kombinera gränsvärdena:')+eq(r'2\cdot3-(-2)=8')],'8.','Läs först av de två gränsvärdena var för sig.',fig=fig)
add(945,3,p('En rörelse beskrivs av '+m('s(t)=t^2+3t')+', där s mäts i meter och t i sekunder. Bestäm gränsvärdet')+eq(r'\lim_{h\to0}\frac{s(2+h)-s(2)}h')+p('(Svara i m/s.)'),7,[p('Först är s(2) = 10. Utveckla s(2+h) och ta bort s(2).')+eq(r's(2+h)=10+7h+h^2'),p('För h ≠ 0 kan kvoten förenklas:')+eq(r'\frac{7h+h^2}{h}=7+h'),p('När h går mot 0 går kvoten mot 7. Det är hastigheten vid t = 2 s.')],'7 m/s.','Utveckla s(2+h) innan du förenklar kvoten.',unit='m/s')
add(946,3,p('Bestäm gränsvärdet')+eq(r'\lim_{x\to0}\frac{\frac1{1+x}-1}{x}'),-1,[p('Skriv täljaren med gemensam nämnare.')+eq(r'\frac1{1+x}-1=\frac{-x}{1+x}'),p('Dividera med x och förkorta för x ≠ 0.')+eq(r'\frac{-x}{x(1+x)}=-\frac1{1+x}'),p('Det sista uttrycket närmar sig −1 när x går mot 0.')],'−1.','Förenkla täljaren innan du dividerar med x.')
body='<path d="M175 70V200H325V70" fill="#e5f1f7" stroke="#24435e" stroke-width="3"/><path d="M380 45H285V65" fill="none" stroke="#096c9a" stroke-width="5"/>'+text(390,30,'x liter vatten',16)+text(250,120,'Från början:')+text(250,150,'20 g salt')+text(250,180,'2 liter lösning')
add(947,2,p('En lösning innehåller 20 g salt i 2 liter vätska. Man tillsätter x liter rent vatten. Koncentrationen blir '+m(r'C(x)=\dfrac{20}{2+x}')+' g/liter. Vilket påstående stämmer när man tillsätter allt mer vatten? (Välj ett alternativ.)'),None,[p('Täljaren är alltid 20 medan nämnaren växer. Därför går koncentrationen mot 0. För varje ändlig vattenmängd är kvoten fortfarande positiv.')],'Koncentrationen närmar sig 0 men blir aldrig exakt 0.','Kan ett bråk med positiv täljare och ändlig positiv nämnare bli noll?',fig=svg('Saltlösning med 20 g salt i 2 liter vätska späds med x liter rent vatten.',body,230),options=[('Koncentrationen blir exakt 0 när x = 20.',False),('Koncentrationen närmar sig 10 g/liter.',False),('Koncentrationen blir negativ när x är tillräckligt stort.',False),('Koncentrationen närmar sig 0 men blir aldrig exakt 0.',True)])
add(948,4,p('Bestäm talet a så att')+eq(r'\lim_{x\to0}\frac{\sqrt{1+ax}-1}{x}=3'),6,[p('Multiplicera med rotuttryckets konjugat i både täljare och nämnare.')+eq(r'\frac{\sqrt{1+ax}-1}{x}=\frac{ax}{x(\sqrt{1+ax}+1)}'),p('För x ≠ 0 förenklas kvoten till:')+eq(r'\frac{a}{\sqrt{1+ax}+1}'),p('När x går mot 0 blir gränsvärdet a/2. Därför ska a/2 = 3, vilket ger a = 6.')],m('a=6')+'.','Hur kan konjugatregeln ta bort roten ur täljaren?',skills=['problemlösning','procedur'])
DIRECT={'1.103':(1,'x+1','1+1',2),'1.106':(2,'x+2','2+2',4),'1.109':(-3,'x-3','-3-3',-6),'1.112':(4,'x+4','4+4',8),'1.115':(0,'x+3','0+3',3)}
EASY=['1.431','1.432','1.435','1.436','1.437']
def revise():
 path=h.ROOT/'uppgiftermato1.js';raw=path.read_text()
 for id in [*DIRECT,*EASY]:
  pos=raw.index('"id": "'+id+'"');beg=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[beg:]);q.update(niva='E',poang='1/0/0' if id in DIRECT else '2/0/0',traningsniva=1 if id in DIRECT else 2,arbetsinsats=1 if id in DIRECT else 2,miniräknare=True,geogebra=False)
  if id in DIRECT:
   at,expr,calc,answer=DIRECT[id];q['s']=h.sol([p('Uttrycket är en kontinuerlig funktion. Därför kan vi sätta in x = '+str(at)+' direkt.')+eq(r'\lim_{x\to '+str(at)+'}('+expr+')='+calc+'='+str(answer))],str(answer)+'.')
  raw=raw[:beg]+json.dumps(q,ensure_ascii=False,indent=2)+raw[beg+n:]
 path.write_text(raw)
if __name__=='__main__':
 raw=(h.ROOT/'uppgiftermato1.js').read_text();bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);assert not {q['id'] for q in bank}&{q['id'] for q in TASKS};revise();h.install(TASKS)
