"""Ma1 3.191 (2026-11-20): facit hade exponenten utanför bråket (\\frac{38\\,934,40}{0{,}92}^3) och decimalkomma
utan klamrar. Ny steglista enligt FACITMALL. Körs: PYTHONUTF8=1 python tools/sprak/facit/ma1_3191.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

S = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
     r'<li><p class="facit-rubrik">En minskning med 8 % ger förändringsfaktorn 0,92</p><div class="facit-matte">\[1-0{,}08=0{,}92\]</div></li>'
     r'<li><p class="facit-rubrik">Tre år ger faktorn \(0{,}92^3\)</p><div class="facit-matte">\[V\cdot0{,}92^3=38\,934{,}40\]</div></li>'
     r'<li><p class="facit-rubrik">Dela båda leden med \(0{,}92^3\)</p><div class="facit-matte">\[V=\frac{38\,934{,}40}{0{,}92^3}=\frac{38\,934{,}40}{0{,}778688}=50\,000\]</div></li>'
     '</ol><p class="facit-svar"><strong>Svar:</strong> 50 000</p></div>')
b = Bank('ma1')
b.ersatt('3.191', [(b.obj('3.191')['s'], S)])
print(b.spara(), 'objekt skrivna')
