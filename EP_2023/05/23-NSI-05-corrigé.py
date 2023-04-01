# Exercice 1

from random import randint

def lancer(n):
    """Renvoie une liste de n entiers obtenus aléatoirement entre 1 et 6.

    :param int n: nombre de valeur pour le tableau
    :return list: liste de nombres aléatoire compris entre 1 à 6
    """
    liste_lancer = []

    for _ in range(n):
        liste_lancer.append(randint(1, 6))

    return liste_lancer


def paire_6(tab):
    """Renvoie True si le nombre de 6 est supérieur ou égal à 2, False sinon.

    :param list tab: liste de nombres entiers compris entre 1 et 6
    :return bool: True ou False
    """
    nombre_6 = 0

    for valeur in tab:
        if valeur == 6:
            nombre_6 = nombre_6 + 1
    
    return nombre_6 >= 2

assert paire_6([5, 6, 6, 2, 2]) == True, "Erreur exercice 1"
assert paire_6([6, 5, 1, 6, 6]) == True, "Erreur exercice 1"
assert paire_6([2, 2, 6]) == False, "Erreur exercice 1"
assert paire_6([]) == False, "Erreur exercice 1"



# Exercice 2

img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

assert nbLig(img) == 4, "Erreur exercice 2"
assert nbCol(img) == 5, "Erreur exercice 2"
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]], "Erreur exercice 2"
assert binaire(img, 120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]
