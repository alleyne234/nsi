def C(n, p):
    '''Renvoie la valeur de ligne n et de colonne p dans le triangle de Pascal.
    : n, p : (int)
    @ return (int)
    '''
    assert n >= 0 and p >= 0, 'n doit varier entre 0 et 10'
    if p == 0 or p == n:
        return 1
    else:
        return C(n - 1, p - 1) + C(n - 1, p)

def affichage_pascal():
    '''Affiche le triangle de Pascal pour 11 lignes.
    '''
    for n in range(11):
        for p in range(n + 1):
            print(C(n, p), end = ' ') # pour n donn, toute les valeurs de lignes
        print() # passage a la ligne
