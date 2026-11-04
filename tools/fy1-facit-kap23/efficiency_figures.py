"""Purpose-built SVG diagrams for the efficiency practice round."""
from html import escape

def txt(x,y,s,size=19,anchor='middle',color='#17334d'):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" paint-order="stroke" stroke="white" stroke-width="4" stroke-linejoin="round">{escape(s)}</text>'
def line(x,y,X,Y,color='#17334d',dash=''):
 return f'<line x1="{x}" y1="{y}" x2="{X}" y2="{Y}" stroke="{color}" stroke-width="2.5"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def wrap(body,label,w=560,h=340):
 return f'<div class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" style="width:100%;max-width:{w}px"><rect width="{w}" height="{h}" rx="12" fill="white"/>'+body+'</svg></div>'
def resistor(x,y,label):
 return f'<rect x="{x-10}" y="{y-24}" width="20" height="48" fill="white" stroke="#17334d" stroke-width="2.5"/>'+txt(x+24,y+6,label,18,'start')
def circuit(E='ε',r='r',R='R',I='',parallel=False):
 s=line(150,50,410,50)+line(410,50,410,270)+line(410,270,150,270)+line(150,270,150,50)
 s+='<rect x="130" y="95" width="40" height="24" fill="white"/>'+line(128,100,172,100)+line(138,116,162,116)
 s+=f'<rect x="115" y="77" width="70" height="168" rx="9" fill="none" stroke="#7593a8" stroke-width="1.5" stroke-dasharray="5 4"/>'
 s+=resistor(150,203,'')+txt(105,109,E,18,'end')+txt(105,209,r,18,'end')+txt(150,301,'Batteri',17)
 s+=resistor(410,160,R)
 if I:s+=line(220,50,290,50,'#b64f22')+'<path d="M280 44 L290 50 L280 56" fill="none" stroke="#b64f22" stroke-width="2.5"/>'+txt(255,32,I,18)
 if parallel:
  s+=line(310,50,310,270)+resistor(310,160,'6,0 Ω')+txt(410,248,'',18)
  for x in [310,410]:
   for y in [50,270]:s+=f'<circle cx="{x}" cy="{y}" r="4" fill="#17334d"/>'
 return wrap(s,'Batterimodell med inre resistans och yttre belastning')
def flow():
 s=txt(100,65,'Omvandlad energi',19)+txt(100,94,'500 J',22)+line(100,110,100,160)+line(100,160,300,160)
 s+='<path d="M288 153 L300 160 L288 167" fill="none" stroke="#17334d" stroke-width="3"/>'
 s+=line(220,160,220,260)+line(220,260,300,260)+'<path d="M288 253 L300 260 L288 267" fill="none" stroke="#17334d" stroke-width="3"/>'
 s+=txt(410,151,'Till yttre kretsen',19)+txt(410,182,'?',22)+txt(410,250,'Värme i batteriet',19)+txt(410,281,'100 J',22)
 return wrap(s,'Energiflöde: 500 J omvandlas, 100 J blir värme i batteriet')
def pulse():
 x=lambda t:65+t*7.5;y=lambda i:280-i*95
 s=''
 for t in [0,10,20,30,40,50,60]:s+=line(x(t),280,x(t),55,'#dae5ec')+txt(x(t),306,str(t),17)
 for i in [.2,1,2]:s+=line(65,y(i),515,y(i),'#dae5ec')+txt(54,y(i)+6,str(i).replace('.',','),17,'end')
 s+=line(65,280,525,280)+line(65,280,65,40)+txt(65,25,'I (A)',18)+txt(520,331,'t (s)',18)
 s+=f'<path d="M{x(0)} {y(2)} H{x(10)} V{y(.2)} H{x(60)}" fill="none" stroke="#126b9a" stroke-width="4"/>'
 return wrap(s,'Strömmen är 2,0 A i 10 s och därefter 0,20 A i 50 s',560,350)
def compare():
 s=txt(280,32,'Samma resistor provas med ett batteri i taget',20)
 for x,name,r in [(145,'A','0,20 Ω'),(405,'B','1,0 Ω')]:
  s+=f'<rect x="{x-100}" y="65" width="200" height="155" rx="14" fill="#eef6fc" stroke="#17334d" stroke-width="2"/>'
  s+=txt(x,98,'Batteri '+name,22)+txt(x,143,'ε = 12 V',21)+txt(x,183,'r = '+r,21)
 s+=txt(280,270,'Yttre resistor: 4,0 Ω',22)
 return wrap(s,'Två batterier med samma ems och olika inre resistans',560,310)
def motor():
 s=txt(110,40,'Batteri',21)+txt(110,72,'ε = 12 V',19)+txt(110,101,'U = 10 V',19)
 s+=line(110,120,110,195)+line(110,195,265,195)+'<path d="M252 187 L265 195 L252 203" fill="none" stroke="#17334d" stroke-width="3"/>'+txt(190,175,'2,0 A',18)
 s+='<circle cx="310" cy="195" r="42" fill="#eef6fc" stroke="#17334d" stroke-width="3"/>'+txt(310,203,'M',26)+txt(310,263,'Motor: η = 75 %',19)
 s+=line(352,195,460,195)+line(460,195,460,100)+'<rect x="430" y="55" width="60" height="45" rx="4" fill="#edf4e8" stroke="#17334d" stroke-width="2"/>'+txt(460,84,'8,0 kg',17)
 s+=line(515,175,515,75,'#b64f22')+'<path d="M508 86 L515 75 L522 86" fill="none" stroke="#b64f22" stroke-width="2.5"/>'+txt(515,212,'3,0 m',17)
 return wrap(s,'Batteriet driver en motor som lyfter en last')
def data_table():
 s=txt(280,35,'Två mätningar på samma batteri',21)
 for x,y,w,h in [(90,65,380,55),(90,120,380,60),(90,180,380,60)]:
  s+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#7694a8"/>'
 s+=line(280,65,280,240,'#7694a8')+txt(185,100,'Ström (A)',20)+txt(375,100,'Polspänning (V)',20)
 for y,i,u in [(158,'0,50','5,5'),(218,'1,0','5,0')]:s+=txt(185,y,i,22)+txt(375,y,u,22)
 return wrap(s,'Tabell: 0,50 A ger 5,5 V och 1,0 A ger 5,0 V',560,280)
def powergraph():
 X=lambda i:65+i*75;Y=lambda p:300-p*24
 s=''
 for i in range(7):s+=line(X(i),300,X(i),50,'#dae5ec')+txt(X(i),325,str(i),17)
 for p in [2,4,6,8,10]:s+=line(65,Y(p),515,Y(p),'#dae5ec')+txt(52,Y(p)+6,str(p),17,'end')
 s+=line(65,300,525,300)+line(65,300,65,40)+txt(65,24,'P (W)',18)+txt(520,353,'I (A)',18)
 pts=' '.join(f'{X(i/30):.2f},{Y(6*i/30-(i/30)**2):.2f}' for i in range(181))
 s+=f'<polyline points="{pts}" fill="none" stroke="#1464a0" stroke-width="3"/>'+line(65,Y(8),515,Y(8),'#b64f22')+txt(510,Y(8)-11,'8,0 W',18,'end','#b64f22')
 for i in [2,4]:s+=line(X(i),Y(8),X(i),300,'#b64f22','5 4')+f'<circle cx="{X(i)}" cy="{Y(8)}" r="5" fill="#b64f22"/>'
 s+=txt(285,25,'P = 6I − I²',19)
 return wrap(s,'Två strömmar, 2 A och 4 A, ger yttre effekt 8 W',560,375)
def cellpair():
 s=txt(280,35,'Två likadana celler',22)
 for x in [165,395]:
  s+=f'<rect x="{x-80}" y="65" width="160" height="155" rx="15" fill="#eef6fc" stroke="#17334d" stroke-width="2"/>'+txt(x,107,'ε = 1,5 V',20)+txt(x,151,'r = 0,50 Ω',20)+txt(x,194,'+       −',24)
 s+=txt(280,265,'Yttre resistor: 1,0 Ω',20)+txt(280,300,'Serie eller parallellt?',20)
 return wrap(s,'Två identiska celler kan seriekopplas eller parallellkopplas')
def heat():
 s=txt(280,35,'Strömmen är 2,0 A under 60 s',21)
 s+='<rect x="180" y="75" width="200" height="145" rx="16" fill="#eef6fc" stroke="#17334d" stroke-width="3"/>'+txt(280,120,'Batteri',22)+txt(280,166,'r = ?',22)
 s+=line(100,105,180,105)+line(380,105,460,105)+line(280,220,280,273,'#b64f22')+'<path d="M272 262 L280 273 L288 262" fill="none" stroke="#b64f22" stroke-width="3"/>'+txt(280,307,'Bildad värme: 72 J',20)
 return wrap(s,'Batteriets inre resistans är okänd, ström och bildad värme är givna')
def ageing():
 s=txt(280,35,'Samma ström genom batteriet',22)
 for x,title,r in [(150,'Före','r'),(410,'Efter','3r')]:
  s+=f'<rect x="{x-90}" y="75" width="180" height="140" rx="12" fill="#eef6fc" stroke="#17334d" stroke-width="2"/>'+txt(x,113,title,22)+txt(x,170,r,27)
 s+=line(255,145,305,145)+'<path d="M294 138 L305 145 L294 152" fill="none" stroke="#17334d" stroke-width="2.5"/>'
 return wrap(s,'Inre resistansen ökar från r till 3r medan strömmen är oförändrad',560,260)
