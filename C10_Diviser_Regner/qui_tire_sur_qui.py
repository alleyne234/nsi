def quiTireSurQui(taille, tire_gauche, tire_droite, g, d):
    """Etant donné un tableau d'entiers strictement positifs tous différents,
    renvoie pour chaque élément du tableau l'indice de l'entier
    le plus grand "visible" à sa droite, ainsi qu'à sa gauche. Un élément du tableau
    ne peut pas "voir" les entiers cachés par des entiers plus grands que lui.
    Exemple :
    taille = [185, 173, 116, 54, 150, 51, 60, 180, 229, 170]
    L'élément 150 d'indice 4 verra à sa gauche 173 d'indice 1 et à sa droite
    180 d'indice 7 d'où tire_gauche[4] =  1 et tire_droite[4] = 7
    
    @param taille : tableau d'entiers strictement positifs
    @param tire_gauche, tire_droite : tableaux d'indices du tableau taille,ou None
    @param g, d : indices du tableau taille avec g <= d
    @return : tire_gauche,tire_droite
    """
    if g == d:
        return
    elif d == g + 1:
        if taille[d] > taille[g]:
            tir_droite[g] = d
        else:
            tire_gauche[d] = g
        return (tire_gauche, tire_droite)
    else:
        median = (g + d) // 2
        quiTireSurQui(taille, tire_gauche, tire_droite, g, median)
        quiTireSurQui(taille, tire_gauche, tire_droite, median + 1, d)
        fusion(taille, tire_gauche, tire_droite, g, d)



def fusion(taille, tire_gauche, tire_droite, g, d):
    """Combine les résultats obtenus lors de la phase de division
    
    @param taille : tableau d'entiers strictement positifs
    @param tire_gauche, tire_droite : tableaux d'indices du tableau taille, ou None
    @param g, d : indices du tableau taille avec g <= d
    @return : (tire_gauche, tire_droite)
    """
    m = (g + d) // 2
    i = m
    j = m + 1
    while i >= g and j <= d:
        if tite_droite[i] is None:
            if taille[i] < taille[j]:
                tire_droite[i] = j
                i = i - 1
            else:
                j = j + 1
        else:
            i = i - 1
