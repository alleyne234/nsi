def puissance(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return puissance(a * a, n / 2)
    else:
        return a * puissance(a * a, (n - 1) / 2)

print(puissance(2, 8))
