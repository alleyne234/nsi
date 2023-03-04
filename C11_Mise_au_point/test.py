from random import randint
from time import perf_counter
import matplotlib.pyplot as plt
import math

def recherche_dicho(tab, valeur):
    """Renvoie l'indice d'une valeur dans un tableau trié
    :tab: (list) liste triée
    :valeur: (int)
    @return (int)
    """
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite:
        milieu= (gauche + droite) // 2
        if valeur < tab[milieu]:
            droite = milieu - 1
        elif valeur == tab[milieu]:
            return milieu
        else:
            gauche = milieu + 1
    return milieu

def recherche_indice_seq(tab, valeur):
    """Renvoie l'indice d'une valeur dans un tableau trié
    :tab: (list) liste triée
    :valeur: (int)
    @return (int)
    """
    for i in range(len(tab)):
        if tab[i] == valeur:
            return i
    return None

def recherche_index(liste, nb):
    try:
        return liste.index(nb)
    except(ValueError):
        return None

def random(n):
    """Renvoie une liste triée de nombres aléatoires
    """
    liste = [randint(0, 9999) for _ in range(n)]
    liste_triee = sorted(liste)
    return liste_triee

#création de la liste pour les abscisses
liste_x = [x for x in range(1,101,5)]

#création de la liste pour les ordonnées
liste_y1 = [x*math.log2(x) for x in liste_x]
liste_y2 = [x**2 for x in liste_x]
liste_y3 = [x for x in liste_x]

#choix des limites des axes [xmin, xmax, ymin, ymax] (facultatif)
plt.axis([0, 100, 0, 100])

#tracé du graphique
#dans 'rx ' 'r' --> rouge, 'x' --> croix, ' '--> pas de lien
#plt.plot(liste_x,liste_y1,'r-', label='n.log(n)')
#plt.plot(liste_x,liste_y2,'b-', label='n²')
#plt.plot(liste_x,liste_y3,'g-', label='n')

#legende
#plt.legend(['n.log(n)', 'n²', 'n'])

#génération de la fenêtre du tracé
#plt.show()

def mesure_temps():
    nb_repetitions = 1000
    temps_final = float('inf')
    for _ in range(nb_repetitions):
        l= [randint(0, 99) for _ in range(1001)]
        debut = perf_counter()
        # ----- Code à mesurer -----

        # --------------------------
        temps = perf_counter() - debut
        if temps < temps_final:
            temps_final = temps
    return temps_final

print(mesure_temps())
