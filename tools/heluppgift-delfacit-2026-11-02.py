"""Lägg till lokala delfacit utan att ändra heluppgiftens lösning."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent.parent
EDIT={
 'uppgifterma1.js':{
  '2.201':[
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför skillnaderna</strong></p><p>När \(x\) ökar med 1 ökar \(y\) med 10 varje gång: \(15-5=25-15=35-25=10\).</p><p><strong>Svar:</strong> Tabellen beskriver en linjär modell eftersom differensen är konstant.</p></div>''',
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför kvoterna</strong></p><p>När \(x\) ökar med 1 multipliceras \(y\) varje gång med samma faktor: \(15/5=45/15=135/45=3\).</p><p><strong>Svar:</strong> Tabellen beskriver en exponentiell modell eftersom förändringsfaktorn är konstant.</p></div>''',
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Använd startvärde och förändringsfaktor</strong></p><p>När \(x=0\) är \(y=5\), och för varje steg i \(x\) multipliceras värdet med 3.</p><p><strong>Svar:</strong> \(y=5\cdot3^x\).</p></div>'''],
  '4.22':[
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Använd Pythagoras sats</strong></p><p>De vinkelräta vektorerna bildar kateter med längderna 5 och 12. Summans längd blir</p>\[|\vec u+\vec v|=\sqrt{5^2+12^2}=13.\]<p><strong>Svar:</strong> 13.</p></div>''',
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Vänd en vektor</strong></p><p>Vektorn \(-\vec v\) är fortfarande vinkelrät mot \(\vec u\) och har längden 12. Pythagoras sats ger</p>\[|\vec u-\vec v|=\sqrt{5^2+12^2}=13.\]<p><strong>Svar:</strong> 13.</p></div>''']},
 'uppgiftermatf1.js':{
  '4.138':[
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Sätt derivatan till noll</strong></p><p>För en konstant lösning gäller \(y'=0\). Därför måste \(y(2-y)=0\).</p><p><strong>Svar:</strong> \(y=0\) och \(y=2\).</p></div>''',
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Undersök tecknet från startvärdet</strong></p><p>Mellan 0 och 2 är både \(y\) och \(2-y\) positiva, så lösningen växer. Den närmar sig jämviktslösningen \(y=2\) underifrån.</p><p><strong>Svar:</strong> \(y\) närmar sig 2 underifrån.</p></div>''',
   r'''<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Undersök tecknet från startvärdet</strong></p><p>För \(y&gt;2\) är \(y\) positiv och \(2-y\) negativ, så lösningen avtar. Den närmar sig jämviktslösningen \(y=2\) ovanifrån.</p><p><strong>Svar:</strong> \(y\) närmar sig 2 ovanifrån.</p></div>''']}
}
for filename,edits in EDIT.items():
 p=ROOT/filename;raw=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=raw.index('[')+1;changes=[];found=set()
 while True:
  while raw[pos].isspace() or raw[pos]==',':pos+=1
  if raw[pos]==']':break
  q,end=dec.raw_decode(raw,pos);id=q.get('id')
  if id in edits:
   assert 'delfacit' not in q,id
   segment=raw[pos:end];segment=segment[:-1]+',\n    "delfacit": '+json.dumps(edits[id],ensure_ascii=False)+'\n  }'
   assert json.loads(segment)['delfacit']==edits[id]
   changes.append((pos,end,segment));found.add(id)
  pos=end
 assert found==set(edits),(filename,found,set(edits))
 for start,end,segment in reversed(changes):raw=raw[:start]+segment+raw[end:]
 json.loads(raw[raw.index('['):raw.rindex(']')+1]);p.write_text(raw,encoding='utf8');print(filename,sorted(found))
