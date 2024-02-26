for a in range(1, 1000):
    for x in range(1, 1000):
        c = 0
        if ((x % 18 == 0) <= ((x % a != 0) <= (x % 12 != 0))) == False:
            c = 1
            break
    if c == 0:
        print(a)