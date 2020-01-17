"""
Autor id3at
Gra w wisielca.
Program, losuje angielski slowo z pliku, "sowpods".
http://norvig.com/ngrams/sowpods.txt
Uzytkownik zgaduje slowo za pomoca wskazywania liter..
Uzytkownik ma 6 prób.
Zz kazdą pomylkę dostaje cześć wisielca.
Po szesciu próbach staje sie wisielcem. :)
"""
import os
import random

with open("sowpods.txt", "r") as txt:
    c = txt.readlines()
slow = {e: line.strip() for e, line in enumerate(c)}
slowo = slow[random.randint(0, 267750)]


tex = "_"* len(slowo)
zgad = list(tex)
slli = list(slowo)
loss = slli[:]

hangman = ["head", "body", "leg left", "leg right", "arm right", "arm left"]
itero = 0
hangmangame = []

print(slli)
print(zgad)

while zgad != slli:
    litera = input("zgadnij litere")
    litera = litera.upper()
    if  litera in loss:
        while litera in loss:
            os.system('clear')

            zgad[loss.index(litera)] = litera
            loss[loss.index(litera)] = "."
        print(zgad)
        print("hangman: ", hangmangame)
        if zgad == slli:
            print("Wygrałeś, Zgadłeś słowo")
    else:
        if litera in zgad:
            os.system('clear')
            print("Ta litera już była")
            print(zgad)
        else:
            os.system('clear')
            print("Nie ma takiej litery w słowie")
            hangmangame.append(hangman[itero])
            itero += 1
            if hangman == hangmangame:
                print("hangman: ", hangmangame)
                print("koniec gry, wisielec")
                break
            print(zgad)
            print("hangman: ", hangmangame)

