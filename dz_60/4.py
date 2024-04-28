def f(a, m1, m2):
    if a >= 68:
        return 0
    if m1 == 0:
        t = [f(a + 3, 1, 0), f(a + 6, 2, 0), f(a * 3, 3, 0)]
    if m2 == 1:
        t = [f(a + 6, ), f(a * 3, 3)]
    if m2 == 2:
        t = [f(a + 3, 1), f(a * 3, 3)]
    if m2 == 3:
        t = [f(a + 3, 1), f(a + 6, 2)]
    n = [x for x in t if x <= 0]
    if n:
        return -max(n) + 1
    return -max(t)

for s in range(1, 68):
    if f(s, 0) == -3:
        print(s)