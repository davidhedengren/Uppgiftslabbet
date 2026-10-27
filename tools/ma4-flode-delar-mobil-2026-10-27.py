import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q=next(q for q in bank if q['id']=='3.209')
old_q=r'\[q(t)=18+6\sin(\pi t/10),\qquad 0\le t\le20.\]'
new_q=r'\[q(t)=18+6\sin(\pi t/10).\]</p><p>Modellen gäller \(0\le t\le20\).'
old_f=r'\[\Delta V=\int_0^{10}(18+6\sin(\pi t/10))\,dt.\]'
new_f=r'\[\Delta V=\int_0^{10}q(t)\,dt.\]'
start=raw.index('    "id": "3.209"');end=raw.index('\n  },',start);segment=raw[start:end]
for old,old_part,new_part in [(q['t'],old_q,new_q),(q['spelIntro'],old_q,new_q),(q['s'],old_f,new_f),(q['spelDelar'][0]['s'],old_f,new_f)]:
 assert old.count(old_part)==1
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(old.replace(old_part,new_part),ensure_ascii=False)
 assert segment.count(before)==1;segment=segment.replace(before,after,1)
p.write_text(raw[:start]+segment+raw[end:],encoding='utf-8')
