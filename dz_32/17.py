for x in range(10000, 1000000):
    s = set()
    for i in range(2, int(x **0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
            break
    if len(s) == 2:
        t = min(s) + max(s)
        if t % 256 == 6:
            print(x, t)