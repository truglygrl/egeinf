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
for x in range(125697, 190235):
    t = 0
    for i in range(2, int(x **0.5) + 1):
        if (x % i == 0) and (p(i)) and (p(x // i)) and (i != x // i):
            t = 1
            break
    c += 1
print(c)
