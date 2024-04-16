def f(a, b, m):
    if (a + b) >= 105:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1, b, m-1), f(a*4, b, m-1), f(a, b+1, m-1), f(a, b*4, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 101) if f(4, s, 2)])
print('20)', [s for s in range(1, 101) if not f(4, s, 2) and f(4, s, 4)])