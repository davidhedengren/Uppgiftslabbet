"""Visa de alternativ som frågorna hänvisar till och rätta en förklaring."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
ids={'0.77','0.80','0.86','0.92','0.98','0.322','0.879'}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in ids:
  assert q['t'].endswith('</p>') and 'alternativ' not in q['t'].lower();new=q['t'][:-4]+' Välj ett alternativ.</p>'
  old=json.dumps(q['t'],ensure_ascii=False);needle='"t": '+old;assert chunk.count(needle)==1;chunk=chunk.replace(needle,'"t": '+json.dumps(new,ensure_ascii=False),1)
  if id=='0.77':
   old='Man ska starta vid det första talet, −6, och sedan lägga till −4.'
   new='Från −4 ska man lägga till −6 och alltså gå sex steg åt vänster, inte åt höger.'
   assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='0.98':
   old=q['s'];new=old.replace('a<b<0','a&lt;b&lt;0').replace(r'0<\frac{b}{a}<1<\frac{a}{b}',r'0&lt;\frac{b}{a}&lt;1&lt;\frac{a}{b}')
   assert new!=old;needle='"s": '+json.dumps(old,ensure_ascii=False);assert chunk.count(needle)==1;chunk=chunk.replace(needle,'"s": '+json.dumps(new,ensure_ascii=False),1)
  assert json.loads(chunk)['id']==id;changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==ids,(found,ids)
for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8');print('Ändrade:',', '.join(sorted(found)))
