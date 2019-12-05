"""
Autor id3at
Ciag Fibonaciego
"""



while True:
    try:
        ilosc = int(input("Wpisz ile cyfr z listy Fibonacciego chcesz zobaczyć"))
        break
    except:
        print('Wpisz cyfrę')

def Fibolist(ilosc):
    """
    Ciag Fibonnaciego
    """
    c = 1
    f = 0
    lista = []
    for t in range(int(ilosc/2)):

        c = c + f
        f = f + c
        lista.append(c)
        lista.append(f)

    return lista


print(Fibolist(ilosc))
