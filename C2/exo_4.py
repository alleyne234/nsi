def boucle(i, k):
    '''Affiche les entiers entre i et k.
    : i, k : (int)
    @ return
    '''
    print(i)
    if i == k:
        return
    else:
        boucle(i + 1, k)
        
def boucle_bis(i, k):
    if k != i - 1:
        print(i)
        return boucle_bis(i + 1, k)
