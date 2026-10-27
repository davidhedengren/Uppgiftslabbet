import json
from pathlib import Path

answers = {
    '4.197': ['sqrt(2)*(cos(pi/4)+i*sin(pi/4))',
              'sqrt(2)*(cos(3*pi/4)+i*sin(3*pi/4))',
              '2*(cos(7*pi/6)+i*sin(7*pi/6))',
              '2*(cos(11*pi/6)+i*sin(11*pi/6))'],
    '4.198': ['2*(cos(pi/2)+i*sin(pi/2))', '3*(cos(pi)+i*sin(pi))',
              '4*(cos(3*pi/2)+i*sin(3*pi/2))', '5*(cos(0)+i*sin(0))'],
}
p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
by_id = {q['id']: q for q in bank}
for task_id, values in answers.items():
    q = by_id[task_id]
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },', start)
    segment = raw[start:end]
    for key, new in [('rättSvar', values), ('svarFormat', ['polar']*len(values))]:
        # JSON-källans indrag bevaras så att endast dessa metadata ändras.
        def field(value):
            return '"' + key + '": ' + json.dumps(value, ensure_ascii=False, indent=2).replace('\n', '\n    ')
        before, after = field(q[key]), field(new)
        assert segment.count(before) == 1, (task_id, key)
        segment = segment.replace(before, after, 1)
    raw = raw[:start] + segment + raw[end:]
p.write_text(raw, encoding='utf-8')
