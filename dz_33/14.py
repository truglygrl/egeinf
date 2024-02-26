for n in range(1000, 10000):
    s = str(n)
    r = ''
    a = int(s[0]) + int(s[2])
    b = int(s[1]) + int(s[3])
    if a < b:
        r = str(a) + str(b)
    else:
        r = str(b) + str(a)
    if int(r) == 815:
        print(n)