for a in range(1000):
    c = 0
    for x in range(1, 1000):
        if (((x & 45 != 0) or (x & 28 != 0) or (x & 56 != 0)) <= (x & a != 0)) == False:
            c = 1
            break

    if c == 0:
        print(a)