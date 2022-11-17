def pascal(n):
    C= [[1]]
    for k in range(1, n):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k - 1][i - 1] + C[k - 1][i])
        Ck.append(1)
        C.append(Ck)
    return C

assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]], "Error"
