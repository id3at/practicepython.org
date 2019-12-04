"""
autor = id3at
Test na liczbe pierwszą
"""

while True:
    try:
        liczba = int(input("Wpisz liczbę!"))
        break
    except:
        print('Musisz podać liczbę!')


def liczPierw(liczba = 7):

    test=[[].append(t) for t in range(2, liczba) if liczba % t != 0]

    if len(test)==len(range(2, liczba)):
        return (f'"{liczba}" To liczba pierwsza!')
    else:
        return (f'"{liczba}" To nie jest liczba pierwsza!')



print(liczPierw(liczba))
