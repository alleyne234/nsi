def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu

print(rendu_monnaie_centimes(700, 700)) # Affiche []
print(rendu_monnaie_centimes(112, 500)) # Affiche [200, 100, 50, 20, 10, 5, 2, 1]
