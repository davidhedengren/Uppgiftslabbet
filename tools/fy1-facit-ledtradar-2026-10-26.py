"""Manuell återkontroll av sex enhetsuppgifter med saknad ledtråd."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REVISIONS={
'2.321':(r'<p>Vad betyder prefixet mikro? Skriv gärna längden med en tiopotens innan du skriver den i decimalform.</p>',r'<p>Prefixet mikro betyder en miljondel. För att omvandla från mikrometer till meter multiplicerar vi därför med \(10^{-6}\).</p>\[75\text{ µm}=75\cdot10^{-6}\text{ m}\]\[=0{,}000075\text{ m}\]'),
'2.322':(r'<p>Omvandla båda sidlängderna till meter innan du beräknar rektangelns area.</p>',r'<p>Arean är längden gånger bredden. Vi omvandlar först båda längderna till meter.</p>\[l=\frac{120}{100}=1{,}20\text{ m}\]\[b=\frac{80}{100}=0{,}80\text{ m}\]<p>Därefter blir arean</p>\[A=lb=1{,}20\cdot0{,}80=0{,}96\text{ m}^2.\]'),
'2.323':(r'<p>Både volymenheten och tidsenheten ska ändras. Om du vet hur mycket som passerar på en minut, hur får du volymen under en sekund?</p>',r'<p>En liter motsvarar 1 000 cm³. Pumpen flyttar därför</p>\[3{,}6\cdot1000=3600\text{ cm}^3\]<p>på en minut. En minut är 60 sekunder. Volymen per sekund blir då</p>\[q=\frac{3600\text{ cm}^3}{60\text{ s}}=60\text{ cm}^3/\text{s}.\]'),
'2.324':(r'<p>Skriv den totala tiden och tiden för en mätning i samma enhet. Hur får du sedan antalet mätningar?</p>',r'<p>Antalet mätningar är den tillgängliga tiden dividerad med tiden för en mätning. Båda tiderna måste ha samma enhet.</p>\[t_{\text{tot}}=2\cdot60=120\text{ s}\]\[t_{\text{mätning}}=150\cdot10^{-3}=0{,}150\text{ s}\]<p>Det ger</p>\[N=\frac{120}{0{,}150}=800.\]<p>Resultatet är ett heltal, så alla 800 mätningar hinner avslutas.</p>'),
'2.325':(r'<p>Tänk dig vattnet som ett jämnt lager över hela taket. Vilka mått behöver du för att få lagrets volym?</p>',r'<p>Vattnet kan ses som ett lager med takets area som basyta och regnmängden som höjd. Volymen är basytans area gånger höjden.</p>\[h=12\text{ mm}=0{,}012\text{ m}\]\[V=Ah=35\cdot0{,}012=0{,}42\text{ m}^3\]<p>En kubikmeter motsvarar 1 000 liter:</p>\[V=0{,}42\cdot1000=420\text{ liter}.\]'),
'2.326':(r'<p>Börja med skillnaden mellan slutvolym och startvolym. Omvandla sedan ökningen från milliliter till mikroliter.</p>',r'<p>Det som fyllts på är skillnaden mellan slutvolymen och startvolymen.</p>\[\Delta V=1{,}8-0{,}6=1{,}2\text{ ml}\]<p>En milliliter är 1 000 mikroliter. Volymökningen blir därför</p>\[\Delta V=1{,}2\cdot1000=1200\text{ µl}.\]')
}
def install():
 p=ROOT/'uppgifter.js';raw=p.read_text()
 for id,(hint,body) in REVISIONS.items():
  pos=re.search(r'"id"\s*:\s*"'+re.escape(id)+'"',raw).start();start=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[start:])
  answer=re.search(r'<p class="facit-svar">[\s\S]*?</p>',q['s']).group()
  q['ledtrad']=hint;q['s']='<div class="facit-v2">'+body+answer+'</div>'
  indent=raw[raw.rfind('\n',0,start)+1:start];raw=raw[:start]+json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n'+indent)+raw[start+n:]
 p.write_text(raw)
if __name__=='__main__':install();print('6 fy1-facit och uppgiftsspecifika ledtrådar klara.')
