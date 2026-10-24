"""Redaktionella ändringar och sex handskrivna trigonometrivariationer."""
import json,importlib.util,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p,m,eq,sol,svg,text=h.p,h.m,h.eq,h.sol,h.svg,h.text
def patch(course,fn):
 path=ROOT/('uppgifter'+course+'.js');raw=path.read_text();bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);changed=[]
 for q in bank:
  before=json.dumps(q,ensure_ascii=False);fn(q)
  if before==json.dumps(q,ensure_ascii=False):continue
  pos=raw.index('"id": "'+q['id']+'"');beg=raw.rfind('{',0,pos);_,n=json.JSONDecoder().raw_decode(raw[beg:]);raw=raw[:beg]+json.dumps(q,ensure_ascii=False,indent=2)+raw[beg+n:];changed.append(q['id'])
 path.write_text(raw);print(course,'Ändrade',changed)
def ma1(q):
 if q['id'] in ['0.607','0.608','0.609','0.610','0.611','0.612']:
  q['t']=q['t'].replace('i vanlig decimalform','som ett vanligt tal utan potenser')
 if q['id']=='0.906':
  q['t']=p('Vilket av talen nedan avrundas till 6,0 när du avrundar till en decimal? (Välj ett alternativ.)')
  q.update(svarstyp='alternativ',svarFormat='text',rättSvar=None,alternativ=[dict(txt=v,ratt=v=='5,96') for v in ['5,94','5,96','6,05','6,1']])
  q['s']=sol([p('5,96 ligger närmare 6,0 än 5,9 och avrundas därför till 6,0.'),p('5,94 avrundas till 5,9. Både 6,05 och 6,1 avrundas till 6,1.')],'5,96.')
 if q['id']=='0.629':
  blister='<rect x="110" y="45" width="280" height="140" rx="12" fill="#e4eff4" stroke="#264663" stroke-width="2"/>'
  blister+=''.join(f'<ellipse cx="{150+50*i}" cy="{75+40*j}" rx="14" ry="10" fill="white" stroke="#264663" stroke-width="2"/>' for j in range(3) for i in range(5))
  blister+=text(250,220,'En karta innehåller 15 tabletter.',19)
  q['t']=p('En tillverkare har 4,8 g av ett ämne till tabletter. Varje tablett ska innehålla 120 mg av ämnet. En tablettkarta ska innehålla 15 tabletter.')+svg('En tablettkarta med fem kolumner och tre rader, totalt femton tabletter.',blister,245)+p('Hur många hela tablettkartor räcker ämnet till?')
  q['arbetsinsats']=2
 if q['id']=='3.34':
  intro=p('Ett träd bär 40 frukter ett år och 46 nästa år. I en modell fortsätter antalet att öka med samma procent varje år.')
  a='Med hur många procent ökade antalet frukter från 40 till 46?'
  b='Hur många frukter ger modellen fem år efter det år då trädet bar 46 frukter? Avrunda till närmaste heltal.'
  sa=sol([p('Antalet ökade med 46−40 = 6 frukter. Jämför ökningen med de ursprungliga 40 frukterna.')+eq(r'\frac6{40}\cdot100=15')],'15 %.')
  sb=sol([p('Förändringsfaktorn per år är 46/40 = 1,15. Börja med 46 frukter och använd faktorn fem gånger.')+eq(r'46\cdot1{,}15^5\approx92{,}52'),p('Avrundning till närmaste heltal ger 93 frukter.')],'93 frukter.')
  q['t']=intro+p('a) '+a)+p('b) '+b);q['s']='<div class="facit-v2">'+p('<strong>a)</strong>')+sa+p('<strong>b)</strong>')+sb+'</div>'
  q.update(svarEnhet=['%',''],svarFormat=['numeriskt','heltal'])
  q['spelDelar'][0].update(t=p('Ett träd bär 40 frukter ett år och 46 nästa år.')+p(a),s=sa,traningsniva=2,arbetsinsats=1,miniräknare=True,geogebra=False,ledtrad=p('Jämför ökningen med antalet frukter från början.'))
  q['spelDelar'][1].update(t=intro+p(b),s=sb,miniräknare=True,geogebra=False)
 if q['id']=='3.80':
  q.update(traningsniva=5,niva='A',poang='0/0/2',arbetsinsats=3)
  q['s']=sol([p('Efter första årets ränta och den extra insättningen finns:')+eq(r'20000\cdot1{,}02+5000=25400'),p('Ta först bort tredje årets ränta ur slutbeloppet:')+eq(r'\frac{27208{,}48}{1{,}04}=26162'),p('Jämför med beloppet före andra året. Förändringsfaktorn är 26162/25400 = 1,03, alltså en ökning med 3 %.')],'3,0 %.')
 if q['id']=='3.32':
  q['t']=q['t'].replace('En vara höjs först','Priset på en vara höjs först').replace('Visa att slutpriset alltid blir lägre än ursprungspriset, oavsett vilket positivt värde \\(p\\) har.', 'Visa att slutpriset blir lägre än ursprungspriset när '+m('0&lt;p&lt;100')+'.')

def circle(show_height=False):
 cx,cy,r=250,170,115;theta=math.asin(.6) if show_height else math.radians(35)
 px,py=cx+r*math.cos(theta),cy-r*math.sin(theta);qx,qy=2*cx-px,2*cy-py
 body=f'<circle cx="250" cy="170" r="115" fill="#f0f7fb" stroke="#25465f" stroke-width="2"/><path d="M95 170H410 M250 310V30" fill="none" stroke="#25465f" stroke-width="2"/>'
 body+=f'<path d="M{px:.2f} {py:.2f}L{qx:.2f} {qy:.2f}" stroke="#087b9b" stroke-width="3"/>'
 body+=f'<circle cx="{px:.2f}" cy="{py:.2f}" r="5" fill="#087b9b"/><circle cx="{qx:.2f}" cy="{qy:.2f}" r="5" fill="#087b9b"/>'
 body+=text(px+18,py-13,'P')+text(qx-20,qy+24,'Q')+text(427,177,'x')+text(252,22,'y')+text(263,192,'O',16)
 ex,ey=cx+40*math.cos(theta),cy-40*math.sin(theta)
 body+=f'<path d="M290 170 A40 40 0 0 0 {ex:.2f} {ey:.2f}" fill="none" stroke="#b35316" stroke-width="2"/>'+text(306,157,'v',18)
 if show_height:
  body+=f'<path d="M{px:.2f} {py:.2f}V170" stroke="#5c6e7e" stroke-width="2" stroke-dasharray="5 4"/>'+text(px+35,140,'3/5',18)
 body+=text(250,340,'P och Q ligger på samma diameter.',17)
 return svg('Enhetscirkel med punkten P i första kvadranten och Q diametralt motsatt. Vinkeln v hör till P.',body,360)

def mato2(q):
 if q['id']=='1.61':
  old=r'\sin^2x=1-25/169=144/169';new=r'\sin^2x=1-\frac{25}{169}=\frac{144}{169}'
  q['s']=q['s'].replace(old,new)
  q['spelDelar'][1]['s']=q['spelDelar'][1]['s'].replace(old,new)
 if q['id']=='1.676':
  q['s']=sol([p('Kvadrera båda leden.')+eq(r'(\sin x+\cos x)^2=1{,}44'),p('Kvadreringsregeln ger kvadraterna '+m(r'\sin^2x+\cos^2x')+' och dubbelprodukten '+m(r'2\sin x\cos x')+'. Kvadraternas summa är 1, enligt trigonometriska ettan.')+eq(r'1+2\sin x\cos x=1{,}44'),p('Subtrahera 1 och dela sedan med 2.')+eq(r'\sin x\cos x=\frac{0{,}44}{2}=0{,}22')],'0,22.')

TASKS=[]
def add(id,level,area,t,answer,steps,final,hint,fig='',numeric=False):
 q=h.make(id,area,'Symmetrier och periodicitet i enhetscirkeln' if area=='enhetscirkeln_formler' else 'Trigonometriska ettan och identiteter',level,t,answer,steps,final,hint,fig=fig)
 q.update(kurs=['2c'],miniräknare=False,svarFormat='numeriskt' if numeric else 'uttryck',svarstyp='numeriskt' if numeric else 'uttryck',tolerans=1e-10 if numeric else None)
 TASKS.append(q)
add('1.693',2,'enhetscirkeln_formler',p('P och Q ligger mitt emot varandra på enhetscirkeln. Punkten P hör till vinkeln v. Förenkla '+m(r'\sin(v+180^\circ)')+'.'),'-sin(v)',[p('Ett halvt varv flyttar P till Q. Då byter båda koordinaterna tecken. Sinus är y-koordinaten.')],m(r'-\sin v')+'.','Hur förändras punktens höjd när den flyttas till motsatt sida?',circle())
add('1.694',3,'enhetscirkeln_formler',p('Förenkla så långt som möjligt:')+eq(r'\sin(180^\circ+x)+\cos(90^\circ+x)'),'-2*sin(x)',[p('Använd symmetrierna för de två vinklarna.')+eq(r'\sin(180^\circ+x)=-\sin x')+eq(r'\cos(90^\circ+x)=-\sin x'),p('De två termerna är lika och kan läggas ihop.')],m(r'-2\sin x')+'.','Skriv båda termerna med samma trigonometriska funktion.')
add('1.695',2,'trig_identiteter',p('Förenkla uttrycket där det är definierat:')+eq(r'\frac{\cos x}{1-\sin^2x}'),'1/cos(x)',[p('Trigonometriska ettan ger 1−sin²x = cos²x.')+eq(r'\frac{\cos x}{\cos^2x}=\frac1{\cos x}'),p('Villkoret cos x ≠ 0 gäller både före och efter förenklingen.')],m(r'\dfrac1{\cos x}')+'.','Vilken term kan ersätta nämnaren?')
add('1.696',3,'trig_identiteter',p('Förenkla uttrycket där det är definierat:')+eq(r'\frac{1-\cos^2x}{\sin x}\div\frac{\cos x}{1-\sin^2x}'),'sin(x)*cos(x)',[p('Trigonometriska ettan gör den första kvoten till sin x och den andra till 1/cos x.'),p('Att dividera med 1/cos x är att multiplicera med cos x.')+eq(r'\sin x\div\frac1{\cos x}=\sin x\cos x'),p('Originaluttrycket kräver både sin x ≠ 0 och cos x ≠ 0.')],m(r'\sin x\cos x')+'.','Förenkla de två kvoterna innan du dividerar.')
add('1.697',4,'trig_identiteter',p('Förenkla uttrycket där det är definierat:')+eq(r'\left(\frac1{1-\sin x}-\frac1{1+\sin x}\right)\cos^2x'),'2*sin(x)',[p('Skriv skillnaden på gemensam nämnare.')+eq(r'\frac{(1+\sin x)-(1-\sin x)}{1-\sin^2x}')+eq(r'=\frac{2\sin x}{\cos^2x}'),p('Multiplikationen med cos²x tar bort nämnaren. Originaluttrycket kräver cos x ≠ 0.')],m(r'2\sin x')+'.','Var noga med minustecknet framför den andra täljaren.')
add('1.698',3,'trig_identiteter',p('För vinkeln v gäller '+m(r'\sin v=3/5')+' och '+m(r'0&lt;v&lt;90^\circ')+'. Bestäm exakt')+eq(r'\frac1{\cos(180^\circ+v)}'),'-5/4',[p('Trigonometriska ettan ger cos²v = 1−9/25 = 16/25. Första kvadranten ger cos v = 4/5.'),p('Ett halvt varv byter tecken på cosinus:')+eq(r'\cos(180^\circ+v)=-\frac45'),p('Vänd på bråket för att få det efterfrågade värdet.')+eq(r'1\div\left(-\frac45\right)=-\frac54')],m(r'-\dfrac54')+'.','Bestäm först cos v, sedan värdet efter ett halvt varv.',circle(True))

if __name__=='__main__':
 patch('ma1',ma1)
 patch('mato2',mato2)
 path=ROOT/'uppgiftermato2.js';s=path.read_text();bank=json.loads(s[s.index('['):s.rindex(']')+1]);assert not {q['id'] for q in bank}&{q['id'] for q in TASKS}
 end=s.rindex(']');path.write_text(s[:end].rstrip()+','+json.dumps(TASKS,ensure_ascii=False,indent=2)[1:-1]+'\n'+s[end:]);print('Nya', [q['id'] for q in TASKS])
