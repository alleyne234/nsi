def traduction_zorglangue(phrase):
    """La fonction traduction_zorglangue(phrase) reçoit une phrase et
    renvoie cette phrase avec tout les mots inversé majuscule compris.
    @arguments:
        phrase: String
    @return:
        String
    @exemple
    >>> traduction_zorglangue('Vive Zorglub')
    'Eviv Bulgroz'
    """
    liste_mot = decoupe_phrase(phrase)
    for mot in liste_mot:
        if est_un_nom_propre(mot):
            liste_mot[liste_mot.index(mot)] = inverse_mot(majuscule_a_la_fin(mot))
        else:
            liste_mot[liste_mot.index(mot)] = inverse_mot(mot)
    return reconstruire_phrase(liste_mot)
    
def decoupe_phrase(phrase):
    """La fonction decoupe_phrase(phrase) reçoit une phrase et renvoie
    une liste contenant les mots de cette phrase.
    @arguments:
        phrase: String
    @return:
        list de String
    @exemple
    >>> decoupe_phrase('la vie est belle')
    ['la', 'vie', 'est', 'belle']
    """
    return phrase.split(" ")
    
def est_un_nom_propre(mot):
    """La fonction est_un_nom_propre(mot) reçoit un mot et renvoie
    True si celui-ci commence par une majuscule, sinon False.
    @arguments:
        mot: String
    @return:
        Bool
    @exemple
    >>> est_un_nom_propre('Zorglub')
    True
    """
    return ord(mot[0]) >= 65 and ord(mot[0]) <= 90
    
def inverse_mot(mot):
    """La fonction inverse_mot(mot) reçoit une chaine de caractères en
    arguments et inverse l'odre de ses lettres.
    @argumetns:
        mot: String
    @return:
        String
    @exemple
    >>> inverse_mot('abcdef')
    'fedcba'
    """
    return mot[::-1] # Solution trouvée sur ce site : https://www.w3schools.com/python/python_howto_reverse_string.asp
    
def majuscule_a_la_fin(mot):
    """La fonction majuscule_a_la_fin(mot) met en minuscule la lettre
    majuscule d'un nom propre et met en majuscule la dernière
    lettre de ce mot.
    @arguments:
        mot: String
    @return:
        String
    @exemple
    >>> majuscule_a_la_fin('Zorglub')
    'zorgluB'
    """
    return mot[0:-1].lower() + mot[-1:].upper() # Renvoie le mot sauf la dernière lettre en minuscule plus la dernière lettre en majuscule.
    
def reconstruire_phrase(liste_mot):
    """La fonction reconstruire_phrase(liste_mot) reçoit une liste de
    mots et avec cet mots construit une phrase où les mots sont
    séparés par un espace.
    @arguments:
        liste_mot: List
    @return:
        String
    @exemple
    >>> reconstruire_phrase(['Je', 'suis', 'en', 'pièces'])
    'Je suis en pièces'
    """
    phrase = ''
    for i in liste_mot:
        if len(phrase) <= 0: # Condition pour éviter d'avoir un espace avant le premier mot.
            phrase = i
        else:
            phrase = phrase + ' ' + i
    return phrase

print(traduction_zorglangue('Vive Zorglub'))
