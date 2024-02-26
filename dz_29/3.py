k = set()

def f(a, c, m):
    if c == 10:
        k.add(a)
    elif c == 0:
        f(a+1, c + 1, 1)
        f(a+2, c + 1, 2)
        f(a+3, c + 1, 3)
        f(a*2, c + 1, 4)
        f(a*3, c + 1, 5)
        f(a*4, c + 1, 6)
    else:
        if m == 1:
            f(a + 2, c + 1, 2)
        if m == 2:
            f(a + 1, c + 1, 1)
            f(a + 3, c + 1, 3)
        if m == 3:
            f(a + 2, c + 1, 2)
            f(a * 2, c + 1, 4)
        if m == 4:
            f(a + 3, c + 1, 3)
            f(a * 3, c + 1, 5)
        if m == 5:
            f(a * 2, c + 1, 4)
            f(a * 4, c + 1, 6)
        if m == 6:
            f(a * 3, c + 1, 5)
f(1, 0, 0)
print(len(k))