# Exercice 1

def maxliste(tab):
    """Renvoie le plus grand élément de la liste tab.

    :param list tab: liste non vide de nombres
    :return int: valeur la plus grand de tab
    """
    valeur_max = tab[0]

    for valeur in tab:
        if valeur > valeur_max:
            valeur_max = valeur

    return valeur_max

assert maxliste([98, 12, 104, 23, 131, 9]) == 131, "Erreur exercice 1"
assert maxliste([-27, 24, -3, 15]) == 24, "Erreur exercice 1"



# Exercice 2

class Pile:
    """
    Classe definissant une pile
    """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """
        Renvoie True si la pile est vide, False sinon
        """
        return self.valeurs == []

    def empiler(self, c):
        """
        Place l'element c au sommet de la pile
        """
        self.valeurs.append(c)

    def depiler(self):
        """
        Supprime l'element place au sommet de la pile, a condition qu'elle soit non vide
        """
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage(ch):
    """
    Renvoie True si la chaine ch est bien parenthesee et False sinon
    """
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

assert parenthesage("((()())(()))") == True, "Erreur exercice 2"
assert parenthesage("())(()") == False, "Erreur exercice 2"
assert parenthesage("(())(()") == False, "Erreur exercice 2"
