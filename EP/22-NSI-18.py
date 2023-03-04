def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac')) # Affiche 'cab'

print(est_palindrome('NSI')) # Affiche False

print(est_nbre_palindrome(214312)) # Affiche False
print(est_nbre_palindrome(213312)) # Affiche True
