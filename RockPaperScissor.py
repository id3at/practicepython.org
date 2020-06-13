"""
Autor Tomasz Głuc
Game Rock Paper and Scissors
"""
import random 
import os
gra = {('Rock', 'Rock'): "Draw", ('Rock', 'Paper'): "Paper Win!", ('Rock', 'Scissors'): "Rock Win!", ('Paper', 'Rock'): "Paper Win!", ('Paper', 'Paper'): "Draw", ('Paper', 'Scissors'): "Scissors Win!", ('Scissors', 'Rock'): "Rock Win!", ('Scissors', 'Paper'): "Scissors Win!", ('Scissors', 'Scissors'): "Draw"}

petla = "y"

while petla == "y":
    try:
        elementy = ["Rock", "Paper", "Scissors"]
        komp = random.choice(elementy)
        
        print("Game: Rock, Scissors and Paper")
        for t, e in enumerate(elementy):
            print(t, "=", e)

        uzytkownik = elementy[int(input("You Chooice: "))]
        dana = (uzytkownik, komp)
        
        for t in gra:
            if t == dana:
                print(f"You Chooise: {uzytkownik}.\nComputer Chooise: {komp}")
                if komp in gra[t]:
                    print('Computer Win')
                elif uzytkownik in gra[t]:
                    print('You Win!')
                else:
                    print(gra[t], )
        petla = input("If you want to continue press: y, if not, press: n")
        os.system('cls')
    except:
        print("Select number!")
