"""Gemensam serialisering och SVG för manuellt författade nivå-3-omgångar."""
from pathlib import Path
import json,html,math,re,sys
ROOT=Path(__file__).resolve().parents[1]
def p(s):return '<p>'+s+'</p>'
def m(s):return r'\('+s+r'\)'
def eq(s):return '<div class="facit-matte">'+r'\['+s+r'\]'+'</div>'
def step(title,body):return '<p class="facit-rubrik">'+title+'</p>'+body
def table(headers,rows):
 return '<table class="data" style="width:100%;max-width:460px;text-align:center"><thead><tr>'+''.join('<th scope="col">'+str(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def text(x,y,s,anchor='middle',size=18):return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-size="{size}" font-family="Arial,sans-serif" fill="#183348">{html.escape(str(s))}</text>'
def graph(key,title,xlim,ylim,lines,xticks,yticks,xlabel='x',ylabel='y',dots=(),shade=()):
 X=lambda v:65+365*(v-xlim[0])/(xlim[1]-xlim[0]);Y=lambda v:250-200*(v-ylim[0])/(ylim[1]-ylim[0])
 body='<rect width="500" height="325" fill="white" rx="10"/>'
 for v in xticks:body+=f'<path d="M{X(v)} 50V250" stroke="#dbe3eb"/>'+text(X(v),276,str(v).replace('-', '−').replace('.',','),size=17)
 for v in yticks:body+=f'<path d="M65 {Y(v)}H430" stroke="#dbe3eb"/>'+text(53,Y(v)+6,str(v).replace('-','−').replace('.',','),'end',17)
 if xlim[0]<=0<=xlim[1]:body+=f'<path d="M{X(0)} 48V252" stroke="#526777" stroke-width="1.7"/>'
 if ylim[0]<=0<=ylim[1]:body+=f'<path d="M63 {Y(0)}H435" stroke="#526777" stroke-width="1.7"/>'
 body+=text(250,307,xlabel)+text(65,29,ylabel,'start')
 body+=f'<defs><clipPath id="clip-{key}"><rect x="63" y="48" width="370" height="205"/></clipPath></defs><g clip-path="url(#clip-{key})">'
 for polygon in shade:body+='<polygon points="'+' '.join(f'{X(x):.2f},{Y(y):.2f}' for x,y in polygon)+'" fill="#2196b5" fill-opacity="0.16"/>'
 for i,points in enumerate(lines):body+='<polyline points="'+' '.join(f'{X(x):.2f},{Y(y):.2f}' for x,y in points)+'" fill="none" stroke="'+['#096c9a','#b35316','#774596'][i%3]+'" stroke-width="3.2" stroke-linejoin="round"/>'
 for x,y,filled in dots:body+=f'<circle cx="{X(x)}" cy="{Y(y)}" r="5" fill="'+('#096c9a' if filled else 'white')+'" stroke="#096c9a" stroke-width="2"/>'
 body+='</g>'
 return '<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 325" style="width:100%;max-width:500px" role="img" aria-label="'+html.escape(title)+'"><title>'+html.escape(title)+'</title>'+body+'</svg></span>'
def curve(fn,a,b,n=120):return [(a+(b-a)*j/n,fn(a+(b-a)*j/n)) for j in range(n+1)]
class Round:
 def __init__(self,slug,course,area,family,start,chapter,tracks):
  self.slug,self.course,self.area,self.family,self.start,self.chapter,self.tracks=slug,course,area,family,start,chapter,tracks;self.tasks=[];self.cases={};self.notes={}
 def add(self,t,answer,steps,final,hint,why,fig='',fmt='numeriskt',unit=None,labels=None,options=None,family=None,calc=True,gg=False,good=(),bad=(),tol=None):
  id=f'{self.chapter}.{self.start+len(self.tasks)}'
  q=dict(id=id,kap=self.chapter,omr=self.area,kurs=self.tracks,familj=family or self.family,niva='C',poang='0/2/0',traningsniva=3,arbetsinsats=2,formaga=['begrepp','resonemang'] if options else ['begrepp','procedur'],miniräknare=calc,geogebra=gg,spel=True,självrättning=True,t=t+fig,s='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li>'+s+'</li>' for s in steps)+'</ol><p class="facit-svar"><strong>Svar: '+final+'</strong></p></div>',ledtrad=p(hint),rättSvar=answer,svarstyp='uttryck' if fmt=='uttryck' else 'numeriskt',svarFormat=fmt,tolerans=tol if tol is not None else (None if fmt in ['uttryck','exakt'] else 1e-9))
  if labels:q.update(svarstyp='flera_delar',svarFormat=[fmt]*len(labels),svarEtiketter=labels,svarsstruktur='ordnad',tolerans=[q['tolerans']]*len(labels))
  if options:q.update(svarstyp='alternativ',svarFormat='text',rättSvar=None,tolerans=None,alternativ=[dict(txt=a[0],ratt=a[1],**({'kommentar':p(a[2])} if len(a)>2 else {})) for a in options])
  if unit:q['svarEnhet']=unit
  self.tasks.append(q);self.cases[self.course+':'+id]=[list(good),list(bad)]
  self.notes[id]={'nivå':why,'figur':'Figur/tabell bär informationen.' if fig else 'Text/algebra är tillräcklig; ingen dekorativ figur.','verktyg':'GeoGebra och miniräknare för digital analys.' if gg else 'Miniräknare tillåten, men sambanden behöver tolkas av eleven.' if calc else 'Exakt algebra/begrepp prövas utan räknare.'}
  return q
 def install(self):
  path=ROOT/f'uppgifter{self.course}.js';s=path.read_text();b=json.loads(s[s.index('['):s.rindex(']')+1]);existing={q['id'] for q in b}&{q['id'] for q in self.tasks}
  if '--refresh' in sys.argv:
   assert existing=={q['id'] for q in self.tasks}
   for q in self.tasks:
    pos=s.index('"id": "'+q['id']+'"');start=s.rfind('{',0,pos);_,n=json.JSONDecoder().raw_decode(s[start:]);s=s[:start]+json.dumps(q,ensure_ascii=False,indent=2)+s[start+n:]
   path.write_text(s)
  else:
   assert not existing
   end=s.rindex(']');path.write_text(s[:end].rstrip()+','+json.dumps(self.tasks,ensure_ascii=False,indent=2)[1:-1]+'\n'+s[end:])
  (ROOT/'tools'/f'{self.slug}.cases.json').write_text(json.dumps(self.cases,ensure_ascii=False,indent=2)+'\n')
  (ROOT/'agent'/f'{self.slug}.json').write_text(json.dumps(self.notes,ensure_ascii=False,indent=2)+'\n')
  print(','.join(q['id'] for q in self.tasks))
