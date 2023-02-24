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

def moyenne_c(tab):
    '''Renvoie la moyenne ponderee
    : tab : lst(tuple)
    @return float moyenne ponderee
    '''
    somme = 0
    somme_coeff = 0
    for tup in tab:
        somme = somme + tup[0] * tup[1]
        somme_coeff = somme_coeff + tup[1]
    return somme / somme_coeff

#print(moyenne_c([(15, 2), (9, 1), (12, 3)]))

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(tab_releve, tab_date):
    '''Renvoie la plus petite valeur rele
    '''
    t_mini = tab_releve[0]
    i_mini = 0
    for i in range(len(tab_releve)):
        if tab_reveve[i] < t_mini:
            t_mini = tab_releve
            