for a in range(1000):
    fl = 0
    for x in range(0, 1000):
        if (((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0)) == False:
            fl = 1
    if fl == 0:
        print(a)