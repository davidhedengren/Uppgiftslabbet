"""Ta bort en rapporterad begreppsfråga ur träning och förtydliga liknande."""
import json
import re
from pathlib import Path

path=Path(__file__).resolve().parent.parent/'uppgifterma2.js'
source=path.read_text(encoding='utf8');dec=json.JSONDecoder();pos=source.index('[')+1;changes=[];seen=set()
updates={
 '3.495':{'spel':False},
 '3.327':{
  't':'<p>Två vinklar har tillsammans summan \\(90^\\circ\\). Den ena är \\(35^\\circ\\). Hur stor är den andra vinkeln?</p>',
  's':'<div class="facit-v2 facit-stegvis"><p>Vinklarna har tillsammans summan \\(90^\\circ\\). Subtrahera den kända vinkeln:</p><div class="facit-matte">\\[90^\\circ-35^\\circ=55^\\circ.\\]</div><p class="facit-svar"><strong>Svar:</strong> \\(55^\\circ\\).</p></div>',
  'ledtrad':'<p>Hur mycket saknas från \\(35^\\circ\\) upp till \\(90^\\circ\\)?</p>'},
 '3.2075':{
  't':'<p>Två vinklar har tillsammans summan \\(90^\\circ\\). Den ena är \\(24^\\circ\\) större än den andra. Hur stor är den större vinkeln? Svara i grader.</p>',
  's':'<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Ställ upp en ekvation</strong></p><p>Kalla den större vinkeln \\(v\\). Den mindre är då \\(v-24^\\circ\\). Tillsammans är de \\(90^\\circ\\):</p><div class="facit-matte">\\[v+(v-24^\\circ)=90^\\circ.\\]</div><p class="facit-rubrik"><strong>Lös och kontrollera</strong></p><div class="facit-matte">\\[2v=114^\\circ\\quad\\Rightarrow\\quad v=57^\\circ.\\]</div><p>Den mindre vinkeln är \\(33^\\circ\\). Summan är \\(90^\\circ\\) och skillnaden är \\(24^\\circ\\).</p><p class="facit-svar"><strong>Svar:</strong> \\(57^\\circ\\).</p></div>',
  'ledtrad':'<p>Kalla den större vinkeln \\(v\\). Hur uttrycker du den mindre, och vad är summan?</p>',
  'typ':'vinklar med given summa och skillnad'}
}
while True:
    while source[pos].isspace() or source[pos]==',':pos+=1
    if source[pos]==']':break
    q,end=dec.raw_decode(source,pos);ident=q.get('id')
    if ident in updates:
        chunk=source[pos:end]
        for key,val in updates[ident].items():
            pattern=r'("'+re.escape(key)+r'"\s*:\s*)'+re.escape(json.dumps(q[key],ensure_ascii=False))
            chunk,count=re.subn(pattern,lambda m:m.group(1)+json.dumps(val,ensure_ascii=False),chunk,count=1)
            assert count==1,(ident,key)
        assert json.loads(chunk)['id']==ident;changes.append((pos,end,chunk));seen.add(ident)
    pos=end
assert seen==set(updates)
for start,end,chunk in reversed(changes):source=source[:start]+chunk+source[end:]
json.loads(source[source.index('['):source.rindex(']')+1]);path.write_text(source,encoding='utf8');print('Ändrade:',', '.join(sorted(seen)))
