# Ma1 räkneordning (omr tal_rakneordning), omskrivet för hand 2026-11-17.
# "Välj ett alternativ." är borttaget och "en elev" har fått namn. Uppgifterna ställer frågan direkt.


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.169': {'t': p('Felix har börjat räkna ut \\(60\\div5-2(3+1)\\) och fått parentesen till 4. Vilket värde har '
                     'uttrycket?')},
    '0.256': {'t': p('Tove skriver (14 − 6) · 3 + 2 = 8 · 5 = 40. Var gör hon det första felet?')},
    '0.264': {'t': p('Vilket uttryck har värdet 0?')},
    '0.267': {'t': p('Vilket uttryck har störst värde?')},
    '0.269': {'t': p('Nadia räknar \\(12-4\\cdot2=(12-4)\\cdot2=16\\). Vilket fel gör hon?')},
    '0.275': {'t': p('Kevin säger att a + b · c alltid är lika med (a + b) · c. Visa med ett exempel att det inte stämmer. '
                     'Vilka villkor måste a och c uppfylla för att uttrycken ska bli lika, vilket värde b än har?')},
    '0.280': {'t': p('Vilket av uttrycken har störst värde?')},
    '0.288': {'t': p('Någon har skrivit 24 ÷ 3 · 2. Det kan betyda ”dividera 24 med 3 och multiplicera med 2” eller ”dividera '
                     '24 med produkten av 3 och 2”. Skriv båda tolkningarna med bråkstreck och beräkna dem. Vilken tolkning '
                     'gäller enligt prioriteringsreglerna?')},
    '0.289': {'t': p('Saga räknar 8 − 3 + 2 som 8 − (3 + 2). Förklara varför värdet ändras. Skriv sedan 8 − 3 + 2 som en '
                     'summa av tre tal, och beräkna uttrycket i en annan ordning.')},
    '0.851': {'t': p('Moa räknar så här:') + p('\\[36\\div4\\cdot3=36\\div12=3\\]') + p('Vilket värde har uttrycket egentligen?')},
}
