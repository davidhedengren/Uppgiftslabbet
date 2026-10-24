"""Handgranskad grafik och variation; ändrar inte appens deluppgiftshantering."""
import json, math, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    p=ROOT/name; src=p.read_text(); start=src.index('[')
    data,_=json.JSONDecoder().raw_decode(src[start:]); return p,src,data
def save(p,src,data,ids):
    for q in data:
        if q['id'] not in ids: continue
        m=re.search(r'\n([ \t]*)\{\n[ \t]*"id": "'+re.escape(q['id'])+'"',src)
        assert m,q['id']
        a=m.start()+1; close='\n'+m[1]+'}'; z=src.index(close,a)+len(close)
        old=json.loads(src[a:z]); assert old['id']==q['id']
        replacement=json.dumps(q,ensure_ascii=False,indent=2)
        replacement=m[1]+replacement.replace('\n','\n'+m[1])
        src=src[:a]+replacement+src[z:]
    p.write_text(src)
def text(x,y,s,color='#243f52',anchor='middle',size=16):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{s}</text>'
def wrap(title,body,w=500,h=310):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title><rect width="{w}" height="{h}" fill="#fff"/>{body}</svg>'
def graph(title,functions,xrange,yrange,regions,ticks,labels):
    xmin,xmax=xrange; ymin,ymax=yrange
    X=lambda x:55+(x-xmin)/(xmax-xmin)*405
    Y=lambda y:255-(y-ymin)/(ymax-ymin)*205
    def coords(f,a,b):return [(X(a+(b-a)*i/120),Y(f(a+(b-a)*i/120))) for i in range(121)]
    def path(points):return 'M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in points)
    body=''
    for f,g,a,b in regions:body+=f'<path d="{path(coords(f,a,b)+coords(g,b,a))} Z" fill="#dcecf1"/>'
    for axis,val,label in ticks:
        if axis=='x': body+=f'<line x1="{X(val)}" y1="{Y(0)-4}" x2="{X(val)}" y2="{Y(0)+4}" stroke="#536979"/>'+text(round(X(val),2),round(Y(0)+24,2),label)
        else: body+=f'<line x1="{X(0)-4}" y1="{Y(val)}" x2="{X(0)+4}" y2="{Y(val)}" stroke="#536979"/>'+text(round(X(0)-12,2),round(Y(val)+5,2),label,anchor='end')
    body+=f'<line x1="45" y1="{Y(0)}" x2="472" y2="{Y(0)}" stroke="#243f52" stroke-width="1.6"/><line x1="{X(0)}" y1="35" x2="{X(0)}" y2="268" stroke="#243f52" stroke-width="1.6"/>'
    body+=text(482,round(Y(0)+5,2),'x')+text(round(X(0)+13,2),31,'y')
    for f,a,b,color in functions:body+=f'<path d="{path(coords(f,a,b))}" fill="none" stroke="{color}" stroke-width="2.5"/>'
    for x,y,label,color in labels:body+=text(x,y,label,color,anchor='start')
    return '<span class="fig">'+wrap(title,body)+'</span>'
BLUE='#176d8d';RED='#b53b26'
solution=lambda body,answer:'<div class="facit-v2 facit-stegvis">'+body+'<p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def set_single(q,t,s,answer,hint,fmt='uttryck'):
    q.update(t=t,s=s,rättSvar=answer,ledtrad=hint,svarFormat=fmt,svarstyp='numeriskt' if fmt=='numeriskt' else 'uttryck',tolerans=None,självrättning=True)

p,src,bank=load('uppgiftermato2.js'); Q={q['id']:q for q in bank}
q=Q['3.91']
fig=graph('Sinus och cosinus. Området mellan y-axeln och första skärningen vid x = π/4 är skuggat.',[(math.cos,0,math.pi/2,BLUE),(math.sin,0,math.pi/2,RED)],(0,math.pi/2),(0,1.15),[(math.cos,math.sin,0,math.pi/4)],[('x',0,'0'),('x',math.pi/4,'π/4'),('x',math.pi/2,'π/2'),('y',1,'1')],[(340,78,'y = sin x',RED),(345,222,'y = cos x',BLUE)])
q['t']=re.sub(r'<span class="fig"><svg[\s\S]*?</svg></span>',lambda _:fig,q['t'])
# Reflow long formulas while preserving this manually assessed exact-area exercise.
q['s']=solution(r'<p>Den första skärningen i första kvadranten uppfyller \(\sin x=\cos x\), alltså \(x=\pi/4\).</p><p>Cosinus ligger över sinus mellan y-axeln och skärningen. Därför är arean</p>\[A=\int_0^{\pi/4}(\cos x-\sin x)\,dx.\]<p>En primitiv funktion till integranden är \(\sin x+\cos x\). Insättning av gränserna ger</p>\[A=\frac{\sqrt2}{2}+\frac{\sqrt2}{2}-(0+1)=\sqrt2-1.\]',r'\(\sqrt2-1\) areaenheter.')
# Keep the basic parabola/line task; remove the unrelated asymptote hint.
Q['3.18']['ledtrad']=r'<p>Bestäm först skärningarnas x-koordinater. Integrera sedan den övre funktionen minus den undre mellan skärningarna.</p>'
Q['3.18']['s']=solution(r'<p>Skärningarna uppfyller \(x^2=2x\), alltså \(x(x-2)=0\). Gränserna är därför \(x=0\) och \(x=2\).</p><p>Linjen ligger över parabeln mellan skärningarna.</p>\[A=\int_0^2(2x-x^2)\,dx\]\[A=\left[x^2-\frac{x^3}{3}\right]_0^2=4-\frac83=\frac43.\]',r'\(4/3\) areaenheter.')
# A signed integral versus geometric area, using a sine curve.
fig=graph('Sinuskurvan från 0 till 2π, med båda områdena mot x-axeln skuggade.',[(math.sin,0,2*math.pi,BLUE)],(0,2*math.pi),(-1.2,1.2),[(math.sin,lambda x:0,0,math.pi),(lambda x:0,math.sin,math.pi,2*math.pi)],[('x',0,'0'),('x',math.pi,'π'),('x',2*math.pi,'2π'),('y',1,'1'),('y',-1,'−1')],[(185,48,'y = sin x',BLUE)])
set_single(Q['3.57'],r'<p>Figuren visar \(y=\sin x\) för \(0\le x\le2\pi\). Bestäm den sammanlagda arean av de två skuggade områdena mellan grafen och x-axeln. Svara exakt.</p>'+fig,solution(r'<p>Sinus är positiv på \(0\le x\le\pi\) och negativ på \(\pi\le x\le2\pi\). De två områdena är lika stora, men deras tecknade integraler har motsatta tecken.</p><p>Den geometriska arean blir därför</p>\[A=2\int_0^\pi\sin x\,dx\]\[A=2[-\cos x]_0^\pi=2(1-(-1))=4.\]<p>Integralen över hela intervallet är noll, men arean är positiv.</p>',r'\(4\) areaenheter.'),4,r'<p>Dela vid x = π. Area under x-axeln ska också räknas positivt.</p>','numeriskt')
Q['3.57']['miniräknare']=False;Q['3.57']['geogebra']=False
# Scaffolded absolute-value task: same a/b/c structure, genuinely different geometry.
fig=graph('Linjen y = 1 och v-formade grafen y = |x − 1| innesluter en triangel.',[(lambda x:1,0,2,BLUE),(lambda x:abs(x-1),0,2,RED)],(0,2),(0,1.3),[(lambda x:1,lambda x:abs(x-1),0,2)],[('x',0,'0'),('x',1,'1'),('x',2,'2'),('y',1,'1')],[(190,73,'y = 1',BLUE),(285,233,'y = |x − 1|',RED)])
intro=r'<p>Graferna \(y=1\) och \(y=|x-1|\) innesluter det skuggade området.</p>'+fig
parts=[r'Bestäm skärningspunkternas x-koordinater.',r'Ställ upp en integral eller en summa av integraler för arean.',r'Beräkna arean exakt.']
solutions=[solution(r'<p>I skärningspunkterna gäller \(|x-1|=1\). Det ger \(x-1=-1\) eller \(x-1=1\).</p>',r'\(x=0\) och \(x=2\).'),solution(r'<p>Linjen ligger över v-grafen. För \(x\le1\) är \(|x-1|=1-x\), och för \(x\ge1\) är \(|x-1|=x-1\).</p>',r'\[A=\int_0^1x\,dx+\int_1^2(2-x)\,dx.\]'),solution(r'<p>Dela vid spetsen, där uttrycket för den undre grafen byts.</p>\[A=\int_0^1x\,dx+\int_1^2(2-x)\,dx\]\[A=\frac12+\frac12=1.\]<p>Kontroll: triangeln har basen 2 och höjden 1, så arean är \(2\cdot1/2=1\).</p>',r'\(1\) areaenhet.')]
hints=[r'<p>När är avståndet mellan x och 1 lika med 1?</p>',r'<p>V-grafen består av två räta linjer. Dela intervallet vid spetsen.</p>',r'<p>Beräkna de två integralerna var för sig eller använd triangelns area.</p>']
q=Q['3.63'];q.update(t=intro+'<ol type="a">'+''.join('<li>'+x+'</li>' for x in parts)+'</ol>',spelIntro=intro,s=''.join('<section><p><strong>'+chr(97+i)+')</strong></p>'+s+'</section>' for i,s in enumerate(solutions)),rättSvar=[[0,2],None,1],ledtrad=hints[1],svarFormat=[['numeriskt','numeriskt'],None,'numeriskt'])
for i,d in enumerate(q['spelDelar']):d.update(fraga='<p>'+parts[i]+'</p>',t=intro+'<p>'+parts[i]+'</p>',s=solutions[i],ledtrad=hints[i])
q['spelDelar'][0]['traningsniva']=2
# Reverse problem rather than another identical request for area.
fig=graph('Parabeln y = x² och en vågrät linje y = a mellan x = −1 och x = 1.',[(lambda x:x*x,-1.25,1.25,RED),(lambda x:2,-1.25,1.25,BLUE)],(-1.25,1.25),(0,2.5),[(lambda x:2,lambda x:x*x,-1,1)],[('x',-1,'−1'),('x',0,'0'),('x',1,'1')],[(340,76,'y = a',BLUE),(345,222,'y = x²',RED)])
set_single(Q['3.177'],r'<p>En vågrät linje \(y=a\), där \(a&gt;1\), ligger över parabeln \(y=x^2\) för \(-1\le x\le1\). Det skuggade området har arean \(10/3\). Bestäm \(a\).</p>'+fig,solution(r'<p>Höjden mellan graferna är \(a-x^2\). Den givna arean ger ekvationen</p>\[\int_{-1}^{1}(a-x^2)\,dx=\frac{10}{3}.\]<p>Integralen av konstanten a över ett intervall med längden 2 är 2a.</p>\[2a-\frac23=\frac{10}{3}\]\[2a=4\quad\Rightarrow\quad a=2.\]',r'\(a=2\).'),2,r'<p>Uttryck arean med a och sätt den lika med den givna arean.</p>','numeriskt')
Q['3.177']['traningsniva']=3
# Variation in the other area card too: exponentials and two curved boundaries.
fig=graph('Området mellan y = eˣ och y = 1 från x = 0 till x = ln 2.',[(math.exp,0,math.log(2),BLUE),(lambda x:1,0,math.log(2),RED)],(0,math.log(2)),(0,2.5),[(math.exp,lambda x:1,0,math.log(2))],[('x',0,'0'),('x',math.log(2),'ln 2'),('y',1,'1'),('y',2,'2')],[(310,65,'y = eˣ',BLUE),(320,195,'y = 1',RED)])
set_single(Q['3.157'],r'<p>Bestäm arean mellan \(y=e^x\) och \(y=1\) för \(0\le x\le\ln2\). Svara exakt.</p>'+fig,solution(r'<p>Exponentialfunktionen ligger över linjen på intervallet.</p>\[A=\int_0^{\ln2}(e^x-1)\,dx\]\[A=[e^x-x]_0^{\ln2}\]\[A=(2-\ln2)-(1-0)=1-\ln2.\]',r'\(1-\ln2\) areaenheter.'),'1-ln(2)',r'<p>Integrera eˣ − 1. Använd att e upphöjt till ln 2 är 2.</p>')
fig=graph('Två parabler y = 4 − x² och y = x² + 2 med skuggat område mellan skärningarna.',[(lambda x:4-x*x,-1.35,1.35,BLUE),(lambda x:x*x+2,-1.35,1.35,RED)],(-1.35,1.35),(0,4.6),[(lambda x:4-x*x,lambda x:x*x+2,-1,1)],[('x',-1,'−1'),('x',0,'0'),('x',1,'1'),('y',2,'2'),('y',4,'4')],[(310,51,'y = 4 − x²',BLUE),(280,189,'y = x² + 2',RED)])
set_single(Q['3.417'],r'<p>Bestäm arean som innesluts av \(y=4-x^2\) och \(y=x^2+2\). Svara exakt.</p>'+fig,solution(r'<p>Skärningarna fås ur \(4-x^2=x^2+2\). Det ger \(x^2=1\), alltså \(x=-1\) och \(x=1\).</p><p>Den nedåtvända parabeln ligger överst mellan skärningarna.</p>\[A=\int_{-1}^{1}(2-2x^2)\,dx\]\[A=\left[2x-\frac{2x^3}{3}\right]_{-1}^{1}\]\[A=\frac43-\left(-\frac43\right)=\frac83.\]',r'\(8/3\) areaenheter.'),'8/3',r'<p>Bestäm skärningarna. Integrera övre funktion minus undre; området är symmetriskt kring y-axeln.</p>')
for id in ['3.91','3.63']:
    def relabel(value):
        if isinstance(value,str):
            return value.replace('x="345" y="222"','x="290" y="222"') if id=='3.91' else value.replace('x="285" y="233"','x="185" y="165"')
        if isinstance(value,list):return [relabel(x) for x in value]
        if isinstance(value,dict):return {k:relabel(v) for k,v in value.items()}
        return value
    q=Q[id]; updated=relabel(q); q.clear(); q.update(updated)
save(p,src,bank,{'3.91','3.18','3.57','3.63','3.177','3.157','3.417'})

p,src,bank=load('uppgifterma1.js');q=next(q for q in bank if q['id']=='8.02')
body='<path d="M140 85 L140 215 A110 24 0 0 0 360 215 L360 85" fill="#f4f8fb" stroke="#24435e" stroke-width="2.5"/><path d="M142 153 L142 215 A108 22 0 0 0 358 215 L358 153 Z" fill="#b5dce9"/><ellipse cx="250" cy="153" rx="108" ry="23" fill="#d4edf5" stroke="#4388a4" stroke-width="1.7"/><ellipse cx="250" cy="85" rx="110" ry="24" fill="none" stroke="#24435e" stroke-width="2.5"/><path d="M410 38 H300 V105" fill="none" stroke="#536979" stroke-width="10"/><path d="M300 105 V136" stroke="#2085a8" stroke-width="5"/><polygon points="300,143 294,132 306,132" fill="#2085a8"/>'+text(403,75,'3 l/min',anchor='middle')+text(250,192,'vatten')+text(250,282,'24 liter från början')
q['t']=re.sub(r'<svg[\s\S]*?</svg>',lambda _:wrap('Tank med vattenyta och ett rör som tillför 3 liter per minut. Från början finns 24 liter.',body),q['t'])
save(p,src,bank,{'8.02'})
print('Updated Ma4: 3.18, 3.57, 3.63, 3.91, 3.157, 3.177, 3.417. Ma1: 8.02.')
