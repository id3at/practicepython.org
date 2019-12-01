"""
Autor id3at
"""


#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#Ask the user for two numbers: one number to check (call it num) and
#one number to divide by (check). If check divides evenly into num,
#tell that to the user. If not, print a different appropriate message.




while True:
    try:
        DZIELNIK = int(input("Podaj dzielnik: "))
        DZIELNA = int(input("Podaj dzielną: "))
        if (DZIELNIK % DZIELNA) == 0:
            print('Te liczby dziela sie bez reszty, wynik dzielenia to :', DZIELNIK/DZIELNA)
        else:
            print('Te liczby dzielą sie z resztą, wynik to:', DZIELNIK/DZIELNA)
        break
    except:
        print('Wpisz liczbę!')
