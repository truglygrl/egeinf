for a in range(-100, 100000000):
    flag = 0
    for x in range(1000):
        for y in range(1000):
            if (((y + 2*x) < a) or (x > 20) or (y > 30)) == False:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        print(a)

