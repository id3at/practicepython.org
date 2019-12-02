"""
Autor id3at
Gra: Jaka to liczba?
"""

import random

ILOSC = []
LICZBA = random.randrange(1, 10)
ZGAD = int()



while ZGAD != LICZBA:
    try:
        ZGAD = int(input("Pomyślałem liczbę od 1 do 10, zgadnij jaka to jest liczba"))
        ILOSC.append(ZGAD)
        if ZGAD > LICZBA:
            print('Ta liczba jest za duża')
        elif ZGAD < LICZBA:
            print('Ta liczba jest za mała')
        else:
            print(f'Zagadłeż za {len(ILOSC)} razem, liczba która pomyslałem to {LICZBA}')
    except:
        print('Wprowadź cyfrę')
