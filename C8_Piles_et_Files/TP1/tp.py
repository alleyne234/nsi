from pile import *


def is_good_par(a):
    pile = creer_pile()
    for i in range(len(a)):
        if a[i] == '(' or a[i] == '[' or a[i] == '{':
            pile.empiler(a[i])
        elif a[i] == ')' and pile.contenu[len(pile.contenu)-1] == '(':
            pile.depiler()
        elif a[i] == ']' and pile.contenu[len(pile.contenu)-1]  == '[':
            pile.depiler()
        elif a[i] == '}' and pile.contenu[len(pile.contenu)-1]  == '{':
            pile.depiler()
    return pile.est_vide()
    
#print(is_good_par("([3])"))

def NPI(expression):
    liste_elts = expression.split(" ")
    pile_int = creer_pile()
    for elt in liste_elts:
        if elt == '+' or elt == '*':
            x = int(pile_int.depiler())
            y = int(pile_int.depiler())
            if elt == '+':
                pile_int.empiler(x + y)
            else:
                pile_int.empiler(x * y)
        else:
            pile_int.empiler(elt)
    return pile_int.depiler()

print(NPI("1 2 3 * + 4 *"))
