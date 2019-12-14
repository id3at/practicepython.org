"""
Autor id3at
Program sprawdzajacy kto wygral w kolko krzyzyk
"""




lista = [[0, 1, 2],
         [2, 2, 1],
         [1, 1, 1]]

c = [t[0] for t in lista]
d = [t[1] for t in lista]
e = [t[2] for t in lista]

przekotna1 = [lista[i][i] for i in [0, 1, 2]]
przekotna2 = [lista[i][2-i] for i in [0, 1, 2]]

for t in range(3):
    if lista[t].count(2) == 3:
        print('2 wygral')
    elif lista[t].count(1) == 3:
        print('1 wygral')
for s in range(1, 3):
    if c.count(s) == 3:
        print(f'{s} wygral')
    elif d.count(s) == 3:
        print(f'{s} wygrał')
    elif e.count(s) == 3:
        print(f'{s} wygrał')
    elif przekotna1.count(s) == 3:
        print(f'{s} wygrał')
    elif przekotna2.count(s) == 3:
        print(f'{s} wygrał')
