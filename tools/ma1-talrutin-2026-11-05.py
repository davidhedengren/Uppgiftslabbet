"""Handvalda rutinserier. Kör med --write för att lägga till nya ID:n i master.

Ingen slumpning: operandsamlingar och metodval är redaktionellt valda.
Fraction verifierar varje mellanled exakt före serialisering.
"""
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 24 blad, tre självständiga beräkningar per blad. Inga dolda textproblem.
FRACTIONS = [
    ('+', 1, [('1/5','2/5'),('3/7','2/7'),('1/9','4/9')]),
    ('+', 1, [('3/10','5/10'),('5/12','1/12'),('2/11','7/11')]),
    ('+', 2, [('1/2','1/8'),('2/3','1/6'),('3/5','1/10')]),
    ('+', 2, [('1/4','5/8'),('1/3','4/9'),('3/10','1/5')]),
    ('+', 2, [('1/3','1/4'),('2/5','1/3'),('3/4','1/6')]),
    ('+', 2, [('2','1/3'),('3/4','1'),('5/6','2/3')]),
    ('-', 1, [('4/5','1/5'),('6/7','2/7'),('7/9','2/9')]),
    ('-', 1, [('9/10','3/10'),('11/12','5/12'),('8/11','3/11')]),
    ('-', 2, [('3/4','1/8'),('5/6','1/3'),('7/10','1/5')]),
    ('-', 2, [('1','2/5'),('2','3/4'),('1','5/8')]),
    ('-', 2, [('2/3','1/4'),('4/5','1/3'),('5/6','1/4')]),
    ('-', 2, [('7/6','1/2'),('9/8','3/4'),('11/10','2/5')]),
    ('*', 1, [('1/2','1/3'),('1/4','1/5'),('2/3','1/5')]),
    ('*', 1, [('3/5','2/7'),('2/9','3/4'),('3/8','2/5')]),
    ('*', 2, [('2/3','3/4'),('3/5','5/6'),('4/7','7/8')]),
    ('*', 2, [('3/4','2/9'),('5/6','3/10'),('7/12','6/7')]),
    ('*', 1, [('3','1/5'),('1/4','6'),('4','2/7')]),
    ('*', 2, [('8','3/4'),('5/6','12'),('9/5','5/3')]),
    ('/', 2, [('1/2','1/4'),('1/3','1/6'),('3/4','1/8')]),
    ('/', 2, [('2/3','4/5'),('3/7','2/5'),('5/8','3/4')]),
    ('/', 2, [('3/5','2'),('7/8','3'),('5/6','4')]),
    ('/', 2, [('2','3/4'),('3','2/5'),('4','5/6')]),
    ('/', 2, [('4/9','2/3'),('5/12','5/6'),('7/10','7/5')]),
    ('/', 2, [('9/8','3/4'),('7/6','7/3'),('5/4','5/8')]),
]

# (typ, nivå, (procentsats, helt värde) eller (del, helt värde)).
# Hela-serierna anger (procentsats, delen), inte det sökta hela.
PERCENTS = [
    ('del',1,[(10,80),(50,36),(25,120)]),
    ('del',1,[(20,150),(5,200),(75,80)]),
    ('del',2,[(15,240),(30,450),(12,350)]),
    ('del',2,[(2,750),(8,125),(35,180)]),
    ('andel',1,[(6,24),(15,30),(8,40)]),
    ('andel',1,[(9,12),(3,60),(14,100)]),
    ('andel',2,[(18,120),(24,80),(42,140)]),
    ('andel',2,[(7,200),(27,180),(36,240)]),
    ('hela',1,[(50,18),(25,15),(10,24)]),
    ('hela',2,[(20,46),(30,72),(75,90)]),
    ('hela',2,[(15,48),(12,54),(8,28)]),
    ('hela',2,[(5,35),(40,180),(60,156)]),
]

def tex(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else rf'\frac{{{x.numerator}}}{{{x.denominator}}}'

def decimal(x):
    return f'{float(x):.10f}'.rstrip('0').rstrip('.').replace('.', '{,}')

def inline(s):
    return r'\(' + s + r'\)'

def step(title, text, lines):
    return '<li><p class="facit-rubrik">'+title+'</p><p>'+text+'</p>' + ''.join('<div class="facit-matte">'+r'\['+line+r'\]'+'</div>' for line in lines)+'</li>'

def solution(steps, answer):
    return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join(steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+inline(answer)+'.</p></div>'

def fraction_part(op, level, left, right):
    a,b=F(left),F(right)
    symbol={'+':'+','-':'-','*':r'\cdot','/':r'\div'}[op]
    expression=tex(a)+symbol+tex(b)
    steps=[]
    if op in ['+','-']:
        n=math.lcm(a.denominator,b.denominator)
        u=a.numerator*(n//a.denominator); v=b.numerator*(n//b.denominator)
        z=u+v if op=='+' else u-v
        answer=F(z,n)
        if a.denominator!=b.denominator:
            names={3:'tredjedelar',4:'fjärdedelar',5:'femtedelar',6:'sjättedelar',8:'åttondelar',9:'niondelar',10:'tiondelar',12:'tolftedelar',15:'femtondelar'}
            conversions=[]
            for value in [a,b]:
                if value.denominator!=n:
                    k=n//value.denominator
                    conversions.append(tex(value)+rf'=\frac{{{value.numerator}\cdot{k}}}{{{value.denominator}\cdot{k}}}=\frac{{{value.numerator*k}}}{{{n}}}')
            steps.append(step('Skriv bråken med gemensam nämnare',
                f'Båda talen kan skrivas som {names[n]}. Multiplicera täljare och nämnare med samma tal.',conversions))
            hint='Skriv båda talen med samma nämnare innan du räknar med täljarna.'
        else:
            hint='Bråken har redan samma nämnare. Räkna med täljarna och behåll nämnaren.'
        title=('Addera täljarna: ' if op=='+' else 'Subtrahera täljarna: ')+inline(r'\frac{a}{n}'+op+r'\frac{b}{n}=\frac{a'+op+r'b}{n}')
        steps.append(step(title,'Delarnas storlek ändras inte, så nämnaren är kvar.',
            [rf'\frac{{{u}{op}{v}}}{{{n}}}=\frac{{{z}}}{{{n}}}']))
        raw=(z,n)
    else:
        if a.denominator==1 or b.denominator==1:
            integer=a if a.denominator==1 else b
            steps.append(step('Skriv heltalet som ett bråk', 'Ett heltal kan skrivas med nämnaren 1.',
                              [tex(integer)+rf'=\frac{{{integer.numerator}}}{{1}}']))
        if op=='/':
            steps.append(step('Division: '+inline(r'\frac{a}{b}\div\frac{c}{d}=\frac{a}{b}\cdot\frac{d}{c}'),
                'Behåll det första talet och vänd på det andra bråket.',[expression+'='+tex(a)+r'\cdot'+tex(1/b)]))
            hint='Behåll det första talet. Byt division mot multiplikation med det andra talets omvända bråk.'
            b=1/b
        else:
            hint='Multiplicera täljarna med varandra och nämnarna med varandra. Ett heltal kan skrivas med nämnaren 1.'
        raw=(a.numerator*b.numerator,a.denominator*b.denominator)
        answer=F(*raw)
        steps.append(step('Multiplicera: '+inline(r'\frac{a}{b}\cdot\frac{c}{d}=\frac{ac}{bd}'),
            'Täljarna ger den nya täljaren och nämnarna den nya nämnaren.',
            [rf'\frac{{{a.numerator}\cdot{b.numerator}}}{{{a.denominator}\cdot{b.denominator}}}=\frac{{{raw[0]}}}{{{raw[1]}}}']))
    factor=math.gcd(*raw)
    if factor>1:
        steps.append(step('Förkorta täljare och nämnare',f'Dividera både täljaren och nämnaren med {factor}.',
            [rf'\frac{{{raw[0]}\div{factor}}}{{{raw[1]}\div{factor}}}='+tex(answer)]))
    # Separat kontroll direkt från ursprungsoperanderna.
    x,y=F(left),F(right)
    expected={'+':lambda:x+y,'-':lambda:x-y,'*':lambda:x*y,'/':lambda:x/y}[op]()
    assert answer==expected
    return dict(t='<p>Beräkna '+inline(expression)+'. Svara exakt.</p>',
                s=solution(steps,tex(answer)),ledtrad='<p>'+hint+'</p>',
                rättSvar=str(answer),svarFormat='bråk',svarstyp='bråk',
                traningsniva=level,arbetsinsats=level,**{'miniräknare':False,'geogebra':False})

def percent_part(kind,level,x,y):
    x,y=F(x),F(y)
    if kind=='del':
        text='Hur mycket är '+inline(decimal(x)+r'\,\%')+' av '+inline(tex(y))+'?'
        answer=x*y/100; unit='';result=decimal(answer)
        steps=[step('Skriv procenten som en andel: '+inline(r'p\,\%=\frac{p}{100}'),
                    'Procent betyder hundradelar.',[decimal(x)+r'\,\%='+decimal(x/100)]),
               step('Beräkna delen: '+inline(r'\text{delen}=\text{andelen}\cdot\text{det hela}'),
                    'Multiplicera andelen i decimalform med det hela.',
                    [decimal(x/100)+r'\cdot'+tex(y)+'='+result])]
        hint='Skriv procentsatsen i decimalform och multiplicera med det hela.'
    elif kind=='andel':
        text='Hur många procent är '+inline(tex(x))+' av '+inline(tex(y))+'?'
        answer=100*x/y;unit='%';result=decimal(answer)+r'\,\%'
        steps=[step('Beräkna andelen: '+inline(r'\text{andelen}=\frac{\text{delen}}{\text{det hela}}'),
                    'Dela den angivna delen med det hela.',[rf'\frac{{{x}}}{{{y}}}='+decimal(x/y)]),
               step('Omvandla till procent: '+inline(r'1=100\,\%'),
                    'Multiplicera decimaltalet med 100 för att få antalet procent.',
                    [decimal(x/y)+'='+result])]
        hint='Sätt delen i täljaren och det hela i nämnaren. Omvandla sedan kvoten till procent.'
    else:
        text=inline(decimal(x)+r'\,\%')+' av ett tal är '+inline(tex(y))+'. Vilket är talet?'
        answer=100*y/x;unit='';result=decimal(answer)
        steps=[step('Skriv procenten som en andel: '+inline(r'p\,\%=\frac{p}{100}'),
                    'Det givna värdet är bara en del av talet.',[decimal(x)+r'\,\%='+decimal(x/100)]),
               step('Beräkna det hela: '+inline(r'\text{det hela}=\frac{\text{delen}}{\text{andelen}}'),
                    'Dividera den givna delen med andelen i decimalform.',
                    [rf'\frac{{{tex(y)}}}{{{decimal(x/100)}}}='+result]),
               step('Kontrollera genom att beräkna delen igen',
                    'Den givna procenten av ditt tal ska bli den angivna delen.',
                    [decimal(x/100)+r'\cdot'+result+'='+tex(y)])]
        hint='Du känner delen och procentsatsen. Dividera delen med andelen i decimalform för att få hela talet.'
    assert answer.denominator in [1,2,4,5,10,20,25,50,100]
    return dict(t='<p>'+text+'</p>',s=solution(steps,result),ledtrad='<p>'+hint+'</p>',
                rättSvar=float(answer) if answer.denominator!=1 else int(answer),
                svarFormat='numeriskt',svarstyp='numeriskt',svarEnhet=unit or None,
                traningsniva=level,arbetsinsats=level,**{'miniräknare':True,'geogebra':False})

def parent(id,parts,topic,family,intro):
    for label,d in zip('abc',parts):
        d.update(etikett=label,niva='E',poang='1/0/0',tolerans=0,självrättning=True)
    q=dict(id=id,kap=0,omr=topic,kurs=['1a','1b','1c'],familj=family,
           formaga=['procedur'],niva='E',poang='3/0/0',traningsniva=max(d['traningsniva'] for d in parts),
           arbetsinsats=2,spel=True,självrättning=True,svarstyp='flera_delar',
           svarsstruktur='ordnad',spelDelning='deluppgifter',spelDelar=parts,
           rättSvar=[d['rättSvar'] for d in parts],svarFormat=[d['svarFormat'] for d in parts],
           tolerans=[0,0,0],svarEtiketter=['a)','b)','c)'],
           geogebra=False,**{'miniräknare':parts[0]['miniräknare']})
    if topic=='andelar':q['svarEnhet']=[d['svarEnhet'] for d in parts]
    q['t']='<p>'+intro+'</p><div class="deluppgifter">'+''.join('<p>'+d['etikett']+') '+d['t'][3:-4]+'</p>' for d in parts)+'</div>'
    q['s']='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+d['etikett']+')</span><div class="facit-arbete">'+d['s'].removeprefix('<div class="facit-v2 facit-stegvis">').removesuffix('</div>')+'</div></div>' for d in parts)+'</div>'
    q['ledtrad']=parts[0]['ledtrad']
    return q

def build():
    result=[]
    for op,level,pairs in FRACTIONS:
        result.append(parent(f'0.{1266+len(result)}',[fraction_part(op,level,*p) for p in pairs],
                             'brakrakning','Räkna med bråk','Räkna med bråktalen.'))
    for kind,level,pairs in PERCENTS:
        family='Andel i procent' if kind=='andel' else 'Beräkningar när procentsatsen är känd'
        intro={'del':'Beräkna delen.','andel':'Beräkna andelen i procent.','hela':'Beräkna det hela.'}[kind]
        result.append(parent(f'0.{1266+len(result)}',[percent_part(kind,level,*p) for p in pairs],
                             'andelar',family,intro))
    return result

if __name__=='__main__':
    new=build()
    if '--write' in sys.argv:
        path=ROOT/'uppgifterma1.js';s=path.read_text();bank=json.loads(s[s.index('['):].strip().removesuffix(';'))
        assert not set(q['id'] for q in new)&set(q['id'] for q in bank),'ID redan upptaget'
        end=s.rfind(']')
        path.write_text(s[:end].rstrip()+',\n'+',\n'.join(json.dumps(q,ensure_ascii=False,indent=2) for q in new)+'\n'+s[end:])
    print(f'{len(new)} uppgifter, {sum(len(q["spelDelar"]) for q in new)} delkort: {new[0]["id"]}–{new[-1]["id"]}')
