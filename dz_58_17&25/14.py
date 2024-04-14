def f(a):
    r = ''
    while a > 0:
        r = str(a % 11) + r
        a //= 11
    return r
print(f(52))
c = 0
for x in range(2031, 14313):
    if f(x).count('2') == 0:
        print(x)
print(c)