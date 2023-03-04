T = [5, 2, 8, 6, 4, 1]

def tri_rapide(T):
    if len(T) < 2:
        return T
    else:
        pivot = T[len(T) // 2]
        Tinf = [valeur for valeur in T if valeur < pivot]
        Tpivot = [valeur for valeur in T if valeur == pivot]
        Tsup = [valeur for valeur in T if valeur > pivot]
        return tri_rapide(Tinf) + Tpivot + tri_rapide(Tsup)
        
print(tri_rapide(T))
        