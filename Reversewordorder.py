"""
Autor id3at
Rewers łancucha znaków
"""


lancuch = input('Wprowadz łancuch znaków: ')



def reversstr(lancuch):
    """
    rewers łancucha znaków
    """
    p = lancuch.rsplit()
    c = p[::-1]
    d = " ".join(c)
    return d.capitalize()

print(reversstr(lancuch))
