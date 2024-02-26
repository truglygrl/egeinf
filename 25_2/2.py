def f(a):
    c = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            c.add(i)
            c.add(a // i)
    return len(c)



p = list()

for x in range(1010101, 101010102):
    l = f(x)
    if l == 64:
        p.append(x)
print(p[-6:])