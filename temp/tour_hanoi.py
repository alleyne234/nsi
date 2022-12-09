def tour_hanoi(nb_disq, debut, milieu, fin):
    '''Affiche les transferts entre les differents colonnes.
    : nb_disq : (int)
    : debut, milieu, fin : (str) 'A' 'B' or 'C'
    '''
    if nb_disq == 1:
        print('Se déplace de {} vers {}'.format(debut, fin))
        return
    tour_hanoi(nb_disq-1, debut, fin, milieu)
    print('Se déplace de {} vers {}'.format(debut, fin))
    tour_hanoi(nb_disq-1, milieu, debut, fin)
