"""Fellogg 11 november: kursplacering och beräknade tabellalternativ."""
from pathlib import Path
import runpy,json
H=runpy.run_path(str(Path(__file__).with_name('felrapporter-2026-11-09.py')));m,st,sol,joined=[H[k]for k in ['m','st','sol','joined']]
b=H['read']('uppgifter.js');old={q['id']:json.loads(json.dumps(q))for q in b};d={q['id']:q for q in b}
q=d['2.59'];intro='<p>Ett tåg kör med farten 14,0 m/s. Ange svaren med en decimal.</p>'
qa='<p>Ange farten i km/h.</p>';qb='<p>Ange farten i m/min.</p>'
sa=sol([st(r'Meter per sekund till kilometer per timme: \(1\ \mathrm{m/s}=3{,}6\ \mathrm{km/h}\)',r'<p>En timme är 3600 sekunder och en kilometer är 1000 meter. Omvandlingsfaktorn är därför 3600/1000.</p>'),st('Multiplicera tågets fart med 3,6',m(r'\begin{aligned}v&=14{,}0\cdot3{,}6\\&=50{,}4\ \mathrm{km/h}\end{aligned}'))],'Tågets fart är 50,4 km/h.')
sb=sol([st(r'Meter per sekund till meter per minut: \(1\ \mathrm{min}=60\) s','<p>Tåget hinner 60 gånger så långt under en minut som under en sekund.</p>'),st('Multiplicera med antalet sekunder per minut',m(r'\begin{aligned}v&=14{,}0\cdot60\\&=840{,}0\ \mathrm{m/min}\end{aligned}'))],'Tågets fart är 840,0 m/min.')
q['t']=intro+'<p>a) Ange farten i km/h.</p><p>b) Ange farten i m/min.</p>';q['spelIntro']=intro;q['s']=joined([sa,sb]);q['rättSvar']=[50.4,840];q['svarEnhet']=['km/h','m/min'];q['ledtrad']='<p>Hur många sekunder går det på en timme respektive en minut? Hur många meter går det på en kilometer?</p>'
for p,t,s,hint in zip(q['spelDelar'],[qa,qb],[sa,sb],['Använd att 1 m/s motsvarar 3,6 km/h.','En minut är 60 sekunder.']):p['t']=intro+t;p['s']=s;p['ledtrad']='<p>'+hint+'</p>'
# Samma uppgifter och svar behålls, men först när energibegreppen har introducerats.
for id,area in [('2.19','blandat_energi'),('2.29','effekt'),('2.33','arbete'),('2.36','blandat_energi'),('2.209','effekt'),('2.217','rorelseenergi'),('2.220','blandat_energi'),('2.362','effekt')]:d[id]['kap']=5;d[id]['omr']=area
q=d['8.294'];q['spel']=False;intro=r'<p><strong>Fördjupning: potential från punktladdningar.</strong></p><p>För en punktladdning gäller \(V=kq/r\) med nollnivån i oändligheten. Potentialerna från flera laddningar adderas med sina tecken.</p>'
if not q['t'].startswith('<p><strong>Fördjupning:'):q['t']=intro+q['t']
q['s']=sol([st(r'Mittpunkten ger \(r=0{,}40/2=0{,}20\) m','<p>Båda laddningarna ligger på samma avstånd från punkten. Det är potentialer som ska adderas, inte vektorer för elektriska fältet.</p>'),st(r'Superposition av potential: \(V=k(q_1+q_2)/r\)',m(r'\begin{aligned}q_1+q_2&=(3{,}0-1{,}0)\cdot10^{-6}\ \mathrm C\\V&=\frac{8{,}99\cdot10^9\cdot2{,}0\cdot10^{-6}}{0{,}20}\\&=89900\ \mathrm V\end{aligned}'))],r'Potentialen är cirka \(9{,}0\cdot10^4\) V relativt oändligheten.')
# Sluttemperatur från energibalans; densiteten är en självständig tabellparameter.
def temp(rho):
 mass=5*rho
 return (.05*(2260+4.18*100)+mass*4.18*11)/((mass+.05)*4.18)
q=d['7.221'];q['svarTabell']={**q.get('svarTabell',{}),'0':[temp(.997),temp(.998),temp(.9982)]}
a=sol([st(r'Massa ur vattenvolym: \(m_v=\rho V\)',r'<p>Med överslagsvärdet 1,0 kg/liter är vattenmassan 5,0 kg. Med tabellvärdet 0,997 kg/liter är den i stället 4,985 kg.</p>'),st(r'Energibalans: \(Q_{av}=Q_{up}\)',r'<p>Ångan kondenserar och det bildade vattnet svalnar från 100 °C till T. Det kalla vattnet värms från 11 °C till T. Energierna nedan anges i kJ. Kondensationen avger 0,050 · 2260 = 113 kJ och avsvalningen ger 0,050 · 4,18 · (100 − T) kJ.</p>'+m(r'\begin{gathered}Q_{kond}=113\\Q_{kyl}=0{,}209(100-T)\\Q_{av}=133{,}9-0{,}209T\\Q_{up}=4{,}18m_v(T-11)\end{gathered}')),st('Lös temperaturbalansen med vald vattenmassa','<p>Med 5,0 kg vatten blir balansen:</p>'+m(r'\begin{gathered}Q_{up}=20{,}9T-229{,}9\\(20{,}9+0{,}209)T\\=133{,}9+229{,}9\\T=\frac{363{,}8}{21{,}109}\approx17{,}234\ {}^\circ\mathrm C\end{gathered}')+'<p>Med 4,985 kg vatten blir samma ekvation:</p>'+m(r'\begin{gathered}Q_{up}=20{,}8373(T-11)\\21{,}0463T=363{,}1103\\T\approx17{,}253\ {}^\circ\mathrm C\end{gathered}'))],'Sluttemperaturen blir cirka 17,2 °C med 1,0 kg/liter eller 17,3 °C med 0,997 kg/liter. Skillnaden beror på tabellvärdet.')
bb=sol([st(r'Isens smältenergi: \(Q=m_i l_s\)',m(r'Q=0{,}50\cdot334=167\ \mathrm{kJ}')),st(r'Ångan avger både kondensations- och avsvalningsenergi: \(Q=m_a(l_a+c\Delta T)\)',m(r'\begin{aligned}167&=m_a(2260+418)\\&=2678m_a\end{aligned}')),st('Lös ut ångmassan',m(r'm_a=\frac{167}{2678}\approx0{,}06236\ \mathrm{kg}'))],'Det behövs cirka 0,062 kg vattenånga.')
c=sol([st(r'Isen smälter och värms: \(Q_i=m_i(l_s+c\Delta T)\)',m(r'\begin{aligned}Q_i&=m_i(334+4{,}18\cdot50)\\&=543m_i\ \mathrm{kJ}\end{aligned}')),st(r'Ångan kondenserar och svalnar: \(Q_a=m_a(l_a+c\Delta T)\)',m(r'\begin{aligned}Q_a&=m_a(2260+4{,}18\cdot50)\\&=2469m_a\ \mathrm{kJ}\end{aligned}')),st(r'Energibalansen ger masskvoten: \(Q_i=Q_a\)',m(r'm_i/m_a=2469/543\approx4{,}55'))],'Isens massa ska vara cirka 4,55 gånger ångans massa.')
q['s']=joined([a,bb,c])
for p,s in zip(q['spelDelar'],[a,bb,c]):p['s']=s
q=d['6.338'];Rs=[8.314,8.314421,8.31446261815324];q['svarTabell']={'0':[.25*R*300/100000*1000 for R in Rs]}
q['s']=sol([st(r'Ideala gaslagen, lös ut volymen: \(V=nRT/p\)',r'<p>SI-enheterna ger volymen i m³. Använd samma värde på gaskonstanten genom hela beräkningen.</p>'),st('Sätt in n = 0,250 mol, T = 300 K och p = 100000 Pa',m(r'\begin{aligned}V&=\frac{0{,}250\cdot8{,}31\cdot300}{100000}\\&=0{,}0062325\ \mathrm{m^3}\end{aligned}')),st(r'Kubikmeter till liter: \(1\ \mathrm{m^3}=1000\) liter',m(r'\begin{aligned}V&=0{,}0062325\cdot1000\\&=6{,}2325\ \text{liter}\end{aligned}')+r'<p>Med R = 8,31 blir svaret 6,23 liter. Med det mer precisa tabellvärdet R ≈ 8,31446 blir det cirka 6,23585 liter, som avrundas till 6,24 liter.</p>')],'Volymen är cirka 6,23–6,24 liter beroende på gaskonstantens tabellvärde.')
# Volymen i isblandningen ger samma densitetsberoende som rapporten.
q=d['7.220'];q['svarTabell']={'0':[(.25*r*4.18*18-.04*(2.2*18+334))/((.25*r+.04)*4.18) for r in (.997,.998,.9982)]}
note='<p>Här används överslagsvärdet 1,0 kg/liter för vattnets densitet. Med 0,997 kg/liter blir vattenmassan 0,24925 kg och sluttemperaturen cirka 3,15084 °C. Även en korrekt avrundning av detta tabellalternativ godtas.</p>'
if note not in q['s']:q['s']=q['s'].replace('<p class="facit-svar">',note+'<p class="facit-svar">')
# Två följdfynd: noggrannare R hamnar utanför tidigare snäva toleranser.
d['6.337']['svarTabell']={'0':[.5*R*300/.012/1000 for R in Rs]}
d['6.201']['svarTabell']={'0':[16*R*T/35000 for R in Rs for T in (283.15,283)]}
H['save']('uppgifter.js',b,old)
