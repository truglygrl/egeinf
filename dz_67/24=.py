def f(a, b, c):
    if c == 10:
        return a == b
    if c < 10:
        return f(a + 4, b, c + 1) + f(a + 7, b, c + 1) + f(a // 2, b, c + 1)

print(f(1, 1, 0))