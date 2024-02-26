def f(a):
    c = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            c.add(i)
            c.add(a // i)
    return sorted(c)
fl = 0
for x in range(800000, 100**10000):
    if fl > 5:
        break
    a = f(x)
    if (a[1] + a[-2]) % 138 == 0:
        fl += 1
        print(x)