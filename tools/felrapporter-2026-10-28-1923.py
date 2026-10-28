import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
def update(file,task_id,transform):
 p=ROOT/file; raw=p.read_text(encoding='utf-8')
 bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]); q=next(q for q in bank if q['id']==task_id)
 changes,add=transform(q)
 if all(q.get(key)==value for key,value in {**changes,**add}.items()): return
 match=re.search(r'(?m)^([ \t]*)\{\s*\n[ \t]*"id": "'+re.escape(task_id)+r'"',raw)
 assert match,(file,task_id)
 start=match.start()+len(match.group(1)); _,length=json.JSONDecoder().raw_decode(raw[start:]);end=start+length
 segment=raw[start:end]
 for key,new in changes.items():
  before='"'+key+'": '+json.dumps(q[key],ensure_ascii=False,indent=2).replace('\n','\n    ')
  after='"'+key+'": '+json.dumps(new,ensure_ascii=False,indent=2).replace('\n','\n    ')
  assert segment.count(before)==1,(file,task_id,key)
  segment=segment.replace(before,after,1)
 if add:
  for key in add: assert key not in q
  close=segment.rfind('}')
  prefix=segment[:close].rstrip()
  indent=match.group(1)+'  '
  segment=prefix+''.join(',\n'+indent+json.dumps(key,ensure_ascii=False)+': '+json.dumps(value,ensure_ascii=False) for key,value in add.items())+'\n'+match.group(1)+'}'
 raw=raw[:start]+segment+raw[end:];p.write_text(raw,encoding='utf-8')

def ma1(q):
 t=('<p>En rektangels längd ökar med 12 % samtidigt som bredden minskar med 12 %. '
    'Hur många procent förändras arean? Ange ett negativt tal vid minskning och visa med en generell beräkning.</p>')
 s=(r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
    r'<li><p><strong>Beskriv ursprungsarean.</strong> Låt längden vara \(l\) och bredden \(b\). Då är arean \(A=lb\).</p></li>'
    r'<li><p><strong>Beräkna den nya arean.</strong> Längden multipliceras med \(1{,}12\) och bredden med \(0{,}88\). '
    r'Därför är \(A_{ny}=1{,}12l\cdot0{,}88b=0{,}9856lb\).</p></li>'
    r'<li><p><strong>Jämför med ursprungsarean.</strong> Skillnaden är \(0{,}9856-1=-0{,}0144\), alltså \(-1{,}44\%\).</p>'
    r'<p><strong>Svar:</strong> Arean minskar med \(1{,}44\%\).</p></li></ol></div>')
 return {'t':t,'s':s,'svarstyp':'numeriskt','rättSvar':-1.44,'självrättning':True}, {'svarFormat':'numeriskt','svarEnhet':'%'}

def geom(q):
 marker='<path d="M192.600 68.200 l8.800 6.600 l6.600 -8.800" fill="none" stroke="#253747" stroke-width="1.5"/>'
 if marker not in q['t'] and '<strong>Bestäm vinkeln vid C.</strong>' in q['s']:
  return {'t':q['t'],'s':q['s']},{}
 assert q['t'].count(marker)==1
 s=(r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
    r'<li><p><strong>Bestäm vinkeln vid C.</strong> Eftersom \(AB\) är en diameter är randvinkeln \(ACB\) rät.</p></li>'
    r'<li><p><strong>Använd likformighet.</strong> Höjden \(CH\) delar den rätvinkliga triangeln i två likformiga trianglar. '
    r'Motsvarande sidor ger \(AH/CH=CH/HB\). Sätt in \(AH=9\) och \(CH=12\): '
    r'\(9/12=12/HB\), så \(HB=16\) cm.</p></li>'
    r'<li><p><strong>Bestäm radien.</strong> Diametern är \(AB=9+16=25\) cm. Radien är hälften av diametern.</p>'
    r'<p><strong>Svar:</strong> Radien är \(12{,}5\) cm.</p></li></ol></div>')
 return {'t':q['t'].replace(marker,''),'s':s},{}

def ma1_jamforelse(q):
 t=('<p>Ett pris höjs först med 10 % och sänks sedan med 10 %. Är priset tillbaka på samma nivå? '
    'Ange den totala förändringen i procent med ett negativt tal vid minskning och motivera.</p>')
 s=(r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
    r'<li><p><strong>Multiplicera faktorerna.</strong> Höjningen ger faktorn \(1{,}10\) och sänkningen \(0{,}90\). '
    r'Den sammanlagda faktorn är \(1{,}10\cdot0{,}90=0{,}99\).</p></li>'
    r'<li><p><strong>Jämför med ursprungspriset.</strong> Slutpriset är 99 % av det ursprungliga priset, '
    r'alltså 1 % lägre. Sänkningen räknas på ett högre pris än höjningen.</p>'
    r'<p><strong>Svar:</strong> Nej, förändringen är \(-1\%\).</p></li></ol></div>')
 return {'t':t,'s':s,'svarstyp':'numeriskt','rättSvar':-1,'självrättning':True},{'svarFormat':'numeriskt','svarEnhet':'%'}

def ma1_rabatt(q):
 t=('<p>En jacka kostar 1 200 kr. Först sänks priset med 25 %. Därefter sänks det nya priset med 40 %.</p>'
    '<p>En elev säger att den totala rabatten är 65 %. Hur stor är den totala rabatten i procent? Bedöm påståendet och förklara.</p>')
 s=(r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
    r'<li><p><strong>Beräkna slutpriset.</strong> Faktorerna är \(0{,}75\) och \(0{,}60\). '
    r'Därför är slutpriset \(1200\cdot0{,}75\cdot0{,}60=540\) kr.</p></li>'
    r'<li><p><strong>Jämför med ursprungspriset.</strong> Rabatten är \(1200-540=660\) kr. '
    r'Andelen rabatt är \(660/1200=0{,}55=55\%\).</p></li>'
    r'<li><p><strong>Bedöm påståendet.</strong> Den andra rabatten räknas på det redan sänkta priset, '
    r'så procenttalen ska inte adderas. <strong>Svar:</strong> Rabatten är \(55\%\); påståendet är fel.</p></li></ol></div>')
 return {'t':t,'s':s,'svarstyp':'numeriskt','rättSvar':55,'självrättning':True},{'svarFormat':'numeriskt','svarEnhet':'%','manuellKomplettering':True}

def quadrant(q):
 t=q['t']
 if not any(re.search(r'>'+label+r'</text>',t) for label in ['I','II','III','IV']):
  return {'t':t},{}
 for label in ['I','II','III','IV']:
  pattern=r'<rect x="(?:246|82)" y="(?:48|248)" width="32" height="20" rx="3" fill="#fff"/><text [^>]+>'+label+r'</text>'
  t,n=re.subn(pattern,'',t);assert n==1,(label,n)
 return {'t':t},{}

update('uppgifterma1.js','3.06',ma1)
update('uppgifterma1.js','3.58',ma1_jamforelse)
update('uppgifterma1.js','3.190',ma1_rabatt)
update('uppgifterma2.js','3.544',geom)
update('uppgifterma2.js','3.669',quadrant)
