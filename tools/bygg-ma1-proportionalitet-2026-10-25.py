"""Åtta olika problemlösningsidéer efter inventering av nivån kring Ma1 8.18."""
import importlib.util,json,math
from pathlib import Path
spec=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
p,m,eq,sol,table,graph,svg,text=h.p,h.m,h.eq,h.sol,h.table,h.graph,h.svg,h.text
TASKS=[]
def add(id,t,answer,steps,final,hint,fig='',unit=None,precision=None):
 q=h.make('0.'+str(id),'proportionalitet_grunder','Proportionalitet i problemlösning',3,t,answer,steps,final,hint,fig=fig,unit=unit,skills=['problemlösning','modellering']);q.update(kap=0,kurs=['1a','1b','1c'],arbetsinsats=2)
 if precision is not None:q['tolerans']=.5*10**(-precision)
 TASKS.append(q)
fig=svg('Två pumpar fyller samma tank. Pump A ger 45 liter på 3 minuter och pump B 60 liter på 5 minuter.',
 '<path d="M175 130V240H325V130" fill="#e8f5fb" stroke="#172e46" stroke-width="3"/>'+
 '<path d="M90 75H220V150 M410 75H280V150" fill="none" stroke="#096c9a" stroke-width="5"/>'+
 '<path d="M214 142L220 153L226 142 M274 142L280 153L286 142" fill="none" stroke="#096c9a" stroke-width="3"/>'+
 text(105,35,'Pump A')+text(105,60,'45 L på 3 min',16)+text(395,35,'Pump B')+text(395,60,'60 L på 5 min',16)+text(250,205,'300 L'),270)
add(1253,p('Två pumpar fyller en tom tank samtidigt. Pump A ger 45 liter på 3 minuter och pump B 60 liter på 5 minuter. Båda har konstant flöde. Hur lång tid tar det att fylla tanken med 300 liter? (Svara i minuter med en decimal.)'),300/27,
 [p('Räkna först om båda flödena till liter per minut.')+eq(r'45/3=15\qquad60/5=12'),p('Tillsammans ger pumparna 15+12 = 27 liter per minut.')+eq(r't=300/27\approx11{,}1')],'11,1 min.','Lägg ihop flöden som anges i samma enhet.',fig=fig,unit='min',precision=1)
add(1254,p('Receptet gäller 12 portioner. Du har 2 000 g mjöl och 900 g socker. Övriga ingredienser räcker. Hur många hela portioner kan du som mest göra om proportionerna i receptet ska behållas?'),32,
 [p('Per portion går det åt 750/12 = 62,5 g mjöl och 300/12 = 25 g socker.'),p('Mjölet räcker till 2 000/62,5 = 32 portioner. Sockret räcker till 900/25 = 36 portioner. Det är alltså mjölet som begränsar antalet.')],'32 portioner.','Kontrollera hur många portioner varje ingrediens räcker till.',fig=table(['Ingrediens','Till 12 portioner'],[['Mjöl','750 g'],['Socker','300 g']]))
fig=graph('Gångsträckan ökar från 0 till 3 km under den första timmen och är sedan konstant fram till 1,5 timmar.',(0,2),(0,4),[[(0,0),(1,3),(1.5,3)]],[0,.5,1,1.5,2],[0,1,2,3,4],xlabel='Tid från start (h)',ylabel='Gångsträcka (km)')
add(1255,p('Grafen visar en vandrings första 1,5 timmar, inklusive en paus. Efter pausen fortsätter gruppen med samma gångfart som före pausen och utan fler stopp. Hur lång tid från starten tar det att gå totalt 9 km? (Svara exakt i timmar.)'),3.5,
 [p('Gruppen går 3 km på 1 timme, alltså 3 km/h. Den vågräta delen visar en paus på 0,5 timmar.'),p('Att gå 9 km tar 9/3 = 3 timmar i rörelse. Lägg till pausen.')+eq(r'3+0{,}5=3{,}5')],'3,5 h.','Skilj mellan tid i rörelse och tid för pausen.',fig=fig,unit='h')
add(1256,p('En färgblandning innehåller 2,4 liter vit färg och 0,8 liter blå färg. Du råkar hälla i ytterligare 0,4 liter blå färg. Hur mycket vit färg måste du tillsätta för att få tillbaka samma förhållande mellan färgerna? (Svara i liter.)'),1.2,
 [p('Från början går det 2,4/0,8 = 3 liter vit färg på varje liter blå.'),p('Den nya mängden blå färg är 0,8+0,4 = 1,2 liter. Då behövs 3·1,2 = 3,6 liter vit färg totalt.'),p('Det finns redan 2,4 liter vit färg.')+eq(r'3{,}6-2{,}4=1{,}2')],'1,2 liter.','Hur många liter vit färg behövs per liter blå?',unit='L')
add(1257,p('En karta i skala 1:40 000 skrivs ut så att alla längder på papperet blir 80 % av de ursprungliga. Vilken skala får den nya utskriften? Ange talet som ska stå efter 1:.'),50000,
 [p('En sträcka som tidigare var 1 cm på kartan blir 0,8 cm. Den motsvarar fortfarande 40 000 cm i verkligheten.'),p('En centimeter på den nya kartan motsvarar därför')+eq(r'40\,000/0{,}8=50\,000\text{ cm}')],'1:50 000.','Följ en bestämd sträcka på kartan genom förminskningen.')
add(1258,p('En drönare har använt 20 % av ett fulladdat batteri för att flyga 12 km. Den står nu stilla med 80 % kvar. Anta att batteriåtgången per kilometer är oförändrad och att stillastående inte drar batteri. Hur långt kan den flyga ytterligare om minst 25 % av batteriet ska finnas kvar? (Svara i km.)'),33,
 [p('Av de 80 procenten som återstår får 80−25 = 55 procentenheter användas.'),p('20 procentenheter räcker till 12 km. Den återstående tillåtna sträckan blir')+eq(r'12\cdot\frac{55}{20}=33')],'33 km.','Räkna först ut hur stor del av hela batteriet som får användas nu.',unit='km')
add(1259,p('Ett liggande foto är 18 cm brett och 12 cm högt. Det ska förstoras utan att beskäras eller vridas och få plats i en öppning som är 44 cm bred och 31 cm hög. Hur stort blir det sammanlagda tomrummet ovanför och under fotot om fotot görs så stort som möjligt? (Svara i cm med en decimal.)'),31-44*12/18,
 [p('Om fotot fyller öppningens bredd blir höjden')+eq(r'h=44\cdot\frac{12}{18}\approx29{,}33\text{ cm}'),p('Den höjden ryms inom 31 cm. Bredden begränsar därför hur stor bilden kan bli. Tomrummet ovanför och under blir sammanlagt')+eq(r'31-29{,}33\ldots\approx1{,}7\text{ cm}')],'1,7 cm.','Kontrollera vilken av öppningens två dimensioner som begränsar förstoringen.',unit='cm',precision=1)
add(1260,p('Lea går en sträcka med farten 4 km/h och kommer fram efter 45 minuter. Sam går samma sträcka med farten 6 km/h, men startar 10 minuter efter Lea. Båda håller konstant fart. Hur många minuter före Lea kommer Sam fram?'),5,
 [p('Lea går i 45/60 = 0,75 timmar. Sträckan är därför 4·0,75 = 3 km.'),p('Sam behöver 3/6 = 0,5 timmar, alltså 30 minuter. Räknat från Leas start kommer han fram efter 10+30 = 40 minuter.'),p('Lea kommer fram efter 45 minuter, så skillnaden är 45−40 = 5 minuter.')],'5 minuter.','Ta reda på sträckan och skilj sedan mellan gångtid och starttid.',unit='min')
if __name__=='__main__':
 path=h.ROOT/'uppgifterma1.js';raw=path.read_text();bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);assert not {q['id'] for q in TASKS}&{q['id'] for q in bank}
 end=raw.rindex(']');path.write_text(raw[:end].rstrip()+','+json.dumps(TASKS,ensure_ascii=False,indent=2)[1:-1]+'\n'+raw[end:]);print([q['id'] for q in TASKS])
