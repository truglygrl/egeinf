for a in range(1000):
    c = 0
    for x in range(1000):
        for y in range(1000):
            if ((x > a) or (y > a) or (2*x + y != 48)) == False:
                c = 1
                break
        if c == 1:
            break
    if c == 0:
        print(a)