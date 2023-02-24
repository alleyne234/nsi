def tri_selection(tab):
    i = 0
    j = len(tab) - 1
    k_min = 0
    while i < j:
        mini = tab[i]
        for k in range(i, j):
            if mini > tab[k]:
                mini = tab[k]
                k_min = k
        tab[i], tab[k_min] = mini, tab[i]
        i = i + 1
    return tab
