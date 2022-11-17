T = [[4, 1, 1, 3],
     [2, 0, 2, 1],
     [3, 1, 5, 1]]

def somme_max(T, i, j):
    if i == 0:
        if j == 0:
            return T[0][0]
        else:
            return T[0][j] + somme_max(T, 0, j - 1)
    else:
        if j == 0:
            return T[i][0] + somme_max(T, i - 1, 0)
        else:
            return T[i][j] + max(somme_max(T, i - 1, j), somme_max(T, i, j - 1))
