"""
Autor id3at
Gra Krowa i byk.
Zgadnij czterocyfrowa liczbę
"""

import random

liczba = random.randint(1000, 9999)
liczba = (list(str(liczba)))
zgadliczba = ""
cow = []
bull = []
ilosc = []
print('Komputer wylosował, liczbę czterocyfrową. Sprubuj zgadnąć, jaka to liczba')
print('''Jesli w twojej liczbie jest cyfra taka sama, jak w liczbie wylosowanej
i znajduje sie ona  na tym samym miejscu, dostajesz "cow", 
Jeśli w twojej liczbie jest cyfra taka sama jak w wylosowanej liczbie,
ale nie na tym samym miejscu dostajesz "bull" \n ''')


while liczba != zgadliczba:
    try:
        liczba2 = list(liczba)
        zgadliczba = list(input('Wpisz czterocyfrową liczbę: '))
        zgadliczb2 = list(zgadliczba)
        cows = list(cow)
        bulls = list(bull)
        ilosc.append(zgadliczba)
        for x, t in enumerate(liczba):
            if t == zgadliczba[x]:
                cows.append(zgadliczba[x])
        if len(cows) != 0:
            for z in cows:
                liczba2.remove(z)
                zgadliczb2.remove(z)
        for n, m in enumerate(zgadliczb2):
            if m in liczba2 and m != liczba2:
                bulls.append(zgadliczb2[n])
                liczba2.remove(m)
        print(f'{len(cows)} cow,   {len(bulls)} bull')
        if liczba == zgadliczba:
            print(f"Zgadłeś za {len(ilosc)} razem!! Liczba wylosowana to {liczba}")
    except:
        print('Liczba powinna się skladac z czterech cyfr')
