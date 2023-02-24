def recherche(caractere, mot):
    """Renvoie le nombre d'occurences du caracteres dans le mot
    :caractere: char
    :mot: str
    @return int
    """
    occurences = 0
    for car in mot:
        if caractere == car:
            occurences = occurences + 1
    return occurences
