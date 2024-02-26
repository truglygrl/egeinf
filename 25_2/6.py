def f(a):
    c = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            c.add(i)
            c.add(a // i)
    return len(c)
mc = -1
c = set()
for i in range(591645, 592846):
    l = f(i)
    if l == 144:
        print(i)