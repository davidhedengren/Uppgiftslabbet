"""Handgranskning av Ma1 kapitel 7, del 2: spill, kostnader, säkerhetsmarginaler, yrkesformler, yrkesverktyg (2026-11-20).

Telegramstil ("Rabatt i kr?", "Total?") blir hela frågor, "I ett räkneexempel …" och "förenklad/idealiserad modell"
får vardagliga formuleringar, fältinstruktioner ("i varsitt fält") flyttas till kgInstruktion.
"""
R = {
    '7.19': {'ers': [('Företag A: 950 kr start + 410 kr/h. B: 520 kr/h utan start. När kostar de lika?',
                      'Företag A tar 950 kr i startavgift och 410 kr per timme. Företag B tar 520 kr per timme och ingen startavgift. Efter hur många timmar kostar de lika mycket?')]},
    '7.20': {'ers': [('Kostnad för 14,5 m²?', 'Vad kostar 14,5 m²?')]},
    '7.84': {'ers': [('Pris 4200 kr före 8 % rabatt.', 'En vara kostar 4 200 kr. Du får 8 % rabatt.'),
                     ('a) Rabatt i kr?', 'a) Hur många kronor är rabatten?'), ('b) Pris efter rabatt?', 'b) Vad kostar varan efter rabatten?'),
                     ('>Rabatt i kr?<', '>Hur många kronor är rabatten?<'), ('>Pris efter rabatt?<', '>Vad kostar varan efter rabatten?<')]},
    '7.171': {'ers': [('Ett jobb kräver 7 h à 480 kr och material 2350 kr.', 'Ett jobb tar 7 timmar och timpriset är 480 kr. Materialet kostar 2 350 kr.'),
                      ('a) Arbetskostnad?', 'a) Vad kostar arbetet?'), ('b) Total?', 'b) Vad blir den totala kostnaden?'),
                      ('c) Total om materialet får 10 % rabatt?', 'c) Vad blir den totala kostnaden om du får 10 % rabatt på materialet?'),
                      ('>Arbetskostnad?<', '>Vad kostar arbetet?<'), ('>Total?<', '>Vad blir den totala kostnaden?<'),
                      ('>Total om materialet får 10 % rabatt?<', '>Vad blir den totala kostnaden om du får 10 % rabatt på materialet?<')]},
    '7.23': {'ers': [('I en förenklad modell minskar vattnets övertryck med 1 bar för varje 10 meters höjdökning.',
                      'Vattnets övertryck i en ledning minskar med ungefär 1 bar för varje 10 meter uppåt.')]},
    '7.173': {'ers': [('I ett räkneexempel innehåller varje tablett 500 mg.', 'Varje tablett innehåller 500 mg av ett läkemedel.')]},
    '7.56': {'ers': [('I ett räkneexempel ska en mängd på 375 mg motsvaras av tabletter som innehåller 250 mg vardera och kan delas i två lika delar. Vilket antal ger rätt mängd?',
                      'En patient ska få 375 mg av ett läkemedel. Tabletterna innehåller 250 mg vardera och kan delas mitt itu. Hur många tabletter ska patienten få?')]},
    '7.64': {'ers': [('En idealiserad rördragning ska', 'En rördragning ska'), ('Böjarnas egna längder försummas.', 'Bortse från böjarnas längd.')]},
    '7.80': {'ers': [('Anta att volymerna', 'Antag att volymerna')]},
    '7.458': {'ers': [('Med 8 % spill, hur många m² behövs?', 'Man räknar med 8 % spill. Hur många m² matta behövs?')]},
    '7.54': {'ers': [(' Ange timmar och minuter i varsitt fält.', '')], 'kg': 'Ange timmar och minuter i varsitt fält.'},
    '7.39': {'ers': [(' Ange klockslagets timmar och minuter i varsitt fält.', '')], 'kg': 'Ange klockslagets timmar och minuter i varsitt fält.'},
    '7.35': {'ers': [('I ett räkneexempel om läkemedelsberäkning är en dos 15 mg per kg kroppsvikt. Personen väger 22 kg och lösningens koncentration är 24 mg/ml. En given beräkningsgräns är 60 mg per kg under ett dygn. Bestäm volymen för en dos och det största hela antalet sådana doser inom gränsen.',
                      'En patient ska få 15 mg av ett läkemedel per kg kroppsvikt i varje dos. Patienten väger 22 kg och lösningen innehåller 24 mg/ml. Under ett dygn får patienten högst få 60 mg per kg kroppsvikt. Bestäm volymen för en dos och det största antalet hela doser som får ges under ett dygn.')]},
    '7.52': {'ers': [('I ett räkneexempel ges dropphastigheten av', 'Dropphastigheten för ett dropp ges av')]},
    '7.467': {'ers': [('En elev beräknar', 'Moa beräknar')]},
    '7.85': {'ers': [(' Ange talen i varsitt fält.', '')], 'kg': 'Ange minuterna och sekunderna i varsitt fält.'},
}
