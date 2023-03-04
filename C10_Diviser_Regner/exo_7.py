def min_et_max(T):
    if len(T) == 1:
        return (T[0], T[0])
    elif len(T) == 2:
        return (min(T[0], T[1]), max(T[0], T[1]))
    else:
        milieu = len(T) // 2
        min_gauche, max_gauche = min_et_max(T[:milieu])
        min_droite, max_droite = min_et_max(T[milieu:])
        return (min(min_gauche, min_droite), max(max_gauche, max_droite))
