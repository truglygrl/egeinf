def f(a, b, m1, m2):
    if a > b:
        return 0
    if a == b:
        return 1
    if m1 == 3:
        return f(a + 1, b, 1) + f(a + 2, b, 2)
    else:
        return f(a + 1, b, 1) + f(a + 2, b, 2) + f(a * 2, b, 3)



print(f(1, 15, 0))