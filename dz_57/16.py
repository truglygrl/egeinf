for a in range(1, 1000):
    f = 0
    for x in range(1, 1000):
        if (((x % 34 == 0) and (x % 51 != 0)) <= ((x % a != 0) or (x % 51 == 0))) == False:
            f = 1
            break
    if f == 0:
        print(a)
        break