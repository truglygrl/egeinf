def f(a):
    s = set()
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            s.add(i)
            s.add(a // i)
    return s

def p(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
c = 0
mx = -100000000000000
for x in range(105673, 220785):
    t = list(set(i for i in f(x) if p(i)))
    if len(t) > 2:
        for i in range(len(t) - 2):
            for j in range(i + 1, len(t) - 1):
                for k in range(j + 1, len(t)):
                    if (t[i] * t[j] * t[k]) == x:
                        c += 1
                        mx = max(mx, x)
print(c)
print(mx)

