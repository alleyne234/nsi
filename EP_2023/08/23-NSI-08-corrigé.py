# Exercice 1

def max_dico(dico):
    """Renvoie un tuple dont la première valeur est une clé du dictionnaire associée à la valeur maximale
    et la seconde valeur est la valeur maximale présente dans le dictionnaire.

    :param dict dico: dictionnaire  contenant les pseudos d'utilisation avec leur nombre de like
    :return _type_: pseudo de l'utilisateur avec le plus de like et sont nombre de like
    """
    max_like = 0
    pseudo_max_like = ""

#    for utilisateur in dico:
#        if dico[utilisateur] > max_like:
#            max_like = dico[utilisateur]
#            pseudo_max_like = dico[utilisateur].keys()

    for pseudo, nb_like in dico.items():
        if nb_like > max_like:
            max_like = nb_like
            pseudo_max_like = pseudo


    return pseudo_max_like, max_like

assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}) == ('Ada', 201), "Erreur exercice 1"
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}) == ('Alan', 222), "Erreur exercice 1"



# Exercice 2

class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()

assert eval_expression([2, 3, '+', 5, '*']) == 25, "Erreur exercice 2"
