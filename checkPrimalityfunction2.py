"""
autor = id3at
Test na liczbe pierwszą
Szybszy
"""

while True:
    try:
        liczba = int(input("Wpisz liczbę!"))
        break
    except:
        print('Musisz podać liczbę!')


def liczPierw(liczba = 7):

    test = [[].append(t) for t in range(1, liczba+1) if liczba % t == 0]

    if len(test) == 2:
        return f'"{liczba}" To liczba pierwsza!'
    else:
        return f'"{liczba}" To nie jest liczba pierwsza!'



print(liczPierw(liczba))
