"""Manuellt granskade lösningsplaner. Rendera enbart angivna Ma2-uppgifter."""
import json,re,sys,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'fy1-facit-kap23'))
from render import solution,p,m,inline as I
f=Path(__file__).resolve().parents[1]/'uppgifterma2.js'
source=f.read_text();start=source.index('[');bank=json.loads(source[start:].strip().removesuffix(';'));Q={q['id']:q for q in bank};changed=[]
def st(h,tex='',why=''):return (h,(p(why) if why else '')+(m(tex) if tex else ''))
def num(v):return f'{v:g}'.replace('.', '{,}')
def pq(a,b,v='x'):
 # Arithmetic rendering of explicitly selected p,q; not heuristic task classification.
 half=-a/2;disc=(a/2)**2-b;root=math.sqrt(disc)
 assert root*2==round(root*2)
 aa=num(a);bb=num(b);sub=bb if b>=0 else '('+bb+')'
 tex=rf'\begin{{aligned}}{v}&=-\frac{{{aa}}}2\pm\sqrt{{\left(\frac{{{aa}}}2\right)^2-{sub}}}\\&={num(half)}\pm\sqrt{{{num((a/2)**2)}'+('-'+bb if b>=0 else '+'+num(-b))+rf'}}\\&={num(half)}\pm\sqrt{{{num(disc)}}}\\&={num(half)}\pm {num(root)}\end{{aligned}}'
 return [st('Pq-formeln: '+I(v+r'=-\frac p2\pm\sqrt{(\frac p2)^2-q}'),why='Jämför med '+I(v+'^2+p'+v+'+q=0')+'. Här är '+I('p='+aa)+' och '+I('q='+bb)+'.'),st('Sätt in p och q',tex),st('Beräkna båda rötterna',rf'{v}_1={num(half+root)},\qquad {v}_2={num(half-root)}')]
def put(id,steps,ans,hint=None):
 Q[id]['s']=solution(steps,ans)
 if hint:Q[id]['ledtrad']=p(hint)
 changed.append(id)
put('2.09',[st('Skriv på nollform',r'x^2-5x-14=0', 'Subtrahera 14 från båda leden.')]+pq(-5,-14)+[st('Kontroll i ursprungsekvationen',r'\begin{aligned}7^2-5\cdot7&=14\\(-2)^2-5\cdot(-2)&=14\end{aligned}')],I('x=7')+' eller '+I('x=-2')+'.','Samla alla termer i vänster led och använd pq-formeln.')
put('2.73',[st('Omkretsen ger summan av två sidor',r'x+y=34/2=17',r'Låt sidorna vara \(x\) och \(y\) cm. Då är \(y=17-x\).'),st('Rektangelns area: '+I('A=xy'),r'\begin{aligned}x(17-x)&=60\\17x-x^2&=60\\x^2-17x+60&=0\end{aligned}')]+pq(-17,60)+[st('Tolka rötterna som sidlängder',why='Rötterna ger samma rektangel: om ena sidan är 5 cm är den andra 12 cm, och tvärtom.'),st('Kontrollera area och omkrets',r'\begin{aligned}5\cdot12&=60\ \mathrm{cm^2}\\2(5+12)&=34\ \mathrm{cm}\end{aligned}')],'Sidorna är 5 cm och 12 cm.')
put('2.102',[st('Ramen ökar båda måtten med 2x',why=r'Låt ramens bredd vara \(x\) cm. Yttermåtten blir \(12+2x\) och \(8+2x\) cm.'),st('Hela tavlans area: '+I('A=bh'),r'\begin{aligned}(12+2x)(8+2x)&=192\\4x^2+40x+96&=192\\x^2+10x-24&=0\end{aligned}', 'Utveckla, subtrahera 192 och dividera med 4.')]+pq(10,-24)+[st('Välj en positiv bredd',why=r'\(x=-12\) kan inte vara en bredd. Med \(x=2\) blir yttermåtten 16 cm och 12 cm, och arean \(16\cdot12=192\) cm².')],'Ramen är 2 cm bred.')
# Three standalone cards: all three solutions must show their own pq insertion.
parts=[]
for d,a,b in zip(Q['2.121']['spelDelar'],[-11,8,-3],[24,15,-18]):
 hi=-a/2+math.sqrt(a*a/4-b);lo=-a/2-math.sqrt(a*a/4-b)
 d['s']=solution(pq(a,b),I('x='+num(hi))+' eller '+I('x='+num(lo))+'.');d['traningsniva']=2
 parts.append('<div class="facit-del"><span class="facit-mark">'+d['etikett']+')</span><div class="facit-arbete">'+d['s']+'</div></div>')
Q['2.121']['s']='<div class="facit-v2 facit-stegvis">'+''.join(parts)+'</div>';changed.append('2.121')
Q['2.121']['t']=Q['2.121']['t'].replace('Faktorisera och lös.','Lös ekvationerna med pq-formeln.')
Q['2.121']['spelIntro']='<p>Lös ekvationen med pq-formeln.</p>'
Q['2.121']['ledtrad']=p(r'Jämför med \(x^2+px+q=0\). Var noga med tecknen på p och q när du använder pq-formeln.')
Q['2.121']['traningsniva']=[2,2,2]
put('2.138',[st('Beskriv två heltal i följd',why=r'Låt det mindre talet vara \(x\). Nästa heltal är \(x+1\).'),st('Produktvillkoret: '+I('x(x+1)=72'),r'x^2+x-72=0')]+pq(1,-72)+[st('Båda rötterna ger giltiga heltalspar',why=r'\(x=8\) ger paret 8 och 9. \(x=-9\) ger paret −9 och −8. Även två negativa tal får en positiv produkt.'),st('Kontrollera produkterna',r'8\cdot9=72,\qquad(-9)(-8)=72')],'8 och 9 eller −9 och −8.',r'Skriv talen som \(x\) och \(x+1\). Använd produktvillkoret och pq-formeln. Talen behöver inte vara positiva.')
put('2.288',[st('Beskriv två positiva heltal i följd',why=r'Låt det mindre talet vara \(x\). Det andra är \(x+1\).'),st('Produktvillkoret: '+I('x(x+1)=132'),r'x^2+x-132=0')]+pq(1,-132)+[st('Välj det positiva talparet',why='Roten 11 ger talen 11 och 12. Roten −12 ger två negativa tal och uppfyller inte villkoret.'),st('Kontrollera produkten',r'11\cdot12=132')],'Talen är 11 och 12.')
put('2.502',[st('Använd summan för att uttrycka båda talen',why=r'Låt ena talet vara \(x\). Då är det andra \(13-x\).'),st('Produktvillkoret: '+I('x(13-x)=30'),r'\begin{aligned}13x-x^2&=30\\x^2-13x+30&=0\end{aligned}')]+pq(-13,30)+[st('Tolka och kontrollera talparet',r'3+10=13,\qquad3\cdot10=30', 'De två rötterna beskriver samma talpar i olika ordning.')],'Talen är 3 och 10.')
# Rectangles: identical algebra, distinct givens and requested quantities.
for id,area,b,ans,unit in [('2.152',40,-40,'Sidorna är 5 cm och 8 cm.','cm'),('2.790',40,-40,'Rabatten är 5 m bred.','m'),('5.44',54,-54,'Bredden är 6 m och längden 9 m.','m')]:
 width=5 if area==40 else 6
 put(id,[st('Uttryck längden med hjälp av bredden',why=f'Låt bredden vara '+I('x')+f' {unit}. Längden är då '+I('x+3')+f' {unit}.'),st('Rektangelns area: '+I('A=bh'),rf'\begin{{aligned}}x(x+3)&={area}\\x^2+3x-{area}&=0\end{{aligned}}')]+pq(3,b)+[st('Välj den positiva bredden',why=f'En sidlängd måste vara positiv. Bredden blir {width} {unit} och längden {width+3} {unit}.'),st('Kontrollera arean',rf'{width}\cdot{width+3}={area}\ \mathrm{{{unit}^2}}')],ans,r'Uttryck längden med hjälp av bredden. Använd sedan arean och pq-formeln.')
Q['2.152']['t']=Q['2.152']['t'].replace('lös den genom faktorisering','lös den med pq-formeln')
put('2.788',[st('Substitution: '+I('t=x-1'),r't^2-5t+6=0', 'Samma parentes förekommer både i kvadrat och som förstagradsterm.')]+pq(-5,6,'t')+[st('Gå tillbaka till x',r'\begin{aligned}x-1=3&\Rightarrow x=4\\x-1=2&\Rightarrow x=3\end{aligned}')],I('x=3')+' eller '+I('x=4')+'.')
put('2.791',[st('Sätt höjden till 16 m',r'-5t^2+20t+1=16'),st('Samla termer och dividera med −5',r'\begin{aligned}-5t^2+20t-15&=0\\t^2-4t+3&=0\end{aligned}')]+pq(-4,3,'t')+[st('Tolka de två tidpunkterna',why='Efter 1 s passerar bollen höjden på väg upp. Efter 3 s passerar den samma höjd på väg ned.')],'Efter 1 s och 3 s.')
# Chords: explicitly verified equations from each diagram/text.
for id,a,b,lhs,rhs,ans,condition in [
 ('3.09',2,-24,'x(x+2)',r'3\cdot8','4','x>0'),('3.49',5,-36,'x(x+5)',r'3\cdot12','4','x>0'),('3.59',3,-40,'x(x+3)',r'4\cdot10','5','x>0'),('3.133',5,-36,'x(x+5)',r'3\cdot12','4','x>0'),('3.168',1,-30,'(x-1)(x+2)',r'4\cdot7','5','x>1'),('3.179',5,-84,'x(x+5)',r'6\cdot14','7','x>0'),('3.204',5,-84,'x(x+5)',r'6\cdot14','7','x>0'),('3.2026',5,-176,'x(x+5)',r'8\cdot22','11','x>0')]:
 eq='x^2+'+('' if a==1 else str(a))+'x'+str(b)+'=0'
 put(id,[st('Kordasatsen: produkterna av delsträckorna är lika',lhs+'='+rhs,'Multiplicera delsträckorna på samma korda med varandra.'),st('Utveckla och samla termer',eq)]+pq(a,b)+[st('Kontrollera längdvillkoret',why='Alla delsträckor måste vara positiva, vilket kräver '+I(condition)+'. Den negativa roten fungerar inte; använd '+I('x='+ans)+'.')],I('x='+ans)+(' m.' if id=='3.2026' else '.'))
put('3.143',[st('Omkretsen ger summan av sidorna',r'x+y=34/2=17',r'Låt sidorna vara \(x\) och \(y\) cm. Då är \(y=17-x\).'),st('Pythagoras sats: '+I('x^2+y^2=13^2'),r'\begin{aligned}x^2+(17-x)^2&=169\\2x^2-34x+289&=169\\x^2-17x+60&=0\end{aligned}')]+pq(-17,60)+[st('Kontrollera rektangeln',r'\begin{aligned}2(5+12)&=34\ \mathrm{cm}\\\sqrt{5^2+12^2}&=13\ \mathrm{cm}\end{aligned}', 'De två rötterna är rektangelns sidlängder.')],'Sidorna är 5 cm och 12 cm.')
put('6.13',[st('Kvadrera båda leden',r'\begin{aligned}x+6&=x^2\\x^2-x-6&=0\end{aligned}',r'Kvadrering kan ge extralösningar. Därför måste kandidaterna prövas i ursprungsekvationen.')]+pq(-1,-6)+[st('Pröva i '+I(r'\sqrt{x+6}=x'),r'\begin{aligned}x=3:&\quad\sqrt{3+6}=3\\x=-2:&\quad\sqrt{-2+6}=2\ne-2\end{aligned}', 'Endast den positiva kandidaten fungerar.')],I('x=3')+'.')
put('6.19',[st('Gången minskar båda innermåtten med 2x',why=r'Låt gångens bredd vara \(x\) m. Innermåtten blir \(24-2x\) och \(18-2x\) m. De måste vara positiva, så \(0<x<9\).'),st('Inre rektangelns area: '+I('A=bh'),r'\begin{aligned}(24-2x)(18-2x)&=280\\432-84x+4x^2&=280\\x^2-21x+38&=0\end{aligned}')]+pq(-21,38)+[st('Välj en bredd som ryms',why=r'\(x=19\) strider mot \(x<9\). Med \(x=2\) blir innermåtten 20 m och 14 m.'),st('Kontrollera den inre arean',r'20\cdot14=280\ \mathrm{m^2}')],'Gången är 2 m bred.')
put('1.1210',[st('Samma y-värde i skärningspunkterna',r'\begin{aligned}x^2&=x+2\\x^2-x-2&=0\end{aligned}')]+pq(-1,-2)+[st('Kontrollera i båda funktionerna',r'\begin{aligned}x=2:&\quad2^2=2+2=4\\x=-1:&\quad(-1)^2=-1+2=1\end{aligned}')],I('x=-1')+' och '+I('x=2')+'.')
put('1.1212',[st('Lös ut y ur summan',r'y=10-x'),st('Substituera i '+I('xy=21'),r'\begin{aligned}x(10-x)&=21\\10x-x^2&=21\\x^2-10x+21&=0\end{aligned}')]+pq(-10,21)+[st('Bestäm det andra talet och kontrollera',r'3+7=10,\qquad3\cdot7=21',r'Om \(x=3\) blir \(y=7\), och om \(x=7\) blir \(y=3\).')],'Talen är 3 och 7.')
# Align the explicitly converted method tasks with their actual teaching area.
for id in ['2.09','2.121']:
 Q[id]['omr']='losningsformel_andragrad';Q[id]['familj']='Lösa med pq-formeln'
for id in ['2.138','2.152']:
 Q[id]['omr']='andragradsekvationer_tillampningar';Q[id]['familj']='Talproblem och villkor' if id=='2.138' else 'Andragradsekvationer i geometri'
# Calculator helps decimal half-coefficients; it does not replace modelling/pq.
for id in changed:Q[id]['miniräknare']=True
# Preserve the bank's mixed formatting and number spellings, changing tokens only.
pat=re.compile(r'"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|true|false|null')
body=source[start:];old=list(pat.finditer(body));new=list(pat.finditer(json.dumps(bank,ensure_ascii=False)))
assert len(old)==len(new)
for x,y in reversed(list(zip(old,new))):
 if json.loads(x.group())!=json.loads(y.group()):body=body[:x.start()]+y.group()+body[x.end():]
f.write_text(source[:start]+body)
print('Changed',len(changed),changed)
