def f(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True

        a, b = b, a + b
    return False
cnt = 0
for x in range(235121, 1004524):
    if f(x):
        print(x)