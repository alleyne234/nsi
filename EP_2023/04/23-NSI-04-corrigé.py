# Exercice 1

def a_doublon(tab):
    """Prend en paramètre une liste triée de nombres et renvoie True si
    la liste contient au moins deux nombres identiques, False sinon.

    :param list tab: liste de nombres triée
    :return bool: True si présence de doublon, False sinon
    """
    n = len(tab)

    if n < 2:
        return False
    
    for i in range(n - 1):
        if tab[i] == tab[i + 1]:
            return True
        
    return False

assert a_doublon([]) == False, "Erreur exercice 1"
assert a_doublon([1]) == False, "Erreur exercice 1"
assert a_doublon([1, 2, 4, 6, 6]) == True, "Erreur exercice 1"
assert a_doublon([2, 5, 7, 7, 7, 9]) == True, "Erreur exercice 1"
assert a_doublon([0, 2, 3]) == False, "Erreur exercice 1"



# Exercice 2

bombes = [(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]
grille_test = [[1, 1, 1, 0, 0], [1, -1, 1, 1, 1], [2, 2, 3, 2, -1], [1, -1, 2, -1, 3], [1, 1, 2, 2, -1]]

def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
        (ligne, colonne) en gèrant les cases sur les bords. """
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incrémente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe. """
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1: # si ce n'est pas une bombe
            grille[l][c] = grille[l][c] + 1 # on ajoute 1 à sa valeur

def génère_grille(bombes):
    """ Renvoie une grille de démineur de taille nxn où n est
        le nombre de bombes, en plaçant les bombes à l'aide de
        la liste bombes de coordonnées (tuples) passée en
        paramètre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]

    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1 # place la bombe
        incrémente_voisins(grille, ligne, colonne) # incrémente ses voisins

    return grille

assert génère_grille(bombes) == grille_test, "Erreur exercice 2"
