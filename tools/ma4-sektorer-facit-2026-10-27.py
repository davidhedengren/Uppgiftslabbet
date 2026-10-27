import json
from pathlib import Path

parts={
 '1.64': [
  [r'När vinkeln \(v\) mäts i radianer är båglängden \(s=rv\). Dela med radien: \(v=12/9=4/3\).',r'<strong>Svar:</strong> Medelpunktsvinkeln är \(4/3\) rad.'],
  [r'Först ger båglängden och radien \(v=s/r=12/9=4/3\) rad.',r'Radierna och sträckan mellan ändpunkterna bildar en likbent triangel. Halvera den: halva sträckan är \(9\sin(v/2)=9\sin(2/3)\) cm.',r'Hela sträckan är \(18\sin(2/3)\approx11{,}1307\) cm. <strong>Svar:</strong> Med en decimal är längden \(11{,}1\) cm.']],
 '1.167': [
  [r'Vinkeln är i radianer. Båglängden är radien gånger vinkeln: \(b=rv=12\cdot5\pi/6\).',r'<strong>Svar:</strong> Båglängden är \(10\pi\) cm.'],
  [r'När vinkeln är i radianer är sektorns area \(A=r^2v/2\). Sätt in radien 12 cm och vinkeln \(5\pi/6\).',r'\(A=12^2\cdot(5\pi/6)/2=60\pi\). <strong>Svar:</strong> Arean är \(60\pi\) cm².']],
 '1.172': [
  [r'Vinkeln är i radianer, så båglängden är \(b=rv=9{,}0\cdot1{,}4\).',r'<strong>Svar:</strong> Båglängden är \(12{,}6\) cm.'],
  [r'När vinkeln är i radianer är sektorns area \(A=r^2v/2\). Sätt in \(r=9{,}0\) cm och \(v=1{,}4\).',r'\(A=9{,}0^2\cdot1{,}4/2=56{,}7\). <strong>Svar:</strong> Arean är \(56{,}7\) cm².']]
}
def sol(rows):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+s+'</p></li>' for s in rows)+'</ol></div>'
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,sections in parts.items():
 q=by_id[task_id];sols=[sol(x) for x in sections];assert len(q['spelDelar'])==2
 combined='<div class="facit-v2 facit-stegvis">'+''.join(f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{s}</div></div>' for i,s in enumerate(sols))+'</div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 for old,new in [(q['s'],combined)]+[(d['s'],s) for d,s in zip(q['spelDelar'],sols)]:
  before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
  segment=segment.replace(before,after,1)
 if task_id=='1.64':
  before='"rättSvar": '+json.dumps(q['rättSvar'],ensure_ascii=False,indent=2).replace('\n','\n    ')
  after='"rättSvar": '+json.dumps(['4/3',11.1],indent=2).replace('\n','\n    ')
  assert segment.count(before)==1;segment=segment.replace(before,after,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
