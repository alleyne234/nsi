"""
NSI Archicture, Systèmes d'exploitation
Un mystérieux problème...
Un thread incrémente un compteur partagé 1000000 de fois
Un autre thread décrément ce même compteur 1000000 de fois
Le compteur devrait être égal à 0 à la fin et pourtant...
"""

# Librairie utilisées
from threading import Thread
from threading import Lock


# Variable partagée par les 2 threads
compteur = 0

# Création d'un verrou partagée par les 2 threads
verrou = Lock()


def incrementer(limite):
    """Incrémente le compteur"""
    global compteur
    for i in range(0, limite):
        verrou.acquire()
        compteur = compteur + 1
        verrou.release()

def decrementer(limite):
    """Décrémente le compteur"""
    global compteur
    for i in range(0, limite):
        verrou.acquire()
        compteur = compteur - 1
        verrou.release()


if __name__ == '__main__':
    print(f"Compteur au début => {compteur}")
    # Création des threads
    t1 = Thread(target=incrementer, args=(1000000,))
    t2 = Thread(target=decrementer, args=(1000000,))

    # Lancement des threads
    t1.start()
    t2.start()

    # Attente de la fin du travail
    t1.join()
    t2.join()

    # Affichage du résultat
    print(f"Compteur à la fin => {compteur}")