import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q=next(q for q in bank if q['id']=='4.113')
old_math=r'\[z_1=1+i,\qquad z_2=5+i,\qquad z_3=3+4i.\]'
new_math=r'\(z_1=1+i\), \(z_2=5+i\) och \(z_3=3+4i\).'
start=raw.index('    "id": "4.113"');end=raw.index('\n  },',start);segment=raw[start:end]
for old in [q['t'],q['spelIntro']]:
 assert old.count(old_math)==1
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(old.replace(old_math,new_math),ensure_ascii=False)
 assert segment.count(before)==1;segment=segment.replace(before,after,1)
p.write_text(raw[:start]+segment+raw[end:],encoding='utf-8')
