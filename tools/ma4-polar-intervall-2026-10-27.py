import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
start = raw.index('    "id": "4.288"')
end = raw.index('\n  },', start)
segment = raw[start:end]
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
q = next(q for q in bank if q['id'] == '4.288')
old = '"svarFormat": ' + json.dumps(q['svarFormat'], indent=2).replace('\n', '\n    ')
new = '"svarFormat": ' + json.dumps(['polar_0_2pi']*4, indent=2).replace('\n', '\n    ')
assert segment.count(old) == 1
p.write_text(raw[:start] + segment.replace(old, new, 1) + raw[end:], encoding='utf-8')
