import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
q = next(q for q in bank if q['id'] == '2.485')
new = (r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
       r'<li><p><strong>Derivera innerfunktionen.</strong> Sätt \(u(t)=0{,}4\cos t\). Då är \(u\prime(t)=-0{,}4\sin t\).</p></li>'
       r'<li><p><strong>Använd kedjeregeln.</strong> \[I\prime(t)=e^{u(t)}u\prime(t)\]</p><p>\[=e^{0{,}4\cos t}(-0{,}4\sin t).\]</p></li>'
       r'<li><p><strong>Sätt in \(t=\pi/2\).</strong> Eftersom \(\cos(\pi/2)=0\) och \(\sin(\pi/2)=1\) får vi \[I\prime(\pi/2)=e^0(-0{,}4)=-0{,}4.\]</p>'
       r'<p><strong>Svar:</strong> \(I\prime(\pi/2)=-0{,}4\).</p></li></ol></div>')
new = new.replace(r'\prime', "'")
start = raw.index('    "id": "2.485"')
end = raw.index('\n  },', start)
segment = raw[start:end]
before, after = json.dumps(q['s'], ensure_ascii=False), json.dumps(new, ensure_ascii=False)
assert segment.count(before) == 1
p.write_text(raw[:start] + segment.replace(before, after, 1) + raw[end:], encoding='utf-8')
