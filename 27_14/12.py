for a in range(1, 1000):
    fl = 0
    for x in range(1, 800):
        for y in range(1, 800):
            if ((x >= 7) or (2*x < y) or (x*y <a)) == False:
                fl = 1
                break
        if fl == 1:
            break
    if fl == 0:
        print(a)