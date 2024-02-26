def f(a):
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a //= 3
    return s
for i in range(1, 1000):
    r = f(i)
    if i % 3 == 0:
        r = '1' + r + '02'
    else:
        os = (i % 3)*4
        r = r + str(f(os))

    if (int(r, 3)) < 199:
        print(i)