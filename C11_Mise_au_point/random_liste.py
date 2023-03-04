from random import randint

def random(n):
    """Renvoie une liste triée de nombres aléatoires
    """
    liste = [randint(0, 9999) for _ in range(n)]
    liste_triee = sorted(liste)
    return liste_triee

print(random(3))
