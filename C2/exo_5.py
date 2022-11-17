def nombre_de_chiffres(n):
    '''Renvoie le nombre de chiffres du nombre en entree.
    : n : (int)
    @ return (int)
    : CU : n doit etre positif
    '''
    assert n >= 0, 'n doit etre positif'
    if n <= 9:
        return 1
    else:
        return 1 + nombre_de_chiffres(n // 10)

def nombre_de_bits(n):
    '''Renvoie le nombre de 1.
    : n : (int)
    @ return (int)
    : CU : n doit etre positif
    '''
    if n < 2:
        if n == 0:
            return 0
        else:
            return 1
    elif n % 2 == 0:
        return nombre_de_bits(n // 2)
    else:
        return 1 + nombre_de_bits(n // 2)
