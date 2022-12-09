class File : 
    def __init__(self):
        self.entree = None
        self.sortie = None
    
    def est_vide(self) :
        return self.entree.est_vide() and self.sortie.est_vide()
    
    def ajouter(self, e):
        self.entree.empiler(e)
    
    def enfile(self,e) :
        '''on enfile sur la queue de la liste
        '''
        c = Cellule(e , None)
        if self.est_vide() :
            self.tete = c
        else :
            self.queue.suivante = c
        self.queue = c

    def defile(self) :
        '''on récupère la valeur de la tete mais on l'enlève de la file
        '''
        if self.est_vide() :
            raise IndexError ( "defile une file vide")
        else :
            t = self.tete.valeur
            self.tete = self.tete.suivante
            if self.tete is None :
                self.queue = None
            return t
     
    def retirer(self):
        if not self.sortie.est_vide() :
            self.sortie.depile()

def creer_file():
    return File()

class Cellule :
    '''cellule d'une liste chaînée
    '''
    def __init__( self, v, s):
        self.valeur = v
        self.suivante = s
