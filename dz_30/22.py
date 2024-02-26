k = 0
for a in range(1, 10000000):
    flag = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if (((y*y < a) <= (y <= 8)) and ((x <= 5) <= (x*x <= a))) == False:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        k += 1
print(k)