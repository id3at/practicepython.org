"""
wstepna logika komputera gry w kolko krzyzyk
"""

gra = [['X', 'O', 'X'],
       ['…', '…', '…'],
       ['…', '…', '…']]

c = [t[0] for t in gra]
d = [t[1] for t in gra]
e = [t[2] for t in gra]
przekotna1 = [gra[i][i] for i in range(3)]
przekotna2 = [gra[i][2-i] for i in range(3)]

wszy = [c,d,e]

for l, t in enumerate(wszy):
    if gra[l].count('X') == 2 and gra[l].count('…') == 1:
        lic = gra[l].index('…')
        gra[l][lic] = "O"
        break
    elif t.count("X") == 2 and t.count('…') ==1:
        lic=t.index('…')
        gra[lic][l] = "O"
        break
    elif przekotna1.count("X") == 2 and przekotna1.count('…') == 1:
        lic = przekotna1.index('…')
        gra[lic][lic] = "O"
        break
    elif przekotna2.count("X") == 2 and przekotna2.count('…') == 1:
        lic = przekotna2.index('…')
        gra[lic][2-lic] = "O"
        break
 
for l, t in enumerate(wszy):
    if gra[l].count('…') == 2 and gra[l].count('O') == 1:
        lic = gra[l].index('…')
        gra[l][lic] = "O"
        break
    elif t.count('…') == 2 and t.count('O') == 1:
        lic=t.index('…')
        gra[lic][l] = "O"
        break
    elif przekotna1.count('…') == 2 and przekotna1.count('O') == 1:
        lic = przekotna1.index('…')
        gra[lic][lic] = "O"
        break
    elif przekotna2.count('…') == 2 and przekotna2.count('O') == 1:
        lic = przekotna2.index('…')
        gra[lic][2-lic] = "O"
        break

"""
elif gra[l].count('…') >= 2:
    gra[l][gra[l].index('…')] = "O"
    break

"""
for e,h in enumerate(gra):
    print(e,h)


for e,h in enumerate(gra):
    print(e,h)


    
