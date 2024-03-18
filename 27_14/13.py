for a in range(1,1000):
    fl = 0
    for x in range(1, 1000):
        if ((a % 7 == 0)  and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))) == False:
            fl = 1
            break
    if fl == 0:
        print(a)