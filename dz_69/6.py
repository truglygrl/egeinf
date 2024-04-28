def f7(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s

f = open('17__1sna7.txt')
c = 0
mn = 10**10
a = [int(i) for i in f]
m63 = max(x for x in a if x % 63 == 0)
for i in range(len(a)-1):
    if (a[i] + a[i+1]) > m63:
        if ('55' in f7(a[i])) or ('55' in f7(a[i+1])):
            c += 1
            mn = min(mn, abs(a[i]) + abs(a[i+1]))

print(c, mn)