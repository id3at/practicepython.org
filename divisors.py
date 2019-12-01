"""
Autor id3at
"""
#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#Exercise 4
#Create a program that asks the user for a number and then prints out a list
#of all the divisors of that number. (If you don’t know what a divisor is, it
#is a number that divides evenly into another number.


while True:
    try:
        LICZBA = (int(input('Wprowadź liczbę: ')))
        DZIELNIKI = [t for t in range(1, LICZBA) if (LICZBA % t) == 0]
        print(f'To są wszystkie dzielniki liczby {LICZBA}', DZIELNIKI)
        break
    except:
        print('Liczba musi sie składać z cyfr')
