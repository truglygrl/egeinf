def f(n):
    s = ''
    while n > 0:
        s = str(n % 14) + s
        n //= 14
    return s

for x in range(1000, 15001):
    if f(x).count('5') == 0:
        print(x)