for a in range(140, 1000):
    c = 0
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <14))) == False:
                c = 1
                break
        if c == 1:
            break
    if c == 0:
        print(a)