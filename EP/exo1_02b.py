def recherche(tab):
    """Renvoie la liste éventuellement vide des couple d'entriers consécutifs
    successifs qu'il peut y avoir dans tab.
    """
    l = []
    for i in range(len(tab) - 1):
        if tab[i + 1] == tab[i] + 1:
            l.append((tab[i], tab[i + 1]))
    return l
