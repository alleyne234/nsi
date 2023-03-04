class Noeud():
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d
            
def ajoute(x, abr):
    '''ajoute x à l'arbre binaire (abr), renvoie un nouvel arbre
    '''
    if abr is None : 
        return Noeud(None, x, None)   # crée le premier noeud
    if x < abr.valeur :
        return Noeud(ajoute(x, abr.gauche) ,abr.valeur ,abr.droite)
    else : 
        return Noeud(abr.gauche, abr.valeur, ajoute(x, abr.droite))

def appartient(x, abr):
    '''détermine si x apparaît dans l'ABR
    '''
    if abr is None: 
        return False
    if x < abr.valeur:
        return appartient(x, abr.gauche)
    elif x > abr.valeur:
        return appartient(x, abr.droite)
    else: 
        return True



class ABR:
    def __init__(self):
        self.racine = None
    
    def ajouter(self, x):
        self.racine = ajoute(x, self.racine) 

    def contient(self, x): 
        return appartient(x, self.racine)

def trier(t):
    """trie en utilisant ABR
    :t: list : liste d'entiers non trié
    :return: list : entier trié croissant
    """
    arbre = ABR()
    for elt in t:
        arbre.ajouter(elt)
    return arbre.lister() # parcours INFIXE: classe par ordre croissant
