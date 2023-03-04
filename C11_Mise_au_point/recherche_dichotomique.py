def recherche_dicho(tab, valeur, gauche, droite):
    """Renvoie l'indice d'une valeur dans un tableau trié
    :tab: (list) liste triée
    :valeur: (int)
    @return (int)
    """
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite:
        milieu= (gauche + droite) // 2
        if valeur < tab[milieu]:
            droit = milieu - 1
        elif valeur == tab[milieu]:
            return milieu
        else:
            gauche = milieu + 1
        return milieu
