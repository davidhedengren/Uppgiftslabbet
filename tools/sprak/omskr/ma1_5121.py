"""Ma1 5.121 (2026-11-20): med 4 röda och 3 blå beskrev 4/7 · 3/6 både ”röd, röd” och ”röd, blå”.
Ny påse: 5 röda och 3 blå, uttrycket 5/8 · 3/7 passar bara ”först röd, sedan blå”.
Körs: PYTHONUTF8=1 python tools/sprak/omskr/ma1_5121.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('ma1')
u = b.obj('5.121')
t_ny = ('<p>En påse innehåller 5 röda och 3 blå kulor. Två kulor dras utan återläggning. '
        'Vilken händelse beskrivs av \\(\\frac58\\cdot\\frac37\\)?</p>')
s_ny = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
        '<li><p class="facit-rubrik">Första faktorn: \\(\\frac58\\) är andelen röda kulor</p>'
        '<p>Från början finns 5 röda av 8 kulor, så \\(\\frac58\\) betyder att den första kulan är röd.</p></li>'
        '<li><p class="facit-rubrik">Andra faktorn: \\(\\frac37\\) är andelen blå kulor som är kvar</p>'
        '<p>Efter en röd kula finns 7 kulor kvar, och alla 3 blå är kvar. Därför betyder \\(\\frac37\\) blå i andra draget.</p></li>'
        '<li><p class="facit-rubrik">Jämför med de andra alternativen</p>'
        '<p>Röd och sedan röd hade gett \\(\\frac58\\cdot\\frac47\\). Blå först hade börjat med \\(\\frac38\\).</p></li></ol>'
        '<p class="facit-svar"><strong>Svar: Först röd, sedan blå.</strong></p></div>')
l_ny = '<p>Vad betyder \\(\\frac58\\) i första draget? Hur många kulor av varje färg finns kvar efter det?</p>'
b.ersatt('5.121', [(u['t'], t_ny), (u['s'], s_ny), (u['ledtrad'], l_ny)])
print(b.spara(), 'objekt skrivna')
