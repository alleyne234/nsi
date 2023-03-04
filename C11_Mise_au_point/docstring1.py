def somme(tab:list) -> int:
    """Renvoie la somme des entiers d'une liste
    """
    a = 0
    for i in range(len(tab)):
        somme = somme + tab[i]
    return somme
