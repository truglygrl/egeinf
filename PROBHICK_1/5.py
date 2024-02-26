def f(n):
    d = bin(n)[2:]
    d += bin(n % 4)[2:]
    r = int(d, 2)
    return r

mk = 0
for i in range(10000):
    s = set()
    for a in range(i, i+49):
        s.add(f(a))
    mk = max(mk, len(s))
    print(len(s))
print(mk)

