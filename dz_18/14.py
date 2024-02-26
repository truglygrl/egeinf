for a in range(1, 1000):
    c = 0
    for x in range(1, 1000):
        if ((a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))) == False:
            c = 1
            break
    if c == 0:
        print(a)