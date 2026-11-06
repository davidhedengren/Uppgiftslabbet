"""Avgränsade, manuellt granskade rättningar. Ingen heuristisk massändring."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
IDS={'ma1':['0.329','0.403','0.727','0.728','6.405','7.38','7.437','1.1187'],
     'ma2':['2.568','2.721','3.104','3.106','3.328'],
     'mato1':['2.800','3.551','3.727'],'mato2':['4.460'],
     'matf1':['4.513','4.587','4.588'],
     'fy1':['4.824','4.828','3.442','2.345'],'fy2':['3.521','4.305','4.317']}
FILES={b:('uppgifter.js' if b=='fy1' else 'uppgifter2.js' if b=='fy2' else 'uppgifter'+b+'.js') for b in IDS}
def I(x):return r'\('+x+r'\)'
def st(title,text,math=''):
    return '<li><p class="facit-rubrik">'+title+'</p><p>'+text+'</p>'+('' if not math else '<div class="facit-matte">'+r'\['+math+r'\]'+'</div>')+'</li>'
def sol(steps,answer):
    return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'.</p></div>'

COMMENTS={
('ma1','0.329'):['Talfaktorn 0,42 är mindre än 1.','Talfaktorn 42 är inte mindre än 10.',None],
('ma1','0.403'):[None,'2,405 är mindre än 2,490.','2,505 är större än 2,500.','2,59 är större än 2,50.'],
('ma1','0.727'):['3,15 avrundas till 3,2.','3,24 avrundas till 3,2.','3,2 är redan angivet med en decimal.',None],
('ma1','0.728'):['45 ligger mitt mellan 40 och 50 och avrundas uppåt till 50.','53 avrundas till 50.','46 avrundas till 50.',None],
('ma1','6.405'):[None,'Bara 14 divideras med 3, inte hela summan.','14 multipliceras med 6+10 i stället för att adderas.','6 ligger utanför divisionen. Hela summan ska delas med 3.'],
('ma1','7.38'):['750 mg = 0,750 g, mindre än 0,850 g.','0,80 g är mindre än 0,850 g.','Massorna är 0,750 g, 0,800 g och 0,850 g.',None],
('ma1','7.437'):['0,1 kg motsvarar ungefär en deciliter vatten, inte tio liter.','100 kg motsvarar ungefär hundra liter vatten.',None,'1 kg motsvarar ungefär en liter vatten.'],
('ma2','2.568'):['En uppåtvänd parabel har positiv koefficient framför x².',None,'Uttrycket innehåller en term med x² och ger en parabel.'],
('ma2','2.721'):[None,'Vid x = −2 blir vänsterledet 2 men högerledet −2.','x = −2 uppfyller inte ursprungsekvationen.','x = 3 ger √9 = 3 och är en lösning.'],
('ma2','3.106'):[None,'x = 3 uppfyller B men inte A.','Ekvivalens kräver båda riktningarna. x = 3 visar att B inte medför A.','A medför B: varje tal större än 5 är också större än 2.'],
('ma2','3.328'):[None,'Kvadrater bekräftar påståendet i några fall men motbevisar det inte.','En triangel är inte en fyrhörning.','En cirkel är inte en fyrhörning.'],
('mato1','2.800'):[None,'Lutningen använder skillnaden mellan funktionsvärdena, inte summan.','Ändringen i funktionsvärde måste divideras med ändringen h i x.','Punkterna ska närma sig varandra: h ska gå mot 0, inte mot oändligheten.'],
('mato2','4.460'):[None,'x+2 skulle kräva nollstället −2, vilket inte är givet.','2x−1 skulle kräva nollstället 1/2, vilket inte är givet.','P(2)=0 säger inget om faktorn x²+2. Polynomet P(x)=x−2 är ett motexempel.'],
('matf1','4.513'):[None,'Vid t = 0 blir v = 19,64. Begynnelsevillkoret v(0)=0 uppfylls inte.','Vid t = 0 är derivatan 0, men ekvationen kräver v′(0)=9,82.','Derivatan är 0,50, men ekvationen kräver v′(0)=9,82.'],
('fy2','4.305'):['Från luft till glas minskar vinkeln mot normalen, den ökar inte.',None,'Vid snett infall ändras riktningen när brytningsindex ändras.','Totalreflektion kan inte ske när ljuset går från luft till glas med högre brytningsindex.'],
('fy2','4.317'):['Radiovågor har samma fart c som synligt ljus i vakuum.','Alla typer av elektromagnetiska vågor kan färdas i vakuum.','Gammastrålning har samma fart c som övriga elektromagnetiska vågor i vakuum.',None]}

def edit(b,q):
    id=q['id']
    if b=='fy1' and id=='3.32':
        q['t']=q['t'].replace('accelererar i 6 s','accelererar med konstant acceleration i 6 s').replace('bromsar därefter till stillastående på 4 s','bromsar därefter med konstant acceleration till stillastående på 4 s')
        q['s']=q['s'].replace('Brytpunkter i diagrammet','Räta linjer mellan brytpunkterna').replace('två trianglar triangel','två trianglar med arean').replace('en rektangel rektangel','en rektangel med arean')
        return
    q['visaAlternativ']=True
    q['t']=q['t'].replace('Välj alla som stämmer.','Välj alla alternativ som stämmer.')
    if not re.search('Välj.*alternativ',q['t']):q['t']+='<p>Välj ett alternativ.</p>'
    for a,c in zip(q['alternativ'],COMMENTS.get((b,id),[])):
        if c:a['kommentar']=c
    if b=='ma1':
        if id=='0.329':
            q['s']=sol([st('Grundpotensform: '+I(r'a\cdot10^n,\quad1\le a\lt10'),'Talfaktorn 4,2 ligger i rätt intervall. 0,42 är för liten och 42 är för stor. Alla uttrycken har samma värde, men bara ett är skrivet i grundpotensform.')],I(r'4{,}2\cdot10^5'))
        elif id=='0.403':
            q['t']=q['t'].replace('Vilket tal ligger','Vilket av talen ligger')
            q['s']=sol([st('Jämför med samma antal decimaler','Skriv gränserna som 2,490 och 2,500. Endast det första alternativet ligger mellan dem.',r'2{,}490\lt2{,}495\lt2{,}500')],'2,495')
        elif id=='0.727':
            q['s']=sol([st('Avrunda varje alternativ till tiondelar','Hundradelssiffran avgör om tiondelen behålls eller ökas.',r'\begin{aligned}3{,}15&\approx3{,}2\\3{,}24&\approx3{,}2\\3{,}2&=3{,}2\\3{,}26&\approx3{,}3\end{aligned}')],'3,26')
        elif id=='0.728':
            q['s']=sol([st('Avrunda varje alternativ till tiotal','Jämför avståndet till de närmaste tiotalen. Vid lika avstånd avrundas dessa positiva tal uppåt.',r'\begin{aligned}45&\approx50\\53&\approx50\\46&\approx50\\44&\approx40\end{aligned}')],'44')
        elif id=='6.405':
            q['s']=sol([st('Medelvärde: '+I(r'\bar x=\frac{\text{summan}}{\text{antalet}}'),'Alla tre talen ska först adderas. Parenteserna gör att programmet dividerar hela summan med 3.',r'\frac{6+10+14}{3}=\frac{30}{3}=10')],'<code>(6+10+14)/3</code>')
        elif id=='7.38':
            q['s']=sol([st('Jämför massorna i gram','Använd samma enhet för alla tre massor.',r'\begin{aligned}750\text{ mg}&=0{,}750\text{ g}\\0{,}80\text{ g}&=0{,}800\text{ g}\\850\,000\text{ µg}&=0{,}850\text{ g}\end{aligned}'),st('Jämför talvärdena','0,850 är större än både 0,800 och 0,750.')],'850 000 µg')
        elif id=='7.437':
            q['ledtrad']='<p>Utgå från vad ungefär en liter vatten väger.</p>'
            q['s']=sol([st('En liter vatten väger ungefär ett kilogram','Tio liter vatten väger därför ungefär tio kilogram. Hinkens egen vikt ändrar inte vilket av de grova alternativen som är rimligt.',r'10\cdot1\text{ kg}=10\text{ kg}')],'Cirka 10 kg')
        else:
            q['t']=q['t'].replace('Tre elever beskriver antalet grå plattor runt en kvadratisk uteplats med sidan \\(s\\) plattor (se figuren).','En kvadratisk uteplats har sidan \\(s\\) plattor, inklusive den grå ramen. De yttersta plattorna är grå (se figuren).')
            q['s']=sol([st('Fyra sidor, men räkna varje hörn en gång','Fyra sidor med s plattor ger 4s. Då räknas de fyra hörnen två gånger, så fyra måste dras bort.',r'4s-4=4(s-1)'),st('Hela kvadraten minus insidan','Det finns s² plattor totalt. Den vita insidan har sidan s−2.',r'\begin{aligned}s^2-(s-2)^2&=s^2-(s^2-4s+4)\\&=4s-4\end{aligned}'),st('Kontrollera det fjärde uttrycket','4s räknar hörnen två gånger. Vid s=3 blir det 12, fast figuren har 8 grå plattor.')],I(r'4(s-1)')+', '+I(r'4s-4')+' och '+I(r's^2-(s-2)^2'))
    elif b=='ma2':
        if id=='2.568':q['s']=sol([st('Andragradsfunktion: '+I(r'f(x)=ax^2+bx+c'),'Här är a = −2. En negativ koefficient framför x² gör parabeln nedåtvänd.')],'Parabeln är nedåtvänd')
        elif id=='2.721':q['s']=sol([st('Kontrollera i '+I(r'\sqrt{x+6}=x'),'Kvadrering kan ge falska rötter. Kontrollera därför båda föreslagna värdena i ursprungsekvationen.',r'\begin{aligned}x=3:\quad\sqrt{3+6}&=3\\x=-2:\quad\sqrt{-2+6}&=2\ne-2\end{aligned}')],'Bara x = 3 är en lösning')
        elif id=='3.104':
            q['s']=sol([st('Pröva '+I(r'A\Rightarrow B'),'Om x är större än 4 är x positivt och dess kvadrat större än 16. Denna riktning gäller.'),st('Pröva '+I(r'B\Rightarrow A'),'Ett negativt tal kan också ha en kvadrat större än 16. Ett motexempel räcker.',r'(-5)^2=25\gt16,\qquad-5\not\gt4')],'Endast A ⇒ B är sann')
        elif id=='3.106':
            q['s']=sol([st('Pröva '+I(r'A\Rightarrow B'),'Ett tal större än 5 är också större än 2.'),st('Pröva '+I(r'B\Rightarrow A'),'Talet 3 är större än 2, men inte större än 5. Det är ett motexempel till den omvända riktningen.')],'A medför B, men B medför inte A')
            q['ledtrad']='<p>Pröva riktningarna var för sig. Ett enda motexempel räcker för att en riktning inte ska gälla.</p>'
        else:q['s']=sol([st('Ett motexempel måste vara en fyrhörning','En rektangel som inte är en kvadrat har två olika sidlängder. Den uppfyller därför inte påståendet om fyra lika långa sidor.'),st('Varför räcker inte de andra förslagen?','Kvadrater har fyra lika långa sidor. Triangeln och cirkeln är inte fyrhörningar och säger därför inget om påståendet.')],'En rektangel som inte är en kvadrat')
    elif b=='mato1':
        if id=='2.800':q['s']=sol([st('Sekantens lutning: '+I(r'\frac{\Delta y}{\Delta x}'),'Punkterna har x-koordinaterna a och a+h. Ändringen i x är h och ändringen i funktionsvärde är f(a+h)−f(a).',r'\frac{\Delta y}{\Delta x}=\frac{f(a+h)-f(a)}{h}'),st('Låt avståndet mellan punkterna gå mot noll','Gränsvärdet av sekantens lutning är derivatan, om gränsvärdet finns.',r"f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h")],q['alternativ'][0]['txt'].replace('\\\\','\\'))
        elif id=='3.551':q['s']=q['s'].replace('Derivera det föreslagna polynomet','Kontrollera att '+I(r"F'(x)=f(x)"))
        else:q['s']=q['s'].replace('En primitiv funktion ska ge x³ − 2x vid derivering','Kontrollera att '+I(r"F'(x)=f(x)"))
    elif b=='mato2':q['s']=sol([st('Faktorsatsen: '+I(r'P(a)=0\Leftrightarrow(x-a)\text{ är en faktor}'),'Det givna nollstället är a = 2. Sätt in det i faktorn x−a.')],I('x-2'))
    elif b=='matf1':
        if id=='4.513':
            q['miniräknare']=True
            q['ledtrad']='<p>Pröva begynnelsevillkoret. Derivera sedan förslaget och jämför med differentialekvationens högerled.</p>'
            q['alternativ'][0]['txt']=r'\(v=19{,}64(1-e^{-0{,}50t})\)'
            q['s']=sol([st('Kontrollera begynnelsevillkoret '+I('v(0)=0'),'Pröva förslaget med faktorn 1−e upphöjt till −0,50t.',r'v(0)=19{,}64(1-1)=0'),st('Derivera: '+I(r'(e^{kt})^{\prime}=ke^{kt}'),'Konstanttermen försvinner och exponentialtermen ger',r'v^{\prime}(t)=9{,}82e^{-0{,}50t}'),st('Sätt förslaget i högerledet','Multiplicera in 0,50 i parentesen och samla termerna. Högerledet blir samma uttryck som derivatan.',r'\begin{aligned}&9{,}82-0{,}50v\\&=9{,}82-9{,}82\\&\quad+9{,}82e^{-0{,}50t}\\&=9{,}82e^{-0{,}50t}\end{aligned}')],I(r'v=19{,}64(1-e^{-0{,}50t})'))
        # Behåll tidigare fullständiga verifieringar och villkoret att likheten
        # måste gälla på ett intervall, inte bara vid en enstaka punkt.
        elif id=='4.587':q['s']=q['s'].replace('Pröva y=x²','Pröva '+I(r'y=x^2'))
        else:q['s']=q['s'].replace('Pröva sinus med argumentet 3x','Pröva '+I(r'y=\sin(3x)'))
    elif b=='fy1':
        if id=='4.828':
            q['s']=sol([st('Newtons tredje lag: '+I(r'\vec F_{A\text{ på }B}=-\vec F_{B\text{ på }A}'),'När A påverkar B med en kraft påverkar B samtidigt A med en lika stor, motsatt riktad kraft. Krafterna verkar på olika föremål och tar därför inte ut varandra på ett enskilt föremål.')],'De verkar på olika föremål')
            q['alternativ'][1]['kommentar']='Kraften verkar på B och motkraften på A. De tar därför inte ut varandra på ett och samma föremål.'
    elif b=='fy2':
        q.update({'miniräknare':True,'geogebra':False})
        if id in ['4.305','4.317']:q['traningsniva']=1;q['arbetsinsats']=1
        if id=='4.305':
            q['ledtrad']='<p>Vinklarna mäts från normalen. Fundera på hur ljusets fart ändras när det går från luft till glas.</p>'
            q['s']=sol([st('Snells lag: '+I(r'n_1\sin\theta_1=n_2\sin\theta_2'),'Glas har högre brytningsindex än luft. Därför måste sinus för brytningsvinkeln vara mindre än sinus för infallsvinkeln.',r'\sin\theta_2=\frac{n_1}{n_2}\sin\theta_1'),st('Jämför vinklarna mot normalen','Brytningsvinkeln är mindre än infallsvinkeln. Strålen bryts alltså mot normalen.')],'Strålen bryts mot normalen')
        elif id=='4.317':
            q['ledtrad']='<p>Skilj på vågens fart, frekvens och våglängd. Frågan gäller vakuum.</p>'
            q['s']=sol([st('Vågsambandet i vakuum: '+I(r'c=f\lambda'),'Alla elektromagnetiska vågor har samma fart c i vakuum. Radiovågor, synligt ljus och gammastrålning skiljer sig i frekvens och våglängd, inte i fart.')],'Alla elektromagnetiska vågor har samma hastighet i vakuum')
        else:q['s']=sol([st('Laddningar i rörelse påverkas av magnetfältet','Magnetkraften skiljer laddningarna åt i staven. Därför uppstår en spänning mellan ändarna P och Q även om kretsen är öppen.'),st('En öppen strömbrytare bryter strömvägen','Ström kan inte gå runt kretsen när strömbrytaren är öppen. Spänning mellan två punkter kräver däremot inte en sluten krets.')],'Det finns spänning mellan P och Q, men ingen ström runt kretsen')

if __name__=='__main__':
    for b,ids in IDS.items():
        ids=ids+(['3.32'] if b=='fy1' else [])
        p=ROOT/FILES[b];s=p.read_text();decoder=json.JSONDecoder();pos=s.index('[')+1;patch=[];found=[]
        while True:
            while s[pos].isspace() or s[pos]==',':pos+=1
            if s[pos]==']':break
            q,end=decoder.raw_decode(s,pos)
            if q['id'] in ids:
                assert not q.get('visaAlternativ'),'Redan rättad: '+q['id']
                edit(b,q);patch.append((pos,end,json.dumps(q,ensure_ascii=False,indent=2)));found.append(q['id'])
            pos=end
        assert set(found)==set(ids)
        for start,end,new in reversed(patch):s=s[:start]+new+s[end:]
        p.write_text(s);print(b,', '.join(found))
