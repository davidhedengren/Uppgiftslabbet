import json
from pathlib import Path

rows={
 '3.31': [
  r'Av figuren ser vi att det skuggade området ligger mellan \(x=\pi/6\) och \(x=\pi/2\). Grafen ligger där under x-axeln.',
  r'Den geometriska arean är därför \[A=-\int_{\pi/6}^{\pi/2}\cos(3x)\,dx.\]',
  r'En primitiv funktion är \(\sin(3x)/3\). Insättning ger \[A=-\tfrac13\left(\sin\tfrac{3\pi}{2}-\sin\tfrac\pi2\right).\]',
  r'<strong>Svar:</strong> \(A=-\frac13(-1-1)=\boxed{\frac23}\).'],
 '3.212': [
  r'Skärningarna ges av \(4x-x^2=x\), det vill säga \(x(3-x)=0\). Gränserna är \(x=0\) och \(x=3\).',
  r'Parabeln ligger över linjen mellan skärningarna. Arean är \[A=\int_0^3(3x-x^2)\,dx.\]',
  r'En primitiv funktion är \(3x^2/2-x^3/3\). Insättning ger \(A=27/2-9\).',
  r'<strong>Svar:</strong> Arean är \(\boxed{9/2}\) areaenheter.'],
}
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,steps in rows.items():
 old=by_id[task_id]['s'];new='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+s+'</p></li>' for s in steps)+'</ol></div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
 raw=raw[:start]+segment.replace(before,after,1)+raw[end:]
p.write_text(raw,encoding='utf-8')
