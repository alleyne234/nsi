# Exercice 1

def fusion(tab1, tab2):
    """Renvoie une liste trié dans l'ordre croissant et contenant l'ensemble
    des valeurs de tab1 et tab2.

    :param list tab1: liste non vide d'entiers
    :param list tab2: liste non vide d'entiers
    :return list: liste des valeurs de tab1 et tab2 trié dans l'ordre croissant
    """
    n1 = len(tab1)
    n2 = len(tab2)
    i1 = 0
    i2 = 0
    tab_trie = []

    while i1 < n1 and i2 < n2:
        if tab1[i1] > tab2[i2]:
            tab_trie.append(tab2[i2])
            i2 = i2 + 1
        else:
            tab_trie.append(tab1[i1])
            i1 = i1 + 1

    while i1 < n1:
        tab_trie.append(tab1(tab1[i1]))
        i1 = i1 + 1

    while i2 < n2:
        tab_trie.append(tab2[i2])
        i2 = i2 + 1

    return tab_trie

assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5], "Erreur exercice 1"
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10], "Erreur exercice 1"
assert fusion([4], [2, 6]) == [2, 4, 6], "Erreur exercice 1"



# Exercice 2

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre[0]]

    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

assert traduire_romain("XIV") == 14, "Erreur exercice 2"
assert traduire_romain("CXLII") == 142, "Erreur exercice 2"
assert traduire_romain("MMXXIII") == 2023, "Erreur exercice 2"
