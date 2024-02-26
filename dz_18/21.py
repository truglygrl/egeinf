for a in range(1000):
    c = 0
    for x in range(1, 1000):
        if ((x & a != 0) <= ((x & 14 == 0) <= (x & 75 != 0))) == False:
            c = 1
            break

    if c == 0:
        print(a)