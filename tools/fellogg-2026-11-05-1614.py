"""Manuell rättning av alternativberoende frågor; ändra bara granskade objekt."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def I(s):return r'\('+s+r'\)'
def step(title,text,math=None):
    return '<li><p class="facit-rubrik">'+title+'</p><p>'+text+'</p>'+('' if math is None else '<div class="facit-matte">'+r'\['+math+r'\]'+'</div>')+'</li>'
def sol(steps,answer):
    return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'.</p></div>'

def edit(q,bank):
    id=q['id']
    if bank=='ma1':
        if id not in ['0.06','0.305','0.306','0.401','0.402','0.782','0.941']:return False
        q['t']=q['t'].replace('Välj rätt rad i den ordningen.','Välj ett alternativ. De tre svaren ska stå i den ordningen.') if id=='0.06' else q['t'][:-4]+' Välj ett alternativ.</p>'
        if id=='0.06':
            q['s']=sol([step('Andel handlar om storlek, inte bara antal bitar','När bitarna är olika stora behöver tre av åtta bitar inte motsvara tre åttondelar av pizzan.'),step('Alla tre möjligheterna kan förekomma','Tre små bitar kan tillsammans vara mindre än tre åttondelar, och tre stora kan vara mer. Tre olika stora bitar kan också tillsammans vara precis tre åttondelar.')],'ja, ja, ja')
            comments=['Alla tre fallen är möjliga eftersom bitarna är olika stora.','Tre små bitar kan ge mindre än tre åttondelar, och tre stora kan ge mer.','Tre små bitar kan tillsammans ge mindre än tre åttondelar.','Tre stora bitar kan tillsammans ge mer än tre åttondelar.']
        elif id=='0.305':
            q['s']=sol([step('Förläng utan att ändra värdet: '+I(r'\frac ab=\frac{ak}{bk}'),'Jämför bråken som hundratjugondelar.',r'\begin{aligned}\frac58&=\frac{75}{120}\\[0.6em]\frac35&=\frac{72}{120}\\[0.6em]\frac23&=\frac{80}{120}\end{aligned}'),step('Jämför täljarna när nämnarna är lika','80 hundratjugondelar är mer än 75 och 72 hundratjugondelar.')],I(r'\frac23'))
            comments=['5/8 är 75/120, vilket är mindre än 80/120.','3/5 är 72/120, vilket är mindre än 80/120.','2/3 är 80/120, det största av de tre bråken.']
        elif id=='0.306':
            q['s']=sol([step('Avståndet till 1: '+I(r'1-\frac ab'),'Alla bråken är mindre än 1. Räkna hur mycket som fattas.',r'\begin{aligned}1-\frac58&=\frac38\\1-\frac7{10}&=\frac3{10}\\1-\frac23&=\frac13\end{aligned}'),step('Jämför avstånden med samma nämnare','Det minsta avståndet ger bråket närmast 1.',r'\begin{aligned}\frac38&=\frac{45}{120}\\[0.6em]\frac3{10}&=\frac{36}{120}\\[0.6em]\frac13&=\frac{40}{120}\end{aligned}')],I(r'\frac7{10}'))
            comments=['Avståndet 3/8 = 45/120 är större än 36/120.','Avståndet 3/10 = 36/120 är minst av de tre avstånden.','Avståndet 1/3 = 40/120 är större än 36/120.']
        elif id=='0.401':
            q['s']=sol([step('Skriv lika många decimaler: '+I(r'0{,}57=0{,}570'),'Nollor sist i decimaldelen ändrar inte värdet.',r'\begin{aligned}0{,}507&\quad 0{,}570\\0{,}509&\quad 0{,}550\end{aligned}'),step('Jämför hundradelarna','Alla har fem tiondelar. Talet 0,570 har flest hundradelar och är därför störst.')],I('0{,}57'))
            comments=['0,507 har noll hundradelar, medan 0,57 har sju.','0,57 = 0,570 är större än de andra tre talen.','0,509 har noll hundradelar, medan 0,57 har sju.','0,55 har fem hundradelar, medan 0,57 har sju.']
        elif id=='0.402':
            q['s']=sol([step('Skriv lika många decimaler: '+I('1{,}08=1{,}080'),'En nolla sist i decimaldelen ändrar inte värdet.',r'\begin{aligned}1{,}080&\quad 1{,}018\\1{,}080&\quad 1{,}008\end{aligned}'),step('Jämför hundradelarna','Alla tal har samma ental och tiondel. 1,008 har noll hundradelar, medan de andra har en eller åtta.')],I('1{,}008'))
            comments=['1,08 = 1,080 har åtta hundradelar; 1,008 har noll.','1,018 har en hundradel; 1,008 har noll.','1,080 har åtta hundradelar; 1,008 har noll.','1,008 har minst antal hundradelar när ental och tiondelar är lika.']
        elif id=='0.782':
            q['s']=sol([step('Skriv procent som bråk: '+I(r'p\,\%=\frac p{100}'),'42 procent är 42 hundradelar.',r'42\,\%=\frac{42}{100}=\frac{21}{50}'),step('Jämför med gemensam nämnare','126 trehundradelar är mer än 125 trehundradelar.',r'\begin{aligned}\frac5{12}&=\frac{125}{300}\\[0.6em]\frac{21}{50}&=\frac{126}{300}\end{aligned}')],'42 %')
            comments=['5/12 = 125/300 är mindre än 42 % = 126/300.','42 % = 126/300 är större än 5/12 = 125/300.']
        else:
            q['s']=sol([step('Skriv bråken som decimaltal: '+I(r'\frac ab=a\div b'),'Det går att jämföra när alla tal är skrivna i samma form.',r'\begin{aligned}\frac58&=0{,}625\\[0.6em]\frac23&=0{,}666\ldots\end{aligned}'),step('Ordna talen efter storlek','Jämför först tiondelarna och sedan hundradelarna.',r'0{,}600\lt0{,}625\lt0{,}650\lt0{,}666\ldots')],I(r'\frac23'))
            comments=['5/8 = 0,625 är mindre än 2/3 = 0,666…','0,6 är mindre än 2/3 = 0,666…','0,65 är mindre än 2/3 = 0,666…','2/3 = 0,666… är störst.']
        for a,c in zip(q['alternativ'],comments):a['kommentar']=c
    else:
        if id not in ['4.245','4.2082','4.2084','4.2143']:return False
        q['t']=q['t'].replace('(Välj alla som stämmer.)','(Välj alla alternativ som stämmer.)')
        if id=='4.245':
            q['t']=q['t'].replace('Vilket påstående stämmer?','Vilket påstående stämmer? Med spridning menas här spridningen i den mittersta hälften av resultaten. Välj ett alternativ.')
            q['s']=sol([step('Jämför medianerna','Klass A:s median är högre än klass B:s.',r'62\gt58'),step('Kvartilavstånd: '+I(r'Q_3-Q_1'),'Kvartilavståndet mäter spridningen i den mittersta hälften. Det givna avståndet är mindre i klass A.',r'10\lt25')],'Klass A har högre median och mindre spridning i den mittersta hälften')
            q['alternativ'][0]['kommentar']='A har högre median: 62 > 58. A har mindre kvartilavstånd: 10 &lt; 25.'
        elif id=='4.2082':
            q['s']=sol([step('Läs av medianerna','Tågets median är 28 minuter och bussens är 30 minuter. Tåget har lägre median.'),step('Variationsbredd: '+I(r'\text{största}-\text{minsta}'),'Jämför avståndet mellan de yttersta värdena.',r'\begin{aligned}\text{Tåg: }36-18&=18\text{ min}\\\text{Buss: }52-15&=37\text{ min}\end{aligned}'),step('Kvartilavstånd: '+I(r'Q_3-Q_1'),'Även spridningen i den mittersta hälften är större för bussen.',r'\begin{aligned}\text{Tåg: }31-24&=7\text{ min}\\\text{Buss: }38-22&=16\text{ min}\end{aligned}'),step('Kontrollera snabbaste resan och övre kvartilen','Den kortaste resan är bussens 15 minuter. För tåget är 31 minuter övre kvartilen, gränsen mot den högsta fjärdedelen, inte medianen.')],'Medianen är lägre för tåget och bussens restider varierar mer')
            q['alternativ'][3]['kommentar']='31 min är övre kvartilen, gränsen mot den högsta fjärdedelen. Medianen är 28 min.'
        elif id=='4.2084':
            q['t']=q['t'].replace('Det rättas från 48 till 38.','Det rättas från 48 till 38. Det rättade värdet är fortfarande störst.')
            q['s']=sol([step('Värdet är fortfarande störst','Enligt frågan ligger det rättade värdet fortfarande sist i storleksordningen. Medianens och kvartilernas platser och värden ändras därför inte.'),step('Största värdet ändras från 48 till 38','Detta följer av att 38 fortfarande är större än alla övriga värden.'),step('Medelvärde: '+I(r'\bar{x}=\frac{\text{summan}}{n}'),'Antalet värden är fortfarande 20. Summan minskar med 10, så medelvärdet minskar med 0,5.',r'\frac{48-38}{20}=0{,}5')],'Största värdet och medelvärdet ändras')
            q['ledtrad']='<p>Det rättade värdet ligger fortfarande sist i storleksordningen. Fundera på vilka mått som beror på de mittersta värdena och vilket mått som använder alla värden.</p>'
            q['alternativ'][1]['kommentar']='Största värdet blir 38 eftersom frågan anger att det rättade värdet fortfarande är störst.'
        else:
            q['s']=sol([step('Läs medianstrecken inne i lådorna','Båda medianerna är 3,5 timmar. Därför stämmer påståendet att medianerna är lika stora.'),step('Kvartilavstånd: '+I(r'Q_3-Q_1'),'Lådans bredd visar spridningen i den mittersta hälften. Klass 2 har större kvartilavstånd.',r'\begin{aligned}\text{Klass 1: }4-2{,}5&=1{,}5\text{ h}\\\text{Klass 2: }5{,}5-2&=3{,}5\text{ h}\end{aligned}'),step('Skilj övre kvartilen från medianen','5,5 timmar är övre kvartilen i klass 2, gränsen mot den högsta fjärdedelen. Det är inte medianen, som delar materialet i två hälfter.')],'Medianerna är lika stora och klass 2 har större spridning i den mittersta hälften')
            q['alternativ'][3]['kommentar']='5,5 h är övre kvartilen, gränsen mot den högsta fjärdedelen. Medianen är 3,5 h.'
    return True

if __name__=='__main__':
    for bank in ['ma1','ma2']:
        p=ROOT/f'uppgifter{bank}.js';s=p.read_text();decoder=json.JSONDecoder();pos=s.index('[')+1;patches=[];ids=[]
        while True:
            while s[pos].isspace() or s[pos]==',':pos+=1
            if s[pos]==']':break
            q,end=decoder.raw_decode(s,pos)
            if edit(q,bank):patches.append((pos,end,json.dumps(q,ensure_ascii=False,indent=2)));ids.append(q['id'])
            pos=end
        for start,end,new in reversed(patches):s=s[:start]+new+s[end:]
        p.write_text(s);print(bank,', '.join(ids))
