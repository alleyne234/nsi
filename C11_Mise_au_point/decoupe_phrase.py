def decouper(phrase):
    L = []
    debut, fin = 0, 0
    while fin < len(phrase):
        while fin < len(phrase) and phrase[fin] != " ":
            fin += 1
        mot = phrase[debut:fin]
        L.append(mot)
        debut, fin = fin + 1, fin + 1
    return L

print(decouper("Un bel été"))