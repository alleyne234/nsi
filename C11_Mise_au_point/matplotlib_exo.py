import matplotlib.pyplot as plt
import math

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
plt.plot(liste_x,liste_y1,'r-', label='n.log(n)')
plt.plot(liste_x,liste_y2,'b-', label='n²')
plt.plot(liste_x,liste_y3,'g-', label='n')

#legende
plt.legend(['n.log(n)', 'n²', 'n'])

#génération de la fenêtre du tracé
plt.show()
