import json
from pathlib import Path

steps={
 '2.269': [
  r'Derivera areafunktionen: \(A\prime(v)=200\cos v+100\cos(2v)\).',
  r'Sätt \(c=\cos v\). Eftersom \(\cos(2v)=2c^2-1\) ger \(A\prime(v)=0\) ekvationen \(2c^2+2c-1=0\).',
  r'Intervallet ger \(0&lt;c&lt;1\), så den enda möjliga roten är \(c=(\sqrt3-1)/2\). Då är \(v\approx1{,}196\) rad \(\approx68{,}5^\circ\).',
  r'Derivatan är positiv nära \(v=0\) och negativ nära \(v=\pi/2\). Den enda stationära punkten är därför ett maximum. Insättning ger \(A\approx220{,}18\) cm².',
  r'<strong>Svar:</strong> Vinkeln är cirka \(68{,}5^\circ\) och största arean cirka \(220\) cm².'],
 '2.131': [
  r'Lådans höjd är \(x\) och botten har sidorna \(30-2x\) och \(20-2x\). Därför är \(V(x)=x(30-2x)(20-2x)\), där \(0&lt;x&lt;10\).',
  r'Utveckla och derivera: \(V(x)=4x^3-100x^2+600x\), så \(V\prime(x)=12x^2-200x+600\).',
  r'\(V\prime(x)=0\) ger \(x=(25\pm5\sqrt7)/3\). Endast den mindre roten ligger mellan \(0\) och \(10\).',
  r'Volymen är noll vid intervallets ändar och positiv däremellan. Den enda stationära punkten ger därför maximum.',
  r'<strong>Svar:</strong> \(x=(25-5\sqrt7)/3\approx3{,}92\) cm.'],
 '2.205': [
  r'Lådans volym är \(V(x)=x(30-2x)(20-2x)\), där \(0&lt;x&lt;10\).',
  r'Utveckla och derivera: \(V(x)=4x^3-100x^2+600x\), så \(V\prime(x)=12x^2-200x+600\).',
  r'\(V\prime(x)=0\) ger \(x=(25\pm5\sqrt7)/3\). Bara den mindre roten ligger i intervallet.',
  r'Volymen är noll vid ändarna och positiv däremellan. Den enda stationära punkten ger därför maximum.',
  r'<strong>Svar:</strong> \(x=(25-5\sqrt7)/3\approx3{,}92\) cm.'],
 '2.224': [
  r'Om ena sidan är \(x\) cm är den andra \(100/x\) cm. Omkretsen är \(P(x)=2x+200/x\), där \(x>0\).',
  r'Derivera: \(P\prime(x)=2-200/x^2\). Villkoret \(P\prime(x)=0\) ger \(x^2=100\), alltså \(x=10\) eftersom en sidlängd är positiv.',
  r'Derivatan är negativ före \(x=10\) och positiv efteråt, så omkretsen är minst där. \(P(10)=2\cdot10+200/10=40\).',
  r'<strong>Svar:</strong> Den minsta omkretsen är \(40\) cm.'],
 '2.251': [
  r'Volymen är \(1000\) cm³. Ur \(\pi r^2h=1000\) får vi \(h=1000/(\pi r^2)\).',
  r'Totalarean är två cirkelytor och en mantelyta: \(A=2\pi r^2+2\pi rh\). Efter insättning blir \(A(r)=2\pi r^2+2000/r\).',
  r'Derivatan är \(A\prime(r)=4\pi r-2000/r^2\). Villkoret \(A\prime(r)=0\) ger \(r^3=500/\pi\), så \(r=\sqrt[3]{500/\pi}\approx5{,}42\) cm.',
  r'Andra derivatan \(A\prime\prime(r)=4\pi+4000/r^3\) är positiv för \(r>0\), så punkten är ett minimum. Insättning ger \(h=2r\approx10{,}84\) cm.',
  r'<strong>Svar:</strong> Radien är cirka \(5{,}42\) cm och höjden cirka \(10{,}84\) cm.'],
 '2.260': [
  r'Rektangelns bredd är \(x\) och höjden \(12-x^2\). Arean är \(A(x)=12x-x^3\), där \(0&lt;x&lt;\sqrt{12}\).',
  r'Derivera: \(A\prime(x)=12-3x^2\). Den positiva lösningen till \(A\prime(x)=0\) är \(x=2\).',
  r'Derivatan är positiv före \(x=2\) och negativ efteråt. Arean är alltså störst där; höjden är \(12-2^2=8\).',
  r'<strong>Svar:</strong> Största arean är \(2\cdot8=16\) areaenheter.'],
}
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'; raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]); by_id={q['id']:q for q in bank}
for task_id,rows in steps.items():
 q=by_id[task_id]; old=q['s']; new='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+r.replace(r'\prime',"'")+'</p></li>' for r in rows)+'</ol></div>'
 start=raw.index(f'    "id": "{task_id}"'); end=raw.index('\n  },',start); segment=raw[start:end]
 before,after=json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False); assert segment.count(before)==1
 segment=segment.replace(before,after,1)
 if task_id=='2.205':
  old_field='"rättSvar": 3.92'; new_field='"rättSvar": 3.9237478148923493'; assert segment.count(old_field)==1
  segment=segment.replace(old_field,new_field,1)
 raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
