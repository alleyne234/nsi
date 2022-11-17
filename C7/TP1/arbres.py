class Noeud :
    ''' un noeud d'un arbre binaire'''
    def __init__(self, g, v, d) :
        self.gauche = g
        self.valeur = v
        self.droite = d
        
    def eq(self, other):
        return other is not None and self.gauche.valeur == other.gauche.valeur and self.valeur == other.valeur and self.droite.valeur == other.droite.valeur
        
        

ab = Noeud(Noeud(None,'B' , Noeud(None, 'C' , None) ), 'A' , Noeud( None, 'D' , None))
ab1 = Noeud(Noeud(None,'G' , Noeud(None, 'C' , None) ), 'A' , Noeud( None, 'D' , None))

def affiche(ab):
    """Affiche l'arbre"""
    if ab is None:
        return
    else:
        print('(', end = '')
        affiche(ab.gauche)
        print(ab.valeur, end = '')
        affiche(ab.droite)
        print(')', end = '')
        
def parfait(h):
    """Renvoie un arbre parfait de hauteur h positive ou nulle."""
    if h == 0:
        return None
    else:
        return Noeud(parfait(h - 1), 'o', parfait(h - 1))
    
def peigne_gauche(h):
    """Renvoie un peigne gauche de hauteur h positive ou nulle;"""
    if h == 0:
        return None
    else:
        return Noeud(peigne_gauche(h - 1), 'o', None)
        
print(ab.eq(ab1))
print(ab.eq(ab))

arbreParfait = parfait(4)
affiche(arbreParfait)

a_peig_g = peigne_gauche(4)
affiche(a_peig_g)
