for a in range(10, 1000):
    flag = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if ((x + 3*y > a) or (x < 18) or (y < 33)) == False:
                flag = 1
                break
    if flag == 0:
        print(a)