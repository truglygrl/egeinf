def d(a):
    c = set()
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            c.add(i)
            c.add(a // i)
    return c
print(d(19226))
print(d(19223))
sm = 0
m = 0
for i in range(7123, 19234):
    for j in range(7124, 19235):
        a = d(i)
        b = d(j)
        if (len(a) == 2) and (len(b) == 2) and (not(a & b)):
            if (i + j) > sm:
                sm = i + j
                m = i
print(m, sm-m)
