def somme(liste):
    """Renvoie la somme d'une liste
    :liste: (list)
    @return (int)
    Examples:
    >>> somme([2, 4, 6, 8])
    20
    >>> somme([3, 5, 0, 2])
    10
    """
    assert len(liste) != 0, "La liste ne peut être vide" # Précondition
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
        assert somme == sum(liste[:i + 1]), "Erreur somme partielle"
    assert somme == sum(liste), "Erreur somme totale"
    return somme

import doctest
doctest.testmod()
