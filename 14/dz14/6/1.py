for x in range(0, 20000):
    x1 = x
    a = 1
    b = 1
    while x > 0:
        a = a + 1
        s = x%1000
        b = b*s
        x = x // 1000
    if a == 3 and b == 63:
        print(x1)