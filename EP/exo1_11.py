def xor(liste_1, liste_2):
    """Renvoie un tableau resultat de la combinaison xor des deux listes
    :liste_1, liste_2: list
    @return list
    """
    assert len(liste_1) == len(liste_2), "Les deux listes doivent avoir la même longueur."
    liste_xor = []
    for i in range(len(liste_1)):
        if liste_1[i] != liste_2[i]:
            liste_xor.append(1)
        else:
            liste_xor.append(0)
    return liste_xor
