def est_dans(value, tab):
    """Renvoie True si une valeur est présente dans un tableau, sinon False
    """
    assert len(tab) != 0, "La liste ne peut être vide"
    i = 0
    while i < len(tab):
        if tab[i] == value:
            return True
        i = i + 1
    return False
