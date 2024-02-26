for a in range(10, 10000000):
    flag = 0
    for x in range(100):
        if ((x & 17 == 0) <= ((x&33 != 0) <= (x & a != 0))) == False:
            flag = 1
            break
    if flag == 0:
        print(a)