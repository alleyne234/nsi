def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []  # on vide T2 copie de T
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ', T)
    return T2

liste = positif([1, -1, 3, 4, -5])
print(liste)
