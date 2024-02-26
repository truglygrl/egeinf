k = 0
for a in range(1, 10000000):
    flag = 0
    for x in range(1, 100):
        if ((70 % a == 0) and ((x % 28 == 0) <= ((x % a != 0) <= (x % 21 != 0)))) == False:
            flag = 1
            break

    if flag == 0:
        print(a)