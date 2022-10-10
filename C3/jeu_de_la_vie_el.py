# jeu de la Vie

########
import time
from random import random
########

class Cellule:
    def __init__(self):
        self.__actuel = False
        self.__futur = False
        self.__voisins = None
    
    def est_vivant(self):
        return self.__actuel
    
    def set_voisins(self, voisins):
        self.__voisins = voisins
    
    def get_voisins(self):
        return self.__voisins
    
    def naitre(self):
        self.__futur = True
    
    def mourir(self):
        self.__futur = False
    
    def basculer(self):
        self.__actuel = self.__futur
    
    def __str__(self):
        """remplace l'affichage print par défaut en renvoyant une chaine de caractères représentant l'objet"""
        if self.est_vivant():
            res ="X"
        else:
            res = "-"
        return res
          
    def nb_vivants_voisins(self):
        """calcule le nombre de vivants dans la liste des voisins"""
        nb = 0
        for elt in self.__voisins:
            if elt.est_vivant():
                nb = nb + 1
        return nb
    
    def calcule_etat_futur(self):
        """gère l'évolution de la cellule"""
        nb_vivants_voisins = self.nb_vivants_voisins() # Recupere le nombre de voisins vivants et le stock dans une variable locale.
        if nb_vivants_voisins != 2 and nb_vivants_voisins != 3: # Rentre dans la condition si le nombre de voisins vinvants est différent de 2 et de 3.
            self.mourir() # Fait mourir la cellule.
        elif nb_vivants_voisins == 3: # Rentre dans la condition si le nombre de voisins vivants est égal à 3.
            self.naitre() # Fait naitre une cellule.
        else:
            self.__futur = self.__actuel
        

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrix = [[Cellule() for i in range(self.largeur)] for j in range(self.hauteur)]
        
    def dans_grille(self, i, j):
        return 0 <= i < self.largeur and 0 <= j < self.hauteur
    
    def setXY(self, i, j, valeur):
        if (i,j) in self : 
            self.matrix[i][j] = valeur
        else:
            raise IndexError(str(i, j))
    
    def getXY(self, i, j):
        if self.dans_grille(i, j):
            return self.matrix[i][j]
        else:
            return None
    
    def get_largeur(self):
        return self.largeur
    
    def get_hauteur(self):
        return self.hauteur
    
    # méthode statique
    def est_voisin(i, j, x, y):
        return max(abs(x - i), abs(y - j)) == 1
    
    def get_voisins(self, x, y):
        liste_voisins = []
        for i in range(x - 1, x + 2):
            for j in range (y - 1, y + 2):
                if self.dans_grille(i, j) and Grille.est_voisin(x, y, i, j):
                    liste_voisins.append(self.getXY(i, j))
        return liste_voisins
    
    def affecte_voisins(self):
        for i in range (self.largeur):
            for j in range(self.hauteur):
                self.getXY(i, j).set_voisins(self.get_voisins(i, j)) # on réutilise la méthode de Cellule privé
    
    def __str__(self):
        res = ""
        for i in range (self.largeur):
            for j in range(self.hauteur):
                res = res + str(self.getXY(i, j)) # str a été redéfinie dans Cellule
            res = res + "\n"
        return res
        
    def remplir_alea(self, taux):
        for i in range (self.largeur):
            for j in range(self.hauteur):
                if random() <= (taux / 100.0):
                    self.getXY(i, j).naitre()
                    self.getXY(i, j).basculer()
                print(self.getXY(i, j))
                
    def jeu(self):
        for i in range (self.largeur):
            for j in range(self.hauteur):
                cel = self.getXY(i, j)
                cel.calcule_etat_futur()
    
    def actualise(self) :
        for i in range (self.largeur):
            for j in range(self.hauteur):
                self.getXY(i, j).basculer()


                    
        
######################
if __name__ == '__main__':
    vie = Grille(30, 30) # default (20, 20)
    vie.remplir_alea(30) # default (15)
    vie.affecte_voisins()
    while True:
        print(vie)
        print("\n")
        time.sleep(3)
        vie.jeu()
        vie.actualise()
