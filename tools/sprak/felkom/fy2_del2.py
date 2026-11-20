# Felkommentarer, Fy2 del 2: stavmagnet, kraft på laddade partiklar, ljus, ljud och astronomi (2026-11-20).
R = ['höger', 'vänster', 'uppåt', 'nedåt', 'in', 'ut']
MOT = {'höger': 'vänster', 'vänster': 'höger', 'uppåt': 'nedåt', 'nedåt': 'uppåt', 'in': 'ut', 'ut': 'in'}
LANGS = {'horisontell': ('höger', 'vänster'), 'vertikal': ('uppåt', 'nedåt')}
I_BILDEN = 'Kompassen ligger i bildens plan och pekar längs fältet där.'


def magnet(axel, typ, ratt):
    """Kompass vid en stavmagnet. typ: 'N' = bortom nordpolen, 'S' = bortom sydpolen, 'sida' = vid magnetens mitt."""
    langs = LANGS[axel]
    if typ == 'N':
        mot = 'Fältlinjerna går ut från nordpolen, så bortom N pekar fältet bort från magneten.'
        tvars = 'P ligger på magnetens axel, så fältet pekar längs axeln.'
    elif typ == 'S':
        mot = 'Fältlinjerna går in i sydpolen, så bortom S pekar fältet mot magneten.'
        tvars = 'P ligger på magnetens axel, så fältet pekar längs axeln.'
    else:
        mot = 'Utanför magneten går fältlinjerna från N till S. Vid magnetens mitt pekar fältet därför från N mot S.'
        tvars = 'Vid magnetens mitt är fältet parallellt med magneten, inte riktat mot den eller bort från den.'
    ut = []
    for r in R:
        if r == ratt:
            ut.append(None)
        elif r in ('in', 'ut'):
            ut.append(I_BILDEN)
        elif r in langs:
            ut.append(mot)
        else:
            ut.append(tvars)
    return ut


def partikel(fart, falt, positiv, ratt):
    ut = []
    for r in R:
        if r == ratt:
            ut.append(None)
        elif r in (fart, MOT[fart]):
            ut.append('Kraften är vinkelrät mot rörelseriktningen.')
        elif r in (falt, MOT[falt]):
            ut.append('Kraften är vinkelrät mot magnetfältet.')
        elif positiv:
            ut.append('Kraften pekar åt motsatt håll. Kontrollera med högerhandsregeln.')
        else:
            ut.append('Det är riktningen för en positiv laddning. För en negativ laddning blir kraften motsatt.')
    return ut


N1 = 'Övergångar till n = 1 ger störst energi, eftersom de lägsta nivåerna ligger längst ifrån varandra.'
VIT_DVARG = 'Vita dvärgar är heta men ljussvaga. De ligger nere till vänster i diagrammet.'
K = {
    # ---------- kompass vid stavmagnet ----------
    '3.231': magnet('horisontell', 'sida', 'höger'),
    '3.232': magnet('horisontell', 'sida', 'höger'),
    '3.233': magnet('horisontell', 'S', 'höger'),
    '3.234': magnet('horisontell', 'N', 'höger'),
    '3.235': magnet('horisontell', 'sida', 'vänster'),
    '3.236': magnet('horisontell', 'sida', 'vänster'),
    '3.237': magnet('vertikal', 'N', 'uppåt'),
    '3.238': magnet('vertikal', 'S', 'uppåt'),
    '3.239': magnet('vertikal', 'sida', 'nedåt'),
    '3.240': magnet('vertikal', 'sida', 'nedåt'),
    # ---------- kraft på laddade partiklar ----------
    '3.173': partikel('höger', 'ut', True, 'nedåt'),
    '3.174': partikel('uppåt', 'ut', True, 'höger'),
    '3.175': partikel('vänster', 'in', True, 'nedåt'),
    '3.176': partikel('nedåt', 'in', True, 'höger'),
    '3.177': partikel('höger', 'ut', False, 'uppåt'),
    '3.178': partikel('uppåt', 'ut', False, 'vänster'),
    '3.179': partikel('vänster', 'in', False, 'uppåt'),
    '3.180': partikel('nedåt', 'in', False, 'vänster'),
    '3.181': partikel('ut', 'höger', True, 'uppåt'),
    '3.182': partikel('in', 'uppåt', False, 'vänster'),
    '3.183': partikel('höger', 'uppåt', True, 'ut'),
    '3.184': partikel('nedåt', 'vänster', False, 'ut'),
    '3.419': [None, 'Strömmen går åt andra hållet. Kontrollera med högerhandsregeln för laddningarna i staven.',
              'Kretsens area växer hela tiden, så flödet ändras och det induceras en ström.',
              'Staven rör sig hela tiden åt samma håll, så strömmen byter inte riktning.'],
    '3.302': ['Fler varv ökar fältet, och det tar ut halveringen av strömmen.',
              'Strömmen halveras samtidigt som antalet varv fördubblas.',
              None,
              'Fältet är proportionellt mot antalet varv gånger strömmen: 2 · 0,5 = 1.'],
    # ---------- ljus, ljud och atomer ----------
    '4.307': [None, 'Strålen går bara rakt fram när den träffar ytan vinkelrätt.',
              'Vid en vinkel större än gränsvinkeln går ingen stråle ut i luften alls.',
              'Ljuset stannar inte. Det reflekteras tillbaka in i glaset.'],
    '4.313': [N1, N1, None, N1],
    '4.316': ['Radiovågor har lägst frekvens, och infrarött ligger före synligt ljus.',
              'Ordningen är omvänd, från högst till lägst frekvens.',
              'Mikrovågor har lägre frekvens än infrarött.', None],
    '2.301': [None, 'Människan hör ungefär 20–20 000 Hz, så 15 Hz är för lågt.',
              'Ultraljud har frekvenser över 20 000 Hz.', 'Ljud är mekaniska vågor, inte elektromagnetisk strålning.'],
    # ---------- kosmologi ----------
    '5.51': [None, None, 'Big Crunch är en kollaps. Bara Big Freeze handlar om ett kallt universum.', None],
    '5.301': ['Expansionen accelererar, den bromsar inte in.', None,
              'Galaxerna rör sig bort från varandra, inte mot oss.', 'Universum expanderar fortfarande.'],
    '5.302': [None, 'Massan är densamma men volymen växer, så tätheten minskar.',
              'Massan är densamma men volymen växer, så tätheten minskar.', 'Tätheten minskar gradvis, den blir inte noll direkt.'],
    '5.303': ['Big Crunch är en kollaps.', None, 'Big Bang beskriver universums början.',
              'Solvind är partiklar som strömmar från solen.'],
    '5.304': ['Stjärnornas färg avgör inte universums framtid.', 'Ljusets hastighet är konstant.', None,
              'Värdet på Hubbles konstant i dag avgör inte om expansionen vänder.'],
    '5.305': ['Mörk energi påverkar inte ljusets färg.', 'Mörk energi märks på mycket stora avstånd, inte i planetsystem.',
              'Mörk energi finns i hela rymden.', None],
    '5.306': [None, 'Galaxgrupper som inte hålls ihop av gravitationen glider isär när universum expanderar.',
              'Avståndet ökar när universum expanderar.', 'Galaxgrupper som inte hålls ihop av gravitationen följer med expansionen.'],
    '5.307': ['Universum blir kallare, inte varmare.', None, 'Det handlar om en mycket långsam utveckling.',
              'Gravitationen finns kvar.'],
    '5.308': ['Krökningen är inte ensam avgörande. Mörk energi spelar stor roll.', 'Stjärnorna är en liten del av universums innehåll.',
              None, 'En enda galax säger för lite om hela universum.'],
    '5.309': ['Pulsarer bildas av mycket tyngre stjärnor.', 'Neutronstjärnor bildas av mycket tyngre stjärnor.',
              'Svarta hål bildas av de allra tyngsta stjärnorna.', None],
    '5.310': ['Mycket massiva stjärnor exploderar som supernovor.', 'En stjärna blir aldrig en planet.', None,
              'Fusionen pågår i miljoner år, inte en dag.'],
    '5.311': ['Temperaturen visas på den vågräta axeln.', 'Temperaturen minskar åt höger.', 'Den lodräta axeln visar luminositeten.', None],
    '5.312': [None, 'En sval och liten stjärna skulle vara ljussvag.', 'En stjärna har alltid en radie.',
              'Luminositeten beror på både temperatur och radie.'],
    '5.313': ['En vit dvärg har ungefär lika stor massa som solen.', None,
              'Vita dvärgar är ljussvaga även utan stoft.', 'Vita dvärgar sänder ut mycket synligt ljus och ultraviolett ljus.'],
    '5.314': [None, 'Solen är ingen superjätte.', 'Solen är inte en vit dvärg ännu.', 'Solen ligger mitt på huvudserien.'],
    '5.315': ['Massiva stjärnor har fusion, mycket kraftig sådan.', None, 'Huvudseriestjärnor fusionerar väte.',
              'Massiva huvudseriestjärnor är de hetaste.'],
    '5.324': ['Längst upp betyder ljusstark och till vänster betyder varm.', 'Längst upp betyder ljusstark, inte ljussvag.',
              'Till vänster betyder varm, inte kall.', None],
    '5.325': ['Expansionen accelererar, den bromsar inte in.', 'Galaxerna fortsätter att glida isär.', None,
              'Inget tyder på att expansionen växlar mellan att öka och minska.'],
    '5.369': [None, 'Under huvudserien fusioneras väte, och det sker i kärnan.',
              'Stjärnans tyngd balanseras av fusionen. Den drar inte ihop sig hela tiden.',
              'Järnfusion ger ingen energi. Den sker inte på huvudserien.'],
    '5.370': [VIT_DVARG, VIT_DVARG, VIT_DVARG, None],
    '5.373': ['2,0 solmassor är mer än 1,4 solmassor, den största massan en vit dvärg kan ha.', None,
              '2,0 solmassor är mindre än 3 solmassor, så det blir inget svart hål.',
              'En röd jätte är en stjärna, inte en kollapsad kärna.'],
}
