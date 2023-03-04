from time import perf_counter
from random import randint

def mesure_temps():
    nb_repetitions = 1000
    temps_final = float('inf')
    for _ in range(nb_repetitions):
        l= [randint(0, 99) for _ in range(1001)]
        debut = perf_counter()
        # ----- Code à mesurer -----
        liste = []
        for i in range(n + 1)
        # --------------------------
        temps = perf_counter() - debut
        if temps < temps_final:
            temps_final = temps
    return temps_final

print(mesure_temps())
