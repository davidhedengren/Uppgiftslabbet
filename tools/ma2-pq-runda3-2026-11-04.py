"""Manuellt granskade lösningar: funktioner, substitution och geometri."""
import json,re
from pathlib import Path
from ma2_pq_format import solution,p,m,I,st,pq
root=Path(__file__).resolve().parents[1];f=root/'uppgifterma2.js';source=f.read_text();start=source.index('[')
bank=json.loads(source[start:].strip().removesuffix(';'));Q={q['id']:q for q in bank};changed=[]
def put(id,steps,answer,hint=None):
 Q[id]['s']=solution(steps,answer);changed.append(id)
 if hint:Q[id]['ledtrad']=p(hint)
def parts(id,plans,cardplans=None):
 sols=[solution(*plan) for plan in plans]
 Q[id]['s']='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+chr(97+i)+')</span><div class="facit-arbete">'+s+'</div></div>' for i,s in enumerate(sols))+'</div>'
 if Q[id].get('spelDelar'):
  cs=[solution(*plan) for plan in cardplans] if cardplans else sols
  assert len(cs)==len(Q[id]['spelDelar'])
  for d,s in zip(Q[id]['spelDelar'],cs):d['s']=s
 changed.append(id)
a05=([st('Nollställen uppfyller '+I('g(x)=0'),r'\begin{aligned}-x^2+8x-12&=0\\x^2-8x+12&=0\end{aligned}','Multiplicera hela ekvationen med −1.')]+pq(-8,12),I('x=2')+' och '+I('x=6')+'.')
b05=([st('Symmetrilinjen ligger mitt mellan nollställena',r'x_s=\frac{x_1+x_2}{2}',r'Använd nollställena 2 och 6 från a).'),st('Beräkna mittpunkten i x-led',r'x_s=\frac{2+6}{2}=4')],'Symmetrilinjen är '+I('x=4')+'.')
b05card=([st('Symmetrilinjen för '+I('ax^2+bx+c'),r'x_s=-\frac{b}{2a}',r'Här är koefficienterna \(a=-1\) och \(b=8\).'),st('Sätt in koefficienterna',r'x_s=-\frac{8}{2\cdot(-1)}=4')],'Symmetrilinjen är '+I('x=4')+'.')
c05=([st('Kvadratkomplettera med '+I('(x-4)^2=x^2-8x+16'),r'\begin{aligned}g(x)&=-(x^2-8x+16)+16-12\\&=-(x-4)^2+4\end{aligned}'),st('En kvadrat är alltid minst noll',why=r'Eftersom \((x-4)^2\ge0\) är \(-(x-4)^2\le0\). Funktionens största värde är därför 4, och det nås när \(x=4\).')],'Funktionens största värde är 4.')
parts('2.05',[a05,b05,c05],[a05,b05card,c05])
Q['2.05']['traningsniva']=[2,1,2]
for d,level in zip(Q['2.05']['spelDelar'],[2,1,2]):d['traningsniva']=level
parts('2.245',[
 ([st('Sätt in '+I('x=4')+' i funktionsformeln',r'\begin{aligned}f(4)&=4^2-5\cdot4+6\\&=16-20+6\\&=2\end{aligned}')],I('f(4)=2')+'.'),
 ([st('Nollställena uppfyller '+I('f(x)=0'),r'x^2-5x+6=0')]+pq(-5,6),I('x=2')+' och '+I('x=3')+'.')])
Q['2.245']['familj']='Egenskaper och funktionsvärden';Q['2.245']['ledtrad']=p(r'Sätt in det givna x-värdet när du söker ett funktionsvärde. För nollställena sätter du f(x)=0 och använder pq-formeln.')
parts('2.297',[
 ([st('Sätt in '+I('x=2')+' i funktionsformeln',r'\begin{aligned}f(2)&=2^2-6\cdot2+5\\&=4-12+5\\&=-3\end{aligned}')],I('f(2)=-3')+'.'),
 ([st('Ett nollställe ger '+I('f(x)=0'),r'\begin{aligned}f(1)&=1^2-6\cdot1+5\\&=1-6+5\\&=0\end{aligned}')],'Ja, '+I('x=1')+' är ett nollställe.'),
 ([st('Sätt funktionsvärdet till noll',r'x^2-6x+5=0')]+pq(-6,5)+[st('Välj det andra nollstället',why=r'Nollstället 1 är redan givet. Den andra roten är därför \(x=5\).')],I('x=5')+'.')])
Q['2.297']['ledtrad']=p(r'Sätt in x-värdet när du söker ett funktionsvärde. För att hitta nollställen löser du f(x)=0 med pq-formeln.')
put('2.302',[st('Nollställen uppfyller '+I('f(x)=0'),r'x^2-6x+8=0')]+pq(-6,8)+[st('Symmetrilinjen ligger mitt mellan nollställena',r'x_s=\frac{2+4}{2}=3'),st('Beräkna värdet på symmetrilinjen',r'\begin{aligned}f(3)&=3^2-6\cdot3+8\\&=9-18+8=-1\end{aligned}'),st('Avgör om värdet är ett minimum',why=r'Koefficienten framför \(x^2\) är positiv. Parabeln är uppåtvänd och har därför sitt minsta värde på symmetrilinjen.')],'Nollställena är 2 och 4. Symmetrilinjen är '+I('x=3')+'. Minsta värdet är −1.',r'Sätt f(x)=0 och använd pq-formeln. Symmetrilinjen ligger mitt mellan nollställena. Sätt sedan in dess x-värde i funktionen.')
if 'Ange nollställena i stigande ordning.' not in Q['2.302']['t']:
 Q['2.302']['t']+=p('Ange nollställena i stigande ordning.')
Q['2.302']['svarEtiketter'][0]='Mindre nollstället';Q['2.302']['svarEtiketter'][1]='Större nollstället'
put('2.303',[st('Samma funktionsvärde betyder '+I('f(x)=g(x)'),r'\begin{aligned}x^2-4x+3&=x-1\\x^2-5x+4&=0\end{aligned}','Subtrahera högerledet från båda leden.')]+pq(-5,4)+[st('Kontrollera i båda funktionerna',r'\begin{aligned}f(1)&=1-4+3=0=g(1)\\f(4)&=16-16+3=3=g(4)\end{aligned}')],I('x=1')+' eller '+I('x=4')+'.',r'Sätt funktionsuttrycken lika, samla alla termer i ett led och använd pq-formeln.')
Q['2.303']['familj']='Egenskaper och funktionsvärden'
put('2.485',[st('Substitution: '+I('u=x^2'),r'u^2-13u+36=0',r'Eftersom \(x^4=(x^2)^2\) får vi en andragradsekvation i u. Dessutom måste \(u\ge0\).')]+pq(-13,36,'u')+[st('Gå tillbaka till x med kvadratrotsmetoden',r'\begin{aligned}x^2=9&\Rightarrow x=\pm3\\x^2=4&\Rightarrow x=\pm2\end{aligned}','Båda u-värdena är positiva. Varje värde ger därför två x-värden, ett positivt och ett negativt.'),st('Kontrollera i ursprungsekvationen',r'\begin{aligned}(\pm3)^4-13(\pm3)^2+36&=81-117+36\\&=0\\(\pm2)^4-13(\pm2)^2+36&=16-52+36\\&=0\end{aligned}')],I('x=-3,-2,2,3')+'.')
put('2.487',[st('Multiplicera med x eftersom '+I(r'x\ne0'),r'x^2+6=5x'),st('Skriv på nollform',r'x^2-5x+6=0')]+pq(-5,6)+[st('Kontrollera i ekvationen med bråket kvar',r'\begin{aligned}2+\frac62&=5\\3+\frac63&=5\end{aligned}','Båda rötterna är skilda från noll, så båda är tillåtna.')],I('x=2')+' eller '+I('x=3')+'.')
put('2.523',pq(-7,10)+[st('Kontrollera båda rötterna',r'\begin{aligned}2^2-7\cdot2+10&=0\\5^2-7\cdot5+10&=0\end{aligned}')],I('x=2')+' eller '+I('x=5')+'.',r'Ekvationen är redan på formen x²+px+q=0. Identifiera p och q och använd pq-formeln.')
parts('2.692',[
 ([st('Isolera kvadraten',r'x^2=16'),st('Kvadratrotsmetoden: '+I(r'x=\pm\sqrt{16}'),r'x=\pm4','Både 4 och −4 har kvadraten 16.')],I('x=-4')+' eller '+I('x=4')+'.'),
 ([st('Bryt ut den gemensamma faktorn x',r'x^2+5x=x(x+5)=0'),st('Nollproduktmetoden: '+I('uv=0'),r'x=0\quad\text{eller}\quad x+5=0', 'Minst en faktor måste vara noll. Dela inte med x, för då försvinner möjligheten x=0.')],I('x=0')+' eller '+I('x=-5')+'.'),
 (pq(4,-21),I('x=3')+' eller '+I('x=-7')+'.')])
Q['2.692']['ledtrad']=p('När x-termen saknas kan du ta kvadratroten. När konstanttermen saknas kan du bryta ut x. När alla tre termer finns kan du använda pq-formeln.')
put('2.163',[st('Sätt in den kända roten '+I('x=3'),r'\begin{aligned}3^2+3p-18&=0\\3p&=9\\p&=3\end{aligned}'),st('Lös ekvationen med det funna p-värdet',r'x^2+3x-18=0')]+pq(3,-18)+[st('Identifiera den andra roten',why=r'Roten 3 är redan känd. Den andra roten är −6. Kontroll: \((-6)^2+3\cdot(-6)-18=0\).')],I('p=3')+' och den andra roten är '+I('x=-6')+'.',r'Sätt in den givna roten och bestäm p. Lös sedan den färdiga andragradsekvationen med pq-formeln.')
put('2.164',[st('Beskriv rötternas summa och produkt',r'\begin{aligned}r_2-r_1&=5\\r_1r_2&=36\end{aligned}',r'Låt \(r_1\) vara den mindre roten och \(r_2\) den större.'),st('Kvadreringsreglerna kopplar summa och differens',r'(r_1+r_2)^2=(r_2-r_1)^2+4r_1r_2'),st('Sätt in de givna villkoren',r'\begin{aligned}(r_1+r_2)^2&=5^2+4\cdot36\\&=25+144=169\end{aligned}'),st('Summan kan vara positiv eller negativ',r'r_1+r_2=\pm13'),st('Rötter och koefficienter: '+I(r'p=-(r_1+r_2),\ q=r_1r_2'),r'\begin{aligned}r_1+r_2=13&\Rightarrow p=-13\,,\ q=36\\r_1+r_2=-13&\Rightarrow p=13\,,\ q=36\end{aligned}'),st('Kontrollera att båda fallen ger heltalsrötter',r'\begin{aligned}r_1+r_2=13:\quad r_2&=\frac{13+5}{2}=9\\r_1&=9-5=4\\r_1+r_2=-13:\quad r_2&=\frac{-13+5}{2}=-4\\r_1&=-4-5=-9\end{aligned}', 'I båda fallen är rötterna heltal med differensen 5 och produkten 36.')],I('p=-13')+' eller '+I('p=13')+'. I båda fallen är '+I('q=36')+'.',r'Koppla rötternas summa till deras differens med kvadreringsreglerna. Använd sedan sambanden mellan rötter och koefficienter.')
put('1.1096',[st('Utveckla produkten med distributiva lagen',r'(x+a)(x+b)=x^2+(a+b)x+ab'),st('Jämför koefficienterna',r'a+b=-2,\qquad ab=-15','Likheten gäller för alla x, så koefficienterna för varje potens av x måste vara lika.'),st('Ersätt b med '+I('b=-2-a'),r'\begin{aligned}a(-2-a)&=-15\\a^2+2a-15&=0\end{aligned}')]+pq(2,-15,'a')+[st('Använd villkoret att a är större än b',why=r'Om \(a=3\) blir \(b=-5\), vilket uppfyller \(a>b\). Valet \(a=-5\) ger \(b=3\) och ska därför inte användas.'),st('Kontrollera summa och produkt',r'3+(-5)=-2,\qquad3\cdot(-5)=-15')],I('a=3')+' och '+I('b=-5')+'.',r'Jämför koefficienterna. Lös ut b ur summan och sätt in i produkten. Använd sedan pq-formeln och villkoret a>b.')
put('3.182',[st('Yttervinkelsatsen: '+I(r'v_{\mathrm{yttre}}=\angle A+\angle B'),r'x^2-10=(x+20)+(2x+10)'),st('Samla termer i ett led',r'x^2-3x-40=0')]+pq(-3,-40)+[st('Förkasta roten som ger en nollvinkel',why=r'Om \(x=-5\) blir vinkeln vid B \(2\cdot(-5)+10=0^\circ\). Det är omöjligt i en triangel, så \(x=8\).'),st('Beräkna de två givna vinklarna',r'\begin{aligned}\angle A&=(8+20)^\circ=28^\circ\\\angle B&=(2\cdot8+10)^\circ=26^\circ\end{aligned}'),st('Den inre vinkeln och yttervinkeln bildar 180°',r'\begin{aligned}v_{\mathrm{yttre}}&=(8^2-10)^\circ=54^\circ\\\angle C&=180^\circ-54^\circ=126^\circ\end{aligned}'),st('Kontrollera vinkelsumman och att triangeln är trubbig',r'28^\circ+26^\circ+126^\circ=180^\circ',r'Vinkeln vid C är större än \(90^\circ\), som krävs.')],I(r'\angle A=28^\circ')+', '+I(r'\angle B=26^\circ')+' och '+I(r'\angle C=126^\circ')+'.')
put('3.187',[st('Pythagoras sats: '+I('x^2+(x+7)^2=17^2'),why='Rektangelns diagonal är hypotenusa i en rätvinklig triangel med rektangelns sidor som kateter.'),st('Utveckla och dividera med 2',r'\begin{aligned}2x^2+14x+49&=289\\2x^2+14x-240&=0\\x^2+7x-120&=0\end{aligned}')]+pq(7,-120)+[st('Välj en positiv sidlängd',why=r'En sida kan inte vara negativ. Alltså är \(x=8\), och den längre sidan är \(8+7=15\) cm.'),st('Kontrollera diagonalen',r'8^2+15^2=64+225=289=17^2')],'Sidorna är 8 cm och 15 cm.')
put('3.493',[st('Avståndsformeln: '+I(r'd^2=(x_2-x_1)^2+(y_2-y_1)^2'),r'(t-3)^2+(2t-1)^2=5^2',r'Sätt in punkterna \(P=(t,2t)\) och \(Q=(3,1)\).'),st('Utveckla kvadraterna',r'\begin{aligned}t^2-6t+9+4t^2-4t+1&=25\\5t^2-10t-15&=0\\t^2-2t-3&=0\end{aligned}')]+pq(-2,-3,'t')+[st('Kontrollera båda punkternas avstånd',r'\begin{aligned}t=3:\quad P&=(3,6)\\d&=\sqrt{0^2+5^2}=5\\t=-1:\quad P&=(-1,-2)\\d&=\sqrt{(-4)^2+(-3)^2}=5\end{aligned}', 'Båda punkterna ligger på linjen y=2x och har avståndet 5 till Q.')],I('t=-1')+' eller '+I('t=3')+'.')
put('3.510',[st('Kordasatsen: '+I(r'AS\cdot SB=CS\cdot SD'),r'x(x+4)=3\cdot7=21'),st('Utveckla och samla termer',r'x^2+4x-21=0')]+pq(4,-21)+[st('Välj en positiv delsträcka',why=r'En delsträcka måste vara positiv. Därför är \(x=3\); roten −7 kan inte användas.'),st('Addera båda delarna av bron AB',r'AB=x+(x+4)=3+7=10\ \mathrm m','Frågan gäller hela bron, inte bara den del som betecknas x.')],'Bron AB är 10 m lång.')
for id in changed:Q[id]['miniräknare']=True
pat=re.compile(r'"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|true|false|null')
body=source[start:];old=list(pat.finditer(body));new=list(pat.finditer(json.dumps(bank,ensure_ascii=False)))
assert len(old)==len(new)
for x,y in reversed(list(zip(old,new))):
 if json.loads(x.group())!=json.loads(y.group()):body=body[:x.start()]+y.group()+body[x.end():]
f.write_text(source[:start]+body)
print(len(changed),changed)
