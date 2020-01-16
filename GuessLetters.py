"""
Autor id3at
Program, losuje angielskie slowo z pliku, "sowpods". http://norvig.com/ngrams/sowpods.txt
Uzytkownik zgaduje slowo za pomoca wskazywania liter..
"""

import random

with open("sowpods.txt", "r") as txt:
    c = txt.readlines()
slow = {e: line.strip() for e, line in enumerate(c)}
slowo = slow[random.randint(0, 267750)]


tex = "_"* len(slowo)
zgad = list(tex)
slli = list(slowo)
loss = slli[:]

print(slli)
print(zgad)

while zgad != slli:
    litera = input("zgadnij litere")
    litera = litera.upper()
    if  litera in loss:
        while litera in loss:
            zgad[loss.index(litera)] = litera
            loss[loss.index(litera)] = "."
        print(zgad)
    else:
        print("Nie ma takiej litery w słowie")
        print(zgad)
