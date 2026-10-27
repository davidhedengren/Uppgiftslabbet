import json
from pathlib import Path
steps={
 '3.46': [
  r'Vid rotation kring x-axeln är ytterradien \(1+\sqrt{x}\) och innerradien \(1/2+x/4\). Volymen är skillnaden mellan skivornas volymer.',
  r'\[V=\pi\int_0^4\left((1+\sqrt{x})^2-(1/2+x/4)^2\right)dx.\]',
  r'Utveckla kvadraterna. Integranden blir \(3/4+2\sqrt{x}+3x/4-x^2/16\).',
  r'Integrering på intervallet ger \(3+32/3+6-4/3=55/3\). <strong>Svar:</strong> \(V=55\pi/3\) volymenheter.'],
 '3.49': [
  r'För \(0\le x\le1\) ligger \(\sqrt{x}\) över \(x\). Vid rotation kring x-axeln blir de yttre och inre radierna \(R=\sqrt{x}\) och \(r=x\).',
  r'Brickmetoden ger \(V=\pi\int_0^1(R^2-r^2)\,dx\), alltså \[V=\pi\int_0^1(x-x^2)\,dx.\]',
  r'En primitiv funktion är \(x^2/2-x^3/3\). Insättning ger \(V=\pi(1/2-1/3)=\pi/6\).',
  r'<strong>Svar:</strong> Volymen är \(\pi/6\) volymenheter.'],
 '3.58': [
  r'Kurvan skär x-axeln vid \(x=-2\) och \(x=2\). Rotationsaxeln är \(y=5\), så ytterradien är \(R=5\) och innerradien är \(r=5-(4-x^2)=1+x^2\).',
  r'\[V=\pi\int_{-2}^2\left(25-(1+x^2)^2\right)dx.\] Integranden förenklas till \(24-2x^2-x^4\).',
  r'Integranden är jämn. Integrera därför från 0 till 2 och dubblera: \[V=2\pi\left[24x-\frac{2x^3}{3}-\frac{x^5}{5}\right]_0^2.\]',
  r'<strong>Svar:</strong> Volymen är \(1088\pi/15\) volymenheter.'],
 '3.107': [
  r'Kurvorna skär varandra vid \((0,0)\) och \((1,1)\). Vid rotation kring y-axeln använder vi \(y\) som integrationsvariabel.',
  r'Kurvorna skrivs \(x=y\) och \(x=\sqrt[3]{y}\). För \(0&lt;y&lt;1\) är ytterradien \(R=y^{1/3}\) och innerradien \(r=y\).',
  r'Brickmetoden ger \[V=\pi\int_0^1(y^{2/3}-y^2)\,dy.\]',
  r'En primitiv funktion är \(3y^{5/3}/5-y^3/3\). Insättning ger \(V=\pi(3/5-1/3)=4\pi/15\).',
  r'<strong>Svar:</strong> Volymen är \(4\pi/15\) volymenheter.'],
 '3.122': [
  r'Området ligger mellan \(y=0\) och \(y=x\) för \(0\le x\le2\). Rotationsaxeln \(y=3\) ligger ovanför området.',
  r'Avstånden till axeln är ytterradien \(R=3\) och innerradien \(r=3-x\). Brickmetoden ger \[V=\pi\int_0^2(9-(3-x)^2)\,dx.\]',
  r'Förenkla integranden till \(6x-x^2\). Då är \(V=\pi[3x^2-x^3/3]_0^2=\pi(12-8/3)\).',
  r'<strong>Svar:</strong> Volymen är \(28\pi/3\) volymenheter.'],
 '3.126': [
  r'Rotationsaxeln \(y=3\) ligger ovanför området för \(0\le x\le4\). Ytterradien är \(R=3\) och innerradien \(r=3-\sqrt{x}\).',
  r'Brickmetoden ger \[V=\pi\int_0^4\left(9-(3-\sqrt{x})^2\right)dx.\]',
  r'Integranden är \(6\sqrt{x}-x\), med primitiv funktion \(4x^{3/2}-x^2/2\). Insättning ger \(V=\pi(32-8)\).',
  r'<strong>Svar:</strong> Volymen är \(24\pi\) volymenheter.'],
}
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,rows in steps.items():
 old=by_id[task_id]['s'];new='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+s+'</p></li>' for s in rows)+'</ol></div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
 raw=raw[:start]+segment.replace(before,after,1)+raw[end:]
p.write_text(raw,encoding='utf-8')
