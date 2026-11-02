"""Rätta rapporterade frågor, ledtrådar och genomgående punktterminologi."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent.parent
A={
 '5.272':{
  't':'<p>En fabrik tillverkar komponenter. I genomsnitt är 3 % av komponenterna felaktiga. Hur många komponenter behöver fabriken tillverka för att det i genomsnitt ska bli 24 felaktiga?</p>',
  's':r'<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Låt antalet komponenter vara n</strong></p><p>Tre procent av antalet ska motsvara 24 felaktiga komponenter.</p>\[0{,}03n=24\quad\Rightarrow\quad n=\frac{24}{0{,}03}=800.\]<p class="facit-svar"><strong>Svar:</strong> 800 komponenter.</p></div>',
  'ledtrad':'<p>Hur kan 3 % av antalet komponenter skrivas som ett uttryck?</p>','miniräknare':True,'svarFormat':'numeriskt'},
 '5.485':{
  't':'<p>Ett försäkringsbolag har många likadana försäkringar. Under ett år får i genomsnitt 0,5 % av kunderna en vattenskada, och ersättningen för varje skada är i genomsnitt 80 000 kr. Hur stor är den genomsnittliga ersättningen per försäkring och år?</p>',
  's':r'<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Fördela den genomsnittliga ersättningen</strong></p><p>Andelen skador är \(0{,}5\,\%=0{,}005\). Multiplicera andelen med den genomsnittliga ersättningen per skada.</p>\[0{,}005\cdot80\,000=400\ \text{kr}.\]<p class="facit-svar"><strong>Svar:</strong> 400 kr per försäkring och år.</p></div>',
  'ledtrad':'<p>Hur stor andel får en ersättning? Multiplicera andelen med ersättningen för en skada.</p>','svarEnhet':'kr'},
 '5.486':{
  't':'<p>Ett försäkringsbolag försäkrar många cyklar som var och en är värd 12 000 kr. Under ett år blir i genomsnitt 3 % av cyklarna stulna. Bolaget ersätter hela värdet för varje stulen cykel. Hur stor är bolagets genomsnittliga utbetalning per försäkrad cykel och år?</p>',
  's':r'<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Fördela ersättningen på alla cyklar</strong></p><p>Andelen stölder är \(3\,\%=0{,}03\). Multiplicera andelen med ersättningen för en stulen cykel.</p>\[0{,}03\cdot12\,000=360\ \text{kr}.\]<p class="facit-svar"><strong>Svar:</strong> 360 kr per cykel och år.</p></div>',
  'ledtrad':'<p>Tänk dig 100 försäkrade cyklar. Hur många ersättningar betalas i genomsnitt ut och hur fördelas summan per cykel?</p>','svarEnhet':'kr'},
 '5.490':{
  't':'<p>Risken för en olycka är 1 på 1 000 000 per resa. En person gör 500 resor under ett år. Anta att risken är lika stor och oberoende för varje resa. Ungefär hur stor är risken för minst en olycka under året? Svara med fyra decimaler.</p>',
  's':r'<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Beräkna risken under året</strong></p><p>Sannolikheten för minst en olycka är ett minus sannolikheten att undvika olyckor på alla 500 oberoende resor.</p>\[1-(1-0{,}000001)^{500}\approx0{,}000499875.\]<p class="facit-svar"><strong>Svar:</strong> \(0{,}0005\) med fyra decimaler.</p></div>',
  'ledtrad':'<p>Beräkna först sannolikheten att ingen olycka inträffar och använd sedan komplementhändelsen.</p>','tolerans':0}}
B={
 '3.1227':{'traningsniva':5},
 '3.518':{'traningsniva':4,'t':r'<p>En modell för effekten från en solpanel under en dag är \(P(t)=760e^{-0{,}08(t-6)^2}\) watt för \(0\le t\le12\). Här är \(t\) antalet timmar efter att mätningen börjar. Bestäm när effekten är störst och hur stor den är.</p>'},
 '2.308':{'traningsniva':2,'ledtrad':'<p>Derivera varje term med potensregeln. Derivera sedan uttrycket du får en gång till.</p>'},
 '2.1206':{'traningsniva':4},
 '2.1233':{'traningsniva':4}}
word=re.compile(r'\b(?:minpunkterna|minpunkter|minpunkten|minpunkt|maxpunkterna|maxpunkter|maxpunkten|maxpunkt)\b',re.I)
def replaceword(m):
 x=m.group();v=re.sub(r'^min', 'minimi',x,flags=re.I) if x.lower().startswith('min') else re.sub(r'^max','maximi',x,flags=re.I)
 return v[0].upper()+v[1:] if x[0].isupper() else v

def changefile(filename,edits,words=False):
 p=ROOT/filename;s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set();wordids=[]
 while True:
  while s[pos].isspace() or s[pos]==',':pos+=1
  if s[pos]==']':break
  q,end=dec.raw_decode(s,pos);id=q.get('id');updates=dict(edits.get(id,{}))
  if words:
   for k in ('t','s','ledtrad'):
    if isinstance(q.get(k),str) and word.search(q[k]):updates[k]=word.sub(replaceword,q[k]);wordids.append(id)
  if not updates and not (id=='2.302' and filename=='uppgiftermato1.js'):pos=end;continue
  chunk=s[pos:end]
  def setfield(k,v):
   nonlocal chunk
   if k not in q:
    i=chunk.rfind('}');chunk=chunk[:i].rstrip()+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  '+chunk[i:];return
   old=json.dumps(q[k],ensure_ascii=False);pattern=r'("'+re.escape(k)+r'"\s*:\s*)'+re.escape(old)
   chunk,n=re.subn(pattern,lambda m:m.group(1)+json.dumps(v,ensure_ascii=False),chunk,count=1);assert n==1,(filename,id,k)
  for k,v in updates.items():setfield(k,v)
  if id=='2.302' and filename=='uppgiftermato1.js':
   def prefer(s):
    r=s.replace(r'f^{\prime}(x)=2 x \left(9 x - 1\right)',r'f^{\prime}(x)=18x^2-2x').replace("f'(x)=2x(9x-1)","f'(x)=18x^2-2x")
    assert r!=s;return r
   setfield('s',prefer(q['s']))
   old=json.dumps(q['rättSvar'][0],ensure_ascii=False);new=json.dumps("f'(x)=18*x^2-2*x",ensure_ascii=False)
   assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
   old=json.dumps(q['spelDelar'][0]['s'],ensure_ascii=False);new=json.dumps(prefer(q['spelDelar'][0]['s']),ensure_ascii=False)
   assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  parsed=json.loads(chunk);assert parsed['id']==id
  for k,v in updates.items():assert parsed[k]==v
  changes.append((pos,end,chunk));found.add(id);pos=end
 assert set(edits).issubset(found),(filename,set(edits)-found)
 for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
 json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8')
 print(filename,'ändrade',sorted(found),'punktterminologi',sorted(set(wordids)))
changefile('uppgifterma1.js',A)
changefile('uppgiftermato1.js',B,True)
