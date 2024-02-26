for x in range(800001, 810000):
    s = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            s = i + x // i
            break
    if s % 138 == 0 and s > 0:
        print(x, s)