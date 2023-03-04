class Cellule: 
    '''cellule d'une liste s.
    '''
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

liste_ch = Cellule('Alex', Cellule('Steve', Cellule('Bob', None)))

#print(liste_ch)
#print(liste_ch.valeur)
#print(liste_ch.suivante)
#print(liste_ch.suivante.valeur)
#print(liste_ch.suivante.suivante)
#print(liste_ch.suivante.suivante.valeur)



# Exercice 2

def n_ieme_elt(n, liste_ch):
    ''' Renvoie le n-ième élément de la liste chaîne.
    : n : (int) indice de la Cellule
    : liste_ch : instance de la classe Cellule, liste chaine
    @ return valeur
    '''
    liste_etudiee = liste_ch
    if liste_ch is None or n < 0:
        raise IndexError("Indice invalide")
    compteur = 0
    while compteur < n and liste_etudiee is not None:
        liste_etudiee = liste_etudiee.suivante
        compteur = compteur + 1
    return liste_etudiee.valeur 

#print(n_ieme_elt(0, liste_ch))



# Exercice 3

l_c2 = Cellule(6, Cellule(5, Cellule(4, Cellule(3, None))))
l_c1 = Cellule(9, Cellule(8, Cellule(7, None)))
l_c1.suivante.suivante.suivante = l_c2
#print(n_ieme_elt(3, l_c1))
#print(n_ieme_elt(6, l_c1))

l_c3 = Cellule(2, Cellule(1, None))
l_c2.suivante.suivante.suivante.suivante = l_c3
#print(n_ieme_elt(7, l_c1))



# Exercice 4

def affiche_liste_recursif(l_c):
    '''Affiche les valeurs de la liste chainee sur une ligne (recursif).
    : l_c : instance de la classe Cellule
    '''
    if l_c is None:
        print()
    else:
        print(l_c.valeur, end = ' ')
        affiche_liste_recursif(l_c.suivante)
    
#affiche_liste_recursif(l_c1)
        
def affiche_liste_iteratif(l_c):
    '''Affiche les valeurs de la liste chainee sur une ligne (iteratif).
    : l_c : instance de la classe Cellule
    '''
    liste_etudiee = l_c
    while liste_etudiee is not None:
        print(liste_etudiee.valeur, end = ' ')
        liste_etudiee = liste_etudiee.suivante
    print()
    
#affiche_liste_iteratif(l_c1)



# Exercice 5

def listeN_iteratif(n):
    '''Renvoie une liste chainee de 1 à n.
    : n : int
    @return instance de Cellule
    '''
    compteur = n
    l_c = None
    while compteur > 0:
        l_c = Cellule(compteur, l_c)
        compteur = compteur - 1
    return l_c

#affiche_liste_iteratif(listeN_iteratif(7))

def listeN_recursif(n, liste = None):
    '''Renvoie une liste chainee de 1 à n.
    : n : int
    @return instance de Cellule
    '''
    if n <= 0:
        return liste
    else:
        return listeN_recursif(n - 1, Cellule(n, liste))

#affiche_liste_iteratif(listeN_recursif(8))
    


# Exercice 6

liste_c = Cellule('l',Cellule('a',Cellule(' ',Cellule('n',Cellule('s',Cellule('i',Cellule(' ',Cellule('c',Cellule("'",Cellule('e',Cellule('s',Cellule('t',Cellule(' ',Cellule('l',Cellule('a',Cellule(' ',Cellule('v',Cellule('i',Cellule('e',None)))))))))))))))))))

def occurences_recursif(x, liste_c, acc = 0):
    '''Renvoie le nombre doccurence de la valeur x dans la liste_c.
    : x : string
    : liste_c : instance de classe Cellule
    : acc : int
    @return int : nombre doccurences
    '''
    if liste_c is None:
        return acc
    elif liste_c.valeur == x:
        return occurences_recursif(x, liste_c.suivante, acc + 1)
    else:
        return occurences_recursif(x, liste_c.suivante, acc)

#print(occurences_recursif('e', liste_c))

def occurences_iteratif(x, liste_c):
    '''Renvoie le nombre doccurence de la valeur x dans la liste_c.
    : x : string
    : liste_c : instance de classe Cellule
    : acc : int
    @return int : nombre doccurences
    '''
    acc = 0
    l_c = liste_c
    while l_c is not None:
        if l_c.valeur == x:
            acc = acc + 1
        l_c = l_c.suivante
    return acc

#print(occurences_iteratif('e', liste_c))

def trouve_recursif(x, liste_c, indice = 0):
    '''Renvoie le nombre doccurence de la valeur x dans la liste_c.
    : x : string
    : liste_c : instance de classe Cellule
    : indice : int
    @return int : rang
    '''
    if liste_c is None:
        return None
    elif liste_c.valeur == x:
        return indice
    else:
        return trouve_recursif(x, liste_c.suivante, indice + 1)
    
#print(trouve_recursif('l', liste_c))

def trouve_iteratif(x, liste_c):
    '''Renvoie le nombre doccurence de la valeur x dans la liste_c.
    : x : string
    : liste_c : instance de classe Cellule
    : indice : int
    @return int : rang
    '''
    indice = 0
    liste_etudiee = liste_c
    while liste_c is not None:
        if liste_etudiee.valeur == x:
            return indice
        liste_etudiee = liste_etudiee.suivante
        indice = indice + 1
    return None

#print(trouve_iteratif('l', liste_c))



# Exercice 7

lst = Cellule(2,Cellule(4,None))

def inserer(x, lst):
    '''Renvoie une nouvelle liste chainee dans laquelle x a ete insere a sa place.
    : x : int
    : lst : instance de classe Cellule
    @return instance de classe Cellule
    '''
    if lst is None:
        return Cellule(x, None)
    elif x <= lst.valeur:
        return Cellule(x, lst)
    else:
        return Cellule(lst.valeur, inserer(x, lst.suivante))
    
#affiche_liste_iteratif(inserer(3, lst))

def tri_par_insertion(lst):
    '''Renvoie une liste chainee triee.
    : lst : instance de Cellule
    @return instance de Cellule, valeur triees
    '''
    if lst is None or lst.suivante is None:
        return lst
    else:
        return inserer(lst.valeur, tri_par_insertion(lst.suivante))

#affiche_liste_iteratif(tri_par_insertion(liste_c))
