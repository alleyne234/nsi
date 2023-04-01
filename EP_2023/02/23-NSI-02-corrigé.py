# Exercice 1

def indices_maxi(tab):
    """Prend en paramètre une liste tab non vide de nombres entiers et renvoie
    un couple donnant d'une part le plus grand élément de cette liste et d'autre part 
    la liste des indices de la liste tab où apparaît ce plus grand élément.

    :param list tab: liste de nombres entiers
    :return int, list: valeur maximale et indices où elle apparaît
    """
    indices_max = []
    valeur_max = tab[0]
    n = len(tab)

    for i in range(1, n):   # Cherche la plus grande valeur de la liste
        if tab[i] > valeur_max:
            valeur_max = tab[i]
            
    for i in range(n):   # Cherche tous les indices où la plus grande valeur apparaît
        if tab[i] == valeur_max:
            indices_max.append(i)
            
    return valeur_max, indices_max

assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8]), "Erreur exercice 1"
assert indices_maxi([7]) == (7, [0]), "Erreur exercice 1"



# Exercice 2

def positif(pile):
    pile_1 = list(pile)   # Fait une copie indépendante de la pile 1
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9], "Erreur exercice 2"
