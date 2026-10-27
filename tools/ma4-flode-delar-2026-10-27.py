import json, math
from pathlib import Path

parts={
 '3.209': [
  [r'Volymökningen fås genom att integrera inflödet under de första 10 minuterna: \[\Delta V=\int_0^{10}(18+6\sin(\pi t/10))\,dt.\]',r'En primitiv funktion är \(18t-60\cos(\pi t/10)/\pi\). Insättning av gränserna ger \(\Delta V=180+120/\pi\).',r'Tanken innehåller redan 120 liter. <strong>Svar:</strong> Volymen blir \(300+120/\pi\approx338{,}2\) liter.'],
  [r'På 20 minuter genomgår sinusdelen en hel period. Dess positiva och negativa bidrag till integralen tar ut varandra.',r'Totalt strömmar därför \(18\cdot20=360\) liter in. Medelflödet är \(360/20=18\) liter per minut.',r'<strong>Svar:</strong> Det genomsnittliga inflödet är \(18\) L/min.']],
 '3.225': [
  [r'Volymen är integralen av flödet: \[V=\int_0^6(30+12\sin(\pi t/6))\,dt.\]',r'En primitiv funktion är \(30t-72\cos(\pi t/6)/\pi\). Insättning av gränserna ger \(V=180+144/\pi\).',r'<strong>Svar:</strong> Ungefär \(225{,}8\) m³ vatten passerar.'],
  [r'Medelvärdet är den totala volymen delad med tiden. Använd \(V=180+144/\pi\) m³ för de sex minuterna.',r'\(V/6=30+24/\pi\approx37{,}6\) m³/min. Det är större än 30 eftersom sinusdelen är positiv under denna halva period.',r'<strong>Svar:</strong> Påståendet stämmer inte; medelflödet är cirka \(37{,}6\) m³/min.']]
}
def solution(rows):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+s+'</p></li>' for s in rows)+'</ol></div>'
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,sections in parts.items():
 q=by_id[task_id];sols=[solution(x) for x in sections]
 combined='<div class="facit-v2 facit-stegvis">'+''.join(f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{s}</div></div>' for i,s in enumerate(sols))+'</div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 changes=[(q['s'],combined)]
 if q.get('spelDelar'):
  assert len(q['spelDelar'])==2
  changes += [(d['s'],s) for d,s in zip(q['spelDelar'],sols)]
 for old,new in changes:
  before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
  segment=segment.replace(before,after,1)
 if task_id=='3.209':
  before='"rättSvar": '+json.dumps(q['rättSvar'],indent=2).replace('\n','\n    ')
  after='"rättSvar": '+json.dumps([300+120/math.pi,18],indent=2).replace('\n','\n    ')
  assert segment.count(before)==1;segment=segment.replace(before,after,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
