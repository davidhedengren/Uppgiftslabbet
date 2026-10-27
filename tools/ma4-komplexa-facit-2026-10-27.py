import json
from pathlib import Path

# Varje rad är ett eget, matematiskt kontrollerat delkort: förklaring, svar.
data = {
    '4.12': [
        (r'\(r=\sqrt{2^2+2^2}=2\sqrt2\). Punkten ligger i första kvadranten och \(v=\pi/4\).', r'2\sqrt2(\cos\frac\pi4+i\sin\frac\pi4)'),
        (r'Avståndet till origo är \(r=3\). Punkten ligger på negativa imaginära axeln, så \(v=3\pi/2\).', r'3(\cos\frac{3\pi}2+i\sin\frac{3\pi}2)'),
        (r'\(r=\sqrt{(-1)^2+(-\sqrt3)^2}=2\). Punkten ligger i tredje kvadranten med referensvinkeln \(\pi/3\), alltså \(v=4\pi/3\).', r'2(\cos\frac{4\pi}3+i\sin\frac{4\pi}3)'),
    ],
    '4.197': [
        (r'\(r=\sqrt{1^2+1^2}=\sqrt2\) och vinkeln i första kvadranten är \(v=\pi/4\).', r'\sqrt2(\cos\frac\pi4+i\sin\frac\pi4)'),
        (r'\(r=\sqrt{(-1)^2+1^2}=\sqrt2\). Punkten ligger i andra kvadranten, så \(v=3\pi/4\).', r'\sqrt2(\cos\frac{3\pi}4+i\sin\frac{3\pi}4)'),
        (r'\(r=\sqrt{(-\sqrt3)^2+(-1)^2}=2\). Punkten ligger i tredje kvadranten med referensvinkeln \(\pi/6\), så \(v=7\pi/6\).', r'2(\cos\frac{7\pi}6+i\sin\frac{7\pi}6)'),
        (r'\(r=\sqrt{(\sqrt3)^2+(-1)^2}=2\). Punkten ligger i fjärde kvadranten med referensvinkeln \(\pi/6\), så \(v=11\pi/6\).', r'2(\cos\frac{11\pi}6+i\sin\frac{11\pi}6)'),
    ],
    '4.198': [
        (r'Punkten ligger på positiva imaginära axeln: \(r=2\) och \(v=\pi/2\).', r'2(\cos\frac\pi2+i\sin\frac\pi2)'),
        (r'Punkten ligger på negativa reella axeln: \(r=3\) och \(v=\pi\).', r'3(\cos\pi+i\sin\pi)'),
        (r'Punkten ligger på negativa imaginära axeln: \(r=4\) och \(v=3\pi/2\).', r'4(\cos\frac{3\pi}2+i\sin\frac{3\pi}2)'),
        (r'Punkten ligger på positiva reella axeln: \(r=5\) och \(v=0\).', r'5(\cos0+i\sin0)'),
    ],
    '4.199': [
        (r'Sätt in \(\cos(\pi/3)=1/2\) och \(\sin(\pi/3)=\sqrt3/2\): \(4(1/2+i\sqrt3/2)=2+2\sqrt3i\).', r'2+2\sqrt3i'),
        (r'\(\cos\pi=-1\) och \(\sin\pi=0\), så \(6(-1+i\cdot0)=-6\).', r'-6'),
        (r'\(\cos(7\pi/4)=\sqrt2/2\) och \(\sin(7\pi/4)=-\sqrt2/2\). Multiplicera båda termerna med \(2\sqrt2\).', r'2-2i'),
        (r'\(\cos(3\pi/2)=0\) och \(\sin(3\pi/2)=-1\), så \(3(0-i)=-3i\).', r'-3i'),
    ],
    '4.203': [
        (r'Eulers formel ger \(e^{iv}=\cos v+i\sin v\). Här är \(\cos(\pi/2)=0\) och \(\sin(\pi/2)=1\).', r'2i'),
        (r'Eulers formel ger \(4e^{i\pi}=4(\cos\pi+i\sin\pi)=4(-1+i\cdot0)\).', r'-4'),
        (r'Eulers formel ger \(3e^{2i\pi/3}=3(\cos(2\pi/3)+i\sin(2\pi/3))=3(-1/2+i\sqrt3/2)\).', r'-\frac32+\frac{3\sqrt3}{2}i'),
        (r'Eulers formel ger \(2\sqrt2e^{-i\pi/4}=2\sqrt2(\sqrt2/2-i\sqrt2/2)\).', r'2-2i'),
    ],
    '4.204': [
        (r'\(r=\sqrt{1^2+1^2}=\sqrt2\) och \(v=\pi/4\). Använd \(z=re^{iv}\).', r'\sqrt2e^{i\pi/4}'),
        (r'\(r=\sqrt{(-2)^2+2^2}=2\sqrt2\). Punkten ligger i andra kvadranten och \(v=3\pi/4\).', r'2\sqrt2e^{i3\pi/4}'),
        (r'Punkten ligger på negativa imaginära axeln, så \(r=3\) och exempelvis \(v=-\pi/2\).', r'3e^{-i\pi/2}'),
        (r'\(r=\sqrt{(\sqrt3)^2+(-1)^2}=2\). Punkten ligger i fjärde kvadranten och kan ges argumentet \(v=-\pi/6\).', r'2e^{-i\pi/6}'),
    ],
    '4.288': [
        (r'\(r=\sqrt{1^2+1^2}=\sqrt2\) och \(v=\pi/4\), som ligger i det angivna intervallet.', r'\sqrt2(\cos\frac\pi4+i\sin\frac\pi4)'),
        (r'\(r=\sqrt{(-\sqrt3)^2+1^2}=2\). Punkten ligger i andra kvadranten med referensvinkeln \(\pi/6\), så \(v=5\pi/6\).', r'2(\cos\frac{5\pi}6+i\sin\frac{5\pi}6)'),
        (r'\(r=\sqrt{(-2)^2+(-2)^2}=2\sqrt2\). Punkten ligger i tredje kvadranten, så \(v=5\pi/4\).', r'2\sqrt2(\cos\frac{5\pi}4+i\sin\frac{5\pi}4)'),
        (r'Punkten ligger på positiva imaginära axeln, så \(r=3\) och \(v=\pi/2\).', r'3(\cos\frac\pi2+i\sin\frac\pi2)'),
    ],
}

def solution(explanation, answer):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
            f'<li><p>{explanation}</p></li><li><p><strong>Svar:</strong> \\({answer}\\).</p></li>'
            '</ol></div>')

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']') + 1])
by_id = {q['id']: q for q in bank}
for task_id, parts in data.items():
    task = by_id[task_id]
    assert len(task['spelDelar']) == len(parts)
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },', start)
    segment = raw[start:end]
    solutions = [solution(*part) for part in parts]
    combined = '<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{s}</div></div>'
        for i, s in enumerate(solutions)) + '</div>'
    for old, new in [(task['s'], combined)] + [(d['s'], s) for d, s in zip(task['spelDelar'], solutions)]:
        old_json, new_json = json.dumps(old, ensure_ascii=False), json.dumps(new, ensure_ascii=False)
        assert segment.count(old_json) == 1, (task_id, old[:80], segment.count(old_json))
        segment = segment.replace(old_json, new_json, 1)
    raw = raw[:start] + segment + raw[end:]
p.write_text(raw, encoding='utf-8')
