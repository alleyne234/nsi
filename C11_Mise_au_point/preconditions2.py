def max_indice(tab):
    """Renvoie l'indice du plus grand nombre
    Parameters:
        tab : (list) Liste de nombres
    Returns:
        (int) Indice plus grand nombre
    """
    max_indice = 0
    for i in range(len(tab)):
        if tab[i] > tab[max_indice]:
            max_indice = i
    return max_indice
