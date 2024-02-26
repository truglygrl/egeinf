def f(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
c = set()
for x in range(523456, 578926):
    d = 0
    for i in range(2, int(x**0.5) + 1):
        if (x % i == 0) and f(i) and f(x // i) and (i != x // i):
            d = x // i - i
    if d == 4:
        print(x)
for i in range(1, 549077):
    if 549077 % i == 0:
        print(i)