# 2026-11-20: deluppgifter som blivit likadana på papper (Fy1 5.45, 5.71) och en dubblerad
# "Stämmer påståendet?" i Ma1 5.190 och 5.193 (ma1_korrelation.py kördes två gånger).
# Körs: SPRAKBANK=fy1 … apply.py fy1, SPRAKBANK=ma1 … apply.py ma1
import os
BANK = os.environ.get('SPRAKBANK', 'fy1')
FAGEL = '<li>Hur stor lägesenergi har fågeln, räknat från marken?</li>'
VASKA = '<li>Hur stor lägesenergi har väskan, räknat från golvet?</li>'
DUBB = '<p>Stämmer påståendet?</p><p>Stämmer påståendet?</p>'
ALLA = {
    'fy1': {
        '5.45': {'ers': [(FAGEL + FAGEL, '<li>Hur stor lägesenergi har fågeln på 15 m höjd, räknat från marken?</li>'
                          '<li>Hur stor lägesenergi har fågeln på 30 m höjd, räknat från marken?</li>')]},
        '5.71': {'ers': [(VASKA + VASKA, '<li>Hur stor lägesenergi har väskan när den står på golvet?</li>'
                          '<li>Hur stor lägesenergi har väskan när den står på bordet, räknat från golvet?</li>')]},
    },
    'ma1': {
        '5.190': {'ers': [(DUBB, '<p>Stämmer påståendet?</p>')]},
        '5.193': {'ers': [(DUBB, '<p>Stämmer påståendet?</p>')]},
    },
}
R = ALLA[BANK]
