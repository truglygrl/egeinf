def f(a):
    c = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            if i % 2 == 1:
                c.add(i)
            if (a // i) % 2 == 1:
                c.add(a // i)
    return len(c)


cnt = 0

for x in range(22333, 89000):
    ll = f(x)
    if ll == 3:
        cnt += 1
print(cnt)