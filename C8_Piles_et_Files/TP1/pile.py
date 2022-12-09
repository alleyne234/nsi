class Cellule :
    '''cellule d'une liste chaînée
    '''
    def __init__( self, v, s):
        self.valeur = v
        self.suivante = s

class Pile :
    def __init__(self):
        self.contenu = []
    
    def est_vide(self) :
        return len(self.contenu) == 0
        
    def empiler(self, e):
        self.contenu.append(e)
        
    def depiler(self) :
        if self.est_vide() : # on utilise la méthode !!!!
            raise IndexError("dépiler une liste vide")
        else :
            return self.contenu.pop()
            
    def consulter(self):
        if self.est_vide():
            raise IndexError("consultation d'une pile")
        else:
            return self.contenu.valeur
        
    def vider(self):
        self.contenu = None
        
    def inverse(self):
        new_pile = creer_pile()
        while not self.est_vide():
            new_pile.empiler(self.depiler())
        return new_pile
    
    
        
def creer_pile():
    return Pile() 


