premiers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]

def rechercher(x, T, debut, fin):
    """ Renvoie l'indice de x, entre debut et fin, dans le
    tableau trié dans l'ordre croissant T, et -1 sinon."""
    milieu = (debut + fin) // 2
    if debut > fin:
        return -1
    else:
        if x == T[milieu]:
            return milieu
        elif x < T[milieu]:
            return rechercher(x, T, debut, milieu - 1)
        else:
            return rechercher(x, T, milieu + 1, fin)
    
def indice(x, L):
    return rechercher(x, L, 0, len(L) - 1)
    
print(indice(19, premiers))

print(indice(51, premiers))
