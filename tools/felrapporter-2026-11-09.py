"""Handgranskade rättningar från felloggen 2026-11-09 07:58. Bevara andra objekt."""
import json,re,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def m(x):return '<div class="facit-matte">\\['+x+'\\]</div>'
def st(h,b):return '<li><p class="facit-rubrik">'+h+'</p>'+b+'</li>'
def sol(steps,answer):return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def joined(parts):return '<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+chr(97+i)+')</span><div class="facit-arbete">'+s+'</div></div>' for i,s in enumerate(parts))+'</div>'
def read(f):
 s=(ROOT/f).read_text();return json.JSONDecoder().raw_decode(s,s.index('['))[0]
def save(f,b,original):
 changed={q['id']:q for q in b if q!=original[q['id']]};src=(ROOT/f).read_text();dec=json.JSONDecoder();pos=src.index('[')+1;edits=[]
 while True:
  while src[pos].isspace() or src[pos]==',':pos+=1
  if src[pos]==']':break
  q,end=dec.raw_decode(src,pos)
  if q['id'] in changed:
   prefix=src[src.rfind('\n',0,pos)+1:pos]
   indent=prefix if not prefix.strip() else ''
   rendered=json.dumps(changed[q['id']],ensure_ascii=False,indent=2).replace('\n','\n'+indent) if '\n' in src[pos:end] else json.dumps(changed[q['id']],ensure_ascii=False,separators=(',',':'))
   edits.append((pos,end,rendered))
  pos=end
 for a,z,s in reversed(edits):src=src[:a]+s+src[z:]
 (ROOT/f).write_text(src);print(f,list(changed))

def fy(b):
 d={q['id']:q for q in b}
 # Himlakroppens lokala g är nödvändigt situationsdata. Samma värde på alla kort.
 for id,body,value in [('4.190','Mars','3,71'),('4.470','Mars','3,71'),('4.503','Mars','3,71'),('4.187','månen','1,62'),('4.215','månen','1,62'),('4.472','månen','1,62'),('4.498','månen','1,62'),('4.900','månen','1,62'),('4.901','månen','1,62')]:
  q=d[id];sentence=f'<p>I denna uppgift används tyngdaccelerationen {value} m/s² på {body}.</p>'
  for obj in [q,*q.get('spelDelar',[])]:
   for key in ['t','spelIntro']:
    if obj.get(key) and sentence not in obj[key]:obj[key]=sentence+obj[key]
 q=d['4.190'];q['rättSvar']=[78*3.71,9.82/3.71];q['svarVardesiffror']=[2,3];q['svarTabell']={'0':[78*3.72],'1':[9.82/3.72,9.81/3.71,9.81/3.72]}
 for obj in [q,q['spelDelar'][0]]:
  obj['s']=obj['s'].replace('<strong>Svar:</strong> 289,38 N.','<strong>Svar:</strong> Cirka 290 N (två värdesiffror).')
 q['spelDelar'][0]['ledtrad']='<p>Vilket samband kopplar ihop massan, tyngdaccelerationen och tyngdkraften?</p>'
 q=d['4.470'];q['rättSvar']=1025*3.71/1000;q['svarTabell']={'0':[1025*3.72/1000]}
 q=d['4.503'];q['rättSvar']=.4*9.82/3.71;q['svarTabell']={'0':[.4*9.82/3.72,.4*9.81/3.71,.4*9.81/3.72]}
 q=d['3.452'];q['s']=q['s'].replace(r'v=\frac{10-(-20)}{6-0}=\frac{30}{6}=+5\ \mathrm{m/s}',r'\begin{aligned}v&=\frac{10-(-20)}{6-0}\\&=\frac{30}{6}=+5\ \mathrm{m/s}\end{aligned}');t=q['t'];t=t.replace('M65 45V215H380','M65 45V224 M65 108.333H390')
 t=t.replace('<line x1="65" y1="108.333" x2="365" y2="108.333" stroke="#5c6878" stroke-dasharray="4 3"/>','<path d="M385 103.333L392 108.333L385 113.333 M60 50L65 43L70 50" fill="none" stroke="#172033" stroke-width="2"/>')
 for x in [65,115,165,215,265,315,365]:
  t=t.replace(f'<text x="{x}" y="237"',f'<text x="{x}" y="130" style="paint-order:stroke;stroke:white;stroke-width:4px"')
 t=t.replace('<text x="342" y="266"','<text x="402" y="90"').replace('>Tid (s)</text>','>t (s)</text>');q['t']=t

# Samma axelfel i närliggande graf med negativa positioner.
 q=d['3.453'];t=q['t'];t=t.replace('M65 45V215H380','M65 45V224 M65 161.667H390')
 t=t.replace('<line x1="65" y1="161.667" x2="365" y2="161.667" stroke="#5c6878" stroke-dasharray="4 3"/>','<path d="M385 156.667L392 161.667L385 166.667 M60 50L65 43L70 50" fill="none" stroke="#172033" stroke-width="2"/>')
 for x in [65,115,165,215,265,315,365]:
  t=t.replace(f'<text x="{x}" y="237"',f'<text x="{x}" y="183" style="paint-order:stroke;stroke:white;stroke-width:4px"')
 t=t.replace('<text x="342" y="266"','<text x="402" y="146"').replace('>Tid (s)</text>','>t (s)</text>');q['t']=t

def ma2(b):
 d={q['id']:q for q in b}
 q=d['1.123'];q['t']=q['t'].replace('men ett värde är fel','men ett av funktionsvärdena i raden f(x) är fel');q['spelIntro']=re.sub(r'^<p>.*?</p>', '<p>Tabellen ska beskriva en linjär funktion. Ett funktionsvärde i raden f(x) är fel.</p>',q['spelIntro'])
 q['spelDelar'][0]['fraga']=r'<p>Vid \(x=2\) står det felaktiga funktionsvärdet 2. Vilket funktionsvärde ska stå där i stället?</p>'
 sa=sol([st(r'Linjär förändring: \(k=\Delta y/\Delta x\)',m(r'k=\frac{7-13}{-1-(-4)}=-2')+'<p>När x ökar med 3 minskar funktionsvärdet med 6. De tre övriga värdena 13, 7 och −5 passar detta mönster.</p>'),st('Rätta funktionsvärdet vid x = 2',m(r'7-6=1'))],'Funktionsvärdet vid x = 2 ska vara 1.')
 sb=sol([st(r'Skriv \(f(x)=kx+m\)',m(r'k=\frac{7-13}{-1-(-4)}=-2')),st(r'Punkten \((-1,7)\) bestämmer konstanttermen',m(r'\begin{aligned}7&=-2\cdot(-1)+m\\m&=5\end{aligned}'))],r'\(f(x)=-2x+5\).')
 q['spelDelar'][0]['s']=sa;q['spelDelar'][1]['s']=sb;q['s']=joined([sa,sb]);q['rättSvar']=[1,'-2*x+5'];q['svarFormat']=['numeriskt','uttryck']
 q=d['2.141'];q['t']=q['t'].replace(r'funktionen \(q\)',r'funktionen \(f\)').replace('c) Bestäm en möjlig funktionsformel.',r'c) Bestäm funktionens formel. Skriv svaret som \(f(x)=\ldots\).');q['spelIntro']=q['spelIntro'].replace(r'\(q\)',r'\(f\)');q['spelDelar'][2]['fraga']=r'<p>Bestäm funktionens formel. Skriv svaret som \(f(x)=\ldots\).</p>'
 # Samma funktion, endast konsekvent beteckning. Rättningen accepterar även y= och högerledet.
 for obj in [q,*q['spelDelar']]:
  for key in ['s','ledtrad']:
   if obj.get(key):obj[key]=obj[key].replace('q(x)','f(x)').replace('q(0)','f(0)')
 for id,idx in [('2.259',0),('2.629',1)]:
  q=d[id];q['svarFormat']=['faktoriserat','numeriskt'] if id=='2.259' else ['numeriskt','uttryck'];q['spelDelar'][idx]['svarFormat']=q['svarFormat'][idx]
 q=d['2.259'];a=sol([st(r'Nollställena ger \(f(x)=a(x-1)(x-6)\)','<p>Använd också den givna punkten på y-axeln.</p>'),st(r'Sätt in \(f(0)=-6\)',m(r'-6=a\cdot(-1)\cdot(-6)=6a')+m(r'a=-1'))],r'\(f(x)=-(x-1)(x-6)\).');bb=sol([st(r'Symmetrilinjen: \(x=\frac{1+6}{2}\)',m(r'x=3{,}5')),st('Beräkna värdet i parabelns topp',r'<p>Från a) har vi \(f(x)=-(x-1)(x-6)\). Koefficienten framför x² är negativ, så toppen ger största värdet.</p>'+m(r'f(3{,}5)=-2{,}5\cdot(-2{,}5)=6{,}25'))],'Det största värdet är 6,25.');q['spelDelar'][0]['s']=a;q['spelDelar'][1]['s']=bb;q['s']=joined([a,bb]);q['spelDelar'][1]['fraga']=r'<p>Funktionen är \(f(x)=-(x-1)(x-6)\). Bestäm dess största värde.</p>'
 q=d['2.629'];a=sol([st(r'Symmetrilinjen är \(x=3\)','<p>Nollställena ligger lika långt från symmetrilinjen.</p>'+m(r'3-(-1)=4')),st('Flytta lika långt åt höger',m(r'x=3+4=7'))],r'Det andra nollstället är \(x=7\).');bb=sol([st(r'Nollställena ger \(f(x)=a(x+1)(x-7)\)','<p>Det andra nollstället är 7 enligt symmetrin kring x = 3.</p>'),st(r'Sätt in \(f(0)=21/4\)',m(r'-7a=\frac{21}{4}\quad\Rightarrow\quad a=-\frac34')),st('Kontrollera det största värdet',m(r'f(3)=-\frac34\cdot4\cdot(-4)=12'))],r'\(f(x)=-\frac34(x+1)(x-7)\).');q['s']=joined([a,bb]);q['spelDelar'][0]['s']=a;q['spelDelar'][1]['s']=bb
 q=d['4.279'];q['s']=q['s'].replace(r'\bar x=\frac{3+7+8+12+x}{5}=\frac{30+x}{5}',r'\begin{aligned}\bar x&=\frac{3+7+8+12+x}{5}\\&=\frac{30+x}{5}\end{aligned}').replace(r'\frac{30+x}{5}=x\ \Rightarrow\ 4x=30\ \Rightarrow\ x=7{,}5',r'\begin{aligned}\frac{30+x}{5}&=x\\4x&=30\\x&=7{,}5\end{aligned}');q['t']=q['t'].replace('Bestäm alla värden','Bestäm exakt alla värden');q['svarFormat']=['numeriskt']*3
 q=d['4.273'];svg=re.search(r'<svg[\s\S]*?</svg>',q['t']).group();svg=re.sub(r'<line[^>]*stroke-dasharray="3 4"[^>]*/>','',svg);svg=re.sub(r'<text[^>]*>.*?</text>','',svg);labels=''.join(f'<text x="{50+(i-2)*460/18:.1f}" y="126" text-anchor="middle" font-family="Arial" font-size="15" fill="#24262b">{i}</text>' for i in range(2,21,2));svg=svg.replace('</svg>',labels+'</svg>');q['t']=re.sub(r'<svg[\s\S]*?</svg>',lambda _:svg,q['t'])
 q=d['4.2073'];table='<table class="data" style="width:100%;max-width:320px"><thead><tr><th scope="col">Månad</th><th scope="col">Antal besök</th></tr></thead><tbody>'+''.join(f'<tr><th scope="row">{month}</th><td style="white-space:nowrap;text-align:right">{n}</td></tr>' for month,n in zip(['Januari','Februari','Mars','April','Maj','Juni'],['2 400','2 100','2 600','2 300','2 900','3 500']))+'</tbody></table>';q['t']=re.sub(r'<table[\s\S]*?</table>',lambda _:table,q['t']);q['s']=q['s'].replace(r'2400+2100+2600+2300+2900+3500=15\,800',r'\begin{aligned}&2400+2100+2600\\&+2300+2900+3500=15\,800\end{aligned}').replace(r'\frac{4200}{15\,800+4200}=\frac{4200}{20\,000}=0{,}21=21\ \%',r'\begin{aligned}\frac{4200}{15\,800+4200}&=\frac{4200}{20\,000}\\&=0{,}21=21\ \%\end{aligned}')
 q=d['5.01'];q['t']=q['t'].replace('De rörliga kampanjkostnaderna är 2 500 kr för Bas och 4 000 kr för Plus. Beräkna hur mycket som återstår av faktureringen när dessa kostnader har dragits bort.','Kostnaden för att genomföra ett Bas-paket är 2 500 kr och ett Plus-paket 4 000 kr. Hur många kronor finns kvar av intäkterna när dessa kampanjkostnader betalats?');q['spelDelar'][2]['fraga']='<p>Det såldes 10 Bas-paket och 8 Plus-paket. Byrån fick in 176 000 kr. Kostnaden för att genomföra ett Bas-paket är 2 500 kr och ett Plus-paket 4 000 kr. Hur många kronor finns kvar av intäkterna när dessa kampanjkostnader betalats?</p>';q['spelDelar'][2]['ledtrad']='<p>Beräkna först den sammanlagda kostnaden för att genomföra de sålda kampanjerna. Dra den från intäkterna.</p>'
 # Uppgiften om antal svar använder en avgränsad ordnormalisering i appen.

def ma4(b):
 d={q['id']:q for q in b}
 q=d['2.52'];q['geogebra']=False;q.update(svarstyp='flera_delar',rättSvar=[2,1],svarFormat=['numeriskt']*2,svarsstruktur='ordnad',svarEtiketter=['a','b'],tolerans=[0,0]);q['s']=sol([st('Polynomdivision ger kvot och rest',m(r'\begin{aligned}f(x)&=ax+(a+b)\\&\quad+\frac{1+a+b}{x-1}\end{aligned}')),st('Restbråket går mot noll när x blir stort',r'<p>Den sneda asymptoten är därför \(y=ax+(a+b)\).</p>'),st(r'Jämför koefficienterna med \(y=2x+3\)',m(r'a=2,\quad a+b=3')+m(r'b=3-2=1'))],r'\(a=2\) och \(b=1\).');q['ledtrad']='<p>Polynomdividera täljaren med x−1. Vilka koefficienter måste kvoten ha för att ge den angivna asymptoten?</p>'
 q=d['4.539'];q['svarEnhet']='s';q['rättSvar']=28.9;q['tolerans']=0.000001;q['t']=r'<p>Tiden mellan två telefonsamtal till ett företag är exponentialfördelad. Om medeltiden är \(m\) sekunder ges sannolikheten för en väntetid längre än \(t\) sekunder av \(P(T&gt;t)=e^{-t/m}\).</p><p>Det är 50 % chans att tiden mellan två samtal är längre än 20 s. Bestäm medeltiden. (Svara i sekunder med en decimal.)</p>';q['s']=sol([st(r'Sätt in villkoret \(P(T&gt;20)=0{,}5\)',m(r'e^{-20/m}=0{,}5')),st(r'Logaritmlagen: \(\ln(e^u)=u\)',m(r'-\frac{20}{m}=\ln(0{,}5)=-\ln2')),st('Lös ut medeltiden',m(r'm=\frac{20}{\ln2}\approx28{,}9\ \mathrm{s}'))],'Medeltiden är cirka 28,9 s.');q['ledtrad']='<p>Sätt in den givna tiden och sannolikheten i sambandet. Vilken logaritm tar bort exponentialfunktionen?</p>'
 q=d['1.345'];q['t']=r'<p>Linjen \(y=a(x-2)\) tangerar kurvan \(y=\sin x\) i en punkt där \(0&lt;x&lt;2\pi\). Vinkeln x mäts i radianer.</p><p>Bestäm a och tangentpunktens x-koordinat. (Svara med tre decimaler; x i radianer.)</p>';q['svarEnhet']=['','rad'];q['ledtrad']='<p>I tangentpunkten är både linjens och kurvans y-värde lika, och deras lutningar lika. Använd radianer när du deriverar sinusfunktionen.</p>'
 q['s']=sol([st(r"Tangentens lutning: \((\sin x)'=\cos x\)",r'<p>Derivatan gäller när x mäts i radianer. Linjens lutning är a, så \(a=\cos x\).</p>'),st('Linjen och kurvan har samma värde i tangentpunkten',m(r'\sin x=a(x-2)')+m(r'\sin x=(x-2)\cos x')),st('Lös tangentvillkoret numeriskt',r'<p>Rita \(h(x)=\sin x-(x-2)\cos x\) i radianläge. Sök nollstället i intervallet \(0&lt;x&lt;2\pi\): \(x\approx4{,}302689\).</p>'),st('Sätt in x i uttrycket för lutningen',m(r'a=\cos(4{,}302689)\approx-0{,}398334'))],r'\(a\approx-0{,}398\) och \(x\approx4{,}303\) rad.')
 q=d['4.333'];q['t']=q['t'].replace('samtliga lösningar','samtliga reella lösningar');q['ledtrad']='<p>Flytta 2,5 till vänsterledet. Grafens skärningar med x-axeln visar de reella lösningarna.</p>';q.update(svarstyp='flera_delar',rättSvar=[-1.866,-.914,1.984],tolerans=[.0005]*3,självrättning=True,svarsstruktur='mängd',svarFormat=['numeriskt']*3);q['s']=sol([st(r'Samla termerna: \(x^5-4x^3+x-1{,}5=0\)',r'<p>Rita vänsterledet som en funktion. Vi söker de reella nollställena.</p>'),st('Läs av de tre skärningarna med x-axeln',m(r'\begin{aligned}x_1&\approx-1{,}865995\\x_2&\approx-0{,}913577\\x_3&\approx1{,}984442\end{aligned}')),st('Avrunda till tre decimaler','<p>Polynomet har även två icke-reella komplexa rötter, men frågan gäller endast reella lösningar.</p>')],r'\(x\approx-1{,}866\), \(x\approx-0{,}914\) eller \(x\approx1{,}984\).')


def pic(name,alt):return '<span class="fig"><img src="bilder/geogebra-'+name+'.png" alt="'+alt+'" style="width:100%;max-width:680px;height:auto"></span>'
def finalise(f,b):
 d={q['id']:q for q in b}
 if f=='uppgifterma2.js':
  q=d['5.28'];intro='<p>En butik uppskattar att den dagliga efterfrågan på en produkt är normalfördelad. Medelvärdet är 240 varor per dag och standardavvikelsen 35 varor.</p>'
  qa='<p>Butiken har 300 varor i lager när dagen börjar. Hur stor är sannolikheten att kunderna vill köpa fler varor än så under dagen? (Svara i procent.)</p>'
  qb='<p>Butiken vill att efterfrågan ska överstiga morgonlagret under högst 2,5 % av dagarna. Vilket är det minsta antal hela varor som ska finnas i lager på morgonen?</p>'
  qc='<p>Anta att risken för att efterfrågan överstiger lagret är 2,5 % varje dag. Under ungefär hur många av 250 försäljningsdagar överstiger efterfrågan lagret? (Avrunda till hela dagar.)</p>'
  menu='<p>Öppna geogebra.org/classic. Välj ☰ → Perspektiv → Sannolikhet och därefter Normalfördelning.</p>'+pic('sannolikhet-perspektiv','Meny, Perspektiv och Sannolikhet är markerade i GeoGebra.')
  sa=sol([st(r'Sök högersvansen \(P(X&gt;300)\)','<p>Slumpvariabeln X anger dagens efterfrågan. Lagret räcker inte när X är större än 300.</p>'),st('Öppna sannolikhetskalkylatorn',menu),st('Ange fördelningen och lagergränsen','<p>Skriv 240 i μ-fältet (1) och 35 i σ-fältet (2). Välj Öppet åt höger (3). Skriv 300 som nedre gräns (4). Andelen (5) blir cirka 0.0432. GeoGebra använder decimalpunkt.</p>'+pic('ma2-5-28-a','GeoGebra: medelvärde 240, standardavvikelse 35, högersvans över 300.')),st('Omvandla sannolikheten till procent',m(r'0{,}0432\cdot100\approx4{,}32\ \%'))],'Sannolikheten är cirka 4,32 %.')
  sb=sol([st(r'Sök gränsen L där \(P(X&gt;L)=0{,}025\)','<p>Vi söker ett lagervärde, inte andelen. 97,5 % ska ligga till vänster om gränsen.</p>'),st('Öppna sannolikhetskalkylatorn',menu),st('Låt GeoGebra bestämma gränsen','<p>Skriv μ = 240 (1) och σ = 35 (2). Välj Öppet åt höger (3). Skriv 0.025 i sannolikhetsfältet efter likhetstecknet (4) och tryck Enter. GeoGebra räknar baklänges och visar gränsen cirka 308.5987 (5). Punkt används som decimaltecken.</p>'+pic('ma2-5-28-b','GeoGebra räknar ut lagergränsen för högersvansen 0,025.')),st('Avrunda uppåt till ett helt antal varor','<p>Gränsen ligger mellan 308 och 309. Ett lager på 308 varor ger större risk än 2,5 %, medan 309 varor ger cirka 2,43 %. Därför behövs minst 309.</p>')],'Minst 309 varor.')
  sc=sol([st(r'Förväntat antal dagar: \(n=pN\)',m(r'n=0{,}025\cdot250=6{,}25')),st('Tolka och avrunda antalet dagar','<p>Det motsvarar ungefär 6 dagar. Det är en förväntan enligt modellen, ingen garanti för hur många dagar det faktiskt blir.</p>')],'Ungefär 6 dagar av 250.')
  q['spelIntro']=intro;q['t']=intro+''.join('<p>'+chr(97+i)+') '+t[3:] for i,t in enumerate([qa,qb,qc]))+'<p>Förklara också en begränsning med att använda normalfördelningsmodellen som enda underlag för lagerbeslut.</p>'
  for i,(t,ss) in enumerate(zip([qa,qb,qc],[sa,sb,sc])):q['spelDelar'][i]['fraga']=t;q['spelDelar'][i]['s']=ss
  q['s']=joined([sa,sb,sc])+'<p>Modellen kan missa exempelvis säsongsvariationer, kampanjer och plötsliga förändringar i efterfrågan.</p>'
  q['rättSvar']=[100*.5*math.erfc((300-240)/35/math.sqrt(2)),309,6];q['tolerans']=[.005,0,0]
  q['spelDelar'][0]['ledtrad']='<p>Vilken sida om lagergränsen motsvarar att varorna inte räcker?</p>'
  q['spelDelar'][1]['ledtrad']='<p>Sök en gräns som lämnar 2,5 % av normalfördelningen till höger. Fundera på hur gränsen ska avrundas till hela varor.</p>'
  q['spelDelar'][2]['ledtrad']='<p>Hur beräknar du 2,5 % av 250 dagar?</p>'
 if f=='uppgiftermato2.js':
  for id,slug,body in [('1.345','mato2-1-345',r'<p>Öppna GeoGebra Classic i grafritarläge. Skriv <code>h(x)=sin(x)-(x-2)*cos(x)</code> och därefter <code>A=Root(h,4,4.6)</code>. Funktionen använder radianer. Punktens x-koordinat ger tangentpunkten. Skriv <code>a=cos(x(A))</code> för lutningen. GeoGebra använder decimalpunkt.</p>'),('4.333','mato2-4-333',r'<p>Öppna GeoGebra Classic i grafritarläge. Skriv <code>p(x)=x^5-4*x^3+x-1.5</code>. Grafen skär x-axeln i tre punkter. Bestäm dem med <code>A=Root(p,-2,-1.5)</code>, <code>B=Root(p,-1.2,-0.5)</code> och <code>C=Root(p,1.5,2.2)</code>. Läs punkternas x-koordinater. GeoGebra använder decimalpunkt.</p>')]:
   q=d[id];s=q['s'];needle='<li><p class="facit-rubrik">'+('Sätt in x i uttrycket för lutningen' if id=='1.345' else 'Avrunda till tre decimaler')
   q['s']=s.replace(needle,st('Så gör du i GeoGebra',body+pic(slug,'GeoGebra visar inmatade funktioner, nollställen och deras koordinater.'))+needle)

if __name__=='__main__':
 for f,func in [('uppgifter.js',fy),('uppgifterma2.js',ma2),('uppgiftermato2.js',ma4)]:
  b=read(f);old={q['id']:json.loads(json.dumps(q)) for q in b};func(b);finalise(f,b);save(f,b,old)
