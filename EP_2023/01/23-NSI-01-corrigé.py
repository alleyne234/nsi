# Exercice 1

def verifie(tab):
    """Prend en paramètre un tableau de valeurs numériques non vide et
    renvoie True si ce tableau est trié dans l'ordre croissant, False sinon.

    :param list tab: Liste de nombres numériques non vide.
    :return bool: Renvoie True ou False
    """
    valeur_max = tab[0]
    for nombre in tab:
        if valeur_max <= nombre:
            valeur_max = nombre
        else:
            return False
    return True

assert verifie([0, 5, 8, 8, 9]) == True, "Erreur exercice 1"
assert verifie([8, 12, 4]) == False, "Erreur exercice 1"
assert verifie([-1, 4]) == True, "Erreur exercice 1"
assert verifie([5]) == True, "Erreur exercice 1"



# Exercice 2

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}   # Initialisation d'un dictionnaire
    for bulletin in urne:
        if bulletin in resultat:   # Vérifie si le bulletin se trouve déjà dans resultat
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1   # Met le resultat du bulletin à 1 car c'est le premier
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :   # Regarde si le candidat sélectionné à plus de votes que le précédent
            nmax = election[candidat]   # nmax prend le nombre de votes du candidat avec le plus de votes
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]   # Renvoie la liste des candidats avec le nombre de votes égal à nmax
    return liste_finale

election = depouille(urne)
assert vainqueur(election) == ['B'], "Erreur exercice 2"
