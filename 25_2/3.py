def f(a):
    c = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            c.add(i)
            c.add(a // i)
    return len(c)


cnt = 0
for x in range(22222, 88889):
    p = f(x)
    if p == 5:
        cnt += 1
        print(x)

print(cnt)