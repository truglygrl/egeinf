for a in range(10, 1000):
    flag = 0
    for x in range(1, 100):
        if ((x & a != 0) <= ((x & 10 != 0) <= (x&5 != 0))) == False:
            flag = 1
            break
    if flag == 0:
        print(a)