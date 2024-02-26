for n in range(1, 100):
    x = n
    n = bin(n)[2:]
    summ = n.count('1')
    n = n + str(summ % 2)
    summ = n.count('1')
    n = n + str(summ % 2)
    print(x, int(n, 2))