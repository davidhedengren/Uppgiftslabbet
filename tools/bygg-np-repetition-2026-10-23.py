"""Handskrivna repetitionsuppgifter. Ingen textimport eller mallbaserad talvariation.

Kör från valfri katalog. Befintliga uppgifter ändras inte; ID-kollision avbryter.
Ämnesval och källgranskning dokumenteras i agent/nationella-prov/.
"""
from pathlib import Path
import json, math, html

ROOT = Path(__file__).resolve().parents[1]
TITLE = 'Repetera inför Nationella provet'
AREA = 'np_repetition'
CFG = {'ma1': (8, ['1a','1b','1c']), 'ma2': (6, ['2a','2b','2c']),
       'mato1': (5, ['1b','1c']), 'mato2': (6, ['2c'])}
BANKS = {c: [] for c in CFG}
E = html.escape

def p(t): return '<p>'+t+'</p>'
def latex(t): return t.replace(r'\prime', "'").replace('<', r'\lt ').replace('>', r'\gt ')
def m(t): return r'\('+latex(t)+r'\)'
def mathline(t): return '<div class="facit-matte">'+r'\['+latex(t)+r'\]'+'</div>'
def solution(idea, calculation, answer):
    return '<div class="facit-v2"><p class="facit-rubrik"><strong>'+idea+'</strong></p>'+calculation+'<p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'

def svg(title, content, height=300):
    return '<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 '+str(height)+'" role="img" aria-label="'+E(title,quote=True)+'" style="width:100%;max-width:500px"><title>'+E(title)+'</title><rect width="500" height="'+str(height)+'" rx="12" fill="#fff"/>'+content+'</svg></span>'
def txt(x,y,s,anchor='middle',size=17):
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="#172e46">{E(str(s))}</text>'
def line(x1,y1,x2,y2,color='#334b63',width=2):
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" stroke-width="{width}"/>'
def table(headers,rows):
    return '<table style="border-collapse:collapse;width:100%;max-width:420px"><thead><tr>'+''.join('<th style="padding:7px;border:1px solid #8192a3">'+str(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td style="padding:7px;text-align:center;border:1px solid #8192a3">'+str(c)+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table>'
def plot(title, xr, yr, funcs=(), points=(), xlabel='x', ylabel='y', xticks=None, yticks=None):
    X=lambda x:65+370*(x-xr[0])/(xr[1]-xr[0]); Y=lambda y:245-200*(y-yr[0])/(yr[1]-yr[0])
    if xticks is None: xticks=[xr[0]+i*(xr[1]-xr[0])/4 for i in range(5)]
    if yticks is None: yticks=[yr[0]+i*(yr[1]-yr[0])/4 for i in range(5)]
    bits=[]
    for x in xticks: bits.extend([line(X(x),45,X(x),245,'#d9e2eb',1),txt(X(x),269,f'{x:g}')])
    for y in yticks: bits.extend([line(65,Y(y),435,Y(y),'#d9e2eb',1),txt(55,Y(y)+5,f'{y:g}','end')])
    bits.extend([line(65,Y(max(yr[0],min(0,yr[1]))),445,Y(max(yr[0],min(0,yr[1])))),line(X(max(xr[0],min(0,xr[1]))),245,X(max(xr[0],min(0,xr[1]))),35),txt(440,292,xlabel,'end'),txt(65,24,ylabel,'start')])
    for fn,color in funcs:
        path=[]; prev=False
        for i in range(241):
            x=xr[0]+(xr[1]-xr[0])*i/240
            try:y=fn(x)
            except (ValueError,ZeroDivisionError):prev=False;continue
            if not math.isfinite(y) or not yr[0]<=y<=yr[1]:prev=False;continue
            path.append(('L' if prev else 'M')+f'{X(x):.3f} {Y(y):.3f}');prev=True
        bits.append('<path d="'+' '.join(path)+'" fill="none" stroke="'+color+'" stroke-width="3"/>')
    for x,y,label in points:
        bits.append(f'<circle cx="{X(x):.3f}" cy="{Y(y):.3f}" r="4" fill="#af3451"/>')
        if label:
            bits.append(f'<rect x="{X(x)+5:.3f}" y="{Y(y)-27:.3f}" width="{len(label)*12+10}" height="21" fill="#fff"/>')
            bits.append(txt(X(x)+8,Y(y)-10,label,'start'))
    return svg(title,''.join(bits))
def rectangle(title, a, b, wall=False):
    s='<rect x="105" y="65" width="290" height="145" fill="#e8f3f8" stroke="#24435e" stroke-width="3"/>'
    s+=txt(250,238,a)+txt(410,145,b,'start',15)
    if wall:s+=line(80,65,420,65,'#596777',9)+txt(250,40,'Vägg')
    return svg(title,s,260)
def triangle(title, base, side, angle=None):
    s='<path d="M85 235L405 235L405 85.782Z" fill="#e8f3f8" stroke="#24435e" stroke-width="3"/>'
    s+='<path d="M389 235V219H405" fill="none" stroke="#24435e" stroke-width="2"/>'
    s+=txt(245,265,base)+txt(420,155,side,'start')
    if angle:s+='<path d="M125 235 A40 40 0 0 0 121.252 218.095" fill="none" stroke="#b24d17" stroke-width="2"/>'+txt(175,226,angle)
    return svg(title,s)

def add(course, family, level, question, answer, explanation, hint, *, tracks=None, fmt=None, unit=None, calc=True, geo=False, fig='', labels=None, ordered=True, options=None, ability='procedur', topic=None, source=None):
    kap,default=CFG[course]; idx=len(BANKS[course])+1
    if fmt is None:fmt='numeriskt' if isinstance(answer,(float,int)) else 'uttryck'
    q={'id':f'{kap}.{idx:02d}','kap':kap,'omr':AREA,'kurs':tracks or default,
       'niva':'E' if level<=2 else 'C' if level<=4 else 'A','poang':'1/0/0' if level<=2 else '0/1/0' if level<=4 else '0/0/1',
       'familj':family,'formaga':[ability],'traningsniva':level,'arbetsinsats':min(4,max(1,level)),
       'miniräknare':calc,'geogebra':geo,'spel':True,'självrättning':True,
       't':question+fig,'s':explanation,'ledtrad':p(hint),'rättSvar':answer,'svarFormat':fmt,
       'svarstyp':'numeriskt' if fmt=='numeriskt' else 'uttryck','tolerans':1e-9 if fmt=='numeriskt' else 0,
       'repetition':{'typ':'egen','omgang':'2026-10-23','amnesplan':topic or family,
                     'underlag':source or {'ma1':'Ma1a/b/c VT22, delprov B','ma2':'Ma2a/b/c VT22','mato1':'Ma3b/c VT22','mato2':'Ma4 VT22'}[course]}}
    if unit:q['svarEnhet']=unit
    if isinstance(answer,list):
        q.update(svarstyp='flera_delar',svarsstruktur='ordnad' if ordered else 'mängd',svarEtiketter=labels or ['Svar '+str(i+1) for i in range(len(answer))],svarFormat=fmt if isinstance(fmt,list) else [fmt]*len(answer),tolerans=[1e-9]*len(answer))
    if options:
        q.update(svarstyp='alternativ',rättSvar=None,svarFormat='text',alternativ=[{'txt':t,'ratt':ok} for t,ok in options],tolerans=None)
    BANKS[course].append(q)
    return q

# Matematik nivå 1: kontext, representation och metodval varierar avsiktligt.
add('ma1','Procent och modeller',1,p('En ryggsäck kostar 275 kr. Priset sänks med 12 %. Vad kostar den efter sänkningen? (Svara i kr.)'),242,
    solution('Det nya priset är 88 % av det gamla.',mathline(r'275\cdot0{,}88=242'),'242 kr.'),'Vilken andel av priset återstår?',unit='kr')
add('ma1','Funktioner och grafer',1,p('En tank innehåller '+m(r'V(t)=24+3t')+' liter vatten efter '+m(r't')+' minuter. Hur mycket vatten finns i tanken efter 6 minuter? (Svara i liter.)'),42,
    solution('Sätt in tiden i modellen.',mathline(r'V(6)=24+3\cdot6=42'),'42 liter.'),'Ersätt t med den angivna tiden.',unit='l',fig=rectangle('Tank med inflöde','24 liter från början','+3 l/min'))
add('ma1','Algebra och ekvationer',2,p('Förenkla uttrycket '+m(r'4(2x-3)-3(x+2)')+' så att det inte innehåller några parenteser.'),'5*x-18',
    solution('Multiplicera in och samla lika termer.',mathline(r'8x-12-3x-6=5x-18'),m(r'5x-18')+'.'),'Minustecknet framför den andra parentesen påverkar båda termerna.',calc=False)
add('ma1','Algebra och ekvationer',2,p('En verkstad köper två likadana förvaringslådor. Frakten är 35 kr och hela beställningen kostar 185 kr. Vad kostar en låda? (Svara i kr.)'),75,
    solution('Ta bort frakten innan kostnaden delas.',mathline(r'2x+35=185')+mathline(r'x=\frac{185-35}{2}=75'),'75 kr.'),'Vilken del av totalsumman gäller själva lådorna?',unit='kr')
add('ma1','Funktioner och grafer',1,p('Grafen visar funktionen '+m(r'f')+'. Läs av '+m(r'f(3)')+'.'),7,
    solution('Gå från x-värdet till grafen.',p('Vid '+m(r'x=3')+' ligger grafen på höjden '+m(r'y=7')+'.'),m(r'f(3)=7')+'.'),'Funktionsvärdet är grafens höjd vid det givna x-värdet.',fig=plot('En linjär funktion i ett rutnät',(0,4),(0,10),[(lambda x:2*x+1,'#146a96')],xticks=list(range(5)),yticks=list(range(0,11,2))))
add('ma1','Procent och modeller',2,p('En batterimodell anger att den lagrade energin minskar med 4 % varje timme. Från början är energin 850 Wh. Hur mycket återstår efter tre timmar? (Svara i Wh.)'),850*.96**3,
    solution('Samma förändringsfaktor används tre gånger.',mathline(r'850\cdot0{,}96^3=752{,}0256'),'Ungefär 752 Wh.'),'Minskningen beräknas på den energi som finns kvar varje timme.',unit='Wh')
add('ma1','Procent och modeller',2,p('En cykelhjälm kostar 720 kr under en rea med 20 % rabatt. Vad var priset före rean? (Svara i kr.)'),900,
    solution('Reapriset motsvarar 80 % av ursprungspriset.',mathline(r'0{,}80x=720')+mathline(r'x=720/0{,}80=900'),'900 kr.'),'Vilket pris är det som procenttalet räknas på?',unit='kr')
add('ma1','Sannolikhet och granskning',3,p('Risken att en viss leverans blir försenad är 8 %. Tre leveranser görs oberoende av varandra. Hur stor är sannolikheten att minst en blir försenad? (Svara i procent.)'),100*(1-.92**3),
    solution('Beräkna först sannolikheten att alla kommer i tid.',mathline(r'P(\text{alla i tid})=0{,}92^3')+mathline(r'P(\text{minst en sen})=1-0{,}92^3'),r'Ungefär 22,1 %.'),'Vilken händelse är motsatsen till att minst en leverans blir sen?',unit='%',ability='problemlösning')
add('ma1','Sannolikhet och granskning',2,p('I en låda finns två röda och tre blå brickor. Två brickor tas utan återläggning. Hur stor är sannolikheten att båda är röda? (Svara som bråk eller decimaltal.)'),.1,
    solution('Antalet brickor ändras efter det första valet.',mathline(r'\frac25\cdot\frac14=\frac1{10}=0{,}1'),m(r'1/10')+'.'),'Hur många röda brickor och hur många brickor totalt finns kvar efter en röd?',fig=svg('Två röda och tre blå brickor',''.join(f'<circle cx="{90+i*80}" cy="65" r="25" fill="{c}"/>'+txt(90+i*80,112,l) for i,(c,l) in enumerate([('#ba344e','R'),('#ba344e','R'),('#146a96','B'),('#146a96','B'),('#146a96','B')])),135))
add('ma1','Funktioner och grafer',1,p('Ett abonnemang kostar 90 kr per månad plus 12 kr för varje extra gigabyte. Vilken modell ger månadskostnaden '+m(r'K')+' för '+m(r'x')+' extra gigabyte? Välj ett alternativ.'),None,
    solution('Skilj på fast och rörlig kostnad.',p('De 90 kronorna betalas en gång. Varje extra gigabyte bidrar med 12 kr.'),m(r'K=90+12x')+'.'),'Vilken kostnad finns även när x är noll?',options=[(m(r'K=102x'),False),(m(r'K=90+12x'),True),(m(r'K=12+90x'),False),(m(r'K=90\cdot1{,}12^x'),False)],ability='modellering')
add('ma1','Procent och modeller',2,p('Tabellen visar ett prisindex. Hur många procent steg priset från 2023 till 2025?')+table(['År','Index'],[[2023,160],[2025,178]])+p('(Svara i procent.)'),11.25,
    solution('Jämför ökningen med startårets index.',mathline(r'\frac{178-160}{160}\cdot100=11{,}25'),'11,25 %.'),'År 2023 är jämförelseåret i just den här frågan.',tracks=['1b'],unit='%',topic='Begreppet index')
add('ma1','Geometri och vektorer',2,p('En rak ramp har en horisontell längd på 8,0 m och lutar 25° mot marken. Hur stor är höjdskillnaden mellan rampens ändar? (Svara i m.)'),8*math.tan(math.radians(25)),
    solution('Höjden och marksträckan är kateter.',mathline(r'\tan25^\circ=\frac{h}{8{,}0}')+mathline(r'h=8{,}0\tan25^\circ\approx3{,}73'),'Ungefär 3,73 m.'),'Vilka två sidor jämför tangens?',tracks=['1a','1c'],unit='m',fig=triangle('Ramp, marksträcka och höjd; schematisk figur','8,0 m','h','25°'),topic='Trigonometri i rätvinkliga trianglar; yrkesrelevant geometri för 1a')
add('ma1','Geometri och vektorer',2,p('En robot förflyttas först med vektorn '+m(r'(4,-1)')+' m och sedan med '+m(r'(-2,5)')+' m. Hur långt är det rakt mellan startpunkten och slutpunkten? (Svara i m.)'),math.sqrt(20),
    solution('Addera förflyttningarna före längdberäkningen.',mathline(r'(4,-1)+(-2,5)=(2,4)')+mathline(r'd=\sqrt{2^2+4^2}=\sqrt{20}'),m(r'2\sqrt5')+' m, ungefär 4,47 m.'),'Den sammanlagda förflyttningen är inte summan av de två vägarnas längder.',tracks=['1c'],unit='m',fig=plot('Robotens start, mellanstopp och slutpunkt',(-1,5),(-2,5),points=[(0,0,'Start'),(4,-1,'Stopp'),(2,4,'Slut')],xticks=list(range(-1,6)),yticks=[-2,0,2,4]),topic='Addition och absolutbelopp av vektorer')
add('ma1','Algebra och ekvationer',2,p('Det kostar 95 kr att hämta ut en hyrvagn och sedan 18 kr per hel timme. Du får använda högst 240 kr. Hur många hela timmar kan du som mest hyra vagnen?'),8,
    solution('Hitta gränsen och kontrollera hela timmar.',mathline(r'95+18t\le240')+mathline(r't\le145/18\approx8{,}06')+p('Åtta timmar kostar 239 kr. Nio timmar kostar 257 kr och är för dyrt.'),'8 timmar.'),'Räkna först bort den fasta avgiften.',ability='problemlösning')
add('ma1','Funktioner och grafer',3,p('En förening betalar en fast avgift och samma pris per deltagare för en aktivitet. Tabellen visar två bokningar. Vad är priset per deltagare? (Svara i kr.)')+table(['Deltagare','Total kostnad'],[[4,'620 kr'],[7,'935 kr']]),105,
    solution('Den fasta avgiften försvinner när bokningarna jämförs.',mathline(r'\frac{935-620}{7-4}=105'),'105 kr per deltagare.'),'Vad kostar de tre extra deltagarna tillsammans?',unit='kr',ability='modellering')
add('ma1','Procent och modeller',2,p('Priset på en biljett sänks med 10 % och höjs senare med 20 %. Hur många procent högre är slutpriset än priset före båda ändringarna?'),8,
    solution('Multiplicera förändringsfaktorerna.',mathline(r'0{,}90\cdot1{,}20=1{,}08')+p('Faktorn 1,08 betyder att 108 % av ursprungspriset återstår.'),'8 % högre.'),'Den andra förändringen räknas på det redan sänkta priset.',unit='%')
add('ma1','Sannolikhet och granskning',2,p('En enkät visar att elever som cyklar till skolan i genomsnitt sover längre. Vilken slutsats stöds av enkäten? Välj ett alternativ.'),None,
    solution('Ett samband visar inte i sig vad som orsakar det.',p('Andra skillnader mellan grupperna kan påverka både resvanor och sömn.'),'Det finns ett samband i de undersökta svaren, men orsaken är inte visad.'),'Skilj på samband och orsak.',options=[('Cykling gör att alla elever sover längre.',False),('Mer sömn gör alltid att elever börjar cykla.',False),('Resvanor och sömn kan aldrig hänga ihop.',False),('Det finns ett samband i svaren, men orsaken är inte visad.',True)],ability='resonemang')
add('ma1','Algebra och ekvationer',3,p('Två vänner delar lika på en avgift och betalar 210 kr var. Om ytterligare en vän hade varit med skulle samma avgift ha delats lika på tre. Hur mycket mindre skulle var och en då ha betalat? (Svara i kr.)'),70,
    solution('Den sammanlagda avgiften är oförändrad.',mathline(r'2\cdot210=420')+mathline(r'420/3=140')+mathline(r'210-140=70'),'70 kr mindre.'),'Bestäm hela avgiften innan du ändrar antalet personer.',unit='kr',ability='problemlösning')
add('ma1','Funktioner och grafer',3,p('Två modeller används för mängden material i ett lager. Vilket påstående stämmer med tabellen? Välj ett alternativ.')+table(['Vecka','Modell A (ton)','Modell B (ton)'],[[0,100,100],[1,90,90],[2,80,81],[3,70,'72,9']]),None,
    solution('Jämför skillnader respektive kvoter.',p('A minskar med 10 ton per vecka. B multipliceras med 0,90 varje vecka.'),'A är linjär och B är exponentiell.'),'Är förändringen lika stor i ton eller i procent?',options=[('Båda är linjära.',False),('A är exponentiell och B är linjär.',False),('A är linjär och B är exponentiell.',True),('Båda är exponentiella.',False)],ability='begrepp')
add('ma1','Algebra och ekvationer',4,p('Ett kvadratiskt mönster består av '+m(r'n\times n')+' vita plattor. Runt det läggs en ram som är en platta bred, även vid hörnen. Skriv ett förenklat uttryck för antalet plattor i ramen.'),'4*n+4',
    solution('Ta bort den vita kvadraten från den större kvadraten.',mathline(r'(n+2)^2-n^2')+mathline(r'=n^2+4n+4-n^2=4n+4'),m(r'4n+4')+' plattor.'),'Hur lång blir sidan om ramen räknas med på båda sidor?',calc=False,ability='problemlösning',fig=svg('En kvadrat med en ram som är en platta bred','<rect x="130" y="25" width="240" height="240" fill="#a7ccdf" stroke="#24435e" stroke-width="2"/><rect x="170" y="65" width="160" height="160" fill="white" stroke="#24435e" stroke-width="2"/>'+txt(250,145,'n × n')+txt(390,150,'1 platta','start',15)))

# Matematik nivå 2. Statistik använder Sx; rotekvationer begränsas till 2c.
add('ma2','Algebra och ekvationer',1,p('Lös ekvationen '+m(r'x^2=49')+'. Ange båda lösningarna i var sitt svarsfält.'),[-7,7],
    solution('Både ett positivt och ett negativt tal kan ge samma kvadrat.',mathline(r'7^2=49\quad\text{och}\quad(-7)^2=49'),m(r'x=-7')+' eller '+m(r'x=7')+'.'),'Glöm inte den negativa lösningen.',fmt='numeriskt',ordered=False,calc=False)
add('ma2','Algebra och ekvationer',1,p('Skriv '+m(r'x^2-6x+9')+' som en produkt av förstagradsfaktorer.'),'(x-3)^2',
    solution('Känn igen en kvadrat.',mathline(r'x^2-6x+9=x^2-2\cdot3x+3^2')+mathline(r'=(x-3)^2'),m(r'(x-3)^2')+'.'),'Vilket tal ger både mittentermen och konstanttermen?',fmt='faktoriserat',calc=False)
add('ma2','Funktioner och modeller',1,p('Grafen visar en andragradsfunktion. Vilket '+m(r'x')+'-värde ger funktionens minsta värde?'),2,
    solution('Sök grafens lägsta punkt.',p('Lägsta punkten ligger vid '+m(r'x=2')+'. Frågan gäller x-koordinaten, inte höjden −4.'),m(r'x=2')+'.'),'Läs av den vågräta koordinaten för den lägsta punkten.',fig=plot('Parabel i ett koordinatsystem',(-1,5),(-5,5),[(lambda x:(x-2)**2-4,'#146a96')],xticks=list(range(-1,6)),yticks=[-4,-2,0,2,4]))
add('ma2','Algebra och ekvationer',2,p('I ett förråd står sammanlagt 17 tvåhjuliga cyklar och trehjuliga cyklar. De har tillsammans 42 hjul. Hur många finns det av varje sort?'),[9,8],
    solution('Använd både antalet cyklar och antalet hjul.',mathline(r'x+y=17,\qquad2x+3y=42')+p('Dubbla den första ekvationen och jämför med den andra:')+mathline(r'y=42-34=8,\qquad x=17-8=9'),'9 tvåhjuliga och 8 trehjuliga cyklar.'),'Två uppgifter om samma förråd ger två ekvationer.',fmt='numeriskt',labels=['Tvåhjuliga cyklar','Trehjuliga cyklar'],ability='modellering')
add('ma2','Funktioner och modeller',2,p('En maskins värde beskrivs av '+m(r'V(t)=18000\cdot0{,}92^t')+', där '+m(r't')+' är antal år efter inköpet och '+m(r'V')+' mäts i kr. När har värdet halverats? (Svara i år.)'),math.log(.5)/math.log(.92),
    solution('Halva startvärdet är 9 000 kr.',mathline(r'18000\cdot0{,}92^t=9000')+p('Ekvationens lösning med digitalt verktyg är '+m(r't\approx8{,}31')+'.'),r'Ungefär 8,31 år.'),'Bestäm vilket funktionsvärde som motsvarar halva startvärdet.',unit='år',geo=True,topic='Digital lösning av exponentialekvation; 2b/c även logaritmer')
add('ma2','Algebra och ekvationer',2,p('Skriv '+m(r'\lg 2+\lg 7')+' som en enda tiologaritm.'),'lg(14)',
    solution('En summa av logaritmer blir logaritmen av en produkt.',mathline(r'\lg2+\lg7=\lg(2\cdot7)=\lg14'),m(r'\lg14')+'.'),'Använd logaritmlagen för en produkt.',tracks=['2b','2c'],calc=False,fmt='en_logaritm',topic='Logaritmlagar')
iso=svg('Likbent triangel ABC med lika sidor AB och AC','<path d="M168.396 240L250 65L331.604 240Z" fill="#e8f3f8" stroke="#24435e" stroke-width="3"/>'+txt(250,42,'A')+txt(150,258,'B')+txt(350,258,'C')+'<path d="M233.095 101.252A40 40 0 0 0 266.905 101.252" fill="none" stroke="#b65d14" stroke-width="2"/>'+txt(250,132,'50°')+line(203,152,217,159)+line(283,159,297,152)+txt(250,285,'AB = AC'))
add('ma2','Geometri och samband',1,p('Triangeln är likbent med '+m(r'AB=AC')+'. Vinkeln vid A är 50°. Hur stor är vinkeln vid B? (Svara i grader.)'),65,
    solution('De två basvinklarna är lika stora.',mathline(r'B=C=\frac{180^\circ-50^\circ}{2}=65^\circ'),'65°.'),'Hur stor vinkelsumma återstår till de två lika vinklarna?',tracks=['2b','2c'],unit='°',fig=iso,topic='Vinklar i likbent triangel')
shadow=svg('Två lodräta föremål med skuggor; solstrålarna är parallella',line(45,230,480,230)+line(75,230,75,166,'#146a96',4)+line(250,230,250,86,'#146a96',4)+line(75,166,171,230,'#b77323')+line(250,86,466,230,'#b77323')+txt(68,190,'1,6 m','end',15)+txt(123,259,'2,4 m')+txt(358,259,'5,4 m')+txt(232,140,'h','end'))
add('ma2','Geometri och samband',2,p('En 1,6 m hög stolpe har en 2,4 m lång skugga. Samtidigt har ett träd en 5,4 m lång skugga på samma plana mark. Hur högt är trädet? (Svara i m.)'),3.6,
    solution('Solstrålarna ger likformiga trianglar.',mathline(r'\frac{h}{5{,}4}=\frac{1{,}6}{2{,}4}')+mathline(r'h=5{,}4\cdot\frac{1{,}6}{2{,}4}=3{,}6'),'3,6 m.'),'Förhållandet mellan höjd och skugga är detsamma.',tracks=['2b','2c'],unit='m',fig=shadow,topic='Likformighet')
add('ma2','Statistik och tolkning',2,p('Tabellen visar väntetider för fyra samtal. Bestäm standardavvikelsen Sx. (Svara i minuter.)')+table(['Samtal','Väntetid (min)'],[['A',4],['B',6],['C',6],['D',8]]),math.sqrt(8/3),
    solution('Beräkna Sx för alla fyra observationerna.',p('Medelvärdet är 6 minuter. De kvadrerade avvikelserna är 4, 0, 0 och 4. Deras summa är 8.')+mathline(r'S_x=\sqrt{\frac{8}{4-1}}=\sqrt{8/3}')+mathline(r'S_x\approx1{,}63'),'Ungefär 1,63 minuter.'),'Använd statistikfunktionen och välj stickprovsstandardavvikelsen Sx.',unit='min',geo=True,topic='Digital beräkning av standardavvikelse Sx')
add('ma2','Statistik och tolkning',1,p('En produkts livslängd är normalfördelad med medelvärdet 60 månader och standardavvikelsen 4 månader. Ungefär hur många procent har en livslängd mellan 56 och 64 månader?'),100*math.erf(1/math.sqrt(2)),
    solution('Gränserna ligger en standardavvikelse från medelvärdet.',p('I en normalfördelning ligger ungefär 68 % inom en standardavvikelse från medelvärdet.'),'Ungefär 68 %.'),'Hur långt från medelvärdet ligger de två gränserna?',unit='%',fig=plot('Normalfördelning centrerad vid 60 månader',(48,72),(0,.12),[(lambda x:math.exp(-.5*((x-60)/4)**2)/(4*math.sqrt(2*math.pi)),'#146a96')],xlabel='Månader',ylabel='Täthet',xticks=[48,52,56,60,64,68,72],yticks=[]),topic='Normalfördelning med given standardavvikelse')
box=svg('Lådagram med skala för leveranstid',line(70,120,430,120)+line(70,100,70,140)+line(430,100,430,140)+'<rect x="150" y="90" width="160" height="60" fill="#c9e5ef" stroke="#24435e" stroke-width="3"/>'+line(230,90,230,150)+line(50,200,450,200)+''.join(line(70+i*40,195,70+i*40,205)+txt(70+i*40,230,10+2*i) for i in range(10))+txt(250,270,'Leveranstid (dagar)'))
add('ma2','Statistik och tolkning',1,p('Lådagrammet visar leveranstider. Hur stort är kvartilavståndet? (Svara i dagar.)'),8,
    solution('Kvartilerna ligger vid lådans kanter.',mathline(r'Q_1=14,\qquad Q_3=22')+mathline(r'Q_3-Q_1=22-14=8'),'8 dagar.'),'Lådans bredd motsvarar kvartilavståndet.',unit='dagar',fig=box,topic='Kvartiler och spridningsmått')
add('ma2','Funktioner och modeller',3,p('En rektangel har omkretsen 36 cm. Den ena sidan är '+m(r'x')+' cm. Vilket värde på '+m(r'x')+' ger störst area? (Svara i cm.)'),9,
    solution('Skriv arean som en andragradsfunktion.',p('Sidorna har summan 18 cm, så den andra sidan är '+m(r'18-x')+'.')+mathline(r'A(x)=x(18-x)=81-(x-9)^2')+p('Kvadraten är minst när x = 9; då är arean störst.'),'9 cm.'),'Omkretsen ger ett samband mellan sidorna.',unit='cm',ability='problemlösning',fig=rectangle('Rektangel med omkrets 36 cm','x cm','y cm'))
add('ma2','Algebra och ekvationer',3,p('Lös ekvationen '+m(r'\sqrt{x+6}=x')+'.'),3,
    solution('Kvadrera och pröva sedan kandidaterna i ursprungsekvationen.',mathline(r'x+6=x^2')+mathline(r'(x-3)(x+2)=0')+p('Kandidaterna är 3 och −2. För x = 3 är båda leden 3. För x = −2 blir vänsterledet 2 och högerledet −2.') ,'Endast '+m(r'x=3')+'.'),'En kvadratrot kan inte vara negativ.',tracks=['2c'],calc=False,topic='Rotekvationer och extralösningar')
add('ma2','Algebra och ekvationer',3,p('Vilket värde ska '+m(r'k')+' ha för att '+m(r'x^2-8x+k=0')+' ska ha exakt en reell lösning?'),16,
    solution('Skriv vänsterledet med en kvadrat.',mathline(r'(x-4)^2+k-16=0')+p('En enda reell lösning fås när kvadraten måste vara noll. Därför ska '+m(r'k-16=0')+'.'),m(r'k=16')+'.'),'När sammanfaller de två rötterna?',calc=False,ability='begrepp')
add('ma2','Geometri och samband',2,p('Punkten '+m(r'M=(4,2)')+' är mittpunkt på sträckan AB. Punkten '+m(r'A=(1,-3)')+'. Bestäm koordinaterna för B.'),[7,7],
    solution('Gå lika långt från M som du gick från A till M.',mathline(r'\overrightarrow{AM}=(4-1,2-(-3))=(3,5)')+mathline(r'B=(4+3,2+5)=(7,7)'),m(r'B=(7,7)')+'.'),'Mittpunkten delar sträckan i två lika långa delar.',fmt='numeriskt',labels=['B:s x-koordinat','B:s y-koordinat'],tracks=['2b','2c'],fig=plot('Punkterna A och M i ett rutnät',(0,8),(-4,8),points=[(1,-3,'A'),(4,2,'M')],xticks=[0,2,4,6,8],yticks=[-4,-2,0,2,4,6,8]),topic='Koordinatgeometri och mittpunkt')
add('ma2','Funktioner och modeller',3,p('En andragradsfunktion har nollställena 2 och 8. Dess graf går genom '+m(r'(0,32)')+'. Bestäm '+m(r'f(5)')+'.'),-18,
    solution('Använd nollställena och bestäm sedan skalfaktorn.',mathline(r'f(x)=a(x-2)(x-8)')+mathline(r'32=a(-2)(-8)\Rightarrow a=2')+mathline(r'f(5)=2\cdot3\cdot(-3)=-18'),m(r'f(5)=-18')+'.'),'Hur skrivs en andragradsfunktion när nollställena är kända?',ability='problemlösning')
add('ma2','Statistik och tolkning',2,p('Anpassa en rät linje till tabellens mätvärden med linjär regression. Använd linjen för att uppskatta '+m(r'y')+' när '+m(r'x=5')+'.')+table(['x','y'],[[1,3],[2,6],[3,7],[4,10]]),12,
    solution('Regressionslinjen använder samtliga mätpunkter.',p('Digital linjär regression ger '+m(r'y=2{,}2x+1')+'.')+mathline(r'y(5)=2{,}2\cdot5+1=12'),'12.'),'Välj linjär regression, inte en linje genom bara två av punkterna.',tracks=['2b','2c'],geo=True,topic='Digital linjär regression')
add('ma2','Statistik och tolkning',2,p('Fem mätvärden är 10, 11, 12, 13 och 14. Det största värdet ändras till 54. Vilket påstående stämmer? Välj ett alternativ.'),None,
    solution('Jämför summan och det mittersta värdet.',p('Summan ökar med 40, så medelvärdet ökar med '+m(r'40/5=8')+'. Det mittersta värdet är fortfarande 12.'),'Medelvärdet ökar med 8 och medianen är oförändrad.'),'Vilket av måtten påverkas av alla värden?',options=[('Både medelvärdet och medianen ökar med 8.',False),('Medelvärdet ökar med 8 och medianen är oförändrad.',True),('Medianen ökar med 40 och medelvärdet är oförändrat.',False),('Båda måtten är oförändrade.',False)],ability='begrepp',fig=table(['Mätning',1,2,3,4,5], [['Före',10,11,12,13,14],['Efter',10,11,12,13,54]]),topic='Medelvärde och median')
add('ma2','Geometri och samband',4,p('En rektangulär yta är 24 m lång och 18 m bred. En gång med samma bredd längs alla fyra kanter lämnar 280 m² kvar i mitten. Hur bred är gången? (Svara i m.)'),2,
    solution('Gången tar plats på två sidor i varje riktning.',mathline(r'(24-2x)(18-2x)=280')+mathline(r'x^2-21x+38=0')+mathline(r'(x-2)(x-19)=0')+p('x = 19 fungerar inte som bredd, eftersom x måste vara mindre än 9 m. Kontroll: '+m(r'20\cdot14=280')+'.'),'2 m.'),'Skriv längd och bredd för den inre rektangeln.',unit='m',ability='problemlösning',fig=svg('Rektangulär yta med en lika bred gång längs kanterna','<rect x="80" y="45" width="340" height="210" fill="#c9d4df" stroke="#24435e" stroke-width="3"/><rect x="115" y="80" width="270" height="140" fill="#e6f4e1" stroke="#24435e" stroke-width="2"/>'+txt(250,30,'24 m')+txt(460,160,'18 m')+txt(250,155,'280 m²')+txt(98,155,'x')))
add('ma2','Funktioner och modeller',5,p('Linjen '+m(r'y=kx+1')+' ska ha exakt en gemensam punkt med parabeln '+m(r'y=x^2+10')+'. Bestäm alla möjliga värden på '+m(r'k')+'. Ange dem i var sitt fält.'),[-6,6],
    solution('En gemensam punkt betyder en dubbelrot.',mathline(r'x^2-kx+9=0')+mathline(r'\left(x-\frac{k}{2}\right)^2=\frac{k^2}{4}-9')+p('Högerledet måste vara noll för att det ska finnas exakt ett x-värde.')+mathline(r'k^2=36\Rightarrow k=\pm6'),m(r'k=-6')+' eller '+m(r'k=6')+'.'),'Sätt funktionernas värden lika och undersök antalet lösningar.',fmt='numeriskt',ordered=False,calc=False,ability='problemlösning')

# Matematik – fortsättning nivå 1, gemensamt samt särskilda b/c-tillämpningar.
add('mato1','Derivata och förändring',1,p('Bestäm derivatan till '+m(r'f(x)=4x^3-5x')+'.'),'12*x^2-5',
    solution('Derivera varje term.',mathline(r'f\prime(x)=4\cdot3x^2-5=12x^2-5'),m(r'f\prime(x)=12x^2-5')+'.'),'Potensens exponent minskar med ett vid derivering.',calc=False)
add('mato1','Integraler och area',1,p('Ange en primitiv funktion till '+m(r'f(x)=6x^2-4x')+'.'),'2*x^3-2*x^2',
    solution('Välj termer som ger rätt derivata.',mathline(r'F(x)=2x^3-2x^2')+p('Kontroll: '+m(r'F\prime(x)=6x^2-4x')+'.'),r'Till exempel '+m(r'F(x)=2x^3-2x^2')+'. En valfri konstant kan läggas till.'),'Kontrollera ditt förslag genom att derivera det.',fmt='primitiv',calc=False)
add('mato1','Derivata och förändring',1,p('Tabellen visar mängden vatten i en tank. Bestäm den genomsnittliga förändringen per minut mellan mätningarna. (Svara i l/min, med tecken.)')+table(['Tid (min)','Volym (l)'],[[2,80],[8,50]]),-5,
    solution('Dela volymändringen med tidsändringen.',mathline(r'\frac{50-80}{8-2}=\frac{-30}{6}=-5'),'−5 l/min.'),'En minskning ska ge en negativ förändringshastighet.',unit='l/min')
add('mato1','Derivata och förändring',1,p('Den blå kurvan har den orange tangenten vid '+m(r'x=3')+'. Tangenten går genom de markerade punkterna '+m(r'(1,2)')+' och '+m(r'(5,10)')+'. Bestäm '+m(r'f\prime(3)')+'.'),2,
    solution('Derivatan är tangentens lutning.',mathline(r'f\prime(3)=\frac{10-2}{5-1}=2'),m(r'f\prime(3)=2')+'.'),'Använd två punkter på tangenten, inte två godtyckliga punkter på kurvan.',fig=plot('Funktionskurva med tangent och två markerade tangentpunkter',(0,6),(0,14),[(lambda x:.3*(x-3)**2+2*x,'#146a96'),(lambda x:2*x,'#b65d14')],[(1,2,''),(5,10,'')],xticks=list(range(7)),yticks=[0,2,4,6,8,10,12,14]))
add('mato1','Algebra och samband',2,p('Förenkla '+m(r'\dfrac{x^2-25}{x-5}')+' för '+m(r'x\ne5')+' så att svaret inte innehåller något bråk.'),'x+5',
    solution('Faktorisera täljaren innan du förkortar.',mathline(r'\frac{(x-5)(x+5)}{x-5}=x+5')+p('Förkortningen gäller eftersom x inte är 5.'),m(r'x+5')+', för '+m(r'x\ne5')+'.'),'Använd konjugatregeln baklänges.',calc=False,topic='Rationella uttryck')
add('mato1','Derivata och förändring',2,p('Funktionen '+m(r'f(x)=x^3-6x^2+9')+' har en lokal minimipunkt. Bestäm punktens '+m(r'x')+'-koordinat.'),4,
    solution('Derivatans tecken avgör vilken stationär punkt som är ett minimum.',mathline(r'f\prime(x)=3x^2-12x=3x(x-4)')+p('Derivatan är noll vid 0 och 4. Strax före 4 är den negativ och strax efter 4 positiv: funktionen vänder från att minska till att öka.'),m(r'x=4')+'.'),'En minimipunkt har övergång från negativ till positiv derivata.',calc=False)
add('mato1','Integraler och area',2,p('Bestäm arean mellan grafen '+m(r'y=2x+1')+', x-axeln och linjerna '+m(r'x=0')+' och '+m(r'x=3')+'. (Svara i areaenheter.)'),12,
    solution('Integralen ger arean eftersom grafen ligger över x-axeln.',mathline(r'\int_0^3(2x+1)\,dx=[x^2+x]_0^3')+mathline(r'=9+3-0=12'),'12 areaenheter.'),'En primitiv funktion kan användas för att beräkna arean.',fig=plot('Linjen y = 2x + 1 mellan 0 och 3',(0,3),(0,8),[(lambda x:2*x+1,'#146a96')],xticks=[0,1,2,3],yticks=[0,2,4,6,8]))
add('mato1','Integraler och area',2,p('En funktion uppfyller '+m(r'F\prime(x)=4x+3')+' och '+m(r'F(1)=10')+'. Bestäm '+m(r'F(x)')+'.'),'2*x^2+3*x+5',
    solution('Bestäm först en primitiv funktion, sedan konstanten.',mathline(r'F(x)=2x^2+3x+C')+mathline(r'F(1)=2+3+C=10\Rightarrow C=5'),m(r'F(x)=2x^2+3x+5')+'.'),'Villkoret F(1) bestämmer den annars fria konstanten.',calc=False)
add('mato1','Derivata och förändring',2,p('Mängden av ett ämne ges av '+m(r'M(t)=300e^{-0{,}2t}')+' mg, där '+m(r't')+' är tiden i timmar. Hur snabbt förändras mängden efter 5 timmar? (Svara i mg/h, med tecken.)'),-60/math.e,
    solution('Beräkna derivatans värde vid t = 5.',mathline(r'M\prime(t)=-60e^{-0{,}2t}')+mathline(r'M\prime(5)=-60e^{-1}\approx-22{,}1'),'Ungefär −22,1 mg/h. Mängden minskar.'),'Frågan gäller förändringshastigheten, inte själva mängden.',unit='mg/h')
add('mato1','Optimering och modeller',3,p('Ett rektangulärt odlingsland ligger längs en vägg. De övriga tre sidorna ska inhägnas med sammanlagt 60 m staket. Vilken är den största möjliga arean? (Svara i m².)'),450,
    solution('Skriv arean med en variabel och undersök derivatan.',p('Om de två korta sidorna är x meter blir den tredje sidan '+m(r'60-2x')+' meter.')+mathline(r'A(x)=x(60-2x)')+mathline(r'A\prime(x)=60-4x=0\Rightarrow x=15')+p('Derivatan går från positiv till negativ. Den andra sidan är 30 m och arean blir '+m(r'15\cdot30=450')+'.'),'450 m².'),'Väggen ersätter staket på en sida.',unit='m²',ability='problemlösning',fig=rectangle('Odlingsland längs en vägg','y m','x m',True))
add('mato1','Integraler och area',2,p('För funktionen '+m(r'f')+' gäller '+m(r'f\prime(x)=6x^2-4x')+' och '+m(r'f(0)=7')+'. Bestäm '+m(r'f(2)')+'.'),15,
    solution('Funktionsvärdet ändras med integralen av derivatan.',mathline(r'f(2)=7+\int_0^2(6x^2-4x)\,dx')+mathline(r'=7+[2x^3-2x^2]_0^2')+mathline(r'=7+16-8=15'),m(r'f(2)=15')+'.'),'Startvärdet måste läggas till förändringen.')
add('mato1','Integraler och area',3,p('En behållare innehåller från början 20 liter. Vatten strömmar in med '+m(r'4+2t')+' l/min och ut med 1 l/min. Tiden '+m(r't')+' mäts i minuter från starten. Hur mycket vatten finns efter 5 minuter? (Svara i liter.)'),60,
    solution('Integrera skillnaden mellan inflöde och utflöde.',mathline(r'V(5)=20+\int_0^5(4+2t-1)\,dt')+mathline(r'=20+[3t+t^2]_0^5')+mathline(r'=20+15+25=60'),'60 liter.'),'Bestäm först hur snabbt vattenmängden i behållaren ökar.',unit='l',ability='modellering',fig=svg('Behållare med separat in- och utflöde','<path d="M170 65V220H330V65" fill="#d5ebf5" stroke="#24435e" stroke-width="4"/>'+line(40,90,155,90,'#146a96',4)+'<path d="M145 82L157 90L145 98" fill="none" stroke="#146a96" stroke-width="3"/>'+line(340,190,465,190,'#b65d14',4)+'<path d="M455 182L467 190L455 198" fill="none" stroke="#b65d14" stroke-width="3"/>'+txt(95,65,'4 + 2t l/min',size=16)+txt(405,165,'1 l/min')+txt(250,160,'20 l vid start')))
add('mato1','Integraler och area',3,p('Bestäm den sammanlagda arean mellan linjen '+m(r'y=x-1')+' och x-axeln på intervallet '+m(r'0\le x\le3')+'. (Svara i areaenheter.)'),2.5,
    solution('Dela vid nollstället; båda delareorna är positiva.',p('Linjen skär x-axeln vid x = 1. De två områdena är trianglar.')+mathline(r'A=\frac{1\cdot1}{2}+\frac{2\cdot2}{2}')+mathline(r'=0{,}5+2=2{,}5'),'2,5 areaenheter.'),'En integral med tecken är inte alltid samma sak som sammanlagd area.',ability='begrepp',fig=plot('Linje som skär x-axeln inom intervallet',(0,3),(-2,3),[(lambda x:x-1,'#146a96')],xticks=[0,1,2,3],yticks=[-2,-1,0,1,2,3]))
tri60=svg('Två sidor i en triangel och mellanliggande vinkel','<path d="M80 235L400 235L200 27.154Z" fill="#e8f3f8" stroke="#24435e" stroke-width="3"/>'+txt(240,266,'8,0 cm')+txt(115,121,'6,0 cm','end')+txt(327,117,'c')+'<path d="M120 235A40 40 0 0 0 100 200.359" fill="none" stroke="#b65d14" stroke-width="2"/>'+txt(143,213,'60°'))
add('mato1','Trigonometri',2,p('Två sidor i en triangel är 6,0 cm och 8,0 cm. Vinkeln mellan dem är 60°. Hur lång är den tredje sidan? (Svara i cm.)'),math.sqrt(52),
    solution('Cosinussatsen använder vinkeln mellan de kända sidorna.',mathline(r'c^2=6^2+8^2-2\cdot6\cdot8\cos60^\circ')+mathline(r'c=\sqrt{52}\approx7{,}21'),'Ungefär 7,21 cm.'),'Triangeln är inte rätvinklig.',tracks=['1c'],unit='cm',fig=tri60,topic='Cosinussatsen')
add('mato1','Trigonometri',4,p('I en triangel är '+m(r'A=30^\circ')+', sidan mitt emot A är 5 cm och sidan mitt emot B är 8 cm. Hur många olika trianglar kan uppfylla dessa villkor?'),2,
    solution('Sinussatsen kan ge två olika vinklar.',mathline(r'\frac{\sin B}{8}=\frac{\sin30^\circ}{5}')+mathline(r'\sin B=0{,}8')+p('B kan vara ungefär 53,1° eller 126,9°. Båda ger en positiv tredje vinkel när A = 30°. De ger olika trianglar.'),'2 trianglar.'),'Två vinklar mellan 0° och 180° kan ha samma sinusvärde.',tracks=['1c'],ability='resonemang',topic='Sinussatsen och den tvetydiga situationen')
add('mato1','Optimering och modeller',2,p('Vid slutet av varje år sätts 3 000 kr in på ett konto med 4 % årsränta. Hur mycket finns direkt efter den tredje insättningen? (Svara i kr.)'),3000*(1.04**2+1.04+1),
    solution('Insättningarna får ränta olika länge.',p('Den första får ränta i två år, den andra i ett år och den tredje har just satts in.')+mathline(r'3000\cdot1{,}04^2+3000\cdot1{,}04+3000')+mathline(r'=9364{,}8'),'9 364,80 kr.'),'Rita en tidslinje och räkna antalet ränteperioder för varje insättning.',tracks=['1b'],unit='kr',fig=table(['Insättning','Tid med ränta'],[['Första','2 år'],['Andra','1 år'],['Tredje','0 år']]),topic='Geometriska summor')
add('mato1','Optimering och modeller',3,p('En verkstad gör '+m(r'x')+' små och '+m(r'y')+' stora skyltar per dag. Villkoren är '+m(r'x+y\le10')+', '+m(r'2x+y\le14')+' och '+m(r'x,y\ge0')+'. Vinsten är '+m(r'40x+25y')+' kr. Vilken är den största möjliga dagsvinsten? (Svara i kr.)'),310,
    solution('Jämför vinsten i det tillåtna områdets hörn.',p('Hörnen är (0,0), (0,10), (4,6) och (7,0). Skärningen (4,6) fås genom att lösa de två gränsekvationerna.')+p('Vinsterna är 0, 250, 310 respektive 280 kr. Störst vinst fås av fyra små och sex stora skyltar.'),'310 kr.'),'En linjär målfunktion når ett maximum i ett hörn av det tillåtna området.',tracks=['1b'],geo=True,unit='kr',ability='modellering',fig=plot('Gränslinjerna x + y = 10 och 2x + y = 14',(0,10),(0,14),[(lambda x:10-x,'#146a96'),(lambda x:14-2*x,'#b65d14')],xticks=[0,2,4,6,8,10],yticks=[0,2,4,6,8,10,12,14]),topic='Linjär optimering')
add('mato1','Derivata och förändring',3,p('Funktionen '+m(r'f(x)=x^3+ax^2+4')+' ska ha en horisontell tangent vid '+m(r'x=1')+'. Bestäm '+m(r'a')+'.'),-1.5,
    solution('En horisontell tangent har lutningen noll.',mathline(r'f\prime(x)=3x^2+2ax')+mathline(r'f\prime(1)=3+2a=0')+mathline(r'a=-\frac32'),m(r'a=-1{,}5')+'.'),'Översätt tangentens riktning till ett villkor på derivatan.',calc=False,ability='problemlösning')
add('mato1','Derivata och förändring',5,p('En tangent till '+m(r'y=x^2')+' dras i punkten '+m(r'(a,a^2)')+', där '+m(r'a>0')+'. Tangenten, x-axeln och linjen '+m(r'x=a')+' bildar en triangel. Bestäm '+m(r'a')+' om triangelns area är 16 areaenheter.'),4,
    solution('Uttryck tangentens nollställe och triangelns mått med a.',mathline(r'y=2a(x-a)+a^2=2ax-a^2')+p('Tangenten skär x-axeln vid '+m(r'x=a/2')+'. Triangelns bas är därför a/2 och höjden a².')+mathline(r'\frac{(a/2)\,a^2}{2}=16')+mathline(r'a^3=64\Rightarrow a=4'),m(r'a=4')+'.'),'Bestäm först var tangenten skär x-axeln.',ability='problemlösning',fig=svg('Schematisk tangenttriangel till en parabel','<path d="M90 245Q230 245 370 60" fill="none" stroke="#146a96" stroke-width="3"/><path d="M230 245L370 60L370 245Z" fill="#e4f1f5" stroke="#b65d14" stroke-width="2"/>'+line(65,245,440,245)+txt(370,273,'a')+txt(382,60,'(a, a²)','start',15)+txt(435,275,'x')))
add('mato1','Derivata och förändring',4,p('Funktionen '+m(r'f(x)=x^4-ax^2')+' har lokala minimipunkter vid '+m(r'x=-2')+' och '+m(r'x=2')+'. Bestäm '+m(r'a')+'.'),8,
    solution('Använd en minimipunkt och kontrollera att den verkligen är ett minimum.',mathline(r'f\prime(x)=4x^3-2ax')+mathline(r'f\prime(2)=32-4a=0\Rightarrow a=8')+p('Då är '+m(r'f\prime\prime(x)=12x^2-16')+', som är 32 vid både −2 och 2. Båda punkterna är alltså lokala minima.'),m(r'a=8')+'.'),'Derivatan måste vara noll i minimipunkterna.',calc=False,ability='problemlösning')

# Matematik – fortsättning nivå 2.
add('mato2','Derivata och funktioner',1,p('Bestäm derivatan till '+m(r'f(x)=\sin(3x)')+'.'),'3*cos(3*x)',
    solution('Multiplicera med den inre derivatan.',mathline(r'f\prime(x)=\cos(3x)\cdot3'),m(r'3\cos(3x)')+'.'),'Använd kedjeregeln.',calc=False)
add('mato2','Trigonometri och modeller',1,p('Bestäm perioden för '+m(r'f(x)=1+4\cos(2x)')+'. (Svara i radianer.)'),math.pi,
    solution('Argumentet ska öka med ett helt varv.',mathline(r'2T=2\pi\Rightarrow T=\pi'),m(r'\pi')+' radianer.'),'Hur mycket behöver x öka för att 2x ska öka med 2π?',calc=False,unit='rad')
add('mato2','Komplexa tal och algebra',1,p('Det komplexa talet '+m(r'z=-3+4i')+' är markerat i figuren. Bestäm '+m(r'|z|')+'.'),5,
    solution('Absolutbeloppet är avståndet till origo.',mathline(r'|z|=\sqrt{(-3)^2+4^2}=5'),'5.'),'Använd realdelen och imaginärdelen som kateter.',fig=plot('Komplext tal i talplanet',(-5,1),(-1,5),points=[(-3,4,'z')],xlabel='Re',ylabel='Im',xticks=[-4,-3,-2,-1,0,1],yticks=[0,1,2,3,4,5]))
add('mato2','Derivata och funktioner',2,p('Derivera '+m(r'f(x)=(x^2+1)e^x')+'.'),'exp(x)*(x^2+2*x+1)',
    solution('Båda faktorerna beror på x.',mathline(r'f\prime(x)=2xe^x+(x^2+1)e^x')+mathline(r'=e^x(x^2+2x+1)'),m(r'e^x(x^2+2x+1)')+'.'),'Använd produktregeln.',calc=False)
add('mato2','Derivata och funktioner',2,p('Derivera '+m(r'f(x)=\dfrac{x}{x+2}')+', där '+m(r'x\ne-2')+'.'),'2/(x+2)^2',
    solution('Kvotregeln tar hänsyn till både täljare och nämnare.',mathline(r'f\prime(x)=\frac{1\cdot(x+2)-x\cdot1}{(x+2)^2}')+mathline(r'=\frac{2}{(x+2)^2}'),m(r'\dfrac{2}{(x+2)^2}')+'.'),'Kontrollera ordningen i kvotregelns täljare.',calc=False)
add('mato2','Derivata och funktioner',2,p('Funktionen '+m(r'f(x)=\ln(7-2x)')+' är definierad för '+m(r'x<3{,}5')+'. Bestäm '+m(r'f\prime(x)')+'.'),'-2/(7-2*x)',
    solution('Derivatan av ln u är u′/u.',mathline(r'f\prime(x)=\frac{-2}{7-2x}'),m(r'-\dfrac{2}{7-2x}')+'.'),'Den inre funktionen är 7 − 2x.',calc=False)
add('mato2','Trigonometri och modeller',2,p('Lös '+m(r'\sin x=1/2')+' på intervallet '+m(r'0\le x\le2\pi')+'. Ange båda lösningarna i radianer, i var sitt fält.'),[math.pi/6,5*math.pi/6],
    solution('Sinus är positiv i första och andra kvadranten.',mathline(r'x=\frac{\pi}{6}\quad\text{eller}\quad x=\pi-\frac{\pi}{6}=\frac{5\pi}{6}'),m(r'\pi/6')+' och '+m(r'5\pi/6')+' radianer.'),'Vilka två vinklar på ett varv har höjden 1/2 i enhetscirkeln?',fmt='numeriskt',ordered=False,calc=True,unit='rad')
add('mato2','Integraler och tillämpningar',2,p('Beräkna '+m(r'\displaystyle\int_0^{\pi/4}\cos(2x)\,dx')+' exakt.'),.5,
    solution('Ta hänsyn till den inre derivatan i den primitiva funktionen.',mathline(r'\left[\frac12\sin(2x)\right]_0^{\pi/4}')+mathline(r'=\frac12\sin(\pi/2)-\frac12\sin0=\frac12'),m(r'1/2')+'.'),'Vilken faktor behövs framför sin(2x)?',calc=False)
add('mato2','Integraler och tillämpningar',3,p('Området mellan '+m(r'y=\sqrt{2x}')+', x-axeln och linjerna '+m(r'x=0')+' och '+m(r'x=3')+' roterar ett helt varv kring x-axeln. Bestäm volymen. (Svara exakt i volymenheter.)'),'9*pi',
    solution('Tvärsnittets radie är √(2x).',mathline(r'V=\pi\int_0^3(\sqrt{2x})^2\,dx')+mathline(r'=\pi[x^2]_0^3=9\pi'),m(r'9\pi')+' volymenheter.'),'Vid rotationen bildar varje tvärsnitt en cirkelskiva.',calc=True,ability='modellering',fig=plot('Rotationsområdets övre gräns',(0,3),(0,3),[(lambda x:math.sqrt(2*x),'#146a96')],xticks=[0,1,2,3],yticks=[0,1,2,3]))
add('mato2','Integraler och tillämpningar',3,p('En täthetsfunktion är '+m(r'f(x)=kx')+' för '+m(r'0\le x\le4')+' och noll utanför intervallet. Bestäm konstanten '+m(r'k')+'.'),.125,
    solution('Den totala sannolikheten är 1.',mathline(r'\int_0^4kx\,dx=k\left[\frac{x^2}{2}\right]_0^4=8k')+mathline(r'8k=1\Rightarrow k=\frac18'),m(r'k=1/8')+'.'),'Hela arean under en täthetsfunktion ska vara ett.',ability='begrepp')
add('mato2','Komplexa tal och algebra',2,p('Skriv '+m(r'\dfrac{5+i}{1-2i}')+' på formen '+m(r'a+bi')+'.'),'3/5+11/5*i',
    solution('Förläng med nämnarens konjugat.',mathline(r'\frac{(5+i)(1+2i)}{(1-2i)(1+2i)}')+mathline(r'=\frac{3+11i}{5}'),m(r'\dfrac35+\dfrac{11}{5}i')+'.'),'Gör nämnaren reell genom att använda konjugatet.',calc=True)
add('mato2','Komplexa tal och algebra',3,p('Polynomet '+m(r'p(x)=x^3-3x^2+4')+' har nollstället '+m(r'x=2')+'. Faktorisera polynomet i förstagradsfaktorer.'),'(x-2)^2*(x+1)',
    solution('Faktorsatsen ger den första faktorn.',mathline(r'p(x)=(x-2)(x^2-x-2)')+mathline(r'=(x-2)(x-2)(x+1)'),m(r'(x-2)^2(x+1)')+'.'),'Dela först polynomet med x − 2.',fmt='faktoriserat',calc=False)
add('mato2','Derivata och funktioner',1,p('Grafen till '+m(r'f(x)=\dfrac{2x+1}{x-3}')+' har en lodrät asymptot. Ange asymptotens '+m(r'x')+'-värde.'),3,
    solution('Nämnaren är noll utan att täljaren är noll.',mathline(r'x-3=0\Rightarrow x=3')+p('Täljaren har då värdet 7, så det finns ingen gemensam faktor som tar bort avbrottet.'),m(r'x=3')+'.'),'Var är nämnaren noll?',calc=False)
add('mato2','Trigonometri och modeller',2,p('En nivå varierar enligt '+m(r'h(t)=5+3\cos(\pi t/3)')+' meter, där '+m(r't')+' är tiden i timmar. Bestäm nivån efter en timme. (Svara i m.)'),6.5,
    solution('Sätt in t = 1 och använd radianer.',mathline(r'h(1)=5+3\cos(\pi/3)')+mathline(r'=5+3\cdot\frac12=6{,}5'),'6,5 m.'),'Kontrollera att räknaren använder radianer.',unit='m',fig=plot('Periodisk nivå under sex timmar',(0,6),(0,10),[(lambda t:5+3*math.cos(math.pi*t/3),'#146a96')],xlabel='Tid (h)',ylabel='Nivå (m)',xticks=[0,1,2,3,4,5,6],yticks=[0,2,4,6,8,10]))
add('mato2','Derivata och funktioner',3,p('För '+m(r'x\ge0')+' ges funktionen '+m(r'f(x)=xe^{-x}')+'. Vid vilket '+m(r'x')+'-värde är funktionen som störst?'),1,
    solution('Exponentialfaktorn är alltid positiv.',mathline(r'f\prime(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)')+p('Derivatan är positiv för 0 ≤ x &lt; 1 och negativ för x &gt; 1. Därför är x = 1 ett maximum på hela det givna intervallet.'),m(r'x=1')+'.'),'Använd produktregeln och undersök derivatans tecken.',calc=False,ability='problemlösning')
add('mato2','Derivata och funktioner',2,p('Funktionen är '+m(r'f(x)=(2x+1)^3')+'. Bestäm '+m(r'f\prime\prime(1)')+'.'),72,
    solution('Kedjeregeln behövs vid båda deriveringarna.',mathline(r'f\prime(x)=6(2x+1)^2')+mathline(r'f\prime\prime(x)=24(2x+1)')+mathline(r'f\prime\prime(1)=24\cdot3=72'),'72.'),'Glöm inte den inre derivatan när du deriverar en andra gång.')
add('mato2','Komplexa tal och algebra',2,p('Lös ekvationen '+m(r'z^2=-12')+'. Ange båda rötterna i var sitt fält.'),['2*sqrt(3)*i','-2*sqrt(3)*i'],
    solution('Använd att i² = −1.',mathline(r'z=\pm\sqrt{12}\,i=\pm2\sqrt3\,i')+p('Båda rötterna ger −12 när de kvadreras.'),m(r'z=2\sqrt3\,i')+' eller '+m(r'z=-2\sqrt3\,i')+'.'),'Rötterna är rent imaginära.',fmt='uttryck',ordered=False,calc=False)
add('mato2','Integraler och tillämpningar',3,p('Bestäm '+m(r'a')+' så att '+m(r'\displaystyle\int_0^{\pi/2}(a\cos x+\sin x)\,dx=2')+'.'),1,
    solution('Integrera med a som konstant.',mathline(r'[a\sin x-\cos x]_0^{\pi/2}')+mathline(r'=a-(-1)=a+1')+mathline(r'a+1=2\Rightarrow a=1'),m(r'a=1')+'.'),'Den okända konstanten a påverkas inte när du integrerar med avseende på x.',calc=False)
add('mato2','Integraler och tillämpningar',4,p('Beräkna '+m(r'\displaystyle\int_0^{\pi/2}(x\cos x+\sin x)\,dx')+' exakt.'),'pi/2',
    solution('Känn igen derivatan av en produkt.',mathline(r'\frac{d}{dx}(x\sin x)=\sin x+x\cos x')+mathline(r'\int_0^{\pi/2}(x\cos x+\sin x)\,dx')+mathline(r'=[x\sin x]_0^{\pi/2}=\frac\pi2'),m(r'\pi/2')+'.'),'Vilken produkt får två termer när den deriveras?',calc=False,ability='problemlösning')
add('mato2','Trigonometri och modeller',5,p('Funktionen '+m(r'f(x)=3\sin x+b\cos x')+' har största värdet 5. Konstanten '+m(r'b')+' är positiv. Bestäm '+m(r'b')+'.'),4,
    solution('Skriv summan som en förskjuten sinuskurva.',p('Sätt '+m(r'f(x)=R\sin(x+\varphi)')+'. Additionsformeln ger '+m(r'R\cos\varphi=3')+' och '+m(r'R\sin\varphi=b')+'.')+mathline(r'R^2=3^2+b^2')+p('Största värdet är R = 5, så '+m(r'25=9+b^2')+'. Eftersom b är positivt väljs b = 4.'),m(r'b=4')+'.'),'Använd additionsformeln för sin(x + φ) och trigonometriska ettan.',calc=False,ability='problemlösning')

# Senaste användarbeslutet: vanliga ämnesområden, bevara de publicerade ID:na.
PLACEMENTS=json.loads((ROOT/'agent/nationella-prov/OMPLACERING_2026-10-24.json').read_text())['tasks']
for placement in PLACEMENTS:
    task=next(q for q in BANKS[placement['course']] if q['id']==placement['id'])
    task.update(placement['after'])
    task['omrTidigare']=placement['before']['omr']
    task['familjTidigare']=placement['before']['familj']


def install():
    for course, tasks in BANKS.items():
        if not tasks:continue
        path=ROOT/f'uppgifter{course}.js'; raw=path.read_text(); start=raw.index('['); end=raw.rindex(']')
        old=json.loads(raw[start:end+1]); ids={q['id'] for q in old}
        assert not ids.intersection(q['id'] for q in tasks), f'ID-kollision i {course}'
        block=json.dumps(tasks,ensure_ascii=False,indent=2)[1:-1]
        path.write_text(raw[:end].rstrip()+','+block+'\n'+raw[end:])
    print({c:len(q) for c,q in BANKS.items()})

if __name__=='__main__':install()
