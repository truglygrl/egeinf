for a in range(1, 1000):
    f = 0
    for x in range(1, 500):
        if ((x & 39 == 0) or ((x & 41 == 0) <= (x & a != 0))) == False:
            f = 1
            break
    if f == 0:
        print(a)
        break