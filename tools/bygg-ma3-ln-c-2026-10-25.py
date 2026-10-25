"""20 individuellt konstruerade C-uppgifter. Kör bara i masterrepot."""
import importlib.util, json, math
from pathlib import Path
sp=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'))
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p,m,eq,sol,graph,table,svg,text=h.p,h.m,h.eq,h.sol,h.graph,h.table,h.svg,h.text
TASKS=[]; REVIEW={}; CASES={}
def add(n,t,answer,steps,final,hint,why,fig='',fmt='uttryck',labels=None,calc=True,options=None,unit=None,cases=None):
 q=h.make('2.'+str(n),'naturliga_logaritmer','Naturliga logaritmer och ekvationer',3,t,answer,steps,final,hint,fig=fig,labels=labels,options=options,unit=unit,skills=['begrepp','problemlösning'])
 q['kap']=2;q['poang']='0/2/0';q['miniräknare']=calc
 if not options:
  q['svarFormat']=[fmt]*len(answer) if labels else fmt
  q['svarstyp']='flera_delar' if labels else ('uttryck' if fmt=='uttryck' else 'numeriskt')
  q['tolerans']=[None]*len(answer) if labels and fmt=='uttryck' else (None if fmt=='uttryck' else 0.005)
 TASKS.append(q);REVIEW[q['id']]={'C-motivering':why,'figur':'Figur/tabell hjälper representationen.' if fig else 'Symbolisk analys är själva innehållet; en figur skulle inte tillföra information.','verktyg':'Miniräknare tillåten; GeoGebra behövs inte.' if calc else 'Utan räknare: det exakta symbolsambandet är det som prövas. GeoGebra behövs inte.','kommentar':final}
 if cases:CASES['mato1:'+q['id']]=cases

add(1201,p('Lös ekvationen. Ange alla reella lösningar.')+eq(r'\ln(x-1)+\ln(x+1)=\ln8'),3,
 [p('Båda logaritmerna kräver positiva argument. Därför måste x vara större än 1.'),p('Samla logaritmerna och jämför argumenten.')+eq(r'(x-1)(x+1)=8')+eq(r'x^2=9\quad\Rightarrow\quad x=\pm3'),p('Endast 3 uppfyller villkoret x > 1.')],m('x=3')+'.','Vilka x-värden är tillåtna innan du använder logaritmlagen?','Kombinerar logaritmlag, andragradsekvation och bortval av en otillåten rot.',cases=[['3','x=3'],['-3','9']])

fig=svg('Två kvadrater med sidlängderna a och b. Figuren är schematisk.', '<rect x="45" y="130" width="95" height="95" fill="#e5f3fa" stroke="#195578" stroke-width="3"/><rect x="260" y="55" width="170" height="170" fill="#e5f3fa" stroke="#195578" stroke-width="3"/>'+text(93,253,'a')+text(345,253,'b')+text(250,290,'Schematisk figur',16))
add(1202,p('Två kvadrater har sidlängderna a och b, där b &gt; a. Det gäller att '+m(r'\ln b-\ln a=1{,}5')+'. Hur många gånger så stor area har den större kvadraten? Svara exakt.'),'e^3',
 [p('Logaritmskillnaden beskriver kvoten mellan sidlängderna.')+eq(r'\ln(b/a)=1{,}5\Rightarrow b/a=e^{1{,}5}'),p('Areafaktorn är kvadraten på längdfaktorn.')+eq(r'\frac{b^2}{a^2}=(e^{1{,}5})^2=e^3')],m('e^3')+' gånger.','Hur hänger en längdfaktor ihop med en areafaktor?','Växlar mellan logaritmskillnad, längdkvot och areafaktor.',fig=fig,cases=[['e^3','exp(3)'],['e^1.5','3']])

add(1203,p('Talen 4, x och 25 är positiva och står i stigande ordning. Skillnaden mellan deras naturliga logaritmer är lika stor i båda stegen:')+p('Bestäm x.'),10,
 [p('Flytta ihop termerna med ln x.')+eq(r'2\ln x=\ln4+\ln25=\ln100'),p('Skriv vänsterledet som ln(x²).')+eq(r'x^2=100'),p('x är positivt och ligger mellan 4 och 25, alltså x = 10.')],'x = 10.','Lika steg i logaritmerna betyder inte lika stora skillnader mellan talen.','Identifierar geometriskt mellanvärde i stället för aritmetiskt medelvärde.',fig=table(['Tal','Naturlig logaritm'],[['4',m(r'\ln4')],['x',m(r'\ln x')],['25',m(r'\ln25')]]),cases=[['10'],['14.5','100']])

add(1204,p('Lös ekvationen och ange alla reella lösningar.')+eq(r'\ln(x+2)=2\ln x'),2,
 [p('Högerledet kräver x > 0. Skriv 2 ln x som ln(x²).')+eq(r'x+2=x^2'),p('Lös andragradsekvationen.')+eq(r'(x-2)(x+1)=0'),p('Kandidaterna är 2 och −1. Bara 2 ligger i definitionsmängden.')],'x = 2.','Kontrollera definitionsmängden innan du godtar en rot.','Logaritmlag och faktorisering ger en extrakandidat som måste uteslutas.',cases=[['2','x=2'],['-1','1']])

add(1205,p('Funktionen är '+m(r'f(x)=a\ln x+b')+'. Tabellen visar två funktionsvärden. Bestäm '+m(r'f(e^{-1})')+'.'),1,
 [p('Eftersom ln 1 = 0 visar första raden att b = 4.'),p('Den andra raden ger 2a+4 = 10, alltså a = 3.'),p('Nu är ln(e⁻¹) = −1.')+eq(r'f(e^{-1})=3\cdot(-1)+4=1')],'1.','Vilken av tabellraderna bestämmer en av konstanterna direkt?','Bestämmer en modell från två villkor och använder ln som invers till e-potens.',fig=table(['x',m('f(x)')],[['1','4'],[m('e^2'),'10']]),cases=[['1'],['-1','7']])

add(1206,p('De positiva talen p och q uppfyller '+m(r'\ln p=2a')+' och '+m(r'\ln q=a-1')+'. Bestäm '+m(r'\ln\left(\frac{p}{q^2}\right)')+'. Svaret ska inte innehålla a.'),2,
 [p('Skriv kvotens logaritm som en skillnad.')+eq(r'\ln(p/q^2)=\ln p-2\ln q'),p('Sätt in de givna sambanden. Termerna med a tar ut varandra.')+eq(r'2a-2(a-1)=2')],'2.','Bryt upp kvotens logaritm innan du sätter in uttrycken.','Generaliserar med två logaritmlagar och ser att parametern försvinner.',calc=False,cases=[['2'],['0','a+1']])

add(1207,p('För '+m(r'x\lt2')+' vill en elev skriva om '+m(r'\ln((x-2)^2)')+'. Vilket uttryck är lika med det ursprungliga för alla dessa x? Välj ett alternativ.'),None,
 [p('När x < 2 är x−2 negativt, så ln(x−2) är inte definierad. Däremot är 2−x positivt.'),p('Kvadraterna är lika. Potenslagen kan därför användas med det positiva argumentet 2−x.')+eq(r'\ln((x-2)^2)=\ln((2-x)^2)')+eq(r'=2\ln(2-x)')],m(r'2\ln(2-x)')+'.','Vilket argument är positivt när x är mindre än 2?','Bedömer logaritmlagens giltighet och bevarar definitionsmängden.',calc=False,options=[(m(r'2\ln(x-2)'),False),(m(r'\ln(2-x)'),False),(m(r'2\ln(2-x)'),True),(m(r'2\ln x-2\ln2'),False)])

add(1208,p('Funktionen är '+m(r'f(x)=\ln(3x-2)')+'. Bestäm det x-värde som uppfyller '+m('f(f(x))=0')+'. Svara exakt.'),'(e+2)/3',
 [p('Börja med den yttre funktionen. ln(3f(x)−2) = 0 betyder att argumentet är 1.')+eq(r'3f(x)-2=1\Rightarrow f(x)=1'),p('Lös sedan den inre ekvationen.')+eq(r'\ln(3x-2)=1')+eq(r'3x-2=e\Rightarrow x=\frac{e+2}{3}'),p('Vid detta x är det inre argumentet e och det yttre 1. Båda är positiva.')],m(r'x=\frac{e+2}{3}')+'.','Vilket värde måste f(x) ha för att den yttre funktionen ska ge 0?','Arbetar baklänges genom två sammansatta logaritmfunktioner.',cases=[['(e+2)/3','x=(exp(1)+2)/3'],['1','(e-2)/3']])

fig=graph('Logaritmkurvan och sträckan mellan (1,0) och (4,ln 4). M är sträckans mittpunkt.',(0,4.5),(0,2),[[(i/100,math.log(i/100)) for i in range(100,451)],[(1,0),(4,math.log(4))]],[0,1,2,3,4],[0,1,2],dots=[(1,0,True),(4,math.log(4),True),(2.5,math.log(2),True)])
fig=fig.replace('</svg>',text(270,211,'M',19)+'</svg>')
add(1209,p('A = (1, 0) och '+m(r'B=(4,\ln4)')+' ligger på grafen '+m(r'y=\ln x')+'. M är mittpunkten på sträckan AB. Hur långt ovanför M ligger kurvan vid samma x-värde? Svara exakt.'),'ln(5/4)',
 [p('Mittpunktens koordinater är medelvärdena av ändpunkternas koordinater.')+eq(r'x_M=\frac{1+4}{2}=\frac52')+eq(r'y_M=\frac{\ln4}{2}=\ln2'),p('Kurvans höjd vid samma x är ln(5/2). Skillnaden blir')+eq(r'\ln(5/2)-\ln2=\ln(5/4)')],m(r'\ln(5/4)')+' längdenheter.','Bestäm först båda koordinaterna för mittpunkten.','Kombinerar koordinatgeometri med logaritmlagar, inte bara avläsning.',fig=fig,cases=[['ln(5/4)','ln(2.5)-ln(2)'],['ln(2.5)','0']])

add(1210,p('En funktion har formen '+m(r'f(x)=a\ln x+b')+'. Tabellen visar tre värden. Bestäm det x-värde som ger '+m('f(x)=9')+'.'),162,
 [p('När x multipliceras med 3 ökar ln x med ln 3. Funktionen ökar därför alltid med samma tal vid en sådan tredubbling.'),p('Tabellen visar att ökningen är 2. Från f(18) = 5 behövs två ökningar till 9. Därför ska x tredubblas två gånger.')+eq(r'x=18\cdot3^2=162')],'x = 162.','Vad händer med ln x när x multipliceras med samma faktor igen?','Använder regelbundenhet i en logaritmisk modell utan att behöva bestämma båda konstanterna.',fig=table(['x',m('f(x)')],[['2','1'],['6','3'],['18','5']]),cases=[['162'],['54','30']])

fig=graph('Temperaturen närmar sig 20 grader. Markering vid 4 minuter och 50 grader.',(0,20),(0,90),[[(i/10,20+60*2**(-i/40)) for i in range(201)]],[0,4,8,12,16,20],[0,20,40,60,80],dots=[(4,50,True)],xlabel='Tid (min)',ylabel='Temperatur (°C)')
add(1211,p('En dryck svalnar enligt '+m(r'T(t)=20+60e^{-kt}')+', där T mäts i °C och t i minuter. Efter 4 minuter är temperaturen 50 °C. Hur lång tid från starten tar det tills temperaturen är 25 °C? Svara i minuter med två decimaler.'),4*math.log(12)/math.log(2),
 [p('Använd mätningen för att bestämma k.')+eq(r'50=20+60e^{-4k}')+eq(r'e^{-4k}=\frac12\Rightarrow k=\frac{\ln2}{4}'),p('Vid 25 °C är temperaturskillnaden mot rummet 5 °C.')+eq(r'e^{-kt}=\frac5{60}=\frac1{12}'),p('Logaritmera och sätt in k.')+eq(r't=\frac{\ln12}{k}=\frac{4\ln12}{\ln2}')+eq(r't\approx14{,}34')],'14,34 min.','Det är skillnaden från rumstemperaturen som avtar exponentiellt.','Bestämmer först en okänd modellparameter och hanterar en basnivå före logaritmering.',fig=fig,fmt='numeriskt',unit='min',cases=[['14,34','14.34 min'],['14.33','4.34','12']])

add(1212,p('Två odlingar beskrivs av '+m('A(t)=100e^{0{,}30t}')+' och '+m('B(t)=400e^{0{,}10t}')+', där t är tiden i dygn från starten. Efter hur många dygn är antalen lika stora? Svara med två decimaler.'),math.log(4)/.2,
 [p('Sätt antalen lika. Dividera båda leden med 100e⁰·¹⁰ᵗ.')+eq(r'100e^{0{,}30t}=400e^{0{,}10t}')+eq(r'e^{0{,}20t}=4'),p('Logaritmera för att få tiden.')+eq(r'0{,}20t=\ln4')+eq(r't=\frac{\ln4}{0{,}20}\approx6{,}93')],'6,93 dygn.','Samla exponentialfaktorerna genom att dividera leden.','Jämför två olika exponentiella modeller och tolkar skillnaden mellan tillväxttakterna.',fig=table(['Odling','Antal vid start','Modell'],[['A','100',m('100e^{0{,}30t}')],['B','400',m('400e^{0{,}10t}')]]),fmt='numeriskt',unit='dygn',cases=[['6,93','6.93 dygn'],['6.92','4.62']])

fig=svg('Logaritmisk skala från 10 till 1000. P ligger tre fjärdedelar av sträckan från 10.', '<path d="M60 120H440 M60 105V135 M440 105V135 M345 105V135" stroke="#244c66" stroke-width="3" fill="none"/>'+text(60,165,'10')+text(440,165,'1000')+text(345,92,'P')+'<path d="M60 202H345 M60 194V210 M345 194V210" stroke="#a15320" stroke-width="2"/>'+text(205,235,'¾ av hela sträckan',18),270)
add(1213,p('På skalan är avståndet mellan två positiva tal proportionellt mot skillnaden mellan deras naturliga logaritmer. P ligger tre fjärdedelar av sträckan från 10 till 1000. Vilket tal motsvarar P? Svara med en decimal.'),10**2.5,
 [p('Tre fjärdedelar av logaritmskillnaden ger')+eq(r'\ln P-\ln10')+eq(r'=\frac34(\ln1000-\ln10)'),p('Skriv om till en kvot och använd inverssambandet.')+eq(r'\ln(P/10)=\frac34\ln100')+eq(r'P=10\cdot100^{3/4}\approx316{,}2')],'316,2.','Avståndet gäller logaritmerna, inte skillnaden 1000−10.','Översätter en geometrisk position på logaritmisk skala till ett tal.',fig=fig,fmt='numeriskt',cases=[['316,2','316.2'],['752.5','316.1']])
TASKS[-1]['tolerans']=.05

add(1214,p('Två positiva tal a och b uppfyller båda sambanden. Bestäm a och b.')+eq(r'\ln a+\ln b=\ln12')+eq(r'\ln a-\ln b=\ln3'),[6,2],
 [p('Logaritmlagarna ger både en produkt och en kvot.')+eq(r'ab=12,\qquad a/b=3'),p('Sätt a = 3b i produkten.')+eq(r'3b^2=12\Rightarrow b^2=4'),p('Båda talen är positiva, så b = 2 och a = 6.')],'a = 6 och b = 2.','Vilka samband mellan a och b motsvarar summan respektive skillnaden av logaritmer?', 'Översätter två logaritmsamband till ett ekvationssystem och använder positivitet.',labels=['a','b'])

add(1215,p('Jämför ekvationerna '+m(r'\ln(x^2)=\ln9')+' och '+m(r'2\ln x=\ln9')+'. Vilket påstående är korrekt? Välj ett alternativ.'),None,
 [p('I den första ekvationen räcker det att x² är positivt. Både x = −3 och x = 3 ger x² = 9.'),p('I den andra måste x vara positivt redan för att ln x ska finnas. Därför återstår bara x = 3.'),p('Omskrivningen ln(x²) = 2 ln x gäller alltså inte för negativa x.')],'Den första har lösningarna −3 och 3, den andra bara 3.','Jämför vilka x-värden som är tillåtna i de två ursprungliga uttrycken.','Skiljer formellt liknande uttryck genom definitionsmängder och lösningsmängder.',calc=False,options=[('Båda har bara lösningen 3.',False),('Den första har lösningarna −3 och 3, den andra bara 3.',True),('Båda har lösningarna −3 och 3.',False),('Den första har bara lösningen 3, den andra −3 och 3.',False)])

add(1216,p('Hur många heltal x uppfyller olikheten?')+eq(r'\ln(x-1)+\ln(7-x)\gt\ln8'),1,
 [p('Logaritmerna är definierade om 1 < x < 7. Eftersom ln är växande kan vi jämföra argumenten efter att ha samlat logaritmerna.')+eq(r'(x-1)(7-x)\gt8'),p('Flytta allt till ett led och faktorisera.')+eq(r'x^2-8x+15\lt0')+eq(r'(x-3)(x-5)\lt0'),p('Detta ger 3 < x < 5. Endast heltalet 4 ligger i intervallet.')],'1 heltal.','Börja med definitionsmängden. Därefter kan argumenten jämföras.','Kombinerar definitionsvillkor, logaritmens monotoni och en andragradsolikhet.')
CASES['mato1:2.1216']=[['1'],['3','4','5']]

add(1217,p('Lös ekvationen och ange alla reella lösningar exakt.')+eq(r'(\ln x)^2-3\ln x=0'),['1','e^3'],
 [p('x måste vara positivt. Bryt ut ln x.')+eq(r'\ln x(\ln x-3)=0'),p('En produkt är noll om minst en faktor är noll.')+eq(r'\ln x=0\quad\text{eller}\quad\ln x=3'),p('Gå tillbaka från logaritmer till x.')+eq(r'x=1\quad\text{eller}\quad x=e^3')],m('x=1')+' eller '+m('x=e^3')+'.','Se ln x som ett enda uttryck som kan faktoriseras.','Ser andragradsstrukturen i ln x och bevarar båda lösningarna.',labels=['En lösning','Den andra lösningen'])
TASKS[-1]['svarsstruktur']='mängd'

fig=graph('Grafen till ln(x−a)+b har lodrät asymptot x=2 och går genom (3,4).',(0,6),(-2,6),[[(2+math.exp(-6+i/40),-2+i/40) for i in range(296)]],[0,1,2,3,4,5,6],[-2,0,2,4,6],dots=[(3,4,True)])
fig=fig.replace('M65 45V250H445','M65 45V250 M65 200H445').replace('</svg>','<path d="M188.333 50V250" stroke="#a15320" stroke-width="2" stroke-dasharray="6 5"/>'+'<rect x="282" y="110" width="56" height="26" fill="white"/>'+text(310,130,'(3, 4)',18)+'</svg>')

add(1218,p('Grafen visar '+m(r'f(x)=\ln(x-a)+b')+'. Den lodräta asymptoten är x = 2 och grafen går genom (3, 4). Bestäm grafens nollställe exakt.'),'2+e^(-4)',
 [p('Logaritmens argument närmar sig 0 vid asymptoten. Därför är a = 2.'),p('Punkten ger ln(3−2)+b = 4. Eftersom ln 1 = 0 är b = 4.'),p('Sätt funktionsvärdet lika med noll.')+eq(r'\ln(x-2)+4=0')+eq(r'x-2=e^{-4}\Rightarrow x=2+e^{-4}')],m(r'x=2+e^{-4}')+'.','Vad berättar asymptoten om a, och punkten om b?','Hämtar två parameterkrav ur en figur och löser sedan en logaritmekvation.',fig=fig,cases=[['2+e^(-4)','x=2+1/e^4'],['e^(-4)','2-e^(-4)']])

add(1219,p('Ett pris höjs med p procent och sänks sedan med lika många procent, där 0 &lt; p &lt; 100. Förhållandet mellan slutpriset S och ursprungspriset U uppfyller '+m(r'\ln(S/U)=\ln(3/4)')+'. Bestäm p.'),50,
 [p('Lika logaritmer ger S/U = 3/4. Höjningen och sänkningen har faktorerna 1+p/100 respektive 1−p/100.')+eq(r'\left(1+\frac p{100}\right)\left(1-\frac p{100}\right)=\frac34'),p('Använd konjugatregeln.')+eq(r'1-\left(\frac p{100}\right)^2=\frac34')+eq(r'\left(\frac p{100}\right)^2=\frac14'),p('p är positivt, så p/100 = 1/2 och p = 50.')],'p = 50.','Procenten vid sänkningen räknas på det redan höjda priset.','Kopplar logaritmisk kvot till två procentförändringar och en andragradsekvation.',fig=table(['Händelse','Pris'],[['Start','U'],['Höjning med p %','Mellanpris'],['Sänkning med p %','S']]),cases=[['50','p=50'],['25','75']])

add(1220,p('För x &gt; 2 är logaritmskillnaden från x−2 till x lika stor som från x till x+6. Bestäm x.')+eq(r'\ln x-\ln(x-2)=\ln(x+6)-\ln x'),3,
 [p('Skriv skillnaderna som logaritmer av kvoter.')+eq(r'\ln\frac{x}{x-2}=\ln\frac{x+6}{x}'),p('Argumenten är positiva. Lika logaritmer ger lika kvoter.')+eq(r'x^2=(x-2)(x+6)'),p('Utveckla och förenkla.')+eq(r'x^2=x^2+4x-12\Rightarrow x=3'),p('Kontroll: talen är då 1, 3 och 9, med samma faktor 3 mellan intilliggande tal.')],'x = 3.','Uttryck lika logaritmskillnader med hjälp av kvoter.','Översätter lika logaritmsteg till kvoter och förenklar en ekvation där kvadrattermerna försvinner.',cases=[['3','x=3'],['4','6']])

if __name__=='__main__':
 h.install(TASKS)
 (h.ROOT/'agent/MA3_LN_C_2026-10-25.json').write_text(json.dumps(REVIEW,ensure_ascii=False,indent=2)+'\n')
 (h.ROOT/'tools/ma3-ln-c-2026-10-25.cases.json').write_text(json.dumps(CASES,ensure_ascii=False,indent=2)+'\n')
