# Exercice 1

def multiplication(n1, n2):
    """Renvoie le produit de n1 par n2.

    :param int n1: nombre entier
    :param int n2: nombre entier
    :return int: produit de n1 par n2
    """
    somme = 0

    if n1 == 0 or n2 == 0:
        return 0
    
    if n1 < 0:
        return -multiplication(-n1, n2)

    if n2 < 0:
        return -multiplication(n1, -n2)
    
    for i in range(n2):
        somme = somme + n1
    
    return somme

assert multiplication(3, 5) == 15, "Erreur exercice 1"
assert multiplication(-4, -8) == 32, "Erreur exercice 1"
assert multiplication(-2, 6) == -12, "Erreur exercice 1"
assert multiplication(-2, 0) == 0, "Erreur exercice 1"



# Exercice 2

# -*- coding: utf-8 -*-

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m + 1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m - 1)
    else:
        return m

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None, "Erreur exercice 2"
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None, "Erreur exercice 2"
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4, "Erreur exercice 2"
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2, "Erreur exercice 2"
