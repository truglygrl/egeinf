def f(a):
    c = set()
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            c.add(i)
            c.add(a // i)
    return sorted(c)
fl = 0

for x in range(650001, 100**1000):
    if fl == 6:
        break
    a = f(x)
    if a:
        if len(f(a[-1])) != 0:
            print(x, a[-1])
            fl += 1