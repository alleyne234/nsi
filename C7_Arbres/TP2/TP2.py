class Noeud :
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

ABR= Noeud(Noeud(None,1,Noeud(None,2,None)) ,
            3,
            Noeud(None ,4, None))

def minimum(abr):
    '''renvoie la valeur minimale de l'abr
    '''
    if abr is None :
        return
    if abr.gauche is None :
        return abr.valeur
    else :
        return minimum(abr.gauche)

def maximum(abr):
    '''renvoie la valeur minimale de l'abr
    '''
    if abr is None :
        return
    if abr.droit is None :
        return abr.valeur
    else :
        return maximum(abr.droit)

## ex 3
def ajoute(abr,x):
    if abr is None :
        return Noeud(None,x,None)
    if x< abr.valeur :
        return Noeud(ajoute(abr.gauche,x),abr.valeur, abr.droit)
    elif x == abr.valeur :
        return abr
    else :
        return Noeud(abr.gauche,abr.valeur,ajoute(abr.droit,x))
ABR0= ajoute(ABR,0)
ABR5 = ajoute(ABR0,5)

a = Noeud(Noeud(Noeud(None ,3,None ) ,4 ,Noeud( None,4, None) ),
           6 , 
           Noeud( Noeud(None, 6,None), 9 ,Noeud(None,10,None) ))

def compte(x,a):
    '''compte le nombre d'occurrence de x dans
    a
    x: int valeur recherchee
    a : abr
    '''
    if a is None :
        return 0
    elif x == a.valeur :
        return 1 + compte(x, a.gauche) + compte(x,a.droit)
    elif x < a.valeur :
        return compte(x, a.gauche)
    else :
        return compte(x, a.droit)
#print(compte(6,a))

t = []
def remplir(a,t):
    '''remplir une liste avec les valeurs de l'arbre
    en parcours infixe
    : a : arbre
    : t : (list)
    '''
    if a is None :
        return
    remplir(a.gauche, t)
    t.append(a.valeur)
    remplir(a.droit, t)
    return t

remplir(ABR,t)
print(t)
 
from ABR import *
arbre_exo4= ABR()
arbre_exo4.ajouter(6)
arbre_exo4.ajouter(4)
arbre_exo4.ajouter(4)
arbre_exo4.ajouter(3)
arbre_exo4.ajouter(9)
arbre_exo4.ajouter(6)
arbre_exo4.ajouter(10)

print('valeur minimale : ',minimum(arbre_exo4.racine))
print('valeur maximale :', maximum(arbre_exo4.racine))
print(arbre_exo4.lister())