"""18 handskrivna C-uppgifter: algebraisk träning, familjer och grafiska samband."""
import importlib.util,json,math
from pathlib import Path
sp=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p,m,eq,table=h.p,h.m,h.eq,h.table
TASKS=[];REVIEW={};CASES={}
def add(n,t,ans,steps,final,hint,why,fig='',labels=None,options=None,fmt='uttryck',calc=True,family='Bestämma primitiva funktioner'):
 q=h.make('3.'+str(n),'primitiva',family,3,t,ans,steps,final,hint,fig=fig,labels=labels,options=options,skills=['begrepp','procedur']);q.update(poang='0/2/0',miniräknare=calc)
 if not options:q.update(svarFormat=[fmt]*len(ans) if labels else fmt,svarstyp='flera_delar' if labels else 'uttryck',tolerans=[None]*len(ans) if labels else None)
 TASKS.append(q);REVIEW[q['id']]={'C-motivering':why,'figur':'Figur eller tabell förtydligar den givna informationen.' if fig else 'Symbolisk bearbetning är innehållet; en extra bild skulle inte hjälpa.','verktyg':'Miniräknare tillåten; GeoGebra behövs inte.' if calc else 'Familjer av uttryck och konstantens betydelse prövas utan räknare.','kommentar':final}

add(1215,p('Funktionerna F och G ska vara primitiva funktioner till samma funktion för alla reella x. Bestäm a och b.')+eq(r'F(x)=(x-1)^3+ax^2+bx')+eq(r'G(x)=x^3+2x'),[3,-1],
 [p('Primitiva funktioner till samma funktion har lika derivator. Derivera efter att ha utvecklat kuben.')+eq(r"\begin{aligned}F'(x)&=3x^2+(2a-6)x\\&\quad+3+b\end{aligned}")+eq(r"G'(x)=3x^2+2"),p('Uttrycken ska vara lika för alla x. Därför måste x-termerna och konstanttermerna stämma var för sig.')+eq(r'2a-6=0,\qquad 3+b=2')],'a = 3 och b = −1.','Jämför derivatornas koefficienter, inte bara ett enstaka funktionsvärde.','Kombinerar kubutveckling med villkoret att två funktioner har samma derivata.',labels=['a','b'])

add(1216,p('F och G är primitiva funktioner till '+m('f(x)=6x-4')+' på hela tallinjen. Tabellen anger ett värde på vardera funktionen. Bestäm skillnaden '+m('F(3)-G(3)')+'.'),-4,
 [p('Alla primitiva funktioner har formen 3x²−4x+C. Villkoret F(0) = 2 ger konstanten 2.'),p('För G använder vi värdet vid x = 1.')+eq(r'3-4+C_G=5\Rightarrow C_G=6'),p('De x-beroende termerna är samma. Därför är skillnaden överallt 2−6 = −4, även vid x = 3.')],'F(3)−G(3) = −4.','Funktionsvärden vid olika x kan inte jämföras direkt.', 'Skiljer kända värden vid olika punkter från den konstanta skillnaden mellan två primitiva funktioner.',fig=table(['Givet värde','Tal'],[[m('F(0)'),'2'],[m('G(1)'),'5']]),family='Konstanten i primitiva funktioner')

add(1217,p('Bestäm alla primitiva funktioner till funktionen för x &gt; 0.')+eq(r'f(x)=\frac{(x^2-1)^2}{x^2}'),'x^3/3-2*x-1/x+C',
 [p('Utveckla kvadraten och dela varje term med x².')+eq(r'f(x)=x^2-2+x^{-2}'),p('Integrera term för term. När exponenten −2 ökas med 1 blir den −1, så den sista termen får minustecken.')+eq(r'F(x)=\frac{x^3}3-2x-\frac1x+C'),p('Derivering ger x²−2+1/x², vilket är den ursprungliga funktionen.')],m(r'F(x)=x^3/3-2x-1/x+C')+'.','Förenkla kvoten till en summa innan du integrerar.', 'Algebraisk mängdträning med kvadrering, division och en negativ exponent.',fmt='primitiva')

add(1218,p('Bestäm alla primitiva funktioner till funktionen för x &gt; 0.')+eq(r'f(x)=\frac{(x+1)^2}{\sqrt{x}}'),'2*x^(5/2)/5+4*x^(3/2)/3+2*sqrt(x)+C',
 [p('Utveckla täljaren och skriv roten som x¹ᐟ².')+eq(r'f(x)=x^{3/2}+2x^{1/2}+x^{-1/2}'),p('Öka exponenterna med 1 och dividera med de nya exponenterna.')+eq(r'F(x)=\frac25x^{5/2}+\frac43x^{3/2}')+eq(r'\phantom{F(x)={}}+2\sqrt{x}+C'),p('Derivering av de tre termerna ger tillbaka x³ᐟ², 2√x och 1/√x.')],m(r'F(x)=\frac25x^{5/2}+\frac43x^{3/2}+2\sqrt{x}+C')+'.','Dela upp kvoten i tre potenstermer.', 'Bearbetar en kvadrat över en rot och hanterar tre olika bråkexponenter.',fmt='primitiva')

add(1219,p('Funktionen '+m(r'F(x)=ax\sqrt{x}+b/x+C')+' ska vara en primitiv funktion till '+m(r'f(x)=3\sqrt{x}-2/x^2')+' för x &gt; 0. Bestäm a och b.'),[2,2],
 [p('Skriv x√x som x³ᐟ². Konstanten C försvinner vid derivering.')+eq(r"F'(x)=\frac{3a}2\sqrt{x}-\frac b{x^2}"),p('Jämför koefficienterna med f(x).')+eq(r'3a/2=3,\qquad -b=-2'),p('Det ger a = 2 och b = 2. C får vara vilken konstant som helst.')],'a = 2 och b = 2.','Kontrollera det föreslagna uttrycket genom att derivera.', 'Återskapar två koefficienter och skiljer en term med negativ exponent från integrationskonstanten.',labels=['a','b'])

add(1220,p('Bestäm alla primitiva funktioner till')+eq(r'f(x)=(e^x-2)^2.'),'e^(2*x)/2-4*e^x+4*x+C',
 [p('Utveckla kvadraten. Produkten eˣ·eˣ är e²ˣ.')+eq(r'f(x)=e^{2x}-4e^x+4'),p('Derivatan av e²ˣ är 2e²ˣ. Därför behöver den första primitiva termen faktorn 1/2.')+eq(r'F(x)=\frac12e^{2x}-4e^x+4x+C'),p('Konstanten 4 i f ger termen 4x i F; den får inte försvinna.')],m(r'F(x)=e^{2x}/2-4e^x+4x+C')+'.','Utveckla kvadraten innan du använder integrationsreglerna.', 'Kombinerar kvadreringsregel, exponentiallag och korrekt kedjefaktor.',fmt='primitiva')

add(1221,p('Bestäm alla primitiva funktioner till funktionen för x &gt; 0.')+eq(r'f(x)=\frac{(2x^2-3)(x^2+1)}{x^2}'),'2*x^3/3-x+3/x+C',
 [p('Multiplicera parenteserna.')+eq(r'\begin{aligned}&(2x^2-3)(x^2+1)\\&=2x^4-x^2-3\end{aligned}'),p('Dividera termvis med x² och integrera.')+eq(r'f(x)=2x^2-1-3x^{-2}')+eq(r'F(x)=\frac23x^3-x+\frac3x+C'),p('Sista termen är positiv eftersom −3 divideras med exponenten −1.')],m(r'F(x)=2x^3/3-x+3/x+C')+'.','Börja med att skriva funktionen som en summa av potenser.', 'Tränar en produkt av parenteser följd av division och integration med teckenkontroll.',fmt='primitiva')

add(1222,p('Alla primitiva funktioner till '+m('f(x)=x^2+2x')+' kan skrivas i formen')+eq(r'F(x)=\frac{(x+a)^3}{3}+bx+C.')+p('Bestäm a och b.'),[1,-1],
 [p('Utveckla kuben och derivera. Det ger')+eq(r"F'(x)=x^2+2ax+a^2+b"),p('Jämför med x²+2x: x-termen ger 2a = 2, alltså a = 1.'),p('Konstanttermen ska vara noll, så a²+b = 0. Med a = 1 får vi b = −1. Den fria konstanten C påverkar inte derivatan.')],'a = 1 och b = −1.','Utveckla uttrycket eller kontrollera det genom derivering.', 'Prövar om en förskjuten kub beskriver rätt familj och bestämmer två samverkande parametrar.',labels=['a','b'])

fig=h.graph('Grafen visar f(x)=roten ur x. Den okända primitiva funktionen F är inte ritad.',(0,10),(0,4),[[(i/20,math.sqrt(i/20)) for i in range(201)]],[0,1,4,9],[0,1,2,3,4],dots=[(1,1,True),(9,3,True)],ylabel='f(x)')
add(1223,p('F är en primitiv funktion till '+m(r'f(x)=\sqrt{x}')+' för x &gt; 0. Bestäm lutningen hos sekanten genom punkterna (1, F(1)) och (9, F(9)). Svara exakt.')+p('Figuren visar f, inte F.'),'13/6',
 [p('En primitiv funktion är F(x) = 2x³ᐟ²/3+C. Sekantens lutning beräknas från F:s värden.')+eq(r'k=\frac{F(9)-F(1)}{9-1}'),p('Konstanten C försvinner i skillnaden. 9³ᐟ² = 27 och 1³ᐟ² = 1.')+eq(r'k=\frac{(2/3)(27-1)}8=\frac{13}6')],m('13/6')+'.','Vilken funktion hör sekanten till, och vad händer med C i skillnaden?', 'Kopplar primitiv funktion till medellutning och skiljer f:s graf från F:s.',fig=fig)

add(1224,p('F är en primitiv funktion till '+m('f(x)=6x^2')+'. En ny funktion definieras av '+m('G(x)=F(2x)')+'. Bestäm '+m("G'(1)")+'.'),48,
 [p('Först är F(x) = 2x³+C. Byt sedan varje x mot 2x.')+eq(r'G(x)=2(2x)^3+C=16x^3+C'),p('Derivera G och sätt in x = 1.')+eq(r"G'(x)=48x^2\Rightarrow G'(1)=48"),p('Att bara beräkna f(2) skulle ge 24 och missa att G använder det dubbla x-värdet.')],'G′(1) = 48.','Skriv först ett uttryck för F och sätt sedan in 2x.', 'Kombinerar primitiv funktion, substitution i ett uttryck och ny derivering; ingen kedjeregel krävs.')

add(1225,p('Vilken av familjerna nedan innehåller alla primitiva funktioner till '+m('f(x)=2x')+' på hela tallinjen? C får vara vilket reellt tal som helst.'),None,
 [p('Alla primitiva funktioner har formen x²+k, där k ska kunna vara vilket reellt tal som helst.'),p('2C kan anta alla reella värden. C² kan bara vara icke-negativt, och sin C ligger mellan −1 och 1. Den fasta konstanten 7 ger bara en funktion.')],'x²+2C beskriver hela familjen.','Räcker det att derivatan är rätt, eller måste alla möjliga konstanta förskjutningar också finnas med?', 'Skiljer rätt derivata från att verkligen beskriva hela familjen av primitiva funktioner.',calc=False,options=[(m('x^2+C^2'),False),(m('x^2+2C'),True),(m(r'x^2+\sin C'),False),(m('x^2+7'),False)],family='Konstanten i primitiva funktioner')

add(1226,p('Funktionen '+m('f(x)=-1/x^2')+' är definierad för x ≠ 0. Två förslag på primitiva funktioner är')+eq(r'F_1(x)=1/x')+eq(r'F_2(x)=\begin{cases}1/x+2,&x\lt0\\1/x-3,&x\gt0.\end{cases}')+p('Vilket påstående är korrekt?'),None,
 [p('På vart och ett av intervallen x < 0 och x > 0 är den extra termen i F₂ konstant. Både F₁ och F₂ har därför derivatan −1/x² där.'),p('Varken f eller de föreslagna funktionerna är definierade vid x = 0. De två skilda intervallen behöver inte ha samma integrationskonstant.')],'Båda är primitiva funktioner på vart och ett av intervallen x < 0 och x > 0.','Undersök derivatan på varje intervall där f är definierad.', 'Använder konstantbegreppet på två skilda intervall och undviker ett felaktigt krav vid den uteslutna punkten.',calc=False,options=[('Bara F₁, eftersom en primitiv funktion alltid måste ha samma konstant överallt.',False),('Bara F₂, eftersom F₁ saknar en utskriven konstant.',False),('Ingen, eftersom de inte är definierade vid x = 0.',False),('Båda, på vart och ett av intervallen x < 0 och x > 0.',True)],family='Konstanten i primitiva funktioner')

add(1227,p('F och G är primitiva funktioner till f respektive g på hela tallinjen. Det gäller att '+m('f(x)-g(x)=2x')+' och att '+m('F(1)=G(1)')+'. Bestäm '+m('F(3)-G(3)')+'.'),8,
 [p('Betrakta skillnaden H(x) = F(x)−G(x). Dess derivata är f(x)−g(x) = 2x. Därför är H(x) = x²+C.'),p('Det givna villkoret betyder H(1) = 0, så 1+C = 0 och C = −1.'),p('Vid x = 3 blir skillnaden H(3) = 9−1 = 8.')],'F(3)−G(3) = 8.','Det går att bestämma skillnaden utan att känna F och G var för sig.', 'Introducerar en hjälpfunktion och kopplar ett villkor på två funktioner till dess konstant.',family='Konstanten i primitiva funktioner')

add(1228,p('Två elever skriver alla primitiva funktioner till '+m('f(x)=(x-1)^2')+' på olika sätt. C och K får vara vilka reella tal som helst.')+eq(r'F_1(x)=\frac{(x-1)^3}{3}+C')+eq(r'F_2(x)=\frac{x^3}{3}-x^2+x+K')+p('Vilket påstående är korrekt?'),None,
 [p('Utveckla kuben i det första uttrycket.')+eq(r'F_1(x)=\frac{x^3}{3}-x^2+x-\frac13+C'),p('Välj K = C−1/3. Då beskriver de två uttrycken samma funktion. Eftersom C och K kan vara vilka reella tal som helst beskriver båda hela familjen.')],'Båda är korrekta och beskriver samma familj.','Jämför uttrycken efter att kuben utvecklats. Är skillnaden beroende av x?', 'Känner igen likvärdiga familjer trots en dold konstant efter utveckling.',calc=False,options=[('Bara det första är korrekt.',False),('Båda är korrekta, men familjerna är olika.',False),('Båda är korrekta och beskriver samma familj.',True),('Bara det andra är korrekt.',False)],family='Konstanten i primitiva funktioner')

add(1229,p('Bestäm alla primitiva funktioner till funktionen för x &gt; 0.')+eq(r'f(x)=\left(\sqrt{x}-\frac1{\sqrt{x}}\right)(x+2)'),'2*x^(5/2)/5+2*x^(3/2)/3-4*sqrt(x)+C',
 [p('Multiplicera in båda termerna och samla dem med samma exponent.')+eq(r'f(x)=x^{3/2}+x^{1/2}-2x^{-1/2}'),p('Integrera de tre potenserna.')+eq(r'F(x)=\frac25x^{5/2}+\frac23x^{3/2}')+eq(r'\phantom{F(x)={}}-4\sqrt{x}+C'),p('Kontroll: derivatorna är x³ᐟ², √x och −2/√x, vilket ger den förenklade funktionen.')],m(r'F(x)=\frac25x^{5/2}+\frac23x^{3/2}-4\sqrt{x}+C')+'.','Multiplicera parenteserna innan du integrerar.', 'Algebraisk mängdträning där rottermer först måste multipliceras och slås ihop.',fmt='primitiva')

add(1230,p('F är en primitiv funktion till '+m('f(x)=kx^2')+'. För alla reella x gäller')+eq(r'F(2x)-F(x)=7x^3.')+p('Bestäm k.'),3,
 [p('En primitiv funktion är F(x) = kx³/3+C. Sätt in 2x i samma uttryck.')+eq(r'F(2x)-F(x)=\frac{k}{3}(8x^3-x^3)'),p('Konstanten försvinner, och skillnaden blir 7kx³/3. Detta ska vara 7x³ för alla x, så k/3 = 1.')],'k = 3.','Skriv en primitiv funktion med k kvar och använd sedan skillnadsvillkoret.', 'Bestämmer en parameter genom hur en hel familj förändras när argumentet fördubblas.',family='Konstanten i primitiva funktioner')

def true_axes(fig,xlim,ylim):
 X=65+370*(0-xlim[0])/(xlim[1]-xlim[0]);Y=250-200*(0-ylim[0])/(ylim[1]-ylim[0])
 return fig.replace('M65 45V250H445',f'M{X} 45V250 M65 {Y}H445')
fig=h.graph('Graf till f(x)=x²−1. F är en primitiv funktion och är inte ritad.',(-2,2),(-1.5,3.5),[[(i/100,(i/100)**2-1) for i in range(-200,201)]],[-2,-1,0,1,2],[-1,0,1,2,3],ylabel='f(x)')
fig=true_axes(fig,(-2,2),(-1.5,3.5))
add(1231,p('F är en primitiv funktion till '+m('f(x)=x^2-1')+'. F har en lokal maximipunkt vid x = −1 och en lokal minimipunkt vid x = 1. Hur stor är skillnaden mellan dessa två funktionsvärden hos F? Svara exakt.')+p('Figuren visar f, inte F.'),'4/3',
 [p('Alla primitiva funktioner är F(x) = x³/3−x+C. Vi ska ta maximivärdet minus minimivärdet.'),p('Beräkna värdena vid de två angivna x-koordinaterna.')+eq(r'F(-1)=\frac23+C')+eq(r'F(1)=-\frac23+C'),p('Konstanten försvinner i skillnaden.')+eq(r'F(-1)-F(1)=\frac43')],m('4/3')+' längdenheter i höjdled.','Grafens höjd är f(x). Den efterfrågade skillnaden gäller i stället en primitiv funktion F.', 'Skiljer derivatagraf från primitiv funktion och visar att en höjdskillnad inte kräver känd konstant.',fig=fig,family='Konstanten i primitiva funktioner')

fig=h.graph('Graf till f(x)=4x³−12x med tre nollställen. Den primitiva funktionen F är inte ritad.',(-2,2),(-9,9),[[(i/100,4*(i/100)**3-12*i/100) for i in range(-200,201)]],[-2,-1,0,1,2],[-8,-4,0,4,8],ylabel='f(x)')
fig=true_axes(fig,(-2,2),(-9,9))
add(1232,p('F är en primitiv funktion till '+m('f(x)=4x^3-12x')+'. Bestäm skillnaden mellan F:s lokala maximivärde och dess minsta värde. Svara exakt.')+p('Figuren visar f, inte F.'),9,
 [p('En primitiv funktion är F(x) = x⁴−6x²+C. F har stationära punkter där f(x) = 0.')+eq(r'4x(x^2-3)=0'),p('Det ger x = −√3, 0 och √3. Tecknet på f växlar från minus till plus vid ±√3 och från plus till minus vid 0. F har alltså minimum vid ±√3 och lokalt maximum vid 0.'),p('Båda minimivärdena är C−9. Det är även det minsta värdet på hela tallinjen, eftersom F kan skrivas (x²−3)²+C−9. Vid x = 0 är värdet C.')+eq(r'C-(C-9)=9')],'Skillnaden är 9.','Bestäm först var f är noll, men jämför sedan värdena på F.', 'Kombinerar primitiv funktion, teckenstudium och extremvärden; konstanten elimineras.',fig=fig,family='Konstanten i primitiva funktioner')

for n,valid,invalid in [
 (1216,['-4','−4'],['4','-3']),
 (1217,['x^3/3-2*x-1/x+C','K+x^3/3-2*x-1/x','F(x)=x^3/3-2*x-1/x+2K'],['x^3/3-2*x-1/x','x^3/3-2*x+1/x+C']),
 (1218,['2*x^(5/2)/5+4*x^(3/2)/3+2*sqrt(x)+K'],['2*x^(5/2)/5+2*x^(3/2)/3+2*sqrt(x)+C']),
 (1220,['exp(2*x)/2-4*exp(x)+4*x+K','e^(2*x)/2-4*e^x+4*x+2C'],['e^(2*x)-4*e^x+4*x+C','e^(2*x)/2-4*e^x+4+C']),
 (1221,['2*x^3/3-x+3/x+K'],['2*x^3/3-x-3/x+C']),
 (1223,['13/6','26/12'],['1/4','2']),
 (1224,['48'],['24','12']),
 (1227,['8'],['9','6']),
 (1229,['2*x^(5/2)/5+2*x^(3/2)/3-4*sqrt(x)+K'],['2*x^(5/2)/5+2*x^(3/2)/3-2*sqrt(x)+C']),
 (1230,['3','k=3'],['1','7']),
 (1231,['4/3','8/6'],['-4/3','2']),
 (1232,['9'],['0','-9'])]:CASES['mato1:3.'+str(n)]=[valid,invalid]

if __name__=='__main__':
 h.install(TASKS)
 (h.ROOT/'agent/MA3_PRIMITIVA_C_2026-10-25.json').write_text(json.dumps(REVIEW,ensure_ascii=False,indent=2)+'\n')
 (h.ROOT/'tools/ma3-primitiva-c-2026-10-25.cases.json').write_text(json.dumps(CASES,ensure_ascii=False,indent=2)+'\n')
