import json
from pathlib import Path

parts={
 '4.10': [
  [r'\(|z-(2+i)|\) är avståndet från \(z\) till punkten \(2+i\), som har koordinaterna \((2,1)\).',r'<strong>Svar:</strong> Alla punkter på avståndet 3 bildar en cirkel med centrum \((2,1)\) och radie 3.'],
  [r'På den reella axeln är \(z=x\). Villkoret \(|x-(2+i)|=3\) ger efter kvadrering \((x-2)^2+1=9\).',r'Därmed är \((x-2)^2=8\) och \(x=2\pm\sqrt8=2\pm2\sqrt2\).',r'<strong>Svar:</strong> De två reella lösningarna är \(2+2\sqrt2\) och \(2-2\sqrt2\).']],
 '4.97': [
  [r'\(|z-(2-i)|\) är avståndet från \(z\) till punkten \(2-i\). Villkoret anger att avståndet ska vara 3.',r'<strong>Svar:</strong> Figuren är en cirkel.'],
  [r'\(|z-(2-i)|=3\) anger alla punkter på avståndet 3 från \(2-i\).',r'<strong>Svar:</strong> Medelpunkten är \((2,-1)\) och radien är 3.'],
  [r'Cirkeln har centrum \((2,-1)\) och radie 3. Linjen \(\operatorname{Im}z=-1\) går horisontellt genom centrum.',r'Skärningarna ligger tre enheter till vänster och höger om centrum: \(2-3=-1\) och \(2+3=5\).',r'<strong>Svar:</strong> Punkterna är \(-1-i\) och \(5-i\).']]
}
other={
 '4.06': [r'\(|z-(1-i)|\) är avståndet från punkten \(z\) till \(1-i\), alltså till \((1,-1)\).',r'Villkoret ger alla punkter på avståndet 3 från centrum. Det är en cirkel med centrum \((1,-1)\) och radie 3.',r'Skrivs \(z=x+iy\) blir cirkelns ekvation \(\boxed{(x-1)^2+(y+1)^2=9}\). Rita centrum och en cirkel med denna radie.'],
 '4.18': [r'\(|z-(2+i)|=3\) beskriver alla punkter på avstånd 3 från \(2+i\). Mängden är därför en cirkel med centrum \((2,1)\) och radie 3.',r'På den reella axeln är \(z=x\). Då ger avståndsformeln \((x-2)^2+1=9\), alltså \((x-2)^2=8\).',r'<strong>Svar:</strong> Cirkeln skär den reella axeln i \(2+2\sqrt2\) och \(2-2\sqrt2\).'],
 '4.164': [r'\(|z-1|\) är avståndet till \((1,0)\), och \(|z+3|\) är avståndet till \((-3,0)\).',r'Punkter med samma avstånd till dessa två punkter ligger på sträckans mittpunktsnormal. Mittpunkten är \((-1,0)\), och normalen är vertikal.',r'<strong>Svar:</strong> Mängden är den räta linjen \(x=-1\).'],
 '4.221': [r'För \(z=x+iy\) är \(\operatorname{Re}z=x\). Dessutom är \(z+2i=x+i(y+2)\), så \(\operatorname{Im}(z+2i)=y+2\).',r'Villkoret ger \(x=y+2\), alltså \(y=x-2\).',r'<strong>Svar:</strong> Mängden är den räta linjen \(y=x-2\) i det komplexa talplanet.'],
 '4.271': [r'\(|z-(2-i)|\) är avståndet från punkten \(z\) till punkten \(2-i\), alltså \((2,-1)\).',r'<strong>Svar:</strong> Villkoret beskriver en cirkel med centrum \((2,-1)\) och radie 3.']
}
def sol(rows):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+r+'</p></li>' for r in rows)+'</ol></div>'
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id in list(parts)+list(other):
 q=by_id[task_id];start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 if task_id in parts:
  sols=[sol(x) for x in parts[task_id]];assert len(q['spelDelar'])==len(sols)
  combined='<div class="facit-v2 facit-stegvis">'+''.join(f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{s}</div></div>' for i,s in enumerate(sols))+'</div>'
  changes=[(q['s'],combined)]+[(d['s'],s) for d,s in zip(q['spelDelar'],sols)]
 else:changes=[(q['s'],sol(other[task_id]))]
 for old,new in changes:
  before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1,(task_id,old[:40])
  segment=segment.replace(before,after,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
