def somme(n):
    """Renvoie la somme des élémnts d'une liste
    @param n : (int) un entier positif ou nul.
    """
    s = 0
    for i in range(0, n + 1):
        s = s + i
    return s

# === Programme principal ===
def est_correcte():
    """Vérifie si la fonction somme fonctionne correctement
    """
    from random import randint
    liste = [randint(0, 100) for _ in range(21)]
    for n in liste:
        assert somme(n) == n*(n + 1) / 2
    return True

if est_correcte():
    print("La fonction donne bien le résultat attendu !")
