for i in range(1, 200):
    n = bin(i)[2:]
   # print(n)
    s = sum([int(i) for i in n])
    if s % 2 == 0:
        n = n + '00'
    else:
        n = n + '11'
   # print(n)
    if int(n, 2) > 57:
        print(int(n, 2))