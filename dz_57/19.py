for a in range(1, 1000):
    f = 0
    for x in range(1, 1000):
        if ((70 % a == 0) and ((x % a != 0) <= ((x % 18 == 0) <= (x % 42 != 0)))) == False:
            f = 1
            break
    if f == 0:
        print(a)
