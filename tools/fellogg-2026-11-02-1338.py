"""Avgränsade, matematiskt granskade svar och delfacit."""
from pathlib import Path
import json,re
p=Path(__file__).resolve().parent.parent/'uppgiftermato1.js'
s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];ids=set()
graphs={'2.85','2.90','2.95','2.100','2.105','2.110','2.115','2.120'}
poly={
'3.359':(r"<p>\(f'(x)=3(x-3)(x+1)\). Derivatan är positiv när \(x&lt;-1\), negativ när \(-1&lt;x&lt;3\) och positiv när \(x&gt;3\).</p>",r"<p>Derivatan byter tecken från plus till minus vid \(x=-1\) och från minus till plus vid \(x=3\). Eftersom \(f(-1)=10\) och \(f(3)=-22\) är maximipunkten \((-1,10)\) och minimipunkten \((3,-22)\).</p>"),
'3.365':(r"<p>\(f'(x)=4x(x-2)(x+2)\). Derivatans tecken är i tur och ordning minus, plus, minus och plus på intervallen \(x&lt;-2\), \(-2&lt;x&lt;0\), \(0&lt;x&lt;2\) och \(x&gt;2\).</p>",r"<p>Tecknet går från minus till plus vid \(x=-2\) och \(x=2\), samt från plus till minus vid \(x=0\). Med \(f(-2)=f(2)=-16\) och \(f(0)=0\) fås minimipunkterna \((-2,-16)\) och \((2,-16)\), samt maximipunkten \((0,0)\).</p>"),
'3.369':(r"<p>\(f'(x)=x(x-2)^2\). Kvadraten är positiv på båda sidor om 2, så derivatans tecken är minus för \(x&lt;0\) och plus för både \(0&lt;x&lt;2\) och \(x&gt;2\).</p>",r"<p>Vid \(x=0\) går derivatan från minus till plus och \(f(0)=0\), så \((0,0)\) är en minimipunkt. Vid \(x=2\) byter derivatan inte tecken; där finns ingen extrempunkt.</p>")}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');old=s[pos:end];new=old
 def field(k,v):
  global new
  if k in q:
   pattern=r'("'+re.escape(k)+r'"\s*:\s*)'+re.escape(json.dumps(q[k],ensure_ascii=False));new,n=re.subn(pattern,lambda m:m.group(1)+json.dumps(v,ensure_ascii=False),new,count=1);assert n==1,(id,k)
  else:
   i=new.rfind('}');new=new[:i].rstrip()+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  '+new[i:]
 if id=='3.132':
  parts=q['spelDelar'];assert len(parts)==2 and all('rättSvar' not in d for d in parts)
  for label,value in [('a',5),('b',13)]:
   needle='"etikett": "'+label+'",';assert new.count(needle)==1
   new=new.replace(needle,needle+'\n        "rättSvar": '+str(value)+',',1)
 elif id=='3.731':
  field('delfacit',[r'<p>En primitiv funktion till \(10t\) är \(5t^2\). Därför är \(\int_1^2 10t\,dt=[5t^2]_1^2=20-5=15\).</p>',r'<p>Hastigheten är positiv under intervallet. Integralen beskriver därför den sträcka stenen faller från \(t=1\) s till \(t=2\) s. Sträckan är 15 m.</p>'])
 elif id=='3.500':
  field('t',q['t'].replace('Hur stor är den sammanlagda kostnaden under de första 4 månaderna?','Hur stor är den sammanlagda kostnaden under de första 4 månaderna? Svara i tusen kronor (tkr).'))
  field('s',r'<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Integrera kostnadstakten över fyra månader</strong></p><p>Integralen ger kostnaden i tusen kronor.</p>\[\int_0^4(12+0{,}5t^2)\,dt=\left[12t+\frac{t^3}{6}\right]_0^4=48+\frac{32}{3}=\frac{176}{3}.\]<p class="facit-svar"><strong>Svar:</strong> \(\frac{176}{3}\approx58{,}67\) tkr.</p></div>')
  field('rättSvar',176/3);field('tolerans',None);field('svarEnhet','tkr')
 elif id in graphs:
  m=re.search(r'<li><p><strong>b\)</strong> (.*?)</p></li><li><p>(.*?)</p></li>',q['s']);assert m,id
  field('delfacit',[None,'<p>'+m.group(1)+'</p><p>'+m.group(2)+'</p>'])
 elif id in poly:
  b,c=poly[id];field('delfacit',[None,b,c])
 if new!=old:json.loads(new);changes.append((pos,end,new));ids.add(id)
 pos=end
expected={'3.132','3.731','3.500'}|graphs|set(poly);assert ids==expected,(ids,expected)
for a,b,v in reversed(changes):s=s[:a]+v+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8');print('Ändrade ID:',', '.join(sorted(ids)))
