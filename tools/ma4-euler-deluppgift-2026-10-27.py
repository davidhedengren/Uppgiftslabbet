import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
q = next(q for q in bank if q['id'] == '4.105')
old = next(d['s'] for d in q['spelDelar'] if d['etikett'] == 'b')
new = (r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
       r'<li><p><strong>Skriv talet på exponentiell form.</strong> \(|z|=\sqrt{(-1)^2+(\sqrt3)^2}=2\). '
       r'Punkten ligger i andra kvadranten och argumentet är \(2\pi/3\), så \(z=2e^{i2\pi/3}\).</p></li>'
       r'<li><p><strong>Beräkna kuben.</strong> \[z^3=2^3e^{i2\pi}\]'
       r'Eftersom \(e^{i2\pi}=1\) blir \(z^3=8\).</p></li>'
       r'<li><p><strong>Svar:</strong> \(\boxed{8}\).</p></li></ol></div>')
start = raw.index('    "id": "4.105"')
end = raw.index('\n  },', start)
segment = raw[start:end]
before, after = json.dumps(old, ensure_ascii=False), json.dumps(new, ensure_ascii=False)
assert segment.count(before) == 1
p.write_text(raw[:start] + segment.replace(before, after, 1) + raw[end:], encoding='utf-8')
