def for_1():
    valeur = 1
    n = int(input("quelle est la valeur de n ?" ))
    for _ in range(n) :
        valeur = valeur * 2
    print(valeur)
    
def for_2():
    '''
    CU : n > 0
    '''
    somme = 0
    n = int(input("quelle est la valeur de n ?" ))
    entier = (n*(n+1)//2)
    for i in range(1, n+1):
        somme = somme + i
    print("la somme de 1 à ",n , "vaut ", somme)
    print("l'entier vaut ",entier)
    
def for_3(car,chaine):
    occu = 0
    for elt in chaine :
        if elt == car :
            occu = occu + 1
        return occu
    
    

def while_1(n):
    acc = 0
    while n > 0:
        n = n // 10
        acc = acc + 1
    return acc
    
def while_2(n):
    assert n > 0, "n doit être strictement positif"
    while n != 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)



def triangle():
    l1 = int(input("première longueur"))
    l2 = int(input("deuxième longueur"))
    l3 = int(input("troisième longueur"))
    if l1 <= l2 + l3 and l2 <= l3 + l1 and l3 <= l1 + l2:
        if l1 == l2 and l2 == l3:
            print("le triangle est équilatéral")
        elif l1 and l2 or l2 == l3 or l1 == l3:
            print("le triangle est isocèle")
        else:
            print("le triangle est scalère")
            
    else:
        print("ces valeurs ne peuvent pas formr un triangle")



liste = [1, 2, 4, 7, 3, 6, 8, 2]

def liste_1_i(v, liste):
    occu = 0
    for i in range(len(liste)):
        if liste[i] == v :
            occu = occu + 1
        return occu

def liste_1_s(v, liste):
    '''renvoie nombre d'occurence de v dans la liste
    : v : (int) valeur recherchée
    : liste : (list)
    @ return (int)'''
    occu = 0
    for elt in liste :
        if elt == v :
            occu = occu + 1
        return occu
    
import random

liste_random = []

def liste_2():
    '''construit une liste de 20 entier aléatoire entre 1 et 1000'''
    for _ in range (20):
        liste_random.append(random.randint(1,1000))
    print(liste_random)

def liste_3(n):
    '''renvoie une liste contenant ncaractères "*"
    : n: (int) nombre de symboles
    @ return (list)'''
    return ['*' for _ in range(n)]

    
def liste_4():
    '''lise de 10 nombres pairs
    @ return (list)'''
    return [i for i in range(1, 21) if i%2 == 0]



def tup_1(chaine):
    '''renvoie un tuple à partir d'une chaine de caratères
    : chaine : (str)
    @ return (tuple)'''
    return tuple(chaine)
    
t = (2,4,6,7,1)

def tup_2(t):
    '''renvoie la valeur maximale et son indice dans t'''
    maxi = t[0]
    indice = 0
    for i in range (len(t)):
        if t[i] > maxi:
            maxi = t[i]
            indice = i
    return maxi, indice



d1 = {'nom' : 'Tourist' , 'prenom' : 'Bob' , 'lieu' : 'Ennevelin'}
d2 = {'nom': 'Lenon' , 'prenom' : 'Bob' , 'lieu' : 'MC'}
d3 = {'nom' : 'Alex' , 'prenom' : 'Wauquier' , 'lieu' : 'Ennevelin'}

# print(d1.keys())

amis = {'a' : d1, 'b' : d2, 'c' : d3}

def dico_1(amis):
    '''affiche tous les prénoms des amis
    : amis : (dict (dict))'''
    for dico in amis.values():
        print(dico["prenom"])


def dico_2(amis):
    '''renvoie une liste avec tous les lieux d'habitation sans de doublon'''
    liste_lieux = []
    for dico in amis.values():
        hab = dico["lieu"]
        if hab not in liste_lieux:
            liste_lieux.append(hab)
    return liste_lieux
