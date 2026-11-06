"""Ma2 4.257: förklara metodvalet; fyra nya tillämpningar utan gissade medelvärden."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def math(s):return '<div class="facit-matte">\\['+s+'\\]</div>'
def step(title,body):return '<li><p class="facit-rubrik">'+title+'</p>'+body+'</li>'
def img(slug,alt):return '<span class="fig"><img src="bilder/geogebra-'+slug+'.png" alt="'+alt+'" style="width:100%;max-width:560px;height:auto"/></span>'
def solution(steps,answer):return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
MENU='<p>Öppna geogebra.org/classic. Klicka på menyknappen ☰, välj <strong>Perspektiv</strong> och sedan <strong>Sannolikhet</strong>. Välj <strong>Normalfördelning</strong>.</p>'+img('sannolikhet-perspektiv','GeoGebra: menyknappen, Perspektiv och Sannolikhet är markerade.')
def geo(title,mu,sigma,lo,hi,slug,result,mode='Intervall'):
    return step(title,'<p>Skriv '+mu+' i μ-fältet (1) och '+sigma+' i σ-fältet (2). Tryck Enter efter varje tal. Välj <strong>'+mode+'</strong> (3), och skriv '+lo+' respektive '+hi+' som gränser (4). Efter likhetstecknet (5) visas '+result+'. GeoGebra skriver decimaler med punkt.</p>'+img(slug,'GeoGebras sannolikhetskalkylator: μ = '+mu+', σ = '+sigma+', gränser '+lo+' och '+hi+', läge '+mode+', andel '+result+'. Markeringarna visar fälten och knappen.'))

def build(bank):
    q=next(q for q in bank if q['id']=='4.257')
    figure=re.search(r'<div class="fig smal">[\s\S]*?</div>',q['t']).group(0)
    old=json.loads(json.dumps(q));lis=re.findall(r'<li>[\s\S]*?</li>',q['s'])
    # Behåll den redan verifierade GeoGebra-bilden och instruktionerna till den.
    start=next(i for i,s in enumerate(lis) if 'Öppna Sannolikhetskalkylatorn för skruvarnas diameter' in s)
    geo_old=lis[start:start+4]
    geo_old[1]=geo_old[1].replace('Pröva medelvärdet μ = 5,90 med σ = 0,05','Kontrollera det härledda medelvärdet μ = 5,90')
    old['t']=old['t'].replace('Bestäm ungefär det minsta möjliga medelvärdet.</p>', 'Bestäm ungefär det minsta möjliga medelvärdet. Svara i mm med två decimaler.</p>')
    old['s']=solution([
      step(r'Börja vid mittpunkten: \(\frac{5{,}85+6{,}05}{2}=5{,}95\)',
           '<p>Om medelvärdet är 5,95 mm ligger båda gränserna 0,10 mm från det. Med σ = 0,05 mm är det två standardavvikelser åt varje håll. Då ligger ungefär 95,4 % i intervallet, för mycket jämfört med de givna 84 procenten. Medelvärdet måste alltså ligga på ena sidan om mittpunkten.</p>'+img('4-257-mitt','GeoGebra med μ = 5,95, σ = 0,05 och intervallet 5,85–6,05 visar 0.9545, cirka 95,45 %.')),
      step(r'Intervallets bredd är \(4\sigma\)',math(r'6{,}05-5{,}85=0{,}20=4\cdot0{,}05')+'<p>Vi söker fyra intilliggande standardavvikelseband som tillsammans ger ungefär 84 %.</p>'),
      step(r'Fyra band från \(\mu-\sigma\) till \(\mu+3\sigma\)',
           '<p>I figuren finns två mittband på 34,13 %, följda av 13,59 % och 2,14 % på samma sida. De fyra banden ger:</p>'+math(r'\begin{gathered}34{,}13+34{,}13+13{,}59+2{,}14\\=83{,}99\end{gathered}')+'<p>Summan är ungefär 84 %. Den lägre möjliga mittpunkten fås därför när 5,85 ligger en standardavvikelse under medelvärdet.</p>'),
      step(r'Lös \(\mu-0{,}05=5{,}85\)',math(r'\mu=5{,}85+0{,}05=5{,}90\ \text{mm}')+'<p>Kontrollera även övre gränsen:</p>'+math(r'5{,}90+3\cdot0{,}05=6{,}05')+'<p>Det är så 5,90 hittas – båda intervallgränserna passar de valda banden.</p>'),
      *geo_old,
      step(r'Symmetrin ger även \(\mu=6{,}00\)',
           '<p>Spegelvänd de fyra banden: tre ligger under medelvärdet och ett över. Då får vi:</p>'+math(r'\mu=5{,}85+3\cdot0{,}05=6{,}00\ \text{mm}')+'<p>5,90 och 6,00 ligger lika långt från intervallets mittpunkt 5,95 och ger samma andel. När medelvärdet flyttas längre från mittpunkten minskar andelen i det fasta intervallet. Därför väljer vi den mindre av de två placeringarna. Andelen 84 % och figurens procenttal är avrundade; resultaten är ungefärliga.</p>'),
      step('Alternativ: sök systematiskt från 5,95 i GeoGebra',
           '<p>Om du inte känner igen procentbanden: behåll σ = 0,05 och intervallet 5,85–6,05. Börja med mittpunkten och minska μ, eftersom vi söker den mindre lösningen.</p><table><thead><tr><th>μ (mm)</th><th>Andel i intervallet</th></tr></thead><tbody><tr><td>5,950</td><td>95,45 %</td></tr><tr><td>5,925</td><td>92,70 %</td></tr><tr><td>5,900</td><td>84,00 %</td></tr><tr><td>5,875</td><td>69,12 %</td></tr></tbody></table><p>Du vet alltså var du börjar, åt vilket håll du ska ändra och att du ska stanna vid ungefär 84 %.</p>')],
      'Det minsta medelvärdet är ungefär 5,90 mm.')
    rows=[]
    def new(id,text,steps,answer,hint,level,right,unit,tol):
        d=dict(id=id,kap=4,omr='normalfordelat_material',kurs=['2a','2b','2c'],niva='C',poang='0/3/0',familj='Svansar och standardavvikelse',formaga=['begrepp','problemlösning'],miniräknare=True,geogebra=True,spel=True,självrättning=True,traningsniva=level,arbetsinsats=3,t=text+'<p>Figuren visar ungefärliga andelar i en normalfördelning.</p>'+figure,s=solution(steps,answer),ledtrad='<p>'+hint+'</p>',svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=right,svarEnhet=unit,tolerans=tol)
        rows.append(d);return d
    d=new('4.2148','<p>En maskin kapar metallstift. Längderna är normalfördelade med standardavvikelsen 2 mm. Ungefär 84 % av stiften är mellan 48 och 56 mm långa.</p><p>Vilka två ungefärliga medelvärden är möjliga? Ange båda i mm.</p>',[
      step(r'Mittpunkten \(52\) ger för stor andel',math(r'\frac{48+56}{2}=52')+math(r'56-48=8=4\cdot2')+'<p>Intervallet är fyra standardavvikelser brett. Med μ = 52 är gränserna μ−2σ och μ+2σ. Då ligger cirka 95,4 % mellan dem, inte 84 %.</p>'),
      step(r'Välj fyra band: \(\mu-\sigma\) till \(\mu+3\sigma\)',math(r'\begin{gathered}34{,}13+34{,}13+13{,}59+2{,}14\\=83{,}99\end{gathered}')+'<p>De fyra banden ger ungefär 84 %. Nedre gränsen ligger då en standardavvikelse under medelvärdet.</p>'),
      step(r'Den lägre placeringen uppfyller \(\mu-2=48\)',math(r'\mu=50\ \text{mm}')+'<p>Övre gränsen stämmer också: 50+3·2=56 mm.</p>'),
      step(r'Spegelvänd kring \(52\)',math(r'\mu=48+3\cdot2=54\ \text{mm}')+'<p>Nu ligger tre band under medelvärdet och ett över. Även 54+2=56 mm stämmer. Andelen avtar åt båda håll när medelvärdet flyttas från 52, så dessa är de två motsvarande placeringarna.</p>'),
      step('Öppna GeoGebra för att kontrollera stiftens båda medelvärden',MENU),
      geo('Kontrollera stiften med μ = 50','50','2','48','56','ma2-4-2148-lag','0.84'),
      geo('Ändra till μ = 54 och jämför','54','2','48','56','ma2-4-2148-hog','0.84')],
      'Medelvärdet kan vara ungefär 50 mm eller 54 mm.',
      'Hur brett är intervallet uttryckt i standardavvikelser? Använd symmetrin för att hitta två placeringar.',4,[50,54],['mm','mm'],[.02,.02])
    d.update(svarstyp='flera_delar',svarFormat=['numeriskt','numeriskt'],svarsstruktur='mängd')
    new('4.2149','<p>Vikten hos frallor är normalfördelad med standardavvikelsen 10 g. Ungefär 81,85 % väger mellan 190 och 220 g. Medelvikten är större än 205 g.</p><p>Bestäm ungefär medelvikten i gram.</p>',[
      step(r'Bredden är \(220-190=3\sigma\)',math(r'220-190=30=3\cdot10')+'<p>Tre intilliggande band ska alltså ge ungefär 81,85 %.</p>'),
      step(r'Banden \(\mu-2\sigma\) till \(\mu+\sigma\) passar',math(r'13{,}59+34{,}13+34{,}13=81{,}85')+'<p>Med två band under medelvärdet och ett över blir medelvärdet högre än intervallets mittpunkt 205.</p>'),
      step(r'Lös \(\mu-2\cdot10=190\)',math(r'\mu=210\ \text{g}')+'<p>Kontroll av övre gränsen: 210+10=220 g. Spegelplaceringen skulle ge 200 g, men den strider mot villkoret att medelvärdet är större än 205 g.</p>'),
      step('Öppna sannolikhetskalkylatorn för frallornas vikt',MENU),
      geo('Kontrollera intervallet för frallor med μ = 210','210','10','190','220','ma2-4-2149','0.8186'),
      step('Tolka skillnaden mellan 81,85 % och 81,86 %','<p>GeoGebra ger cirka 81,86 %. Figurens band och uppgiftens andel är avrundade, så medelvikten är ungefär 210 g.</p>')],
      'Medelvikten är ungefär 210 g.',
      'Summera tre intilliggande band. Vilken av de två spegelvända placeringarna ger en medelvikt över 205 g?',4,210,'g',.05)
    new('4.2150','<p>En maskin fyller flaskor. Volymen är normalfördelad med medelvärdet 500 ml och standardavvikelsen 5 ml. Medelvärdet ska sänkas, men standardavvikelsen ska vara kvar på 5 ml.</p><p>Minst cirka 84 % av flaskorna ska fortfarande innehålla mellan 490 och 510 ml. Ungefär hur mycket kan medelvärdet som mest sänkas? Svara i ml.</p>',[
      step(r'Nu är intervallet \(\mu\pm2\sigma\)',math(r'\begin{gathered}490=500-2\cdot5\\510=500+2\cdot5\end{gathered}')+'<p>Från början ligger cirka 95,4 % inom gränserna. När medelvärdet sänks från mittpunkten 500 minskar andelen. Största sänkningen fås när andelen når cirka 84 %.</p>'),
      step(r'Behåll bredden \(4\sigma\) och flytta mittpunkten',math(r'\begin{gathered}34{,}13+34{,}13+13{,}59+2{,}14\\=83{,}99\end{gathered}')+'<p>Fyra band från μ−σ till μ+3σ ger ungefär 84 %. Vid sänkningen ligger nedre gränsen därför en standardavvikelse under det nya medelvärdet.</p>'),
      step(r'Det nya medelvärdet uppfyller \(\mu-5=490\)',math(r'\mu=495\ \text{ml}')+'<p>Övre gränsen blir samtidigt 495+3·5=510 ml.</p>'),
      step('Kontrollera gränsläget för flaskornas volym i GeoGebra',MENU),
      geo('Kontrollera volymfördelningen vid μ = 495','495','5','490','510','ma2-4-2150','0.84'),
      step(r'Skillnaden som efterfrågas är \(500-495\)',math(r'500-495=5\ \text{ml}')+'<p>En större sänkning flyttar fördelningen ännu längre från det fasta intervallets mitt och ger mindre än cirka 84 % inom gränserna. 495 ml är det nya medelvärdet; 5 ml är sänkningen.</p>')],
      'Medelvärdet kan sänkas med ungefär 5 ml.',
      'Hitta först det lägre medelvärde som ger cirka 84 % i intervallet. Frågan gäller sedan skillnaden mot 500 ml.',5,5,'ml',.02)
    new('4.2151','<p>Restiden för en buss är normalfördelad med standardavvikelsen 2 minuter. Ungefär 18,15 % av resorna tar kortare tid än 23 minuter eller längre tid än 29 minuter. Medelrestiden är längre än 26 minuter.</p><p>Bestäm ungefär medelrestiden i minuter.</p>',[
      step(r'Komplementhändelsen ger \(100-18{,}15=81{,}85\) %',
           '<p>Andelen i frågan gäller båda svansarna tillsammans. Andelen mellan 23 och 29 minuter är därför ungefär 81,85 %. Vi kan inte dela svansandelen lika, eftersom medelvärdet inte ligger i intervallets mitt.</p>'),
      step(r'Intervallets bredd är \(29-23=3\sigma\)',math(r'29-23=6=3\cdot2')+math(r'13{,}59+34{,}13+34{,}13=81{,}85')+'<p>De tre banden kan ligga två under medelvärdet och ett över, eller tvärtom.</p>'),
      step(r'Välj placeringen med \(\mu\gt26\)',math(r'\mu-2\cdot2=23')+math(r'\mu=27')+'<p>Övre gränsen stämmer: 27+2=29 minuter. Spegelplaceringen ger 25 minuter och uppfyller inte villkoret.</p>'),
      step('Öppna sannolikhetskalkylatorn för bussens restid',MENU),
      geo('Kontrollera båda svansarna vid μ = 27','27','2','23','29','ma2-4-2151','0.1814','Intervallkomplement'),
      step('Tolka andelen utanför intervallet','<p>GeoGebra visar cirka 18,14 % utanför, vilket stämmer med ungefär 18,15 % när figurens procenttal är avrundade. GeoGebra summerar med fler decimaler än vad som visas i de två svansandelarna. Medelrestiden är därför ungefär 27 minuter.</p>')],
      'Medelrestiden är ungefär 27 minuter.',
      'Börja med andelen mellan gränserna. Använd sedan villkoret om medelrestiden för att välja mellan spegelvända placeringar.',4,27,'min',.02)
    return [old,*rows]

if __name__=='__main__':
    p=ROOT/'uppgifterma2.js';src=p.read_text();dec=json.JSONDecoder();bank,end=dec.raw_decode(src,src.index('['));new=build(bank);by={q['id']:q for q in new};changes=[];pos=src.index('[')+1
    while True:
        while src[pos].isspace() or src[pos]==',':pos+=1
        if src[pos]==']':break
        q,e=dec.raw_decode(src,pos)
        if q['id'] in by:changes.append((pos,e,json.dumps(by[q['id']],ensure_ascii=False,indent=2).replace('\n','\n  ')))
        pos=e
    absent=[q for q in new if not any(b['id']==q['id'] for b in bank)]
    if absent:changes.append((end-1,end-1,',\n'+',\n'.join('  '+json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ') for q in absent)+'\n'))
    for a,b,s in sorted(changes,reverse=True):src=src[:a]+s+src[b:]
    p.write_text(src);print('Uppdaterade:',list(by))
