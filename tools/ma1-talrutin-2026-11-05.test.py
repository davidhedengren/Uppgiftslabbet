"""Kontrollera bankens faktiska frågor, facit/mellanled och kortmetadata."""
import json
import re
from collections import Counter
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'uppgifterma1.js').read_text()
bank=json.loads(s[s.index('['):].strip().removesuffix(';'))
ids={f'0.{i}' for i in range(1266,1302)}
qs=[q for q in bank if q['id'] in ids]
assert len(qs)==36
assert len({q['id'] for q in bank})==len(bank)

def value(tex):
    tex=tex.replace('{,}','.').replace(r'\,','').replace(r'\%','/100')
    while r'\frac' in tex:
        changed=re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}',r'((\1)/(\2))',tex)
        assert changed!=tex,tex
        tex=changed
    tex=tex.replace(r'\cdot','*').replace(r'\div','/')
    return sp.sympify(tex,rational=True)

levels=Counter();equations=0
for q in qs:
    assert q['kurs']==['1a','1b','1c']
    assert q['kap']==0 and q['niva']=='E' and q['poang']=='3/0/0'
    assert q['spelDelning']=='deluppgifter' and q['svarsstruktur']=='ordnad'
    assert len(q['spelDelar'])==3
    assert all(q['t'].count(label+')')==1 for label in 'abc')
    assert all(q['s'].count('>'+label+')</span>')==1 for label in 'abc')
    for i,d in enumerate(q['spelDelar']):
        levels[d['traningsniva']]+=1
        assert d['rättSvar']==q['rättSvar'][i]
        assert d['svarFormat']==q['svarFormat'][i]
        assert d['miniräknare']==q['miniräknare']==(q['omr']=='andelar')
        assert d['geogebra']==q['geogebra']==False
        assert d['självrättning'] and d['tolerans']==0
        assert d['etikett']=='abc'[i] and d['poang']=='1/0/0'
        question=re.findall(r'\\\((.*?)\\\)',d['t'])
        if q['omr']=='brakrakning':
            expected=value(question[0])
            assert 'Svara exakt' in d['t']
        elif 'Hur mycket' in d['t']:
            expected=value(question[0])*value(question[1])
        elif 'Hur många procent' in d['t']:
            expected=100*value(question[0])/value(question[1])
            assert d['svarEnhet']=='%'
        else:
            expected=value(question[1])/value(question[0])
        assert expected==sp.Rational(str(d['rättSvar'])),(q['id'],d['etikett'],expected)
        assert len(d['ledtrad'])>50 and not any(w in d['ledtrad'] for w in ['None','null'])
        assert 'facit-steglista' in d['s']
        for li in re.findall(r'<li>(.*?)</li>',d['s']):
            assert 'facit-rubrik' in li and 'facit-matte' in li
        assert re.search(r'facit-rubrik">[^<]*\\\(',d['s'])
        for equation in re.findall(r'\\\[(.*?)\\\]',d['s']):
            sides=[value(side) for side in equation.split('=')]
            assert all(x==sides[0] for x in sides),(q['id'],d['etikett'],equation)
            equations+=1
        answer=re.search(r'facit-svar.*?\\\((.*?)\\\)',d['s'])[1]
        assert value(answer)==expected/(100 if d.get('svarEnhet')=='%' else 1)
assert levels=={1:36,2:72},levels
print(f'36 huvuduppgifter, 108 kort, {equations} exakta facitberäkningar verifierade. Nivåer: {dict(levels)}')
