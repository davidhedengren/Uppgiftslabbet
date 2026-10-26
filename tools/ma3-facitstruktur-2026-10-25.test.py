"""Kontrollerar facit/delkort och räknar nya mellanresultat oberoende."""
import json, re, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def data(name):return json.loads((ROOT/'tools'/name).read_text())
raw=(ROOT/'uppgiftermato1.js').read_text();bank={q['id']:q for q in json.loads(raw[raw.index('['):raw.rindex(']')+1])}
headings=data('ma3-facitstruktur-2026-10-25.rubriker.json')
assert len(headings)==158
for id,titles in headings.items():
 q=bank[id]
 for card in [q]+q.get('spelDelar',[]):
  steps=re.findall(r'<li>([\s\S]*?)</li>',card['s'])
  assert steps and 'facit-svar' in card['s'],id
  for step in steps:
   title=re.match(r'<p class="facit-rubrik">([^<]+)</p>',step)
   assert title and len(title[1])>15,(id,step)
   assert re.sub('<[^>]*>','',step[title.end():]).strip(),id
  assert card.get('ledtrad',q['ledtrad']).strip(),id
 assert len(re.findall('class="facit-rubrik"',q['s']))==len(titles),id
 assert q.get('geogebra') is not True or q['miniräknare'] is True,id
 for option in q.get('alternativ',[]):assert len(option.get('kommentar',''))>30,id
 # Alla delkortens lösningar ska finnas ordagrant i huvudfacitet.
 for part in q.get('spelDelar',[]):assert part['s'] in q['s'],id
# Det felaktiga strikt-positiva påståendet får inte återkomma i ledtråden.
assert 'vågrät tangent' in bank['3.198']['ledtrad']
S=lambda x:math.sin(math.radians(x));C=lambda x:math.cos(math.radians(x))
b=math.degrees(math.asin(10*S(30)/7))
checks={
('4.532','2'):80*(S(65)+S(40))/S(75)-80,
('4.533','1'):60*S(75)/S(50),('4.533','2'):60*60*S(75)/S(50)*S(55)/2,
('4.534','2'):20/(1+S(65)/S(35)),('4.535','3'):36*S(75)/(S(45)+S(60)+S(75)),
('4.537','2'):10*S(40),('4.538','3'):10*14*S(150-b)*S(30)/2,
('4.539','2'):40/(2+S(40)/S(70)),('4.539','3'):(40/(2+S(40)/S(70)))**2*S(40)/2,
('4.540','2'):30*S(115)/S(25),('4.540','3'):30*S(115)/S(25)*S(40),
('4.541','1'):10*S(80)/S(40),('4.541','3'):10*S(80)/S(40)*S(60)/S(100),
('4.543','3'):10*S(math.degrees(math.asin(14*S(35)/10))-35)/S(35),
('4.544','3'):130-math.degrees(math.asin(S(50)/2)),('4.545','2'):50*S(30)/S(100),
('4.547','3'):2*S(80)/(1-S(80)),('4.548','3'):math.sqrt(120*S(35)/S(70)/S(75)),
('4.550','2'):math.sqrt(28),('4.551','3'):math.sqrt(10*5*3*2), # Herons formel, s=10
('4.552','3'):math.sqrt((2*10**2+2*12**2-14**2)/4),
('4.553','3'):math.sqrt(3**2+4**2-2*3*4*C(120)),
('4.554','3'):math.sqrt(4**2+6**2-2*4*6*C(75)),
('4.555','3'):2*math.sqrt(13.5*5.5*4.5*3.5)/10, # Herons formel
('4.556','2'):math.sqrt(11**2-8**2)-6,
('4.557','3'):math.degrees(math.acos((7**2+5**2-52)/(2*7*5))),
('4.559','4'):math.sqrt(10*12*(1-14**2/(10+12)**2)), # bisektrislängden
('4.562','3'):math.sqrt(7**2+5**2+2*7*5*C(60)),
('4.563','3'):5*2*6*S(36),('4.564','3'):math.sqrt(8**2+12**2-2*8*12*C(50)),
('4.565','2'):(math.sqrt(273)/math.sqrt(97)-1)*100,
}
extras=data('ma3-facitstruktur-2026-10-25.mellanled.json')
for (id,step),expected in checks.items():
 numbers=re.findall(r'\\approx([0-9]+)\{,\}([0-9]+)',extras[id][step]);assert numbers,(id,step)
 a,b=numbers[-1];value=float(a+'.'+b)
 assert abs(value-expected)<=0.5*10**-len(b)+1e-10,(id,step,value,expected)
print('158 huvudfacit, delkort, flervalskommentarer och 31 oberoende mellanberäkningar godkända.')
