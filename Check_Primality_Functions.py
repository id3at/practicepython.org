liczba = 8

def liczPierw(liczba):

    przedział = int(liczba ** 0.5 + 1)
    zbior = []
    for t in range(2, przedział):
        if liczba % t == 0:
            zbior.append(t)
            
    
    if len(zbior) >= 1:
        return(f"Liczba {liczba}, nie jest liczba pierwsza")
    else:
        return(f"Liczba {liczba}, jest liczba pierwsza")

print(liczPierw(liczba))
