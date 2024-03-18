for a in range(1000):
    fl = 0
    for x in range(1000):
        for y in range(1000):
            if ((x - y >= 5) or (x <= a) or (y >= a) or (x+y <= 64)) == False:
                fl = 1
                break
        if fl == 1:
            break
    if fl == 0:
        print(a)