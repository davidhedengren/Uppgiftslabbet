"""Visa enbart aktuella komponenter i facit för vektorernas x-del."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent.parent/'uppgifter.js'
XS={'3.301':(-2,2),'3.302':(-5,5),'3.303':(4,-4),'3.304':(4,2),'3.305':(3,3),'3.306':(1,-4),'3.307':(3,-1),'3.308':(-2,0)}
s=P.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id')
 if id in XS:
  x1,x2=XS[id];d=q['spelDelar'][0];old=d['s'];assert d.get('etikett')=='a' and 'vektorform' in old
  new=(r'<div class="facit-v2 facit-stegvis"><p>Läs av krafternas x-komposanter i figuren och addera dem. Höger är positiv riktning.</p>'
   +r'\[F_{Rx}='+str(x1)+'+('+str(x2)+')='+str(x1+x2)+r'\,\mathrm N\]'
   +r'<p><strong>Svar:</strong> \('+str(x1+x2)+r'\,\mathrm N\).</p></div>')
  oldenc=json.dumps(old,ensure_ascii=False);newenc=json.dumps(new,ensure_ascii=False);chunk=s[pos:end];assert chunk.count(oldenc)==1,id
  chunk=chunk.replace(oldenc,newenc,1);assert json.loads(chunk)['spelDelar'][0]['s']==new
  changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==set(XS),set(XS)-found
for start,end,chunk in reversed(changes):s=s[:start]+chunk+s[end:]
json.loads(s[s.index('['):s.rindex(']')+1]);P.write_text(s,encoding='utf8');print('Ändrade',', '.join(sorted(found)))
