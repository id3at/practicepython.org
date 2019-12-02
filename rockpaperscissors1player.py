"""
Autor id3at
Gra Kamien nozyce papier.
"""
import random
import itertools

LISTA = ['Papier', 'Kamień', 'Nożyce']
MOZLI = list(itertools.permutations(LISTA, 2))
ODP = 't'

while ODP == 't':
    try:
        print("""0 = Papier
1 = Kamień
2 = Nożyce\n""")

        WYBOR = int(input('Wybierz cyfrę od 0 do 2: '))

        LOS = random.choice(LISTA)

        GRA = tuple((LISTA[WYBOR], LOS))

        print(GRA, end="\n\n")

        if GRA == MOZLI[0]:
            print('Wygrałes')
        elif GRA == MOZLI[1]:
            print('Przegrałeś')
        elif GRA == MOZLI[2]:
            print('Przegrałeś')
        elif GRA == MOZLI[3]:
            print('Wygrałeś')
        elif GRA == MOZLI[4]:
            print('Wygrałeś')
        elif GRA == MOZLI[5]:
            print('Przegrałeś')
        else:
            print('Remis')
        ODP = input('Chcesz zagrać ponownie? Wcisni t, jesli nie, to wcisni cokolwiek')
    except:
        print('\nMusisz wpisać cyfre od 0 do 2\n')
