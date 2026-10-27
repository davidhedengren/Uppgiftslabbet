import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']') + 1])
by_id = {q['id']: q for q in bank}
prefix = ('<ol class="facit-steglista" role="list"><li><p class="facit-metod">'
          '<strong>Tänk så här:</strong> Skilj på startvärde och förändringsfaktor.</p></li>'
          '<li><p class="facit-metod">När den okända finns i exponenten logaritmerar du först '
          'efter att exponentialuttrycket isolerats.</p></li></ol>')
suffix = ('<ol class="facit-steglista" role="list"><li><p class="facit-not">'
          '<strong>Kontroll och insikt:</strong> Kontrollera att modellen får rätt värde vid tiden '
          'noll och att faktorn beskriver ökning eller minskning på rätt sätt.</p></li></ol>')
for task_id in ['2.482', '2.483', '2.485', '2.467', '4.105']:
    old = by_id[task_id]['s']
    assert old.count(prefix) == old.count(suffix) == 1
    new = old.replace(prefix, '').replace(suffix, '')
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },', start)
    segment = raw[start:end]
    before, after = json.dumps(old, ensure_ascii=False), json.dumps(new, ensure_ascii=False)
    assert segment.count(before) == 1
    raw = raw[:start] + segment.replace(before, after, 1) + raw[end:]
p.write_text(raw, encoding='utf-8')
