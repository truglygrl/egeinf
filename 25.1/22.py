for n in range(300000, 333001):
    c = set()
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            c.add(i)
            c.add(n//i)
    if len(c) == 3:
        print(n)
