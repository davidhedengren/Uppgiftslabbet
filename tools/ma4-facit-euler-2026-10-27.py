import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
q = next(q for q in bank if q['id'] == '4.105')
old_math = r'\[z^3=2^3e^{i2\pi}\]</p><p>\[=8(\cos2\pi+i\sin2\pi)=\boxed{8}.\]'
new_math = r'\[e^{i2\pi}=1\]</p><p>\[z^3=2^3\cdot1=\boxed{8}.\]'
start = raw.index('    "id": "4.105"')
end = raw.index('\n  },', start)
segment = raw[start:end]
fields = [q['s'], next(d['s'] for d in q['spelDelar'] if d['etikett'] == 'b')]
for old in fields:
    assert old.count(old_math) == 1
    before, after = json.dumps(old, ensure_ascii=False), json.dumps(old.replace(old_math, new_math), ensure_ascii=False)
    assert segment.count(before) == 1
    segment = segment.replace(before, after, 1)
p.write_text(raw[:start] + segment + raw[end:], encoding='utf-8')
