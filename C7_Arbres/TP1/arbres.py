class Noeud :
    ''' un noeud d'un arbre binaire'''
    def __init__(self, g, v, d) :
        self.gauche = g
        self.valeur = v
        self.droite = d
        
    def eq(self, other):
        return other is not None and self.gauche == other.gauche and self.valeur == other.valeur and self.droite == other.droite
        


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

def est_peigne_gauche(ab):
    """"Prédicat"""
    if ab is None:
        return True
    elif ab.droite is not None:
        return False
    return est_peigne_gauche(ab.gauche)
        
def eq(a1, a2):
    if a1 is None and a2 is None:
        return True
    elif a1.valeur == a2.valeur:
        return eq(a1.gauche, a2.gauche) and eq(a1.droite, a2.droite)
    else:
        return False

def parcours_infixe(a):
    '''réalise le parcours infixe d'un arbre
    '''
    if a is None : 
        return
    parcours_infixe(a.gauche)
    print(a.valeur)
    parcours_infixe(a.droite)
    
def parcours_prefixe(a):
    '''réalise le parcours prefixe d'un arbre
    '''
    if a is None : 
        return
    print(a.valeur)
    parcours_prefixe(a.gauche)
    parcours_prefixe(a.droite)

def parcours_postfixe(a):
    '''réalise le parcours postfixe d'un arbre
    '''
    if a is None : 
        return
    parcours_postfixe(a.gauche)
    parcours_postfixe(a.droite)
    print(a.valeur)


        
print(ab.eq(ab1))
print(ab.eq(ab))

arbreParfait = parfait(4)
affiche(arbreParfait)

a_peig_g = peigne_gauche(4)
affiche(a_peig_g)

test = Noeud(Noeud(Noeud(None, 'D', None), 'B', Noeud(Noeud(None, 'G', None), 'E', Noeud(None, 'H', None))),
             'A',
             Noeud(None, 'C', Noeud(Noeud(None, 'I', None), 'F', None)))

print(' ')
affiche(test)
