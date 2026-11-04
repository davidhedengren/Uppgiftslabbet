"""Render explicitly authored, reviewed facit plans; never infer headings/content."""
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BANK=ROOT/'uppgifter.js'
SOURCE=BANK.read_text()
bank=json.loads(SOURCE.removeprefix('window.BANK = ').strip().removesuffix(';'))
byid={q['id']:q for q in bank}
changes={}
def m(x):
    # Line-wrap chains of equalities without changing formulas or step headings.
    if len(x)>65 and r'\begin' not in x:
        depth=0;cuts=[]
        for i,char in enumerate(x):
            if char=='{': depth+=1
            elif char=='}': depth-=1
            elif char=='=' and depth==0: cuts.append(i)
        if len(cuts)>=2:
            segments=[];start=0
            for i in cuts: segments.append(x[start:i]);start=i+1
            segments.append(x[start:])
            x=r'\begin{aligned}'+segments[0]+'&='+segments[1]+''.join(r'\\&='+v for v in segments[2:])+r'\end{aligned}'
    return '<div class="facit-matte">\\['+x+'\\]</div>'
def p(x): return '<p>'+x+'</p>'
def inline(x): return '\\('+x+'\\)'
def solution(steps, answer):
    assert steps and answer
    result='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+h+'</p>'+b+'</li>' for h,b in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
    return re.sub(r'\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]',lambda m:m.group().replace('<',r'\lt ').replace('>',r'\gt '),result)
def setq(id, steps, answer):
    byid[id]['s']=solution(steps,answer);changes[id]='Åtgärdad'
def multi(id, plans, cardplans=None):
    q=byid[id]; sols=[solution(*z) for z in plans]
    q['s']='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+chr(97+i)+')</span><div class="facit-arbete">'+s.removeprefix('<div class="facit-v2 facit-stegvis">')[:-6]+'</div></div>' for i,s in enumerate(sols))+'</div>'
    if q.get('spelDelar'):
        cs=sols if cardplans is None else [solution(*z) for z in cardplans]
        assert len(cs)==len(q['spelDelar']),id
        for d,s in zip(q['spelDelar'],cs): d['s']=s
    changes[id]='Åtgärdad'
def conv(rule, calc, answer, why=''):
    return ([(rule, (p(why) if why else '')+m(calc))],inline(answer)+'.')
def save():
    # Patch only changed JSON strings, preserving original number spellings and spacing.
    pattern=re.compile(r'"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|true|false|null')
    old=list(pattern.finditer(SOURCE))
    new=list(pattern.finditer(json.dumps(bank,ensure_ascii=False,indent=2)))
    assert len(old)==len(new), 'Structural changes need a separate explicit patch'
    result=SOURCE
    for a,b in reversed(list(zip(old,new))):
        if json.loads(a.group())!=json.loads(b.group()):
            result=result[:a.start()]+b.group()+result[a.end():]
    BANK.write_text(result)
