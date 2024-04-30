def f(a, b, m):
    if (a+b) >= 77:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+2, b, m-1), f(a*2, b, m-1), f(a, b+2, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

for s in range(1, 70):
    if (f(7, s, 4)) and (not (f(7, s, 2))):
        print(s)