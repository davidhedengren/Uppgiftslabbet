import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
by_id = {q['id']:q for q in bank}
for task_id in ['3.11','3.179']:
    q = by_id[task_id]
    fields = [q['s']] + [d['s'] for d in q.get('spelDelar',[]) if '<x<' in d.get('s','')]
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },',start)
    segment = raw[start:end]
    for old in fields:
        assert '<x<' in old
        new = old.replace('<x<','&lt;x&lt;')
        before,after=json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False)
        assert segment.count(before)==1
        segment=segment.replace(before,after,1)
    raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
