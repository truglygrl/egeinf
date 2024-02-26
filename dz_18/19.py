for a in range(1000):
    c = 0
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 2*x != 77) or (y > a) or (x > a)) == False:
                c = 1
                break
        if c == 1:
            break
    if c == 0:
        print(a)