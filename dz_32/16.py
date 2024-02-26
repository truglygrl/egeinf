for x in range(20560, 1000000):
    s = set()
    for i in range(6, x, 6):
        if (x % i == 0) and (x != i):
            s.add(i)

            if len(s) > 4:
                break
    if len(s) == 3:
        s = sorted(s)
        print(x, s[-1])