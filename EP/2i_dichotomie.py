# 2 i ( dichotomie)
tab_trie = [i for i in range(1, 9)]

def recherche_dicho(tab_trie, n):
    gauche = 0
    droite = len(tab_trie) - 1
    i_milieu = (gauche + droite) // 2
    while gauche <= droite:
        if n == tab_trie[i_milieu]:
            return i_milieu
        elif n < tab_trie[i_milieu]:
            droite = i_milieu - 1
        else:
            gauche = i_milieu + 1
    return -1
