for a in range(1, 1000):
    fl = 0
    for x in range(1, 1000):
        if ((x & a != 0) <= (((x & 17 == 0) or (x & 5 == 0)) <= (x & 3 != 0))) == False:
            fl = 1
            break
    if fl == 0:
        print(a)