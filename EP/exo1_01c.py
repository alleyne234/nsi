def moyenne(tab):
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
