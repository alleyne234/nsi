from ABR import *

arbre = ABR()
arbre.ajouter(15)
arbre.ajouter(13)
arbre.ajouter(11)
arbre.ajouter(14)
arbre.ajouter(21)
arbre.ajouter(18)
arbre.ajouter(27)
arbre.ajouter(20)

print(arbre.lister())


def nb_sup(v, abr):
    if abr is None:
        return 0
    else:
        if abr.racine.valeur > v:
            return 1 + nb_sup(v, abr.droit) + nb_sup(v, abr.gauche)
        elif abr.racine.valeur == v:
            return 1 + nb_sup(v, abr.droit)
        else:
            return nb_sup(v, abr.droit)
            

print(nb_sup(16, arbre).lister())
