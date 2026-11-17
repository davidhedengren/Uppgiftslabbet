# Fy1 kapitel 8 (Elektricitet), handgranskat 2026-11-17. Elläran undervisas nu och görs först.
# Steg 1: varje träff i k8_traffar (rättningsinstruktioner, flervalsfraser, "sammanlagd", "en elev",
# "modell", "Räkna med", "alltså", tecken- och precisionskrav) är beslutad per uppgift nedan.
# Lärarens prov skriver "en lampa på 10 Ω", "ett batteri på 9 V" och "ersättningsresistansen", så
# "på X Ω/V/W" står kvar. Enheten visas i Kunskapsgymmet via svarEnhet, så "(Svara i X.)" tas bort
# när X är en av uppgiftens svarsenheter.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

ALT = ['(Markera det korrekta alternativet.)', 'Markera det korrekta alternativet.','(Välj ett alternativ.)', 'Välj ett alternativ.', '(Välj ett uttag.)']
SYN = {'timmar': 'h', 'sekunder': 's', 'meter': 'm', 'procent': '%', 'grader': '°'}

# Instruktioner som rättningen behöver: (fras i texten, kgInstruktion, delkort som också får den).
TILL_KG = {
    '8.338': ('(Svara i N med höger som positiv riktning.)', 'Höger räknas som positiv riktning.', []),
    '8.342': ('(Svara i N med höger som positiv riktning.)', 'Höger räknas som positiv riktning.', []),
    '8.346': ('(Svara i N med höger som positiv riktning.)', 'Höger räknas som positiv riktning.', []),
    '8.76': ('(Svara i mA, först med torr hud och sedan med våt hud.)', 'Svara först med torr hud och sedan med våt hud.', ['a']),
    '8.84': ('(Svara i V, först kabeln och sedan lampan.)', 'Svara först med spänningen över kabeln och sedan över lampan.', ['c']),
    '8.40': ('Ange först effekten i 220 Ω och sedan i 330 Ω.', 'Svara först med effekten i 220 Ω och sedan i 330 Ω.', ['c']),
    '8.49': ('Ange först A, sedan B.', 'Svara först med potentialen i A och sedan i B.', ['c']),
    '8.141': ('Ange först spänningen över R₁, sedan över parallelldelen.', 'Svara först med spänningen över R₁ och sedan över parallelldelen.', ['b']),
    '8.166': ('Ange först punkten närmast minuspolen, sedan punkten närmast pluspolen.', 'Svara först med punkten närmast minuspolen.', ['b']),
    '8.124': ('(Svara med ett ord.)', 'Svara med ett ord.', ['a']),
}
# 8.104 har två riktningsinstruktioner (c och d).
TILL_KG_FLERA = {'8.104': (['(Svara i N med uppåt som positiv riktning.)', '(Svara med uppåt som positiv riktning.)'],
                           'Uppåt räknas som positiv riktning.', ['c', 'd'])}

# Precisionskrav och andra svarsinstruktioner som bara tas bort (Fy1-beslut 2026-10-26: korrekt avrundning godtas).
BORT = {
    '8.394': ['(Ange svaret med tre värdesiffror.)'],
    '8.397': ['(Svara med tre decimaler respektive en decimal.)'],
    '8.527': ['(Svara i V och procent, med en decimal.)'],
    '8.528': ['(Svara i W med två decimaler.)'],
    '8.529': ['(Svara i Ω respektive A med två decimaler.)'],
    '8.600': ['(Svara i V med 1 decimal.)'],
    '8.605': ['(Svara i V med 1 decimal.)'],
    '8.650': ['(Svara med två värdesiffror, i b i kg.)'],
    '8.675': ['(Svara i A med två värdesiffror och i Ω med två värdesiffror.)'],
    '8.520': ['(Svara i µN respektive grader med en decimal.)'],
    '8.33': ['(Svara i µN och grader.)'], '8.160': ['(Svara i µN och grader.)'],
    '8.477': ['(Svara i µC och ta med tecknet.)'], '8.489': ['(Svara i nC med tecken.)'],
    '8.524': ['(Svara i V respektive Ω.)'], '8.525': ['(Svara i V respektive Ω.)'], '8.526': ['(Svara i V respektive mA.)'],
    '8.667': ['(Svara i Ω och A.)'], '8.673': ['(Svara i A och Ω.)'], '8.735': ['(Svara i Ω respektive procent.)'],
}

# Handskrivna meningsbyten.
EXTRA = {
    '8.10': [('c) Vilken kortslutningsström ger modellen?', 'c) Bestäm kortslutningsströmmen.'),
             ('Bestäm modellens kortslutningsström.', 'Bestäm kortslutningsströmmen.')],
    '8.12': [('Hur många kilowattimmar motsvarar det, och ge ett exempel på vad energin skulle räcka till?',
              'Hur många kilowattimmar motsvarar det? Ge ett exempel på vad energin skulle räcka till.'),
             ('Luft slår igenom vid ungefär 3 MV/m. Vilket avstånd skulle 100 MV motsvara? Anta att molnet ligger 1,0 km över marken. Förklara varför modellen med ett jämnt fält inte kan beskriva hela blixten.',
              'Luft börjar leda ström vid ungefär 3 MV/m. Hur långt avstånd motsvarar 100 MV i ett jämnt fält? Molnet ligger 1,0 km över marken. Förklara varför fältet inte kan vara jämnt mellan moln och mark när blixten slår ner.'),
             ('Luft kan börja leda ström vid ungefär 3 MV/m. Anta ett jämnt elektriskt fält. Vilket avstånd motsvarar 100 MV? Molnet ligger 1,0 km över marken. Varför kan modellen inte beskriva hela blixten?',
              'Luft börjar leda ström vid ungefär 3 MV/m. Hur långt avstånd motsvarar 100 MV i ett jämnt fält? Molnet ligger 1,0 km över marken. Varför kan fältet inte vara jämnt mellan moln och mark när blixten slår ner?')],
    '8.13': [('(Svara i Ω och motivera med beräkningar eller en graf.)', 'Motivera med en beräkning eller en graf.')],
    '8.213': [('Bestäm kortslutningsströmmen enligt batterimodellen.', 'Bestäm kortslutningsströmmen.')],
    '8.235': [('I batterimodellen blir kortslutningsströmmen 4,0 A.', 'Kortslutningsströmmen är 4,0 A.')],
    '8.238': [('I batterimodellen blir kortslutningsströmmen 7,0 A.', 'Kortslutningsströmmen är 7,0 A.')],
    '8.241': [('I batterimodellen blir kortslutningsströmmen 6,0 A.', 'Kortslutningsströmmen är 6,0 A.')],
    '8.66': [('b) Vilken ström ger modellen vid kortslutning?', 'b) Hur stor blir strömmen vid kortslutning?'),
             ('Vilken ström ger batterimodellen vid kortslutning?', 'Hur stor blir strömmen vid kortslutning?')],
    '8.93': [('a) Vilken kortslutningsström ger modellen?', 'a) Bestäm kortslutningsströmmen.'),
             ('Vilken kortslutningsström ger modellen?', 'Bestäm kortslutningsströmmen.')],
    '8.32': [('det sammanlagda fältet är noll', 'det resulterande fältet är noll')],
    '8.33': [('den sammanlagda kraften', 'den resulterande kraften')],
    '8.160': [('den sammanlagda kraften', 'den resulterande kraften')],
    '8.121': [('den sammanlagda kraften', 'den resulterande kraften')],
    '8.40': [('Bestäm den sammanlagda resistansen.', 'Bestäm ersättningsresistansen.'),
             ('Bestäm deras sammanlagda resistans, som också kallas ersättningsresistans.', 'Bestäm ersättningsresistansen.'),
             ('Kretsens sammanlagda resistans är 550 Ω.', 'Ersättningsresistansen är 550 Ω.')],
    '8.124': [('Bestäm den sammanlagda resistansen.', 'Bestäm ersättningsresistansen.'),
              ('Bestäm deras sammanlagda resistans, som också kallas ersättningsresistans.', 'Bestäm ersättningsresistansen.'),
              ('Spänningen över en krets är 9,0 V och den sammanlagda resistansen är 300 Ω.', 'Spänningen över en krets är 9,0 V och ersättningsresistansen är 300 Ω.'),
              ('Spänningen är 9,0 V och den sammanlagda resistansen 300 Ω.', 'Spänningen är 9,0 V och ersättningsresistansen 300 Ω.')],
    '8.76': [('I en förenklad modell har kroppen resistansen 100 kΩ med torr hud och 1,0 kΩ med våt hud.',
              'Antag att kroppens resistans är 100 kΩ med torr hud och 1,0 kΩ med våt hud.'),
             ('I modellen blir strömmen 2,3 mA med torr hud och 230 mA med våt hud.',
              'Strömmen genom kroppen blir 2,3 mA med torr hud och 230 mA med våt hud.')],
    '8.77': [(' Räkna med samma resistans i del c.', '')],
    '8.82': [('Ange vad som ska vara oförändrat.', 'Vad måste då vara oförändrat?')],
    '8.84': [('Bestäm kabelns sammanlagda resistans.', 'Bestäm kabelns totala resistans.'),
             ('c) Räkna med att lampans resistans är 6,0 Ω.', 'c) Lampans resistans är 6,0 Ω.')],
    '8.98': [('Ledarnas sammanlagda resistans är 0,050 Ω per km.', 'Ledarna har tillsammans resistansen 0,050 Ω per km.'),
             ('b) Bestäm strömmen i A och värmeeffekten i MW.', 'b) Bestäm strömmen och värmeeffekten i ledningen.'),
             ('Bestäm strömmen i A och värmeeffekten i MW.', 'Bestäm strömmen och värmeeffekten i ledningen.'),
             ('c) Pröva samma beräkning vid 20 kV. Ange beräknad ström i A och värmeeffekt i MW.', 'c) Gör samma beräkning vid 20 kV.'),
             ('d) Kan resultatet i c beskriva ett verkligt driftfall? Förklara.', 'd) Kan resultatet i c stämma i verkligheten? Förklara.'),
             ('Pröva samma modell med 100 MW vid 20 kV och ledningsresistansen 10 Ω. Vilka värden ger beräkningen för strömmen i A och värmeeffekten i MW? Resultatet ska granskas, inte antas vara ett möjligt driftfall.',
              'Från en kraftstation skickas 100 MW vid 20 kV genom en ledning med resistansen 10 Ω. Bestäm strömmen och värmeeffekten i ledningen.'),
             ('En överföringsmodell skickar in 100 MW men ger 250 MW som värme i ledningen. Kan detta beskriva ett verkligt driftfall?',
              'En beräkning ger att en ledning som tar emot 100 MW avger 250 MW som värme. Kan det stämma i verkligheten? Förklara.')],
    '8.103': [(', alltså har den potentialen 0 V.', '.')],
    '8.149': [(' Punkten mellan resistorerna är jordad, alltså har potentialen 0 V.', ' Punkten mellan resistorerna är jordad.')],
    '8.150': [('C är ansluten till batteriets minuspol och är vald som jordpunkt, alltså 0 V.', 'C är ansluten till batteriets minuspol och är jordad.')],
    '8.144': [('Vilka potentialer får A och B om B väljs som jordpunkt, alltså 0 V?', 'Vilka potentialer får A och B om B jordas i stället?')],
    '8.128': [('Räkna med att lampornas resistans är konstant.', 'Antag att lampornas resistans är konstant.')],
    '8.280': [(r'Hur stort arbete motsvarar en potentialskillnad på \(900\,\mathrm V\) för en laddning på \(2{,}5\,\mathrm{nC}\)? (Ange svaret i \(\mu\mathrm J\).)',
               r'En laddning på \(2{,}5\,\mathrm{nC}\) flyttas mellan två punkter med potentialskillnaden \(900\,\mathrm V\). Hur stort arbete uträttas?')],
    '8.284': [(', uttryckt i eV inklusive tecken.', ' i eV.')],
    '8.287': [(', uttryckt i eV inklusive tecken.', ' i eV.')],
    '8.290': [(', uttryckt i eV inklusive tecken.', ' i eV.')],
    '8.293': [(', uttryckt i eV inklusive tecken.', ' i eV.')],
    '8.286': [('Bestäm förändringen i elektrisk potentiell energi inklusive tecken.', 'Bestäm förändringen i laddningens elektriska potentiella energi.')],
    '8.289': [('Bestäm förändringen i elektrisk potentiell energi inklusive tecken.', 'Bestäm förändringen i laddningens elektriska potentiella energi.')],
    '8.292': [('Bestäm förändringen i elektrisk potentiell energi inklusive tecken.', 'Bestäm förändringen i laddningens elektriska potentiella energi.')],
    '8.294': [(' Potentialerna från flera laddningar adderas med sina tecken.', ''),
              (' Sätt nollnivån för potentialen i oändligheten.', '')],
    '8.316': [('Bestäm kraften på testladdningen med tecken. Riktningen åt höger är positiv.', 'Bestäm den resulterande kraften på testladdningen.')],
    '8.523': [('Hur stor är kraften efter kontakten jämfört med före? Ange kvoten kraftens storlek efter / kraftens storlek före.',
               'Hur många gånger så stor är kraften efter kontakten som före?')],
    '8.528': [('I denna uppgift räknas lampornas resistanser som konstanta.', 'Antag att lampornas resistanser är konstanta.')],
    '8.350': [('sammanlagda elektriska fältet', 'resulterande elektriska fältet')],
    '8.353': [('sammanlagda elektriska fältet', 'resulterande elektriska fältet')],
    '8.356': [('sammanlagda elektriska fältet', 'resulterande elektriska fältet')],
    '8.359': [('sammanlagda elektriska fältet', 'resulterande elektriska fältet')],
    '8.312': [('sammanlagda elektriska kraften', 'resulterande elektriska kraften')],
    '8.313': [('sammanlagda elektriska kraften', 'resulterande elektriska kraften')],
    '8.319': [('sammanlagda elektriska kraften', 'resulterande elektriska kraften')],
    '8.511': [('sammanlagda elektriska kraften', 'resulterande elektriska kraften')],
    '8.519': [('sammanlagda elektriska kraften', 'resulterande elektriska kraften'), (' (Svara i meter.)', '')],
    '8.520': [('Bestäm den sammanlagda elektriska kraftens storlek på O', 'Bestäm storleken av den resulterande elektriska kraften på O')],
    '8.402': [('Bestäm deras sammanlagda effekt.', 'Bestäm deras totala effekt.'),
              ('Vilken sammanlagd effekt utvecklas i dem?', 'Hur stor effekt utvecklas totalt i dem?')],
    '8.405': [('har sammanlagd ems 3,0 V', 'har tillsammans ems 3,0 V')],
    '8.406': [('Lampor med sammanlagd resistans 5,00 Ω', 'Lampor med ersättningsresistansen 5,00 Ω')],
    '8.423': [('Vilken blir den sammanlagda resistansen?', 'Vad blir den totala resistansen?')],
    '8.446': [('I en förenklad blixtmodell är spänningen 300 kV och strömmen 30 kA under 0,52 s. Räkna med konstanta värden under denna tid.',
               'Vid en blixt är spänningen 300 kV och strömmen 30 kA under 0,52 s. Antag att värdena är konstanta.'),
              ('c) Bestäm den sammanlagda energin under ett år.', 'c) Bestäm den totala energin under ett år.'),
              ('I en blixtmodell är spänningen 300 kV och strömmen 30 kA.', 'Vid en blixt är spänningen 300 kV och strömmen 30 kA.'),
              ('En blixtmodell har effekten 9,0 GW under 0,52 s.', 'En blixt har effekten 9,0 GW under 0,52 s.'),
              ('Varje blixt ger 4,7 GJ i en modell. Det sker 45 blixtar per sekund. Hur stor blir den sammanlagda energin under 365,25 dagar?',
               'Varje blixt ger 4,7 GJ och det sker 45 blixtar per sekund. Hur stor blir den totala energin under 365,25 dagar?')],
    '8.452': [('b) Räkna med att den energi', 'b) Antag att den energi')],
    '8.465': [('Räkna med konstant ström.', 'Antag att strömmen är konstant.')],
    '8.551': [('Du ska mäta den sammanlagda spänningen över R₁ och R₂.', 'Du ska mäta spänningen över R₁ och R₂ tillsammans.')],
    '8.574': [('Diagrammet visar den sammanlagda laddning som har passerat', 'Diagrammet visar hur stor laddning som totalt har passerat')],
    '8.575': [('Tabellen visar den sammanlagda laddning som har passerat', 'Tabellen visar hur stor laddning som totalt har passerat')],
    '8.579': [('Diagrammen visar sammanlagd laddning som har passerat', 'Diagrammen visar hur stor laddning som totalt har passerat')],
    '8.637': [(r'Grafen visar den sammanlagda laddningen \(Q\) som har passerat', r'Grafen visar hur stor laddning \(Q\) som totalt har passerat')],
    '8.597': [('Lampornas sammanlagda effekt är 10,0 W.', 'Lampornas totala effekt är 10,0 W.')],
    '8.598': [('Hur stor är den sammanlagda spänningen över lamporna?', 'Hur stor är spänningen över lamporna tillsammans?')],
    '8.374': [('En elev påstår att hon har mätt', 'Elsa påstår att hon har mätt')],
    '8.508': [('En elev mäter kraften', 'Hugo mäter kraften')],
    '8.534': [('En elev vill mäta spänningen över en lampa.', 'Maja vill mäta spänningen över en lampa.')],
    '8.546': [('En elev har kopplat in multimetern som amperemeter', 'Leo har kopplat in multimetern som amperemeter')],
    '8.547': [('En elev har kopplat in multimetern som voltmeter', 'Wilma har kopplat in multimetern som voltmeter')],
    '8.549': [('En elev vill mäta resistansen', 'Adam vill mäta resistansen')],
    '8.670': [('En elev ska mäta spänningen', 'Nora ska mäta spänningen')],
    '8.442': [('Uppskatta glödtrådens temperatur med modellen när lampan lyser.', 'Uppskatta glödtrådens temperatur när lampan lyser.')],
}
for _i, _v in [('8.451', 'vattnet'), ('8.458', 'vattnet'), ('8.459', 'vattnet'), ('8.460', 'korven'), ('8.462', 'isen')]:
    EXTRA[_i] = [(f'Räkna med att all värme går till {_v}.', f'Antag att all värme går till {_v}.')]
EXTRA.update({
    '8.47': [('En elektron går vågrätt in mitt mellan', 'En elektron går horisontellt in mitt mellan'),
             ('En elektron går vågrätt in mellan', 'En elektron går horisontellt in mellan'),
             ('Dess lodräta starthastighet är noll. Den konstanta lodräta accelerationen är', 'Den har ingen vertikal hastighet från början. Den vertikala accelerationen är'),
             ('från sin vågräta bana', 'från sin horisontella bana')],
    '8.340': [('Den elektriska kraften på en laddning är −0,0060 N med höger som positiv riktning.',
               'Den elektriska kraften på en laddad partikel är 0,0060 N åt vänster.')],
    '8.146': [('En elektron startar från vila och accelereras', 'En stillastående elektron accelereras')],
    '8.680': [('En proton startar från vila och accelereras', 'En stillastående proton accelereras')],
    '8.683': [('En elektron släpps från vila i ett elektriskt fält.', 'En stillastående elektron släpps i ett elektriskt fält.')],
    '8.492': [('Två små klot på 1,00 g vardera', 'Två små klot med massan 1,00 g vardera'),
              ('på ett friktionsfritt vågrätt bord', 'på ett friktionsfritt horisontellt bord')],
    '8.494': [('Med en vikt på 1,0 g blir den 5,0 cm lång.', 'När en vikt med massan 1,0 g hängs i den blir den 5,0 cm lång.'),
              ('på ett friktionsfritt vågrätt bord', 'på ett friktionsfritt horisontellt bord')],
    '8.732': [('lyfter en last på 8,0 kg', 'lyfter en last med massan 8,0 kg')],
})
EXTRA['8.455'] =[('Räkna med att all elenergi värmer vattnet.', 'Antag att all elenergi värmer vattnet.')]
# Fördjupningen om temperaturberoende resistans behåller formeln (den ingår inte i kursen) men utan "Använd modellen".
for _i in ('8.439', '8.440', '8.441', '8.442', '8.443', '8.444'):
    EXTRA.setdefault(_i, []).append((r'Använd modellen \(R=R_0(1+\alpha\Delta T)\), där',
                                     r'Resistansen beror på temperaturen enligt \(R=R_0(1+\alpha\Delta T)\), där'))


def texter(u):
    yield u.get('t') or ''
    yield u.get('spelIntro') or ''
    for d in u.get('spelDelar') or []:
        yield d.get('t') or ''
        yield d.get('fraga') or ''


def enheter(u):
    e = set()
    def w(x):
        if isinstance(x, list):
            [w(y) for y in x]
        elif x:
            e.add(str(x))
    w(u.get('svarEnhet'))
    for d in u.get('spelDelar') or []:
        w(d.get('svarEnhet'))
    return e


def bort(alla, fras):
    """Hitta hur frasen sitter i texten och ta bort den med rätt mellanrum eller stycke."""
    for v in (f'<p>{fras}</p>', f' {fras}', f'{fras} ', fras):
        if v in alla:
            return (v, '')
    return None


b = Bank('fy1')
R = {}
GRANSKA = []  # "(Svara i X.)" där X inte är en svarsenhet: skrivs ut för handgranskning
for u in b.arr:
    if u.get('kap') != 8:
        continue
    id_ = u['id']
    ers, kg, dkg = [], None, []
    alla = ' '.join(texter(u))
    for f in ALT:
        if f in alla:
            e = bort(alla, f)
            if e and not any(e[0] in x[0] or x[0] in e[0] for x in ers):
                ers.append(e)
    # Rester "()" från en första körning som tog bort frasen men inte parentesen.
    if ' ()' in alla:
        ers.append((' ()', ''))
    if id_ in TILL_KG:
        fr, kg, dkg = TILL_KG[id_]
        ers.append(bort(alla, fr))
    if id_ in TILL_KG_FLERA:
        frs, kg, dkg = TILL_KG_FLERA[id_]
        ers += [bort(alla, fr) for fr in frs]
    for fr in BORT.get(id_, []):
        ers.append(bort(alla, fr))
    ers += [e for e in EXTRA.get(id_, []) if e[0] in alla]
    # Övriga "(Svara i X.)" och "Svara i X." där X är en svarsenhet.
    enh = enheter(u)
    rest = alla
    for a, _ in [e for e in ers if e]:
        rest = rest.replace(a, '')
    for m in re.finditer(r'\(Svara i ([^)]*?)\.\)|(?<![(\w])Svara i ([^.<]*?)\.', rest):
        x = m.group(1) or m.group(2)
        if SYN.get(x, x) in enh:
            e = bort(alla, m.group(0))
            if e and e not in ers:
                ers.append(e)
        else:
            GRANSKA.append((id_, m.group(0), sorted(enh)))
    ers = [e for e in ers if e]
    if ers or kg:
        R[id_] = {'ers': ers}
        if kg:
            R[id_]['kg'] = kg
            if dkg:
                R[id_]['d'] = {et: {'kg': kg} for et in dkg}

if __name__ == '__main__' or os.environ.get('VISA_GRANSKA'):
    for g in GRANSKA:
        print('GRANSKA', *g)
