for x in range(14678, 15157):
    s = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
            if len(s) > 2:
                break
    if len(s) >= 1:
        t = max(s) - min(s)
        if t > 7570:
            print(x, t)
