def tri_iteratif(tab):
    for k in range(len(tab) - 1, 0, -1):
        imax = 0
        for i in range(0, k + 1):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k], tab[imax] = tab[imax], tab[k]
    return tab

print(tri_iteratif([41, 55, 21, 18, 12, 6, 25])) # Affiche [6, 12, 18, 21, 25, 41, 55]
