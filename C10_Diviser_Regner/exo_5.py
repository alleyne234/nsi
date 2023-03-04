def produit(a, b):
    if b == 1:
        return a
    else:
        if b % 2 == 0:
            return produit(a * 2, b / 2)
        else:
            return a + produit(a * 2 , (b - 1) / 2)
    
print(produit(2, 8))
