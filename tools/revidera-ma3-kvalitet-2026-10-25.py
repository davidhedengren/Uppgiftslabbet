"""Individuellt granskade ändringar; inga heuristiska massändringar."""
import importlib.util,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('h',Path(__file__).with_name('bygg-ma3-kontinuitet-2026-10-24.py'));h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
p,m,eq,sol=h.p,h.m,h.eq,h.sol
path=ROOT/'uppgiftermato1.js';raw=path.read_text();bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);Q={q['id']:q for q in bank};CHANGES={}
def edit(id,reason,**changes):Q[id].update(changes);CHANGES[id]={'ändring':reason,'fält':list(changes)}
def level(id,n,reason,grade=None,points=None):
 changes={'traningsniva':n}
 if grade:changes.update(niva=grade,poang=points)
 edit(id,reason,**changes)
# Bedöm varje metod, inte frågans längd eller ursprungliga bokstavsnivå.
level('3.182',2,'4 → 2: derivera en given funktion och jämför en koefficient.','E','2/0/0')
Q['3.182']['ledtrad']=p('Derivera F och jämför koefficienten framför x² med motsvarande koefficient i f.');CHANGES['3.182']['fält']+=['ledtrad']
level('3.194',2,'4 → 2: F′ är redan given som f. Horisontell tangent ger en enkel insättning.','E','2/0/0')
Q['3.194']['ledtrad']=p('Vilket värde ska F′ ha vid en horisontell tangent? Använd att F′ = f.');CHANGES['3.194']['fält']+=['ledtrad']
for id in ['3.283','3.551','3.617','3.727']:
 level(id,2,'1 → 2: flera termvisa operationer eller jämförelse av flera derivator; behålls som E-mängdträning.')
level('2.825',3,'4 → 3: vanlig extremvärdesundersökning med negativ potens, positiv domän och teckenkontroll.','C','0/2/0')
level('2.812',3,'5 → 3: samma metodkrav som #2.1227, en okänd tangentpunkt och en linjär ekvation efter förenkling.','C','0/2/0')
level('3.58',3,'4 → 3: kort samband mellan derivatan av en skillnad och en konstant funktion; manuell motivering kvar.','C','0/2/0')
# En bred formelrad får inte dölja mellanled på mobilen.
edit('3.283','Nivå 2 och mobilfacit med separata mellanled; svaret och primitiv-formatet oförändrade.',traningsniva=2,s=sol([p('Integrera de två termerna var för sig.')+eq(r'\int16x^3\,dx=4x^4')+eq(r'\int2x\,dx=x^2'),p('En primitiv funktion räcker. Vi kan därför välja konstanten till 0. Kontroll: derivatan av 4x⁴+x² är 16x³+2x.')],m('F(x)=4x^4+x^2')+' är ett exempel.'),ledtrad=p('Öka exponenten med ett och dividera med den nya exponenten i varje term.'))
# En skiss hjälper till att skilja den givna punkten från tangentpunkten.
fig=h.graph('Kurvan y=roten ur x och en tangent genom den givna punkten (-4,0).',(-5,10),(0,4),[[(x/10,math.sqrt(x/10)) for x in range(0,101)], [(-4,0),(10,3.5)]],[-4,0],[],dots=[(-4,0,True)],xlabel='x',ylabel='y')
# Flytta y-axeln från figurhjälparens vänsterkant till x=0.
fig=fig.replace('M65 45V250H445','M188.33333333333331 45V250 M65 250H445').replace('x="65" y="28"','x="188.33333333333331" y="28"')
fig=fig.replace('</svg>','<circle cx="287" cy="150" r="4" fill="#00749b"/>'+h.text(270,128,'P',18)+h.text(355,65,'y = √x',17)+'</svg>')
Q['2.812']['t']=p('En tangent till kurvan '+m(r'y=\sqrt x')+' går genom punkten '+m('(-4,0)')+' på x-axeln. Bestäm tangeringspunkten.')+fig
Q['2.812']['s']=sol([p('Låt tangentpunkten vara (a, √a), där a > 0. Tangentens lutning är derivatan.')+eq(r'f^{\prime}(a)=\frac1{2\sqrt a}'),p('Samma lutning kan beräknas mellan (−4, 0) och tangentpunkten.')+eq(r'\frac{\sqrt a}{a+4}=\frac1{2\sqrt a}'),p('Multiplicera med 2√a(a+4).')+eq(r'2a=a+4\quad\Rightarrow\quad a=4'),p('Då är y = √4 = 2. Tangenten har lutningen 1/4 och går genom både (−4, 0) och (4, 2).')],m('(4,2)')+'.')
CHANGES['2.812']['fält']+=['t','s'];CHANGES['2.812']['ändring']+=' Tydligare mellanled och situationsfigur.'
# Bevara en av varje exakt dubblett; variera tanke eller representation i de andra.
edit('2.740','Nära dubblett av #2.605 blir omvänd användning av samma derivata; nivå 2 kvar.',
 t=p('Funktionen är '+m(r'f(x)=\sqrt{x}')+'. Vid vilket x-värde är tangentens lutning '+m(r'\frac16')+'?'),rättSvar=9,tolerans=None,miniräknare=True,
 s=sol([p('Derivatan anger tangentens lutning.')+eq(r'f^{\prime}(x)=\frac1{2\sqrt x}'),p('Sätt derivatan lika med den efterfrågade lutningen.')+eq(r'\frac1{2\sqrt x}=\frac16'),p('Då är 2√x = 6, alltså √x = 3 och x = 9.')],m('x=9')+'.'),ledtrad=p('Här är lutningen känd och x okänt. Ställ upp en ekvation med derivatan.'))
edit('2.744','Nära dubblett av #2.585 blir kvalitativ teckenfråga för negativ x; nivå 2 kvar.',
 t=p('Funktionen är '+m('f(x)=1/x')+'. Vilket påstående om tangenternas lutning är rätt när x < 0? Välj ett alternativ.'),rättSvar=None,svarstyp='alternativ',svarFormat='text',
 alternativ=[{'txt':'Lutningen är positiv eftersom x är negativt.','ratt':False},{'txt':'Lutningen är noll eftersom inga positiva x-värden används.','ratt':False},{'txt':'Lutningen är negativ eftersom f′(x) = −1/x².','ratt':True},{'txt':'Derivatan finns inte när x är negativt.','ratt':False}],
 s=sol([p('Derivera den negativa potensen.')+eq(r'f^{\prime}(x)=-x^{-2}=-\frac1{x^2}'),p('x² är positivt även när x är negativt. Därför är −1/x² negativt. Derivatan finns för alla x utom 0.')],'Lutningen är negativ.'),ledtrad=p('Vilket tecken får kvadraten av ett negativt tal?'),formaga=['begrepp','procedur'],miniräknare=True)
edit('3.921','Exakt dubblett blir förändring mellan två x-värden; fullprecisionsmål och halv hundradels tolerans ersätter för stor tolerans.',
 t=p('F är en primitiv funktion till '+m('f(x)=e^x')+'. Hur mycket större är F(1) än F(0)? Svara med två decimaler.'),rättSvar=math.e-1,tolerans=.005,
 s=sol([p('Alla primitiva funktioner har formen F(x) = eˣ+C. Vid x = 1 är värdet e+C och vid x = 0 är det 1+C. När värdena subtraheras försvinner konstanten.')+eq(r'(e+C)-(1+C)=e-1')],m(r'F(1)-F(0)\approx1{,}72')+'.'),ledtrad=p('Skriv de två funktionsvärdena med samma konstant och subtrahera.'))
edit('3.1052','Exakt dubblett av #3.1011 blir baklängesberäkning av ett startvärde; nivå 2 kvar.',
 t=p('F är en primitiv funktion till '+m('f(x)=e^x')+' och F(1) = 6. Bestäm F(0). Svara med två decimaler.'),rättSvar=7-math.e,tolerans=.005,
 s=sol([p('Skriv F(x) = eˣ+C. Villkoret vid x = 1 ger')+eq(r'e+C=6\quad\Rightarrow\quad C=6-e'),p('Sätt sedan in x = 0.')+eq(r'F(0)=1+(6-e)=7-e')],m(r'F(0)\approx4{,}28')+'.'),ledtrad=p('Använd det kända värdet vid x = 1 för att bestämma konstanten.'))
edit('3.1063','Exakt dubblett av #3.1012 blir bestämning av skillnad utan givet startvärde; nivå 2 kvar.',
 t=p('F är en primitiv funktion till '+m('f(x)=6x^2-2x')+'. Bestäm '+m('F(2)-F(1)')+'.'),rättSvar=11,
 s=sol([p('En allmän primitiv funktion är')+eq(r'F(x)=2x^3-x^2+C'),p('Vid de två x-värdena får vi F(2) = 12+C och F(1) = 1+C. Skillnaden påverkas inte av C.')+eq(r'(12+C)-(1+C)=11')],'11.',),ledtrad=p('Du behöver inte känna C för att beräkna skillnaden.'))
edit('3.1057','Exakt dubblett av #3.1015 blir enkel vertikal förskjutning av en primitiv funktion; nivå 1 kvar.',
 t=p('F och G är primitiva funktioner till samma funktion. G:s graf ligger 3 enheter ovanför F:s graf. F(0) = 7. Vad är G(0)?'),rättSvar=10,
 s=sol([p('Vid samma x-värde är G:s funktionsvärde 3 större än F:s.')+eq(r'G(0)=F(0)+3=7+3=10')],m('G(0)=10')+'.'),ledtrad=p('Jämför grafernas höjd vid samma x-värde.'))
# Matematiska preciseringar: ingen skärpning av tecken kan härledas ur monotonin ensam.
edit('3.178','Samma intervall måste anges, i linje med den tidigare rättningen av #3.58.',t=p('Två funktioner F och G är båda primitiva funktioner på samma intervall till samma funktion f. Vad kan du säga om F−G? Motivera.'))
edit('3.198','Korrigerar slutsatsen växande ⇒ strikt positiv derivata. Enstaka nollvärden kan förekomma.',
 s=sol([p('Eftersom F är deriverbar gäller f = F′ ≥ 0 där F växer och f = F′ ≤ 0 där F avtar.'),p('Alltså är f ≥ 0 för x < −1 och x > 2, och f ≤ 0 för −1 < x < 2. En växande funktion kan ha enstaka vågräta tangenter; därför kan vi inte utesluta f = 0 inne i intervallen.'),p('F går från att växa till att avta vid x = −1, så där finns ett lokalt maximum. Vid x = 2 går F från att avta till att växa och har ett lokalt minimum. Vid båda extrempunkterna är f = 0.')],'F har lokalt maximum vid x = −1 och lokalt minimum vid x = 2. Derivatans tecken anges med ≥ respektive ≤ i intervallen.'))
edit('3.1016','Förtydligar tidsvariabeln och visar insättning och startvolym i facit. Svaret 28 liter oförändrat.',
 t=p('Vatten rinner in i en tank med hastigheten '+m('q(t)=4t')+' liter per minut, där t är antalet minuter från start. Från början finns 10 liter i tanken. Hur mycket vatten finns efter 3 minuter? Svara i liter.'),
 s=sol([p('Volymens derivata är inflödet, så V′(t) = 4t. En primitiv funktion är V(t) = 2t²+C.'),p('Från början finns 10 liter: V(0) = C = 10. Därför blir')+eq(r'V(3)=2\cdot3^2+10=28')],'28 liter.'))
edit('3.1106','Anger hastighetens enhet i frågan och svarsfältet; korrekt svar med eller utan m/s.',
 t=p('En rörelse beskrivs av '+m('s(t)=t^2+t')+' meter, där t mäts i sekunder. Bestäm hastigheten vid t = 1 s. Svara i m/s.'),svarEnhet='m/s',s=sol([p('Hastigheten är lägets derivata.')+eq(r'v(t)=s^{\prime}(t)=2t+1'),p('Sätt in t = 1.')+eq(r'v(1)=2\cdot1+1=3')],'3 m/s.'))
# Samma matematik, med korta formelrader i manuella lösningar på mobil.
Q['3.551']['s']=sol([p('Derivera förslaget F(x) = 2x³−2x²+3x term för term.')+eq(r'F^{\prime}(x)=6x^2-4x+3'),p('Det är samma funktion som f. Därför är F en primitiv funktion till f.')],m('F(x)=2x^3-2x^2+3x')+'.')
CHANGES['3.551']['fält']+=['s'];CHANGES['3.551']['ändring']+=' Mobilanpassat facit.'
edit('2.539','Delar upp derivatans potensform och bråkform i facit för mobilvisning; samma svar.',
 s=sol([p('Skriv bråket som en negativ potens.')+eq(r'f(x)=ax^2-4x^{-1}'),p('a är en konstant. Derivera termerna var för sig.')+eq(r'f^{\prime}(x)=2ax+4x^{-2}')],m(r'f^{\prime}(x)=2ax+\frac4{x^2}')+'.'))
edit('3.792','Kortare formelrader i facit för mobil; konstanten och svaret oförändrade.',
 s=sol([p('F och G har samma x²-term. När vi beräknar F−G tar dessa termer ut varandra.')+eq(r'(x^2+3)-(x^2-5)=3+5=8')],'Skillnaden F(x)−G(x) är alltid 8.'))
for id in ['3.58','3.178']:
 Q[id]['s']=sol([p('Båda funktionerna har samma derivata f. Derivatan av skillnaden blir därför')+eq(r'(F-G)^{\prime}=F^{\prime}-G^{\prime}')+eq(r'=f-f=0'),p('En funktion med derivatan 0 överallt på ett intervall är konstant där.')],m('F(x)-G(x)=C')+' på intervallet.')
 CHANGES[id]['fält']+=['s'];CHANGES[id]['ändring']+=' Kortare formelrader för mobilvisning.'
edit('3.355','Kortare formelrader i fråga och facit så båda funktionerna syns på mobil; samma matematik och nivå.',
 t=p('Två funktioner ges av')+eq(r'F_1(x)=x^3-3x+2')+eq(r'F_2(x)=x^3-3x-5')+p('Förklara varför de är primitiva funktioner till samma funktion f, och bestäm det lodräta avståndet mellan deras grafer.'),
 s=sol([p('Derivera funktionerna var för sig.')+eq(r'F_1^{\prime}(x)=3x^2-3')+eq(r'F_2^{\prime}(x)=3x^2-3'),p('De har samma derivata och är därför primitiva funktioner till f(x) = 3x²−3.'),p('Termerna x³−3x är lika. Skillnaden är därför bara skillnaden mellan konstanterna.')+eq(r'F_1(x)-F_2(x)=2-(-5)=7')],'Graferna ligger 7 enheter från varandra i höjdled.'))
# Endast berörda objekt serialiseras; orelaterade bankobjekt bevaras.
if __name__=='__main__':
 for id in CHANGES:
  pos=raw.index('"id": "'+id+'"');start=raw.rfind('{',0,pos);old,n=json.JSONDecoder().raw_decode(raw[start:])
  indent=raw[raw.rfind('\n',0,start)+1:start]
  replacement=json.dumps(Q[id],ensure_ascii=False,indent=2).replace('\n','\n'+indent)
  raw=raw[:start]+replacement+raw[start+n:]
 path.write_text(raw)
 (ROOT/'agent/MA3_KVALITET_2026-10-25.andringar.json').write_text(json.dumps(CHANGES,ensure_ascii=False,indent=2)+'\n')
 print(len(CHANGES),list(CHANGES))
