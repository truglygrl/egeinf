for a in range(10, 1000):
    flag = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if ((69 < y + 2*x) or (a > x) or (a > y)) == False:
                flag = 1
                break
    if flag == 0:
        print(a)