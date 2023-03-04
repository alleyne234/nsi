def recherche_indice_seq(tab, valeur):
    """Renvoie l'indice d'une valeur dans un tableau trié
    :tab: (list) liste triée
    :valeur: (int)
    @return (int)
    """
    for i in range(len(tab)):
        if tab[i] == valeur:
            return i
    return None
