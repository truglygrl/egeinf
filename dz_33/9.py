for n in range(1, 1900):
    r = bin(n)[2:]

    a = (''.join(r[1:len(r):2])).count('0')
    b = (''.join(r[0:len(r):2])).count('1')
    if abs(a*b) == 12:
        print(n)