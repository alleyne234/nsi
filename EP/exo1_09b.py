def occurence_lettres(phrase):
    """Renvoie un dico contenant le nombre d'occurence de chaque lettres
    :phrade: String
    @return dict
    """
    dico = {}
    for car in phrase:
        if car in dico.keys:
            dico[car] = dico[car] + 1
        else:
            dico[car] = 1
    return dico
