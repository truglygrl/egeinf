cnt = 0
for n in range(500000, 50000000):

    c = set()
    for i in range(9, n):
        if (n % i ==0 ) and i % 10 == 8:
            print(n, i)
            cnt += 1
            break
    if cnt == 5:
        break
