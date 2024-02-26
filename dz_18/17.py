for a in range(-10000, 1000):
    c = 0
    for x in range(1000):
        for y in range(1000):
            if ((x*y > a) and (x > y) and (x < 8)) == True:
                c = 1
                break
        if c == 1:
            break
    if c == 0:
        print(a)