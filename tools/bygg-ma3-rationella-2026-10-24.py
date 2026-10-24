"""Tolv handskrivna uppgifter och tre avgränsade förtydliganden. Kör bara en gång."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
def p(s):return '<p>'+s+'</p>'
def m(s):return r'\('+s+r'\)'
def eq(s):return '<div class="facit-matte">'+r'\['+s+r'\]'+'</div>'
def sol(steps,answer):return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li>'+s+'</li>' for s in steps)+'</ol><p class="facit-svar"><strong>Svar: '+answer+'</strong></p></div>'
def label(x,y,s,size=18):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="#172e46">{html.escape(s)}</text>'
def svg(title,body,h=180):return '<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 '+str(h)+'" role="img" aria-label="'+html.escape(title)+'" style="width:100%;max-width:500px"><title>'+html.escape(title)+'</title><rect width="500" height="'+str(h)+'" fill="#fff" rx="10"/>'+body+'</svg></span>'
def table(headers,rows):return '<table style="border-collapse:collapse;width:100%;max-width:360px"><thead><tr>'+''.join('<th style="border:1px solid #8796a5;padding:7px">'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td style="border:1px solid #8796a5;padding:7px;text-align:center">'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table>'
def route(first,second):return svg('Två sträckor efter varandra; schematisk figur','<path d="M45 80H455" fill="none" stroke="#146a96" stroke-width="4"/>'+''.join(f'<circle cx="{x}" cy="80" r="5" fill="#172e46"/>'+label(x,115,v) for x,v in [(45,'Start'),(250,'Mellanpunkt'),(455,'Mål')])+label(145,50,first)+label(350,50,second)+label(250,155,'Schematisk figur',14))
TASKS=[]
def add(area,family,level,text,answer,steps,final,hint,fig='',options=None,unit=None):
 q=dict(id=f'1.{913+len(TASKS)}',kap=1,omr=area,kurs=['1b','1c'],niva='E' if level<=2 else 'C',poang='1/0/0' if level<=2 else '0/1/0',familj=family,formaga=['begrepp'] if options else ['procedur','problemlösning'] if level>=3 else ['procedur'],traningsniva=level,arbetsinsats=min(level,3),miniräknare=True,geogebra=False,spel=True,självrättning=True,t=text+fig,s=sol(steps,final),ledtrad=p(hint),rättSvar=answer,svarFormat='numeriskt' if isinstance(answer,(int,float)) else 'uttryck',svarstyp='numeriskt' if isinstance(answer,(int,float)) else 'uttryck',tolerans=1e-9 if isinstance(answer,(int,float)) else None)
 if isinstance(answer,list):q.update(svarstyp='flera_delar',svarsstruktur='mängd',svarFormat=['numeriskt']*len(answer),svarEtiketter=['x-värde']*len(answer),tolerans=[1e-9]*len(answer))
 if options:q.update(svarstyp='alternativ',svarFormat='text',alternativ=[{'txt':t,'ratt':ok} for t,ok in options])
 if unit:q['svarEnhet']=unit
 TASKS.append(q)
D='rationella_uttryck';F='Definitionsmängd för rationella uttryck';R='rakna_rationella';G='Rationella uttryck i tillämpningar och grafer'
add(D,F,1,p('Vilket av x-värdena i tabellen gör '+m(r'\dfrac4{x-3}')+' odefinierat?'),3,[p('Uttrycket saknar värde om nämnaren är noll.')+eq(r'x-3=0\Rightarrow x=3')],m('x=3')+'.','Kontrollera nämnaren för varje x-värde.',fig=table(['x-värde'],[['−3'],['0'],['3'],['6']]))
add(D,F,1,p('Funktionen är '+m(r'f(x)=\dfrac{x-6}{x+2}')+'. Bestäm '+m('f(6)')+'.'),0,[p('Sätt in 6 i både täljaren och nämnaren.')+eq(r'f(6)=\frac{6-6}{6+2}=\frac{0}{8}=0')+p('En nolla i täljaren är tillåten. Här är nämnaren 8, inte 0.')],'0.','Vad blir täljaren och nämnaren var för sig?',fig=svg('Talet 6 matas in i funktionen f','<path d="M100 85H195M305 85H400" stroke="#146a96" stroke-width="3"/><path d="M185 78L195 85L185 92M390 78L400 85L390 92" fill="none" stroke="#146a96" stroke-width="3"/><rect x="195" y="45" width="110" height="80" rx="12" fill="#e2f1f7" stroke="#24435e" stroke-width="2"/>'+label(65,92,'6',24)+label(250,93,'f',24)+label(440,92,'?',24)))
add(D,F,3,p('För vilka två x-värden är uttrycket '+m(r'\dfrac1{x+1}\div\dfrac{x-2}{3}')+' inte definierat? Ange värdena i var sitt fält.'),[-1,2],[p('Det första bråkets nämnare får inte vara noll:')+eq(r'x+1=0\Rightarrow x=-1'),p('Man får heller inte dividera med 0. Det andra bråket är 0 när:')+eq(r'\frac{x-2}{3}=0\Rightarrow x=2')],m('x=-1')+' och '+m('x=2')+'.','Kontrollera både nämnarna och det uttryck som du dividerar med.')
line='<path d="M45 80H455" stroke="#146a96" stroke-width="3"/>'
for n in range(-4,5):
 x=250+45*n;line+=f'<path d="M{x} 74V86" stroke="#24435e" stroke-width="2"/>'+label(x,115,str(n).replace('-','−'),16)
line+='<circle cx="160" cy="80" r="8" fill="#fff" stroke="#b34e28" stroke-width="3"/>'+label(465,65,'x')
add(D,F,2,p('Uttrycket '+m(r'\dfrac6{x-a}')+' är definierat för alla reella x utom värdet vid den öppna ringen. Bestäm '+m('a')+'.'),-2,[p('Ringen visar att x = −2 är det förbjudna värdet. Nämnaren måste då bli noll.')+eq(r'-2-a=0\Rightarrow a=-2')],m('a=-2')+'.','Vilket x-värde gör x − a till noll?',fig=svg('Tallinje med en öppen ring vid minus två',line,145))
add(D,F,2,p('Uttrycket '+m(r'\dfrac{x-2}{x^2+bx-6}')+' är inte definierat när '+m('x=3')+'. Bestäm '+m('b')+'.'),-1,[p('Nämnaren ska vara noll när x = 3.')+eq(r'3^2+3b-6=0')+eq(r'3+3b=0\Rightarrow b=-1')],m('b=-1')+'.','Sätt in det förbjudna x-värdet i nämnaren.')
add(D,F,2,p('Lea förenklar '+m(r'R(x)=\dfrac{x^2-16}{x-4}')+' till '+m('x+4')+' och drar slutsatsen att '+m('R(4)=8')+'. Vilken kommentar är korrekt? (Välj ett alternativ.)'),None,[p('Faktoriseringen ger:')+eq(r'R(x)=\frac{(x-4)(x+4)}{x-4}=x+4'),p('Förkortningen gäller bara när x ≠ 4. Originalets nämnare är fortfarande noll vid x = 4.')],'R(4) är inte definierat.','Kontrollera det ursprungliga uttrycket vid x = 4.',options=[('Lea har rätt: en förenkling gör även x = 4 tillåtet.',False),('R(4) = 0 eftersom täljaren är noll.',False),('R(4) = 4 eftersom faktorn x − 4 förkortas bort.',False),('R(4) är inte definierat; x + 4 gäller bara för x ≠ 4.',True)])
add(R,G,1,p('Sträckorna är '+m(r'\dfrac{x+1}{5}')+' km och '+m(r'\dfrac{2x-1}{5}')+' km, där '+m(r'x\gt1')+'. Skriv ett förenklat uttryck för hela sträckan. (Svara i km.)'),'3*x/5',[p('Addera sträckorna. Bråken har samma nämnare.')+eq(r'\frac{x+1}{5}+\frac{2x-1}{5}=\frac{3x}{5}')],m(r'\dfrac{3x}{5}')+' km.','Vad händer med +1 och −1 när du lägger ihop täljarna?',fig=route('(x + 1)/5 km','(2x − 1)/5 km'),unit='km')
bars='<rect x="90" y="45" width="240" height="38" fill="#2b789f"/><rect x="90" y="105" width="160" height="38" fill="#d78a38"/>'+label(55,71,'A')+label(55,131,'B')+label(405,71,'3x/4 liter')+label(335,131,'x/2 liter')
add(R,'Dividera rationella uttryck',1,p('Behållare A innehåller '+m(r'3x/4')+' liter och behållare B innehåller '+m(r'x/2')+' liter, där '+m(r'x\gt0')+'. Hur många gånger så mycket vätska finns i A som i B? (Svara exakt.)'),1.5,[p('Dela volymen i A med volymen i B.')+eq(r'\frac{3x}{4}\div\frac{x}{2}=\frac{3x}{4}\cdot\frac2x=\frac32')],'1,5 gånger så mycket.','Jämför volymerna genom att dividera A:s volym med B:s.',fig=svg('Volym i behållare A och B, visad med proportionella staplar',bars))
add(R,G,4,p('En cyklist färdas 6 km med farten '+m('x')+' km/h och sedan ytterligare 6 km med farten '+m('2x')+' km/h, där '+m(r'x\gt0')+'. Inga pauser görs. Skriv ett förenklat uttryck för medelfarten under hela färden. (Svara i km/h.)'),'4*x/3',[p('Tiden är sträcka delad med fart. Tiderna blir 6/x och 6/(2x) timmar.')+eq(r't=\frac6x+\frac6{2x}=\frac9x'),p('Dela hela sträckan, 12 km, med hela tiden.')+eq(r'v_{\text{medel}}=12\div\frac9x=\frac{4x}{3}')+p('Det är inte medelvärdet av farterna: cyklisten tillbringar mer tid på den långsamma sträckan.')],m(r'\dfrac{4x}{3}')+' km/h.','Bestäm först tiden på varje sträcka.',fig=route('6 km, fart x km/h','6 km, fart 2x km/h'),unit='km/h')
add(R,G,3,p('Det kostar 400 kr att starta en tryckning och sedan 8 kr per affisch. Styckkostnaden är kostnaden per affisch. Hur mycket lägre blir styckkostnaden om man beställer '+m('2n')+' affischer i stället för '+m('n')+'? Antalet '+m('n')+' är ett positivt heltal. (Svara med ett uttryck i kr.)'),'200/n',[p('Dela kostnaden med antalet affischer i båda fallen.')+eq(r'K(n)=\frac{400+8n}{n}=\frac{400}{n}+8')+eq(r'K(2n)=\frac{400+16n}{2n}=\frac{200}{n}+8'),p('Skillnaden är:')+eq(r'K(n)-K(2n)=\frac{200}{n}')],m(r'\dfrac{200}{n}')+' kr lägre.','Den fasta kostnaden fördelas på olika många affischer.',fig=table(['Kostnad','Belopp'],[['Startavgift','400 kr'],['Varje affisch','8 kr']]),unit='kr')
add(R,'Dividera rationella uttryck',2,p('Förenkla uttrycket '+m(r'\dfrac{1/x}{1/x+1/6}')+', där '+m(r'x\gt0')+'.'),'6/(x+6)',[p('Multiplicera både den stora täljaren och den stora nämnaren med 6x.')+eq(r'\frac{1/x}{1/x+1/6}=\frac{6}{6+x}')],m(r'\dfrac6{x+6}')+'.','Vilken faktor tar bort båda de små nämnarna?')
add(R,'Räkna med rationella uttryck',3,p('Bestäm talet '+m('a')+' så att sambandet gäller för alla '+m(r'x\ne2')+':')+eq(r'\frac{x+1}{x-2}+\frac{x-5}{2-x}=\frac{a}{x-2}'),6,[p('Nämnarna är varandras motsatser: 2 − x = −(x − 2).')+eq(r'\frac{x+1}{x-2}-\frac{x-5}{x-2}')+eq(r'=\frac{x+1-(x-5)}{x-2}=\frac6{x-2}')],m('a=6')+'.','Skriv båda bråken med nämnaren x − 2. Var noga med minustecknet.')

def revise(q):
 if q['id'] in ['1.73','1.78']:
  car=q['id']=='1.73';total=240 if car else 600;given=4 if car else 5;answer=60 if car else 120;unit='km/h' if car else 'MB/s';time='timmar' if car else 'sekunder'
  intro=p(('En bil kör 240 km med konstant fart. Restiden T mäts i timmar och farten v i km/h.' if car else 'En fil på 600 MB överförs med konstant hastighet. Tiden T mäts i sekunder och överföringshastigheten v i MB/s.')+' Modellen är '+m(r'T(v)=\frac{'+str(total)+r'}{v}')+'.')
  questions=[p('Förklara varför '+m('v=0')+' inte är tillåtet i modellen.'),p('Bestäm '+m('v')+' om tiden är '+str(given)+' '+time+'. (Svara i '+unit+'.)'),p('Vad händer med tiden '+m('T(v)')+' i modellen när '+m('v')+' blir mycket stor?')]
  solutions=[sol([p('Vid v = 0 blir nämnaren noll, och division med noll är inte definierad.'),p('Utan fart blir resan aldrig färdig.' if car else 'Utan överföringshastighet blir filen aldrig överförd.')],'v = 0 är inte tillåtet.'),sol([p('Sätt in den givna tiden och lös ekvationen.')+eq(r'\frac{'+str(total)+r'}v='+str(given))+eq(str(total)+'='+str(given)+'v'+r'\Rightarrow v='+str(answer))],str(answer)+' '+unit+'.'),sol([p('Ett fast positivt tal delas med ett allt större positivt tal. Kvoten blir därför mindre och närmar sig 0.')],'Tiden närmar sig 0, men blir inte 0.')]
  q['t']=intro+''.join('<div class="deluppgift"><b>'+chr(97+i)+')</b> '+t+'</div>' for i,t in enumerate(questions))
  q['s']=''.join('<section><h4>'+chr(97+i)+')</h4>'+s+'</section>' for i,s in enumerate(solutions))
  q['traningsniva']=3
  for i,d in enumerate(q['spelDelar']):d.update(t=intro+questions[i],s=solutions[i],traningsniva=[2,1,3][i],miniräknare=True,geogebra=False)
 if q['id']=='1.854':
  q['t']=q['t'].replace('Hur många bitar blir det?', 'Delningen går jämnt upp, utan någon rest. Hur många bitar blir det?')
  q['s']=sol([p('Dela hela repets längd med längden på en bit.')+eq(r'\frac{x^2-1}{6}\div\frac{x+1}{3}'),p('Faktorisera x² − 1 och multiplicera med det andra bråkets invers.')+eq(r'\frac{(x-1)(x+1)}6\cdot\frac3{x+1}=\frac{x-1}2'),p('Eftersom delningen går jämnt upp anger uttrycket ett helt antal bitar.')],m(r'\dfrac{x-1}2')+' bitar.')
  q['miniräknare']=True
 return q

def install():
 pth=ROOT/'uppgiftermato1.js';raw=pth.read_text();start=raw.index('[');end=raw.rindex(']');bank=json.loads(raw[start:end+1]);assert not {q['id'] for q in bank}&{q['id'] for q in TASKS}
 for id in ['1.73','1.78','1.854']:
  marker='"id": "'+id+'"';pos=raw.index(marker);beg=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[beg:]);q=revise(q);raw=raw[:beg]+json.dumps(q,ensure_ascii=False,indent=2)+raw[beg+n:]
 end=raw.rindex(']');raw=raw[:end].rstrip()+','+json.dumps(TASKS,ensure_ascii=False,indent=2)[1:-1]+'\n'+raw[end:];pth.write_text(raw)
 print('Tillagda:',[q['id'] for q in TASKS])
if __name__=='__main__':install()
