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
    
def compte(x, a):
    """Renvoie le nombre d'occurences de x dans un arbre."""
    if a is None:
        return 0
    elif x == a.valeur:
        return 1 + compte(x, a.gauche) + compte(x, a.droite)
    elif x < a.valeur:
        return compte(x, a.gauche)
    else:
        return compte(x, a.droite)
    
temp = ajoute(ABR, 10)
temp = ajoute(temp, 0)

print(compte(3, ABR))



t = []

def remplir(a, t):
    """Renvoie tois les éléments de l'abre dans un tableau dans l'ordre infixe."""
    if a is None:
        return
    remplir(a.gauche, t)
    t.append(a.valeur)
    remplir(a.droite, t)
    