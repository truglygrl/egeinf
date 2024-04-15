for a in range(1, 1000):
    f = 0
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((2*x < y) or (x > 13) or (x*y < a)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)
        break