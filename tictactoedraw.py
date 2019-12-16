"""
Autor id3at
wprowadzanie wartosci 
do tablicy gry "kolkokrzyzyk' przez dwóch graczy

"""
gra = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]




print('''Gra kolko krzyzyk.
Pusta plansza\n''')

print('   0  1  2')
for x, y in  enumerate(gra):
    print(x, y)


print('''\nKrzyzyk = 1
Kolko = 2
Wprowadzanie krzyzyka polega na wybraniu 
przez gracza nr. rzedu np. "1" i nr.  kolumny np. "1".
Przykladowo wybor "11" zmieni plansze tak.
''')

print('   0  1  2')
for x, y in  enumerate(gra):
    if y[1] == 0:
        gra[1][1] = 1
    print(x, y,)
print('\n')
gra[1][1] = 0

############################################
print('Zacznijmy grę.\n')
print('   0  1  2')
for x, y in  enumerate(gra):
    print(x, y)
print('\n')


while 0 in gra[0] or 0 in gra[1] or 0 in gra[2]:
    wejscie = input('Gdzie wprowadzic krzyzyk?:  ')

    wejscieint = []
    for t in wejscie: #zamiana wejscia na liczbe
        t = int(t)
        wejscieint.append(t)

    gra[wejscieint[0]][wejscieint[1]] = 1
    print('   0  1  2')
    for x, y in  enumerate(gra):
        print(x, y)

    wejscie2 = input('Gdzie wprowadzic kolko?: ')

    wejscieint2 = []
    for t in wejscie2: #zamiana wejscia na liczbe
        t = int(t)
        wejscieint2.append(t)

    gra[wejscieint2[0]][wejscieint2[1]] = 2
    print('   0  1  2')
    for x, y in  enumerate(gra):
        print(x, y)
