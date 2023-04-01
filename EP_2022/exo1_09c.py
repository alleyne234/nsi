def identity(mot, mot_a_trous):
    """Predicat qui compare les deux mots et renvoie True
    si il diffère seulement par des *, sinon False
    :mot, mot_a_trous: str
    @retrun bool
    """
    for i in range(len(mot)):
        if mot_a_trous[i] != '*' and mot_a_trous[i] != mot[i]:
            return False
    return True

print(identity('INFORMATIQUE', 'INFO*MA*IQUE'))