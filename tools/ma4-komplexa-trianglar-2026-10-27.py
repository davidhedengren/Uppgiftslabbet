import json
from pathlib import Path
parts={
 '4.113': [
  [r'Sidlängderna är absolutbeloppen av skillnaderna mellan hörnens komplexa tal.',r'\(|z_2-z_1|=|4|=4\). De andra två skillnaderna är \(z_3-z_1=2+3i\) och \(z_3-z_2=-2+3i\).',r'<strong>Svar:</strong> Sidlängderna är \(4\), \(\sqrt{2^2+3^2}=\sqrt{13}\) och \(\sqrt{(-2)^2+3^2}=\sqrt{13}\).'],
  [r'Punkterna \(z_1=1+i\) och \(z_2=5+i\) har samma imaginärdel. Den horisontella basen har därför längden \(5-1=4\).',r'Punkten \(z_3=3+4i\) ligger \(4-1=3\) enheter ovanför baslinjen. Arean är \(A=4\cdot3/2=6\).',r'<strong>Svar:</strong> Triangelns area är \(6\) areaenheter.']],
 '4.294': [
  [r'Sätt in vart och ett av de tre ursprungliga talen i \(w=(1+i)z+2\).',r'För \(z=0\) fås \(w=2\). För \(z=2\) fås \(w=4+2i\).',r'För \(z=2i\) fås \(w=2i+2i^2+2=2i\). <strong>Svar:</strong> De tre värdena är \(2\), \(4+2i\) och \(2i\).'],
  [r'För två ursprungliga punkter \(z_a\) och \(z_b\) blir skillnaden mellan bilderna \(w_a-w_b=(1+i)(z_a-z_b)\).',r'Ta absolutbelopp: \(|w_a-w_b|=|1+i|\,|z_a-z_b|\). Här är \(|1+i|=\sqrt{1^2+1^2}=\sqrt2\); additionen av 2 försvinner i differensen.',r'<strong>Svar:</strong> Varje sidlängd multipliceras med \(\sqrt2\).']]
}
def sol(rows):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+r+'</p></li>' for r in rows)+'</ol></div>'
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,sections in parts.items():
 q=by_id[task_id];sols=[sol(x) for x in sections];assert len(q['spelDelar'])==2
 combined='<div class="facit-v2 facit-stegvis">'+''.join(f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{s}</div></div>' for i,s in enumerate(sols))+'</div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 for old,new in [(q['s'],combined)]+[(d['s'],s) for d,s in zip(q['spelDelar'],sols)]:
  before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
  segment=segment.replace(before,after,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
