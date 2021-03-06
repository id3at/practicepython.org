"""
Autor id3at
Gra w kolko krzyzyk
"""
import os

gra = [['…', '…', '…'],
       ['…', '…', '…'],
       ['…', '…', '…']]
#########################################
def tablica():
    print('   0     1    2')
    for x, y in  enumerate(gra):
        print(x, y)
##########################################
print('''Gra kolko krzyzyk.
Pusta plansza\n''')
tablica()
print('''\n
Wprowadzanie krzyzyka "X" polega na wybraniu
przez gracza nr. rzedu np. "1" i nr.  kolumny np. "1".
Przykladowo wybor "11" zmieni plansze tak.
''')
print('   0     1    2')
for x, y in  enumerate(gra):
    if y[1] == '…':
        gra[1][1] = 'X'
    print(x, y)
print('\n')
gra[1][1] = '…'
##################################################################
print('Zacznijmy grę.\n')
tablica()
print('\n')
##################################################################
def checttt(gra):
    """ Funkcja sprawdzajaca wygraną w grze."""
    c = [t[0] for t in gra]
    d = [t[1] for t in gra]
    e = [t[2] for t in gra]
    przekotna1 = [gra[i][i] for i in range(3)]
    przekotna2 = [gra[i][2-i] for i in range(3)]
    wyg = []
    for t in range(3):
        if gra[t].count('X') == 3:
            wyg.append('X wygral')
        elif gra[t].count('O') == 3:
            wyg.append('O wygral')
    for s in ['X', 'O']:
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
def tictactoe(wejscie, wartosc):
    """Funkcja pobierajaca dane od uzytkownika."""
    war = []
    os.system('clear')
    while len(war) == 0:
        wejscieint = [int(t) for t in wejscie]
        if  gra[wejscieint[0]][wejscieint[1]] == '…':
            gra[wejscieint[0]][wejscieint[1]] = wartosc
            war.append(1)
            tablica()
        else:
            print(f'Miejsce "{wejscie}" jest zajete, wybierz inne miejsce dla {wartosc}')
            tablica()
            wejscie = input(f'Gdzie wprowadzić {wartosc}?: ')
##################################################################
while ('…' in  gra[0] or '…' in gra[1] or '…' in gra[2]):
    try:
        wejscie = input('Gdzie wprowadzic "X"?: ')
        wartosc = 'X'
        tictactoe(wejscie, wartosc)
        if len(checttt(gra)) == 1:
            print(checttt(gra))
            break
        if ('…' not in  gra[0] and '…' not in gra[1] and '…' not in gra[2]): continue
        wejscie2 = input('Gdzie wprowadzic "O"?: ')
        wartosc2 = 'O'
        tictactoe(wejscie2, wartosc2)
        if len(checttt(gra)) == 1:
            print(checttt(gra))
            break
    except:
        print("Prosze wpisać dwie cyfry, zlozone z liczb od 0 do 2 np '01'")
        tablica()
input('Koniec gry! Nacisnij Enter!')
