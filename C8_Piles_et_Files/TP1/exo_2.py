from pile import *

def is_good_par(chaine):
    pile = creer_pile()
    for car in chaine:
        if car == '(' or car == '[' or car == '{':
            pile.empiler(car)
        elif car == ')' and pile.contenu[len(pile.contenu)-1] == '(':
            pile.depiler()
        elif car == ']' and pile.contenu[len(pile.contenu)-1] == '[':
            pile.depiler()
        elif car == '}' and pile.contenu[len(pile.contenu)-1] == '{':
            pile.depiler()
    return pile.est_vide()
            
            
            
            
chaine1= "(2 * [3 + 2])"


is_good_par(chaine1)
            