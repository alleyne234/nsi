def est_palindrome_r(mot):
    if len(mot) == 0 or len(mot) == 1:
        return True
    elif mot[0] != mot[len(mot) - 1]:
        return False
    else:
        return est_palindrome_r(mot[1:len(mot) - 1])
