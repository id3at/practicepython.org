"""
Autor id3at
Generator hasła.
Brak limitu długosci hasla.
"""
import random
import string


znaki = [t for t in string.printable if t not in "\t, ' ', '\n', '\r', '\x0b', '\x0c'"]
prehaslo = []

while True:
    try:
        t = int(input("Wpisz długosc generowanego hasła: "))
        break
    except Exception:
        print('Wpisz liczbe !!!')

while t != len(prehaslo):
    prehaslo.append(random.choice(znaki))
haslo = "".join(prehaslo)

print(haslo)
