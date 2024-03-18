for a in range(1, 1000):
    fl = 0
    for k in range(1, 500):
        for n in range(1, 500):
            if ((5*k + 6*n > 57) or ((k <= a) and (n < a))) == False:
                fl = 1
                break
        if fl == 1:
            break
    if fl == 0:
        print(a)