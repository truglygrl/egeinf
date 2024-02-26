for a in range(1, 100000):
    c = 0
    for x in range(1, 1000):
        if ((x % 24 == 0) <= ((x % 72 == 0) <= (x % a == 0))) == False:
            c = 1
            break
    if c == 0:
        print(a)