""" 
Autor: id3at
"""
#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Exercise 3 (and Solution)
# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that ask the user for a number and return a list that
#contains only elements from the original list a that are smaller than that
#number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


while True:
    try:
        USERNUM = int(input("Podaj liczbę: "))
        LISTA = [t for t in a if t < USERNUM]
        if len(LISTA) == 0:
            print('W liście nie ma mniejszych liczb')
        else:
            print(f'{LISTA}: to są wszystkie liczby mniejsze od podanej liczby z listy "a"')
        break
    except:
        print("Liczba musi być wpisana za pomocą cyfr i być liczbą całkowitą")
