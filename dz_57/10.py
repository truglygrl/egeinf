for a in range(1, 1000):
    f = 0
    for x in range(1, 500):
        for y in range(1, 500):
            if (((3*x + 5*y) < a) or (y > x) or (x > 15)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)
        break