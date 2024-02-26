for a in range(1, 1000):
    for x in range(100000):
        c = 0
        if (((x % a == 0) and (x % 22 != 0)) <= ((x%40 == 0) or (x % 15 == 0))) == False:
            c = 1
            break
    if c == 0:
        print(a)
        break