for a in range(1, 10000000):
    c = 0
    for x in range(1, 1000):
        if (((x % a != 0) and (x % 15 == 0)) <= ((x % 18 != 0) or (x % 15 != 0))) == False:
            c = 1
            break
    if c == 0:
        print(a)