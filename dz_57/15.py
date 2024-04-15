for a in range(1, 1000):
    f = 0
    for x in range(1, 1000):
        if (((x & a != 0) <= ((x & 14 == 0) <= (x & 3 != 0)))) == False:
            f = 1
            break
    if f == 0:
        print(a)