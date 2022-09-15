### IMPORTS ###
from random import randint



### CODE ###

def moyenne(tableau):
    '''Renvoie la moyenne des valeurs du tableau.
    :tableau : (list)
    @ return (float)
    '''
    assert len(tableau) > 0 , 'Le tableau est vide !'
    sum = 0
    for elt in tableau:
        sum = sum + elt
    return sum / len(tableau)
    
def create_tab(n):
    '''Creer un tableau de nombres aleatoires compris entre 0 et n.
    '''
    # assert n > 0 , 'n doit etre superieur a 0 !'
    tab = []
    for _ in range(n):
        tab.append(randint(1,n))
    return tab
    
def max_value(tab):
    '''Renvoie la valeur maximale d'un tableau.
    '''
    assert len(tab) > 0 , 'Le tableau est vide !'
    max = tab[0]
    for elt in tab:
        if elt > max:
            max = elt
    return max
    
def min_value(tab):
    '''Renvoie la valeur minimale d'un tableau.
    '''
    assert len(tab) > 0 , 'Le tableau est vide !'
    min = tab[0]
    for elt in tab:
        if elt < min:
            min = elt
    return min

def insere_element(tab, position, element):
    '''Insere un element dans le tableau a une position donner.
    : tableau : (list)
    : position : (int)
    : element : (int)
    @ return (list)
    '''
    assert position <= len(tab) and position >= 0, 'La position doit etre inferieur a la longueur du tableau et superieur a 0 !'
    new_tab = []
    for i in range(0, position):
        new_tab.append(tab[i])
    new_tab.append(element)
    for i in range(position, len(tab)):
        new_tab.append(tab[i])
    return new_tab

def main():
    print("Ce fichier est top secret! Personne ne doit connaître ma moyenne")
    print(moyenne([5,8,9,10,14]))

if __name__ == "__main__":
    main()
