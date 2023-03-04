def syracuse(u_n):
    '''Affiche toutes les valeurs pour la conjecture de Syracuse.
    : u_n : (int)
    @ return (int)
    C U : u_n doit etre un entier positif
    '''
    assert u_n >= 0, 'u_n doit etre positif ou nul.'
    assert type(u_n) == int, 'u_n doit etre un entier.'
    print(u_n) # Cas ou u_n = 1 et affichage a chaque etape.
    if u_n == 1:
        return 1
    elif u_n % 2 == 0:
        return syracuse(u_n // 2)
    else:
        return syracuse(u_n * 3 + 1)

syracuse(15)
