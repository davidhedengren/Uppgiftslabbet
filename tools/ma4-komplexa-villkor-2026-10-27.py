import json
from pathlib import Path

steps={
 '4.17': [
  r'Sätt \(z=x+iy\) och kvadrera avstånden: \((x-2)^2+(y-1)^2=4((x+1)^2+y^2)\).',
  r'Utveckling och samling ger \(3x^2+3y^2+12x+2y-1=0\). Dividera med 3 och kvadratkomplettera:',
  r'\[(x+2)^2+(y+1/3)^2=40/9.\]',
  r'<strong>Svar:</strong> Mängden är en cirkel med centrum \((-2,-1/3)\) och radie \(\sqrt{40}/3=2\sqrt{10}/3\).'],
 '4.316': [
  r'Sätt \(z=x+iy\). Lika avstånd till \(2-i\) och \(-1+2i\) ger \((x-2)^2+(y+1)^2=(x+1)^2+(y-2)^2\).',
  r'Förenkla till \(y=x\). Villkoret \(|z|=3\) ger samtidigt \(x^2+y^2=9\).',
  r'Sätt in \(y=x\): \(2x^2=9\), så \(x=y=\pm3\sqrt2/2\) med samma tecken.',
  r'<strong>Svar:</strong> \(z=\frac{3\sqrt2}{2}(1+i)\) eller \(z=-\frac{3\sqrt2}{2}(1+i)\).'],
 '4.272': [
  r'Kvadrera båda leden: \((x-2)^2+y^2=4((x+1)^2+y^2)\).',
  r'Utveckla och samla termerna: \(x^2+4x+y^2=0\). Kvadratkomplettering ger \((x+2)^2+y^2=4\).',
  r'<strong>Svar:</strong> Mängden är en cirkel med centrum \((-2,0)\) och radie 2.'],
 '4.299': [
  r'Låt \(z=x+iy\). Kvadrera avstånden till \(2\) och \(-2i\): \((x-2)^2+y^2=x^2+(y+2)^2\).',
  r'Utveckla och ta bort gemensamma termer: \(-4x=4y\), alltså \(y=-x\).',
  r'<strong>Svar:</strong> Mängden är den räta linjen \(y=-x\), genom origo med lutning \(-1\).'],
 '4.302': [
  r'Sätt \(z=x+iy\). Cirkeln ges av \((x-1)^2+y^2=4\) och linjen av \(y=x-1\).',
  r'Insättning ger \(2(x-1)^2=4\), så \(x-1=\pm\sqrt2\). Samtidigt är \(y=\pm\sqrt2\), med samma tecken.',
  r'<strong>Svar:</strong> \(z=1+\sqrt2+i\sqrt2\) eller \(z=1-\sqrt2-i\sqrt2\).'],
 '4.306': [
  r'Triangelolikheten ger \(|z+3|\le |z|+3=5\), eftersom \(|z|=2\).',
  r'Välj \(z=2\), som uppfyller \(|z|=2\). Då är \(|z+3|=5\), så gränsen uppnås.',
  r'<strong>Svar:</strong> Största värdet är 5 och det fås exempelvis för \(z=2\).'],
 '4.314': [
  r'Centrum är \(1=(1,0)\). Hörnet \(1+i\) ligger en enhet ovanför centrum.',
  r'I en kvadrat ligger hörnen på samma avstånd från centrum och efter varandra med en kvarts varvs vinkel. De övriga ligger därför en enhet åt höger, nedåt och åt vänster.',
  r'<strong>Svar:</strong> De övriga hörnen är \(2\), \(1-i\) och \(0\).'],
}
p=Path(__file__).resolve().parent.parent/'uppgiftermato2.js';raw=p.read_text(encoding='utf-8')
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);by_id={q['id']:q for q in bank}
for task_id,rows in steps.items():
 old=by_id[task_id]['s'];new='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+s+'</p></li>' for s in rows)+'</ol></div>'
 start=raw.index(f'    "id": "{task_id}"');end=raw.index('\n  },',start);segment=raw[start:end]
 before=json.dumps(old,ensure_ascii=False);after=json.dumps(new,ensure_ascii=False);assert segment.count(before)==1
 raw=raw[:start]+segment.replace(before,after,1)+raw[end:]
p.write_text(raw,encoding='utf-8')
