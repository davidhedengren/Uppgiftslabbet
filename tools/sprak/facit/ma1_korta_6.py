# Ma1 kapitel 6: representationer, digitala verktyg, programmering, samhällsliv (2026-11-23).
import os
exec(open(os.path.join('tools', 'sprak', 'facit', 'ma1_korta_gemensamt.py'), encoding='utf-8').read())
GEKV = 'Lös ekvationen grafiskt: läs av x där graferna skär varandra'
LOOP = 'Följ programmet rad för rad och håll reda på variablernas värden'
CELL = 'En cellformel räknar med innehållet i de celler den pekar på'
KOPIA = 'När en formel kopieras nedåt ökar radnumren lika mycket'


F = {
    '6.10': ett(GEKV, r"x=4", r"\(x=4\)", 'Linjen y = 14 skär grafen till y = 3x + 2 där x = 4. Kontroll: 3 · 4 + 2 = 14.'),
    '6.78': ett(GEKV, r"(2,\ 5)", r"\((2,5)\)", 'Kontroll: 2 · 2 + 1 = 5 och 7 − 2 = 5.'),
    '6.32': ([('Sätt modellerna lika och lös digitalt', r"80\cdot1{,}05^t=140+2t"), (GEKV, r"t\approx15{,}6", 'Rita båda graferna, till exempel i GeoGebra, och läs av skärningen.')],
             r"\(t\approx15{,}6\)"),
    # procent och samhällsliv
    '6.20': ett(PROCAV, r"0{,}15\cdot1\,200=180", "180 kr"),
    '6.132': ett(PROCAV, r"0{,}12\cdot18\,500=2\,220", "2 220 kr"),
    '6.21': ett(PROCAV, r"0{,}15\cdot240=36", "36 miljoner kronor"),
    '6.113': ett(PROCAV, r"0{,}012\cdot84\,000=1\,008", "cirka 1 008 personer"),
    '6.139': ([('Andelen upptagna platser', r"100\ \%-35\ \%=65\ \%"), (PROCAV, r"0{,}65\cdot180=117")], "117 personer"),
    '6.131': ett(r"Nytt värde: förändringsfaktor gånger gammalt värde", r"1\,600\cdot0{,}75=1\,200", "1 200 kr"),
    '6.129': ([('Ökningen i kronor', r"2\,640-2\,400=240"), (r"Procentuell ökning: \(\frac{\text{ökningen}}{\text{ursprungligt värde}}\)", r"\frac{240}{2\,400}=0{,}10=10\ \%")], "10 %"),
    '6.115': ett(ANDEL, r"\frac{765}{900}=0{,}85=85\ \%", "85 %"),
    '6.105': ett('Antal paneler gånger produktion per panel', r"12\cdot340=4\,080", "4 080 kWh"),
    '6.107': ett('Skillnaden mellan före och efter', r"250-190=60", "60 kg mindre per vecka"),
    '6.117': ett(PER1, r"\frac{720}{40}=18", "18 kr per resa"),
    '6.114': ([('Viktat medelvärde: total restid delat med antal personer', r"\frac{120\cdot18+80\cdot32}{200}=\frac{2\,160+2\,560}{200}"), ('Beräkna', r"\frac{4\,720}{200}=23{,}6")], "23,6 minuter"),
    '6.123': delar(
        ('a', [('Dra bort alla kostnader från budgeten', r"24\,000-9\,000-3\,600-1\,800=9\,600")], "9 600 kr"),
        ('b', [(ANDEL, r"\frac{9\,000}{24\,000}=0{,}375=37{,}5\ \%")], "37,5 %"),
        ('c', [(ANDEL, r"\frac{9\,600}{24\,000}=0{,}40=40\ \%")], "40 %"),
    ),
    '6.409': mc('Babylonierna räknade med ett positionssystem med bas 60', 'Det lever kvar i 60 minuter per timme och 60 sekunder per minut.', 'Bas 60'),
    '6.416': ([('Antalet ökar med 3 för varje figur', r"\text{figur }n:\ 3n+1"), (r"Sätt in \(n=13\)", r"3\cdot13+1=40")], "40 stickor"),
    # programmering
    '6.34': ett('Varje varv multiplicerar med 0,9', r"100\cdot0{,}9\cdot0{,}9\cdot0{,}9\cdot0{,}9\cdot0{,}9=100\cdot0{,}9^5", r"\(100\cdot0{,}9^5\)"),
    '6.401': ett(LOOP, r"100\cdot1{,}02^3=106{,}1208", "106,1208"),
    '6.402': ett(LOOP, r"3+5\cdot4=23", "23"),
    '6.403': ett(LOOP, r"1+2+3+4+5=15", "15"),
    '6.406': ett('Sätt in x = 4 i regeln', r"2\cdot4+1=9", "9"),
    '6.421': ett(LOOP, r"1+2+3+4+5=15", "15", 'range(1, 6) ger talen 1–5; 6 ingår inte.'),
    '6.430': ett(LOOP, r"b=3\cdot4=12,\qquad12+5=17", "17"),
    '6.431': ett(LOOP, r"10+6=16,\qquad3\cdot16=48", "48", 'Följ pilarna i flödesschemat.'),
    '6.432': ett(LOOP, r"2+4\cdot3=14", "14", 'range(4) ger fyra varv.'),
    '6.433': ett(LOOP, r"5\to2\cdot5+1=11\to2\cdot11+1=23\to2\cdot23+1=47", "47"),
    '6.434': mc(LOOP, '−3 är mindre än 0, så villkoret är sant och första grenen körs.', "is"),
    '6.435': ([(LOOP, r"100\cdot1{,}2^3=172{,}8<200"), ('Ett varv till', r"100\cdot1{,}2^4\approx207{,}4>200")], "4"),
    '6.436': ett('Sätt in x = 5 i funktionen', r"5^2-3=25-3=22", "22"),
    '6.437': mc('Rektangelns area är längd gånger bredd', None, "print(6 * 4)"),
    '6.438': ett(LOOP, r"1+2+\dots+9=45", "45", 'range(1, 10) slutar på 9. För att få med 10 ska det stå range(1, 11).'),
    '6.439': ett('sum delat med len är medelvärdet', r"\frac{12+9+15+6}{4}=\frac{42}{4}=10{,}5", "10,5"),
    '6.440': ett(LOOP, r"3,\ 6,\ 9,\ 12,\ 15,\ 18", "6", 'Programmet räknar talen 1–20 som är delbara med 3.'),
    # kalkylprogram
    '6.49': mc(CELL, 'Totalsumman är pris gånger antal.', "=B2*C2"),
    '6.450': mc(CELL, 'SUMMA adderar cellerna B2 till B5.', "=SUMMA(B2:B5)"),
    '6.452': mc(CELL, 'Nytt pris är ordinarie pris minus rabatten.', "=B2-C2"),
    '6.451': ett(CELL, r"12\cdot35=420", "420"),
    '6.453': ett(KOPIA, r"\text{C5}=\text{B5}-\text{B4}=298-231=67", "67"),
    '6.454': ett('MEDEL ger medelvärdet', r"\frac{18+23+15+27+22}{5}=\frac{105}{5}=21", "21"),
    '6.455': ett('MAX ger största och MIN minsta värdet', r"7-(-4)=11", "11"),
    '6.456': mc(KOPIA, None, "=A3*B3"),
    '6.458': ett(KOPIA, r"1\,000\cdot1{,}05^4\approx1\,215{,}51", "1 215,51", 'Från B2 till B6 multipliceras med 1,05 fyra gånger.'),
    '6.459': mc('OM(villkor; om sant; om falskt)', '47 ≥ 50 är falskt.', "Ej godkänd"),
}
