def f(a):
    s = set()
    for i in range(2, int(a**0.5) + 1):
        if (a % i == 0) and ((i % 2 == 0) or (i % 3 == 0)):
            s.add(i)
            if ((a // i) % 3 == 0) or ((a // i) % 2 == 0):
                s.add(a // i)
    if len(s) != 6:
        return False
    if len(s) == 6:
        return True


c = 0
for x in range(3,30002):
    if f(x):
        c += 1
print(c)