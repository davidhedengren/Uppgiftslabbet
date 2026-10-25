"""Avgränsade, manuellt granskade rättningar. Ändra bara de angivna objekten."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def p(s): return '<p>'+s+'</p>'
def m(s): return r'\('+s+r'\)'
def eq(s): return '<div class="facit-matte">'+r'\['+s+r'\]'+'</div>'
def sol(body,answer): return '<div class="facit-v2 facit-stegvis">'+body+'<p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def revise(bank,q):
 if bank=='ma1':
  if q['id']=='1.963':
   q['t']=p('En penna kostar '+m('x')+' kr. Skriv ett förenklat uttryck för priset på fyra sådana pennor.')
   q['s']=sol(p('Fyra pennor kostar fyra gånger priset för en penna. När ett tal multipliceras med en bokstav kan multiplikationstecknet utelämnas.')+eq(r'4\cdot x=4x'),m('4x')+' kr.')
   q['ledtrad']=p('Hur får du totalpriset när varje penna kostar lika mycket?')
   q['familjTidigare']=[v for v in dict.fromkeys(q.get('familjTidigare',[])+[q['familj']]) if v!='Multiplikation av tal och bokstäver']
   q['familj']='Multiplikation av tal och bokstäver'
   q['svarEnhet']='kr'
  if q['id']=='0.649':
   q['t']=p('Vilket påstående stämmer om det negativa talet '+m(r'-3{,}4\cdot10^5')+'? (Välj ett alternativ.)')
   q['alternativ'][-1]['txt']='Det är redan skrivet i grundpotensform.'
   q['s']=sol(p('Skriv först det positiva talet i grundpotensform. Talet 3,4 är minst 1 och mindre än 10, så '+m(r'3{,}4\cdot10^5')+' är i grundpotensform.')+p('För att ange det negativa talet sätter vi ett minustecken framför. Exponenten ska inte ändras.'),'Det är redan skrivet i grundpotensform.')
   q['ledtrad']=p('Börja med att betrakta det positiva talet. Minustecknet visar sedan att talet är negativt.')
  if q['id'] in ['0.644','0.648'] and 'alternativ' not in q['t']:
   q['t']=q['t'].replace('</p>',' (Välj ett alternativ.)</p>',1)
  if q['id']=='0.1073':
   q['svarFormat']='grundpotensform'
   q['s']=q['s'].replace(r'=\frac{5{,}6}{5{,}97}\cdot10^{-13}\approx',r'=\frac{5{,}6}{5{,}97}\cdot10^{-13}\]</div><div class="facit-matte">\[\approx')
 if bank=='mato2' and q['id']=='3.22':
  bodies=[p('Grafen skär x-axeln vid x = 1. Areorna under och över axeln räknas båda positiva.')+eq(r'A=\int_0^1(1-x)\,dx+\int_1^3(x-1)\,dx')+p('De två områdena är trianglar med bas och höjd 1 respektive 2.')+eq(r'A=\frac{1\cdot1}{2}+\frac{2\cdot2}{2}=\frac52'),
   p('Grafen skär x-axeln vid x = 2. De två trianglarna har båda basen 2 och höjden 4.')+eq(r'A=\frac{2\cdot4}{2}+\frac{2\cdot4}{2}=8'),
   p('På intervallet ligger grafen på eller över x-axeln. Arean är därför integralen av sin x.')+eq(r'A=\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi')+eq(r'A=-(-1)-(-1)=2')]
  for d,body,a in zip(q['spelDelar'],bodies,[m(r'\frac52')+' a.e.','8 a.e.','2 a.e.']):d['s']=sol(body,a)
  q['s']=''.join(p('<strong>'+d['etikett']+')</strong>')+d['s'] for d in q['spelDelar'])
  q['ledtrad']=p('Undersök om grafen byter sida om x-axeln. Delarnas geometriska areor ska adderas, inte ta ut varandra.')
 if bank=='mato2' and q['id']=='3.51':
  bodies=[p('Vattenmängden minskar när utflödet är större än inflödet, alltså när q(t) är negativt. Den börjar öka när q(t) blir positivt.')+eq(r'3t-6=0\quad\Rightarrow\quad t=2')+p('q(t) är negativt före 2 h och positivt efter 2 h. Därför är vattenmängden som minst vid denna tidpunkt.'),
   p('Integralen av q(t) ger ändringen av vattenmängden. Lägg till de 120 m³ som fanns från början.')+eq(r'V(2)=120+\int_0^2(3t-6)\,dt')+eq(r'=120+[1{,}5t^2-6t]_0^2')+eq(r'=120+6-12=114'),
   p('Integralen ger nettoändringen under de åtta timmarna. Lägg den till startvolymen.')+eq(r'V(8)=120+\int_0^8(3t-6)\,dt')+eq(r'=120+[1{,}5t^2-6t]_0^8')+eq(r'=120+96-48=168')]
  for d,body,a in zip(q['spelDelar'],bodies,['Efter 2 h.','114 m³.','168 m³.']):d['s']=sol(body,a)
  q['s']=''.join(p('<strong>'+d['etikett']+')</strong>')+d['s'] for d in q['spelDelar'])
 if bank=='mato2' and q['id'] in ['2.263','2.225','2.193']:
  q['traningsniva']=4
  q['formaga']=list(dict.fromkeys(q['formaga']+['begrepp']))
  if q['id']=='2.263':
   q['s']=sol(p('När x = 3 är den inre funktionens värde 2·3−1 = 5. Därför är det just det givna värdet f′(5) som behövs.')+p('Kedjeregeln multiplicerar den yttre derivatan med den inre derivatan, som är 2.')+eq(r"h'(x)=f'(2x-1)\cdot2")+eq(r"h'(3)=f'(5)\cdot2=4\cdot2=8"),m('8')+'.')

if __name__=='__main__':
 for bank in ['ma1','mato2']:
  path=ROOT/('uppgifter'+bank+'.js');raw=path.read_text();qs=json.loads(raw[raw.index('['):raw.rindex(']')+1])
  for q in qs:
   before=json.dumps(q);revise(bank,q)
   if before==json.dumps(q):continue
   pos=raw.index('"id": "'+q['id']+'"');start=raw.rfind('{',0,pos);_,n=json.JSONDecoder().raw_decode(raw[start:]);raw=raw[:start]+json.dumps(q,ensure_ascii=False,indent=2)+raw[start+n:];print(bank,q['id'])
  path.write_text(raw)
