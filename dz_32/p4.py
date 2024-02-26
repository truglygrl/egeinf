
def f5(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s


f = open('17-324__2n0lz.txt')
a = [int(i) for i in f]

s = sum(i for i in a if i % 31 == 0) / len([i for i in a if i % 31 == 0])
mn = 100000000000000
c = 0
print(s)

for i in range(len(a)-2):
    t = a[i] + a[i+1] + a[i+2]
    if (f5(t) == f5(t)[::-1]) and (t/3 > s):
        c += 1
        mn = min(mn, t)
print(c, mn)