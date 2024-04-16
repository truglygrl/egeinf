def f(a, b, m):
    if (a + b) >= 60:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print(len([s for s in range(1, 50) if f(10, s, 4) and not f(10, s, 2)]), [s for s in range(1, 50) if f(10, s, 4) and not f(10, s, 2)])