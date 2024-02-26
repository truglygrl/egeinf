for n in range(1000, 10000):
    s = str(n)
    r = ''
    a = int(s[0]) + int(s[1])
    b = int(s[1]) + int(s[2])
    c = int(s[2]) + int(s[3])
    p = sorted([a, b, c])
    r = str(p[0]) + str(p[1])
    if int(r) == 915:
        print(n)