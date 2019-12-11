"""
Autor id3at
Rewers zdan
"""


lancuch = input('Wprowadz zdanie: ')



def reversstr(lancuch):
    """
    rewers zdań
    """
    p = lancuch.rsplit()
    c = p[::-1]
    d = " ".join(c)
    return d.capitalize()

print(reversstr(lancuch))
