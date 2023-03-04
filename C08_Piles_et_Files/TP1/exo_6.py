from file import *

class File_bornee():
    def __init__(self, c):
        self.contenu = [None] * c
        self.premier = 2
        self.nombre = 0
        
    def est_vide(self):
        return self.nombre == 0
    
    def est_pleine(self):
        return self.nombre == len(self.contenu)
    
    def ajouter(self, e):
        if self.est_pleine:
            raise IndexError("la file est pleine")
        index = (self.premier + self.nombre) % len(self.contenu)
        self.contenu[index] = e
        self.nombre = self.nombre + 1
        
    def retirer(self):
        if self.est_vide:
            raise IndexError("la file est vide")
        index = (self.premier + self.nombre) % len(self.contenu)
        value = self.contenu[index]
        self.contenu[index] = None
        self.nombre = self.nombre - 1
        self.premier = (self.premier - 1) % len(self.contenu)
        return value

f_b = File_bornee(6)
f_b.ajouter(5)
print(f_b.contenu)
