"""Förtydliga tre granskade frågor om korrelation och statistisk slutsats."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
fig='''<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 215" role="img" aria-label="Två punktdiagram med samma skala. A har fem punkter på en fallande rät linje. B har fem punkter med fallande trend som inte ligger på en rät linje." style="width:100%;max-width:580px"><title>Punktmoln A och B</title><rect width="580" height="215" fill="#fff"/><g fill="none" stroke="#334155" stroke-width="2"><path d="M55 25V175H245"/><path d="M335 25V175H525"/></g><g font-family="Arial,sans-serif" font-size="20" fill="#1e293b"><text x="55" y="20">Punktmoln A</text><text x="335" y="20">Punktmoln B</text><text x="245" y="196">x</text><text x="36" y="35">y</text><text x="525" y="196">x</text><text x="316" y="35">y</text></g><g fill="#176a89"><circle cx="75" cy="45" r="5"/><circle cx="110" cy="70" r="5"/><circle cx="145" cy="95" r="5"/><circle cx="180" cy="120" r="5"/><circle cx="215" cy="145" r="5"/><circle cx="355" cy="55" r="5"/><circle cx="390" cy="45" r="5"/><circle cx="425" cy="105" r="5"/><circle cx="460" cy="90" r="5"/><circle cx="495" cy="155" r="5"/></g></svg></span>'''
C={
'5.198':[None,'I A ligger alla punkter exakt på en fallande linje; B har en negativ trend men är inte perfekt.','Båda är negativa, men A är perfekt linjärt och B är det inte.','En fallande trend innebär negativ, inte positiv, korrelation.'],
'5.512':['Korrelation är samvariation; kausalitet handlar om orsak och verkan.','Orsakssamband kan ibland undersökas genom välplanerade experiment.','En stark korrelation visar samvariation men bevisar inte orsak.',None],
'5.90':['En statistiskt signifikant skillnad kan vara så liten att den har liten praktisk betydelse.','Signifikans garanterar inte att urvalet är representativt.','Signifikans ger ingen sådan garanti för alla populationer.',None]}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  if id=='5.198':
   t='<p>Diagrammen visar två punktmoln. Vilket påstående beskriver deras linjära samband bäst? Välj ett alternativ.</p>'+fig
   sol='<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför riktning och hur väl punkterna följer en linje</strong></p><p>I A ligger alla punkter exakt på en fallande rät linje. Sambandet är därför perfekt negativt.</p><p>I B finns också en fallande trend, men punkterna ligger inte på en rät linje. Det negativa linjära sambandet är därmed svagare än i A.</p><p class="facit-svar"><strong>Svar:</strong> A visar starkare negativ korrelation än B.</p></div>'
  elif id=='5.512':
   t='<p>Vilket påstående om korrelation och orsak är sant? Välj ett alternativ.</p>'
   sol='<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Samvariation visar inte orsaken</strong></p><p>Korrelation beskriver hur två variabler samvarierar. En bakomliggande faktor kan påverka båda, så samvariation visar inte i sig att den ena orsakar den andra.</p><p>Välplanerade experiment kan ibland undersöka orsakssamband. Även ett starkt korrelationsvärde bevisar inte orsak.</p><p class="facit-svar"><strong>Svar:</strong> En korrelation visar samvariation men är inte i sig ett bevis för orsakssamband.</p></div>'
  else:
   t='<p>Vad innebär statistisk signifikans på en vald signifikansnivå? Välj ett alternativ.</p>'
   sol='<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför resultatet med nollhypotesen</strong></p><p>Om nollhypotesen och testets modell stämmer beräknas hur sannolikt ett minst lika extremt resultat är. När p-värdet ligger under den valda signifikansnivån kallas resultatet statistiskt signifikant.</p><p>Det garanterar inte att skillnaden är praktiskt viktig eller att urvalet är representativt.</p><p class="facit-svar"><strong>Svar:</strong> Ett minst lika extremt resultat är enligt nollhypotesen och modellen tillräckligt ovanligt på den valda nivån.</p></div>'
  for k,v in [('t',t),('s',sol)]:
   old='"'+k+'": '+json.dumps(q[k],ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,'"'+k+'": '+json.dumps(v,ensure_ascii=False),1)
  if id in {'5.512','5.90'}:
   old=q['alternativ'][3]['txt'];new='En korrelation visar samvariation men är inte i sig ett bevis för orsakssamband.' if id=='5.512' else 'Om nollhypotesen och testets modell stämmer är ett minst lika extremt resultat så ovanligt att p-värdet ligger under den valda signifikansnivån.'
   a='"txt": '+json.dumps(old,ensure_ascii=False);assert chunk.count(a)==1;chunk=chunk.replace(a,'"txt": '+json.dumps(new,ensure_ascii=False),1)
  assert len(q['alternativ'])==len(C[id]) and sum(a['ratt'] for a in q['alternativ'])==1
  for alt,text in zip(q['alternativ'],C[id]):
   if alt['ratt']:assert text is None;continue
   assert text and 'kommentar' not in alt
   pattern=r'"txt"\s*:\s*'+re.escape(json.dumps(alt['txt'],ensure_ascii=False))+r'\s*,\s*"ratt"\s*:\s*false'
   chunk,n=re.subn(pattern,lambda m:m.group(0)+', "kommentar": '+json.dumps(text,ensure_ascii=False),chunk,count=1);assert n==1,(id,alt['txt'])
  assert json.loads(chunk)['id']==id;changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==set(C)
for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8');print('Ändrade:',', '.join(sorted(found)))
