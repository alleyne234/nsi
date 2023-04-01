def dec_to_bin(a):
    bin_a = ""
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
