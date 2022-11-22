def min_value(tab, current_ind):
    '''Renvoie l'indice de la valeur minimal du tableau a partir de l'indice current.
    : tab : (list)
    : current_ind : (int)
    @ return (int)
    '''
    min_ind = current_ind
    min_value = tab[min_ind]
    for i in range(current_ind, len(tab)):
        if min_value > tab[i]:
            min_value = tab[i]
            min_ind = i
    return min_ind

def echange(tab, min_ind, current_ind):
    '''Echange l'indice etudier par l'indice minimum.
    : tab : (list)
    : current_ind : (int)
    @ return (int)
    '''
    temp = tab[min_ind]
    tab[min_ind] = tab[current_ind]
    tab[current_ind] = temp

def tri_s(tab):
    '''Tri le tableau par selection.
    '''
    for i in range(len(tab)-1):
        min_ind = min_value(tab, i)
        echange(tab, min_ind, i)
    return tab



def insert(tab, current_ind):
    '''Insere la valeur actuel a la bonne place.
    '''
    to_ind = tab[current_ind]
    j = current_ind
    while(j >= 1 and to_ind < tab[j - 1]):
        tab[j] = tab[j-1]
        j = j - 1
    tab[j] = to_ind
    return tab

def tri_insert(tab):
    for i in range (1, len(tab)):
        tab_trie = insert(tab, i)
    print(tab)
    