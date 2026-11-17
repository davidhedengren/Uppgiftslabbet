import json,re,collections,sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from monster import M
b=json.load(open('bank_t.json',encoding='utf-8'))
koder=['fy1','fy2','ma1','ma2','mato1','mato2','matf1']
val=["Välj ett alternativ","Markera det korrekta alternativet","Du kan svara med","Skriv svaret som ett vanligt tal","(Svara i …)","Svara i … (utan parentes)","<sak> på <tal> kg","vågrät/lodrät","från vila","positiv riktning/räknas som positiv","med tecken","andra krafters impuls / den korta stöten","Behandla … som / i en förenklad modell","formel i frågan (X-lag:/-ekvationen:)","Bortse från","En elev säger/påstår/menar","sammanlagda/sammanlagt","Anta att","digitalt verktyg","Två tal …: X och X"]
print('%-42s'%'mönster'+''.join('%7s'%k for k in koder))
for n in val:
  r=re.compile(M[n]); row=[]
  for kod in koder:
    row.append(sum(1 for k,t in b.items() if k.startswith(kod+'|') and r.search(t)))
  print('%-42s'%n+''.join('%7d'%x for x in row))
