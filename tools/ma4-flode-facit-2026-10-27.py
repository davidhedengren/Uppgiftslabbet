import json
from pathlib import Path

steps={
 '3.95': [
  r'Den tillförda volymen är arean under flödesgrafen. Dela området i en rektangel, en trapets och en rektangel.',
  r'Under 0–5 minuter är volymen \(5\cdot60=300\) liter. Under 5–15 minuter är den \(10(60+20)/2=400\) liter.',
  r'Under 15–20 minuter är volymen \(5\cdot20=100\) liter. <strong>Svar:</strong> Totalt har \(300+400+100=800\) liter tillförts.'],
 '3.105': [
  r'Volymen är arean under flödesgrafen. Under 0–4 minuter ger trapetsen \(4(10+30)/2=80\) liter.',
  r'Under 4–8 minuter ger rektangeln \(4\cdot30=120\) liter. Under 8–12 minuter ger triangeln \(4\cdot30/2=60\) liter.',
  r'<strong>Svar:</strong> Den passerade volymen är \(80+120+60=260\) liter.'],
 '3.106': [
  r'Nettoflödet är \((30+5t)-12=18+5t\) liter per minut. Lägg integralen till de 50 liter som fanns från början.',
  r'\[V(t)=50+\int_0^t(18+5u)\,du\] \[=50+18t+2{,}5t^2.\]',
  r'Sätt \(V(t)=300\). Den positiva roten till \(2{,}5t^2+18t-250=0\) är \(t=(-18+\sqrt{2824})/5\approx7{,}03\).',
  r'Nettoflödet är positivt på intervallet, så volymen ökar hela tiden och passerar 300 liter endast en gång. <strong>Svar:</strong> Efter cirka \(7{,}03\) minuter.'],
 '3.470': [
  r'Nettoflödet är inflöde minus utflöde: \((20+2t)-14=6+2t\) liter per minut.',
  r'Integrera nettoflödet under de fem minuterna: \[\Delta V=\int_0^5(6+2t)\,dt\] \[=[6t+t^2]_0^5=55.\]',
  r'<strong>Svar:</strong> Vattenmängden ökar med \(55\) liter.'],
 '3.121': [
  r'Volymen är arean under flödesgrafen. Trapetsen under 0–4 minuter ger \((15+30)\cdot4/2=90\) liter.',
  r'Rektangeln under 4–10 minuter ger \(30\cdot6=180\) liter. Trapetsen under 10–16 minuter ger \((30+15)\cdot6/2=135\) liter.',
  r'<strong>Svar:</strong> Totalt passerar \(90+180+135=405\) liter.'],
 '3.248': [
  r'Låt \(V(t)\) vara nettovolymen sedan starten. Integrering av \(q\) ger \[V(t)=\int_0^tq(u)\,du\] \[=-10t+t^2+\frac{120}{\pi}\left(1-\cos\frac{\pi t}{6}\right).\]',
  r'För ett största värde undersöker vi ändpunkterna och punkterna där \(V\prime(t)=q(t)=0\). Nollställena är ungefär \(0{,}823\), \(6{,}237\) och \(10{,}815\) timmar.',
  r'Volymerna vid dessa tidpunkter är cirka \(-4{,}06\), \(52{,}63\) och \(15{,}93\) m³. Vid ändpunkterna är \(V(0)=0\) och \(V(12)=24\) m³.',
  r'<strong>Svar:</strong> Den största nettovolymen är cirka \(52{,}63\) m³ och fås efter \(6{,}237\) timmar.'],
}
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,rows in steps.items():
 q=by_id[task_id];old=q['s'];new='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+r.replace(r'\prime',"'")+'</p></li>' for r in rows)+'</ol></div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 before,after=json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
 segment=segment.replace(before,after,1)
 if task_id=='3.106':
  before='"rättSvar": 7.03';after='"rättSvar": 7.028264204469139';assert segment.count(before)==1
  segment=segment.replace(before,after,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
