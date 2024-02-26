def f(x):
    s = str(x)
    t = sum(int(i) for i in s)
    return x % t == 0
c = set()
cnt = 0
for n in range(775240, 778901):
    if f(n):
        c.add(n)
        cnt += 1
print(sorted(c), cnt)