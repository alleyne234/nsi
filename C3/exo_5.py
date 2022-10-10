class Tableau:
    def __init__(self, imin, imax, v):
        self.premier = imin
        self.contenu = [v for i in range(imax - imin + 1)]
        
    def __len__(self):
        return len(self.contenu)
    
    def __indice_valide__(self, i):
        if i < self.premier or i > self.premier + self.__len__():
            raise IndexError(i)
        
    def __getitem__(self, i):
        self.__indice_valide(i)
        return self.contenu[i - self.premier]
        
t = Tableau(-10, 9, 42)
t.__indice_valide__(18)
print(t.__len__())

