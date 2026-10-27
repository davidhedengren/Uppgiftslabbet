import json
from pathlib import Path

solutions = {
    '3.473': [
        r'\(x^2-1=0\) ger nollställena \(x=-1\) och \(x=1\). Funktionen är negativ mellan nollställena och positiv utanför dem.',
        r'Använd symmetri och beräkna de två areorna för \(x\ge0\): \[\int_0^1(1-x^2)\,dx=\frac23\] \[\int_1^2(x^2-1)\,dx=\frac43.\]',
        r'Dubblera summan för att ta med området till vänster: \[A=2\left(\frac23+\frac43\right)=4.\]'],
    '3.179': [
        r'Skärningarna fås ur \(ax=x^2\), alltså \(x=0\) eller \(x=a\). När \(0&lt;x&lt;a\) ligger \(y=ax\) över \(y=x^2\).',
        r'Arean är \[A=\int_0^a(ax-x^2)\,dx.\] En primitiv funktion ger \[A=\left[\frac{ax^2}{2}-\frac{x^3}{3}\right]_0^a=\frac{a^3}{6}.\]',
        r'Sätt arean till \(9/2\): \(a^3/6=9/2\), så \(a^3=27\). Därmed är \(\boxed{a=3}\).'],
    '3.206': [
        r'Skärningspunkterna ges av \(x^2-2x=2x\), vilket ger \(x(x-4)=0\). Gränserna är alltså \(0\) och \(4\).',
        r'På intervallet ligger \(y=2x\) över \(y=x^2-2x\). Arean blir \[A=\int_0^4(4x-x^2)\,dx.\]',
        r'Beräkna integralen: \[A=\left[2x^2-\frac{x^3}{3}\right]_0^4\] \[=32-\frac{64}{3}=\boxed{\frac{32}{3}}.\]'],
    '3.475': [
        r'\(\sin x\) är positiv på \((0,\pi)\) och negativ på \((\pi,2\pi)\). Den geometriska arean består av båda delarna.',
        r'Integralerna blir \[\int_0^\pi\sin x\,dx=2\] och \[\int_\pi^{2\pi}\sin x\,dx=-2.\]',
        r'Den andra delens geometriska area är positiv trots att integralen är negativ. Därför är \(A=2+2=\boxed4\).'],
}
p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
by_id = {q['id']:q for q in bank}
for task_id, steps in solutions.items():
    old = by_id[task_id]['s']
    new = '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p>'+s+'</p></li>' for s in steps)+'</ol></div>'
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },', start)
    segment = raw[start:end]
    before, after = json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False)
    assert segment.count(before)==1
    raw = raw[:start]+segment.replace(before,after,1)+raw[end:]
p.write_text(raw,encoding='utf-8')
