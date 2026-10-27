import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'; raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]); q=next(q for q in bank if q['id']=='3.43')
old_math=r'\[A=[4x-x^3/3]_0^2=8-8/3=16/3.\]'
new_math=r'\[A=[4x-x^3/3]_0^2\] \[=8-8/3=16/3.\]'
start=raw.index('    "id": "3.43"');end=raw.index('\n  },',start);segment=raw[start:end]
for old in [q['s'],next(d['s'] for d in q['spelDelar'] if d['etikett']=='b')]:
 assert old.count(old_math)==1
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(old.replace(old_math,new_math),ensure_ascii=False)
 assert segment.count(before)==1;segment=segment.replace(before,after,1)
p.write_text(raw[:start]+segment+raw[end:],encoding='utf-8')
