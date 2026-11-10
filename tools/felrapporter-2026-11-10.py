"""Manuellt granskad fysikprecision och kursavgränsning, fellogg 10 november."""
from pathlib import Path
import runpy,json
H=runpy.run_path(str(Path(__file__).with_name('felrapporter-2026-11-09.py')))
m,st,sol,joined=[H[x] for x in ['m','st','sol','joined']]
b=H['read']('uppgifter.js');old={q['id']:json.loads(json.dumps(q)) for q in b};d={q['id']:q for q in b}
q=d['3.217'];q['rättSvar']=46*12500/13;q['svarVardesiffror']=2;q['s']=q['s'].replace('44 230,77 m/s².',r'Cirka \(4{,}4\cdot10^4\) m/s².')
q=d['7.144'];q['svarVardesiffror']=[2,2]
a=sol([st(r'Värmeenergi: \(Q=mc\Delta T\)',r'<p>Massan är 20 g = 0,020 kg. Lös ut temperaturökningen.</p>'+m(r'\Delta T=\frac{100}{0{,}020\cdot140}\approx35{,}714\ \mathrm K'))],r'Temperaturen ökar med cirka 36 K (36 °C).')
bb=sol([st(r'Samma massa och temperaturökning: \(Q=mc\Delta T\)',r'<p>Förhållandet mellan energierna blir därför förhållandet mellan de specifika värmekapaciteterna. Då behöver vi inte avrunda temperaturökningen från a).</p>'+m(r'\frac{Q_v}{Q_{Hg}}=\frac{c_v}{c_{Hg}}')),st('Sätt in värdena',m(r'Q_v=100\cdot\frac{4180}{140}\approx2985{,}7\ \mathrm J'))],r'Vattnet tar upp cirka \(3{,}0\cdot10^3\) J, alltså 3,0 kJ.')
q['spelDelar'][0]['s']=a;q['spelDelar'][1]['s']=bb;q['s']=joined([a,bb]);q['spelDelar'][1]['t']=q['spelIntro']+'<p>Hur mycket energi tar 20 g vatten upp vid samma temperaturökning som kvicksilvret?</p>'
q['spelDelar'][0]['ledtrad']=r'<p>Lös ut temperaturökningen ur \(Q=mc\Delta T\). Använd massan i kg.</p>'
q['spelDelar'][1]['ledtrad']='<p>Massorna och temperaturökningarna är lika. Hur förhåller sig då energierna till de specifika värmekapaciteterna?</p>'
q=d['4.73'];q['rättSvar']=[6,.5*9.82,.5*9.82/.06,20+6*1.2/.5];q['svarVardesiffror']=[1,2,1,2]
for obj in [q,*q['spelDelar']]:
 obj['s']=obj['s'].replace('<strong>Svar:</strong> 81,83 N/m.','<strong>Svar:</strong> Cirka 80 N/m.').replace('<strong>Svar:</strong> 34,4 cm.','<strong>Svar:</strong> Cirka 34 cm.')
for obj in [q,q['spelDelar'][3]]:
 obj['s']=obj['s'].replace(r'x=\frac{1{,}2\cdot9{,}82}{81{,}83}\approx0{,}144\ \mathrm m=14{,}4\ \mathrm{cm}',r'\begin{aligned}x&=0{,}06\cdot\frac{1{,}2}{0{,}500}\\&=0{,}144\ \mathrm m=14{,}4\ \mathrm{cm}\end{aligned}').replace('med 1,2 kg, lös ut',r'med 1,2 kg: förlängningen är proportionell mot massan; lös ut')
q=d['4.539'];q['traningsniva']=4;q['arbetsinsats']=3;q['rättSvar']=2000/(12**2*9.82);q['svarVardesiffror']=2
q['s']=q['s'].replace(r'\mu\ge\frac{13{,}9}{9{,}82}\approx1{,}41',r'\mu\ge\frac{2\cdot1000}{12^2\cdot9{,}82}\approx1{,}414').replace('<strong>Svar:</strong> 1,41.','<strong>Svar:</strong> Minst cirka 1,4.')
# Hög precision i facit är inte samma sak som precision hos mätdata.
for id,answer,n,replacements in [
 ('3.216',60/.0047,2,[('12 765,96 m/s².',r'Cirka \(1{,}3\cdot10^4\) m/s².')]),
 ('3.218',[-6.75/.04,5.60/.04],[3,3],[('-168,75 m/s².','Cirka −169 m/s².')]),
 ('3.219',[9.82,9.82*1.2],[3,2],[('11,78 m/s.','Cirka 12 m/s.')]),
 ('7.143',150/(.0062*900)-12,2,[]),
 ('7.145',8800*3600/(4180*30),2,[])
]:
 q=d[id];q['rättSvar']=answer;q['svarVardesiffror']=n
 for obj in [q,*q.get('spelDelar',[])]:
  for a,z in replacements:obj['s']=obj['s'].replace(a,z)
# Temperaturkoefficientens modell är extra material, inte förutsatt grundkunskap.
for id in ['8.439','8.440','8.441','8.442','8.443','8.444']:
 q=d[id];q['spel']=False
 intro=r'<p><strong>Fördjupning: temperaturberoende resistans.</strong></p><p>Använd modellen \(R=R_0(1+\alpha\Delta T)\), där \(R_0\) är resistansen vid starttemperaturen, \(\Delta T\) temperaturändringen och \(\alpha\) temperaturkoefficienten.</p>'
 if not q['t'].startswith('<p><strong>Fördjupning:'):q['t']=intro+q['t']
q=d['8.444'];q['s']=sol([st(r'Relativ resistansökning: \(\Delta R/R_0=\alpha\Delta T\)',r'<p>Guldtrådens ökning är 7,0 %, alltså 0,070.</p>'+m(r'\Delta T=\frac{0{,}070}{0{,}0034}\approx20{,}588\ \mathrm K')),st('Använd samma temperaturökning för volfram',m(r'\begin{aligned}\frac{\Delta R}{R_0}&=0{,}0045\cdot\frac{0{,}070}{0{,}0034}\\&\approx0{,}092647\end{aligned}'))],'Volframtrådens resistans ökar med cirka 9,3 %.')
H['save']('uppgifter.js',b,old)
