"""Tio handskrivna ekvationsproblem. Kör bara i master; befintliga objekt bevaras."""
import json
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]

def p(s): return '<p>'+s+'</p>'
def m(s): return r'\('+s+r'\)'
def step(title,text='',math=''):
    return '<li><p class="facit-rubrik">'+title+'</p>'+ (p(text) if text else '') + ('<div class="facit-matte">'+r'\['+math+r'\]'+'</div>' if math else '')+'</li>'
def sol(steps,answer):
    return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'.</p></div>'
def txt(x,y,s,size=21,fill='#172b46',anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-family="Arial, sans-serif">{escape(s)}</text>'
def line(x1,y1,x2,y2,col='#334b64',width=3,dash=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def svg(title,body,height=230):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 {height}" role="img" aria-label="{escape(title,quote=True)}" style="display:block;width:100%;max-width:560px;height:auto;margin:16px auto"><title>{escape(title)}</title><rect x="1" y="1" width="478" height="{height-2}" rx="16" fill="#ffffff" stroke="#c7d5e3"/>'+body+'</svg>'
def arrow(x1,y,x2):
    return line(x1,y,x2-9,y,'#315e9a')+f'<path d="M {x2-17} {y-7} L {x2-8} {y} L {x2-17} {y+7}" fill="none" stroke="#315e9a" stroke-width="3"/>'
def vessel(x,col):
    return f'<path d="M {x-49} 81 V 166 Q {x-49} 181 {x-34} 181 H {x+34} Q {x+49} 181 {x+49} 166 V 81" fill="{col}" stroke="#334b64" stroke-width="3"/><path d="M {x-49} 111 Q {x} 122 {x+49} 111" fill="none" stroke="#334b64" stroke-width="2"/>'
def pair(title,left,right,change,colour1='#f7d994',colour2='#add9e8'):
    body=txt(112,34,left[0])+txt(368,34,right[0])+vessel(112,colour1)+vessel(368,colour2)
    body+=arrow(181,142,303)+txt(240,89,change,19)
    body+=txt(112,212,left[1])+txt(368,212,right[1])
    return svg(title,body+txt(240,246,'Schematisk bild',18),270)

def cards(title,columns,footer=None):
    body=''
    for i,(head,rows) in enumerate(columns):
        x=18+232*i
        body+=f'<rect x="{x}" y="20" width="212" height="190" rx="12" fill="'+('#edf5ff' if i==0 else '#e8f6f0')+'"/>'
        body+=txt(x+106,56,head,23)
        for j,r in enumerate(rows):body+=txt(x+106,102+j*38,r,20)
    return svg(title,body+(txt(240,246,footer,20) if footer else ''),270 if footer else 230)

TASKS=[]
def add(id,title,t,h,steps,answer,value,unit,fig,n=4):
    TASKS.append(dict(id=id,kap=1,omr='ekv_problemlosning',kurs=['1a','1b','1c'],niva='A' if n==5 else 'C',poang='0/1/2' if n==5 else '0/2/0',typ=title,familj='Problemlösning i flera steg',formaga=['problemlösning','modellering'],traningsniva=n,arbetsinsats=3 if n==5 else 2,miniräknare=True,geogebra=False,spel=True,självrättning=True,t=t+fig,s=sol(steps,answer),ledtrad=p(h),svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=value,tolerans=1e-9,svarEnhet=unit))

add('1.1675','Bensin till oljeblandning',
    p('Du har 4,5 liter olja och ska tillsätta ren bensin. I den färdiga blandningen ska 2,0 % av volymen vara olja.')+p('Hur många liter bensin ska du tillsätta?'),
    'Vilken volym ska oljemängden jämföras med: bara bensinen eller hela den färdiga blandningen?',[
    step('Bensin och olja ger tillsammans '+m('x+4{,}5')+' liter','Låt '+m('x')+' vara antalet liter bensin. De 4,5 literna olja finns kvar efter blandningen.'),
    step('Oljan är 2,0 % av hela volymen: '+m('4{,}5=0{,}020(x+4{,}5)'), 'Både oljan och bensinen ingår i den volym som procenten räknas på.'),
    step('Dela med 0,020 och ta bort oljans volym','',r'\begin{aligned}x+4{,}5&=225\\x&=220{,}5\end{aligned}'),
    step('Kontrollera oljehalten i 225 liter','Den stora bensinmängden är rimlig eftersom oljan bara ska vara en liten del.',r'\frac{4{,}5}{220{,}5+4{,}5}=0{,}020')],
    '220,5 liter bensin',220.5,'liter',pair('Olja blandas med bensin till 2,0 procent olja',('Olja','4,5 L'),('Blandning','2,0 % olja'),'Bensin tillförs'))

add('1.1676','Två fruktdrycker',
    p('En fruktdryck innehåller 12 % juice. En annan innehåller 30 % juice. Du har 8,0 liter av den svagare drycken och blandar i den starkare tills juicehalten blir 20 %. Halterna avser volym.')+p('Hur många liter av drycken med 30 % juice behövs?'),
    'Här tillförs både juice och annan vätska. Beskriv juicemängden från varje dryck var för sig.',[
    step('Juicemängd = andel '+m(r'\cdot')+' dryckens volym','Låt '+m('x')+' vara antalet liter av den starkare drycken. Den svagare bidrar med 0,96 liter juice; den starkare bidrar med '+m('0{,}30x')+' liter.',r'0{,}12\cdot8=0{,}96'),
    step('Den färdiga drycken innehåller '+m('0{,}20(8+x)')+' liter juice','Sätt summan av de två juicemängderna lika med juicemängden i den färdiga drycken.',r'0{,}96+0{,}30x=0{,}20(8+x)'),
    step('Samla juicebidragen med '+m('x')+' i samma led','',r'\begin{aligned}0{,}96+0{,}30x&=1{,}60+0{,}20x\\0{,}10x&=0{,}64\\x&=6{,}4\end{aligned}'),
    step('Kontrollera 2,88 liter juice i 14,4 liter dryck','',r'\begin{aligned}0{,}96+0{,}30\cdot6{,}4&=2{,}88\\\frac{2{,}88}{8+6{,}4}&=0{,}20\end{aligned}')],
    '6,4 liter av den starkare drycken',6.4,'liter',cards('Två fruktdrycker ska blandas till 20 procent juice',[('Svagare dryck',['8,0 liter','12 % juice']),('Starkare dryck',['Okänd volym','30 % juice'])]))

add('1.1677','Byta ut kylvätska',
    p('En behållare innehåller 18 liter väl omblandad kylvätska med 40 % glykol och resten vatten. Du tappar ur en del av blandningen och fyller på lika många liter rent vatten. Därefter är glykolhalten 25 %. Halterna avser volym.')+p('Hur många liter blandning tappade du ur?'),
    'När blandningen tappas ur försvinner både glykol och vatten. Hur stor del av den urtappade volymen är glykol?',[
    step('Från början finns '+m(r'0{,}40\cdot18')+' liter glykol','Låt '+m('x')+' vara urtappad volym i liter. Eftersom vätskan är omblandad följer '+m('0{,}40x')+' liter glykol med ut.',r'0{,}40\cdot18=7{,}2'),
    step('Slutvolymen är fortfarande 18 liter','Rent vatten innehåller ingen glykol. Slutmängden glykol ska vara '+m(r'0{,}25\cdot18=4{,}5')+' liter.',r'7{,}2-0{,}40x=4{,}5'),
    step('2,7 liter glykol ska följa med ut','',r'\begin{aligned}0{,}40x&=2{,}7\\x&=6{,}75\end{aligned}'),
    step('Kontrollera både volym och glykolhalt','11,25 liter av den gamla blandningen blir kvar. Den innehåller 4,5 liter glykol. Efter påfyllningen är totalvolymen åter 18 liter.',r'\frac{4{,}5}{18}=0{,}25')],
    '6,75 liter blandning',6.75,'liter',pair('Samma volym kylvätska tappas ur som vatten fylls på',('Före','18 L · 40 %'),('Efter','18 L · 25 %'),'Byt mot vatten','#b8e4cf','#d9efe6'))

add('1.1678','Sockerlag i två steg',
    p('En sockerlag av vatten och socker väger 10 kg och innehåller 30 % socker räknat på massan. Den kokas så att 3,0 kg vatten avdunstar. Inget socker försvinner. Därefter tillsätts rent socker tills sockerhalten blir 50 % av den nya massan.')+p('Hur många kg socker ska tillsättas?'),
    'Håll reda på socker och total massa var för sig efter kokningen. När socker sedan tillsätts ändras båda.',[
    step('Socker före kokningen: '+m(r'0{,}30\cdot10=3')+' kg','Efter kokningen finns fortfarande 3 kg socker, men totalmassan har minskat till '+m('10-3=7')+' kg.'),
    step('Tillsatt socker ökar både delen och det hela','Låt '+m('x')+' vara tillsatt sockermassa i kg. Då finns '+m('3+x')+' kg socker i '+m('7+x')+' kg sockerlag.',r'3+x=0{,}50(7+x)'),
    step('Ta bort '+m('0{,}50x')+' och 3 från båda leden','',r'\begin{aligned}3+x&=3{,}5+0{,}50x\\0{,}50x&=0{,}5\\x&=1\end{aligned}'),
    step('Kontrollera 4 kg socker av 8 kg sockerlag','Efter tillsatsen är hälften av massan socker.',r'\frac{3+1}{7+1}=0{,}50')],
    '1 kg socker',1,'kg',pair('Sockerlag kokas och sedan tillsätts socker',('Före kokning','10 kg · 30 %'),('Efter båda stegen','50 % socker'),'Koka','#f7d994','#f0c66e').replace('</svg>',txt(240,191,'+ socker',19)+'</svg>'))

add('1.1679','Två föreningskassor',
    p('Två elevföreningar har sammanlagt 5 000 kr i sina kassor. Musikföreningen använder 25 % av sina pengar till en spelning. Filmföreningen får samtidigt ett bidrag på 600 kr. Därefter har föreningarna lika mycket pengar.')+p('Hur mycket pengar hade musikföreningen från början? (Svara i kr.)'),
    'Om musikföreningens startbelopp är okänt kan filmföreningens startbelopp skrivas med hjälp av totalsumman.',[
    step('Startbeloppen är '+m('x')+' och '+m('5000-x')+' kr','Låt '+m('x')+' vara musikföreningens startbelopp. Den behåller 75 % av det. Filmföreningen lägger 600 kr till sitt startbelopp.'),
    step('Samma slutbelopp: '+m('0{,}75x=5000-x+600'),'Den ena kassan minskar och den andra ökar. De behöver alltså inte ha varit lika stora från början.'),
    step('Addera '+m('x')+' och dela med 1,75','',r'\begin{aligned}1{,}75x&=5600\\x&=3200\end{aligned}'),
    step('Kontrollera att båda får 2 400 kr','Filmföreningen hade 1 800 kr från början.',r'\begin{aligned}0{,}75\cdot3200&=2400\\1800+600&=2400\end{aligned}')],
    '3 200 kr',3200,'kr',cards('Två kassor förändras och blir lika stora',[('Musikföreningen',['Använder 25 %','av sin kassa']),('Filmföreningen',['Får 600 kr','i bidrag'])]))

add('1.1680','Två rabatter och en kupong',
    p('En jacka kostar 240 kr mer än en väska före rabatter. På rean är rabatten 20 % på jackan och 10 % på väskan. När båda köps får kunden dessutom dra av en kupong på 150 kr från den redan rabatterade totalsumman. Kunden betalar 1 164 kr.')+p('Vad kostade jackan före rabatterna? (Svara i kr.)'),
    'Utgå från jackans ordinarie pris. Skriv väskans pris med samma obekanta och behandla rabatterna var för sig.',[
    step('Jackan kostar '+m('x')+' kr och väskan '+m('x-240')+' kr','Efter rabatterna betalas 80 % av jackans pris och 90 % av väskans pris.'),
    step('Pris efter rabatt = ordinarie pris '+m(r'\cdot')+' förändringsfaktor','Kupongen dras av sist, en gång för hela köpet.',r'\begin{gathered}0{,}80x+0{,}90(x-240)\\-150=1164\end{gathered}'),
    step('Utveckla väskans rabatt och samla priserna','',r'\begin{aligned}1{,}70x-216-150&=1164\\1{,}70x&=1530\\x&=900\end{aligned}'),
    step('Kontrollera köpet med ordinarie priserna 900 och 660 kr','Jackan kostar 720 kr och väskan 594 kr på rean.',r'720+594-150=1164')],
    '900 kr',900,'kr',cards('Jacka och väska har olika rabatter; kupongen dras av sist',[('Jacka',['20 % rabatt','240 kr dyrare']),('Väska',['10 % rabatt'])],footer='Därefter: 150 kr av på hela köpet'))

fence=svg('Rektangulär hage med en gemensam mellanvägg och en två meter bred grind',
    '<rect x="60" y="55" width="360" height="140" fill="#eaf5e8"/>'+line(60,55,420,55)+line(60,55,60,195)+line(420,55,420,195)+line(240,55,240,195)+line(60,195,314,195)+line(360,195,420,195)+line(314,195,360,195,'#b5620b',3,'6 5')+
    txt(240,31,'Längd = 2 · bredd + 4 m',21)+txt(30,130,'B',23)+txt(150,131,'Hage 1')+txt(330,131,'Hage 2')+txt(338,228,'Grind 2 m',20)+txt(240,267,'Schematisk bild · B = bredd',18),290)
add('1.1681','Stängsel till två hagar',
    p('En rektangulär hage delas i två med ett stängsel tvärs över bredden. Längden är 4 m längre än dubbla bredden. Längs ytterkanten finns en 2 m bred grind som inte behöver något stängsel. Mellanstängslet har ingen grind.')+p('Totalt används 90 m stängsel, inklusive mellanstängslet. Hur lång är hela hagen? (Svara i m.)'),
    'Räkna vilka hela sträckor som behöver stängsel, inklusive den gemensamma mellanväggen. Grinden ska bara räknas bort en gång.',[
    step('Bredden är '+m('x')+' och längden '+m('2x+4')+' meter','Ytterkanten har två längder och två bredder. Mellanstängslet lägger till en tredje bredd. Grinden tar bort 2 m.'),
    step('Stängsellängd = två längder + tre bredder − grinden','',r'2(2x+4)+3x-2=90'),
    step('Samla de sju bredderna och bestäm bredden','',r'\begin{aligned}4x+8+3x-2&=90\\7x&=84\\x&=12\end{aligned}'),
    step('Frågan gäller längden: '+m('2x+4'),'Bredden 12 m är ett mellanresultat. Längden är 28 m.',r'2\cdot12+4=28'),
    step('Kontrollera de 90 metrarna stängsel','',r'2\cdot28+3\cdot12-2=90')],
    '28 m',28,'m',fence)

cable=svg('En kabel kapas till en lång och fem korta kablar; två meter kasseras',
    line(42,70,430,70,'#2868a1',7)+txt(240,39,'Kabeln från början',23)+
    line(42,154,170,154,'#2868a1',7)+txt(106,126,'Lång kabel',21)+
    ''.join(line(216+i*44,154,244+i*44,154,'#317957',7) for i in range(5))+txt(318,126,'Fem korta',21)+
    txt(240,205,'Dessutom kasseras 2 m',21)+txt(240,239,'Schematisk bild',18),260)
add('1.1682','Kapa kablar',
    p('Från en kabelrulle klipps först en lång kabel som är en fjärdedel av rullens ursprungliga längd. Därefter kasseras 2 m skadad kabel. All kabel som återstår klipps i fem lika långa korta kablar. Varje kort kabel är 1,5 m kortare än den långa.')+p('Hur många meter kabel fanns på rullen från början?'),
    'Beskriv både den långa kabeln och en kort kabel med samma obekanta. Tillsammans med den kasserade biten ska de ge hela ursprungslängden.',[
    step('Den långa kabeln är '+m(r'\frac{x}{4}')+' meter','Låt '+m('x')+' vara ursprungslängden i meter. En kort kabel är då '+m(r'\frac{x}{4}-1{,}5')+' meter.'),
    step('Alla kabelbitar tillsammans har längden '+m('x'),'Räkna med en lång kabel, fem korta och den kasserade biten.',r'\frac{x}{4}+5\left(\frac{x}{4}-1{,}5\right)+2=x'),
    step('Sex fjärdedelar är '+m('1{,}5')+' gånger ursprungslängden','',r'\begin{aligned}1{,}5x-7{,}5+2&=x\\0{,}5x&=5{,}5\\x&=11\end{aligned}'),
    step('Kontrollera att alla kabellängder är positiva','Den långa kabeln är 2,75 m och var och en av de fem korta är 1,25 m. Skillnaden är 1,5 m.',r'2{,}75+5\cdot1{,}25+2=11')],
    '11 m',11,'m',cable)

chase=svg('Tidslinje över två cyklisters starter och den första cyklistens paus',
    txt(28,36,'Nora: 15 km/h',22,anchor='start')+txt(28,112,'Sam: 24 km/h',22,anchor='start')+
    line(45,68,330,68,'#2868a1',5)+line(330,68,425,68,'#b5620b',5,'7 5')+line(235,144,425,144,'#317957',5)+
    ''.join(line(x,170,x,182,'#334b64',2)+txt(x,210,label,20) for x,label in [(45,'09.00'),(235,'09.20'),(330,'09.30'),(425,'09.40')])+
    txt(378,40,'Paus',20)+txt(240,246,'Samma startplats och färdväg',20),270)
add('1.1683','Hinna ikapp under en paus',
    p('Nora startar kl. 09.00 och cyklar med konstant fart 15 km/h. Efter 30 minuters cykling stannar hon i 10 minuter och fortsätter sedan med samma fart. Sam startar kl. 09.20 från samma plats och följer samma väg med konstant fart 24 km/h utan paus.')+p('Hur många minuter efter kl. 09.00 hinner Sam ikapp Nora första gången? (Svara i minuter.)'),
    'Undersök var båda befinner sig när Noras paus börjar och när den slutar. Det avgör vilket rörelseförlopp din ekvation ska beskriva.',[
    step('Sträcka = fart '+m(r'\cdot')+' tid: '+m('s=vt'),'När pausen börjar kl. 09.30 har Nora cyklat i en halvtimme. Sam har då cyklat i tio minuter.',r'\begin{aligned}s_\text{Nora}&=15\cdot\frac{30}{60}=7{,}5\ \mathrm{km}\\s_\text{Sam}&=24\cdot\frac{10}{60}=4\ \mathrm{km}\end{aligned}'),
    step('Sam passerar 7,5 km innan pausen är slut','Kl. 09.40 har Sam cyklat i 20 minuter och nått 8 km. Därför sker mötet under pausen. Före pausen har han inte hunnit ikapp: avståndet minskar från 5 km vid hans start till 3,5 km kl. 09.30.',r'24\cdot\frac{20}{60}=8\ \mathrm{km}'),
    step('Under pausen är Noras sträcka konstant','Låt '+m('t')+' vara antalet minuter efter kl. 09.00. Sam har cyklat i '+m('t-20')+' minuter när han når Noras 7,5 km.',r'24\cdot\frac{t-20}{60}=7{,}5'),
    step('Bestäm tiden och kontrollera att den ligger i pausen','',r'\begin{aligned}0{,}4(t-20)&=7{,}5\\t-20&=18{,}75\\t&=38{,}75\end{aligned}'),
    step('38,75 minuter är mellan 30 och 40 minuter','Mötet sker kl. 09.38.45, alltså innan Nora börjar cykla igen.')],
    '38,75 minuter efter kl. 09.00',38.75,'min',chase,n=5)

add('1.1684','Extra ritblock på köpet',
    p('En skola beställer ett antal likadana ritblock till ordinarie styckepris. Butiken skickar med tre extra block utan extra kostnad. Om den betalda summan fördelas på alla levererade block blir kostnaden per block 6 kr lägre än ordinarie styckepris.')+p('Om butiken i stället hade skickat med fem extra block för samma totalsumma, hade kostnaden per block blivit 9 kr lägre än ordinarie styckepris.')+p('Hur många ritblock beställde skolan från början?'),
    'Jämför värdet av de extra blocken med prissänkningen utslagen på samtliga levererade block. Uttryck ordinarie styckepris på två sätt.',[
    step('Tre gratis block motsvarar 6 kr lägre pris på '+m('n+3')+' block','Låt '+m('n')+' vara beställt antal och '+m('p')+' ordinarie styckepris i kr. Skolan betalar '+m('np')+' kr. Skillnaden till ordinarie pris för alla '+m('n+3')+' block är '+m('3p')+' kr.',r'\begin{aligned}3p&=6(n+3)\\p&=2n+6\end{aligned}'),
    step('Fem gratis block motsvarar 9 kr lägre pris på '+m('n+5')+' block','I det andra erbjudandet är skillnaden till ordinarie pris för alla levererade block '+m('5p')+' kr.',r'\begin{aligned}5p&=9(n+5)\\p&=1{,}8n+9\end{aligned}'),
    step('Samma styckepris: '+m('2n+6=1{,}8n+9'),'De två uttrycken gäller samma ordinarie pris. Därmed får vi en ekvation med bara antalet som obekant.',r'\begin{aligned}0{,}2n&=3\\n&=15\end{aligned}'),
    step('Kontrollera båda erbjudandena','Ordinarie pris är '+m(r'2\cdot15+6=36')+' kr och totalsumman är '+m(r'15\cdot36=540')+' kr. Med tre extra blir kostnaden 30 kr per block; med fem extra blir den 27 kr.',r'\begin{aligned}\frac{540}{18}&=30=36-6\\\frac{540}{20}&=27=36-9\end{aligned}')],
    '15 ritblock',15,'',cards('Två alternativa erbjudanden för samma beställning och totalsumma',[('Erbjudande 1',['3 extra block','6 kr lägre per block']),('Erbjudande 2',['5 extra block','9 kr lägre per block'])]),n=5)

if __name__=='__main__':
    path=ROOT/'uppgifterma1.js';raw=path.read_text();start=raw.index('[');end=raw.rfind(']')
    bank=json.loads(raw[start:end+1]);assert len(TASKS)==10
    assert not {q['id'] for q in bank}&{q['id'] for q in TASKS},'ID finns redan'
    # Lägg endast till nya objekt, utan omformatering av den gamla banken.
    addition=',\n'+',\n'.join('  '+json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ') for q in TASKS)
    path.write_text(raw[:end].rstrip()+addition+'\n'+raw[end:])
    print('Tillagda:',', '.join(q['id'] for q in TASKS))
