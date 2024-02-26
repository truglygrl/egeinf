def f(a):
    s = ''
    while a>0:
        s = str(a % 5) + s
        a //= 5
    return int(s)
n = 4*25**4 - 5**4 + 14
p = sum([int(i) for i in str(f(n))])
print(p, f(n))