for a in range(1, 1000):
    c = 0
    for x in range(500):
        for y in range(500):
            if (((y * y < a) <= (y <= 14)) and ((x <=13) <= (x*x < a))) == False:
                c = 1
                break
        if c == 1:
            break
    if c == 0:
        print(a)
        break