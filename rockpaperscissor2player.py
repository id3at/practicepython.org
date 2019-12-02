"""
Autor id3at
Gra Kamien nozyce papier.
"""
import itertools

LISTA = ['Papier', 'Kamień', 'Nożyce']
MOZLI = list(itertools.permutations(LISTA, 2))
ODP = 't'

while ODP == 't':
    try:
        print("""0 = Papier
1 = Kamień
2 = Nożyce\n""")

        WYBOR = int(input('Gracz.nr.1 Wybierz cyfrę od 0 do 2: '))

        WYBOR2 = int(input('Gracz.nr.2 Wybierz cyfrę od 0 do 2: '))


        GRA = tuple((LISTA[WYBOR], LISTA[WYBOR2]))

        print(GRA, end="\n\n")

        if GRA == MOZLI[0]:
            print('Wygrał Gracz.nr.1')
        elif GRA == MOZLI[1]:
            print('Wygrał Gracz.nr.2')
        elif GRA == MOZLI[2]:
            print('Wygrał Gracz.nr.2')
        elif GRA == MOZLI[3]:
            print('Wygrał Gracz.nr.1')
        elif GRA == MOZLI[4]:
            print('Wygrał Gracz.nr.1')
        elif GRA == MOZLI[5]:
            print('Wygrał Gracz.nr.2')
        else:
            print('Remis')
        ODP = input('Chcesz zagrać ponownie? Wcisni t, jesli nie, to wcisni cokolwiek')
    except:
        print('\nMusisz wpisać cyfre od 0 do 2\n')
