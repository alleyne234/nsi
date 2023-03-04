def somme(liste:list) -> int:
    """Renvoie la somme d'une liste
    :liste: (list)
    @return (int)
    Examples:
    >>> somme([2, 4, 6, 8])
    20
    >>> somme([3, 5, 0, 2])
    10
    """
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
    return somme

def test():
    assert somme([2, 4, 6, 8]) == 10, "Erreur"
    