def liczPierw(liczba=7):

    przedział = int(liczba ** 0.5 + 1)
    zbior = [t for t in range(2, przedział) if liczba % t == 0]
    
    if len(zbior) >= 1:
        return(f"Liczba {liczba}, nie jest liczba pierwsza")
    else:
        return(f"Liczba {liczba}, jest liczba pierwsza")

print(liczPierw())
