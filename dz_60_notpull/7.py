def f(a, b, c, m):
    if (a + b + c) >= 110:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1, b, c, m-1), f(a*2, b, c, m-1), f(a, b+1, c, m-1), f(a, b*2, c, m-1), f(a, b, c+1, m-1), f(a, b, c*2, m-1)]
    return any(h) if (m - 1) % 2 == 0 else any(h)
print(len([s for s in range(1, 95) if f(10, 5, s, 4) and not f(10, 5, s, 2)]))