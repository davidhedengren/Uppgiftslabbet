import json
from pathlib import Path

p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'
raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]); q=next(q for q in bank if q['id']=='2.269')
old=q['t']
before_math=r'\[A(v)=200\sin v+100\sin v\cos v,\qquad0&lt;v&lt;\frac\pi2.\]'
after_math=r'\[A(v)=200\sin v+100\sin v\cos v.\]</p><p>Här är \(0&lt;v&lt;\frac\pi2\).'
assert old.count(before_math)==1
new=old.replace(before_math,after_math)
start=raw.index('    "id": "2.269"'); end=raw.index('\n  },',start); segment=raw[start:end]
before,after=json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False); assert segment.count(before)==1
p.write_text(raw[:start]+segment.replace(before,after,1)+raw[end:],encoding='utf-8')
