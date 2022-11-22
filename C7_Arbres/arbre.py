class Noeud():
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d
        
ABR = Noeud(Noeud(None, 1, Noeud(None, 2, None)),
            3,
            Noeud(None, 4, None))

def minimum(abr):
    """Renvoie la valeur minimale de l'arbre.
    """
    if abr is None:
        return
    if abr.gauche is None:
        return abr.valeur
    else:
        return minimum(abr.gauche)

def maximum(abr):
    """Renvoie la valeur maximale de l'arbre.
    """
    if abr is None:
        return
    if abr.droite is None:
        return abr.valeur
    else:
        return maximum(abr.droite)

def ajoute(abr, x):
    """Ajoute une valeur à l'arbre si celle-ci n'est pas déjà dans l'arbre.
    """
    if abr is None:
        return Noeud(None, x, None)
    if x < abr.valeur:
        return Noeud(ajoute(abr.gauche, x), abr.valeur, abr.droite)
    elif x == abr.valeur:
        return abr
    else:
        return Noeud(abr.gauche, abr.valeur, ajoute(abr.droite, x))
    
temp = ajoute(ABR, 10)
temp = ajoute(temp, 0)
