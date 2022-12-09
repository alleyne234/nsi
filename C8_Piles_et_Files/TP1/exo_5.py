class Pile_bornee:
    def __init__(self, c):
        self.contenu = [None] * c
        self.indice = 0
    
    def est_vide(self):
        return self.contenu == None
    
    def est_pleine(self):
        return self.indice == len(self.contenu)
    
    def empiler(self, e):
        if self.est_pleine():
            raise IndexError("la pile a dépassé sa capacité")
        else:
            self.contenu[self.indice] = e
            self.indice = self.indice + 1
            
    def depiler(self):
        if self.est_vide():
            raise IndexError("la pile est vide")
        value = self.contenu[self.indice]
        self.contenu[self.indice] = None
        self.indice = self.indice - 1
        return value

pb = Pile_bornee(6)
print(pb.contenu)
