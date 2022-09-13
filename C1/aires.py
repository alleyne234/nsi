### IMPORTS ###

from math import pi

### CODES ###

def disque(rayon):
    '''Renvoie l'aire d'un disque à partir de son rayon.'''
    aire_disque = pi * (rayon ** 2)
    print(aire_disque)
    
def rectangle(largeur, longueur):
    '''Renvoie l'aire d'un rectangle à partir de sa largeur et de sa longeur.'''
    aire_rectangle = largeur * longueur
    print(aire_rectangle)
    
def triangle(base, hauteur):
    '''Renvoie l'aire d'un triangle à partir de sa base et de sa hauteur.'''
    aire_triangle = (base * hauteur) / 2
    print(aire_triangle)

def main():
    print("calcul d'aires")
    print("Disque : pi*r^2")
    print("par exemple, avec r = 5")
    print ("Aire = pi*5^2 =", disque(5))

if __name__ == "__main__":
    main()
