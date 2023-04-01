def max_dico(dico):
    """Renvoie le nom et le nombre de like de la personne avec le plus de like
    :dico: dict
    @return tuple (str, int)
    """
    max_value = 0
    name_max_like = "None"
    for key in dico.keys():
        if dico[key] > max_value:
            max_value = dico[key]
            max_key = key
    return (max_key, max_value)
