"""
Autor id3at
Gra w której komputer zgaduje pomyslaną liczbe za pomocą algorytmu, wyszukiwanie binarne.
"""

tablica = list(range(0, 101))

print('Pomysl liczbę od 1 do 100 \n')

odp = input(f'''Czy liczba wybrana jest wieksza
od liczby {tablica[(len(tablica)//2)]}, czy mniejsza?
    Jeśli wieksza wcisni,"w" jesli mniejsza wcisni "m"
    jesli program zgadl wcisni "z" by zakończyć''')


while odp != 'z':
    if odp == 'w':
        del tablica[0 : (len(tablica) // 2)]
        odp = input(f'''Czy liczba wybrana jest wieksza
        od liczby {tablica[(len(tablica)//2)]}, czy mniejsza?
    Jeśli wieksza wcisni,"w" jesli mniejsza wcisni "m"
    jesli zgadlem wcisni "z"''')


    elif odp == 'm':
        del tablica[(len(tablica) // 2):]
        odp = input(f'''Czy liczba wybrana jest wieksza
        od liczby {tablica[(len(tablica)//2)]}, czy mniejsza?
    Jeśli wieksza wcisni,"w" jesli mniejsza wcisni "m"
    jesli zgadlem wcisni "z"''')
