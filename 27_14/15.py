for a in range(1, 1000):
    fl = 0
    for x in range(1, 1000):
        if ((x & 10 != 0) or (x & 39 == 0) or (x & a == 0)) == False:
            fl = 1
            break
    if fl == 0:
        print(a)