import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q=next(q for q in bank if q['id']=='3.46')
old=q['t'];new=old.replace(r'\(y_{yttre}=1+\sqrt{x}\) och \(y_{inre}=\frac12+\frac{x}{4}\), för \(0\le x\le4\),',r'\(y_{yttre}=1+\sqrt{x}\) och \(y_{inre}=\frac12+\frac{x}{4}\) för \(0\le x\le4\)')
assert old!=new
start=raw.index('    "id": "3.46"');end=raw.index('\n  },',start);segment=raw[start:end]
before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
p.write_text(raw[:start]+segment.replace(before,after,1)+raw[end:],encoding='utf-8')
