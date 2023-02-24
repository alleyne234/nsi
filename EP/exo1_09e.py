alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
occurence = [0] * 26

ch = "je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique"

def occurence_max(ch):
    """Renvoie le caractere avec le plus d'occurence
    :chaine: str
    @return char
    """
    for car in ch:
        if car in alphabet:
            i = alphabet.index(car)
            occurence[i] = occurence[i] + 1
    val_max = 0
    k_max = 0
    for k in range(len(occurence)):
        if occurence[k] > val_max:
            val_max = occurence[k]
            k_max = k
    return alphabet[k_max]

print(occurence_max(ch))