import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q=next(q for q in bank if q['id']=='3.248')
old_t=r'\[q(t)=-10+2t+20\sin\left(\frac{\pi t}{6}\right),\qquad0\le t\le12,\]</p><p>där \(q\) mäts i m³/h.'
new_t=r'\[q(t)=-10+2t+20\sin\left(\frac{\pi t}{6}\right).\]</p><p>Här är \(0\le t\le12\) och \(q\) mäts i m³/h.'
old_s=r'\[=-10t+t^2+\frac{120}{\pi}\left(1-\cos\frac{\pi t}{6}\right).\]'
new_s=r'\[=-10t+t^2\] \[+\frac{120}{\pi}\left(1-\cos\frac{\pi t}{6}\right).\]'
start=raw.index('    "id": "3.248"');end=raw.index('\n  },',start);segment=raw[start:end]
for old,old_part,new_part in [(q['t'],old_t,new_t),(q['s'],old_s,new_s)]:
 assert old.count(old_part)==1
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(old.replace(old_part,new_part),ensure_ascii=False)
 assert segment.count(before)==1;segment=segment.replace(before,after,1)
p.write_text(raw[:start]+segment+raw[end:],encoding='utf-8')
