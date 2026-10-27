import json
from pathlib import Path

pieces={
 '3.43': [
  r'\(2x+2\) är positiv på intervallet, så arean är integralen. En primitiv funktion är \(x^2+2x\). \[A=[x^2+2x]_0^3=15.\]',
  r'\(4-x^2\) är icke-negativ på intervallet. En primitiv funktion är \(4x-x^3/3\). \[A=[4x-x^3/3]_0^2\] \[=8-8/3=16/3.\]',
  r'\(e^x\) är positiv på intervallet och är sin egen primitiva funktion. \[A=[e^x]_0^1=e-1.\]'],
 '3.71': [
  r'Skärningarna ges av \(x^2=2x\), alltså \(x=0\) och \(x=2\). Punkterna är \((0,0)\) och \((2,4)\). Linjen ligger ovanför parabeln mellan dem. \[A=\int_0^2(2x-x^2)\,dx\] \[=[x^2-x^3/3]_0^2=4/3.\]',
  r'\(x^2-1=3\) ger \(x=-2\) och \(x=2\), alltså punkterna \((-2,3)\) och \((2,3)\). Linjen ligger över parabeln mellan punkterna. \[A=\int_{-2}^2(4-x^2)\,dx\] \[=[4x-x^3/3]_{-2}^2=32/3.\]',
  r'\(x^2=4x-x^2\) ger \(x=0\) och \(x=2\), alltså punkterna \((0,0)\) och \((2,4)\). Kurvan \(y=4x-x^2\) ligger över \(y=x^2\) mellan punkterna. \[A=\int_0^2(4x-2x^2)\,dx\] \[=[2x^2-2x^3/3]_0^2=8/3.\]'],
}
other={
 '3.64': [r'Sätt kurvorna lika: \(4-x^2=2-x\) ger \((x-2)(x+1)=0\), så gränserna är \(-1\) och \(2\).',r'Parabeln ligger över linjen mellan skärningarna. \[A=\int_{-1}^2(2+x-x^2)\,dx.\]',r'En primitiv funktion är \(2x+x^2/2-x^3/3\). Insättning av båda gränserna ger \(A=9/2\).'],
 '3.198': [r'Nollställena är \(x=\pm\sqrt a\). Mellan dem är \(x^2-a\le0\), så arean är integralen av \(a-x^2\).',r'Av symmetri får vi \[A=2\int_0^{\sqrt a}(a-x^2)\,dx.\] En primitiv funktion är \(ax-x^3/3\), vilket ger \(A=\frac43a^{3/2}\).',r'Sätt \(\frac43a^{3/2}=\frac{32}3\). Då är \(a^{3/2}=8\), och eftersom \(a>0\) blir \(\boxed{a=4}\).'],
 '3.224': [r'Skärningarna ges av \(6-x^2=x+2\), så \(x=(-1\pm\sqrt{17})/2\). Parabeln ligger över linjen mellan skärningarna.',r'Skillnaden mellan kurvorna är \(4-x-x^2=17/4-(x+1/2)^2\). Sätt \(u=x+1/2\); gränserna blir \(\pm\sqrt{17}/2\).',r'Med symmetri är \[A=2\int_0^{\sqrt{17}/2}(17/4-u^2)\,du.\] Den primitiva funktionen är \(17u/4-u^3/3\). Insättning ger \(\boxed{17\sqrt{17}/6}\).'],
 '3.232': [r'Skärningarna ges av \(x^2=4x-x^2\), som ger \(x=0\) och \(x=2\). Kurvan \(4x-x^2\) ligger över \(x^2\) mellan dem.',r'Arean är \[A=\int_0^2(4x-2x^2)\,dx.\] Med den primitiva funktionen \(2x^2-2x^3/3\) får vi \(A=8-16/3=\boxed{8/3}\).'],
}
def solution(rows):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+r+'</p></li>' for r in rows)+'</ol></div>'
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'; raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]); by_id={q['id']:q for q in bank}
for task_id in list(pieces)+list(other):
 q=by_id[task_id]; start=raw.index(f'    "id": "{task_id}"'); end=raw.index('\n  },',start); segment=raw[start:end]; changes=[]
 if task_id in pieces:
  sols=[solution([s]) for s in pieces[task_id]]; assert len(q['spelDelar'])==len(sols)
  combined='<div class="facit-v2 facit-stegvis">'+''.join(f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{s}</div></div>' for i,s in enumerate(sols))+'</div>'
  changes=[(q['s'],combined)]+[(d['s'],s) for d,s in zip(q['spelDelar'],sols)]
  if task_id=='3.71':
   old='Bestäm först skärningspunkterna och beräkna sedan arean mellan kurvorna.'
   new='Bestäm arean mellan kurvorna. Börja med att bestämma deras skärningspunkter.'
   changes += [(q['t'],q['t'].replace(old,new)),(q['spelIntro'],q['spelIntro'].replace(old,new))]
 else: changes=[(q['s'],solution(other[task_id]))]
 for old,new in changes:
  assert old!=new
  before,after=json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False); assert segment.count(before)==1,(task_id,old[:60]); segment=segment.replace(before,after,1)
 if task_id=='3.71':
  before='"rättSvar": '+json.dumps(q['rättSvar'],ensure_ascii=False,indent=2).replace('\n','\n    ')
  after='"rättSvar": '+json.dumps(['4/3','32/3','8/3'],indent=2).replace('\n','\n    ')
  assert segment.count(before)==1; segment=segment.replace(before,after,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
