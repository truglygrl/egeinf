for a in range(1, 1000):
    fl = 0
    for x in range(1, 100000):
        if ((((x % a == 0) and (x % 36 == 0)) <= (x % 324 == 0)) and (a > 100)) == False:
            fl = 1
            break
    if fl == 0:
        print(a)
        break