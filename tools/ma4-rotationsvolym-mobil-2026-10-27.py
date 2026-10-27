import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q=next(q for q in bank if q['id']=='3.46')
old_t=r'\[y_{yttre}=1+\sqrt{x},\qquad y_{inre}=\frac12+\frac{x}{4},\qquad0\le x\le4\]'
new_t=r'\(y_{yttre}=1+\sqrt{x}\) och \(y_{inre}=\frac12+\frac{x}{4}\) för \(0\le x\le4\)'
old_s=r'\[V=\pi\int_0^4\left((1+\sqrt{x})^2-(1/2+x/4)^2\right)dx.\]'
new_s=r'Med ytterradie \(R\) och innerradie \(r\) är \[V=\pi\int_0^4(R^2-r^2)\,dx.\]'
start=raw.index('    "id": "3.46"');end=raw.index('\n  },',start);segment=raw[start:end]
for old,old_part,new_part in [(q['t'],old_t,new_t),(q['s'],old_s,new_s)]:
 assert old.count(old_part)==1
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(old.replace(old_part,new_part),ensure_ascii=False)
 assert segment.count(before)==1;segment=segment.replace(before,after,1)
p.write_text(raw[:start]+segment+raw[end:],encoding='utf-8')
