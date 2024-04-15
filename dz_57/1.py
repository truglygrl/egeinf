for a in range(100, 1000):
    f = 0
    for x in range(1, 500):
        for y in range(1, 500):
            if (((x + 3*y) > a) or (x < 18) or y < 33) == False:
                f = 1
                break
    if f == 0:
        print(a)