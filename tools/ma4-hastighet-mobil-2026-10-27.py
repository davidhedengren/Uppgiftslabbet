import json
from pathlib import Path

steps={
 '2.26': [
  r'\(A=\pi r^2\). Eftersom radien förändras med tiden ger kedjeregeln \(\dfrac{dA}{dt}=2\pi r\dfrac{dr}{dt}\).',
  r'Sätt in \(r=0{,}75\) m och \(dr/dt=0{,}20\) m/år: \[\frac{dA}{dt}=2\pi\cdot0{,}75\cdot0{,}20.\]',
  r'<strong>Svar:</strong> Arean ökar med \(0{,}30\pi\approx0{,}94\) m²/år.'],
 '2.100': [
  r'Klotets volym är \(V=\frac43\pi r^3\). Kedjeregeln ger \(\dfrac{dV}{dt}=4\pi r^2\dfrac{dr}{dt}\).',
  r'Sätt in \(r=5{,}0\) cm och \(dr/dt=0{,}40\) cm/s: \[\frac{dV}{dt}=4\pi\cdot25\cdot0{,}40=40\pi.\]',
  r'<strong>Svar:</strong> Volymen ökar med \(40\pi\approx126\) cm³/s.'],
 '2.248': [
  r'Klotets volym är \(V=\frac43\pi r^3\). Kedjeregeln ger \(\dfrac{dV}{dt}=4\pi r^2\dfrac{dr}{dt}\).',
  r'Sätt in \(r=10\) cm och \(dr/dt=0{,}8\) cm/s: \[\frac{dV}{dt}=4\pi\cdot100\cdot0{,}8.\]',
  r'<strong>Svar:</strong> Volymen ökar med \(320\pi\) cm³/s.'],
}
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'; raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]); by_id={q['id']:q for q in bank}
for task_id,rows in steps.items():
 old=by_id[task_id]['s']; new='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+r+'</p></li>' for r in rows)+'</ol></div>'
 start=raw.index(f'    "id": "{task_id}"'); end=raw.index('\n  },',start); segment=raw[start:end]
 before=json.dumps(old,ensure_ascii=False); after=json.dumps(new,ensure_ascii=False); assert segment.count(before)==1
 raw=raw[:start]+segment.replace(before,after,1)+raw[end:]
p.write_text(raw,encoding='utf-8')
