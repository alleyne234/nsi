def nombre_de_mots(phrase):
    """Renvoie le nombre de mots dans une phrase
    :phrase: str
    @return int
    """
    liste = phrase.split(' ')
    if liste[len(liste) - 1 ] == '?' or liste[len(liste) - 1] == '!':
        return len(liste) - 1
    else:
        return len(liste)
