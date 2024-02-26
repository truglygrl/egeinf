for a in range(10, 1000):
    flag = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if ((3*x + 9*y >= a) or (x <= 20) or (y < 10)) == False:
                flag = 1
                break
    if flag == 0:
        print(a)