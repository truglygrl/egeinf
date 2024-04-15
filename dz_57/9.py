for a in range(1, 1000):
    f = 0
    for x in range(1, 1000):
        if (((x % 45 == 0) and (x % 70 == 0)) <= (x % a == 0)) == False:
            f = 1
            break
    if f == 0:
        print(a)