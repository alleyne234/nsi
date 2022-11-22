def facto(n):
    '''Renvoie la valeur du calcul factoriel n.
    : n : (int)
    @ return : (int)
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)

def facto_bis(n, acc = 1):
    '''Renvoie la valeur du calcul factoriel n.
    : n : (int)
    @ return : (int)
    '''
    if n == 0 or n == 1:
        return acc
    else:
        return facto_bis(n - 1, acc * n)
