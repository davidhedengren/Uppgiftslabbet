"""Fy1 kopplingar: fler kretsar på E-nivå, 8.782–8.811 (2026-11-24).

Användaren 2026-11-24, efter 8.740–8.781: ”Bra, lägg till ännu fler kretsar på E-nivå.”

30 uppgifter på träningsnivå 1 (ett steg) och 2 (två steg), alla med en egen kretsfigur. Tyngdpunkt på det som
eleverna behöver för att förstå en blandad krets innan de räknar på den: vilka komponenter som är parallell- eller
seriekopplade, vilka som har samma ström eller samma spänning, vad mätarna visar, och korta beräkningar med
knutpunktsregeln, spänningslagen och Ohms lag. Nya topologier och sammanhang jämfört med 8.740–8.781.

Hjälpfunktioner, nivåer och fält kommer från bygg-fy1-komplexa-kopplingar-2026-11-24.py; figurerna från kretsrit.py.

  python tools/bygg-fy1-komplexa-kopplingar-e-2026-11-24.py [--skriv]
"""
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location('kk1', HERE / 'bygg-fy1-komplexa-kopplingar-2026-11-24.py')
K = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(K)
import bankobjekt as B  # noqa: E402
from kretsrit import R, L, M, S, Sakring, Ser, Par, krets  # noqa: E402,F401

uppgift, givet, li, p, mt, al, par = K.uppgift, K.givet, K.li, K.p, K.mt, K.al, K.par
F_RES, F_IU = K.F_RES, K.F_IU
OHM, V, A = K.OHM, K.V, K.A
OHMS_LAG, SERIE, PARALLELL, KNUT = K.OHMS_LAG, K.SERIE, K.PARALLELL, K.KNUT
ROOT, SKRIV = K.ROOT, '--skriv' in sys.argv
mA = '\\ \\mathrm{mA}'


def begrepp():
    """Flerval på nivå 1: se kopplingen i figuren."""
    uppgift('8.782', 1, F_IU, 'Tre resistorer är kopplade till ett batteri.',
            krets(Ser(R('R₁'), Par(R('R₂'), R('R₃'))), '6,0 V', 'R₁ i serie med R₂ och R₃, som är parallellkopplade'),
            'Vilka resistorer är parallellkopplade med varandra?', None, None,
            [li('Parallellkopplade komponenter sitter mellan samma två knutpunkter',
                p('R₂ och R₃ börjar i samma knutpunkt och slutar i samma knutpunkt. R₁ sitter före förgreningen, i huvudledningen.'))],
            'R₂ och R₃.', 'Leta efter de två knutpunkterna där strömmen delar sig och samlas igen.', formaga=('begrepp',),
            alternativ=[('R₂ och R₃', True, 'De sitter mellan samma två knutpunkter.'),
                        ('R₁ och R₂', False, 'R₁ sitter i huvudledningen före förgreningen, i serie med paret.'),
                        ('R₁ och R₃', False, 'R₁ har inte samma två ändpunkter som R₃.'),
                        ('Alla tre', False, 'R₁ ligger i serie med de två andra.')])

    uppgift('8.783', 1, F_IU, 'En krets har två parallella grenar. I den undre grenen sitter R₂ och R₃.',
            krets(Par(R('R₁'), Ser(R('R₂'), R('R₃'))), '9,0 V', 'R₁ i en gren, R₂ och R₃ i serie i den andra'),
            'Vilka resistorer har alltid samma ström?', None, None,
            [li('Seriekopplade komponenter har samma ström',
                p('I den undre grenen finns ingen förgrening mellan R₂ och R₃. Strömmen som går genom R₂ måste också gå genom R₃.'))],
            'R₂ och R₃.', 'Var kan strömmen dela sig? Finns det någon knutpunkt mellan R₂ och R₃?', formaga=('begrepp',),
            alternativ=[('R₂ och R₃', True, 'De sitter efter varandra i samma gren utan någon förgrening emellan.'),
                        ('R₁ och R₂', False, 'R₁ och R₂ sitter i olika grenar och har samma spänning över grenarna, inte samma ström.'),
                        ('R₁ och R₃', False, 'Strömmen delar sig mellan grenarna, så R₁ och R₃ har i allmänhet olika ström.'),
                        ('Alla tre', False, 'Strömmen delar sig mellan grenarna.')])

    uppgift('8.784', 1, F_IU, 'I kretsen sitter lampan L₁ i huvudledningen. L₂ och L₃ sitter i var sin gren.',
            krets(Ser(L('L₁'), Par(L('L₂'), L('L₃'))), '4,5 V', 'L₁ i serie med parallellkopplade L₂ och L₃'),
            'Vilka lampor har alltid samma spänning?', None, None,
            [li('Parallellkopplade komponenter har samma spänning',
                p('L₂ och L₃ är kopplade mellan samma två knutpunkter, så spänningen över dem är lika stor även om lamporna är olika.'))],
            'L₂ och L₃.', 'Vilka lampor har samma två knutpunkter i ändarna?', formaga=('begrepp',),
            alternativ=[('L₂ och L₃', True, 'De är parallellkopplade och har samma spänning.'),
                        ('L₁ och L₂', False, 'L₁ och L₂ är seriekopplade. De delar på batteriets spänning.'),
                        ('L₁ och L₃', False, 'L₁ sitter i huvudledningen och har inte samma knutpunkter som L₃.'),
                        ('Alla tre', False, 'L₁ sitter inte mellan samma knutpunkter som L₂ och L₃, så den har i allmänhet en annan spänning.')])

    uppgift('8.785', 2, F_IU, 'Tre amperemetrar sitter i kretsen: A₁ i huvudledningen och A₂ och A₃ i var sin gren.',
            krets(Ser(M('A', 'A₁'), Par(Ser(R('R₁', '10 Ω'), M('A', 'A₂')), Ser(R('R₂', '20 Ω'), M('A', 'A₃')))), '6,0 V',
                  'Amperemetern A₁ i huvudledningen, R₁ = 10 Ω med A₂ och R₂ = 20 Ω med A₃ i var sin gren'),
            'Vilken amperemeter visar störst värde?', None, None,
            [li(f'{KNUT}: \\(I_1=I_2+I_3\\)', p('A₁ mäter hela strömmen, som sedan delar sig på grenarna. A₁ visar alltså summan av A₂ och A₃.')),
             li(OHMS_LAG, mt('I_2=\\frac{6{,}0}{10}=0{,}60' + A + ',\\quad I_3=\\frac{6{,}0}{20}=0{,}30' + A),
                mt('I_1=0{,}60+0{,}30=0{,}90' + A))],
            'A₁.', 'Vilken amperemeter mäter strömmen innan den delar sig?', formaga=('begrepp',),
            alternativ=[('A₁', True, 'A₁ mäter hela strömmen, summan av grenströmmarna.'),
                        ('A₂', False, 'A₂ visar störst av grenströmmarna, men A₁ visar summan av båda.'),
                        ('A₃', False, 'Grenen med 20 Ω får minst ström.'),
                        ('Alla visar samma', False, 'Strömmen delar sig i knutpunkten, så grenströmmarna är mindre än huvudströmmen.')])

    uppgift('8.786', 2, F_IU, 'R₂ och R₃ är parallellkopplade, och R₁ sitter i huvudledningen. Brytaren sluts, så att resistorn R₄ kopplas in '
            'som en tredje gren.',
            krets(Ser(R('R₁'), Par(R('R₂'), R('R₃'), Ser(R('R₄'), S('', oppen=True)))), '12 V', 'R₁ i serie med R₂ och R₃ parallellt, och R₄ med en brytare som tredje gren'),
            'Hur ändras strömmen genom R₁ när brytaren sluts?', None, None,
            [li('Fler parallella grenar ger mindre ersättningsresistans',
                p('Strömmen får ytterligare en väg genom parallellkopplingen, så dess resistans blir mindre. Hela kretsens resistans minskar.')),
             li(f'{OHMS_LAG}: \\(I=\\frac{{U}}{{R}}\\)', p('Samma batterispänning och mindre resistans ger större ström. Hela strömmen går genom R₁.'))],
            'Strömmen genom R₁ ökar.', 'Blir det lättare eller svårare för strömmen att ta sig igenom parallelldelen?', formaga=('begrepp',),
            alternativ=[('Den ökar', True, 'Ersättningsresistansen minskar, så batteriet driver mer ström genom R₁.'),
                        ('Den minskar', False, 'En extra parallell gren minskar resistansen, den ökar den inte.'),
                        ('Den är oförändrad', False, 'Hela kretsens resistans ändras, och därmed strömmen genom R₁.'),
                        ('Den blir noll', False, 'R₁ sitter kvar i en sluten krets.')])


def matare():
    uppgift('8.787', 1, F_IU,
            'Voltmetern V₁ visar 3,5 V över R₁, och voltmetern V₂ visar spänningen över de parallellkopplade R₂ och R₃. '
            'Batteriets spänning är 9,0 V.',
            krets(Ser(Par(R('R₁'), M('V', 'V₁')), Par(R('R₂'), R('R₃'), M('V', 'V₂'))), '9,0 V',
                  'R₁ med voltmetern V₁, i serie med R₂ och R₃ parallellt med voltmetern V₂'),
            'Vad visar V₂?', 5.5, 'V',
            [givet('U=9{,}0\\ \\mathrm V', 'U_1=3{,}5\\ \\mathrm V', sokt='spänningen \\(U_2\\) som V₂ visar'),
             li('Spänningarna längs vägen genom kretsen summeras: \\(U=U_1+U_2\\)', mt('U_2=9{,}0-3{,}5=5{,}5' + V))],
            '5,5 V.', 'Följ en väg från pluspolen till minuspolen. Vilka två spänningar ligger längs den?')

    uppgift('8.788', 1, F_IU,
            'Två voltmetrar mäter spänningarna i en lampkrets. V₁ över L₁ visar 2,0 V, och V₂ över de parallellkopplade '
            'L₂ och L₃ visar 4,0 V.',
            krets(Ser(Par(L('L₁'), M('V', 'V₁')), Par(L('L₂'), L('L₃'), M('V', 'V₂'))), '', 'L₁ med voltmetern V₁ i serie med L₂ och L₃ parallellt med V₂'),
            'Hur stor är batteriets spänning?', 6.0, 'V',
            [givet('U_1=2{,}0\\ \\mathrm V', 'U_2=4{,}0\\ \\mathrm V', sokt='batteriets spänning \\(U\\)'),
             li('Spänningarna längs vägen genom kretsen summeras: \\(U=U_1+U_2\\)', mt('U=2{,}0+4{,}0=6{,}0' + V))],
            '6,0 V.', 'Batteriets spänning fördelas längs vägen genom kretsen. Vilka delar passerar vägen?')

    uppgift('8.789', 1, F_IU,
            'A₁ i huvudledningen visar 450 mA. A₂ sitter i grenen med R₂ och visar 180 mA.',
            krets(Ser(M('A', 'A₁'), Par(Ser(R('R₂'), M('A', 'A₂')), R('R₃')), R('R₁')), '9,0 V',
                  'A₁ i huvudledningen, R₂ med A₂ parallellt med R₃, R₁ i serie'),
            'Hur stor är strömmen genom R₃ i mA?', 270, 'mA',
            [givet('I=450\\ \\mathrm{mA}', 'I_2=180\\ \\mathrm{mA}', sokt='strömmen \\(I_3\\) genom R₃'),
             li(f'{KNUT}: \\(I=I_2+I_3\\)', mt('I_3=450-180=270' + mA))],
            '270 mA.', 'Strömmen i huvudledningen delar sig mellan grenen med R₂ och R₃.')

    uppgift('8.790', 1, F_IU,
            'Amperemetern A₂ sitter i grenen med lampan L₂ (24 Ω). Grenen är kopplad direkt över batteriet på 12 V.',
            krets(Par(Ser(L('L₁'), L('L₃')), Ser(L('L₂', '24 Ω'), M('A', 'A₂'))), '12 V', 'L₁ och L₃ i serie i en gren, L₂ = 24 Ω med amperemetern A₂ i den andra'),
            'Vad visar A₂?', 0.50, 'A',
            [givet('U=12\\ \\mathrm V', 'R_2=24\\ \\Omega', sokt='strömmen genom L₂'),
             li(f'{OHMS_LAG}: \\(I=\\frac{{U}}{{R}}\\)', p('Grenen med L₂ har hela batterispänningen. Amperemetern har mycket liten resistans.'),
                mt('I_2=\\frac{12}{24}=0{,}50' + A))],
            '0,50 A.', 'Vilken spänning ligger över grenen med L₂? Påverkar den andra grenen den?')

    uppgift('8.791', 2, F_IU,
            'A₁ i huvudledningen visar 1,2 A och A₂, i grenen med R₁ = 15 Ω, visar 0,40 A.',
            krets(Ser(M('A', 'A₁'), Par(Ser(R('R₁', '15 Ω'), M('A', 'A₂')), R('R₂'))), '', 'A₁ i huvudledningen, R₁ = 15 Ω med A₂ parallellt med R₂'),
            'Hur stor är resistansen R₂?', 7.5, 'Ω',
            [givet('I=1{,}2\\ \\mathrm A', 'I_1=0{,}40\\ \\mathrm A', 'R_1=15\\ \\Omega', sokt='\\(R_2\\)'),
             li(f'{OHMS_LAG} för R₁ ger spänningen över grenarna', mt('U=15\\cdot0{,}40=6{,}0' + V)),
             li(f'{KNUT}, sedan Ohms lag för R₂', mt('I_2=1{,}2-0{,}40=0{,}80' + A), mt('R_2=\\frac{6{,}0}{0{,}80}=7{,}5' + OHM))],
            '7,5 Ω.', 'R₁ och R₂ har samma spänning. Hur stor är den, och hur stor ström går genom R₂?')

    uppgift('8.792', 2, F_IU,
            'Voltmetern visar spänningen över R₁ = 25 Ω, som sitter i huvudledningen. Amperemetern visar 0,40 A och '
            'batteriets spänning är 18 V.',
            krets(Ser(M('A'), Par(R('R₁', '25 Ω'), M('V')), Par(R('R₂'), R('R₃'))), '18 V', 'Amperemeter och R₁ = 25 Ω med voltmeter, i serie med R₂ och R₃ parallellt'),
            'Hur stor är spänningen över parallellkopplingen av R₂ och R₃?', 8.0, 'V',
            [givet('U=18\\ \\mathrm V', 'I=0{,}40\\ \\mathrm A', 'R_1=25\\ \\Omega', sokt='spänningen \\(U_p\\) över parallelldelen'),
             li(OHMS_LAG + ' för R₁', mt('U_1=25\\cdot0{,}40=10' + V)),
             li('Spänningarna längs vägen summeras: \\(U=U_1+U_p\\)', mt('U_p=18-10=8{,}0' + V))],
            '8,0 V.', 'Räkna först ut vad voltmetern visar.')


def berakningar():
    uppgift('8.793', 1, F_IU,
            'Strömmen genom R₂ är 0,30 A. R₂ och R₃ sitter efter varandra i samma gren, och R₁ sitter i den andra grenen.',
            krets(Par(R('R₁'), Ser(R('R₂'), R('R₃'))), '6,0 V', 'R₁ i en gren, R₂ och R₃ i serie i den andra'),
            'Hur stor är strömmen genom R₃?', 0.30, 'A',
            [givet('I_2=0{,}30\\ \\mathrm A', sokt='strömmen \\(I_3\\) genom R₃'),
             li('Seriekopplade komponenter har samma ström: \\(I_3=I_2\\)', p('Det finns ingen förgrening mellan R₂ och R₃.'), mt('I_3=0{,}30' + A))],
            '0,30 A.', 'Finns det någon knutpunkt mellan R₂ och R₃ där strömmen kan dela sig?')

    uppgift('8.794', 1, F_IU,
            'I en grenledning ligger R₂ och R₃ i serie. Över R₂ är spänningen 2,5 V och över R₃ 3,5 V. R₁ sitter i den '
            'andra grenen.',
            krets(Par(R('R₁'), Ser(R('R₂'), R('R₃'))), '', 'R₁ parallellt med grenen R₂ och R₃'),
            'Hur stor är spänningen över R₁?', 6.0, 'V',
            [givet('U_2=2{,}5\\ \\mathrm V', 'U_3=3{,}5\\ \\mathrm V', sokt='spänningen \\(U_1\\)'),
             li('Parallella grenar har samma spänning: \\(U_1=U_2+U_3\\)', p('Grenen med R₂ och R₃ och R₁ sitter mellan samma två knutpunkter.'),
                mt('U_1=2{,}5+3{,}5=6{,}0' + V))],
            '6,0 V.', 'Hur stor spänning ligger över hela grenen med R₂ och R₃?')

    uppgift('8.795', 1, F_RES, 'Tre resistorer på 30 Ω är parallellkopplade, och R₄ ligger i serie med dem.',
            krets(Ser(Par(R('R₁', '30 Ω'), R('R₂', '30 Ω'), R('R₃', '30 Ω')), R('R₄')), '', 'Tre parallellkopplade 30 Ω i serie med R₄', batteri=False),
            'Vilken ersättningsresistans har de tre parallellkopplade resistorerna?', 10, 'Ω',
            [givet('R_1=R_2=R_3=30\\ \\Omega', sokt='ersättningsresistansen för de tre'),
             li('Tre lika parallellkopplade resistorer: \\(R_p=\\frac{R}{3}\\)', mt('R_p=\\frac{30}{3}=10' + OHM))],
            '10 Ω.', 'Strömmen får tre lika breda vägar.')

    uppgift('8.796', 1, F_IU,
            'En liten pump och en lampa i ett akvarium har tillsammans med en resistor ersättningsresistansen 12 Ω. '
            'Kretsen drivs av 9,0 V.',
            krets(Ser(R('R'), Par(L('Lampa'), R('Pump'))), '9,0 V', 'Resistor i serie med lampan och pumpen parallellt'),
            'Hur stor ström går genom resistorn R?', 0.75, 'A',
            [givet('U=9{,}0\\ \\mathrm V', 'R_{\\text{tot}}=12\\ \\Omega', sokt='strömmen genom R'),
             li(f'{OHMS_LAG} för hela kretsen', p('R sitter i huvudledningen och har hela strömmen.'),
                mt('I=\\frac{9{,}0}{12}=0{,}75' + A))],
            '0,75 A.', 'R sitter i huvudledningen. Vilken ström har den jämfört med batteriet?')

    uppgift('8.797', 1, F_IU,
            'En ljusslinga har två parallella grenar med tio lika lampor i serie i varje gren. Slingan är kopplad till '
            '230 V.',
            krets(Par(Ser(L('L₁'), L('L₂'), L('…'), L('L₁₀')), Ser(L('L₁₁'), L('L₁₂'), L('…'), L('L₂₀'))), '230 V',
                  'Två grenar med tio lampor i serie i varje, 230 V'),
            'Hur stor spänning ligger över varje lampa?', 23, 'V',
            [givet('U=230\\ \\mathrm V', 'n=10\\ \\text{lampor per gren}', sokt='spänningen över en lampa'),
             li('Varje gren har hela spänningen, som delas lika mellan tio lika lampor i serie: \\(U_L=\\frac{U}{n}\\)', mt('U_L=\\frac{230}{10}=23' + V))],
            '23 V.', 'Hur stor spänning ligger över en hel gren?')

    uppgift('8.798', 1, F_RES,
            'En gren med R₂ och R₃ har resistansen 20 Ω. Den är parallellkopplad med R₁ = 20 Ω.',
            krets(Par(R('R₁', '20 Ω'), Ser(R('R₂'), R('R₃'))), '', 'R₁ = 20 Ω parallellt med grenen R₂ och R₃', batteri=False),
            'Vilken ersättningsresistans har kopplingen mellan A och B?', 10, 'Ω',
            [givet('R_1=20\\ \\Omega', 'R_{23}=20\\ \\Omega', sokt='ersättningsresistansen'),
             li('Två lika parallella grenar ger halva resistansen: \\(R=\\frac{R_1}{2}\\)', mt('R=\\frac{20}{2}=10' + OHM))],
            '10 Ω.', 'Jämför de två grenarnas resistans.')

    uppgift('8.799', 1, F_IU,
            'Lampan L₃ (15 Ω) i en modelljärnväg sitter i en egen gren. Spänningen över grenarna är 4,5 V.',
            krets(Ser(R('R₁'), Par(Ser(L('L₁'), L('L₂')), L('L₃', '15 Ω'))), '12 V', 'R₁ i serie med L₁ och L₂ i en gren parallellt med L₃ = 15 Ω'),
            'Hur stor ström går genom L₃?', 0.30, 'A',
            [givet('U_3=4{,}5\\ \\mathrm V', 'R_3=15\\ \\Omega', sokt='strömmen \\(I_3\\)'),
             li(f'{OHMS_LAG}: \\(I=\\frac{{U}}{{R}}\\)', mt('I_3=\\frac{4{,}5}{15}=0{,}30' + A))],
            '0,30 A.', 'Vilken spänning ligger över L₃, och vilken resistans har den?')

    uppgift('8.800', 1, F_IU,
            'I ett kök är tre apparater parallellkopplade efter samma säkring. Strömmarna genom dem är 4,0 A, 2,5 A '
            'och 3,5 A.',
            krets(Ser(Sakring('Säkring'), Par(R('Kokplatta'), R('Kaffebryggare'), R('Brödrost'))), '230 V',
                  'Säkring i serie med kokplatta, kaffebryggare och brödrost parallellt'),
            'Hur stor ström går genom säkringen?', 10, 'A',
            [givet('I_1=4{,}0\\ \\mathrm A', 'I_2=2{,}5\\ \\mathrm A', 'I_3=3{,}5\\ \\mathrm A', sokt='strömmen genom säkringen'),
             li(f'{KNUT}: \\(I=I_1+I_2+I_3\\)', mt('I=4{,}0+2{,}5+3{,}5=10' + A))],
            '10 A.', 'Säkringen sitter före förgreningen. Vilka strömmar går genom den?')

    # ---------------- nivå 2
    uppgift('8.801', 2, F_RES, 'Tre lika resistorer är parallellkopplade, och R₄ = 15 Ω ligger i serie med dem.',
            krets(Ser(Par(R('R₁', '30 Ω'), R('R₂', '30 Ω'), R('R₃', '30 Ω')), R('R₄', '15 Ω')), '', 'Tre parallellkopplade 30 Ω i serie med R₄ = 15 Ω', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B.', 25, 'Ω',
            [givet('R_1=R_2=R_3=30\\ \\Omega', 'R_4=15\\ \\Omega', sokt='ersättningsresistansen'),
             li('Tre lika parallellkopplade resistorer: \\(R_p=\\frac{R}{3}\\)', mt('R_p=\\frac{30}{3}=10' + OHM)),
             li(SERIE, mt('R=10+15=25' + OHM))],
            '25 Ω.', 'Ersätt först de tre parallellkopplade med en resistor.')

    uppgift('8.802', 2, F_RES,
            'Instrumentbelysningen i en bil har lampan L₁ (18 Ω) i huvudledningen och tre lika lampor på 18 Ω i var sin gren.',
            krets(Ser(L('L₁', '18 Ω'), Par(L('L₂', '18 Ω'), L('L₃', '18 Ω'), L('L₄', '18 Ω'))), '12 V', 'L₁ = 18 Ω i serie med tre parallellkopplade lampor på 18 Ω'),
            'Bestäm lampkopplingens ersättningsresistans.', 24, 'Ω',
            [givet('R_1=R_2=R_3=R_4=18\\ \\Omega', sokt='ersättningsresistansen'),
             li('Tre lika parallellkopplade lampor: \\(R_p=\\frac{R}{3}\\)', mt('R_p=\\frac{18}{3}=6{,}0' + OHM)),
             li(SERIE, mt('R=18+6{,}0=24' + OHM))],
            '24 Ω.', 'Vilka lampor delar på strömmen?')

    uppgift('8.803', 2, F_RES, 'Två parallellkopplingar sitter efter varandra mellan A och B.',
            krets(Ser(Par(L('L₁', '12 Ω'), L('L₂', '4,0 Ω')), Par(R('R₁', '10 Ω'), R('R₂', '15 Ω'))), '',
                  'L₁ = 12 Ω parallellt med L₂ = 4,0 Ω, i serie med R₁ = 10 Ω parallellt med R₂ = 15 Ω', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B.', 9.0, 'Ω',
            [givet('R_{L1}=12\\ \\Omega', 'R_{L2}=4{,}0\\ \\Omega', 'R_1=10\\ \\Omega', 'R_2=15\\ \\Omega', sokt='ersättningsresistansen'),
             li(f'Lamporna. {PARALLELL}', mt('\\frac{1}{R_L}=\\frac{1}{12}+\\frac{1}{4{,}0}=\\frac{4}{12}\\quad\\Rightarrow\\quad R_L=3{,}0' + OHM)),
             li('Resistorerna, på samma sätt', mt('\\frac{1}{R_R}=\\frac{1}{10}+\\frac{1}{15}=\\frac{5}{30}\\quad\\Rightarrow\\quad R_R=6{,}0' + OHM)),
             li(f'De två delarna i serie. {SERIE}', mt('R=3{,}0+6{,}0=9{,}0' + OHM))],
            '9,0 Ω.', 'Ersätt varje parallellkoppling med en resistor för sig.')

    uppgift('8.804', 2, F_RES, 'På ett kretskort är tre resistorer kopplade mellan A och B.',
            krets(Par(Ser(R('R₁', '4,7 kΩ'), R('R₂', '5,3 kΩ')), R('R₃', '10 kΩ')), '', 'R₁ = 4,7 kΩ och R₂ = 5,3 kΩ i serie, parallellt med R₃ = 10 kΩ', batteri=False),
            'Bestäm ersättningsresistansen mellan A och B i kΩ.', 5.0, 'kΩ',
            [givet('R_1=4{,}7\\ \\mathrm{k\\Omega}', 'R_2=5{,}3\\ \\mathrm{k\\Omega}', 'R_3=10\\ \\mathrm{k\\Omega}', sokt='ersättningsresistansen i kΩ'),
             li(f'R₁ och R₂ i samma gren. {SERIE}', mt('R_{12}=4{,}7+5{,}3=10\\ \\mathrm{k\\Omega}')),
             li('Två lika parallella grenar ger halva resistansen: \\(R=\\frac{R_{12}}{2}\\)', mt('R=\\frac{10}{2}=5{,}0\\ \\mathrm{k\\Omega}'))],
            '5,0 kΩ.', 'Räkna först ut grenen med två resistorer. Jämför den sedan med R₃.')

    uppgift('8.805', 2, F_IU, 'Tre grenar är parallellkopplade till ett batteri på 6,0 V. Amperemetern sitter i huvudledningen.',
            krets(Ser(M('A'), Par(R('R₁', '12 Ω'), R('R₂', '6,0 Ω'), R('R₃', '4,0 Ω'))), '6,0 V', 'Amperemeter i serie med tre parallellkopplade resistorer 12 Ω, 6,0 Ω och 4,0 Ω'),
            'Vad visar amperemetern?', 3.0, 'A',
            [givet('U=6{,}0\\ \\mathrm V', 'R_1=12\\ \\Omega', 'R_2=6{,}0\\ \\Omega', 'R_3=4{,}0\\ \\Omega', sokt='huvudströmmen'),
             li(f'{OHMS_LAG} för varje gren, som har hela batterispänningen',
                al('I_1=\\frac{6{,}0}{12}=0{,}50' + A, 'I_2=\\frac{6{,}0}{6{,}0}=1{,}0' + A, 'I_3=\\frac{6{,}0}{4{,}0}=1{,}5' + A)),
             li(f'{KNUT}: \\(I=I_1+I_2+I_3\\)', mt('I=0{,}50+1{,}0+1{,}5=3{,}0' + A))],
            '3,0 A.', 'Varje gren har batteriets spänning. Hur stor ström går i varje gren?')

    uppgift('8.806', 2, F_IU, 'En ficklampa har två lampor, L₁ (8,0 Ω) och L₂ (4,0 Ω), i serie i en gren. Grenen sitter direkt över batteriet på 6,0 V, '
            'parallellt med lampan L₃.',
            krets(Par(Ser(L('L₁', '8,0 Ω'), L('L₂', '4,0 Ω')), L('L₃')), '6,0 V', 'L₁ = 8,0 Ω och L₂ = 4,0 Ω i serie, parallellt med L₃'),
            'Hur stor ström går genom L₁?', 0.50, 'A',
            [givet('U=6{,}0\\ \\mathrm V', 'R_1=8{,}0\\ \\Omega', 'R_2=4{,}0\\ \\Omega', sokt='strömmen \\(I_1\\)'),
             li(f'Grenens resistans. {SERIE}', mt('R_{12}=8{,}0+4{,}0=12' + OHM)),
             li(f'{OHMS_LAG} för grenen, som har hela batterispänningen', mt('I_1=\\frac{6{,}0}{12}=0{,}50' + A))],
            '0,50 A.', 'L₁ och L₂ har samma ström. Vilken spänning ligger över deras gren?')

    uppgift('8.807', 2, F_IU, 'Parallellkopplingen av R₂ och R₃ har ersättningsresistansen 4,0 Ω. R₁ = 8,0 Ω och batteriet ger 12 V.',
            krets(Ser(R('R₁', '8,0 Ω'), Par(R('R₂'), R('R₃'))), '12 V', 'R₁ = 8,0 Ω i serie med R₂ och R₃ parallellt'),
            'Hur stor är spänningen över parallellkopplingen?', 4.0, 'V',
            [givet('U=12\\ \\mathrm V', 'R_1=8{,}0\\ \\Omega', 'R_p=4{,}0\\ \\Omega', sokt='spänningen \\(U_p\\)'),
             li(f'{OHMS_LAG} för hela kretsen', mt('I=\\frac{12}{8{,}0+4{,}0}=1{,}0' + A)),
             li('Ohms lag för parallellkopplingen: \\(U_p=R_pI\\)', mt('U_p=4{,}0\\cdot1{,}0=4{,}0' + V))],
            '4,0 V.', 'Räkna ut huvudströmmen. Den går genom hela parallellkopplingen.')

    uppgift('8.808', 2, F_IU, 'Grenen med R₁ = 5,0 Ω och R₂ = 10 Ω är kopplad direkt över ett batteri på 6,0 V. R₃ sitter i en egen gren.',
            krets(Par(Ser(R('R₁', '5,0 Ω'), R('R₂', '10 Ω')), R('R₃')), '6,0 V', 'R₁ = 5,0 Ω och R₂ = 10 Ω i serie, parallellt med R₃'),
            'Hur stor är spänningen över R₁?', 2.0, 'V',
            [givet('U=6{,}0\\ \\mathrm V', 'R_1=5{,}0\\ \\Omega', 'R_2=10\\ \\Omega', sokt='spänningen \\(U_1\\)'),
             li(f'{OHMS_LAG} för grenen', mt('I=\\frac{6{,}0}{5{,}0+10}=0{,}40' + A)),
             li('Ohms lag för R₁', mt('U_1=5{,}0\\cdot0{,}40=2{,}0' + V))],
            '2,0 V.', 'Grenen har batteriets spänning. Hur stor ström går då i den?')

    uppgift('8.809', 2, F_IU, 'Spänningen över parallelldelen är 6,0 V. I den ena grenen sitter L₂ (8,0 Ω) och L₃ (4,0 Ω) i serie.',
            krets(Ser(L('L₁'), Par(L('L₄'), Ser(L('L₂', '8,0 Ω'), L('L₃', '4,0 Ω')))), '9,0 V', 'L₁ i serie med L₄ parallellt med L₂ = 8,0 Ω och L₃ = 4,0 Ω i serie'),
            'Hur stor är spänningen över L₃?', 2.0, 'V',
            [givet('U_p=6{,}0\\ \\mathrm V', 'R_2=8{,}0\\ \\Omega', 'R_3=4{,}0\\ \\Omega', sokt='spänningen \\(U_3\\)'),
             li(f'{OHMS_LAG} för grenen med L₂ och L₃', mt('I=\\frac{6{,}0}{8{,}0+4{,}0}=0{,}50' + A)),
             li('Ohms lag för L₃', mt('U_3=4{,}0\\cdot0{,}50=2{,}0' + V))],
            '2,0 V.', 'Grenen med L₂ och L₃ har 6,0 V. Hur delas den mellan lamporna?')

    uppgift('8.810', 2, F_IU, 'Strömmen i huvudledningen är 0,60 A. R₂ och R₃ är parallellkopplade och lika stora, 10 Ω vardera.',
            krets(Ser(R('R₁'), Par(R('R₂', '10 Ω'), R('R₃', '10 Ω'))), '', 'R₁ i serie med två parallellkopplade 10 Ω'),
            'Hur stor är spänningen över R₂?', 3.0, 'V',
            [givet('I=0{,}60\\ \\mathrm A', 'R_2=R_3=10\\ \\Omega', sokt='spänningen \\(U_2\\)'),
             li('Lika grenar delar strömmen lika: \\(I_2=\\frac{I}{2}\\)', mt('I_2=\\frac{0{,}60}{2}=0{,}30' + A)),
             li(OHMS_LAG + ' för R₂', mt('U_2=10\\cdot0{,}30=3{,}0' + V))],
            '3,0 V.', 'Hur delar sig strömmen mellan två lika grenar?')

    uppgift('8.811', 2, F_IU, 'En sensor R₂ och en lysdiodskrets R₃ är parallellkopplade. Grenströmmarna är 20 mA och 30 mA, och R₁ = 100 Ω sitter i huvudledningen.',
            krets(Ser(R('R₁', '100 Ω'), Par(R('R₂'), R('R₃'))), '', 'R₁ = 100 Ω i serie med R₂ och R₃ parallellt'),
            'Hur stor är spänningen över R₁?', 5.0, 'V',
            [givet('I_2=20\\ \\mathrm{mA}', 'I_3=30\\ \\mathrm{mA}', 'R_1=100\\ \\Omega', sokt='spänningen \\(U_1\\)'),
             li(f'{KNUT}: \\(I_1=I_2+I_3\\)', mt('I_1=20+30=50\\ \\mathrm{mA}=0{,}050' + A)),
             li(OHMS_LAG + ' för R₁', mt('U_1=100\\cdot0{,}050=5{,}0' + V))],
            '5,0 V.', 'Hur stor ström går genom R₁? Glöm inte att göra om mA till A.')


def main():
    begrepp()
    matare()
    berakningar()
    nya = [K.objekt(u) for u in K.UPPG]
    src, bank = B.las(ROOT / 'uppgifter.js')
    ids = {q['id'] for q in bank}
    for q in nya:
        assert q['id'] not in ids, q['id']
        assert q['traningsniva'] <= 2 and q['niva'] == 'E', q['id']
    sista = max(i for i, q in enumerate(bank) if q.get('kap') == 8)
    spannen = B.spann(src)
    slut = spannen[sista][1]
    prefix = B._prefix(src, spannen[sista][0])
    ny_src = src[:slut] + ''.join(',\n' + B._dump(q, prefix) for q in nya) + src[slut:]
    assert len(json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])) == len(bank) + len(nya)
    for q in nya:
        print(q['id'], q['traningsniva'], q['familj'][:10], q['rättSvar'])
    if SKRIV:
        B.skriv(ROOT / 'uppgifter.js', ny_src)
    return nya


if __name__ == '__main__':
    main()
