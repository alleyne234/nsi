# Exercice 1

def moyenne(tab):
    """Renvoie la moyenne pondérée d'une liste non vide de tuples à deux éléments de la forme
    (valeur, coefficient) où valeur et coefficient sont des nombres positifs ou nuls.

    :param list tab: liste de notes avec leur coefficient
    :return None, float: None si coefficient nul, sinon moyenne pondérée
    """
    somme_note = 0
    somme_coef = 0
    
    for valeur in tab:
        somme_note = somme_note + valeur[0] * valeur[1]
        somme_coef = somme_coef + valeur[1]

    if somme_coef == 0:
        return None
    else:
        return somme_note / somme_coef

assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142, "Erreur exercice 1"
assert moyenne([(3, 0), (5, 0)]) == None, "Erreur exercice 1"



# Exercice 2

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        des " *" , les 0 par deux espaces "  " 
        La valeur "" donnée au paramètre end permet 
        de ne pas avoir de  saut de ligne. '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)   # Ajoute k-fois l'élément à la liste
    return liste_zoom

def zoomDessin(grille, k):
    '''renvoie une grille ou les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur, 3))
