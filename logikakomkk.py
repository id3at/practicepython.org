"""
wstepna logika komputera gry w kolko krzyzyk
"""

gra = [['O', '…', '…'],
       ['…', 'X', '…'],
       ['X', '…', '…']]

c = [t[0] for t in gra]
d = [t[1] for t in gra]
e = [t[2] for t in gra]
przekotna1 = [gra[i][i] for i in range(3)]
przekotna2 = [gra[i][2-i] for i in range(3)]

wszy = [c,d,e]

def logikakom(x, y, z):
    zbior = []
    for l, t in enumerate(wszy):
        if gra[1][1] == '…':
            gra[1][1] = 'O'
        
        if gra[l].count(x) == 2 and gra[l].count(y) == 1:
            lic = gra[l].index(y)
            gra[l][lic] = z
            zbior.append(l)
            break
        elif t.count(x) == 2 and t.count(y) ==1:
            lic=t.index(y)
            gra[lic][l] = z
            zbior.append(l)
            break
        elif przekotna1.count(x) == 2 and przekotna1.count(y) == 1:
            lic = przekotna1.index(y)
            gra[lic][lic] = z
            zbior.append(l)
            break
        elif przekotna2.count(x) == 2 and przekotna2.count(y) == 1:
            lic = przekotna2.index(y)
            gra[lic][2-lic] = z
            zbior.append(l)
            break
        
    return zbior


logikakom('X', '…', 'O')
if len(logikakom('X', '…', 'O')) == 0:
    logikakom('O', '…', 'O')
    print(len(logikakom('X', '…', 'O')), "pierwszy")
if len(logikakom('O', '…', 'O')) == 0:
    logikakom('…', 'O', 'O')
    print(len(logikakom('O', '…', 'O')), "drugi" )
if len(logikakom('…', 'O', 'O')) == 0:
    for l, t in enumerate(wszy):
        gra[l].count('…') >= 2
        gra[l][gra[l].index('…')] = "O"
        print(len(logikakom('…', 'O', 'O')), "trzeci")
        break
       
for e,h in enumerate(gra):
    print(e,h)
