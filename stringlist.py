"""
Autor id3at
"""

#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#Exercise 6
#Ask the user for a string and print out whether this string is
#a palindrome or not. (A palindrome is a string that reads
#        the same forwards and backwards.)





NAZWA = input('Podaj słowo a sprawdzimy czy to  Palindrom: ')


if NAZWA == NAZWA[::-1]:
    print('To jest Palindrom')
else:
    print('To nie jest Palindrom')
