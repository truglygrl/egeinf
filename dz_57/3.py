for a in range(1, 1000):
    f = 0
    for x in range(1, 500):
        if ((x & a != 0) <= ((x & 10 == 0) <= (x & 5 != 0))) == False:
            f = 1
            break
    if f == 0:
        print(a)