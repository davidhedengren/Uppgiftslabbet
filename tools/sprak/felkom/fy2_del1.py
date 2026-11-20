# Felkommentarer, Fy2 del 1: interferens, magnetfält och kraft på ledare (2026-11-20).
# Riktningsuppgifterna har alltid alternativen höger, vänster, uppåt, nedåt, in i pappret, ut ur pappret.
R = ['höger', 'vänster', 'uppåt', 'nedåt', 'in', 'ut']
MOT = {'höger': 'vänster', 'vänster': 'höger', 'uppåt': 'nedåt', 'nedåt': 'uppåt', 'in': 'ut', 'ut': 'in'}


def ledare(strom, laget, ratt):
    """Fältet runt en rak ledare med strömmen in i/ut ur pappret; P ligger på sidan 'laget' (riktning från ledaren)."""
    varv = 'moturs' if strom == 'ut' else 'medurs'
    regel = f'Med strömmen {strom} ur pappret går fältet {varv} runt ledaren.' if strom == 'ut' else \
        f'Med strömmen in i pappret går fältet {varv} runt ledaren.'
    ut = []
    for r in R:
        if r == ratt:
            ut.append(None)
        elif r in ('in', 'ut'):
            ut.append('Fältet går i cirklar runt ledaren i pappersplanet. Det pekar inte in i eller ut ur pappret.')
        elif r in (laget, MOT[laget]):
            ut.append('Fältet går runt ledaren, inte mot den eller bort från den. ' + regel)
        else:
            ut.append('Det är motsatt riktning. ' + regel)
    return ut


def kraft(strom, falt, ratt):
    """Kraften på en ledare: vinkelrät mot både strömmen och fältet."""
    ut = []
    for r in R:
        if r == ratt:
            ut.append(None)
        elif r in (strom, MOT[strom]):
            ut.append('Kraften är vinkelrät mot strömmen, så den kan inte peka längs ledaren.')
        elif r in (falt, MOT[falt]):
            ut.append('Kraften är vinkelrät mot magnetfältet, så den kan inte peka längs fältet.')
        else:
            ut.append('Kraften pekar åt motsatt håll. Kontrollera med högerhandsregeln.')
    return ut


def slinga(medurs):
    ratt = 'in' if medurs else 'ut'
    regel = ('Medurs ström ger ett fält in i pappret i mitten.' if medurs else
             'Moturs ström ger ett fält ut ur pappret i mitten.')
    return [None if r == ratt else (regel if r in ('in', 'ut') else
            'I mitten av slingan är fältet vinkelrätt mot slingans plan, alltså in i eller ut ur pappret.') for r in R]


MAX = lambda n: f'Vägskillnaden delat med våglängden är {n}, ett heltal. Vågorna förstärker varandra.'
MIN = lambda n: f'Vägskillnaden delat med våglängden är {n}, alltså en halv våglängd extra. Vågorna släcker ut varandra.'

K = {
    # ---------- interferens ----------
    '2.90': [None, MAX('0,50/0,50 = 1')],
    '2.116': [None, 'Två toppar som sammanfaller ger en dubbelt så hög topp, inte noll.',
              'När två toppar sammanfaller adderas de.', 'När två toppar sammanfaller adderas de, så amplituden blir större.'],
    '2.117': [None, MAX('0,80/0,40 = 2')],
    '2.118': [None, MIN('0,25/0,50 = 0,5')],
    '2.121': [None, MIN('0,90/0,60 = 1,5')],
    '2.151': [None, 'Det är omvänt. I fas och med samma väg möts topp mot topp, så det blir maximum.',
              'C ligger mitt emellan högtalarna, så vägskillnaden är 0.',
              'I motfas möts topp mot dal när vägskillnaden är 0. Det ger ett minimum.'],
    '2.152': [None, MAX('0,8/0,80 = 1')],
    '2.156': [None, MIN('0,75/0,50 = 1,5')],
    '2.164': [None, 'Vägskillnaden är \\(\\sqrt8-\\sqrt5\\approx0{,}59\\) m, ungefär en halv våglängd. Det ger ett minimum.'],
    '2.165': [None, 'Vägskillnaden är ungefär 0,46 m, och våglängden är 340/735 ≈ 0,46 m. En hel våglängd ger ett maximum.'],
    '2.166': [None, 'Vägskillnaden är ungefär 0,76 m, och våglängden är 340/223 ≈ 1,52 m. En halv våglängd ger ett minimum.'],
    # ---------- fältet runt en rak ledare ----------
    '3.145': ledare('ut', 'uppåt', 'vänster'),
    '3.146': ledare('in', 'nedåt', 'vänster'),
    '3.147': ledare('ut', 'vänster', 'nedåt'),
    '3.148': ledare('in', 'höger', 'nedåt'),
    '3.149': ledare('ut', 'nedåt', 'höger'),
    '3.150': ledare('in', 'vänster', 'uppåt'),
    '3.151': ledare('ut', 'höger', 'uppåt'),
    '3.152': ledare('in', 'uppåt', 'höger'),
    '3.153': ledare('ut', 'uppåt', 'vänster'),
    '3.154': ledare('in', 'nedåt', 'vänster'),
    '3.155': ledare('ut', 'vänster', 'nedåt'),
    '3.156': ledare('in', 'höger', 'nedåt'),
    '3.157': ledare('ut', 'nedåt', 'höger'),
    '3.158': ledare('in', 'vänster', 'uppåt'),
    '3.159': ledare('ut', 'höger', 'uppåt'),
    '3.160': ledare('in', 'uppåt', 'höger'),
    # ---------- kraft på strömförande ledare ----------
    '3.161': kraft('höger', 'ut', 'nedåt'),
    '3.162': kraft('vänster', 'ut', 'uppåt'),
    '3.163': kraft('uppåt', 'ut', 'höger'),
    '3.164': kraft('nedåt', 'ut', 'vänster'),
    '3.165': kraft('höger', 'in', 'uppåt'),
    '3.166': kraft('uppåt', 'in', 'vänster'),
    '3.167': kraft('ut', 'höger', 'uppåt'),
    '3.168': kraft('in', 'vänster', 'uppåt'),
    '3.169': kraft('höger', 'uppåt', 'ut'),
    '3.170': kraft('vänster', 'nedåt', 'ut'),
    '3.171': kraft('nedåt', 'höger', 'ut'),
    '3.172': kraft('uppåt', 'vänster', 'ut'),
    # ---------- strömslinga och spole ----------
    '3.185': slinga(False), '3.186': slinga(True), '3.187': slinga(False), '3.188': slinga(True),
    '3.189': slinga(False), '3.190': slinga(True), '3.191': slinga(False), '3.192': slinga(True),
    # ---------- stavmagnet ----------
    '3.229': ['Fältlinjerna går ut från nordpolen. Till vänster om N pekar fältet därför åt vänster.', None,
              'P ligger på magnetens axel, så fältet pekar längs axeln.', 'P ligger på magnetens axel, så fältet pekar längs axeln.',
              'Fältet ligger i pappersplanet här.', 'Fältet ligger i pappersplanet här.'],
    '3.230': ['Fältlinjerna går in i sydpolen. Till höger om S pekar fältet därför åt vänster, mot S.', None,
              'P ligger på magnetens axel, så fältet pekar längs axeln.', 'P ligger på magnetens axel, så fältet pekar längs axeln.',
              'Kompassen ligger i bildens plan och pekar längs fältet där.', 'Kompassen ligger i bildens plan och pekar längs fältet där.'],
    # ---------- kosmologi ----------
    '5.14': [None, 'Stjärnorna är en liten del av universums energiinnehåll och avgör inte ensamma.', None,
             'Framtiden beror på hur mörk energi och materia påverkar expansionen.'],
}
