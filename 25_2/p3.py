def f(n):
    for a in range(2, int(n**0.5) + 1):
        if n % a == 0:
            return False
    return True
cnt = 0
for x in range(105673, 220785):
    c = set()
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            if f(i):
                c.add(i)
            if f(x // i):
                c.add(x // i)
    t = list(c)
    fg = 0
    if len(t) >= 3:
        for i in t:
            for j in t:
                for k in t:
                    if (i*j*k == x) and (j != k) and (k != i) and (i != j):
                        fg = 1
    if fg == 1:
        cnt += 1
print(cnt)