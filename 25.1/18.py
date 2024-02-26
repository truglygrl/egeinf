for n in range(81234, 81299):
    c = set()
    for i in range(2, n+1):
        if (n % i == 0) and (i % 2 == 0):
            c.add(i)

    if len(c) == 4:
        print(*(sorted(c)))