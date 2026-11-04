"""Apply reviewed line breaks without changing equation tokens, 2026-11-04."""
from render import *
plan=json.loads((ROOT/'tools/fy1-facit-kap23/layout-plan.json').read_text())
for change in plan:
 q=byid[change['id']];found=False
 for obj in [q]+q.get('spelDelar',[]):
  old,new=change['old'],change['new']
  if old in obj['s']:obj['s']=obj['s'].replace(old,new);found=True
  elif change.get('previous') and change['previous'] in obj['s']:obj['s']=obj['s'].replace(change['previous'],new);found=True
  elif new in obj['s']:found=True
 assert found,change['id']
 changes[q['id']]='Åtgärdad'
q=byid['3.65']
old='<p>Anta att kulan startar från vila och pröva en modell med konstant acceleration. Kan mätpunkterna bevisa att accelerationen varit konstant mellan mätningarna? Motivera.</p>'
if old in q['t']:
 q['t']=q['t'].replace(old,'').replace('<ol type="a">','<p>Anta att kulan startar från vila och pröva en modell med konstant acceleration.</p>\n<ol type="a">').replace('</ol>','<li>Kan mätpunkterna bevisa att accelerationen varit konstant mellan mätningarna? Motivera.</li></ol>')
changes['3.65']='Åtgärdad'
# Keep the exact speed from a) in the acceleration calculation in 3.388.
q=byid['3.388']
for obj in [q]+q.get('spelDelar',[]):
 obj['s']=obj['s'].replace(r"\frac{18-12{,}91}{11}",r"\frac{18-\frac{142}{11}}{11}")
if __name__=='__main__':save();print('Adjusted',len(changes),'tasks')
