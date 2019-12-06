"""
Autor id3at
Generator hasła.
Brak limitu długosci hasla.
"""
import random


znaki = "qwertyuioplkjhgfdsazxcvbnm~!@#$%^&*()_+><?|}{[]0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
prehaslo = []

while True:
    try:
        t = int(input("Wpisz długosc generowanego hasła: "))
        break
    except:
        print('Wpisz liczbe !!!')

while t != len(prehaslo):
    prehaslo.append(random.choice(znaki))
haslo = "".join(str(xt) for xt in prehaslo)

print(haslo)
