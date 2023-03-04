# Définition des fonctions
def fact(n):
    """
    Calcul et renvoie factoriel de n.
    Paramètre n : (int) un entier positif
    Valeur renvoyée : (int) la factorielle de n.

    Exemples :
    >>> fact(3)
    6
    >>> fact(5)
    120
    """
    assert n >= 0 , 'n doit positif'
    
    if n == 0:
        return 0
    else:
        resultat = 1
        while n > 0:
            resultat = resultat * n
            n = n - 1
    return resultat

# Programme principal
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
    assert fact(0) == 0
    assert fact(1) == 1
    assert fact(3) == 6
    print("Tous les tests sont ok")
