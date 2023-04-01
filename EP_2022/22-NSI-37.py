urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit']

def depouille(urne):
    resultat = {}   # ou dict
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:   # ou election.keys()
        if election[candidat] > nmax :
            nmax = candidat
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == ...]
    return depouille()


