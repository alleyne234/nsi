# Exercice 1

def recherche(tab, n):
    """Renvoie l'indice de la dernière occurence de l'élément cherché.

    :param list tab: liste non vide de nombres entiers
    :param entier n: élément cherché dans la liste
    :return int: dernière occurence de l'élément cherché dans la liste
    """
    indice = len(tab)

    for i in range(len(tab) - 1):
        if tab[i] == n:
            indice = i

    return indice

assert recherche([5, 3], 1) == 2, "Erreur exercice 1"
assert recherche([2, 4], 2) == 0, "Erreur exercice 1"
assert recherche([2, 3, 5, 2, 4], 2) == 3, "Erreur exercice 1"



# Exercice 2

from math import sqrt   # import de la fonction racine carree

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert distance((1, 0), (5, 3)) == 5.0, "Erreur fonction distance exercice 2"
assert distance((1, 0), (0, 1)) == 1.4142135623730951, "Erreur fonction distance exercice 2"

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5),"Erreur fonction plus_courte_distance exercice 2"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)) == (5, 2),"Erreur fonction plus_courte_distance exercice 2"
