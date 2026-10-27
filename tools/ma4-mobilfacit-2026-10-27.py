import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']') + 1])
by_id = {q['id']: q for q in bank}
changes = {
    '2.485': (r"\[I'(t)=e^{u(t)}u'(t)=e^{0{,}4\cos t}(-0,4\sin t).\]",
              r"\[I'(t)=e^{u(t)}u'(t)\]" + '</p><p>' + r"\[=e^{0{,}4\cos t}(-0{,}4\sin t).\]"),
    '4.105': (r'\[z^3=2^3e^{i2\pi}=8(\cos2\pi+i\sin2\pi)=\boxed{8}.\]',
              r'\[z^3=2^3e^{i2\pi}\]' + '</p><p>' + r'\[=8(\cos2\pi+i\sin2\pi)=\boxed{8}.\]'),
}
for task_id, (old_math, new_math) in changes.items():
    q = by_id[task_id]
    fields = [q['s']] + [d['s'] for d in q.get('spelDelar', []) if old_math in d.get('s', '')]
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },', start)
    segment = raw[start:end]
    for old in fields:
        assert old.count(old_math) == 1
        before = json.dumps(old, ensure_ascii=False)
        after = json.dumps(old.replace(old_math, new_math), ensure_ascii=False)
        assert segment.count(before) == 1
        segment = segment.replace(before, after, 1)
    raw = raw[:start] + segment + raw[end:]
p.write_text(raw, encoding='utf-8')
