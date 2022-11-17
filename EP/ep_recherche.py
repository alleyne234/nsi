def recherche_a(tab, n):
    """Renvoie l'indice de la dernière occurence de l'élément n cherché.
    Si l'élément n'est pas présent, la fonction renvoie la longueur du tableau.
    : tab : (list)
    : n : (int)
    @ return indice ou longueur du tableau
    """
    i = len(tab) - 1
    while i >= 0:
        if tab[i] == n:
            return i
        else:
            i = i - 1
    return len(tab)
    
#print(recherche_a([2, 4, 2], 4))

def recherche_b(tab):
    """Renvoie la liste éventuellement vide des couple d'entriers consécutifs
    successifs qu'il peut y avoir dans tab.
    """
    l = []
    for i in range(len(tab) - 1):
        if tab[i + 1] == tab[i] + 1:
            l.append((tab[i], tab[i + 1]))
    return l
