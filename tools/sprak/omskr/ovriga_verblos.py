"""”Funktionen \\(f(x)=…\\).” utan verb i Ma2, Ma3c och Ma5 (2026-11-23). Körs med tools/sprak/byt_falt.py
per bank: BYT väljs ur BANKER med miljövariabeln BANK."""
import os


def verblos(namn, uttryck, var='x'):
    return [(f'Funktionen \\({namn}({var})={uttryck}\\).',
             f'För funktionen \\({namn}\\) gäller att \\({namn}({var})={uttryck}\\).')]


BANKER = {
    'ma2': {'2.211': verblos('f', 'x^2-4x+3'), '2.394': verblos('h', '3x-7'), '2.400': verblos('f', '5-2x')},
    'mato1': {'3.704': verblos('A', '\\int_0^x(2t+1)\\,dt')},
    'matf1': {'3.207': verblos('f', 'x^3-9x+4'), '3.212': verblos('f', 'x^3-12x+4')},
}
BYT = BANKER[os.environ['BANK']]
