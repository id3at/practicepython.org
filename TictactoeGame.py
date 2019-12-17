"""
Autor id3at
Gra w kolko krzyzyk
"""
import os

gra = [['…', '…', '…'],
       ['…', '…', '…'],
       ['…', '…', '…']]

print('''Gra kolko krzyzyk.
Pusta plansza\n''')

print('   0     1    2')
for x, y in  enumerate(gra):
    print(x, y)

print('''\nKrzyzyk = 1
Kolko = 2
Wprowadzanie krzyzyka polega na wybraniu 
przez gracza nr. rzedu np. "1" i nr.  kolumny np. "1".
Przykladowo wybor "11" zmieni plansze tak.
''')

print('   0     1    2')
for x, y in  enumerate(gra):
    if y[1] == '…':
        gra[1][1] = 'X'
    print(x, y,)
print('\n')
gra[1][1] = '…'

############################################
print('Zacznijmy grę.\n')
print('   0     1    2')
for x, y in  enumerate(gra):
    print(x, y)
print('\n')
##########################################################
"""
Funkcja sprawdzajaca wygraną w grze.
"""

def checttt(gra):

    c = [t[0] for t in gra]
    d = [t[1] for t in gra]
    e = [t[2] for t in gra]

    przekotna1 = [gra[i][i] for i in range(3)]
    przekotna2 = [gra[i][2-i] for i in range(3)]
    wyg  = []
    for t in range(3):
        if gra[t].count('X') == 3:
            wyg.append('2 wygral')
        elif gra[t].count('O') == 3:
            wyg.append('1 wygral')


    for s in ['X','O']:
        if c.count(s) == 3:
            wyg.append(f'{s} wygral')
        elif d.count(s) == 3:
            wyg.append(f'{s} wygrał')
        elif e.count(s) == 3:
            wyg.append(f'{s} wygrał')
        elif przekotna1.count(s) == 3:
            wyg.append(f'{s} wygrał')
        elif przekotna2.count(s) == 3:
            wyg.append(f'{s} wygrał')
    return wyg
##################################################################

"""
Funkcja pobierajaca dane od uzytkownika.
"""

def tictactoe(wejscie,wartosc):
    war = []
    os.system('clear')
    while len(war) == 0:

        wejscieint = []
        for t in wejscie: #zamiana wejscia na liczbe
            t = int(t)
            wejscieint.append(t)

        if  gra[wejscieint[0]][wejscieint[1]] == '…':
            gra[wejscieint[0]][wejscieint[1]] =  wartosc
            war.append(1)

            print('   0     1    2')
            for x, y in  enumerate(gra):
                print(x, y)


        else:
            print(f'Miejsce "{wejscie}" jest zajete, wybierz inne miejsce dla {wartosc}')
            print('   0     1    2')
            for x, y in  enumerate(gra):
                print(x, y)
            wejscie = input(f'Gdzie wprowadzić {wartosc}?: ')
##################################################################################



while ('…' in  gra[0] or '…' in gra[1] or '…' in gra[2]):
    wejscie = input('Gdzie wprowadzic "X"?ok : ')
    wartosc = 'X'
    tictactoe(wejscie, wartosc)
    if len(checttt(gra)) == 1:
        print(checttt(gra))
        break
    if ('…' not in  gra[0] and '…' not in gra[1] and '…' not in gra[2]): continue
    wejscie2 = input('Gdzie wprowadzic "O"ok? : ')
    wartosc2 = 'O'
    tictactoe(wejscie2,wartosc2)
    if len(checttt(gra)) == 1:
        print(checttt(gra))
        break
input('Koniec gry! Nacisnij Enter!')

