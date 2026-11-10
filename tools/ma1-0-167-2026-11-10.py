from pathlib import Path
import runpy,json
H=runpy.run_path(str(Path(__file__).with_name('felrapporter-2026-11-09.py')))
b=H['read']('uppgifterma1.js');old={q['id']:json.loads(json.dumps(q)) for q in b};q=next(q for q in b if q['id']=='0.167')
q['t']='<p>Lägg först ihop 4 och 2. Dividera sedan 48 med resultatet.</p><p>Skriv ett uttryck som beskriver beräkningen.</p>'
q['ledtrad']='<p>Vilka tal ska läggas ihop innan divisionen görs? Hur visar du det i ett uttryck?</p>'
q['s']=q['s'].replace('”Med summan” betyder att 4 + 2 är en enda divisor','Summan 4 + 2 ska beräknas före divisionen').replace('Summan måste därför stå inom parentes.','Sätt 4 + 2 inom parentes så att 48 divideras med hela summan, inte bara med 4.')
for a,text in zip(q['alternativ'],['Här delas 48 bara med 4. Tvåan läggs till efter divisionen.','Parentesen visar att 48 ska divideras med hela summan 4 + 2.','Här läggs 48 och 4 ihop, men instruktionen säger att 4 och 2 ska läggas ihop.','Här divideras 4 med 2 först. Det är inte den beskrivna beräkningen.']):a['kommentar']=text
q=next(q for q in b if q['id']=='0.278')
q['s']=q['s'].replace(r'\begin{gathered}(6+4)\cdot3-5 =10\cdot3-5 =30-5\\=25\end{gathered}',r'\begin{aligned}(6+4)\cdot3-5&=10\cdot3-5\\&=30-5\\&=25\end{aligned}')
H['save']('uppgifterma1.js',b,old)
