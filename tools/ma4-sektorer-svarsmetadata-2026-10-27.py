import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id in ['1.64','1.167','1.172']:
 q=by_id[task_id];start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 if task_id=='1.64':
  before='"tolerans": '+json.dumps(q['tolerans'],indent=2).replace('\n','\n    ')
  after='"tolerans": '+json.dumps([None,0],indent=2).replace('\n','\n    ')
 else:
  assert q.get('svarEnhet') is None
  before='"svarFormat": '+json.dumps(q['svarFormat'],ensure_ascii=False,indent=2).replace('\n','\n    ')
  after=before+',\n    "svarEnhet": '+json.dumps(['cm','cm²'],ensure_ascii=False,indent=2).replace('\n','\n    ')
 assert segment.count(before)==1;segment=segment.replace(before,after,1);raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
