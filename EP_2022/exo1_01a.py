def moyenne(tab):
    '''Correspondant à la moyenne des valeurs présentes dans le tableau.
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    '''

    if len(tab) == 0:
        return 'erreur'
    else:
        sum = 0
        for elt in tab:
            sum = sum + elt
        return sum / len(tab)
    assert moyenne([1]) == 1
    assert moyenne([1,2,3,4,5,6,7]) == 4
    assert moyenne([1,2]) == 1.5
    
#print(moyenne([1,2,3,4,5,6,7,8,9,10]))
