def verifie(tab):
    i = 0
    while i < len(tab) - 1:
        if tab[i] <= tab[i + 1]:
            i = i + 1
        else:
            return False
    return True
