class Noeud :
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d
        
def ajoute(x,abr):
    '''ajoute x à l'arbre binaire (abr), renvoie un nouvel arbre
    '''
    if abr is None : 
        return Noeud(None,x,None)   # crée le premier noeud
    if x < abr.valeur :
        return Noeud(ajoute(x, abr.gauche) , abr.valeur , abr.droit)
    else : 
        return Noeud( abr.gauche , abr.valeur , ajoute(x, abr.droit))

def appartient(x,abr):
    '''détermine si x apparaît dans l'ABR
    '''
    if abr is None : 
        return False
    if x < abr.valeur:
        return appartient(x,abr.gauche)
    elif x > abr.valeur:
        return appartient(x,abr.droit)
    else : 
        return True
def remplir(a,t):
    '''remplir une liste avec les valeurs de l'arbre
    en parcours infixe
    : a : arbre
    : t : (list)
    '''
    if a is None :
        return
    remplir(a.gauche, t)
    t.append(a.valeur)
    remplir(a.droit, t)
    return t

class ABR :
    def __init__(self ):
        self.racine = None
    
    def ajouter(self, x) :
        self.racine = ajoute(x, self.racine) 

    def contient(self, x) : 
        return appartient(x, self.racine)
    
    def lister(self):
        t = []
        return remplir(self.racine, t)
